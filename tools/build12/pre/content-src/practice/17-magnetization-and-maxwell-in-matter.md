---
title: "Practice — Lecture 17: Magnetization and Maxwell's equations in matter"
description: "12 practice problems (5 easy, 3 medium, 4 hard) on magnetic moments and torque, M = Nm, magnetization currents ∇×M and M×n̂ (Cartesian and cylindrical, with zero net bound current), H = B/μ₀ − M, dia-, para- and ferromagnets and hysteresis, magnetic slabs between current sheets, interfaces and refraction at iron, a gapped toroid, a short bar magnet, and polarization–magnetization twins, each with a folded hint and a worked solution."
tags: [practice, waves]
lecture: 17
---

*Practice for [[3-maxwell-and-waves/17-magnetization-and-maxwells-equations-in-matter|Lecture 17]] · concepts: [[concepts/magnetization]] · [[concepts/permeability]] · [[concepts/boundary-conditions]] · [[concepts/polarization]] · all practice: [[practice/index|hub]] · by difficulty: [[practice/easy|easy]] · [[practice/medium|medium]] · [[practice/hard|hard]] · [[practice/topics|by topic]]*

Work each problem on paper first. Open the **hint** only when stuck, and the **solution** only after you have an answer you would hand in. Every answer here has been checked numerically.

## Easy

### 17.1 Moment and torque on a loop

> [!easy] Easy · magnetic dipole · right-hand rule
> A rectangular loop lies in the plane $z = 0$ with corners $(0,0,0)$, $(4,0,0)$, $(4,5,0)$ and $(0,5,0)$ cm. It carries $I = 2$ A, flowing from $(0,0,0)$ to $(4,0,0)$ to $(4,5,0)$ to $(0,5,0)$ and back. A uniform field $\mathbf{B} = 0.3\,\hat{x}+0.4\,\hat{z}$ T is applied.
>
> (a) Find the magnetic moment $\mathbf{m}$ of the loop.
>
> (b) Find the torque on the loop and the net force on it.
>
> (c) As the loop starts to turn, which of its two edges parallel to $y$ sinks and which rises? In which orientation is the loop in stable equilibrium?
>
> (d) An electron circles in the plane $z = 0$, counter-clockwise as seen from $+z$. Which way does its orbital moment point, and which way does this field turn it?
>
> *Source: Lecture 17 slides ($\mathbf{m} = I\mathbf{A}$ and the torque on a tilted orbit), re-posed with a rectangular loop and numbers.*

> [!hint]- Hint
> Curl the fingers of your right hand along the current; the thumb gives $\hat{n}$, and $\mathbf{m} = IA\,\hat{n}$. For (c), find the force $I\boldsymbol{\ell}\times\mathbf{B}$ on each edge parallel to $y$, or remember that $\mathbf{m}\times\mathbf{B}$ always turns $\mathbf{m}$ toward $\mathbf{B}$.

> [!solution]- Solution
> **(a)** Seen from $+z$ the current runs counter-clockwise ($+x$ along the edge $y = 0$, then $+y$ along the edge $x = 4$ cm), so the right-hand rule puts the thumb along $+\hat{z}$:
> $$
> \mathbf{m} = IA\,\hat{z} = 2\ \text{A}\times(0.04\times0.05)\ \text{m}^2\ \hat{z} = 4.0\times10^{-3}\,\hat{z}\ \text{A}\cdot\text{m}^2 .
> $$
> **(b)**
> $$
> \mathbf{T} = \mathbf{m}\times\mathbf{B} = 4.0\times10^{-3}\,\hat{z}\times(0.3\,\hat{x}+0.4\,\hat{z}) = 1.2\times10^{-3}\,\hat{y}\ \text{N}\cdot\text{m},
> $$
> which is $mB\sin\theta$ with $\sin\theta = 0.6$: only the $x$ component of $\mathbf{B}$ twists the loop. The net force is zero, because in a uniform field $\oint I\,d\mathbf{l}\times\mathbf{B} = I\big(\oint d\mathbf{l}\big)\times\mathbf{B} = 0$.
>
> **(c)** The edge at $x = 4$ cm carries current along $+\hat{y}$: $\mathbf{F} = I\ell\,\hat{y}\times\mathbf{B} = 2(0.05)\,\hat{y}\times(0.3\,\hat{x}+0.4\,\hat{z}) = 0.04\,\hat{x}-0.03\,\hat{z}$ N. It is pushed **down** and sinks. The edge at $x = 0$ carries current along $-\hat{y}$ and feels $-0.04\,\hat{x}+0.03\,\hat{z}$ N, so it **rises**. (The two edges along $x$ feel $\mp0.032\,\hat{y}$ N on the same line, $x = 2$ cm, and make no torque.) The loop turns about the $y$ direction, and $\mathbf{m}$ tilts from $+\hat{z}$ toward $+\hat{x}$, toward $\mathbf{B}$. Stable equilibrium has $\mathbf{m}$ parallel to $\mathbf{B}$: the normal along $0.6\,\hat{x}+0.8\,\hat{z}$, i.e. the loop tilted by $36.9^\circ$ about the $y$ axis with the $x = 4$ cm edge lowered. ($\mathbf{m}$ antiparallel to $\mathbf{B}$ is also an equilibrium, but an unstable one.)
>
> **Check:** the vertical forces act $\pm2$ cm from the centre along $x$: $(0.02\,\hat{x})\times(-0.03\,\hat{z})+(-0.02\,\hat{x})\times(0.03\,\hat{z}) = 1.2\times10^{-3}\,\hat{y}$ N·m ✓.
>
> **(d)** The electron's charge is negative, so its current runs **clockwise** seen from $+z$, and its moment points along $-\hat{z}$. The torque per unit moment, $-\hat{z}\times\mathbf{B} = -0.3\,\hat{y}$, tilts it from $-\hat{z}$ toward $+\hat{x}$, closing its $143.1^\circ$ angle with $\mathbf{B}$: the field turns this moment toward itself too.
>
> **Watch out:** for a negative charge, $\mathbf{m}$ points opposite to what the motion alone suggests. Always find the direction of the *current* first.
>
> **Answer.** (a) $\mathbf{m} = 4.0\times10^{-3}\,\hat{z}$ A·m². (b) $\mathbf{T} = 1.2\times10^{-3}\,\hat{y}$ N·m; net force zero. (c) The $x = 4$ cm edge sinks and the $x = 0$ edge rises; stable equilibrium with $\mathbf{m}$ parallel to $\mathbf{B}$ (loop tilted $36.9^\circ$ about $y$). (d) Along $-\hat{z}$; the field turns it toward $\mathbf{B}$ as well.

### 17.2 Four rods in a solenoid

> [!easy] Easy · multiple choice · permeability · magnetization
> Four long, thin rods are placed one at a time along the axis of a long solenoid whose winding produces $\mathbf{H} = 400\,\hat{z}$ A/m. Each rod lies along $\mathbf{H}$, so $\mathbf{H}$ inside it is also $400\,\hat{z}$ A/m. The measured magnetizations are: rod P, $\mathbf{M} = -3.76\times10^{-3}\,\hat{z}$ A/m; rod Q, $+8.4\times10^{-3}\,\hat{z}$ A/m; rod R, $+0.32\,\hat{z}$ A/m; rod S, $+2.0\times10^{5}\,\hat{z}$ A/m. Which classification is correct?
>
> (a) P diamagnetic; Q and R paramagnetic; S ferromagnetic
>
> (b) P paramagnetic; Q and R diamagnetic; S ferromagnetic
>
> (c) P diamagnetic; Q paramagnetic; R and S ferromagnetic
>
> (d) P diamagnetic; Q, R and S paramagnetic
>
> (e) P, Q and R non-magnetic; S ferromagnetic
>
> Then find $\chi_m$ and $\mu_r$ for each rod, $B$ inside S, and how much $B$ inside P differs from $B$ in the empty solenoid.
>
> *Source: Lecture 17 slides (the $\chi_m$ and $\mu_r$ tables), re-posed as a measurement.*

> [!hint]- Hint
> $\mathbf{M}$ and $\mathbf{H}$ are both in A/m, so $\chi_m = M/H$, with no $\mu_0$. The sign of $\chi_m$ separates dia from para; its size separates para from ferro.

