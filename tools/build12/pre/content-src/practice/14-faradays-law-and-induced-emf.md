---
title: "Practice — Lecture 14: Faraday's law and induced emf"
description: "12 practice problems (5 easy, 3 medium, 4 hard) on flux through tilted loops, emf from a changing field, Lenz directions, motional emf of sliding bars, rotating rods and generator coils, loops crossing field regions, the induced field around a solenoid, magnetic braking and voltmeter readings in a changing flux, each with a folded hint and a worked solution."
tags: [practice, magnetostatics]
lecture: 14
---

*Practice for [[2-magnetostatics/14-faradays-law-and-induced-emf|Lecture 14]] · concepts: [[concepts/faradays-law]] · [[concepts/electromotive-force]] · [[concepts/magnetic-flux]] · [[concepts/lorentz-force]] · all practice: [[practice/index|hub]] · by difficulty: [[practice/easy|easy]] · [[practice/medium|medium]] · [[practice/hard|hard]] · [[practice/topics|by topic]]*

Work each problem on paper first. Open the **hint** only when stuck, and the **solution** only after you have an answer you would hand in. Every answer here has been checked numerically.

## Easy

### 14.1 Flux through a tilted loop

> [!easy] Easy · magnetic flux · Faraday's law · Lenz
> A square loop of wire, 20 cm on a side, has its corners at $(0,0,0)$, $(0.2,0,0)$, $(0.2,\,0.1,\,0.1\sqrt3)$ and $(0,\,0.1,\,0.1\sqrt3)$ m, and the path $C$ visits them in that order. The loop has resistance $0.5\ \Omega$ and sits in the uniform field $\mathbf{B} = (0.8-2t)\,\hat{z}$ T ($t$ in seconds).
> (a) Find the unit normal $\hat{n}$ tied to $C$ by the right-hand rule, and the angle between the loop and the $xy$-plane.
> (b) Find the flux $\Psi(t)$ through the loop.
> (c) Find the emf around $C$ and the induced current. Does the current flow along $C$ or against it?
>
> *Source: original.*

> [!hint]- Hint
> $d\mathbf{S} = \hat{n}\,dS$, so only the component of $\mathbf{B}$ along $\hat{n}$ counts. Build $\hat{n}$ from the cross product of two consecutive edges, taken in the order $C$ visits them.

> [!solution]- Solution
> (a) Two consecutive edges of $C$ are $\mathbf{a} = (0.2,\,0,\,0)$ m and $\mathbf{b} = (0,\,0.1,\,0.1\sqrt3)$ m: each is 0.2 m long, and they are perpendicular. Their cross product is the area vector, already oriented by the right-hand rule:
> $$
> \mathbf{a}\times\mathbf{b} = (0,\,-0.02\sqrt3,\,0.02)\ \text{m}^2,\qquad \lvert\mathbf{a}\times\mathbf{b}\rvert = 0.04\ \text{m}^2,\qquad \hat{n} = \Big(0,\,-\frac{\sqrt3}{2},\,\frac12\Big).
> $$
> Since $\hat{n}\cdot\hat{z} = \tfrac12$, the normal makes $60^\circ$ with $\hat{z}$: the loop is tilted $60^\circ$ from the $xy$-plane.
>
> (b) $\mathbf{B}$ is uniform, so the flux integral is a dot product:
> $$
> \Psi = \mathbf{B}\cdot\hat{n}\,A = (0.8-2t)\cdot\tfrac12\cdot0.04 = (0.8-2t)(0.02) = 0.016-0.04t\ \text{Wb}.
> $$
> (c) $\mathcal{E} = -d\Psi/dt = +0.04$ V $= 40$ mV, and $I = \mathcal{E}/R = 0.08$ A $= 80$ mA. Both are positive, so the current flows **along** $C$.
>
> **Lenz:** $B_z$ falls at 2 T/s, so the flux along $\hat{n}$ (which has a $+z$ component) falls. The induced current must prop it up with a field along $+\hat{n}$ inside the loop, and by the right-hand rule that is a current along $C$ ✓.
>
> **Check:** only $B_z$ is nonzero, so only the loop's shadow on the $xy$-plane counts: the rectangle $0\le x\le0.2$, $0\le y\le0.1$ m, of area 0.02 m² — exactly the $z$ component of $\mathbf{a}\times\mathbf{b}$. And any surface spanning $C$ gives the same flux ($\nabla\cdot\mathbf{B} = 0$): a tent of four triangles over the rim also gives 0.012 Wb at $t = 0.1$ s.
>
> **Watch out:** using the full area 0.04 m² instead of its projection doubles every answer.
>
> **Answer.** $\hat{n} = (0,-\sqrt3/2,1/2)$, tilt $60^\circ$; $\Psi = 0.016-0.04t$ Wb; $\mathcal{E} = 40$ mV and $I = 80$ mA, both along $C$.

### 14.2 Current from a ramping field

> [!easy] Easy · multiple choice · Faraday's law
> A rectangular loop of wire, 20 cm by 30 cm, lies in the plane $z = 0$ and has a total resistance of $3\ \Omega$. A uniform field $\mathbf{B} = (0.7-5t)\,\hat{z}$ T ($t$ in seconds) passes through it. The induced current is:
>
> (a) 100 mA, clockwise seen from $+z$
>
> (b) 100 mA, counter-clockwise seen from $+z$, at all times
>
> (c) 100 mA, counter-clockwise seen from $+z$ until $B_z$ reverses at $t = 0.14$ s, then clockwise
>
> (d) 1 A, counter-clockwise seen from $+z$
>
> (e) zero, because a uniform field cannot make an electric field circulate
>
> *Source: SP18 Exam 2 #1(ii) style, new numbers, direction added.*

> [!hint]- Hint
> Only $dB_z/dt$ enters the emf, not $B_z$ itself. And convert the area carefully: how many cm² are in 1 m²?

> [!solution]- Solution
> **(b).** Take $C$ counter-clockwise seen from $+z$, so $d\mathbf{S} = \hat{z}\,dS$ and $\Psi = B_zA$ with $A = 0.2\times0.3 = 0.06$ m² (600 cm²). Then
> $$
> \mathcal{E} = -\frac{d\Psi}{dt} = -A\frac{dB_z}{dt} = -(0.06)(-5) = +0.3\ \text{V},\qquad I = \frac{0.3\ \text{V}}{3\ \Omega} = 0.1\ \text{A} = 100\ \text{mA}.
> $$
> Positive means along $C$: counter-clockwise seen from $+z$. In words (Lenz): $B_z$ is falling, so the $+z$ flux falls; the induced current props it up with a $+z$ field inside the loop, and that takes a counter-clockwise current.
>
> - (a) is the classic Lenz slip "the induced field opposes $\mathbf{B}$". It opposes the *change* in the flux.
> - (c) The slope $dB_z/dt = -5$ T/s never changes, so neither does the emf. After $t = 0.14$ s the field points along $-z$ and *grows*; opposing that growth again takes a $+z$ field inside, i.e. the same counter-clockwise current. (Starting from $B_z = +0.7$ T or from $-0.7$ T makes no difference either: $\Psi(0) = \pm0.042$ Wb, but $\mathcal{E} = +0.3$ V in both cases.)
> - (d) uses 600 cm² $= 0.6$ m², wrong by a factor of 10 (there are $10^4$ cm² in a m²), and gets 1 A. The opposite slip, 0.006 m², gives 10 mA.
> - (e) Faraday: $(\nabla\times\mathbf{E})_z = -\partial B_z/\partial t = +5$ T/s $\ne0$. A changing field, uniform or not, always makes $\mathbf{E}$ circulate.
>
> **Answer.** (b): 100 mA, counter-clockwise seen from $+z$, for as long as the ramp lasts.

