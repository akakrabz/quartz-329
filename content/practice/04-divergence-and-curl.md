---
title: "Practice — Lecture 4: Divergence and curl"
description: "12 practice problems (5 easy, 3 medium, 4 hard) on divergence and curl in Cartesian, cylindrical and spherical coordinates, deciding whether a field can be electrostatic, the divergence theorem and Stokes' theorem, surface charge from a jump in D, and the continuity equation, each with a folded hint and a worked solution."
tags: [practice, electrostatics, exam-1]
lecture: 4
---

*Practice for [[1-electrostatics/04-divergence-and-curl|Lecture 4]] · concepts: [[concepts/divergence]] · [[concepts/curl]] · [[concepts/divergence-theorem]] · [[concepts/stokes-theorem]] · all practice: [[practice/index|hub]] · by difficulty: [[practice/easy|easy]] · [[practice/medium|medium]] · [[practice/hard|hard]] · [[practice/topics|by topic]]*

Work each problem on paper first. Open the **hint** only when stuck, and the **solution** only after you have an answer you would hand in. Every answer here has been checked numerically.

## Easy

### 4.1 Faucet or whirlpool

> [!easy] Easy · divergence · curl
> Two fields are given in free space, with $x$, $y$, $z$ in metres:
> $$
> \mathbf{E}_1 = 3x\,\hat{x} - y\,\hat{y} + 2z\,\hat{z}\ \text{V/m},\qquad \mathbf{E}_2 = 2y\,\hat{x} - 3x\,\hat{y}\ \text{V/m}.
> $$
> (a) Find the divergence and the curl of each field.
>
> (b) Which one could be an electrostatic field? For that one, find the charge density $\rho$.
>
> (c) Picture $\mathbf{E}_2$ as the velocity pattern of a flowing fluid. Which way would a small paddlewheel with its axle along $z$ turn, seen from $+z$?
>
> *Source: original.*

> [!hint]- Hint
> Divergence asks how each component changes *along* its own direction ($\partial E_x/\partial x$, …); curl asks how it changes *across* it ($\partial E_y/\partial x$, …). An electrostatic field must have zero curl.

> [!solution]- Solution
> **(a)** In $\mathbf{E}_1$ each component depends only on its own coordinate, so the field changes only *along* its direction:
> $$
> \nabla\cdot\mathbf{E}_1 = \frac{\partial(3x)}{\partial x}+\frac{\partial(-y)}{\partial y}+\frac{\partial(2z)}{\partial z} = 3-1+2 = 4\ \text{V/m}^2 .
> $$
> Every curl term is a cross-derivative such as $\partial E_{1y}/\partial x = \partial(-y)/\partial x = 0$, so $\nabla\times\mathbf{E}_1 = 0$. In $\mathbf{E}_2$ it is the other way round: $E_{2x} = 2y$ depends only on $y$ and $E_{2y} = -3x$ only on $x$, so $\nabla\cdot\mathbf{E}_2 = 0$, while
> $$
> \nabla\times\mathbf{E}_2 = \hat{z}\Big(\frac{\partial E_{2y}}{\partial x}-\frac{\partial E_{2x}}{\partial y}\Big) = \hat{z}\,(-3-2) = -5\,\hat{z}\ \text{V/m}^2 .
> $$
> (The $\hat{x}$ and $\hat{y}$ components vanish because nothing depends on $z$ and $E_{2z} = 0$.)
>
> **(b)** A static field must be curl-free, so only $\mathbf{E}_1$ qualifies. It is a uniform "faucet":
> $$
> \rho = \epsilon_0\nabla\cdot\mathbf{E}_1 = 4\epsilon_0\approx3.54\times10^{-11}\ \text{C/m}^3\quad\text{everywhere}.
> $$
> $\mathbf{E}_2$ is a "whirlpool": it has no charge anywhere, but it has curl, which only a changing magnetic field can supply ($\nabla\times\mathbf{E} = -\partial\mathbf{B}/\partial t$).
>
> **(c)** The curl points along $-\hat{z}$, so by the right-hand rule the wheel turns **clockwise seen from $+z$**. Check with two arrows. At $(0,1,0)$, above the axle, $\mathbf{E}_2 = +2\hat{x}$ pushes to the right. At $(1,0,0)$, to the right of the axle, $\mathbf{E}_2 = -3\hat{y}$ pushes down. Top going right and right side going down is clockwise ✓.
>
> **Watch out:** the $\hat{z}$ component is $\partial E_y/\partial x-\partial E_x/\partial y$, in that order. Reversed, it gives $+5\hat{z}$ and the wrong spin.
>
> **Answer.** $\nabla\cdot\mathbf{E}_1 = 4$ V/m², $\nabla\times\mathbf{E}_1 = 0$; $\nabla\cdot\mathbf{E}_2 = 0$, $\nabla\times\mathbf{E}_2 = -5\hat{z}$ V/m². Only $\mathbf{E}_1$ can be electrostatic, with $\rho = 4\epsilon_0\approx3.54\times10^{-11}$ C/m³. The paddlewheel in $\mathbf{E}_2$ turns clockwise seen from $+z$.

### 4.2 Curl-free but not charge-free

> [!easy] Easy · multiple choice · curl · divergence
> In a region of free space the electric field is $\mathbf{E} = (z^2+2y)\,\hat{x} + (2x-3)\,\hat{y} + 2xz\,\hat{z}$ V/m, with coordinates in metres. Which **one** of the following statements is **false**?
>
> (a) $\nabla\times\mathbf{E} = 0$ everywhere.
>
> (b) $\oint_C\mathbf{E}\cdot d\mathbf{l} = 0$ around every closed path $C$.
>
> (c) The charge density is $\rho = 2\epsilon_0x$ C/m³: positive for $x>0$, negative for $x<0$.
>
> (d) Because $\nabla\times\mathbf{E} = 0$, the region contains no charge.
>
> (e) $\int\mathbf{E}\cdot d\mathbf{l}$ from $(0,0,0)$ to $(1,2,3)$ m equals 7 V along every path.
>
> *Source: original.*

> [!hint]- Hint
> Curl and divergence answer different questions. Compute both (each takes one line) before you read the options.

> [!solution]- Solution
> **(d) is false.** Work out both derivatives first:
> $$
> \begin{aligned}
> \nabla\times\mathbf{E} &= \hat{x}\Big(\frac{\partial(2xz)}{\partial y}-\frac{\partial(2x-3)}{\partial z}\Big)+\hat{y}\Big(\frac{\partial(z^2+2y)}{\partial z}-\frac{\partial(2xz)}{\partial x}\Big)+\hat{z}\Big(\frac{\partial(2x-3)}{\partial x}-\frac{\partial(z^2+2y)}{\partial y}\Big)\\
> &= \hat{x}\,(0-0)+\hat{y}\,(2z-2z)+\hat{z}\,(2-2) = 0,\\
> \nabla\cdot\mathbf{E} &= 0+0+2x = 2x\ \text{V/m}^2 .
> \end{aligned}
> $$
>
> - (a) **True**, as just computed.
> - (b) **True**: by Stokes' theorem, $\oint_C\mathbf{E}\cdot d\mathbf{l} = \int_S(\nabla\times\mathbf{E})\cdot d\mathbf{S} = 0$ for every loop.
> - (c) **True**: $\rho = \epsilon_0\nabla\cdot\mathbf{E} = 2\epsilon_0x$, for example $1.77\times10^{-11}$ C/m³ at $x = 1$ m. It vanishes only on the plane $x = 0$.
> - (d) **False**: (c) shows charge almost everywhere. Zero curl says the field is conservative; it says nothing about sources. Sources are measured by the divergence.
> - (e) **True**: by (b) the integral is path-independent, so take the staircase $(0,0,0)\to(1,0,0)\to(1,2,0)\to(1,2,3)$. On the first leg $y = z = 0$, so $E_x = 0$; on the second $E_y = 2(1)-3 = -1$ V/m over 2 m; on the third $E_z = 2z$. Total: $0+(-1)(2)+\int_0^3 2z\,dz = -2+9 = 7$ V.
>
> **Check:** $\mathbf{E} = -\nabla f$ with $f = -(xz^2+2xy-3y)$, and the gradient theorem gives $f(0,0,0)-f(1,2,3) = 0-(-7) = 7$ V ✓. This is also *why* the curl vanished: $\nabla\times(\nabla f) = 0$ for every $f$.
>
> **Answer.** (d). The field is curl-free, yet it carries the charge density $\rho = 2\epsilon_0x$ C/m³.

