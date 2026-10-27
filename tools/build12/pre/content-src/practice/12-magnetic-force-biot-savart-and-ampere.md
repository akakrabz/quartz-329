---
title: "Practice — Lecture 12: Magnetic force, Biot–Savart and Ampère's law"
description: "12 practice problems (5 easy, 3 medium, 4 hard) on qv×B forces and circular orbits, forces between parallel wires, δ-function currents, the ∇·B = 0 test, Biot–Savart for a square loop and a hairpin, the force on a loop beside a wire, crossing line currents, and Ampère's law for a nonuniform wire, an unequal-current coax and a wire with an off-axis hole, each with a folded hint and a worked solution."
tags: [practice, magnetostatics]
lecture: 12
---

*Practice for [[2-magnetostatics/12-magnetic-force-biot-savart-and-amperes-law|Lecture 12]] · concepts: [[concepts/lorentz-force]] · [[concepts/biot-savart-law]] · [[concepts/amperes-law]] · [[concepts/magnetic-field]] · all practice: [[practice/index|hub]] · by difficulty: [[practice/easy|easy]] · [[practice/medium|medium]] · [[practice/hard|hard]] · [[practice/topics|by topic]]*

Work each problem on paper first. Open the **hint** only when stuck, and the **solution** only after you have an answer you would hand in. Every answer here has been checked numerically.

## Easy

### 12.1 A charge passing a wire

> [!easy] Easy · multiple choice · Lorentz force · right-hand rule
> An infinitely long wire lies along the $y$ axis in free space and carries $I = 2$ A in the $-\hat{y}$ direction. A point charge $Q>0$ passes through the point $(0,1,-3)$ m with velocity $\mathbf{v} = 5\hat{z}$ m/s. At that instant the magnetic force on the charge points along
>
> (a) $+\hat{x}$
>
> (b) $-\hat{x}$
>
> (c) $+\hat{y}$
>
> (d) $-\hat{y}$
>
> (e) nowhere: the force is zero, because the wire is electrically neutral.
>
> *Source: original.*

> [!hint]- Hint
> Two steps, in this order: the direction of $\mathbf{B}$ at the charge (right-hand rule, with $r$ measured perpendicular to the wire), then $\mathbf{v}\times\mathbf{B}$.

> [!solution]- Solution
> **(c).** *Field.* The perpendicular from the wire to the charge runs from $(0,1,0)$ to $(0,1,-3)$, so $r = 3$ m and $\hat{r} = -\hat{z}$. Right-hand rule: thumb along the current, $-\hat{y}$; the fingers curl along $\hat\phi = (-\hat{y})\times\hat{r} = (-\hat{y})\times(-\hat{z}) = +\hat{x}$. Hence
> $$
> \mathbf{B} = \frac{\mu_0I}{2\pi r}\hat{x} = \frac{(2\times10^{-7})(2)}{3}\hat{x} = 1.33\times10^{-7}\,\hat{x}\ \text{T}.
> $$
> *Force.* $\mathbf{F} = Q\mathbf{v}\times\mathbf{B} = Q(5)(1.33\times10^{-7})\,\hat{z}\times\hat{x} = 6.67\times10^{-7}\,Q\,\hat{y}$ N (with $Q$ in coulombs), because $\hat{z}\times\hat{x} = +\hat{y}$.
>
> - (a) is the direction of $\mathbf{B}$ itself, and a magnetic force is always perpendicular to $\mathbf{B}$.
> - (b) is $-\mathbf{B}$: the right-hand rule done with the current taken along $+\hat{y}$. It still lies along the line of $\mathbf{B}$, so it cannot be a magnetic force either.
> - (d) is $\mathbf{B}\times\mathbf{v}$: the cross product in the wrong order.
> - (e) Neutrality removes the *electric* force only. A moving charge feels $Q\mathbf{v}\times\mathbf{B}$, and here $\mathbf{v}$ is not parallel to $\mathbf{B}$.
>
> **Check:** $\mathbf{F}\cdot\mathbf{v} = 0$ and $\mathbf{F}\cdot\mathbf{B} = 0$, as they must be for a magnetic force.
>
> **Watch out:** the coordinate $y = 1$ m lies *along* the wire and does not enter $r$. And had the charge moved along $\hat{x}$ (parallel to $\mathbf{B}$), the force would have been zero.
>
> **Answer.** (c): $\mathbf{F} = 6.67\times10^{-7}\,Q\,\hat{y}$ N ($Q$ in C), from $\mathbf{B} = 1.33\times10^{-7}\,\hat{x}$ T at the charge.

### 12.2 Two antiparallel wires

> [!easy] Easy · force between wires · right-hand rule
> Two long parallel wires lie in the plane $z = 0$ in free space. Wire 1 runs along the $x$ axis and carries $I_1 = 10$ A in the $+\hat{x}$ direction; wire 2 runs along the line $y = 4$ cm, $z = 0$, and carries $I_2 = 6$ A in the $-\hat{x}$ direction. (a) Find the field $\mathbf{B}_1$ of wire 1 at wire 2. (b) Find the force per metre on wire 2. Do the wires attract or repel? (c) Find the total $\mathbf{B}$ midway between the wires, at $(0,\,2\text{ cm},\,0)$.
>
> *Source: classic.*

> [!hint]- Hint
> Use $d\mathbf{F} = I\,d\mathbf{l}\times\mathbf{B}$ with $d\mathbf{l}$ along wire 2's *own* current, $-\hat{x}$.

> [!solution]- Solution
> (a) At wire 2, $d = 0.04$ m and $\hat{r} = +\hat{y}$. Right-hand rule, thumb along $+\hat{x}$: $\hat\phi = \hat{x}\times\hat{y} = +\hat{z}$. So $\mathbf{B}_1 = \dfrac{\mu_0I_1}{2\pi d}\hat{z} = \dfrac{(2\times10^{-7})(10)}{0.04}\hat{z} = 5\times10^{-5}\,\hat{z}$ T.
>
> (b) Per metre of wire 2:
> $$
> \frac{\mathbf{F}_2}{\ell} = I_2(-\hat{x})\times\mathbf{B}_1 = (6)(5\times10^{-5})\,(-\hat{x}\times\hat{z}) = 3\times10^{-4}\,\hat{y}\ \text{N/m},
> $$
> because $\hat{x}\times\hat{z} = -\hat{y}$. Wire 2 is pushed toward $+\hat{y}$, away from wire 1: antiparallel currents **repel**, with $\mu_0I_1I_2/(2\pi d) = 3\times10^{-4}$ N/m.
>
> (c) Wire 1 at $r = 2$ cm gives $1\times10^{-4}\,\hat{z}$ T (same direction as in (a)). For wire 2, $\hat{r} = -\hat{y}$ (from wire 2 down to the midpoint) and the thumb points along $-\hat{x}$: $\hat\phi = (-\hat{x})\times(-\hat{y}) = +\hat{z}$, so it gives $6\times10^{-5}\,\hat{z}$ T. Total: $1.6\times10^{-4}\,\hat{z}$ T. Between antiparallel currents the two fields add.
>
> **Check:** wire 2's field at wire 1 is $\mathbf{B}_2 = 3\times10^{-5}\,\hat{z}$ T, so the force on wire 1 is $I_1\hat{x}\times\mathbf{B}_2 = -3\times10^{-4}\,\hat{y}$ N/m: equal and opposite, as Newton's third law demands.
>
> **Answer.** (a) $\mathbf{B}_1 = 5\times10^{-5}\,\hat{z}$ T. (b) $3\times10^{-4}\,\hat{y}$ N/m on wire 2: the wires repel. (c) $\mathbf{B} = 1.6\times10^{-4}\,\hat{z}$ T.

