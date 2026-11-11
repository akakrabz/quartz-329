---
title: "Resonances of a line segment"
description: "A lossless line with open or shorted ends rings at harmonically related frequencies: nv/2ℓ when the ends are alike, (2n+1)v/4ℓ when one is open and one shorted. Each resonance is a standing wave."
tags: [concept, transmission-lines]
aliases: ["line resonances", "resonant modes of a line", "standing-wave modes"]
---

> [!key] Rule
> $$
> \begin{gathered}
> \text{like ends:}\quad \ell = n\frac\lambda2,\qquad f_n = \frac{nv}{2\ell}\quad(n = 1, 2, \ldots),\\[4pt]
> \text{unlike ends:}\quad \ell = (2n+1)\frac\lambda4,\qquad f_n = (2n+1)\frac{v}{4\ell}\quad(n = 0, 1, \ldots).
> \end{gathered}
> $$
> An open end forces $I = 0$, a short forces $V = 0$.

**Physics.** Cut a lossless line off from every source and it can still carry waves, reflected for ever by its ends ($\Gamma = +1$ at an open, $-1$ at a short).
- Like ends: the wave returns unchanged after one round trip, so everything is periodic with $T = 2\ell/v$. The harmonics of $1/T$ are the resonances.
- Unlike ends: one round trip flips the sign. The period is $4\ell/v$ and only odd harmonics survive.
- Each resonance is a standing wave: from an open end $V\propto\cos\beta z$ and $I\propto\sin\beta z$; from a short, the reverse. Voltage nulls sit on current maxima.
- In one mode $\lvert V\rvert_{\max} = Z_0\lvert I\rvert_{\max}$, and $V$, $I$ are a quarter period apart in time: energy sloshes between $\mathcal{C}$ and $\mathcal{L}$ with no average power flow.

> [!derivation]- From f and g (open–open)
> $I = [f(t-z/v)-g(t+z/v)]/Z_0$. $I(0,t) = 0$ gives $g = f$. $I(\ell,t) = 0$ gives $f(t-\ell/v) = f(t+\ell/v)$: period $2\ell/v$. With $f = F\cos(\omega t+\theta)$, $I = (2F/Z_0)\sin(\omega t+\theta)\sin\beta z$ and $V = 2F\cos(\omega t+\theta)\cos\beta z$, which vanish as required when $\beta\ell = n\pi$.

**Examples.**
- Notes, Lecture 31: 600 m, open at one end, shorted at the other, $v = c$: $f_n = (2n+1)/8$ MHz, that is 0.125, 0.375, 0.625 MHz. A 1 A current mode goes with a $Z_0 = 50$ V voltage mode.
- Both ends open instead: 0.25, 0.5, 0.75 MHz.

> [!trap]
> - "Lowest resonance": $\lambda/2$ for like ends, $\lambda/4$ for unlike ends.
> - $f$ against $\omega = 2\pi f$: read which is asked.
> - A voltage null is a current maximum. The line there looks like a short circuit, not like nothing.

> [!exam] On exams
> Past papers only: Lectures 31–33 are **not on FA26 Midterm 3** (Lectures 1–30). Two steady-state measurements, one per end ($\tilde V = 0$ or $\tilde I = 0$): name the ends, list the lowest resonances, pick the shapes of $\lvert\tilde V\rvert$ and $\lvert\tilde I\rvert$ (SP19 Exam 3 #5, FA23 Exam 3 #7). Worked twin: [[exams/e3-steady-state-lines#s3-resonances-from-two-measurements|S3]].

**Where it appears.** [[4-transmission-lines/31-periodic-oscillations-in-lossless-tl-circuits|Lecture 31]] (derivation, modes, the notes' example); [[4-transmission-lines/32-input-impedance-and-microwave-resonators|Lecture 32]], where the same frequencies are the stub's series and parallel resonances.

**Practice.** [[practice/topics#resonances-of-line-segments|Resonances of line segments]] (9 problems) — for example [[practice/31-resonances-of-line-segments#311-the-three-lowest-three-ways|31.1 The three lowest, three ways]] (easy), [[practice/31-resonances-of-line-segments#315-a-mode-on-a-shortopen-line|31.5 A mode on a short–open line]] (medium), [[practice/31-resonances-of-line-segments#317-a-resonator-from-two-zero-readings|31.7 A resonator from two zero readings]] (hard).

Related: [[concepts/standing-waves|Standing waves]] · [[concepts/stub-input-impedance|Input impedance of a stub]] · [[concepts/bounce-diagram|Bounce diagram]] · [[concepts/telegraphers-equations|Telegrapher's equations]].
