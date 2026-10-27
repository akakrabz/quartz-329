---
title: "Lecture 3 — Gauss's law at work: flux, symmetry, and charge densities"
description: "Flux; the three symmetric cases where Gauss's law gives E in two lines (line, sheet, slab) and their superposition (pn junction); charge densities and δ-functions; the half-space flux argument; ∮B·dS = 0."
tags: [lecture, electrostatics, exam-1]
lecture: 3
---

*Lecture 3 · course notes §3 · slides "Surface integrals, connecting Coulomb's and Gauss's law" · prev: [[1-electrostatics/02-coulombs-law-superposition-and-gauss|Lecture 2]] · next: [[1-electrostatics/04-divergence-and-curl|Lecture 4]] · practice: [[practice/03-gauss-law-at-work|12 problems]]*

> [!abstract] In one breath
> The flux of $\mathbf{D}$ out of a closed surface always equals the charge inside. When symmetry makes $|\mathbf{D}|$ *constant* and *normal* on a well-chosen surface, the integral collapses to "$D\times$area" and $\mathbf{E}$ falls out in two lines. Three symmetries do this: spherical, cylindrical, planar. The rest of the lecture builds the tool (flux, densities, δ-functions) or superposes these three.

## 1. Flux: counting arrows through a surface

The **flux** of $\mathbf{F}$ through a small flat patch $\Delta\mathbf{S}$ (magnitude = area, direction = chosen normal $\hat{n}$) is

$$
\Delta\psi = \mathbf{F}\cdot\Delta\mathbf{S} = (\mathbf{F}\cdot\hat{n})\,\Delta S = F\cos\alpha\,\Delta S = F_n\,\Delta S .
$$

Only the normal component pokes through: it depends on arrow density ($|\mathbf{F}|$), tilt ($\cos\alpha$) and size ($\Delta S$).

<!-- fig:flux-patch -->

A curved surface is tiled with flat patches and summed — the surface integral:

$$
\psi = \sum_j \mathbf{F}_j\cdot\Delta\mathbf{S}_j \;\longrightarrow\; \psi = \int_S \mathbf{F}\cdot d\mathbf{S} .
$$

> [!tip] The "trick that works sometimes" — and it is the whole method
> Field **uniform in magnitude** and **everywhere parallel to $d\mathbf{S}$**: $\int_S\mathbf{F}\cdot d\mathbf{S} = F\cdot A$. Field **parallel to the surface**: flux **zero**. Every Gauss's-law surface in this course is built only from these two kinds of piece.

A closed surface's normal is **outward**, and its flux integral is written $\oint_S$. An open surface needs a *chosen* $\hat{n}$; flip it and the flux changes sign. Concept page: [[concepts/flux]].

## 2. Gauss's law, restated for use

From Lecture 2, with $\mathbf{D} = \epsilon_0\mathbf{E}$ (C/m²):

> [!key] Gauss's law
> $$
> \psi_E = \oint_S \mathbf{D}\cdot d\mathbf{S} = Q_{\text{enc}} \quad [\text{C}]
> $$
> Flux of $\mathbf{D}$ **out** of any closed surface = net charge **inside**. Charges outside contribute nothing; $Q_{\text{enc}}$ is the algebraic sum of what is inside.

Concept checks, by symmetry and superposition alone:

- $Q$ at the centre of a **cube**: flux $Q$ in total, $Q/6$ through each face.
- $Q$ at the centre of a **very thin box** ($h\to 0$): nearly all flux leaves through the two big faces, $Q/2$ each.
- $Q$ at the centre of the flat face of a **hemisphere**: $Q/2$ through the dome, **zero** through the flat base (field tangential there); the other half go into the lower half-space. (The charge sits *on* the surface: "enclosed" is solid angle, $2\pi$ of $4\pi$.)
- $Q$ a distance $h$ above an **infinite plane**: half the lines cross it, so the flux is $\pm Q/2$, sign fixed by your normal.

<!-- fig:flux-plane -->

