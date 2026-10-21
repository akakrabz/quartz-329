---
title: "Lecture 4 — Divergence and curl: Maxwell's equations at a point"
description: "Shrinking Gauss's law to a point gives the divergence; shrinking a circulation to a point gives the curl. The divergence theorem and Stokes' theorem connect the integral and differential forms of all four Maxwell equations; static E fields are curl-free."
tags: [lecture, electrostatics, exam-1]
lecture: 4
---

*Lecture 4 · course notes §4 · slides "Divergence and curl, Maxwell's equations in differential form" · prev: [[1-electrostatics/03-gauss-law-at-work|Lecture 3]] · next: [[1-electrostatics/05-curl-free-fields-and-the-electrostatic-potential|Lecture 5]] · practice: [[practice/04-divergence-and-curl|12 problems]]*

> [!abstract] In one breath
> Apply Gauss's law to a vanishingly small box and divide by its volume: the **divergence** of $\mathbf{D}$ equals the charge density *at that point*, $\nabla\cdot\mathbf{D} = \rho$. The same move on a tiny loop turns a circulation $\oint\mathbf{E}\cdot d\mathbf{l}$ into the **curl**. Divergence = "flux per unit volume" (sources); curl = "circulation per unit area" (whirlpools). The divergence and Stokes' theorems switch between integral and differential laws — and static electric fields have zero curl, which makes voltage possible (Lecture 5).

## 1. From the fundamental theorem of calculus to Stokes

One idea: *chop a region into tiny pieces, add a local quantity over them; interior contributions cancel, leaving only the boundary.*

- **1-D**: $\displaystyle\int_a^b \frac{df}{dx}\,dx = f(b)-f(a)$.
- **Along a curve** (gradient theorem): $\displaystyle\int_a^b \nabla f\cdot d\mathbf{l} = f(b) - f(a)$, where $\nabla f = \hat{x}\dfrac{\partial f}{\partial x}+\hat{y}\dfrac{\partial f}{\partial y}+\hat{z}\dfrac{\partial f}{\partial z}$ is the gradient (steepest increase; $df = \nabla f\cdot d\mathbf{l}$). Only the endpoints matter, so $\oint_C\nabla f\cdot d\mathbf{l} = 0$ around any *closed* loop: a gradient field is **conservative**, or **curl-free**.
- **Over a surface** (Stokes) and **through a volume** (divergence theorem): below.

$\nabla$ ("del") $= \left(\dfrac{\partial}{\partial x},\dfrac{\partial}{\partial y},\dfrac{\partial}{\partial z}\right)$; dotted into a field it gives the divergence, crossed the curl. Formulas: [[0-toolkit/02-vector-calculus-cheatsheet]].

## 2. Divergence: flux per unit volume

Apply $\oint_S\mathbf{D}\cdot d\mathbf{S} = \int_V\rho\,dV$ to a tiny box $\Delta x\,\Delta y\,\Delta z$ centred at $(x,y,z)$. Flux out of the two faces perpendicular to $\hat{x}$:

$$
\Big[D_x\big(x+\tfrac{\Delta x}{2}\big) - D_x\big(x-\tfrac{\Delta x}{2}\big)\Big]\Delta y\,\Delta z \approx \frac{\partial D_x}{\partial x}\,\Delta x\,\Delta y\,\Delta z ,
$$

likewise for the other pairs; enclosed charge $\rho\,\Delta x\Delta y\Delta z$. Divide by the volume and shrink:

> [!key] Divergence, and Gauss's law in differential form
> $$
> \nabla\cdot\mathbf{D} \equiv \frac{\partial D_x}{\partial x}+\frac{\partial D_y}{\partial y}+\frac{\partial D_z}{\partial z}
> = \lim_{\Delta V\to 0}\frac{\oint\mathbf{D}\cdot d\mathbf{S}}{\Delta V},
> \qquad\boxed{\ \nabla\cdot\mathbf{D} = \rho\ }
> $$
> A **scalar**: net outward flux per unit volume. $\nabla\cdot\mathbf{D}>0$: a *source* (faucet; lines start there); negative: a *sink* (drain); zero: what flows in flows out.

