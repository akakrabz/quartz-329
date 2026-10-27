---
title: "Lecture 10 — Capacitance and conductance"
description: "Q = CV for two conductors with equal and opposite charge; C is computed by a chain of steps from V to Q or Q to V, for parallel plates, coax and concentric spheres. A lossy filling adds a conductance G = (σ/ε)C in parallel, energy is stored at ½εE² per unit volume, and a pn junction is a capacitor whose C depends on V."
tags: [lecture, electrostatics, exam-1]
lecture: 10
---

*Lecture 10 · course notes §10 · slides "Capacitance and Conductance" · prev: [[1-electrostatics/09-static-fields-in-dielectric-media|Lecture 9]] · next: [[1-electrostatics/11-lorentz-drude-models-for-conductivity-and-susceptibility|Lecture 11]] (not on Exam 1) · practice: [[practice/10-capacitance-and-conductance|12 problems]]*

> [!abstract] In one breath
> $\pm Q$ on two conductors produces a potential difference $V$; electrostatics is linear, so $C = Q/V$ is a constant of the *geometry and the dielectric* — the **capacitance**, in farads. You compute it by running the chain of the last five lectures either way: $V$ through Laplace's equation to the charge, or $Q$ through Gauss's law to the voltage. A slightly conducting filling also carries a leakage current $I = GV$, $G = (\sigma/\epsilon)C$; the stored energy is $\tfrac12CV^2$, spread through the field at $\tfrac12\epsilon E^2$ per cubic metre; a diode's depletion layer is a capacitor whose $C$ shrinks as the voltage grows.

## 1. Definition, and the two recipes

> [!key] Capacitance
> For two conductors carrying $+Q$ and $-Q$, with potential difference $V = V_+ - V_-> 0$ between them,
> $$
> Q = CV,\qquad C = \frac{Q}{V}\quad[\text{F} = \text{C/V}].
> $$
> $C$ depends only on the shapes, the separation and the filling's $\epsilon$ — not on $Q$ or $V$ (linear media). $V$ is the **drop** from the positive conductor to the negative one, so $C>0$ always.

<!-- fig:capacitance-recipes -->