### 14.3 Magnet pulled up through a ring

> [!easy] Easy · multiple choice · Lenz
> A conducting ring lies in the plane $z = 0$, centred on the $z$ axis. A bar magnet lies on the $z$ axis below the ring with its **north pole pointing up** ($+z$). The magnet is pulled straight up along $+z$ at constant speed, passes through the ring and keeps going. Seen from above (from $+z$), the induced current in the ring is:
>
> (a) counter-clockwise while the magnet approaches, clockwise after it has passed through
>
> (b) clockwise while the magnet approaches, counter-clockwise after it has passed through
>
> (c) clockwise throughout
>
> (d) counter-clockwise throughout
>
> (e) zero, because the magnet moves at constant speed
>
> *Source: SP18 Exam 2 #1(iii) style, reversed (north pole up, magnet pulled up instead of dropped).*

> [!hint]- Hint
> Near its axis, a bar magnet's field leaves the north pole and returns into the south pole, so on the axis it points the same way, $+z$ here, both above and below the magnet. What does the $+z$ flux through the ring do before and after the magnet passes?

> [!solution]- Solution
> **(b).** With the north pole up, the magnet's field on and near its axis points along $+z$ on both sides of the magnet, so the ring's flux is along $+z$ the whole time. It grows while the magnet approaches and shrinks after the magnet has passed.
>
> - **Approaching** (magnet below the ring, moving up): the $+z$ flux grows. The induced current opposes the growth with a $-z$ field inside the ring: **clockwise** seen from $+z$.
> - **Receding** (magnet above the ring, moving away): the $+z$ flux shrinks. The induced current props it up with a $+z$ field: **counter-clockwise** seen from $+z$.
>
> The flux peaks as the magnet passes through the plane of the ring, and that is where the current reverses.
>
> - (a) is what happens in the exam's original set-up, a magnet falling with its north pole *down*: then the ring's flux is along $-z$, and the same reasoning flips both senses.
> - (c), (d): the flux first grows and then shrinks, so the current must reverse.
> - (e): constant speed does not mean constant flux. The ring sits in the magnet's nonuniform field, and the flux changes as the magnet moves.
>
> **Check (forces):** a clockwise current makes the ring a small magnet with its north face *down*, facing the approaching north pole: they repel, and the approach is resisted. After the pass, the counter-clockwise ring has its north face *up*, attracting the receding south pole at the magnet's bottom: the escape is resisted. In both phases the ring is pushed along $+z$ and the magnet is held back — Lenz's rule in the language of forces. A numerical model (a dipole pulled through a 5 cm ring) gives exactly these signs.
>
> **Answer.** (b): clockwise seen from $+z$ while the magnet approaches, counter-clockwise after it has passed through.

### 14.4 Lenz's rule, true or false

> [!easy] Easy · true or false · Lenz
> True or false? Every loop lies in the plane $z = 0$, and "clockwise" means clockwise seen from $+z$.
>
> (a) A circular loop of radius 10 cm, centred on the $z$ axis in the constant field $\mathbf{B} = 0.5\,\hat{z}$ T, is being shrunk: its radius decreases at 2 cm/s. The induced current is counter-clockwise.
>
> (b) A square loop of side 30 cm moves at $\mathbf{v} = 2\hat{x}$ m/s through the same uniform, constant field. Because $\mathbf{v}\times\mathbf{B}\ne0$ on its sides, a current is induced.
>
> (c) A fixed circular loop of radius 10 cm, centred on the $z$ axis, sits in $\mathbf{B} = -0.5\,e^{-t/2}\,\hat{z}$ T ($t$ in seconds). The induced current is clockwise.
>
> (d) If the loop of (c) is cut by a narrow gap, its emf becomes zero.
>
> (e) The magnetic field of an induced current always points opposite to the applied field.
>
> *Source: original.*

> [!hint]- Hint
> For each loop, first say what the flux is doing — along $+z$ or $-z$, growing or shrinking — and only then ask which way a current must circulate to fight that change.

> [!solution]- Solution
> (a) **True.** $\Psi = \pi r^2B$ along $+z$ shrinks with the loop. The induced current props it up with a $+z$ field inside: counter-clockwise. In numbers, $\mathcal{E} = -\frac{d}{dt}(\pi r^2B) = -2\pi rB\,\frac{dr}{dt} = 2\pi(0.1)(0.5)(0.02)\approx6.28$ mV at the start, positive (counter-clockwise). Motional check: the wire moves inward, $\mathbf{v} = -0.02\,\hat{r}$ m/s, so $\mathbf{v}\times\mathbf{B} = +0.01\,\hat\phi$ V/m pushes charge counter-clockwise ✓.
>
> (b) **False.** A rigid loop translating through a *uniform* static field keeps the same flux, 0.045 Wb, so $\mathcal{E} = 0$. $\mathbf{v}\times\mathbf{B} = 2\hat{x}\times0.5\hat{z} = -1\,\hat{y}$ V/m is indeed nonzero, but it is the same on both sides parallel to $y$, and the loop runs through those sides in opposite directions: $+0.3$ V and $-0.3$ V cancel.
>
> (c) **True.** The field points along $-z$ and decays, so the $-z$ flux shrinks. The induced current props it up with a $-z$ field inside: clockwise. In numbers (counter-clockwise $C$, $d\mathbf{S} = \hat{z}\,dS$): $\Psi(1\text{ s}) = -9.53$ mWb and $\mathcal{E}(1\text{ s}) = -4.76$ mV — negative, so clockwise ✓.
>
> (d) **False.** The emf belongs to the closed path, gap included, and the flux through that path changes exactly as before: still $-4.76$ mV at $t = 1$ s. It now appears as a voltage across the gap. What vanishes is the current.
>
> (e) **False.** The induced field opposes the *change* in flux, not the field itself. In (a) and (c) it points the same way as the applied field, because in both cases the flux is shrinking.
>
> **Answer.** (a) true, (b) false, (c) true, (d) false, (e) false.

### 14.5 A sliding bar, find the error

> [!easy] Easy · find the error · motional emf
> Two long rails run along $x$ on the lines $y = 0$ and $y = 0.4$ m in the plane $z = 0$, joined at $x = 0$ by a resistor $R = 0.6\ \Omega$. A conducting bar bridges the rails at $x = 5t$ m, i.e. it slides at $\mathbf{v} = 5\hat{x}$ m/s. The field $\mathbf{B} = 0.3\,\hat{z}$ T is uniform and constant; bar and rails have no resistance. A student finds the current like this:
>
> *"Flux rule: $\Psi = B\ell x = 0.3\times0.4\times5t = 0.6t$ Wb, so $\lvert d\Psi/dt\rvert = 0.6$ V. Motional emf of the bar: $vB\ell = 5\times0.3\times0.4 = 0.6$ V. Total emf $0.6+0.6 = 1.2$ V, so $I = 1.2/0.6 = 2$ A."*
>
> What is wrong? Find the correct current, its direction around the circuit, and the magnetic force on the bar.
>
> *Source: original.*

