---
title: "Unit 4 · Transmission lines"
description: "Lectures 27–38: guided TEM waves on two-conductor lines, bounce diagrams, sinusoidal steady state, input impedance, the Smith chart, and impedance matching."
tags: [transmission-lines]
---

A transmission line is Maxwell's equations reduced to two wires — voltages and currents that travel, reflect, and interfere. Transients are handled with bounce diagrams, sinusoidal steady state with phasors and the Smith chart. This is where the course pays off for anyone who will ever route a fast signal.

| # | page | one line | practice |
|---|---|---|---|
| 27 | [[4-transmission-lines/27-guided-tem-waves-on-transmission-lines\|Guided TEM waves on transmission lines]] | plates confine a plane wave: $V = E_xd$, $I = H_yW$; telegrapher's equations; $v = 1/\sqrt{\mathcal{L}\mathcal{C}}$, $Z_0 = \sqrt{\mathcal{L}/\mathcal{C}}$; $V = f + g$, $I = (f-g)/Z_0$ | [[practice/27-transmission-line-basics\|12 problems]] |
| 28 | [[4-transmission-lines/28-distributed-circuits-and-bounce-diagrams\|Distributed circuits and bounce diagrams]] | generator launches $\tau_g = Z_0/(R_g+Z_0)$; $\Gamma = (R-Z_0)/(R+Z_0)$ at each end; bounce diagram; DC limit | [[practice/28-bounce-diagrams\|12 problems]] |
| 29 | [[4-transmission-lines/29-bounce-diagram-examples\|Bounce diagram examples]] | impulse response read off the diagram; burst, step and pulse sources; records and snapshots | [[practice/29-bounce-diagram-examples\|12 problems]] |
| 30 | [[4-transmission-lines/30-multi-line-circuits\|Multi-line circuits]] | junction $\Gamma = (Z_k-Z_j)/(Z_k+Z_j)$, $\tau = 1+\Gamma$; resistors at junctions; bounce diagrams across lines | [[practice/30-multi-line-circuits\|12 problems]] |
| 31 | Periodic oscillations in lossless TL circuits | *coming* | — |
| 32 | Input impedance and microwave resonators | *coming* | — |
| 33 | TL circuits with half- and quarter-wave transformers | *coming* | — |
| 34 | Line impedance, generalized reflection coefficient, Smith chart | *coming* | — |
| 36 | Smith chart and VSWR | *coming* | — |
| 37 | Smith chart and impedance matching | *coming* | — |
| 38 | Distribution networks | *coming* | — |

> [!note] Lectures 27–30 follow the course notes
> Written from the course notes (Kudeki) without the slides; every bounce-diagram number was checked against an independent simulation of the line.

**Worked problems:** [[problems/a-backward-pulse-on-a-parallel-plate-line]] (Lecture 27) · [[problems/reading-a-line-from-two-pulses]] (Lecture 28) · [[problems/a-ramp-pulse-meets-its-echo]] (Lecture 29) · [[problems/echoes-trapped-on-the-second-line]] (Lecture 30)

**Concepts:** [[concepts/telegraphers-equations]] · [[concepts/characteristic-impedance]] · [[concepts/bounce-diagram]] · [[concepts/inductance]] · [[concepts/capacitance]] · [[concepts/reflection-and-transmission]]

Planned demos for this unit: reflected waves on a line, open/short standing-wave modes, and an in-browser Smith chart.
