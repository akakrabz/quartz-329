---
title: "Worked problem — The sliding bar, and what a voltmeter reads"
description: "Part 1: a bar sliding on rails through a magnetic field — motional emf, current, the lab electric field inside the bar and the load, the open-circuit case, and the mechanical power that pays for the I²R. Part 2: a loop with two resistors in a changing flux, and why voltmeters on the same two nodes read different values."
tags: [problem, magnetostatics]
---

*Problem · re-parameterized from course notes Lecture 14, Examples 4 and 6 · uses [[2-magnetostatics/14-faradays-law-and-induced-emf|Lecture 14]] · concepts: [[concepts/electromotive-force]], [[concepts/faradays-law]], [[concepts/lorentz-force]]*

> [!question] Problem, part 1 — the bar
> Two horizontal, perfectly conducting rails $\ell = 0.5$ m apart lie along $x$ and are joined at their left end ($x = 0$) by a load resistor $R_2 = 0.6\ \Omega$. A bar of resistance $R_1 = 0.2\ \Omega$ slides along the rails at $\mathbf{v} = 6\hat x$ m/s. A uniform $\mathbf{B} = 0.8$ T points *into* the page ($-\hat z$; $x$ to the right, $y$ up).
> (a) Find the emf around the loop and the current, with its direction. (b) Find the lab-frame electric field inside the bar and inside the load. (c) Repeat (b) for an open-circuit load ($R_2\to\infty$). (d) What force must be applied to keep the bar moving, and what mechanical power does it deliver? Compare with the electrical dissipation.

## (a) EMF and current

**Flux route.** Take the loop counter-clockwise (seen from the front): up the bar ($+\hat y$), left along the top rail, down through $R_2$, right along the bottom rail. Right-hand rule: $d\mathbf{S} = +\hat z$ — *out* of the page, against $\mathbf{B}$. The loop's area is $\ell x_{\text{bar}} = \ell vt$, so $\Psi = \mathbf{B}\cdot\hat z\,\ell vt = -B\ell vt = -0.8\times0.5\times6\,t = -2.4\,t$ Wb and

$$
\mathcal{E} = -\frac{d\Psi}{dt} = +2.4\ \text{V}\quad(\text{counter-clockwise}).
$$

**Motional route.** Only the bar moves: $\mathbf{v}\times\mathbf{B} = 6\hat x\times(-0.8\hat z) = +4.8\,\hat y$ V/m, along the bar, pushing positive charge toward the top rail. Times the length: $4.8\times0.5 = 2.4$ V ✓.

**Current.** $I = \mathcal{E}/(R_1+R_2) = 2.4/0.8 = 3$ A, flowing up the bar, left along the top rail, down through the load.

> [!key] Answer (a)
> $\mathcal{E} = vB\ell = 2.4$ V; $I = 3$ A counter-clockwise (up the bar). The bar is a battery of 2.4 V with internal resistance $0.2\ \Omega$ and its $+$ terminal at the top.

## (b) The electric field in the bar and in the load

$\mathbf{B}$ is constant in time, so $\nabla\times\mathbf{E} = -\partial\mathbf{B}/\partial t = 0$: the lab $\mathbf{E}$ is curl-free (the quasi-static Coulomb field of the charges on the rails) and $\oint\mathbf{E}\cdot d\mathbf{l} = 0$. The rails are perfect conductors ($\mathbf{E}\cdot d\mathbf{l} = 0$ along them), so the $\mathbf{E}$-integrals up the bar and down the load must cancel: $E_y$ **is the same in both**.

*Load.* The current flows *down* ($-\hat y$) through $R_2$ with a drop $IR_2 = 1.8$ V over $0.5$ m, so $\mathbf{E} = -3.6\,\hat y$ V/m (pointing down, driving the downward current).

*Bar.* The drop across the bar's own resistance, in the direction of the current ($+\hat y$), is $IR_1 = 0.6$ V, and that drop is produced by the *total* force per charge, $\mathbf{E}+\mathbf{v}\times\mathbf{B}$: $(E_y + 4.8)\times0.5 = 0.6\Rightarrow E_y = -3.6$ V/m ✓ — the same field, as it had to be.

> [!key] Answer (b)
> $\mathbf{E} = -3.6\,\hat y$ V/m in the load **and** in the bar. In the bar the $\mathbf{v}\times\mathbf{B}$ term ($+4.8$ V/m) overpowers it, leaving $1.2$ V/m to drive the current through $R_1$; in the load there is no $\mathbf{v}\times\mathbf{B}$ and the $-3.6$ V/m drives the current alone. The static field is made by charge that has accumulated on the rails.

## (c) Open circuit

