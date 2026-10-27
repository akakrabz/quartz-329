---
title: "Lecture 5 — Curl-free fields and the electrostatic potential"
description: "Because static E has zero curl, E·dl is an exact differential and a scalar potential V exists with E = −∇V. Potential difference is work per unit charge; V comes from E by a path-independent line integral and from charge by scalar superposition; equipotentials are perpendicular to E."
tags: [lecture, electrostatics, exam-1]
lecture: 5
---

*Lecture 5 · course notes §5 · slides "Potential Functions for Static Fields" · prev: [[1-electrostatics/04-divergence-and-curl|Lecture 4]] · next: [[1-electrostatics/06-circulation-and-boundary-conditions|Lecture 6]] · practice: [[practice/05-electrostatic-potential|12 problems]]*

> [!abstract] In one breath
> Because $\nabla\times\mathbf{E} = 0$ (Lecture 4), a static field is the **gradient of a scalar**, $\mathbf{E} = -\nabla V$, and $V$ is the familiar **voltage** — work per unit charge to move a test charge between two points, independent of route. $V$ to $\mathbf{E}$: a derivative; $\mathbf{E}$ to $V$: a line integral along any convenient path; charge to $V$: scalar superposition. Poisson's equation, conductors as equipotentials and capacitance are all easier in $V$ than in $\mathbf{E}$.

## 1. Why a potential: energy per unit charge

Move a charge $q$ through $d\mathbf{l}$ in a field $\mathbf{E}$. The field does work $q\mathbf{E}\cdot d\mathbf{l}$; *you* (holding it against the field) do $-q\mathbf{E}\cdot d\mathbf{l}$, the increase in potential energy:

$$
dU = -q\,\mathbf{E}\cdot d\mathbf{l}.
$$

To describe the *field alone* (as $gh$ does for gravity, whatever the mass), divide by $q$:

> [!key] Potential difference
> $$
> V(b) - V(a) = -\int_a^b \mathbf{E}\cdot d\mathbf{l}\qquad[\text{V} = \text{J/C} = \text{N·m/C}]
> $$
> is the work per unit charge to carry a test charge from $a$ to $b$ against the field. Equivalently, $\displaystyle\int_a^b\mathbf{E}\cdot d\mathbf{l} = V(a) - V(b)$ is the **voltage drop** from $a$ to $b$: work per unit charge done by the *field*. Units of $\mathbf{E}$: N/C = V/m.

The field's work becomes kinetic energy (a free charge between capacitor plates) or heat (charge dragged through a resistor), paid from the field's stored energy. Charge pushed *against* the field (inside a battery): negative field work, a voltage *rise* along the motion, and the stored energy grows.

## 2. From V to E: the gradient

For an infinitesimal step $dV = -\mathbf{E}\cdot d\mathbf{l} = -(E_x\,dx + E_y\,dy + E_z\,dz)$; the total differential is $dV = \dfrac{\partial V}{\partial x}dx + \dfrac{\partial V}{\partial y}dy + \dfrac{\partial V}{\partial z}dz$. Matching coefficients:

> [!key] The most important definition of the day
> $$
> \mathbf{E} = -\nabla V,\qquad \nabla V \equiv \hat{x}\frac{\partial V}{\partial x} + \hat{y}\frac{\partial V}{\partial y} + \hat{z}\frac{\partial V}{\partial z}.
> $$
> The **gradient** $\nabla V$ points where $V$ increases fastest, with magnitude equal to that rate. The minus sign (a convention) makes $\mathbf{E}$ point from **high** to **low** potential: positive charges "fall" downhill, like rocks.

<!-- fig:equipotentials-gradient -->

> [!intuition] Mount Electron
> $V$ is altitude on a topographic map; contours are **equipotentials** (no work to move a charge along them). The gradient points straight uphill, perpendicular to the contours; $\mathbf{E}$ points *downhill*. Crowded contours: steep, strong field; spread contours: weak field. Memorize: **$\mathbf{E}$ is everywhere perpendicular to the equipotentials**, and **$\lvert\mathbf{E}\rvert$ is the potential drop per unit distance** along the steepest direction.

> [!example] Example — E from V
> $V = x^2 - 6y$ V. Then $\mathbf{E} = -\nabla V = -2x\,\hat{x} + 6\,\hat{y}$ V/m. At the origin $\mathbf{E} = 6\hat{y}$: $V$ decreases with $y$, and the field points toward decreasing $V$. Equipotentials $x^2 - 6y = \text{const}$ are parabolas, crossed at right angles by the arrows in the figure.

Cylindrical and spherical gradients carry metric factors ([[0-toolkit/02-vector-calculus-cheatsheet|cheat sheet]]):

