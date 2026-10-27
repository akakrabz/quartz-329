---
title: "Lecture 15 — Inductance, magnetic energy, and the potentials"
description: "A loop's own current links Ψ = LI; the self-emf −L dI/dt is a rise, V = L dI/dt the circuit drop, a shorted coil decays with τ = L/R, and L follows from the chain I → H → B → Ψ (solenoid n²μ₀Aℓ, coax 𝓛 = (μ/2π)ln(b/a)), with energy ½LI² = ∫½μH² dV and 𝓛𝓒 = με for any two-conductor line. With time variation E = −∇Φ − ∂A/∂t, B = ∇×A, up to a gauge transformation."
tags: [lecture, magnetostatics]
lecture: 15
---

*Lecture 15 · course notes §15 · slides "Potentials" and "Inductance" · prev: [[2-magnetostatics/14-faradays-law-and-induced-emf|Lecture 14]] · next: [[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Lecture 16]] · practice: [[practice/15-inductance-and-magnetic-energy|12 problems]]*

> [!abstract] In one breath
> [[1-electrostatics/10-capacitance-and-conductance|Lecture 10]] made electrostatics a circuit element, $Q = CV$; here magnetostatics plus Faraday does the same: a loop links its *own* flux, $\Psi = LI$. Changing $I$ produces a self-emf $-L\,dI/dt$ — a rise in the direction of $I$, written in circuits as the drop $V = L\,dI/dt$. Shorted through a resistor the current decays with $\tau = L/R$, twin of $RC$. $L$ comes from the capacitance chain with letters changed: Ampère gives $\mathbf{H}$, $\mu$ gives $\mathbf{B}$, a surface integral gives $\Psi$. The energy $\tfrac12LI^2$ lives in the field at $\tfrac12\mu H^2$ per cubic metre, and for a coax or plates the per-metre inductance and capacitance multiply to $\mu\epsilon$ — the seed of Unit 4. With time variation $\mathbf{E}$ needs the pair $(\Phi,\mathbf{A})$, defined up to a gauge transformation.

## 1. Self-inductance

$\mathbf{B}\propto I$ (Biot–Savart is linear), so a coil's flux through its own surface is $\propto I$:

> [!key] Inductance
> $$
> \Psi = LI,\qquad L = \frac{\Psi}{I}\ \ge0\quad[\text{H} = \text{Wb/A}].
> $$
> $L$ depends on geometry and permeability only — twin of $C = Q/V$. For $N$ turns each linking the same single-turn flux $\Psi$, the $N$ emfs add: $\mathcal{E} = -N\,d\Psi/dt\equiv-L\,dI/dt$, so $L = N\Psi/I$ (other books: flux *linkage* $N\Psi$ over $I$). *Mutual* inductance, $M = \Psi_{\text{coil 1 due to }I_2}/I_2$, also in henries, is the transformer's parameter; the course names it and moves on (ECE 330 takes it up).

When $I$ changes, Faraday's law on the coil's own loop gives a **self-emf**

$$
\mathcal{E} = -\frac{d\Psi}{dt} = -L\frac{dI}{dt},
$$

a voltage *rise* around the coil in the direction of the current (the **back-emf**, as opposed to emfs from externally produced flux). Circuit courses state it from the other side:

