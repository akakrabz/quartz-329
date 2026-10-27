---
title: "Lecture 10 — Capacitance and conductance"
description: "Q = CV by the given-V and given-Q chains for plates, coax and spheres, layered dielectrics in series and parallel, stored energy, the leaky capacitor's G = (σ/ε)C, and the pn junction as a nonlinear capacitor; the full treatment is on the topic pages linked from each section."
tags: [lecture, electrostatics, exam-1]
lecture: 10
---

*Lecture 10 · course notes §10 · slides "Capacitance and Conductance" · prev: [[1-electrostatics/09-static-fields-in-dielectric-media|Lecture 9]] · next: [[1-electrostatics/11-lorentz-drude-models-for-conductivity-and-susceptibility|Lecture 11]] (not on Exam 1) · practice: [[practice/10-capacitance-and-conductance|12 problems]]*

> [!abstract] In one breath
> $\pm Q$ on two conductors produces a potential difference $V$; electrostatics is linear, so $C = Q/V$ is a constant of the *geometry and the dielectric* — the **capacitance**, in farads. You compute it by running the chain of the last five lectures either way: $V$ through Laplace's equation to the charge, or $Q$ through Gauss's law to the voltage. A slightly conducting filling also carries a leakage current $I = GV$, $G = (\sigma/\epsilon)C$; the stored energy is $\tfrac12CV^2$, spread through the field at $\tfrac12\epsilon E^2$ per cubic metre; a diode's depletion layer is a capacitor whose $C$ shrinks as the voltage grows.

## 1. Definition, and the two recipes

$Q = CV$ with $V$ the drop from $+$ to $-$ (so $C>0$); given $V$: Laplace $\to\mathbf{E}\to\mathbf{D}\to\rho_s\to Q$; given $Q$: Gauss $\to\mathbf{D}\to\mathbf{E}\to V$. Two conditions: no fringing ($d\ll\sqrt A$) and quasi-static ($\sqrt A\ll c/f$, else a transmission line).

→ Full treatment: [[concepts/capacitance|Capacitance]]

## 2. Parallel plates, both ways

Plates at 0 and $V_0$ a distance $d$ apart: $V = V_0x/d$, $\rho_s = \epsilon V_0/d$ on the positive plate, $C = \epsilon A/d$; from $\pm Q$, $\mathbf{D} = -(Q/A)\hat{x}$ and $V = Qd/\epsilon A$, the same $C$. Trap: a slide's $V = \int_0^d\mathbf{E}\cdot d\mathbf{l}$ comes out negative — integrate from the positive conductor.

→ Full treatment: [[concepts/capacitance|Capacitance]]

## 3. The coaxial cable

By Laplace, $V = V_0\ln(b/r)/\ln(b/a)$ and $\mathbf{E} = V_0\hat{r}/(r\ln(b/a))$; by Gauss with $\lambda$, $V = (\lambda/2\pi\epsilon)\ln(b/a)$. Either way $C = 2\pi\epsilon L/\ln(b/a)$, $\mathcal{C} = 2\pi\epsilon/\ln(b/a)$ F/m. Concept checks: replacing $3\epsilon_0$ by air at fixed $Q$ triples $\mathbf{E}$ and $V$; at fixed $V$ it cuts $\mathbf{D}$ and $Q$ by 3 — $C$ falls by 3 either way.

→ Full treatment: [[concepts/capacitance|Capacitance]]

## 4. Layered dielectrics: series and parallel

Spheres: $C = 4\pi\epsilon ab/(b-a)$, isolated sphere $4\pi\epsilon a$. Layers crossed in succession share $\mathbf{D}$ — series, $1/C = \sum1/C_i$ (Lecture 9's two layers: $C/A = \tfrac23\epsilon_0$, $V = 3$ V ✓; FA26 4(e)'s two-layer coax); layers side by side share $\mathbf{E}$ — parallel, $\mathcal{C} = \pi(\epsilon_1+\epsilon_2)/\ln(b/a)$ for a half-and-half annulus.

→ Full treatment: [[concepts/capacitance|Capacitance]]

## 5. Energy stored in a capacitor and in the field

