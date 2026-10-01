---
title: "Practice — Lecture 6: Circulation and boundary conditions"
description: "12 practice problems (5 easy, 3 medium, 4 hard) on circulation and KVL, Stokes' theorem on a loop, the four boundary conditions at charged and uncharged dielectric interfaces, tilted interfaces, refraction of field lines, conductor surfaces, current sheets and bound surface charge, each with a worked solution and folded hints."
tags: [practice, electrostatics, exam-1]
lecture: 6
---

*Practice for [[1-electrostatics/06-circulation-and-boundary-conditions|Lecture 6]] · concepts: [[concepts/boundary-conditions]] · [[concepts/conservative-field]] · [[concepts/stokes-theorem]] · [[concepts/conductors]] · all practice: [[practice/index|hub]] · by difficulty: [[practice/easy|easy]] · [[practice/medium|medium]] · [[practice/hard|hard]] · [[practice/topics|by topic]]*

Work each problem on paper first. Open the **hint** only when stuck, and the **solution** only after you have an answer you would hand in. Every answer here has been checked numerically.

## Easy

### 6.1 What is always continuous

> [!easy] Easy · multiple choice · boundary conditions
> A flat interface separates two dielectrics, $\epsilon_1 = 2\epsilon_0$ (medium 1) and $\epsilon_2 = 5\epsilon_0$ (medium 2), and carries a free surface charge $\rho_s\neq0$. Static fields are present on both sides. Which of these quantities must have the same value on the two sides of the interface, right at it, whatever the fields are?
>
> (a) the normal component of $\mathbf{E}$
>
> (b) the normal component of $\mathbf{D}$
>
> (c) the tangential component of $\mathbf{E}$
>
> (d) the tangential component of $\mathbf{D}$
>
> (e) the magnitude $\lvert\mathbf{E}\rvert$
>
> Follow-up: which answers change if $\rho_s = 0$?
>
> *Source: original.*

> [!solution]- Solution
> **(c).** A thin loop hugging the interface has zero circulation, and only its two long edges contribute, so $\hat{n}\times(\mathbf{E}_1-\mathbf{E}_2) = 0$ at *every* interface, charged or not, whatever the materials.
>
> To see the others fail, take one concrete case: $\hat{n} = \hat{z}$ (from medium 2 into medium 1), $\rho_s = 4\epsilon_0$ C/m² and $\mathbf{E}_2 = 1.3\hat{x}-0.7\hat{y}+2.1\hat{z}$ V/m. Then $\mathbf{E}_{1t} = 1.3\hat{x}-0.7\hat{y}$ V/m, and the pillbox condition $2\epsilon_0E_{1z}-5\epsilon_0(2.1) = 4\epsilon_0$ gives $E_{1z} = 7.25$ V/m.
>
> - (a) is wrong: $E_{1z}-E_{2z} = 5.15$ V/m. In general normal $\mathbf{E}$ jumps at a charged surface (think of a conductor: field outside, zero inside).
> - (b) is wrong: normal $\mathbf{D}$ jumps by exactly the free charge, $\hat{n}\cdot(\mathbf{D}_1-\mathbf{D}_2) = \rho_s = 4\epsilon_0$.
> - (d) is wrong: $\mathbf{D}_t = \epsilon\mathbf{E}_t$ with $\mathbf{E}_t$ common to both sides, so $D_{1t}/D_{2t} = \epsilon_1/\epsilon_2 = 2/5$.
> - (e) is wrong: the normal component changes while the tangential part does not, so in general the magnitudes differ; here $\lvert\mathbf{E}_1\rvert = 7.40$ V/m against $\lvert\mathbf{E}_2\rvert = 2.57$ V/m.
>
> **Follow-up:** with $\rho_s = 0$, (b) becomes true as well. (a) is still false: $\epsilon_1E_{1n} = \epsilon_2E_{2n}$ gives $E_{1n}/E_{2n} = \epsilon_2/\epsilon_1 = 2.5$. (d) and (e) stay false.
>
> **Answer.** (c) only. With $\rho_s = 0$: (b) and (c).

### 6.2 Kirchhoff around a triangle

> [!easy] Easy · circulation · KVL
> In free space the field is uniform, $\mathbf{E} = 3\hat{x}+4\hat{y}-2\hat{z}$ V/m. Take the triangle with corners $P_1 = (0,0,0)$, $P_2 = (2,0,0)$ and $P_3 = (2,3,0)$ m, traversed $P_1\to P_2\to P_3\to P_1$.
>
> (a) Compute $\int\mathbf{E}\cdot d\mathbf{l}$ along each side, and the circulation.
>
> (b) Find $V(P_3)-V(P_1)$, once through $P_2$ and once along the slanted side.
>
> *Source: original.*

> [!solution]- Solution
> **(a)** On each straight side, $d\mathbf{l}$ points along the side and the limits walk it in the direction of travel. The triangle lies in the plane $z = 0$, so $d\mathbf{l}$ has no $z$ part and $E_z$ never contributes.
>
> - $P_1\to P_2$: $d\mathbf{l} = \hat{x}\,dx$, $x$ from 0 to 2: $\int_0^2 3\,dx = 6$ V.
> - $P_2\to P_3$: $d\mathbf{l} = \hat{y}\,dy$, $y$ from 0 to 3: $\int_0^3 4\,dy = 12$ V.
> - $P_3\to P_1$: $\mathbf{r} = P_3+t(P_1-P_3)$, so $d\mathbf{l} = (-2\hat{x}-3\hat{y})\,dt$ with $t$ from 0 to 1, and $\mathbf{E}\cdot d\mathbf{l} = [3(-2)+4(-3)]\,dt = -18\,dt$: the side gives $-18$ V.
>
> Circulation: $6+12-18 = 0$. An electrostatic field has zero circulation around every loop — Kirchhoff's voltage law.
>
> **(b)** Through $P_2$: $V(P_3)-V(P_1) = -\int_{P_1}^{P_3}\mathbf{E}\cdot d\mathbf{l} = -(6+12) = -18$ V. Along the slanted side walked from $P_1$ to $P_3$, the reverse of the third side: $-(+18) = -18$ V. The same, as zero circulation demands.
>
> **Check:** the uniform field is $-\nabla V$ with $V = -(3x+4y-2z)$, and $V(P_3)-V(P_1) = -(3\cdot2+4\cdot3) = -18$ V ✓.
>
> **Answer.** The sides give $6$, $12$ and $-18$ V; circulation $0$; $V(P_3)-V(P_1) = -18$ V by either route.

### 6.3 A field at a metal surface

> [!easy] Easy · multiple choice · conductors
> A conductor fills the region $3x+4y<12$ (coordinates in metres); its surface is the plane $3x+4y = 12$, and outside is free space. Under static conditions, which of these could be the electric field just outside the surface?
>
> (a) $\mathbf{E} = 4\hat{x}+3\hat{y}$ V/m
>
> (b) $\mathbf{E} = -6\hat{x}-8\hat{y}$ V/m
>
> (c) $\mathbf{E} = 3\hat{x}+4\hat{y}+5\hat{z}$ V/m
>
> (d) $\mathbf{E} = 8\hat{x}-6\hat{y}$ V/m
>
> For the possible one, find the surface charge density on the metal.
>
> *Source: original.*

> [!hint]- Hint
> Inside the metal $\mathbf{E} = 0$, so just outside $\hat{n}\times\mathbf{E} = 0$ and $\rho_s = \hat{n}\cdot\mathbf{D}$, with $\hat{n}$ pointing out of the metal. Which way does the gradient of $3x+4y$ point?

