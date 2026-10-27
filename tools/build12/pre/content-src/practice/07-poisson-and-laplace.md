---
title: "Practice — Lecture 7: Poisson's and Laplace's equations"
description: "12 practice problems (5 easy, 3 medium, 4 hard) on Laplace's equation between plates, in a coax, between spheres and in a wedge, Poisson's equation with uniform and graded space charge, two-region matching at a charged sheet, a p-i-n junction, the space-charge-limited vacuum diode, and uniqueness, each with a folded hint and a worked solution."
tags: [practice, electrostatics, exam-1]
lecture: 7
---

*Practice for [[1-electrostatics/07-poisson-and-laplace|Lecture 7]] · concepts: [[concepts/poissons-equation]] · [[concepts/electrostatic-potential]] · [[concepts/boundary-conditions]] · all practice: [[practice/index|hub]] · by difficulty: [[practice/easy|easy]] · [[practice/medium|medium]] · [[practice/hard|hard]] · [[practice/topics|by topic]]*

Work each problem on paper first. Open the **hint** only when stuck, and the **solution** only after you have an answer you would hand in. Every answer here has been checked numerically.

## Easy

### 7.1 Two plates, two potentials

> [!easy] Easy · Laplace's equation · parallel plates
> Two large parallel conducting plates in free space lie on the planes $x = 0$ and $x = d = 3$ mm. The plate at $x = 0$ is held at $9$ V and the plate at $x = d$ is grounded; the gap holds no charge. (a) Solve Laplace's equation for $V(x)$ in the gap and evaluate $V$ at $x = 1$ mm. (b) Find $\mathbf{E}$ in the gap. (c) Find the surface charge density on the inner face of each plate.
>
> *Source: course notes Lecture 7, Examples 1–2 style, new numbers.*

> [!hint]- Hint
> With no charge in the gap, $d^2V/dx^2 = 0$, so $V$ is a straight line through the two plate potentials. For (c) use $\rho_s = \hat{n}\cdot\mathbf{D}$ with $\hat{n}$ pointing out of each plate into the gap.

> [!solution]- Solution
> **(a)** The plates are infinite in $y$ and $z$, so $V = V(x)$ and Laplace's equation is $V'' = 0$: $V = Ax + B$. $V(0) = 9$ V gives $B = 9$ V; $V(d) = 0$ gives $A = -9/d = -3000$ V/m. So
> $$
> V(x) = 9 - 3000\,x\ \text{V}\quad(x\ \text{in m}),\qquad V(1\ \text{mm}) = 9 - 3 = 6\ \text{V}.
> $$
> **(b)** $\mathbf{E} = -\hat{x}\,dV/dx = +3000\,\hat{x}$ V/m, uniform, pointing from the 9 V plate toward the grounded plate — from high to low potential.
>
> **(c)** At $x = 0$, $\hat{n} = +\hat{x}$: $\rho_s = \epsilon_0E_x = 8.854\times10^{-12}\times3000\approx2.66\times10^{-8}$ C/m² $= +26.6$ nC/m². At $x = d$, $\hat{n} = -\hat{x}$: $\rho_s = -\epsilon_0E_x = -26.6$ nC/m².
>
> **Check:** two sheets $\pm\rho_s$ make $E = \rho_s/\epsilon_0 = 3000$ V/m between them and zero outside — the same field, now seen from the charges.
>
> **Answer.** $V(x) = 9 - 3000x$ V ($x$ in m), $V(1\text{ mm}) = 6$ V; $\mathbf{E} = 3000\,\hat{x}$ V/m; $\rho_s = +26.6$ nC/m² on the 9 V plate and $-26.6$ nC/m² on the grounded plate.

### 7.2 Which potential needs charge

> [!easy] Easy · Poisson's equation · multiple choice
> Five electrostatic potentials in free space are given below, in volts with coordinates in metres. In the region stated for each, exactly one of them requires a nonzero volume charge density. Which one, and what is that density?
>
> (a) $V = 3x^2 - 2y^2 - z^2$, everywhere
>
> (b) $V = 5xyz$, everywhere
>
> (c) $V = x^2 + y^2 - z^2$, everywhere
>
> (d) $V = 4\ln r$ for $1<r<2$ m, with $r$ the distance from the $z$ axis
>
> (e) $V = 2/r$ for $r>1$ m, with $r$ the distance from the origin
>
> *Source: original.*

> [!hint]- Hint
> Poisson's equation read backwards: $\rho = -\epsilon_0\nabla^2V$. For (d) and (e) use the Laplacian of the matching coordinate system ([[0-toolkit/02-vector-calculus-cheatsheet|cheat sheet]]), not just $d^2V/dr^2$.

> [!solution]- Solution
> A potential can exist without charge only if its Laplacian vanishes, because $\rho = -\epsilon_0\nabla^2V$.
>
> (a) $\dfrac{\partial^2V}{\partial x^2}+\dfrac{\partial^2V}{\partial y^2}+\dfrac{\partial^2V}{\partial z^2} = 6 - 4 - 2 = 0$. Each term is nonzero, but only the sum counts: no charge.
>
> (b) $\partial^2V/\partial x^2$, $\partial^2V/\partial y^2$ and $\partial^2V/\partial z^2$ of $5xyz$ are all zero (the mixed derivatives are not, but they do not enter $\nabla^2V$): no charge.
>
> (c) $2 + 2 - 2 = 2$ V/m², so $\rho = -2\epsilon_0\approx-1.77\times10^{-11}$ C/m³ everywhere. **This is the one.**
>
> (d) Cylindrical Laplacian: $\dfrac1r\dfrac{d}{dr}\Big(r\dfrac{dV}{dr}\Big) = \dfrac1r\dfrac{d}{dr}\Big(r\cdot\dfrac4r\Big) = \dfrac1r\dfrac{d}{dr}(4) = 0$. This is the potential of a line charge on the $z$ axis, harmonic away from the axis.
>
> (e) Spherical Laplacian: $\dfrac{1}{r^2}\dfrac{d}{dr}\Big(r^2\cdot\dfrac{-2}{r^2}\Big) = \dfrac{1}{r^2}\dfrac{d}{dr}(-2) = 0$. A point charge at the origin, harmonic for $r>0$.
>
> **Watch out:** for (d) and (e), $d^2V/dr^2$ alone is $-4/r^2$ and $+4/r^3$, both nonzero. Using it as the Laplacian in cylindrical or spherical coordinates "finds" charge that is not there; the factors of $r$ inside the derivatives are essential.
>
> **Answer.** (c): $\nabla^2V = 2$ V/m², so $\rho = -2\epsilon_0\approx-1.77\times10^{-11}$ C/m³. Options (a), (b), (d) and (e) satisfy Laplace's equation in their regions.

### 7.3 Concentric spheres, find the error