$W = \int_0^Q(q/C)\,dq = Q^2/2C = \tfrac12CV^2$; for plates this is $\tfrac12\epsilon E^2$ times the gap volume, so $w = \tfrac12\epsilon E^2 = \tfrac12\mathbf{D}\cdot\mathbf{E}$ J/m³ (not W/m³). A battery supplies $CV^2$ to store $\tfrac12CV^2$.

→ Full treatment: [[concepts/electrostatic-energy|Electrostatic energy]]

## 6. Conductance: the leaky capacitor

The same $\mathbf{E}$ drives $\mathbf{J} = \sigma\mathbf{E}$: $I = GV$, $G = \sigma A/d$ for plates, and $G = (\sigma/\epsilon)C$ for any single-medium geometry (one geometric factor). Circuit: $I = C\,dV/dt + GV$, $C\parallel R$; self-discharge $\tau = RC = \epsilon/\sigma$. HW4 #4: spheres $a = 1$ m in $\epsilon = 2\epsilon_0$, $\sigma = 2\times10^{-6}$ S/m — $C\approx222$ pF, $G\approx25$ µS, $\tau = 8.85$ µs.

→ Full treatment: [[concepts/conductance|Conductance and the leaky capacitor]]

## 7. A nonlinear capacitor: the diode junction

The depletion layers store $\pm\rho_2W_2A$ across $V_{21}$; eliminating the widths gives $Q\propto\sqrt V$ and the small-signal $C = dQ/dV = \epsilon_0A/(W_1+W_2)\propto V^{-1/2}$ — the plate formula with the depletion width as gap (varactors).

→ Full treatment: [[concepts/pn-junction|The pn junction]]

## 8. Summary

- $C = Q/V$, $V$ the drop from $+$ to $-$; by a chain: $V\to E\to D\to\rho_s\to Q$ or $Q\to D\to E\to V$.
- Plates $\epsilon A/d$; coax $2\pi\epsilon L/\ln(b/a)$, $\mathcal{C} = 2\pi\epsilon/\ln(b/a)$; spheres $4\pi\epsilon ab/(b-a)$.
- Layers in succession: series ($D$ common); side by side: parallel ($E$ common).
- $W = \tfrac12CV^2$; $w = \tfrac12\epsilon E^2$ [J/m³].
- Lossy filling: $G = (\sigma/\epsilon)C$, $I = C\,dV/dt + GV$, $\tau = RC = \epsilon/\sigma$.
- Diode: $Q\propto\sqrt V$, $C = dQ/dV = \epsilon_0A/(W_1+W_2)$.

Concept pages: [[concepts/capacitance]] · [[concepts/electrostatic-energy]] · [[concepts/conductance]] · [[concepts/pn-junction]].

> [!exam] On Exam 1
> FA26 problem 4: the two-layer coax — one $\mathbf{D}$, $\mathbf{E}$ per layer, $-\lambda$ on the outer conductor, $V$ through both layers, $\mathcal{C}$ in F/m; series formula for (e). Gradable errors and the $G = (\sigma/\epsilon)C$ formula-sheet line: [[concepts/capacitance]], [[concepts/conductance]]; worked in [[problems/two-layer-coaxial-capacitor]].

> [!tip] Practice this lecture
> [[practice/10-capacitance-and-conductance|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/10-capacitance-and-conductance#101-four-capacitances-by-formula|10.1 Four capacitances by formula]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 10 (parallel plate from $\pm Q$; lossy capacitor $I = C\,dV/dt + GV$; quasi-static condition; energy density; $G = (\sigma/\epsilon)C$; frequency criterion; coax $C$, $\mathcal{C}$, $\mathcal{G}$; diode $Q\propto\sqrt V$ and small-signal $C$). Shao, Lecture 10 slides (given-$V$/given-$Q$ flowcharts; coax by Laplace and by Gauss; fixed-$Q$/fixed-$V$ challenges; energy; "geometric factor"; $V\to E\to J\to I\to G$). FA26 HW4 #4, Exam 1 problem 4. Slips in the course material: see [[0-toolkit/04-errata-in-the-course-materials|errata]].
