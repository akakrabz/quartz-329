---
title: "Practice — Lecture 3: Gauss's law at work"
description: "12 practice problems (5 easy, 3 medium, 4 hard) on flux through tilted and curved surfaces, δ-function charges, spheres, slabs and coaxes with uniform and graded densities, superposition of sheets, slabs and balls (up to a sphere with an off-centre cavity), and ∮B·dS = 0, each with a folded hint and a worked solution."
tags: [practice, electrostatics, exam-1]
lecture: 3
---

*Practice for [[1-electrostatics/03-gauss-law-at-work|Lecture 3]] · concepts: [[concepts/gauss-law]] · [[concepts/flux]] · [[concepts/superposition]] · [[concepts/charge-density]] · all practice: [[practice/index|hub]] · by difficulty: [[practice/easy|easy]] · [[practice/medium|medium]] · [[practice/hard|hard]] · [[practice/topics|by topic]]*

Work each problem on paper first. Open the **hint** only when stuck, and the **solution** only after you have an answer you would hand in. Every answer here has been checked numerically.

## Easy

### 3.1 Two sheets of charge

> [!easy] Easy · Gauss's law · charge sheets · superposition
> Two infinite sheets lie in free space: $\rho_{s1} = +4$ nC/m² on the plane $z = 0$ and $\rho_{s2} = -1$ nC/m² on the plane $z = 2$ m. Find $\mathbf{E}$ in the three regions $z<0$, $0<z<2$ m and $z>2$ m.
>
> *Source: original.*

> [!hint]- Hint
> One sheet gives a field of magnitude $\rho_s/(2\epsilon_0)$ on both sides, the same at every distance, pointing away from the sheet if it is positive. Add the two sheets region by region.

> [!solution]- Solution
> A single sheet $\rho_s$ on $z = z_0$ makes $\mathbf{E} = \dfrac{\rho_s}{2\epsilon_0}\operatorname{sgn}(z-z_0)\,\hat{z}$: pointing away from a positive sheet, toward a negative one, the same magnitude at every distance. Superpose:
> $$
> E_z = \frac{1}{2\epsilon_0}\Big[\rho_{s1}\operatorname{sgn}(z) + \rho_{s2}\operatorname{sgn}(z-2)\Big].
> $$
> $z<0$: $E_z = \dfrac{-4+1}{2\epsilon_0}\times10^{-9} = -169$ V/m. $\quad 0<z<2$: $E_z = \dfrac{4+1}{2\epsilon_0}\times10^{-9} = +282$ V/m. $\quad z>2$: $E_z = \dfrac{4-1}{2\epsilon_0}\times10^{-9} = +169$ V/m.
>
> **Check:** crossing $z = 0$ upward, $\epsilon_0E_z$ jumps by $(5+3)/2 = 4$ nC/m² $= \rho_{s1}$; crossing $z = 2$, by $(3-5)/2 = -1$ nC/m² $= \rho_{s2}$ — the boundary condition of Lecture 6.
>
> **Answer.** $\mathbf{E} = -169\,\hat{z}$ V/m for $z<0$, $+282\,\hat{z}$ V/m between the sheets, $+169\,\hat{z}$ V/m for $z>2$ m.

### 3.2 Flux through a tilted window

> [!easy] Easy · flux · surface normal
> A flat rectangular window in free space has corners $(0,0,0)$, $(0,2,0)$, $(3,2,4)$ and $(3,0,4)$, in metres. Choose its unit normal $\hat{n}$ with a positive $z$ component.
> (a) A uniform field $\mathbf{E} = 500\,\hat{z}$ V/m fills space. Find the flux $\int_S\mathbf{E}\cdot d\mathbf{S}$ through the window, and the flux of $\mathbf{D}$, $\psi_E = \int_S\mathbf{D}\cdot d\mathbf{S}$.
> (b) Repeat for the uniform field $\mathbf{E} = 300\,\hat{x}+400\,\hat{z}$ V/m, which has the same strength.
>
> *Source: original.*

> [!hint]- Hint
> Only the normal component of $\mathbf{E}$ crosses the window. Two edges leaving the corner at the origin are $\mathbf{u} = (0,2,0)$ and $\mathbf{v} = (3,0,4)$; their cross product gives you the normal *and* the area.

> [!solution]- Solution
> The edges from the origin, $\mathbf{u} = 2\,\hat{y}$ and $\mathbf{v} = 3\,\hat{x}+4\,\hat{z}$ (m), are perpendicular ($\mathbf{u}\cdot\mathbf{v} = 0$), so the window is a 2 m × 5 m rectangle. Their cross product is normal to the window and as long as the window's area:
> $$
> \mathbf{u}\times\mathbf{v} = 8\,\hat{x}-6\,\hat{z}\ \text{m}^2,\qquad A = \lvert\mathbf{u}\times\mathbf{v}\rvert = 10\ \text{m}^2 .
> $$
> It points toward negative $z$, so the normal we want is the opposite one: $\hat{n} = -0.8\,\hat{x}+0.6\,\hat{z}$. The field is uniform and the window flat, so the flux is simply $(\mathbf{E}\cdot\hat{n})A$.
>
> **(a)** $\mathbf{E}\cdot\hat{n} = 500\times0.6 = 300$ V/m, so $\int_S\mathbf{E}\cdot d\mathbf{S} = 300\times10 = 3000$ V·m, and $\psi_E = \epsilon_0\times3000\approx26.56$ nC.
>
> **(b)** $\mathbf{E}\cdot\hat{n} = 300(-0.8)+400(0.6) = 0$: no flux at all. Indeed $\mathbf{E} = 300\,\hat{x}+400\,\hat{z}$ is parallel to the edge $\mathbf{v} = 3\,\hat{x}+4\,\hat{z}$, so it lies in the plane of the window and its field lines slide along it without crossing.
>
> **Check:** a field along $\hat{z}$ only "sees" the window's shadow on the $xy$ plane, the rectangle $0\le x\le3$, $0\le y\le2$ of area 6 m²: $500\times6 = 3000$ V·m ✓.
>
> **Watch out:** both fields have $\lvert\mathbf{E}\rvert = 500$ V/m, yet the fluxes are 3000 V·m and zero. Flux is "field times area" only when the field is uniform *and* normal to the surface.
>
> **Answer.** (a) $\int_S\mathbf{E}\cdot d\mathbf{S} = 3000$ V·m and $\psi_E\approx26.56$ nC; (b) zero, because this $\mathbf{E}$ is parallel to the window.