> [!hint]- Hint
> Write the full law, $\oint(\mathbf{E}+\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l} = -d\Psi/dt$. Which side of this one equation did the student use for each "emf"? Is there any $\partial\mathbf{B}/\partial t$ here?

> [!solution]- Solution
> **The slip:** the same emf is counted twice. The flux rule $\mathcal{E} = \oint(\mathbf{E}+\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l} = -d\Psi/dt$ *already contains* the motional term. Here $\mathbf{B}$ is static, so $\nabla\times\mathbf{E} = -\partial\mathbf{B}/\partial t = 0$, $\oint\mathbf{E}\cdot d\mathbf{l} = 0$, and the whole of $-d\Psi/dt$ *is* the bar's $\int(\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l}$. "Flux" and "motional" are two routes to one number, not two sources in series.
>
> **Correct work.** Take $C$ counter-clockwise seen from $+z$ ($+\hat{x}$ along $y = 0$, $+\hat{y}$ up the bar, $-\hat{x}$ along the top rail, $-\hat{y}$ through $R$), so $d\mathbf{S} = \hat{z}\,dS$ and $\Psi = 0.6t$ Wb:
> $$
> \mathcal{E} = -\frac{d\Psi}{dt} = -0.6\ \text{V}.
> $$
> Motional route, as a check: $\mathbf{v}\times\mathbf{B} = 5\hat{x}\times0.3\hat{z} = -1.5\,\hat{y}$ V/m; up the bar ($+\hat{y}$, the direction of $C$) this gives $-1.5\times0.4 = -0.6$ V ✓ — the same emf, not a second one.
>
> So $I = 0.6/0.6 = 1.0$ A, and the minus sign says it flows against $C$: **clockwise** seen from $+z$, down the bar ($-\hat{y}$) and up through the resistor. Lenz agrees: the circuit grows, its $+z$ flux grows, and a clockwise current makes a $-z$ field inside that opposes the growth.
>
> Force on the bar: $\mathbf{F} = I\boldsymbol{\ell}\times\mathbf{B} = 1.0\,(-0.4\,\hat{y})\times0.3\,\hat{z} = -0.12\,\hat{x}$ N, a drag against the motion.
>
> **Answer.** The student added the same emf twice. Correct: $\lvert\mathcal{E}\rvert = 0.6$ V and $I = 1.0$ A, clockwise seen from $+z$ (down the bar, along $-\hat{y}$); the force on the bar is $-0.12\,\hat{x}$ N.

## Medium

### 14.6 Rotating rod on a circular rail

> [!medium] Medium · motional emf · rotating rod
> A copper rod of length $L = 0.5$ m lies in the plane $z = 0$ with one end on a pivot at the origin. It rotates about the $z$ axis at $\omega = 40$ rad/s, counter-clockwise seen from $+z$, and its outer end slides on a circular rail of radius 0.5 m centred on the origin. A resistor $R = 0.25\ \Omega$ is connected between the pivot and the point $(0.5,0,0)$ m of the rail by a lead along the $x$ axis. The field is $\mathbf{B} = 0.2\,\hat{z}$ T; all other resistances are negligible.
> (a) Find the emf of the rod by integrating $\mathbf{v}\times\mathbf{B}$ from the pivot to the rim. Which end is the positive terminal?
> (b) Check (a) with the flux rule, for the closed path that runs out along the rod, back along the rail to $(0.5,0,0)$ m, and along the lead to the pivot (take $0<\omega t<2\pi$).
> (c) Find the current and its direction in the rod, the torque needed to keep $\omega$ constant, and check the power balance.
>
> *Source: classic.*

> [!hint]- Hint
> A point of the rod at distance $s$ from the pivot moves at speed $\omega s$ along $\hat\phi$, so $\mathbf{v}\times\mathbf{B}$ grows linearly along the rod. For (b), the path encloses a sector whose angle grows at the rate $\omega$.

> [!solution]- Solution
> **Setup.** $\mathbf{B}$ is constant, so there is no induced $\mathbf{E}$: all of the emf is motional. Use cylindrical coordinates; the rod lies along $\hat{r}$ at the angle $\phi = \omega t$.
>
> (a) At distance $s$ from the pivot, $\mathbf{v} = \omega\hat{z}\times s\hat{r} = \omega s\,\hat\phi$, so
> $$
> \mathbf{v}\times\mathbf{B} = \omega sB\,(\hat\phi\times\hat{z}) = \omega sB\,\hat{r},
> $$
> pointing outward along the rod (4 V/m at the tip). It pushes positive charge toward the rim, so **the rim is the $+$ terminal**. Integrating from the pivot to the rim:
> $$
> \mathcal{E}_{\text{rod}} = \int_0^L\omega sB\,ds = \tfrac12B\omega L^2 = \tfrac12(0.2)(40)(0.5)^2 = 1.0\ \text{V}.
> $$
> (b) The path encloses the sector $0<\phi<\omega t$ of radius $L$, whose area is $\tfrac12L^2\omega t$. It runs out along the rod and back toward $\phi = 0$ — clockwise seen from $+z$ — so the right-hand rule gives $d\mathbf{S} = -\hat{z}\,dS$:
> $$
> \Psi = -B\cdot\tfrac12L^2\omega t\quad\Rightarrow\quad \mathcal{E} = -\frac{d\Psi}{dt} = \tfrac12B\omega L^2 = 1.0\ \text{V}\ \checkmark
> $$
> It is positive along the path, i.e. outward along the rod: the same as (a).
>
> (c) $I = \mathcal{E}/R = 1.0/0.25 = 4$ A, **outward along the rod** (pivot to rim), returning from the rail through the resistor to the pivot. Lenz: the sector's $+z$ flux grows as the rod turns; the current circulates clockwise seen from $+z$ and makes a $-z$ field in the sector, opposing the growth ✓.
>
> The force on a piece $ds$ of the rod is $I\,ds\,\hat{r}\times B\hat{z} = -IB\,ds\,\hat\phi$, against the rotation. Its torque about the axis:
> $$
> \tau_z = -\int_0^L s\,IB\,ds = -\tfrac12IBL^2 = -\tfrac12(4)(0.2)(0.25) = -0.1\ \text{N}\cdot\text{m}.
> $$
> So you must apply $+0.1$ N·m (along $+\hat{z}$) to keep $\omega$ constant. Power: $\tau\omega = 0.1\times40 = 4$ W, $I^2R = 4^2\times0.25 = 4$ W, and $\mathcal{E}I = 1.0\times4 = 4$ W ✓ — the work you do becomes heat in $R$.
>
> **Check:** units of $B\omega L^2$: T·s⁻¹·m² = Wb/s = V ✓. Doubling $L$ quadruples the emf, because both the length and the average speed double.
>
> **Watch out:** the speed is not the same all along the rod. Using the tip speed $\omega L$ for the whole rod doubles the answer; the average speed is $\omega L/2$.
>
> **Answer.** $\mathcal{E} = \tfrac12B\omega L^2 = 1.0$ V with the rim positive; $I = 4$ A outward along the rod; applied torque 0.1 N·m along $+\hat{z}$; 4 W in, 4 W dissipated.

### 14.7 Generator coil in a uniform field