> [!solution]- Solution
> **(b).** The normal out of the metal points toward increasing $3x+4y$: $\hat{n} = (3\hat{x}+4\hat{y})/5 = 0.6\hat{x}+0.8\hat{y}$. The metal side has no field, so the conditions reduce to $\hat{n}\times\mathbf{E} = 0$ (no tangential field outside) and $\rho_s = \hat{n}\cdot\mathbf{D}$.
>
> - (a) $\hat{n}\times\mathbf{E} = -1.4\hat{z}$ V/m $\neq0$: besides its normal part ($\hat{n}\cdot\mathbf{E} = 4.8$ V/m) it has a tangential part. Not allowed.
> - (b) $\mathbf{E} = -10\,\hat{n}$, so $\hat{n}\times\mathbf{E} = 0$. Allowed: the field is perpendicular to the surface and points *into* the metal.
> - (c) The $3\hat{x}+4\hat{y}$ part is normal ($\hat{n}\cdot\mathbf{E} = 5$ V/m), but $\hat{z}$ lies *in* the surface ($\hat{n}\cdot\hat{z} = 0$), so $5\hat{z}$ is tangential: $\hat{n}\times\mathbf{E} = 4\hat{x}-3\hat{y}$ V/m $\neq0$. Not allowed.
> - (d) $\hat{n}\cdot\mathbf{E} = 0$: the field is *purely* tangential ($\hat{n}\times\mathbf{E} = -10\hat{z}$ V/m), the opposite of what a conductor allows.
>
> For (b), $\rho_s = \hat{n}\cdot\epsilon_0\mathbf{E} = -10\epsilon_0\approx-8.85\times10^{-11}$ C/m². It is negative, as it must be where field lines end on the metal.
>
> **Watch out:** (c) is the trap. Checking only the $xy$ direction is not enough: the plane $3x+4y = 12$ contains the whole $z$ direction.
>
> **Answer.** (b) only; $\rho_s = -10\epsilon_0\approx-8.85\times10^{-11}$ C/m².

### 6.4 Crossing a current sheet

> [!easy] Easy · current sheet · magnetic boundary conditions
> The plane $x = 0$ carries the surface current $\mathbf{J}_s = 4\hat{z}$ A/m, with free space on both sides. Medium 1 is $x>0$ and medium 2 is $x<0$, so $\hat{n} = \hat{x}$. Just to the left of the sheet, $\mathbf{H}_2 = 3\hat{x}-2\hat{y}$ A/m. Find $\mathbf{H}_1$ just to the right of the sheet, and $\mathbf{B}$ on both sides in μT.
>
> *Source: original.*

> [!hint]- Hint
> Only the tangential part of $\mathbf{H}$ can jump. Write the jump as $\mathbf{H}_{1t}-\mathbf{H}_{2t} = a\hat{y}+b\hat{z}$ and use $\hat{x}\times(a\hat{y}+b\hat{z}) = a\hat{z}-b\hat{y}$.

> [!solution]- Solution
> **Normal part.** $\hat{n}\cdot(\mathbf{B}_1-\mathbf{B}_2) = 0$ with $\mathbf{B} = \mu_0\mathbf{H}$ on both sides, so $H_{1x} = H_{2x} = 3$ A/m.
>
> **Tangential part.** $\hat{x}\times(\mathbf{H}_1-\mathbf{H}_2) = \mathbf{J}_s$. With the jump written as $a\hat{y}+b\hat{z}$: $\hat{x}\times(a\hat{y}+b\hat{z}) = a\hat{z}-b\hat{y} = 4\hat{z}$, so $a = 4$ and $b = 0$. $H_y$ rises by 4 A/m and $H_z$ is unchanged:
> $$
> \mathbf{H}_1 = 3\hat{x}+(-2+4)\hat{y} = 3\hat{x}+2\hat{y}\ \text{A/m}.
> $$
> Then $\mathbf{B}_1 = \mu_0\mathbf{H}_1\approx3.77\hat{x}+2.51\hat{y}$ μT and $\mathbf{B}_2 = \mu_0\mathbf{H}_2\approx3.77\hat{x}-2.51\hat{y}$ μT.
>
> **Check (Ampère):** a thin rectangle in the $xy$-plane straddling the sheet, with long sides of 2 m along $+\hat{y}$ (at $x>0$) and $-\hat{y}$ (at $x<0$), runs counter-clockwise seen from $+z$. Its circulation is $(2)(2)-(-2)(2) = 8$ A, and the current through it is $J_s\times2\text{ m} = 8$ A ✓.
>
> **Answer.** $\mathbf{H}_1 = 3\hat{x}+2\hat{y}$ A/m; $\mathbf{B}_1\approx3.77\hat{x}+2.51\hat{y}$ μT and $\mathbf{B}_2\approx3.77\hat{x}-2.51\hat{y}$ μT ($B_x$ continuous, $B_y$ reverses).

### 6.5 The flipped normal

> [!easy] Easy · find the error · surface charge
> The plane $z = 0$ has free space on both sides. Just below it $\mathbf{D} = 2\hat{x}+6\hat{z}$ nC/m², and just above it $\mathbf{D} = 2\hat{x}+\hat{z}$ nC/m². A student finds the surface charge on the plane like this:
>
> "Call the region below medium 1 and the region above medium 2. The normal of the plane is $\hat{n} = \hat{z}$, so $\rho_s = \hat{n}\cdot(\mathbf{D}_1-\mathbf{D}_2) = \hat{z}\cdot[(2\hat{x}+6\hat{z})-(2\hat{x}+\hat{z})] = 6-1 = +5$ nC/m²."
>
> What is wrong? Find the correct $\rho_s$.
>
> *Source: original.*

> [!solution]- Solution
> **The slip:** $\hat{n}$ must point **from medium 2 into medium 1**. The student put medium 1 below, so the normal must point down, $\hat{n} = -\hat{z}$; $\hat{z}$ was used only because it is "the" normal of the plane. Relabelling the media without flipping $\hat{n}$ flips the sign of $\rho_s$.
>
> **Fix**, either way:
>
> - keep medium 1 below and use $\hat{n} = -\hat{z}$: $\rho_s = -\hat{z}\cdot[(2\hat{x}+6\hat{z})-(2\hat{x}+\hat{z})] = -(6-1) = -5$ nC/m²;
> - or relabel, medium 1 above with $\hat{n} = +\hat{z}$: $\rho_s = \hat{z}\cdot[(2\hat{x}+\hat{z})-(2\hat{x}+6\hat{z})] = 1-6 = -5$ nC/m².
>
> **Check:** picture a pillbox. $\mathbf{D}$ flux enters through the bottom cap at 6 nC/m² but only 1 nC/m² leaves through the top, so the sheet swallows flux: it is negatively charged. The tangential parts agree ($D_x = 2$ nC/m² on both sides), as they must in vacuum, where $\mathbf{D}_t = \epsilon_0\mathbf{E}_t$ is continuous.
>
> **Answer.** The normal points the wrong way (it must point into medium 1, here $-\hat{z}$); $\rho_s = -5$ nC/m².

## Medium

### 6.6 Circulation of two fields

