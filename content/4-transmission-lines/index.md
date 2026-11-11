---
title: "Unit 4 · Transmission lines"
description: "Lectures 27–38: guided TEM waves on two-conductor lines, bounce diagrams, sinusoidal steady state, input impedance, the Smith chart, and impedance matching."
tags: [transmission-lines]
---

A transmission line is Maxwell's equations reduced to two wires — voltages and currents that travel, reflect, and interfere. Transients are handled with bounce diagrams, sinusoidal steady state with phasors and the Smith chart. This is where the course pays off for anyone who will ever route a fast signal.

> [!tip] Studying for Midterm 3?
> This unit's part of the exam is Lectures 27–30; Lectures 31–33 below come after its scope. Bounce diagrams are a quarter to a half of every past Exam 3 on hand. The [[exams/index|Midterm 3 review]] page sorts the past papers by problem type with worked twins; the [[0-toolkit/09-midterm-3-summary#8-bounce-diagrams-lectures-2830|equation summary, §8]] has the recipe on one screen.

| # | page | one line | practice |
|---|---|---|---|
| 27 | [[4-transmission-lines/27-guided-tem-waves-on-transmission-lines\|Guided TEM waves on transmission lines]] | plates confine a plane wave: $V = E_xd$, $I = H_yW$; telegrapher's equations; $v = 1/\sqrt{\mathcal{L}\mathcal{C}}$, $Z_0 = \sqrt{\mathcal{L}/\mathcal{C}}$; $V = f + g$, $I = (f-g)/Z_0$ | [[practice/27-transmission-line-basics\|12 problems]] |
| 28 | [[4-transmission-lines/28-distributed-circuits-and-bounce-diagrams\|Distributed circuits and bounce diagrams]] | generator launches $\tau_g = Z_0/(R_g+Z_0)$; $\Gamma = (R-Z_0)/(R+Z_0)$ at each end; bounce diagram; DC limit | [[practice/28-bounce-diagrams\|12 problems]] |
| 29 | [[4-transmission-lines/29-bounce-diagram-examples\|Bounce diagram examples]] | impulse response read off the diagram; burst, step and pulse sources; records and snapshots | [[practice/29-bounce-diagram-examples\|12 problems]] |
| 30 | [[4-transmission-lines/30-multi-line-circuits\|Multi-line circuits]] | junction $\Gamma = (Z_k-Z_j)/(Z_k+Z_j)$, $\tau = 1+\Gamma$; resistors at junctions; bounce diagrams across lines | [[practice/30-multi-line-circuits\|12 problems]] |
| 31 | [[4-transmission-lines/31-periodic-oscillations-in-lossless-tl-circuits\|Periodic oscillations in lossless TL circuits]] | a source-free segment rings in standing-wave modes: like ends $\ell = n\lambda/2$, $f_n = nv/2\ell$; unlike ends $\ell = (2n+1)\lambda/4$; $\lvert V\rvert_{\max} = Z_0\lvert I\rvert_{\max}$ | [[practice/31-resonances-of-line-segments\|8 problems]] |
| 32 | [[4-transmission-lines/32-input-impedance-and-microwave-resonators\|Input impedance and microwave resonators]] | phasors from the load, $\tilde V(d) = V^+e^{j\beta d}+V^-e^{-j\beta d}$; shorted stub $jZ_0\tan\beta\ell$, open stub $-jZ_0\cot\beta\ell$; series and parallel resonance; stub filters | [[practice/32-stubs-and-input-impedance\|8 problems]] |
| 33 | [[4-transmission-lines/33-half-wave-and-quarter-wave-transformers\|TL circuits with half- and quarter-wave transformers]] | $\lambda/2$: $Z_{\text{in}} = Z_L$, signs flip; $\lambda/4$: $Z_{\text{in}} = Z_0^2/Z_L$, $\tilde I_L = -j\tilde V_{\text{in}}/Z_0$; chaining; matching | [[practice/33-half-and-quarter-wave-transformers\|8 problems]] |
| 34 | Line impedance, generalized reflection coefficient, Smith chart | *coming* | — |
| 36 | Smith chart and VSWR | *coming* | — |
| 37 | Smith chart and impedance matching | *coming* | — |
| 38 | Distribution networks | *coming* | — |

> [!note] Lectures 27–33 follow the course notes
> Written from the course notes (Kudeki); build 13 added the Lecture 27–29 slides (Shao; Lecture 28 with the in-class ink). Build 14 added the Lecture 30–32 decks (in-class ink on Lecture 30 and on the first slides of 31 and 32) and the annotated Lecture 27 and 29 decks; Lecture 33 rests on the notes alone. The decks titled Lecture 31 and 32 split the material differently from the notes: each lecture page's header says which slides it uses. Every bounce-diagram and steady-state number was checked against an independent simulation of the line.

**Worked problems:** [[problems/a-backward-pulse-on-a-parallel-plate-line]] (Lecture 27) · [[problems/reading-a-line-from-two-pulses]] (Lecture 28) · [[problems/a-ramp-pulse-meets-its-echo]] (Lecture 29) · [[problems/echoes-trapped-on-the-second-line]] (Lecture 30) · for Lectures 31–33, the five worked twins on [[exams/e3-steady-state-lines#4-worked-twins|Lines in sinusoidal steady state]]

**Concepts:** [[concepts/telegraphers-equations]] · [[concepts/characteristic-impedance]] · [[concepts/bounce-diagram]] · [[concepts/line-resonances]] · [[concepts/stub-input-impedance]] · [[concepts/quarter-wave-transformer]] · [[concepts/inductance]] · [[concepts/capacitance]] · [[concepts/reflection-and-transmission]]

Planned demos for this unit: reflected waves on a line, open/short standing-wave modes, and an in-browser Smith chart.