> [!easy] Easy · find the error · spherical symmetry
> Two concentric conducting spherical shells in free space have radii $a = 1$ cm (held at $100$ V) and $b = 2$ cm (grounded). A student finds the potential in the gap $a<r<b$ like this:
>
> *"Only $r$ matters, so Laplace's equation is $d^2V/dr^2 = 0$, giving $V = Ar + B$. From $V(a) = 100$ V and $V(b) = 0$: $V(r) = 100\,(b-r)/(b-a)$. So $\mathbf{E} = -\hat{r}\,dV/dr = 10^4\,\hat{r}$ V/m everywhere in the gap, and $V(1.5\text{ cm}) = 50$ V."*
>
> What is wrong? Give the correct $V(r)$, the field at $r = a$ and at $r = b$, and $V(1.5\text{ cm})$.
>
> *Source: original.*

> [!hint]- Hint
> In which coordinate system is the student's Laplacian written? Compare with the table of one-dimensional solutions in Lecture 7.

> [!solution]- Solution
> **The slip:** $d^2V/dr^2 = 0$ is the *Cartesian* Laplacian with $x$ renamed $r$. In spherical coordinates, for $V = V(r)$,
> $$
> \nabla^2V = \frac{1}{r^2}\frac{d}{dr}\Big(r^2\frac{dV}{dr}\Big) = 0\quad\Longrightarrow\quad r^2\frac{dV}{dr} = -A\quad\Longrightarrow\quad V = \frac{A}{r} + B .
> $$
> **Fix.** $V(a) - V(b) = A\Big(\dfrac1a - \dfrac1b\Big) = A\,(100 - 50)\ \text{m}^{-1} = 100$ V gives $A = 2$ V·m, and $V(b) = 0$ gives $B = -A/b = -100$ V. So $V(r) = 2/r - 100$ V ($r$ in m) and
> $$
> \mathbf{E} = -\frac{dV}{dr}\hat{r} = \frac{2}{r^2}\hat{r}\ \text{V/m}:\qquad E(a) = 20\ \text{kV/m},\qquad E(b) = 5\ \text{kV/m}.
> $$
> $V(1.5\text{ cm}) = 2/0.015 - 100\approx33.3$ V, not 50 V.
>
> **Check:** with no charge between the shells, the flux through every sphere $r$ is the same, so $r^2E_r$ must be constant; here it is $A = 2$ V·m at every radius. The student's $10^4$ V/m is only the *average* field, $(V(a)-V(b))/(b-a)$. Put the student's linear $V$ into the spherical Laplacian and you get $-2\times10^4/r$, about $-1.33\times10^6$ V/m² at $1.5$ cm: that potential would need charge in the gap.
>
> **Answer.** The student used the Cartesian Laplacian in a spherical problem. Correct: $V(r) = 2/r - 100$ V, $\mathbf{E} = (2/r^2)\,\hat{r}$ V/m, so $E(a) = 20$ kV/m and $E(b) = 5$ kV/m (both outward), and $V(1.5\text{ cm})\approx33.3$ V.

### 7.4 Wedge between two plates

> [!easy] Easy · Laplace's equation · cylindrical coordinates
> Two large conducting half-planes meet at a right angle along the $z$ axis, separated there by a hairline insulating gap. One occupies $\phi = 0$ (the half-plane $y = 0$, $x>0$) and is grounded; the other occupies $\phi = \pi/2$ ($x = 0$, $y>0$) and is held at $100$ V. The region $0<\phi<\pi/2$ between them is charge-free free space. (a) Argue that $V$ depends on $\phi$ only, and solve Laplace's equation for $V(\phi)$. (b) Find $\mathbf{E}$ at $r = 10$ cm on the bisector $\phi = \pi/4$, in cylindrical and in Cartesian components. (c) Find $\rho_s$ on the face of each plate toward this region, at $r = 10$ cm.
>
> *Source: classic.*

> [!hint]- Hint
> When only $\phi$ varies, the cylindrical Laplacian reduces to $\dfrac{1}{r^2}\dfrac{d^2V}{d\phi^2}$, and the gradient to $\dfrac1r\dfrac{dV}{d\phi}\hat\phi$.

> [!solution]- Solution
> **(a)** Each plate is a whole half-plane at one potential, so moving along $z$, or out along $r$, never changes the boundary values; nothing in the problem sets a length scale. Try $V = V(\phi)$:
> $$
> \nabla^2V = \frac{1}{r^2}\frac{d^2V}{d\phi^2} = 0\quad\Longrightarrow\quad V = A\phi + B .
> $$
> $V(0) = 0$ gives $B = 0$, and $V(\pi/2) = 100$ V gives $A = 200/\pi$ V/rad. So $V = (200/\pi)\,\phi$ V. It satisfies Laplace's equation and both boundary values, and it stays bounded far from the corner, so by uniqueness it *is* the answer. (Boundedness matters because the region is open: $V + c\,xy$ also satisfies Laplace's equation and both plate values, but grows without limit.) On the bisector, $V = 50$ V.
>
> **(b)**
> $$
> \mathbf{E} = -\frac1r\frac{dV}{d\phi}\hat\phi = -\frac{200}{\pi r}\hat\phi\ \text{V/m},\qquad \lvert\mathbf{E}\rvert = \frac{2000}{\pi}\approx637\ \text{V/m at}\ r = 10\ \text{cm}.
> $$
> It points along $-\hat\phi$: around the corner from the 100 V plate toward the grounded one (clockwise seen from $+z$). At $\phi = \pi/4$, $-\hat\phi = \hat{x}\sin\phi - \hat{y}\cos\phi = (\hat{x}-\hat{y})/\sqrt2$, so $\mathbf{E}\approx450\,\hat{x} - 450\,\hat{y}$ V/m.
>
> **(c)** $\rho_s = \hat{n}\cdot\epsilon_0\mathbf{E}$ with $\hat{n}$ out of the plate into the field region. On $\phi = 0$, $\hat{n} = +\hat\phi$ (that is, $+\hat{y}$): $\rho_s = \epsilon_0E_\phi = -\dfrac{200\,\epsilon_0}{\pi r}\approx-5.64$ nC/m² at $r = 10$ cm. On $\phi = \pi/2$, $\hat{n} = -\hat\phi$ (that is, $+\hat{x}$): $\rho_s\approx+5.64$ nC/m².
>
> **Check:** walk the quarter circle of radius $10$ cm from the 100 V plate to the grounded one: $\lvert\mathbf{E}\rvert\times(\pi r/2) = (2000/\pi)(0.05\pi) = 100$ V ✓. The field and the charge grow like $1/r$ toward the corner, where the plates are closest.
>
> **Answer.** $V = (200/\pi)\,\phi$ V; $\mathbf{E} = -(200/\pi r)\,\hat\phi$ V/m, about $637$ V/m at $r = 10$ cm, i.e. $450\,\hat{x} - 450\,\hat{y}$ V/m on the bisector; $\rho_s\approx-5.64$ nC/m² on the grounded plate and $+5.64$ nC/m² on the 100 V plate at $r = 10$ cm.

### 7.5 Laplace's equation, true or false

> [!easy] Easy · true or false · uniqueness
> A region of free space contains no charge, and $V$ satisfies Laplace's equation in it. True or false? Give a one-line reason for each.
>
> (a) If $V_1$ and $V_2$ both satisfy Laplace's equation in the region, so does $3V_1 - 2V_2 + 7$.
>
> (b) If $V$ satisfies Laplace's equation, so does $V^2$.
>
> (c) There can be a point inside the region where $V$ is lower than at every point around it.
>
> (d) If $V = 0$ everywhere on the closed surface that bounds the region, then $V = 0$ everywhere inside.
>
> *Source: original.*