### 4.3 Along or across the flow

> [!easy] Easy · true or false · divergence · curl
> True or false? Give a one-line reason for each. Here $E_0$, $a$, $k$ and $Q$ are positive constants; $r$ is the distance from the origin in (c) and from the $z$ axis in (d).
>
> (a) The field $\mathbf{F} = E_0e^{-y/a}\,\hat{x}$ has zero divergence everywhere.
>
> (b) A small paddlewheel with its axle along $z$, placed in the flow $\mathbf{F}$ of (a), turns counter-clockwise seen from $+z$.
>
> (c) The Coulomb field $\mathbf{E} = \dfrac{Q}{4\pi\epsilon_0r^2}\,\hat{r}$ gets weaker along its own direction, so its divergence is nonzero at every point away from the charge.
>
> (d) The field $\mathbf{v} = \dfrac{k}{r}\,\hat\phi$ circulates around the $z$ axis, so its curl is nonzero at every point.
>
> *Source: original.*

> [!hint]- Hint
> For a field whose arrows all point the same way, divergence comes from change *along* the arrows and curl from change *across* them. When the arrows spread out or bend, use the formula in spherical or cylindrical coordinates instead.

> [!solution]- Solution
> - **(a) True.** $\mathbf{F}$ points along $\hat{x}$ and changes only with $y$, across its direction: $\nabla\cdot\mathbf{F} = \partial F_x/\partial x = 0$.
> - **(b) True.** $(\nabla\times\mathbf{F})_z = \dfrac{\partial F_y}{\partial x}-\dfrac{\partial F_x}{\partial y} = +\dfrac{E_0}{a}e^{-y/a}>0$, so the spin axis is $+\hat{z}$: counter-clockwise seen from $+z$. Physically, the paddles below the axle (smaller $y$) are pushed toward $+x$ harder than the paddles above it.
> - **(c) False.** In spherical coordinates, $\nabla\cdot\mathbf{E} = \dfrac{1}{r^2}\dfrac{\partial}{\partial r}\Big(r^2\cdot\dfrac{Q}{4\pi\epsilon_0r^2}\Big) = 0$ for $r>0$. The weakening is exactly compensated by the spreading of the field lines; all the divergence sits at the charge.
> - **(d) False.** In cylindrical coordinates, $(\nabla\times\mathbf{v})_z = \dfrac1r\dfrac{\partial(rv_\phi)}{\partial r} = \dfrac1r\dfrac{\partial k}{\partial r} = 0$ for $r>0$, and the other two components vanish because nothing depends on $\phi$ or $z$. Yet the circulation around any circle centred on the axis is $\dfrac{k}{r}\cdot2\pi r = 2\pi k\ne0$. By Stokes' theorem the curl must therefore be concentrated *on the axis*, just like the magnetic field of a thin wire, whose current flows along the axis.
>
> **Watch out:** the "along the flow" and "across the flow" rules are exact only for fields whose arrows all point the same way. For the curved fields in (c) and (d) the geometry adds a term, so use the formula.
>
> **Answer.** (a) True. (b) True. (c) False. (d) False.

### 4.4 The missing metric factor

> [!easy] Easy · find the error · cylindrical coordinates
> Inside a long cylinder of radius $a = 3$ cm on the $z$ axis, the flux density is $\mathbf{D} = D_0\,(r/a)^2\,\hat{r}$ with $D_0 = 6\ \mu$C/m², where $r$ is the distance from the $z$ axis. A student finds the charge density at $r = a/2$:
>
> *"$\rho = \nabla\cdot\mathbf{D} = \dfrac{\partial D_r}{\partial r} = \dfrac{2D_0r}{a^2}$, so $\rho(a/2) = \dfrac{D_0}{a} = 200\ \mu$C/m³."*
>
> What is wrong? Find the correct $\rho(a/2)$.
>
> *Source: original.*

> [!hint]- Hint
> Look up the divergence in cylindrical coordinates. What does the factor $\frac1r\frac{\partial}{\partial r}(r\,\cdot\,)$ account for that $\partial/\partial r$ alone misses?

> [!solution]- Solution
> **The slip:** $\nabla\cdot\mathbf{D} = \partial D_r/\partial r$ is the Cartesian formula applied to a cylindrical component. In cylindrical coordinates the radial term carries a metric factor, because a cylinder at larger $r$ has more area and the field lines spread out:
> $$
> \nabla\cdot\mathbf{D} = \frac1r\frac{\partial(rD_r)}{\partial r} = \frac1r\frac{\partial}{\partial r}\Big(\frac{D_0r^3}{a^2}\Big) = \frac{3D_0r}{a^2}.
> $$
> Expanded, $\frac1r\frac{\partial(rD_r)}{\partial r} = \frac{\partial D_r}{\partial r}+\frac{D_r}{r}$: the student kept the first term and lost $D_r/r = D_0r/a^2$. At $r = a/2$:
> $$
> \rho = \frac{3D_0}{2a} = \frac{3\times6\times10^{-6}}{2\times0.03} = 300\ \mu\text{C/m}^3 .
> $$
> **Check** with Gauss's law on a cylinder of radius $r$ and length $L$: the flux is $D_r\cdot2\pi rL = 2\pi LD_0r^3/a^2$, and the charge from the corrected density is $\int_0^r\frac{3D_0r'}{a^2}\,2\pi r'L\,dr' = 2\pi LD_0r^3/a^2$ ✓. The student's density would enclose only $\tfrac{4\pi}{3}LD_0r^3/a^2$, two thirds of the flux.
>
> **Answer.** The student dropped the cylindrical metric factor: $\nabla\cdot\mathbf{D} = \frac1r\frac{\partial(rD_r)}{\partial r} = 3D_0r/a^2$, so $\rho(a/2) = 3D_0/(2a) = 300\ \mu$C/m³, not 200.

### 4.5 Draining a cube

> [!easy] Easy · continuity · divergence theorem
> In a region of space the current density is $\mathbf{J} = 4x\,\hat{x} + 2y\,\hat{y} - z\,\hat{z}$ A/m², with coordinates in metres.
>
> (a) Find $\partial\rho/\partial t$ at any point.
>
> (b) At what rate does the total charge inside the cube $0<x<0.5$ m, $0<y<0.5$ m, $0<z<0.5$ m change? Is the cube gaining or losing charge?
>
> *Source: classic.*

> [!hint]- Hint
> Charge is conserved: $\nabla\cdot\mathbf{J} = -\partial\rho/\partial t$. Current flowing out of a point drains the charge there.

