---
title: "Gauss's law"
description: "The flux of D out of any closed surface equals the charge enclosed — derived from Coulomb's law, always true, and a two-line calculation of E whenever the symmetry is spherical, cylindrical or planar."
tags: [concept, electrostatics, exam-1]
aliases: ["Gauss law", "Gauss's law for E", "Maxwell equation 1", "enclosed charge", "Gaussian surface"]
---

> [!key] Gauss's law — the first Maxwell equation
> $$
> \oint_S \mathbf{D}\cdot d\mathbf{S} = Q_{\text{enc}} = \int_V \rho\,dV
> $$
> for **any** closed surface $S$ bounding volume $V$, $d\mathbf{S}$ **outward**, $\mathbf{D} = \epsilon_0\mathbf{E}$ in vacuum (C/m²). Flux out = charge enclosed, the algebraic sum of what is inside. Charges outside $S$ add nothing to the *flux* (they do change $\mathbf{E}$ on $S$; their flux cancels). Differential form: $\nabla\cdot\mathbf{D} = \rho$ ([[concepts/divergence|Divergence]]).

**Physics — from Coulomb to Gauss.** Surround a point charge $Q$ by a sphere of radius $r$ and compute the flux of $\epsilon_0\mathbf{E}$:

$$
\oint_S \epsilon_0\mathbf{E}\cdot d\mathbf{S}
= \epsilon_0\,\frac{Q}{4\pi\epsilon_0 r^2}\;\underbrace{(4\pi r^2)}_{\text{sphere area}} = Q .
$$

On the sphere $\mathbf{E}$ has constant magnitude and is parallel to the outward $d\mathbf{S}$, so the integral is $\lvert\mathbf{E}\rvert\times$area; the area's $r^2$ cancels Coulomb's $1/r^2$ **exactly**, independent of $r$. Three observations make this a law:

- **Any surface.** Lines leaving $Q$ never stop; each crosses any enclosing surface exactly once net (a wiggly surface crossed three times: two cancel). So the flux is $Q$ through *any* closed surface around $Q$ — and **zero** for one *not* enclosing $Q$ (every line that enters also leaves).
- **Superposition.** Flux is linear in $\mathbf{E}$: $Q_1 + Q_2 + \dots$ for charges inside, nothing for those outside.
- **Naming.** The **electric flux density** $\mathbf{D} = \epsilon_0\mathbf{E}$ (C/m²) makes flux come out in coulombs. In materials $\mathbf{D} = \epsilon_0\mathbf{E}+\mathbf{P}$, and $\mathbf{D}$ keeps counting *free* charge ([[concepts/electric-flux-density|Electric flux density D]]).

Derived here from Coulomb's law, Gauss's law is more fundamental: it holds for moving charges and time-varying fields, where Coulomb's law fails. The notes: "at this stage the introduction of Gauss's law may seem unnecessary"; [[concepts/symmetric-charge-distributions|Lecture 3]] gets the line charge in two lines, and Lecture 4 makes it one of the four governing equations ([[concepts/maxwells-equations|Maxwell's equations]]).

**Always true, sometimes useful.** As a *calculation tool* it works only when symmetry makes $\lvert\mathbf{D}\rvert$ constant on a surface you can name:

| symmetry | source | Gaussian surface | result |
|---|---|---|---|
| spherical | point, uniformly charged sphere/shell | concentric sphere | $D = Q_{\text{enc}}/(4\pi r^2)$ |
| cylindrical | infinite line, cylinder, coax | coaxial cylinder (caps give 0) | $D = \rho_{l,\text{enc}}/(2\pi r)$ |
| planar | infinite sheet or slab, charge symmetric about its mid-plane | pillbox straddling the symmetry plane (sides give 0; both caps count) | $2D = \rho_{s,\text{enc}}$ |
| planar, *not* symmetric | parallel plates $\pm\rho_s$, layered sheets | superpose sheet fields, or a one-cap pillbox with its other cap where $E=0$ | plates: $D = \rho_s$ between, $0$ outside |

> [!recipe] The four lines
> 1. State the symmetry: direction of $\mathbf{D}$ and what it depends on.
> 2. Choose the surface so each piece is "$\mathbf{D}\parallel d\mathbf{S}$, constant" or "$\mathbf{D}\perp d\mathbf{S}$".
> 3. Write *top + bottom + side* $= Q_{\text{enc}}$; cancel the arbitrary $L$ or $A$.
> 4. $\mathbf{E} = \mathbf{D}/\epsilon$; attach direction and units.
>
> The three symmetric cases worked out, and their superposition: [[concepts/symmetric-charge-distributions|Symmetric charge distributions]].

