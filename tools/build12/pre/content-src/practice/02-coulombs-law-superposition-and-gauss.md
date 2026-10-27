---
title: "Practice — Lecture 2: Coulomb's law, superposition and Gauss's law"
description: "12 practice problems (5 easy, 3 medium, 4 hard) on vector Coulomb forces, null points, flux through cubes and spheres, the 5-step integrals (ring, semicircle, dipole, finite line, disk), velocity and mass selectors, and the step from Coulomb to Gauss, each with a folded hint and a worked solution."
tags: [practice, electrostatics, exam-1]
lecture: 2
---

*Practice for [[1-electrostatics/02-coulombs-law-superposition-and-gauss|Lecture 2]] · concepts: [[concepts/coulombs-law]] · [[concepts/superposition]] · [[concepts/five-step-recipe]] · [[concepts/gauss-law]] · all practice: [[practice/index|hub]] · by difficulty: [[practice/easy|easy]] · [[practice/medium|medium]] · [[practice/hard|hard]] · [[practice/topics|by topic]]*

Work each problem on paper first. Open the **hint** only when stuck, and the **solution** only after you have an answer you would hand in. Every answer here has been checked numerically.

## Easy

### 2.1 Coulomb force as a vector

> [!easy] Easy · Coulomb's law · vectors
> Two point charges sit in free space: $Q_1 = 2\ \mu\text{C}$ at $(1,0,2)$ m and $Q_2 = -3\ \mu\text{C}$ at $(3,2,1)$ m. (a) Find the force $\mathbf{F}_2$ on $Q_2$ as a vector, and its magnitude. (b) Find the force $\mathbf{F}_1$ on $Q_1$. (c) Is the force attractive or repulsive, and how does your formula show it?
>
> *Source: original.*

> [!hint]- Hint
> Build $\mathbf{R} = \mathbf{r}_2-\mathbf{r}_1$ from the source $Q_1$ to the charge that feels the force, and let the sign of $Q_1Q_2$ set the direction. Do not add a minus sign by hand.

> [!solution]- Solution
> **(a)** In Coulomb's law $\hat{R}$ points from the source $Q_1$ to $Q_2$:
> $$
> \mathbf{R} = \mathbf{r}_2-\mathbf{r}_1 = (2,\,2,\,-1)\ \text{m},\qquad R = \sqrt{4+4+1} = 3\ \text{m},\qquad \hat{R} = \tfrac13(2,\,2,\,-1).
> $$
> With $1/(4\pi\epsilon_0) = 8.988\times10^9$ m/F and $R^2 = 9$ m²,
> $$
> \mathbf{F}_2 = \frac{Q_1Q_2}{4\pi\epsilon_0R^2}\,\hat{R} = \frac{(2\times10^{-6})(-3\times10^{-6})}{4\pi\epsilon_0\,(9)}\,\hat{R} = (-5.99\ \text{mN})\,\tfrac13(2,\,2,\,-1),
> $$
> so $\mathbf{F}_2 = -3.99\,\hat{x}-3.99\,\hat{y}+2.00\,\hat{z}$ mN and $\lvert\mathbf{F}_2\rvert = 5.99$ mN. A quick estimate agrees: $\lvert Q_1Q_2\rvert = 6\times10^{-12}$ C², times $9\times10^9$, over 9 m², gives 6 mN.
>
> **(b)** Newton's third law: $\mathbf{F}_1 = -\mathbf{F}_2 = +3.99\,\hat{x}+3.99\,\hat{y}-2.00\,\hat{z}$ mN.
>
> **(c)** The scalar factor $Q_1Q_2/(4\pi\epsilon_0R^2) = -5.99$ mN is negative, so $\mathbf{F}_2$ points along $-\hat{R}$, from $Q_2$ back toward $Q_1$: attractive, as it must be for opposite charges. Check: $\mathbf{F}_2\cdot\hat{R} = -5.99$ mN $= -\lvert\mathbf{F}_2\rvert$, so the force lies exactly along the line joining the charges.
>
> **Watch out:** if you compute a magnitude and then choose the direction separately, the sign of $Q_1Q_2$ gets used twice or not at all. Keep the sign inside the scalar factor and let $\hat{R}$ (source to target) carry the geometry.
>
> **Answer.** $\mathbf{F}_2 = -3.99\hat{x}-3.99\hat{y}+2.00\hat{z}$ mN, $\lvert\mathbf{F}_2\rvert = 5.99$ mN; $\mathbf{F}_1 = +3.99\hat{x}+3.99\hat{y}-2.00\hat{z}$ mN; attractive.

### 2.2 Where the field vanishes

> [!easy] Easy · multiple choice · null point
> A point charge $+q$ ($q>0$) sits at the origin and a point charge $-4q$ at $x = 3$ m on the $x$ axis, in free space. At which point is $\mathbf{E} = 0$?
>
> (a) $x = 1$ m
>
> (b) $x = 2$ m
>
> (c) $x = -3$ m
>
> (d) $x = 6$ m
>
> (e) Nowhere at a finite distance
>
> *Source: classic.*

> [!hint]- Hint
> Before solving any equation, ask in which of the regions $x<0$, $0<x<3$ m and $x>3$ m the two fields point in *opposite* directions, and in which of those the weaker charge is the closer one.

> [!solution]- Solution
> **Setup.** Off the $x$ axis the two contributions point along different lines and cannot cancel, so look on the axis. Measure $E_x$ in units of $q/(4\pi\epsilon_0)$ per square metre.
>
> **Which region?** Between the charges both fields point along $+\hat{x}$ (away from $+q$, toward $-4q$): they add. For $x>3$ m they are opposed, but $-4q$ is both larger and closer, so it always wins. Only for $x<0$, beyond the *smaller* charge, can a weak but close $+q$ balance a strong but distant $-4q$:
> $$
> \frac{1}{x^2} = \frac{4}{(3-x)^2}\ \Rightarrow\ (3-x)^2 = 4x^2\ \Rightarrow\ x = -3\ \text{m}\ \text{ or }\ x = 1\ \text{m}.
> $$
> Only $x = -3$ m lies in the allowed region. There $+q$, 3 m away, gives $E_x = -\tfrac19$ and $-4q$, 6 m away, gives $+\tfrac{4}{36} = +\tfrac19$: they cancel. A numerical scan of the whole axis finds no other zero.
>
> **The distractors.** (a) $x = 1$ m is the other root of the squared equation. There the *magnitudes* are equal, but both fields point along $+\hat{x}$, so $E_x = +2$: squaring threw the directions away. (b) $x = 2$ m is also between the charges: $E_x = +4.25$. (d) At $x = 6$ m, beyond the larger charge, $E_x = -\tfrac{5}{12}\approx-0.417$: the $-4q$ term dominates. (e) fails because (c) works. With unequal opposite charges a null point always exists, outside the pair on the side of the smaller charge.
>
> **Answer.** (c) $x = -3$ m.