> [!hint]- Hint
> For (b), expand $\nabla\cdot\nabla(V^2)$ with the product rule. For (c), recall what Lecture 7 says $\nabla^2V$ measures at a point. For (d), find one function that obviously works, then think about uniqueness.

> [!solution]- Solution
> **(a) True.** Laplace's equation is linear: $\nabla^2(3V_1 - 2V_2 + 7) = 3\nabla^2V_1 - 2\nabla^2V_2 + 0 = 0$. This is superposition, the reason building-block solutions may be added.
>
> **(b) False.** By the product rule, $\nabla^2(V^2) = \nabla\cdot(2V\nabla V) = 2V\nabla^2V + 2\lvert\nabla V\rvert^2 = 2\lvert\mathbf{E}\rvert^2$, positive wherever there is a field. Simplest counterexample: $V = x$ is harmonic, but $\nabla^2(x^2) = 2\neq0$. A linear equation allows sums and multiples of solutions, not squares.
>
> **(c) False.** $\nabla^2V$ at a point is proportional to (average of $V$ over a small sphere around the point) minus (the value at the point). With $\nabla^2V = 0$, $V$ everywhere equals the average around it, so no point can sit below all its neighbours: no pits, and no peaks, in empty space. A pit needs $\nabla^2V>0$, i.e. negative charge right there.
>
> **(d) True.** $V = 0$ satisfies Laplace's equation and the boundary values, and the solution with given boundary values is unique, so it is the only one. (Equivalently, by (c): with no peaks or pits inside, $V$ stays between its largest and smallest boundary values, and both are zero.)
>
> **Watch out:** (c) is why a charge cannot be held in stable equilibrium by electrostatic fields alone — a stable spot would be a pit of potential energy in a charge-free region.
>
> **Answer.** (a) true, (b) false, (c) false, (d) true.

## Medium

### 7.6 Coaxial cable by Laplace

> [!medium] Medium · Laplace's equation · coaxial cable · surface charge
> A long air-filled coaxial cable has an inner conductor of radius $a = 1$ mm held at $100$ V and an outer conductor of inner radius $b = 4$ mm that is grounded. (a) Solve Laplace's equation for $V(r)$ in $a<r<b$. (b) Find $\mathbf{E}$ at $r = a$ and at $r = b$. (c) At what radius is $V = 50$ V? (d) Find the surface charge density on each conductor surface facing the gap, and the charge per unit length on each conductor.
>
> *Source: classic.*

> [!hint]- Hint
> In cylindrical coordinates with $V = V(r)$, Laplace's equation says $r\,dV/dr$ is constant, so $V = A\ln r + B$. Writing it as $V = C\ln(b/r)$ makes the grounded outer conductor automatic.

> [!solution]- Solution
> **Setup.** A long cable with round conductors: $V$ depends on $r$ only, and $\rho = 0$ in the gap, so
> $$
> \frac1r\frac{d}{dr}\Big(r\frac{dV}{dr}\Big) = 0\quad\Longrightarrow\quad V = A\ln r + B .
> $$
> **(a)** $V(b) = 0$ suggests the form $V = C\ln(b/r)$. Then $V(a) = C\ln4 = 100$ V gives $C = 100/1.386\approx72.1$ V:
> $$
> V(r) = \frac{100}{\ln4}\,\ln\frac{b}{r}\approx72.1\,\ln\frac{b}{r}\ \text{V}.
> $$
> **(b)** $\mathbf{E} = -\dfrac{dV}{dr}\hat{r} = \dfrac{C}{r}\hat{r}$, radially outward, from the 100 V conductor to the grounded one. $E(a) = 72.1/10^{-3}\approx72.1$ kV/m and $E(b) = E(a)/4\approx18.0$ kV/m.
>
> **(c)** $V = 50$ V means $\ln(b/r) = \tfrac12\ln(b/a)$, so $r = \sqrt{ab} = 2$ mm, the *geometric* mean. At the arithmetic mean, $2.5$ mm, $V\approx33.9$ V: the potential drops fastest near the thin inner conductor, where the field is strongest.
>
> **(d)** $\rho_s = \hat{n}\cdot\epsilon_0\mathbf{E}$ with $\hat{n}$ out of each conductor into the gap: $\hat{n} = +\hat{r}$ at $r = a$ and $-\hat{r}$ at $r = b$.
> $$
> \rho_s(a) = \epsilon_0E(a)\approx639\ \text{nC/m}^2,\qquad \rho_s(b) = -\epsilon_0E(b)\approx-160\ \text{nC/m}^2 .
> $$
> Per unit length, $\rho_l = 2\pi a\,\rho_s(a) = \dfrac{2\pi\epsilon_0(100)}{\ln4}\approx4.01$ nC/m on the inner conductor, and $2\pi b\,\rho_s(b)\approx-4.01$ nC/m on the outer one.
>
> **Check:** Gauss's law with $\rho_l = 4.01$ nC/m gives $E = \rho_l/(2\pi\epsilon_0r)$, which at $r = 3$ mm is $24.0$ kV/m, the same as $C/r = 72.1/0.003$ ✓. The charges per length are equal and opposite: every field line that leaves the inner conductor ends on the outer one.
>
> **Watch out:** the outer conductor carries the *smaller* surface density but the same total charge per length; $\rho_s$ scales as $1/r$ because the same charge is spread over a larger circumference.
>
> **Answer.** $V(r) = (100/\ln4)\ln(b/r)\approx72.1\ln(b/r)$ V; $\mathbf{E} = (72.1/r)\,\hat{r}$ V/m, i.e. $72.1$ kV/m at $r = a$ and $18.0$ kV/m at $r = b$; $V = 50$ V at $r = 2$ mm; $\rho_s\approx+639$ nC/m² (inner) and $-160$ nC/m² (outer); $\rho_l\approx\pm4.01$ nC/m.

### 7.7 Space charge between grounded plates

> [!medium] Medium · Poisson's equation · space charge · surface charge
> Two large grounded plates in free space lie on $x = 0$ and $x = d = 3$ cm, and the gap holds a fixed space charge. (a) For a uniform density $\rho = \rho_0 = 1\ \mu\text{C/m}^3$, find $V(x)$, the maximum potential and where it occurs, $\mathbf{E}$ at each plate, and the surface charge density on each plate. (b) Repeat for the graded density $\rho(x) = 2\rho_0x/d$, which carries the same total charge per unit area. (c) For (b), check that the plates carry exactly the opposite of the space charge, and show that the plane where $\mathbf{E} = 0$ divides the space charge between the plates in the same ratio as the plate charges.
>
> *Source: original.*

> [!hint]- Hint
> Integrate $V'' = -\rho(x)/\epsilon_0$ twice and fix the two constants with $V(0) = V(d) = 0$. The maximum of $V$ is where $V' = 0$, i.e. where $\mathbf{E} = 0$.