> [!recipe] Two routes to C
> **Given $V$** (the conductors' potentials): solve Laplace's equation with those boundary values → $\mathbf{E} = -\nabla V$ → $\mathbf{D} = \epsilon\mathbf{E}$ → $\rho_s = \hat{n}\cdot\mathbf{D}$ on **one** conductor ($\hat{n}$ out of the conductor) → $Q = \int\rho_s\,dA$ → $C = Q/V$.
>
> **Given $Q$**: Gauss's law (or sheet superposition) → $\mathbf{D}$ → $\mathbf{E} = \mathbf{D}/\epsilon$ → $V = -\int_-^+\mathbf{E}\cdot d\mathbf{l}$ from the negative conductor to the positive one (a positive number) → $C = Q/V$.
>
> Both pass through the same field pattern and give the same $C$. On an exam the given-$Q$ route is usually shorter.

**No fringing:** the infinite-plate (or infinite-coax) field pattern needs $d\ll\sqrt{A}$; otherwise field lines bulge at the edges and $C$ is somewhat larger. **Quasi-static:** $Q=CV$ holds for a time-varying capacitor only if $\sqrt{A}\ll c/f$; a large structure driven fast is a transmission line, not a lumped element ([[4-transmission-lines/index|Unit 4]]).

## 2. Parallel plates, both ways

Plates of area $A$ at $x=0$ (grounded) and $x=d$ (at $V_0$); dielectric $\epsilon$ between.

**Given $V$.** $V(x) = V_0x/d$ (Laplace), so $\mathbf{E} = -\dfrac{V_0}{d}\hat{x}$ and $\mathbf{D} = -\dfrac{\epsilon V_0}{d}\hat{x}$. At the positive plate ($x=d$) the normal into the gap is $-\hat{x}$: $\rho_s = (-\hat{x})\cdot\mathbf{D} = +\dfrac{\epsilon V_0}{d}$ [C/m²], so $Q = \rho_sA = \dfrac{\epsilon AV_0}{d}$ and

> [!key] Parallel-plate capacitor
> $$
> C = \frac{\epsilon A}{d}\qquad(d\ll\sqrt{A}).
> $$

**Given $Q$.** The plates carry $\pm Q/A$ on their facing surfaces only (the field vanishes inside each conductor and outside the pair). Between them $\mathbf{D} = -\dfrac{Q}{A}\hat{x}$ (from $+$ to $-$), $\mathbf{E} = -\dfrac{Q}{\epsilon A}\hat{x}$, and the drop is $V = V(d) - V(0) = -\int_0^dE_x\,dx = \dfrac{Qd}{\epsilon A}$. Again $C = \epsilon A/d$.

> [!trap] Signs in the given-$Q$ route
> A slide writes $V = \int_0^d\mathbf{E}\cdot d\mathbf{l}$; with $\mathbf{E} = -(Q/\epsilon A)\hat{x}$ that is *negative*. Correct: $V(d)-V(0) = -\int_0^d\mathbf{E}\cdot d\mathbf{l}$, or "the drop from the positive plate to the negative plate is $\int_+^-\mathbf{E}\cdot d\mathbf{l} = Ed$". Integrate from the positive conductor to the other. The same slip gives negative coax capacitances (FA26 4(e) key, intermediate line; [[0-toolkit/04-errata-in-the-course-materials|errata page]]).

## 3. The coaxial cable

Inner conductor radius $a$, outer conductor inner radius $b$, dielectric $\epsilon$ between, length $L\gg b$, so $\mathbf{E} = E_r(r)\hat{r}$.

<!-- fig:coax-capacitor -->

**Given $V$** ($V(a) = V_0$, $V(b) = 0$). Laplace in cylindrical coordinates: $\dfrac1r\dfrac{d}{dr}\Big(r\dfrac{dV}{dr}\Big) = 0 \Rightarrow r\dfrac{dV}{dr} = A \Rightarrow V = A\ln r + B$. The boundary values give

$$
V(r) = V_0\,\frac{\ln(b/r)}{\ln(b/a)},\qquad
\mathbf{E} = -\frac{dV}{dr}\hat{r} = \frac{V_0}{\ln(b/a)}\,\frac{1}{r}\,\hat{r},\qquad
\mathbf{D} = \frac{\epsilon V_0}{\ln(b/a)}\,\frac{1}{r}\,\hat{r}.
$$

On the inner conductor ($\hat{n} = \hat{r}$): $\rho_s(a) = \dfrac{\epsilon V_0}{a\ln(b/a)}$, so $Q = \rho_s\cdot2\pi aL = \dfrac{2\pi\epsilon LV_0}{\ln(b/a)}$. (Outer: $\rho_s(b) = -\hat{r}\cdot\mathbf{D}(b) = -\dfrac{\epsilon V_0}{b\ln(b/a)}$, times $2\pi bL$ gives $-Q$ ✓.)

**Given $Q$** (or $\lambda = Q/L$ — the exam's symbol for what this site otherwise calls $\rho_l$). Gauss on a cylinder $a<r<b$: $D_r\,2\pi rL = Q$, so $\mathbf{D} = \dfrac{\lambda}{2\pi r}\hat{r}$, $\mathbf{E} = \dfrac{\lambda}{2\pi\epsilon r}\hat{r}$, and the drop from inner to outer is $V = \displaystyle\int_a^b\frac{\lambda\,dr}{2\pi\epsilon r} = \frac{\lambda}{2\pi\epsilon}\ln\frac ba$.

> [!key] Coaxial capacitor
> $$
> C = \frac{2\pi\epsilon L}{\ln(b/a)},\qquad \mathcal{C} \equiv \frac{C}{L} = \frac{2\pi\epsilon}{\ln(b/a)}\quad[\text{F/m}].
> $$
> The **per-unit-length** capacitance $\mathcal{C}$ (script C) is the one transmission-line theory uses. It depends on the radii only through their ratio.

> [!example] Example — two concept checks that train the chain
> A coax filled with $\epsilon = 3\epsilon_0$ has its dielectric replaced by air.
> - *Same charge:* $Q$ same → $\rho_s$ same → $\mathbf{D}$ same → $\mathbf{E} = \mathbf{D}/\epsilon$ **triples** → $V = \int E\,dr$ **triples** → $C$ drops by 3. "The voltage is reduced by 3×" is **false**.
> - *Same voltage:* $V$ same → $\mathbf{E} = -\nabla V$ **same** → $\mathbf{D} = \epsilon\mathbf{E}$ drops by 3 → $\rho_s$ and $Q$ drop by 3 → $C$ drops by 3. "The E-field is reduced by 3×" is **false**.
>
> $C$ falls by $\epsilon_r$ either way (a property of the structure); *which* of $Q$ and $V$ moves depends on what is held fixed.

## 4. Layered dielectrics: series and parallel

> [!key] Concentric spheres, and combinations
> For conducting spheres of radii $a<b$ with $\epsilon$ between: Gauss gives $E_r = Q/(4\pi\epsilon r^2)$, the drop is $V = \dfrac{Q}{4\pi\epsilon}\Big(\dfrac1a - \dfrac1b\Big)$, and
> $$
> C = 4\pi\epsilon\,\frac{ab}{b-a}\ \xrightarrow{\ b\to\infty\ }\ 4\pi\epsilon a\quad(\text{an isolated sphere}).
> $$
> Layers crossed **in succession** (normal to $\mathbf{E}$): $\mathbf{D}$ common, drops add, $\dfrac1C = \sum_i\dfrac1{C_i}$ — **series**. Layers **side by side** (interfaces parallel to $\mathbf{E}$): $\mathbf{E}$ common, charges add, $C = \sum_iC_i$ — **parallel**.

Plates with layers $d_1$ ($\epsilon_1$) and $d_2$ ($\epsilon_2$): $\dfrac1C = \dfrac{d_1}{\epsilon_1A} + \dfrac{d_2}{\epsilon_2A}$. Check against the two-layer example of [[1-electrostatics/09-static-fields-in-dielectric-media#3-laplaces-equation-layer-by-layer|Lecture 9]]: $C/A = \big(1/\epsilon_0 + 1/(2\epsilon_0)\big)^{-1} = \tfrac23\epsilon_0$ F/m², and with $2\epsilon_0$ C/m² on the plates, $V = (2\epsilon_0)/(\tfrac23\epsilon_0) = 3$ V ✓. Coax with $\epsilon_1$ on $a<r<c$ and $\epsilon_2$ on $c<r<b$: $\dfrac{1}{\mathcal{C}} = \dfrac{\ln(c/a)}{2\pi\epsilon_1} + \dfrac{\ln(b/c)}{2\pi\epsilon_2}$ — Exam 1 problem 4(e), worked in [[problems/two-layer-coaxial-capacitor]]. Two dielectrics each filling *half the angle* of the annulus share $\mathbf{E}$ and add in parallel: $\mathcal{C} = \pi(\epsilon_1+\epsilon_2)/\ln(b/a)$.

## 5. Energy stored in a capacitor and in the field

At charge $q$ the voltage is $q/C$, and moving the next $dq$ across costs $dW = (q/C)\,dq$:

> [!key] Stored energy
> $$
> W = \int_0^Q\frac{q}{C}\,dq = \frac{Q^2}{2C} = \tfrac12CV^2 = \tfrac12QV\quad[\text{J}].
> $$
> For the parallel plate, $C = \epsilon A/d$ and $V = Ed$ give $W = \tfrac12\epsilon E^2\,(Ad)$: gap volume times
> $$
> w = \tfrac12\epsilon E^2 = \tfrac12\mathbf{D}\cdot\mathbf{E}\quad[\text{J/m}^3],
> $$
> taken in general as the **energy density of the electrostatic field**: energy lives wherever the field is. (J/m³, not the W/m³ a slide writes — that is a power density.)

From power: $P = VI = V\,C\,dV/dt = \dfrac{d}{dt}\big(\tfrac12CV^2\big)$. A battery at fixed $V$ delivers $QV = CV^2$ while charging the capacitor to $Q$; only half is stored — the other half is dissipated in the charging resistance, however small. For a coax, $W' = \tfrac12\mathcal{C}V^2$ per metre.

## 6. Conductance: the leaky capacitor

<!-- fig:lossy-capacitor-rc -->

Give the filling a small conductivity $\sigma$ too. The same $\mathbf{E}$ drives $\mathbf{J} = \sigma\mathbf{E}$ from the positive conductor to the negative one. For plates, $J = \sigma V/d$ and $I = JA = \dfrac{\sigma A}{d}V$:

> [!key] Conductance, and its relation to capacitance
> $$
> I = GV,\qquad G = \frac{\sigma A}{d}\ (\text{plates}),\qquad R = \frac1G = \frac{d}{\sigma A},\qquad\boxed{\ G = \frac{\sigma}{\epsilon}\,C\ }.
> $$
> $G$ [S] and $C$ [F] share one **geometric factor** ($A/d$ for plates, $2\pi L/\ln(b/a)$ for a coax, $4\pi ab/(b-a)$ for spheres): $C = \epsilon\times$(factor), $G = \sigma\times$(factor). So $G = (\sigma/\epsilon)C$ for *any* geometry filled with one homogeneous medium — not for layered fillings unless every layer has the same $\sigma/\epsilon$.

> [!recipe] Conductance directly
> $V\to\mathbf{E} = -\nabla V\to\mathbf{J} = \sigma\mathbf{E}\to I = \int\mathbf{J}\cdot d\mathbf{S}$ through any surface separating the conductors $\to G = I/V$ (and $\mathcal{G} = G/L$ per unit length).
>
> *Coax:* $\mathbf{J} = \dfrac{\sigma V_0}{\ln(b/a)}\dfrac1r\hat{r}$; through a cylinder of radius $r$, $I = J_r\cdot2\pi rL = \dfrac{2\pi\sigma LV_0}{\ln(b/a)}$, the same for every $r$ ($\nabla\cdot\mathbf{J} = 0$, steady current). So $G = \dfrac{2\pi\sigma L}{\ln(b/a)}$, $\mathcal{G} = \dfrac{2\pi\sigma}{\ln(b/a)}$ [S/m]. *Spheres:* shells in series, $dR = \dfrac{dr}{4\pi\sigma r^2}$, so $R = \dfrac{1}{4\pi\sigma}\Big(\dfrac1a - \dfrac1b\Big)$ and $G = 4\pi\sigma\dfrac{ab}{b-a} = \dfrac{\sigma}{\epsilon}C$ ✓.

**The circuit model.** Charge on the positive conductor grows with the external current and shrinks with the leakage: $\dfrac{dQ}{dt} = C\dfrac{dV}{dt} = I - GV$, i.e.

$$
I = C\frac{dV}{dt} + GV:
$$

a capacitance $C$ in **parallel** with $R = 1/G$. With no external circuit ($I=0$), $C\,dV/dt = -GV$, so

> [!key] Self-discharge and the relaxation time
> $$
> Q(t) = Q(0)\,e^{-t/\tau},\qquad \tau = RC = \frac{C}{G} = \frac{\epsilon}{\sigma},
> $$
> the relaxation time that empties a conductor's interior ([[1-electrostatics/08-conductors-dielectrics-and-polarization|Lecture 8]]), likewise independent of geometry. Driven sinusoidally, the element is resistor-like for $\omega\ll\sigma/\epsilon$ and capacitor-like for $\omega\gg\sigma/\epsilon$: a good insulator has $\sigma/\epsilon$ far below every frequency you care about.

> [!example] Example — concentric spheres in a lossy medium (HW4 #4)
> Shells of radii $a = 1$ m and $b\to\infty$, medium $\epsilon = 2\epsilon_0$, $\sigma = 2\times10^{-6}$ S/m. $C = 4\pi\epsilon a = 8\pi\epsilon_0 \approx 222$ pF; $G = (\sigma/\epsilon)C = 8\pi\times10^{-6}\ \text{S} \approx 25\ \mu$S (shell-by-shell $\int dR$ agrees); $\tau = \epsilon/\sigma = 8.85\ \mu$s. With $Q(0) = 1$ C on the inner sphere and nothing connected, $Q(t) = e^{-t/(8.85\,\mu\text{s})}$ C: the charge flows outward through the medium, which *is* the return path.

## 7. A nonlinear capacitor: the diode junction

The pn junction of [[1-electrostatics/07-poisson-and-laplace#3-poissons-equation-where-there-is-charge|Lecture 7]] stores $\pm Q = \pm\rho_2W_2A$ in its depletion layers, with $V = V_{21} = \dfrac{\rho_2W_2(W_1+W_2)}{2\epsilon_0}$ across them. Eliminating the widths with $\rho_1W_1 = \rho_2W_2$ gives $W_1 + W_2 = \sqrt{\dfrac{2\epsilon_0V(\rho_1+\rho_2)}{\rho_1\rho_2}}$ — the depletion region *widens* with $V$ — and

$$
Q = A\sqrt{\frac{2\epsilon_0\rho_1\rho_2}{\rho_1+\rho_2}}\;\sqrt{V}:
$$

$Q\propto\sqrt V$, not linear. Circuit theory uses the **small-signal capacitance**, the slope of the $Q$–$V$ curve:

$$
C \equiv \frac{dQ}{dV} = A\sqrt{\frac{\epsilon_0\,\rho_1\rho_2}{2V(\rho_1+\rho_2)}} = \frac{\epsilon_0A}{W_1+W_2}\ \propto\ V^{-1/2}.
$$

The last form is the parallel-plate formula with the depletion width as the gap — why varactor diodes work as voltage-controlled capacitors. (The secant $Q/V$ would give exactly twice this; for a linear capacitor the two coincide. In silicon, replace $\epsilon_0$ by $\epsilon\approx11.7\epsilon_0$.)

## 8. Summary

- $C = Q/V$, $V$ the drop from $+$ to $-$; by a chain: $V\to E\to D\to\rho_s\to Q$ or $Q\to D\to E\to V$.
- Plates $\epsilon A/d$; coax $2\pi\epsilon L/\ln(b/a)$, $\mathcal{C} = 2\pi\epsilon/\ln(b/a)$; spheres $4\pi\epsilon ab/(b-a)$.
- Layers in succession: series ($D$ common); side by side: parallel ($E$ common).
- $W = \tfrac12CV^2$; $w = \tfrac12\epsilon E^2$ [J/m³].
- Lossy filling: $G = (\sigma/\epsilon)C$, $I = C\,dV/dt + GV$, $\tau = RC = \epsilon/\sigma$.
- Diode: $Q\propto\sqrt V$, $C = dQ/dV = \epsilon_0A/(W_1+W_2)$.

Concept pages: [[concepts/capacitance]] · [[concepts/conductance]] · [[concepts/electrostatic-energy]].

> [!exam] On Exam 1
> FA26 problem 4 is this lecture's coax with two dielectric layers: $\mathbf{D}$ from Gauss (one expression for both layers), $\mathbf{E} = \mathbf{D}/\epsilon$ per layer, $-\lambda$ on the outer conductor, $V(b) - V(a)$ through both layers (negative — the inner conductor is positive), then $\mathcal{C} = \lambda/[V(a) - V(b)]$ in F/m. The series formula gives (e) in one line and checks (d). Gradable errors: a negative $\mathcal{C}$, F instead of F/m, a single $\epsilon$ over $\ln(b/a)$, layers added in parallel. Worked with new numbers in [[problems/two-layer-coaxial-capacitor]]. The review formula sheet lists $Q = CV$, $G = (\sigma/\epsilon)C$ and $R = 1/G$ together — know why the middle one is true.

> [!tip] Practice this lecture
> [[practice/10-capacitance-and-conductance|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/10-capacitance-and-conductance#101-four-capacitances-by-formula|10.1 Four capacitances by formula]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 10 (parallel plate from $\pm Q$; lossy capacitor $I = C\,dV/dt + GV$; quasi-static condition; energy density; $G = (\sigma/\epsilon)C$; frequency criterion; coax $C$, $\mathcal{C}$, $\mathcal{G}$; diode $Q\propto\sqrt V$ and small-signal $C$). Shao, Lecture 10 slides (given-$V$/given-$Q$ flowcharts; coax by Laplace and by Gauss; fixed-$Q$/fixed-$V$ challenges; energy; "geometric factor"; $V\to E\to J\to I\to G$). FA26 HW4 #4, Exam 1 problem 4. Slips in the course material: see [[0-toolkit/04-errata-in-the-course-materials|errata]].