> [!medium] Medium · circulation · Stokes' theorem · potential
> Two candidate fields, with $x, y$ in metres and the fields in V/m:
> $$
> \mathbf{E}_a = (2x+y)\,\hat{x}+x\,\hat{y},\qquad \mathbf{E}_b = xy\,\hat{y}.
> $$
> Take the triangle $O = (0,0,0)$, $A = (2,0,0)$, $B = (2,2,0)$ m, traversed $O\to A\to B\to O$ (counter-clockwise seen from $+z$).
>
> (a) Compute the circulation of each field around the triangle, side by side.
>
> (b) Which field could be electrostatic? Confirm with the curls, and verify Stokes' theorem on the triangle for the other one.
>
> (c) For the electrostatic one, find $V(B)-V(O)$ and a potential $V(x,y)$. Why does "$V(B)-V(O)$" make no sense for the other field?
>
> *Source: classic.*

> [!hint]- Hint
> On the hypotenuse $B\to O$ put $x = y = s$ with $s$ running from 2 down to 0, so $d\mathbf{l} = (\hat{x}+\hat{y})\,ds$. For Stokes, the right-hand rule gives $d\mathbf{S} = +\hat{z}\,dx\,dy$ over the region $0\le y\le x\le2$.

> [!solution]- Solution
> **Setup.** Three straight sides, each with its own $d\mathbf{l}$ and limits that walk the loop in the stated direction: $O\to A$ has $y = 0$, $d\mathbf{l} = \hat{x}\,dx$, $x: 0\to2$; $A\to B$ has $x = 2$, $d\mathbf{l} = \hat{y}\,dy$, $y: 0\to2$; $B\to O$ has $x = y = s$, $d\mathbf{l} = (\hat{x}+\hat{y})\,ds$, $s: 2\to0$.
>
> **(a)** On the hypotenuse $\mathbf{E}_a = 3s\,\hat{x}+s\,\hat{y}$ and $\mathbf{E}_b = s^2\,\hat{y}$, so
> $$
> \begin{aligned}
> \oint\mathbf{E}_a\cdot d\mathbf{l} &= \int_0^2 2x\,dx+\int_0^2 2\,dy+\int_2^0(3s+s)\,ds = 4+4-8 = 0,\\
> \oint\mathbf{E}_b\cdot d\mathbf{l} &= 0+\int_0^2 2y\,dy+\int_2^0 s^2\,ds = 0+4-\tfrac83 = \tfrac43\ \text{V}.
> \end{aligned}
> $$
>
> **(b)** Only $\mathbf{E}_a$ can be electrostatic: a static field has zero circulation around *every* loop, and $\mathbf{E}_b$ already fails on this one. The curls have only $z$ components:
> $$
> (\nabla\times\mathbf{E}_a)_z = \frac{\partial E_{ay}}{\partial x}-\frac{\partial E_{ax}}{\partial y} = 1-1 = 0,\qquad (\nabla\times\mathbf{E}_b)_z = \frac{\partial(xy)}{\partial x}-0 = y.
> $$
> Stokes for $\mathbf{E}_b$, with $d\mathbf{S} = \hat{z}\,dx\,dy$ for a loop that is counter-clockwise seen from $+z$:
> $$
> \int_S(\nabla\times\mathbf{E}_b)\cdot d\mathbf{S} = \int_0^2\!\!\int_0^x y\,dy\,dx = \int_0^2\frac{x^2}{2}\,dx = \frac43\ \text{V},
> $$
> the same as the circulation ✓.
>
> **(c)** Walking $O\to A\to B$: $V(B)-V(O) = -\int_O^B\mathbf{E}_a\cdot d\mathbf{l} = -(4+4) = -8$ V. A potential needs $-\partial V/\partial x = 2x+y$ and $-\partial V/\partial y = x$; $V = -(x^2+xy)$ does both, and gives $V(B)-V(O) = -(4+4)-0 = -8$ V ✓.
>
> For $\mathbf{E}_b$ the line integral from $O$ to $B$ depends on the path: $4$ V along $O\to A\to B$ but $\tfrac83$ V along the straight line $O\to B$. They differ by exactly the circulation, $\tfrac43$ V, so no single-valued $V$ exists.
>
> **Watch out:** a zero circulation around *one* loop does not prove a field conservative; the curl, zero at every point, does.
>
> **Answer.** Circulations $0$ for $\mathbf{E}_a$ and $\tfrac43$ V for $\mathbf{E}_b$; $\nabla\times\mathbf{E}_a = 0$ (electrostatic), $\nabla\times\mathbf{E}_b = y\,\hat{z}$, whose flux through the triangle is $\tfrac43$ V. $V(B)-V(O) = -8$ V, with $V = -(x^2+xy)$.

### 6.7 A charged tilted interface

> [!medium] Medium · boundary conditions · oblique interface · bound charge
> The plane $x+2y+2z = 0$ separates vacuum (medium 1, the side $x+2y+2z>0$) from a dielectric with $\epsilon_2 = 2\epsilon_0$ (medium 2, the side $x+2y+2z<0$), and carries a free surface charge $\rho_s = 3\epsilon_0$ C/m². Just inside the dielectric, $\mathbf{E}_2 = 3\hat{x}+\hat{y}+2\hat{z}$ V/m. Use $\mathbf{D} = \epsilon\mathbf{E}$ in each medium.
>
> (a) Find the unit normal $\hat{n}$ from medium 2 into medium 1, and split $\mathbf{E}_2$ into its normal and tangential parts.
>
> (b) Find $\mathbf{E}_1$ and $\mathbf{D}_1$ just on the vacuum side, and $\mathbf{D}_2$.
>
> (c) Verify both electric boundary conditions with the full vectors.
>
> (d) The *total* surface charge is what Gauss's law for $\epsilon_0\mathbf{E}$ sees, $\hat{n}\cdot(\epsilon_0\mathbf{E}_1-\epsilon_0\mathbf{E}_2)$. Find it, and the bound surface charge (total minus free).
>
> *Source: original (the Lecture 6 in-class challenge question, tilted and re-parameterized).*

> [!hint]- Hint
> The gradient of $x+2y+2z$ points toward the vacuum side. The normal part of $\mathbf{E}_2$ is $E_{2n} = \mathbf{E}_2\cdot\hat{n}$ and the tangential part is $\mathbf{E}_2-E_{2n}\hat{n}$. Copy the tangential part across; get the new normal part from $D_n$, not from $E_n$.