> [!solution]- Solution
> **Setup.** Infinite plates, so $V = V(x)$, and inside the charge Poisson's equation reads $V'' = -\rho(x)/\epsilon_0$ with $V(0) = V(d) = 0$. A useful number: $\rho_0/\epsilon_0\approx1.13\times10^5$ V/m².
>
> **(a)** Integrating twice and using $V(0) = 0$: $V = -\rho_0x^2/(2\epsilon_0) + C_1x$; then $V(d) = 0$ gives $C_1 = \rho_0d/(2\epsilon_0)$:
> $$
> V(x) = \frac{\rho_0\,x(d-x)}{2\epsilon_0},\qquad V_{\max} = V(d/2) = \frac{\rho_0d^2}{8\epsilon_0}\approx12.7\ \text{V at}\ x = 1.5\ \text{cm}.
> $$
> $E_x = -V' = \rho_0(x - d/2)/\epsilon_0$, so $E_x(0) = -\rho_0d/(2\epsilon_0)\approx-1.69$ kV/m and $E_x(d)\approx+1.69$ kV/m: at both plates the field points *into* the plate. With $\hat{n}$ out of each plate into the gap, $\rho_s(0) = \epsilon_0E_x(0) = -\rho_0d/2 = -15$ nC/m² and $\rho_s(d) = -\epsilon_0E_x(d) = -15$ nC/m².
>
> **(b)** $V'' = -2\rho_0x/(\epsilon_0d)$ integrates to $V = -\rho_0x^3/(3\epsilon_0d) + C_1x$, and $V(d) = 0$ gives $C_1 = \rho_0d/(3\epsilon_0)$:
> $$
> V(x) = \frac{\rho_0\,x\,(d^2-x^2)}{3\epsilon_0d},\qquad E_x = -V' = -\frac{\rho_0\,(d^2-3x^2)}{3\epsilon_0d}.
> $$
> $E_x = 0$ at $x = d/\sqrt3\approx1.73$ cm, where $V_{\max} = \dfrac{2\rho_0d^2}{9\sqrt3\,\epsilon_0}\approx13.0$ V. At the plates, $E_x(0) = -\rho_0d/(3\epsilon_0)\approx-1.13$ kV/m and $E_x(d) = +2\rho_0d/(3\epsilon_0)\approx+2.26$ kV/m, so $\rho_s(0) = -\rho_0d/3 = -10$ nC/m² and $\rho_s(d) = -2\rho_0d/3 = -20$ nC/m². The peak has moved toward the denser side, and the plate nearer the denser charge collects more induced charge.
>
> **(c)** Space charge per area: $\int_0^d\rho\,dx = \rho_0d = 30$ nC/m²; plates: $-10 - 20 = -30$ nC/m² ✓. Between $x = 0$ and the zero-field plane lies $\int_0^{d/\sqrt3}(2\rho_0x/d)\,dx = \rho_0d/3 = 10$ nC/m², and beyond it $20$ nC/m² — the ratio $1:2$ of the plate charges. Reason: a Gauss box from inside a plate (where $\mathbf{E} = 0$) to the plane $\mathbf{E} = 0$ has zero flux, so it encloses zero charge; each plate exactly balances the space charge on its side.
>
> **Check:** both profiles satisfy $V'' = -\rho/\epsilon_0$ and $V(0) = V(d) = 0$ by direct substitution, and $V''\le0$ everywhere in the gap: dome-shaped, as positive charge demands.
>
> **Answer.** (a) $V = \rho_0x(d-x)/(2\epsilon_0)$, $V_{\max}\approx12.7$ V at $x = 1.5$ cm; $E_x\approx-1.69$ kV/m at $x = 0$ and $+1.69$ kV/m at $x = d$ (into each plate); $\rho_s = -15$ nC/m² on each plate. (b) $V = \rho_0x(d^2-x^2)/(3\epsilon_0d)$, $V_{\max}\approx13.0$ V at $x\approx1.73$ cm; $E_x(0)\approx-1.13$ kV/m, $E_x(d)\approx+2.26$ kV/m; $\rho_s(0) = -10$ nC/m², $\rho_s(d) = -20$ nC/m². (c) the plates carry $-30$ nC/m² $= -\rho_0d$ in total, split $1:2$ like the space charge on either side of $x = d/\sqrt3$.

### 7.8 Plates and a charged sheet

> [!medium] Medium · Laplace's equation · boundary conditions · charge sheets
> Two large conducting plates in free space lie on $z = 0$ (grounded) and $z = 4$ m (held at $3$ V). A thin sheet of charge $\rho_s = 9\epsilon_0$ C/m² lies on the plane $z = 3$ m between them; there is no other charge in the gap. (a) Find $V(z)$ in both regions and the potential of the sheet. (b) Find $\mathbf{E}$ in both regions. (c) Find the surface charge density on the inner face of each plate, and check that the total charge is zero. (d) Keep the sheet charge as a symbol $\rho_s$: find the sheet potential as a function of $\rho_s$, and evaluate it for $\rho_s = 13\epsilon_0$ C/m².
>
> *Source: original.*

> [!hint]- Hint
> Laplace's equation holds separately in $0<z<3$ m and $3<z<4$ m, so $V$ is a different straight line in each. Call the unknown sheet potential $V_s$: continuity of $V$ is then built in, and the jump condition $\hat{z}\cdot(\mathbf{D}_{\text{above}} - \mathbf{D}_{\text{below}}) = \rho_s$ fixes $V_s$.

