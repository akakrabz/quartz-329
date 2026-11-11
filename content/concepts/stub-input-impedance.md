---
title: "Input impedance of a stub"
description: "A shorted line of length ℓ looks like jZ₀ tan βℓ at its input, an open one like −jZ₀ cot βℓ: purely reactive, periodic every half wavelength, zero at series resonance and infinite at parallel resonance."
tags: [concept, transmission-lines]
aliases: ["stub", "shorted stub", "open stub", "series resonance", "parallel resonance"]
---

> [!key] Definition
> With $d$ measured from the load, $\tilde V(d) = V^+e^{j\beta d}+V^-e^{-j\beta d}$ and $\tilde I(d) = (V^+e^{j\beta d}-V^-e^{-j\beta d})/Z_0$. At the input $d = \ell$:
> $$
> \begin{gathered}
> \text{shorted stub:}\quad Z(\ell) = jZ_0\tan\beta\ell,\\[4pt]
> \text{open stub:}\quad Z(\ell) = -jZ_0\cot\beta\ell,\qquad \beta\ell = \frac{2\pi\ell}{\lambda}.
> \end{gathered}
> $$

**Physics.** A stub is a line segment used as a two-terminal element at one frequency.
- The far end fixes the standing wave: a short gives $\tilde V\propto\sin\beta d$, $\tilde I\propto\cos\beta d$; an open gives the reverse. $Z(\ell)$ is their ratio at the input.
- It is purely reactive: a lossless stub stores energy and absorbs none.
- **Series resonance:** $Z(\ell) = 0$, the stub is a short circuit. **Parallel resonance:** $Y(\ell) = 0$, it is an open circuit and draws no current. These are the resonant frequencies of [[concepts/line-resonances|the line segment]] with its input end shorted or open.
- Short stubs are lumped elements: shorted, $Z\approx j\omega\mathcal{L}\ell$; open, $Z\approx1/j\omega\mathcal{C}\ell$.

| length | shorted | open |
|---|---|---|
| $0<\ell<\lambda/4$ | inductive | capacitive |
| $\lambda/4$ | open circuit | short circuit |
| $\lambda/4<\ell<\lambda/2$ | capacitive | inductive |
| $\lambda/2$ | short circuit | open circuit |

The pattern repeats every $\lambda/2$.

**Examples.**
- Notes, Lecture 32: a 3 m shorted air stub in series with 50 Ω passes everything at 0, 50, 100 MHz (series resonances) and nothing at 25, 75, 125 MHz (parallel resonances).
- A $\lambda/8$ shorted stub on a 50 Ω line: $j50\tan45^\circ = j50\ \Omega$. The same stub open-ended: $-j50\ \Omega$.
- At twice the frequency a quarter-wave stub is a half-wave stub: an open circuit turns into a short.

> [!trap]
> - $d$ runs from the load toward the generator; $e^{+j\beta d}$ is the wave going toward the load.
> - The reflected wave's current has a minus sign. At a short the two current terms add.
> - A stub at parallel resonance draws no current but carries a large one inside.

> [!exam] On exams
> Past papers only: Lectures 31–33 are **not on FA26 Midterm 3** (Lectures 1–30). A stub in series with a resistor and a source, the resistor current zero: $Z(\ell) = \infty$; find $\ell$ in wavelengths, or every possible $\lambda$ (SP17 Exam 3 #6, SP18 Exam 3 #4a). $Z_{\text{in}}$ at twice or half a resonance frequency (SP18 #1(ix), (x)). Worked twins: [[exams/e3-steady-state-lines#s1-an-open-stub-that-blocks-the-source|S1]], [[exams/e3-steady-state-lines#s4-an-open-stub-at-four-frequencies|S4]].

**Where it appears.** [[4-transmission-lines/32-input-impedance-and-microwave-resonators|Lecture 32]] (derivation, the reactance curve, four examples); [[4-transmission-lines/33-half-wave-and-quarter-wave-transformers|Lecture 33]] generalizes to any load.

**Practice.** [[practice/topics#stubs-and-input-impedance|Stubs and input impedance]] (9 problems) — for example [[practice/32-stubs-and-input-impedance#321-five-stubs|32.1 Five stubs]] (easy), [[practice/32-stubs-and-input-impedance#325-a-stub-across-the-load|32.5 A stub across the load]] (medium), [[practice/32-stubs-and-input-impedance#327-a-shorted-line-that-stops-the-current|32.7 A shorted line that stops the current]] (hard).

Related: [[concepts/line-resonances|Resonances of a line segment]] · [[concepts/quarter-wave-transformer|Quarter- and half-wave transformers]] · [[concepts/characteristic-impedance|Characteristic impedance]] · [[concepts/standing-waves|Standing waves]].
