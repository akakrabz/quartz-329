---
title: "Worked problem — A backward pulse on a parallel-plate line"
description: "A polyethylene-filled parallel-plate line: its parameters, a current pulse travelling toward −z, the power of a sinusoidal wave, and the filling found from a delay. Modelled on SP19 Exam 3 #2, SP17 #2(ii) and FA23 #4(d)."
tags: [problem, transmission-lines]
---

*Problem · style of SP19 Exam 3 #2, SP17 Exam 3 #2(ii) and FA23 Exam 3 #4(d) · uses [[4-transmission-lines/27-guided-tem-waves-on-transmission-lines|Lecture 27]], [[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation|Lecture 21]] · concepts: [[concepts/telegraphers-equations]], [[concepts/characteristic-impedance]]*

> [!question] Problem
> Two perfectly conducting plates, $W = 4$ cm wide, lie at $x = 0$ and $x = d = 2$ mm and run along $z$ for $l = 30$ m. The gap is filled with polyethylene: $\mu = \mu_0$, $\epsilon = 2.25\epsilon_0$. Neglect fringing. Use $\eta_0 = 120\pi\ \Omega$, $c = 3\times10^8$ m/s and $\epsilon_0 = 10^{-9}/36\pi$ F/m.
>
> (a) Find $\mathcal{L}$, $\mathcal{C}$, $v$, $Z_0$ and the one-way delay.
>
> (b) A current pulse $0.5\,\Pi\big((t+z/v)/T\big)$ A, with $T = 2$ ns and $\Pi$ a unit rectangle, flows along $+z$ on the **top** plate ($x = d$) and returns on the bottom one. Which way does it travel? Inside the pulse, find $V$, $\mathbf{E}$, $\mathbf{H}$, the charge density on each plate, and the power.
>
> (c) The line instead carries $\tilde V(z) = 12\,e^{-j\beta z}$ V at $f = 1.5$ GHz. Find $\beta$, $\tilde I$, $\tilde{\mathbf{E}}$, $\tilde{\mathbf{H}}$, and $\langle P\rangle$ two ways. Is TEM the only mode that propagates?
>
> (d) A line of the same geometry with an unknown non-magnetic filling delays a pulse by 200 ns over its 30 m. Find $\epsilon_r$ and $Z_0$.

## (a) Line parameters

$$
\begin{gathered}
\mathcal{L} = \mu_0\frac dW = 4\pi\times10^{-7}\cdot\frac{1}{20} = 62.8\ \text{nH/m},\\[4pt]
\mathcal{C} = \epsilon\frac Wd = \frac{2.25\times10^{-9}}{36\pi}\cdot20 = 398\ \text{pF/m},\\[4pt]
v = \frac{1}{\sqrt{\mathcal{L}\mathcal{C}}} = \frac{c}{1.5} = 2\times10^8\ \text{m/s},\\[4pt]
Z_0 = \sqrt{\frac{\mathcal{L}}{\mathcal{C}}} = \eta\frac dW = 80\pi\cdot0.05 = 4\pi = 12.6\ \Omega.
\end{gathered}
$$

The delay is $l/v = 150$ ns. $W/d = 20$ justifies neglecting fringing.

## (b) The backward pulse

The argument $t+z/v$ means travel toward $-z$. The lecture's $I$ is the $+z$ current on plate 2 ($x = 0$), which here carries the return: $I = -0.5$ A inside the pulse.

A backward wave has $V = g$ and $I = -g/Z_0$:

$$
\begin{gathered}
V = -Z_0I = 4\pi\cdot0.5 = 2\pi = 6.28\ \text{V},\\[4pt]
E_x = \frac Vd = 1000\pi\ \text{V/m} = 3.14\ \text{kV/m},\\[4pt]
H_y = \frac IW = -12.5\ \text{A/m}.
\end{gathered}
$$

Checks:
- $\lvert E_x/H_y\rvert = 1000\pi/12.5 = 80\pi = \eta$.
- $\mathbf{E}\times\mathbf{H}\propto\hat x\times(-\hat y) = -\hat z$, the travel direction.
- Top plate, $\hat n = -\hat x$: $\mathbf{J}_s = \hat n\times\mathbf{H} = (-\hat x)\times(-12.5\,\hat y) = +\hat z\,12.5$ A/m. Times 4 cm: the given 0.5 A.

Charge, from $\rho_s = \hat n\cdot\mathbf{D}$ with $\hat n$ into the gap:

