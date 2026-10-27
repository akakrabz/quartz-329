---
title: "Worked problem — EMF of a loop moving away from a line current"
description: "A rectangular loop recedes from a long straight current. The emf by the flux rule and by the motional integral ∮(v×B)·dl, the direction of the induced current by Lenz, numbers, and the case that trips people: moving parallel to the wire gives no emf even though v×B is not zero."
tags: [problem, magnetostatics]
---

*Problem · re-parameterized from course notes Lecture 14, Example 2 · uses [[2-magnetostatics/14-faradays-law-and-induced-emf|Lecture 14]] and [[2-magnetostatics/12-magnetic-force-biot-savart-and-amperes-law|Lecture 12]] · concepts: [[concepts/faradays-law]], [[concepts/magnetic-flux]], [[concepts/electromotive-force]]*

> [!question] Problem
> A long straight wire along the $x$ axis carries $I = 5$ A in the $+\hat x$ direction. A rectangular loop in the $xy$-plane has sides $a = 0.5$ m (parallel to $x$) and $b = 0.3$ m (parallel to $y$); its near edge is at $y_1(t) = 0.2\ \text{m} + vt$ with $v = 4$ m/s, so the loop moves away from the wire. Take the loop counter-clockwise when viewed from $+z$, and let its resistance be $R = 0.01\ \Omega$.
> (a) Find the flux $\Psi(t)$ linking the loop. (b) Find the emf $\mathcal{E}(t)$ from the flux rule, and evaluate it at $t = 0$. (c) Recompute $\mathcal{E}$ as $\oint(\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l}$. (d) Give the direction and magnitude of the induced current at $t = 0$, and check it against Lenz's rule. (e) Suppose instead the loop moves parallel to the wire, $\mathbf{v} = 4\hat x$ m/s. What is the emf?

## (a) The flux

**Field.** A current along $+\hat x$ makes $\mathbf{B} = \dfrac{\mu_0I}{2\pi r}\hat\phi$ with $r$, $\hat\phi$ cylindrical *about the $x$ axis*. In the $xy$-plane at $y>0$ the right-hand rule (thumb along $+\hat x$) gives $\hat\phi = +\hat z$ and $r = y$: $\mathbf{B} = \dfrac{\mu_0I}{2\pi y}\hat z$.

**Orientation.** Counter-clockwise from $+z$ ⟹ $d\mathbf{S} = \hat z\,dx\,dy$. The field is uniform along $x$, so the $x$ integral is just the width $a$:

$$
\Psi(t) = \int_S\mathbf{B}\cdot d\mathbf{S} = a\int_{y_1}^{y_1+b}\frac{\mu_0I}{2\pi y}\,dy = \frac{\mu_0Ia}{2\pi}\ln\frac{y_1+b}{y_1},
$$

with $y_1 = 0.2+4t$ m.

> [!key] Answer (a)
> $\Psi(t) = \dfrac{\mu_0Ia}{2\pi}\ln\dfrac{y_1(t)+b}{y_1(t)}$; at $t = 0$, $\Psi = (5\times10^{-7})\ln2.5 = 4.6\times10^{-7}$ Wb. It is positive (field along $+\hat z$, $d\mathbf{S}$ along $+\hat z$) and it decreases as the loop recedes.

## (b) EMF by the flux rule

Differentiate with $dy_1/dt = v$:

$$
\mathcal{E} = -\frac{d\Psi}{dt} = -\frac{\mu_0Ia}{2\pi}\Big(\frac{v}{y_1+b} - \frac{v}{y_1}\Big) = \frac{\mu_0Iav}{2\pi}\Big(\frac1{y_1} - \frac1{y_1+b}\Big).
$$

At $t = 0$: $\dfrac{\mu_0Iav}{2\pi} = 2\times10^{-7}\times5\times0.5\times4 = 2\times10^{-6}$ V·m, and $\dfrac1{0.2} - \dfrac1{0.5} = 5 - 2 = 3\ \text{m}^{-1}$.

