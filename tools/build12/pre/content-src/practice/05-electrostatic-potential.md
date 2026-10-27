---
title: "Practice — Lecture 5: The electrostatic potential"
description: "12 practice problems (5 easy, 3 medium, 4 hard) on potential differences along paths, E = −∇V and equipotentials, path independence and curl, V from E for a ball, a cylinder and a slab with a chosen reference, scalar superposition for point charges and a charged annulus, work in electron-volts, and the energy of assembling charges, each with a folded hint and a worked solution."
tags: [practice, electrostatics, exam-1]
lecture: 5
---

*Practice for [[1-electrostatics/05-curl-free-fields-and-the-electrostatic-potential|Lecture 5]] · concepts: [[concepts/electrostatic-potential]] · [[concepts/conservative-field]] · [[concepts/electrostatic-energy]] · [[concepts/superposition]] · all practice: [[practice/index|hub]] · by difficulty: [[practice/easy|easy]] · [[practice/medium|medium]] · [[practice/hard|hard]] · [[practice/topics|by topic]]*

Work each problem on paper first. Open the **hint** only when stuck, and the **solution** only after you have an answer you would hand in. Every answer here has been checked numerically.

## Easy

### 5.1 Uniform field between two points

> [!easy] Easy · potential difference · multiple choice
> A uniform field $\mathbf{E} = 50\,\hat{x}$ V/m fills a region of free space. Point $a$ is at $(1, 2, 0)$ m and point $b$ at $(4, -2, 0)$ m. What is $V(b) - V(a)$?
>
> (a) $+150$ V
>
> (b) $-150$ V
>
> (c) $-250$ V
>
> (d) It depends on the path taken from $a$ to $b$.
>
> *Source: original.*

> [!hint]- Hint
> Only the part of the displacement *along* $\mathbf{E}$ matters; a step perpendicular to $\mathbf{E}$ changes nothing. Use $V(b) - V(a) = -\int_a^b\mathbf{E}\cdot d\mathbf{l}$ on the easiest path you can think of.

> [!solution]- Solution
> A uniform field has zero curl, so every path from $a$ to $b$ gives the same line integral; pick the staircase $a\to(1,-2,0)\to b$. On the first leg $d\mathbf{l} = \hat{y}\,dy$, so $\mathbf{E}\cdot d\mathbf{l} = 0$. On the second $d\mathbf{l} = \hat{x}\,dx$ with $x$ running from 1 to 4:
> $$
> V(b) - V(a) = -\int_a^b\mathbf{E}\cdot d\mathbf{l} = -\int_1^4 50\,dx = -150\ \text{V}.
> $$
> In one line: for a uniform field, $\int_a^b\mathbf{E}\cdot d\mathbf{l} = \mathbf{E}\cdot(\mathbf{r}_b - \mathbf{r}_a) = 50\,\hat{x}\cdot(3\,\hat{x} - 4\,\hat{y}) = 150$ V.
>
> **Check:** $b$ lies 3 m further along $\mathbf{E}$ than $a$, and $\mathbf{E}$ points from high to low potential, so $V(b) < V(a)$ ✓.
>
> Why the others are wrong: (a) drops the minus sign. $+150$ V is $\int_a^b\mathbf{E}\cdot d\mathbf{l}$, the voltage *drop* from $a$ to $b$, not the change $V(b) - V(a)$. (c) multiplies $E$ by the full distance $\lvert\mathbf{r}_b - \mathbf{r}_a\rvert = 5$ m, but the 4 m moved along $-\hat{y}$ is perpendicular to $\mathbf{E}$ and costs nothing. (d) would need $\nabla\times\mathbf{E}\neq0$; a uniform field is curl-free, and a straight path, the staircase and a wiggly path all give the same $\int_a^b\mathbf{E}\cdot d\mathbf{l} = 150$ V.
>
> **Answer.** (b): $V(b) - V(a) = -150$ V.

### 5.2 Three charges, one point

> [!easy] Easy · point charges · superposition · electron-volts
> In free space, $Q_1 = +2$ nC sits at the origin, $Q_2 = -4$ nC at $(0.6, 0, 0)$ m and $Q_3 = +3$ nC at $(0, 0.8, 0)$ m. Take $V(\infty) = 0$ and $1/(4\pi\epsilon_0)\approx9\times10^{9}$ m/F.
> (a) Find the potential at $P = (0.6, 0.8, 0)$ m.
> (b) How much work must an external agent do to carry an electron from very far away to $P$, starting and ending at rest? Give it in eV and in joules.
>
> *Source: classic.*

> [!hint]- Hint
> Potentials are scalars: add $Q_i/(4\pi\epsilon_0R_i)$ with their signs, with no components and no unit vectors. The agent's work is $q\,[V(P) - V(\infty)]$ with $q = -e$.

> [!solution]- Solution
> **Distances to $P$.** $R_1 = \sqrt{0.6^2 + 0.8^2} = 1$ m, $R_2 = 0.8$ m (straight up from $Q_2$), $R_3 = 0.6$ m (straight across from $Q_3$).
>
> **(a)** Add the potentials as plain numbers, signs included:
> $$
> V(P) = \frac{1}{4\pi\epsilon_0}\sum_i\frac{Q_i}{R_i} = 9\times10^{9}\Big(\frac{2}{1} - \frac{4}{0.8} + \frac{3}{0.6}\Big)\times10^{-9} = 9\,(2 - 5 + 5) = 18\ \text{V}
> $$
> (17.98 V with the exact constant).
>
> **(b)** The agent's work is the change in the electron's potential energy:
> $$
> W = q\,[V(P) - V(\infty)] = (-e)(18\ \text{V}) = -18\ \text{eV} = -18\times1.602\times10^{-19}\ \text{J}\approx-2.88\times10^{-18}\ \text{J}.
> $$
> It is negative because $P$ is at a positive potential and the electron is negative, so its potential energy $qV$ ends 18 eV lower than it started: on balance the agent holds the electron back, and the field does $+18$ eV of work on it.
>
> **Check:** units, $\dfrac{\text{m}}{\text{F}}\cdot\dfrac{\text{C}}{\text{m}} = \dfrac{\text{C}}{\text{F}} = \text{V}$ ✓. An independent route, integrating $-\mathbf{E}\cdot d\mathbf{l}$ of the full vector field numerically along a straight line in from far away, gives the same 18 V.
>
> **Watch out:** do not add $Q_i/R_i^2$. That is the size of each charge's *field*, and fields add as vectors.
>
> **Answer.** $V(P) = 18$ V; $W = -18$ eV $\approx-2.88\times10^{-18}$ J.

### 5.3 True or false on potential

> [!easy] Easy · true or false · equipotentials · curl
> True or false? Give a one-line reason or a counter-example for each.
>
> (a) $\mathbf{E}$ is perpendicular to the equipotential surfaces and points toward lower potential.
>
> (b) If $V = 0$ at a point, then $\mathbf{E} = 0$ at that point.
>
> (c) Inside a uniformly charged spherical shell $\mathbf{E} = 0$, so with $V(\infty) = 0$ the potential inside is zero too.
>
> (d) $\mathbf{E} = \sin y\,\hat{x} + \cos x\,\hat{y}$ V/m can be an electrostatic field.
>
> (e) A charge released from rest in an electrostatic field moves toward lower potential *energy*, but not necessarily toward lower *potential*.
>
> *Source: original.*