### 12.3 An electron in Earth's field

> [!easy] Easy · Lorentz force · circular motion
> *Calculator problem* ($e = 1.602\times10^{-19}$ C, $m_e = 9.109\times10^{-31}$ kg). An electron moves in vacuum in the uniform field $\mathbf{B} = 5\times10^{-5}\,\hat{z}$ T, about the strength of Earth's field. At $t = 0$ it is at the origin with velocity $\mathbf{v} = 2\times10^5\,\hat{x}$ m/s. (a) Find the force on it at $t = 0$. (b) Find the radius, period and frequency of its orbit. (c) Does it circle counter-clockwise or clockwise, seen from $+z$, and where is the centre of the orbit?
>
> *Source: classic.*

> [!hint]- Hint
> The force is always perpendicular to $\mathbf{v}$, so the speed never changes: set $evB$ equal to $m_ev^2/R$. Keep the electron's negative charge in $\mathbf{F} = q\mathbf{v}\times\mathbf{B}$.

> [!solution]- Solution
> (a) With $q = -e$: $\mathbf{F} = -e\,(2\times10^5)(5\times10^{-5})\,\hat{x}\times\hat{z} = -e\,(10)(-\hat{y}) = 1.60\times10^{-18}\,\hat{y}$ N, because $\hat{x}\times\hat{z} = -\hat{y}$.
>
> (b) A force of fixed size that is always perpendicular to $\mathbf{v}$ does no work and bends the path into a circle (here $\mathbf{v}\perp\mathbf{B}$, so there is no drift along $z$):
> $$
> \frac{m_ev^2}{R} = evB\ \Rightarrow\ R = \frac{m_ev}{eB} = \frac{(9.109\times10^{-31})(2\times10^5)}{(1.602\times10^{-19})(5\times10^{-5})} = 2.27\ \text{cm},
> $$
> $$
> T = \frac{2\pi R}{v} = \frac{2\pi m_e}{eB} = 7.14\times10^{-7}\ \text{s} = 0.714\ \mu\text{s},\qquad f = \frac1T = 1.40\ \text{MHz}.
> $$
> The period does not depend on the speed: a faster electron runs a bigger circle in the same time.
>
> (c) At $t = 0$ the electron moves along $+\hat{x}$ and is pushed toward $+\hat{y}$, so it turns left: it circles **counter-clockwise seen from $+z$**, about the centre $(0,\,2.27\text{ cm},\,0)$, one radius away along the initial force.
>
> **Check:** a proton in the same place would feel $+e\,\mathbf{v}\times\mathbf{B}$ along $-\hat{y}$ and circle clockwise seen from $+z$: opposite charges, opposite senses. A numerical integration of $m_e\,d\mathbf{v}/dt = -e\,\mathbf{v}\times\mathbf{B}$ traces the same circle.
>
> **Watch out:** dropping the minus sign of the electron's charge reverses both the force and the sense of rotation.
>
> **Answer.** (a) $\mathbf{F} = 1.60\times10^{-18}\,\hat{y}$ N. (b) $R = 2.27$ cm, $T = 0.714\ \mu$s, $f = 1.40$ MHz. (c) Counter-clockwise seen from $+z$, centred at $(0,\,2.27\text{ cm},\,0)$.

### 12.4 Could this be a magnetic field

> [!easy] Easy · multiple choice · divergence · curl
> $B_0$ and $a$ are positive constants, $(x,y,z)$ are Cartesian coordinates, and $\hat{r}$ in (d) is the spherical radial unit vector. Which of these could be a static magnetic flux density? For that one, find the current density $\mathbf{J}$ that produces it (free space, $\mathbf{H} = \mathbf{B}/\mu_0$).
>
> (a) $\mathbf{B} = \dfrac{B_0}{a}(x\hat{x}+y\hat{y})$
>
> (b) $\mathbf{B} = \dfrac{B_0}{a}(x\hat{x}-y\hat{y}+z\hat{z})$
>
> (c) $\mathbf{B} = \dfrac{B_0}{a}(y\hat{x}-x\hat{y})$
>
> (d) $\mathbf{B} = B_0\hat{r}$
>
> *Source: classic.*

> [!hint]- Hint
> One of the two laws of magnetostatics holds for every magnetic field, whatever the currents. Test each option with it; then use the other law to find $\mathbf{J}$.

> [!solution]- Solution
> **(c).** Every magnetic field obeys $\nabla\cdot\mathbf{B} = 0$: there is no magnetic charge for field lines to start or end on. Test each option:
>
> - (a) $\nabla\cdot\mathbf{B} = \dfrac{B_0}{a}(1+1) = \dfrac{2B_0}{a}\ne0$: impossible.
> - (b) $\nabla\cdot\mathbf{B} = \dfrac{B_0}{a}(1-1+1) = \dfrac{B_0}{a}\ne0$: impossible. Two terms cancel, but the $z$ term survives.
> - (c) $\nabla\cdot\mathbf{B} = \dfrac{B_0}{a}\Big(\dfrac{\partial y}{\partial x}-\dfrac{\partial x}{\partial y}\Big) = 0$: allowed.
> - (d) $\nabla\cdot\mathbf{B} = \dfrac{1}{r^2}\dfrac{\partial}{\partial r}(r^2B_0) = \dfrac{2B_0}{r}\ne0$: the field of a magnetic "point charge", which does not exist.
>
> The current follows from $\nabla\times\mathbf{H} = \mathbf{J}$. Only the $z$ component of the curl survives:
> $$
> J_z = \frac{1}{\mu_0}\Big(\frac{\partial B_y}{\partial x}-\frac{\partial B_x}{\partial y}\Big) = \frac{1}{\mu_0}\frac{B_0}{a}(-1-1)\ \Rightarrow\ \mathbf{J} = -\frac{2B_0}{\mu_0a}\hat{z},
> $$
> a uniform current density flowing along $-\hat{z}$.
>
> **Check:** in cylindrical coordinates (c) is $\mathbf{B} = -\dfrac{B_0r}{a}\hat\phi$: on the $+x$ axis it points along $-\hat{y}$, on the $+y$ axis along $+\hat{x}$, so it circulates clockwise seen from $+z$. Right-hand rule: thumb along the current, $-\hat{z}$, and the fingers curl clockwise seen from $+z$ ✓. Its size $B_0r/a = \mu_0\lvert J_z\rvert r/2$ is the field inside a uniformly filled wire, as Ampère's law gives ✓.
>
> **Answer.** Only (c). It is produced by the uniform current density $\mathbf{J} = -\dfrac{2B_0}{\mu_0a}\hat{z}$ A/m².