### 3.3 Finite line in a closed cylinder

> [!easy] Easy · multiple choice · Gauss's law
> A segment of line charge, $\rho_l = 3$ nC/m, occupies the $z$ axis for $-1<z<1$ m in free space. A closed cylindrical surface (curved side plus both flat caps) bounds the region $r\le1$ m, $-2\le z\le2$ m. Which statement is true?
>
> (a) The outward flux of $\mathbf{D}$ is 6 nC, and all of it leaves through the curved side; the caps get none.
>
> (b) The outward flux of $\mathbf{D}$ is 6 nC; most of it leaves through the curved side, but some leaves through the caps.
>
> (c) The flux cannot be found without integrating Coulomb's law, because a finite segment has no cylindrical symmetry.
>
> (d) The outward flux of $\mathbf{D}$ is 12 nC.
>
> *Source: original.*

> [!hint]- Hint
> Gauss's law is *always* true; symmetry is only needed to turn it into a formula for $\mathbf{E}$. And near the ends of a finite segment, which way do the field lines fan out?

> [!solution]- Solution
> **(b).** Gauss's law holds for any closed surface and any charge distribution: the total outward flux equals the enclosed charge, $\rho_l\times(2\text{ m}) = 6$ nC. How that total is shared among the pieces depends on the field, though. The segment's field lines fan out past its ends, so the field has a $z$ component on the caps and some flux leaves through them. A direct Coulomb integration gives $\rho_l(\sqrt{10}-\sqrt{2})\approx5.244$ nC through the curved side and $\approx0.378$ nC through each cap: $5.244+0.756 = 6$ nC ✓.
>
> (a) is the infinite-line picture: there the field is purely radial and the caps carry nothing. A finite segment's field is not purely radial.
>
> (c) confuses "Gauss's law is true" with "Gauss's law alone gives $\mathbf{E}$". Without symmetry you cannot pull $D$ out of the integral, but the *total* flux needs no symmetry at all.
>
> (d) is $\rho_l\times4$ m, the length of the surface. Only the charge inside counts, and the line exists only for $-1<z<1$.
>
> **Answer.** (b): 6 nC in total, about 5.24 nC through the side and 0.378 nC through each cap.

### 3.4 Charges written with delta functions

> [!easy] Easy · delta functions · enclosed charge
> In free space the charge density is
> $$
> \begin{aligned}
> \rho(x,y,z) = 10^{-9}\Big[&\,4\,\delta(x-1)\,\delta(y+1)\,\delta(z) - 2\,\delta(x+1)\,\delta(y)\\
> &+ 0.5\,\delta(z-1) + 2\,\delta(x)\,\delta(y-3)\,\delta(z)\Big]\ \text{C/m}^3,
> \end{aligned}
> $$
> with $x$, $y$, $z$ in metres.
> (a) Say what each term is (point, line or sheet charge), where it is, and its strength with units.
> (b) Find the outward flux of $\mathbf{D}$ through the surface of the cube $\lvert x\rvert\le2$, $\lvert y\rvert\le2$, $\lvert z\rvert\le2$ m.
>
> *Source: original.*

> [!hint]- Hint
> Each $\delta$ has units of 1/m, so a term with three $\delta$'s needs a coefficient in C, two $\delta$'s C/m, one $\delta$ C/m². Then $Q_{\text{enc}} = \int_V\rho\,dV$ just asks how much of each object lies inside the cube.

> [!solution]- Solution
> **(a)** Read each term with the table of Lecture 3, using $[\delta] = 1/\text{m}$:
> - $4\times10^{-9}\,\delta(x-1)\,\delta(y+1)\,\delta(z)$: a **point** charge of 4 nC at $(1,-1,0)$.
> - $-2\times10^{-9}\,\delta(x+1)\,\delta(y)$: a **line** charge of $-2$ nC/m parallel to the $z$ axis, through $x = -1$, $y = 0$.
> - $0.5\times10^{-9}\,\delta(z-1)$: a **sheet** of $0.5$ nC/m² on the plane $z = 1$.
> - $2\times10^{-9}\,\delta(x)\,\delta(y-3)\,\delta(z)$: a **point** charge of 2 nC at $(0,3,0)$.
>
> **(b)** By Gauss's law the flux equals $Q_{\text{enc}} = \int_V\rho\,dV$. Integrating a $\delta$ over the cube gives 1 if its zero lies inside and 0 if not:
> - the 4 nC point is inside: $+4$ nC;
> - the line crosses the whole cube, a length of 4 m: $-2\times4 = -8$ nC;
> - the sheet cuts the cube in a 4 m × 4 m square of 16 m²: $0.5\times16 = +8$ nC;
> - the 2 nC point has $y = 3>2$, so it is outside: 0.
>
> So $\psi_E = 4-8+8+0 = 4$ nC.
>
> **Check (units):** $[\text{C}][1/\text{m}]^3$, $[\text{C/m}][1/\text{m}]^2$ and $[\text{C/m}^2][1/\text{m}]$ are all C/m³ ✓.
>
> **Answer.** (a) Point 4 nC at $(1,-1,0)$; line $-2$ nC/m along $z$ through $(x,y) = (-1,0)$; sheet 0.5 nC/m² on $z = 1$; point 2 nC at $(0,3,0)$. (b) The flux out of the cube is 4 nC.

### 3.5 Magnetic flux through a dome

> [!easy] Easy · multiple choice · magnetic flux
> A uniform magnetic field $\mathbf{B} = 0.3\,\hat{x}+0.4\,\hat{z}$ T fills space. $S$ is the open hemispherical dome of radius $a = 0.5$ m centred on the origin, $z\ge0$ (no base), with $d\mathbf{S}$ pointing away from the origin. What is $\int_S\mathbf{B}\cdot d\mathbf{S}$?
>
> (a) $0$, because $\oint\mathbf{B}\cdot d\mathbf{S} = 0$
>
> (b) $0.1\pi\approx0.314$ Wb
>
> (c) $0.2\pi\approx0.628$ Wb
>
> (d) $0.25\pi\approx0.785$ Wb
>
> (e) $0.125\pi\approx0.393$ Wb
>
> *Source: original.*