> [!solution]- Solution
> **(a)** The continuity equation gives
> $$
> \frac{\partial\rho}{\partial t} = -\nabla\cdot\mathbf{J} = -(4+2-1) = -5\ \text{A/m}^3\quad(\text{C/m}^3\ \text{per second}),
> $$
> the same at every point, even though $\mathbf{J}$ itself varies.
>
> **(b)** Integrate over the cube, whose volume is $0.5^3 = 0.125$ m³:
> $$
> \frac{dQ}{dt} = \int_V\frac{\partial\rho}{\partial t}\,dV = -5\times0.125 = -0.625\ \text{A}.
> $$
> The cube is **losing** charge at 0.625 C/s.
>
> **Check** with the divergence theorem, face by face (each face has area 0.25 m²). On $x = 0.5$ m, $J_x = 2$ A/m², so $+0.5$ A flows out. On $y = 0.5$ m, $J_y = 1$ A/m², so $+0.25$ A flows out. On $z = 0.5$ m, $J_z = -0.5$ A/m², so 0.125 A flows *in* ($-0.125$ A out). The faces on $x = 0$, $y = 0$ and $z = 0$ carry nothing, because the normal component ($4x$, $2y$ or $-z$) vanishes there. The net outward current is $0.5+0.25-0.125 = 0.625$ A $= -dQ/dt$ ✓.
>
> **Answer.** $\partial\rho/\partial t = -5$ A/m³ (C/m³ per second) everywhere; $dQ/dt = -0.625$ A, so the cube loses charge at 0.625 C/s.

## Medium

### 4.6 Three fields in curved coordinates

> [!medium] Medium · curvilinear coordinates · curl · divergence
> Three fields in free space are given below, with $E_0 = 5$ V/m and $a = 10$ cm. In (a), $r$ is the distance from the $z$ axis (cylindrical coordinates); in (b) and (c), $(r,\theta,\phi)$ are spherical coordinates and $r>0$. For each field, find the divergence and the curl.
>
> (a) $\mathbf{E}_1 = E_0\dfrac{r}{a}\,\hat\phi$
>
> (b) $\mathbf{E}_2 = E_0\dfrac{a^2}{r^2}\cos\theta\,\hat{r}$
>
> (c) $\mathbf{E}_3 = E_0\Big[\dfrac{a^3}{r^3}\big(2\cos\theta\,\hat{r}+\sin\theta\,\hat\theta\big)+\dfrac{r}{a}\,\hat{r}\Big]$
>
> (d) Which of the three could be an electrostatic field? For that one, find the charge density $\rho$.
>
> *Source: original.*

> [!hint]- Hint
> Copy the cylindrical or spherical formulas from the [[0-toolkit/02-vector-calculus-cheatsheet|cheat sheet]] and cross out every term whose component is zero or does not depend on that coordinate; only one or two terms survive each time. In (b) the field is radial, but does its strength depend on $r$ alone?

> [!solution]- Solution
> **Setup.** Work in the coordinates each field is written in, with the metric factors of the curvilinear formulas. No field depends on $\phi$ and none has more than two components, so only a few terms survive.
>
> **(a)** Only $E_\phi = E_0r/a$ is nonzero, and it depends on $r$ only:
> $$
> \nabla\cdot\mathbf{E}_1 = \frac1r\frac{\partial E_\phi}{\partial\phi} = 0,\qquad
> \nabla\times\mathbf{E}_1 = \hat{z}\,\frac1r\frac{\partial(rE_\phi)}{\partial r} = \hat{z}\,\frac1r\frac{\partial}{\partial r}\Big(\frac{E_0r^2}{a}\Big) = \frac{2E_0}{a}\,\hat{z} = 100\,\hat{z}\ \text{V/m}^2 .
> $$
> This is rigid rotation: a uniform whirlpool.
>
> **(b)** Only $E_r$ is nonzero, but it depends on $\theta$:
> $$
> \nabla\cdot\mathbf{E}_2 = \frac1{r^2}\frac{\partial}{\partial r}\big(r^2E_r\big) = \frac1{r^2}\frac{\partial}{\partial r}\big(E_0a^2\cos\theta\big) = 0,\qquad
> \nabla\times\mathbf{E}_2 = \hat\phi\,\frac1r\Big[\frac{\partial(rE_\theta)}{\partial r}-\frac{\partial E_r}{\partial\theta}\Big] = \hat\phi\,\frac{E_0a^2\sin\theta}{r^3}.
> $$
> With $E_0a^2 = 0.05$ V·m, the curl is $0.05\sin\theta/r^3$ V/m² along $\hat\phi$ ($r$ in metres). The arrows all lie along $\pm\hat{r}$, yet the field is strongest along the $z$ axis (outward above the equator, inward below) and zero at the equator. It varies *across* its own direction, so it has curl.
>
> **(c)** Split $\mathbf{E}_3$ into the first term in the bracket, $\mathbf{E}_d$ (with $E_r = 2E_0a^3\cos\theta/r^3$ and $E_\theta = E_0a^3\sin\theta/r^3$), and $\mathbf{E}_b = E_0(r/a)\,\hat{r}$. For $\mathbf{E}_d$:
> $$
> \begin{aligned}
> \nabla\cdot\mathbf{E}_d &= \frac1{r^2}\frac{\partial}{\partial r}\Big(\frac{2E_0a^3\cos\theta}{r}\Big)+\frac{1}{r\sin\theta}\frac{\partial}{\partial\theta}\Big(\frac{E_0a^3\sin^2\theta}{r^3}\Big) = -\frac{2E_0a^3\cos\theta}{r^4}+\frac{2E_0a^3\cos\theta}{r^4} = 0,\\
> (\nabla\times\mathbf{E}_d)_\phi &= \frac1r\Big[\frac{\partial}{\partial r}\Big(\frac{E_0a^3\sin\theta}{r^2}\Big)-\frac{\partial}{\partial\theta}\Big(\frac{2E_0a^3\cos\theta}{r^3}\Big)\Big] = \frac1r\Big[-\frac{2E_0a^3\sin\theta}{r^3}+\frac{2E_0a^3\sin\theta}{r^3}\Big] = 0 .
> \end{aligned}
> $$
> (The other curl components vanish because $E_\phi = 0$ and nothing depends on $\phi$; $\mathbf{E}_d$ is the field of a point dipole at the origin.) $\mathbf{E}_b$ is radial with a strength that depends on $r$ only, so it is curl-free, and $\nabla\cdot\mathbf{E}_b = \dfrac1{r^2}\dfrac{\partial}{\partial r}\Big(\dfrac{E_0r^3}{a}\Big) = \dfrac{3E_0}{a}$. Altogether $\nabla\times\mathbf{E}_3 = 0$ and $\nabla\cdot\mathbf{E}_3 = 3E_0/a = 150$ V/m².
>
> **(d)** Only $\mathbf{E}_3$ is curl-free, so only it can be electrostatic:
> $$
> \rho = \epsilon_0\nabla\cdot\mathbf{E}_3 = \frac{3\epsilon_0E_0}{a} = 150\,\epsilon_0\approx1.33\ \text{nC/m}^3,
> $$
> uniform for $r>0$. $\mathbf{E}_1$ and $\mathbf{E}_2$ have zero divergence (no charge) but nonzero curl, so they would need a changing magnetic field.
>
> **Check:** the flux of $\epsilon_0\mathbf{E}_3$ out of a sphere of radius $r$ should equal $\rho\cdot\tfrac43\pi r^3$. The dipole part has zero net flux because $\int_0^\pi\cos\theta\sin\theta\,d\theta = 0$, and the $\mathbf{E}_b$ part gives $\epsilon_0\dfrac{E_0r}{a}\cdot4\pi r^2 = \dfrac{3\epsilon_0E_0}{a}\cdot\dfrac43\pi r^3$ ✓.
>
> **Watch out:** "radial means curl-free" holds only when the strength depends on $r$ alone, as (b) shows.
>
> **Answer.** (a) $\nabla\cdot\mathbf{E}_1 = 0$, $\nabla\times\mathbf{E}_1 = 100\,\hat{z}$ V/m². (b) $\nabla\cdot\mathbf{E}_2 = 0$, $\nabla\times\mathbf{E}_2 = \hat\phi\,E_0a^2\sin\theta/r^3 = 0.05\sin\theta/r^3\,\hat\phi$ V/m² ($r$ in m). (c) $\nabla\cdot\mathbf{E}_3 = 150$ V/m², $\nabla\times\mathbf{E}_3 = 0$. (d) Only $\mathbf{E}_3$ can be electrostatic, with $\rho = 150\,\epsilon_0\approx1.33$ nC/m³.