> [!solution]- Solution
> **Setup.** Divergence laws constrain normal components and curl laws tangential ones, so first split every vector along $\hat{n}$.
>
> **(a)** $\nabla(x+2y+2z) = \hat{x}+2\hat{y}+2\hat{z}$ points into medium 1 and has length 3:
> $$
> \hat{n} = \tfrac13(\hat{x}+2\hat{y}+2\hat{z}),\qquad E_{2n} = \mathbf{E}_2\cdot\hat{n} = \tfrac13(3\cdot1+1\cdot2+2\cdot2) = 3\ \text{V/m}.
> $$
> The normal part is $E_{2n}\hat{n} = \hat{x}+2\hat{y}+2\hat{z}$ V/m and the tangential part is $\mathbf{E}_{2t} = \mathbf{E}_2-E_{2n}\hat{n} = 2\hat{x}-\hat{y}$ V/m (check: $\mathbf{E}_{2t}\cdot\hat{n} = \tfrac13(2\cdot1-1\cdot2) = 0$ ✓).
>
> **(b)** Tangential $\mathbf{E}$ is continuous: $\mathbf{E}_{1t} = 2\hat{x}-\hat{y}$ V/m. Normal $\mathbf{D}$ jumps by $\rho_s$: $D_{2n} = 2\epsilon_0(3) = 6\epsilon_0$, so $D_{1n} = 6\epsilon_0+3\epsilon_0 = 9\epsilon_0$ and $E_{1n} = D_{1n}/\epsilon_0 = 9$ V/m. Reassemble:
> $$
> \mathbf{E}_1 = (2\hat{x}-\hat{y})+9\cdot\tfrac13(\hat{x}+2\hat{y}+2\hat{z}) = 5\hat{x}+5\hat{y}+6\hat{z}\ \text{V/m},
> $$
> so $\mathbf{D}_1 = \epsilon_0(5\hat{x}+5\hat{y}+6\hat{z})$ C/m², and $\mathbf{D}_2 = 2\epsilon_0\mathbf{E}_2 = \epsilon_0(6\hat{x}+2\hat{y}+4\hat{z})$ C/m².
>
> **(c)** $\mathbf{D}_1-\mathbf{D}_2 = \epsilon_0(-\hat{x}+3\hat{y}+2\hat{z})$, so $\hat{n}\cdot(\mathbf{D}_1-\mathbf{D}_2) = \tfrac{\epsilon_0}{3}(-1+2\cdot3+2\cdot2) = 3\epsilon_0 = \rho_s$ ✓. And $\mathbf{E}_1-\mathbf{E}_2 = 2\hat{x}+4\hat{y}+4\hat{z}$ is parallel to $\hat{n}$, so $\hat{n}\times(\mathbf{E}_1-\mathbf{E}_2) = 0$ ✓.
>
> **(d)** Total: $\hat{n}\cdot\epsilon_0(\mathbf{E}_1-\mathbf{E}_2) = \epsilon_0(9-3) = 6\epsilon_0$ C/m². Bound: $\rho_{sb} = 6\epsilon_0-3\epsilon_0 = 3\epsilon_0\approx2.66\times10^{-11}$ C/m².
>
> **Check** (a preview of Lecture 8): $\mathbf{P}_2 = \mathbf{D}_2-\epsilon_0\mathbf{E}_2 = \epsilon_0(3\hat{x}+\hat{y}+2\hat{z})$, and the dielectric's outward normal is $+\hat{n}$, so $\rho_{sb} = \mathbf{P}_2\cdot\hat{n} = 3\epsilon_0$ ✓.
>
> **Watch out:** tangential $\mathbf{D}$ is *not* continuous. $\mathbf{D}_{2t} = \epsilon_0(4\hat{x}-2\hat{y})$ but $\mathbf{D}_{1t} = \epsilon_0(2\hat{x}-\hat{y})$: it halves along with $\epsilon$.
>
> **Answer.** $\hat{n} = (\hat{x}+2\hat{y}+2\hat{z})/3$; $E_{2n} = 3$ V/m, $\mathbf{E}_{2t} = 2\hat{x}-\hat{y}$ V/m; $\mathbf{E}_1 = 5\hat{x}+5\hat{y}+6\hat{z}$ V/m, $\mathbf{D}_1 = \epsilon_0(5\hat{x}+5\hat{y}+6\hat{z})$ C/m², $\mathbf{D}_2 = \epsilon_0(6\hat{x}+2\hat{y}+4\hat{z})$ C/m²; total surface charge $6\epsilon_0$, bound $\rho_{sb} = 3\epsilon_0\approx2.66\times10^{-11}$ C/m².

### 6.8 Refraction of field lines

> [!medium] Medium · refraction · dielectric interface · bound charge
> The plane $y = 0$ separates air (medium 1, $y>0$, $\epsilon_1 = \epsilon_0$) from glass (medium 2, $y<0$, $\epsilon_2 = 3\epsilon_0$), so $\hat{n} = \hat{y}$. The interface carries no free charge. Just above it, the field in the air has magnitude 200 V/m and makes $\theta_1 = 30^\circ$ with the normal: $\mathbf{E}_1 = 200(\sin30^\circ\,\hat{x}+\cos30^\circ\,\hat{y})$ V/m. Use $\mathbf{D} = \epsilon\mathbf{E}$ in each medium.
>
> (a) Find $\mathbf{E}_2$ in the glass, its magnitude, and the angle $\theta_2$ it makes with the normal.
>
> (b) Show that $\tan\theta_1/\tan\theta_2 = \epsilon_1/\epsilon_2$.
>
> (c) Find $\mathbf{D}$ on both sides, in nC/m².
>
> (d) Find the bound surface charge density on the glass surface (the total surface charge, from the jump in $\epsilon_0E_n$, minus the free charge).
>
> (e) Inside water ($\epsilon_r = 81$) a field makes $45^\circ$ with the normal to the flat water surface, which carries no free charge. At what angle to the normal does it emerge into the air?
>
> *Source: classic.*

> [!hint]- Hint
> $E_t$ is the same on both sides of any interface, and with no free charge so is $\epsilon E_n$. The angle from the normal obeys $\tan\theta = E_t/E_n$.

> [!solution]- Solution
> **Setup.** $\mathbf{E}_1 = 100\hat{x}+100\sqrt3\,\hat{y}\approx100\hat{x}+173.2\hat{y}$ V/m: tangential part $E_{1t} = 100$ V/m, normal part $E_{1n} = 173.2$ V/m.
>
> **(a)** Tangential $\mathbf{E}$ is continuous, $E_{2t} = 100$ V/m. With no free charge $D_n$ is continuous, $\epsilon_2E_{2n} = \epsilon_1E_{1n}$, so $E_{2n} = 173.2/3 = 57.7$ V/m:
> $$
> \mathbf{E}_2 = 100\hat{x}+57.7\hat{y}\ \text{V/m},\qquad \lvert\mathbf{E}_2\rvert = \frac{200}{\sqrt3} = 115.5\ \text{V/m},\qquad \tan\theta_2 = \frac{100}{57.7} = \sqrt3\ \Rightarrow\ \theta_2 = 60^\circ.
> $$
> In the glass the field is weaker and bent *away* from the normal.
>
> **(b)** $\tan\theta = E_t/E_n$, with $E_t$ common to both sides and $E_n\propto1/\epsilon$, so $\tan\theta\propto\epsilon$. Here $\tan30^\circ/\tan60^\circ = 1/3 = \epsilon_1/\epsilon_2$ ✓.
>
> **(c)** $\mathbf{D}_1 = \epsilon_0\mathbf{E}_1 = \epsilon_0(100\hat{x}+173.2\hat{y})\approx0.885\hat{x}+1.53\hat{y}$ nC/m², and $\mathbf{D}_2 = 3\epsilon_0\mathbf{E}_2 = \epsilon_0(300\hat{x}+173.2\hat{y})\approx2.66\hat{x}+1.53\hat{y}$ nC/m². $D_y$ is continuous; $D_x$ triples.
>
> **(d)** With $\hat{n} = \hat{y}$ from the glass into the air, the total surface charge is $\epsilon_0(E_{1n}-E_{2n})$, and with no free charge all of it is bound:
> $$
> \rho_{sb} = \epsilon_0(173.2-57.7) = \frac{200}{\sqrt3}\,\epsilon_0\approx1.02\times10^{-9}\ \text{C/m}^2 .
> $$
> It is positive: the polarized glass turns its positive ends toward the air.
>
> **(e)** $\tan\theta_{\text{air}} = \tan45^\circ/81$, so $\theta_{\text{air}} = 0.71^\circ$. The field leaves the water almost perpendicular to its surface, much as it leaves a conductor.
>
> **Check** (a preview of Lecture 8): $\mathbf{P}_2 = \mathbf{D}_2-\epsilon_0\mathbf{E}_2$ and the glass's outward normal is $+\hat{y}$, so $\rho_{sb} = \mathbf{P}_2\cdot\hat{y} = (3\epsilon_0-\epsilon_0)E_{2n} = 2\epsilon_0(57.7)\approx115.5\,\epsilon_0$ ✓.
>
> **Watch out:** $\theta$ is measured from the *normal*. Measured from the surface, the tangent ratio would come out inverted.
>
> **Answer.** $\mathbf{E}_2 = 100\hat{x}+57.7\hat{y}$ V/m, $\lvert\mathbf{E}_2\rvert = 115.5$ V/m, $\theta_2 = 60^\circ$; $\mathbf{D}_1\approx0.885\hat{x}+1.53\hat{y}$ nC/m², $\mathbf{D}_2\approx2.66\hat{x}+1.53\hat{y}$ nC/m²; $\rho_{sb} = 200\epsilon_0/\sqrt3\approx1.02\times10^{-9}$ C/m²; $0.71^\circ$ from the normal.