> [!intuition] "Variation along the flow"
> For a unidirectional field $\mathbf{F} = F(x,y,z)\,\hat{u}$, $\hat{u}$ fixed, divergence is nonzero exactly when $F$ changes *along* $\hat{u}$: $+x$ arrows growing with $x$ (more leaving the right face than entering the left). Change only *across* the direction gives zero divergence (the instructor's rule; figure in §4). When lines spread, converge or curve, geometry contributes too: the Coulomb field $Q\hat{r}/r^2$ weakens along its direction yet has *zero* divergence off the charge (the spreading compensates). When in doubt, use the formula.

> [!example] Two quick divergences
> 1. $\mathbf{D} = 5x\,\hat{x} + 12\,\hat{y}$ C/m²: $\nabla\cdot\mathbf{D} = 5 + 0 + 0 = 5$ C/m³ — uniform charge filling all space, a "faucet of strength 5" (the constant $\hat{y}$ part adds nothing).
> 2. The pn-junction field of Lecture 3, $E_x = -\rho_1(x+W_1)/\epsilon_0$ on $(-W_1,0)$ and $\rho_2(x-W_2)/\epsilon_0$ on $(0,W_2)$: $\nabla\cdot\mathbf{E} = \partial E_x/\partial x = -\rho_1/\epsilon_0$ and $+\rho_2/\epsilon_0$ respectively, zero outside: differentiating returns the charge that produced it — Gauss's law checked.

The same argument on $\oint\mathbf{B}\cdot d\mathbf{S} = 0$ gives $\nabla\cdot\mathbf{B} = 0$: no magnetic sources or sinks anywhere.

### The divergence theorem

Tile $V$ with tiny boxes. A shared face counts as "out" of each neighbour with opposite signs and cancels; only the outer boundary survives:

> [!key] Divergence theorem
> $$
> \int_V \nabla\cdot\mathbf{F}\,dV = \oint_{S}\mathbf{F}\cdot d\mathbf{S}\qquad (S = \partial V,\ d\mathbf{S}\ \text{outward})
> $$
> Integral ↔ differential Gauss: $\oint\mathbf{D}\cdot d\mathbf{S} = \int_V\nabla\cdot\mathbf{D}\,dV = \int_V\rho\,dV$ for *every* $V$ forces $\nabla\cdot\mathbf{D} = \rho$ pointwise.

Concept pages: [[concepts/divergence]] · [[concepts/divergence-theorem]].

## 3. Curl: circulation per unit area

The **circulation** around a closed curve $C$ is $\oint_C\mathbf{v}\cdot d\mathbf{l}$. Shrink the loop, divide by its area; the limit depends on orientation, so it is a **vector**, defined component by component:

> [!key] Curl
> $$
> (\nabla\times\mathbf{v})\cdot\hat{n} = \lim_{\Delta S\to 0}\frac{\oint_C \mathbf{v}\cdot d\mathbf{l}}{\Delta S}
> \qquad(\text{$C$ bounds $\Delta S$, right-hand rule between $d\mathbf{l}$ and $\hat{n}$})
> $$
> In Cartesian components,
> $$
> \nabla\times\mathbf{v} =
> \begin{vmatrix}\hat{x}&\hat{y}&\hat{z}\\[2pt] \dfrac{\partial}{\partial x}&\dfrac{\partial}{\partial y}&\dfrac{\partial}{\partial z}\\[6pt] v_x&v_y&v_z\end{vmatrix}
> = \hat{x}\Big(\frac{\partial v_z}{\partial y}-\frac{\partial v_y}{\partial z}\Big)
> + \hat{y}\Big(\frac{\partial v_x}{\partial z}-\frac{\partial v_z}{\partial x}\Big)
> + \hat{z}\Big(\frac{\partial v_y}{\partial x}-\frac{\partial v_x}{\partial y}\Big).
> $$

The $\hat{z}$-component from a small $xy$ rectangle 1–2–3–4: the $v_y$ legs give $[v_y(\text{right}) - v_y(\text{left})]\Delta y \approx \frac{\partial v_y}{\partial x}\Delta x\Delta y$, the $v_x$ legs $-\frac{\partial v_x}{\partial y}\Delta x\Delta y$. Nonzero curl means the line integral from 1 to 3 differs along 1→2→3 and 1→4→3 — *path-dependent*.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 262" width="640" height="262" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px"><defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker><marker id="ahs" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs><line x1="40.0" y1="30.0" x2="40.0" y2="220.0" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><line x1="190.0" y1="30.0" x2="190.0" y2="220.0" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><line x1="52.0" y1="200.0" x2="52.0" y2="167.5" stroke="var(--accent)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.8" stroke-linecap="round"/><line x1="73.0" y1="200.0" x2="73.0" y2="132.2" stroke="var(--accent)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.8" stroke-linecap="round"/><line x1="94.0" y1="200.0" x2="94.0" y2="111.1" stroke="var(--accent)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.8" stroke-linecap="round"/><line x1="115.0" y1="200.0" x2="115.0" y2="104.0" stroke="var(--accent)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.8" stroke-linecap="round"/><line x1="136.0" y1="200.0" x2="136.0" y2="111.1" stroke="var(--accent)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.8" stroke-linecap="round"/><line x1="157.0" y1="200.0" x2="157.0" y2="132.2" stroke="var(--accent)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.8" stroke-linecap="round"/><line x1="178.0" y1="200.0" x2="178.0" y2="167.5" stroke="var(--accent)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.8" stroke-linecap="round"/><circle cx="115.0" cy="120.0" r="16.0" fill="var(--paper)" stroke="currentColor" stroke-width="1.8"/><line x1="99.0" y1="120.0" x2="131.0" y2="120.0" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><line x1="103.7" y1="108.7" x2="126.3" y2="131.3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><line x1="115.0" y1="104.0" x2="115.0" y2="136.0" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><line x1="126.3" y1="108.7" x2="103.7" y2="131.3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><text x="115.0" y="234.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">mid-stream: same speed both sides</text><text x="115.0" y="248.0" text-anchor="middle" fill="currentColor" style="font-size:12px;font-weight:600;">no spin: curl = 0</text><line x1="245.0" y1="30.0" x2="245.0" y2="220.0" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><line x1="395.0" y1="30.0" x2="395.0" y2="220.0" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><line x1="257.0" y1="200.0" x2="257.0" y2="167.5" stroke="var(--accent)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.8" stroke-linecap="round"/><line x1="278.0" y1="200.0" x2="278.0" y2="132.2" stroke="var(--accent)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.8" stroke-linecap="round"/><line x1="299.0" y1="200.0" x2="299.0" y2="111.1" stroke="var(--accent)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.8" stroke-linecap="round"/><line x1="320.0" y1="200.0" x2="320.0" y2="104.0" stroke="var(--accent)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.8" stroke-linecap="round"/><line x1="341.0" y1="200.0" x2="341.0" y2="111.1" stroke="var(--accent)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.8" stroke-linecap="round"/><line x1="362.0" y1="200.0" x2="362.0" y2="132.2" stroke="var(--accent)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.8" stroke-linecap="round"/><line x1="383.0" y1="200.0" x2="383.0" y2="167.5" stroke="var(--accent)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.8" stroke-linecap="round"/><circle cx="285.0" cy="120.0" r="16.0" fill="var(--paper)" stroke="currentColor" stroke-width="1.8"/><line x1="269.0" y1="120.0" x2="301.0" y2="120.0" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><line x1="273.7" y1="108.7" x2="296.3" y2="131.3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><line x1="285.0" y1="104.0" x2="285.0" y2="136.0" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><line x1="296.3" y1="108.7" x2="273.7" y2="131.3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><path d="M259,116 A26,26 0 0 0 311,116" fill="none" stroke="var(--hi)" stroke-width="2.2" marker-end="url(#ah)" stroke-linejoin="round" stroke-linecap="round"/><text x="320.0" y="234.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">near left bank: right side faster</text><text x="320.0" y="248.0" text-anchor="middle" fill="currentColor" style="font-size:12px;font-weight:600;">spins CCW: curl ≠ 0</text><line x1="450.0" y1="30.0" x2="450.0" y2="220.0" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><line x1="600.0" y1="30.0" x2="600.0" y2="220.0" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><line x1="462.0" y1="200.0" x2="462.0" y2="167.5" stroke="var(--accent)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.8" stroke-linecap="round"/><line x1="483.0" y1="200.0" x2="483.0" y2="132.2" stroke="var(--accent)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.8" stroke-linecap="round"/><line x1="504.0" y1="200.0" x2="504.0" y2="111.1" stroke="var(--accent)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.8" stroke-linecap="round"/><line x1="525.0" y1="200.0" x2="525.0" y2="104.0" stroke="var(--accent)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.8" stroke-linecap="round"/><line x1="546.0" y1="200.0" x2="546.0" y2="111.1" stroke="var(--accent)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.8" stroke-linecap="round"/><line x1="567.0" y1="200.0" x2="567.0" y2="132.2" stroke="var(--accent)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.8" stroke-linecap="round"/><line x1="588.0" y1="200.0" x2="588.0" y2="167.5" stroke="var(--accent)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.8" stroke-linecap="round"/><circle cx="560.0" cy="120.0" r="16.0" fill="var(--paper)" stroke="currentColor" stroke-width="1.8"/><line x1="544.0" y1="120.0" x2="576.0" y2="120.0" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><line x1="548.7" y1="108.7" x2="571.3" y2="131.3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><line x1="560.0" y1="104.0" x2="560.0" y2="136.0" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><line x1="571.3" y1="108.7" x2="548.7" y2="131.3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><path d="M534,116 A26,26 0 0 1 586,116" fill="none" stroke="var(--hi)" stroke-width="2.2" marker-end="url(#ah)" stroke-linejoin="round" stroke-linecap="round"/><text x="525.0" y="234.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">near right bank: left side faster</text><text x="525.0" y="248.0" text-anchor="middle" fill="currentColor" style="font-size:12px;font-weight:600;">spins CW: curl ≠ 0</text></svg><figcaption><strong>Curl as a paddlewheel test.</strong> Drop a tiny paddlewheel into the flow. For a straight flow it spins where the speed differs from one side of the wheel to the other — where the field varies <em>across</em> its own direction (curved flow adds a geometric part: see the text). The spin axis (right-hand rule) is the direction of ∇×<b>v</b>; a uniform stream, however fast, has zero curl.</figcaption></figure>

> [!intuition] "Variation across the flow"
> For a unidirectional field, curl is nonzero exactly when it changes *across its own direction*: $+y$ arrows growing with $x$ — a paddlewheel spins because its right side is pushed harder. A uniform stream has no curl; a straight shear flow does, though nothing goes "around". Curved flow adds geometry: rigid rotation ($\mathbf{v}\propto r\hat{\phi}$) has curl though the speed is equal on both sides of a small wheel, while the free vortex $\mathbf{v}\propto\hat{\phi}/r$ — the field around a wire — has *zero* curl except on its axis. Spin axis (right-hand rule) = direction of $\nabla\times\mathbf{v}$.

> [!example] A whirlpool of strength 5
> $\mathbf{v} = -3y\,\hat{x} + 2x\,\hat{y}$. Only the $\hat{z}$-component can be nonzero:
> $\nabla\times\mathbf{v} = \hat{z}\left(\dfrac{\partial(2x)}{\partial x} - \dfrac{\partial(-3y)}{\partial y}\right) = \hat{z}\,(2+3) = 5\hat{z}$.
> Uniform. (Compare $\mathbf{v} = 3x\hat{x}+2y\hat{y}$: a "faucet of strength 5", zero curl.)

> [!trap] Determinant sign errors — even solution keys make them
> The middle term carries a **minus** (top-row expansion), and the $\hat{z}$ term is $\partial_x v_y - \partial_y v_x$, in that order. The backwards bracket turns up even in official keys, unpunished only when the two partials are equal. Expand mechanically, then *check one component with the "across the flow" picture*.

### Stokes' theorem

Tile $S$ with tiny loops: each interior edge is traversed both ways and cancels; only the boundary $C$ survives:

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 220" width="640" height="220" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px"><defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker><marker id="ahs" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs><path d="M40.0,110 C40.0,50.0 90.0,40.0 120.0,55.0 S185.0,70.0 180.0,115.0 S130.0,180.0 90.0,170.0 S40.0,160.0 40.0,110" fill="var(--accent)" fill-opacity="0.10" stroke="currentColor" stroke-width="2"/><path d="M70,148 A45,45 0 1 1 152,140" fill="none" stroke="var(--hi)" stroke-width="2.4" marker-end="url(#ah)" stroke-linejoin="round" stroke-linecap="round"/><text x="110.0" y="118.0" text-anchor="middle" fill="currentColor" style="font-size:16px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">C</text><text x="110.0" y="200.0" text-anchor="middle" fill="currentColor" style="font-size:14px;">∮ v·dl around C</text><text x="230.0" y="115.0" text-anchor="middle" fill="currentColor" style="font-size:26px;">=</text><path d="M260.0,110 C260.0,50.0 310.0,40.0 340.0,55.0 S405.0,70.0 400.0,115.0 S350.0,180.0 310.0,170.0 S260.0,160.0 260.0,110" fill="var(--accent)" fill-opacity="0.10" stroke="currentColor" stroke-width="2"/><path d="M282,84 A8,8 0 1 1 276.7,91.5" fill="none" stroke="var(--hi)" stroke-width="1.4" opacity="0.9" marker-end="url(#ah)" stroke-linejoin="round" stroke-linecap="round"/><path d="M282,110 A8,8 0 1 1 276.7,117.5" fill="none" stroke="var(--hi)" stroke-width="1.4" opacity="0.9" marker-end="url(#ah)" stroke-linejoin="round" stroke-linecap="round"/><path d="M282,136 A8,8 0 1 1 276.7,143.5" fill="none" stroke="var(--hi)" stroke-width="1.4" opacity="0.9" marker-end="url(#ah)" stroke-linejoin="round" stroke-linecap="round"/><path d="M310,58 A8,8 0 1 1 304.7,65.5" fill="none" stroke="var(--hi)" stroke-width="1.4" opacity="0.9" marker-end="url(#ah)" stroke-linejoin="round" stroke-linecap="round"/><path d="M310,84 A8,8 0 1 1 304.7,91.5" fill="none" stroke="var(--hi)" stroke-width="1.4" opacity="0.9" marker-end="url(#ah)" stroke-linejoin="round" stroke-linecap="round"/><path d="M310,110 A8,8 0 1 1 304.7,117.5" fill="none" stroke="var(--hi)" stroke-width="1.4" opacity="0.9" marker-end="url(#ah)" stroke-linejoin="round" stroke-linecap="round"/><path d="M310,136 A8,8 0 1 1 304.7,143.5" fill="none" stroke="var(--hi)" stroke-width="1.4" opacity="0.9" marker-end="url(#ah)" stroke-linejoin="round" stroke-linecap="round"/><path d="M310,162 A8,8 0 1 1 304.7,169.5" fill="none" stroke="var(--hi)" stroke-width="1.4" opacity="0.9" marker-end="url(#ah)" stroke-linejoin="round" stroke-linecap="round"/><path d="M338,58 A8,8 0 1 1 332.7,65.5" fill="none" stroke="var(--hi)" stroke-width="1.4" opacity="0.9" marker-end="url(#ah)" stroke-linejoin="round" stroke-linecap="round"/><path d="M338,84 A8,8 0 1 1 332.7,91.5" fill="none" stroke="var(--hi)" stroke-width="1.4" opacity="0.9" marker-end="url(#ah)" stroke-linejoin="round" stroke-linecap="round"/><path d="M338,110 A8,8 0 1 1 332.7,117.5" fill="none" stroke="var(--hi)" stroke-width="1.4" opacity="0.9" marker-end="url(#ah)" stroke-linejoin="round" stroke-linecap="round"/><path d="M338,136 A8,8 0 1 1 332.7,143.5" fill="none" stroke="var(--hi)" stroke-width="1.4" opacity="0.9" marker-end="url(#ah)" stroke-linejoin="round" stroke-linecap="round"/><path d="M338,162 A8,8 0 1 1 332.7,169.5" fill="none" stroke="var(--hi)" stroke-width="1.4" opacity="0.9" marker-end="url(#ah)" stroke-linejoin="round" stroke-linecap="round"/><path d="M366,58 A8,8 0 1 1 360.7,65.5" fill="none" stroke="var(--hi)" stroke-width="1.4" opacity="0.9" marker-end="url(#ah)" stroke-linejoin="round" stroke-linecap="round"/><path d="M366,84 A8,8 0 1 1 360.7,91.5" fill="none" stroke="var(--hi)" stroke-width="1.4" opacity="0.9" marker-end="url(#ah)" stroke-linejoin="round" stroke-linecap="round"/><path d="M366,110 A8,8 0 1 1 360.7,117.5" fill="none" stroke="var(--hi)" stroke-width="1.4" opacity="0.9" marker-end="url(#ah)" stroke-linejoin="round" stroke-linecap="round"/><path d="M366,136 A8,8 0 1 1 360.7,143.5" fill="none" stroke="var(--hi)" stroke-width="1.4" opacity="0.9" marker-end="url(#ah)" stroke-linejoin="round" stroke-linecap="round"/><path d="M366,162 A8,8 0 1 1 360.7,169.5" fill="none" stroke="var(--hi)" stroke-width="1.4" opacity="0.9" marker-end="url(#ah)" stroke-linejoin="round" stroke-linecap="round"/><path d="M394,84 A8,8 0 1 1 388.7,91.5" fill="none" stroke="var(--hi)" stroke-width="1.4" opacity="0.9" marker-end="url(#ah)" stroke-linejoin="round" stroke-linecap="round"/><path d="M394,110 A8,8 0 1 1 388.7,117.5" fill="none" stroke="var(--hi)" stroke-width="1.4" opacity="0.9" marker-end="url(#ah)" stroke-linejoin="round" stroke-linecap="round"/><path d="M394,136 A8,8 0 1 1 388.7,143.5" fill="none" stroke="var(--hi)" stroke-width="1.4" opacity="0.9" marker-end="url(#ah)" stroke-linejoin="round" stroke-linecap="round"/><text x="330.0" y="200.0" text-anchor="middle" fill="currentColor" style="font-size:14px;">Σ small circulations</text><text x="455.0" y="115.0" text-anchor="middle" fill="currentColor" style="font-size:26px;">=</text><path d="M480.0,110 C480.0,50.0 530.0,40.0 560.0,55.0 S625.0,70.0 620.0,115.0 S570.0,180.0 530.0,170.0 S480.0,160.0 480.0,110" fill="var(--accent)" fill-opacity="0.10" stroke="currentColor" stroke-width="2"/><circle cx="494.0" cy="84.0" r="6.0" fill="none" stroke="var(--hi)" stroke-width="1.4"/><circle cx="494.0" cy="84.0" r="1.8" fill="var(--hi)" stroke="none" stroke-width="1.5"/><circle cx="494.0" cy="110.0" r="6.0" fill="none" stroke="var(--hi)" stroke-width="1.4"/><circle cx="494.0" cy="110.0" r="1.8" fill="var(--hi)" stroke="none" stroke-width="1.5"/><circle cx="494.0" cy="136.0" r="6.0" fill="none" stroke="var(--hi)" stroke-width="1.4"/><circle cx="494.0" cy="136.0" r="1.8" fill="var(--hi)" stroke="none" stroke-width="1.5"/><circle cx="522.0" cy="58.0" r="6.0" fill="none" stroke="var(--hi)" stroke-width="1.4"/><circle cx="522.0" cy="58.0" r="1.8" fill="var(--hi)" stroke="none" stroke-width="1.5"/><circle cx="522.0" cy="84.0" r="6.0" fill="none" stroke="var(--hi)" stroke-width="1.4"/><circle cx="522.0" cy="84.0" r="1.8" fill="var(--hi)" stroke="none" stroke-width="1.5"/><circle cx="522.0" cy="110.0" r="6.0" fill="none" stroke="var(--hi)" stroke-width="1.4"/><circle cx="522.0" cy="110.0" r="1.8" fill="var(--hi)" stroke="none" stroke-width="1.5"/><circle cx="522.0" cy="136.0" r="6.0" fill="none" stroke="var(--hi)" stroke-width="1.4"/><circle cx="522.0" cy="136.0" r="1.8" fill="var(--hi)" stroke="none" stroke-width="1.5"/><circle cx="522.0" cy="162.0" r="6.0" fill="none" stroke="var(--hi)" stroke-width="1.4"/><circle cx="522.0" cy="162.0" r="1.8" fill="var(--hi)" stroke="none" stroke-width="1.5"/><circle cx="550.0" cy="58.0" r="6.0" fill="none" stroke="var(--hi)" stroke-width="1.4"/><circle cx="550.0" cy="58.0" r="1.8" fill="var(--hi)" stroke="none" stroke-width="1.5"/><circle cx="550.0" cy="84.0" r="6.0" fill="none" stroke="var(--hi)" stroke-width="1.4"/><circle cx="550.0" cy="84.0" r="1.8" fill="var(--hi)" stroke="none" stroke-width="1.5"/><circle cx="550.0" cy="110.0" r="6.0" fill="none" stroke="var(--hi)" stroke-width="1.4"/><circle cx="550.0" cy="110.0" r="1.8" fill="var(--hi)" stroke="none" stroke-width="1.5"/><circle cx="550.0" cy="136.0" r="6.0" fill="none" stroke="var(--hi)" stroke-width="1.4"/><circle cx="550.0" cy="136.0" r="1.8" fill="var(--hi)" stroke="none" stroke-width="1.5"/><circle cx="550.0" cy="162.0" r="6.0" fill="none" stroke="var(--hi)" stroke-width="1.4"/><circle cx="550.0" cy="162.0" r="1.8" fill="var(--hi)" stroke="none" stroke-width="1.5"/><circle cx="578.0" cy="58.0" r="6.0" fill="none" stroke="var(--hi)" stroke-width="1.4"/><circle cx="578.0" cy="58.0" r="1.8" fill="var(--hi)" stroke="none" stroke-width="1.5"/><circle cx="578.0" cy="84.0" r="6.0" fill="none" stroke="var(--hi)" stroke-width="1.4"/><circle cx="578.0" cy="84.0" r="1.8" fill="var(--hi)" stroke="none" stroke-width="1.5"/><circle cx="578.0" cy="110.0" r="6.0" fill="none" stroke="var(--hi)" stroke-width="1.4"/><circle cx="578.0" cy="110.0" r="1.8" fill="var(--hi)" stroke="none" stroke-width="1.5"/><circle cx="578.0" cy="136.0" r="6.0" fill="none" stroke="var(--hi)" stroke-width="1.4"/><circle cx="578.0" cy="136.0" r="1.8" fill="var(--hi)" stroke="none" stroke-width="1.5"/><circle cx="578.0" cy="162.0" r="6.0" fill="none" stroke="var(--hi)" stroke-width="1.4"/><circle cx="578.0" cy="162.0" r="1.8" fill="var(--hi)" stroke="none" stroke-width="1.5"/><circle cx="606.0" cy="84.0" r="6.0" fill="none" stroke="var(--hi)" stroke-width="1.4"/><circle cx="606.0" cy="84.0" r="1.8" fill="var(--hi)" stroke="none" stroke-width="1.5"/><circle cx="606.0" cy="110.0" r="6.0" fill="none" stroke="var(--hi)" stroke-width="1.4"/><circle cx="606.0" cy="110.0" r="1.8" fill="var(--hi)" stroke="none" stroke-width="1.5"/><circle cx="606.0" cy="136.0" r="6.0" fill="none" stroke="var(--hi)" stroke-width="1.4"/><circle cx="606.0" cy="136.0" r="1.8" fill="var(--hi)" stroke="none" stroke-width="1.5"/><text x="550.0" y="200.0" text-anchor="middle" fill="currentColor" style="font-size:14px;">∬ (∇×v)·dS over S</text></svg><figcaption><strong>Stokes' theorem by tiling.</strong> Cut the surface into small cells. Adjacent cells share an edge traversed in opposite directions, so all interior contributions cancel and only the outer boundary survives. Each cell's circulation is (∇×<b>v</b>)·d<b>S</b>: curl is <em>circulation per unit area</em>. The divergence theorem is the same idea with flux through small volumes.</figcaption></figure>

> [!key] Stokes' theorem
> $$
> \oint_C \mathbf{F}\cdot d\mathbf{l} = \int_S (\nabla\times\mathbf{F})\cdot d\mathbf{S}\qquad (C = \partial S,\ \text{right-hand rule})
> $$
> Circulation around the boundary = total curl through the surface, for any surface bounded by $C$.

Concept pages: [[concepts/curl]] · [[concepts/stokes-theorem]].

## 4. The two pictures, side by side

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 300" width="640" height="300" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px"><defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker><marker id="ahs" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs><rect x="40" y="40" width="280" height="110" rx="6" fill="var(--muted)" fill-opacity="0.12" stroke="currentColor" stroke-width="1.2"/><text x="180.0" y="32.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600;">E = Eₓ(x) x̂ — arrows along x, growing along x</text><line x1="66.0" y1="75.0" x2="74.0" y2="75.0" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#ahs)" stroke-linecap="round"/><line x1="66.0" y1="115.0" x2="74.0" y2="115.0" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#ahs)" stroke-linecap="round"/><line x1="107.5" y1="75.0" x2="120.5" y2="75.0" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#ahs)" stroke-linecap="round"/><line x1="107.5" y1="115.0" x2="120.5" y2="115.0" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#ahs)" stroke-linecap="round"/><line x1="149.0" y1="75.0" x2="167.0" y2="75.0" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#ahs)" stroke-linecap="round"/><line x1="149.0" y1="115.0" x2="167.0" y2="115.0" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#ahs)" stroke-linecap="round"/><line x1="190.5" y1="75.0" x2="213.5" y2="75.0" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#ahs)" stroke-linecap="round"/><line x1="190.5" y1="115.0" x2="213.5" y2="115.0" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#ahs)" stroke-linecap="round"/><line x1="232.0" y1="75.0" x2="260.0" y2="75.0" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#ahs)" stroke-linecap="round"/><line x1="232.0" y1="115.0" x2="260.0" y2="115.0" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#ahs)" stroke-linecap="round"/><line x1="273.5" y1="75.0" x2="306.5" y2="75.0" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#ahs)" stroke-linecap="round"/><line x1="273.5" y1="115.0" x2="306.5" y2="115.0" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#ahs)" stroke-linecap="round"/><circle cx="180.0" cy="95.0" r="3.0" fill="currentColor" stroke="currentColor" stroke-width="1.5"/><rect x="40" y="185" width="280" height="110" rx="6" fill="var(--muted)" fill-opacity="0.12" stroke="currentColor" stroke-width="1.2"/><text x="180.0" y="177.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600;">E = Eᵧ(x) ŷ — arrows along y, growing along x</text><line x1="70.0" y1="224.0" x2="70.0" y2="216.0" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#ahs)" stroke-linecap="round"/><line x1="70.0" y1="264.0" x2="70.0" y2="256.0" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#ahs)" stroke-linecap="round"/><line x1="114.0" y1="226.5" x2="114.0" y2="213.5" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#ahs)" stroke-linecap="round"/><line x1="114.0" y1="266.5" x2="114.0" y2="253.5" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#ahs)" stroke-linecap="round"/><line x1="158.0" y1="229.0" x2="158.0" y2="211.0" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#ahs)" stroke-linecap="round"/><line x1="158.0" y1="269.0" x2="158.0" y2="251.0" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#ahs)" stroke-linecap="round"/><line x1="202.0" y1="231.5" x2="202.0" y2="208.5" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#ahs)" stroke-linecap="round"/><line x1="202.0" y1="271.5" x2="202.0" y2="248.5" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#ahs)" stroke-linecap="round"/><line x1="246.0" y1="234.0" x2="246.0" y2="206.0" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#ahs)" stroke-linecap="round"/><line x1="246.0" y1="274.0" x2="246.0" y2="246.0" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#ahs)" stroke-linecap="round"/><line x1="290.0" y1="236.5" x2="290.0" y2="203.5" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#ahs)" stroke-linecap="round"/><line x1="290.0" y1="276.5" x2="290.0" y2="243.5" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#ahs)" stroke-linecap="round"/><circle cx="180.0" cy="240.0" r="3.0" fill="currentColor" stroke="currentColor" stroke-width="1.5"/><text x="340.0" y="70.0" text-anchor="start" fill="currentColor" style="font-size:13px;">variation ALONG the flow</text><text x="340.0" y="92.0" text-anchor="start" fill="currentColor" style="font-size:14px;font-weight:600;">→ ∇·E ≠ 0  (a source)</text><text x="340.0" y="118.0" text-anchor="start" fill="currentColor" style="font-size:13px;">no variation ACROSS the flow</text><text x="340.0" y="140.0" text-anchor="start" fill="currentColor" style="font-size:14px;font-weight:600;">→ ∇×E = 0</text><text x="340.0" y="215.0" text-anchor="start" fill="currentColor" style="font-size:13px;">no variation ALONG the flow</text><text x="340.0" y="237.0" text-anchor="start" fill="currentColor" style="font-size:14px;font-weight:600;">→ ∇·E = 0</text><text x="340.0" y="263.0" text-anchor="start" fill="currentColor" style="font-size:13px;">variation ACROSS the flow</text><text x="340.0" y="285.0" text-anchor="start" fill="currentColor" style="font-size:14px;font-weight:600;">→ ∇×E ≠ 0  (a paddlewheel spins)</text></svg><figcaption><strong>The instructor's rule of thumb.</strong> Divergence measures how a field changes <em>along</em> its own direction (a scalar: net outflow); curl measures how it changes <em>across</em> its direction (a vector: net circulation). The same two pictures answer both questions — with opposite answers.</figcaption></figure>

The same two fields give opposite answers to the two questions. Practise calling an arrow plot "source-like" or "whirlpool-like" without computing.

## 5. Conservative fields

Four equivalent statements (on all of space or any region without holes):

1. $\nabla\times\mathbf{v} = 0$ everywhere — **curl-free**;
2. $\oint_C\mathbf{v}\cdot d\mathbf{l} = 0$ around every closed loop (by Stokes);
3. $\int_a^b\mathbf{v}\cdot d\mathbf{l}$ is **path-independent**;
4. $\mathbf{v} = -\nabla f$ for some scalar function $f$ — the field is a gradient (a **potential** exists).

The minus sign in (4) makes $f$ the familiar voltage for $\mathbf{E}$; Lecture 5 exploits (4). Concept page: [[concepts/conservative-field]].

## 6. Static electric fields are curl-free

The point-charge field $\mathbf{E} = \dfrac{Q}{4\pi\epsilon_0}\dfrac{\mathbf{r}}{r^3}$ has components $x\,g(r)$, $y\,g(r)$, $z\,g(r)$ with $g = (4\pi\epsilon_0)^{-1}Q\,r^{-3}$:

$$
(\nabla\times\mathbf{E})_z = \frac{\partial}{\partial x}\big(y\,g(r)\big) - \frac{\partial}{\partial y}\big(x\,g(r)\big)
= y\,g'(r)\frac{x}{r} - x\,g'(r)\frac{y}{r} = 0 ,
$$

likewise for the other components: **every radial field $g(r)\,\mathbf{r}$ is curl-free.** Curl is linear and every static field superposes Coulomb fields, so **all electrostatic fields are curl-free, without exception**. (The notes check the infinite-line field $\dfrac{\rho_l}{2\pi\epsilon_0}\dfrac{x\hat{x}+y\hat{y}}{x^2+y^2}$ the same way: $\partial_x\!\left(\dfrac{y}{x^2+y^2}\right) - \partial_y\!\left(\dfrac{x}{x^2+y^2}\right) = \dfrac{-2xy+2xy}{(x^2+y^2)^2} = 0$.)

> [!key] The laws of electrostatics
> $$
> \nabla\cdot\mathbf{D} = \rho,\qquad \nabla\times\mathbf{E} = 0,\qquad \mathbf{D} = \epsilon_0\mathbf{E}\ (\text{vacuum}).
> $$
> **Helmholtz theorem**: a field vanishing at infinity is fixed by its divergence and curl, so these two equations *are* electrostatics: $\rho$ fixes the field. Lecture 5 writes $\mathbf{E} = -\nabla V$; Lecture 7 combines both into Poisson's equation $\nabla^2 V = -\rho/\epsilon_0$.

## 7. The differential form of Maxwell's equations

Each integral law becomes local by the matching theorem plus "true for every surface/volume ⇒ true pointwise":

| integral form | theorem | differential form |
|---|---|---|
| $\oint_C\mathbf{E}\cdot d\mathbf{l} = -\dfrac{\partial}{\partial t}\displaystyle\int_S\mathbf{B}\cdot d\mathbf{S}$ (Faraday) | Stokes | $\nabla\times\mathbf{E} = -\dfrac{\partial\mathbf{B}}{\partial t}$ |
| $\oint_C\mathbf{H}\cdot d\mathbf{l} = \displaystyle\int_S\Big(\mathbf{J}+\dfrac{\partial\mathbf{D}}{\partial t}\Big)\cdot d\mathbf{S}$ (Ampère–Maxwell) | Stokes | $\nabla\times\mathbf{H} = \mathbf{J}+\dfrac{\partial\mathbf{D}}{\partial t}$ |
| $\oint_S\mathbf{D}\cdot d\mathbf{S} = \displaystyle\int_V\rho\,dV$ (Gauss) | divergence | $\nabla\cdot\mathbf{D} = \rho$ |
| $\oint_S\mathbf{B}\cdot d\mathbf{S} = 0$ | divergence | $\nabla\cdot\mathbf{B} = 0$ |

$\oint_C\mathbf{E}\cdot d\mathbf{l}$ is an **EMF** (volts), $\oint_C\mathbf{H}\cdot d\mathbf{l}$ an **MMF** (amperes). Ampère's right side: the static **conduction current** $\mathbf{J}$ plus the dynamic **displacement current** $\partial\mathbf{D}/\partial t$ — Maxwell's addition, and the reason light exists ([[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Lecture 16]] onward).

> [!trap] Partial, not total, time derivatives
> Fields depend on $(x,y,z,t)$: use $\partial/\partial t$. Read a slide's $d/dt$ as $\partial/\partial t$.

### A free consequence: charge is conserved

Take the divergence of the Ampère–Maxwell equation. Since $\nabla\cdot(\nabla\times\mathbf{H}) = 0$ identically,

$$
0 = \nabla\cdot\mathbf{J} + \frac{\partial}{\partial t}\nabla\cdot\mathbf{D} = \nabla\cdot\mathbf{J} + \frac{\partial\rho}{\partial t}
\quad\Longrightarrow\quad
\boxed{\ \nabla\cdot\mathbf{J} = -\frac{\partial\rho}{\partial t}\ }
$$

the **continuity equation**: current flowing out of a point drains its charge — conservation is built into Maxwell's equations. Identities for any smooth fields:

$$
\nabla\cdot(\nabla\times\mathbf{A}) = 0,\qquad
\nabla\times(\nabla f) = 0,\qquad
\nabla\times\nabla\times\mathbf{A} = \nabla(\nabla\cdot\mathbf{A}) - \nabla^2\mathbf{A},\qquad \nabla^2\mathbf{A}\equiv\hat{x}\nabla^2A_x+\hat{y}\nabla^2A_y+\hat{z}\nabla^2A_z .
$$

(The identity holds in any coordinates; the component-wise Laplacian on the right is valid for *Cartesian* components only.)

Concept page: [[concepts/maxwells-equations]].

## 8. Summary

- Divergence = flux per unit volume (scalar, "along the flow"); $\nabla\cdot\mathbf{D} = \rho$, $\nabla\cdot\mathbf{B} = 0$.
- Curl = circulation per unit area (vector, "across the flow"); Faraday and Ampère are curl equations.
- Divergence and Stokes' theorems: local ↔ integral, by "interior contributions cancel".
- Static $\mathbf{E}$ is curl-free ⇒ conservative ⇒ a potential exists (Lecture 5).
- Continuity, $\nabla\cdot\mathbf{J} = -\partial\rho/\partial t$, is contained in Maxwell's equations.

> [!exam] On Exam 1
> FA26 problem 1 is this lecture plus Lecture 5: $\nabla\times\mathbf{E}$ of a polynomial field (zero), the potential, $\rho = \epsilon_0\nabla\cdot\mathbf{E}$, and a line integral by path independence. Worked with other numbers in [[problems/curl-potential-and-charge-from-a-field]]. Tested every time: the determinant expanded correctly, and that "curl-free" says nothing about whether $\rho$ is zero.

> [!tip] Practice this lecture
> [[practice/04-divergence-and-curl|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/04-divergence-and-curl#41-faucet-or-whirlpool|4.1 Faucet or whirlpool]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 4 (Gauss on a small cube → divergence; Examples 1–4; Helmholtz; curl-free Coulomb and line fields). Shao, Lecture 4 slides (FTC → gradient theorem → Stokes ladder; whirlpool/faucet; paddlewheel; true/false panels; pn junction; continuity from Ampère). Slips in the course material: see [[0-toolkit/04-errata-in-the-course-materials|errata]].