### 4.7 Divergence theorem on a hemisphere

> [!medium] Medium · divergence theorem · flux
> In free space $\mathbf{D} = D_0\Big(\dfrac{x}{a}\,\hat{x}+\hat{z}\Big)$ with $D_0 = 6\ \mu$C/m² and $a = 0.5$ m. Consider the solid hemisphere $x^2+y^2+z^2\le a^2$, $z\ge0$.
>
> (a) Find the charge density $\rho$, and the total charge $Q$ inside the hemisphere by integrating $\rho$.
>
> (b) Find the outward flux of $\mathbf{D}$ through the flat base and through the curved dome separately.
>
> (c) Verify the divergence theorem.
>
> *Source: classic.*

> [!hint]- Hint
> On the dome, $d\mathbf{S} = \hat{r}\,a^2\sin\theta\,d\theta\,d\phi$ and $x = a\sin\theta\cos\phi$, so $\hat{x}\cdot\hat{r} = \sin\theta\cos\phi$. The uniform $\hat{z}$ part needs no integral over the dome: it has zero divergence, so what enters through the base must leave through the dome.

> [!solution]- Solution
> **Setup.** The divergence theorem says that the outward flux through the closed surface (base plus dome) equals the integral of $\nabla\cdot\mathbf{D} = \rho$ over the volume. Compute both sides independently.
>
> **(a)** $\nabla\cdot\mathbf{D} = \dfrac{\partial}{\partial x}\Big(\dfrac{D_0x}{a}\Big) = \dfrac{D_0}{a} = 12\ \mu$C/m³, uniform. The hemisphere's volume is $\tfrac23\pi a^3 = 0.2618$ m³, so
> $$
> Q = \frac{D_0}{a}\cdot\frac{2\pi a^3}{3} = \frac{2\pi a^2D_0}{3} = \pi\ \mu\text{C}\approx3.1416\ \mu\text{C}.
> $$
> **(b) Base** ($z = 0$, outward normal $-\hat{z}$). The $\hat{x}$ part is tangent to the base; the $\hat{z}$ part gives $\mathbf{D}\cdot(-\hat{z}) = -D_0$ over the area $\pi a^2$. Base flux $= -\pi a^2D_0\approx-4.712\ \mu$C.
>
> **Dome.** The uniform part $D_0\hat{z}$ is divergence-free, so its flux out through the dome equals its flux in through the base, $+\pi a^2D_0$. For the $\hat{x}$ part, $\mathbf{D}\cdot\hat{r} = D_0\sin^2\theta\cos^2\phi$ on $r = a$:
> $$
> \int_0^{2\pi}\!\!\int_0^{\pi/2}D_0\sin^2\theta\cos^2\phi\;a^2\sin\theta\,d\theta\,d\phi = D_0a^2\Big(\int_0^{\pi/2}\sin^3\theta\,d\theta\Big)\Big(\int_0^{2\pi}\cos^2\phi\,d\phi\Big) = D_0a^2\cdot\frac23\cdot\pi = \frac{2\pi a^2D_0}{3}.
> $$
> Dome flux $= \pi a^2D_0+\tfrac23\pi a^2D_0 = \tfrac53\pi a^2D_0\approx7.854\ \mu$C.
>
> **(c)** Base plus dome: $\big(-1+\tfrac53\big)\pi a^2D_0 = \tfrac23\pi a^2D_0 = \pi\ \mu$C $= Q$ ✓.
>
> **Check:** only the $\hat{x}$ part has divergence, and its dome flux alone, $\tfrac23\pi a^2D_0$, already equals $Q$. The $\hat{z}$ part contributes $-\pi a^2D_0$ to the base and $+\pi a^2D_0$ to the dome, nothing net, as a divergence-free field must.
>
> **Watch out:** the base's *outward* normal is $-\hat{z}$, not $+\hat{z}$. With the wrong sign, the base adds flux instead of removing it, and the theorem seems to fail.
>
> **Answer.** $\rho = 12\ \mu$C/m³ and $Q = \pi\ \mu$C $\approx3.14\ \mu$C; the flux is $-\pi a^2D_0\approx-4.712\ \mu$C through the base and $+\tfrac53\pi a^2D_0\approx7.854\ \mu$C through the dome, and their sum is $\pi\ \mu$C $= Q$ ✓.

### 4.8 Circulation from a given curl

> [!medium] Medium · Stokes' theorem · Faraday's law
> Four points lie in the plane $x = 0$ (coordinates in metres): $P_1 = (0,0,0)$, $P_2 = (0,0,2)$, $P_3 = (0,3,2)$ and $P_4 = (0,3,0)$. The closed path $C$ runs along straight segments $P_1\to P_2\to P_3\to P_4\to P_1$.
>
> (a) If $\mathbf{E} = 3\hat{x}+2\hat{y}-4\hat{z}$ V/m everywhere, find $\int\mathbf{E}\cdot d\mathbf{l}$ along $P_1\to P_2\to P_3$, and the circulation $\oint_C\mathbf{E}\cdot d\mathbf{l}$.
>
> (b) Suppose instead that $\mathbf{E}$ is unknown but its curl is uniform: $\nabla\times\mathbf{E} = 3\hat{x}+2\hat{y}-4\hat{z}$ V/m². Find $\oint_C\mathbf{E}\cdot d\mathbf{l}$, and the rate of change $\partial\mathbf{B}/\partial t$ that must be present.
>
> (c) In case (b), by how much does $\int\mathbf{E}\cdot d\mathbf{l}$ from $P_1$ to $P_3$ via $P_2$ differ from the same integral via $P_4$? Can a potential difference between $P_1$ and $P_3$ be defined?
>
> (d) Check (b) and (c) with the field $\mathbf{E} = 2z\,\hat{x}-4x\,\hat{y}+3y\,\hat{z}$ V/m: show that it has the curl of (b), and compute $\int\mathbf{E}\cdot d\mathbf{l}$ along each of the four segments.
>
> *Source: SP18 Exam 1 #2 style, re-parameterized.*

> [!hint]- Hint
> A uniform field has zero curl, but a uniform curl does not mean a uniform field. For (b), Stokes' theorem on the flat rectangle gives $\oint_C\mathbf{E}\cdot d\mathbf{l} = (\nabla\times\mathbf{E})\cdot\hat{n}\,A$. Find $\hat{n}$ from the sense of $C$ with the right-hand rule.

