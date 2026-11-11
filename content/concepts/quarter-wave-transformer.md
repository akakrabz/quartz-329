---
title: "Quarter- and half-wave transformers"
description: "A quarter-wave line inverts its load, Z_in Z_L = Z₀², and forces the load current −jV_in/Z₀; a half-wave line repeats its load with V and I reversed in sign."
tags: [concept, transmission-lines]
aliases: ["quarter-wave transformer", "half-wave transformer", "current forcing"]
---

> [!key] Two rules
> $$
> \begin{gathered}
> \ell = \frac\lambda4:\quad Z_{\text{in}} = \frac{Z_0^2}{Z_L},\qquad \tilde I_L = -j\frac{\tilde V_{\text{in}}}{Z_0},\qquad \tilde V_L = -jZ_0\tilde I_{\text{in}},\\[6pt]
> \ell = \frac\lambda2:\quad Z_{\text{in}} = Z_L,\qquad \tilde V_{\text{in}} = -\tilde V_L,\qquad \tilde I_{\text{in}} = -\tilde I_L .
> \end{gathered}
> $$

**Physics.** Both follow from $\tilde V(d) = V^+e^{j\beta d}+V^-e^{-j\beta d}$ and $\tilde I(d) = (V^+e^{j\beta d}-V^-e^{-j\beta d})/Z_0$ with $e^{\pm j\beta\ell} = \pm j$ or $-1$.
- **Quarter wave:** the factor $j$ multiplies $V^+$ and $-j$ multiplies $V^-$, which swaps the roles of sum and difference: the input voltage is set by the load **current**, the input current by the load **voltage**. Hence the inversion about $Z_0$.
- **Current forcing:** $\tilde I_L$ depends on $\tilde V_{\text{in}}$ and $Z_0$, not on $Z_L$. Several loads fed from one point through quarter-wave lines carry equal currents.
- **Half wave:** both waves pick up $-1$, so the line is invisible apart from the sign.
- A lossless section delivers to the load all the power it takes in.
- Chain the rules for longer lines: $3\lambda/4$ inverts, $\lambda$ repeats.

**Examples.**
- Notes, Lecture 33: $Z_L = 50+j50\ \Omega$ behind a 50 Ω quarter-wave line looks like $25-j25\ \Omega$. With 100 V at the input, $\tilde I_L = -j2$ A and the load takes 100 W.
- Notes: 100 Ω behind $0.75\lambda$ of 50 Ω line looks like 25 Ω.
- Matching: a section with $Z_q = \sqrt{Z_0R_L}$ makes a resistive load $R_L$ look like $Z_0$. For 200 Ω on a 50 Ω system, $Z_q = 100\ \Omega$.
- A quarter-wave shorted stub: $Z_0^2/0 = \infty$, an open circuit ([[concepts/stub-input-impedance|Input impedance of a stub]]).

> [!trap]
> - $Z_0^2/Z_L$ only at odd multiples of $\lambda/4$, at one frequency.
> - Current forcing needs the input **voltage**; get it from a divider with $Z_{\text{in}}$ first.
> - Keep the $-j$: it is a quarter period of delay.

> [!exam] On exams
> Past papers only: Lectures 31–33 are **not on FA26 Midterm 3** (Lectures 1–30). SP18 Exam 3 #4(b): a resistive load behind a quarter-wave line, in series with a resistor and a source: $Z_{\text{in}}$, then $\tilde V_{\text{in}}$ by a divider. Worked twin: [[exams/e3-steady-state-lines#s2-a-quarter-wave-section-between-source-and-load|S2]].

**Where it appears.** [[4-transmission-lines/33-half-wave-and-quarter-wave-transformers|Lecture 33]] (derivation and four examples). The general length is Lecture 34.

**Practice.** [[practice/topics#half--and-quarter-wave-transformers|Half- and quarter-wave transformers]] (8 problems) — for example [[practice/33-half-and-quarter-wave-transformers#331-five-inputs|33.1 Five inputs]] (easy), [[practice/33-half-and-quarter-wave-transformers#335-five-quarter-waves-and-a-complex-load|33.5 Five quarter waves and a complex load]] (medium), [[practice/33-half-and-quarter-wave-transformers#337-one-line-at-three-frequencies|33.7 One line at three frequencies]] (hard).

Related: [[concepts/stub-input-impedance|Input impedance of a stub]] · [[concepts/line-resonances|Resonances of a line segment]] · [[concepts/characteristic-impedance|Characteristic impedance]] · [[concepts/reflection-and-transmission|Reflection and transmission]].