> [!solution]- Solution
> **(a).** Divide each $M$ by $H = 400$ A/m, then $\mu_r = 1+\chi_m$:
>
> | rod | $\chi_m = M/H$ | $\mu_r$ | class (slides' material with this $\chi_m$) |
> |---|---|---|---|
> | P | $-9.4\times10^{-6}$ | 0.9999906 | diamagnetic (copper) |
> | Q | $+2.1\times10^{-5}$ | 1.000021 | paramagnetic (aluminum) |
> | R | $+8.0\times10^{-4}$ | 1.0008 | paramagnetic (palladium) |
> | S | $500$ | 501 | ferromagnetic (between cobalt and nickel) |
>
> Why the others fail. (b) swaps the signs: a *negative* $\chi_m$, with $\mathbf{M}$ opposing $\mathbf{H}$, is diamagnetism ("**Para** ↔ **Pos**itive"). (c) R's $\chi_m = 8\times10^{-4}$ is larger than Q's but still $\ll1$; ferromagnetism means $\chi_m\gg1$, from domains, and S's $\chi_m$ is $6.25\times10^5$ times R's. (d) puts S among the paramagnets, but partial alignment of single atomic moments against thermal agitation never gives $\chi_m = 500$. (e) "Non-magnetic" is everyday shorthand for $\mu\approx\mu_0$, which is true of P, Q and R in practice, but it is not one of the classes: strictly, only the vacuum has $\chi_m = 0$. P, Q and R have small but definite susceptibilities, and their signs classify them.
>
> **Fields.** In the empty solenoid $B = \mu_0H = 0.503$ mT. Inside S, $B = \mu_0(H+M) = \mu_0(400+2.0\times10^5) = 0.252$ T, 501 times more. Inside P, $B-\mu_0H = \mu_0M = -4.7\times10^{-9}$ T: the diamagnet lowers the 503 μT of the empty coil by 4.7 nT.
>
> **Watch out:** writing $\chi_m = M/(\mu_0H)$, by analogy with $\mathbf{P} = \epsilon_0\chi_e\mathbf{E}$, gives numbers $1/\mu_0\approx8\times10^5$ times too big. $\mathbf{M} = \chi_m\mathbf{H}$ has no $\mu_0$.
>
> **Answer.** (a). For P, Q, R, S: $\chi_m = -9.4\times10^{-6}$, $2.1\times10^{-5}$, $8.0\times10^{-4}$, 500 and $\mu_r = 0.9999906$, 1.000021, 1.0008, 501. $B = 0.252$ T inside S; $B$ inside P is 4.7 nT lower than in the empty coil.

### 17.3 Ferrite between sheets, find the error

> [!easy] Easy · find the error · current sheets · permeability
> Free current sheets $\mathbf{J}_s = 0.5\,\hat{x}$ A/m on the plane $z = 0$ and $\mathbf{J}_s = -0.5\,\hat{x}$ A/m on the plane $z = 4$ cm lie in air. A ferrite slab with $\mu = 500\mu_0$ fills $1<z<3$ cm. A student writes:
>
> "(1) The two sheets give $\mathbf{H} = -0.5\,\hat{y}$ A/m between them and zero outside. (2) At the faces of the slab the normal component of $\mathbf{B}$ is continuous, so $\mathbf{B}$ in the slab equals $\mathbf{B}$ in the air gaps, $\mathbf{B} = \mu_0(-0.5\,\hat{y}) = -0.628\,\hat{y}$ μT, and $\mathbf{H}_{\text{slab}} = \mathbf{B}/\mu = -1.0\times10^{-3}\,\hat{y}$ A/m. (3) $\mathbf{M} = \chi_m\mathbf{H}_{\text{slab}} = -0.499\,\hat{y}$ A/m. The ferrite hardly changes the field."
>
> What is wrong? Find the correct $\mathbf{H}$, $\mathbf{B}$ and $\mathbf{M}$ in the slab, and the magnetization current on its faces.
>
> *Source: original (the Lecture 17 slides' slab between two sheets, with air gaps, new numbers and a student slip).*

> [!hint]- Hint
> Which component of the field is normal to the faces $z = 1$ cm and $z = 3$ cm? Do those faces carry any free current?

> [!solution]- Solution
> **The slip is in step (2).** The faces are planes $z = $ const, so the normal component is $B_z$. It is zero on both sides, which makes it continuous but says nothing about $B_y$. The field runs *along* the faces, and for a tangential field the condition is $\hat{n}\times(\mathbf{H}_1-\mathbf{H}_2) = \mathbf{J}_s$. The faces carry no free current, so **tangential $\mathbf{H}$ is continuous**. Step (1) is right (check: $\tfrac12(0.5\,\hat{x})\times\hat{z}+\tfrac12(-0.5\,\hat{x})\times(-\hat{z}) = -0.5\,\hat{y}$ A/m between the sheets), and the formula in step (3) is right; it was fed the wrong $\mathbf{H}$.
>
> **Fix.** The free sheets set $\mathbf{H}$, and the slab cannot change it:
> $$
> \mathbf{H}_{\text{slab}} = -0.5\,\hat{y}\ \text{A/m},\qquad \mathbf{B}_{\text{slab}} = 500\mu_0(-0.5\,\hat{y}) = -3.14\times10^{-4}\,\hat{y}\ \text{T},\qquad \mathbf{M} = 499\,(-0.5\,\hat{y}) = -249.5\,\hat{y}\ \text{A/m}.
> $$
> In the air gaps $\mathbf{H} = -0.5\,\hat{y}$ A/m and $\mathbf{B} = -0.628\,\hat{y}$ μT; outside the sheets both vanish. $\mathbf{B}$ in the ferrite is 500 times $\mathbf{B}$ in the air.
>
> **Magnetization current** ($\mathbf{M}\times\hat{n}$ with outward normals): top face $z = 3$ cm, $(-249.5\,\hat{y})\times\hat{z} = -249.5\,\hat{x}$ A/m; bottom face $z = 1$ cm, $(-249.5\,\hat{y})\times(-\hat{z}) = +249.5\,\hat{x}$ A/m. Each runs the same way as the free sheet next to it.
>
> **Check:** free plus bound current is $\pm250$ A/m on each side of the slab, and the vacuum sheet formula gives $\mu_0\times250$ A/m $= 3.14\times10^{-4}$ T inside the slab. Outside the slab the two bound sheets cancel each other, leaving the gaps at $0.628$ μT ✓.
>
> **Watch out:** "normal $\mathbf{B}$ is continuous" decides the field when it *crosses* the slab. With the field along the faces, the slab behaves like a long core in a solenoid: same $\mathbf{H}$, and $\mu_r$ times the $\mathbf{B}$.
>
> **Answer.** The student applied the normal-$\mathbf{B}$ condition to a tangential field. Correct: $\mathbf{H} = -0.5\,\hat{y}$ A/m, $\mathbf{B} = -3.14\times10^{-4}\,\hat{y}$ T and $\mathbf{M} = -249.5\,\hat{y}$ A/m in the slab; $\mathbf{J}_{sM} = -249.5\,\hat{x}$ A/m on $z = 3$ cm and $+249.5\,\hat{x}$ A/m on $z = 1$ cm.

### 17.4 Reading a hysteresis loop

> [!easy] Easy · true or false · hysteresis · magnetization
> A permanent-magnet material is magnetized to saturation along $+z$, and then the magnetizing field is switched off. Its $B$–$H$ loop ($z$ components) has remanence $B_r = 0.4\pi\approx1.26$ T and coercivity $H_c = 8.0\times10^5$ A/m. True or false?
>
> (a) At the remanence point ($H = 0$, $B = B_r$) the magnetization is $M = 1.0\times10^6$ A/m.
>
> (b) At the coercive point of the same branch ($H = -H_c$, $B = 0$) the magnetization is zero.
>
> (c) On the saturated part of the loop, raising $H$ by $10^5$ A/m raises $B$ by about 0.126 T.
>
> (d) The material obeys $\mathbf{B} = \mu\mathbf{H}$ with a constant $\mu$.
>
> (e) It would make a good transformer core.
>
> (f) A paramagnet driven by the same coil traces a similar loop, only much narrower.
>
> *Source: original (course notes Lecture 17: hysteresis, remanence and permanent magnets).*

> [!hint]- Hint
> At every point of the loop, $M = B/\mu_0-H$. At saturation all the moments are already aligned, so $M$ cannot grow any further.

> [!solution]- Solution
> **(a) True.** $M = B_r/\mu_0-0 = 0.4\pi/(4\pi\times10^{-7}) = 1.0\times10^6$ A/m. That is what a permanent magnet is: $\mathbf{B}\neq0$ with $\mathbf{H} = 0$.
>
> **(b) False.** $M = 0/\mu_0-(-H_c) = +8.0\times10^5$ A/m, still along $+z$. The reverse field has not demagnetized the material; at this point $\mu_0\mathbf{H}$ just cancels $\mu_0\mathbf{M}$ in $\mathbf{B} = \mu_0(\mathbf{H}+\mathbf{M})$.
>
> **(c) True.** With $M$ stuck at its saturation value $M_s$, $B = \mu_0(H+M_s)$ grows only as $\mu_0\Delta H = 4\pi\times10^{-7}\times10^5 = 0.126$ T — the slope of vacuum.
>
> **(d) False.** $\mathbf{B} = \mu\mathbf{H}$ would give $B = 0$ at $H = 0$, and the loop has two values of $B$ for each $H$, depending on the history. A tabulated $\mu_r$ for a ferromagnet is only a small-field slope.
>
> **(e) False.** A transformer core goes round its loop 50 or 60 times a second, and the area of the loop is the energy turned into heat per cubic metre in every cycle. Cores use *soft* materials with narrow loops (small $H_c$); a wide loop like this one marks a *hard* material, made for permanent magnets.
>
> **(f) False.** A paramagnet has no domains and no memory: $\mathbf{M} = \chi_m\mathbf{H}$ is single-valued and vanishes with $\mathbf{H}$. Its "loop" is a straight line through the origin with slope $\mu_0(1+\chi_m)$.
>
> **Answer.** (a) True; (b) False; (c) True; (d) False; (e) False; (f) False.

### 17.5 A nickel rod as a solenoid

> [!easy] Easy · magnetization · magnetization current · sheets and solenoids
> A long nickel rod of radius $a = 5$ mm lies along the $z$ axis. It is magnetized to saturation along $+z$, and there is no free current anywhere. Nickel has $N = 9.14\times10^{28}$ atoms/m³, and at saturation each atom contributes on average $0.60\,\mu_B$ along $+z$, where $\mu_B = 9.27\times10^{-24}$ A·m² is the Bohr magneton.
>
> (a) Find $\mathbf{M}$.
>
> (b) Find the magnetization current density inside the rod and the magnetization surface current on its side and on its ends.
>
> (c) Find $\mathbf{B}$ and $\mathbf{H}$ inside the rod, far from its ends.
>
> (d) What current in a winding of 1000 turns per metre would produce the same $\mathbf{B}$ in an empty coil?
>
> *Source: course notes Lecture 17 ($\mathbf{M} = N\mathbf{m}$ and the stacked atomic loops), with nickel's numbers.*

> [!hint]- Hint
> $\mathbf{M} = N\mathbf{m}$, in A/m. A uniform $\mathbf{M}$ has no curl; on a surface $\mathbf{J}_{sM} = \mathbf{M}\times\hat{n}$ with $\hat{n}$ the outward normal ($\hat{r}$ on the side, $\pm\hat{z}$ on the ends).

> [!solution]- Solution
> **(a)** $\mathbf{M} = N\mathbf{m} = 9.14\times10^{28}\times0.60\times9.27\times10^{-24}\,\hat{z} = 5.08\times10^{5}\,\hat{z}$ A/m.
>
> **(b)** $\mathbf{M}$ is uniform, so $\mathbf{J}_M = \nabla\times\mathbf{M} = 0$: neighbouring atomic loops cancel inside. On the side, $\hat{n} = \hat{r}$ and $\mathbf{J}_{sM} = M\,\hat{z}\times\hat{r} = M\,\hat\phi = 5.08\times10^{5}\,\hat\phi$ A/m, circling the rod counter-clockwise as seen from $+z$. On the ends, $\hat{z}\times(\pm\hat{z}) = 0$: no current.
>
> **(c)** The side current is a solenoid winding with $nI\to M$, so inside, far from the ends, $\mathbf{B} = \mu_0\mathbf{M} = 0.639\,\hat{z}$ T. And $\mathbf{H} = \mathbf{B}/\mu_0-\mathbf{M} = 0$, as it must be: there is no free current, so Ampère's law around a rectangle with one long side inside the rod and one outside gives $H_{\text{in}} = H_{\text{out}} = 0$.
>
> **(d)** $nI = M$ gives $I = 5.08\times10^{5}/1000 = 508$ A in every turn — a measure of how much circulating current the aligned atomic moments represent.
>
> **Watch out:** $\mathbf{H} = 0$ inside a long magnet although $\mathbf{B} = 0.64$ T. $\mathbf{H}$ answers only to free current, and here all the current is magnetization current.
>
> **Answer.** (a) $\mathbf{M} = 5.08\times10^{5}\,\hat{z}$ A/m. (b) $\mathbf{J}_M = 0$; $\mathbf{J}_{sM} = 5.08\times10^{5}\,\hat\phi$ A/m on the side, none on the ends. (c) $\mathbf{B} = 0.639\,\hat{z}$ T, $\mathbf{H} = 0$. (d) 508 A.

## Medium

### 17.6 Graded magnetization in a slab

> [!medium] Medium · magnetization current · curl · current slab
> A magnetized slab fills $0<z<d$ with $d = 2$ cm and is unbounded in $x$ and $y$; outside is free space, and there is no free current anywhere. Its magnetization is $\mathbf{M} = M_0(z/d)^2\,\hat{x}$ with $M_0 = 3.0\times10^4$ A/m.
>
> (a) Find the magnetization current density $\mathbf{J}_M$ in the slab and the magnetization surface current $\mathbf{J}_{sM}$ on each face.
>
> (b) Show that the total magnetization current crossing the plane $y = 0$ is zero (per metre of length along $x$).
>
> (c) Find $\mathbf{H}$ and $\mathbf{B}$ everywhere. Evaluate $\mathbf{B}$ at $z = 1$ cm, just below the top face and just above it.
>
> (d) Check $\mathbf{B}$ at $z = 1$ cm by adding up the fields of all the magnetization currents, treated as current sheets.
>
> *Source: original.*

> [!hint]- Hint
> With only $M_x(z)$, the curl has a single component, $(\nabla\times\mathbf{M})_y = \partial M_x/\partial z$. On each face use $\mathbf{M}\times\hat{n}$ with the outward normal. For (c): there is no free current, and nothing depends on $x$ or $y$. What does $\nabla\times\mathbf{H} = 0$ leave for $\mathbf{H}$?

> [!solution]- Solution
> **Setup.** $\mathbf{M}$ depends on $z$ only and points along $x$, so every bound current runs along $\pm\hat{y}$, like a stack of current sheets.
>
> **(a)**
> $$
> \mathbf{J}_M = \nabla\times\mathbf{M} = \frac{\partial M_x}{\partial z}\,\hat{y} = \frac{2M_0z}{d^2}\,\hat{y} = 1.5\times10^{8}\,z\ \hat{y}\ \text{A/m}^2\quad(z\text{ in m}),
> $$
> rising from 0 at the bottom to $1.5\times10^6$ A/m² at $z = 1$ cm and $3.0\times10^6$ A/m² at the top. Top face, $\hat{n} = +\hat{z}$: $\mathbf{J}_{sM} = M_0\,\hat{x}\times\hat{z} = -M_0\,\hat{y} = -3.0\times10^4\,\hat{y}$ A/m. Bottom face: $\mathbf{M}(0) = 0$, no current.
>
> **(b)** Per metre along $x$, the volume current through $y = 0$ is $\displaystyle\int_0^d\frac{2M_0z}{d^2}\,dz = M_0 = 3.0\times10^4$ A along $+\hat{y}$, and the top face returns $3.0\times10^4$ A along $-\hat{y}$. Net zero ✓. This holds for any profile: $\int_0^d\partial_zM_x\,dz = M_x(d)-M_x(0)$ is cancelled exactly by the face currents $-M_x(d)$ on top and $+M_x(0)$ at the bottom.
>
> **(c)** There is no free current, so $\nabla\times\mathbf{H} = 0$. With everything depending on $z$ only, this makes $H_x$ and $H_y$ constant, and $\nabla\cdot\mathbf{B} = 0$ makes $B_z = \mu_0H_z$ constant too ($M_z = 0$). All of them vanish far from the slab, so $\mathbf{H} = 0$ **everywhere**, and
> $$
> \mathbf{B} = \mu_0(\mathbf{H}+\mathbf{M}) = \mu_0M_0\Big(\frac zd\Big)^2\hat{x}\ \ (0<z<d),\qquad \mathbf{B} = 0\ \ \text{outside}.
> $$
> At $z = 1$ cm, $\mu_0M_0/4 = 9.42$ mT along $\hat{x}$; just below the top, $\mu_0M_0 = 37.7$ mT; just above, 0. The face current carries the jump: $\hat{z}\times(0-\mu_0M_0\,\hat{x})/\mu_0 = -M_0\,\hat{y} = \mathbf{J}_{sM}$ ✓.
>
> **(d)** A layer $dz'$ at height $z'$ is a sheet $J_M\,dz'\,\hat{y}$; by $\tfrac{\mu_0}{2}\mathbf{J}_s\times\hat{n}$ it gives $+\tfrac{\mu_0}{2}J_M\,dz'\,\hat{x}$ above itself and $-\tfrac{\mu_0}{2}J_M\,dz'\,\hat{x}$ below. At $z = d/2$, in units of $\mu_0M_0/2$: the layers below carry $M_0/4$ and give $+\tfrac14$; the layers above carry $3M_0/4$ and give $-\tfrac34$; the top sheet $-M_0\,\hat{y}$ lies above the point and gives $+1$. So
> $$
> B_x\Big(\frac d2\Big) = \frac{\mu_0M_0}{2}\Big(\frac14-\frac34+1\Big) = \frac{\mu_0M_0}{4}\ \checkmark
> $$
> **Watch out:** $\mathbf{H} = 0$ while $\mathbf{B}\neq0$ is no contradiction, since $\mathbf{H}$ answers only to free current. The bound currents form a closed system (every ampere flowing along $+\hat{y}$ inside returns along $-\hat{y}$ on the top face), so their field stays inside, like the field of a solenoid.
>
> **Answer.** $\mathbf{J}_M = (2M_0z/d^2)\,\hat{y} = 1.5\times10^{8}\,z\,\hat{y}$ A/m²; $\mathbf{J}_{sM} = -3.0\times10^4\,\hat{y}$ A/m on $z = d$ and none on $z = 0$; net current zero. $\mathbf{H} = 0$ everywhere; $\mathbf{B} = \mu_0M_0(z/d)^2\,\hat{x}$ inside and 0 outside: 9.42 mT at $z = 1$ cm, 37.7 mT just below the top face, 0 just above.

### 17.7 A wire of magnetic steel

> [!medium] Medium · magnetization current · Ampère's law · internal inductance
> A long straight wire of radius $a = 1$ mm along the $z$ axis is made of a steel with $\mu = 200\mu_0$ (treat it as linear). It carries a free current $I = 5$ A along $+\hat{z}$, spread uniformly over its cross-section; outside is air.
>
> (a) Find $\mathbf{H}$ and $\mathbf{B}$ inside and outside the wire, and evaluate $B$ just inside and just outside $r = a$.
>
> (b) Find $\mathbf{M}$, the magnetization current density inside the wire, the magnetization surface current on it, and the total magnetization current along the wire.
>
> (c) Put free plus magnetization current into the vacuum form of Ampère's law to recover $\mathbf{B}$ inside and outside. Does a steel wire have a different field outside than a copper wire carrying the same current?
>
> (d) Find the internal inductance per unit length. (Lecture 15 gave $\mu_0/8\pi$ for a non-magnetic wire.)
>
> *Source: classic (a current-carrying magnetic wire), new numbers.*

> [!hint]- Hint
> Ampère's law for $\mathbf{H}$ needs only the free current enclosed: $H_\phi\cdot2\pi r = I\,r^2/a^2$ inside. Then $\mathbf{B} = \mu\mathbf{H}$ and $\mathbf{M} = \chi_m\mathbf{H}$ with $\chi_m = 199$; in cylindrical coordinates $(\nabla\times\mathbf{M})_z = \dfrac1r\dfrac{d}{dr}(rM_\phi)$.

> [!solution]- Solution
> **Setup.** Cylindrical symmetry and the right-hand rule give $\mathbf{H} = H_\phi(r)\hat\phi$. Ampère's law on a circle of radius $r$ counts free current only, whatever the wire is made of.
>
> **(a)**
> $$
> \mathbf{H} = \frac{Ir}{2\pi a^2}\,\hat\phi\ \ (r<a),\qquad \mathbf{H} = \frac{I}{2\pi r}\,\hat\phi\ \ (r>a);\qquad \mathbf{B} = 200\mu_0\mathbf{H}\ \ (r<a),\qquad \mathbf{B} = \mu_0\mathbf{H}\ \ (r>a).
> $$
> At $r = a$, $H = I/(2\pi a) = 795.8$ A/m on both sides (tangential $\mathbf{H}$ is continuous, as there is no free surface current), while $B = 0.200$ T just inside and $1.00$ mT just outside.
>
> **(b)** $\mathbf{M} = \chi_m\mathbf{H} = 199\,\dfrac{Ir}{2\pi a^2}\,\hat\phi$, reaching $1.58\times10^5$ A/m at the surface. Inside,
> $$
> \mathbf{J}_M = \frac1r\frac{d}{dr}\big(rM_\phi\big)\,\hat{z} = 199\,\frac{I}{\pi a^2}\,\hat{z} = \chi_m\mathbf{J}_f = 3.17\times10^{8}\,\hat{z}\ \text{A/m}^2,
> $$
> uniform and in the direction of the free current ($J_f = 1.59\times10^6$ A/m²), carrying $\chi_mI = 995$ A in all. On the surface, $\hat{n} = \hat{r}$: $\mathbf{J}_{sM} = M(a)\,\hat\phi\times\hat{r} = -1.58\times10^{5}\,\hat{z}$ A/m, carrying $-1.58\times10^5\times2\pi a = -995$ A. Net magnetization current: zero ✓.
>
> **(c)** Inside, the total current through a circle of radius $r$ is $(I+995\ \text{A})\,r^2/a^2 = 200\,I\,r^2/a^2$, so $B_\phi = \mu_0\cdot200\,Ir/(2\pi a^2) = \mu H$ ✓. Outside, the circle encloses $I+995-995$ A $= I$, so $B = \mu_0I/(2\pi r)$, **the same as for copper**. The steel concentrates $B$ inside the wire, but its magnetization current returns along its own surface, so nothing outside notices it.
>
> **(d)** The energy per metre inside the wire is
> $$
> W' = \int_0^a\tfrac12\mu\Big(\frac{Ir}{2\pi a^2}\Big)^2 2\pi r\,dr = \frac{\mu I^2}{16\pi},\qquad \mathcal{L}_{\text{int}} = \frac{2W'}{I^2} = \frac{\mu}{8\pi} = 200\times5.0\times10^{-8} = 1.0\times10^{-5}\ \text{H/m},
> $$
> that is 10 μH/m instead of copper's 0.05 μH/m ($W' = 1.25\times10^{-4}$ J/m at 5 A). Inductance grows with $\mu$ wherever the flux runs through the material.
>
> **Check:** at $r = a$ the surface current carries the jump in tangential $\mathbf{B}$: $\hat{r}\times(\mathbf{B}_{\text{out}}-\mathbf{B}_{\text{in}})/\mu_0 = \hat{r}\times(-0.199\ \text{T}\ \hat\phi)/\mu_0 = -1.58\times10^5\,\hat{z}$ A/m $= \mathbf{J}_{sM}$ ✓.
>
> **Answer.** $\mathbf{H} = Ir/(2\pi a^2)\,\hat\phi$ inside and $I/(2\pi r)\,\hat\phi$ outside; $\mathbf{B} = \mu\mathbf{H}$ inside and $\mu_0\mathbf{H}$ outside, 0.200 T just inside and 1.00 mT just outside. $\mathbf{M} = 199\,Ir/(2\pi a^2)\,\hat\phi$; $\mathbf{J}_M = 3.17\times10^8\,\hat{z}$ A/m² (995 A) and $\mathbf{J}_{sM} = -1.58\times10^5\,\hat{z}$ A/m ($-995$ A), net zero. The field outside is that of a copper wire. $\mathcal{L}_{\text{int}} = \mu/8\pi = 10$ μH/m.