> [!solution]- Solution
> **(a)** For a constant field, $\int\mathbf{E}\cdot d\mathbf{l} = \mathbf{E}\cdot\Delta\mathbf{r}$ along a straight segment. $P_1\to P_2$ is $\Delta\mathbf{r} = 2\hat{z}$, giving $-8$ V; $P_2\to P_3$ is $3\hat{y}$, giving $+6$ V. The total is $-2$ V $= \mathbf{E}\cdot(P_3-P_1)$, the same along any route (via $P_4$: $+6-8 = -2$ V). Around the closed path the displacements add to zero, so $\oint_C\mathbf{E}\cdot d\mathbf{l} = 0$: a uniform field is curl-free.
>
> **(b) Setup.** Apply Stokes' theorem to the flat rectangle bounded by $C$, of area $2\times3 = 6$ m². The first two legs are $2\hat{z}$ and then $3\hat{y}$, and $\hat{z}\times\hat{y} = -\hat{x}$, so $\hat{n} = -\hat{x}$. Equivalently, $C$ runs clockwise seen from $+x$. Then
> $$
> \oint_C\mathbf{E}\cdot d\mathbf{l} = \int_S(\nabla\times\mathbf{E})\cdot d\mathbf{S} = (3\hat{x}+2\hat{y}-4\hat{z})\cdot(-\hat{x})\times6 = -18\ \text{V}.
> $$
> Only the component of the curl *normal* to the loop matters. By Faraday's law, $\partial\mathbf{B}/\partial t = -\nabla\times\mathbf{E} = -3\hat{x}-2\hat{y}+4\hat{z}$ T/s.
>
> **(c)** Going $P_1\to P_2\to P_3$ and returning $P_3\to P_4\to P_1$ traces the loop $C$, so
> $$
> \int_{P_1\to P_2\to P_3}\mathbf{E}\cdot d\mathbf{l}-\int_{P_1\to P_4\to P_3}\mathbf{E}\cdot d\mathbf{l} = \oint_C\mathbf{E}\cdot d\mathbf{l} = -18\ \text{V}.
> $$
> The line integral depends on the path, so no potential difference between $P_1$ and $P_3$ can be defined.
>
> **(d)** The curl of $2z\,\hat{x}-4x\,\hat{y}+3y\,\hat{z}$ is
> $$
> \hat{x}\Big(\frac{\partial(3y)}{\partial y}-\frac{\partial(-4x)}{\partial z}\Big)+\hat{y}\Big(\frac{\partial(2z)}{\partial z}-\frac{\partial(3y)}{\partial x}\Big)+\hat{z}\Big(\frac{\partial(-4x)}{\partial x}-\frac{\partial(2z)}{\partial y}\Big) = 3\hat{x}+2\hat{y}-4\hat{z},
> $$
> the curl of (b) ✓. On the plane $x = 0$ the field is $2z\,\hat{x}+3y\,\hat{z}$, and $d\mathbf{l}$ has no $x$ part, so only $3y\,dz$ contributes. $P_1\to P_2$ (at $y = 0$): 0. $P_2\to P_3$ ($dz = 0$): 0. $P_3\to P_4$ (at $y = 3$, $z$ from 2 to 0): $\int_2^0 9\,dz = -18$ V. $P_4\to P_1$ ($dz = 0$): 0. The loop gives $-18$ V ✓. From $P_1$ to $P_3$, the route via $P_2$ gives $0$ and the route via $P_4$ gives $0+\int_0^2 9\,dz = 18$ V; their difference is $-18$ V ✓.
>
> **Check:** (d) is an independent second route: four line integrals of a concrete field with this curl add up to the same $-18$ V that Stokes' theorem gave in one line.
>
> **Watch out:** the same vector appears in (a) and (b) with opposite consequences. As a field it gives zero circulation; as a curl it gives $-18$ V.
>
> **Answer.** (a) $-2$ V along $P_1\to P_2\to P_3$; $\oint_C\mathbf{E}\cdot d\mathbf{l} = 0$. (b) $\oint_C\mathbf{E}\cdot d\mathbf{l} = -18$ V; $\partial\mathbf{B}/\partial t = -3\hat{x}-2\hat{y}+4\hat{z}$ T/s. (c) The route via $P_2$ minus the route via $P_4$ is $-18$ V; no potential difference exists. (d) Segments $0$, $0$, $-18$ V and $0$; routes $0$ (via $P_2$) and $18$ V (via $P_4$).

## Hard

### 4.9 Electrostatic or not

> [!hard] Hard · curl · path dependence · Stokes' theorem
> In free space $\mathbf{E} = \mathbf{E}_1+\mathbf{E}_2$, where ($x$ and $y$ in metres)
> $$
> \mathbf{E}_1 = 3\cos\Big(\frac{\pi y}{2}\Big)\hat{y}\ \text{V/m},\qquad \mathbf{E}_2 = 2\cos\Big(\frac{\pi x}{2}\Big)\hat{y}\ \text{V/m}.
> $$
> (a) Find $\nabla\times\mathbf{E}_1$ and $\nabla\times\mathbf{E}_2$. Which part could be produced by static charges? Can $\mathbf{E}$ be an electrostatic field?
>
> (b) Find the charge density $\rho$. Where is $\lvert\rho\rvert$ largest, and what is its maximum value?
>
> (c) Where is $\lvert\nabla\times\mathbf{E}\rvert$ largest, and what is its maximum value?
>
> (d) Let $O = (0,0,0)$ and $P = (2,1,0)$ m. Find $\int_O^P\mathbf{E}_2\cdot d\mathbf{l}$ along route A, $O\to(2,0,0)\to P$, and along route B, $O\to(0,1,0)\to P$ (straight segments). Show that the difference agrees with Stokes' theorem on the rectangle $0\le x\le2$ m, $0\le y\le1$ m.
>
> (e) Find $\int_O^P\mathbf{E}_2\cdot d\mathbf{l}$ along the straight segment from $O$ to $P$. Then find $x_0$, with $0\le x_0\le2$ m, such that the staircase $O\to(x_0,0,0)\to(x_0,1,0)\to P$ gives exactly $-1$ V. Finally, find $\int_O^P\mathbf{E}_1\cdot d\mathbf{l}$ along routes A and B.
>
> *Source: Summer 2018 HE1 #2a–b style, re-parameterized (part (c) from Summer 2017 HE1 #2a(iii); compare Summer 2020 HE1 #1b).*

> [!hint]- Hint
> Both parts point along $\hat{y}$, so divergence comes from change *along* $\hat{y}$ ($\partial E_y/\partial y$) and curl from change *across* it ($\partial E_y/\partial x$). Curl and divergence are linear, so treat $\mathbf{E}_1$ and $\mathbf{E}_2$ separately. On a segment parallel to $\hat{x}$, a field along $\hat{y}$ contributes nothing.

