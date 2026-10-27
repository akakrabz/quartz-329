---
title: "Practice — Lecture 13: Current sheets, solenoids and the vector potential"
description: "12 practice problems (5 easy, 3 medium, 4 hard) on current sheets and slabs, the jump in tangential H, solenoids, nested solenoids and toroids, the vector potential (curl, Coulomb gauge, gauge freedom, wire and solenoid), the current loop on its axis, Helmholtz coils, finite solenoids and the 1/r³ dipole far field, each with a folded hint and a worked solution."
tags: [practice, magnetostatics]
lecture: 13
---

*Practice for [[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential|Lecture 13]] · concepts: [[concepts/amperes-law]] · [[concepts/vector-potential]] · [[concepts/boundary-conditions]] · [[concepts/magnetic-field]] · all practice: [[practice/index|hub]] · by difficulty: [[practice/easy|easy]] · [[practice/medium|medium]] · [[practice/hard|hard]] · [[practice/topics|by topic]]*

Work each problem on paper first. Open the **hint** only when stuck, and the **solution** only after you have an answer you would hand in. Every answer here has been checked numerically.

## Easy

### 13.1 One current sheet, two points

> [!easy] Easy · current sheets · cross product
> The plane $z = 0$ carries the uniform surface current $\mathbf{J}_s = 8\hat{y}$ A/m in free space.
> (a) Find $\mathbf{H}$ and $\mathbf{B}$ at $P_1 = (0, 0, 0.5)$ m and at $P_2 = (3, -2, -40)$ m.
> (b) The current is changed to $\mathbf{J}_s = 6\hat{x}+8\hat{y}$ A/m. Find $\mathbf{H}$ above and below the sheet, and check that $\lvert\mathbf{H}\rvert = \lvert\mathbf{J}_s\rvert/2$ and $\mathbf{H}\perp\mathbf{J}_s$.
>
> *Source: original.*

> [!hint]- Hint
> Only the *side* of the sheet matters, not the distance or the position along the sheet. Write $\hat{n}$ for each point (from the sheet toward the point), then work out $\tfrac12\mathbf{J}_s\times\hat{n}$ term by term.

> [!solution]- Solution
> An infinite sheet gives $\mathbf{H} = \tfrac12\mathbf{J}_s\times\hat{n}$, with $\hat{n}$ the unit normal pointing from the sheet toward the field point. The sheet has no edge and no length scale, so the field depends only on which side you are on — not on $x$, $y$ or the distance.
>
> **(a)** $P_1$ is above the sheet ($z = 0.5$ m $>0$), so $\hat{n} = +\hat{z}$:
> $$
> \mathbf{H}(P_1) = \tfrac12(8\hat{y})\times\hat{z} = 4\,(\hat{y}\times\hat{z}) = 4\hat{x}\ \text{A/m}.
> $$
> $P_2$ is below ($z = -40$ m), so $\hat{n} = -\hat{z}$: $\mathbf{H}(P_2) = \tfrac12(8\hat{y})\times(-\hat{z}) = -4\hat{x}$ A/m — the same size 40 m away, reversed. Then $\mathbf{B} = \mu_0\mathbf{H}$: $+4\mu_0\hat{x}$ at $P_1$ and $-4\mu_0\hat{x}$ at $P_2$, of magnitude $4\mu_0\approx5.027$ μT.
>
> **(b)** Above, $\hat{n} = +\hat{z}$; with $\hat{x}\times\hat{z} = -\hat{y}$ and $\hat{y}\times\hat{z} = \hat{x}$,
> $$
> \mathbf{H}_{\text{above}} = \tfrac12(6\hat{x}+8\hat{y})\times\hat{z} = 3(\hat{x}\times\hat{z})+4(\hat{y}\times\hat{z}) = 4\hat{x}-3\hat{y}\ \text{A/m}.
> $$
> Below, $\hat{n} = -\hat{z}$ flips every sign: $\mathbf{H}_{\text{below}} = -4\hat{x}+3\hat{y}$ A/m. The size is $\sqrt{4^2+3^2} = 5$ A/m $=\tfrac12\sqrt{6^2+8^2} = \lvert\mathbf{J}_s\rvert/2$, and $\mathbf{H}\cdot\mathbf{J}_s = 4(6)+(-3)(8) = 0$: the field lies in the sheet at right angles to the current, just as the field of each current filament circles that filament.
>
> **Check:** the tangential field must jump by $\mathbf{J}_s$ across the sheet: $\hat{z}\times(\mathbf{H}_{\text{above}}-\mathbf{H}_{\text{below}}) = \hat{z}\times(8\hat{x}-6\hat{y}) = 8\hat{y}+6\hat{x} = \mathbf{J}_s$ ✓. Summing the fields of the sheet's filaments numerically gives the same vectors.
>
> **Watch out:** a current along $\hat{y}$ makes a field along $\pm\hat{x}$ — not along $\hat{y}$, and never along the normal $\hat{z}$. Let the cross product decide the sign.
>
> **Answer.** (a) $\mathbf{H}(P_1) = 4\hat{x}$ A/m, $\mathbf{B}(P_1) = 4\mu_0\hat{x}$ ($\approx5.027$ μT along $+\hat{x}$); $\mathbf{H}(P_2) = -4\hat{x}$ A/m, $\mathbf{B}(P_2) = -4\mu_0\hat{x}$. (b) $\mathbf{H} = 4\hat{x}-3\hat{y}$ A/m above and $-4\hat{x}+3\hat{y}$ A/m below; $\lvert\mathbf{H}\rvert = 5$ A/m $=\lvert\mathbf{J}_s\rvert/2$ and $\mathbf{H}\cdot\mathbf{J}_s = 0$.

### 13.2 Crossing a current sheet

> [!easy] Easy · multiple choice · boundary conditions
> The plane $x = 0$ carries the surface current $\mathbf{J}_s = 3\hat{z}$ A/m, with free space on both sides; other, distant sources are also present. Just to the left of the sheet ($x<0$) the total field is $\mathbf{H} = 2\hat{x}-\hat{y}$ A/m. What is $\mathbf{H}$ just to the right ($x>0$)?
>
> (a) $2\hat{x}-4\hat{y}$ A/m
>
> (b) $2\hat{x}+2\hat{y}$ A/m
>
> (c) $5\hat{x}-\hat{y}$ A/m
>
> (d) $2\hat{x}-\hat{y}+3\hat{z}$ A/m
>
> (e) $2\hat{x}+0.5\hat{y}$ A/m
>
> (f) $-2\hat{x}+2\hat{y}$ A/m
>
> *Source: original.*

> [!hint]- Hint
> Split $\mathbf{H}$ into its part normal to the sheet ($\hat{x}$) and its part along the sheet. One part is continuous; the other jumps by an amount fixed by $\hat{n}\times(\mathbf{H}_1-\mathbf{H}_2) = \mathbf{J}_s$.

> [!solution]- Solution
> **(b).** Call the right side region 1 and the left side region 2, so $\hat{n} = \hat{x}$ points from 2 into 1.
>
> *Normal part.* $\nabla\cdot\mathbf{B} = 0$ makes $B_x$ continuous, and with $\mu_0$ on both sides so is $H_x = 2$ A/m.
>
> *Tangential part.* For a jump lying in the sheet, $\hat{n}\times(\mathbf{H}_1-\mathbf{H}_2) = \mathbf{J}_s$ is solved by $\mathbf{H}_1-\mathbf{H}_2 = \mathbf{J}_s\times\hat{n}$ (because $\hat{n}\times(\mathbf{J}_s\times\hat{n}) = \mathbf{J}_s$ when $\mathbf{J}_s\perp\hat{n}$):
> $$
> \mathbf{J}_s\times\hat{n} = 3\,(\hat{z}\times\hat{x}) = 3\hat{y}\ \text{A/m}\quad\Rightarrow\quad\mathbf{H}_1 = 2\hat{x}+(-1+3)\hat{y} = 2\hat{x}+2\hat{y}\ \text{A/m}.
> $$
> **Check:** $\hat{x}\times(\mathbf{H}_1-\mathbf{H}_2) = \hat{x}\times3\hat{y} = 3\hat{z} = \mathbf{J}_s$ ✓. Second route: the sheet's own field is $\tfrac12\mathbf{J}_s\times\hat{n}$, i.e. $\tfrac12(3\hat{z})\times(-\hat{x}) = -1.5\hat{y}$ A/m on the left and $+1.5\hat{y}$ A/m on the right. Removing it from the left-side field leaves the distant sources' field, $2\hat{x}+0.5\hat{y}$ A/m, which passes through the sheet unchanged; adding the right-side $+1.5\hat{y}$ gives $2\hat{x}+2\hat{y}$ ✓.
>
> Why the others fail:
>
> - (a) uses $\hat{n}\times\mathbf{J}_s = -3\hat{y}$ for the jump; then $\hat{x}\times(\mathbf{H}_1-\mathbf{H}_2) = -3\hat{z} = -\mathbf{J}_s$, the wrong sign.
> - (c) puts the jump into the normal component. $H_x$ cannot change (that would make $B_n$ jump), and with the tangential part unchanged $\hat{x}\times(\mathbf{H}_1-\mathbf{H}_2) = 0\ne\mathbf{J}_s$.
> - (d) adds $\mathbf{J}_s$ itself. The jump in $\mathbf{H}$ is perpendicular to the current, not along it: $\hat{x}\times3\hat{z} = -3\hat{y}\ne\mathbf{J}_s$.
> - (e) adds only half the jump. It is the distant sources' field (the average of the two sides), not the field on the right: $\hat{x}\times(\mathbf{H}_1-\mathbf{H}_2) = 1.5\hat{z}$.
> - (f) gets the tangential jump right, $\hat{x}\times(-4\hat{x}+3\hat{y}) = 3\hat{z}$, but flips $H_x$ from $+2$ to $-2$, so $B_n$ would jump — impossible.
>
> **Answer.** (b) $\mathbf{H} = 2\hat{x}+2\hat{y}$ A/m: $H_x$ is continuous, and the tangential part rises by $\mathbf{J}_s\times\hat{x} = 3\hat{y}$ A/m.