> [!hint]- Hint
> Two of the five are true. For each false one, a single counter-example is enough: a $\pm$ pair of charges, a hollow shell, a quick curl.

> [!solution]- Solution
> **(a) True.** Along an equipotential surface $dV = -\mathbf{E}\cdot d\mathbf{l} = 0$ for every step $d\mathbf{l}$ that stays in the surface, so $\mathbf{E}$ has no component along the surface. And $\mathbf{E} = -\nabla V$ points opposite to the direction in which $V$ increases.
>
> **(b) False.** $\mathbf{E}$ depends on how $V$ *changes*, not on its value. Counter-example: $+1$ nC at $x = -10$ cm and $-1$ nC at $x = +10$ cm. At the origin the two potentials cancel, so $V = 0$, but both fields point along $+\hat{x}$ (away from the $+$ charge, toward the $-$ charge) and add: $E = \dfrac{2q}{4\pi\epsilon_0d^2}\approx1798$ V/m, with $q = 1$ nC and $d = 10$ cm.
>
> **(c) False.** $\mathbf{E} = 0$ inside means $V$ is *constant* inside, not zero. The constant is the shell's own potential, $V = \dfrac{Q}{4\pi\epsilon_0a}$; for $Q = 1$ nC and $a = 20$ cm that is 44.94 V at every interior point.
>
> **(d) False.** $(\nabla\times\mathbf{E})_z = \partial_xE_y - \partial_yE_x = -\sin x - \cos y$, which is not zero (it is $-1.06$ V/m² at $(0.3, 0.7, 0)$). A static field must be curl-free, so no potential exists for this $\mathbf{E}$.
>
> **(e) True.** Released from rest, the charge moves along the force $q\mathbf{E}$, which does positive work, so $U = qV$ decreases. A proton moves along $\mathbf{E}$, toward lower $V$. An electron moves against $\mathbf{E}$, toward *higher* $V$, but with $q<0$ its $U = qV$ still falls. In $\mathbf{E} = 10\,\hat{x}$ V/m, a 1 mm step along the force changes $V$ by $-0.01$ V for the proton and by $+0.01$ V for the electron, and lowers $U$ by $1.6\times10^{-21}$ J for both.
>
> **Answer.** (a) True, (b) False, (c) False, (d) False, (e) True.

### 5.4 Field from a potential

> [!easy] Easy · gradient · equipotentials
> In a region of free space the potential is $V(x,y,z) = 2x^2y - 3yz + 5$ V, with coordinates in metres.
> (a) Find $\mathbf{E}$ at $P = (1, 2, -1)$ m and its magnitude.
> (b) In which direction does $V$ increase fastest at $P$, and at what rate? How is this direction related to the equipotential surface through $P$?
>
> *Source: classic.*

> [!hint]- Hint
> Take the three partial derivatives as functions of $x, y, z$ first, and substitute $P$ only at the end. Mind the minus sign in $\mathbf{E} = -\nabla V$.

> [!solution]- Solution
> **(a)** Differentiate term by term:
> $$
> \nabla V = \hat{x}\frac{\partial V}{\partial x} + \hat{y}\frac{\partial V}{\partial y} + \hat{z}\frac{\partial V}{\partial z} = 4xy\,\hat{x} + (2x^2 - 3z)\,\hat{y} - 3y\,\hat{z}.
> $$
> At $P$ this is $8\,\hat{x} + 5\,\hat{y} - 6\,\hat{z}$ V/m, so
> $$
> \mathbf{E}(P) = -\nabla V = -8\,\hat{x} - 5\,\hat{y} + 6\,\hat{z}\ \text{V/m},\qquad \lvert\mathbf{E}\rvert = \sqrt{64 + 25 + 36} = \sqrt{125}\approx11.18\ \text{V/m}.
> $$
> **(b)** $\nabla V$ points along the steepest increase of $V$: the unit vector $(8\,\hat{x} + 5\,\hat{y} - 6\,\hat{z})/\sqrt{125}\approx0.716\,\hat{x} + 0.447\,\hat{y} - 0.537\,\hat{z}$, with rate $\lvert\nabla V\rvert\approx11.18$ V/m. This is the normal to the equipotential surface through $P$ (moving within that surface does not change $V$), and $\mathbf{E}$ points the opposite way, downhill.
>
> **Check:** at $P$, $V$ falls as $z$ grows ($\partial V/\partial z = -3y = -6$ V/m), so $\mathbf{E}$ must have a positive $z$ component, and indeed $E_z = +6$ V/m ✓. The constant 5 drops out: the choice of reference never affects $\mathbf{E}$.
>
> **Answer.** $\mathbf{E}(P) = -8\,\hat{x} - 5\,\hat{y} + 6\,\hat{z}$ V/m and $\lvert\mathbf{E}\rvert = \sqrt{125}\approx11.18$ V/m; $V$ increases fastest along $0.716\,\hat{x} + 0.447\,\hat{y} - 0.537\,\hat{z}$ (the normal to the equipotential through $P$), at 11.18 V/m.

### 5.5 Find the sign error

> [!easy] Easy · find the error · point charge
> A student computes the potential at $r = 0.3$ m from a point charge $Q = 1$ nC at the origin (free space, $V(\infty) = 0$, $1/(4\pi\epsilon_0)\approx9\times10^9$ m/F). The student writes: "I bring the test charge in from infinity, so I move along $-\hat{r}$ and $d\mathbf{l} = -\hat{r}\,dr'$." Then:
> $$
> V(r) = -\int_\infty^r\mathbf{E}\cdot d\mathbf{l} = -\int_\infty^r\frac{Q}{4\pi\epsilon_0r'^2}\,\hat{r}\cdot(-\hat{r}\,dr') = \int_\infty^r\frac{Q\,dr'}{4\pi\epsilon_0r'^2} = -\frac{Q}{4\pi\epsilon_0r} = -30\ \text{V}.
> $$
> Find the slip, fix it, and give the correct $V(0.3\text{ m})$.
>
> *Source: original, on the Lecture 5 sign trap.*

> [!hint]- Hint
> What tells the integral that you are moving inward: the sign in $d\mathbf{l}$, or the order of the limits? It cannot be both.