$$
\begin{gathered}
\rho_s(x = 0) = +\epsilon E_x = \frac{2.25\times10^{-9}}{36\pi}\cdot1000\pi\\[4pt]
= 62.5\ \text{nC/m}^2 .
\end{gathered}
$$

The top plate carries $-62.5$ nC/m². Per metre: $62.5\times0.04 = 2.5$ nC/m $= \mathcal{C}V$.

The pulse is $vT = 0.4$ m long. $p = VI = -\pi$ W: $\pi$ W toward $-z$, so the pulse carries $\pi\cdot2\ \text{ns} = 6.28$ nJ.

> [!key] Answer (b)
> Toward $-z$. $V = 2\pi$ V; $\mathbf{E} = \hat x\,1000\pi$ V/m and $\mathbf{H} = -\hat y\,12.5$ A/m inside the pulse, zero outside. $\rho_s = +62.5$ nC/m² at $x = 0$, $-62.5$ nC/m² at $x = d$. Power $\pi$ W toward $-z$.

> [!trap] Where (b) loses points
> - Fixing only one sign (plate or direction) gives $V = -2\pi$ V. Sign $I$ on plate 2 first, then $V = -Z_0I$.
> - Guessing the positive plate from the current. The charge follows $E_x$.

## (c) A sinusoidal wave

$$
\begin{gathered}
\lambda = \frac vf = 13.3\ \text{cm},\\[4pt]
\beta = \frac{2\pi}{\lambda} = 15\pi = 47.1\ \text{rad/m},\\[4pt]
\tilde I = \frac{\tilde V}{Z_0} = \frac{3}{\pi}e^{-j\beta z}\\[4pt]
= 0.955\,e^{-j\beta z}\ \text{A},\\[4pt]
\tilde{\mathbf{E}} = \hat x\,\frac{\tilde V}{d} = \hat x\,6000\,e^{-j\beta z}\ \text{V/m},\\[4pt]
\tilde{\mathbf{H}} = \hat y\,\frac{\tilde I}{W} = \hat y\,23.9\,e^{-j\beta z}\ \text{A/m}.
\end{gathered}
$$

Power, from the fields and from the circuit:

$$
\begin{gathered}
\langle S\rangle = \tfrac12(6000)(23.9) = 71.6\ \text{kW/m}^2,\\[4pt]
\langle S\rangle Wd = 71.6\times10^3\cdot8\times10^{-5} = 5.73\ \text{W},\\[4pt]
\tfrac12\text{Re}\{\tilde V\tilde I^*\} = \frac{12^2}{2\cdot4\pi} = \frac{18}{\pi} = 5.73\ \text{W}.
\end{gathered}
$$

Only TEM propagates: $d = 2\ \text{mm}\ll\lambda/2 = 6.7$ cm; the first non-TEM mode needs $f>v/2d = 50$ GHz.

## (d) The filling from a delay

$$
\begin{gathered}
v = \frac{30\ \text{m}}{200\ \text{ns}} = 1.5\times10^8\ \text{m/s},\\[4pt]
\epsilon_r = \Big(\frac cv\Big)^2 = 4 .
\end{gathered}
$$

Then $\eta = 60\pi\ \Omega$ and $Z_0 = 60\pi\cdot0.05 = 3\pi = 9.42\ \Omega$.

> [!key] Answers (c), (d)
> (c) $\beta = 15\pi$ rad/m, $\langle P\rangle = 18/\pi = 5.73$ W, TEM only. (d) $\epsilon_r = 4$, $Z_0 = 3\pi\ \Omega$.

## The pattern

1. $\mathcal{L}$ and $\mathcal{C}$ from GF; $v$ from the filling; $Z_0 = \eta/\text{GF}$.
2. Direction from the argument, then the sign of $I$ on the reference conductor.
3. $V = \pm Z_0I$, $E_x = V/d$, $H_y = I/W$; check $\mathbf{E}\times\mathbf{H}$ and $\hat n\times\mathbf{H}$.
4. Power as $VI$ or $\tfrac12\text{Re}\{\tilde V\tilde I^*\}$, cross-checked with $\langle S\rangle Wd$.

SP19 Exam 3 #2 runs these steps for a forward delta pulse on the bottom plate; SP17 #2(ii) asks (b)'s sign questions; FA23 #4(d) is (d). Here the pulse runs backward on the top plate: $I$ and $\mathbf{H}$ change sign, $V$ and the charges do not.