> [!solution]- Solution
> **Setup.** Only $E_y$ is nonzero and nothing depends on $z$, so $\nabla\cdot\mathbf{E} = \partial E_y/\partial y$ and $\nabla\times\mathbf{E} = \hat{z}\,\partial E_y/\partial x$; every other curl term needs a $z$ dependence or another component.
>
> **(a)** $E_{1y}$ depends only on $y$, along its own direction, while $E_{2y}$ depends only on $x$, across it:
> $$
> \nabla\times\mathbf{E}_1 = \hat{z}\,\frac{\partial}{\partial x}\Big[3\cos\Big(\frac{\pi y}{2}\Big)\Big] = 0,\qquad
> \nabla\times\mathbf{E}_2 = \hat{z}\,\frac{\partial}{\partial x}\Big[2\cos\Big(\frac{\pi x}{2}\Big)\Big] = -\pi\sin\Big(\frac{\pi x}{2}\Big)\hat{z}\ \text{V/m}^2 .
> $$
> $\mathbf{E}_1$ is curl-free and could come from static charges. $\mathbf{E}_2$ has curl, so it cannot. Since $\nabla\times\mathbf{E} = \nabla\times\mathbf{E}_2\ne0$, neither can $\mathbf{E}$: a changing magnetic field, $\partial\mathbf{B}/\partial t = -\nabla\times\mathbf{E}$, must be present.
>
> **(b)** Gauss's law $\nabla\cdot\mathbf{D} = \rho$ holds for any field, static or not. Only $\mathbf{E}_1$ varies with $y$:
> $$
> \rho = \epsilon_0\frac{\partial E_y}{\partial y} = -\frac{3\pi}{2}\epsilon_0\sin\Big(\frac{\pi y}{2}\Big)\ \text{C/m}^3 .
> $$
> $\lvert\rho\rvert$ peaks where $\lvert\sin(\pi y/2)\rvert = 1$, on the planes $y = \pm1,\pm3,\ldots$ m, where $\lvert\rho\rvert = \tfrac{3\pi}{2}\epsilon_0\approx4.17\times10^{-11}$ C/m³. It is negative on $y = 1$ m and positive on $y = -1$ m and $y = 3$ m. $\mathbf{E}_2$ contributes no charge at all.
>
> **(c)** $\lvert\nabla\times\mathbf{E}\rvert = \pi\lvert\sin(\pi x/2)\rvert$, largest on the planes $x = \pm1,\pm3,\ldots$ m, where it equals $\pi\approx3.14$ V/m².
>
> **(d)** $\mathbf{E}_2$ points along $\hat{y}$, so only the segments parallel to $\hat{y}$ count, each a 1 m climb. Route A climbs at $x = 2$ m, where $E_{2y} = 2\cos\pi = -2$ V/m, so it gives **$-2$ V**. Route B climbs at $x = 0$, where $E_{2y} = 2$ V/m, so it gives **2 V**.
>
> Stokes: route A followed by route B backwards is the boundary of the rectangle $0\le x\le2$ m, $0\le y\le1$ m, traversed counter-clockwise seen from $+z$, so $d\mathbf{S} = \hat{z}\,dx\,dy$ and
> $$
> \int_0^1\!\!\int_0^2\Big[-\pi\sin\Big(\frac{\pi x}{2}\Big)\Big]dx\,dy = -\pi\cdot\frac{4}{\pi} = -4\ \text{V},
> $$
> which matches route A minus route B, $-2-2 = -4$ V ✓.
>
> **(e)** On the straight segment, $x = 2t$, $y = t$ with $t$ from 0 to 1 and $d\mathbf{l} = (2\hat{x}+\hat{y})\,dt$:
> $$
> \int_0^1 2\cos(\pi t)\,dt = \frac{2}{\pi}\Big[\sin(\pi t)\Big]_0^1 = 0.
> $$
> This zero comes from symmetry, not from a potential: $E_{2y}$ is odd about $x = 1$ m, the middle of the run, so the two halves of the segment cancel, while routes A and B give $-2$ and $2$ V. The staircase collects its whole contribution on the climb at $x = x_0$: $2\cos(\pi x_0/2)\times1$ m $= -1$ V requires $\cos(\pi x_0/2) = -\tfrac12$, so $x_0 = \tfrac43$ m. By choosing where to climb you can get any value from $-2$ to $2$ V, so $\mathbf{E}_2$ has no potential.
>
> For $\mathbf{E}_1$ only the climbs count too, but $E_{1y}$ depends on $y$ alone, so both routes give $\int_0^1 3\cos(\pi y/2)\,dy = 6/\pi\approx1.91$ V, as a curl-free field must.
>
> **Check:** in (d), the flux of the curl ($-4$ V) and the two route integrals ($-2-2$ V) are independent computations that agree. Units: the curl in V/m² times an area in m² gives V ✓.
>
> **Answer.** (a) $\nabla\times\mathbf{E}_1 = 0$ (could be electrostatic); $\nabla\times\mathbf{E}_2 = -\pi\sin(\pi x/2)\,\hat{z}$ V/m², so $\mathbf{E}$ is not electrostatic. (b) $\rho = -\tfrac{3\pi}{2}\epsilon_0\sin(\pi y/2)$ C/m³, with maximum $\lvert\rho\rvert = \tfrac{3\pi}{2}\epsilon_0\approx4.17\times10^{-11}$ C/m³ on $y = \pm1,\pm3,\ldots$ m. (c) Maximum $\lvert\nabla\times\mathbf{E}\rvert = \pi\approx3.14$ V/m² on $x = \pm1,\pm3,\ldots$ m. (d) Route A $-2$ V, route B 2 V; the flux of the curl is $-4$ V ✓. (e) 0 V; $x_0 = 4/3$ m; $\int_O^P\mathbf{E}_1\cdot d\mathbf{l} = 6/\pi\approx1.91$ V on both routes.

### 4.10 Charge layers from a piecewise D

> [!hard] Hard · spherical coordinates · surface charge · Gauss's law
> In free space a spherically symmetric flux density is given by ($r$ = distance from the origin)
> $$
> \mathbf{D} = \begin{cases} D_0\,(r/a)^2\,\hat{r}, & r<a\\ -2D_0\,(a/r)^2\,\hat{r}, & a<r<2a\\ 0, & r>2a\end{cases}
> $$
> with $D_0 = 2\ \mu$C/m² and $a = 10$ cm.
>
> (a) Find the volume charge density $\rho$ in each region, and its values at $r = a/2$ and just inside $r = a$.
>
> (b) $\mathbf{D}$ jumps at $r = a$ and at $r = 2a$. Find the surface charge density on each of these two spheres.
>
> (c) Find the total charge in the core $r<a$, on each sphere, and altogether.
>
> (d) Check (c) with Gauss's law on the sphere $r = 1.5a$. Why is $\mathbf{D}$ zero outside $r = 2a$?
>
> *Source: original.*

> [!hint]- Hint
> Inside each region use the spherical divergence $\frac{1}{r^2}\frac{d}{dr}(r^2D_r)$. At a jump the derivative does not exist, so go back to the integral form: apply Gauss's law to a thin spherical shell that straddles the jump.

> [!solution]- Solution
> **Setup.** By symmetry $\mathbf{D} = D_r(r)\,\hat{r}$, which is automatically curl-free (radial, with a strength that depends on $r$ only). Between the jumps use $\rho = \nabla\cdot\mathbf{D}$; at the jumps use Gauss's law on a thin shell.
>
> **(a)**
> $$
> \begin{aligned}
> r<a:&\quad \rho = \frac1{r^2}\frac{d}{dr}\Big(r^2\cdot\frac{D_0r^2}{a^2}\Big) = \frac{4D_0r}{a^2},\\
> a<r<2a:&\quad \rho = \frac1{r^2}\frac{d}{dr}\big(-2D_0a^2\big) = 0,\\
> r>2a:&\quad \rho = 0 .
> \end{aligned}
> $$
> So $\rho(a/2) = 2D_0/a = 40\ \mu$C/m³ and $\rho(a^-) = 4D_0/a = 80\ \mu$C/m³. The middle region is charge-free even though $\mathbf{D}\ne0$ there: its $1/r^2$ field is produced by charge further in.
>
> **(b)** Take a thin shell $a-\delta<r<a+\delta$. Its outward flux is $4\pi(a+\delta)^2D_r(a+\delta)-4\pi(a-\delta)^2D_r(a-\delta)$, while the volume charge inside it vanishes as $\delta\to0$. What remains must be a surface charge: $4\pi a^2\rho_s = 4\pi a^2\big[D_r(a^+)-D_r(a^-)\big]$. Hence
> $$
> \rho_s(a) = D_r(a^+)-D_r(a^-) = -2D_0-D_0 = -3D_0 = -6\ \mu\text{C/m}^2,\qquad
> \rho_s(2a) = 0-\Big(-\frac{2D_0}{4}\Big) = \frac{D_0}{2} = +1\ \mu\text{C/m}^2 .
> $$
> **(c)**
> $$
> \begin{aligned}
> Q_{\text{core}} &= \int_0^a\frac{4D_0r}{a^2}\,4\pi r^2\,dr = 4\pi a^2D_0\approx+0.2513\ \mu\text{C},\\
> Q_a &= 4\pi a^2(-3D_0)\approx-0.7540\ \mu\text{C},\qquad
> Q_{2a} = 4\pi(2a)^2\cdot\frac{D_0}{2} = 8\pi a^2D_0\approx+0.5027\ \mu\text{C},
> \end{aligned}
> $$
> and the total is $(4-12+8)\pi a^2D_0 = 0$.
>
> **(d)** On $r = 1.5a$, or on any sphere in the middle region: $\oint\mathbf{D}\cdot d\mathbf{S} = 4\pi r^2\cdot\Big(-\dfrac{2D_0a^2}{r^2}\Big) = -8\pi a^2D_0\approx-0.5027\ \mu$C, which equals $Q_{\text{core}}+Q_a$ ✓. Outside $r = 2a$ the enclosed charge is the total, zero, so by Gauss's law and symmetry $\mathbf{D} = 0$ there: the outer sphere's $+0.5027\ \mu$C exactly cancels the net inner charge.
>
> **Check:** follow the flux $4\pi r^2D_r$ outward. It is $+4\pi a^2D_0$ just inside $r = a$, drops to $-8\pi a^2D_0$ just outside, stays there through the charge-free middle region, and returns to 0 at $r = 2a$. Each step equals the charge on that sphere ✓.
>
> **Watch out:** differentiating $D_r$ across a jump gives nothing sensible. A jump in the normal component of $\mathbf{D}$ always signals a surface charge, $\rho_s = D_r(\text{outside})-D_r(\text{inside})$.
>
> **Answer.** (a) $\rho = 4D_0r/a^2$ for $r<a$ (40 μC/m³ at $r = a/2$, 80 μC/m³ just inside $r = a$) and zero elsewhere. (b) $\rho_s = -6\ \mu$C/m² on $r = a$ and $+1\ \mu$C/m² on $r = 2a$. (c) $+0.2513\ \mu$C in the core, $-0.7540\ \mu$C on $r = a$, $+0.5027\ \mu$C on $r = 2a$; total 0. (d) The flux through $r = 1.5a$ is $-0.5027\ \mu$C $= Q_{\text{core}}+Q_a$ ✓; $\mathbf{D} = 0$ outside because the total charge is zero.