### 2.3 Charge at a cube corner

> [!easy] Easy · Gauss's law · flux · symmetry
> A point charge $Q = 12$ nC sits at the origin, which is a corner of the cube $0\le x,y,z\le2$ m (free space). (a) What is the outward flux of $\mathbf{D}$ through each of the three faces that touch the charge ($x = 0$, $y = 0$, $z = 0$)? (b) Through each of the three far faces ($x = 2$, $y = 2$ and $z = 2$ m)? (c) Through the whole cube? (d) For comparison: if the charge sat at the centre $(1,1,1)$ m, what would the flux through each face be?
>
> *Source: classic.*

> [!hint]- Hint
> Put eight copies of the cube together so that the charge sits at the centre of one big cube.

> [!solution]- Solution
> **(a)** The charge lies *in the plane* of the face $x = 0$, so $\mathbf{D}$, which points radially away from the origin, is tangent to that face everywhere: $\mathbf{D}\cdot d\mathbf{S} = 0$ and the flux is 0. The same holds for $y = 0$ and $z = 0$.
>
> **(b)–(c)** Eight cubes like this one, one per octant, fill a 4 m cube centred on $Q$. By Gauss's law the big cube passes flux $Q$, and by symmetry the eight small cubes share it equally: $Q/8 = 1.5$ nC each. In our cube all of it leaves through the three far faces, which are equivalent under $x\to y\to z$: $Q/24 = 0.5$ nC each.
>
> **(d)** At the centre all six faces are equivalent: $Q/6 = 2$ nC each.
>
> **Check:** integrating $\mathbf{D}\cdot d\mathbf{S}$ numerically over each face gives 0, 0, 0 and 0.5, 0.5, 0.5 nC for the corner charge and 2 nC per face for the centred one.
>
> **Watch out:** "the charge is on the surface, so half of it is enclosed" is wrong for a corner. A corner sees only one eighth of the surrounding space (an edge would see a quarter, a flat face one half).
>
> **Answer.** (a) 0 through each face touching the charge; (b) $Q/24 = 0.5$ nC through each far face; (c) $Q/8 = 1.5$ nC; (d) $Q/6 = 2$ nC per face.

### 2.4 A velocity selector

> [!easy] Easy · Lorentz force · velocity selector
> Charged particles move with velocity $\mathbf{v} = 2\times10^5\,\hat{x}$ m/s through a region of uniform magnetic field $\mathbf{B} = 0.25\,\hat{y}$ T. (a) What uniform $\mathbf{E}$ (a vector) lets them pass undeflected? (b) Would electrons with the same velocity also pass undeflected? (c) A proton ($e = 1.602\times10^{-19}$ C) enters the selector of (a) with $\mathbf{v} = 4\times10^5\,\hat{x}$ m/s. Find the electric, the magnetic and the net force on it, and say which way it is deflected.
>
> *Source: classic.*

> [!hint]- Hint
> Zero force means $\mathbf{E}+\mathbf{v}\times\mathbf{B} = 0$. Work out $\hat{x}\times\hat{y}$ first.

> [!solution]- Solution
> **(a)** The force $q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$ vanishes when $\mathbf{E} = -\mathbf{v}\times\mathbf{B}$. With $\hat{x}\times\hat{y} = \hat{z}$:
> $$
> \mathbf{v}\times\mathbf{B} = (2\times10^5)(0.25)\,\hat{x}\times\hat{y} = 5\times10^4\,\hat{z}\ \text{V/m},\qquad \mathbf{E} = -5\times10^4\,\hat{z}\ \text{V/m},
> $$
> of magnitude $vB = 50$ kV/m.
>
> **(b)** Yes. The condition $\mathbf{E}+\mathbf{v}\times\mathbf{B} = 0$ contains neither $q$ nor $m$: for an electron both forces reverse together and still cancel. The selector picks a *velocity*, nothing else.
>
> **(c)** Electric force: $e\mathbf{E} = -8.01\times10^{-15}\,\hat{z}$ N, the same at any speed. Magnetic force: $e\mathbf{v}\times\mathbf{B} = +1.60\times10^{-14}\,\hat{z}$ N, twice as large as at the selected speed, because $v$ doubled. Net force: $+8.01\times10^{-15}\,\hat{z}$ N. The magnetic force wins and the proton is deflected toward $+z$.
>
> **Check:** units. Since 1 T = 1 V·s/m², a speed times a field, (m/s)·T, is V/m ✓.
>
> **Answer.** (a) $\mathbf{E} = -5\times10^4\hat{z}$ V/m; (b) yes, the condition does not involve $q$ or $m$; (c) $-8.01\times10^{-15}\hat{z}$ N (electric) plus $+1.60\times10^{-14}\hat{z}$ N (magnetic) gives $+8.01\times10^{-15}\hat{z}$ N, deflected toward $+z$.

### 2.5 A sphere cutting a charged plane

> [!easy] Easy · multiple choice · Gauss's law
> An infinite sheet with $\rho_s = -3$ C/m² lies on the plane $z = 0$, and a point charge $+10$ C sits at $(0,0,5)$ m (free space). What is the net outward flux of $\mathbf{D}$ through the sphere of radius 3 m centred at $(0,0,1)$ m?
>
> (a) $-27\pi$ C
>
> (b) $-24\pi$ C
>
> (c) $10-24\pi$ C
>
> (d) $-12\pi$ C
>
> *Source: original.*

> [!hint]- Hint
> Gauss's law needs only the charge *inside* the sphere. Which part of the sheet is inside? Sketch the cross-section in the $xz$ plane.

> [!solution]- Solution
> **Setup.** The flux equals the enclosed charge, so we never need the field itself.
>
> **Point charge.** $(0,0,5)$ is 4 m from the centre, more than the radius of 3 m. It is outside and contributes nothing (numerically, its flux through the sphere is 0).
>
> **Sheet.** The plane $z = 0$ passes 1 m below the centre, so it cuts the sphere in a disk of radius $\sqrt{3^2-1^2} = \sqrt8\approx2.83$ m and area $8\pi$ m². The enclosed charge is $\rho_s\cdot8\pi = -24\pi\approx-75.4$ C. A numerical surface integral of the sheet's field $\mathbf{D} = \tfrac12\rho_s\operatorname{sgn}(z)\,\hat{z}$ over the sphere gives the same $-75.4$ C.
>
> **The distractors.** (a) uses the sphere's radius, 3 m, for the disk, but the plane misses the centre by 1 m. (c) counts the point charge, which is outside: it changes $\mathbf{E}$ on the sphere but not the net flux. (d) halves the result, as if only one side of the sheet counted. Field lines end on the enclosed (negative) disk from both above and below, and both sets cross the sphere, so the whole $-24\pi$ C counts.
>
> **Answer.** (b) $-24\pi$ C $\approx-75.4$ C.