$$
\nabla V = \hat{r}\frac{\partial V}{\partial r} + \hat{\phi}\frac{1}{r}\frac{\partial V}{\partial\phi} + \hat{z}\frac{\partial V}{\partial z},
\qquad
\nabla V = \hat{r}\frac{\partial V}{\partial r} + \hat{\theta}\frac{1}{r}\frac{\partial V}{\partial\theta} + \hat{\phi}\frac{1}{r\sin\theta}\frac{\partial V}{\partial\phi}.
$$

## 3. Why V exists at all: exact differentials

Any $V$ gives a curl-free $\mathbf{E} = -\nabla V$:

$$
\nabla\times(\nabla V) =
\begin{vmatrix}\hat{x}&\hat{y}&\hat{z}\\[2pt] \partial_x&\partial_y&\partial_z\\[2pt] \partial_xV&\partial_yV&\partial_zV\end{vmatrix}
= \hat{x}\,(\partial_y\partial_zV - \partial_z\partial_yV) + \cdots = 0
$$

(mixed partials commute). The useful converse: **if $\nabla\times\mathbf{E} = 0$, a potential exists**, because $\mathbf{E}\cdot d\mathbf{l} = E_x\,dx + E_y\,dy + E_z\,dz$ is then an **exact differential** — the total differential $-dV$ of a single function — and can be "antidifferentiated". Two tiny fields:

- $\mathbf{E} = y\,\hat{x} + x\,\hat{y}$: $\mathbf{E}\cdot d\mathbf{l} = y\,dx + x\,dy = d(xy)$, exact. So $dV = -d(xy)$ and $V = -xy + C$. (Check: $-\nabla(-xy) = y\hat{x}+x\hat{y}$ ✓.)
- $\mathbf{E} = y\,\hat{x} - x\,\hat{y}$: $y\,dx - x\,dy$ is *not* a differential. $\partial V/\partial x = -y$ forces $V = -xy + f(y,z)$, so $\partial V/\partial y = -x + \partial f/\partial y$, never the required $+x$. No $V$ — and $\nabla\times\mathbf{E} = -2\hat{z}\neq 0$.

$C$ lets you put $V=0$ anywhere: the **ground** or **reference point**. Only *differences* are physical.

> [!trap] $\nabla\cdot\nabla V$ is not zero
> A slide says $\mathbf{E} = -\nabla V$ "satisfies Gauss's law by the identity $\nabla\cdot\nabla V = 0$". The identity is $\nabla\times\nabla V = 0$, which makes $\mathbf{E} = -\nabla V$ satisfy the *curl* equation. $\nabla\cdot\nabla V = \nabla^2V$ is the Laplacian, and Gauss's law makes it Poisson's equation, $\nabla^2V = -\rho/\epsilon_0$ ([[1-electrostatics/07-poisson-and-laplace|Lecture 7]]).

## 4. Path independence

$\int_a^b\mathbf{E}\cdot d\mathbf{l}$ is the limit of sums $\sum_j\mathbf{E}_j\cdot\Delta\mathbf{l}_j$ along a chosen path, $\Delta\mathbf{l}_j$ pointing from $a$ toward $b$; in general it depends on the path. For a curl-free field $\mathbf{E}\cdot d\mathbf{l} = -dV$, and the $-dV$'s along any route sum to $V(a) - V(b)$ — the fundamental theorem of calculus (the gradient theorem of [[1-electrostatics/04-divergence-and-curl#1-from-the-fundamental-theorem-of-calculus-to-stokes|Lecture 4 §1]]).

<!-- fig:path-independence -->

> [!example] Example — two paths, two fields
> Integrate $\mathbf{E} = y\,\hat{x} \pm x\,\hat{y}$ from $o = (0,0,0)$ to $p = (1,1,0)$ along $C_u$ (up the $y$-axis, then across) and $C_l$ (along the $x$-axis, then up). On each leg one coordinate is fixed and its differential vanishes — strike those terms out visibly.
> $$
> C_u:\ \int_{y=0}^{1}(\pm x)\,dy\Big|_{x=0} + \int_{x=0}^{1}y\,dx\Big|_{y=1} = 0 + 1 = 1,
> \qquad
> C_l:\ \int_{x=0}^{1}y\,dx\Big|_{y=0} \pm \int_{y=0}^{1}x\,dy\Big|_{x=1} = 0 \pm 1 = \pm 1.
> $$
> $+$ sign: both paths give 1 — path independent, $V(p) - V(o) = -1$, as $V=-xy$ predicts. $-$ sign: $+1$ versus $-1$, no potential. The difference, 2, is the flux of $\nabla\times\mathbf{E} = -2\hat{z}$ through the square with the loop's (clockwise, $-\hat{z}$) orientation: Stokes' theorem, checked.