### 4.11 An expanding ion cloud

> [!hard] Hard · continuity · displacement current
> A spherical cloud of positive ions centred on the origin expands uniformly in free space. For $t\ge0$ it fills the ball $r<R(t) = a\,e^{t/\tau}$ with the uniform charge density $\rho(t) = \rho_0e^{-3t/\tau}$, and every ion moves radially with velocity $\mathbf{v} = (r/\tau)\,\hat{r}$. Take $a = 1$ cm, $\rho_0 = 3\ \mu$C/m³ and $\tau = 2$ ms.
>
> (a) Find the current density $\mathbf{J}$ inside the cloud and verify the continuity equation there. Show that the total charge of the cloud is constant, and find it.
>
> (b) Find the outward current through the fixed sphere $r = a$ as a function of time, and check it against the rate of change of the charge inside that sphere. Evaluate $J_r(a)$ and the current at $t = 0^+$.
>
> (c) When has half of the cloud's charge left the sphere $r = a$? What is the cloud's radius then?
>
> (d) Find $\mathbf{D}$ inside the cloud from Gauss's law, and show that $\mathbf{J}+\partial\mathbf{D}/\partial t = 0$ there. What does this imply for the magnetic field?
>
> *Source: original.*

> [!hint]- Hint
> $\mathbf{J} = \rho\mathbf{v}$, and for a radial field $\nabla\cdot\mathbf{J} = \frac{1}{r^2}\frac{\partial}{\partial r}(r^2J_r)$. For $t>0$ the cloud is larger than the sphere $r = a$, so the charge inside that sphere is just $\rho(t)$ times its volume.

> [!solution]- Solution
> **(a)** Inside the cloud, $\mathbf{J} = \rho\mathbf{v} = \dfrac{\rho_0}{\tau}e^{-3t/\tau}\,r\,\hat{r}$. Then
> $$
> \nabla\cdot\mathbf{J} = \frac{1}{r^2}\frac{\partial}{\partial r}\Big(r^2\cdot\frac{\rho r}{\tau}\Big) = \frac{3\rho}{\tau},\qquad
> \frac{\partial\rho}{\partial t} = -\frac{3}{\tau}\rho_0e^{-3t/\tau} = -\frac{3\rho}{\tau},
> $$
> so $\nabla\cdot\mathbf{J}+\partial\rho/\partial t = 0$ ✓: the density falls exactly as fast as the outflow requires. The cloud's charge is
> $$
> Q = \rho(t)\cdot\frac43\pi R(t)^3 = \rho_0e^{-3t/\tau}\cdot\frac43\pi a^3e^{3t/\tau} = \frac43\pi a^3\rho_0 = 4\pi\ \text{pC}\approx12.566\ \text{pC},
> $$
> constant in time: the volume grows as $e^{3t/\tau}$ while the density falls as $e^{-3t/\tau}$.
>
> **(b)** At $r = a$, $J_r = \rho(t)\,a/\tau$, so the outward current is
> $$
> I(t) = J_r(a)\cdot4\pi a^2 = \frac{4\pi a^3\rho_0}{\tau}e^{-3t/\tau} = \frac{3Q}{\tau}e^{-3t/\tau}.
> $$
> The charge inside the fixed sphere is $Q_a(t) = \rho(t)\cdot\frac43\pi a^3 = Qe^{-3t/\tau}$, and $dQ_a/dt = -\dfrac{3Q}{\tau}e^{-3t/\tau} = -I(t)$ ✓, the integral form of continuity. At $t = 0^+$: $J_r(a) = \rho_0a/\tau = 15\ \mu$A/m² and $I = 3Q/\tau = 6\pi$ nA $\approx18.85$ nA.
>
> **(c)** $Q_a = Q/2$ when $e^{-3t/\tau} = \tfrac12$:
> $$
> t_{1/2} = \frac{\tau}{3}\ln2\approx0.4621\ \text{ms},\qquad R(t_{1/2}) = a\,2^{1/3}\approx1.2599\ \text{cm}.
> $$
> Independent check: an ion that starts at $r_0$ is at $r_0e^{t/\tau}$ later, so the ions still inside $r = a$ at $t_{1/2}$ are those that started inside $r = a\,2^{-1/3}$, a ball with half the original volume and hence half the charge ✓.
>
> **(d)** Gauss's law on a sphere of radius $r<R(t)$ gives $D_r\cdot4\pi r^2 = \rho\cdot\frac43\pi r^3$, so $\mathbf{D} = \dfrac{\rho(t)\,r}{3}\,\hat{r}$. Then
> $$
> \frac{\partial\mathbf{D}}{\partial t} = \frac{r}{3}\frac{\partial\rho}{\partial t}\,\hat{r} = -\frac{\rho r}{\tau}\,\hat{r} = -\mathbf{J}.
> $$
> The conduction current and the displacement current cancel at every point inside. Outside the cloud, $\mathbf{D} = Q\hat{r}/(4\pi r^2)$ does not change and $\mathbf{J} = 0$, so the sum vanishes there too. By the Ampère–Maxwell law, $\nabla\times\mathbf{H} = \mathbf{J}+\partial\mathbf{D}/\partial t = 0$ everywhere. A spherically symmetric $\mathbf{H}$ would also have to be radial, $H_r(r)\,\hat{r}$, and $\nabla\cdot\mathbf{B} = 0$ then makes $r^2H_r$ a constant, which must be zero because there is no magnetic charge at the origin. So $\mathbf{H} = 0$: the expanding cloud makes no magnetic field at all.
>
> **Answer.** (a) $\mathbf{J} = (\rho_0/\tau)e^{-3t/\tau}\,r\,\hat{r}$; $\nabla\cdot\mathbf{J} = 3\rho/\tau = -\partial\rho/\partial t$; $Q = \tfrac43\pi a^3\rho_0 = 4\pi$ pC $\approx12.566$ pC, constant. (b) $I(t) = (3Q/\tau)e^{-3t/\tau}$ outward, equal to $-dQ_a/dt$; at $t = 0^+$, $J_r(a) = 15\ \mu$A/m² and $I = 6\pi$ nA $\approx18.85$ nA. (c) $t_{1/2} = (\tau/3)\ln2\approx0.4621$ ms, when $R\approx1.2599$ cm. (d) $\mathbf{D} = (\rho r/3)\,\hat{r}$ and $\partial\mathbf{D}/\partial t = -\mathbf{J}$, so $\nabla\times\mathbf{H} = 0$ and $\mathbf{H} = 0$.