## Medium

### 2.6 Ring of charge on its axis

> [!medium] Medium · five-step program · ring
> A thin ring of radius $a = 10$ cm lies in the plane $z = 0$, centred on the origin, and carries a uniform line charge $\rho_l = 5$ nC/m (free space).
>
> (a) Use the 5-step program to find $\mathbf{E}$ at a point $(0,0,z)$ on the axis.
>
> (b) Evaluate it at $z = 10$ cm and at $z = 1$ m. Compare the second value with the field of a point charge equal to the ring's total charge.
>
> (c) At what height is the field strongest, and what is its largest value?
>
> *Source: classic (the Lecture 2 ring example), new numbers.*

> [!hint]- Hint
> Every element of the ring is the same distance $\sqrt{a^2+z^2}$ from the field point, and the element directly across the ring cancels the sideways part of yours. For (c), set $dE_z/dz = 0$.

> [!solution]- Solution
> **Setup.** Cylindrical coordinates. The element at angle $\phi'$ sits at $\mathbf{r}' = a\cos\phi'\,\hat{x}+a\sin\phi'\,\hat{y}$ and carries $dQ = \rho_l\,a\,d\phi'$.
>
> **(a)** From the element to $P = (0,0,z)$: $\mathbf{R} = z\hat{z}-a\cos\phi'\,\hat{x}-a\sin\phi'\,\hat{y}$, with $R = \sqrt{a^2+z^2}$ for every $\phi'$. The element at $\phi'+\pi$ has the opposite in-plane part, so the $x$ and $y$ components cancel in pairs (step 4). Only $dE_z = \dfrac{dQ}{4\pi\epsilon_0R^2}\cdot\dfrac{z}{R}$ survives, and its direction $\hat{z}$ is fixed:
> $$
> E_z = \int_0^{2\pi}\frac{\rho_l\,a\,z\,d\phi'}{4\pi\epsilon_0(a^2+z^2)^{3/2}} = \frac{\rho_l\,a\,z}{2\epsilon_0(a^2+z^2)^{3/2}} = \frac{Q\,z}{4\pi\epsilon_0(a^2+z^2)^{3/2}},\qquad Q = 2\pi a\rho_l .
> $$
> **(b)** $Q = 2\pi(0.1)(5\times10^{-9})$ C $= \pi$ nC $\approx3.14$ nC, and $Q/(4\pi\epsilon_0) = 28.2$ V·m. At $z = 10$ cm, $E_z = 998$ V/m. At $z = 1$ m, $E_z = 27.8$ V/m, while a point charge $Q$ at the origin would give $Q/(4\pi\epsilon_0z^2) = 28.2$ V/m, only 1.5% more. Seen from ten radii away, the ring already looks like a point charge.
>
> **(c)** Differentiate:
> $$
> \frac{d}{dz}\,\frac{z}{(a^2+z^2)^{3/2}} = \frac{(a^2+z^2)-3z^2}{(a^2+z^2)^{5/2}} = 0\quad\Rightarrow\quad z = \frac{a}{\sqrt2} = 7.07\ \text{cm},
> $$
> where
> $$
> E_{\max} = \frac{\rho_l}{3\sqrt3\,\epsilon_0a} = 1087\ \text{V/m}\qquad\Big(=\frac{2}{3\sqrt3}\,\frac{Q}{4\pi\epsilon_0a^2}\approx0.385\,\frac{Q}{4\pi\epsilon_0a^2}\Big).
> $$
> **Check:** $E_z(0) = 0$, since at the centre each element is cancelled by the one opposite; for $z\gg a$, $E_z\to Q/(4\pi\epsilon_0z^2)$; and $E_z$ is odd in $z$, pointing away from the positive ring on both sides. A field that starts at zero and dies away at large $z$ must peak in between, and a numerical maximization puts the peak at 7.07 cm too.
>
> **Watch out:** $\hat{R}$ changes direction around the ring. Integrate only the component along the *fixed* direction $\hat{z}$.
>
> **Answer.** $\mathbf{E} = \dfrac{\rho_l\,a\,z}{2\epsilon_0(a^2+z^2)^{3/2}}\,\hat{z}$; $998$ V/m at $z = 10$ cm and $27.8$ V/m at $z = 1$ m (point charge: $28.2$ V/m), both along $+\hat{z}$; largest magnitude $1087$ V/m at $z = \pm a/\sqrt2 = \pm7.07$ cm.

### 2.7 Semicircular arc, find the error

> [!medium] Medium · find the error · five-step program
> A thin wire bent into a semicircle of radius $a = 5$ cm, the half of the circle $x^2+y^2 = a^2$, $z = 0$ with $y>0$, carries a uniform line charge $\rho_l = 2$ nC/m (free space). A student finds the field at the centre (the origin) like this:
>
> *"Each element $dQ = \rho_l\,a\,d\phi$ is a distance $a$ from the centre, so $dE = \dfrac{\rho_l\,a\,d\phi}{4\pi\epsilon_0a^2}$. Adding up the half circle, $E = \displaystyle\int_0^\pi\frac{\rho_l\,d\phi}{4\pi\epsilon_0a} = \frac{\rho_l}{4\epsilon_0a} = 1129$ V/m, pointing along $-\hat{y}$, away from the wire."*
>
> (a) What is wrong? (b) Find the correct $\mathbf{E}$ at the origin.
>
> *Source: original.*

> [!hint]- Hint
> Draw $d\mathbf{E}$ at the origin for the elements at $\phi$ and at $\pi-\phi$. Do they point the same way? What happens to their $x$ components?

> [!solution]- Solution
> **The slip.** The student added the *magnitudes* $dE$ as if every $d\mathbf{E}$ pointed the same way. They do not: the element at angle $\phi$ pushes along $-(\cos\phi\,\hat{x}+\sin\phi\,\hat{y})$, a direction that turns with $\phi$. Treating that unit vector as a constant is exactly what step 4 of the 5-step program forbids.
>
> **The fix.** The element sits at $\mathbf{r}' = a\cos\phi\,\hat{x}+a\sin\phi\,\hat{y}$, so from it to the origin $\hat{R} = -(\cos\phi\,\hat{x}+\sin\phi\,\hat{y})$. Resolve into Cartesian components, whose unit vectors *are* constant:
> $$
> \mathbf{E} = \frac{\rho_l}{4\pi\epsilon_0a}\int_0^\pi\big(-\cos\phi\,\hat{x}-\sin\phi\,\hat{y}\big)\,d\phi .
> $$
> $\int_0^\pi\cos\phi\,d\phi = 0$ (the elements at $\phi$ and $\pi-\phi$ cancel in $x$) and $\int_0^\pi\sin\phi\,d\phi = 2$, so
> $$
> \mathbf{E} = -\frac{2\rho_l}{4\pi\epsilon_0a}\,\hat{y} = -\frac{\rho_l}{2\pi\epsilon_0a}\,\hat{y} = -719\,\hat{y}\ \text{V/m}.
> $$
> The student's value is too large by the factor $\pi/2\approx1.57$: $\pi$ from $\int_0^\pi d\phi$ instead of 2 from $\int_0^\pi\sin\phi\,d\phi$. The direction $-\hat{y}$ was right, because symmetry fixes it.
>
> **Check:** the magnitude of a sum of vectors can never exceed the sum of their magnitudes, so the true field had to be below 1129 V/m ✓. A neat cross-check: $\rho_l/(2\pi\epsilon_0a)$ is exactly the field of an *infinite* straight line with the same $\rho_l$ at distance $a$, and numerical integrals of both agree.
>
> **Answer.** (a) Magnitudes of vectors with different directions were added (the varying $\hat{R}$ was treated as constant). (b) $\mathbf{E} = -\dfrac{\rho_l}{2\pi\epsilon_0a}\,\hat{y} = -719\,\hat{y}$ V/m.

### 2.8 Dipole on axis and bisector

> [!medium] Medium · dipole · superposition
> A charge $-Q$ sits at $(0,0,d/2)$ and $+Q$ at $(0,0,-d/2)$ in free space, with $Q = 3$ nC and $d = 4$ mm.
>
> (a) Find the dipole moment $\mathbf{p}$.
>
> (b) Find the exact $\mathbf{E}$ at $P_1 = (0,0,2\ \text{cm})$ on the axis and at $P_2 = (2\ \text{cm},0,0)$ on the bisector, by superposing the two Coulomb fields.
>
> (c) Compare with the far-field formulas $\dfrac{2\mathbf{p}}{4\pi\epsilon_0D^3}$ (axis) and $-\dfrac{\mathbf{p}}{4\pi\epsilon_0D^3}$ (bisector), with $D = 2$ cm.
>
> (d) How far from the centre must a point on the axis be for the far-field value to differ from the exact one by less than 1%? Give $D$ in units of $d$.
>
> *Source: classic; extends the Lecture 2 bisector example.*

> [!hint]- Hint
> $\mathbf{p}$ points from $-Q$ to $+Q$, which here is downward. On the axis the two fields are collinear and partly cancel; on the bisector their $x$ components cancel and their $z$ components add. For (d), expand $(1-d^2/4D^2)^2$ to first order.

> [!solution]- Solution
> **(a)** $\mathbf{p} = Q(\mathbf{r}_+-\mathbf{r}_-) = Q\,(-d)\,\hat{z} = -1.2\times10^{-11}\,\hat{z}$ C·m. The dipole points *down*, from the negative charge to the positive one.
>
> **(b) Axis.** $P_1$ is $D-d/2 = 1.8$ cm from $-Q$ and $D+d/2 = 2.2$ cm from $+Q$. With $Q/(4\pi\epsilon_0) = 27.0$ V·m, $-Q$ pulls toward itself ($-\hat{z}$) with $8.32\times10^4$ V/m and $+Q$ pushes along $+\hat{z}$ with $5.57\times10^4$ V/m. Together:
> $$
> E_z(P_1) = \frac{Q}{4\pi\epsilon_0}\Big[\frac{1}{(D+d/2)^2}-\frac{1}{(D-d/2)^2}\Big] = -\frac{Q}{4\pi\epsilon_0}\,\frac{2Dd}{(D^2-d^2/4)^2} = -2.75\times10^4\ \text{V/m}.
> $$
> **Bisector.** Both charges are $\sqrt{D^2+d^2/4}$ from $P_2$. The $x$ components cancel (one field points away from $+Q$, the other toward $-Q$), and both $z$ components point along $+\hat{z}$:
> $$
> E_z(P_2) = \frac{Q}{4\pi\epsilon_0}\,\frac{d}{(D^2+d^2/4)^{3/2}} = +1.33\times10^4\ \text{V/m}.
> $$
> **(c)** At $D = 2$ cm the far-field formulas give $-2.70\times10^4\,\hat{z}$ V/m on the axis (2.0% below the exact value) and $+1.35\times10^4\,\hat{z}$ V/m on the bisector (1.5% above). The exact axis field is 2.07 times the bisector field here. The ratio tends to 2 (it is 2.0001 at $D = 0.5$ m), and doubling $D$ divides the field by 8: the $1/D^3$ law.
>
> **(d)** On the axis, $E_{\text{exact}} = E_{\text{far}}\,(1-d^2/4D^2)^{-2}$, so the relative difference is
> $$
> \frac{E_{\text{exact}}-E_{\text{far}}}{E_{\text{exact}}} = 1-\Big(1-\frac{d^2}{4D^2}\Big)^2\approx\frac{d^2}{2D^2}.
> $$
> Setting $d^2/(2D^2) = 0.01$ gives $D = d/\sqrt{0.02}\approx7.07\,d$. Solving the exact expression gives $D = 7.06\,d$, about 2.82 cm.
>
> **Check:** both exact results reduce to the far-field forms when $d\ll D$. Directions: on the axis $\mathbf{E}$ is parallel to $\mathbf{p}$ (both along $-\hat{z}$); on the bisector it is antiparallel ✓.
>
> **Answer.** $\mathbf{p} = -1.2\times10^{-11}\hat{z}$ C·m; $\mathbf{E}(P_1) = -2.75\times10^4\hat{z}$ V/m, $\mathbf{E}(P_2) = +1.33\times10^4\hat{z}$ V/m; far-field values $-2.70\times10^4\hat{z}$ and $+1.35\times10^4\hat{z}$ V/m (2.0% low and 1.5% high); within 1% on the axis for $D\gtrsim7.06\,d\approx2.82$ cm.

## Hard

### 2.9 Finite line charge at any point

> [!hard] Hard · five-step program · finite line · Gauss's law
> A uniform line charge $\rho_l = 60\pi\epsilon_0$ C/m ($\approx1.67$ nC/m) occupies the segment $0\le z\le4$ m of the $z$ axis in free space. Use cylindrical coordinates $(r,\phi,z)$.
>
> (a) With the 5-step program, show that a segment $z_1\le z'\le z_2$ on the axis produces, at a field point $(r,\phi,z)$,
> $$
> E_r = \frac{\rho_l}{4\pi\epsilon_0r}\,(\sin\alpha_2-\sin\alpha_1),\qquad E_z = \frac{\rho_l}{4\pi\epsilon_0r}\,(\cos\alpha_2-\cos\alpha_1),
> $$
> where $\alpha_i$ is the angle between the perpendicular from the field point to the axis and the line to the end $z_i$, counted positive toward $+z$: $\sin\alpha_i = (z_i-z)/\sqrt{r^2+(z_i-z)^2}$.
>
> (b) Find $\mathbf{E}$ at $P = (3,0,0)$ m: components, magnitude and direction. Show that $\mathbf{E}$ lies along the bisector of the angle that the segment subtends at $P$.
>
> (c) Extend the line to $0\le z<\infty$, then to $-\infty<z<\infty$. Find $\mathbf{E}$ at $P$ in both cases, and compare the infinite-line result with the lecture's $\rho_l/(2\pi\epsilon_0r)$.
>
> (d) Gauss's law also holds for the finite segment. What is the outward flux of $\mathbf{D}$ through the closed cylinder $r\le3$ m, $-1\le z\le5$ m? Explain why it still cannot give you $\mathbf{E}$, using your formula to evaluate $\mathbf{E}$ on the cylinder's side at $z = -1$, $2$ and $5$ m.
>
> *Source: classic; extends the Lecture 2 finite-line example to a general point.*

> [!hint]- Hint
> Substitute $z'-z = r\tan\alpha$. Then $dz' = r\sec^2\alpha\,d\alpha$ and $R = r\sec\alpha$, and both components become one-line integrals of $\cos\alpha$ and $\sin\alpha$. For (d), compare $E_r$ at different heights on the side of the cylinder.

> [!solution]- Solution
> **(a) Setup.** The element $dQ = \rho_l\,dz'$ sits at $(0,0,z')$, so $\mathbf{R} = r\hat{r}+(z-z')\hat{z}$ and $R^2 = r^2+(z'-z)^2$. Here $\hat{r}$ is the radial direction *at the field point*: it does not depend on $z'$, so it can leave the integral. The segment is not centred on the field point, so no symmetry removes a component and we keep both:
> $$
> E_r = \frac{\rho_l}{4\pi\epsilon_0}\int_{z_1}^{z_2}\frac{r\,dz'}{R^3},\qquad E_z = \frac{\rho_l}{4\pi\epsilon_0}\int_{z_1}^{z_2}\frac{(z-z')\,dz'}{R^3}.
> $$
> With $z'-z = r\tan\alpha$, $dz' = r\sec^2\alpha\,d\alpha$ and $R = r\sec\alpha$, the integrands become $\cos\alpha\,d\alpha/r$ and $-\sin\alpha\,d\alpha/r$:
> $$
> \begin{aligned}
> E_r &= \frac{\rho_l}{4\pi\epsilon_0r}\int_{\alpha_1}^{\alpha_2}\cos\alpha\,d\alpha = \frac{\rho_l}{4\pi\epsilon_0r}(\sin\alpha_2-\sin\alpha_1),\\
> E_z &= -\frac{\rho_l}{4\pi\epsilon_0r}\int_{\alpha_1}^{\alpha_2}\sin\alpha\,d\alpha = \frac{\rho_l}{4\pi\epsilon_0r}(\cos\alpha_2-\cos\alpha_1).
> \end{aligned}
> $$
> For a symmetric segment, $\alpha_1 = -\alpha_2$, this gives $E_z = 0$ and $E_r = \dfrac{\rho_l}{4\pi\epsilon_0r}\,2\sin\alpha_2$: the Lecture 2 result.
>
> **(b)** At $P$: $r = 3$ m, $\rho_l/(4\pi\epsilon_0) = 15$ V, so $\rho_l/(4\pi\epsilon_0r) = 5$ V/m. The near end $z_1 = 0$ is straight across, $\alpha_1 = 0$. The far end $(0,0,4)$ is 5 m away: $\sin\alpha_2 = 0.8$, $\cos\alpha_2 = 0.6$. With $\hat{r} = \hat{x}$ at $\phi = 0$:
> $$
> E_r = 5\,(0.8-0) = 4\ \text{V/m},\qquad E_z = 5\,(0.6-1) = -2\ \text{V/m},\qquad \mathbf{E} = 4\hat{x}-2\hat{z}\ \text{V/m},
> $$
> with $\lvert\mathbf{E}\rvert = \sqrt{20} = 4.47$ V/m at $26.6^\circ$ below the $+x$ direction: tilted away from the charge, which all lies above $P$.
>
> *Bisector:* the unit vectors from $P$ toward the two ends are $-\hat{x}$ and $-0.6\hat{x}+0.8\hat{z}$; their sum, $-1.6\hat{x}+0.8\hat{z}$, runs along the bisector of the angle. Its cross product with $\mathbf{E}$ is zero, so $\mathbf{E}$ lies along the bisector, and their dot product is $-8<0$, so $\mathbf{E}$ points away from the segment, as the field of positive charge should.
>
> **(c)** Semi-infinite line ($z_2\to\infty$, so $\alpha_2\to90^\circ$): $E_r = 5\,(1-0) = 5$ V/m and $E_z = 5\,(0-1) = -5$ V/m, so $\mathbf{E} = 5\hat{x}-5\hat{z}$ V/m. The added piece $4\le z<\infty$ contributes $\hat{x}-3\hat{z}$ V/m. Infinite line ($\alpha_1\to-90^\circ$ as well): $E_r = 5\,(1+1) = 10$ V/m and $E_z = 5\,(0-0) = 0$, so $\mathbf{E} = 10\,\hat{x}$ V/m $= \dfrac{\rho_l}{2\pi\epsilon_0r}\,\hat{r}$.
>
> *Preview of Lecture 3 (Gauss's law with symmetry):* for the infinite line, symmetry forces $\mathbf{D} = D_r(r)\,\hat{r}$. On a closed coaxial cylinder of radius $r$ and height $h$ the caps carry no flux and $D_r$ is constant on the side, so $D_r\cdot2\pi rh = \rho_lh$ and $E_r = \rho_l/(2\pi\epsilon_0r) = 10$ V/m at $r = 3$ m ✓. Two lines instead of a substitution integral.
>
> **(d)** The cylinder encloses the whole segment, so the flux is $Q_{\text{enc}} = 4\rho_l = 240\pi\epsilon_0$ C $\approx6.68$ nC. On its side, though, the formula from (a) gives $(E_r,E_z) = (2.71,\,-2.17)$ V/m at $z = -1$ m, $(5.55,\,0)$ V/m at $z = 2$ m and $(2.71,\,+2.17)$ V/m at $z = 5$ m. $E_r$ varies along the side and the caps receive flux, so $\oint\mathbf{D}\cdot d\mathbf{S}$ is not "$D$ times area" and cannot be solved for $\mathbf{E}$. (A numerical integration splits the 6.68 nC into 4.45 nC through the side and 1.11 nC through each cap.) Gauss's law is always *true*; it is *useful* only when symmetry makes $\mathbf{D}\cdot\hat{n}$ constant on the surface.
>
> **Check:** units, $\rho_l/(4\pi\epsilon_0)$ is in volts, and dividing by $r$ gives V/m ✓. The semi-infinite line gives $\lvert E_r\rvert = \lvert E_z\rvert$ at the point opposite its end, a 45° field, for any $r$ ✓. A brute-force numerical integral reproduces (b), and a second segment and field point off the plane $\phi = 0$ confirm the formulas of (a).
>
> **Answer.** (a) As stated. (b) $\mathbf{E} = 4\hat{x}-2\hat{z}$ V/m, $4.47$ V/m at $26.6^\circ$ below $+x$, along the bisector, pointing away from the segment. (c) $5\hat{x}-5\hat{z}$ V/m for the semi-infinite line and $10\hat{x}$ V/m for the infinite line, equal to $\rho_l/(2\pi\epsilon_0r)$. (d) $240\pi\epsilon_0$ C $\approx6.68$ nC, but $\mathbf{E}$ is not constant on the surface, so Gauss's law cannot be inverted.

### 2.10 Disk and annulus on axis

> [!hard] Hard · five-step program · disk · limits
> A thin disk of radius $a = 30$ cm lies in the plane $z = 0$, centred on the origin, with uniform surface charge $\rho_s = -5\ \mu\text{C/m}^2$ (free space).
>
> (a) Use the 5-step program to find $\mathbf{E}$ on the axis, for both $z>0$ and $z<0$.
>
> (b) Evaluate $\mathbf{E}$ at $z = 1$ cm and at $z = 3$ m. Compare the first value with an infinite sheet of the same $\rho_s$ and the second with a point charge equal to the disk's total charge (percent differences).
>
> (c) At what height has the field dropped to half its value right next to the disk?
>
> (d) A hole of radius $b = 10$ cm is cut from the centre, leaving an annulus $b<r<a$. Find $\mathbf{E}$ at $z = 10$ cm, and the field at the centre of the hole ($z\to0$).
>
> *Source: classic (disk on its axis); the annulus in (d) is original.*

> [!hint]- Hint
> Chop the disk into rings: the ring between $r'$ and $r'+dr'$ carries $dQ = \rho_s\,2\pi r'\,dr'$, and problem 2.6 gives its axial field. Careful: $\sqrt{z^2} = \lvert z\rvert$. For (d), a disk with a hole is a full disk plus a smaller disk of opposite charge.

> [!solution]- Solution
> **(a) Setup.** Cylindrical coordinates. Chop the disk into rings of radius $r'$ and width $dr'$, with $dQ = \rho_s\,2\pi r'\,dr'$. For each ring the in-plane components cancel around the ring, exactly as in 2.6, and the axial field is $dE_z = \dfrac{dQ\,z}{4\pi\epsilon_0(r'^2+z^2)^{3/2}}$. Add up the rings:
> $$
> E_z = \frac{\rho_s z}{2\epsilon_0}\int_0^a\frac{r'\,dr'}{(r'^2+z^2)^{3/2}} = \frac{\rho_s z}{2\epsilon_0}\Big[-\frac{1}{\sqrt{r'^2+z^2}}\Big]_0^a = \frac{\rho_s}{2\epsilon_0}\Big(\frac{z}{\lvert z\rvert}-\frac{z}{\sqrt{z^2+a^2}}\Big),
> $$
> that is, $E_z = \dfrac{\rho_s}{2\epsilon_0}\Big(\operatorname{sgn}(z)-\dfrac{z}{\sqrt{z^2+a^2}}\Big)$. With $\rho_s<0$ the field points toward the disk on both sides. Numerically, $\rho_s/(2\epsilon_0) = -2.82\times10^5$ V/m.
>
> **(b)** At $z = 1$ cm, $z/\sqrt{z^2+a^2} = 0.0333$, so $E_z = -2.82\times10^5\times0.967 = -2.73\times10^5$ V/m. Letting $a\to\infty$ in (a) gives the infinite sheet, $E_z = \dfrac{\rho_s}{2\epsilon_0}\operatorname{sgn}(z) = -2.82\times10^5$ V/m above it: only 3.4% stronger, because seen from 1 cm the edge of the disk is far away.
>
> At $z = 3$ m, $1-z/\sqrt{z^2+a^2} = 0.00496$, so $E_z = -1401$ V/m. The total charge is $Q = \pi a^2\rho_s = -1.41\ \mu\text{C}$, and a point charge gives $Q/(4\pi\epsilon_0z^2) = -1412$ V/m: 0.75% stronger. The binomial expansion $1-(1+a^2/z^2)^{-1/2}\approx a^2/(2z^2)$ turns the exact formula into $\dfrac{\rho_sa^2}{4\epsilon_0z^2} = \dfrac{Q}{4\pi\epsilon_0z^2}$, so far away the disk is a point charge.
>
> **(c)** Next to the disk $E_z\to\rho_s/(2\epsilon_0)$. Half of that requires
> $$
> 1-\frac{z}{\sqrt{z^2+a^2}} = \frac12\quad\Rightarrow\quad4z^2 = z^2+a^2\quad\Rightarrow\quad z = \frac{a}{\sqrt3} = 17.3\ \text{cm}.
> $$
> **(d)** By superposition the annulus is the disk of radius $a$ plus a disk of radius $b$ with charge density $-\rho_s$. For $z>0$ the $\operatorname{sgn}(z)$ terms cancel:
> $$
> E_z = \frac{\rho_s}{2\epsilon_0}\Big(\frac{z}{\sqrt{z^2+b^2}}-\frac{z}{\sqrt{z^2+a^2}}\Big) = -2.82\times10^5\,(0.707-0.316) = -1.10\times10^5\ \text{V/m}
> $$
> at $z = 10$ cm: the full disk's $-1.93\times10^5$ V/m minus the removed disk's $-8.27\times10^4$ V/m. As $z\to0$ both fractions vanish, so $E_z\to0$. At the centre of the hole the ring of charge pulls equally in every direction within its plane, and there is no charge at the centre to cause a jump.
>
> **Check:** across the full disk the field jumps by $E_z(0^+)-E_z(0^-) = \rho_s/\epsilon_0 = -5.65\times10^5$ V/m, the same jump as across an infinite sheet: right at the surface, every charged surface looks like an infinite sheet. Brute-force 2-D integrals over the disk and over the annulus reproduce every value above.
>
> **Watch out:** writing $\sqrt{z^2} = z$ gives a field that does not flip direction below the disk, which is wrong for every $z<0$.
>
> **Answer.** (a) $E_z = \dfrac{\rho_s}{2\epsilon_0}\Big(\operatorname{sgn}(z)-\dfrac{z}{\sqrt{z^2+a^2}}\Big)$, pointing toward the disk. (b) $\mathbf{E} = -2.73\times10^5\hat{z}$ V/m at 1 cm (sheet: $-2.82\times10^5$ V/m, 3.4% more) and $-1401\,\hat{z}$ V/m at 3 m (point charge: $-1412$ V/m, 0.75% more). (c) $z = a/\sqrt3 = 17.3$ cm. (d) $-1.10\times10^5\hat{z}$ V/m at 10 cm, and 0 at the centre of the hole.

### 2.11 A boron mass spectrometer

> [!hard] Hard · Lorentz force · velocity selector · mass spectrometer
> Boron ions travel along $+y$ through a velocity selector in the region $y<0$. In the selector $\mathbf{E} = E_0\hat{x}$ with $E_0 = 4\times10^4$ V/m, and a magnetic field $\mathbf{B}_1$ of magnitude $0.10$ T points along $+z$ or $-z$. Ions that pass leave through a slit at the origin, still moving along $+y$, and enter the analyzer region $y>0$, where $\mathbf{E} = 0$ and $\mathbf{B}_2 = 0.5\,\hat{z}$ T. They are detected where they come back to a plate in the plane $y = 0$. Take $m = 10u$ for $^{10}\text{B}$ and $11u$ for $^{11}\text{B}$, with $u = 1.6605\times10^{-27}$ kg and $e = 1.602\times10^{-19}$ C, and neglect gravity.
>
> (a) Which direction of $\mathbf{B}_1$ makes the selector work for positive ions, and what speed does it select? Does that speed depend on the ion's mass or charge?
>
> (b) An $^{11}\text{B}^{+}$ ion enters the selector 10% too fast. Find the electric, the magnetic and the net force on it, and the direction in which it is deflected.
>
> (c) In the analyzer, find the direction of the initial force and the sense of rotation, and the radius of the path, the landing point on the plate and the time spent in the analyzer for $^{10}\text{B}^{+}$, $^{11}\text{B}^{+}$ and $^{11}\text{B}^{2+}$.
>
> (d) How far apart are the $^{10}\text{B}^{+}$ and $^{11}\text{B}^{+}$ spots? What singly charged ion would land on the $^{11}\text{B}^{2+}$ spot? With what speed and kinetic energy do the $^{11}\text{B}^{+}$ ions arrive?
>
> *Source: original; combines the Lecture 2 velocity and mass selectors.*

> [!hint]- Hint
> The selector condition is $\mathbf{E}+\mathbf{v}\times\mathbf{B}_1 = 0$, so work out $\hat{y}\times\hat{z}$. In the analyzer, $qvB_2 = mv^2/R$, and the ions return to the plate after half a circle.

> [!solution]- Solution
> **(a)** We need $\mathbf{v}\times\mathbf{B}_1 = -E_0\hat{x}$ with $\mathbf{v} = v\hat{y}$. Since $\hat{y}\times\hat{z} = \hat{x}$, the choice $\mathbf{B}_1 = +B_1\hat{z}$ would *add* to $\mathbf{E}$, giving a force $2eE_0\hat{x} = 1.28\times10^{-14}\hat{x}$ N on a singly charged ion at the speed below. The choice $\mathbf{B}_1 = -B_1\hat{z}$ gives $\mathbf{v}\times\mathbf{B}_1 = -vB_1\hat{x}$, which cancels $\mathbf{E}$ when
> $$
> v = \frac{E_0}{B_1} = \frac{4\times10^4}{0.10} = 4\times10^5\ \text{m/s}.
> $$
> So $\mathbf{B}_1 = -0.10\,\hat{z}$ T. The condition contains neither $q$ nor $m$, so all three species leave with the same speed.
>
> **(b)** At $v = 4.4\times10^5$ m/s the electric force is $eE_0\hat{x} = +6.41\times10^{-15}\hat{x}$ N and the magnetic force is $e\mathbf{v}\times\mathbf{B}_1 = -evB_1\hat{x} = -7.05\times10^{-15}\hat{x}$ N, so the net force is $-6.41\times10^{-16}\hat{x}$ N. The magnetic force grows with speed and wins: the fast ion drifts toward $-x$ and misses the slit. (A slow ion would drift toward $+x$.)
>
> **(c)** At the origin $q\mathbf{v}\times\mathbf{B}_2 = qvB_2\,\hat{y}\times\hat{z} = +qvB_2\,\hat{x}$, so the ions start to curve toward $+x$. The magnetic force is always perpendicular to $\mathbf{v}$, so the speed stays $4\times10^5$ m/s and the path is a circle, with $qvB_2 = mv^2/R$:
> $$
> R = \frac{mv}{qB_2},\qquad \text{landing at } x = 2R \text{ after half a turn},\qquad t = \frac{\pi R}{v} = \frac{\pi m}{qB_2}.
> $$
> The centre of the circle is at $(R,0,0)$, and the ion starts on its left-hand side moving along $+y$: clockwise as seen from $+z$.
>
> | ion | $m$ | $q$ | $R$ | landing point $x = 2R$ | time in analyzer |
> |---|---|---|---|---|---|
> | $^{10}\text{B}^{+}$ | $10u$ | $e$ | 8.29 cm | 16.58 cm | 0.651 μs |
> | $^{11}\text{B}^{+}$ | $11u$ | $e$ | 9.12 cm | 18.24 cm | 0.716 μs |
> | $^{11}\text{B}^{2+}$ | $11u$ | $2e$ | 4.56 cm | 9.12 cm | 0.358 μs |
>
> **(d)** The $^{10}\text{B}^{+}$ and $^{11}\text{B}^{+}$ spots are $2(R_{11}-R_{10}) = 1.66$ cm apart. The radius depends only on $m/q$, and $^{11}\text{B}^{2+}$ has $m/q = 5.5u/e$, so it lands exactly where a singly charged ion of mass $5.5u$ would. The $^{11}\text{B}^{+}$ ions arrive with their entry speed, $4\times10^5$ m/s, and kinetic energy $\tfrac12(11u)v^2 = 9.12$ keV, because the magnetic force does no work.
>
> **Check:** integrating $m\,d\mathbf{v}/dt = q\mathbf{v}\times\mathbf{B}_2$ numerically lands each ion at $x = 2R$ after $\pi m/(qB_2)$, with its speed unchanged ✓. Units: since 1 T = 1 kg/(C·s), $mv/(qB)$ is (kg·m/s)/(kg/s) = m ✓.
>
> **Watch out:** the sense of rotation depends on the sign of $q$. Negative ions would curve toward $-x$ and land at $x = -2R$, on the other side of the slit.
>
> **Answer.** (a) $\mathbf{B}_1 = -0.10\hat{z}$ T; $v = 4\times10^5$ m/s for every species. (b) $+6.41\times10^{-15}\hat{x}$ N (electric) and $-7.05\times10^{-15}\hat{x}$ N (magnetic), net $-6.41\times10^{-16}\hat{x}$ N: deflected toward $-x$. (c) Initial force along $+\hat{x}$, clockwise seen from $+z$; $R = 8.29$, $9.12$ and $4.56$ cm, landing at $x = 16.58$, $18.24$ and $9.12$ cm after $0.651$, $0.716$ and $0.358$ μs. (d) 1.66 cm; an ion of mass $5.5u$; $4\times10^5$ m/s and $9.12$ keV.

### 2.12 Two charges, one given field

> [!hard] Hard · superposition · null point · Gauss's law
> In free space, a point charge $Q_1$ sits at $(0,0,2)$ m.
>
> (a) On its own, $Q_1$ produces $\mathbf{E} = -3\hat{z}$ V/m at the origin. Find $Q_1$, as a multiple of $\pi\epsilon_0$ and in nC.
>
> (b) A second point charge $Q_2$, with $\lvert Q_2\rvert = 16\pi\epsilon_0$ C, is placed somewhere on the $x$ axis, and the total field at the origin becomes $\mathbf{E} = -4\hat{x}-3\hat{z}$ V/m. Find every possible sign and position of $Q_2$.
>
> (c) Take $Q_2 = +16\pi\epsilon_0$ C at $(1,0,0)$ m. Find the point where $\mathbf{E} = 0$, and explain why there is no other.
>
> (d) With the charges of (c), find the net outward flux of $\mathbf{D}$ through the sphere of radius $1.5$ m centred on the origin, and through the cube $0\le x,y,z\le1$ m.
>
> *Source: Summer 2017 HE1 #1a style, re-parameterized and extended (null point, flux).*

> [!hint]- Hint
> (a)–(b): a point charge's field points *away* from it if it is positive and *toward* it if it is negative, so a direction fixes a combination of sign and side, not a sign alone. (c): between two like charges the null point lies on the segment joining them, closer to the smaller charge. (d): where exactly is $Q_2$ relative to the cube?

> [!solution]- Solution
> **(a)** At the origin the field points along $-\hat{z}$, away from $(0,0,2)$, so $Q_1>0$. Magnitude:
> $$
> \frac{Q_1}{4\pi\epsilon_0\,(2)^2} = 3\quad\Rightarrow\quad Q_1 = 48\pi\epsilon_0\ \text{C}\approx1.34\ \text{nC}.
> $$
> **(b)** By superposition $Q_2$ must supply $\mathbf{E}-\mathbf{E}_1 = -4\hat{x}$ V/m at the origin. If $Q_2$ sits at $(X,0,0)$, its field there has magnitude $\dfrac{16\pi\epsilon_0}{4\pi\epsilon_0X^2} = \dfrac{4}{X^2} = 4$, so $\lvert X\rvert = 1$ m. The direction $-\hat{x}$ means *away* from a positive charge at $x = +1$ m, or *toward* a negative charge at $x = -1$ m:
> $$
> Q_2 = +16\pi\epsilon_0\ \text{C at }(1,0,0)\ \text{m}\qquad\text{or}\qquad Q_2 = -16\pi\epsilon_0\ \text{C at }(-1,0,0)\ \text{m}.
> $$
> A root search along the whole $x$ axis, for both signs, finds exactly these two. (For example, $+16\pi\epsilon_0$ C at $x = -1$ m would give $+4\hat{x}$ instead.) Both give $\lvert\mathbf{E}\rvert = 5$ V/m.
>
> **(c)** Both charges are positive. Off the line through them, their fields are not collinear and cannot cancel. On that line but outside the segment, they point the same way and add. So the null point is on the segment, where they are opposite. With $d_1$ and $d_2$ the distances to $Q_1$ and $Q_2$:
> $$
> \frac{48\pi\epsilon_0}{4\pi\epsilon_0d_1^2} = \frac{16\pi\epsilon_0}{4\pi\epsilon_0d_2^2}\quad\Rightarrow\quad\frac{d_1}{d_2} = \sqrt3 .
> $$
> The segment from $(1,0,0)$ to $(0,0,2)$ has length $\sqrt5 = 2.24$ m, so $d_2 = \sqrt5/(1+\sqrt3) = 0.818$ m, and the null point is
> $$
> \mathbf{r}_0 = (1,0,0)+\frac{1}{1+\sqrt3}\,(-1,0,2) = \Big(\frac{3-\sqrt3}{2},\ 0,\ \sqrt3-1\Big)\approx(0.634,\ 0,\ 0.732)\ \text{m}.
> $$
> Check: $d_1 = 1.42$ m and $d_1/d_2 = 1.73$ ✓. A numerical search from 400 random starting points finds this point and no other.
>
> **(d)** Sphere of radius 1.5 m: $Q_2$, 1 m from the origin, is inside, and $Q_1$, 2 m away, is outside. The flux is $Q_2 = 16\pi\epsilon_0$ C $\approx0.445$ nC.
>
> Cube: $Q_1$ is outside, and $Q_2$ sits exactly on the cube's *corner* $(1,0,0)$. As in 2.3, a corner charge sends one eighth of its flux through the cube: $Q_2/8 = 2\pi\epsilon_0$ C $\approx55.6$ pC. All of it leaves through the three faces that do not touch $Q_2$ ($x = 0$, $y = 1$ and $z = 1$), $Q_2/24\approx18.5$ pC each.
>
> **Check:** numerical surface integrals give 0.445 nC through the sphere and 55.6 pC through the cube, with the outside charge contributing zero in both cases ✓.
>
> **Watch out:** in (b), a field direction alone does not fix the sign of a charge. Always pair the sign with the side.
>
> **Answer.** (a) $Q_1 = 48\pi\epsilon_0$ C $\approx1.34$ nC. (b) $+16\pi\epsilon_0$ C at $(1,0,0)$ m, or $-16\pi\epsilon_0$ C at $(-1,0,0)$ m. (c) $\mathbf{r}_0 = \big((3-\sqrt3)/2,\,0,\,\sqrt3-1\big)\approx(0.634,\,0,\,0.732)$ m, the only null point. (d) $16\pi\epsilon_0$ C $\approx0.445$ nC through the sphere and $2\pi\epsilon_0$ C $\approx55.6$ pC through the cube.

### Sources for this page
Lecture 2 notes and slides: the velocity and mass selectors behind 2.4 and 2.11, the "review at home" ring (2.6), the dipole on the bisector (2.8), the finite line charge (2.9) and the step from Coulomb to Gauss (2.3, 2.5). Old exam: Summer 2017 HE1 #1a, the model for 2.12, re-parameterized and extended with a null point and a flux. Classic textbook configurations with new numbers: the null point of two charges (2.2), the charge at a cube corner (2.3), the finite segment at a general point (2.9) and the disk on its axis (2.10). Problems 2.1, 2.5, 2.7 and 2.11 and the annulus of 2.10 are original.

*Next: [[practice/03-gauss-law-at-work|Lecture 3 practice]] · [[practice/index|all practice]]*