### 12.5 Counting current in delta functions

> [!easy] Easy · current density · delta functions
> In free space the current density is
> $$
> \mathbf{J} = \hat{z}\Big[4\,\delta(x-1)\,\delta(y-1) - 6y(1-y)\,\delta(x-2)\,\text{rect}\big(y-\tfrac12\big)\Big]\ \text{A/m}^2,
> $$
> with $x$ and $y$ in metres and $\text{rect}(u) = 1$ for $\lvert u\rvert<\tfrac12$, $0$ otherwise. (a) Describe the two pieces: what kind of current, where, which way, how strong. (b) Find the net current in the $+\hat{z}$ direction through the square $0<x<3$ m, $0<y<3$ m of the plane $z = 0$. (c) Repeat for the rectangle $1.5<x<3$ m, $0<y<3$ m.
>
> *Source: original.*

> [!hint]- Hint
> $I = \int_S J_z\,dx\,dy$. Each δ-function carries units of 1/m, removes one integral, and contributes only if its location lies inside the region.

> [!solution]- Solution
> (a) The first term has two δ's, so its coefficient is a current: a **line current of 4 A along $+\hat{z}$** on the line $x = 1$ m, $y = 1$ m. The second has one δ, so $6y(1-y)$ is a surface current density in A/m: a **strip** on the plane $x = 2$ m, $0<y<1$ m, carrying $\mathbf{J}_s = -6y(1-y)\hat{z}$ A/m. It flows along $-\hat{z}$, is zero at the strip's edges and peaks at 1.5 A/m at $y = 0.5$ m.
>
> (b) Both pieces lie inside the square. The δ's sift: the line gives $+4$ A. The strip gives the integral of $J_s$ *across the flow*:
> $$
> -\int_0^1 6y(1-y)\,dy = -\big[3y^2-2y^3\big]_0^1 = -1\ \text{A}.
> $$
> Net: $I = 4-1 = +3$ A.
>
> (c) The line at $x = 1$ m is outside $1.5<x<3$ m, so only the strip counts: $I = -1$ A, i.e. 1 A flowing along $-\hat{z}$.
>
> **Check:** units — $\delta(x-2)$ carries 1/m, so (A/m)$\times$(1/m) gives A/m², as $\mathbf{J}$ must be. And (b) minus (c) is $3-(-1) = 4$ A, the line current alone ✓.
>
> **Answer.** (a) A 4 A line current along $+\hat{z}$ at $x = y = 1$ m, and a strip on $x = 2$ m, $0<y<1$ m, carrying 1 A in total along $-\hat{z}$ (peak 1.5 A/m). (b) $+3$ A. (c) $-1$ A.

## Medium

### 12.6 The centre of a square loop

> [!medium] Medium · find the error · Biot–Savart · Ampère's law
> A square loop of side $a = 10$ cm lies in the plane $z = 0$ of free space, centred on the origin with its sides parallel to the axes, and carries $I = 5$ A counter-clockwise seen from $+z$. A student finds the field at the centre like this:
>
> *"Ampère's law on a circle of radius $r = a/4$ centred on the origin in the plane $z = 0$: no current pierces the disk inside it, so $I_{\text{enc}} = 0$ and $H\cdot2\pi r = 0$. Hence $\mathbf{H} = 0$ at the centre."*
>
> (a) What is wrong? (b) Find $\mathbf{H}$ and $\mathbf{B}$ at the centre with the Biot–Savart law. (c) Compare with the centre of a circular loop of radius $a/2$ carrying the same current.
>
> *Source: classic.*

> [!hint]- Hint
> Ampère's law fixes $\oint\mathbf{H}\cdot d\mathbf{l}$, not $\mathbf{H}$. Which way does the field of a flat loop point at points in the loop's own plane, and what is $\mathbf{H}\cdot d\mathbf{l}$ along the student's circle? For (b), integrate one side and multiply by four.

> [!solution]- Solution
> **(a) The slip.** Ampère's law gives $H$ only when symmetry makes $\mathbf{H}$ tangent to the path and constant along it, so that it comes out of the integral. Here every current element and every point of the student's circle lie in the plane $z = 0$, so $d\mathbf{l}\times\hat{R}$, and with it $\mathbf{H}$, is along $\pm\hat{z}$: perpendicular to the circle everywhere. Then $\mathbf{H}\cdot d\mathbf{l} = 0$ at every point and the circulation vanishes *whatever* $H$ is. (On that circle $\mathbf{H}$ is in fact along $\hat{z}$, between 53.0 and 54.7 A/m.) The equation $0 = 0$ is true and useless.
>
> **(b) Setup.** By symmetry the four sides contribute equally. Take the bottom side, $y = -h$ with $h = a/2$, carrying current along $+\hat{x}$. An element $dx\,\hat{x}$ at $(x,-h,0)$ sees the centre at $\mathbf{R} = -x\hat{x}+h\hat{y}$, $R = \sqrt{x^2+h^2}$, and $d\mathbf{l}\times\mathbf{R} = dx\,\hat{x}\times(-x\hat{x}+h\hat{y}) = h\,dx\,\hat{z}$. With $d\mathbf{B} = \mu_0I\,d\mathbf{l}\times\mathbf{R}/(4\pi R^3)$:
> $$
> \mathbf{B}_{\text{side}} = \frac{\mu_0Ih}{4\pi}\hat{z}\int_{-h}^{h}\frac{dx}{(x^2+h^2)^{3/2}} = \frac{\mu_0Ih}{4\pi}\cdot\frac{\sqrt2}{h^2}\hat{z} = \frac{\sqrt2\,\mu_0I}{2\pi a}\hat{z} = 1.41\times10^{-5}\,\hat{z}\ \text{T},
> $$
> using the antiderivative $x/(h^2\sqrt{x^2+h^2})$ from the straight-wire integral of Lecture 12. Four sides:
> $$
> \mathbf{B} = \frac{2\sqrt2\,\mu_0I}{\pi a}\hat{z} = 5.66\times10^{-5}\,\hat{z}\ \text{T},\qquad \mathbf{H} = \frac{\mathbf{B}}{\mu_0} = 45.0\,\hat{z}\ \text{A/m}.
> $$
> Direction by the right-hand rule: fingers along the current, counter-clockwise seen from $+z$, so the thumb points along $+\hat{z}$ at the centre, as $\hat{x}\times\hat{y} = \hat{z}$ for the bottom side says.
>
> **(c)** On a circle of radius $R = a/2$ every element is at distance $R$ with $d\mathbf{l}\perp\hat{R}$, so $B = \dfrac{\mu_0I}{4\pi R^2}\cdot2\pi R = \dfrac{\mu_0I}{2R} = \dfrac{\mu_0I}{a} = 6.28\times10^{-5}$ T. The square gives $2\sqrt2/\pi = 0.900$ of this: its corners are farther from the centre than the circle is.
>
> **Check:** the general finite-segment result $B = \dfrac{\mu_0I}{4\pi h}(\sin\alpha_2-\sin\alpha_1)$, with $\alpha_1,\alpha_2$ the angles of the segment's ends measured from the perpendicular, gives the same $1.41\times10^{-5}$ T per side for $\alpha = \mp45^\circ$.
>
> **Answer.** (a) $\mathbf{H}$ is perpendicular to the student's circle, so $\oint\mathbf{H}\cdot d\mathbf{l} = 0$ says nothing about $H$. (b) $\mathbf{H} = 45.0\,\hat{z}$ A/m and $\mathbf{B} = \dfrac{2\sqrt2\,\mu_0I}{\pi a}\hat{z} = 5.66\times10^{-5}\,\hat{z}$ T. (c) The circle gives $6.28\times10^{-5}$ T; the square gives 0.900 of that.