$I = 0$. In the bar the net force per charge must vanish: $\mathbf{E} = -\mathbf{v}\times\mathbf{B} = -4.8\,\hat y$ V/m. The same field exists across the open gap at $x = 0$ (curl-free again), where the whole emf appears: $4.8\times0.5 = 2.4$ V between the rails.

> [!key] Answer (c)
> $E_y = -4.8$ V/m everywhere between the rails; the bar's 2.4 V appears across the open terminals — an unloaded battery reads its full emf.

## (d) Force and power

The current in the bar sits in the field: $\mathbf{F} = I\boldsymbol{\ell}\times\mathbf{B} = 3\times(0.5\hat y)\times(-0.8\hat z) = -1.2\,\hat x$ N — a drag opposing the motion (Lenz, as a force). To keep $v$ constant someone must push with $+1.2$ N, delivering $P = Fv = 1.2\times6 = 7.2$ W. Electrical dissipation: $I^2(R_1+R_2) = 9\times0.8 = 7.2$ W ✓.

> [!key] Answer (d)
> $1.2$ N, $7.2$ W — exactly the $I^2R$ heat. The magnetic field does no work; it only converts the pusher's work into electrical energy.

> [!question] Problem, part 2 — the voltmeter
> A rectangular loop of $0.4\ \text{m}\times0.5$ m ($0.2$ m²) in the $xy$-plane has $R_1 = 3\ \Omega$ on its left side and $R_2 = 2\ \Omega$ on its right side (the top and bottom sides are perfect conductors). Node A is the top-right corner, node B the bottom-left corner. The field is $\mathbf{B} = (6 - 10t)\,\hat z$ T.
> (e) Find the emf and the current. (f) What does an ideal voltmeter read, from A to B, if its leads run (i) along the $R_1$ side, (ii) along the $R_2$ side, (iii) along the diagonal?

## (e) EMF and current

Counter-clockwise from $+z$: $d\mathbf{S} = \hat z$, $\Psi = 0.2\,(6-10t)$ Wb, $\mathcal{E} = -d\Psi/dt = +2$ V. The $+\hat z$ flux is decreasing, so the induced current is counter-clockwise (making $+\hat z$ field inside — Lenz ✓): $I = 2/(3+2) = 0.4$ A, flowing up the right side ($R_2$), left along the top, down the left side ($R_1$), right along the bottom.

> [!key] Answer (e)
> $\mathcal{E} = 2$ V, $I = 0.4$ A counter-clockwise.

## (f) Three voltmeters, three readings

An ideal voltmeter (no current through it) reads $\int_{\text{A}}^{\text{B}}\mathbf{E}\cdot d\mathbf{l}$ *along its own leads*.

- (i) Leads along the top edge and down the $R_1$ side: this path runs **with** the current; the only drop is in $R_1$: $V_{\text{AB}} = +IR_1 = +1.2$ V.
- (ii) Leads down the $R_2$ side and along the bottom: this path runs **against** the current: $V_{\text{AB}} = -IR_2 = -0.8$ V.
- (iii) Leads along the diagonal A→B. Faraday's law for the triangle formed by the diagonal and the $R_2$ side (half the area, so an emf of $1$ V): going counter-clockwise around it — up through $R_2$ (with the current, drop $+0.8$ V) then along the diagonal from A to B (drop $V_{\text{AB}}$) — the drops must sum to the triangle's emf: $0.8 + V_{\text{AB}} = 1\Rightarrow V_{\text{AB}} = +0.2$ V. (The other triangle gives $1.2 - V_{\text{AB}} = 1$ — same answer.)

> [!key] Answer (f)
> $+1.2$ V, $-0.8$ V, $+0.2$ V. Readings (i) and (ii) differ by $2$ V — the emf of the loop the two lead paths enclose. In general, reading $= V_{(\text{i})} - \mathcal{E}\times(\text{fraction of the loop area between the lead path and the }R_1\text{ path})$: the diagonal, enclosing half, reads $1.2 - 1 = 0.2$ V.

> [!trap] Where this problem loses points
> - Part 1: $d\mathbf{S}$ not tied to the stated sense of the loop; forgetting that the rails contribute nothing to $\oint\mathbf{E}\cdot d\mathbf{l}$; writing the bar's field as $+\mathbf{v}\times\mathbf{B}$ (it is the *total* force per charge that produces $IR_1$).
> - Part 1(d): claiming the magnetic force does the work. It does not; it is the pusher's $Fv$ that becomes $I^2R$.
> - Part 2: saying "the voltage across $R_2$ is $0.8$ V" without a sign and a path. From A to B along $R_2$ the reading is $-0.8$ V, because that path runs against the current. "The voltage between A and B" does not exist here; the voltage of each *path* does.