> [!key] Answer (b)
> $\mathcal{E}(0) = 6\ \mu$V, positive — i.e. a drive in the counter-clockwise sense. It decays as the loop gets further away (both $1/y$ terms shrink and their difference shrinks faster).

## (c) EMF by the motional integral

$\mathbf{v}\times\mathbf{B} = 4\hat y\times\dfrac{\mu_0I}{2\pi y}\hat z = \dfrac{4\mu_0I}{2\pi y}\hat x$: it points along $\hat x$, so only the two edges *parallel to the wire* contribute; on the edges parallel to $y$, $(\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l} = 0$. Going counter-clockwise, the near edge ($y = y_1$) is traversed in $+\hat x$ and the far edge ($y = y_1+b$) in $-\hat x$:

$$
\mathcal{E} = \frac{4\mu_0I}{2\pi y_1}\,a - \frac{4\mu_0I}{2\pi(y_1+b)}\,a = \frac{\mu_0Iav}{2\pi}\Big(\frac1{y_1}-\frac1{y_1+b}\Big)\quad\checkmark
$$

> [!key] Answer (c)
> The same expression as (b), term for term: the near edge, in the stronger field, wins. This is Lecture 14's point — for a loop moving in a *static* field the whole emf is motional, and $-d\Psi/dt$ is just the bookkeeping of $\oint(\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l}$.

## (d) The current, and Lenz

$I_{\text{loop}} = \mathcal{E}/R = 6\ \mu\text{V}/0.01\ \Omega = 0.6$ mA, counter-clockwise (the sense in which $\mathcal{E}$ was computed and found positive).

**Lenz check.** The linked flux is $+\hat z$ and *decreasing*. A counter-clockwise current (seen from $+z$) produces a $+\hat z$ field inside the loop — it tries to restore the flux that is being lost. ✓ Equivalently, the force on the near edge (current $+\hat x$ in a $+\hat z$ field) is $I\,d\mathbf{l}\times\mathbf{B}\propto\hat x\times\hat z = -\hat y$: toward the wire, a drag opposing the motion — which is where the dissipated $I^2R$ comes from.

> [!key] Answer (d)
> $0.6$ mA counter-clockwise at $t = 0$; Lenz ✓ (the induced field props up the falling flux; the magnetic force on the loop opposes its motion).

## (e) Moving parallel to the wire

With $\mathbf{v} = 4\hat x$, the loop's position relative to the wire never changes, so $\Psi$ is constant and $\mathcal{E} = -d\Psi/dt = 0$. Yet $\mathbf{v}\times\mathbf{B} = 4\hat x\times\dfrac{\mu_0I}{2\pi y}\hat z = -\dfrac{4\mu_0I}{2\pi y}\hat y\neq0$ on every edge. It is along $\hat y$, so it does work on the two edges parallel to $y$ — but those edges sit at $x$-positions that differ by $a$ and see the *same* $y$-dependence; one is traversed in $+\hat y$ and the other in $-\hat y$, and their contributions cancel exactly.

> [!key] Answer (e)
> $\mathcal{E} = 0$. A nonzero $\mathbf{v}\times\mathbf{B}$ is not an emf; only its *circulation* is. Motion through a field that is uniform along the direction of motion links no new flux.

> [!trap] Where this problem loses points
> - Taking $r$ and $\hat\phi$ about the $z$ axis out of habit; here the wire is the $x$ axis, and in the loop's plane $\mathbf{B}$ is along $\hat z$.
> - Not tying $d\mathbf{S}$ to the stated sense of the loop (the sign of $\mathcal{E}$ is meaningless without it).
> - Forgetting the loop width $a$ in the flux (the field does not depend on $x$, but the area does).
> - Including the $y$-parallel edges in the motional integral in part (c): $(\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l} = 0$ there.
> - Reporting a current without a direction, or a direction without the Lenz sentence that justifies it.