### 13.3 A solenoid inside a solenoid

> [!easy] Easy · solenoid · magnetic flux · superposition
> A long solenoid of radius $a_1 = 2$ cm on the $z$ axis has $n_1 = 2000$ turns/m and carries $I_1 = 0.5$ A, counter-clockwise seen from $+z$. Free space inside.
> (a) Find $\mathbf{H}$ and $\mathbf{B}$ inside it, and the flux through its cross-section.
> (b) A second long solenoid, of radius $a_2 = 1$ cm with $n_2 = 400$ turns/m, is slid in coaxially. What current $I_2$ (size and sense) makes the field zero for $r<1$ cm?
> (c) With that $I_2$, find $\mathbf{H}$ for $1<r<2$ cm and the flux through a disk of radius 2 cm perpendicular to the axis.
>
> *Source: Summer 2017 HE2 #1b and Summer 2020 HE2 #2b style (an inner solenoid whose current cancels the field in the core), re-parameterized.*

> [!hint]- Hint
> An ideal solenoid's field is confined to its own interior. At a point with $r<1$ cm, which coils contribute? At $1<r<2$ cm?

> [!solution]- Solution
> **(a)** Inside a long solenoid $\mathbf{H} = nI\hat{z}$ for current counter-clockwise seen from $+z$ (right-hand rule: fingers along the current, thumb along $+\hat{z}$), and zero outside. So $\mathbf{H} = 2000\times0.5\,\hat{z} = 1000\hat{z}$ A/m and $\mathbf{B} = \mu_0\mathbf{H} = 4\pi\times10^{-4}\hat{z}$ T $\approx1.257$ mT along $+\hat{z}$ — uniform, with no radius in it. The flux is
> $$
> \Psi = B\,\pi a_1^2 = 4\pi\times10^{-4}\times\pi(0.02)^2 = 16\pi^2\times10^{-8}\ \text{Wb}\approx1.58\ \mu\text{Wb}.
> $$
> **(b)** For $r<1$ cm you are inside *both* coils, so $H_z = n_1I_1+n_2I_2$. Zero needs
> $$
> I_2 = -\frac{n_1I_1}{n_2} = -\frac{1000}{400} = -2.5\ \text{A},
> $$
> that is, 2.5 A *clockwise* seen from $+z$.
>
> **(c)** For $1<r<2$ cm you are outside the inner coil, whose field is zero there, and inside the outer one: $\mathbf{H} = 1000\hat{z}$ A/m, unchanged. Only the annulus carries flux:
> $$
> \Psi = \mu_0(1000)\,\pi\big(a_1^2-a_2^2\big) = 12\pi^2\times10^{-8}\ \text{Wb}\approx1.18\ \mu\text{Wb}.
> $$
> **Check:** each winding is a cylindrical sheet $\mathbf{J}_s = nI\hat\phi$, so tangential $\mathbf{H}$ must jump by it. At $r = a_2$, with $\hat{n} = \hat{r}$ from the core (2) into the annulus (1): $\hat{r}\times(1000\hat{z}-0) = -1000\hat\phi$ A/m $= n_2I_2\hat\phi$ ✓ (using $\hat{r}\times\hat{z} = -\hat\phi$). At $r = a_1$: $\hat{r}\times(0-1000\hat{z}) = +1000\hat\phi$ A/m $= n_1I_1\hat\phi$ ✓. A Biot–Savart sum over the rings of two 2-m-long coils gives 999.8 A/m in the annulus.
>
> **Watch out:** the inner coil does not weaken the field in the annulus — its field stops at its own winding.
>
> **Answer.** (a) $\mathbf{H} = 1000\hat{z}$ A/m, $\mathbf{B} = 4\pi\times10^{-4}\hat{z}$ T $\approx1.257$ mT, $\Psi = 16\pi^2\times10^{-8}$ Wb $\approx1.58$ μWb. (b) $I_2 = 2.5$ A clockwise seen from $+z$ ($I_2 = -2.5$ A). (c) $\mathbf{H} = 1000\hat{z}$ A/m; $\Psi = 12\pi^2\times10^{-8}$ Wb $\approx1.18$ μWb.

### 13.4 Toroid with rectangular cross-section

> [!easy] Easy · Ampère's law · toroid
> A toroid with a rectangular cross-section is centred on the $z$ axis: inner radius $a = 4$ cm, outer radius $b = 6$ cm, height $h = 2$ cm ($-1<z<1$ cm). Its $N = 600$ turns carry $I = 2$ A, wound so that the current flows along $+\hat{z}$ on the inner wall $r = a$ and along $-\hat{z}$ on the outer wall $r = b$. Free space throughout.
> (a) Use Ampère's law to find $\mathbf{H}$ everywhere.
> (b) Evaluate $B$ at $r = 4$, 5 and 6 cm (at 4 and 6 cm, just inside the core), and the ratio $B(a)/B(b)$. Does the answer depend on $h$?
>
> *Source: classic.*

> [!hint]- Hint
> Take a circle of radius $r$ about the $z$ axis. Count the wires that pierce the flat disk bounded by the circle, with their signs, for $r<a$, $a<r<b$ and $r>b$.

> [!solution]- Solution
> **(a)** The winding looks the same after any rotation about $z$, so $\mathbf{H} = H_\phi\hat\phi$. Ampère's law on a circle of radius $r$, traversed counter-clockwise seen from $+z$ (so currents along $+\hat{z}$ count positive), gives $H_\phi\cdot2\pi r = I_{\text{enc}}$. For $r<a$ no wire pierces the disk; for $a<r<b$ the $N$ inner-wall wires do, each carrying $I$ along $+\hat{z}$, so $I_{\text{enc}} = NI$; for $r>b$ the $N$ outer-wall wires carrying $I$ along $-\hat{z}$ pierce it too, so $I_{\text{enc}} = 0$; above or below the core nothing pierces it. Hence
> $$
> \mathbf{H} = \begin{cases}\dfrac{NI}{2\pi r}\,\hat\phi, & a<r<b,\ \lvert z\rvert<h/2\ \ (\text{inside the core}),\\[4pt] 0, & \text{everywhere else}.\end{cases}
> $$
> **(b)** $B = \mu_0NI/(2\pi r)$ with $\mu_0NI/(2\pi) = 2\times10^{-7}\times600\times2 = 2.4\times10^{-4}$ T·m:
> $$
> B(4\ \text{cm}) = 6\ \text{mT},\qquad B(5\ \text{cm}) = 4.8\ \text{mT},\qquad B(6\ \text{cm}) = 4\ \text{mT}
> $$
> ($H = 4775$, 3820 and 3183 A/m). So $B(a)/B(b) = b/a = 1.5$: the field is strongest at the inner wall. The height $h$ never entered — it only sets where the formula applies (it will matter for the flux).
>
> **Check:** a Biot–Savart sum over the 600 rectangular turns gives $H_\phi = 3820$ A/m at $r = 5$ cm, and less than $10^{-11}$ A/m (zero up to rounding) at $r = 3$ and 7 cm. For a thin toroid, $b-a\ll a$, $N/(2\pi r)$ is the number of turns per metre along the core and $H = nI$: the solenoid result bent into a ring.
>
> **Watch out:** the toroid's field is not uniform over the cross-section; it falls as $1/r$, and the formula uses the total $N$, not turns per metre.
>
> **Answer.** (a) $\mathbf{H} = \dfrac{NI}{2\pi r}\hat\phi$ inside the core ($4<r<6$ cm, $\lvert z\rvert<1$ cm), zero everywhere else. (b) $B = 6$, 4.8 and 4 mT at $r = 4$, 5 and 6 cm; $B(a)/B(b) = 1.5$; no dependence on $h$.

### 13.5 Five true or false statements