> [!solution]- Solution
> **Setup.** The sheet splits the gap into two charge-free regions, so Laplace's equation holds in each and $V$ is linear in each. Let $V_s$ be the unknown potential of the sheet ($V$ is continuous there):
> $$
> V(z) = \begin{cases} V_s\,z/3, & 0\le z\le3\ \text{m}\\[4pt] V_s + (3 - V_s)(z-3), & 3\le z\le4\ \text{m}\end{cases}
> \qquad\Longrightarrow\qquad
> E_z = \begin{cases} -V_s/3 & \text{below the sheet}\\[4pt] V_s - 3 & \text{above the sheet.}\end{cases}
> $$
> The sheet fixes the jump in $D_z$. With $\hat{n} = +\hat{z}$ pointing from the region below (medium 2) into the region above (medium 1), $\epsilon_0\big[E_z(\text{above}) - E_z(\text{below})\big] = \rho_s$:
> $$
> V_s - 3 + \frac{V_s}{3} = \frac{\rho_s}{\epsilon_0}\quad\Longrightarrow\quad \boxed{V_s = \frac34\Big(\frac{\rho_s}{\epsilon_0} + 3\Big)}
> $$
> **(a)** With $\rho_s/\epsilon_0 = 9$ V/m: $V_s = 9$ V, so $V(z) = 3z$ V below the sheet and $V(z) = 27 - 6z$ V above it ($z$ in m).
>
> **(b)** $\mathbf{E} = -3\,\hat{z}$ V/m for $0<z<3$ m and $+6\,\hat{z}$ V/m for $3<z<4$ m: pointing away from the positive sheet on both sides.
>
> **(c)** At $z = 0$, $\hat{n} = +\hat{z}$: $\rho_s(0) = \epsilon_0E_z = -3\epsilon_0\approx-2.66\times10^{-11}$ C/m². At $z = 4$ m, $\hat{n} = -\hat{z}$: $\rho_s(4) = -\epsilon_0E_z = -6\epsilon_0\approx-5.31\times10^{-11}$ C/m². Total: $-3\epsilon_0 - 6\epsilon_0 + 9\epsilon_0 = 0$ ✓ — every field line leaving the sheet ends on a plate.
>
> **(d)** The boxed formula with $\rho_s/\epsilon_0 = 13$ V/m gives $V_s = \tfrac34(16) = 12$ V; then $E_z = -4$ V/m below and $+9$ V/m above the sheet, and the plates carry $-4\epsilon_0$ and $-9\epsilon_0$ C/m².
>
> **Check:** superpose three sheets, $-3\epsilon_0$ at $z = 0$, $9\epsilon_0$ at $z = 3$ m and $-6\epsilon_0$ at $z = 4$ m, each giving $\rho_s/(2\epsilon_0)$ directed away from itself: $E_z = 0,\ -3,\ +6,\ 0$ V/m in the four regions — the same field, and zero outside the plates. Note also that the sheet is the highest point of $V$: a maximum of the potential can only sit on charge.
>
> **Watch out:** the jump condition is (field above) minus (field below), with $\hat{n}$ pointing from below to above. Subtracting in the other order makes $V_s$ come out negative — a potential minimum on a positive sheet, which is impossible.
>
> **Answer.** $V_s = 9$ V; $V = 3z$ V for $0\le z\le3$ m and $V = 27 - 6z$ V for $3\le z\le4$ m; $\mathbf{E} = -3\,\hat{z}$ V/m below and $+6\,\hat{z}$ V/m above the sheet; $\rho_s = -3\epsilon_0\approx-2.66\times10^{-11}$ C/m² at $z = 0$ and $-6\epsilon_0\approx-5.31\times10^{-11}$ C/m² at $z = 4$ m; $V_s = \tfrac34(\rho_s/\epsilon_0 + 3)$ V with $\rho_s/\epsilon_0$ in V/m, which is $12$ V for $\rho_s = 13\epsilon_0$ C/m².

## Hard

### 7.9 Junction with an intrinsic layer

> [!hard] Hard · Poisson's equation · pn junction · matching conditions
> A one-dimensional p-i-n structure in free space has the charge density ($z$ in m)
> $$
> \rho(z) = \begin{cases}-3, & -3<z<-1\\ 0, & -1<z<1\quad\text{(intrinsic layer)}\\ +6, & 1<z<2\\ 0, & \text{elsewhere}\end{cases}\qquad[\text{C/m}^3].
> $$
> Keep $\epsilon_0$ as a symbol. The field vanishes for $z<-3$ m, and $V = 0$ there.
> (a) Show that the structure is neutral and find $E_z(z)$ in every region. Is the field zero for $z>2$ m?
> (b) Integrate Poisson's equation to find $V(z)$ in every region, matching $V$ at each interface. Give $V(-1)$, $V(0)$ and $V(1)$.
> (c) Find the built-in potential $V(2) - V(-3)$ and the largest field. Compare with the same two slabs placed side by side with no intrinsic layer, and explain the difference in one line.
> (d) A silicon p-i-n diode ($\epsilon = 11.7\epsilon_0$) has acceptor density $N_A = 10^{22}$ m⁻³ in a p-layer of width $W_1 = 0.2\ \mu$m, an intrinsic layer of width $g = 0.2\ \mu$m, and donor density $N_D = 2\times10^{22}$ m⁻³ in an n-layer of width $W_2 = 0.1\ \mu$m, so $\rho = -eN_A$ and $+eN_D$ in the doped layers ($e = 1.602\times10^{-19}$ C). Find the largest field and the built-in potential.
>
> *Source: Summer 2019 HE1 #1a style (oppositely charged slabs separated by a gap, $\epsilon_0$ kept symbolic) and Summer 2020 HE1 #2a (V inside a slab), extended to the junction of course notes Lecture 7, Example 4.*

> [!hint]- Hint
> Work from left to right. $E_z$ starts at zero and changes at the rate $dE_z/dz = \rho/\epsilon_0$ (Gauss's law, or Poisson's equation integrated once); $V$ then changes at the rate $dV/dz = -E_z$. In the intrinsic layer $\rho = 0$, so $E_z$ is constant there — and that constant field over $2$ m is the new ingredient in (c).

> [!solution]- Solution
> **Setup.** Everything depends on $z$ only, so Poisson's equation is $d^2V/dz^2 = -\rho/\epsilon_0$, which splits into $dE_z/dz = \rho/\epsilon_0$ and $dV/dz = -E_z$. Start at $z = -3$ m, where $E_z = 0$ and $V = 0$, and integrate region by region. There are no surface charges, so both $E_z$ and $V$ are continuous at every interface.
>
> **(a)** Charge per unit area: $(-3)(2) + (6)(1) = 0$, so the structure is neutral. Integrating $dE_z/dz = \rho/\epsilon_0$:
> $$
> \epsilon_0E_z = \begin{cases} -3(z+3), & -3<z<-1\\ -6, & -1<z<1\\ 6(z-2), & 1<z<2\\ 0, & z<-3\ \text{or}\ z>2 .\end{cases}
> $$
> The last slab brings $E_z$ back to exactly zero at $z = 2$ m, as neutrality guarantees: a Gauss pillbox around the whole structure encloses no charge. So yes, $\mathbf{E} = 0$ for $z>2$ m. Inside, $E_z<0$: the field points from the positive n-side toward the negative p-side.
>
> **(b)** Integrating $dV/dz = -E_z$ and matching $V$ at $z = -1$, $1$ and $2$ m:
> $$
> \epsilon_0V = \begin{cases} \tfrac32(z+3)^2, & -3\le z\le-1\\ 6(z+2), & -1\le z\le1\\ 21 - 3(z-2)^2, & 1\le z\le2\\ 21, & z\ge2 .\end{cases}
> $$
> The matching: at $z = -1$ the first branch gives $6$ and the second $6(1) = 6$ ✓; at $z = 1$ the second gives $6(3) = 18$ and the third $21 - 3 = 18$ ✓. So $V(-1) = 6/\epsilon_0$, $V(0) = 12/\epsilon_0\approx1.36\times10^{12}$ V and $V(1) = 18/\epsilon_0$ (volts, with $\epsilon_0$ in SI units). Curvature check: $V'' = -\rho/\epsilon_0 = +3/\epsilon_0>0$ in the negative slab (bowl), $0$ in the intrinsic layer (straight line), $-6/\epsilon_0<0$ in the positive slab (dome).
>
> **(c)** $V(2) - V(-3) = 21/\epsilon_0\approx2.37\times10^{12}$ V. The largest field is the constant $\lvert E_z\rvert = 6/\epsilon_0\approx6.78\times10^{11}$ V/m (along $-\hat{z}$) throughout the intrinsic layer. Without the layer, the lecture's junction formula gives
> $$
> V_2 - V_1 = \frac{\rho_2W_2\,(W_1+W_2)}{2\epsilon_0} = \frac{6\cdot1\cdot3}{2\epsilon_0} = \frac{9}{\epsilon_0}\approx1.02\times10^{12}\ \text{V}.
> $$
> The difference, $12/\epsilon_0$, is exactly $E_{\max}\times g = (6/\epsilon_0)(2)$: the intrinsic layer inserts a stretch of uniform field, while the peak field stays the same because it is set by the charge $\rho_1W_1$ on one side.
>
> **(d)** Same structure, new numbers: $eN_A\approx1.60\times10^3$ C/m³ and $eN_D\approx3.20\times10^3$ C/m³, and it is neutral because $N_AW_1 = N_DW_2 = 2\times10^{15}$ m⁻². The peak field, constant across the intrinsic layer, is
> $$
> E_{\max} = \frac{eN_AW_1}{\epsilon} = \frac{(1.602\times10^{-19})(10^{22})(0.2\times10^{-6})}{11.7\times8.854\times10^{-12}}\approx3.09\ \text{MV/m},
> $$
> and the potential is the area under the $\lvert E_z\rvert$ profile — two triangles and a rectangle:
> $$
> V_2 - V_1 = E_{\max}\Big(\frac{W_1}{2} + g + \frac{W_2}{2}\Big) = (3.09\times10^6)(0.35\times10^{-6})\approx1.08\ \text{V}.
> $$
> **Check:** the same area rule reproduces (c): $6\,(1 + 2 + 0.5) = 21$ in units of $1/\epsilon_0$ ✓. And $E_{\max} = eN_DW_2/\epsilon$, computed from the n side, gives the same $3.09$ MV/m, as neutrality demands.
>
> **Watch out:** the curvature of $V$ is set by the *local* charge density. In the intrinsic layer $V$ is a straight line even though it sits between two charged slabs — Laplace's equation holds there.
>
> **Answer.** (a) Neutral; $\epsilon_0E_z = -3(z+3)$, $-6$ and $6(z-2)$ in the three layers and $0$ outside, including $z>2$ m. (b) $\epsilon_0V = \tfrac32(z+3)^2$, $6(z+2)$, $21 - 3(z-2)^2$, then $21$; $V(-1) = 6/\epsilon_0$, $V(0) = 12/\epsilon_0$, $V(1) = 18/\epsilon_0$. (c) $V(2) - V(-3) = 21/\epsilon_0\approx2.37\times10^{12}$ V; largest field $6/\epsilon_0\approx6.78\times10^{11}$ V/m along $-\hat{z}$ in the intrinsic layer; without the layer $9/\epsilon_0$. (d) $E_{\max}\approx3.09$ MV/m and a built-in potential of about $1.08$ V.