### 17.8 Field lines leaving iron

> [!medium] Medium · magnetic boundary conditions · permeability · magnetization current
> The region $y<0$ is iron with $\mu = 2000\mu_0$ (treat it as linear), the region $y>0$ is air, and the surface $y = 0$ carries no free current. Just inside the iron, at a point of the surface,
> $$
> \mathbf{B}_{\text{iron}} = 0.8\,\hat{x}+0.01\,\hat{y}-0.6\,\hat{z}\ \text{T}.
> $$
> (a) Find $\mathbf{H}$ in the iron, and $\mathbf{B}$ and $\mathbf{H}$ just outside, in the air.
>
> (b) Find the angle between $\mathbf{B}$ and the surface normal on each side, and check the refraction law.
>
> (c) Find $\mathbf{M}$ in the iron and the magnetization current on the surface, and check that it accounts for the jump in tangential $\mathbf{B}$.
>
> *Source: original (the iron-surface refraction of Lecture 17 §6, with B given inside the iron).*

> [!hint]- Hint
> Call the air medium 1 and the iron medium 2, so that $\hat{n} = +\hat{y}$ points from 2 into 1. The normal component is the $y$ component: copy $B_y$ across, and copy $H_x$ and $H_z$ across.

> [!solution]- Solution
> **Setup.** Normal: $y$. Tangential: $x$ and $z$. Two rules: $B_n$ is always continuous; $\mathbf{H}_t$ is continuous because the surface carries no free current.
>
> **(a)** In the iron, $\mathbf{H}_2 = \mathbf{B}_{\text{iron}}/(2000\mu_0) = 318.3\,\hat{x}+3.98\,\hat{y}-238.7\,\hat{z}$ A/m. In the air, $H_x = 318.3$ A/m and $H_z = -238.7$ A/m are copied, and $B_y = 0.01$ T is copied, so $H_y = 0.01/\mu_0 = 7958$ A/m:
> $$
> \mathbf{H}_1 = 318.3\,\hat{x}+7958\,\hat{y}-238.7\,\hat{z}\ \text{A/m},\qquad \mathbf{B}_1 = \mu_0\mathbf{H}_1 = 0.4\,\hat{x}+10\,\hat{y}-0.3\,\hat{z}\ \text{mT}.
> $$
> **(b)** In the iron, $\lvert\mathbf{B}_t\rvert = 1.0$ T against $B_n = 0.01$ T: $\tan\theta_2 = 100$ and $\theta_2 = 89.43^\circ$, so the field runs almost along the surface. In the air, $\lvert\mathbf{B}_t\rvert = 0.5$ mT against $B_n = 10$ mT: $\tan\theta_1 = 0.05$ and $\theta_1 = 2.86^\circ$, so the field leaves almost perpendicularly. Check: $\tan\theta_1/\tan\theta_2 = 0.05/100 = 1/2000 = \mu_1/\mu_2$ ✓.
>
> **(c)** $\mathbf{M}_2 = \mathbf{B}_{\text{iron}}/\mu_0-\mathbf{H}_2 = 1999\,\mathbf{H}_2 = 6.363\times10^5\,\hat{x}+7.95\times10^3\,\hat{y}-4.772\times10^5\,\hat{z}$ A/m, and $\mathbf{M}_1 = 0$. On the interface
> $$
> \mathbf{J}_{sM} = \hat{n}\times(\mathbf{M}_1-\mathbf{M}_2) = -\hat{y}\times\mathbf{M}_2 = 4.772\times10^{5}\,\hat{x}+6.363\times10^{5}\,\hat{z}\ \text{A/m},
> $$
> of magnitude $7.95\times10^5$ A/m. It is the same as $\mathbf{M}_2\times\hat{n}$ for the iron's own face, whose outward normal is $+\hat{y}$. Check: $\mathbf{B}_1-\mathbf{B}_2 = -0.7996\,\hat{x}+0.5997\,\hat{z}$ T, and
> $$
> \frac{\hat{y}\times(\mathbf{B}_1-\mathbf{B}_2)}{\mu_0} = \frac{0.5997\,\hat{x}+0.7996\,\hat{z}}{\mu_0} = 4.772\times10^5\,\hat{x}+6.363\times10^5\,\hat{z}\ \text{A/m} = \mathbf{J}_s+\mathbf{J}_{sM}\quad(\mathbf{J}_s = 0)\ \checkmark
> $$
> The normal part of $\mathbf{M}$ drives no current. It shows up instead as the jump of $H_y$, from 3.98 to 7958 A/m.
>
> **Watch out:** "no surface current, so $\mathbf{B}$ is continuous" is wrong twice. Only $B_n$ is continuous, and there *is* a surface current, a bound one. Here tangential $\mathbf{B}$ drops 2000-fold across the surface.
>
> **Answer.** (a) $\mathbf{H}_{\text{iron}} = 318.3\,\hat{x}+3.98\,\hat{y}-238.7\,\hat{z}$ A/m; in the air $\mathbf{B} = 0.4\,\hat{x}+10\,\hat{y}-0.3\,\hat{z}$ mT and $\mathbf{H} = 318.3\,\hat{x}+7958\,\hat{y}-238.7\,\hat{z}$ A/m. (b) $89.43^\circ$ in the iron and $2.86^\circ$ in the air; the ratio of the tangents is $1/2000 = \mu_1/\mu_2$. (c) $\mathbf{M} = 6.363\times10^5\,\hat{x}+7.95\times10^3\,\hat{y}-4.772\times10^5\,\hat{z}$ A/m; $\mathbf{J}_{sM} = 4.772\times10^5\,\hat{x}+6.363\times10^5\,\hat{z}$ A/m.

