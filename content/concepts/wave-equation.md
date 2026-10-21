---
title: "Wave equation"
description: "∇²E = με ∂²E/∂t² in a source-free, lossless region; in 1D its solutions are f(t − z/v) + g(t + z/v)."
tags: [concept, waves]
aliases: ["vector wave equation", "1D wave equation", "scalar wave equation", "d'Alembert solution", "d'Alembert solutions"]
---

> [!key] Definition
> $$
> \begin{gathered}
> \nabla^2\mathbf{E} = \mu\epsilon\,\frac{\partial^2\mathbf{E}}{\partial t^2},\qquad \nabla^2\mathbf{H} = \mu\epsilon\,\frac{\partial^2\mathbf{H}}{\partial t^2},\\[6pt]
> \frac{\partial^2E_x}{\partial z^2} = \frac{1}{v^2}\frac{\partial^2E_x}{\partial t^2}\quad\Longrightarrow\quad E_x = f\Big(t-\frac zv\Big) + g\Big(t+\frac zv\Big),\qquad v = \frac{1}{\sqrt{\mu\epsilon}} .
> \end{gathered}
> $$
> Line 1: the 3D vector wave equation, per Cartesian component. Line 2: the 1D form for a field depending on $z$, $t$ only, and its general solution. Conditions: $\rho = 0$, $\mathbf{J} = 0$, constant $\mu$, $\epsilon$. $f$, $g$ arbitrary (**d'Alembert solutions**). Vacuum: $v = c = 1/\sqrt{\mu_0\epsilon_0} = 2.998\times10^8$ m/s.

**Physics.** Curl Faraday's law, use $\nabla\times(\nabla\times\mathbf{E}) = \nabla(\nabla\cdot\mathbf{E}) - \nabla^2\mathbf{E}$ with $\nabla\cdot\mathbf{E} = 0$ (needs $\rho = 0$ *and* constant $\epsilon$), and replace $\nabla\times\mathbf{H}$ by $\epsilon\,\partial\mathbf{E}/\partial t$. Only the [[concepts/displacement-current|displacement current]] survives on the right; without it, $\nabla^2\mathbf{E} = 0$ (Laplace) has no travelling solutions. Maxwell's 1861 term made visible.

In 1D, with $\tau = z/v$, the operator factors as $(\partial_\tau + \partial_t)(\partial_\tau - \partial_t)$, zeroed by functions of $t - \tau$ and of $t + \tau$. In $\xi = t - \tau$, $\zeta = t + \tau$ it reads $\partial^2E/\partial\xi\,\partial\zeta = 0$, so *every* solution is $F(\xi) + G(\zeta)$. $f(t - z/v)$ is constant wherever $t - z/v$ is: it slides rigidly toward $+z$ at $v$. A pulse keeps its shape: the equation is linear and time-invariant, and every Fourier component travels at one $v$ (non-dispersive).

**Necessary but not sufficient**: a Maxwell field must also be divergence-free, with $\mathbf{E}$ and $\mathbf{H}$ obeying the curl equations together. Check $\nabla\cdot\mathbf{E} = 0$ and get $\mathbf{H}$ from Faraday's law.

**Examples.** $\cos\big(\omega(t - z/v)\big)$: the second $z$-derivative is $-(\omega/v)^2 = -\omega^2\mu\epsilon$ times the field, the second $t$-derivative $-\omega^2$ times it, so it holds for every $\omega$. Speeds: vacuum $2.998\times10^8$ m/s (30 cm/ns); polyethylene ($\epsilon_r = 2.25$) $2.00\times10^8$ m/s; $\epsilon_r = 4$, $1.50\times10^8$ m/s; $\epsilon_r\approx9$, $10^8$ m/s. Slide 24: $(0.05y - t)^2$ goes $+y$ at 20 m/s, $u(t + 0.02x)$ $-x$ at 50 m/s, $\cos(2\pi10^8t - 2\pi z)$ $+z$ at $10^8$ m/s. Polyethylene coax: $1/\sqrt{\mathcal{L}\mathcal{C}} = 1/\sqrt{\mu\epsilon} = 2.00\times10^8$ m/s ([[problems/coax-inductance-and-the-lc-product]]); line voltage and current obey the same 1D equation (Unit 4).

> [!trap]
> - $\mathbf{E} = \hat z\,f(t - z/v)$ solves the 1D equation but has $\nabla\cdot\mathbf{E} = -f'/v\neq0$.
> - Minus goes with plus: $f(t - z/v)$ and $f(z - vt)$ travel toward $+z$.
> - In $t - z/v$ the coefficient of $z$ is the *slowness* $1/v$ (s/m), not the speed.
> - $\nabla^2$ per component: Cartesian components only.
> - Partial derivatives throughout; the slides' $d/dt$ means $\partial/\partial t$.
> - $\sigma\neq0$ adds $\mu\sigma\,\partial\mathbf{E}/\partial t$: waves decay and change shape (Lectures 22–23). Distortion-free travel needs a lossless medium.

**Where it appears.** [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves|Lecture 18]] (derived two ways, solved); Lecture 19 (d'Alembert, current sheets); Lectures 21–22 (phasor form, $\partial^2/\partial t^2\to-\omega^2$); Unit 4 (lines); [[problems/a-pulse-on-the-move]].

**Practice.** [[practice/topics#plane-waves-and-the-wave-equation|Plane waves and the wave equation]] (25 problems) — for example [[practice/18-wave-equation-and-plane-waves#181-which-way-and-how-fast|18.1 Which way and how fast]] (easy), [[practice/18-wave-equation-and-plane-waves#186-which-fields-can-be-waves|18.6 Which fields can be waves]] (medium), [[practice/18-wave-equation-and-plane-waves#189-triangle-pulse-in-a-magnetic-medium|18.9 Triangle pulse in a magnetic medium]] (hard).

Related: [[concepts/plane-waves]] · [[concepts/intrinsic-impedance]] · [[concepts/displacement-current]] · [[concepts/faradays-law]] · [[concepts/maxwells-equations]] · [[concepts/curl]].