> [!intuition] What a voltmeter measures
> An ideal voltmeter on $p$ and $o$ reads $\int_p^o\mathbf{E}\cdot d\mathbf{l}$ *along its own leads* — a meaningful "voltage between two points" only because static fields make it independent of lead routing. With Faraday's law ([[2-magnetostatics/14-faradays-law-and-induced-emf|Lecture 14]]) the induced $\mathbf{E}$ has curl, and the reading depends on where you drape the wires.

## 5. From E to V: two recipes

$V(\mathbf{r}) = V(\mathbf{r}_{\text{ref}}) - \int_{\mathbf{r}_{\text{ref}}}^{\mathbf{r}}\mathbf{E}\cdot d\mathbf{l}$, evaluated two ways.

> [!recipe] V from E
> 0. **Check the curl.** If $\nabla\times\mathbf{E}\neq 0$, stop: there is no $V$.
> 1. **Spot the exact differential.** Regroup $\mathbf{E}\cdot d\mathbf{l}$ with the product rule backwards ($y\,dx + x\,dy = d(xy)$, $y\,dz + z\,dy = d(yz)$, $2x\,dx = d(x^2)$, …), until it reads $d(\text{something})$. Then $V = -(\text{something}) + C$.
> 2. **Or integrate along an axis-parallel staircase** from the reference: $(0,0,0)\to(x,0,0)\to(x,y,0)\to(x,y,z)$. One differential per leg; other coordinates at their *current* values (0 on the first leg, $x$ fixed on the second, $x$ and $y$ on the third).
> 3. **Fix $C$** from the reference condition ($V=0$ at the origin, or at infinity).
> 4. **Check:** $-\nabla V$ must give back $\mathbf{E}$.

> [!example] Example — both recipes on one field
> $\mathbf{E} = 2x\,\hat{x} + 3z\,\hat{y} + 3(y+1)\,\hat{z}$ V/m with $V(0,0,0) = 0$. (Curl: $\partial_yE_z - \partial_zE_y = 3 - 3 = 0$, the other components trivially zero ✓.)
>
> *Exact differential:* $\mathbf{E}\cdot d\mathbf{l} = 2x\,dx + 3z\,dy + 3y\,dz + 3\,dz = d(x^2) + 3\,d(yz) + 3\,dz = d(x^2 + 3yz + 3z)$, so $V = -x^2 - 3yz - 3z + C$, and $V(0)=0$ gives $C=0$.
>
> *Staircase:* $V(X,Y,Z) = -\int_0^X 2x\,dx\big|_{y=z=0} - \int_0^Y 3z\,dy\big|_{x=X,\,z=0} - \int_0^Z 3(y+1)\,dz\big|_{x=X,\,y=Y} = -X^2 - 0 - 3(Y+1)Z.$
>
> Both: $V(x,y,z) = -x^2 - 3(y+1)z$ V. Check: $-\nabla V = 2x\,\hat{x} + 3z\,\hat{y} + 3(y+1)\,\hat{z}$ ✓. From the slides: $\mathbf{E} = yz\,\hat{x} + (y+zx)\,\hat{y} + xy\,\hat{z}$ gives $\mathbf{E}\cdot d\mathbf{l} = d(xyz) + y\,dy$, so $V = -xyz - \tfrac12y^2$.

> [!trap] Three ways to lose the sign
> 1. **Forgetting the minus** in $V(b) - V(a) = -\int_a^b\mathbf{E}\cdot d\mathbf{l}$. Moving away from a positive charge, $V$ must fall.
> 2. **Counting the direction twice.** Radially inward from $\infty$: $d\mathbf{l} = \hat{r}\,dr$, and the limits $\int_\infty^{r}$ carry the direction ($dr<0$ automatically). $d\mathbf{l} = -\hat{r}\,dr$ *and* $\infty\to r$ flips the sign twice.
> 3. **Antidifferentiating each component separately and adding** ($\int E_x\,dx + \int E_y\,dy + \int E_z\,dz$, all variables free) double-counts cross terms — $3yz$ twice above. One integral, one path.

## 6. From charge to V: the point charge and superposition

Point charge $Q$ at the origin, $\mathbf{E} = \dfrac{Q}{4\pi\epsilon_0r^2}\hat{r}$; reference at infinity, integrate inward along a radius, $d\mathbf{l} = \hat{r}\,dr$:

$$
V(r) = V(\infty) - \int_\infty^{r}\frac{Q}{4\pi\epsilon_0r'^2}\,dr' = 0 - \Big[-\frac{Q}{4\pi\epsilon_0r'}\Big]_\infty^{r}
$$

> [!key] Potential of a point charge, and superposition
> $$
> V(r) = \frac{Q}{4\pi\epsilon_0\,r}\quad[\text{V}],\qquad V(\mathbf{r}) = \frac{1}{4\pi\epsilon_0}\sum_i\frac{Q_i}{\lvert\mathbf{r}-\mathbf{r}_i\rvert},\qquad V(\mathbf{r}) = \frac{1}{4\pi\epsilon_0}\int\frac{\rho(\mathbf{r}')\,d^3\mathbf{r}'}{\lvert\mathbf{r}-\mathbf{r}'\rvert}.
> $$
> $V$ falls as $1/r$ (one power slower than $\mathbf{E}$); equipotentials are concentric spheres; superposition is a **scalar** sum — no components or unit vectors; take $-\nabla$ once at the end for the field. (Exact-differential route, one line: $\mathbf{E}\cdot d\mathbf{l} = \dfrac{Q\,dr}{4\pi\epsilon_0r^2} = d\!\Big(\!-\dfrac{Q}{4\pi\epsilon_0r}\Big) = -dV$.)

> [!example] Example — the hydrogen atom in volts
> Proton's potential at the Bohr radius $a = 0.529\times10^{-10}$ m: $V(a) = \dfrac{e}{4\pi\epsilon_0a} = \dfrac{(1.6\times10^{-19})(9\times10^{9})}{0.529\times10^{-10}} \approx 27.2$ V. A charge $q$ at $\mathbf{r}$ has $U = qV(\mathbf{r})$: an electron there has $U = -e\,V(a) = -27.2$ eV (a second proton $+27.2$ eV). $1\ \text{eV} = 1.602\times10^{-19}$ J is "charge $e$ times one volt". The ground-state energy, $-13.6$ eV, is half this potential energy; the electron's kinetic energy cancels the other half.

> [!trap] When "zero at infinity" is not available
> $V(\infty)=0$ needs finite total charge. For an infinite line, sheet or slab $\int_\infty^r\mathbf{E}\cdot d\mathbf{l}$ diverges, so the problem must give a reference — "$V(0)=0$" in [[problems/charged-slab-with-a-power-law-profile|the slab problem]]. Line charge: $V(r) = -\dfrac{\rho_l}{2\pi\epsilon_0}\ln\dfrac{r}{r_0}$ with $V(r_0)=0$ — logarithms, not $1/r$. Only the bookkeeping constant moves.

## 7. Summary

- $V(b) - V(a) = -\int_a^b\mathbf{E}\cdot d\mathbf{l}$: work per unit charge, path-independent because $\nabla\times\mathbf{E}=0$.
- $\mathbf{E} = -\nabla V$: downhill, perpendicular to equipotentials, "volts per metre".
- Existence of $V$ ⇔ $\mathbf{E}\cdot d\mathbf{l}$ exact ⇔ curl-free ⇔ conservative ([[concepts/conservative-field]]).
- $V$ from $\mathbf{E}$: check curl → exact differential or staircase path → fix the constant → verify with $-\nabla V$.
- $V$ from charge: $Q/(4\pi\epsilon_0r)$ and scalar superposition; $U = qV$.
- The reference point is yours to choose; only differences matter.

Concept pages: [[concepts/electrostatic-potential]] · [[concepts/conservative-field]].

> [!exam] On Exam 1
> FA26 1(b): $V(x,y,z)$ from a polynomial field with $V(0,0,0)=0$ — staircase, or exact differential if you see it. 1(d): $\int_A^B\mathbf{E}\cdot d\mathbf{l}$ between named points is $V(A) - V(B)$ (no path: the curl was checked in 1(a)). 2(c): $V(b)$ outside a charged slab with $V(0)=0$ — integrate $-E_x\,dx$ from 0 to $b$, split where the field changes form. Worked with new numbers in [[problems/curl-potential-and-charge-from-a-field]] and [[problems/charged-slab-with-a-power-law-profile]]. The grader checks the sign first.

> [!tip] Practice this lecture
> [[practice/05-electrostatic-potential|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/05-electrostatic-potential#51-uniform-field-between-two-points|5.1 Uniform field between two points]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 5 (gradient, $\nabla\times\nabla V = 0$; exact/inexact differentials, $\pm$ example; path integral; Examples 1–3, 5, 6; voltmeter; Bohr factoid). Shao, Lecture 5 slides (work against the field; Mount Electron; equipotential spacing; two-path example; point-charge potential, $dr<0$ warning; $V$ from $\mathbf{E}$ two ways; curvilinear gradients). Slips in the course material: see [[0-toolkit/04-errata-in-the-course-materials|errata]].