### 7.10 Space-charge-limited vacuum diode

> [!hard] Hard · Poisson's equation · vacuum diode · space charge
> In a planar vacuum diode the cathode ($x = 0$, $V = 0$) emits electrons with negligible initial speed, and the anode at $x = d = 8$ mm is held at $V_a = 16$ V. In the space-charge-limited steady state the potential between the electrodes is $V(x) = V_a(x/d)^{4/3}$. Use $e = 1.602\times10^{-19}$ C and $m_e = 9.109\times10^{-31}$ kg.
> (a) Check the boundary values and find $V$ at $x = 1$ mm.
> (b) Use Poisson's equation to find the charge density $\rho(x)$ of the electron cloud. Evaluate it at $x = 1$ mm and at the anode. Why is its sign right?
> (c) Find $\mathbf{E}(x)$ and the surface charge densities on the cathode and the anode. Show that the electrodes plus the space charge are neutral, and compare the anode charge with that of the same diode without electrons.
> (d) An electron leaving the cathode at rest has speed $v(x) = \sqrt{2eV(x)/m_e}$ (energy conservation). Show that the current density $\mathbf{J} = \rho v\,\hat{x}$ is the same at every $x$, and evaluate it with its direction. Find the transit time of an electron from cathode to anode.
>
> *Source: FA26 HW3 #1 style (vacuum diode with $V\propto x^{4/3}$), new numbers; part (d) classic (Child–Langmuir law).*

> [!hint]- Hint
> $\rho = -\epsilon_0V''$. For (c), $\rho_s = \hat{n}\cdot\epsilon_0\mathbf{E}$ with $\hat{n}$ out of each electrode into the gap, and you will need $\int_0^dx^{-2/3}dx = 3d^{1/3}$. For (d), write $\rho\propto x^{-2/3}$ and $v\propto x^{2/3}$ before multiplying.

> [!solution]- Solution
> **(a)** $V(0) = 0$ and $V(d) = V_a$ ✓. $V(1\text{ mm}) = 16\,(1/8)^{4/3} = 16/16 = 1$ V.
>
> **(b)** Differentiating twice, $V' = \dfrac{4V_a}{3d}\Big(\dfrac xd\Big)^{1/3}$ and $V'' = \dfrac{4V_a}{9d^2}\Big(\dfrac dx\Big)^{2/3}$, so
> $$
> \rho(x) = -\epsilon_0V'' = -\frac{4\epsilon_0V_a}{9d^2}\Big(\frac dx\Big)^{2/3},\qquad \frac{4\epsilon_0V_a}{9d^2}\approx9.84\times10^{-7}\ \text{C/m}^3 .
> $$
> $\rho(1\text{ mm}) = -9.84\times10^{-7}\times8^{2/3}\approx-3.94\ \mu$C/m³ and $\rho(d)\approx-0.984\ \mu$C/m³. The sign is negative because the carriers are electrons, and $V''>0$ (a bowl-shaped $V$) is exactly what negative charge produces. The density is largest near the cathode, where the electrons are slowest and crowd together.
>
> **(c)** $\mathbf{E} = -V'\hat{x} = -\dfrac{4V_a}{3d}\Big(\dfrac xd\Big)^{1/3}\hat{x}$: zero at the cathode and $-2.67\,\hat{x}$ kV/m at the anode, pointing from anode to cathode, so it pushes electrons toward the anode. With $\hat{n} = +\hat{x}$ at the cathode and $-\hat{x}$ at the anode:
> $$
> \rho_s(0) = \epsilon_0E_x(0) = 0,\qquad \rho_s(d) = -\epsilon_0E_x(d) = \frac{4\epsilon_0V_a}{3d}\approx23.6\ \text{nC/m}^2 .
> $$
> The space charge per unit area is $\displaystyle\int_0^d\rho\,dx = -\frac{4\epsilon_0V_a}{9d^2}\,d^{2/3}\cdot3d^{1/3} = -\frac{4\epsilon_0V_a}{3d}\approx-23.6$ nC/m², which cancels the anode charge ✓. Without electrons $V$ would be linear and the anode would carry $\epsilon_0V_a/d\approx17.7$ nC/m²; the space charge raises it by the factor $4/3$. The zero field at the cathode is what "space-charge-limited" means: the cloud screens the cathode completely, so any extra electron emitted would be pushed back.
>
> **(d)** $v(x) = \sqrt{2eV_a/m_e}\,(x/d)^{2/3}$, with $v(d) = \sqrt{2(1.602\times10^{-19})(16)/(9.109\times10^{-31})}\approx2.37\times10^6$ m/s. In $\rho v$ the factors $(d/x)^{2/3}$ and $(x/d)^{2/3}$ cancel:
> $$
> J_x = \rho v = -\frac{4\epsilon_0}{9}\sqrt{\frac{2e}{m_e}}\,\frac{V_a^{3/2}}{d^2}\approx-2.33\ \text{A/m}^2 ,
> $$
> independent of $x$, as a steady current must be: continuity gives $\nabla\cdot\mathbf{J} = -\partial\rho/\partial t = 0$. $\mathbf{J}$ points along $-\hat{x}$, opposite to the motion of the (negative) electrons. The transit time, with $u = x/d$:
> $$
> T = \int_0^d\frac{dx}{v} = \frac{d}{v(d)}\int_0^1u^{-2/3}\,du = \frac{3d}{v(d)}\approx10.1\ \text{ns}.
> $$
> **Check:** the current must equal the charge in transit divided by the transit time, and it does:
> $$
> \frac{4\epsilon_0V_a/(3d)}{3d/v(d)} = \frac{4\epsilon_0V_a}{9d^2}\,v(d) = \lvert\rho(d)\rvert\,v(d) = \lvert J_x\rvert\ \checkmark
> $$
>
> **Watch out:** $\rho$ is negative, so $\mathbf{J}$ and the electron velocity point in opposite directions; quoting $+2.33\,\hat{x}$ A/m² is the classic sign slip.
>
> **Answer.** (a) $V(1\text{ mm}) = 1$ V. (b) $\rho = -(4\epsilon_0V_a/9d^2)(d/x)^{2/3}$: $-3.94\ \mu$C/m³ at 1 mm and $-0.984\ \mu$C/m³ at the anode. (c) $\mathbf{E} = -(4V_a/3d)(x/d)^{1/3}\,\hat{x}$, zero at the cathode and $-2.67\,\hat{x}$ kV/m at the anode; $\rho_s = 0$ on the cathode and $+23.6$ nC/m² on the anode, balancing $-23.6$ nC/m² of space charge (empty diode: $17.7$ nC/m²). (d) $\mathbf{J}\approx-2.33\,\hat{x}$ A/m² at every $x$; $v(d)\approx2.37\times10^6$ m/s; $T\approx10.1$ ns.