> [!key] The inductor as a circuit element
> $$
> V = L\frac{dI}{dt}
> $$
> is the voltage **drop** across the inductor in the direction of $I$ (passive sign convention); $-L\,dI/dt$ is the equal and opposite *rise* Faraday supplies. For a resistive coil with no other source, KVL reads $RI = -L\,dI/dt$: rise matches drop. (A typed slide has the wrong sign; the circuit symbol's $+$/$-$ is right — [[0-toolkit/04-errata-in-the-course-materials|errata page]].)

## 2. The RL decay, and when I = ℰ/R was allowed

<!-- fig:rc-vs-rl -->

$RI = -L\,dI/dt$ gives $I(t) = I(0)e^{-t/\tau}$, $\tau = L/R$; the self-emf obeys the same equation, $R\mathcal{E} = -L\,d\mathcal{E}/dt$.

> [!example] Example 1 (course notes) — a coil discharging into itself
> An $N$-turn coil, $R = 1\ \Omega$, $L = 1\ \mu$H, carries 3 A at $t = 0$ and is then shorted. $RI = -L\,dI/dt \Rightarrow I(t) = 3e^{-10^6t}$ A: gone in microseconds; $N$ never enters once $L$ is given.

> [!intuition] Capacitor ↔ inductor
> $\tau = RC$ for the leaky capacitor ([[1-electrostatics/10-capacitance-and-conductance#6-conductance-the-leaky-capacitor|Lecture 10 §6]]) ↔ $\tau = L/R$. A large $C$ holds its voltage while slowly discharging — a slowly varying **voltage source**; a large $L$ holds its *current* — a slowly varying **current source**, maintaining whatever rise $-L\,dI/dt$ the circuit requires. (Interrupt a big inductor's current abruptly and $dI/dt\to\infty$: the spark across the switch is the inductor insisting.)

In general a resistive loop's current solves an ODE built from its total emf. [[2-magnetostatics/14-faradays-law-and-induced-emf|Lecture 14]]'s algebraic $I = \mathcal{E}/R$ is the special case where the self-emf $-L\,dI/dt$ is negligible next to the external emf — true for those small loops and modest rates (60 Hz generator: $L\,dI/dt\sim$ millivolts against 118 V).

## 3. Computing L: the Ampère chain

<!-- fig:inductance-recipes -->

> [!recipe] Inductance, five steps
> Assume $I$ → $\mathbf{H}$ by Ampère's law (or Biot–Savart) → $\mathbf{B} = \mu\mathbf{H}$ → $\Psi = \int_S\mathbf{B}\cdot d\mathbf{S}$ through the surface bounded by the current path (times $N$ for $N$ turns) → $L = N\Psi/I$. The assumed $I$ cancels, as $Q$ did for capacitance.

**Long solenoid.** $n$ turns per metre, cross-section $A$, length $\ell\gg$ radius (minor edge effects), $N = n\ell$ turns. From [[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential|Lecture 13]], $\mathbf{B} = \mu_0nI\hat z$ inside, so each turn links $\Psi = \mu_0nIA$ and

> [!key] Inductance of a long solenoid
> $$
> L = \frac{N\Psi}{I} = \frac{n\ell\cdot\mu_0nIA}{I} = n^2\mu_0A\ell = N^2\mu_0\frac{A}{\ell}.
> $$
> Quadratic in winding density: doubling the turns doubles the field *and* the number of turns linking it. ($n$ is per metre; a slide swaps $N$ and $n$.)

## 4. Energy: ½LI², and ½μH² per cubic metre

With a quasi-static current (size $\ll\lambda = c/f$, as for capacitors) the terminal voltage is $V = L\,dI/dt$ and the inductor absorbs

$$
P = VI = LI\frac{dI}{dt} = \frac{d}{dt}\Big(\tfrac12LI^2\Big),
$$

> [!key] Stored magnetic energy and its density
> $$
> W = \tfrac12LI^2 = \tfrac12(n^2\mu_0A\ell)I^2 = \frac{(\mu_0nI)^2}{2\mu_0}A\ell = \frac{B_z^2}{2\mu_0}A\ell = \tfrac12\mu_0H_z^2\cdot A\ell
> $$
> for the solenoid — field volume times
> $$
> w = \tfrac12\mu_0\,\mathbf{H}\cdot\mathbf{H} = \tfrac12\mathbf{B}\cdot\mathbf{H}\quad[\text{J/m}^3],
> $$
> taken, like $\tfrac12\epsilon E^2$, as the **energy density of the magnetic field** in general. In a medium $\mu_0\to\mu = (1+\chi_m)\mu_0$ in $L$, $W$ and $w$, as $\epsilon = (1+\chi_e)\epsilon_0$; Lecture 17 explains $\chi_m$. Poynting's theorem (Lecture 20) tracks the total $\tfrac12\epsilon E^2 + \tfrac12\mu H^2$.

Since $W = \int w\,dV\ge0$, $L = 2W/I^2\ge0$ — not an assumption.

## 5. Transmission-line geometries: 𝓛, 𝓒, and their product

<!-- fig:coax-l-and-c -->

**Shorted coax.** Inner radius $a$, outer inner radius $b$, length $\ell\gg b$, shorted at the far end: $I$ goes down the inner conductor and back along the inside of the outer one. Ampère for $a<r<b$: $B_\phi = \dfrac{\mu I}{2\pi r}$; for $r>b$ the currents cancel, $\mathbf{B} = 0$ — flux confined to the cable. The linked flux threads the rectangle $a<r<b$, $0<z<\ell$ (normal $\hat\phi$, along $\mathbf{B}$):

$$
\Psi = \int_S\mathbf{B}\cdot d\mathbf{S} = \ell\int_a^b\frac{\mu I}{2\pi r}dr = \frac{\mu\ell I}{2\pi}\ln\frac ba,
$$

> [!key] Coax and parallel-plate inductance per unit length
> $$
> \begin{gathered}
> L = \frac{\mu\ell}{2\pi}\ln\frac ba,\qquad \mathcal{L}\equiv\frac L\ell = \frac{\mu}{2\pi}\ln\frac ba\ [\text{H/m}]\\[4pt]
> \text{vs.}\qquad \mathcal{C} = \frac{2\pi\epsilon}{\ln(b/a)}\ [\text{F/m}]\ (\text{Lecture 10}).
> \end{gathered}
> $$
> Shorted parallel plates, width $W$, separation $d$: surface current $I/W$ on each plate makes $H = I/W$ between them (the sheet rule, twice), so $\Psi = \mu\dfrac IW d\ell$ and $\mathcal{L} = \mu\dfrac dW$, beside $\mathcal{C} = \epsilon\dfrac Wd$. In both, the geometric factor of $\mathcal{L}$ is the **arithmetic inverse** of that of $\mathcal{C}$; $\mathcal{L}\propto\mu$, $\mathcal{C}\propto\epsilon$ (the notes swap them: errata).

This is the external inductance (flux inside the inner conductor ignored) — the right idealization at the frequencies where cables matter.

> [!key] The line parameters, and what they multiply to
> | | parallel plates | coax |
> |---|---|---|
> | $\mathcal{C}$ | $\epsilon W/d$ | $2\pi\epsilon/\ln(b/a)$ |
> | $\mathcal{G}$ | $\sigma W/d$ | $2\pi\sigma/\ln(b/a)$ |
> | $\mathcal{L}$ | $\mu d/W$ | $(\mu/2\pi)\ln(b/a)$ |
>
> $$
> \mathcal{L}\mathcal{C} = \mu\epsilon,\qquad \frac{\mathcal{G}}{\mathcal{C}} = \frac\sigma\epsilon,\qquad \frac{1}{\sqrt{\mathcal{L}\mathcal{C}}} = \frac{1}{\sqrt{\mu\epsilon}}\ (= c\ \text{in vacuum}).
> $$
> Both relations hold for *any* two-conductor line filled with one homogeneous medium: all three parameters share one geometric factor. The slides' $v_p = 1/\sqrt{\mathcal{LC}}$ (beside $c = 1/\sqrt{\mu_0\epsilon_0}$) is the signal speed on the line, where Unit 4 begins.

Slide challenge: increase the plate separation $d$ and $\mathcal{L}$ rises, $\mathcal{C}$ falls, $\mathcal{G}$ falls (answer (c)) — the same current links more flux, the same charge gives a bigger voltage drop. [[problems/coax-inductance-and-the-lc-product]] runs the table for a coax with numbers.

## 6. The potentials when fields vary in time

In statics $\mathbf{E} = -\nabla V$ because $\nabla\times\mathbf{E} = 0$; Faraday gives $\mathbf{E}$ a curl, so no scalar potential alone suffices. $\nabla\cdot\mathbf{B} = 0$ still holds, so $\mathbf{B} = \nabla\times\mathbf{A}$, and Faraday's law becomes

$$
\nabla\times\mathbf{E} = -\frac{\partial}{\partial t}\nabla\times\mathbf{A}\quad\Rightarrow\quad\nabla\times\Big(\mathbf{E}+\frac{\partial\mathbf{A}}{\partial t}\Big) = 0 .
$$

The bracket is curl-free, hence a gradient:

> [!key] Fields from potentials, in general
> $$
> \mathbf{B} = \nabla\times\mathbf{A},\qquad \mathbf{E} = -\nabla\Phi - \frac{\partial\mathbf{A}}{\partial t}.
> $$
> (The slides' $\Phi$ is the notes' $V$.) Four potential components replace six field components, and the two homogeneous Maxwell equations ($\nabla\cdot\mathbf{B} = 0$, Faraday) hold identically. $-\partial\mathbf{A}/\partial t$ is the induced, circulating part of $\mathbf{E}$ — the part a voltmeter path integral cannot ignore. In the static limit $\mathbf{E} = -\nabla\Phi$, and Gauss's law gives back Poisson's equation.

**Gauge freedom.** For any scalar $\lambda(\mathbf{r},t)$,

$$
\mathbf{A}' = \mathbf{A} + \nabla\lambda,\qquad \Phi' = \Phi - \frac{\partial\lambda}{\partial t}
$$

give the same $\mathbf{B}$ ($\nabla\times\nabla\lambda = 0$) and the same $\mathbf{E}$ ($-\nabla\partial_t\lambda$ from $\Phi'$ cancels $-\partial_t\nabla\lambda$ from $\mathbf{A}'$) — answer (b) of the slide's challenge. The Coulomb gauge $\nabla\cdot\mathbf{A} = 0$ of [[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential#5-the-vector-potential|Lecture 13]] is one way to spend the freedom; the wave-friendly Lorenz gauge appears with radiation.

## 7. Summary

- $\Psi = LI$, $L = N\Psi/I$ [H]; self-emf $-L\,dI/dt$ (rise), circuit drop $V = L\,dI/dt$; $M$ for two coils.
- Shorted coil: $RI = -L\,dI/dt$, $I = I(0)e^{-t/\tau}$, $\tau = L/R$; large $L$ ≈ current source; $I = \mathcal{E}/R$ needs $L\,dI/dt\ll\mathcal{E}$.
- Chain: $I\to\mathbf{H}\to\mathbf{B}\to\Psi\to L$. Solenoid $L = n^2\mu_0A\ell = N^2\mu_0A/\ell$.
- $W = \tfrac12LI^2$; $w = \tfrac12\mu\mathbf{H}\cdot\mathbf{H}$ [J/m³]; $\mu = (1+\chi_m)\mu_0$.
- Coax $\mathcal{L} = (\mu/2\pi)\ln(b/a)$, plates $\mathcal{L} = \mu d/W$; $\mathcal{LC} = \mu\epsilon$, $\mathcal{G}/\mathcal{C} = \sigma/\epsilon$, $1/\sqrt{\mathcal{LC}} = 1/\sqrt{\mu\epsilon}$.
- $\mathbf{B} = \nabla\times\mathbf{A}$, $\mathbf{E} = -\nabla\Phi - \partial\mathbf{A}/\partial t$; gauge: $\mathbf{A}+\nabla\lambda$, $\Phi - \partial_t\lambda$.

Concept pages: [[concepts/inductance]] · [[concepts/magnetic-energy]] · [[concepts/vector-potential]] · [[concepts/capacitance]].

> [!exam] On exams
> "Find the inductance (per unit length) of …" is the magnetic twin of Exam 1 problem 4, graded on the same chain: $\mathbf{H}$ from Ampère with the right loop, $\mathbf{B} = \mu\mathbf{H}$ with the *medium's* $\mu$, flux over the surface bounded by the current path (for a coax, the $r$–$z$ rectangle, not a circle), units H or H/m, and $N$ counted once in the field and again in the turns linked. Energy questions want $\tfrac12LI^2$ or $\int\tfrac12\mu H^2dV$, shown to agree. Sign questions want $V = L\,dI/dt$ as a drop in the direction of $I$. And $\mathcal{LC} = \mu\epsilon$: if your coax numbers fail it, the chain has an error.

> [!tip] Practice this lecture
> [[practice/15-inductance-and-magnetic-energy|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/15-inductance-and-magnetic-energy#151-a-long-solenoid-by-the-numbers|15.1 A long solenoid by the numbers]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 15 (self-inductance, self-emf as a rise; back-emf; $RL$ decay, current-source remark; $N$ turns; Example 1; solenoid; $w = \tfrac12\mu_0\mathbf{H}\cdot\mathbf{H}$, $\mu = (1+\chi_m)\mu_0$; shorted coax and plates; inverse geometric factors). Shao, Lecture 15 slides (potentials and the gauge challenge; $L = \Psi/I$ beside $C = Q/V$; circuit symbol; mutual inductance; five-step recipe; $\mathcal{C}$, $\mathcal{G}$, $\mathcal{L}$ table with $\mathcal{LC} = \mu\epsilon$ — only implied in the notes; $v_p = 1/\sqrt{\mathcal{LC}}$; plate-separation challenge). Slips in the course material: see [[0-toolkit/04-errata-in-the-course-materials|errata]].
