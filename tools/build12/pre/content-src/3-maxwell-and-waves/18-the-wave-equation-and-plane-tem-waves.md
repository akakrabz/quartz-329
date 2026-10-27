---
title: "Lecture 18 — The wave equation and plane TEM waves"
description: "Without sources, Maxwell's curl equations sustain each other and give the wave equation ∇²E = με ∂²E/∂t². Plane solutions E = x̂ f(t ∓ z/v) travel undistorted at v = 1/√(με), with H = ±ŷ f/η, η = √(μ/ε) ≈ 377 Ω in vacuum."
tags: [lecture, waves]
lecture: 18
---

*Lecture 18 · course notes §18 · slides "Uniform Plane Waves in Free Space" · prev: [[3-maxwell-and-waves/17-magnetization-and-maxwells-equations-in-matter|Lecture 17]] · next: [[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets|Lecture 19]] · worked problem: [[problems/a-pulse-on-the-move|A pulse on the move]] · practice: [[practice/18-wave-equation-and-plane-waves|12 problems]]*

> [!abstract] In one breath
> With no charges or currents, Maxwell's curl equations still feed each other: changing $\mathbf{H}$ curls $\mathbf{E}$ (Faraday), changing $\mathbf{E}$ curls $\mathbf{H}$ (the displacement current of [[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Lecture 16]]). Together: the **wave equation** $\nabla^2\mathbf{E} = \mu\epsilon\,\partial^2\mathbf{E}/\partial t^2$. Its **plane waves** $\mathbf{E} = \hat x\,f(t\mp z/v)$, any waveform $f$, slide along $\pm z$ unchanged at $v = 1/\sqrt{\mu\epsilon}$ ($c\approx3\times10^8$ m/s in vacuum) with $\mathbf{H} = \pm\hat y\,f/\eta$, the **intrinsic impedance** $\eta = \sqrt{\mu/\epsilon}$ being $\approx377\ \Omega$ in vacuum, and $\mathbf{E}\times\mathbf{H}$ along the travel. Light, radio and X-rays are this one solution with different waveforms.

## 1. Fields without sources?

Take a region that is **homogeneous** (same $\mu$, $\epsilon$ everywhere), **lossless** ($\sigma = 0$) and **source-free**. Can a time-varying field exist there?

> [!key] Maxwell's equations in a source-free, homogeneous, lossless region
> $$
> \begin{gathered}
> \nabla\cdot\mathbf{E} = 0,\qquad \nabla\cdot\mathbf{H} = 0,\\[4pt]
> \nabla\times\mathbf{E} = -\mu\frac{\partial\mathbf{H}}{\partial t},\qquad \nabla\times\mathbf{H} = \epsilon\frac{\partial\mathbf{E}}{\partial t}.
> \end{gathered}
> $$
> Conditions: $\rho = 0$, $\mathbf{J} = 0$ (so $\sigma = 0$), $\mu$ and $\epsilon$ constant in space and time — a linear medium of [[3-maxwell-and-waves/17-magnetization-and-maxwells-equations-in-matter|Lecture 17]] ($\mathbf{B} = \mu\mathbf{H}$, $\mathbf{D} = \epsilon\mathbf{E}$) or vacuum.

A *static* field cannot exist there alone: zero divergence and curl everywhere, dying off far away, means zero (Helmholtz, [[1-electrostatics/04-divergence-and-curl|Lecture 4]]); a capacitor gap holds one only from outside charges. A *time-varying* field can: electromagnetic waves, radio to gamma rays, carrying energy and momentum from Sun to Earth. Their sources (time-varying $\rho$, $\mathbf{J}$, linked by the [[concepts/continuity-equation|continuity equation]]) are elsewhere; once launched, the fields carry on alone.

How, in the slides' opening argument (slide 3, terms circled and joined by arrows in class):

1. a time-varying source current $\mathbf{J}(t)$ produces a time-varying $\mathbf{H}$ around it (Ampère–Maxwell);
2. a time-varying $\mathbf{B} = \mu\mathbf{H}$ produces an $\mathbf{E}$ that curls ([[concepts/faradays-law|Faraday]], Lecture 14);
3. a time-varying $\mathbf{D} = \epsilon\mathbf{E}$ produces an $\mathbf{H}$ that curls (the [[concepts/displacement-current|displacement current]], Lecture 16);
4. back to step 2.