## Hard

### 6.9 Two tilted charged planes

> [!hard] Hard · charged sheets · oblique interface · circulation
> Two infinite planes lie in vacuum. Plane $P$, $3x+4z = 0$, carries $\rho_{sP} = 5\epsilon_0$ C/m²; plane $Q$, $3x+4z = 10$ m, carries an unknown $\rho_{sQ}$. Call the regions $L$ ($3x+4z<0$), $M$ (between the planes) and $R$ ($3x+4z>10$ m); $\mathbf{D}$ is uniform in each. In $M$, $\mathbf{D}_M = \epsilon_0(7\hat{x}+2\hat{y}+\hat{z})$ C/m², and in $R$ the $x$ component of $\mathbf{D}$ is measured to be $\epsilon_0$ C/m².
>
> (a) Find the unit normal $\hat{n}$ pointing toward increasing $3x+4z$, the distance between the planes, and the normal and tangential parts of $\mathbf{D}_M$.
>
> (b) Find $\mathbf{D}_L$.
>
> (c) Find $\mathbf{D}_R$ and $\rho_{sQ}$.
>
> (d) Find $V(B)-V(A)$ for $A = (0,0,0)$ and $B = (2,0,1)$ m. Then verify that the circulation of $\mathbf{E}$ around the triangle $A\to B\to C\to A$, with $C = (2,0,-2)$ m, is zero even though the triangle crosses plane $P$.
>
> *Source: original (the two-plane examples of Lecture 6, tilted).*

> [!hint]- Hint
> At each plane, medium 1 is the side $\hat{n}$ points into. Everything is vacuum, so the tangential part $\mathbf{D}_t = \epsilon_0\mathbf{E}_t$ is the same in all three regions, and only $D_n$ changes, by $\rho_s$ at each plane. In (c), write $\mathbf{D}_R = \mathbf{D}_{Mt}+D_{Rn}\hat{n}$ and let the measured $x$ component fix $D_{Rn}$. In (d), find where side $B\to C$ crosses $P$ and split it there.

> [!solution]- Solution
> **Setup.** $\mathbf{D} = \epsilon_0\mathbf{E}$ everywhere, so continuity of $\mathbf{E}_t$ makes $\mathbf{D}_t$ continuous too. At $P$ take $M$ as medium 1 and $L$ as medium 2; at $Q$ take $R$ as medium 1 and $M$ as medium 2. Either way $\hat{n}$ points toward increasing $3x+4z$.
>
> **(a)** $\nabla(3x+4z) = 3\hat{x}+4\hat{z}$, so $\hat{n} = (3\hat{x}+4\hat{z})/5 = 0.6\hat{x}+0.8\hat{z}$, and the planes are $10/5 = 2$ m apart. Then
> $$
> D_{Mn} = \hat{n}\cdot\mathbf{D}_M = \frac{\epsilon_0}{5}(3\cdot7+4\cdot1) = 5\epsilon_0,\qquad \mathbf{D}_{Mt} = \mathbf{D}_M-5\epsilon_0\hat{n} = \epsilon_0(4\hat{x}+2\hat{y}-3\hat{z}),
> $$
> and indeed $\mathbf{D}_{Mt}\cdot\hat{n} = \tfrac{\epsilon_0}{5}(3\cdot4+4\cdot(-3)) = 0$ ✓.
>
> **(b)** At $P$: $\hat{n}\cdot(\mathbf{D}_M-\mathbf{D}_L) = \rho_{sP}$, so $D_{Ln} = 5\epsilon_0-5\epsilon_0 = 0$. With the tangential part copied,
> $$
> \mathbf{D}_L = \epsilon_0(4\hat{x}+2\hat{y}-3\hat{z})\ \text{C/m}^2,\qquad \mathbf{E}_L = 4\hat{x}+2\hat{y}-3\hat{z}\ \text{V/m}:
> $$
> in $L$ the field runs parallel to the planes.
>
> **(c)** $\mathbf{D}_R = \mathbf{D}_{Mt}+D_{Rn}\hat{n}$ has $x$ component $4\epsilon_0+0.6D_{Rn} = \epsilon_0$, so $D_{Rn} = -5\epsilon_0$ and
> $$
> \mathbf{D}_R = \epsilon_0(4\hat{x}+2\hat{y}-3\hat{z})-5\epsilon_0(0.6\hat{x}+0.8\hat{z}) = \epsilon_0(\hat{x}+2\hat{y}-7\hat{z})\ \text{C/m}^2 .
> $$
> At $Q$: $\rho_{sQ} = \hat{n}\cdot(\mathbf{D}_R-\mathbf{D}_M) = -5\epsilon_0-5\epsilon_0 = -10\epsilon_0\approx-8.85\times10^{-11}$ C/m².
>
> **(d)** $A$ lies on $P$, and $B$ lies on $Q$ ($3\cdot2+4\cdot1 = 10$), so the straight segment $AB$ stays in $M$, where $\mathbf{E}_M = 7\hat{x}+2\hat{y}+\hat{z}$ V/m is uniform:
> $$
> V(B)-V(A) = -\mathbf{E}_M\cdot(B-A) = -(7\cdot2+2\cdot0+1\cdot1) = -15\ \text{V}.
> $$
> Circulation, side by side:
>
> - $A\to B$: $+15$ V (the integral just computed, without the minus sign).
> - $B\to C$: $x = 2$, $y = 0$, $d\mathbf{l} = \hat{z}\,dz$ with $z$ from 1 to $-2$. It crosses $P$ where $3\cdot2+4z = 0$, at $z = -1.5$ m. The part in $M$ gives $\int_1^{-1.5}1\,dz = -2.5$ V and the part in $L$ gives $\int_{-1.5}^{-2}(-3)\,dz = +1.5$ V: $-1$ V in all.
> - $C\to A$: $C$ is in $L$ ($3\cdot2+4\cdot(-2) = -2<0$) and the segment stays in $L$ up to $A$: $\mathbf{E}_L\cdot(A-C) = 4(-2)+(-3)(2) = -14$ V.
>
> Sum: $15-1-14 = 0$ ✓, as it must be for an electrostatic field, plane or no plane.
>
> **Check 1:** across both planes $D_n$ changes by $D_{Rn}-D_{Ln} = -5\epsilon_0-0 = -5\epsilon_0 = \rho_{sP}+\rho_{sQ}$ ✓ (a pillbox enclosing both planes).
>
> **Check 2:** reach $B$ in two steps instead. $B' = 2\hat{n} = (1.2, 0, 1.6)$ m is the foot of the perpendicular from $A$ to $Q$; $V(B')-V(A) = -E_{Mn}(2\text{ m}) = -10$ V uses only the normal field, and $V(B)-V(B') = -\mathbf{E}_{Mt}\cdot(B-B') = -5$ V runs along $Q$ and uses only the tangential field. Total $-15$ V ✓.
>
> **Watch out:** continuity of $\mathbf{E}_t$ is what makes the circulation vanish. Had you let $E_y$ jump by 1 V/m at $P$, a thin rectangle straddling $P$ with 2 m sides along $\hat{y}$ would have a circulation of 2 V.
>
> **Answer.** (a) $\hat{n} = (3\hat{x}+4\hat{z})/5$; 2 m apart; $D_{Mn} = 5\epsilon_0$, $\mathbf{D}_{Mt} = \epsilon_0(4\hat{x}+2\hat{y}-3\hat{z})$. (b) $\mathbf{D}_L = \epsilon_0(4\hat{x}+2\hat{y}-3\hat{z})$ C/m². (c) $\mathbf{D}_R = \epsilon_0(\hat{x}+2\hat{y}-7\hat{z})$ C/m², $\rho_{sQ} = -10\epsilon_0\approx-8.85\times10^{-11}$ C/m². (d) $V(B)-V(A) = -15$ V; circulation $15-1-14 = 0$.

