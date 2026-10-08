---
title: "Wave equation"
description: "∇²E = με ∂²E/∂t² is what Faraday's law and Ampère–Maxwell combine into in a source-free, homogeneous, lossless region. In one dimension its solutions are d'Alembert's f(t − z/v) + g(t + z/v): any two waveforms, one travelling each way, without distortion, at v = 1/√(με)."
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
> The first line is the 3D vector wave equation; it holds for each Cartesian component separately. The second line is the 1D scalar wave equation for a field that depends only on $z$ and $t$, with its general solution. The conditions are $\rho = 0$, $\mathbf{J} = 0$ and constant $\mu$, $\epsilon$. $f$ and $g$ are arbitrary waveforms (the **d'Alembert solutions**). In vacuum $v = c = 1/\sqrt{\mu_0\epsilon_0} = 2.998\times10^8$ m/s.

**Physics.** It is the two first-order curl equations combined into one second-order equation for each field. Take the curl of Faraday's law and use $\nabla\times(\nabla\times\mathbf{E}) = \nabla(\nabla\cdot\mathbf{E}) - \nabla^2\mathbf{E}$, with $\nabla\cdot\mathbf{E} = 0$ (which needs $\rho = 0$ *and* constant $\epsilon$). Then replace $\nabla\times\mathbf{H}$ by $\epsilon\,\partial\mathbf{E}/\partial t$. The only term on the right that survives is the [[concepts/displacement-current|displacement current]]. Without it you get $\nabla^2\mathbf{E} = 0$, Laplace's equation, which has no travelling solutions. So the equation is Maxwell's 1861 term made visible.

In one dimension, write $\tau = z/v$. The operator factors as $(\partial_\tau + \partial_t)(\partial_\tau - \partial_t)$. The first factor is zeroed by any function of $t - \tau$ and the second by any function of $t + \tau$. In the variables $\xi = t - \tau$, $\zeta = t + \tau$ the equation becomes $\partial^2E/\partial\xi\,\partial\zeta = 0$, so *every* solution is $F(\xi) + G(\zeta)$. Physically, $f(t - z/v)$ has the same value wherever $t - z/v$ does, so it slides rigidly toward $+z$ at speed $v$. A pulse keeps its shape because the equation is linear and time-invariant and every Fourier component travels at the same $v$: the medium is non-dispersive.

The wave equation is **necessary but not sufficient**. A Maxwell field must also be divergence-free, and its $\mathbf{E}$ and $\mathbf{H}$ must satisfy the curl equations together. So after solving the wave equation for $\mathbf{E}$, check $\nabla\cdot\mathbf{E} = 0$ and get $\mathbf{H}$ from Faraday's law.

**Examples.** $\cos\big(\omega(t - z/v)\big)$: the second $z$-derivative is $-(\omega/v)^2 = -\omega^2\mu\epsilon$ times the field, and the second $t$-derivative is $-\omega^2$ times it, so the equation holds for every $\omega$. Speeds: in vacuum, $2.998\times10^8$ m/s (30 cm/ns); in polyethylene ($\epsilon_r = 2.25$), $2.00\times10^8$ m/s; with $\epsilon_r = 4$, $1.50\times10^8$ m/s; with $\epsilon_r\approx9$, $10^8$ m/s. Reading a solution (slide 24): $(0.05y - t)^2$ travels toward $+y$ at 20 m/s, $u(t + 0.02x)$ toward $-x$ at 50 m/s, and $\cos(2\pi10^8t - 2\pi z)$ toward $+z$ at $10^8$ m/s. A coax filled with polyethylene carries signals at $1/\sqrt{\mathcal{L}\mathcal{C}} = 1/\sqrt{\mu\epsilon} = 2.00\times10^8$ m/s ([[problems/coax-inductance-and-the-lc-product]]): the line's voltage and current obey the same 1D equation (Unit 4).

> [!trap]
> - A solution of the wave equation need not solve Maxwell's equations. $\mathbf{E} = \hat z\,f(t - z/v)$ solves the 1D equation but has $\nabla\cdot\mathbf{E} = -f'/v\neq0$.
> - Minus goes with plus: $f(t - z/v)$ travels toward $+z$. So does $f(z - vt)$, which is the same kind of function.
> - In $t - z/v$, the coefficient of $z$ is the *slowness* $1/v$ in s/m, not the speed.
> - "$\nabla^2$ of each component" holds only for Cartesian components.
> - Partial derivatives throughout; the slides' $d/dt$ means $\partial/\partial t$.
> - With $\sigma\neq0$ the equation gains a term $\mu\sigma\,\partial\mathbf{E}/\partial t$ and waves decay and change shape (Lectures 22–23). Travel without distortion is a property of lossless media.

**Where it appears.** [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves|Lecture 18]] (derived by the curl-curl route and by cross-differentiation, then solved); Lecture 19 (d'Alembert solutions, radiation from current sheets); Lectures 21–22 (phasor form, where $\partial^2/\partial t^2\to-\omega^2$); Unit 4 (the same equation for the voltage and current on a line); [[problems/a-pulse-on-the-move]].

**Practice.** [[practice/topics#plane-waves-and-the-wave-equation|Plane waves and the wave equation]] (20 problems) — for example [[practice/18-wave-equation-and-plane-waves#181-which-way-and-how-fast|18.1 Which way and how fast]] (easy), [[practice/18-wave-equation-and-plane-waves#186-which-fields-can-be-waves|18.6 Which fields can be waves]] (medium), [[practice/18-wave-equation-and-plane-waves#189-triangle-pulse-in-a-magnetic-medium|18.9 Triangle pulse in a magnetic medium]] (hard).

Related: [[concepts/plane-waves]] · [[concepts/intrinsic-impedance]] · [[concepts/displacement-current]] · [[concepts/faradays-law]] · [[concepts/maxwells-equations]] · [[concepts/curl]].