> [!easy] Easy · true or false · sheets and solenoids · vector potential
> True or false? Give a one-line reason for each.
>
> (i) The field of the current sheet $\mathbf{J}_s = 6\hat{y}$ A/m on the plane $z = 0$ is weaker at $z = 2$ m than at $z = 1$ m.
>
> (ii) Doubling the radius of a long solenoid at fixed $n$ and $I$ leaves the field inside unchanged and multiplies the flux through its cross-section by 4.
>
> (iii) The magnetic field of an infinite plane current sheet has no component perpendicular to the sheet.
>
> (iv) $\mathbf{A}_1 = \tfrac12B_0(-y\hat{x}+x\hat{y})$ and $\mathbf{A}_2 = B_0x\hat{y}$, with $B_0 = 0.7$ T, are different vector fields, so they describe different magnetic fields.
>
> (v) Far from a circular current loop, along its axis, $B$ falls off as $1/z^2$, like the electric field of a point charge.
>
> *Source: original.*

> [!hint]- Hint
> For (i) and (iii), look at what $\tfrac12\mathbf{J}_s\times\hat{n}$ depends on and which way it can point. For (iv), take both curls. For (v), let $\lvert z\rvert\gg a$ in the on-axis loop formula.

> [!solution]- Solution
> **(i) False.** $\lvert\mathbf{H}\rvert = J_s/2 = 3$ A/m at *every* distance: an infinite sheet has no length scale to fall off with. (Summing the fields of the sheet's filaments numerically gives 3.000000 A/m at both 1 m and 2 m.)
>
> **(ii) True.** $B = \mu_0nI$ contains no radius, and $\Psi = B\pi a^2$ scales as $a^2$. With $n = 1000$ turns/m and $I = 1$ A, $B = 1.2566$ mT for both $a = 1$ cm and $a = 2$ cm, while $\Psi$ grows from 0.395 μWb to 1.58 μWb. (These are the centre values of a 4-m-long coil; they match $\mu_0nI$ to the digits shown.)
>
> **(iii) True.** $\tfrac12\mathbf{J}_s\times\hat{n}$ is a cross product with $\hat{n}$, so it is perpendicular to $\hat{n}$: the field lies in the plane of the sheet (and is also perpendicular to $\mathbf{J}_s$).
>
> **(iv) False.** Neither potential depends on $z$ or has a $z$ component, so only the $\hat{z}$ part of each curl survives:
> $$
> \nabla\times\mathbf{A}_1 = \hat{z}\Big(\frac{\partial A_{1y}}{\partial x}-\frac{\partial A_{1x}}{\partial y}\Big) = \hat{z}\big(\tfrac12B_0+\tfrac12B_0\big) = B_0\hat{z},\qquad\nabla\times\mathbf{A}_2 = \hat{z}\,\frac{\partial(B_0x)}{\partial x} = B_0\hat{z}.
> $$
> Both describe the uniform field $\mathbf{B} = 0.7\hat{z}$ T. They differ by a gradient, $\mathbf{A}_2-\mathbf{A}_1 = \tfrac12B_0(y\hat{x}+x\hat{y}) = \nabla\big(\tfrac12B_0xy\big)$, and $\nabla\times\nabla\lambda = 0$: this is the gauge freedom of $\mathbf{A}$. Both even have $\nabla\cdot\mathbf{A} = 0$, so here the Coulomb gauge does not single one out.
>
> **(v) False.** On the axis $B_z = \dfrac{\mu_0Ia^2}{2(a^2+z^2)^{3/2}}\to\dfrac{\mu_0Ia^2}{2\lvert z\rvert^3}$, an inverse *cube*, like the electric dipole: there is no magnetic charge to produce a $1/z^2$ term, and a loop's leading far field is a dipole field. For $a = 1$ m and $I = 1$ A, $B_zz^3$ climbs toward $\mu_0/2 = 6.283\times10^{-7}$ T·m³ (it is $4.496$, $5.737$, $6.139$ and $6.247\times10^{-7}$ T·m³ at $z = 2$, 4, 8 and 16 m), while $B_zz^2$ keeps falling.
>
> **Check:** for (iv), finite-difference curls of $\mathbf{A}_1$ and $\mathbf{A}_2$ at two arbitrary points both give $(0, 0, 0.7)$ T, and $\mathbf{A}_2-\mathbf{A}_1$ equals $\nabla(\tfrac12B_0xy)$ there.
>
> **Answer.** (i) False — 3 A/m at both heights. (ii) True. (iii) True. (iv) False — the same $\mathbf{B} = 0.7\hat{z}$ T; the potentials differ by a gradient. (v) False — $B\propto1/\lvert z\rvert^3$.

## Medium

### 13.6 Parallel-plate line, find the error

> [!medium] Medium · find the error · current sheets · superposition
> A parallel-plate line is made of two thin metal strips of width $w = 4$ cm in the $z$ direction, very long in $x$, on the planes $y = 0$ and $y = d = 2$ mm in free space. The top strip ($y = d$) carries $I = 8$ A in the $+x$ direction and the bottom strip carries it back in the $-x$ direction. Treating both strips as infinite current sheets, a student writes:
>
> *"Each strip carries $K = I/w = 200$ A/m. With $\mathbf{H} = \tfrac12\mathbf{J}_s\times\hat{n}$ and $\hat{n} = \hat{y}$: top, $\tfrac12(200\hat{x})\times\hat{y} = 100\hat{z}$ A/m; bottom, $\tfrac12(-200\hat{x})\times\hat{y} = -100\hat{z}$ A/m. They cancel, so $\mathbf{H} = 0$ between the plates."*
>
> (a) What is wrong? Find $\mathbf{H}$ and $\mathbf{B}$ between the plates, and $\mathbf{H}$ above and below the line.
> (b) Check your answer with the boundary condition at the top plate.
> (c) If the gap is doubled and the current halved, by what factor does $B$ between the plates change?
>
> *Source: original.*

> [!hint]- Hint
> Mark a point between the plates. Is it above or below the *top* plate? $\hat{n}$ must point from each sheet toward that point.

> [!solution]- Solution
> **The slip.** $\hat{n}$ points from *each* sheet toward the field point, so it belongs to the sheet, not to the problem. A point between the plates lies *below* the top plate: there $\hat{n} = -\hat{y}$ for the top plate and $+\hat{y}$ for the bottom one. Using $\hat{n} = +\hat{y}$ for both describes a point *above* the whole line — the student has correctly computed the field above the line, where it does vanish.
>
> **(a)** Between the plates, with $\hat{x}\times\hat{y} = \hat{z}$:
> $$
> \mathbf{H} = \underbrace{\tfrac12(200\hat{x})\times(-\hat{y})}_{\text{top plate}}+\underbrace{\tfrac12(-200\hat{x})\times\hat{y}}_{\text{bottom plate}} = -100\hat{z}-100\hat{z} = -200\hat{z}\ \text{A/m},
> $$
> so $\mathbf{B} = \mu_0\mathbf{H} = -2.5133\times10^{-4}\hat{z}$ T, i.e. 251.3 μT along $-\hat{z}$. Above the line ($y>d$) both normals are $+\hat{y}$: $+100\hat{z}-100\hat{z} = 0$. Below it ($y<0$) both are $-\hat{y}$: $-100\hat{z}+100\hat{z} = 0$. Opposite currents add their fields between the plates and cancel outside: the field is trapped in the gap, as $\mathbf{E}$ is in a parallel-plate capacitor. Right-hand-rule cross-check: the top current runs along $+\hat{x}$ and the gap lies below it, so its field there points along $\hat{x}\times(-\hat{y}) = -\hat{z}$ ✓.
>
> **(b)** At the top plate take $\hat{n} = \hat{y}$, from the gap (region 2) into the space above (region 1):
> $$
> \hat{y}\times(\mathbf{H}_1-\mathbf{H}_2) = \hat{y}\times\big(0-(-200\hat{z})\big) = 200\,(\hat{y}\times\hat{z}) = 200\hat{x}\ \text{A/m},
> $$
> which is the top plate's surface current ✓. The student's answer ($\mathbf{H} = 0$ on both sides of the plate) has no jump at all — impossible for a sheet carrying 200 A/m.
>
> **(c)** $B = \mu_0K = \mu_0I/w$: the gap $d$ does not appear, because a sheet's field does not depend on distance. Doubling $d$ changes nothing and halving $I$ halves $K$, so $B$ changes by a factor of 0.50.
>
> **Check:** for real strips of finite width, adding up the fields of the strips' filaments gives the exact mid-gap value $B = \dfrac{2\mu_0K}{\pi}\arctan\dfrac{w}{d} = 0.9682\,\mu_0K = 2.4333\times10^{-4}$ T. The sheet model is high by only 3.3 %, because $w/d = 20$ is large.
>
> **Watch out:** "$\hat{n} = \hat{y}$ for both" is the most common sign slip with sheets. Draw the field point first, then write one $\hat{n}$ per sheet.
>
> **Answer.** The student used the top plate's normal for the wrong side. Between the plates $\mathbf{H} = -200\hat{z}$ A/m and $\mathbf{B} = -2.5133\times10^{-4}\hat{z}$ T (251.3 μT); $\mathbf{H} = 0$ above and below the line; the jump at the top plate is $200\hat{x}$ A/m $=\mathbf{J}_s$; $B$ changes by a factor of 0.50.

### 13.7 A slab with graded current

> [!medium] Medium · current slab · Ampère's law · superposition
> The slab $0<x<d$, with $d = 5$ cm and infinite in $y$ and $z$, carries the current density $\mathbf{J} = J_0\dfrac{x}{d}\hat{z}$ with $J_0 = 400$ A/m²; there is no current anywhere else. Free space.
> (a) Find the current per metre of width (along $y$), $K$.
> (b) Find $\mathbf{H}$ for all $x$.
> (c) Where is $\mathbf{H} = 0$? Explain why it is there and not at the centre of the slab.
> (d) Evaluate $H_y$ at $x = 1.25$, 2.5 and 4 cm.
>
> *Source: classic.*

> [!hint]- Hint
> Slice the slab into thin sheets $dK = J(x')\,dx'$. Each contributes $\tfrac12dK\,\hat{z}\times\hat{n}$, and you only need to know whether the slice lies to the left or to the right of the field point.

> [!solution]- Solution
> **Setup.** The current is along $\hat{z}$ and depends only on $x$, so $\mathbf{H} = H_y(x)\hat{y}$, as for any planar current. The layer between $x'$ and $x'+dx'$ is a sheet $dK\,\hat{z}$ with $dK = J(x')\,dx'$. If it lies to the left of the field point, $\hat{n} = +\hat{x}$ and its field is $\tfrac12dK\,(\hat{z}\times\hat{x}) = +\tfrac12dK\,\hat{y}$; if it lies to the right, $\hat{n} = -\hat{x}$ and its field is $-\tfrac12dK\,\hat{y}$.
>
> **(a)** $K = \displaystyle\int_0^dJ_0\frac{x'}{d}\,dx' = \frac{J_0d}{2} = \frac{400\times0.05}{2} = 10$ A/m.
>
> **(b)** Outside, every layer lies on the same side: $H_y = -K/2 = -5$ A/m for $x<0$ and $+5$ A/m for $x>d$. Inside, the layers left of $x$ push along $+\hat{y}$ and those right of $x$ along $-\hat{y}$:
> $$
> H_y(x) = \frac12\left[\int_0^xJ\,dx'-\int_x^dJ\,dx'\right] = \frac12\left[\frac{J_0x^2}{2d}-\left(\frac{J_0d}{2}-\frac{J_0x^2}{2d}\right)\right] = \frac{J_0x^2}{2d}-\frac{J_0d}{4},
> $$
> that is, $H_y = 4000x^2-5$ A/m with $x$ in metres.
>
> **(c)** $H_y = 0$ where $x^2 = d^2/2$: $x_0 = d/\sqrt2 = 3.5355$ cm. There the current to the left, $\int_0^{x_0}J\,dx = 5$ A/m, equals the current to the right, $\int_{x_0}^dJ\,dx = 5$ A/m, so their opposite fields cancel — the same reason $\mathbf{H} = 0$ on the midplane of a *uniform* slab. Here the current crowds toward $x = d$, so the balance point moves right of the centre; at $x = d/2$ the field is still $-2.5$ A/m.
>
> **(d)** $H_y(1.25\ \text{cm}) = -4.375$ A/m, $H_y(2.5\ \text{cm}) = -2.5$ A/m, $H_y(4\ \text{cm}) = +1.4$ A/m.
>
> **Check:** *continuity* — at $x = 0$ the inside formula gives $-5$ A/m and at $x = d$ it gives $J_0d/2-J_0d/4 = +5$ A/m, matching the outside values (no surface current, so no jump). *Curl* — $(\nabla\times\mathbf{H})_z = dH_y/dx = J_0x/d = J_z$ ✓; finite differences give 80, 240 and 360 A/m² at $x = 1$, 3 and 4.5 cm, equal to $J_z$ there. *Second route* — integrating $dH_y/dx = J_z$ from $H_y(0) = -K/2$ gives the same parabola.
>
> **Watch out:** "$\mathbf{H} = 0$ at the centre" comes from the odd symmetry of a slab that is symmetric about its midplane. This slab is not, so find the zero from the formula.
>
> **Answer.** (a) $K = 10$ A/m. (b) $\mathbf{H} = -5\hat{y}$ A/m for $x<0$; $\Big(\dfrac{J_0x^2}{2d}-\dfrac{J_0d}{4}\Big)\hat{y} = (4000x^2-5)\hat{y}$ A/m for $0<x<d$; $+5\hat{y}$ A/m for $x>d$. (c) $x_0 = d/\sqrt2 = 3.5355$ cm, where the current splits into equal halves. (d) $-4.375$, $-2.5$ and $+1.4$ A/m.

### 13.8 Three sheets in three directions

> [!medium] Medium · current sheets · superposition · boundary conditions
> Three infinite current sheets lie in free space: $\mathbf{J}_{s1} = 4\hat{x}$ A/m on $z = 0$, $\mathbf{J}_{s2} = 6\hat{y}$ A/m on $z = 1$ m, and an unknown $\mathbf{J}_{s3}$ on $z = 2$ m.
> (a) Find $\mathbf{J}_{s3}$ such that $\mathbf{H} = 0$ for $z>2$ m, and show that $\mathbf{H}$ then also vanishes for $z<0$.
> (b) Find $\mathbf{H}$ in $0<z<1$ m and in $1<z<2$ m, and $\lvert\mathbf{B}\rvert$ in each region.
> (c) Verify the boundary condition at each sheet.
>
> *Source: original.*

> [!hint]- Hint
> In each region you only need to know which sheets lie below the field point ($\hat{n} = +\hat{z}$) and which lie above it ($\hat{n} = -\hat{z}$). Alternatively, start where $\mathbf{H} = 0$ and cross the sheets one at a time: crossing a sheet upward changes $\mathbf{H}$ by $\mathbf{J}_s\times\hat{z}$.

> [!solution]- Solution
> **Setup.** Superpose $\tfrac12\mathbf{J}_s\times\hat{n}$, one term per sheet; the distance to each sheet does not matter. The products needed are $\hat{x}\times\hat{z} = -\hat{y}$ and $\hat{y}\times\hat{z} = \hat{x}$.
>
> **(a)** Above all three sheets every $\hat{n} = +\hat{z}$, and below all three every $\hat{n} = -\hat{z}$:
> $$
> \mathbf{H}(z>2) = \tfrac12\big(\mathbf{J}_{s1}+\mathbf{J}_{s2}+\mathbf{J}_{s3}\big)\times\hat{z},\qquad\mathbf{H}(z<0) = -\tfrac12\big(\mathbf{J}_{s1}+\mathbf{J}_{s2}+\mathbf{J}_{s3}\big)\times\hat{z}.
> $$
> The currents are all perpendicular to $\hat{z}$, so the first vanishes only if their sum vanishes: $\mathbf{J}_{s3} = -(4\hat{x}+6\hat{y})$ A/m. The same sum appears in the second expression, so $\mathbf{H} = 0$ below as well. Zero net current, no field outside — as for the two plates of 13.6.
>
> **(b)** For $0<z<1$ sheet 1 lies below the point and sheets 2 and 3 above it:
> $$
> \begin{aligned}
> \text{sheet 1: }&\tfrac12(4\hat{x})\times\hat{z} = 2\,(\hat{x}\times\hat{z}) = -2\hat{y}\\
> \text{sheet 2: }&\tfrac12(6\hat{y})\times(-\hat{z}) = -3\,(\hat{y}\times\hat{z}) = -3\hat{x}\\
> \text{sheet 3: }&\tfrac12(-4\hat{x}-6\hat{y})\times(-\hat{z}) = 2\,(\hat{x}\times\hat{z})+3\,(\hat{y}\times\hat{z}) = 3\hat{x}-2\hat{y}
> \end{aligned}
> $$
> The sum is $\mathbf{H} = -4\hat{y}$ A/m, so $\lvert\mathbf{B}\rvert = 4\mu_0 = 5.027$ μT. For $1<z<2$ sheet 2 now lies below, so its term flips to $+3\hat{x}$: $\mathbf{H} = -2\hat{y}+3\hat{x}+(3\hat{x}-2\hat{y}) = 6\hat{x}-4\hat{y}$ A/m, with $\lvert\mathbf{H}\rvert = \sqrt{52} = 7.2111$ A/m and $\lvert\mathbf{B}\rvert = 9.062$ μT. Sheets with currents in different directions make a field that changes direction from region to region.
>
> *Faster: march through the sheets.* Crossing a sheet upward, $\hat{z}\times\Delta\mathbf{H} = \mathbf{J}_s$, so $\Delta\mathbf{H} = \mathbf{J}_s\times\hat{z}$. Start from $\mathbf{H} = 0$ below: sheet 1 adds $4\hat{x}\times\hat{z} = -4\hat{y}$; sheet 2 adds $6\hat{y}\times\hat{z} = 6\hat{x}$, giving $6\hat{x}-4\hat{y}$; sheet 3 adds $(-4\hat{x}-6\hat{y})\times\hat{z} = -6\hat{x}+4\hat{y}$, back to zero ✓.
>
> **(c)** $\hat{z}\times(\mathbf{H}_{\text{above}}-\mathbf{H}_{\text{below}})$ at each sheet: at $z = 0$, $\hat{z}\times(-4\hat{y}) = 4\hat{x} = \mathbf{J}_{s1}$ ✓; at $z = 1$, $\hat{z}\times6\hat{x} = 6\hat{y} = \mathbf{J}_{s2}$ ✓; at $z = 2$, $\hat{z}\times(-6\hat{x}+4\hat{y}) = -4\hat{x}-6\hat{y} = \mathbf{J}_{s3}$ ✓.
>
> **Check:** a brute-force sum of the fields of the sheets' filaments at points in the four regions reproduces $0$, $-4\hat{y}$, $6\hat{x}-4\hat{y}$ and $0$ A/m.
>
> **Answer.** (a) $\mathbf{J}_{s3} = -4\hat{x}-6\hat{y}$ A/m, which makes $\mathbf{H} = 0$ both above and below the stack. (b) $\mathbf{H} = -4\hat{y}$ A/m ($\lvert\mathbf{B}\rvert = 5.027$ μT) for $0<z<1$ m; $\mathbf{H} = 6\hat{x}-4\hat{y}$ A/m ($\lvert\mathbf{H}\rvert = 7.2111$ A/m, $\lvert\mathbf{B}\rvert = 9.062$ μT) for $1<z<2$ m. (c) At each sheet the jump in tangential $\mathbf{H}$ equals that sheet's $\mathbf{J}_s$.

## Hard

### 13.9 Two opposite slabs and a sheet

> [!hard] Hard · current slabs · boundary conditions · vector potential
> Two slabs, infinite in $x$ and $y$, carry currents along $y$ in free space: slab 1 occupies $-3<z<-1$ m with $\mathbf{J} = 3\hat{y}$ A/m², and slab 2 occupies $0<z<4$ m with $\mathbf{J} = -1.5\hat{y}$ A/m².
> (a) Find $\mathbf{H}$ for all $z$.
> (b) A sheet $\mathbf{J}_s = -3\hat{y}$ A/m is added on the plane $z = 1$ m (inside slab 2). Find the new $\mathbf{H}$ for all $z$, and verify the boundary condition at the sheet.
> (c) Where is $\mathbf{H} = 0$, without and with the sheet?
> (d) Show that $\mathbf{A} = \tfrac32\mu_0\lvert z-1\rvert\,\hat{y}$ (in Wb/m, with $z$ in metres) is a vector potential of the sheet alone: check the Coulomb gauge, find $\mathbf{H}$ from $\mathbf{B} = \nabla\times\mathbf{A}$ on both sides of the sheet, and recover $\mathbf{J}_s$ from $\nabla^2\mathbf{A} = -\mu_0\mathbf{J}$.
>
> *Source: Summer 2019 HE2 #2a–b style (two current slabs plus a sheet; a vector potential proportional to $\lvert z\rvert$), re-parameterized.*

> [!hint]- Hint
> All currents are along $\pm\hat{y}$ and depend only on $z$, so $\mathbf{H} = H_x(z)\hat{x}$ and Ampère's law in point form becomes $dH_x/dz = J_y$. Find a region where you already know $H_x$, then integrate upward; a sheet adds a step $\mathbf{J}_s\times\hat{z}$.

> [!solution]- Solution
> **Setup.** The currents are along $\pm\hat{y}$ and depend only on $z$, so by the sheet symmetry $\mathbf{H} = H_x(z)\hat{x}$. Since $\hat{y}\times\hat{z} = \hat{x}$, a $+\hat{y}$ current makes a $+\hat{x}$ field above itself and a $-\hat{x}$ field below. In point form, $(\nabla\times\mathbf{H})_y = \partial H_x/\partial z-\partial H_z/\partial x = dH_x/dz = J_y$: inside a slab $H_x$ is a ramp of slope $J_y$.
>
> **(a)** *Building blocks.* Seen from outside, each slab is a sheet carrying $K = J\times$ thickness. Slab 1 has $K_1 = 3\times2 = 6$ A/m: below it $\tfrac12(6\hat{y})\times(-\hat{z}) = -3\hat{x}$, above it $\tfrac12(6\hat{y})\times\hat{z} = +3\hat{x}$, and inside a ramp of slope 3 through zero at its midplane, $H_x = 3(z+2)$. Slab 2 has $K_2 = -1.5\times4 = -6$ A/m: below it $\tfrac12(-6\hat{y})\times(-\hat{z}) = +3\hat{x}$, above it $-3\hat{x}$, and inside a ramp of slope $-1.5$ through zero at its midplane $z = 2$, $H_x = 3-1.5z$. Superposing region by region:
> $$
> H_x(z) = \begin{cases}
> -3+3 = 0, & z<-3\\
> 3(z+2)+3 = 3z+9, & -3<z<-1\\
> 3+3 = 6, & -1<z<0\\
> 3+(3-1.5z) = 6-1.5z, & 0<z<4\\
> 3-3 = 0, & z>4
> \end{cases}\qquad\text{(A/m)}.
> $$
> *Second route.* $K_1+K_2 = 0$, so $\mathbf{H} = 0$ below everything (as in 13.8(a)). Integrating $dH_x/dz = J_y$ upward: $H_x = 3(z+3)$ in slab 1, reaching 6 at $z = -1$; constant 6 across the gap; then $6-1.5z$ in slab 2, back to 0 at $z = 4$ ✓.
>
> **(b)** The sheet's own field is $\tfrac12(-3\hat{y})\times(-\hat{z}) = 1.5\,(\hat{y}\times\hat{z}) = +1.5\hat{x}$ A/m below $z = 1$ and $\tfrac12(-3\hat{y})\times\hat{z} = -1.5\hat{x}$ A/m above. Adding $+1.5$ below and $-1.5$ above:
> $$
> H_x(z) = \begin{cases}
> 1.5, & z<-3\\
> 3z+10.5, & -3<z<-1\\
> 7.5, & -1<z<0\\
> 7.5-1.5z, & 0<z<1\\
> 4.5-1.5z, & 1<z<4\\
> -1.5, & z>4
> \end{cases}\qquad\text{(A/m)}.
> $$
> At $z = 1$, $H_x$ drops from 6 to 3 A/m. With $\hat{n} = \hat{z}$ from region 2 (below) into region 1 (above): $\hat{z}\times(\mathbf{H}_1-\mathbf{H}_2) = \hat{z}\times(-3\hat{x}) = -3\hat{y}$ A/m $=\mathbf{J}_s$ ✓. At the slab faces $z = -3$, $-1$, $0$ and $4$ the field is continuous (1.5, 7.5, 7.5 and $-1.5$ A/m from both sides), as it must be with no surface current there.
>
> **(c)** Without the sheet, $\mathbf{H} = 0$ everywhere below and above the pair of slabs ($z<-3$ and $z>4$) and nowhere between, gap included: $3z+9$, $6$ and $6-1.5z$ are all positive for $-3<z<4$. With the sheet: $3z+10.5$ would vanish only at $z = -3.5$, outside slab 1; $7.5$ and $7.5-1.5z\ge6$ never vanish; $4.5-1.5z = 0$ at $z = 3$ m, which does lie in $1<z<4$; and outside the field is $\pm1.5$ A/m. So $\mathbf{H} = 0$ only on the plane $z = 3$ m.
>
> **(d)** Here $\mathbf{A} = A_y(z)\hat{y}$ with $A_y = \tfrac32\mu_0\lvert z-1\rvert$.
>
> *Gauge.* $\nabla\cdot\mathbf{A} = \partial A_y/\partial y = 0$ ✓.
>
> *Field.* With only $A_y(z)$ present,
> $$
> \nabla\times\mathbf{A} = \hat{x}\Big(\frac{\partial A_z}{\partial y}-\frac{\partial A_y}{\partial z}\Big)+\hat{z}\Big(\frac{\partial A_y}{\partial x}-\frac{\partial A_x}{\partial y}\Big) = -\frac{dA_y}{dz}\,\hat{x} = -\tfrac32\mu_0\operatorname{sgn}(z-1)\,\hat{x},
> $$
> so $\mathbf{H} = \mathbf{B}/\mu_0 = +1.5\hat{x}$ A/m below $z = 1$ and $-1.5\hat{x}$ A/m above — exactly the sheet's field from (b). Finite-difference curls at $z = -0.6$ m and $z = 2.3$ m give $\mathbf{B} = +1.885\times10^{-6}\hat{x}$ T and $-1.885\times10^{-6}\hat{x}$ T.
>
> *Current.* The slope $dA_y/dz = \tfrac32\mu_0\operatorname{sgn}(z-1)$ jumps by $3\mu_0 = 3.7699\times10^{-6}$ Wb/m² at $z = 1$, so $\nabla^2A_y = d^2A_y/dz^2 = 3\mu_0\,\delta(z-1)$. Then $\nabla^2\mathbf{A} = -\mu_0\mathbf{J}$ gives $J_y = -3\,\delta(z-1)$ A/m², which is a sheet $\mathbf{J}_s = -3\hat{y}$ A/m on $z = 1$ ✓.
>
> **Check:** the slopes inside the slabs equal $J_y$ — $dH_x/dz = +3$ in slab 1 and $-1.5$ in slab 2, by finite differences at four points; superposing thin sheets $dK = J\,dz'$ numerically reproduces the piecewise $H_x$ of (a) and (b); and the outside values $\pm1.5$ A/m are those of a single sheet carrying the net current $6-6-3 = -3$ A/m.
>
> **Watch out:** a sheet *inside* a slab still makes a full step of $\lvert J_s\rvert$; on either side of it the slab's ramp continues with the same slope.
>
> **Answer.** (a) $\mathbf{H} = H_x\hat{x}$ with $H_x = 0$ for $z<-3$, $3z+9$ for $-3<z<-1$, $6$ for $-1<z<0$, $6-1.5z$ for $0<z<4$ and $0$ for $z>4$ (A/m, $z$ in m). (b) $H_x = 1.5$, $3z+10.5$, $7.5$, $7.5-1.5z$ ($0<z<1$), $4.5-1.5z$ ($1<z<4$) and $-1.5$ ($z>4$); the step at $z = 1$ satisfies $\hat{z}\times\Delta\mathbf{H} = -3\hat{y}$ A/m $=\mathbf{J}_s$. (c) Without the sheet $\mathbf{H} = 0$ for $z<-3$ m and for $z>4$ m; with it, only on the plane $z = 3$ m. (d) $\nabla\cdot\mathbf{A} = 0$; $\mathbf{H} = +1.5\hat{x}$ A/m below and $-1.5\hat{x}$ A/m above $z = 1$; $\mathbf{J}_s = -3\hat{y}$ A/m.

### 13.10 Vector potentials of wire and solenoid

> [!hard] Hard · vector potential · Stokes' theorem · solenoid
> (a) A long straight wire on the $z$ axis carries $I = 10$ A in the $+z$ direction. Show that $\mathbf{A} = \dfrac{\mu_0I}{2\pi}\ln\dfrac{r_0}{r}\,\hat{z}$ ($r_0$ any fixed length) satisfies $\nabla\cdot\mathbf{A} = 0$ and $\nabla^2\mathbf{A} = 0$ for $r>0$ and gives the correct $\mathbf{B}$. Evaluate $\mathbf{B}$ at $(x,y,z) = (3, 4, 0)$ cm.
> (b) Find the magnetic flux through the rectangle in the plane $y = 0$ with corners $(x,z) = (1\ \text{cm}, 0)$, $(1\ \text{cm}, 1\ \text{m})$, $(4\ \text{cm}, 1\ \text{m})$, $(4\ \text{cm}, 0)$, oriented by traversing the corners in that order — first as $\oint\mathbf{A}\cdot d\mathbf{l}$, then as $\int\mathbf{B}\cdot d\mathbf{S}$. Why does $r_0$ not matter?
> (c) A long solenoid of radius $R = 1$ cm on the $z$ axis has $n = 1000$ turns/m carrying $I = 2$ A counter-clockwise seen from $+z$, so $\mathbf{B} = B_0\hat{z}$ inside with $B_0 = \mu_0nI$. Show that $\mathbf{A} = \tfrac12B_0r\,\hat\phi$ for $r<R$ and $\mathbf{A} = \dfrac{B_0R^2}{2r}\hat\phi$ for $r>R$ gives the right $\mathbf{B}$ everywhere, is in the Coulomb gauge, and is continuous at $r = R$.
> (d) Evaluate $\mathbf{A}$ at $r = 2R$, where $\mathbf{B} = 0$, and compute $\oint\mathbf{A}\cdot d\mathbf{l}$ around a circle of any radius $r>R$. Is a non-zero $\mathbf{A}$ where $\mathbf{B} = 0$ a contradiction?
>
> *Source: classic.*

> [!hint]- Hint
> In cylindrical components, $\nabla\times(A_z(r)\hat{z}) = -\dfrac{dA_z}{dr}\hat\phi$ and $\nabla\times(A_\phi(r)\hat\phi) = \dfrac1r\dfrac{d(rA_\phi)}{dr}\hat{z}$. For the flux, Stokes' theorem turns $\int(\nabla\times\mathbf{A})\cdot d\mathbf{S}$ into $\oint\mathbf{A}\cdot d\mathbf{l}$.

> [!solution]- Solution
> **Setup.** $\mathbf{A}$ follows the current: the Coulomb integral $\int\mu_0\mathbf{J}\,dV'/(4\pi\lvert\mathbf{r}-\mathbf{r}'\rvert)$ adds up vectors parallel to $\mathbf{J}$, so a wire along $\hat{z}$ has $\mathbf{A}\parallel\hat{z}$ and a winding with $\mathbf{J}_s\parallel\hat\phi$ has $\mathbf{A}\parallel\hat\phi$. And by Stokes' theorem $\oint_C\mathbf{A}\cdot d\mathbf{l} = \int_S\mathbf{B}\cdot d\mathbf{S} = \Psi$: the circulation of $\mathbf{A}$ is the flux, just as the circulation of $\mathbf{H}$ is the current.
>
> **(a)** In Cartesian form $A_z = \dfrac{\mu_0I}{2\pi}\ln\dfrac{r_0}{\sqrt{x^2+y^2}}$, so
> $$
> B_x = \frac{\partial A_z}{\partial y} = -\frac{\mu_0I}{2\pi}\frac{y}{r^2},\qquad B_y = -\frac{\partial A_z}{\partial x} = \frac{\mu_0I}{2\pi}\frac{x}{r^2},\qquad B_z = 0,
> $$
> i.e. $\mathbf{B} = \dfrac{\mu_0I}{2\pi r}\cdot\dfrac{-y\hat{x}+x\hat{y}}{r} = \dfrac{\mu_0I}{2\pi r}\hat\phi$, the wire's field from Lecture 12 ✓. $\nabla\cdot\mathbf{A} = \partial A_z/\partial z = 0$ ✓. For $r>0$, $\nabla^2A_z = \dfrac1r\dfrac{d}{dr}\Big(r\dfrac{dA_z}{dr}\Big) = \dfrac1r\dfrac{d}{dr}\Big(-\dfrac{\mu_0I}{2\pi}\Big) = 0$ ✓: there is no current off the axis. All of it sits on the axis: around any circle $\oint\dfrac{\partial A_z}{\partial r}\,dl = -\dfrac{\mu_0I}{2\pi r}\cdot2\pi r = -\mu_0I$, so $\nabla^2A_z = -\mu_0I\,\delta(x)\delta(y) = -\mu_0J_z$.
>
> At $(3, 4, 0)$ cm: $r = 5$ cm and $\hat\phi = (-y\hat{x}+x\hat{y})/r = -0.8\hat{x}+0.6\hat{y}$. With $\mu_0I/(2\pi) = 2\times10^{-6}$ T·m, $B = 2\times10^{-6}/0.05$ T $= 40$ μT, so $\mathbf{B} = 40(-0.8\hat{x}+0.6\hat{y})$ μT $= (-32\hat{x}+24\hat{y})$ μT.
>
> **(b)** Traversing up the side $x = 1$ cm, out along the top and down the side $x = 4$ cm gives, by the right-hand rule, the normal $\hat{z}\times\hat{x} = \hat{y}$, which at $y = 0$, $x>0$ is $+\hat\phi$ — the direction of $\mathbf{B}$, so the flux is positive. $\mathbf{A}\parallel\hat{z}$, so the horizontal sides contribute nothing. With $a = 1$ cm and $b = 4$ cm,
> $$
> \Psi = \oint\mathbf{A}\cdot d\mathbf{l} = \big[A_z(a)-A_z(b)\big](1\ \text{m}) = \frac{\mu_0I}{2\pi}\ln\frac{b}{a}\,(1\ \text{m}) = 2\times10^{-6}\ln4\ \text{Wb} = 2.772589\times10^{-6}\ \text{Wb},
> $$
> about 2.77 μWb. Directly, $\displaystyle\int_a^b\frac{\mu_0I}{2\pi r}(1\ \text{m})\,dr$ gives the same ✓. The constant $r_0$ cancels in $A_z(a)-A_z(b)$: it is the reference of $\mathbf{A}$, like the reference radius of $V$ for an infinite line charge, whose $V$ itself diverges. For a finite wire the Coulomb integral gives an $A_z(a)$ that keeps growing with length ($1.5202\times10^{-5}$ Wb/m for half-length 10 m, $2.4412\times10^{-5}$ Wb/m for half-length 1 km), while $A_z(a)-A_z(b)$ stays put ($2.772581\times10^{-6}$ and $2.772589\times10^{-6}$ Wb/m).
>
> **(c)** *Derivation by Stokes* (Ampère's law for $\mathbf{A}$): by symmetry $\mathbf{A} = A_\phi(r)\hat\phi$, and around a circle of radius $r$, $2\pi rA_\phi = \Psi_{\text{enc}}$:
> $$
> r<R:\ 2\pi rA_\phi = B_0\pi r^2\ \Rightarrow\ A_\phi = \tfrac12B_0r;\qquad r>R:\ 2\pi rA_\phi = B_0\pi R^2\ \Rightarrow\ A_\phi = \frac{B_0R^2}{2r}.
> $$
> *Verification.* Inside, $\dfrac1r\dfrac{d}{dr}\big(r\cdot\tfrac12B_0r\big) = B_0$ ✓ (in Cartesian form $\mathbf{A} = \tfrac12B_0(-y\hat{x}+x\hat{y}) = \tfrac12\mathbf{B}\times\mathbf{r}$, the $\mathbf{A}_1$ of 13.5(iv)). Outside, $\dfrac1r\dfrac{d}{dr}\big(\tfrac12B_0R^2\big) = 0$ ✓. In both regions $\nabla\cdot\mathbf{A} = \dfrac1r\dfrac{\partial A_\phi}{\partial\phi} = 0$ ✓. At $r = R$ both forms give $\tfrac12B_0R$: with $B_0 = \mu_0nI = 2.51327\times10^{-3}$ T, $A_\phi(R) = 1.25664\times10^{-5}$ Wb/m from either side ✓.
>
> **(d)** $A_\phi(2R) = \dfrac{B_0R}{4} = 6.28319\times10^{-6}$ Wb/m, along $\hat\phi$, although $\mathbf{B} = 0$ there. Around any circle with $r>R$:
> $$
> \oint\mathbf{A}\cdot d\mathbf{l} = \frac{B_0R^2}{2r}\cdot2\pi r = B_0\pi R^2 = 7.89568\times10^{-7}\ \text{Wb},
> $$
> the flux inside the solenoid, whatever $r$ is. No contradiction: $\mathbf{B}$ is built from the *derivatives* of $\mathbf{A}$, and the $1/r$ profile is curl-free — exactly like $\mathbf{H} = \dfrac{I}{2\pi r}\hat\phi$ outside a wire, which circulates around a current it never touches. A circle around the solenoid encloses flux, so $\mathbf{A}$ must circulate along it.
>
> **Check:** the Coulomb integral $\int\mu_0\mathbf{J}_s\,dS'/(4\pi\lvert\mathbf{r}-\mathbf{r}'\rvert)$ for a very long finite solenoid, evaluated numerically, gives $A_\phi = 6.28319\times10^{-6}$, $1.25664\times10^{-5}$, $6.28319\times10^{-6}$ and $3.14159\times10^{-6}$ Wb/m at $r = 0.5$, 1, 2 and 4 cm, matching the two formulas; finite-difference curls give $\mathbf{B} = 0.002513\hat{z}$ T inside and $0$ outside.
>
> **Answer.** (a) $\nabla\cdot\mathbf{A} = 0$, $\nabla^2A_z = 0$ for $r>0$, $\mathbf{B} = \dfrac{\mu_0I}{2\pi r}\hat\phi$; at $(3,4,0)$ cm, $\mathbf{B} = (-32\hat{x}+24\hat{y})$ μT, magnitude 40 μT. (b) $\Psi = \dfrac{\mu_0I}{2\pi}\ln4\,(1\ \text{m}) = 2.772589\times10^{-6}$ Wb by both routes; $r_0$ cancels in the difference. (c) $\mathbf{B} = B_0\hat{z}$ inside and $0$ outside, $\nabla\cdot\mathbf{A} = 0$, and $A_\phi(R) = 1.25664\times10^{-5}$ Wb/m from both sides. (d) $\mathbf{A}(2R) = 6.28319\times10^{-6}\hat\phi$ Wb/m; $\oint\mathbf{A}\cdot d\mathbf{l} = B_0\pi R^2 = 7.89568\times10^{-7}$ Wb for every $r>R$; no contradiction.

### 13.11 Helmholtz coils and the far field

> [!hard] Hard · current loop · Helmholtz coils · magnetic dipole
> A flat circular coil of $N = 50$ turns and radius $a = 20$ cm carries $I = 2$ A, counter-clockwise seen from $+z$. Free space.
> (a) With the coil in the plane $z = 0$, find $B$ on its axis at $z = 0$, 10 cm and 30 cm.
> (b) Two such coils, coaxial and with currents in the same sense, are placed in the planes $z = -a/2$ and $z = +a/2$ (a Helmholtz pair). Show that the field at the midpoint is $(4/5)^{3/2}\mu_0NI/a$, and evaluate it.
> (c) Show that $dB_z/dz$ and $d^2B_z/dz^2$ both vanish at the midpoint. Compare how much the field drops 2 cm from the midpoint with how much it drops 2 cm from the centre of a single coil.
> (d) Far away the pair acts as a magnetic dipole of moment $m = 2NI\pi a^2$. Compare the exact on-axis field at $z = 2$ m and 4 m with $\mu_0m/(2\pi z^3)$, and check the $1/z^3$ law.
>
> *Source: classic.*

> [!hint]- Hint
> Each coil contributes the on-axis loop field $\dfrac{\mu_0NIa^2}{2(a^2+s^2)^{3/2}}$, with $s$ the distance from that coil's plane. For (c), differentiate this single-coil function twice before adding the two shifted copies.

> [!solution]- Solution
> **Setup.** On the axis of one coil, at distance $s$ from its plane, $\mathbf{B} = \dfrac{\mu_0NIa^2}{2(a^2+s^2)^{3/2}}\hat{z}$ — the loop result of Lecture 13 times $N$, along $+\hat{z}$ for current counter-clockwise seen from $+z$. For two coils on the same axis, add, each with its own $s$.
>
> **(a)** At the centre,
> $$
> B = \frac{\mu_0NI}{2a} = \frac{4\pi\times10^{-7}\times50\times2}{2\times0.2}\ \text{T} = \pi\times10^{-4}\ \text{T} = 0.314159\ \text{mT}.
> $$
> At $z = 10$ cm the formula gives 0.2248 mT, and at $z = 30$ cm 0.05362 mT, all along $+\hat{z}$.
>
> **(b)** Each coil is $a/2$ from the midpoint:
> $$
> B(0) = 2\cdot\frac{\mu_0NIa^2}{2\big(a^2+a^2/4\big)^{3/2}} = \frac{\mu_0NIa^2}{(5/4)^{3/2}a^3} = \Big(\frac45\Big)^{3/2}\frac{\mu_0NI}{a} = 0.71554\times6.28319\times10^{-4}\ \text{T} = 4.495881\times10^{-4}\ \text{T},
> $$
> about 0.4496 mT along $+\hat{z}$.
>
> **(c)** Write $f(s) = \dfrac{\mu_0NIa^2}{2(a^2+s^2)^{3/2}}$, so that $B(z) = f(z-a/2)+f(z+a/2)$. Since $f$ is even, $f'$ is odd and $B'(0) = f'(-a/2)+f'(a/2) = 0$; in fact $B(z)$ is even, so every odd derivative vanishes at the midpoint. Differentiating twice,
> $$
> f''(s) = \frac{3\mu_0NIa^2}{2}\cdot\frac{4s^2-a^2}{(a^2+s^2)^{7/2}},\qquad B''(0) = 2f''(a/2) = 0\quad\text{because}\quad4\Big(\frac a2\Big)^2-a^2 = 0.
> $$
> That is the point of the spacing $a$: it removes the curvature, so the first correction is of fourth order in $z$. Numerically, 2 cm from the midpoint the pair's field is lower by only 0.0114 %, while 2 cm from the centre of a single coil (where $B'' = -2.356\times10^{-2}$ T/m²) the field is lower by 1.481 %.
>
> **(d)** $m = 2NI\pi a^2 = 2\times50\times2\times\pi\times0.04 = 8\pi\approx25.13$ A·m². The exact field (sum of the two coil formulas, $z$ measured from the midpoint) against the dipole field:
> $$
> \begin{aligned}
> z = 2\ \text{m}:&\quad B = 6.281448\times10^{-7}\ \text{T},\quad\frac{\mu_0m}{2\pi z^3} = 6.283185\times10^{-7}\ \text{T},\quad\text{ratio }0.999724\\
> z = 4\ \text{m}:&\quad B = 7.853844\times10^{-8}\ \text{T},\quad\frac{\mu_0m}{2\pi z^3} = 7.853982\times10^{-8}\ \text{T},\quad\text{ratio }0.999982
> \end{aligned}
> $$
> and $B(2\ \text{m})/B(4\ \text{m}) = 7.99793\approx2^3$: inverse cube ✓.
>
> **Check:** a direct Biot–Savart sum over the discretized coils reproduces the on-axis values (0.4496 mT at the midpoint, $6.281447\times10^{-7}$ T at 2 m), and $\mu_0NI/a$ has units of T ✓. A bonus: one coil at the same relative distance, $z = 10a$, has exact/dipole $= 0.98519$, so the pair is much closer to its dipole value. A pair with spacing $s$ deviates from the dipole law by the factor $1+\tfrac32\big((s/a)^2-1\big)(a/z)^2$ to leading order, so the Helmholtz spacing $s = a$ also cancels the leading far-field correction.
>
> **Answer.** (a) $B = \pi\times10^{-4}$ T $= 0.314159$ mT, 0.2248 mT and 0.05362 mT, along $+\hat{z}$. (b) $B = (4/5)^{3/2}\mu_0NI/a = 4.495881\times10^{-4}$ T $\approx0.4496$ mT. (c) $B' = B'' = 0$ at the midpoint; 2 cm away the field drops by 0.0114 % for the pair and by 1.481 % for one coil. (d) $m = 8\pi\approx25.13$ A·m²; exact/dipole $= 0.999724$ at 2 m and 0.999982 at 4 m; $B(2\ \text{m})/B(4\ \text{m}) = 7.99793\approx8$.

### 13.12 A finite solenoid on its axis

> [!hard] Hard · finite solenoid · superposition · magnetic dipole
> A solenoid of length $\ell = 30$ cm and radius $a = 3$ cm is centred at the origin with its axis along $z$. Its $N = 600$ closely spaced turns carry $I = 1.5$ A, counter-clockwise seen from $+z$. Free space.
> (a) Treat the winding as a stack of loops — a slice $dz'$ holds $n\,dz'$ turns, with $n = N/\ell$ — and integrate the loop's on-axis field to find $B_z(z)$ on the axis.
> (b) Evaluate $B$ at the centre and at an end ($z = \ell/2$), and compare both with $\mu_0nI$. Explain why the end value is close to one half.
> (c) How long must a solenoid be, as a multiple of its radius, for its centre field to be within 1 % of $\mu_0nI$?
> (d) Far away on the axis the solenoid acts as a dipole of moment $m = NI\pi a^2$. Compare the exact field with $\mu_0m/(2\pi z^3)$ at $z = 1.5$ m and 3 m.
>
> *Source: classic.*

> [!hint]- Hint
> The slice at $z'$ is a loop carrying $nI\,dz'$ at axial distance $z-z'$ from the field point. With $u = z'-z$ you need $\displaystyle\int\frac{a^2\,du}{(a^2+u^2)^{3/2}} = \frac{u}{\sqrt{a^2+u^2}}$.

> [!solution]- Solution
> **Setup.** The slice between $z'$ and $z'+dz'$ is a loop of radius $a$ carrying $nI\,dz'$. On the axis it adds
> $$
> dB_z = \frac{\mu_0\,nI\,dz'\,a^2}{2\big[a^2+(z-z')^2\big]^{3/2}}
> $$
> along $+\hat{z}$ (current counter-clockwise seen from $+z$). Superpose all slices from $z' = -\ell/2$ to $z' = \ell/2$.
>
> **(a)** With $u = z'-z$,
> $$
> B_z(z) = \frac{\mu_0nI}{2}\left[\frac{u}{\sqrt{a^2+u^2}}\right]_{u=-\ell/2-z}^{u=\ell/2-z} = \frac{\mu_0nI}{2}\left[\frac{\ell/2-z}{\sqrt{a^2+(\ell/2-z)^2}}+\frac{\ell/2+z}{\sqrt{a^2+(\ell/2+z)^2}}\right].
> $$
> Each term is $\cos\alpha$, with $\alpha$ the angle between the axis and the line from the field point to the rim of one end; for an infinitely long coil both terms are 1 and $B = \mu_0nI$ ✓.
>
> **(b)** $n = 600/0.3 = 2000$ turns/m and $\mu_0nI = 3.76991\times10^{-3}$ T. At the centre, with $\ell/2 = 15$ cm and $a = 3$ cm,
> $$
> B(0) = \mu_0nI\,\frac{\ell/2}{\sqrt{a^2+(\ell/2)^2}} = \mu_0nI\,\frac{15}{\sqrt{15^2+3^2}} = \frac{5}{\sqrt{26}}\,\mu_0nI = 0.980581\,\mu_0nI = 3.69670\times10^{-3}\ \text{T}.
> $$
> At the end the first term is 0 and the second is $\ell/\sqrt{a^2+\ell^2}$:
> $$
> B(\ell/2) = \frac{\mu_0nI}{2}\cdot\frac{30}{\sqrt{30^2+3^2}} = \frac12\cdot\frac{10}{\sqrt{101}}\,\mu_0nI = 0.497519\,\mu_0nI = 1.87560\times10^{-3}\ \text{T},
> $$
> so $B(\text{end})/B(\text{centre}) = 0.50737$. **Why one half:** two semi-infinite solenoids placed end to end make an infinite one, with $\mu_0nI$ at the joint, and by symmetry each supplies half of it. The end of a long coil sees, very nearly, a semi-infinite coil on one side and nothing on the other; for a very long coil the formula gives $0.500000\,\mu_0nI$ at the end.
>
> **(c)** At the centre $B/(\mu_0nI) = \dfrac{x}{\sqrt{x^2+1}}$ with $x = \ell/(2a)$. Requiring this to be at least 0.99: $x^2\ge(0.99)^2(x^2+1)$, so $x\ge0.99/\sqrt{1-0.99^2} = 0.99/\sqrt{0.0199}$ and
> $$
> \frac{\ell}{a}\ge\frac{1.98}{\sqrt{0.0199}} = 14.0358 .
> $$
> This coil has $\ell/a = 10$, which is why its centre field is 1.9 % below $\mu_0nI$.
>
> **(d)** For $z\gg\ell$ and $z\gg a$, every slice is at distance $\approx z$, so $B\approx\dfrac{\mu_0nI\ell a^2}{2z^3} = \dfrac{\mu_0NIa^2}{2z^3} = \dfrac{\mu_0m}{2\pi z^3}$, with $m = NI\pi a^2 = 0.81\pi = 2.54469$ A·m². Exact versus dipole:
> $$
> \begin{aligned}
> z = 1.5\ \text{m}:&\quad B = 1.53763\times10^{-7}\ \text{T},\quad\frac{\mu_0m}{2\pi z^3} = 1.50796\times10^{-7}\ \text{T},\quad\text{ratio }1.01967\\
> z = 3\ \text{m}:&\quad B = 1.89413\times10^{-8}\ \text{T},\quad\frac{\mu_0m}{2\pi z^3} = 1.88496\times10^{-8}\ \text{T},\quad\text{ratio }1.00487
> \end{aligned}
> $$
> The exact field is a little *higher* because $1/z^3$ is steep: the turns in the near half of the 30-cm coil gain more than those in the far half lose; the excess shrinks as $z$ grows — the dipole law is a far-field statement.
>
> **Check:** a direct Biot–Savart sum over 600 discrete rings gives $3.696702\times10^{-3}$ T at the centre and $1.875601\times10^{-3}$ T at the end, matching (a), and integrating the loop formula numerically over $z'$ gives the same. Limits: as $\ell\to\infty$ the formula gives $\mu_0nI$ at the centre and $\tfrac12\mu_0nI$ at the ends, as stated in Lecture 13.
>
> **Answer.** (a) $B_z(z) = \dfrac{\mu_0nI}{2}\Big[\dfrac{\ell/2-z}{\sqrt{a^2+(\ell/2-z)^2}}+\dfrac{\ell/2+z}{\sqrt{a^2+(\ell/2+z)^2}}\Big]$ along $+\hat{z}$. (b) With $\mu_0nI = 3.76991\times10^{-3}$ T: $B(0) = 0.980581\,\mu_0nI = 3.69670\times10^{-3}$ T and $B(\ell/2) = 0.497519\,\mu_0nI = 1.87560\times10^{-3}$ T (ratio 0.50737). (c) $\ell/a\ge14.0358$. (d) $m = 0.81\pi = 2.54469$ A·m²; exact/dipole $= 1.01967$ at 1.5 m and 1.00487 at 3 m.

### Sources for this page
Course notes and slides for Lecture 13 supply the methods: the sheet rule $\mathbf{H} = \tfrac12\mathbf{J}_s\times\hat{n}$, the slab ramp, the solenoid, the vector potential with its gauge freedom, and the loop's on-axis field with its dipole limit. Old exams, re-parameterized: the nested solenoids of 13.3 (Summer 2017 HE2 #1b and Summer 2020 HE2 #2b) and the two current slabs, added sheet and vector potential of 13.9 (Summer 2019 HE2 #2a–b), which also extends the worked problem [[problems/current-slab-and-sheet-by-amperes-law]] to two opposite slabs with a sheet inside one of them. Classic textbook problems, reworded with new numbers: the toroid (13.4), the graded slab (13.7), the vector potentials of a wire and a solenoid (13.10), the Helmholtz pair (13.11) and the finite solenoid (13.12). Problems 13.1, 13.2, 13.5, 13.6 and 13.8 are original.

*Previous: [[practice/12-magnetic-force-biot-savart-and-ampere|Lecture 12 practice]] · next: [[practice/14-faradays-law-and-induced-emf|Lecture 14 practice]] · [[practice/index|all practice]]*