### 6.10 Plates around a charged sheet

> [!hard] Hard · conductors · charged sheets · KVL
> Metal fills the half-spaces $x<0$ and $x>3$ m (two thick plates), with free space between them. A thin insulating sheet with a uniform surface charge lies on the plane $x = 2$ m. The plate at $x = 0$ is grounded, the plate at $x = 3$ m is held at $+6$ V by a battery, and a probe finds the sheet at $V = -2$ V.
>
> (a) Find $\mathbf{E}$ in the gaps $0<x<2$ m and $2<x<3$ m.
>
> (b) Find the surface charge densities on the two metal faces and on the sheet.
>
> (c) Show that the three densities add to zero and explain why they must. Check your fields by superposing the three charged planes, and check the voltages with KVL.
>
> (d) The battery is replaced by a wire, so the two plates are at the same potential; the sheet's charge does not change. Find the new fields, the new face charges and the new potential of the sheet. What fraction of the plates' charge sits on the nearer plate?
>
> *Source: classic.*

> [!hint]- Hint
> Each gap is free of charge, so $\mathbf{E}$ is uniform in it and follows from the potential difference across it. At a metal face, $\rho_s = \hat{n}\cdot\mathbf{D}$ with $\hat{n}$ pointing out of the metal. In (d) you have two unknown fields: zero circulation around the loop *gap, gap, wire* gives one equation, the jump at the sheet the other.

> [!solution]- Solution
> **Setup.** Planar symmetry gives $\mathbf{E} = E_x(x)\,\hat{x}$. In each gap $\epsilon_0\,dE_x/dx = \rho = 0$, so $E_x$ is constant there; call it $E_A$ for $0<x<2$ m and $E_B$ for $2<x<3$ m. In the metal $\mathbf{E} = 0$.
>
> **(a)** In a uniform field $V(b)-V(a) = -E_x\,(b-a)$, so
> $$
> E_A = -\frac{V(2)-V(0)}{2} = -\frac{-2-0}{2} = +1\ \text{V/m},\qquad E_B = -\frac{V(3)-V(2)}{1} = -\frac{6-(-2)}{1} = -8\ \text{V/m}.
> $$
> Both fields point *toward* the sheet, which must therefore be negative.
>
> **(b)** At a metal face, $\hat{n}$ points out of the metal into the gap:
>
> - face at $x = 0$: $\hat{n} = +\hat{x}$, $\rho_{s0} = \epsilon_0E_A = \epsilon_0\approx8.85\times10^{-12}$ C/m²;
> - face at $x = 3$ m: $\hat{n} = -\hat{x}$, $\rho_{s3} = -\epsilon_0E_B = 8\epsilon_0\approx7.08\times10^{-11}$ C/m²;
> - sheet: medium 1 is the gap $2<x<3$, medium 2 the gap $0<x<2$, $\hat{n} = +\hat{x}$: $\rho_{s2} = \epsilon_0(E_B-E_A) = -9\epsilon_0\approx-7.97\times10^{-11}$ C/m².
>
> **(c)** $\rho_{s0}+\rho_{s2}+\rho_{s3} = \epsilon_0(1-9+8) = 0$. It has to vanish: a stack of infinite charged planes with net charge $\rho_{\text{tot}}$ per area makes a field $\pm\rho_{\text{tot}}/(2\epsilon_0)$ on its two far sides, and here both far sides are metal with zero field. Superposition of the three planes, $E_x = \sum_i\dfrac{\rho_{si}}{2\epsilon_0}\operatorname{sgn}(x-x_i)$:
> $$
> 0<x<2:\ \tfrac12(1+9-8) = 1\ \text{V/m}\ \checkmark,\qquad 2<x<3:\ \tfrac12(1-9-8) = -8\ \text{V/m}\ \checkmark,
> $$
> and $0$ in both slabs of metal ✓. KVL around the loop through the battery: $-(E_A\cdot2+E_B\cdot1) = -(2-8) = 6$ V $= V(3)-V(0)$ ✓.
>
> **(d)** The fields in the gaps are still uniform, call them $E_A'$ and $E_B'$. Zero circulation around the loop from plate to plate across the gaps and back through the wire (no field in metal or wire) gives the first equation; the jump at the sheet, whose charge is unchanged, gives the second:
> $$
> 2E_A'+1\cdot E_B' = 0,\qquad \epsilon_0(E_B'-E_A') = \rho_{s2} = -9\epsilon_0 .
> $$
> So $E_B' = -2E_A'$, $-3E_A' = -9$, and
> $$
> E_A' = 3\ \text{V/m},\qquad E_B' = -6\ \text{V/m},\qquad \rho_{s0}' = 3\epsilon_0\approx2.66\times10^{-11}\ \text{C/m}^2,\qquad \rho_{s3}' = 6\epsilon_0\approx5.31\times10^{-11}\ \text{C/m}^2,
> $$
> with $V(2) = -E_A'\cdot2 = -6$ V. The plates still carry $9\epsilon_0$ in total, equal and opposite to the sheet (zero field in the metal requires it), and the nearer plate, at $x = 3$ m, holds $2/3$ of it. In general, for a sheet $\rho_s$ at $x = a$ between joined plates at $x = 0$ and $x = d$, the same two equations give $\rho_{s0}' = -\rho_s(d-a)/d$ and $\rho_{sd}' = -\rho_s\,a/d$: each plate's share is the sheet's distance from the *other* plate, divided by $d$.
>
> **Check:** superposing the new charges, $\tfrac12(-3+9-6) = 0$ for $x<0$ and $\tfrac12(3-9+6) = 0$ for $x>3$ m ✓; and $V(3)-V(0) = -(3\cdot2-6\cdot1) = 0$ ✓.
>
> **Watch out:** at $x = 3$ m the normal out of the metal is $-\hat{x}$. Using $+\hat{x}$ there gives the face charge $-8\epsilon_0$, and the total charge no longer adds to zero.
>
> **Answer.** (a) $\mathbf{E} = +1\,\hat{x}$ V/m for $0<x<2$ m and $-8\,\hat{x}$ V/m for $2<x<3$ m. (b) $\rho_{s0} = \epsilon_0\approx8.85\times10^{-12}$ C/m², $\rho_{s3} = 8\epsilon_0\approx7.08\times10^{-11}$ C/m², sheet $-9\epsilon_0\approx-7.97\times10^{-11}$ C/m². (d) $E_A' = 3$ V/m, $E_B' = -6$ V/m; $\rho_{s0}' = 3\epsilon_0\approx2.66\times10^{-11}$ C/m², $\rho_{s3}' = 6\epsilon_0\approx5.31\times10^{-11}$ C/m²; sheet at $-6$ V; the nearer plate holds $2/3$.