> [!medium] Medium · generator · motional emf
> A rectangular coil of $N = 50$ turns, 4 cm wide and 5 cm tall, spins at 1800 rpm about the $z$ axis in the uniform field $\mathbf{B} = 0.25\,\hat{x}$ T. The axis runs through the middle of the coil, parallel to its 5 cm sides. At time $t$ the coil's unit normal is $\hat{n}(t) = -\sin\omega t\,\hat{x} + \cos\omega t\,\hat{y}$ (the coil turns counter-clockwise seen from $+z$ and lies in the $xz$-plane at $t = 0$), and its winding sense $C$ is tied to $\hat{n}$ by the right-hand rule. Slip rings connect it to a load; the total resistance is $10\ \Omega$.
> (a) Find the flux $\Psi(t)$ through one turn and the emf $\mathcal{E}(t)$ of the coil. Evaluate $\mathcal{E}$ at $t = 1/180$ s.
> (b) Check the peak emf by integrating $\mathbf{v}\times\mathbf{B}$ around one turn at $t = 0$.
> (c) Find the current amplitude and the average power delivered.
>
> *Source: classic.*

> [!hint]- Hint
> For a flat loop in a uniform field, $\Psi = \mathbf{B}\cdot\hat{n}\,A$. For (b), only the two 5 cm sides cut across $\mathbf{B}$; each is 2 cm from the axis.

> [!solution]- Solution
> **Setup.** $\omega = 1800\times2\pi/60 = 60\pi$ rad/s $\approx188.5$ rad/s, and $A = 0.04\times0.05 = 0.002$ m². $\mathbf{B}$ is uniform and constant, so all of the emf is motional; the flux rule gets it fastest.
>
> (a) Per turn,
> $$
> \Psi(t) = \mathbf{B}\cdot\hat{n}(t)\,A = 0.25\,(-\sin\omega t)(0.002) = -5\times10^{-4}\sin\omega t\ \text{Wb}.
> $$
> The $N$ turns are in series and each links the same flux, so their emfs add:
> $$
> \mathcal{E}(t) = -N\frac{d\Psi}{dt} = NBA\omega\cos\omega t = 50(0.25)(0.002)(60\pi)\cos\omega t = 1.5\pi\cos\omega t\ \text{V}\approx4.71\cos\omega t\ \text{V}.
> $$
> At $t = 1/180$ s, $\omega t = \pi/3$ and $\mathcal{E} = 0.75\pi\approx2.36$ V.
>
> **Lenz:** at $t = 0$ the plane of the coil contains $\mathbf{B}$ and $\Psi = 0$; just after, $\Psi$ turns negative — the field starts to thread the coil against $\hat{n}$. The positive emf drives current along $C$, whose own field inside the coil points along $+\hat{n}$: it opposes that change ✓.
>
> (b) At $t = 0$ the coil lies in the $xz$-plane with its 5 cm sides at $x = \pm2$ cm, and $C$ (counter-clockwise seen from $+y$) runs down the side at $x = +2$ cm and up the side at $x = -2$ cm. Each side moves at $\omega\times0.02 = 1.2\pi\approx3.77$ m/s. On the side at $x = +2$ cm:
> $$
> \mathbf{v} = 1.2\pi\,\hat{y}\ \text{m/s},\qquad \mathbf{v}\times\mathbf{B} = 1.2\pi(0.25)(\hat{y}\times\hat{x}) = -0.3\pi\,\hat{z}\ \text{V/m},
> $$
> along $-\hat{z}$, the way $C$ runs there, so this side gives $0.3\pi\times0.05 = 0.015\pi$ V. The other side has $\mathbf{v}$ and $\mathbf{v}\times\mathbf{B}$ reversed and is traversed upward: another $+0.015\pi$ V. On the 4 cm sides $\mathbf{v}\times\mathbf{B}$ is along $\pm\hat{z}$, perpendicular to the wire, and gives nothing. One turn: $0.03\pi$ V; fifty turns: $1.5\pi$ V ✓, the peak of (a).
>
> (c) $I_0 = 1.5\pi/10 = 0.15\pi\approx0.471$ A. The time average of $\cos^2$ is $\tfrac12$, so
> $$
> \langle P\rangle = \frac{\mathcal{E}_0^2}{2R} = \frac{(1.5\pi)^2}{20}\approx1.11\ \text{W}.
> $$
> **Check:** units of $NBA\omega$: T·m²·s⁻¹ = Wb/s = V ✓. The emf peaks when the flux passes through zero (coil plane parallel to $\mathbf{B}$, sides cutting the field head-on) and vanishes when the flux is largest.
>
> **Answer.** $\Psi = -5\times10^{-4}\sin(60\pi t)$ Wb per turn; $\mathcal{E} = 1.5\pi\cos(60\pi t)\approx4.71\cos(60\pi t)$ V, about 2.36 V at $t = 1/180$ s; by $\mathbf{v}\times\mathbf{B}$, $0.015\pi$ V per side and $1.5\pi$ V in all; $I_0\approx0.471$ A; $\langle P\rangle\approx1.11$ W.

### 14.8 Square loop in a graded field

> [!medium] Medium · motional emf · nonuniform field
> The static field $\mathbf{B} = 0.5\,(z\,\hat{x} + x\,\hat{z})$ T ($x$, $z$ in metres) has zero divergence and zero curl, so it can exist in a current-free region; in the plane $z = 0$ it is simply $\mathbf{B} = 0.5x\,\hat{z}$ T. A square loop of side 20 cm and resistance $0.05\ \Omega$ lies in the plane $z = 0$ with its sides parallel to the axes, and moves at $\mathbf{v} = 3\hat{x}$ m/s; at $t = 0$ it occupies $0.1\le x\le0.3$ m, $0\le y\le0.2$ m.
> (a) Find the flux $\Psi(t)$ (with $d\mathbf{S} = \hat{z}\,dS$) and the emf, counter-clockwise seen from $+z$.
> (b) Check (a) at $t = 0$ by integrating $\mathbf{v}\times\mathbf{B}$ around the loop, edge by edge.
> (c) Find the current and its sense, the force needed to keep the velocity constant, and check the power balance.
>
> *Source: Summer 2020 HE2 #3 and Summer 2018 HE2 #2 style (a loop moving through a linearly graded field), new numbers, with an edge-by-edge check and the force added.*

> [!hint]- Hint
> A rigid loop translating through a *uniform* field has no emf (14.4(b)); here the two edges along $y$ sit in different fields. For the flux, integrate $0.5x$ over the square at time $t$: for a field that is linear in $x$, the result is the field at the centre times the area.