> [!hint]- Hint
> Close the dome with the flat disk $z = 0$, $r\le a$. What does $\oint\mathbf{B}\cdot d\mathbf{S} = 0$ say about that closed surface, and how hard is the flux through the flat disk?

> [!solution]- Solution
> **(b).** The dome plus the flat base disk ($z = 0$, $r\le0.5$ m, outward normal $-\hat{z}$) form a closed surface, and $\oint\mathbf{B}\cdot d\mathbf{S} = 0$ for every closed surface. The base is easy, because $\mathbf{B}$ is uniform and the base is flat with area $\pi a^2 = 0.25\pi$ m²:
> $$
> \psi_{\text{base}} = \mathbf{B}\cdot(-\hat{z})\,\pi a^2 = -0.4\times0.25\pi = -0.1\pi\ \text{Wb},
> \qquad
> \psi_{\text{dome}} = -\psi_{\text{base}} = 0.1\pi\approx0.314\ \text{Wb}.
> $$
> Every field line that enters through the base leaves through the dome. The $x$ component adds nothing: its lines enter the dome on the $x<0$ side and leave it on the $x>0$ side.
>
> (a) applies $\oint\mathbf{B}\cdot d\mathbf{S} = 0$ to an *open* surface; it holds only for closed ones.
>
> (c) is $B_z$ times the dome's area $2\pi a^2 = 0.5\pi$ m², as if $B_z$ were normal to the dome everywhere; it is normal to it only at the top.
>
> (d) is $\lvert\mathbf{B}\rvert = 0.5$ T times the dome's area, as if $\mathbf{B}$ were normal to the dome everywhere.
>
> (e) is $\lvert\mathbf{B}\rvert$ times the base area. It counts $B_x$, but $B_x$ is parallel to the base and sends no flux through it.
>
> **Answer.** (b) $\int_S\mathbf{B}\cdot d\mathbf{S} = 0.1\pi\approx0.314$ Wb.

## Medium

### 3.6 Sphere with a graded density

> [!medium] Medium · spherical symmetry · graded density
> A sphere of radius $a = 9$ cm in free space holds the volume charge density $\rho = \rho_0(1-r/a)$ for $r<a$ (zero outside), with $\rho_0 = 2$ μC/m³.
> (a) Find the total charge $Q$.
> (b) Find $\mathbf{E}$ for $r<a$ and for $r>a$.
> (c) Where inside the sphere is $\lvert\mathbf{E}\rvert$ largest? Find that maximum and compare it with $E$ at the surface.
> (d) A thin concentric spherical shell of radius $b = 18$ cm is added so that $\mathbf{E} = 0$ for $r>b$. What uniform surface charge density must it carry?
>
> *Source: classic.*