> [!solution]- Solution
> **The slip: the direction is counted twice.** In spherical coordinates the radial line element is always $d\mathbf{l} = \hat{r}\,dr'$. Moving inward is already built into the limits $\int_\infty^r$, because $dr'<0$ along the way automatically. Writing $d\mathbf{l} = -\hat{r}\,dr'$ *and* running the limits from $\infty$ to $r$ flips the sign a second time.
>
> **Fix.**
> $$
> V(r) - V(\infty) = -\int_\infty^r\frac{Q}{4\pi\epsilon_0r'^2}\,\hat{r}\cdot\hat{r}\,dr' = -\Big[-\frac{Q}{4\pi\epsilon_0r'}\Big]_\infty^r = \frac{Q}{4\pi\epsilon_0r} = \frac{9\times10^9\times10^{-9}}{0.3} = 30\ \text{V}.
> $$
> **Check:** near a positive charge the potential must be positive and must fall as you move away. And $-dV/dr$ must give back the outward field: for $V = Q/(4\pi\epsilon_0r)$, $-dV/dr = Q/(4\pi\epsilon_0r^2) = 100$ V/m, outward ✓. The student's $-Q/(4\pi\epsilon_0r)$ would give an *inward* field around a positive charge ✗.
>
> **Answer.** The direction was counted twice ($d\mathbf{l} = -\hat{r}\,dr'$ together with limits from $\infty$ to $r$); the correct value is $V(0.3\text{ m}) = +30$ V (29.96 V with the exact constant).

## Medium

### 5.6 Two fields, three paths

> [!medium] Medium · path independence · curl · Stokes' theorem
> Two candidate fields in free space are $\mathbf{E}_\pm = 3x^2y\,\hat{x} \pm x^3\,\hat{y}$ V/m, with coordinates in metres.
> (a) Find $\nabla\times\mathbf{E}_+$ and $\nabla\times\mathbf{E}_-$. Which field can be electrostatic?
> (b) For each field, evaluate $\int_O^P\mathbf{E}\cdot d\mathbf{l}$ from $O = (0,0,0)$ to $P = (1,2,0)$ m along three paths: $C_1$, along the $x$ axis to $(1,0,0)$ and then parallel to $y$ up to $P$; $C_2$, along the $y$ axis to $(0,2,0)$ and then parallel to $x$ across to $P$; $C_3$, the straight line $y = 2x$.
> (c) For the electrostatic field, find $V(x,y,z)$ with $V(O) = 0$, and $V(P) - V(O)$.
> (d) For the other field, show that the results along $C_1$ and $C_3$ differ by exactly the flux of its curl through the triangle between those two paths.
>
> *Source: course notes, Lecture 5 two-path example, new field and a third path.*

> [!hint]- Hint
> On an axis-parallel leg one coordinate is frozen, so its differential is zero: cross that term out before you integrate, and use the frozen value in the other term. On $C_3$ substitute $y = 2x$ and $dy = 2\,dx$. In (d), "out along $C_1$, back along $C_3$" circles the triangle counter-clockwise seen from $+z$.

> [!solution]- Solution
> **Setup.** Both fields lie in the $xy$ plane and depend on $x$ and $y$ only, so only the $z$ component of the curl can survive: $(\nabla\times\mathbf{E})_z = \partial_xE_y - \partial_yE_x$.
>
> **(a)** $\nabla\times\mathbf{E}_+ = (3x^2 - 3x^2)\,\hat{z} = 0$ and $\nabla\times\mathbf{E}_- = (-3x^2 - 3x^2)\,\hat{z} = -6x^2\,\hat{z}\neq0$. Only $\mathbf{E}_+$ can be electrostatic.
>
> **(b)** On each straight leg only one term of $\mathbf{E}\cdot d\mathbf{l} = E_x\,dx + E_y\,dy$ survives:
> $$
> \begin{aligned}
> C_1:&\quad \int_0^1 E_x\big|_{y=0}\,dx + \int_0^2 E_y\big|_{x=1}\,dy = \int_0^1 0\,dx + \int_0^2(\pm1)\,dy = \pm2\ \text{V},\\
> C_2:&\quad \int_0^2 E_y\big|_{x=0}\,dy + \int_0^1 E_x\big|_{y=2}\,dx = \int_0^2 0\,dy + \int_0^1 6x^2\,dx = 2\ \text{V},\\
> C_3:&\quad \int_0^1\big[3x^2(2x) \pm x^3(2)\big]\,dx = \int_0^1(6\pm2)\,x^3\,dx = \frac{6\pm2}{4} = 2\ \text{or}\ 1\ \text{V}.
> \end{aligned}
> $$
> So $\mathbf{E}_+$ gives 2 V on all three paths, while $\mathbf{E}_-$ gives $-2$ V, $+2$ V and $+1$ V: three paths, three answers.
>
> **(c)** $\mathbf{E}_+\cdot d\mathbf{l} = 3x^2y\,dx + x^3\,dy = d(x^3y)$ is an exact differential (the product rule backwards), so $-dV = d(x^3y)$ and $V = -x^3y + C$, with $C = 0$ because $V(O) = 0$:
> $$
> V(x,y,z) = -x^3y\ \text{V},\qquad V(P) - V(O) = -\int_O^P\mathbf{E}_+\cdot d\mathbf{l} = -(1)^3(2) = -2\ \text{V},
> $$
> in agreement with all three paths. Also $-\nabla(-x^3y) = 3x^2y\,\hat{x} + x^3\,\hat{y}$ ✓.
>
> **(d)** Out along $C_1$ and back along $C_3$, the loop $O\to(1,0,0)\to P\to O$ runs counter-clockwise seen from $+z$, so the right-hand rule gives $d\mathbf{S} = +\hat{z}\,dx\,dy$ over the triangle $0<x<1$, $0<y<2x$:
> $$
> \oint\mathbf{E}_-\cdot d\mathbf{l} = \int_{C_1} - \int_{C_3} = -2 - 1 = -3\ \text{V},\qquad \int_0^1\!\!\int_0^{2x}(-6x^2)\,dy\,dx = \int_0^1(-12x^3)\,dx = -3\ \text{V}.
> $$
> Stokes' theorem holds: the path dependence is exactly the curl flux enclosed between the two paths.
>
> **Check:** the other pair works too. Out along $C_2$ and back along $C_3$ is clockwise seen from $+z$, so $d\mathbf{S} = -\hat{z}\,dA$. The line integrals give $\int_{C_2} - \int_{C_3} = 2 - 1 = +1$ V; the flux of $-6x^2\,\hat{z}$ through the upper triangle is $-1$ V with $+\hat{z}$, hence $+1$ V with $-\hat{z}$ ✓.
>
> **Answer.** (a) $\nabla\times\mathbf{E}_+ = 0$, $\nabla\times\mathbf{E}_- = -6x^2\,\hat{z}$ V/m²; only $\mathbf{E}_+$ can be electrostatic. (b) $\mathbf{E}_+$: 2 V on $C_1$, $C_2$ and $C_3$; $\mathbf{E}_-$: $-2$ V, $+2$ V and $+1$ V. (c) $V = -x^3y$ V and $V(P) - V(O) = -2$ V. (d) $\int_{C_1} - \int_{C_3} = -3$ V, equal to the flux of the curl through the lower triangle.

### 5.7 Potential of a charged ball

> [!medium] Medium · V from E · spherical symmetry
> A ball of radius $a = 9$ cm carries $Q = 1$ nC spread uniformly through its volume, in free space. Take $V(\infty) = 0$ and $1/(4\pi\epsilon_0)\approx9\times10^9$ m/F.
> (a) Use Gauss's law to find $\mathbf{E}$ inside and outside the ball.
> (b) Find $V(r)$ for $r\ge a$ and for $r\le a$.
> (c) Evaluate $V(a)$, $V(a/2)$ and $V(0)$.
> (d) A narrow tunnel is drilled to the centre. How much work must an external agent do to bring a proton from far away to the centre, starting and ending at rest? Give it in eV and in joules.
>
> *Source: classic.*

> [!hint]- Hint
> Integrate inward from the reference in two pieces, $V(r) = -\int_\infty^a E_r\,dr' - \int_a^r E_r\,dr'$, using the outside field on the first piece and the inside field on the second. The point-charge formula is not valid inside.

> [!solution]- Solution
> **Setup.** Spherical symmetry gives $\mathbf{E} = E_r(r)\,\hat{r}$, and Gauss's law on a sphere of radius $r$ gives $E_r\,4\pi r^2 = Q_{\text{enc}}/\epsilon_0$. Then integrate inward from $\infty$ with $d\mathbf{l} = \hat{r}\,dr'$.
>
> **(a)** Outside, $Q_{\text{enc}} = Q$; inside, $Q_{\text{enc}} = Q\,r^3/a^3$:
> $$
> E_r = \frac{Q}{4\pi\epsilon_0r^2}\quad(r\ge a),\qquad E_r = \frac{Q\,r}{4\pi\epsilon_0a^3}\quad(r\le a).
> $$
> **(b)** Outside, $V(r) = -\displaystyle\int_\infty^r\frac{Q\,dr'}{4\pi\epsilon_0r'^2} = \frac{Q}{4\pi\epsilon_0r}$, exactly as for a point charge. Inside, start from $V(a)$ and keep going inward:
> $$
> V(r) = V(a) - \int_a^r\frac{Q\,r'}{4\pi\epsilon_0a^3}\,dr' = \frac{Q}{4\pi\epsilon_0a} - \frac{Q\,(r^2 - a^2)}{8\pi\epsilon_0a^3} = \frac{Q}{8\pi\epsilon_0a}\Big(3 - \frac{r^2}{a^2}\Big).
> $$
> **(c)** $\dfrac{Q}{4\pi\epsilon_0a} = \dfrac{9\times10^9\times10^{-9}}{0.09} = 100$ V, so $V(a) = 100$ V, $V(a/2) = 50\,(3 - \tfrac14) = 137.5$ V and $V(0) = \tfrac32\times100 = 150$ V. (With the exact constant: 99.86 V and 149.79 V.)
>
> **(d)** $W = q\,[V(0) - V(\infty)] = e\times150\ \text{V} = 150$ eV $\approx2.40\times10^{-17}$ J. It is positive: you push a positive charge uphill.
>
> **Check:** both formulas give $Q/(4\pi\epsilon_0a)$ at $r = a$, so $V$ is continuous; and $-dV/dr$ of the inside formula is $\dfrac{Q}{8\pi\epsilon_0a}\cdot\dfrac{2r}{a^2} = \dfrac{Q\,r}{4\pi\epsilon_0a^3} = E_r$ ✓. The centre is the highest point, as it must be: $\mathbf{E}$ points outward everywhere, so $V$ falls steadily from the centre outward.
>
> **Watch out:** $E = 0$ at the centre does not make $V(0) = 0$. And using $Q/(4\pi\epsilon_0r)$ inside would send $V$ to infinity at $r = 0$.
>
> **Answer.** $E_r = Qr/(4\pi\epsilon_0a^3)$ inside and $Q/(4\pi\epsilon_0r^2)$ outside; $V = \dfrac{Q}{8\pi\epsilon_0a}\big(3 - r^2/a^2\big)$ inside and $Q/(4\pi\epsilon_0r)$ outside; $V(a) = 100$ V, $V(a/2) = 137.5$ V, $V(0) = 150$ V; $W = 150$ eV $\approx2.40\times10^{-17}$ J.

### 5.8 Potential of a long cylinder

> [!medium] Medium · V from E · cylindrical symmetry · reference point
> A long cylinder of radius $a = 2$ cm along the $z$ axis is filled with a uniform volume charge; its charge per unit length is $\rho_l = 200\pi\epsilon_0$ C/m ($\approx5.56$ nC/m). The surroundings are free space.
> (a) Find $\mathbf{E}$ inside and outside by Gauss's law.
> (b) Take the surface as the reference, $V(a) = 0$. Find $V(r)$ inside and outside.
> (c) Evaluate $V(0)$, $V(2a)$ and $V(0) - V(2a)$.
> (d) Why can't you use $V(\infty) = 0$ here? If instead the reference is put on the axis, $V(0) = 0$, what are $V(a)$ and $V(2a)$, and which of your results in (c) does not change?
>
> *Source: classic.*

> [!hint]- Hint
> A Gauss cylinder of radius $r<a$ encloses $\rho_l\,r^2/a^2$ per unit length. Then $V(r) = V(a) - \int_a^r E_r\,dr'$; for $r<a$ the limits simply run inward.

> [!solution]- Solution
> **Setup.** Cylindrical symmetry gives $\mathbf{E} = E_r(r)\,\hat{r}$, with $r$ the distance from the axis. Gauss's law on a coaxial cylinder of radius $r$ and length $\ell$: $E_r\,2\pi r\ell = Q_{\text{enc}}/\epsilon_0$. Note that $\rho_l/(2\pi\epsilon_0) = 100$ V, which keeps the numbers clean.
>
> **(a)**
> $$
> E_r = \frac{\rho_l}{2\pi\epsilon_0r} = \frac{100}{r}\ \text{V/m}\quad(r\ge a),\qquad E_r = \frac{\rho_l\,r}{2\pi\epsilon_0a^2} = \frac{100\,r}{a^2}\ \text{V/m}\quad(r\le a).
> $$
> **(b)** $V(r) = V(a) - \int_a^r E_r\,dr'$ with $V(a) = 0$:
> $$
> V(r) = -\frac{\rho_l}{2\pi\epsilon_0}\ln\frac{r}{a}\quad(r\ge a),\qquad V(r) = -\frac{\rho_l}{2\pi\epsilon_0a^2}\cdot\frac{r^2 - a^2}{2} = \frac{\rho_l}{4\pi\epsilon_0}\Big(1 - \frac{r^2}{a^2}\Big)\quad(r\le a).
> $$
> **(c)** $V(0) = \dfrac{\rho_l}{4\pi\epsilon_0} = 50$ V; $V(2a) = -100\ln2\approx-69.31$ V; $V(0) - V(2a) = 50 + 100\ln2\approx119.31$ V.
>
> **(d)** An infinite line holds infinite total charge, and the logarithm never levels off: $V(r) - V(a) = -100\ln(r/a)$ V is $-1082$ V at 1 km, $-1773$ V at $10^3$ km and $-2464$ V at $10^6$ km. There is no finite value at infinity to call zero. With $V(0) = 0$ instead, subtract $V(0) = 50$ V from every value of (c): $V(a) = -50$ V and $V(2a) = -50 - 100\ln2\approx-119.31$ V. The difference $V(0) - V(2a)\approx119.31$ V is unchanged: moving the reference adds the same constant everywhere and never changes $\mathbf{E}$ or any potential difference.
>
> **Check:** both forms vanish at $r = a$, and $-dV/dr$ gives back $100\,r/a^2$ inside and $100/r$ outside ✓. $V$ is highest on the axis, as it must be for positive charge whose field points outward.
>
> **Answer.** $E_r = 100\,r/a^2$ V/m inside and $100/r$ V/m outside. With $V(a) = 0$: $V = 50\,(1 - r^2/a^2)$ V inside and $-100\ln(r/a)$ V outside; $V(0) = 50$ V, $V(2a)\approx-69.31$ V, $V(0) - V(2a)\approx119.31$ V. With $V(0) = 0$: $V(a) = -50$ V, $V(2a)\approx-119.31$ V, same difference.

## Hard

### 5.9 Circulation and two voltmeters

> [!hard] Hard · circulation · Stokes' theorem · voltmeters
> The closed path $C$ is the boundary of the rectangle $-1\le x\le2$ m, $0\le y\le2$ m in the plane $z = 0$, traversed $a\to c_1\to b\to c_2\to a$ with $a = (2,2,0)$, $c_1 = (2,0,0)$, $b = (-1,0,0)$ and $c_2 = (-1,2,0)$ (all in m), which is clockwise seen from $+z$. Call $C_R$ the half $a\to c_1\to b$ and $C_L$ the half $a\to c_2\to b$.
> (a) In the uniform field $\mathbf{E} = 3\,\hat{x} + 4\,\hat{y} - 2\,\hat{z}$ V/m, find $\oint_C\mathbf{E}\cdot d\mathbf{l}$ leg by leg, and $V(b) - V(a)$.
> (b) Suppose instead that a field has the uniform curl $\nabla\times\mathbf{E} = 2\,\hat{x} - 3\,\hat{y} + 5\,\hat{z}$ V/m². Without knowing $\mathbf{E}$ itself, find $\oint_C\mathbf{E}\cdot d\mathbf{l}$.
> (c) One such field is $\mathbf{E} = -(2.5y + 1.5z)\,\hat{x} + (2.5x - z)\,\hat{y} + (1.5x + y)\,\hat{z}$ V/m. Verify its curl, compute $\int_a^b\mathbf{E}\cdot d\mathbf{l}$ along $C_R$ and along $C_L$, and check that their difference is your answer to (b).
> (d) Two ideal voltmeters both have their $+$ lead at $b$ and their $-$ lead at $a$; one meter's leads run along $C_R$, the other's along $C_L$. Each reads $\int_b^a\mathbf{E}\cdot d\mathbf{l}$ along its own leads. What do they read in the field of (c)? Can that field be electrostatic?
>
> *Source: original.*

> [!hint]- Hint
> On each leg only one coordinate changes. For (b), only the component of the curl along the loop's normal counts, and for a loop that runs clockwise seen from $+z$ the right-hand rule gives $d\mathbf{S} = -\hat{z}\,dA$.

> [!solution]- Solution
> **Setup.** The loop lies in the plane $z = 0$, so on it $d\mathbf{l} = \hat{x}\,dx + \hat{y}\,dy$ and $E_z$ never contributes. The enclosed area is $3\times2 = 6$ m².
>
> **(a)** For a uniform field each leg contributes $\mathbf{E}\cdot\Delta\mathbf{l}$:
> $$
> \oint_C\mathbf{E}\cdot d\mathbf{l} = \underbrace{4(-2)}_{a\to c_1} + \underbrace{3(-3)}_{c_1\to b} + \underbrace{4(+2)}_{b\to c_2} + \underbrace{3(+3)}_{c_2\to a} = -8 - 9 + 8 + 9 = 0.
> $$
> The circulation vanishes, as it must for a curl-free field, and the potential difference is the same along any route:
> $$
> V(b) - V(a) = -\int_a^b\mathbf{E}\cdot d\mathbf{l} = -\mathbf{E}\cdot(\mathbf{r}_b - \mathbf{r}_a) = -\big[3(-3) + 4(-2)\big] = 17\ \text{V}.
> $$
> **(b)** Stokes' theorem, $\oint_C\mathbf{E}\cdot d\mathbf{l} = \int_S(\nabla\times\mathbf{E})\cdot d\mathbf{S}$, with $d\mathbf{S} = -\hat{z}\,dA$ because $C$ is clockwise seen from $+z$:
> $$
> \oint_C\mathbf{E}\cdot d\mathbf{l} = (2\,\hat{x} - 3\,\hat{y} + 5\,\hat{z})\cdot(-\hat{z})\times6\ \text{m}^2 = -30\ \text{V}.
> $$
> The $x$ and $y$ components of the curl do not thread this loop at all.
>
> **(c)** Curl, component by component:
> $$
> \nabla\times\mathbf{E} = \hat{x}\,(\partial_yE_z - \partial_zE_y) + \hat{y}\,(\partial_zE_x - \partial_xE_z) + \hat{z}\,(\partial_xE_y - \partial_yE_x) = \hat{x}\,(1 + 1) + \hat{y}\,(-1.5 - 1.5) + \hat{z}\,(2.5 + 2.5),
> $$
> which is $2\,\hat{x} - 3\,\hat{y} + 5\,\hat{z}$ V/m² ✓. On the plane $z = 0$ the field is $E_x = -2.5y$, $E_y = 2.5x$, so
> $$
> \begin{aligned}
> C_R:&\quad \int_2^0 E_y\big|_{x=2}\,dy + \int_2^{-1}E_x\big|_{y=0}\,dx = \int_2^0 5\,dy + \int_2^{-1}0\,dx = -10 + 0 = -10\ \text{V},\\
> C_L:&\quad \int_2^{-1}E_x\big|_{y=2}\,dx + \int_2^0 E_y\big|_{x=-1}\,dy = \int_2^{-1}(-5)\,dx + \int_2^0(-2.5)\,dy = 15 + 5 = 20\ \text{V}.
> \end{aligned}
> $$
> The loop is $C_R$ out and $C_L$ back, so $\oint_C\mathbf{E}\cdot d\mathbf{l} = \int_{C_R} - \int_{C_L} = -10 - 20 = -30$ V ✓, matching (b).
>
> **(d)** Each meter reads $\int_b^a = -\int_a^b$ along its own leads: the meter on $C_R$ reads $+10$ V and the meter on $C_L$ reads $-20$ V. The same two points give two readings, 30 V apart, which is exactly $\lvert\oint_C\mathbf{E}\cdot d\mathbf{l}\rvert$. "The voltage between $a$ and $b$" has no meaning here, so this field cannot be electrostatic. A static $\mathbf{E}$ is curl-free, every closed-loop integral vanishes, and both meters would agree, as they do in (a), where both read 17 V. Fields like the one in (c) do exist: they are induced by a changing magnetic flux ([[2-magnetostatics/14-faradays-law-and-induced-emf|Lecture 14]]), and there a voltmeter's reading genuinely depends on where its leads run.
>
> **Check:** the field in (c) is $\tfrac12\,\mathbf{c}\times\mathbf{r}$ with $\mathbf{c} = 2\,\hat{x} - 3\,\hat{y} + 5\,\hat{z}$, the standard field with uniform curl $\mathbf{c}$. So (b) and (c) are two independent routes to the same $-30$ V.
>
> **Answer.** (a) $\oint_C\mathbf{E}\cdot d\mathbf{l} = -8 - 9 + 8 + 9 = 0$; $V(b) - V(a) = 17$ V. (b) $\oint_C\mathbf{E}\cdot d\mathbf{l} = -30$ V. (c) $\nabla\times\mathbf{E} = 2\,\hat{x} - 3\,\hat{y} + 5\,\hat{z}$ V/m²; $\int_{C_R} = -10$ V and $\int_{C_L} = 20$ V, difference $-30$ V. (d) $+10$ V and $-20$ V; not electrostatic, because its circulation is not zero.

### 5.10 Charged slab, sheet and staircase

> [!hard] Hard · V from E · charge slabs · exact differentials
> **Part 1.** A slab $0<x<d$ with $d = 2$ m carries the uniform charge density $\rho_0 = 6\epsilon_0$ C/m³ ($\approx53.1$ pC/m³), and the plane $x = 0$ carries the sheet charge $\rho_s = -\rho_0d = -12\epsilon_0$ C/m² ($\approx-106$ pC/m²). Everything is infinite in $y$ and $z$, in free space.
> (a) Find $\mathbf{E}$ for $x<0$, $0<x<d$ and $x>d$.
> (b) With $V(0) = 0$, find $V(x)$ everywhere, and evaluate $V(0.5\text{ m})$, $V(1\text{ m})$, $V(2\text{ m})$ and $V(3\text{ m})$.
> (c) An electron is released from rest just to the right of the sheet, at $x = 0^+$. Which way is it pushed? With what kinetic energy (in eV and J) and speed does it leave the slab?
>
> **Part 2.** (d) In a different region, $\mathbf{E} = y\cos x\,\hat{x} + \sin x\,\hat{y} - 2z\,\hat{z}$ V/m. Show that it can be an electrostatic field, find $V(x,y,z)$ given $V(0,0,0) = 5$ V, evaluate $V$ at $B = (\pi/2, 2, 1)$ m, and find the work an external agent does to move a charge $q = 2\ \mu\text{C}$ slowly from the origin to $B$.
>
> *Source: FA26 Exam 1 #1(b),(d) and #2(c) style.*

> [!hint]- Hint
> (a) The pair is neutral: the slab's $\rho_0d$ per unit area cancels the sheet, so the field vanishes outside both. Inside, superpose the slab's thin layers and the sheet. (b) Split $-\int_0^xE_x\,dx'$ at $x = d$, where the field changes form. (d) Group the first two terms of $\mathbf{E}\cdot d\mathbf{l}$ into one product-rule differential.

> [!solution]- Solution
> **Setup.** Planar symmetry gives $\mathbf{E} = E_x(x)\,\hat{x}$. Build the field by superposing infinite sheets: a sheet $\rho_s$ on the plane $x = x_0$ gives $E_x = \dfrac{\rho_s}{2\epsilon_0}\operatorname{sgn}(x - x_0)$, and the slab is a stack of thin sheets $\rho_0\,dx'$.
>
> **(a)** For $x<0$ every slab layer lies to the right and contributes $-\hat{x}$, adding up to $-\dfrac{\rho_0d}{2\epsilon_0}$, while the negative sheet gives $\dfrac{\rho_s}{2\epsilon_0}(-1) = +\dfrac{\rho_0d}{2\epsilon_0}$: the total is 0. The same cancellation, with both signs reversed, happens for $x>d$. For $0<x<d$ the layers on the left push along $+\hat{x}$ and those on the right along $-\hat{x}$:
> $$
> E_x = \frac{\rho_0}{2\epsilon_0}\big[x - (d - x)\big] + \frac{\rho_s}{2\epsilon_0} = \frac{\rho_0}{\epsilon_0}\Big(x - \frac{d}{2}\Big) - \frac{\rho_0d}{2\epsilon_0} = \frac{\rho_0}{\epsilon_0}(x - d) = 6(x - 2)\ \text{V/m}.
> $$
> So $E_x(0^+) = -12$ V/m, rising linearly to 0 at $x = d$.
>
> **(b)** $V(x) = V(0) - \int_0^xE_x\,dx'$, split where the field changes form:
> $$
> V(x) = \begin{cases} 0, & x\le0,\\ -\displaystyle\int_0^x6(x' - 2)\,dx' = 12x - 3x^2\ \text{V}, & 0\le x\le2\ \text{m},\\ V(2\ \text{m}) = 12\ \text{V}, & x\ge2\ \text{m}. \end{cases}
> $$
> So $V(0.5\text{ m}) = 5.25$ V, $V(1\text{ m}) = 9$ V, $V(2\text{ m}) = 12$ V and $V(3\text{ m}) = 12$ V. In general $V(d) = \rho_0d^2/(2\epsilon_0)$.
>
> **(c)** The force is $\mathbf{F} = -e\mathbf{E}$. At $x = 0^+$, $\mathbf{E} = -12\,\hat{x}$ V/m, so $\mathbf{F} = +12e\,\hat{x}\approx1.92\times10^{-18}\,\hat{x}$ N: the electron is pushed along $+\hat{x}$, toward higher potential. Inside the slab $E_x<0$ throughout, so it accelerates all the way to $x = d$ and then coasts, since there is no field beyond. Energy conservation, with $m_e = 9.11\times10^{-31}$ kg:
> $$
> K = -q\,[V(d) - V(0)] = -(-e)(12 - 0)\ \text{V} = 12\ \text{eV}\approx1.92\times10^{-18}\ \text{J},\qquad v = \sqrt{2K/m_e}\approx2.05\times10^{6}\ \text{m/s}.
> $$
> **(d)** Curl: $\partial_xE_y - \partial_yE_x = \cos x - \cos x = 0$; and $E_z = -2z$ depends on $z$ only while $E_x$ and $E_y$ do not depend on $z$, so the other two components vanish too. A potential exists. The exact differential:
> $$
> \mathbf{E}\cdot d\mathbf{l} = y\cos x\,dx + \sin x\,dy - 2z\,dz = d(y\sin x) - d(z^2) = -dV\quad\Rightarrow\quad V = 5 - y\sin x + z^2\ \text{V},
> $$
> with the constant fixed by $V(0,0,0) = 5$ V. At $B$: $V(B) = 5 - 2\sin(\pi/2) + 1^2 = 4$ V. The staircase $(0,0,0)\to(\pi/2,0,0)\to(\pi/2,2,0)\to B$ confirms it: its legs give $\int\mathbf{E}\cdot d\mathbf{l} = 0 + 2 - 1 = 1$ V, so $V(B) - V(O) = -\int_O^B\mathbf{E}\cdot d\mathbf{l} = -1$ V. The agent's work is $W = q\,[V(B) - V(O)] = (2\times10^{-6})(-1) = -2\ \mu\text{J}$: the field does the work, and the agent only holds the charge back.
>
> **Check:** a Gauss pillbox across the sheet requires $\epsilon_0\,[E_x(0^+) - E_x(0^-)] = \epsilon_0(-12 - 0) = \rho_s$ ✓. Inside the slab $-dV/dx = 6x - 12 = E_x$ ✓, and $V$ has zero slope at $x = d$, where $\mathbf{E}$ switches off. In Part 2, $-\nabla(5 - y\sin x + z^2) = y\cos x\,\hat{x} + \sin x\,\hat{y} - 2z\,\hat{z}$ ✓.
>
> **Answer.** (a) $\mathbf{E} = 0$ for $x<0$ and for $x>2$ m, and $\mathbf{E} = 6(x - 2)\,\hat{x}$ V/m inside. (b) $V = 0$ for $x\le0$, $12x - 3x^2$ V for $0\le x\le2$ m, 12 V for $x\ge2$ m; $V = 5.25$, 9, 12 and 12 V. (c) Pushed along $+\hat{x}$; it leaves with 12 eV $\approx1.92\times10^{-18}$ J and $v\approx2.05\times10^6$ m/s. (d) Curl-free; $V = 5 - y\sin x + z^2$ V, $V(B) = 4$ V, $W = -2\ \mu\text{J}$.

### 5.11 Charged washer on its axis

> [!hard] Hard · scalar superposition · disk on axis · electron-volts
> A flat annulus (a washer) $a\le r\le b$ on the plane $z = 0$, with $a = 5$ cm and $b = 9$ cm, carries the uniform surface charge $\rho_s = 1000\epsilon_0$ C/m² ($\approx8.85$ nC/m²) in free space. Take $V(\infty) = 0$.
> (a) By scalar superposition, find $V(z)$ on the $z$ axis.
> (b) Evaluate $V(0)$ and $V(12\text{ cm})$. Find $\mathbf{E}$ on the axis from $V$, evaluate it at $z = 12$ cm, and explain why $\mathbf{E} = 0$ at the centre.
> (c) Check your field by integrating Coulomb's law directly for the on-axis field. Then let $a\to0$ to get the on-axis field of a full disk, and check $V(z)$ against a point charge far away, at $z = 1$ m.
> (d) A proton approaches along the axis from far away. What minimum kinetic energy does it need to pass through the hole? An electron is released from rest on the axis at $z = 12$ cm: with what kinetic energy and speed does it cross the centre?
>
> *Source: classic.*

> [!hint]- Hint
> Cut the washer into rings of radius $r'$ and width $dr'$. Every bit of a ring is the same distance $\sqrt{r'^2 + z^2}$ from the axis point, so a ring contributes $dq/(4\pi\epsilon_0\sqrt{r'^2 + z^2})$ with $dq = \rho_s\,2\pi r'\,dr'$. The integral is elementary: $\int r'\,dr'/\sqrt{r'^2 + z^2} = \sqrt{r'^2 + z^2}$.

> [!solution]- Solution
> **Setup.** Use rings: a ring of radius $r'$ and width $dr'$ holds $dq = \rho_s\,2\pi r'\,dr'$, all of it at distance $R = \sqrt{r'^2 + z^2}$ from the field point $(0,0,z)$. Potentials are scalars, so the contributions simply add, with nothing to resolve into components.
>
> **(a)**
> $$
> V(z) = \int_a^b\frac{\rho_s\,2\pi r'\,dr'}{4\pi\epsilon_0\sqrt{r'^2 + z^2}} = \frac{\rho_s}{2\epsilon_0}\Big[\sqrt{r'^2 + z^2}\Big]_a^b = \frac{\rho_s}{2\epsilon_0}\Big(\sqrt{b^2 + z^2} - \sqrt{a^2 + z^2}\Big).
> $$
> **(b)** Here $\rho_s/(2\epsilon_0) = 500$ V/m. At the centre, $V(0) = 500\,(0.09 - 0.05) = 20$ V. At $z = 0.12$ m the square roots come from 9-12-15 and 5-12-13 right triangles, 0.15 m and 0.13 m, so $V(12\text{ cm}) = 500\,(0.15 - 0.13) = 10$ V.
>
> On the axis, symmetry forces $E_x = E_y = 0$ (the transverse pulls of opposite bits of each ring cancel), so the only component is $E_z = -dV/dz$, and that needs $V$ on the axis only:
> $$
> E_z = -\frac{dV}{dz} = \frac{\rho_s}{2\epsilon_0}\Big(\frac{z}{\sqrt{a^2 + z^2}} - \frac{z}{\sqrt{b^2 + z^2}}\Big),\qquad E_z(0.12\text{ m}) = 60\Big(\frac{1}{0.13} - \frac{1}{0.15}\Big)\approx61.54\ \text{V/m}.
> $$
> So $\mathbf{E}\approx61.54\,\hat{z}$ V/m at $z = 12$ cm, pointing away from the washer. At $z = 0$, $E_z = 0$: the charge is mirror-symmetric about the plane $z = 0$, so $E_z(-z) = -E_z(z)$, and since the centre lies in the hole (no charge there) $E_z$ is continuous through it and must vanish. Equivalently, $V(z)$ is even and has its maximum at $z = 0$, where its slope is zero.
>
> **(c)** *Direct Coulomb integral.* On the axis each ring's field points along $\hat{z}$, and only the $z$ component $z/R$ of each $\hat{R}$ survives, so $dE_z = \dfrac{dq\,z}{4\pi\epsilon_0R^3}$:
> $$
> E_z = \frac{\rho_s z}{2\epsilon_0}\int_a^b\frac{r'\,dr'}{(r'^2 + z^2)^{3/2}} = \frac{\rho_s z}{2\epsilon_0}\Big[-\frac{1}{\sqrt{r'^2 + z^2}}\Big]_a^b = \frac{\rho_s z}{2\epsilon_0}\Big(\frac{1}{\sqrt{a^2 + z^2}} - \frac{1}{\sqrt{b^2 + z^2}}\Big),
> $$
> the same as $-dV/dz$ ✓, though notice how much shorter the scalar route was. *Full disk:* setting $a = 0$ gives, for $z>0$,
> $$
> E_z = \frac{\rho_s}{2\epsilon_0}\Big(1 - \frac{z}{\sqrt{b^2 + z^2}}\Big),
> $$
> which tends to the sheet value $\rho_s/(2\epsilon_0)$ as $z\to0^+$ and to $\pi b^2\rho_s/(4\pi\epsilon_0z^2)$, a point charge, for $z\gg b$. *Far field of V:* for $z\gg b$, $\sqrt{b^2 + z^2} - \sqrt{a^2 + z^2}\approx(b^2 - a^2)/(2z)$, so $V\approx\dfrac{\rho_s(b^2 - a^2)}{4\epsilon_0z} = \dfrac{Q}{4\pi\epsilon_0z}$ with $Q = \pi\rho_s(b^2 - a^2)\approx1.56\times10^{-10}$ C. At $z = 1$ m that gives 1.400 V, against the exact 1.396 V ✓.
>
> **(d)** On the axis $V$ peaks at the centre (20 V) and falls to 0 far away. A proton coming in along the axis must climb this hill, so it needs $K\ge e\,[V(0) - V(\infty)] = 20$ eV $\approx3.20\times10^{-18}$ J to get through. An electron ($q = -e$) released at $z = 12$ cm is pushed toward higher $V$, that is, toward the centre:
> $$
> K = -q\,[V(0) - V(12\text{ cm})] = e\,(20 - 10)\ \text{V} = 10\ \text{eV}\approx1.60\times10^{-18}\ \text{J},\qquad v = \sqrt{2K/m_e}\approx1.88\times10^{6}\ \text{m/s}.
> $$
> **Check:** units, $\rho_s/\epsilon_0$ is V/m and times a length gives V ✓. The force on the electron at 12 cm is $-eE_z\,\hat{z}$ with $E_z>0$, pointing toward the washer ✓, consistent with the energy argument.
>
> **Answer.** (a) $V(z) = \dfrac{\rho_s}{2\epsilon_0}\big(\sqrt{b^2 + z^2} - \sqrt{a^2 + z^2}\big)$. (b) $V(0) = 20$ V, $V(12\text{ cm}) = 10$ V, $\mathbf{E}(12\text{ cm})\approx61.54\,\hat{z}$ V/m, and $\mathbf{E} = 0$ at the centre. (c) Coulomb gives the same $E_z$; the full disk has $E_z = \dfrac{\rho_s}{2\epsilon_0}\big(1 - z/\sqrt{b^2 + z^2}\big)$ for $z>0$; at 1 m the point-charge estimate is 1.400 V against the exact 1.396 V. (d) Proton: at least 20 eV $\approx3.20\times10^{-18}$ J. Electron: 10 eV $\approx1.60\times10^{-18}$ J and $v\approx1.88\times10^6$ m/s at the centre.

### 5.12 Square of charges, zero energy

> [!hard] Hard · energy of charges · Coulomb force · scaling
> Four equal point charges $q = 2$ nC sit at the corners of a square of side $s = 30$ cm in the plane $z = 0$, centred on the origin, in free space. Use $1/(4\pi\epsilon_0)\approx9\times10^9$ m/F.
> (a) How much work does it take to assemble the four charges, bringing them in one at a time from far away? Show that the order does not matter.
> (b) Find the potential at the centre of the square due to the four charges.
> (c) What charge $Q$ placed at the centre makes the total electrostatic energy of the five charges zero?
> (d) With that $Q$ in place, find the net force on each corner charge and on $Q$. Explain the result with a scaling argument.
>
> *Source: classic.*

> [!hint]- Hint
> The assembly energy is one term per *pair*, $W = \sum_{\text{pairs}}\dfrac{q_iq_j}{4\pi\epsilon_0R_{ij}}$, and a square has 4 side pairs and 2 diagonal pairs. Adding $Q$ at the centre costs $Q$ times the centre potential. For (d), ask what happens to the total energy if the whole configuration is scaled by a factor $\lambda$.

> [!solution]- Solution
> **Setup.** Write $k = 1/(4\pi\epsilon_0)$. The energy of a set of point charges is the work done to bring them in one at a time, each against the potential of the charges already in place.
>
> **(a)** Charge 1 comes in for free (no field yet). Charge 2, at an adjacent corner, costs $kq^2/s$. Charge 3, adjacent to charge 2 and diagonal to charge 1, costs $kq^2/s + kq^2/(s\sqrt2)$. Charge 4, adjacent to charges 1 and 3 and diagonal to charge 2, costs $2kq^2/s + kq^2/(s\sqrt2)$. In total, one term for each of the 4 sides and the 2 diagonals:
> $$
> W_4 = \frac{kq^2}{s}\Big(4 + \frac{2}{\sqrt2}\Big) = (4 + \sqrt2)\,\frac{kq^2}{s} = 5.414\times(1.2\times10^{-7}\ \text{J})\approx6.50\times10^{-7}\ \text{J}.
> $$
> A different order changes the individual steps but every order still meets each of the six pairs exactly once, so the total is the same.
>
> **(b)** Each corner is $s/\sqrt2\approx0.2121$ m from the centre, so
> $$
> V_{\text{centre}} = 4\,\frac{kq}{s/\sqrt2} = 4\sqrt2\,\frac{kq}{s}\approx339.4\ \text{V}.
> $$
> **(c)** Bringing $Q$ to the centre costs $Q\,V_{\text{centre}}$, so the total energy is $W_4 + Q\,V_{\text{centre}}$. Setting it to zero:
> $$
> Q = -\frac{W_4}{V_{\text{centre}}} = -\frac{(4 + \sqrt2)\,kq^2/s}{4\sqrt2\,kq/s} = -\Big(\frac{1}{\sqrt2} + \frac14\Big)\,q\approx-0.957\,q\approx-1.91\ \text{nC}.
> $$
> **(d)** Take the corner at $(s/2, s/2, 0)$. Its two neighbours push it along $\hat{x}$ and $\hat{y}$ with $kq^2/s^2$ each, and the far corner pushes it along the diagonal $(\hat{x} + \hat{y})/\sqrt2$ with $kq^2/(2s^2)$. The sum points outward along the diagonal:
> $$
> F_{\text{corners}} = \frac{kq^2}{s^2}\Big(2\cdot\frac{1}{\sqrt2} + \frac12\Big) = \Big(\sqrt2 + \frac12\Big)\frac{kq^2}{s^2}\approx7.66\times10^{-7}\ \text{N, outward}.
> $$
> The centre charge sits at distance $s/\sqrt2$ and, being negative, pulls the corner inward with
> $$
> \frac{kq\lvert Q\rvert}{s^2/2} = 2\Big(\frac{1}{\sqrt2} + \frac14\Big)\frac{kq^2}{s^2} = \Big(\sqrt2 + \frac12\Big)\frac{kq^2}{s^2}.
> $$
> The two cancel exactly, so the net force on every corner charge is zero. On $Q$ it is zero by symmetry: four equal pulls in opposite pairs.
>
> *Why it had to happen:* every pair term is proportional to $1/R_{ij}$, so scaling all distances by $\lambda$ turns the total energy $W$ into $W/\lambda$. Here $W = 0$, so the energy stays zero at every size, and a small uniform expansion costs no work. In such an expansion each corner moves outward along its diagonal by the same $\delta r$ while $Q$ stays put. By symmetry the net force on each corner lies along its diagonal, say $F$ outward, so the electric forces do work $4F\,\delta r$, which must equal minus the change in energy, zero. Hence $F = 0$.
>
> **Check:** units, $kq^2/s$ is $(\text{m/F})\,\text{C}^2/\text{m} = \text{C}^2/\text{F} = \text{J}$ ✓, and $kq^2/s^2$ is J/m = N ✓. Numbers: $kq^2/s^2 = 4\times10^{-7}$ N, so the other corners push with $5.414\times10^{-7}$ N along each of $\hat{x}$ and $\hat{y}$, and $Q$ pulls with $5.414\times10^{-7}$ N along each of $-\hat{x}$ and $-\hat{y}$ ✓.
>
> **Answer.** (a) $W_4 = (4 + \sqrt2)\,kq^2/s\approx6.50\times10^{-7}$ J, in any order. (b) $V_{\text{centre}} = 4\sqrt2\,kq/s\approx339.4$ V. (c) $Q = -(1/\sqrt2 + 1/4)\,q\approx-1.91$ nC. (d) Zero net force on every charge: the other corners push each corner outward with $7.66\times10^{-7}$ N, and $Q$ pulls it inward with the same force.

### Sources for this page
Course notes, Lecture 5: the two-path $\pm$ example behind 5.6 (new field, a third path and a Stokes check), and the "counting the direction twice" sign trap behind the find-the-error item 5.5. FA26 Exam 1 problems 1(b), 1(d) and 2(c), as summarized on the Lecture 5 page (a potential from a curl-free field, a line integral between named points, and $V$ beyond a charged slab with $V(0) = 0$), set the style of 5.10. Classic textbook problems with new numbers: 5.2, 5.4, 5.7, 5.8, 5.11 and 5.12. Problems 5.1, 5.3, 5.5 and 5.9 are original.

*Previous: [[practice/04-divergence-and-curl|Lecture 4 practice]] · next: [[practice/06-circulation-and-boundary-conditions|Lecture 6 practice]] · [[practice/index|all practice]]*