> [!solution]- Solution
> **Setup.** $\mathbf{B}$ is static, so there is no transformer emf; everything is motional (the lecture's third case: motion through a nonuniform field). The edges along $y$ are at $x_1 = 0.1+3t$ and $x_2 = x_1+0.2$ m, and the centre is at $x_c = 0.2+3t$ m.
>
> (a)
> $$
> \Psi(t) = \int_0^{0.2}\!dy\int_{x_1}^{x_2}0.5x\,dx = 0.5\,x_c\,(0.2)^2 = 0.5\,(0.2+3t)(0.04) = 0.004+0.06t\ \text{Wb},
> $$
> $$
> \mathcal{E} = -\frac{d\Psi}{dt} = -0.06\ \text{V}:
> $$
> 60 mV, clockwise seen from $+z$, and the same wherever the loop is, because it keeps moving into a field that grows at a steady rate.
>
> (b) $\mathbf{v}\times\mathbf{B} = 3\hat{x}\times0.5x\,\hat{z} = -1.5x\,\hat{y}$ V/m points along $y$, so only the two edges along $y$ contribute. Counter-clockwise, the right edge ($x_2 = 0.3$ m, $B = 0.15$ T) runs along $+\hat{y}$ and the left edge ($x_1 = 0.1$ m, $B = 0.05$ T) along $-\hat{y}$:
> $$
> \mathcal{E} = -vB(x_2)\,s + vB(x_1)\,s = -3(0.15)(0.2) + 3(0.05)(0.2) = -0.09+0.03 = -0.06\ \text{V}\ \checkmark
> $$
> Each edge on its own is a "battery"; the loop feels only their difference.
>
> (c) $I = 0.06/0.05 = 1.2$ A, **clockwise** seen from $+z$. Lenz: the loop moves into a stronger $+z$ field, so its $+z$ flux grows; the clockwise current's $-z$ field opposes the growth ✓.
>
> Clockwise means $-\hat{y}$ on the right edge and $+\hat{y}$ on the left edge, so with $\mathbf{F} = I\boldsymbol{\ell}\times\mathbf{B}$ at $t = 0$:
> $$
> \mathbf{F}_{\text{right}} = -IsB(x_2)\,\hat{x} = -0.036\,\hat{x}\ \text{N},\qquad \mathbf{F}_{\text{left}} = +IsB(x_1)\,\hat{x} = +0.012\,\hat{x}\ \text{N}.
> $$
> The forces on the two edges along $x$ are $\mp0.024\,\hat{y}$ N and cancel. Net: $\mathbf{F} = -Is\,[B(x_2)-B(x_1)]\,\hat{x} = -1.2(0.2)(0.1)\,\hat{x} = -0.024\,\hat{x}$ N, again independent of position. You must push with $+0.024\,\hat{x}$ N. Power: $Fv = 0.024\times3 = 0.072$ W $= I^2R = 1.2^2\times0.05 = 0.072$ W ✓.
>
> **Check:** for *any* loop shape, $\Psi = 0.5\,\bar{x}A$ with $\bar{x}$ the $x$ of the centroid, so $\mathcal{E} = -0.5vA = -0.06$ V: a circle of the same 0.04 m² area gives $-0.06$ V too, by both routes.
>
> **Answer.** $\Psi = 0.004+0.06t$ Wb; $\mathcal{E} = -0.06$ V, i.e. 60 mV clockwise seen from $+z$ ($-0.09$ V from the right edge, $+0.03$ V from the left); $I = 1.2$ A clockwise; applied force $0.024\,\hat{x}$ N; 0.072 W in = 0.072 W dissipated.

## Hard

### 14.9 Loop crossing a field strip

> [!hard] Hard · motional emf · Lenz · energy
> A uniform magnetic field of 0.4 T pointing along $-\hat{z}$ fills the slab $0<x<0.5$ m; outside the slab $\mathbf{B} = 0$. A square loop of side $s = 0.2$ m and resistance $0.1\ \Omega$ lies in the plane $z = 0$ with its sides along $x$ and $y$, and is pulled through the slab at the constant velocity $\mathbf{v} = 5\hat{x}$ m/s. Its leading edge reaches $x = 0$ at $t = 0$.
> (a) Find the flux $\Psi(t)$ through the loop, with $d\mathbf{S} = \hat{z}\,dS$, from $t = 0$ until the loop has left the field, and sketch it.
> (b) Find the emf and the current (magnitude and sense seen from $+z$) in each phase of the motion. Check the entry phase with $\oint(\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l}$.
> (c) Find the external force needed to keep the velocity constant in each phase.
> (d) Show that the total work done by that force equals the total heat dissipated in the loop.
> (e) Repeat (b) and (d) for a slab only 0.1 m wide, $0<x<0.1$ m.
>
> *Source: classic.*

> [!hint]- Hint
> First find the times at which an edge crosses a boundary of the slab. In each phase, ask which edges are in the field: only an edge along $y$ that sits in the field contributes to $\oint(\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l}$, and only such an edge feels an uncancelled force.

> [!solution]- Solution
> **Setup.** The field is static, so all of the emf is motional. The leading edge is at $x = 5t$ and the trailing edge at $x = 5t-0.2$ m. The loop is entirely inside the slab at $t = s/v = 0.04$ s; its leading edge leaves at $t = 0.5/5 = 0.10$ s and its trailing edge at $t = 0.7/5 = 0.14$ s.
>
> (a) With $d\mathbf{S} = \hat{z}\,dS$, $\Psi$ is $-0.4$ T times the part of the loop's area that is inside the slab:
> $$
> \Psi(t) = \begin{cases} -0.4\,(0.2)(5t) = -0.4t\ \text{Wb}, & 0<t<0.04\ \text{s}\\ -0.4\,(0.2)(0.2) = -0.016\ \text{Wb}, & 0.04<t<0.10\ \text{s}\\ -0.016+0.4\,(t-0.10)\ \text{Wb}, & 0.10<t<0.14\ \text{s}\\ 0, & t>0.14\ \text{s} \end{cases}
> $$
> The sketch is a trapezoid: a straight ramp down to $-0.016$ Wb, a flat bottom, and a ramp back up to zero (for example $\Psi = -0.008$ Wb at $t = 0.02$ s and again at $t = 0.12$ s).
>
> (b) $\mathcal{E} = -d\Psi/dt$, positive meaning counter-clockwise seen from $+z$:
>
> - **Entering** ($0<t<0.04$ s): $\mathcal{E} = +0.4$ V, $I = 0.4/0.1 = 4$ A **counter-clockwise**. Lenz: the loop takes in more and more $-z$ flux; the current opposes that growth with a $+z$ field inside, which is counter-clockwise ✓.
> - **Inside** ($0.04<t<0.10$ s): $\Psi$ is constant, so $\mathcal{E} = 0$ and $I = 0$, even though the loop is moving through the field.
> - **Leaving** ($0.10<t<0.14$ s): $\mathcal{E} = -0.4$ V, $I = 4$ A **clockwise**. Lenz: the $-z$ flux shrinks; the current props it up with a $-z$ field inside, which is clockwise ✓.
> - After $t = 0.14$ s: nothing.
>
> Motional check while entering: only the leading edge is in the field, where $\mathbf{v}\times\mathbf{B} = 5\hat{x}\times(-0.4\hat{z}) = +2\,\hat{y}$ V/m. Counter-clockwise runs along $+\hat{y}$ on the leading (right-hand) edge: $2\times0.2 = +0.4$ V ✓. On the edges along $x$, $\mathbf{v}\times\mathbf{B}$ is perpendicular to the wire and contributes nothing. While leaving, the trailing edge (traversed along $-\hat{y}$) gives $-0.4$ V ✓; with the loop fully inside, the two edges give $+0.4-0.4 = 0$ ✓.
>
> (c) Entering: the 4 A runs along $+\hat{y}$ in the leading edge, so $\mathbf{F} = I\boldsymbol{\ell}\times\mathbf{B} = 4\,(0.2\,\hat{y})\times(-0.4\,\hat{z}) = -0.32\,\hat{x}$ N. Leaving: the clockwise 4 A runs along $+\hat{y}$ in the trailing edge, giving the same force, $-0.32\,\hat{x}$ N. (On the pieces of the two $x$-edges inside the slab the currents are opposite, so those forces cancel.) The magnetic force always opposes the motion — Lenz again — so you must pull with $+0.32\,\hat{x}$ N while the loop enters or leaves, and with no force while it is wholly inside or wholly outside.
>
> (d) Work: $0.32\ \text{N}\times(0.2+0.2)\ \text{m} = 0.128$ J. Heat: $I^2R = 4^2\times0.1 = 1.6$ W for $0.04+0.04 = 0.08$ s, i.e. 0.128 J ✓. Every joule you put in becomes heat in the wire.
>
> (e) With $w = 0.1$ m $<s$ the middle phase changes character. The leading edge crosses the slab during $0<t<0.02$ s: $\mathcal{E} = +0.4$ V (4 A counter-clockwise). For $0.02<t<0.04$ s the whole slab lies *inside* the loop: $\Psi = -0.4\,(0.1)(0.2) = -0.008$ Wb, constant, so $\mathcal{E} = 0$. The trailing edge crosses during $0.04<t<0.06$ s: $\mathcal{E} = -0.4$ V (4 A clockwise). The emf has the same size, $vBs$, which does not depend on the width of the slab, but each pulse lasts half as long, so the heat is $1.6\ \text{W}\times0.04\ \text{s} = 0.064$ J, half as much, and the work, $0.32\ \text{N}\times(0.1+0.1)\ \text{m} = 0.064$ J, matches it ✓.
>
> **Answer.** (a) $\Psi$ ramps from 0 to $-0.016$ Wb during $0<t<0.04$ s, stays there until 0.10 s, and returns to 0 at 0.14 s. (b) $+0.4$ V and 4 A counter-clockwise (seen from $+z$) while entering, 0 while inside, $-0.4$ V and 4 A clockwise while leaving. (c) 0.32 N along $+\hat{x}$ while entering or leaving, 0 otherwise. (d) 0.128 J of work = 0.128 J of heat. (e) $\pm0.4$ V during $0<t<0.02$ s and $0.04<t<0.06$ s, zero in between; 0.064 J of work = 0.064 J of heat.

### 14.10 Voltmeters around a ramping solenoid

> [!hard] Hard · voltmeters · induced field · Faraday's law
> A long solenoid of radius 0.2 m lies along the $z$ axis. Its current is ramped down so that the flux inside it, $\Psi_s$ (along $+\hat{z}$), changes at the constant rate $d\Psi_s/dt = -2$ Wb/s; outside the solenoid $\mathbf{B} = 0$. A rectangular circuit in the plane $z = 0$, centred on the axis, has corners $P_1 = (1.5,-1)$, $P_2 = (1.5,1)$, $P_3 = (-1.5,1)$ and $P_4 = (-1.5,-1)$ m. Side $P_1P_2$ contains $R_1 = 4\ \Omega$, side $P_2P_3$ contains $R_2 = 6\ \Omega$, side $P_3P_4$ contains $R_3 = 10\ \Omega$, and side $P_4P_1$ is a plain wire of negligible resistance.
> (a) Find the current, its sense, and the voltage drop across each resistor in the direction of the current.
> (b) Find the electric field that the solenoid produces outside itself, and evaluate it at $r = 0.5$ m and $r = 1$ m.
> (c) Two ideal voltmeters both have their $+$ lead on $P_1$ and their $-$ lead on $P_2$. Meter 1's leads run just outside side $P_1P_2$ (along $x = 1.6$ m). Meter 2's leads go the other way round, just outside the other three sides (along $y = -1.1$, $x = -1.6$ and $y = 1.1$ m). What does each meter read?
> (d) Meter 3 has its $+$ lead on $P_4$ and its $-$ lead on $P_1$, the two ends of the plain wire. What does it read if its leads run just below the wire (along $y = -1.1$ m)? And if they run inside the rectangle and pass the solenoid on its $+y$ side (along $y = 0.5$ m)?
>
> *Source: Summer 2017 HE2 #3 and Summer 2018 HE2 #3 style (resistor square and voltmeters in changing flux), with the flux confined to a solenoid.*

> [!hint]- Hint
> A meter reads $\int\mathbf{E}\cdot d\mathbf{l}$ along its own leads, from $+$ to $-$. Close that path with a piece of the circuit and apply Faraday's law to the loop you have made: its emf is $-d\Psi_s/dt$ if it encircles the solenoid counter-clockwise seen from $+z$, $+d\Psi_s/dt$ if it encircles it clockwise, and zero if it does not encircle it.

> [!solution]- Solution
> **Setup.** Take $C$ counter-clockwise seen from $+z$ ($P_1\to P_2\to P_3\to P_4$), so $d\mathbf{S} = \hat{z}\,dS$. The only flux is inside the solenoid, so any loop that encircles the solenoid once counter-clockwise has emf $-d\Psi_s/dt = +2$ V (clockwise: $-2$ V), and any loop that does not encircle it has emf 0.
>
> (a) $\mathcal{E} = +2$ V counter-clockwise and the total resistance is $20\ \Omega$, so $I = 0.1$ A **counter-clockwise**: up through $R_1$ (at $x = 1.5$ m), leftward through $R_2$, down through $R_3$, and rightward along the wire. Lenz: the $+z$ flux is falling, and a counter-clockwise current makes a $+z$ field inside that props it up ✓. Drops: $IR_1 = 0.4$ V, $IR_2 = 0.6$ V, $IR_3 = 1.0$ V, adding up to 2 V — Kirchhoff's voltage law with the emf as the source.
>
> (b) By symmetry $\mathbf{E} = E_\phi(r)\,\hat\phi$. Faraday's law on a counter-clockwise circle of radius $r>0.2$ m:
> $$
> 2\pi r\,E_\phi = -\frac{d\Psi_s}{dt} = 2\ \text{V}\quad\Rightarrow\quad E_\phi = \frac{2}{2\pi r} = \frac{1}{\pi r}\ \text{V/m}\quad(r\text{ in m}),
> $$
> counter-clockwise: 0.637 V/m at $r = 0.5$ m and 0.318 V/m at $r = 1$ m. There is no $\mathbf{B}$ where this $\mathbf{E}$ lives; it is set up by the changing current in the solenoid.
>
> (c) **Meter 1.** Its leads ($P_1\to P_2$ along $x = 1.6$ m) and side $P_1P_2$, walked back from $P_2$ to $P_1$, form a thin loop that encircles no flux:
> $$
> V_1 + \int_{P_2\to P_1,\ \text{through }R_1}\mathbf{E}\cdot d\mathbf{l} = 0 .
> $$
> Walking from $P_2$ to $P_1$ goes *against* the current in $R_1$, so that integral is $-IR_1 = -0.4$ V, and $V_1 = +0.4$ V.
>
> **Meter 2.** Its leads ($P_1$ round the left of the solenoid to $P_2$) and side $P_1P_2$, walked back from $P_2$ to $P_1$, form a loop that encircles the solenoid **clockwise** seen from $+z$ (leftward along the bottom, up the left, rightward along the top, down the right). Its emf is $-2$ V:
> $$
> V_2 + (-IR_1) = -2\ \text{V}\quad\Rightarrow\quad V_2 = -2+0.4 = -1.6\ \text{V}.
> $$
> Second route: meter 2's leads hug the wire, $R_3$ and $R_2$ in thin flux-free loops, so it reads the drop along that route from $P_1$ to $P_2$. All three pieces are walked against the current: $0-1.0-0.6 = -1.6$ V ✓.
>
> **Check:** $V_1-V_2 = 0.4-(-1.6) = 2$ V, exactly the emf of the loop formed by the two sets of leads, which encircles the solenoid. Same two nodes, two readings, both correct.
>
> (d) Leads along the wire: the leads and the wire form a flux-free loop, and the perfectly conducting wire has $\mathbf{E} = 0$ inside, so meter 3 reads **0**. Leads passing the solenoid on its $+y$ side: the leads plus the wire (walked from $P_1$ back to $P_4$) encircle the solenoid clockwise seen from $+z$, with emf $-2$ V, and the wire contributes nothing, so meter 3 reads **$-2$ V** — across a piece of plain wire.
>
> **Watch out:** there is no such thing as "the voltage between $P_1$ and $P_2$" here. $\oint\mathbf{E}\cdot d\mathbf{l}\ne0$ around the solenoid, so $\int\mathbf{E}\cdot d\mathbf{l}$ between two points depends on the path, and a meter reports the path of its own leads.
>
> **Answer.** (a) $I = 0.1$ A counter-clockwise seen from $+z$; drops 0.4 V ($R_1$), 0.6 V ($R_2$), 1.0 V ($R_3$). (b) $\mathbf{E} = \dfrac{1}{\pi r}\,\hat\phi$ V/m (counter-clockwise seen from $+z$): 0.637 V/m at 0.5 m, 0.318 V/m at 1 m. (c) Meter 1: $+0.4$ V; meter 2: $-1.6$ V. (d) 0 with the leads along the wire; $-2$ V with the leads passing the solenoid on its $+y$ side.

### 14.11 Magnetic braking

> [!hard] Hard · motional emf · Lenz · energy
> A bar of mass $m = 0.1$ kg slides without friction on two horizontal rails that run along $x$ on the lines $y = 0$ and $y = \ell = 0.5$ m in the plane $z = 0$; the rails are joined at $x = 0$ by a resistor $R = 0.2\ \Omega$ (bar and rails have negligible resistance). A uniform field $\mathbf{B} = 0.4\,\hat{z}$ T is perpendicular to the plane of the rails. At $t = 0$ the bar moves away from the resistor at $\mathbf{v} = 3\hat{x}$ m/s and is then left alone.
> (a) Find the current and the magnetic force on the bar as functions of its speed $v$, with directions.
> (b) Find $v(t)$ and the distance the bar travels before stopping.
> (c) Show that the total energy dissipated in $R$ equals the initial kinetic energy.
> (d) Now the bar starts from rest at $t = 0$ and is pulled along $+\hat{x}$ by a constant force of 0.6 N. Find $v(t)$, the speed at $t = 0.5$ s, the terminal speed, and the power balance at terminal speed.
>
> *Source: classic.*

> [!hint]- Hint
> The emf is $vB\ell$, the current $vB\ell/R$, and the force on the current-carrying bar is $I\ell B$ opposing the motion — so Newton's law becomes $m\,dv/dt = -kv$. In (d) the pull adds a constant term: $m\,dv/dt = F-kv$.

> [!solution]- Solution
> **(a)** Take $C$ counter-clockwise seen from $+z$, so $d\mathbf{S} = \hat{z}\,dS$ and $\Psi = B\ell x$. As the bar moves away the flux grows: $\mathcal{E} = -d\Psi/dt = -vB\ell$. Motional check: $\mathbf{v}\times\mathbf{B} = v\hat{x}\times B\hat{z} = -vB\,\hat{y}$, which integrated up the bar (the $+\hat{y}$ direction of $C$) gives $-vB\ell$ ✓; at $v = 3$ m/s both routes give $-0.6$ V. So $I = vB\ell/R$ flows **clockwise** seen from $+z$: down the bar, along $-\hat{y}$. Lenz: the $+z$ flux grows, and the clockwise current's $-z$ field opposes the growth.
>
> The force on the bar is $I\boldsymbol{\ell}\times\mathbf{B} = I\ell(-\hat{y})\times B\hat{z} = -I\ell B\,\hat{x}$:
> $$
> \mathbf{F} = -\frac{B^2\ell^2}{R}\,v\,\hat{x},
> $$
> directed *against* the velocity. At $t = 0$: $I = 3$ A, $F = 0.6$ N.
>
> **(b)** Newton, with $k = B^2\ell^2/R = 0.2$ kg/s: $m\dfrac{dv}{dt} = -kv$, so
> $$
> v(t) = v_0e^{-t/\tau},\qquad \tau = \frac{mR}{B^2\ell^2} = \frac{0.1\times0.2}{0.16\times0.25} = 0.5\ \text{s},
> $$
> i.e. $v = 3e^{-2t}$ m/s. Distance: $\displaystyle\int_0^\infty v\,dt = v_0\tau = 1.5$ m.
>
> **(c)** $\displaystyle\int_0^\infty I^2R\,dt = \frac{B^2\ell^2v_0^2}{R}\int_0^\infty e^{-2t/\tau}dt = \frac{B^2\ell^2v_0^2}{R}\cdot\frac{\tau}{2} = \tfrac12mv_0^2 = 0.45$ J ✓.
>
> **(d)** Now $m\dfrac{dv}{dt} = F-kv$ with $v(0) = 0$:
> $$
> v(t) = \frac{F}{k}\big(1-e^{-t/\tau}\big) = 3\big(1-e^{-2t}\big)\ \text{m/s},
> $$
> with the same $\tau = 0.5$ s. At $t = 0.5$ s, $v = 3(1-e^{-1})\approx1.90$ m/s. The terminal speed $F/k = FR/(B\ell)^2 = 3$ m/s is where the magnetic drag $kv$ balances the pull. There $P_{\text{in}} = Fv = 0.6\times3 = 1.8$ W, and $I = vB\ell/R = 3$ A gives $I^2R = (3)^2(0.2) = 1.8$ W ✓: in the steady state every watt you supply is dissipated in $R$.
>
> **Check:** the time constant $\tau = mR/(B^2\ell^2)$ governs both the braking in (b) and the spin-up in (d); it is set by the circuit and the mass, not by the force.
>
> **Watch out:** the magnetic force does no work on the charges; the kinetic energy becomes heat through the electric field in the resistor.
>
> **Answer.** (a) $I = vB\ell/R$, clockwise seen from $+z$ (down the bar, along $-\hat{y}$); $\mathbf{F} = -(B^2\ell^2/R)\,v\,\hat{x}$, opposing the motion (3 A and 0.6 N at $t = 0$). (b) $v = 3e^{-2t}$ m/s; 1.5 m. (c) 0.45 J dissipated = initial kinetic energy. (d) $v = 3(1-e^{-2t})$ m/s, 1.90 m/s at 0.5 s, terminal speed 3 m/s, 1.8 W supplied = 1.8 W dissipated.

### 14.12 Shrinking ring in a ramping solenoid

> [!hard] Hard · induced field · transformer emf · motional emf
> A long solenoid of radius $a = 10$ cm lies along the $z$ axis; inside it the field is uniform, $\mathbf{B} = (0.1+2t)\,\hat{z}$ T ($t$ in seconds), and outside it $\mathbf{B} = 0$.
> (a) Find the induced electric field inside and outside the solenoid, with its direction, and evaluate it at $r = a$ and $r = 2a$.
> (b) A conducting ring in the plane $z = 0$, centred on the axis, is pulled inward so that its radius is $r(t) = 0.08-0.5t$ m for $0\le t\le0.1$ s. Find the flux $\Psi(t)$ through the ring and the emf $\mathcal{E}(t)$, both for the counter-clockwise sense seen from $+z$ ($d\mathbf{S} = \hat{z}\,dS$).
> (c) At $t = 0$, split $\mathcal{E}$ into its transformer part $\oint\mathbf{E}\cdot d\mathbf{l}$ and its motional part $\oint(\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l}$, and check that they add up to your result from (b).
> (d) When does the induced current reverse? Give its sense before and after, with a Lenz argument, and the emf at $t = 0.1$ s.
>
> *Source: original.*

> [!hint]- Hint
> (a) Faraday's law on a fixed circle of radius $r$: $2\pi rE_\phi = -d\Psi_{\text{enc}}/dt$, and outside the solenoid only the area $\pi a^2$ carries flux. (b) $\Psi = \pi r^2B$ with *both* factors changing. (d) The current reverses when $\Psi$ stops growing and starts to shrink.

> [!solution]- Solution
> **Setup.** Cylindrical symmetry: $\mathbf{E} = E_\phi(r)\,\hat\phi$. Faraday's law on a fixed circle of radius $r$, counter-clockwise seen from $+z$: $2\pi r\,E_\phi = -d\Psi_{\text{enc}}/dt$, with $dB/dt = 2$ T/s.
>
> (a) Inside ($r<a$), $\Psi_{\text{enc}} = \pi r^2B$; outside ($r>a$), $\Psi_{\text{enc}} = \pi a^2B$. So
> $$
> E_\phi = \begin{cases} -\dfrac{r}{2}\dfrac{dB}{dt} = -r\ \text{V/m}, & r<a\\[8pt] -\dfrac{a^2}{2r}\dfrac{dB}{dt} = -\dfrac{0.01}{r}\ \text{V/m}, & r>a \end{cases}\qquad(r\text{ in m}).
> $$
> At $r = a$: $E_\phi = -0.1$ V/m; at $r = 2a$: $E_\phi = -0.05$ V/m. Negative $E_\phi$ means **clockwise** seen from $+z$. Lenz: charges pushed clockwise would make a $-z$ field, opposing the growth of $B_z$ ✓.
>
> **Check:** $(\nabla\times\mathbf{E})_z = \dfrac1r\dfrac{d}{dr}(rE_\phi)$ is $-2$ T/s $= -\partial B_z/\partial t$ inside and 0 outside, where $\mathbf{B} = 0$: the field outside circulates, yet has no curl.
>
> (b) The ring stays inside the solenoid ($r\le8$ cm $<a$), so
> $$
> \Psi(t) = \pi r^2B = \pi(0.08-0.5t)^2(0.1+2t)\ \text{Wb},
> $$
> $$
> \mathcal{E} = -\frac{d\Psi}{dt} = -\pi r\Big(2B\frac{dr}{dt} + r\frac{dB}{dt}\Big) = -\pi r\,(0.06-3t) = 3\pi(0.08-0.5t)(t-0.02)\ \text{V}.
> $$
> (c) At $t = 0$: $r = 0.08$ m, $B = 0.1$ T.
>
> - Transformer part: $\oint\mathbf{E}\cdot d\mathbf{l} = 2\pi rE_\phi = -\pi r^2\dfrac{dB}{dt} = -\pi(0.0064)(2) = -12.8\pi$ mV $\approx-40.21$ mV.
> - Motional part: the ring moves inward, $\mathbf{v} = -0.5\,\hat{r}$ m/s, so $\mathbf{v}\times\mathbf{B} = -0.5B\,(\hat{r}\times\hat{z}) = +0.5B\,\hat\phi$ and $\oint(\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l} = 2\pi r(0.5)B = 2\pi(0.08)(0.5)(0.1) = 8\pi$ mV $\approx25.13$ mV.
>
> Sum: $(-12.8+8)\pi = -4.8\pi$ mV $\approx-15.08$ mV, which is (b) at $t = 0$: $3\pi(0.08)(-0.02)$ V $= -4.8\pi$ mV ✓. The two causes pull opposite ways: the growing field drives charges clockwise, the shrinking ring drives them counter-clockwise.
>
> (d) $\mathcal{E}\propto(t-0.02)$: negative for $t<0.02$ s, zero at $t = 0.02$ s, positive afterwards. At $t = 0.02$ s the flux is at its maximum, $\Psi = \pi(0.07)^2(0.14)\approx2.16\times10^{-3}$ Wb, and the two parts cancel exactly ($\mp30.79$ mV).
>
> - $t<0.02$ s: $B$ grows faster than the area shrinks, so the $+z$ flux grows; the current opposes it with a $-z$ field: **clockwise**.
> - $t>0.02$ s: the shrinking area wins and the $+z$ flux falls; the current props it up with a $+z$ field: **counter-clockwise**.
>
> At $t = 0.1$ s ($r = 0.03$ m, $B = 0.3$ T): $\mathcal{E} = 3\pi(0.03)(0.08) = 7.2\pi$ mV $\approx22.62$ mV, counter-clockwise (transformer part $-5.65$ mV, motional part $+28.27$ mV).
>
> **Answer.** (a) $\mathbf{E} = -r\,\hat\phi$ V/m inside and $-(0.01/r)\,\hat\phi$ V/m outside, i.e. clockwise seen from $+z$; magnitude 0.1 V/m at $r = a$ and 0.05 V/m at $r = 2a$. (b) $\Psi = \pi(0.08-0.5t)^2(0.1+2t)$ Wb, $\mathcal{E} = 3\pi(0.08-0.5t)(t-0.02)$ V. (c) $-12.8\pi$ mV $+\ 8\pi$ mV $= -4.8\pi$ mV $\approx-15.1$ mV. (d) It reverses at $t = 0.02$ s: clockwise before, counter-clockwise after; $\mathcal{E}(0.1\text{ s})\approx+22.6$ mV.

### Sources for this page
Old exams, re-parameterized: SP18 Exam 2 #1(ii) (the ramping-field current of 14.2, with a direction added) and #1(iii) (the magnet and ring of 14.3, with the pole and the motion reversed); Summer 2020 HE2 #3 and Summer 2018 HE2 #2 (the loop moving through a linearly graded field of 14.8, with new numbers, an edge-by-edge check and the force added); Summer 2017 HE2 #3 and Summer 2018 HE2 #3 (the resistor loop and voltmeters in a changing flux of 14.10, with new numbers and the flux confined to a solenoid). Classic textbook problems with new numbers: the rotating rod (14.6), the generator coil (14.7), the loop crossing a field region (14.9) and magnetic braking (14.11). Problems 14.1, 14.4, 14.5 and 14.12 are original. Related worked examples in the course notes for Lecture 14: Example 3 (generator) for 14.7, Example 4 (bar on rails) for 14.11, and Examples 5–6 (voltmeters) for 14.10.

*Previous: [[practice/13-current-sheets-solenoids-and-vector-potential|Lecture 13 practice]] · next: [[practice/15-inductance-and-magnetic-energy|Lecture 15 practice]] · [[practice/index|all practice]]*