### 7.11 Charged ball, two ways

> [!hard] Hard · Poisson's equation · spherical symmetry · uniqueness
> A ball of radius $a = 10$ cm in free space carries a uniform charge density $\rho_0 = 1\ \mu\text{C/m}^3$, and $V\to0$ far away.
> (a) Write Poisson's equation inside the ball and Laplace's equation outside for $V(r)$, and give their general solutions. Explain why one constant is dropped in each region.
> (b) Fix the remaining constants by matching at $r = a$. Which two conditions do you use, and why do both hold?
> (c) Evaluate $V(0)$, $V(5\text{ cm})$, $V(a)$ and $V(20\text{ cm})$.
> (d) Check $V(0)$ independently with the general solution $V(\mathbf{r}) = \displaystyle\int\frac{\rho(\mathbf{r}')}{4\pi\epsilon_0\lvert\mathbf{r}-\mathbf{r}'\rvert}\,d^3\mathbf{r}'$, building the ball from thin shells.
>
> *Source: classic.*

> [!hint]- Hint
> Inside, multiply $\dfrac{1}{r^2}\dfrac{d}{dr}\Big(r^2\dfrac{dV}{dr}\Big) = -\dfrac{\rho_0}{\epsilon_0}$ by $r^2$ and integrate twice. A term $A/r$ inside would be the potential of a point charge at the centre, which the problem does not have. For (d), every point of a shell of radius $r'$ is the same distance $r'$ from the centre.

> [!solution]- Solution
> **(a)** Spherical symmetry: $V = V(r)$.
> $$
> r<a:\quad \frac{1}{r^2}\frac{d}{dr}\Big(r^2\frac{dV}{dr}\Big) = -\frac{\rho_0}{\epsilon_0}\ \Longrightarrow\ r^2\frac{dV}{dr} = -\frac{\rho_0r^3}{3\epsilon_0} + C_1\ \Longrightarrow\ V = -\frac{\rho_0r^2}{6\epsilon_0} - \frac{C_1}{r} + C_2 ,
> $$
> $$
> r>a:\quad \frac{1}{r^2}\frac{d}{dr}\Big(r^2\frac{dV}{dr}\Big) = 0\ \Longrightarrow\ V = \frac{C_3}{r} + C_4 .
> $$
> Inside, $C_1 = 0$: the $1/r$ term would blow up at the centre — it is the potential of a point charge there, which the problem does not have. Outside, $C_4 = 0$ because $V\to0$ far away.
>
> **(b)** At $r = a$: (i) $V$ is continuous (it always is — a finite field cannot produce a jump in potential), and (ii) $D_r = -\epsilon_0\,dV/dr$ is continuous, because there is no surface charge on $r = a$. From (ii): $-\rho_0a/(3\epsilon_0) = -C_3/a^2$, so $C_3 = \rho_0a^3/(3\epsilon_0) = Q/(4\pi\epsilon_0)$ with $Q = \tfrac43\pi a^3\rho_0$. From (i): $C_3/a = -\rho_0a^2/(6\epsilon_0) + C_2$, so $C_2 = \rho_0a^2/(2\epsilon_0)$:
> $$
> V(r) = \begin{cases}\dfrac{\rho_0\,(3a^2 - r^2)}{6\epsilon_0}, & r\le a\\[10pt] \dfrac{\rho_0a^3}{3\epsilon_0r} = \dfrac{Q}{4\pi\epsilon_0r}, & r\ge a .\end{cases}
> $$
> It satisfies the right equation in each region, both matching conditions and the condition at infinity, so by uniqueness it is *the* potential.
>
> **(c)** With $\rho_0/\epsilon_0\approx1.13\times10^5$ V/m²: $V(0) = \rho_0a^2/(2\epsilon_0)\approx565$ V, $V(5\text{ cm})\approx518$ V, $V(a) = \rho_0a^2/(3\epsilon_0)\approx376$ V and $V(20\text{ cm})\approx188$ V. The centre is the highest point, $\tfrac32V(a)$: inside positive charge $V$ is dome-shaped.
>
> **(d)** A shell of radius $r'$ and thickness $dr'$ holds $dq = \rho_0\,4\pi r'^2dr'$, all of it at distance $r'$ from the centre, so
> $$
> V(0) = \int_0^a\frac{\rho_0\,4\pi r'^2\,dr'}{4\pi\epsilon_0\,r'} = \frac{\rho_0}{\epsilon_0}\int_0^ar'\,dr' = \frac{\rho_0a^2}{2\epsilon_0} ,
> $$
> the same as (c) ✓. Two very different routes — a differential equation with boundary conditions, and a superposition integral — give one answer, as uniqueness promises.
>
> **Check:** $E_r = -dV/dr = \rho_0r/(3\epsilon_0)$ inside and $Q/(4\pi\epsilon_0r^2)$ outside, which is Gauss's law: at $r = 5$ cm, $4\pi r^2\epsilon_0E_r\approx0.524$ nC $= Q_{\text{enc}}$; outside, $Q\approx4.19$ nC.
>
> **Answer.** $V = \rho_0(3a^2 - r^2)/(6\epsilon_0)$ for $r\le a$ and $\rho_0a^3/(3\epsilon_0r)$ for $r\ge a$; $V(0)\approx565$ V, $V(5\text{ cm})\approx518$ V, $V(a)\approx376$ V, $V(20\text{ cm})\approx188$ V; the shell integral gives the same $V(0) = \rho_0a^2/(2\epsilon_0)$.

### 7.12 Grounded sphere in a uniform field

> [!hard] Hard · Laplace's equation · uniqueness · conductors
> A grounded conducting sphere of radius $a = 10$ cm is placed in free space in an initially uniform field $\mathbf{E}_0 = E_0\hat{z}$ with $E_0 = 1000$ V/m, centred at the origin. A candidate for the potential outside the sphere is
> $$
> V(r,\theta) = -E_0\Big(r - \frac{a^3}{r^2}\Big)\cos\theta\qquad(r\ge a).
> $$
> (a) Show that $V$ satisfies Laplace's equation for $r>a$.
> (b) Show that it meets the boundary conditions: $V = 0$ on the sphere, and $V\to-E_0z$ (the uniform field) far away. Why does this make it *the* answer?
> (c) Find $\mathbf{E}$ on the surface of the sphere. Where is the field strongest, and how strong is it?
> (d) Find the induced surface charge density $\rho_s(\theta)$, its values at the poles and on the equator, the charge on the upper hemisphere ($z>0$), and the total induced charge.
>
> *Source: classic.*

> [!hint]- Hint
> With no $\phi$ dependence, $\nabla^2V = \dfrac{1}{r^2}\dfrac{\partial}{\partial r}\Big(r^2\dfrac{\partial V}{\partial r}\Big) + \dfrac{1}{r^2\sin\theta}\dfrac{\partial}{\partial\theta}\Big(\sin\theta\dfrac{\partial V}{\partial\theta}\Big)$; work out the two parts separately and compare. On the conductor, $\rho_s = \hat{r}\cdot\epsilon_0\mathbf{E}$.

> [!solution]- Solution
> **(a)** Write $V = -E_0f(r)\cos\theta$ with $f = r - a^3/r^2$, so $f' = 1 + 2a^3/r^3$ and $r^2f' = r^2 + 2a^3/r$.
> $$
> \text{radial part:}\quad \frac{-E_0\cos\theta}{r^2}\frac{d}{dr}\Big(r^2 + \frac{2a^3}{r}\Big) = -2E_0\cos\theta\Big(\frac1r - \frac{a^3}{r^4}\Big),
> $$
> $$
> \text{angular part:}\quad \frac{-E_0f}{r^2\sin\theta}\frac{d}{d\theta}\big(-\sin^2\theta\big) = \frac{2E_0f\cos\theta}{r^2} = +2E_0\cos\theta\Big(\frac1r - \frac{a^3}{r^4}\Big).
> $$
> They cancel, so $\nabla^2V = 0$ for $r>a$ ✓. (Both parts blow up at $r = 0$, but that point is inside the metal, outside the region where we need the equation.)
>
> **(b)** At $r = a$, $f(a) = a - a = 0$, so $V = 0$ over the whole sphere ✓ — it is grounded and an equipotential. Far away $a^3/r^2\to0$ and $V\to-E_0r\cos\theta = -E_0z$, whose field is $E_0\hat{z}$ ✓. The solution of Laplace's equation with the potential fixed on every boundary is unique, so a guess that passes all these tests *is* the answer; there is nothing left to derive. Physically, the extra term $E_0a^3\cos\theta/r^2$ is the potential of a dipole $p = 4\pi\epsilon_0a^3E_0$ at the centre: from outside, the induced charges look like a dipole.
>
> **(c)**
> $$
> E_r = -\frac{\partial V}{\partial r} = E_0\Big(1 + \frac{2a^3}{r^3}\Big)\cos\theta,\qquad E_\theta = -\frac1r\frac{\partial V}{\partial\theta} = -E_0\Big(1 - \frac{a^3}{r^3}\Big)\sin\theta .
> $$
> At $r = a$: $E_r = 3E_0\cos\theta$ and $E_\theta = 0$ — the field is normal to the conductor, as it must be. It is strongest at the poles, $\lvert\mathbf{E}\rvert = 3E_0 = 3000$ V/m: three times the applied field.
>
> **(d)** $\hat{n} = \hat{r}$ points out of the conductor, so
> $$
> \rho_s = \epsilon_0E_r(a) = 3\epsilon_0E_0\cos\theta:\qquad +26.6\ \text{nC/m}^2\ \text{at}\ \theta = 0,\quad -26.6\ \text{nC/m}^2\ \text{at}\ \theta = \pi,\quad 0\ \text{on the equator}.
> $$
> Upper hemisphere: $\displaystyle\int_0^{\pi/2}3\epsilon_0E_0\cos\theta\;2\pi a^2\sin\theta\,d\theta = 3\pi\epsilon_0E_0a^2\approx8.34\times10^{-10}$ C. The lower hemisphere carries the opposite amount, so the total induced charge is zero: the sphere is grounded and could have drawn net charge from ground, but the symmetric field pulls in none.
>
> **Check:** far away $E_r\to E_0\cos\theta$ and $E_\theta\to-E_0\sin\theta$, which are exactly the spherical components of $E_0\hat{z}$ ✓. The positive charge gathers on the $+z$ side, the direction in which the applied field pushes positive charge.
>
> **Watch out:** off the $z$ axis, $E_\theta$ vanishes only *on* the sphere. Just off the surface the field already has a tangential part, which is how the field lines bend around the sphere.
>
> **Answer.** (a), (b) $V$ satisfies Laplace's equation and both boundary conditions, so by uniqueness it is the potential. (c) On the surface $\mathbf{E} = 3E_0\cos\theta\,\hat{r}$, normal to the sphere, with a maximum of $3E_0 = 3000$ V/m at the poles. (d) $\rho_s = 3\epsilon_0E_0\cos\theta$: $+26.6$ nC/m² at the north pole, $-26.6$ nC/m² at the south pole, $0$ on the equator; $+8.34\times10^{-10}$ C on the upper hemisphere; total induced charge $0$.

### Sources for this page
Course notes, Lecture 7: Examples 1–2 (parallel plates and their surface charges) behind 7.1, and Example 4 (the pn junction) extended with an intrinsic layer in 7.9. Old exams, re-parameterized: Summer 2019 HE1 #1a (oppositely charged slabs separated by a gap, $\epsilon_0$ kept symbolic) and Summer 2020 HE1 #2a ($V$ inside a charged slab, with a chosen reference) set the style of 7.9. FA26 homework: HW3 #1 (the vacuum diode with $V\propto x^{4/3}$) behind 7.10, with new numbers and the Child–Langmuir current added. Classic textbook problems with new numbers: the wedge (7.4), the coaxial cable (7.6), the uniformly charged ball (7.11) and the grounded sphere in a uniform field (7.12). Problems 7.2, 7.3, 7.5, 7.7 and 7.8 are original.

*Previous: [[practice/06-circulation-and-boundary-conditions|Lecture 6 practice]] · next: [[practice/08-conductors-dielectrics-and-polarization|Lecture 8 practice]] · [[practice/index|all practice]]*
