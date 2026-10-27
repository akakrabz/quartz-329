---
title: "Characteristic impedance"
description: "Z₀ = √(𝓛/𝓒) = η/GF is the voltage-to-current ratio of one wave on a transmission line, +Z₀ toward +z and −Z₀ toward −z. The filling and the cross-section set it; the length does not."
tags: [concept, transmission-lines]
aliases: ["Z0", "geometrical factor", "GF"]
---

> [!key] Definition
> $$
> \begin{gathered}
> Z_0 = \sqrt{\frac{\mathcal{L}}{\mathcal{C}}} = \frac{1}{\mathcal{C}v} = \mathcal{L}v = \frac{\eta}{\text{GF}}\ [\Omega],\\[4pt]
> \mathcal{C} = \epsilon\,\text{GF},\qquad \mathcal{L} = \frac{\mu}{\text{GF}}.
> \end{gathered}
> $$
> One wave on a lossless line: $V/I = +Z_0$ toward $+z$, $-Z_0$ toward $-z$.

**Physics.** $Z_0$ is the line's version of the intrinsic impedance $\eta$.
- On parallel plates, $V = E_xd$ and $I = H_yW$ give $V/I = (E_x/H_y)(d/W) = \eta\,d/W$.
- In general $V = f+g$ goes with $I = (f-g)/Z_0$ ([[concepts/telegraphers-equations|Telegrapher's equations]]), just as $H_y = (f-g)/\eta$.
- The cross-section and the filling fix $Z_0$. The length and whatever hangs on the ends do not.
- It is not a resistance. A lossless line dissipates nothing; a forward wave carries power $f^2/Z_0$ along it.

**Geometrical factors** (notes):

| line | GF | $Z_0$ |
|---|---|---|
| parallel plates, width $W$, gap $d$ | $W/d$ | $\eta\,d/W$ |
| coax, radii $a<b$ | $2\pi/\ln(b/a)$ | $(\eta/2\pi)\ln(b/a)$ |
| twin-lead, radius $a$, spacing $D$ | $\pi/\cosh^{-1}(D/2a)$ | $(\eta/\pi)\cosh^{-1}(D/2a)$ |

**Examples.**
- Polyethylene coax ($\eta = 251\ \Omega$): $b/a = 3.5$ gives 50 Ω, $b/a = 6.5$ gives 75 Ω.
- Twin-lead in air with $D/2a = 6.14$: 300 Ω.
- Air plates with $d/W = 0.2$: 75.3 Ω.
- [[problems/a-backward-pulse-on-a-parallel-plate-line|Worked problem — A backward pulse on a parallel-plate line]]: $\epsilon_r = 2.25$ and $d/W = 0.05$ give $4\pi = 12.6\ \Omega$.

> [!trap]
> - $V/I = Z_0$ holds for a single forward wave only. For $f+g$ the ratio varies with $z$ and $t$.
> - $Z_0 = \sqrt{\mathcal{L}/\mathcal{C}}$; $\sqrt{\mathcal{L}\mathcal{C}}$ is $1/v$.
> - A wider gap or a thinner inner conductor raises $Z_0$; a larger $\epsilon_r$ lowers it.

**Where it appears.** [[4-transmission-lines/27-guided-tem-waves-on-transmission-lines|Lecture 27]] (definition, GF table); [[4-transmission-lines/28-distributed-circuits-and-bounce-diagrams|Lecture 28]] onward. A load $R$ reflects with $(R-Z_0)/(R+Z_0)$, the wave $\Gamma$ of [[concepts/reflection-and-transmission|Reflection and transmission coefficients]] with $Z_0$ for $\eta_1$ and $R$ for $\eta_2$.

**Practice.** [[practice/topics#transmission-lines-telegraphers-equations-and-characteristic-impedance|Transmission lines: telegrapher's equations and characteristic impedance]] (14 problems) — for example [[practice/27-transmission-line-basics#271-strip-line-parameters|27.1 Strip-line parameters]] (easy), [[practice/27-transmission-line-basics#276-reading-a-line-from-v-and-i|27.6 Reading a line from V and I]] (medium), [[practice/27-transmission-line-basics#279-a-pulse-on-a-coax|27.9 A pulse on a coax]] (hard).

Related: [[concepts/intrinsic-impedance|Intrinsic impedance]] · [[concepts/telegraphers-equations|Telegrapher's equations]] · [[concepts/capacitance|Capacitance]] · [[concepts/inductance|Inductance]].