## Hard

### 17.9 Electret and magnet twins

> [!hard] Hard · bound charge · magnetization current · displacement current
> Two long cylinders of radius $a = 1$ cm lie along the $z$ axis, each on its own in free space; neither carries free charge or free current.
>
> Cylinder A, an electret, has a frozen-in radial polarization $\mathbf{P} = P_0(r/a)^2\,\hat{r}$ for $r<a$, with $P_0 = 2.0$ μC/m².
>
> Cylinder B, a permanent magnet, has a frozen-in azimuthal magnetization $\mathbf{M} = M_0(r/a)^2\,\hat\phi$ for $r<a$, with $M_0 = 5.0\times10^4$ A/m.
>
> (a) Find the bound charge densities of A and show that its total bound charge is zero.
>
> (b) Find the magnetization currents of B and show that its total magnetization current along $z$ is zero.
>
> (c) Find $\mathbf{D}$ and $\mathbf{E}$ of A, and $\mathbf{H}$ and $\mathbf{B}$ of B, inside and outside. Evaluate $\mathbf{E}$ and $\mathbf{B}$ at $r = a/2$ and just inside $r = a$.
>
> (d) In each cylinder, does the field of the bound sources point along the dipole density or against it? Relate the answer to $\mathbf{D} = \epsilon_0\mathbf{E}+\mathbf{P}$ and $\mathbf{H} = \mathbf{B}/\mu_0-\mathbf{M}$.
>
> (e) A's polarization now grows slowly, at $dP_0/dt = 0.4$ μC/(m²·s). Write A's current density $\mathbf{J} = \mathbf{J}_f+\partial\mathbf{P}/\partial t+\nabla\times\mathbf{M}$, check charge conservation for its bound charge, and show that A makes no magnetic field although its bound charge moves.
>
> *Source: original (the slides' "M → P" pairing, posed as twin problems).*

> [!hint]- Hint
> In cylindrical coordinates $\nabla\cdot\mathbf{P} = \dfrac1r\dfrac{d}{dr}(rP_r)$ and $(\nabla\times\mathbf{M})_z = \dfrac1r\dfrac{d}{dr}(rM_\phi)$; on the surface $\rho_{sb} = \mathbf{P}\cdot\hat{r}$ and $\mathbf{J}_{sM} = \mathbf{M}\times\hat{r}$. For (c), Gauss's law for $\mathbf{D}$ and Ampère's law for $\mathbf{H}$ count only free sources, and there are none.

> [!solution]- Solution
> **(a)**
> $$
> \rho_b = -\frac1r\frac{d}{dr}\Big(r\,\frac{P_0r^2}{a^2}\Big) = -\frac{3P_0r}{a^2},\qquad \rho_{sb} = \mathbf{P}\cdot\hat{r}\,\Big|_{r=a} = P_0 = 2.0\ \mu\text{C/m}^2 .
> $$
> ($\rho_b = -3.0\times10^{-4}$ C/m³ at $r = a/2$.) Per metre of length the volume holds $\displaystyle\int_0^a-\frac{3P_0r}{a^2}\,2\pi r\,dr = -2\pi aP_0 = -1.26\times10^{-7}$ C/m and the surface $+2\pi aP_0 = +1.26\times10^{-7}$ C/m, so 126 nC/m each way and zero in total ✓.
>
> **(b)**
> $$
> \mathbf{J}_M = \frac1r\frac{d}{dr}\Big(r\,\frac{M_0r^2}{a^2}\Big)\hat{z} = \frac{3M_0r}{a^2}\,\hat{z},\qquad \mathbf{J}_{sM} = M_0\,\hat\phi\times\hat{r} = -M_0\,\hat{z} = -5.0\times10^4\,\hat{z}\ \text{A/m}.
> $$
> ($J_M = 7.5\times10^6$ A/m² at $r = a/2$.) The volume carries $\displaystyle\int_0^a\frac{3M_0r}{a^2}\,2\pi r\,dr = 2\pi aM_0 = 3.14\times10^3$ A along $+z$, and the surface carries $3.14\times10^3$ A back along $-z$: zero in total ✓.
>
> **(c)** *Cylinder A.* Symmetry gives $\mathbf{D} = D_r(r)\hat{r}$, and Gauss's law on a coaxial cylinder encloses no free charge, so $\mathbf{D} = 0$ everywhere. Then
> $$
> \mathbf{E} = \frac{\mathbf{D}-\mathbf{P}}{\epsilon_0} = -\frac{\mathbf{P}}{\epsilon_0} = -\frac{P_0}{\epsilon_0}\Big(\frac ra\Big)^2\hat{r}\ \ (r<a),\qquad \mathbf{E} = 0\ \ (r>a).
> $$
> At $r = a/2$, $\mathbf{E} = -P_0/(4\epsilon_0)\,\hat{r} = -5.65\times10^4\,\hat{r}$ V/m, pointing inward; just inside $r = a$, $-2.26\times10^5\,\hat{r}$ V/m.
>
> *Cylinder B.* Symmetry and $\nabla\cdot\mathbf{B} = 0$ leave only $H_\phi(r)$ and $H_z(r)$; with no free current $\nabla\times\mathbf{H} = 0$ makes $H_z$ a constant, which must vanish far away. Ampère's law on a coaxial circle encloses no free current, so $\mathbf{H} = 0$ everywhere, and
> $$
> \mathbf{B} = \mu_0(\mathbf{H}+\mathbf{M}) = \mu_0M_0\Big(\frac ra\Big)^2\hat\phi\ \ (r<a),\qquad \mathbf{B} = 0\ \ (r>a).
> $$
> At $r = a/2$, $\mu_0M_0/4 = 15.7$ mT along $\hat\phi$; just inside $r = a$, 62.8 mT.
>
> **Check** with the bound sources in the vacuum laws: $\epsilon_0E_r\cdot2\pi r = -2\pi P_0r^3/a^2$ (the bound charge inside radius $r$, per metre) and $B_\phi\cdot2\pi r = \mu_0\cdot2\pi M_0r^3/a^2$ (the magnetization current inside $r$) give the same fields, and so does a direct superposition of line charges and line currents, including zero outside.
>
> **(d)** In A, $\mathbf{E} = -\mathbf{P}/\epsilon_0$ points **against** $\mathbf{P}$; in B, $\mathbf{B} = +\mu_0\mathbf{M}$ points **along** $\mathbf{M}$. Both follow from an auxiliary field that vanishes: $\mathbf{D} = \epsilon_0\mathbf{E}+\mathbf{P} = 0$ puts a minus sign in $\mathbf{E}$, while $\mathbf{H} = \mathbf{B}/\mu_0-\mathbf{M} = 0$ puts a plus sign in $\mathbf{B}$. Physically, between its two charges a dipole's field runs from $+$ to $-$, against $\mathbf{p}$, while inside a current loop the field runs along $\mathbf{m}$. That is why a dielectric weakens $\mathbf{E}$ while a para- or ferromagnet strengthens $\mathbf{B}$.
>
> **(e)** A has no free current and no magnetization, so $\mathbf{J} = \partial\mathbf{P}/\partial t = \dfrac{dP_0}{dt}\Big(\dfrac ra\Big)^2\hat{r}$, an outward current of bound charge (0.1 μA/m² at $r = a/2$). Charge conservation:
> $$
> \frac{\partial\rho_b}{\partial t}+\nabla\cdot\frac{\partial\mathbf{P}}{\partial t} = -\frac{3r}{a^2}\frac{dP_0}{dt}+\frac{3r}{a^2}\frac{dP_0}{dt} = 0\ \checkmark
> $$
> At $r = a$ the current delivers 0.4 μC/m² per second to the surface, exactly the growth rate of $\rho_{sb} = P_0$. For the magnetic field: $\mathbf{D} = 0$ at every instant, so $\nabla\times\mathbf{H} = \mathbf{J}_f+\partial\mathbf{D}/\partial t = 0$, and the symmetry argument of (c) gives $\mathbf{H} = 0$ and $\mathbf{B} = \mu_0\mathbf{H} = 0$. In the vacuum form, the polarization current is cancelled point by point by the vacuum displacement current: $\epsilon_0\,\partial\mathbf{E}/\partial t = -\partial\mathbf{P}/\partial t$ ($-0.1$ μA/m² at $r = a/2$), so $\partial\mathbf{P}/\partial t+\epsilon_0\,\partial\mathbf{E}/\partial t = \partial\mathbf{D}/\partial t = 0$.
>
> **Answer.** (a) $\rho_b = -3P_0r/a^2$ and $\rho_{sb} = P_0$: $-126$ and $+126$ nC/m, total zero. (b) $\mathbf{J}_M = (3M_0r/a^2)\,\hat{z}$ and $\mathbf{J}_{sM} = -M_0\,\hat{z}$: $+3.14$ and $-3.14$ kA, total zero. (c) $\mathbf{D} = 0$ and $\mathbf{E} = -\mathbf{P}/\epsilon_0$ ($-5.65\times10^4\,\hat{r}$ V/m at $a/2$, $-2.26\times10^5\,\hat{r}$ V/m just inside $a$); $\mathbf{H} = 0$ and $\mathbf{B} = \mu_0\mathbf{M}$ (15.7 mT along $\hat\phi$ at $a/2$, 62.8 mT just inside $a$); all fields zero outside. (d) $\mathbf{E}$ opposes $\mathbf{P}$; $\mathbf{B}$ follows $\mathbf{M}$. (e) $\mathbf{J} = \partial\mathbf{P}/\partial t$; continuity holds; $\partial\mathbf{D}/\partial t = 0$, so $\mathbf{B} = 0$.

### 17.10 Three sheets and two slabs

> [!hard] Hard · current sheets · magnetic boundary conditions · magnetization current
> Three infinite sheets carry free surface currents: $\mathbf{J}_{s1} = 4\,\hat{y}$ A/m on $z = 0$, $\mathbf{J}_{s2} = 3\,\hat{x}-4\,\hat{y}$ A/m on $z = 2$ cm, and $\mathbf{J}_{s3} = -3\,\hat{x}$ A/m on $z = 4$ cm. The slab $0<z<2$ cm is a linear magnetic material with $\mu = 25\mu_0$, the slab $2<z<4$ cm one with $\mu = 10\mu_0$; outside is air.
>
> (a) Find $\mathbf{H}$ in the four regions $z<0$, $0<z<2$ cm, $2<z<4$ cm and $z>4$ cm. Why do the slabs not change it?
>
> (b) Find $\mathbf{B}$ and $\mathbf{M}$ in each slab.
>
> (c) Verify the boundary conditions at $z = 2$ cm, and find the jump in tangential $\mathbf{B}$ there.
>
> (d) Find the magnetization surface currents on the planes $z = 0$, 2 and 4 cm and show that they add up to zero. Check that free plus magnetization currents, put into the vacuum sheet formula, give the $\mathbf{B}$ of part (b) in both slabs.
>
> (e) If the lower slab were bismuth ($\chi_m = -1.7\times10^{-4}$) instead, what magnetization current would flow on its face $z = 0$, compared with $\mathbf{J}_{s1}$?
>
> *Source: Lecture 17 slides, the slab between two sheets, re-posed with three sheets and two slabs (original numbers); the step across the middle sheet is SP18 Exam 2 #1(vi) style.*

> [!hint]- Hint
> Each sheet contributes $\tfrac12\mathbf{J}_s\times\hat{n}$, with $\hat{n}$ from the sheet toward the field point. At $z = 2$ cm call the upper slab medium 1 and the lower slab medium 2, so that $\hat{n} = +\hat{z}$. Each face of a magnetized body carries $\mathbf{M}\times\hat{n}_{\text{out}}$, with its own outward normal.

> [!solution]- Solution
> **(a)** First note that $\mathbf{J}_{s1}+\mathbf{J}_{s2}+\mathbf{J}_{s3} = 0$, so below and above all three sheets the contributions cancel: $\mathbf{H} = 0$ for $z<0$ and for $z>4$ cm. Between the sheets:
> $$
> \begin{aligned}
> 0<z<2\ \text{cm}:&\quad \tfrac12(4\,\hat{y})\times\hat{z}+\tfrac12(3\,\hat{x}-4\,\hat{y}-3\,\hat{x})\times(-\hat{z}) = 2\,\hat{x}+2\,\hat{x} = 4\,\hat{x}\ \text{A/m},\\
> 2<z<4\ \text{cm}:&\quad \tfrac12(4\,\hat{y}+3\,\hat{x}-4\,\hat{y})\times\hat{z}+\tfrac12(-3\,\hat{x})\times(-\hat{z}) = -1.5\,\hat{y}-1.5\,\hat{y} = -3\,\hat{y}\ \text{A/m}.
> \end{aligned}
> $$
> This $\mathbf{H}$ is parallel to every face, so it meets every boundary condition by itself: $B_n = 0$ on both sides of each face, $\mathbf{H}_t$ continuous where there is no free current, and a jump of exactly the free $\mathbf{J}_s$ where a sheet sits. A field that meets all the conditions is *the* field (uniqueness), so the slabs change $\mathbf{B}$ but not $\mathbf{H}$.
>
> **(b)**
> $$
> \begin{aligned}
> 0<z<2\ \text{cm}:&\quad \mathbf{B} = 25\mu_0(4\,\hat{x}) = 100\mu_0\,\hat{x} = 1.26\times10^{-4}\,\hat{x}\ \text{T},\qquad \mathbf{M} = 24\,(4\,\hat{x}) = 96\,\hat{x}\ \text{A/m};\\
> 2<z<4\ \text{cm}:&\quad \mathbf{B} = 10\mu_0(-3\,\hat{y}) = -30\mu_0\,\hat{y} = -3.77\times10^{-5}\,\hat{y}\ \text{T},\qquad \mathbf{M} = 9\,(-3\,\hat{y}) = -27\,\hat{y}\ \text{A/m}.
> \end{aligned}
> $$
> **(c)** With $\hat{n} = \hat{z}$: $\hat{n}\times(\mathbf{H}_1-\mathbf{H}_2) = \hat{z}\times(-4\,\hat{x}-3\,\hat{y}) = 3\,\hat{x}-4\,\hat{y} = \mathbf{J}_{s2}$ ✓ (the step of SP18 Exam 2 #1(vi)), and $\hat{n}\cdot(\mathbf{B}_1-\mathbf{B}_2) = 0-0 = 0$ ✓. Tangential $\mathbf{B}$ jumps by $\mathbf{B}_1-\mathbf{B}_2 = -100\mu_0\,\hat{x}-30\mu_0\,\hat{y} = -1.26\times10^{-4}\,\hat{x}-3.77\times10^{-5}\,\hat{y}$ T, much more than the free sheet accounts for:
> $$
> \frac{\hat{n}\times(\mathbf{B}_1-\mathbf{B}_2)}{\mu_0} = \hat{z}\times(-100\,\hat{x}-30\,\hat{y}) = 30\,\hat{x}-100\,\hat{y}\ \text{A/m},
> $$
> 20.9 times $\lvert\mathbf{J}_{s2}\rvert = 5$ A/m.
>
> **(d)** Each face carries $\mathbf{M}\times\hat{n}_{\text{out}}$:
> - $z = 0$, bottom face of the lower slab ($\hat{n}_{\text{out}} = -\hat{z}$): $96\,\hat{x}\times(-\hat{z}) = 96\,\hat{y}$ A/m, the same sense as $\mathbf{J}_{s1}$;
> - $z = 2$ cm, the two faces together: $\hat{z}\times(\mathbf{M}_1-\mathbf{M}_2) = \hat{z}\times(-27\,\hat{y}-96\,\hat{x}) = 27\,\hat{x}-96\,\hat{y}$ A/m;
> - $z = 4$ cm, top face of the upper slab ($\hat{n}_{\text{out}} = +\hat{z}$): $(-27\,\hat{y})\times\hat{z} = -27\,\hat{x}$ A/m, the same sense as $\mathbf{J}_{s3}$.
>
> Sum: $96\,\hat{y}+(27\,\hat{x}-96\,\hat{y})-27\,\hat{x} = 0$ ✓. At $z = 2$ cm, free plus bound is $(3\,\hat{x}-4\,\hat{y})+(27\,\hat{x}-96\,\hat{y}) = 30\,\hat{x}-100\,\hat{y}$ A/m, exactly the $\hat{n}\times(\mathbf{B}_1-\mathbf{B}_2)/\mu_0$ found in (c). The total sheets are $100\,\hat{y}$, $30\,\hat{x}-100\,\hat{y}$ and $-30\,\hat{x}$ A/m, and the vacuum formula $\tfrac{\mu_0}{2}\mathbf{J}_s\times\hat{n}$ gives
> $$
> \begin{aligned}
> 0<z<2\ \text{cm}:&\quad \tfrac{\mu_0}{2}\big[(100\,\hat{y})\times\hat{z}+(-100\,\hat{y})\times(-\hat{z})\big] = 100\mu_0\,\hat{x},\\
> 2<z<4\ \text{cm}:&\quad \tfrac{\mu_0}{2}\big[(30\,\hat{x})\times\hat{z}+(-30\,\hat{x})\times(-\hat{z})\big] = -30\mu_0\,\hat{y}\ \checkmark
> \end{aligned}
> $$
> (in each bracket, the sum of the sheets below the point, then the sum of those above), and zero outside, since the three totals add up to zero. The magnetic materials have been replaced by currents in vacuum, and the field is the same.
>
> **(e)** $\mathbf{M} = \chi_m\mathbf{H} = -1.7\times10^{-4}\,(4\,\hat{x}) = -6.8\times10^{-4}\,\hat{x}$ A/m, and on $z = 0$, $\mathbf{M}\times(-\hat{z}) = -6.8\times10^{-4}\,\hat{y}$ A/m: **opposite** to $\mathbf{J}_{s1} = 4\,\hat{y}$ A/m. A diamagnet's bound current opposes the free current beside it and slightly weakens $\mathbf{B}$; a para- or ferromagnet's reinforces it.
>
> **Answer.** (a) $\mathbf{H} = 0$, $4\,\hat{x}$, $-3\,\hat{y}$ and 0 A/m. (b) Lower slab: $\mathbf{B} = 1.26\times10^{-4}\,\hat{x}$ T, $\mathbf{M} = 96\,\hat{x}$ A/m; upper slab: $\mathbf{B} = -3.77\times10^{-5}\,\hat{y}$ T, $\mathbf{M} = -27\,\hat{y}$ A/m. (c) Both conditions hold; tangential $\mathbf{B}$ jumps by $\mathbf{B}_1-\mathbf{B}_2 = -1.26\times10^{-4}\,\hat{x}-3.77\times10^{-5}\,\hat{y}$ T, so $\hat{n}\times(\mathbf{B}_1-\mathbf{B}_2)/\mu_0 = 30\,\hat{x}-100\,\hat{y}$ A/m, 20.9 times $\lvert\mathbf{J}_{s2}\rvert$. (d) $\mathbf{J}_{sM} = 96\,\hat{y}$, $27\,\hat{x}-96\,\hat{y}$ and $-27\,\hat{x}$ A/m on $z = 0$, 2 and 4 cm (sum zero). (e) $-6.8\times10^{-4}\,\hat{y}$ A/m, opposite to $\mathbf{J}_{s1}$.

### 17.11 A toroid with an air gap

> [!hard] Hard · toroid · magnetic boundary conditions · permeability
> A thin iron ring (linear, $\mu = 4000\mu_0$) has mean radius $R = 5$ cm and cross-sectional area $A = 1$ cm². A narrow radial air gap of width $g = 1$ mm is cut through it. $N = 250$ turns are wound on the ring and carry $I = 0.2$ A. Treat $\mathbf{B}$ as azimuthal and uniform over the cross-section, and neglect fringing at the gap.
>
> (a) Explain why $B$ is the same in the iron and in the gap while $H$ is not, and write Ampère's law around the mean circle.
>
> (b) Find $B$, and $H$ in the iron and in the gap. Compare $B$ with that of the same ring without a gap.
>
> (c) Find the flux linkage and the inductance, with and without the gap. What fraction of the magnetic energy is stored in the gap?
>
> (d) Find $M$ in the iron and the magnetization current on the iron's surface per metre of ring, and compare it with the winding's free current per metre. Check Ampère's law in vacuum form around the mean circle. Is there any magnetization current on the gap faces?
>
> (e) The current is increasing at 20 A/s. Find the emf induced in the winding and say which way it acts.
>
> *Source: SP18 Exam 2 #2 style (toroid flux, flux linkage and emf), re-posed with an iron core and an air gap.*

> [!hint]- Hint
> The gap faces are perpendicular to $\mathbf{B}$, so there $\mathbf{B}$ is the *normal* component. Ampère's law counts free current only: $H_{\text{iron}}(2\pi R-g)+H_{\text{gap}}\,g = NI$, with $H_{\text{iron}} = B/\mu$ and $H_{\text{gap}} = B/\mu_0$.

> [!solution]- Solution
> **(a)** $\mathbf{B}$ crosses each gap face along its normal, and $B_n$ is continuous, so $B_{\text{gap}} = B_{\text{iron}}$; with no fringing the flux $BA$ is the same all the way round. $H = B/\mu$ is then 4000 times larger in the gap than in the iron. Here the two materials sit *in series* along the field, like dielectric layers stacked across a capacitor gap ($D$ the same in each). Compare problem 15.9 of the [[practice/15-inductance-and-magnetic-energy|Lecture 15 practice]], where ferrite and air sit *side by side* along the field and $H$ is the same in both. Ampère's law around the mean circle counts only the free current:
> $$
> H_{\text{iron}}\,(2\pi R-g)+H_{\text{gap}}\,g = NI = 250\times0.2 = 50\ \text{A}.
> $$
> **(b)** With the iron path $\ell_i = 2\pi R-g = 0.3132$ m,
> $$
> B = \frac{\mu_0NI}{g+\ell_i/\mu_r} = \frac{4\pi\times10^{-7}\times50}{10^{-3}+0.3132/4000} = 5.83\times10^{-2}\ \text{T},\qquad H_{\text{gap}} = \frac{B}{\mu_0} = 4.64\times10^{4}\ \text{A/m},\qquad H_{\text{iron}} = \frac{B}{\mu} = 11.6\ \text{A/m}.
> $$
> Check: $11.6\times0.3132+4.64\times10^4\times10^{-3} = 3.6+46.4 = 50$ A ✓, so 93% of the ampere-turns are spent on 1 mm of air. Without the gap, $B_0 = \mu NI/(2\pi R) = 0.800$ T, 13.7 times more.
>
> **(c)** $\Psi = BA = 5.83\times10^{-6}$ Wb per turn, $N\Psi = 1.46\times10^{-3}$ Wb, and $L = N\Psi/I = 7.28$ mH, i.e. $L = \mu_0N^2A/(g+\ell_i/\mu_r)$. Without the gap, $N\Psi = 0.0200$ Wb and $L_0 = 100$ mH. The energy $\tfrac12LI^2 = 1.46\times10^{-4}$ J is $\tfrac12BH$ times volume, region by region, and the gap holds the fraction $H_{\text{gap}}g/(NI)$ = 92.7% of it. (A practical bonus: $L$ now hardly depends on the iron's uncertain $\mu$; with $\mu_r = 8000$ it would be 7.56 mH.)
>
> **(d)** $M = B/\mu_0-H_{\text{iron}} = 4.64\times10^4$ A/m along $\mathbf{B}$ ($= \chi_mH_{\text{iron}} = 3999\times11.6$ A/m). On the iron's curved surface, $\mathbf{M}\times\hat{n}$ is a sheet of current circling the cross-section in the same sense as the winding: $4.64\times10^4$ A per metre of ring, against the winding's $NI/(2\pi R) = 159$ A per metre, 291 times more. In vacuum form, Ampère's law around the mean circle counts all the current through the disk it bounds, and the bound sheet crosses that disk along the iron's length $\ell_i$:
> $$
> \frac{B}{\mu_0}\,2\pi R = 1.457\times10^{4}\ \text{A} = NI+M\ell_i = 50+1.452\times10^{4}\ \text{A}\ \checkmark
> $$
> On the gap faces $\mathbf{M}$ is along $\hat{n}$, so $\mathbf{M}\times\hat{n} = 0$: no current there. The gap is a thin slice cut out of a "solenoid" of bound current, and inside such a slice the field is the full field.
>
> **(e)** $\lvert\mathcal{E}\rvert = L\,dI/dt = 7.28\ \text{mH}\times20\ \text{A/s} = 0.146$ V. By Lenz's law it opposes the increase: around each turn it acts against $I$, so the source must supply these 0.146 V on top of any resistive drop.
>
> **Answer.** (a) $B_n$ is continuous across the gap faces; $H_{\text{iron}}(2\pi R-g)+H_{\text{gap}}\,g = NI$. (b) $B = 58.3$ mT (0.800 T without the gap); $H_{\text{iron}} = 11.6$ A/m and $H_{\text{gap}} = 4.64\times10^4$ A/m. (c) $N\Psi = 1.46\times10^{-3}$ Wb and $L = 7.28$ mH (100 mH without the gap); 92.7% of the energy is in the gap. (d) $M = 4.64\times10^4$ A/m; a bound sheet of $4.64\times10^4$ A/m against 159 A/m of free current; none on the gap faces. (e) 0.146 V, opposing the increase of $I$.

### 17.12 A short bar magnet

> [!hard] Hard · magnetization · finite solenoid · magnetic boundary conditions
> A cylindrical magnet of radius $a = 1$ cm and length $\ell = 2$ cm is centred at the origin with its axis along $z$. It is uniformly magnetized, $\mathbf{M} = M_0\,\hat{z}$ with $M_0 = 9.0\times10^5$ A/m, and $\mathbf{M}$ is rigid (it does not respond to $\mathbf{H}$). There is no free current.
>
> (a) Find the magnetization currents. Which Lecture 13 object do they form?
>
> (b) Find $B_z$ on the axis at the centre and at the centre of the end face $z = \ell/2$.
>
> (c) Find $H_z$ at the centre, and just inside and just outside the end face. Which way does $\mathbf{H}$ point inside the magnet?
>
> (d) Which of $B_z$ and $H_z$ is continuous across the end face, and how large is the jump in the other? Explain with the boundary conditions.
>
> (e) What do $B$ and $H$ at the centre tend to for a long rod ($\ell\gg a$) and for a thin disk ($\ell\ll a$)?
>
> *Source: classic (the field of a bar magnet), built on the finite solenoid of Lecture 13 practice problem 13.12.*

> [!hint]- Hint
> The side carries $\mathbf{J}_{sM} = M_0\,\hat\phi$: a solenoid of length $\ell$ with $nI\to M_0$. A slice $dz'$ is a loop carrying $M_0\,dz'$, whose field on the axis is $\dfrac{\mu_0M_0\,dz'\,a^2}{2\big(a^2+(z-z')^2\big)^{3/2}}$. Then $\mathbf{H} = \mathbf{B}/\mu_0-\mathbf{M}$ point by point.

> [!solution]- Solution
> **(a)** $\nabla\times\mathbf{M} = 0$ (uniform). Side, $\hat{n} = \hat{r}$: $\mathbf{J}_{sM} = M_0\,\hat{z}\times\hat{r} = M_0\,\hat\phi = 9.0\times10^5\,\hat\phi$ A/m. Ends, $\hat{n} = \pm\hat{z}$: $\hat{z}\times(\pm\hat{z}) = 0$. The magnet is a finite solenoid of radius $a$ and length $\ell$ with $nI = M_0$, and a short one, since $\ell = 2a$.
>
> **(b)** Integrating the loops over $-\ell/2<z'<\ell/2$, as in problem 13.12 of the [[practice/13-current-sheets-solenoids-and-vector-potential|Lecture 13 practice]]:
> $$
> B_z(z) = \frac{\mu_0M_0}{2}\left[\frac{\ell/2-z}{\sqrt{(\ell/2-z)^2+a^2}}+\frac{\ell/2+z}{\sqrt{(\ell/2+z)^2+a^2}}\right],\qquad \mu_0M_0 = 1.131\ \text{T}.
> $$
> At the centre, $B = \mu_0M_0\dfrac{\ell/2}{\sqrt{(\ell/2)^2+a^2}} = \dfrac{\mu_0M_0}{\sqrt2} = 0.800$ T. On the end face, $B = \dfrac{\mu_0M_0}{2}\,\dfrac{\ell}{\sqrt{\ell^2+a^2}} = \dfrac{\mu_0M_0}{2}\cdot\dfrac{2}{\sqrt5} = 0.506$ T.
>
> **(c)** $H_z = B_z/\mu_0-M_z$. At the centre, $H = M_0(1/\sqrt2-1) = -2.64\times10^5$ A/m: it points along $-\hat{z}$, **against** $\mathbf{M}$. This is the *demagnetizing field*. On the end face, just inside: $0.506/\mu_0-9.0\times10^5 = 4.02\times10^5-9.0\times10^5 = -4.98\times10^5$ A/m; just outside, where $\mathbf{M} = 0$: $+4.02\times10^5$ A/m.
>
> **(d)** On the end face $B_z$ is the normal component, and it is continuous: 0.506 T on both sides. That holds across any surface, since $\nabla\cdot\mathbf{B} = 0$ (a surface current could only make the *tangential* components jump), and the on-axis formula of (b) is indeed continuous at $z = \ell/2$. $H_z$ jumps by $+9.0\times10^5$ A/m $= M_0$ going outward. With the air as medium 1 and the magnet as medium 2 ($\hat{n} = +\hat{z}$), $B_{1n} = B_{2n}$ gives
> $$
> H_{1n}-H_{2n} = -(M_{1n}-M_{2n}) = -(0-M_0) = M_0 .
> $$
> The end faces act as sources and sinks of $\mathbf{H}$, since $\nabla\cdot\mathbf{H} = -\nabla\cdot\mathbf{M}$ there; that is where the demagnetizing field comes from.
>
> **(e)** Long rod: $B_{\text{centre}}\to\mu_0M_0 = 1.13$ T and $H\to0$, the result of 17.5 (already for $\ell = 100a$, $H = -2\times10^{-4}M_0$); on the end face of a long rod $B\to\mu_0M_0/2$. Thin disk: $B_{\text{centre}}\approx\mu_0M_0\,\ell/(2a)\to0$ and $H\to-M_0$ (for $\ell = 0.01a$, $B = 0.005\,\mu_0M_0$ and $H = -0.995\,M_0$). The thin disk is the magnetic twin of a dielectric slab polarized across its faces, where $\mathbf{E} = -\mathbf{P}/\epsilon_0$ ([[1-electrostatics/08-conductors-dielectrics-and-polarization|Lecture 8]]).
>
> **Check:** a direct Biot–Savart sum over the side current reproduces 0.800 T and 0.506 T.
>
> **Watch out:** "$\mathbf{H}$ is the same with or without the material" holds only for a long core along $\mathbf{H}$. Inside a short magnet $\mathbf{H}$ is not zero and points backwards, against $\mathbf{M}$, which is why short, flat magnets demagnetize more easily than long ones.
>
> **Answer.** (a) $\mathbf{J}_{sM} = 9.0\times10^5\,\hat\phi$ A/m on the side only: a short solenoid. (b) 0.800 T at the centre, 0.506 T on the end face. (c) $H_z = -2.64\times10^5$ A/m at the centre (against $\mathbf{M}$); $-4.98\times10^5$ A/m just inside and $+4.02\times10^5$ A/m just outside the end face. (d) $B_z$ is continuous; $H_z$ jumps by $M_0 = 9.0\times10^5$ A/m. (e) Long rod: $B\to\mu_0M_0 = 1.13$ T and $H\to0$; thin disk: $B\to0$ and $H\to-M_0$.

### Sources for this page
No past exam covers Lecture 17, so each problem's source line says honestly whether it is original, classic or adapted. Course notes for Lecture 17: $\mathbf{M} = N\mathbf{m}$ and the stacked atomic loops (17.5), and hysteresis, remanence and permanent magnets (17.4). Lecture 17 slides: $\mathbf{m} = I\mathbf{A}$ and the torque on a tilted orbit (17.1, re-posed with a rectangular loop), the $\chi_m$ and $\mu_r$ tables (17.2, re-posed as a measurement), the slab between two current sheets (17.3 with air gaps and a student slip; 17.10 with three sheets and two slabs), and the "M → P" pairing (17.9, posed as twin problems). Old exams, for the Lecture 13–15 parts only: SP18 Exam 2 #2 (17.11, a toroid's flux, flux linkage and emf, re-posed with an iron core and an air gap) and SP18 Exam 2 #1(vi), the step across a current sheet (inside 17.10). Classic problems with new numbers: the current-carrying magnetic wire (17.7) and the bar magnet as a short solenoid (17.12, built on Lecture 13 practice problem 13.12). Original: 17.6 and 17.8. None of them repeats the worked problem [[problems/fields-across-a-magnetic-interface]] or the numbers of the slab example on the Lecture 17 page.

*Previous: [[practice/16-charge-conservation-and-displacement-current|Lecture 16 practice]] · next: [[practice/18-wave-equation-and-plane-waves|Lecture 18 practice]] · [[practice/index|all practice]]*