> [!hint]- Hint
> The density depends on $r$, so the enclosed charge is $Q_{\text{enc}}(r) = \int_0^r\rho(r')\,4\pi r'^2\,dr'$, not $\rho\times\tfrac43\pi r^3$. For (c), set $dE_r/dr = 0$.

> [!solution]- Solution
> **Setup.** $\rho$ depends only on $r$, so by symmetry $\mathbf{E} = E_r(r)\hat{r}$. On a concentric Gaussian sphere of radius $r$, $\mathbf{D}$ is normal and of constant magnitude, so $\epsilon_0E_r\cdot4\pi r^2 = Q_{\text{enc}}(r)$.
>
> **(a)** For $r\le a$,
> $$
> Q_{\text{enc}}(r) = \int_0^r\rho_0\Big(1-\frac{r'}{a}\Big)4\pi r'^2\,dr' = 4\pi\rho_0\Big(\frac{r^3}{3}-\frac{r^4}{4a}\Big),
> \qquad Q = Q_{\text{enc}}(a) = \frac{\pi\rho_0a^3}{3}\approx1.527\ \text{nC}.
> $$
> **(b)** Divide by $4\pi\epsilon_0r^2$:
> $$
> \mathbf{E} = \frac{\rho_0}{\epsilon_0}\Big(\frac{r}{3}-\frac{r^2}{4a}\Big)\hat{r}\quad(r<a),\qquad
> \mathbf{E} = \frac{Q}{4\pi\epsilon_0r^2}\hat{r} = \frac{\rho_0a^3}{12\epsilon_0r^2}\hat{r}\quad(r>a).
> $$
> **(c)** $\dfrac{dE_r}{dr} = \dfrac{\rho_0}{\epsilon_0}\Big(\dfrac13-\dfrac{r}{2a}\Big) = 0$ at $r = \tfrac23a = 6$ cm, where
> $$
> E_{\max} = \frac{\rho_0}{\epsilon_0}\Big(\frac{2a}{9}-\frac{a}{9}\Big) = \frac{\rho_0a}{9\epsilon_0}\approx2259\ \text{V/m},
> \qquad E(a) = \frac{\rho_0a}{12\epsilon_0}\approx1694\ \text{V/m} = 0.75\,E_{\max}.
> $$
> The field peaks *inside*: near the surface the density has dropped toward zero, so the enclosed charge grows too slowly to keep up with the $1/r^2$ spreading.
>
> **(d)** For $r>b$, Gauss's law gives $\mathbf{E} = 0$ only if $Q_{\text{enc}} = Q+4\pi b^2\rho_s = 0$. With $Q = \pi\rho_0a^3/3$ and $b = 2a$:
> $$
> \rho_s = -\frac{Q}{4\pi b^2} = -\frac{\rho_0a^3}{12b^2} = -\frac{\rho_0a}{48} = -3.75\ \text{nC/m}^2 .
> $$
> **Check:** both forms in (b) give $\rho_0a/(12\epsilon_0)$ at $r = a$ (continuous, as it must be with no surface charge there), and $E\to0$ at the centre, as symmetry demands. A direct Coulomb integration over the ball gives the same field at every radius tested.
>
> **Watch out:** writing $Q_{\text{enc}} = \rho\cdot\tfrac43\pi r^3$ treats a graded density as if it were uniform, and gives the wrong field everywhere.
>
> **Answer.** (a) $Q = \pi\rho_0a^3/3\approx1.527$ nC. (b) $\mathbf{E} = \dfrac{\rho_0}{\epsilon_0}\Big(\dfrac{r}{3}-\dfrac{r^2}{4a}\Big)\hat{r}$ inside, $\dfrac{\rho_0a^3}{12\epsilon_0r^2}\hat{r}$ outside. (c) Maximum $\rho_0a/(9\epsilon_0)\approx2259$ V/m at $r = 6$ cm; the surface value is 1694 V/m. (d) $\rho_s = -3.75$ nC/m².

### 3.7 Point-charge flux through a disk

> [!medium] Medium · flux · solid angle
> A point charge $Q = 12$ nC sits at $(0,0,h)$ with $h = 4$ cm, in free space. A flat disk of radius $a$ lies on the plane $z = 0$, centred on the origin; take $d\mathbf{S}$ along $-\hat{z}$ (away from the charge).
> (a) Show that the flux of $\mathbf{D}$ through the disk is $\psi = \dfrac{Q}{2}\Big(1-\dfrac{h}{\sqrt{h^2+a^2}}\Big)$.
> (b) Evaluate $\psi$ for $a = 3$ cm.
> (c) What radius $a$ catches exactly a quarter of the charge's flux?
> (d) What does $\psi$ tend to as $a\to\infty$? Explain the limit without the formula.
>
> *Source: classic.*

> [!hint]- Hint
> Integrate over rings: on the ring of radius $r$ only $D_z$ matters, and it is the same all around the ring. Or skip the integral: a spherical cap centred on $Q$ with the same rim as the disk catches exactly the same field lines.

> [!solution]- Solution
> **Setup.** Only $D_z$ crosses the disk. From the charge to the disk point at distance $r$ from the centre, the separation vector is $(x,y,-h)$ with length $\sqrt{r^2+h^2}$, so
> $$
> \mathbf{D}\cdot(-\hat{z}) = \frac{Q}{4\pi}\,\frac{h}{(r^2+h^2)^{3/2}} ,
> $$
> positive: the field crosses the disk along the chosen normal. It depends on $r$ only, so integrate over rings of area $2\pi r\,dr$.
>
> **(a)**
> $$
> \psi = \int_0^a\frac{Qh}{4\pi(r^2+h^2)^{3/2}}\,2\pi r\,dr = \frac{Qh}{2}\Big[-\frac{1}{\sqrt{r^2+h^2}}\Big]_0^a = \frac{Q}{2}\Big(1-\frac{h}{\sqrt{h^2+a^2}}\Big).
> $$
> **Second route (solid angle).** The disk and the spherical cap of radius $R = \sqrt{h^2+a^2}$ centred on $Q$ that shares the disk's rim together enclose no charge, so the same flux crosses both. On the cap $\mathbf{D}$ is normal with magnitude $Q/(4\pi R^2)$, and the cap's area is $2\pi R^2(1-\cos\alpha)$ with $\cos\alpha = h/R$, so $\psi = \tfrac{Q}{2}(1-\cos\alpha)$ ✓. The flux is $Q$ times the fraction of the full solid angle $4\pi$ that the disk subtends at the charge.
>
> **(b)** $\sqrt{h^2+a^2} = 5$ cm and $\cos\alpha = 0.8$: $\psi = 6\times0.2 = 1.2$ nC $= Q/10$.
>
> **(c)** $1-\dfrac{h}{\sqrt{h^2+a^2}} = \dfrac12 \;\Rightarrow\; \sqrt{h^2+a^2} = 2h \;\Rightarrow\; a = \sqrt3\,h\approx6.93$ cm. A disk whose radius is less than twice the charge's height already catches a quarter of all its flux.
>
> **(d)** $\psi\to Q/2 = 6$ nC. An infinite plane splits space into two halves; by symmetry half of the field lines head down and cross it, and the other half head up and never do (the half-space argument of Lecture 3).
>
> **Check:** $a\to0$ gives $\psi\to0$ ✓, and $\psi$ never exceeds $Q/2$ ✓. A direct numerical integration of $\mathbf{D}\cdot d\mathbf{S}$ over the disk agrees.
>
> **Answer.** (a) as stated; (b) $\psi = 1.2$ nC $= Q/10$; (c) $a = \sqrt3\,h\approx6.93$ cm; (d) $\psi\to Q/2 = 6$ nC.

### 3.8 Find the error, an odd slab

> [!medium] Medium · find the error · planar symmetry
> The slab $-a<x<a$ in free space carries $\rho = \rho_0x/a$ with $\rho_0>0$; there is no charge outside. A student finds the field inside like this:
>
> *"By symmetry $\mathbf{E} = E(x)\hat{x}$. Take a pillbox with caps of area $A$ at $-x$ and $+x$. The enclosed charge is $A\int_{-x}^{x}\rho_0x'/a\,dx' = 0$, so $2E(x)A = 0$ and $\mathbf{E} = 0$ everywhere inside the slab."*
>
> (a) Which step is wrong, and why?
> (b) Find the correct $\mathbf{E}$ inside and outside the slab, with its direction.
> (c) Evaluate $\lvert\mathbf{E}\rvert$ at $x = 0$ for $\rho_0 = 1$ μC/m³ and $a = 1$ m.
>
> *Source: original.*

> [!hint]- Hint
> The step "$2E(x)A$" assumes that the field on the left cap is the mirror image of the field on the right cap, $E_x(-x) = -E_x(x)$. Reflect this slab in the plane $x = 0$: what happens to its charge, and therefore to its field?

> [!solution]- Solution
> **(a) The slip is "$2E(x)A$".** Adding the two cap fluxes as $2EA$ assumes $E_x$ is odd, $E_x(-x) = -E_x(x)$. That is true for a mirror-symmetric (even) charge distribution such as a uniform slab. Here $\rho$ is odd: reflecting the slab in the plane $x = 0$ gives the same slab with the opposite charge. The reflected field at $-x$ is the mirror image of the original field at $x$, so its $x$ component is $-E_x(x)$; but it is also the field of the negated slab, $-E_x(-x)$. Equating the two gives $E_x(-x) = +E_x(x)$: $E_x$ is **even**. The right cap (normal $+\hat{x}$) then carries $E_x(x)A$ and the left cap (normal $-\hat{x}$) carries $-E_x(-x)A = -E_x(x)A$: they cancel *whatever* $E$ is. The student's Gauss's law reads $0 = 0$, which is true but says nothing about $E$; "$\mathbf{E} = 0$" does not follow.
>
> **(b) A pillbox that works.** First the outside. Treat the slab as a stack of thin sheets, each of which gives $\pm\rho\,dx'/(2\epsilon_0)$. For $x>a$ every sheet is on the left, so $E_x = \frac{1}{2\epsilon_0}\int_{-a}^{a}\rho\,dx' = 0$ because the slab is neutral; likewise for $x<-a$. Now put one cap at $x$ inside the slab and the other at some $x_2>a$, where $E = 0$. The left cap (normal $-\hat{x}$) carries $-E_x(x)A$, the right cap nothing, and the enclosed charge is the part of the slab between $x$ and $a$:
> $$
> \begin{aligned}
> -E_x(x)\,A &= \frac{A}{\epsilon_0}\int_x^a\rho_0\frac{x'}{a}\,dx' = \frac{A\rho_0(a^2-x^2)}{2\epsilon_0a}\\
> \Rightarrow\quad \mathbf{E} &= -\frac{\rho_0(a^2-x^2)}{2\epsilon_0a}\,\hat{x}\qquad(\lvert x\rvert<a),
> \end{aligned}
> $$
> and $\mathbf{E} = 0$ for $\lvert x\rvert>a$. It points along $-\hat{x}$, from the positive half ($x>0$) toward the negative half, as it should.
>
> **(c)** The largest value is at the centre: $\lvert\mathbf{E}(0)\rvert = \dfrac{\rho_0a}{2\epsilon_0}\approx5.65\times10^4$ V/m. That is $1/\epsilon_0$ times the charge per unit area of the positive half, $\rho_0a/2$.
>
> **Check:** the result is even in $x$ ✓ (as the reflection argument requires); it vanishes at $x = \pm a$, so it is continuous with the zero field outside ✓ (no surface charge); and a thin pillbox between $x$ and $x+\Delta x$ gives $[E_x(x+\Delta x)-E_x(x)]A = \rho A\Delta x/\epsilon_0$, i.e. a slope $\rho_0x/(\epsilon_0a)$, which the result has ✓. Summing the field of the sheets directly gives the same curve.
>
> **Answer.** (a) The "$2E(x)A$" step: here $E_x$ is even, so the two cap fluxes cancel and the symmetric pillbox gives no information. (b) $\mathbf{E} = -\dfrac{\rho_0(a^2-x^2)}{2\epsilon_0a}\,\hat{x}$ for $\lvert x\rvert<a$, zero outside. (c) $\lvert\mathbf{E}(0)\rvert = \rho_0a/(2\epsilon_0)\approx5.65\times10^4$ V/m, pointing along $-\hat{x}$.

## Hard

### 3.9 Two slabs and a sheet

> [!hard] Hard · superposition · slabs · charge sheets
> Free space contains two charged slabs: $\rho_1 = 3\epsilon_0$ C/m³ for $-3<z<-1$ m and $\rho_2 = -2\epsilon_0$ C/m³ for $0<z<3$ m, with no charge elsewhere. (The densities are given as multiples of $\epsilon_0$, so the fields come out in V/m.)
> (a) Find the charge per unit area of each slab. Is the pair neutral?
> (b) Find $\mathbf{E}$ in all five regions.
> (c) A sheet $\rho_s = 4\epsilon_0$ C/m² is now added on the plane $z = -1$ m. Find the new $\mathbf{E}$ everywhere.
> (d) In case (c), where is $\mathbf{E} = 0$? Show that there is only one such plane, and check the jump of $E_z$ across the sheet.
>
> *Source: Summer 2019 HE1 #1a style (two charged slabs, then a sheet added), re-parameterized; built on the pn-junction example of Lecture 3.*

> [!hint]- Hint
> Do not draw one pillbox around the whole stack. Each slab is a building block centred on its own midplane: linear inside, $\pm\rho W/(2\epsilon_0)$ outside. Write each block's field region by region and add; the sheet adds $\pm\rho_s/(2\epsilon_0)$.

> [!solution]- Solution
> **Setup.** Everything depends on $z$ only, so $\mathbf{E} = E_z(z)\hat{z}$, and each piece's field is already known from Lecture 3. A slab of density $\rho$, width $W$ and midplane $z_c$ gives
> $$
> E_z = \frac{\rho}{\epsilon_0}(z-z_c)\ \text{inside},\qquad E_z = \pm\frac{\rho W}{2\epsilon_0}\ \text{outside}\ (+\text{ above},\ -\text{ below}).
> $$
> **(a)** Slab 1: $\rho_1W_1 = 3\epsilon_0\times2 = 6\epsilon_0$ C/m². Slab 2: $\rho_2W_2 = -2\epsilon_0\times3 = -6\epsilon_0$ C/m². The pair is neutral, like a pn junction (here with a 1 m gap).
>
> **(b)** Slab 1 ($z_c = -2$, $W = 2$): $3(z+2)$ inside, $\pm3$ outside. Slab 2 ($z_c = 1.5$, $W = 3$): $-2(z-1.5) = 3-2z$ inside; it is negative, so outside it gives $+3$ below and $-3$ above (toward it). Adding region by region:
> $$
> E_z(z) =
> \begin{cases}
> -3+3 = 0, & z<-3\\
> 3(z+2)+3 = 3z+9, & -3<z<-1\\
> 3+3 = 6, & -1<z<0\\
> 3+(3-2z) = 6-2z, & 0<z<3\\
> 3-3 = 0, & z>3
> \end{cases}
> \qquad[\text{V/m}],\ z\text{ in m}.
> $$
> **(c)** The sheet adds $\rho_s/(2\epsilon_0) = 2$ V/m pointing away from it: $-2$ below $z = -1$ and $+2$ above:
> $$
> E_z(z) =
> \begin{cases}
> -2, & z<-3\\
> 3z+7, & -3<z<-1\\
> 8, & -1<z<0\\
> 8-2z, & 0<z<3\\
> +2, & z>3
> \end{cases}
> \qquad[\text{V/m}].
> $$
> **(d)** The constant regions ($-2$, $8$, $+2$) never vanish, and $8-2z = 0$ only at $z = 4$, outside $0<z<3$. The only zero is inside slab 1: $3z+7 = 0\Rightarrow z = -7/3\approx-2.33$ m, so $\mathbf{E} = 0$ on the plane $z = -7/3$ m. Across the sheet, $E_z$ jumps from $3(-1)+7 = 4$ V/m just below to $8$ V/m just above: a jump of $4$ V/m $= \rho_s/\epsilon_0$ ✓.
>
> **Check:** $E_z$ is continuous at the slab faces $z = -3$, $0$, $3$, where there is no surface charge: in (c) both sides give $-2$, $8$ and $2$ ✓. Far away, the whole stack acts like one sheet carrying its net charge $4\epsilon_0$ C/m², which gives $\pm2$ V/m ✓. Inside each slab the slope is $\rho/\epsilon_0$, i.e. $+3$ and $-2$ V/m² ✓.
>
> **Watch out:** a pillbox symmetric about some plane does not work here, because the charge is not mirror-symmetric about any plane. Superposing the known building blocks is the method.
>
> **Answer.** (a) $+6\epsilon_0$ and $-6\epsilon_0$ C/m²: neutral. (b) $E_z = 0$, $3z+9$, $6$, $6-2z$, $0$ V/m in the five regions (bottom to top). (c) $E_z = -2$, $3z+7$, $8$, $8-2z$, $+2$ V/m. (d) $\mathbf{E} = 0$ only on the plane $z = -7/3$ m; the jump across the sheet is 4 V/m $= \rho_s/\epsilon_0$.

### 3.10 Sphere with an off-centre cavity

> [!hard] Hard · superposition · spherical symmetry
> A ball of radius $a = 1$ m centred on the origin carries a uniform charge density $\rho = 30\epsilon_0$ C/m³, except inside an empty spherical cavity of radius $b = 0.4$ m centred at $\mathbf{d} = 0.5\,\hat{x}$ m. The surroundings are free space.
> (a) Use Gauss's law to show that inside a *full* uniform ball, $\mathbf{E} = \dfrac{\rho}{3\epsilon_0}\mathbf{r}$, where $\mathbf{r}$ is the position vector from the ball's centre.
> (b) Show that the field inside the cavity is uniform, and find it.
> (c) Find $\mathbf{E}$ at $P = (0.5, 0.5, 0)$ m.
> (d) Find $\mathbf{E}$ at $S = (2.5, 0, 0)$ m, and compare with the field there if the cavity were filled.
>
> *Source: classic.*

> [!hint]- Hint
> The holed ball is a full ball of density $+\rho$ plus a small ball of density $-\rho$ filling the cavity. Use (a) for each, with each position vector measured from *its own* centre. Outside a ball, its field is that of a point charge at its centre.

> [!solution]- Solution
> **Setup.** The cavity destroys the spherical symmetry, so Gauss's law cannot be applied to the object as a whole. But each piece of the superposition "full ball of $+\rho$ plus cavity ball of $-\rho$" is spherically symmetric about its own centre. Note that $\rho/(3\epsilon_0) = 10$ V/m².
>
> **(a)** For $r<a$, a concentric Gaussian sphere encloses $\rho\cdot\tfrac43\pi r^3$, so $\epsilon_0E_r\cdot4\pi r^2 = \rho\cdot\tfrac43\pi r^3$ and $E_r = \rho r/(3\epsilon_0)$; with $\mathbf{r} = r\hat{r}$ this is $\mathbf{E} = \dfrac{\rho}{3\epsilon_0}\mathbf{r}$. Outside, $\mathbf{E} = \dfrac{\rho a^3}{3\epsilon_0}\dfrac{\mathbf{r}}{r^3}$: the whole charge $\rho\cdot\tfrac43\pi a^3$ acts as a point charge at the centre.
>
> **(b)** At a point $\mathbf{r}$ inside the cavity, both balls contribute their interior fields:
> $$
> \mathbf{E} = \frac{\rho}{3\epsilon_0}\mathbf{r} - \frac{\rho}{3\epsilon_0}(\mathbf{r}-\mathbf{d}) = \frac{\rho}{3\epsilon_0}\mathbf{d} = 10\times0.5\,\hat{x} = 5\,\hat{x}\ \text{V/m}.
> $$
> The $\mathbf{r}$'s cancel: the field is the same at every point of the cavity, directed along the line from the ball's centre to the cavity's centre.
>
> **(c)** $\lvert\mathbf{r}_P\rvert\approx0.707$ m $<a$, so $P$ is inside the big ball; $\lvert\mathbf{r}_P-\mathbf{d}\rvert = 0.5$ m $>b$, so $P$ is in the material, *outside* the cavity ball. Then
> $$
> \begin{aligned}
> \mathbf{E}(P) &= \frac{\rho}{3\epsilon_0}\Big[\mathbf{r}_P - b^3\frac{\mathbf{r}_P-\mathbf{d}}{\lvert\mathbf{r}_P-\mathbf{d}\rvert^3}\Big] = 10\Big[(0.5,0.5,0) - 0.064\,\frac{(0,0.5,0)}{0.125}\Big]\\
> &= (5,5,0)-(0,2.56,0) = 5\,\hat{x}+2.44\,\hat{y}\ \text{V/m},\qquad \lvert\mathbf{E}\rvert\approx5.56\ \text{V/m}.
> \end{aligned}
> $$
> **(d)** $S$ is outside both balls (2.5 m from the origin, 2 m from the cavity's centre), so both act as point charges:
> $$
> \mathbf{E}(S) = \frac{\rho}{3\epsilon_0}\Big[\frac{a^3}{2.5^2} - \frac{b^3}{2^2}\Big]\hat{x} = (1.6-0.16)\,\hat{x} = 1.44\,\hat{x}\ \text{V/m},
> $$
> compared with $1.6\,\hat{x}$ V/m if the cavity were filled.
>
> **Check:** at the cavity-wall point $(0.5,0.4,0)$ the material formula of (c) gives $10(0.5,0.4,0)-10(0,0.4,0) = (5,4,0)-(0,4,0) = 5\,\hat{x}$ V/m, equal to the cavity field: $\mathbf{E}$ is continuous across the wall, as it must be with no surface charge there ✓. A direct Coulomb integration over the holed ball, with no superposition, reproduces (b), (c) and (d).
>
> **Watch out:** in (c) the big-ball term uses the *inside* formula but the cavity term the *outside* one, because $P$ is outside the small ball. Decide for each ball separately.
>
> **Answer.** (b) $\mathbf{E} = \rho\mathbf{d}/(3\epsilon_0) = 5\,\hat{x}$ V/m, uniform throughout the cavity. (c) $\mathbf{E}(P) = 5\,\hat{x}+2.44\,\hat{y}$ V/m ($\approx5.56$ V/m). (d) $\mathbf{E}(S) = 1.44\,\hat{x}$ V/m, against $1.6\,\hat{x}$ V/m without the cavity.

### 3.11 Coaxial cable with a graded core

> [!hard] Hard · cylindrical symmetry · graded density
> An infinitely long coaxial structure lies along the $z$ axis in free space. The core $r<a$ carries $\rho = \rho_0r/a$ with $\rho_0 = 3$ μC/m³ and $a = 1$ cm; the gap $a<r<b$, with $b = 2$ cm, is empty; the outer shell $b<r<c$, with $c = 3$ cm, carries a uniform density $-\rho_1$; there is no charge for $r>c$.
> (a) Find $\rho_1$ so that the structure is neutral (zero net charge per unit length).
> (b) Find $\mathbf{E}$ in all four regions.
> (c) Evaluate $E$ at $r = a$, at $r = b$ and at $r = 2.5$ cm. Where is $\lvert\mathbf{E}\rvert$ largest?
> (d) If the outer charge were instead squeezed into a thin sheet on $r = b$, what $\rho_s$ would it need, and what would change in (b)?
>
> *Source: original.*

> [!hint]- Hint
> Use a coaxial Gaussian cylinder of radius $r$ and length $L$; its caps carry no flux. The charge per unit length inside it is $\int_0^r\rho(r')\,2\pi r'\,dr'$; in the shell, that is the core's total minus the part of the shell inside radius $r$.

> [!solution]- Solution
> **Setup.** Cylindrical symmetry gives $\mathbf{E} = E_r(r)\hat{r}$. On a coaxial cylinder of radius $r$ and length $L$ the caps carry no flux and the side carries $\epsilon_0E_r\cdot2\pi rL$, so $E_r = \dfrac{\rho_{l,\text{enc}}(r)}{2\pi\epsilon_0r}$, where $\rho_{l,\text{enc}}$ is the enclosed charge per unit length.
>
> **(a)** The core holds $\displaystyle\int_0^a\rho_0\frac{r'}{a}\,2\pi r'\,dr' = \frac{2\pi\rho_0a^2}{3}\approx0.628$ nC/m; the shell holds $-\rho_1\pi(c^2-b^2)$. Neutrality requires
> $$
> \rho_1 = \frac{2\rho_0a^2}{3(c^2-b^2)} = \frac{2(3\times10^{-6})(10^{-4})}{3(5\times10^{-4})} = 0.4\ \mu\text{C/m}^3 .
> $$
> **(b)** The enclosed charge per unit length is $2\pi\rho_0r^3/(3a)$ in the core and the full $2\pi\rho_0a^2/3$ in the gap; in the shell, using (a),
> $$
> \rho_{l,\text{enc}} = \frac{2\pi\rho_0a^2}{3}-\rho_1\pi(r^2-b^2) = \frac{2\pi\rho_0a^2}{3}\cdot\frac{c^2-r^2}{c^2-b^2},
> $$
> and zero outside. Dividing by $2\pi\epsilon_0r$:
> $$
> E_r(r) =
> \begin{cases}
> \dfrac{\rho_0r^2}{3\epsilon_0a}, & r<a\\[10pt]
> \dfrac{\rho_0a^2}{3\epsilon_0r}, & a<r<b\\[10pt]
> \dfrac{\rho_0a^2}{3\epsilon_0r}\cdot\dfrac{c^2-r^2}{c^2-b^2}, & b<r<c\\[10pt]
> 0, & r>c
> \end{cases}
> $$
> **(c)** $E(a) = \dfrac{\rho_0a}{3\epsilon_0}\approx1129$ V/m and $E(b) = \dfrac{\rho_0a^2}{3\epsilon_0b}\approx565$ V/m. At $r = 2.5$ cm the gap formula would give $451.8$ V/m; the shell factor $(c^2-r^2)/(c^2-b^2) = 0.55$ cuts it to $E\approx248.5$ V/m. The field grows as $r^2$ through the core and only falls after it, so $\lvert\mathbf{E}\rvert$ is largest at $r = a$, about 1129 V/m.
>
> **(d)** The same charge per unit length spread over a cylinder of radius $b$: $\rho_s = -\dfrac{2\pi\rho_0a^2/3}{2\pi b} = -\dfrac{\rho_0a^2}{3b} = -5$ nC/m². Nothing changes for $r<b$ (a Gaussian cylinder there does not reach the outer charge), and $\mathbf{E} = 0$ for every $r>b$: the field drops abruptly to zero at $r = b$ instead of tapering off across the shell.
>
> **Check:** the pieces match at $r = a$ ($\rho_0a/(3\epsilon_0)$ from both sides), at $r = b$ (shell factor 1) and at $r = c$ (shell factor 0), as they must with no surface charge; and $\mathbf{E} = 0$ outside a neutral cylinder ✓. A direct two-dimensional Coulomb integration agrees at every radius tested.
>
> **Answer.** (a) $\rho_1 = 2\rho_0a^2/[3(c^2-b^2)] = 0.4$ μC/m³. (b) $E_r = \rho_0r^2/(3\epsilon_0a)$, $\rho_0a^2/(3\epsilon_0r)$, $\dfrac{\rho_0a^2}{3\epsilon_0r}\cdot\dfrac{c^2-r^2}{c^2-b^2}$ and $0$ in the four regions, all along $\hat{r}$. (c) 1129 V/m, 565 V/m and 248.5 V/m; the maximum is at $r = a$. (d) $\rho_s = -5$ nC/m²; $\mathbf{E}$ is unchanged for $r<b$ and zero for $r>b$.

### 3.12 Flux bookkeeping, line and sheet

> [!hard] Hard · flux · superposition · closed surfaces
> In free space, a line charge $\rho_l = 6$ nC/m lies on the $z$ axis and a sheet charge $\rho_s = 4$ nC/m² lies on the plane $z = 0$.
> (a) Write $\mathbf{D}$ at every point off the line and the sheet.
> (b) For the closed cylinder $r\le1$ m, $-1\le z\le2$ m, find the outward flux of $\mathbf{D}$ through the top cap, the bottom cap and the curved side, and check the total against Gauss's law.
> (c) For the closed cube $\lvert x\rvert\le1$, $\lvert y\rvert\le1$, $1\le z\le3$ m, find the outward flux through each of its six faces, and the total.
> (d) Find the flux of $\mathbf{D}$ through the open hemispherical dome of radius 1 m centred on $(0,0,1)$, $z\ge1$, with $d\mathbf{S}$ pointing away from the dome's centre.
>
> *Source: original.*

> [!hint]- Hint
> Keep the two sources' fluxes separate. The line's $\mathbf{D}$ is horizontal (radial from the $z$ axis); the sheet's is vertical and uniform on each side. On every flat face only one of them can contribute. For (d), close the dome with a flat disk.

> [!solution]- Solution
> **(a)** Superpose the two building blocks, with $r$ the distance from the $z$ axis:
> $$
> \mathbf{D} = \frac{\rho_l}{2\pi r}\hat{r} + \frac{\rho_s}{2}\operatorname{sgn}(z)\,\hat{z} = \frac{6}{2\pi r}\hat{r} + 2\operatorname{sgn}(z)\,\hat{z}\ \ \text{nC/m}^2\quad(r\text{ in m}).
> $$
> **(b)** Top cap ($z = 2$, normal $+\hat{z}$): only the sheet term is normal to it, giving $2\times\pi(1)^2 = 2\pi\approx6.28$ nC. Bottom cap ($z = -1$, normal $-\hat{z}$): there $D_z = -2$, so $(-2)(-1)\pi = 2\pi\approx6.28$ nC. Curved side ($r = 1$, normal $\hat{r}$, height 3 m): only the line term, $\dfrac{6}{2\pi}\times2\pi(1)(3) = 18$ nC. Total:
> $$
> \oint\mathbf{D}\cdot d\mathbf{S} = 2\pi+2\pi+18 = 18+4\pi\approx30.57\ \text{nC} = \underbrace{\rho_l\,(3\ \text{m})}_{18\ \text{nC}}+\underbrace{\rho_s\,\pi(1\ \text{m})^2}_{4\pi\ \text{nC}},
> $$
> exactly the enclosed charge ✓.
>
> **(c)** The cube lies entirely above the sheet and contains the line from $z = 1$ to $z = 3$. Top ($z = 3$): $+2\times(2\ \text{m})^2 = +8$ nC. Bottom ($z = 1$): $\mathbf{D}$ points up, *into* the cube: $-8$ nC. The line's flux leaves horizontally through the four side faces only, equally by the square's symmetry: $\rho_l(2\ \text{m})/4 = 3$ nC each. Total $8-8+4\times3 = 12$ nC $= \rho_l\times2$ m ✓. The sheet's field lines pass straight through the cube (in at the bottom, out at the top) and add nothing to the total: the sheet is outside.
>
> **(d)** Close the dome with the flat disk $z = 1$, $r\le1$ (outward normal $-\hat{z}$). This closed surface encloses the line from $z = 1$ to $z = 2$, so $Q_{\text{enc}} = 6$ nC. Through the disk, the line's horizontal field sends nothing and the sheet's field sends $2\times\pi\times(-1) = -2\pi$ nC. So
> $$
> \psi_{\text{dome}} = Q_{\text{enc}} - \psi_{\text{disk}} = 6-(-2\pi) = 6+2\pi\approx12.28\ \text{nC}.
> $$
> Split by source: 6 nC from the line (all the flux of that 1 m piece leaves through the dome) and $2\pi$ nC from the sheet (the dome's shadow on the plane $z = 1$ is the unit disk).
>
> **Check:** on the dome, the line's $\mathbf{D}\cdot\hat{n}$ is the constant $\frac{6}{2\pi}$ nC/m² (near the axis the $1/r$ growth is exactly offset by the field becoming tangent to the dome), and the dome's area is $2\pi$ m², which gives 6 nC ✓. A direct numerical surface integral over the dome gives the same $6+2\pi$ nC, and the face-by-face integrals in (b) and (c) match too.
>
> **Watch out:** it is easy to forget that the sheet sends flux through *both* caps in (b), or to count the sheet as enclosed in (c).
>
> **Answer.** (a) $\mathbf{D} = \dfrac{6}{2\pi r}\hat{r}+2\operatorname{sgn}(z)\,\hat{z}$ nC/m². (b) Top $2\pi$, bottom $2\pi$, side 18 nC; total $18+4\pi\approx30.57$ nC $= Q_{\text{enc}}$. (c) Top $+8$, bottom $-8$, each side $+3$ nC; total 12 nC. (d) $6+2\pi\approx12.28$ nC.

### Sources for this page
Problems 3.1–3.5, 3.8, 3.11 and 3.12 are original; 3.12 extends the lecture's "top + bottom + side" bookkeeping to two sources at once. Old exam: Summer 2019 HE1 #1a (two charged slabs, then a sheet added) is the model for 3.9, re-parameterized and built on the pn-junction superposition example in the Lecture 3 notes. Classic textbook exercises, reworded with new numbers: the sphere with a graded density (3.6), the flux of a point charge through a disk by solid angle (3.7), and the uniform ball with an off-centre cavity (3.10). No exam or homework problem was copied. Every number was checked numerically by direct Coulomb integration, numerical surface integrals or sheet-by-sheet superposition.

*Previous: [[practice/02-coulombs-law-superposition-and-gauss|Lecture 2 practice]] · next: [[practice/04-divergence-and-curl|Lecture 4 practice]] · [[practice/index|all practice]]*