### 4.12 Inside a current-carrying rod

> [!hard] Hard · Ampère's law · Stokes' theorem · divergence of B
> A long straight rod of radius $a = 2$ cm along the $z$ axis carries a steady current. Everything is in free space, and with $r$ the distance from the $z$ axis the magnetic field is
> $$
> \mathbf{H} = H_0\Big(\frac{r}{a}\Big)^3\hat\phi\ \ (r<a),\qquad \mathbf{H} = H_0\,\frac{a}{r}\,\hat\phi\ \ (r>a),\qquad H_0 = 400\ \text{A/m}.
> $$
> (a) Find the current density $\mathbf{J}$ inside and outside the rod, and its value at $r = a$. Check that $\nabla\cdot\mathbf{J} = 0$.
>
> (b) Find the total current and its direction.
>
> (c) Verify Stokes' theorem on the quarter-disk $0\le r\le a/2$, $0\le\phi\le\pi/2$ in the plane $z = 0$: compute the MMF $\oint\mathbf{H}\cdot d\mathbf{l}$ around its boundary, counter-clockwise seen from $+z$, and the current through the quarter-disk.
>
> (d) Find the MMF around the circle $r = 2a$ in the plane $z = 0$, counter-clockwise seen from $+z$.
>
> (e) Could $\mathbf{B} = \mu_0\mathbf{H}$ also have a radial component $B_r$ that does not depend on $z$? Use $\nabla\cdot\mathbf{B} = 0$.
>
> *Source: classic.*

> [!hint]- Hint
> For a purely azimuthal field $H_\phi(r)$, the only curl component is $(\nabla\times\mathbf{H})_z = \frac1r\frac{d}{dr}(rH_\phi)$. On the quarter-disk boundary the two straight segments are radial: what is $\mathbf{H}\cdot d\mathbf{l}$ there?

> [!solution]- Solution
> **(a)** Ampère's law in differential form for steady fields is $\nabla\times\mathbf{H} = \mathbf{J}$:
> $$
> r<a:\quad J_z = \frac1r\frac{d}{dr}\Big(\frac{H_0r^4}{a^3}\Big) = \frac{4H_0r^2}{a^3},\qquad
> r>a:\quad J_z = \frac1r\frac{d}{dr}\big(H_0a\big) = 0 .
> $$
> So $\mathbf{J} = 4H_0(r^2/a^3)\,\hat{z}$ inside and zero outside, with $J(a) = 4H_0/a = 8\times10^4$ A/m² at the surface. Its divergence is $\partial J_z/\partial z = 0$, as it must be: $\nabla\cdot(\nabla\times\mathbf{H}) = 0$ for any field, and a steady current cannot pile up charge ($\nabla\cdot\mathbf{J} = -\partial\rho/\partial t = 0$).
>
> **(b)**
> $$
> I = \int_0^a\frac{4H_0r^2}{a^3}\,2\pi r\,dr = 2\pi aH_0 = 16\pi\ \text{A}\approx50.27\ \text{A},
> $$
> along $+\hat{z}$, because $J_z>0$. Equivalently, $\mathbf{H}$ circles counter-clockwise seen from $+z$, the right-hand rule for a current toward $+z$.
>
> **(c)** The boundary has three pieces. On the two radial segments ($\phi = 0$ and $\phi = \pi/2$), $d\mathbf{l}$ is along $\pm\hat{r}$, perpendicular to $\mathbf{H}$, so they contribute nothing. On the arc $r = a/2$, $\mathbf{H}$ is parallel to $d\mathbf{l}$:
> $$
> \oint\mathbf{H}\cdot d\mathbf{l} = H_\phi\Big(\frac a2\Big)\cdot\frac{\pi}{2}\cdot\frac a2 = \frac{H_0}{8}\cdot\frac{\pi a}{4} = \frac{\pi H_0a}{32} = \frac{\pi}{4}\ \text{A}\approx0.7854\ \text{A}.
> $$
> The current through the quarter-disk, with $d\mathbf{S} = \hat{z}\,r\,dr\,d\phi$ by the right-hand rule, is
> $$
> \int_0^{\pi/2}\!\!\int_0^{a/2}\frac{4H_0r^2}{a^3}\,r\,dr\,d\phi = \frac{\pi}{2}\cdot\frac{4H_0}{a^3}\cdot\frac{(a/2)^4}{4} = \frac{\pi H_0a}{32},
> $$
> the same ✓. With the full radius $a$, the same calculation gives $\pi H_0a/2 = 4\pi$ A $\approx12.57$ A $= I/4$, a quarter of the total, as symmetry demands.
>
> **(d)** $\oint\mathbf{H}\cdot d\mathbf{l} = H_0\dfrac{a}{2a}\cdot2\pi(2a) = 2\pi aH_0 = 16\pi$ A $\approx50.27$ A $= I$. The circle encloses the whole current, and outside the rod $\nabla\times\mathbf{H} = 0$, so every loop that goes once around the rod has the same MMF.
>
> **(e)** No. Nothing depends on $z$ and $B_\phi = \mu_0H_\phi$ does not depend on $\phi$, so
> $$
> \nabla\cdot\mathbf{B} = \frac1r\frac{\partial(rB_r)}{\partial r} = 0\quad\Longrightarrow\quad B_r = \frac{g(\phi)}{r}
> $$
> for some function $g$. That blows up on the axis, inside the rod, where the current density is finite and nothing can produce an infinite field; so $g = 0$ and $B_r = 0$. (If $B_r$ depended on $r$ alone, $g$ would be a constant $C$, and the flux of $\mathbf{B}$ out of a closed coaxial cylinder of length $L$ would be $2\pi CL$, which $\oint\mathbf{B}\cdot d\mathbf{S} = 0$ forces to zero.)
>
> **Check:** $\mathbf{H}$ is continuous at $r = a$ ($H_0$ on both sides), so there is no surface current, consistent with $J$ dropping from $8\times10^4$ A/m² to zero without a current sheet. And Ampère's integral law on a circle of radius $r<a$ gives $H_\phi\cdot2\pi r = 2\pi H_0r^4/a^3 = \int_0^r J_z\,2\pi r'\,dr'$ ✓.
>
> **Answer.** (a) $\mathbf{J} = 4H_0(r^2/a^3)\,\hat{z}$ for $r<a$ and 0 outside; $J(a) = 8\times10^4$ A/m²; $\nabla\cdot\mathbf{J} = 0$. (b) $I = 2\pi aH_0 = 16\pi\approx50.27$ A along $+\hat{z}$. (c) Both sides equal $\pi H_0a/32 = \pi/4\approx0.7854$ A. (d) $16\pi\approx50.27$ A $= I$. (e) $B_r = 0$.

### Sources for this page
Problems 4.1–4.4, 4.6, 4.10 and 4.11 are original; 4.1 and 4.3 build on the Lecture 4 notes and slides (the faucet and whirlpool examples, the paddlewheel and the "along/across the flow" rules, the curl-free Coulomb field and the free vortex). Old exams, re-parameterized: SP18 Exam 1 #2 behind 4.8 (a uniform field versus a uniform curl, with a new vector) and Summer 2018 HE1 #2a–b behind 4.9 (new field and endpoints; its maximum-curl part (c) follows Summer 2017 HE1 #2a(iii); compare Summer 2020 HE1 #1b, "which component is electrostatic?"). Classic textbook exercises with new numbers: the draining cube (4.5), the divergence theorem on a hemisphere (4.7) and the field inside a current-carrying rod (4.12).

*Previous: [[practice/03-gauss-law-at-work|Lecture 3 practice]] · next: [[practice/05-electrostatic-potential|Lecture 5 practice]] · [[practice/index|all practice]]*