Steps 2–4 need no current: $\cdots\to\mathbf{H}\to\mathbf{E}\to\mathbf{H}\to\cdots$ sustains itself and moves away from the source. That recursion *is* the wave. Without the displacement current step 3 is missing: induction, but no propagation.

## 2. The wave equation

The notes: curl Faraday's law and replace $\nabla\times\mathbf{H}$ by Ampère–Maxwell:

$$
\nabla\times(\nabla\times\mathbf{E}) = -\mu\frac{\partial}{\partial t}\big(\nabla\times\mathbf{H}\big) = -\mu\epsilon\frac{\partial^2\mathbf{E}}{\partial t^2}.
$$

The left side is $\nabla\times(\nabla\times\mathbf{E}) = \nabla(\nabla\cdot\mathbf{E}) - \nabla^2\mathbf{E}$ ([[1-electrostatics/04-divergence-and-curl#a-free-consequence-charge-is-conserved|Lecture 4]], [[0-toolkit/02-vector-calculus-cheatsheet#identities-valid-for-any-smooth-fields|toolkit]]), whose first term vanishes since $\nabla\cdot\mathbf{E} = 0$. Each step uses an assumption:

- **$\mu$ constant**: it leaves the curl, and $\partial\mathbf{B}/\partial t = \mu\,\partial\mathbf{H}/\partial t$ (swapping $\nabla\times$ and $\partial/\partial t$ is always allowed).
- **$\mathbf{J} = 0$, $\epsilon$ constant**: $\nabla\times\mathbf{H} = \epsilon\,\partial\mathbf{E}/\partial t$. In a conductor $\mathbf{J} = \sigma\mathbf{E}$ adds $\mu\sigma\,\partial\mathbf{E}/\partial t$, and the wave decays (Lectures 22–23).
- **$\nabla\cdot\mathbf{E} = 0$** needs $\rho = 0$ *and* constant $\epsilon$, since $\nabla\cdot(\epsilon\mathbf{E}) = \epsilon\nabla\cdot\mathbf{E} + \mathbf{E}\cdot\nabla\epsilon$.
- **Cartesian components**: only there does $\nabla^2\mathbf{E} = \hat x\nabla^2E_x + \hat y\nabla^2E_y + \hat z\nabla^2E_z$ split into scalar Laplacians; not in cylindrical or spherical components.

> [!key] The 3D vector wave equation
> $$
> \nabla^2\mathbf{E} = \mu\epsilon\,\frac{\partial^2\mathbf{E}}{\partial t^2},\qquad \nabla^2\mathbf{H} = \mu\epsilon\,\frac{\partial^2\mathbf{H}}{\partial t^2},
> $$
> i.e. $\dfrac{\partial^2E_x}{\partial x^2}+\dfrac{\partial^2E_x}{\partial y^2}+\dfrac{\partial^2E_x}{\partial z^2} = \mu\epsilon\dfrac{\partial^2E_x}{\partial t^2}$, and likewise for every Cartesian component of $\mathbf{E}$ and $\mathbf{H}$. The $\mathbf{H}$ equation follows from the curl of Ampère–Maxwell with $\nabla\cdot\mathbf{H} = 0$ and Faraday; the notes derive only the $\mathbf{E}$ one.

**The displacement current is the whole story.** Without $\partial\mathbf{D}/\partial t$ the right side is zero: $\nabla^2\mathbf{E} = 0$, Laplace's equation, no waves. The term Maxwell added for charge conservation is the term that produces light.

**Necessary, not sufficient.** A solution of the wave equation must also be divergence-free, and its $\mathbf{E}$, $\mathbf{H}$ must satisfy the first-order curl equations *together*. §3 shows one that fails.

## 3. The planar problem: only $E_x(z,t)$ and $H_y(z,t)$

The notes and the slides reach this reduced problem by different routes.

**The notes' route: try the simplest field.** $\mathbf{E} = \hat x\,E_x(z,t)$: "$x$-**polarized**" (polarization = direction of $\mathbf{E}$), depending on $z$ and $t$ only. Gauss holds ($\partial E_x/\partial x = 0$). Faraday gives $\nabla\times\mathbf{E} = \hat y\,\partial E_x/\partial z$, so $\mathbf{H} = \hat y\,H_y(z,t)$ (a static field left out). The curl equations collapse to:

> [!key] The two component equations
> $$
> \frac{\partial E_x}{\partial z} = -\mu\,\frac{\partial H_y}{\partial t},\qquad -\frac{\partial H_y}{\partial z} = \epsilon\,\frac{\partial E_x}{\partial t}.
> $$
> First: $y$-component of Faraday, $(\nabla\times\mathbf{E})_y = \partial E_x/\partial z$. Second: $x$-component of Ampère–Maxwell, $(\nabla\times\mathbf{H})_x = \partial H_z/\partial y - \partial H_y/\partial z = -\partial H_y/\partial z$ — hence the minus sign. A field varying along $z$ forces its partner to vary in time: §1's chain as equations.

**The slides' route: a current sheet as the source.** An infinite sheet $\mathbf{J}_s = -J_s(t)\,\hat x$ [A/m] in the plane $z = 0$, free space on both sides.

<!-- fig:wave-current-sheet -->

- *No $x$ or $y$ dependence*: the sheet looks the same from every $(x, y)$ ("→ 0" inked on slides 8–9).
- *$\mathbf{H}$ along $\pm\hat y$*: for steady $J_s$, [[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential|Lecture 13]]'s $\mathbf{H} = \tfrac12\mathbf{J}_s\times\hat n = \pm\tfrac12J_s\,\hat y$ for $z\gtrless0$ ($\hat n$ toward the field point).
- *$\mathbf{E}$ along $\hat x$ only*: Faraday's $y$-component, $\partial E_x/\partial z = -\mu_0\,\partial H_y/\partial t$, gives $E_x\neq0$; its $x$-component, $-\partial E_y/\partial z = -\mu_0\,\partial H_x/\partial t = 0$, makes $E_y$ uniform (and, by Ampère–Maxwell, constant), a field that would outlive the source, so set to zero. Gauss off the sheet, $\partial E_z/\partial z = 0$, removes $E_z$ likewise. So $\mathbf{E} = E_x(z,t)\,\hat x$.

The slides thus *derive* what the notes *assume*. Off the sheet ("in $z = 0$ plane", ink) the component equations hold with $\mu_0$, $\epsilon_0$. Steady $J_s$ gives uniform fields each side, the static sheet; time-varying $J_s$ couples $E_x$ and $H_y$, and waves leave both faces. Lecture 19 finds their amplitude and the jump of $H_y$ by $J_s$, and names them **uniform plane TEM waves**: *transverse electromagnetic* ($\mathbf{E}$, $\mathbf{H}$ perpendicular to the travel), *uniform plane* (same fields on each plane $z = $ const). Slide 10's ink gives the sign: "$\mathbf{E}$ always opposite of $\mathbf{J}_s$".

**Why not $\mathbf{E}$ along $z$?** $\mathbf{E} = \hat z\,f(t\mp z/v)$ solves the 1D wave equation of §4, yet $\nabla\cdot\mathbf{E} = \partial E_z/\partial z = \mp f'/v\neq0$ unless $f$ is constant, violating Gauss with $\rho = 0$. Its curl is zero, so Faraday gives it no $\mathbf{H}$ partner, and Ampère–Maxwell then forces $\partial E_z/\partial t = 0$. This is §2's necessary-not-sufficient point: a source-free plane wave has no field component along its travel.

## 4. The 1D wave equation and its solutions

Cross-differentiate (slide 15): $\partial/\partial z$ of the first equation, swap the derivatives, substitute the second:

$$
\frac{\partial^2E_x}{\partial z^2} = -\mu\frac{\partial}{\partial t}\Big(\frac{\partial H_y}{\partial z}\Big) = -\mu\frac{\partial}{\partial t}\Big(-\epsilon\frac{\partial E_x}{\partial t}\Big).
$$

(The 3D equation with $\mathbf{E} = \hat xE_x(z,t)$ gives it directly: the notes' route.)

> [!key] The 1D scalar wave equation
> $$
> \frac{\partial^2E_x}{\partial z^2} = \mu\epsilon\,\frac{\partial^2E_x}{\partial t^2} = \frac{1}{v^2}\frac{\partial^2E_x}{\partial t^2},\qquad v\equiv\frac{1}{\sqrt{\mu\epsilon}}\ [\text{m/s}],\qquad c = \frac{1}{\sqrt{\mu_0\epsilon_0}} = 2.998\times10^8\ \text{m/s}.
> $$
> $H_y$ obeys the same equation. Handy: $c\approx30$ cm per nanosecond, 300 m per microsecond, 300 km per millisecond.

**Cosines, by substitution (notes).** $E_x = \cos\big(\omega(t - z/v)\big)$ gives $\partial^2E_x/\partial z^2 = -(\omega/v)^2E_x = -\omega^2\mu\epsilon\,E_x$ and $\partial^2E_x/\partial t^2 = -\omega^2E_x$: it works for every $\omega$, as does $\cos\big(\omega(t + z/v)\big)$. The sign inside sets the direction of travel.

**Any waveform, by factoring (slides).** With $\tau\equiv z/v$ (slides: $\tau = z\sqrt{\mu_0\epsilon_0}$ in free space, so 1 m is $\tau = 3.34$ ns), the equation is $\partial^2E_x/\partial\tau^2 = \partial^2E_x/\partial t^2$, and it factors like $x^2 - y^2 = (x+y)(x-y)$:

$$
\Big(\frac{\partial}{\partial\tau}+\frac{\partial}{\partial t}\Big)\Big(\frac{\partial}{\partial\tau}-\frac{\partial}{\partial t}\Big)E_x = 0 .
$$

$\partial_\tau E_x = -\partial_tE_x$ is solved by $E_x = A\,f(t-\tau)$, since $\partial_\tau f(t-\tau) = -f'$ and $\partial_t f(t-\tau) = +f'$ (chain rule, inked on slide 19); $\partial_\tau E_x = +\partial_tE_x$ by $E_x = B\,g(t+\tau)$. Adding, with $\tau = z/v$:

> [!key] d'Alembert's general solution
> $$
> E_x(z,t) = A\,f\Big(t-\frac zv\Big) + B\,g\Big(t+\frac zv\Big),
> $$
> $f$, $g$ *any* waveforms, $A$, $B$ constants. The first term travels toward $+z$, the second toward $-z$: the minus sign goes with $+z$ (the slide circles "$-z$" with "+z direction" and "$+z$" with "−z direction"). The notes call these the **d'Alembert wave solutions**.

> [!derivation]- Why every solution has this form, not just these two families
> Put $\xi = t-\tau$, $\zeta = t+\tau$. Then $\partial_\tau = -\partial_\xi + \partial_\zeta$, $\partial_t = \partial_\xi + \partial_\zeta$, so $\partial_\tau + \partial_t = 2\partial_\zeta$ and $\partial_\tau - \partial_t = -2\partial_\xi$, and the wave equation becomes
> $$
> \frac{\partial}{\partial\xi}\Big(\frac{\partial E_x}{\partial\zeta}\Big) = 0 .
> $$
> So $\partial E_x/\partial\zeta$ is a function of $\zeta$ alone; integrating in $\zeta$, $E_x = G(\zeta) + F(\xi)$ with $F$ arbitrary. This is d'Alembert's argument for the vibrating string; the slide's "two first-order equations" is its operator shorthand.

**Why any waveform works (notes).** Constant $\mu$, $\epsilon$ make the equations *linear and time-invariant*: sums and time shifts of solutions are solutions. So $\sum_nA_n\cos\big(\omega_n(t - z/v) + \theta_n\big) = f(t - z/v)$, $f(t) = \sum_nA_n\cos(\omega_nt + \theta_n)$, solves it, and by Fourier analysis (ECE 210) $f$ can be any practical signal. Key: **every frequency travels at the same $v$** ($\mu$, $\epsilon$ frequency-independent), so a pulse keeps its shape — unlike in conductors (Lectures 22–23) or a dispersive dielectric (Lorentz model, [[1-electrostatics/11-lorentz-drude-models-for-conductivity-and-susceptibility|Lecture 11]]).

**What "travels" means.** $f(t - z/v)$ is constant wherever $t - z/v$ is: a feature at $z_0$ at time $t_0$ is at $z_0 + v(t - t_0)$ at time $t$, so the pattern slides rigidly toward $+z$ at $v$. For $g(t + z/v)$ it is at $z_0 - v(t - t_0)$, toward $-z$.

<!-- fig:wave-pulse-two-times -->

Notation: the slides' $\tau = z/v$ is a time-like *coordinate*; in the notes' margin plots (and Lecture 19) $\tau$ is a *pulse duration*, as in $\triangle(t/\tau)$. Neither is the collision, relaxation or circuit $\tau$ of earlier lectures.

## 5. H from E: the intrinsic impedance

**From Faraday's law (notes).** For $E_x = f(t - z/v)$, $\partial E_x/\partial z = -f'/v$, so $-\mu\,\partial H_y/\partial t = -f'/v$; integrating in time (dropping a static constant), $H_y = f/(\mu v)$. Since $\mu v = \mu/\sqrt{\mu\epsilon} = \sqrt{\mu/\epsilon}$, call it $\eta$: $H_y = f/\eta$. For $E_x = g(t + z/v)$ the $z$-derivative flips sign: $H_y = -g/\eta$.

**From Ampère–Maxwell (slides).** $\partial H_y/\partial z = -\epsilon\,\partial E_x/\partial t = -\epsilon\,[A f' + B g']$. Integrate in $z$ with $\int f'(t - z/v)\,dz = -v f$ and $\int g'(t + z/v)\,dz = +v g$:

$$
H_y = \epsilon v\,\big[A f - B g\big] = \frac1\eta\big[A f - B g\big],\qquad\text{since }\ \epsilon v = \sqrt{\epsilon/\mu} = 1/\eta .
$$

The $z$-integration "constant" is a function of $t$; Faraday's law forces it constant in time too, a uniform static field, set to zero. Slide 21 drops it silently; the reason is slide 9's for $E_y$ ("we can turn off our source"). The routes agree and each satisfies *both* component equations (checked numerically for arbitrary $f$, $g$; flipping the sign of $Bg$ breaks Ampère's law).

> [!key] The plane-wave pair and the intrinsic impedance
> $$
> \begin{gathered}
> E_x = A f\Big(t-\frac zv\Big) + B g\Big(t+\frac zv\Big),\qquad H_y = \frac1\eta\Big[A f\Big(t-\frac zv\Big) - B g\Big(t+\frac zv\Big)\Big],\\[6pt]
> \eta\equiv\sqrt{\frac\mu\epsilon} = \mu v = \frac{1}{\epsilon v}\ [\Omega],\qquad \eta_0 = \sqrt{\frac{\mu_0}{\epsilon_0}} = 376.7\ \Omega\approx120\pi\ \Omega .
> \end{gathered}
> $$
> One wave: $E_x/H_y = +\eta$ toward $+z$, $-\eta$ toward $-z$. Units: (V/m)/(A/m) = Ω. With $\mathbf{B} = \mu\mathbf{H}$: $\lvert\mathbf{B}\rvert = \lvert\mathbf{E}\rvert/v$, a quick check in any problem.

The notes' general rule: **$\mathbf{H}$ is $\mathbf{E}$ divided by $\eta$ and rotated 90° so that $\mathbf{E}\times\mathbf{H}$ points the way the wave travels**; $\mathbf{E}$ is $\eta\mathbf{H}$ rotated back. With $\hat u$ the direction of travel:

$$
\mathbf{H} = \frac1\eta\,\hat u\times\mathbf{E},\qquad \mathbf{E} = \eta\,\mathbf{H}\times\hat u .
$$

$\mathbf{E}\times\mathbf{H}$ is the **Poynting vector**, here only the direction rule (ink: "$\mathbf{E}\times\mathbf{H}\to$ propagation direction"); its meaning as power per unit area is Lecture 20.

<!-- fig:wave-eh-triads -->

> [!key] Sign table (every row checked with an explicit cross product)
> | wave | $\mathbf{E}$ | $\mathbf{H}$ | $\mathbf{E}\times\mathbf{H}$ | travels toward |
> |---|---|---|---|---|
> | $x$-polarized | $\hat x\,f(t-z/v)$ | $+\hat y\,f(t-z/v)/\eta$ | $\hat x\times\hat y = +\hat z$ | $+z$ |
> | $x$-polarized | $\hat x\,f(t+z/v)$ | $-\hat y\,f(t+z/v)/\eta$ | $\hat x\times(-\hat y) = -\hat z$ | $-z$ |
> | $y$-polarized | $\hat y\,f(t-z/v)$ | $-\hat x\,f(t-z/v)/\eta$ | $\hat y\times(-\hat x) = +\hat z$ | $+z$ |
> | $y$-polarized | $\hat y\,f(t+z/v)$ | $+\hat x\,f(t+z/v)/\eta$ | $\hat y\times\hat x = -\hat z$ | $-z$ |
> | $z$-polarized | $\hat z\,f(t\mp z/v)$ | — | — | impossible: $\nabla\cdot\mathbf{E}\neq0$ (§3) |
>
> The notes write the $y$-polarized pair as $\mathbf{E} = \hat yf(t\mp z/v)$, $\mathbf{H} = \mp\hat x f(t\mp z/v)/\eta$ (upper signs together, lower together): the sign before $\hat x$ is opposite to the one before $\hat y$ in the $x$-polarized pair.

> [!example] Example — a 1 V/m plane wave in vacuum
> $E = 1$ V/m in free space: $H = E/\eta_0 = 2.65$ mA/m, $B = \mu_0H = E/c = 3.34$ nT — tiny next to the Earth's roughly 50 μT, but not negligible: different units make "small" meaningless, and the ratio is fixed, $E/B = c$ ($E/H = \eta_0$). If $\mathbf{E} = \hat y$ V/m travels toward $-z$: $\mathbf{H} = \hat u\times\mathbf{E}/\eta_0 = (-\hat z)\times\hat y/\eta_0 = +\hat x\,2.65$ mA/m. Check: $\hat y\times\hat x = -\hat z$ ✓.

## 6. Reading a wave

**Direction and speed from the argument.** A field depending on position and time only through $t - \hat u\cdot\mathbf{r}/v$ travels along $+\hat u$ at speed $v$. Two ways to read an argument:

- Factor out the coefficient of $t$: $at - bz = a\,(t - z/(a/b))$ ($a, b>0$), so $f(at - bz)$ travels toward $+z$ at $a/b$, and $f(at + bz)$ toward $-z$ at $a/b$.
- Compare the signs of the $t$ term and the position term: opposite → toward $+$ that axis; same → toward $-$. Term order and overall sign do not matter: $z - vt = -v(t - z/v)$, so a function of $z - vt$ travels toward $+z$.

> [!example] Example (slides, challenge) — the velocities of three waves
> Velocities of $f = (0.05y - t)^2$, $g = u(t + 0.02x)$, $h = \cos(2\pi10^8t - 2\pi z)$ (metres, seconds)? Options:
> (a) $0.05\hat y,\ -0.02\hat x,\ 10^8\hat z$; (b) $0.05\hat y,\ -0.02\hat x,\ -10^8\hat z$; (c) $20\hat y,\ -50\hat x,\ 10^8\hat z$; (d) $20\hat y,\ 50\hat x,\ 10^8\hat z$; (e) $20\hat y,\ -50\hat x,\ -10^8\hat z$.
> - $f = (0.05y - t)^2 = (t - y/20)^2$: toward $+y$ at **20 m/s**; its zero sits at $y = 20t$.
> - $g = u(t + x/50)$: same signs, toward $-x$ at **50 m/s**.
> - $h = \cos\big(2\pi10^8(t - z/10^8)\big)$: toward $+z$ at **$10^8$ m/s**.
>
> **Answer (c).** (a), (b) quote the *slownesses* $1/v$ in s/m; (d) loses the sign of $g$; (b), (e) flip $h$. In $f$, $(0.05y - t) = -(t - y/20)$: only the relative sign counts. $h$, at a third of $c$, is not in vacuum (§7).

**Fixed position or fixed time.** A wave may be given as a *record* at one place, $E(0,t)$, or a *snapshot* at one instant, $E(z,0)$. Slide 25 converts:

> [!key] Shift identities
> $$
> \begin{gathered}
> \text{toward}\ {+z}:\quad E(z,t) = E\Big(0,\ t-\frac zv\Big) = E(z - vt,\ 0),\\[4pt]
> \text{toward}\ {-z}:\quad E(z,t) = E\Big(0,\ t+\frac zv\Big) = E(z + vt,\ 0).
> \end{gathered}
> $$
> A probe at $z$ sees what the probe at $0$ saw $z/v$ earlier ($+z$ travel) or will see $z/v$ later ($-z$ travel); the snapshot at $t$ is the $t = 0$ snapshot slid $vt$ along the travel.

**The mirror.** At $t = 0$ a $+z$ wave has $E(z,0) = E(0, -z/v)$, the record reversed: the front reaches a probe first (left of the record) but leads on the right in space. A $-z$ wave, $E(z,0) = E(0, z/v)$, is not mirrored. The notes' symmetric triangle hides this; asymmetric pulses show it (§4 figure, rows 2–3).

> [!example] Example (slides) — a moving waveform
> A wave travelling toward $-z$ at 100 m/s is recorded at $z = 0$: $E(0,t)$ rises linearly from 0 to 1 over $0<t<1$ s, stays at 1 until 2 s, falls linearly to 0 at 4 s. Find $E$ at (a) $z = 200$ m, $t = 0.2$ s; (b) $z = -300$ m, $t = 3.4$ s; (c) $z = 100$ m, $t = 0.6$ s.
>
> Toward $-z$: $E(z,t) = E(0,\ t + z/v)$, $z/v = z/(100\ \text{m/s})$.
> - (a) $t + z/v = 0.2 + 2 = 2.2$ s, falling ramp: $E = 1 - (2.2-2)/2 = $ **0.9**.
> - (b) $3.4 - 3 = 0.4$ s, rising ramp: **0.4**.
> - (c) $0.6 + 1 = 1.6$ s, plateau: **1.0**.
>
> The wrong sign, $t - z/v$, gives $-1.8$, $6.4$, $-0.4$ s: all miss the pulse, answers $0, 0, 0$ — when every answer is zero, suspect the sign. The $t = 0$ snapshot $E(0, z/100)$ is zero for $z\le0$, rises to 1 at $z = 100$ m, is flat to 200 m, zero at 400 m; at $t = 1$ s it sits 100 m further toward $-z$. In (b) the record's 0.4 s point reaches $z = -300$ m 3 s later.

<!-- fig:wave-moving-waveform -->

## 7. In matter, and on a cable

Nothing in §§2–6 needed vacuum. In a linear medium ([[3-maxwell-and-waves/17-magnetization-and-maxwells-equations-in-matter|Lecture 17]] for $\mu = \mu_r\mu_0$, [[1-electrostatics/09-static-fields-in-dielectric-media|Lecture 9]] for $\epsilon = \epsilon_r\epsilon_0$) the bound charges and currents are already inside $\mu$ and $\epsilon$:

> [!key] Speed and impedance in a medium
> $$
> v = \frac{c}{\sqrt{\mu_r\epsilon_r}},\qquad \eta = \eta_0\sqrt{\frac{\mu_r}{\epsilon_r}} .
> $$
> Both slow the wave; $\epsilon_r$ lowers $\eta$, $\mu_r$ raises it. $c/v = \sqrt{\mu_r\epsilon_r}$ is the refractive index of optics.

- $\epsilon_r = 4$, $\mu_r = 1$: $v = c/2 = 1.50\times10^8$ m/s, $\eta = \eta_0/2 = 188\ \Omega$ ($\approx60\pi$).
- The challenge wave $h$, at $10^8$ m/s, in a non-magnetic medium: $\epsilon_r = (c/v)^2 = 8.99\approx9$, $\eta = \mu_0v = 40\pi\approx126\ \Omega$.
- Polyethylene, $\epsilon_r = 2.25$: $v = c/1.5 = 2.00\times10^8$ m/s, $\eta = 251\ \Omega$.

**The same numbers on a cable.** [[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials|Lecture 15]] found $\mathcal{L}\mathcal{C} = \mu\epsilon$ for any two-conductor line in one medium, so $1/\sqrt{\mathcal{L}\mathcal{C}} = v$: a cable signal travels at the plane-wave speed of its filling. $\sqrt{\mathcal{L}/\mathcal{C}}$ is $\eta$ times geometry: $(\eta/2\pi)\ln(b/a)$ for a coax, $\eta\,d/W$ for parallel plates. The polyethylene coax of the [[problems/coax-inductance-and-the-lc-product|coax worked problem]]: $251\ \Omega\times\ln(3.5)/2\pi = 251\times0.199$, the 50 Ω found there — a coax guides a TEM wave. Unit 4 calls $\sqrt{\mathcal{L}/\mathcal{C}}$ the characteristic impedance.

## 8. Summary

- $\nabla^2\mathbf{E} = \mu\epsilon\,\partial_t^2\mathbf{E}$ needs the displacement current, constant $\mu,\epsilon$, $\rho = \mathbf{J} = 0$.
- $E_x = Af(t - z/v) + Bg(t + z/v)$, $H_y = (Af - Bg)/\eta$, $\mathbf{H} = \hat u\times\mathbf{E}/\eta$; $\eta_0\approx377\ \Omega$.
- $E(z,t) = E(0, t\mp z/v)$; matter: $v = c/\sqrt{\mu_r\epsilon_r}$, $\eta = \eta_0\sqrt{\mu_r/\epsilon_r}$.

Concept pages: [[concepts/wave-equation]] · [[concepts/plane-waves]] · [[concepts/intrinsic-impedance]] · [[concepts/displacement-current]] · [[concepts/faradays-law]] · [[concepts/maxwells-equations]].

> [!exam] On exams
> 1. **Direction and speed** from an argument (slide 24): slowness vs speed, term order.
> 2. **$\mathbf{H}$ from $\mathbf{E}$, or back**, including $y$-polarized and $-z$ waves; write the cross product out.
> 3. **Moving pulses**, as in SP18 Exam 2 #4 ([[problems/a-pulse-on-the-move|A pulse on the move]]).
> 4. **The derivation**, assumptions named, displacement current located.
> 5. **No $z$-polarized wave along $z$.**
> 6. **Constants**: $c\approx3\times10^8$ m/s $= 300$ m/µs, $\eta_0\approx120\pi\ \Omega$.
> 7. **$v$, $\eta$ in a dielectric**, or $\epsilon_r$ from a speed; slower than $c$ means matter, not loss.
>
> Current-sheet problems (SP18 Exam 2 #5) need Lecture 19's amplitude.

> [!tip] Practice this lecture
> [[practice/18-wave-equation-and-plane-waves|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/18-wave-equation-and-plane-waves#181-which-way-and-how-fast|18.1 Which way and how fast]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 18 (all of it, including the margin pulse plots). Shao, Lecture 18 slides: motivation (3), current sheet (4–11; Lecture 19 material in the notes, used here only for symmetry and sign), component equations (12–16), factoring (17–20), $H_y$ (21), $v_p = c$ (slides' $v_p$ = this site's $v$), $\eta_0$ (22), slides 24–26. This site's own: solutions to slides 24 and 26 (checked numerically), the assumption list, necessary-not-sufficient, the "why every solution" derivation, $\eta = \mu v$, the mirror rule, §7's numbers, all figures. Slips in the course material: see [[0-toolkit/04-errata-in-the-course-materials|errata]].
