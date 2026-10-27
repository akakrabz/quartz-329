---
title: "Coulomb's law"
description: "The 1/r² radial field of a stationary point charge, with the source-to-field-point convention for the unit vector."
tags: [concept, electrostatics, exam-1]
aliases: ["Coulomb field", "Coulomb's law", "point charge field", "source point and field point"]
---

> [!key] Coulomb's law and the Coulomb field
> Force on $Q_2$ due to $Q_1$ (with $\hat{R}$ the unit vector **from 1 to 2** and $R$ their separation):
> $$
> \mathbf{F}_2 = \frac{Q_1 Q_2}{4\pi\epsilon_0 R^2}\,\hat{R},\qquad \mathbf{F}_1 = -\mathbf{F}_2 .
> $$
> Dividing out the test charge, the **field of a point charge $Q$ at the origin** is
> $$
> \mathbf{E}(\mathbf{r}) = \frac{Q}{4\pi\epsilon_0 r^2}\,\hat{r}
> \qquad\text{(units V/m; } \epsilon_0 \approx 8.854\times10^{-12}\ \text{F/m)} .
> $$
> Radial, $1/r^2$, *away* from positive and *toward* negative charge. Force on a second charge $q$ there: $\mathbf{F} = q\mathbf{E}$.

**Physics.** Coulomb (1785): two small charges at rest feel a force along the line joining them, proportional to the product of the charges and to $1/R^2$, repulsive for like signs. The field is the limit $\mathbf{E} = \lim_{q\to 0}\mathbf{F}/q$, so the test charge does not disturb the sources ([[concepts/electric-field|Electric field E]]).

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 200" width="640" height="200" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px"><defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker><marker id="ahs" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs><line x1="150.0" y1="95.0" x2="470.0" y2="95.0" stroke="currentColor" stroke-width="1.2" stroke-dasharray="6 5" opacity="0.6" stroke-linecap="round"/><text x="310.0" y="85.0" text-anchor="middle" fill="currentColor" style="font-size:16px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">R</text><circle cx="150.0" cy="95.0" r="11.0" fill="var(--hi)" stroke="none" stroke-width="1.5"/><line x1="145.0" y1="95.0" x2="155.0" y2="95.0" stroke="white" stroke-width="2.2" stroke-linecap="round"/><line x1="150.0" y1="90.0" x2="150.0" y2="100.0" stroke="white" stroke-width="2.2" stroke-linecap="round"/><circle cx="470.0" cy="95.0" r="11.0" fill="var(--hi)" stroke="none" stroke-width="1.5"/><line x1="465.0" y1="95.0" x2="475.0" y2="95.0" stroke="white" stroke-width="2.2" stroke-linecap="round"/><line x1="470.0" y1="90.0" x2="470.0" y2="100.0" stroke="white" stroke-width="2.2" stroke-linecap="round"/><text x="150.0" y="127.0" text-anchor="middle" fill="currentColor" style="font-size:15px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">Q₁</text><text x="470.0" y="127.0" text-anchor="middle" fill="currentColor" style="font-size:15px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">Q₂</text><line x1="486.0" y1="55.0" x2="530.0" y2="55.0" stroke="currentColor" stroke-width="1.8" marker-end="url(#ah)" stroke-linecap="round"/><text x="508.0" y="47.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">R̂ (from 1 to 2)</text><line x1="486.0" y1="95.0" x2="590.0" y2="95.0" stroke="var(--hi)" stroke-width="3" marker-end="url(#ah)" stroke-linecap="round"/><text x="540.0" y="115.0" text-anchor="middle" fill="var(--hi)" style="font-size:13px;">F₂ on Q₂</text><line x1="134.0" y1="95.0" x2="30.0" y2="95.0" stroke="var(--hi)" stroke-width="3" marker-end="url(#ah)" stroke-linecap="round"/><text x="80.0" y="115.0" text-anchor="middle" fill="var(--hi)" style="font-size:13px;">F₁ on Q₁</text><text x="320.0" y="160.0" text-anchor="middle" fill="currentColor" style="font-size:13px;">F₂ = Q₁Q₂ R̂ / (4πε₀R²) ;  like charges: F₂ ∥ +R̂ (repel), unlike: F₂ ∥ −R̂ (attract);  F₁ = −F₂</text></svg><figcaption><strong>Coulomb's law, with the bookkeeping the course uses.</strong> Label the <em>source</em> 1 and the point where you want the field 2; the unit vector R̂ always runs from the source to the field point. The force on Q₂ is along +R̂ for like charges and along −R̂ for unlike charges. Newton's third law gives F₁ = −F₂.</figcaption></figure>