### 6.11 Charged shell in a dielectric

> [!hard] Hard · cylindrical interface · surface charge · refraction
> A long line charge $\rho_l$ lies on the $z$ axis. The core $r<2$ m is vacuum and the region $r>2$ m is a dielectric with $\epsilon = 4\epsilon_0$ (use $\mathbf{D} = \epsilon\mathbf{E}$). The interface $r = 2$ m carries a uniform free surface charge $\rho_s$, and distant sources add a uniform field along $z$. Just inside the interface the field is $\mathbf{E}(r = 2^{-}) = 6\hat{r}+3\hat{z}$ V/m, and just outside a probe measures $E_r(r = 2^{+}) = 1$ V/m. Take the dielectric as medium 1 and the core as medium 2, so $\hat{n} = \hat{r}$.
>
> (a) Find $\mathbf{E}$ and $\mathbf{D}$ just outside the interface.
>
> (b) Find $\rho_s$.
>
> (c) Find the total surface charge density on the interface (from the jump in $\epsilon_0E_r$) and the bound part (total minus free).
>
> (d) Find $\rho_l$.
>
> (e) Find the angles $\theta_2$ and $\theta_1$ between $\mathbf{E}$ and the normal just inside and just outside. Why is $\tan\theta_1/\tan\theta_2$ not equal to $\epsilon_1/\epsilon_2$? What would $E_r(2^{+})$ be if $\rho_s$ were zero?
>
> *Source: original; combines FA26 Exam 1 #3 (fields across a dielectric interface) with SP18 Exam 1 #4 (free surface charge on a cylindrical interface).*

> [!hint]- Hint
> On the surface $r = 2$ m the normal is $\hat{r}$, and $\hat\phi$ and $\hat{z}$ are tangential. Copy $E_z$ across, use $D_r$ for the jump, and find $\rho_l$ from Gauss's law on a closed cylinder just inside the interface.

