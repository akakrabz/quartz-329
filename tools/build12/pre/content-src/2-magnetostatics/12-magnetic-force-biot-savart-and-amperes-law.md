---
title: "Lecture 12 — Magnetic force, Biot–Savart, and Ampère's law"
description: "Parallel currents attract because, seen from the moving electrons, the other wire is charged (Lorentz contraction); the lab writes the force as qv×B with B = μ₀I/(2πr) φ̂. Biot–Savart generalizes it to any current, Ampère's law ∮H·dl = I_enc is the loop version of Gauss's law, and ∇×H = J, ∇·B = 0 mirror electrostatics with divergence and curl swapped."
tags: [lecture, magnetostatics]
lecture: 12
---

*Lecture 12 · course notes §12 · slides "Magnetic Flux and Magnetic Fields / Biot–Savart Law / Ampère's Law" · prev: [[1-electrostatics/11-lorentz-drude-models-for-conductivity-and-susceptibility|Lecture 11]] · next: [[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential|Lecture 13]] · practice: [[practice/12-magnetic-force-biot-savart-and-ampere|12 problems]]*

> [!abstract] In one breath
> Parallel wires with currents in the same direction attract, though neither carries net charge. In the frame of one wire's drifting electrons, the other wire's ion and electron spacings are Lorentz-contracted by different amounts, so that wire *is* charged there and its Coulomb field pushes on the electrons. The lab packages the same force as $\mathbf{F} = q\mathbf{v}\times\mathbf{B}$ with $\mathbf{B} = \dfrac{\mu_0I}{2\pi r}\hat\phi$ circling the wire. **Biot–Savart** (Coulomb's law with a cross product) and **Ampère** (circulation of $\mathbf{H} = \mathbf{B}/\mu_0$ around a loop equals the current through it — Gauss's law with a loop) give $\mathbf{B}$ for any steady current. Differentially, $\nabla\times\mathbf{H} = \mathbf{J}$ and $\nabla\cdot\mathbf{B} = 0$: electrostatics mirrored.

## 1. The observation, and the definition of B

<!-- fig:two-wires-force -->

Ampère's 1820 experiment: currents in the same direction attract, opposite directions repel, force per unit length $\propto1/r$. The force on a short piece of wire 2 is proportional to $I_2\,d\mathbf{l}_2$ and to wire 1's current, and perpendicular to the wire — so it is a cross product with a field that wire 1 produces:

> [!key] Magnetic force and the magnetic flux density
> $$
> d\mathbf{F} = I\,d\mathbf{l}\times\mathbf{B},\qquad\text{equivalently}\qquad \mathbf{F} = q\mathbf{v}\times\mathbf{B}\quad\text{on a charge }q\text{ moving at }\mathbf{v},
> $$
> because a current element is moving charge: $I\,d\mathbf{l} = (\text{charge per length}\cdot v)\,d\mathbf{l} = q\mathbf{v}$ summed over the carriers in $d\mathbf{l}$. $\mathbf{B}$ is the **magnetic flux density**, in tesla: $\text{T} = \text{N/(A·m)} = \text{Wb/m}^2$. This completes the Lorentz force $\mathbf{F} = q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$ of [[1-electrostatics/01-fields-forces-and-the-maxwell-roadmap|Lecture 1]], now with a source for $\mathbf{B}$.

The force is perpendicular to $\mathbf{v}$, so it **does no work**: static magnetic fields deflect charges, never speed them up. A *stationary* charge near a current-carrying wire feels nothing — the wire is neutral.

## 2. Where the force comes from: a charged wire, in the right frame