**Differential form.** Shrink the surface to a point: $\nabla\cdot\mathbf{D} = \rho$ ([[1-electrostatics/04-divergence-and-curl#2-divergence-flux-per-unit-volume|Lecture 4 §2]]). Given a field, differentiate to find the charge that made it (FA26 problem 1c).

**Magnetic twin.** $\oint_S\mathbf{B}\cdot d\mathbf{S} = 0$, $\nabla\cdot\mathbf{B} = 0$: no magnetic charge ([[concepts/magnetic-flux|Magnetic flux Ψ]]).

**Examples — flux bookkeeping by symmetry and superposition alone (Lecture 3 §2).**
- $Q$ at the centre of a **cube**: flux $Q$ in total, $Q/6$ through each face.
- $Q$ at the centre of a **very thin box** ($h\to 0$): nearly all flux leaves through the two big faces, $Q/2$ each.
- $Q$ at the centre of the flat face of a **hemisphere**: $Q/2$ through the dome, **zero** through the flat base (field tangential there); the other half go into the lower half-space. (The charge sits *on* the surface: "enclosed" is solid angle, $2\pi$ of $4\pi$.)
- $Q$ a distance $h$ above an **infinite plane**: half the lines cross it, so the flux is $\pm Q/2$, sign fixed by your normal.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 260" width="640" height="260" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px"><defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker><marker id="ahs" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs><polygon points="50,180 310,180 350,140 90,140" fill="var(--accent2)" fill-opacity="0.18" stroke="currentColor" stroke-width="1.4"/><text x="54.0" y="194.0" text-anchor="start" fill="currentColor" style="font-size:12px;">z = 0 plane</text><line x1="80.0" y1="160.0" x2="80.0" y2="110.0" stroke="currentColor" stroke-width="2" marker-end="url(#ah)" stroke-linecap="round"/><text x="80.0" y="102.0" text-anchor="middle" fill="currentColor" style="font-size:13px;">n̂ = ẑ</text><line x1="213.5" y1="73.6" x2="259.9" y2="86.0" stroke="var(--hi)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.9" stroke-linecap="round"/><line x1="209.9" y1="79.9" x2="243.8" y2="113.8" stroke="var(--hi)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.9" stroke-linecap="round"/><line x1="203.6" y1="83.5" x2="216.0" y2="129.9" stroke="var(--hi)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.9" stroke-linecap="round"/><line x1="196.4" y1="83.5" x2="184.0" y2="129.9" stroke="var(--hi)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.9" stroke-linecap="round"/><line x1="190.1" y1="79.9" x2="156.2" y2="113.8" stroke="var(--hi)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.9" stroke-linecap="round"/><line x1="186.5" y1="73.6" x2="140.1" y2="86.0" stroke="var(--hi)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.9" stroke-linecap="round"/><line x1="186.5" y1="66.4" x2="140.1" y2="54.0" stroke="var(--accent)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.9" stroke-linecap="round"/><line x1="190.1" y1="60.1" x2="156.2" y2="26.2" stroke="var(--accent)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.9" stroke-linecap="round"/><line x1="196.4" y1="56.5" x2="184.0" y2="10.1" stroke="var(--accent)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.9" stroke-linecap="round"/><line x1="203.6" y1="56.5" x2="216.0" y2="10.1" stroke="var(--accent)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.9" stroke-linecap="round"/><line x1="209.9" y1="60.1" x2="243.8" y2="26.2" stroke="var(--accent)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.9" stroke-linecap="round"/><line x1="213.5" y1="66.4" x2="259.9" y2="54.0" stroke="var(--accent)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.9" stroke-linecap="round"/><circle cx="200.0" cy="70.0" r="11.0" fill="var(--hi)" stroke="none" stroke-width="1.5"/><line x1="195.0" y1="70.0" x2="205.0" y2="70.0" stroke="white" stroke-width="2.2" stroke-linecap="round"/><line x1="200.0" y1="65.0" x2="200.0" y2="75.0" stroke="white" stroke-width="2.2" stroke-linecap="round"/><text x="222.0" y="58.0" text-anchor="start" fill="currentColor" style="font-size:14px;font-weight:600;">+Q</text><text x="220.0" y="208.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">half the lines go up (never cross the plane),</text><text x="220.0" y="224.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">half go down through it, against n̂</text><text x="220.0" y="244.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600;">⇒  ψ(through plane) = −Q/2</text><text x="400.0" y="60.0" text-anchor="start" fill="currentColor" style="font-size:13px;font-weight:600;">Two charges: add the fluxes</text><text x="400.0" y="88.0" text-anchor="start" fill="currentColor" style="font-size:13px;">+3Q at z = +h:  −3Q/2</text><text x="400.0" y="106.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">(half its lines go down, against n̂)</text><text x="400.0" y="130.0" text-anchor="start" fill="currentColor" style="font-size:13px;">−Q at z = −h:   −Q/2</text><text x="400.0" y="148.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">(lines come down into it)</text><text x="400.0" y="176.0" text-anchor="start" fill="currentColor" style="font-size:14px;font-weight:600;">total  ψ = −2Q</text><text x="400.0" y="206.0" text-anchor="start" fill="currentColor" style="font-size:12px;">Flip n̂ → every sign flips.</text><text x="400.0" y="224.0" text-anchor="start" fill="currentColor" style="font-size:12px;">A closed surface would count</text><text x="400.0" y="240.0" text-anchor="start" fill="currentColor" style="font-size:12px;">only the charge inside it.</text></svg><figcaption><strong>The half-space argument.</strong> A point charge sends its field lines out uniformly in all directions, so exactly half of them cross any infinite plane that does not contain the charge: the flux through the plane has magnitude Q/2. Whether it counts as + or − depends only on which way you chose the normal. With several charges, add the contributions (superposition).</figcaption></figure>

That is the in-class "challenge question", a superposition problem: with charges above and below the plane, add $\pm Q_i/2$, sign set by whether that charge's lines cross along or against $\hat{n}$. Worked with other numbers in [[problems/flux-through-a-plane-from-two-charges|Worked problem — Flux through a plane from two point charges]].

> [!trap]
> - Gauss's law gives $\mathbf{D}$, which does not care about the material; $\mathbf{E} = \mathbf{D}/\epsilon$ does.
> - A surface with *less* symmetry than the source (a cube around a point charge) still satisfies the law — it just doesn't let you pull $D$ out of the integral.
> - Pillbox errors (second cap, non-uniform $\rho$, sgn): [[concepts/symmetric-charge-distributions|Symmetric charge distributions]].

> [!exam] On exams
> The exam prefers the Gauss shortcut where symmetry allows (FA26 problems 2 and 4): state the symmetry, write "top + bottom + side" explicitly, $Q_{\text{enc}}$ as an integral when $\rho$ varies, then $\mathbf{E} = \mathbf{D}/\epsilon$ layer by layer. Ideas tested: only enclosed charge sets the flux; the $1/r^2$, $1/r$, "no distance" pattern.

**Where it appears.** [[1-electrostatics/02-coulombs-law-superposition-and-gauss#5-from-coulomb-to-gauss|Lecture 2 §5]] (derived), [[1-electrostatics/03-gauss-law-at-work#2-gausss-law-restated-for-use|Lecture 3 §2–3]] (used), [[1-electrostatics/04-divergence-and-curl|Lecture 4]] (differential form), Lectures 8–10 (conductors, dielectrics, capacitance), [[problems/charged-slab-with-a-power-law-profile|Worked problem — Charged slab with a non-uniform profile]].

**Related.** [[concepts/flux|Flux]] · [[concepts/symmetric-charge-distributions|Symmetric charge distributions]] · [[concepts/electric-flux-density|Electric flux density D]] · [[concepts/divergence|Divergence]] · [[concepts/superposition|Superposition]] · [[concepts/amperes-law|Ampère's law]] (the same idea with a loop: circulation of $\mathbf{H}$ = enclosed current) · [[demos/point-charges-and-gauss|Demo — Point charges, field lines, and a movable Gaussian loop]].

**Practice.** [[practice/topics#gausss-law-and-flux|Gauss's law and flux]] (18 problems) — for example [[practice/03-gauss-law-at-work#31-two-sheets-of-charge|3.1 Two sheets of charge]] (easy), [[practice/03-gauss-law-at-work#37-point-charge-flux-through-a-disk|3.7 Point-charge flux through a disk]] (medium), [[practice/03-gauss-law-at-work#312-flux-bookkeeping-line-and-sheet|3.12 Flux bookkeeping, line and sheet]] (hard).
