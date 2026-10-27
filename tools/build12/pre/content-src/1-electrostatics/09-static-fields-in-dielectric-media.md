---
title: "Lecture 9 — Static fields in dielectric media"
description: "Working rules for dielectric problems: D from the free charge, E = D/ε region by region, V by integrating E, P = D − ε₀E if asked. Field lines refract at an interface; Laplace's equation holds only inside a homogeneous region, so layered media are solved piece by piece and graded ones with Gauss's law directly."
tags: [lecture, electrostatics, exam-1]
lecture: 9
---

*Lecture 9 · course notes §9 · slides "Dielectrics" (examples) · prev: [[1-electrostatics/08-conductors-dielectrics-and-polarization|Lecture 8]] · next: [[1-electrostatics/10-capacitance-and-conductance|Lecture 10]] · practice: [[practice/09-static-fields-in-dielectric-media|12 problems]]*

> [!abstract] In one breath
> Every dielectric problem is a short chain: **free** charge fixes $\mathbf{D}$ (Gauss's law, continuity of normal $\mathbf{D}$), each region's permittivity gives $\mathbf{E} = \mathbf{D}/\epsilon$, a line integral gives $V$, and $\mathbf{P} = \mathbf{D}-\epsilon_0\mathbf{E}$ comes last if asked. Laplace's equation holds only where $\epsilon$ is constant: layered media are solved layer by layer and stitched with boundary conditions; graded media need Gauss's law itself.

## 1. The rules

> [!key] What you may assume in a problem with dielectrics
> 1. $\mathbf{D} = \epsilon\mathbf{E} = \epsilon_0\mathbf{E} + \mathbf{P}$ in each region, with $\epsilon = \epsilon_r\epsilon_0$ given.
> 2. Between two perfect dielectrics there is no free surface charge (unless the problem puts one there): **normal $\mathbf{D}$ is continuous**; **tangential $\mathbf{E}$ is continuous** at every interface.
> 3. At a conductor–dielectric interface, $\hat{n}\cdot\mathbf{D} = \rho_s$ with $\hat{n}$ **from the conductor into the dielectric** and $\mathbf{D}$ on the dielectric side ($\mathbf{D} = 0$ in the conductor).
> 4. Gauss's law, $\nabla\cdot\mathbf{D} = \rho$ and $\oint\mathbf{D}\cdot d\mathbf{S} = Q_{\text{enc}}$, counts **free** charge only.
> 5. When $\mathbf{P}$ is wanted: $\mathbf{P} = \mathbf{D} - \epsilon_0\mathbf{E} = (\epsilon_r - 1)\epsilon_0\mathbf{E}$. Bound surface charge on a face with outward normal $\hat{n}$: $\rho_{sb} = \mathbf{P}\cdot\hat{n}$.

> [!recipe] The planar chain (works whenever the geometry has one coordinate)
> $D$ is constant across any charge-free layer ⟶ read it off a conductor with $\rho_s = \hat{n}\cdot\mathbf{D}$, or off the enclosed free charge ⟶ $E = D/\epsilon$ in each layer ⟶ $V$ by $-\int E\,dz$, layer by layer ⟶ $P = D - \epsilon_0E$ if required. The same chain runs in cylindrical ($D\propto1/r$) and spherical ($D\propto1/r^2$) symmetry.

> [!example] Example — a slab in a known exterior field
> A dielectric slab, faces perpendicular to $\hat{x}$, in free space where $\mathbf{E} = 18\hat{x}$ V/m; inside, $3\hat{x}$ V/m is measured. Find $\mathbf{D}$, $\mathbf{P}$, $\epsilon_r$, $\chi_e$.
>
> *Outside:* $\mathbf{D} = \epsilon_0\mathbf{E} = 18\epsilon_0\hat{x}$ C/m², $\mathbf{P} = 0$. *Inside:* normal $\mathbf{D}$ is continuous (no free charge on the faces), so $\mathbf{D} = 18\epsilon_0\hat{x}$. Then $\epsilon = D/E = 18\epsilon_0/3 = 6\epsilon_0$: $\epsilon_r = 6$, $\chi_e = \epsilon_r - 1 = 5$. And $\mathbf{P} = \mathbf{D} - \epsilon_0\mathbf{E} = 18\epsilon_0\hat{x} - 3\epsilon_0\hat{x} = 15\epsilon_0\hat{x}$ C/m² (check: $\epsilon_0\chi_eE = 5\epsilon_0\cdot3 = 15\epsilon_0$ ✓).
>
> Bound surface charges: $\rho_{sb} = \mathbf{P}\cdot\hat{n} = +15\epsilon_0$ on the $+x$ face, $-15\epsilon_0$ on the $-x$ face. As a pair of sheets they produce $-15$ V/m between them: $18 - 15 = 3$ ✓.

## 2. Refraction of field lines at an interface

Two perfect dielectrics, no free charge on the interface; split each side's field into tangential and normal parts:

<!-- fig:field-refraction -->

> [!key] Field lines bend at a dielectric interface
> $$
> E_{2t} = E_{1t},\qquad \epsilon_2E_{2n} = \epsilon_1E_{1n}\ \Rightarrow\ E_{2n} = \frac{\epsilon_1}{\epsilon_2}E_{1n},
> \qquad\qquad \frac{\tan\theta_1}{\tan\theta_2} = \frac{\epsilon_1}{\epsilon_2}
> $$
> (angles from the normal). Entering the higher-$\epsilon$ medium, the normal component shrinks and the line tilts toward the surface. $\mathbf{D}$, parallel to $\mathbf{E}$, bends by the same angle with the roles swapped: its normal part is continuous, its tangential part scales with $\epsilon$. With free surface charge on the interface, $D_{1n} - D_{2n} = \rho_s$ replaces the second condition ($\hat{n}$ from 2 into 1). The bound surface charge at the interface (with $\rho_s = 0$) is $\rho_{sb} = P_{2n} - P_{1n} = \epsilon_0(E_{1n} - E_{2n})$.

This is FA26 Exam 1 problem 3, worked with different numbers in [[problems/fields-across-a-dielectric-interface]], with the checklist of errors: normal $\mathbf{E}$ made continuous, tangential $\mathbf{D}$ made continuous, ratio inverted, $\epsilon_0$ used for $\epsilon$.

## 3. Laplace's equation, layer by layer

Poisson's equation came from pulling $\epsilon$ out of $\nabla\cdot(\epsilon\nabla V) = -\rho$, which needs $\epsilon$ independent of position. So:

> [!trap] Do not use Laplace's or Poisson's equation in an inhomogeneous medium
> **Homogeneous** means $\epsilon_r$ is the same throughout. Where $\epsilon$ jumps, $\nabla^2V\ne0$ even with no free charge — the kink in $V$ carries a *bound* sheet $\rho_{sb}$ ($\nabla^2V = -\rho_{sb}/\epsilon_0$ in vacuum language). For **piecewise** homogeneous media, solve $\nabla^2V=0$ in each layer and join the pieces with $V$ continuous and $D_n$ continuous. For **continuously** varying $\epsilon(\mathbf{r})$, go back to Gauss's law.

<!-- fig:two-layer-plates -->

> [!example] Example — two layers between charged plates
> Conducting plates at $z=0$ (carrying $-2\epsilon_0$ C/m², held at $V=0$) and $z=2$ m (carrying $+2\epsilon_0$ C/m²); $\epsilon_1 = \epsilon_0$ for $0<z<1$ m, $\epsilon_2 = 2\epsilon_0$ for $1<z<2$ m. Find $V(2)$.
>
> *Laplace, piecewise.* $V_1 = Az$ in the lower layer ($V'' = 0$, $V(0)=0$); $V_2 = A + B(z-1)$ in the upper (continuous at $z=1$ by construction). Two conditions:
> - bottom plate, $\hat{n} = +\hat{z}$ from conductor into dielectric: $\rho_s = \hat{z}\cdot\mathbf{D}_1(0) = \epsilon_1\cdot(-A) = -2\epsilon_0$, so $A = 2$;
> - interface, $D_n$ continuous: $\epsilon_1(-A) = \epsilon_2(-B)$, so $B = A\epsilon_1/\epsilon_2 = 1$.
>
> Hence $V = 2z$ on $(0,1)$, $V = 2 + (z-1)$ on $(1,2)$, $V(2) = 3$ V; $\mathbf{E} = -2\hat{z}$ and $-\hat{z}$ V/m, $\mathbf{D} = -2\epsilon_0\hat{z}$ in both layers. Top-plate check: $-\hat{z}\cdot\mathbf{D}_2(2) = +2\epsilon_0$ ✓.
>
> *$\mathbf{D}$ first (faster).* Sheets $\pm2\epsilon_0$ give $\mathbf{D} = -2\epsilon_0\hat{z}$ whatever fills the gap; $E = D/\epsilon$ per layer; $V(2) - V(0) = -\int_0^2E_z\,dz = -[(-2)(1) + (-1)(1)] = 3$ V. (Planar symmetry: the free sheets alone fix $\mathbf{D}$.)
>
> In general, for a plate at $V_p$ over layers $\epsilon_1$ (thickness $d$) and $\epsilon_2$ (thickness $z_0 - d$), $E_1 = \dfrac{V_p/\epsilon_1}{d/\epsilon_1 + (z_0-d)/\epsilon_2}$: the voltage divides in proportion to $d_i/\epsilon_i$, like two capacitors in series ([[1-electrostatics/10-capacitance-and-conductance#4-layered-dielectrics-series-and-parallel|Lecture 10 §4]]). HW4 #1 and #3 are this problem with the numbers rearranged.

> [!example] Example — a charged sheet between grounded plates
> Both plates ($z=0$ and $z=d$) grounded; a free sheet $\rho_s$ at $z=d_1$ in vacuum, $d_2 = d - d_1$, $V_0 = V(d_1)$. Laplace in each gap gives a "tent": $V = V_0z/d_1$ below the sheet and $V_0(d-z)/d_2$ above, so $\mathbf{E} = -\hat{z}V_0/d_1$ below and $+\hat{z}V_0/d_2$ above. Jump condition at the sheet ($\hat{n} = \hat{z}$, medium 1 above):
> $$
> \epsilon_0\frac{V_0}{d_2} - \Big(-\epsilon_0\frac{V_0}{d_1}\Big) = \rho_s\quad\Longrightarrow\quad V_0 = \frac{\rho_s}{\epsilon_0}\,\frac{d_1d_2}{d}.
> $$
> Plate charges from $\rho_s = \hat{n}\cdot\mathbf{D}$, $\hat{n}$ into the gap: $\rho_{s}(0) = \hat{z}\cdot\epsilon_0\mathbf{E}(0^+) = -\rho_s\,d_2/d$ and $\rho_s(d) = -\hat{z}\cdot\epsilon_0\mathbf{E}(d^-) = -\rho_s\,d_1/d$. They sum to $-\rho_s$ (the image of the sheet); in vacuum the *nearer* plate gets the larger share, and for $d_1 = d/2$ each carries $-\rho_s/2$. HW4 #2: $\epsilon_2 = 2\epsilon_0$ above the sheet, $\epsilon_0$ below, plates at $0$ and $5$ m, sheet $6\epsilon_0$ C/m² at $2$ m; the same steps give $V_0 = 36/7$ V, $\rho_s(0) = -\tfrac{18}{7}\epsilon_0$ and $\rho_s(5) = -\tfrac{24}{7}\epsilon_0$ C/m². With dielectrics the shares go as $\epsilon_i/d_i$ rather than $1/d_i$, so here the *farther* plate, under the $2\epsilon_0$ layer, gets more. (If $\rho_s$ varies slowly in time these are the **quasi-static** fields, valid while $d\ll c/f$.)

## 4. When ε varies continuously: Gauss's law directly

> [!example] Example — a graded dielectric
> Plates at $z=0$ ($V=0$, carrying $\rho_s = 2\epsilon_0$ C/m²) and $z=2$ m bound a dielectric with $\epsilon(z) = \dfrac{4\epsilon_0}{4-z}$ (from $\epsilon_0$ at the bottom to $2\epsilon_0$ at the top). Find $V(2)$.
>
> With no free charge inside, $\nabla\cdot\mathbf{D} = \dfrac{d}{dz}\big(\epsilon E_z\big) = 0$: **$D_z$ is constant**, fixed by the bottom plate, $D_z = \hat{z}\cdot\mathbf{D}(0) = \rho_s = 2\epsilon_0$. Therefore
> $$
> E_z(z) = \frac{D_z}{\epsilon(z)} = \frac{2\epsilon_0(4-z)}{4\epsilon_0} = 2\Big(1-\frac{z}{4}\Big)\ \text{V/m},
> \qquad
> V(2) = V(0) - \int_0^2 2\Big(1-\frac{z}{4}\Big)dz = -2\Big[z - \frac{z^2}{8}\Big]_0^2 = -3\ \text{V}.
> $$
> $\mathbf{E}$ points $+\hat{z}$ away from the positive bottom plate, so the top is lower. Bound charge: $P_z = D_z - \epsilon_0E_z = \epsilon_0z/2$, so $\rho_b = -dP_z/dz = -\epsilon_0/2$ C/m³ throughout, $\rho_{sb} = +\epsilon_0$ on the top face and $0$ on the bottom — total zero. A *uniform* dielectric with no free charge in its bulk has $\rho_b = 0$ (free charge embedded in one drags along $\rho_b = -(\chi_e/\epsilon_r)\rho$); a *graded* $\epsilon$ produces $\rho_b$ with no free charge at all.
>
> Like the two-layer example, $\int_0^2dz/\epsilon_r = 3/2$ and $\lvert V(2)\rvert = 3$ V: only the $\epsilon$ profile along the path matters, since $V = -\int(D/\epsilon)\,dz$ with $D$ constant.

## 5. Spherical symmetry: a charged sphere with a dielectric coat

> [!example] Example — metal sphere, dielectric shell (HW3 #7)
> A metal sphere of radius $a$ carries free charge $Q$; a linear dielectric $\epsilon$ (susceptibility $\chi_e$) fills $a<r<b$; free space beyond. Gauss's law for free charge, for every $r>a$:
> $$
> \mathbf{D} = \frac{Q}{4\pi r^2}\,\hat{r},\qquad
> \mathbf{E} = \begin{cases}0, & r<a\\[4pt] \dfrac{Q}{4\pi\epsilon r^2}\hat{r}, & a<r<b\\[8pt] \dfrac{Q}{4\pi\epsilon_0r^2}\hat{r}, & r>b .\end{cases}
> $$
> Centre potential relative to infinity, summing the drops (none in the metal):
> $$
> V(0) = \int_b^\infty\frac{Q\,dr}{4\pi\epsilon_0r^2} + \int_a^b\frac{Q\,dr}{4\pi\epsilon r^2} = \frac{Q}{4\pi}\Big(\frac{1}{\epsilon_0b} + \frac{1}{\epsilon a} - \frac{1}{\epsilon b}\Big).
> $$
> In the shell, $\mathbf{P} = \epsilon_0\chi_e\mathbf{E} = \Big(1-\dfrac1{\epsilon_r}\Big)\dfrac{Q}{4\pi r^2}\hat{r}$, and $\rho_b = -\nabla\cdot\mathbf{P} = 0$ because $r^2P_r$ is constant. The bound charge sits on the two surfaces: $\rho_{sb}(a) = \mathbf{P}\cdot(-\hat{r}) = -\Big(1-\dfrac1{\epsilon_r}\Big)\dfrac{Q}{4\pi a^2}$ and $\rho_{sb}(b) = +\Big(1-\dfrac1{\epsilon_r}\Big)\dfrac{Q}{4\pi b^2}$ — totals $\mp(1-1/\epsilon_r)Q$, net zero. The negative layer on the metal weakens the shell field from $Q/(4\pi\epsilon_0r^2)$ to $Q/(4\pi\epsilon r^2)$: the dielectric cancels the fraction $1 - 1/\epsilon_r$ of the field, where a metal shell would cancel all of it.

> [!example] Example — which conductor is at the higher potential? (concept check)
> Spherical capacitor: PEC for $r<a$, dielectric $3\epsilon_0$ for $a<r<b$, PEC for $r>b$, equal and opposite charges, $\mathbf{D}$ radially **inward**. So the inner conductor is negative, $\mathbf{E}$ points inward, and $V(b) - V(a) = -\int_a^bE_r\,dr>0$: **$V(b)>V(a)$**. Potential rises walking against the field; $\epsilon$ does not affect the sign.

## 6. Summary

- $\mathbf{D}$ from free charge (Gauss, $D_n$ continuous); $\mathbf{E} = \mathbf{D}/\epsilon$ per region; $V = -\int\mathbf{E}\cdot d\mathbf{l}$ summed over regions; $\mathbf{P} = \mathbf{D}-\epsilon_0\mathbf{E}$ last.
- Interfaces: $E_t$ continuous, $D_n$ continuous (no free charge) ⇒ $\tan\theta_1/\tan\theta_2 = \epsilon_1/\epsilon_2$.
- Laplace/Poisson only inside a homogeneous region; layered ⇒ piecewise plus matching ($V$, $D_n$); graded ⇒ $\nabla\cdot\mathbf{D} = 0$ directly ($D_z$, $rD_r$ or $r^2D_r$ constant).
- Bound charge: $\rho_{sb} = \mathbf{P}\cdot\hat{n}$ on faces, $\rho_b = -\nabla\cdot\mathbf{P}$ (graded $\epsilon$, or free charge inside); total zero.

Concept pages: [[concepts/boundary-conditions]] · [[concepts/permittivity]] · [[concepts/polarization]].

> [!exam] On Exam 1
> FA26 problems 3 and 4 are both this lecture. Problem 3 is §2 verbatim (find $\mathbf{E}_2$, then $\mathbf{D}_{1,2}$, then $\mathbf{P}_{1,2}$); problem 4(a)–(b) is the planar chain in cylindrical dress (one $\mathbf{D}$ across both dielectric layers of a coax, then $\mathbf{E} = \mathbf{D}/\epsilon$ layer by layer). Worked in [[problems/fields-across-a-dielectric-interface]] and [[problems/two-layer-coaxial-capacitor]]. The most common error in both: writing $\mathbf{D}$ with an $\epsilon$ in it, i.e. confusing $\mathbf{D}$ with $\mathbf{E}$.

> [!tip] Practice this lecture
> [[practice/09-static-fields-in-dielectric-media|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/09-static-fields-in-dielectric-media#91-three-layers-between-charged-plates|9.1 Three layers between charged plates]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 9 (rules; homogeneous vs inhomogeneous; Examples 1–4: slab, two layers, sheet between grounded plates with the quasi-static remark, graded $\epsilon(z)$). Shao, Lecture 9 slides (slab; partially filled plates both ways; spherical-shell challenge). FA26 HW3 #7, HW4 #1–#3. Slips in the course material: see [[0-toolkit/04-errata-in-the-course-materials|errata]].