### 12.7 A wire with a nonuniform current

> [!medium] Medium · Ampère's law · cylindrical symmetry
> A long straight wire of radius $a = 1$ mm along the $z$ axis carries the current density $\mathbf{J} = J_0\dfrac{r}{a}\hat{z}$ for $r<a$, with $J_0 = 3\times10^6$ A/m². (a) Find the total current. (b) Find $\mathbf{H}$ inside and outside the wire. (c) Evaluate $H$ at $r = 0.5$ mm and $r = 2$ mm.
>
> *Source: classic.*

> [!hint]- Hint
> The current through a circle of radius $r$ is $\int_0^r J(r')\,2\pi r'\,dr'$ — not $J\cdot\pi r^2$, because $J$ varies with $r$.

> [!solution]- Solution
> **Setup.** Cylindrical symmetry and the right-hand rule give $\mathbf{H} = H_\phi(r)\hat\phi$; Ampère on a circle of radius $r$: $H_\phi\cdot2\pi r = I_{\text{enc}}(r)$.
>
> (a) $I = \displaystyle\int_0^a J_0\frac{r'}{a}\,2\pi r'\,dr' = \frac{2\pi J_0a^2}{3} = 2\pi\ \text{A}\approx6.28$ A.
>
> (b) Inside: $I_{\text{enc}} = \dfrac{2\pi J_0r^3}{3a}$, so $H_\phi = \dfrac{J_0r^2}{3a}$. Outside: $H_\phi = \dfrac{I}{2\pi r} = \dfrac{J_0a^2}{3r}$.
>
> (c) $H(0.5\text{ mm}) = \dfrac{J_0a}{12} = 250$ A/m; $\ H(2\text{ mm}) = \dfrac{J_0a}{6} = 500$ A/m.
>
> **Check:** both forms give $J_0a/3$ at $r = a$ (no surface current, no jump), and $\dfrac1r\dfrac{d}{dr}(rH_\phi) = J_0r/a = J_z$ inside ✓.
>
> **Answer.** $I = 2\pi J_0a^2/3\approx6.28$ A; $\mathbf{H} = \hat\phi\,J_0r^2/(3a)$ for $r<a$ and $\hat\phi\,J_0a^2/(3r)$ for $r>a$; 250 A/m and 500 A/m.

### 12.8 A hairpin of current

> [!medium] Medium · Biot–Savart · superposition
> A long thin wire in the plane $z = 0$ of free space is bent into a hairpin: it comes in from $x = -\infty$ along the line $y = a$, follows the semicircle of radius $a$ centred on the origin through $(a,0,0)$ to $(0,-a,0)$, and goes back out to $x = -\infty$ along the line $y = -a$. It carries $I = 3$ A, flowing along $+\hat{x}$ on the upper leg, and $a = 2$ cm. (a) Find $\mathbf{B}$ at the origin due to each of the three pieces. (b) Find the total $\mathbf{B}$ at the origin.
>
> *Source: classic.*

> [!hint]- Hint
> Each straight leg ends exactly opposite the origin, so seen from there it is half of an infinite wire. On the semicircle every element is at the same distance $a$ and perpendicular to $\hat{R}$.

> [!solution]- Solution
> **Setup.** Biot–Savart, $d\mathbf{B} = \dfrac{\mu_0I\,d\mathbf{l}\times\hat{R}}{4\pi R^2}$ with $\hat{R}$ from the element to the origin. All elements and the field point lie in the plane $z = 0$, so every $d\mathbf{B}$ is along $\pm\hat{z}$ and the pieces simply add.
>
> **Upper leg.** An element $dx\,\hat{x}$ at $(x,a,0)$, $-\infty<x<0$, has $\mathbf{R} = -x\hat{x}-a\hat{y}$ and $d\mathbf{l}\times\mathbf{R} = -a\,dx\,\hat{z}$, so
> $$
> \mathbf{B}_{\text{up}} = -\frac{\mu_0Ia}{4\pi}\hat{z}\int_{-\infty}^{0}\frac{dx}{(x^2+a^2)^{3/2}} = -\frac{\mu_0Ia}{4\pi}\cdot\frac{1}{a^2}\hat{z} = -\frac{\mu_0I}{4\pi a}\hat{z} = -1.5\times10^{-5}\,\hat{z}\ \text{T}.
> $$
> That is half of the infinite-wire value $\mu_0I/(2\pi a)$, as it must be. Right-hand rule: thumb along $+\hat{x}$; below the wire, where the origin is, the fingers point along $-\hat{z}$ ✓.
>
> **Semicircle.** Every element is at $R = a$ with $d\mathbf{l}\perp\hat{R}$. At $(a,0,0)$ the current flows along $-\hat{y}$ and $\hat{R} = -\hat{x}$, so $d\mathbf{l}\times\hat{R}$ points along $(-\hat{y})\times(-\hat{x}) = -\hat{z}$. Adding up the length $\pi a$:
> $$
> \mathbf{B}_{\text{arc}} = -\frac{\mu_0I}{4\pi a^2}\,\pi a\,\hat{z} = -\frac{\mu_0I}{4a}\hat{z} = -4.71\times10^{-5}\,\hat{z}\ \text{T}.
> $$
> The arc runs clockwise seen from $+z$; with the fingers curled clockwise, the right-hand rule puts the thumb along $-\hat{z}$ ✓.
>
> **Lower leg.** The current flows along $-\hat{x}$ at $y = -a$: $(-\hat{x})\times(-x\hat{x}+a\hat{y}) = -a\,\hat{z}$ and the same integral, so $\mathbf{B}_{\text{low}} = -1.5\times10^{-5}\,\hat{z}$ T.
>
> **Total.**
> $$
> \mathbf{B} = -\frac{\mu_0I}{4a}\Big(1+\frac{2}{\pi}\Big)\hat{z} = -7.71\times10^{-5}\,\hat{z}\ \text{T}.
> $$
>
> **Check:** all three pieces circulate the same way around the origin (clockwise seen from $+z$), so nothing cancels. The arc is half of a full clockwise loop, $\mu_0I/(2a) = 9.42\times10^{-5}$ T. The two legs together give $3\times10^{-5}$ T, half of the $6\times10^{-5}$ T that two infinite antiparallel wires $2a$ apart give at their midpoint.
>
> **Answer.** Each leg: $-1.5\times10^{-5}\,\hat{z}$ T; semicircle: $-4.71\times10^{-5}\,\hat{z}$ T; total $\mathbf{B} = -\dfrac{\mu_0I}{4a}\Big(1+\dfrac{2}{\pi}\Big)\hat{z} = -7.71\times10^{-5}\,\hat{z}$ T.

## Hard

### 12.9 A rectangular loop beside a wire

> [!hard] Hard · magnetic force · nonuniform field · Newton's third law
> An infinitely long wire on the $z$ axis carries $I_1 = 20$ A along $+\hat{z}$ in free space. A rigid rectangular loop lies in the plane $y = 0$. Its long sides are the segments $x = d = 1$ cm and $x = d+b = 3$ cm for $0<z<L$, with $L = 10$ cm, joined by short sides along $z = 0$ and $z = L$. The loop carries $I_2 = 5$ A, flowing along $+\hat{z}$ on its near side ($x = d$), i.e. around the path $(d,0,0)\to(d,0,L)\to(d+b,0,L)\to(d+b,0,0)\to(d,0,0)$.
>
> (a) Find the wire's $\mathbf{B}$ in the plane of the loop, and its values on the two long sides.
>
> (b) Find the force on each of the four sides.
>
> (c) Find the net force on the loop. Is the loop attracted or repelled?
>
> (d) What force does the loop exert on the wire? Check (c) in the limits $b\to0$ and $b\to\infty$.
>
> *Source: classic.*

> [!hint]- Hint
> In the half-plane $y = 0$, $x>0$, the wire's field points along $+\hat{y}$ and depends on $x$ only. Apply $d\mathbf{F} = I_2\,d\mathbf{l}\times\mathbf{B}$ side by side. The short sides need an integral over $x$, but compare them before you do it.

> [!solution]- Solution
> **Setup.** The wire's field is $\mathbf{B} = \dfrac{\mu_0I_1}{2\pi r}\hat\phi$. In the half-plane $y = 0$, $x>0$, $r = x$, and by the right-hand rule (thumb along $+\hat{z}$) $\hat\phi = \hat{z}\times\hat{x} = +\hat{y}$. Each side of the loop is a straight current in this field, with force $\int I_2\,d\mathbf{l}\times\mathbf{B}$. A useful shorthand: $\mu_0I_1I_2/(2\pi) = 2\times10^{-5}$ N.
>
> **(a)** $\mathbf{B} = \dfrac{\mu_0I_1}{2\pi x}\hat{y}$: $4\times10^{-4}\,\hat{y}$ T on the near side ($x = 1$ cm) and $1.33\times10^{-4}\,\hat{y}$ T on the far side ($x = 3$ cm).
>
> **(b)** Near side, $d\mathbf{l} = dz\,\hat{z}$, with the same field all along it:
> $$
> \mathbf{F}_{\text{near}} = I_2L\,\hat{z}\times\frac{\mu_0I_1}{2\pi d}\hat{y} = -\frac{\mu_0I_1I_2L}{2\pi d}\hat{x} = -2\times10^{-4}\,\hat{x}\ \text{N},
> $$
> since $\hat{z}\times\hat{y} = -\hat{x}$: toward the wire, as parallel currents attract. Far side, current along $-\hat{z}$:
> $$
> \mathbf{F}_{\text{far}} = +\frac{\mu_0I_1I_2L}{2\pi(d+b)}\hat{x} = 6.67\times10^{-5}\,\hat{x}\ \text{N},
> $$
> away from the wire, as antiparallel currents repel. Top side ($z = L$, current along $+\hat{x}$): $d\mathbf{F} = I_2\,dx\,\hat{x}\times B(x)\hat{y} = I_2B(x)\,dx\,\hat{z}$, so
> $$
> \mathbf{F}_{\text{top}} = \frac{\mu_0I_1I_2}{2\pi}\hat{z}\int_d^{d+b}\frac{dx}{x} = \frac{\mu_0I_1I_2}{2\pi}\ln\frac{d+b}{d}\,\hat{z} = (2\times10^{-5})(\ln3)\,\hat{z} = 2.20\times10^{-5}\,\hat{z}\ \text{N}.
> $$
> Bottom side ($z = 0$): the same field and the opposite current, so $\mathbf{F}_{\text{bot}} = -2.20\times10^{-5}\,\hat{z}$ N.
>
> **(c)** The short-side forces cancel. The long-side forces do not, because the near side sits in the stronger field:
> $$
> \mathbf{F} = -\frac{\mu_0I_1I_2L}{2\pi}\Big(\frac1d-\frac1{d+b}\Big)\hat{x} = -\frac{\mu_0I_1I_2Lb}{2\pi d(d+b)}\hat{x} = -(2\times10^{-6}\ \text{N}\cdot\text{m})(66.7\ \text{m}^{-1})\,\hat{x} = -1.33\times10^{-4}\,\hat{x}\ \text{N}.
> $$
> The loop is **attracted** toward the wire.
>
> **(d)** By Newton's third law the loop pulls the wire with $+1.33\times10^{-4}\,\hat{x}$ N, toward the loop. (Integrating $I_1\,d\mathbf{l}\times\mathbf{B}_{\text{loop}}$ along the wire, with the loop's own Biot–Savart field, gives the same.)
>
> **Check:** as $b\to0$, $1/d-1/(d+b)\to0$: the two long sides fall on top of each other with opposite currents, and the force vanishes ✓. As $b\to\infty$, only the near side is left, $-\mu_0I_1I_2L/(2\pi d)\,\hat{x} = -2\times10^{-4}\,\hat{x}$ N ✓. Units: $\mu_0I_1I_2/(2\pi)$ is in newtons and $Lb/[d(d+b)]$ is dimensionless ✓.
>
> **Watch out:** in a *uniform* field the net force on any closed loop is zero, since $\oint I\,d\mathbf{l} = 0$. The answer here exists only because $B$ falls off with $x$, so never evaluate $B$ at the loop's centre and multiply.
>
> **Answer.** (a) $\mathbf{B} = \dfrac{\mu_0I_1}{2\pi x}\hat{y}$: $4\times10^{-4}\,\hat{y}$ T and $1.33\times10^{-4}\,\hat{y}$ T. (b) $-2\times10^{-4}\,\hat{x}$ N (near), $6.67\times10^{-5}\,\hat{x}$ N (far), $\pm2.20\times10^{-5}\,\hat{z}$ N (top, bottom). (c) $-1.33\times10^{-4}\,\hat{x}$ N: attracted. (d) $+1.33\times10^{-4}\,\hat{x}$ N on the wire.

### 12.10 Two crossing line currents

> [!hard] Hard · superposition · null points · Lorentz force
> Two infinitely long, thin, insulated wires cross at the origin in free space. One lies along the $z$ axis and carries 3 A along $+\hat{z}$; the other lies along the $x$ axis and carries 1 A along $-\hat{x}$.
>
> (a) Find $\mathbf{B}$ at $P = (2,0,1)$ m: each wire's contribution, with its direction, and the total.
>
> (b) Find $\mathbf{B}$ at a general point $(x,y,z)$ off the wires.
>
> (c) Find every point where $\mathbf{B} = 0$.
>
> (d) A proton passes through $P$ with velocity $\mathbf{v} = 10^5\,\hat{x}$ m/s. Find the magnetic force on it, and the uniform electric field $\mathbf{E}$ that would make the total Lorentz force on it zero.
>
> *Source: Summer 2020 HE2 #2a style (cf. Summer 2017 HE2 #1a for the z- and x-axis wire pair).*

> [!hint]- Hint
> For each wire use $\mathbf{B} = \dfrac{\mu_0I}{2\pi r}\hat\phi$ with $r$ the distance from *that* wire and $\hat\phi = \hat{u}\times\hat{r}$, where $\hat{u}$ is the current direction and $\hat{r}$ points perpendicularly from the wire to the field point. For (c), first ask which components each wire can produce.

> [!solution]- Solution
> **Setup.** Superpose two infinite-wire fields. For a wire through the origin along $\hat{u}$, the perpendicular from the wire to the point $\mathbf{r}$ is $\mathbf{r}_\perp = \mathbf{r}-(\mathbf{r}\cdot\hat{u})\hat{u}$, and the right-hand rule (thumb along the current) gives $\hat\phi = \hat{u}\times\mathbf{r}_\perp/r_\perp$.
>
> **(a)** At $P$:
>
> - $z$ wire: $\mathbf{r}_\perp = 2\hat{x}$, $r = 2$ m, $\hat\phi = \hat{z}\times\hat{x} = +\hat{y}$, so $\mathbf{B}_1 = \dfrac{\mu_0(3)}{2\pi(2)}\hat{y} = \dfrac{3\mu_0}{4\pi}\hat{y} = 3\times10^{-7}\,\hat{y}$ T.
> - $x$ wire: $\mathbf{r}_\perp = \hat{z}$, $r = 1$ m, $\hat\phi = (-\hat{x})\times\hat{z} = +\hat{y}$, so $\mathbf{B}_2 = \dfrac{\mu_0(1)}{2\pi(1)}\hat{y} = \dfrac{\mu_0}{2\pi}\hat{y} = 2\times10^{-7}\,\hat{y}$ T.
>
> Total: $\mathbf{B}(P) = \dfrac{5\mu_0}{4\pi}\hat{y} = 5\times10^{-7}\,\hat{y}$ T.
>
> **(b)** For the $z$ wire, $\mathbf{r}_\perp = x\hat{x}+y\hat{y}$ and $\hat{z}\times\mathbf{r}_\perp = -y\hat{x}+x\hat{y}$. For the $x$ wire, $\mathbf{r}_\perp = y\hat{y}+z\hat{z}$ and $(-\hat{x})\times\mathbf{r}_\perp = z\hat{y}-y\hat{z}$. With $B = \mu_0I/(2\pi r_\perp)$ and $\hat\phi = \hat{u}\times\mathbf{r}_\perp/r_\perp$:
> $$
> \mathbf{B} = \frac{3\mu_0}{2\pi}\,\frac{-y\hat{x}+x\hat{y}}{x^2+y^2}+\frac{\mu_0}{2\pi}\,\frac{z\hat{y}-y\hat{z}}{y^2+z^2}\ \ \text{T}\qquad(x,y,z\ \text{in m}).
> $$
> At $P$ this gives $\dfrac{3\mu_0}{2\pi}\cdot\dfrac24+\dfrac{\mu_0}{2\pi}\cdot\dfrac11 = \dfrac{5\mu_0}{4\pi}$ along $\hat{y}$, as in (a) ✓.
>
> **(c)** $B_x = -\dfrac{3\mu_0}{2\pi}\dfrac{y}{x^2+y^2}$ vanishes only for $y = 0$, and then $B_z = 0$ too. On the plane $y = 0$ both fields are along $\hat{y}$:
> $$
> \mathbf{B} = \frac{\mu_0}{2\pi}\Big(\frac3x+\frac1z\Big)\hat{y} = 0\quad\Longleftrightarrow\quad z = -\frac{x}{3}.
> $$
> So $\mathbf{B} = 0$ on the whole line $y = 0$, $z = -x/3$ (origin excluded), e.g. at $(3,0,-1)$ m and $(-3,0,1)$ m. There the two fields are equal in size ($3/\lvert x\rvert = 1/\lvert z\rvert$) and opposite in direction ($x$ and $z$ have opposite signs).
>
> **(d)** $\mathbf{F} = e\,\mathbf{v}\times\mathbf{B} = e\,(10^5)(5\times10^{-7})\,\hat{x}\times\hat{y} = e\,(0.05\ \text{V/m})\,\hat{z} = 8.01\times10^{-21}\,\hat{z}$ N. A zero total force needs $e(\mathbf{E}+\mathbf{v}\times\mathbf{B}) = 0$, so $\mathbf{E} = -\mathbf{v}\times\mathbf{B} = -0.05\,\hat{z}$ V/m: perpendicular to both $\mathbf{v}$ and $\mathbf{B}$, with $E/B = v = 10^5$ m/s, the velocity-selector condition.
>
> **Check:** at $P$ ($z = +1>0$) the two fields point the same way and add, consistent with (a). Along the line $x = 2$ m, $y = 0$, $B_y = \dfrac{\mu_0}{2\pi}\Big(\dfrac32+\dfrac1z\Big)$ vanishes only at $z = -\tfrac23$ m, the point of the null line of (c) (it also flips sign across the $x$ wire at $z = 0$, where it diverges).
>
> **Watch out:** the $x$ wire's current runs along $-\hat{x}$, so its field circulates the "wrong" way about the $+x$ axis. Always form $\hat\phi = \hat{u}\times\hat{r}$ with $\hat{u}$ along the current, not along the coordinate axis.
>
> **Answer.** (a) $3\times10^{-7}\,\hat{y}$ T from the $z$ wire and $2\times10^{-7}\,\hat{y}$ T from the $x$ wire; total $5\times10^{-7}\,\hat{y}$ T. (b) $\mathbf{B} = \dfrac{3\mu_0}{2\pi}\dfrac{-y\hat{x}+x\hat{y}}{x^2+y^2}+\dfrac{\mu_0}{2\pi}\dfrac{z\hat{y}-y\hat{z}}{y^2+z^2}$ T. (c) The line $y = 0$, $z = -x/3$ ($x\ne0$). (d) $\mathbf{F} = 8.01\times10^{-21}\,\hat{z}$ N; $\mathbf{E} = -0.05\,\hat{z}$ V/m.

### 12.11 A coax with unequal currents

> [!hard] Hard · Ampère's law · coaxial cable · enclosed current
> A coaxial cable lies along the $z$ axis, with free space between and around the conductors. The solid inner conductor ($r<a = 1$ mm) carries $I_1 = 3$ A along $+\hat{z}$; the outer conductor ($b = 2$ mm $<r<c = 6$ mm) carries $I_2 = 8$ A along $-\hat{z}$ (the rest of the return current takes another path). Both currents are spread uniformly over their cross-sections.
>
> (a) Find the current density $\mathbf{J}$ in each conductor.
>
> (b) Find $\mathbf{H}$ in all four regions.
>
> (c) Evaluate $H_\phi$ at $r = 0.5$, 1.5, 3, 5 and 10 mm.
>
> (d) At what radius $r>0$ does $\mathbf{H}$ vanish? Which way does $\mathbf{H}$ circulate outside the cable, seen from $+z$?
>
> *Source: classic.*

> [!hint]- Hint
> Ampère on a circle of radius $r$ traversed counter-clockwise seen from $+z$: $H_\phi\cdot2\pi r = I_{\text{enc}}(r)$, with current along $+\hat{z}$ counted positive. Inside the outer conductor only the fraction $(r^2-b^2)/(c^2-b^2)$ of $I_2$ is enclosed.

> [!solution]- Solution
> **Setup.** The currents depend only on $r$ and flow along $\pm\hat{z}$, so by symmetry $\mathbf{H} = H_\phi(r)\hat\phi$. Take a circle of radius $r$ traversed along $+\hat\phi$, counter-clockwise seen from $+z$. By the right-hand rule (fingers along the path, thumb along $+\hat{z}$) current along $+\hat{z}$ counts as positive: $H_\phi\cdot2\pi r = I_{\text{enc}}(r)$.
>
> **(a)** $\mathbf{J}_1 = \dfrac{I_1}{\pi a^2}\hat{z} = 9.55\times10^5\,\hat{z}$ A/m², $\qquad\mathbf{J}_2 = -\dfrac{I_2}{\pi(c^2-b^2)}\hat{z} = -7.96\times10^4\,\hat{z}$ A/m².
>
> **(b)** Counting the enclosed current region by region:
> $$
> H_\phi(r) = \begin{cases}\dfrac{I_1r}{2\pi a^2}, & r<a\quad(I_{\text{enc}} = I_1r^2/a^2)\\[8pt] \dfrac{I_1}{2\pi r}, & a<r<b\\[8pt] \dfrac{1}{2\pi r}\Big[I_1-I_2\,\dfrac{r^2-b^2}{c^2-b^2}\Big], & b<r<c\\[8pt] \dfrac{I_1-I_2}{2\pi r}, & r>c\quad(I_{\text{enc}} = -5\ \text{A}).\end{cases}
> $$
>
> **(c)**
> $$
> \begin{aligned}
> r &= 0.5\ \text{mm}: & I_{\text{enc}} &= 0.75\ \text{A}, & H_\phi &= 238.7\ \text{A/m}\\
> r &= 1.5\ \text{mm}: & I_{\text{enc}} &= 3\ \text{A}, & H_\phi &= 318.3\ \text{A/m}\\
> r &= 3\ \text{mm}: & I_{\text{enc}} &= 1.75\ \text{A}, & H_\phi &= 92.8\ \text{A/m}\\
> r &= 5\ \text{mm}: & I_{\text{enc}} &= -2.25\ \text{A}, & H_\phi &= -71.6\ \text{A/m}\\
> r &= 10\ \text{mm}: & I_{\text{enc}} &= -5\ \text{A}, & H_\phi &= -79.6\ \text{A/m}
> \end{aligned}
> $$
> For example at 3 mm: $I_{\text{enc}} = 3-8\cdot\dfrac{9-4}{36-4} = 1.75$ A.
>
> **(d)** $H = 0$ where $I_{\text{enc}} = 0$, which happens inside the outer conductor:
> $$
> \frac{r_0^2-b^2}{c^2-b^2} = \frac{I_1}{I_2} = \frac38\ \Rightarrow\ r_0^2 = 4+\tfrac38(32) = 16\ \text{mm}^2,\qquad r_0 = 4\ \text{mm}.
> $$
> Outside, $I_{\text{enc}} = -5$ A: the net current flows along $-\hat{z}$, so by the right-hand rule (thumb along $-\hat{z}$) $\mathbf{H}$ circulates along $-\hat\phi$, **clockwise seen from $+z$**. At $(10\ \text{mm},0,0)$, where $\hat\phi = \hat{y}$, $\mathbf{H} = -79.6\,\hat{y}$ A/m.
>
> **Check:** $H_\phi$ is continuous at $r = a$, $b$ and $c$ (477.5, 238.7 and $-132.6$ A/m from either side), as it must be with no surface currents. In the outer conductor $\dfrac1r\dfrac{d}{dr}(rH_\phi) = -\dfrac{I_2}{\pi(c^2-b^2)} = J_{2z}$ ✓, which is $\nabla\times\mathbf{H} = \mathbf{J}$.
>
> **Watch out:** inside the outer conductor $I_{\text{enc}}$ is *not* $I_1-I_2$; only the part of the return current inside radius $r$ is enclosed.
>
> **Answer.** (a) $9.55\times10^5\,\hat{z}$ and $-7.96\times10^4\,\hat{z}$ A/m². (b) As in the cases above. (c) $H_\phi = 238.7$, 318.3, 92.8, $-71.6$ and $-79.6$ A/m. (d) $r_0 = 4$ mm; outside, $\mathbf{H} = -\dfrac{5}{2\pi r}\hat\phi$ A/m, clockwise seen from $+z$.

### 12.12 A wire with an off-axis hole

> [!hard] Hard · Ampère's law · superposition · uniform field
> A long copper wire of radius $a = 3$ cm has its axis on the $z$ axis. A cylindrical hole of radius $b = 1$ cm runs through it parallel to the axis, centred on the line $x = d = 1.5$ cm, $y = 0$, so the hole lies entirely inside the metal. The wire carries $I = 40$ A along $+\hat{z}$, spread uniformly over the remaining metal; everything else is free space.
>
> (a) Find the current density $\mathbf{J}$.
>
> (b) Show that the field in the hole is uniform, and find $\mathbf{H}$ and $\mathbf{B}$ there.
>
> (c) For comparison, take a concentric hole ($d = 0$). Find $\mathbf{H}$ in the hole, and in the metal at $r = 2$ cm.
>
> (d) Back to the off-axis hole: find $\mathbf{H}$ at $(6\ \text{cm},0,0)$. Why can't Ampère's law alone give it, although $\oint\mathbf{H}\cdot d\mathbf{l} = 40$ A on the circle $r = 6$ cm?
>
> *Source: classic.*

> [!hint]- Hint
> Fill the hole: the wire is a solid cylinder of radius $a$ carrying $J\hat{z}$ plus a solid cylinder of radius $b$ (the hole) carrying $-J\hat{z}$. Inside a uniformly filled cylinder Ampère gives $\mathbf{H} = \tfrac12J\,\hat{z}\times\mathbf{r}_\perp$, with $\mathbf{r}_\perp$ measured from *that* cylinder's axis.

> [!solution]- Solution
> **Setup.** The off-centre hole destroys the cylindrical symmetry, so Ampère's law cannot be used on the wire directly. Superposition restores it: the holed wire is a solid cylinder of radius $a$ carrying $+J\hat{z}$, plus a solid cylinder of radius $b$ centred at $\mathbf{d} = d\hat{x}$ carrying $-J\hat{z}$. Each piece alone is cylindrically symmetric, and Ampère handles it.
>
> **(a)** $J = \dfrac{I}{\pi(a^2-b^2)} = \dfrac{40}{\pi(8\times10^{-4})} = \dfrac{5\times10^4}{\pi} = 1.59\times10^4$ A/m², along $+\hat{z}$. The two pieces carry $J\pi a^2 = 45$ A and $-J\pi b^2 = -5$ A: net 40 A ✓.
>
> **(b)** Inside a uniformly filled cylinder, Ampère on a circle of radius $r$ about its own axis gives $H_\phi\cdot2\pi r = J\pi r^2$, i.e. $\mathbf{H} = \tfrac12Jr\,\hat\phi = \tfrac12J\,\hat{z}\times\mathbf{r}_\perp$, because $\hat{z}\times\hat{r} = \hat\phi$. A point in the hole is at $\mathbf{r}_\perp$ from the wire's axis and at $\mathbf{r}_\perp-\mathbf{d}$ from the hole's axis, and lies inside both cylinders:
> $$
> \mathbf{H} = \tfrac12J\,\hat{z}\times\mathbf{r}_\perp-\tfrac12J\,\hat{z}\times(\mathbf{r}_\perp-\mathbf{d}) = \tfrac12J\,\hat{z}\times\mathbf{d}.
> $$
> The position has dropped out: the field is **uniform**. With $\mathbf{d} = d\hat{x}$ and $\hat{z}\times\hat{x} = \hat{y}$:
> $$
> \mathbf{H} = \frac{Jd}{2}\hat{y} = \frac{375}{\pi}\hat{y} = 119.4\,\hat{y}\ \text{A/m},\qquad \mathbf{B} = \mu_0\mathbf{H} = 1.5\times10^{-4}\,\hat{y}\ \text{T},
> $$
> perpendicular both to the current and to the line joining the two axes.
>
> **(c)** With $d = 0$ the same formula gives $\mathbf{H} = 0$ in the hole, and Ampère confirms it directly: the symmetry is back, and a circle inside the hole encloses no current. In the metal at $r = 2$ cm, $I_{\text{enc}} = J\pi(r^2-b^2) = 15$ A, so $\mathbf{H} = \dfrac{I_{\text{enc}}}{2\pi r}\hat\phi = 119.4\,\hat\phi$ A/m (the same size as in (b), a coincidence of these numbers).
>
> **(d)** Outside a cylindrically symmetric current, $\mathbf{H}$ is that of a line current on its axis. The point $(6\ \text{cm},0,0)$ lies on the $+x$ side of both axes, so for both $\hat{r} = \hat{x}$ and, thumb along $+\hat{z}$, $\hat\phi = \hat{z}\times\hat{x} = \hat{y}$:
> $$
> \mathbf{H} = \frac{45}{2\pi(0.06)}\hat{y}-\frac{5}{2\pi(0.045)}\hat{y} = (119.4-17.7)\,\hat{y} = 101.7\,\hat{y}\ \text{A/m},
> $$
> which is 0.958 of the 106.1 A/m a centred 40 A line would give: the "missing" current of the hole is on the near side. Ampère's law still holds (the circulation on $r = 6$ cm is exactly 40 A), but on that circle $\lvert\mathbf{H}\rvert$ varies from 101.7 to 108.8 A/m and $\mathbf{H}$ is not purely along $\hat\phi$, so $H$ cannot be pulled out of the integral.
>
> **Check:** a direct two-dimensional Biot–Savart sum over the metal's cross-section gives $119.4\,\hat{y}$ A/m at several points in the hole, and $101.7\,\hat{y}$ A/m at $(6\ \text{cm},0,0)$. For the concentric case, at $r = a$ the inside form $J(a^2-b^2)/(2a)$ and the outside form $I/(2\pi a)$ both give 212.2 A/m ✓.
>
> **Answer.** (a) $J = 5\times10^4/\pi = 1.59\times10^4$ A/m² along $+\hat{z}$. (b) $\mathbf{H} = \tfrac12J\,\hat{z}\times\mathbf{d} = 119.4\,\hat{y}$ A/m and $\mathbf{B} = 1.5\times10^{-4}\,\hat{y}$ T, the same everywhere in the hole. (c) $\mathbf{H} = 0$ in the hole; $119.4\,\hat\phi$ A/m at $r = 2$ cm. (d) $\mathbf{H} = 101.7\,\hat{y}$ A/m; the cylindrical symmetry Ampère's law needs is missing.

### Sources for this page
Course notes and slides, Lecture 12: the δ-function description of line and surface currents and Example 1's rect strip (the notation of 12.5), the five-step Biot–Savart integral and its antiderivative (12.6, 12.8), and the coax challenge question, extended to unequal currents in 12.11. Old exams, re-parameterized: Summer 2020 HE2 #2a (two crossing line currents, 12.10), with the z- and x-axis wire pair of Summer 2017 HE2 #1a. Classic textbook problems with new numbers: 12.2, 12.3, 12.4, 12.6, 12.8, 12.9, 12.11 and 12.12; 12.7 is the bank's classic nonuniform-wire exemplar. Problems 12.1 and 12.5 are original.

*Previous: [[practice/11-lorentz-drude-models|Lecture 11 practice]] · next: [[practice/13-current-sheets-solenoids-and-vector-potential|Lecture 13 practice]] · [[practice/index|all practice]]*