> [!solution]- Solution
> **Setup.** Locally the interface is a plane with normal $\hat{n} = \hat{r}$, pointing from the core (medium 2) into the dielectric (medium 1). So $E_r$ and $D_r$ are the normal components, and $E_z$ is tangential.
>
> **(a)** Tangential $\mathbf{E}$ is continuous, $E_z(2^{+}) = 3$ V/m. With the measured $E_r(2^{+}) = 1$ V/m:
> $$
> \mathbf{E}_1 = \hat{r}+3\hat{z}\ \text{V/m},\qquad \mathbf{D}_1 = 4\epsilon_0\mathbf{E}_1 = \epsilon_0(4\hat{r}+12\hat{z})\ \text{C/m}^2 .
> $$
>
> **(b)** In the vacuum core $\mathbf{D}_2 = \epsilon_0(6\hat{r}+3\hat{z})$, so
> $$
> \rho_s = \hat{r}\cdot(\mathbf{D}_1-\mathbf{D}_2) = 4\epsilon_0-6\epsilon_0 = -2\epsilon_0\approx-1.77\times10^{-11}\ \text{C/m}^2 .
> $$
>
> **(c)** Total: $\hat{r}\cdot\epsilon_0(\mathbf{E}_1-\mathbf{E}_2) = \epsilon_0(1-6) = -5\epsilon_0$. Bound: $\rho_{sb} = -5\epsilon_0-(-2\epsilon_0) = -3\epsilon_0\approx-2.66\times10^{-11}$ C/m². (Lecture 8 preview: $\mathbf{P}_1 = \mathbf{D}_1-\epsilon_0\mathbf{E}_1 = \epsilon_0(3\hat{r}+9\hat{z})$, and the dielectric's surface faces $-\hat{r}$, so $\rho_{sb} = \mathbf{P}_1\cdot(-\hat{r}) = -3\epsilon_0$ ✓.)
>
> **(d)** Inside the core the only charge is the line charge; the uniform $z$ field puts equal and opposite flux through the two end caps of a closed cylinder. Gauss on a cylinder of radius $2^{-}$ m and length $\ell$: $\epsilon_0E_r(2^{-})\cdot2\pi(2)\,\ell = \rho_l\,\ell$, so
> $$
> \rho_l = 2\pi(2)(6)\,\epsilon_0 = 24\pi\epsilon_0\approx6.68\times10^{-10}\ \text{C/m}.
> $$
>
> **(e)** $\tan\theta = E_t/E_n$. In the core $\tan\theta_2 = 3/6$, so $\theta_2 = 26.6^\circ$; in the dielectric $\tan\theta_1 = 3/1$, so $\theta_1 = 71.6^\circ$. The tangent ratio is 6, not $\epsilon_1/\epsilon_2 = 4$: the refraction law assumes $D_n$ is continuous, i.e. $\rho_s = 0$. Here the negative free charge absorbs some of the normal flux, so the field outside bends even further from the normal. With $\rho_s = 0$, $4\epsilon_0E_{1r} = 6\epsilon_0$ would give $E_{1r} = 1.5$ V/m, $\tan\theta_1 = 2$ and a ratio of exactly 4.
>
> **Check (Gauss for $\mathbf{D}$ outside):** the free charge per metre inside $r = 2^{+}$ is $\rho_l+2\pi(2)\rho_s = 24\pi\epsilon_0-8\pi\epsilon_0 = 16\pi\epsilon_0$, and $D_r(2^{+})\cdot2\pi(2) = 4\epsilon_0\cdot4\pi = 16\pi\epsilon_0$ ✓.
>
> **Answer.** (a) $\mathbf{E}_1 = \hat{r}+3\hat{z}$ V/m, $\mathbf{D}_1 = \epsilon_0(4\hat{r}+12\hat{z})$ C/m². (b) $\rho_s = -2\epsilon_0\approx-1.77\times10^{-11}$ C/m². (c) Total $-5\epsilon_0$; bound $\rho_{sb} = -3\epsilon_0\approx-2.66\times10^{-11}$ C/m². (d) $\rho_l = 24\pi\epsilon_0\approx6.68\times10^{-10}$ C/m. (e) $\theta_2 = 26.6^\circ$, $\theta_1 = 71.6^\circ$; ratio 6 instead of 4 because $\rho_s\neq0$; with $\rho_s = 0$, $E_r(2^{+}) = 1.5$ V/m.

### 6.12 A tilted current sheet

> [!hard] Hard · current sheet · magnetic boundary conditions · oblique interface
> The plane $3y+4z = 0$ carries a uniform surface current $\mathbf{J}_s = 5\hat{x}$ A/m, with free space on both sides. Medium 1 is the side $3y+4z>0$ and medium 2 the side $3y+4z<0$. Just on the medium-2 side, $\mathbf{H}_2 = 2\hat{x}+3\hat{y}+4\hat{z}$ A/m.
>
> (a) Find $\hat{n}$ (from medium 2 into medium 1) and check that $\mathbf{J}_s$ lies in the plane.
>
> (b) Split $\mathbf{H}_2$ into normal and tangential parts.
>
> (c) Find $\mathbf{H}_1$ and $\mathbf{B}_1$ just on the medium-1 side.
>
> (d) How much current crosses the segment from $(0,0,0)$ to $(0,4,-3)$ m, which lies in the sheet, and in which direction?
>
> (e) A lab partner reports $\mathbf{H}_1 = 2\hat{x}-\hat{y}+9\hat{z}$ A/m. Without redoing (c), show in one line that this cannot be right.
>
> *Source: original.*

> [!hint]- Hint
> Crossing $\hat{n}\times(\mathbf{H}_1-\mathbf{H}_2) = \mathbf{J}_s$ with $\hat{n}$ gives the tangential jump directly: $\mathbf{H}_{1t}-\mathbf{H}_{2t} = \mathbf{J}_s\times\hat{n}$. For (e), ask which component of $\mathbf{H}$ can never jump at a current sheet in free space.

> [!solution]- Solution
> **Setup.** Free space on both sides, so $\mathbf{B} = \mu_0\mathbf{H}$, and $\hat{n}\cdot(\mathbf{B}_1-\mathbf{B}_2) = 0$ makes $H_n$ continuous. Only $\mathbf{H}_t$ jumps, as $\hat{n}\times(\mathbf{H}_1-\mathbf{H}_2) = \mathbf{J}_s$ dictates.
>
> **(a)** $\nabla(3y+4z) = 3\hat{y}+4\hat{z}$ points into medium 1: $\hat{n} = (3\hat{y}+4\hat{z})/5 = 0.6\hat{y}+0.8\hat{z}$. $\mathbf{J}_s\cdot\hat{n} = 0$, so the current flows in the plane ✓.
>
> **(b)** $H_{2n} = \mathbf{H}_2\cdot\hat{n} = 0.6(3)+0.8(4) = 5$ A/m, so the normal part is $H_{2n}\hat{n} = 3\hat{y}+4\hat{z}$ A/m and the tangential part is $\mathbf{H}_{2t} = 2\hat{x}$ A/m.
>
> **(c)** The tangential jump: crossing $\hat{n}\times\Delta\mathbf{H}_t = \mathbf{J}_s$ with $\hat{n}$, and using $\hat{n}\times(\hat{n}\times\mathbf{v}) = -\mathbf{v}$ for any tangential $\mathbf{v}$,
> $$
> \Delta\mathbf{H}_t = \mathbf{J}_s\times\hat{n} = 5\hat{x}\times(0.6\hat{y}+0.8\hat{z}) = -4\hat{y}+3\hat{z}\ \text{A/m}.
> $$
> So $\mathbf{H}_{1t} = 2\hat{x}-4\hat{y}+3\hat{z}$ A/m, and adding the unchanged normal part,
> $$
> \mathbf{H}_1 = (2\hat{x}-4\hat{y}+3\hat{z})+(3\hat{y}+4\hat{z}) = 2\hat{x}-\hat{y}+7\hat{z}\ \text{A/m},\qquad \mathbf{B}_1 = \mu_0\mathbf{H}_1\approx2.51\hat{x}-1.26\hat{y}+8.80\hat{z}\ \mu\text{T}.
> $$
> Verify: $\mathbf{H}_1-\mathbf{H}_2 = -4\hat{y}+3\hat{z}$ has $\hat{n}\cdot(\mathbf{H}_1-\mathbf{H}_2) = 0.6(-4)+0.8(3) = 0$ ✓ and $\hat{n}\times(\mathbf{H}_1-\mathbf{H}_2) = 5\hat{x} = \mathbf{J}_s$ ✓.
>
> **(d)** The segment has length 5 m and runs along $\hat{t} = 0.8\hat{y}-0.6\hat{z}$; it lies in the sheet because $3(4)+4(-3) = 0$. The current crossing a line drawn in a sheet is $\int\mathbf{J}_s\cdot\hat{m}\,dl$, with $\hat{m}$ the normal to the line within the sheet. Here $\hat{m} = \hat{t}\times\hat{n} = \hat{x}$, parallel to $\mathbf{J}_s$, so $I = (5\text{ A/m})(5\text{ m}) = 25$ A, flowing in the $+\hat{x}$ direction.
>
> **(e)** The report has $\hat{n}\cdot\mathbf{H}_1 = \tfrac15(3(-1)+4(9)) = 6.6$ A/m, but $H_n$ must stay at $H_{2n} = 5$ A/m: $B_n$ would jump by $1.6\mu_0\approx2.01\times10^{-6}$ T, which $\hat{n}\cdot(\mathbf{B}_1-\mathbf{B}_2) = 0$ forbids.
>
> **Check (Ampère):** a thin rectangle in the plane $x = 0$ straddles the sheet, with long sides of 3 m along $+\hat{t}$ on the medium-2 side and $-\hat{t}$ on the medium-1 side; by the right-hand rule its normal is $\hat{t}\times\hat{n} = +\hat{x}$. Since $\mathbf{H}_2\cdot\hat{t} = 0$ and $\mathbf{H}_1\cdot\hat{t} = -5$ A/m, $\oint\mathbf{H}\cdot d\mathbf{l} = 0\cdot3-(-5)(3) = 15$ A, which is the enclosed current $J_s\times3$ m ✓. Note the pattern: the component of $\mathbf{H}$ along $\mathbf{J}_s$ ($H_x = 2$ A/m) does not jump; the tangential component perpendicular to $\mathbf{J}_s$ jumps by exactly $J_s$.
>
> **Watch out:** the jump is $\mathbf{J}_s\times\hat{n}$, not $\hat{n}\times\mathbf{J}_s$; the wrong order flips $\Delta\mathbf{H}_t$ and gives $\mathbf{H}_1 = 2\hat{x}+7\hat{y}+\hat{z}$ A/m.
>
> **Answer.** (a) $\hat{n} = 0.6\hat{y}+0.8\hat{z}$. (b) $H_{2n} = 5$ A/m, $\mathbf{H}_{2t} = 2\hat{x}$ A/m. (c) $\mathbf{H}_1 = 2\hat{x}-\hat{y}+7\hat{z}$ A/m, $\mathbf{B}_1\approx2.51\hat{x}-1.26\hat{y}+8.80\hat{z}$ μT. (d) 25 A in the $+\hat{x}$ direction. (e) The report has $H_{1n} = 6.6$ A/m $\neq5$ A/m, so $B_n$ would jump.

### Sources for this page
Course notes and slides, Lecture 6: the in-class challenge question behind 6.7 and the two-plane examples behind 6.9, both re-parameterized onto tilted planes. 6.11 is original but combines FA26 Exam 1 #3 (fields across a dielectric interface) with SP18 Exam 1 #4 (free surface charge on a cylindrical interface). Classic exercises with new numbers: circulation and Stokes' theorem on a triangle (6.6), refraction of field lines (6.8) and a charged sheet between two plates (6.10). Problems 6.1–6.5 and 6.12 are original.

*Previous: [[practice/05-electrostatic-potential|Lecture 5 practice]] · next: [[practice/07-poisson-and-laplace|Lecture 7 practice]] · [[practice/index|all practice]]*