That is the in-class "challenge question", a superposition problem: with charges above and below the plane, add $\pm Q_i/2$, sign set by whether that charge's lines cross along or against $\hat{n}$. Worked with other numbers in [[problems/flux-through-a-plane-from-two-charges]].

## 3. The three symmetries

Same four lines every time; the art is choosing the surface.

> [!recipe] Gauss's law for a field
> 1. **Argue the symmetry** (Coulomb + superposition): which way does $\mathbf{D}$ point, what can it depend on? *Spherical* → $\mathbf{D} = D(r)\hat{r}$. *Cylindrical* (infinite line/cylinder) → $D(r)\hat{r}$ with cylindrical $r$. *Planar* (infinite sheet/slab) → $D(x)\hat{x}$, odd in $x$ about the symmetry plane.
> 2. **Choose the Gaussian surface** so every piece is either "$\mathbf{D}\parallel d\mathbf{S}$ with $|\mathbf{D}|$ constant" or "$\mathbf{D}\perp d\mathbf{S}$": a concentric sphere; a coaxial cylinder (caps contribute 0); a pillbox straddling the symmetry plane (sides contribute 0).
> 3. **Write the bookkeeping** — *top + bottom + side* — and set flux $= Q_{\text{enc}}$. Cancel the arbitrary $L$ or $A$.
> 4. **Convert**: $\mathbf{E} = \mathbf{D}/\epsilon_0$ (vacuum); attach direction and **units** in brackets.

### 3a. Infinite line charge (cylindrical)

<!-- fig:gauss-cylinder -->

Coaxial cylinder, radius $r$, length $L$. Caps: $\mathbf{D}\perp d\mathbf{S}$, zero. Side: $D$ constant, parallel to $d\mathbf{S}$, giving $D\cdot 2\pi rL$. Enclosed $\rho_l L$:

$$
D\,(2\pi r L) = \rho_l L \;\Rightarrow\; \mathbf{D} = \frac{\rho_l}{2\pi r}\hat{r}\ [\text{C/m}^2],\qquad
\mathbf{E} = \frac{\rho_l}{2\pi\epsilon_0 r}\hat{r}\ [\text{V/m}] .
$$

Same as Lecture 2's Coulomb integral, in one line.

### 3b. Infinite sheet (planar)

Sheet $\rho_s$ on $z=0$. By symmetry $\mathbf{D} = D(z)\hat{z}$ points away on both sides, $D(-z) = -D(z)$. Pillbox, caps of area $A$ at $\pm z$: sides 0 (field parallel), each cap $D\cdot A$ (normal *and* field point away from the sheet):

$$
2\,D\,A = \rho_s A \;\Rightarrow\; \mathbf{E} = \hat{z}\,\text{sgn}(z)\,\frac{\rho_s}{2\epsilon_0}
\qquad(\text{sgn}(z) = \pm1 \text{ for } z\gtrless 0).
$$

**No distance dependence** — the same at 1 mm and 1 km, because more of the sheet "looks close" as you move away.

### 3c. Uniform slab (planar, with interior)

<!-- fig:sheet-slab -->

Slab $\rho$ (C/m³) filling $-W/2<x<W/2$. Same pillbox, caps at $\pm x$, area $A$; $Q_{\text{enc}}$ now depends on the caps' position:

- Inside ($|x|<W/2$): $Q_{\text{enc}} = \rho\,A\,(2x)$, so $2DA = 2\rho A x$ and $\mathbf{D} = \rho x\,\hat{x}$.
- Outside ($|x|\ge W/2$): $Q_{\text{enc}} = \rho A W$, so $\mathbf{D} = \dfrac{\rho W}{2}\text{sgn}(x)\,\hat{x}$ — the field of a sheet with $\rho_s = \rho W$.

$$
\mathbf{E} =
\begin{cases}
\dfrac{\rho\,x}{\epsilon_0}\,\hat{x}, & |x| < W/2\\[8pt]
\dfrac{\rho W}{2\epsilon_0}\,\text{sgn}(x)\,\hat{x}, & |x| \ge W/2
\end{cases}
$$