**The convention that prevents sign errors.** Number the *source* 1 and the *field point* 2. $\mathbf{R} = \mathbf{r}_2-\mathbf{r}_1$ ("final minus initial"); $\hat{R} = \mathbf{R}/\lvert\mathbf{R}\rvert$ points **from the source to the field point**. The field of a positive charge points along $+\hat{R}$ (away from it); of a negative charge along $-\hat{R}$ (toward it). Newton's third law: $\mathbf{F}_1 = -\mathbf{F}_2$.

> [!trap] Source point vs field point
> For $Q$ at $\mathbf{r}'$ (off the origin), observed at $\mathbf{r}$,
> $$
> \mathbf{E}(\mathbf{r}) = \frac{Q}{4\pi\epsilon_0}\,\frac{\mathbf{r}-\mathbf{r}'}{|\mathbf{r}-\mathbf{r}'|^{3}},
> $$
> with $\mathbf{r}'$ the source location. The cube is not a typo: one power of $\lvert\mathbf{r}-\mathbf{r}'\rvert$ normalizes the direction vector. This is the form used in every superposition integral.

**Numbers.** $\dfrac{1}{4\pi\epsilon_0}\approx 9\times10^{9}$ m/F — but the course never writes "$k = 9\times10^9$": keep $1/(4\pi\epsilon_0)$ explicit, because $\epsilon_0$ becomes $\epsilon = \epsilon_0\epsilon_r$ inside materials ([[concepts/permittivity|Permittivity, susceptibility, and D = εE]], Lectures 8–9).

**Scope.** Exact for charges at rest; for slowly moving charges it is the leading (quasi-static) term. For continuous distributions, replace $Q$ by $dQ = \rho_l\,dl,\ \rho_s\,dS,\ \rho\,dV$ and integrate ([[concepts/five-step-recipe|The 5-step recipe for fields of charge distributions]]). [[concepts/gauss-law|Gauss's law]] is derived from it and outlives it: Gauss holds even when Coulomb fails (moving charges, time-varying fields). Its curl is zero — every radial field is ([[concepts/conservative-field|Conservative (curl-free) fields and the potential]]) — and its potential is $Q/(4\pi\epsilon_0 r)$ ([[concepts/electrostatic-potential|Electrostatic potential V]]).

> [!exam] On exams
> Coulomb integrals are homework; the exam tests the *ideas*: which way $\hat{R}$ points (source → field point, sign of $Q$ decides toward/away), the $1/r^2$ vs $1/r$ vs "no distance" pattern of point, line and sheet, and $4\pi\epsilon_0$ written out.

**Where it appears.** [[1-electrostatics/02-coulombs-law-superposition-and-gauss#2-coulombs-law|Lecture 2 §2]] (statement, convention), [[1-electrostatics/04-divergence-and-curl#6-static-electric-fields-are-curl-free|Lecture 4 §6]] (its curl is zero), [[1-electrostatics/05-curl-free-fields-and-the-electrostatic-potential#6-from-charge-to-v-the-point-charge-and-superposition|Lecture 5 §6]] (its potential).

**Related.** [[concepts/electric-field|Electric field E]] · [[concepts/superposition|Superposition]] · [[concepts/five-step-recipe|The 5-step recipe for fields of charge distributions]] · [[concepts/gauss-law|Gauss's law]] · [[concepts/biot-savart-law|Biot–Savart law]] (the magnetic analogue).

**Practice.** [[practice/topics#coulombs-law-and-point-charges|Coulomb's law and point charges]] (7 problems) — for example [[practice/02-coulombs-law-superposition-and-gauss#21-coulomb-force-as-a-vector|2.1 Coulomb force as a vector]] (easy), [[practice/02-coulombs-law-superposition-and-gauss#28-dipole-on-axis-and-bisector|2.8 Dipole on axis and bisector]] (medium), [[practice/02-coulombs-law-superposition-and-gauss#212-two-charges-one-given-field|2.12 Two charges, one given field]] (hard).