Ideal wire: positive ions at rest, electrons drifting left at $v$, current $I$ to the right. In the lab $\lambda_+ = -\lambda_-$ and $I = v\lambda_+$ ($\lambda$ is the notes' symbol for line charge density, $\rho_l$ elsewhere on this site). A test charge $q$ moving *with* the electrons sees, in **its own frame**, the ions moving right at $v$ and the electrons at rest. Lorentz contraction (a moving ruler is shorter by $1/\gamma$, $\gamma = 1/\sqrt{1-v^2/c^2}$) acts on the two line charges differently:

> [!derivation]- The relativistic bookkeeping (course notes, footnote 3)
> - In the lab the *electrons* move, so their spacing is already contracted: the lab density $\lambda_-$ is $\gamma$ times their own-frame density $\lambda_-'$. Hence in the electron frame $\lambda_-' = \lambda_-/\gamma$ — sparser.
> - In the electron frame the *ions* move, so their spacing is contracted there: $\lambda_+' = \gamma\lambda_+$ — denser.
> - Net line charge seen by the test charge: $\lambda' = \gamma\lambda_+ + \lambda_-/\gamma = \lambda_+\big(\gamma - 1/\gamma\big) = \gamma\lambda_+\dfrac{v^2}{c^2}$, positive.
>
> With $\lambda_+ = I/v$: $\lambda' = \gamma I v/c^2 = \gamma Iv\,\mu_0\epsilon_0$, using $1/c^2 = \mu_0\epsilon_0$. The line-charge field of [[1-electrostatics/03-gauss-law-at-work|Lecture 3]] is then $\mathbf{E}' = \dfrac{\lambda'}{2\pi\epsilon_0r}\hat r = \dfrac{\gamma Iv\mu_0}{2\pi r}\hat r$, and the force on the (here stationary) test charge is $\mathbf{F}' = q\mathbf{E}'$. Transforming a transverse force back to the lab divides by $\gamma$: $\mathbf{F} = \mathbf{F}'/\gamma = q\dfrac{Iv\mu_0}{2\pi r}\hat r$ — the $\gamma$'s cancel exactly, so the result holds for any $v$.

The lab force is radial, $\propto qv$ and $I/r$. Writing it as $q\mathbf{v}\times\mathbf{B}$, $\mathbf{v}$ along the wire, $\mathbf{B}$ *around* it, identifies the field:

> [!key] The field of a long straight current
> $$
> \mathbf{B} = \frac{\mu_0I}{2\pi r}\,\hat\phi,\qquad \mu_0 = 4\pi\times10^{-7}\ \text{H/m},\qquad \mu_0\epsilon_0 = \frac1{c^2}.
> $$
> $\hat\phi$ by the **right-hand rule**: thumb along $I$, fingers curl along $\mathbf{B}$. The field lines are circles around the wire; they do not begin or end.

> [!intuition] Why such a tiny effect produces an everyday force
> The relative charge imbalance is $\lambda'/\lambda_+ = v^2/c^2$: for 1 A in a 1 mm² copper wire the drift speed is $7\times10^{-5}$ m/s, so $v^2/c^2\approx6\times10^{-26}$. But $\lambda_+$ is enormous — about $1.4\times10^4$ C/m, balanced to that precision by electrons. The product, $\lambda'\sim10^{-21}$ C/m, makes a field of order $10^{-9}$ V/m at a centimetre — exactly $vB$ with $B = \mu_0I/(2\pi r) = 2\times10^{-5}$ T. Magnetism is what is left of the Coulomb force when a nearly perfect cancellation is spoiled by relativity.

Signs in the figure: a positive test charge moving *with the electrons* (against $I$) is repelled (a positively charged wire repels it). One moving *along* $I$ is attracted — so the electrons of a second parallel wire, moving against $I_2$ but negative, are attracted when $I_2\parallel I_1$: the two-wire attraction. A real resistive wire also has a small lab-frame surface charge ([[1-electrostatics/11-lorentz-drude-models-for-conductivity-and-susceptibility#6-what-drives-the-current-in-a-wire-a-footnote-worth-a-section|Lecture 11 §6]]); the argument above is for the idealized neutral wire.

## 3. Biot–Savart: Coulomb's law for current elements

By superposition, the wire's field is the sum over its pieces. The rule that reproduces $\mu_0I/(2\pi r)$:

> [!key] Biot–Savart law
> $$
> d\mathbf{B} = \frac{\mu_0}{4\pi}\,\frac{I\,d\mathbf{l}\times\hat{R}}{R^2},
> $$
> $\mathbf{R} = R\hat R$ points **from the current element to the field point**. Coulomb's law with $\rho\,dV\to I\,d\mathbf{l}$ and a cross product making $d\mathbf{B}$ perpendicular to the element and to the line to the field point. Valid for elements of steady, closed current loops (an isolated element is not a possible steady current; only the full loop integral is physical).

<!-- fig:biot-savart-line -->

The slides run the **five-step program** of [[1-electrostatics/02-coulombs-law-superposition-and-gauss|Lecture 2]] with $d\mathbf{B}$ for $d\mathbf{E}$: *draw* (3-D, side view through the field point, top view); *divide* into elements $I\,dz\,\hat z$; *write* $d\mathbf{B}$, with $|d\mathbf{l}\times\hat R| = dz\cos\alpha = dz\,r/R$, $R = \sqrt{r^2+z^2}$; *use symmetry* — every $d\mathbf{B}$ points along $\hat\phi$, so nothing cancels; *integrate*:

$$
B_\phi = \frac{\mu_0Ir}{4\pi}\int_{-\infty}^{\infty}\frac{dz}{(r^2+z^2)^{3/2}} = \frac{\mu_0Ir}{4\pi}\cdot\frac{2}{r^2} = \frac{\mu_0I}{2\pi r}\quad\checkmark
$$

(the line-charge integral of Lecture 2; antiderivative $z/(r^2\sqrt{r^2+z^2})$). Treating the whole wire as one element and "plugging in the formula" is wrong — the slides say so in boldface; it is Coulomb's point-charge law applied to a line charge.

> [!recipe] The vector bookkeeping of Biot–Savart
> Order matters: $d\mathbf{l}\times\hat R$, not $\hat R\times d\mathbf{l}$. $\hat R$ runs from the source element to the field point (the slides' $\hat a_{21}$, "from 2 to 1"). The force between two circuits is a double integral, $\mathbf{F}_1 = \oint_1I_1d\mathbf{l}_1\times\mathbf{B}_2$; the forces $d\mathbf{F}_1$, $d\mathbf{F}_2$ between two *elements* are not equal and opposite — only the totals over closed loops are.

## 4. Ampère's law: the circulation of B

Around a circle of radius $r$ centred on the wire, $d\mathbf{l} = r\,d\phi\,\hat\phi$ and $\oint\mathbf{B}\cdot d\mathbf{l} = \dfrac{\mu_0I}{2\pi r}\cdot2\pi r = \mu_0I$, **for any radius**. It holds for *every* closed path and every steady current distribution:

> [!key] Ampère's law (static)
> $$
> \oint_C\mathbf{B}\cdot d\mathbf{l} = \mu_0I_C\qquad\Longleftrightarrow\qquad \oint_C\mathbf{H}\cdot d\mathbf{l} = I_C = \int_S\mathbf{J}\cdot d\mathbf{S},\qquad \mathbf{H}\equiv\frac{\mathbf{B}}{\mu_0}\ [\text{A/m}],
> $$
> $I_C$ is the net current through **any** surface $S$ bounded by $C$, positive in the right-hand direction from the sense of $C$ (thumb along $d\mathbf{l}$, fingers through $S$; i.e. $d\mathbf{S}$ by the Stokes convention of [[1-electrostatics/06-circulation-and-boundary-conditions|Lecture 6]]). Currents not *linked* by $C$ contribute nothing, however close. $\mathbf{H}$ is introduced "for convenience": the field whose circulation is the current, in A/m; in free space just $\mathbf{B}/\mu_0$.

> [!intuition] Gauss ↔ Ampère
> Gauss: flux of $\mathbf{D}$ out of a closed *surface* = charge inside. Ampère: circulation of $\mathbf{H}$ around a closed *loop* = current through. Same recipe (the slides put $\oint\mathbf{D}\cdot d\mathbf{S} = Q_{\text{enc}}$ atop the coax challenge). Pick the surface or loop matching the symmetry so the field leaves the integral as a constant; $D\cdot(\text{area}) = Q_{\text{enc}}$ becomes $H\cdot(\text{length}) = I_{\text{enc}}$ — "$B\cdot2\pi r$" is the magnetic "$D\cdot4\pi r^2$". Names match too: $\oint\mathbf{E}\cdot d\mathbf{l}$ is an **EMF** [V], $\oint\mathbf{H}\cdot d\mathbf{l}$ an **MMF** [A]; in statics the first is zero and the second is the linked current.

**Differential form.** Stokes, $\oint_C\mathbf{H}\cdot d\mathbf{l} = \int_S(\nabla\times\mathbf{H})\cdot d\mathbf{S}$, equals $\int_S\mathbf{J}\cdot d\mathbf{S}$ for every $S$, so the integrands agree:

> [!key] The laws of magnetostatics
> $$
> \nabla\times\mathbf{H} = \mathbf{J},\qquad \nabla\cdot\mathbf{B} = 0 .
> $$
> Electrostatics: $\nabla\times\mathbf{E} = 0$, $\nabla\cdot\mathbf{D} = \rho$. The magnetic field's source is in its **curl**, with no divergence; the electric field's is in its **divergence**, with no curl. $\nabla\cdot\mathbf{B} = 0$ is the law of [[1-electrostatics/03-gauss-law-at-work#6-the-magnetic-counterpart--bds--0|Lecture 3]] — no magnetic charge, closed lines — and holds for time-varying fields too. ("$\nabla\cdot\mathbf{H} = 0$", as a slide lists it, is equivalent only where $\mu$ is uniform.)

Check on the straight wire: off the axis, $(\nabla\times\mathbf{B})_z = \dfrac1r\dfrac{d}{dr}(rB_\phi) = \dfrac1r\dfrac{d}{dr}\Big(\dfrac{\mu_0I}{2\pi}\Big) = 0$ and $\nabla\cdot\mathbf{B} = \dfrac1r\partial_\phi B_\phi = 0$. The curl sits on the wire, where $\mathbf{J}$ is a δ-function (next section).

**When "static" is good enough.** These laws hold *quasi-statically* for a time-varying $\mathbf{J}(\mathbf{r},t)$ over a region of size $L$ if the current changes on a time scale $\tau\gg L/c$, equivalently $L\ll\lambda = c/f$. Then $\mathbf{B}(\mathbf{r},t) = \mu_0\mathbf{H}(\mathbf{r},t)$ follows the instantaneous current, with a slowly varying $\mathbf{E}$ from Faraday's law ([[2-magnetostatics/14-faradays-law-and-induced-emf|Lecture 14]]). This **magneto-quasi-static** (MQS) regime is where inductors live, as capacitors live in the quasi-static regime of [[1-electrostatics/10-capacitance-and-conductance|Lecture 10]].

## 5. Describing currents: J, Jₛ, I, and δ-functions

$\mathbf{J}$ in Ampère's law is a volume current density [A/m²] — $\sigma\mathbf{E}$ in a conductor, $Nq\mathbf{v}$ in general ([[1-electrostatics/11-lorentz-drude-models-for-conductivity-and-susceptibility|Lecture 11]]). Thinner distributions use δ-functions, as charge densities did in [[1-electrostatics/03-gauss-law-at-work#5-charge-densities-and-δ-functions|Lecture 3]]:

| distribution | units | as a volume density $\mathbf{J}$ |
|---|---|---|
| surface current $\mathbf{J}_s(y,z)$ on the plane $x = x_0$ | A/m | $\mathbf{J}_s(y,z)\,\delta(x-x_0)$ |
| line current $I(z)$ along the line $x = x_0$, $y = y_0$ | A | $\hat z\,I(z)\,\delta(x-x_0)\,\delta(y-y_0)$ |
| point charge $Q$ moving at $\mathbf{v}$ through $\mathbf{r}_0(t)$ | — | $Q\mathbf{v}\,\delta(x-x_0)\delta(y-y_0)\delta(z-z_0)$ (time-varying) |

Each δ carries 1/m, so the units come out A/m². $\mathbf{J}_s$ is current per unit **width**, measured across the flow; integrate across the flow, not over an area, to get amperes.

> [!example] Example — total current on a sheet (course notes, Example 1)
> $\mathbf{J}_s = \hat z\,y\,\text{rect}(y - \tfrac12)$ A/m on the plane $x = 0$: a strip $0<y<1$ m wide (infinite in $z$) whose current density grows linearly from 0 to 1 A/m across it. Total current, integrating *across* the strip: $I = \displaystyle\int_0^1y\,dy = \tfrac12$ A. (A slide once dropped a δ from the line current: [[0-toolkit/04-errata-in-the-course-materials|errata page]].)

## 6. Ampère at work: the coaxial cable

<!-- fig:ampere-coax-profile -->

The challenge question: a solid core of radius $a$ carries $I$ uniformly ($J = I/\pi a^2$); the thin shell at $r = b$ returns it. Where is $\mathbf{H}$ constant? By symmetry $\mathbf{H} = H_\phi(r)\hat\phi$, so $H_\phi\cdot2\pi r = I_{\text{enc}}(r)$:

$$
H_\phi = \begin{cases}\dfrac{Ir}{2\pi a^2}, & r<a\quad(I_{\text{enc}} = I\,r^2/a^2)\\[8pt] \dfrac{I}{2\pi r}, & a<r<b\\[8pt] 0, & r>b\quad(I_{\text{enc}} = I - I).\end{cases}
$$

Answer **(c)**, $r>b$: the only constant $H$ is zero. Each region translates a Lecture 3 result: linear growth like $D$ inside a uniformly charged cylinder, $1/r$ like $D$ outside a line charge, zero like $D$ outside a coax with $\pm$ charges.

> [!trap] Counting the enclosed current
> $I_{\text{enc}}$ is a *signed* sum. A clockwise contour linking $I_1$ out of the page and $I_2$ into the page has $I_{\text{enc}} = I_2 - I_1$ (into the page is the right-hand direction for clockwise); counter-clockwise, $I_1 - I_2$. Only current *through* the surface counts: a wire passing the loop without threading it contributes nothing, though its field is present all along the path. The sense of $\hat\phi$ follows the current, not the axes: a current in $-\hat x$ makes $\mathbf{H}$ circulate in $-\hat\phi$ about the $+x$ axis.

## 7. Summary

- $\mathbf{F} = q\mathbf{v}\times\mathbf{B}$, $d\mathbf{F} = I\,d\mathbf{l}\times\mathbf{B}$; magnetic forces do no work; parallel currents attract.
- The force is the Coulomb force of a wire charged *in the moving frame*; the lab writes $\mathbf{B} = \mu_0I/(2\pi r)\,\hat\phi$, $\mu_0\epsilon_0 = 1/c^2$.
- Biot–Savart: $d\mathbf{B} = \mu_0I\,d\mathbf{l}\times\hat R/(4\pi R^2)$, $\hat R$ from source to field point; five steps; $\int dz/(r^2+z^2)^{3/2} = 2/r^2$.
- Ampère: $\oint\mathbf{H}\cdot d\mathbf{l} = I_{\text{enc}}$ through any surface on $C$, right-hand rule; $\mathbf{H} = \mathbf{B}/\mu_0$ [A/m].
- $\nabla\times\mathbf{H} = \mathbf{J}$, $\nabla\cdot\mathbf{B} = 0$ — div and curl swapped; quasi-statically valid for $L\ll c/f$.
- $\mathbf{J}_s\,\delta(x-x_0)$, $\hat zI\,\delta(x-x_0)\delta(y-y_0)$; integrate $\mathbf{J}_s$ across the flow for $I$.
- Coax: $H_\phi = Ir/(2\pi a^2)$, $I/(2\pi r)$, $0$.

Concept pages: [[concepts/magnetic-field]] · [[concepts/biot-savart-law]] · [[concepts/amperes-law]] · [[concepts/lorentz-force]].

> [!exam] On exams
> The magnetic twin of Exam 1 problem 2: "a current distribution with planar/cylindrical symmetry — find $\mathbf{H}$ everywhere". State the symmetry ($\mathbf{H} = H_\phi(r)\hat\phi$ or $H_y(x)\hat y$), draw the loop, count $I_{\text{enc}}$ region by region, give units (A/m for $\mathbf{H}$, T for $\mathbf{B}$). Direction questions — which way $\mathbf{B}$ points, which way the force on a charge or wire — are cheap points; use the right-hand rule and $q\mathbf{v}\times\mathbf{B}$ explicitly, not by instinct.

> [!tip] Practice this lecture
> [[practice/12-magnetic-force-biot-savart-and-ampere|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/12-magnetic-force-biot-savart-and-ampere#121-a-charge-passing-a-wire|12.1 A charge passing a wire]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 12 (two-wire attraction; relativity footnote, $\lambda' = \gamma\lambda_+v^2/c^2$, $\mathbf{F} = \mathbf{F}'/\gamma$; $\mathbf{B}$ and the right-hand rule; Biot–Savart and its validity; Ampère's law, $\mathbf{H} = \mathbf{B}/\mu_0$, differential laws; δ-function currents, Example 1; MQS note). Shao, "Lectures 11–12" slides (Ampère's experiment; $I\,d\mathbf{l} = q\mathbf{v}$; five-step Biot–Savart; circulation; laws beside electrostatics; current units; coax challenge, signed currents). The site's own: copper numbers. Slips in the course material: see [[0-toolkit/04-errata-in-the-course-materials|errata]].