Linear inside (zero on the symmetry plane), constant outside, continuous at the faces (no surface charge). Memorize the *shape*: it is the building block for §4 and for the FA26 exam's [[problems/charged-slab-with-a-power-law-profile|non-uniform slab]].

> [!key] Static fields you should recognize on sight
> | source | $\mathbf{E}$ | dependence |
> |---|---|---|
> | point $Q$ | $\dfrac{Q}{4\pi\epsilon_0 r^2}\hat{r}$ | $1/r^2$ |
> | line $\rho_l$ | $\dfrac{\rho_l}{2\pi\epsilon_0 r}\hat{r}$ | $1/r$ |
> | sheet $\rho_s$ at $x=0$ | $\dfrac{\rho_s}{2\epsilon_0}\text{sgn}(x)\,\hat{x}$ | none |
> | slab $\rho$, $\lvert x\rvert<W/2$ | inside $\dfrac{\rho x}{\epsilon_0}\hat{x}$; outside $\dfrac{\rho W}{2\epsilon_0}\text{sgn}(x)\hat{x}$ | linear, then flat |
> | uniform cylinder $\rho$, radius $R$ | inside $\dfrac{\rho r}{2\epsilon_0}\hat{r}$; outside $\dfrac{\rho R^2}{2\epsilon_0 r}\hat{r}$ | linear, then $1/r$ |

> [!trap] Three ways the pillbox goes wrong
> 1. **Forgetting the second cap.** Both caps carry flux — the 2 in $2DA$. One cap is legitimate only after arguing $E=0$ on the other (e.g., a cap on the symmetry plane).
> 2. **Uniform-slab formula for a non-uniform slab.** If $\rho$ depends on $x$, $Q_{\text{enc}} = A\int_{-x}^{x}\rho\,dx'$, not $\rho\cdot 2xA$.
> 3. **Dropping sgn.** The field on the left points left. Write $\text{sgn}(x)\hat{x}$ (or "$\pm\hat{x}$" with cases), and check $\mathbf{E}$ is continuous where there is no sheet charge.

## 4. Superposition of the building blocks

Anything assembled from sheets and slabs is solved by adding known fields — no new integrals.

> [!example] Two opposite sheets (a parallel-plate capacitor, in embryo)
> $+\rho_s$ on $x=-W/2$, $-\rho_s$ on $x=+W/2$. Each sheet gives $\pm\dfrac{\rho_s}{2\epsilon_0}$; they cancel outside and add between:
> $$
> \mathbf{E} = \frac{\rho_s}{\epsilon_0}\,\hat{x}\ \text{ for } |x|<\tfrac{W}{2},\qquad \mathbf{E} = 0 \text{ otherwise.}
> $$
> The parallel-plate capacitor field (Lecture 10), pointing from + to −.

> [!example] A pn junction's depletion region (ECE 340 preview)
> Acceptor charge $-\rho_1$ fills $-W_1<x<0$, donor charge $+\rho_2$ fills $0<x<W_2$, $\rho_1W_1 = \rho_2W_2$ (neutral). Add the two slab fields, each shifted to its layer's centre:
>
> - layer 1 alone: $+\dfrac{\rho_1W_1}{2\epsilon_0}$ for $x<-W_1$, ramping down to $-\dfrac{\rho_1W_1}{2\epsilon_0}$ at $x=0$, flat beyond;
> - layer 2 alone: $-\dfrac{\rho_2W_2}{2\epsilon_0}$ for $x<0$, ramping up to $+\dfrac{\rho_2W_2}{2\epsilon_0}$ at $x = W_2$, flat beyond.
>
> Outside, the plateaus cancel (neutrality); inside each layer, its ramp is shifted by the other layer's plateau:
> $$
> \mathbf{E} =
> \begin{cases}
> -\dfrac{\rho_1}{\epsilon_0}(x+W_1)\,\hat{x}, & -W_1<x<0\\[6pt]
> \dfrac{\rho_2}{\epsilon_0}(x-W_2)\,\hat{x}, & 0<x<W_2\\[6pt]
> 0, & \text{otherwise}
> \end{cases}
> $$
> a triangle peaking at $-\rho_1W_1/\epsilon_0$ at the junction, pointing from n side to p side — the built-in field that stops further diffusion.

