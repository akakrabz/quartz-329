---
title: "Telegrapher's equations"
description: "−∂V/∂z = 𝓛 ∂I/∂t and −∂I/∂z = 𝓒 ∂V/∂t govern voltage and current on a lossless two-conductor line. They are Faraday's and Ampère's laws rewritten with V = E_x d and I = H_y W."
tags: [concept, transmission-lines]
aliases: ["transmission-line equations", "telegrapher equations", "distributed-circuit model"]
---

> [!key] Definition (lossless line)
> $$
> -\frac{\partial V}{\partial z} = \mathcal{L}\frac{\partial I}{\partial t},\qquad -\frac{\partial I}{\partial z} = \mathcal{C}\frac{\partial V}{\partial t}.
> $$
> $V(z,t)$ is the voltage of conductor 2 relative to conductor 1. $I(z,t)$ is the current along $+z$ on conductor 2, returning on conductor 1. $\mathcal{L}$ [H/m] and $\mathcal{C}$ [F/m] are per unit length. A lossy line adds $\mathcal{R}I$ to the first right side and $\mathcal{G}V$ to the second.

**Physics.** On a parallel-plate line, $V = E_xd$ and $I = H_yW$ turn Faraday's law into the first equation and Ampère's law into the second, with $\mathcal{L} = \mu d/W$ and $\mathcal{C} = \epsilon W/d$.
- The first is Faraday's law for a thin loop spanning the gap.
- The second is charge conservation on a conductor that holds $\mathcal{C}V$ per metre.
- Mnemonic: an inductor's $v = L\,di/dt$ and a capacitor's $i = C\,dv/dt$, with $-\partial/\partial z$ on the left.

**Consequences.**
- Wave equation $\partial^2V/\partial z^2 = \mathcal{L}\mathcal{C}\,\partial^2V/\partial t^2$, speed $v = 1/\sqrt{\mathcal{L}\mathcal{C}} = 1/\sqrt{\mu\epsilon}$.
- d'Alembert solutions $V = f(t-z/v) + g(t+z/v)$ and $I = (f-g)/Z_0$, with $Z_0 = \sqrt{\mathcal{L}/\mathcal{C}}$ ([[concepts/characteristic-impedance|Characteristic impedance]]).
- Distributed-circuit model: each $\Delta z\ll\lambda$ is a series inductor $\Delta z\,\mathcal{L}$ and a shunt capacitor $\Delta z\,\mathcal{C}$.
- Power $p = VI$.
- Phasor form (sinusoidal steady state): $-d\tilde V/dz = j\omega\mathcal{L}\tilde I$, $-d\tilde I/dz = j\omega\mathcal{C}\tilde V$.

**Examples.**
- 50 Ω at $v = 2\times10^8$ m/s: $\mathcal{L} = Z_0/v = 250$ nH/m, $\mathcal{C} = 1/(Z_0v) = 100$ pF/m.
- A 3 V battery connected to that line at $t = 0$: $V = 3\,u(t-z/v)$ V and $I = 60\,u(t-z/v)$ mA, until a reflection returns.
- [[problems/a-backward-pulse-on-a-parallel-plate-line|Worked problem — A backward pulse on a parallel-plate line]]: a pulse toward $-z$, with $V = -Z_0I$.

> [!trap]
> - Mind the minus signs: where $I$ grows in time, $V$ falls along $+z$.
> - Series inductors and shunt capacitors, not the reverse.
> - $\mathcal{L}$ and $\mathcal{C}$ are per metre; the line's length enters only through the ends.

**Where it appears.** [[4-transmission-lines/27-guided-tem-waves-on-transmission-lines|Lecture 27]] (derivation from the fields, the ladder model); [[4-transmission-lines/28-distributed-circuits-and-bounce-diagrams|Lectures 28]]–30 (bounce diagrams with sources and loads); Lecture 31 onward in phasor form.

**Related.** [[0-toolkit/08-waves-in-media-figures|Waves in media — figures]]

**Practice.** [[practice/topics#transmission-lines-telegraphers-equations-and-characteristic-impedance|Transmission lines: telegrapher's equations and characteristic impedance]] (14 problems) — for example [[practice/27-transmission-line-basics#271-strip-line-parameters|27.1 Strip-line parameters]] (easy), [[practice/27-transmission-line-basics#276-reading-a-line-from-v-and-i|27.6 Reading a line from V and I]] (medium), [[practice/27-transmission-line-basics#279-a-pulse-on-a-coax|27.9 A pulse on a coax]] (hard).

Related: [[concepts/inductance|Inductance]] · [[concepts/capacitance|Capacitance]] · [[concepts/wave-equation|Wave equation]] · [[concepts/faradays-law|Faraday's law]] · [[concepts/continuity-equation|Continuity equation (charge conservation)]].