<!-- fig:pn-superposition -->

The instructor solved this on the whiteboard *by reusing the slab result*. The habit: **recognize the building blocks, then superpose.**

## 5. Charge densities and δ-functions

Gauss's law uses a volume density $\rho$, but charge often lives on points, lines, sheets. The unifying device is the **impulse** (Dirac δ) from ECE 210:

$$
\int_{-\infty}^{\infty}\delta(x)\,dx = 1,\qquad \delta(x-x_0) = 0\ \text{for } x\ne x_0,\qquad [\delta(x)] = \tfrac{1}{\text{m}} .
$$

| charge | volume density $\rho(x,y,z)$ |
|---|---|
| point $Q$ at $(x_0,y_0,z_0)$ | $Q\,\delta(x-x_0)\,\delta(y-y_0)\,\delta(z-z_0)$ |
| line $\rho_l$ along $z$ through $(x_0,y_0)$ | $\rho_l\,\delta(x-x_0)\,\delta(y-y_0)$ |
| sheet $\rho_s(y,z)$ on $x=x_0$ | $\rho_s(y,z)\,\delta(x-x_0)$ |

Units each time: $[\text{C}]\cdot[1/\text{m}]^3 = \text{C/m}^3$ ✓. Integrating $\rho$ over a volume recovers the total charge, so $Q_{\text{enc}} = \int_V\rho\,dV$ covers points, lines, sheets and volumes at once — as does Lecture 4's differential Gauss's law.

Concept page: [[concepts/charge-density]].

## 6. The magnetic counterpart: ∮ B·dS = 0

Magnetic field lines have no ends: they close or run on forever. The slides' "Yadaraf bugs" (Faraday backwards) always return to their hole, so any *closed* net catches as many leaving as returning. The second Maxwell equation:

> [!key] Gauss's law for magnetism
> $$
> \psi_B = \oint_S \mathbf{B}\cdot d\mathbf{S} = 0 \quad\text{for every closed surface } S.
> $$
> No magnetic charge. An *open* surface can have nonzero magnetic flux (Faraday's law, [[2-magnetostatics/14-faradays-law-and-induced-emf|Lecture 14]]); a *closed* one never does.

## 7. Summary

- Flux = normal component × area, summed; closed surface = "flux out".
- $\oint_S\mathbf{D}\cdot d\mathbf{S} = Q_{\text{enc}}$ is always true, *useful* when symmetry makes $D$ constant on a sphere, cylinder or pillbox.
- Point $1/r^2$, line $1/r$, sheet constant, slab linear-then-constant; superpose.
- $\oint_S\mathbf{B}\cdot d\mathbf{S} = 0$.

> [!exam] On Exam 1
> FA26 problem 2: slab with $\rho\propto|x|$ — pillbox, both caps, $Q_{\text{enc}}$ as an integral, sgn on the direction, then a potential (Lecture 5). Problem 4: coaxial cylinder with two dielectric layers — §3a's Gaussian cylinder, $\mathbf{D}$ independent of material, $\mathbf{E} = \mathbf{D}/\epsilon$ layer by layer (Lecture 9). Write "top + bottom + side" explicitly; state units.

> [!tip] Practice this lecture
> [[practice/03-gauss-law-at-work|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/03-gauss-law-at-work#31-two-sheets-of-charge|3.1 Two sheets of charge]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 3 (sheet, slab, two sheets, two slabs = pn junction, δ-function formalism, dipole flux example). Shao, Lecture 3 slides (flux intuition, "trick that works sometimes", symmetry ladder, challenge questions, line/sheet/slab derivations, Yadaraf bugs) and Lecture 4 whiteboard page (pn junction by superposition). Slips in the course material: see [[0-toolkit/04-errata-in-the-course-materials|errata]].
