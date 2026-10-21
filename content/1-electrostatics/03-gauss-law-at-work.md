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

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 230" width="640" height="230" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px"><defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker><marker id="ahs" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs><line x1="20.0" y1="45.0" x2="300.0" y2="45.0" stroke="var(--accent)" stroke-width="1.6" marker-end="url(#ah)" opacity="0.55" stroke-linecap="round"/><line x1="340.0" y1="45.0" x2="620.0" y2="45.0" stroke="var(--accent)" stroke-width="1.6" marker-end="url(#ah)" opacity="0.55" stroke-linecap="round"/><line x1="20.0" y1="73.0" x2="300.0" y2="73.0" stroke="var(--accent)" stroke-width="1.6" marker-end="url(#ah)" opacity="0.55" stroke-linecap="round"/><line x1="340.0" y1="73.0" x2="620.0" y2="73.0" stroke="var(--accent)" stroke-width="1.6" marker-end="url(#ah)" opacity="0.55" stroke-linecap="round"/><line x1="20.0" y1="101.0" x2="300.0" y2="101.0" stroke="var(--accent)" stroke-width="1.6" marker-end="url(#ah)" opacity="0.55" stroke-linecap="round"/><line x1="340.0" y1="101.0" x2="620.0" y2="101.0" stroke="var(--accent)" stroke-width="1.6" marker-end="url(#ah)" opacity="0.55" stroke-linecap="round"/><line x1="20.0" y1="129.0" x2="300.0" y2="129.0" stroke="var(--accent)" stroke-width="1.6" marker-end="url(#ah)" opacity="0.55" stroke-linecap="round"/><line x1="340.0" y1="129.0" x2="620.0" y2="129.0" stroke="var(--accent)" stroke-width="1.6" marker-end="url(#ah)" opacity="0.55" stroke-linecap="round"/><line x1="20.0" y1="157.0" x2="300.0" y2="157.0" stroke="var(--accent)" stroke-width="1.6" marker-end="url(#ah)" opacity="0.55" stroke-linecap="round"/><line x1="340.0" y1="157.0" x2="620.0" y2="157.0" stroke="var(--accent)" stroke-width="1.6" marker-end="url(#ah)" opacity="0.55" stroke-linecap="round"/><line x1="20.0" y1="185.0" x2="300.0" y2="185.0" stroke="var(--accent)" stroke-width="1.6" marker-end="url(#ah)" opacity="0.55" stroke-linecap="round"/><line x1="340.0" y1="185.0" x2="620.0" y2="185.0" stroke="var(--accent)" stroke-width="1.6" marker-end="url(#ah)" opacity="0.55" stroke-linecap="round"/><ellipse cx="160" cy="115" rx="10" ry="70" fill="var(--accent2)" fill-opacity="0.25" stroke="currentColor" stroke-width="1.6"/><line x1="160.0" y1="115.0" x2="230.0" y2="115.0" stroke="currentColor" stroke-width="2.4" marker-end="url(#ah)" stroke-linecap="round"/><text x="222.0" y="105.0" text-anchor="middle" fill="currentColor" style="font-size:15px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">n̂</text><text x="160.0" y="210.0" text-anchor="middle" fill="currentColor" style="font-size:14px;">ψ = E · A  (max)</text><ellipse cx="480" cy="115" rx="10" ry="70" transform="rotate(-40 480 115)" fill="var(--accent2)" fill-opacity="0.25" stroke="currentColor" stroke-width="1.6"/><line x1="480.0" y1="115.0" x2="533.6" y2="70.0" stroke="currentColor" stroke-width="2.4" marker-end="url(#ah)" stroke-linecap="round"/><text x="543.2" y="68.7" text-anchor="start" fill="currentColor" style="font-size:15px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">n̂</text><path d="M518,115 A38,38 0 0 0 509.1,90.6" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linejoin="round" stroke-linecap="round"/><text x="530.0" y="101.0" text-anchor="middle" fill="currentColor" style="font-size:15px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">α</text><text x="480.0" y="210.0" text-anchor="middle" fill="currentColor" style="font-size:14px;">ψ = E A cos α = Eₙ A</text><text x="320.0" y="22.0" text-anchor="middle" fill="var(--accent)" style="font-size:13px;">uniform E</text></svg><figcaption><strong>Flux = how many field lines pierce the patch.</strong> Only the component of the field along the patch normal n̂ counts: Δψ = <b>E</b>·Δ<b>S</b> = (E cos α) ΔS. Tilting the patch by α reduces the flux by cos α; edge-on (α = 90°) nothing passes through.</figcaption></figure>

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

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 260" width="640" height="260" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px"><defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker><marker id="ahs" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs><polygon points="50,180 310,180 350,140 90,140" fill="var(--accent2)" fill-opacity="0.18" stroke="currentColor" stroke-width="1.4"/><text x="54.0" y="194.0" text-anchor="start" fill="currentColor" style="font-size:12px;">z = 0 plane</text><line x1="80.0" y1="160.0" x2="80.0" y2="110.0" stroke="currentColor" stroke-width="2" marker-end="url(#ah)" stroke-linecap="round"/><text x="80.0" y="102.0" text-anchor="middle" fill="currentColor" style="font-size:13px;">n̂ = ẑ</text><line x1="213.5" y1="73.6" x2="259.9" y2="86.0" stroke="var(--hi)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.9" stroke-linecap="round"/><line x1="209.9" y1="79.9" x2="243.8" y2="113.8" stroke="var(--hi)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.9" stroke-linecap="round"/><line x1="203.6" y1="83.5" x2="216.0" y2="129.9" stroke="var(--hi)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.9" stroke-linecap="round"/><line x1="196.4" y1="83.5" x2="184.0" y2="129.9" stroke="var(--hi)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.9" stroke-linecap="round"/><line x1="190.1" y1="79.9" x2="156.2" y2="113.8" stroke="var(--hi)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.9" stroke-linecap="round"/><line x1="186.5" y1="73.6" x2="140.1" y2="86.0" stroke="var(--hi)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.9" stroke-linecap="round"/><line x1="186.5" y1="66.4" x2="140.1" y2="54.0" stroke="var(--accent)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.9" stroke-linecap="round"/><line x1="190.1" y1="60.1" x2="156.2" y2="26.2" stroke="var(--accent)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.9" stroke-linecap="round"/><line x1="196.4" y1="56.5" x2="184.0" y2="10.1" stroke="var(--accent)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.9" stroke-linecap="round"/><line x1="203.6" y1="56.5" x2="216.0" y2="10.1" stroke="var(--accent)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.9" stroke-linecap="round"/><line x1="209.9" y1="60.1" x2="243.8" y2="26.2" stroke="var(--accent)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.9" stroke-linecap="round"/><line x1="213.5" y1="66.4" x2="259.9" y2="54.0" stroke="var(--accent)" stroke-width="1.8" marker-end="url(#ahs)" opacity="0.9" stroke-linecap="round"/><circle cx="200.0" cy="70.0" r="11.0" fill="var(--hi)" stroke="none" stroke-width="1.5"/><line x1="195.0" y1="70.0" x2="205.0" y2="70.0" stroke="white" stroke-width="2.2" stroke-linecap="round"/><line x1="200.0" y1="65.0" x2="200.0" y2="75.0" stroke="white" stroke-width="2.2" stroke-linecap="round"/><text x="222.0" y="58.0" text-anchor="start" fill="currentColor" style="font-size:14px;font-weight:600;">+Q</text><text x="220.0" y="208.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">half the lines go up (never cross the plane),</text><text x="220.0" y="224.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">half go down through it, against n̂</text><text x="220.0" y="244.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600;">⇒  ψ(through plane) = −Q/2</text><text x="400.0" y="60.0" text-anchor="start" fill="currentColor" style="font-size:13px;font-weight:600;">Two charges: add the fluxes</text><text x="400.0" y="88.0" text-anchor="start" fill="currentColor" style="font-size:13px;">+3Q at z = +h:  −3Q/2</text><text x="400.0" y="106.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">(half its lines go down, against n̂)</text><text x="400.0" y="130.0" text-anchor="start" fill="currentColor" style="font-size:13px;">−Q at z = −h:   −Q/2</text><text x="400.0" y="148.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">(lines come down into it)</text><text x="400.0" y="176.0" text-anchor="start" fill="currentColor" style="font-size:14px;font-weight:600;">total  ψ = −2Q</text><text x="400.0" y="206.0" text-anchor="start" fill="currentColor" style="font-size:12px;">Flip n̂ → every sign flips.</text><text x="400.0" y="224.0" text-anchor="start" fill="currentColor" style="font-size:12px;">A closed surface would count</text><text x="400.0" y="240.0" text-anchor="start" fill="currentColor" style="font-size:12px;">only the charge inside it.</text></svg><figcaption><strong>The half-space argument.</strong> A point charge sends its field lines out uniformly in all directions, so exactly half of them cross any infinite plane that does not contain the charge: the flux through the plane has magnitude Q/2. Whether it counts as + or − depends only on which way you chose the normal. With several charges, add the contributions (superposition).</figcaption></figure>

That is the in-class "challenge question", a superposition problem: with charges above and below the plane, add $\pm Q_i/2$, sign set by whether that charge's lines cross along or against $\hat{n}$. Worked with other numbers in [[problems/flux-through-a-plane-from-two-charges]].

## 3. The three symmetries

Same four lines every time; the art is choosing the surface.

> [!recipe] Gauss's law for a field
> 1. **Argue the symmetry** (Coulomb + superposition): which way does $\mathbf{D}$ point, what can it depend on? *Spherical* → $\mathbf{D} = D(r)\hat{r}$. *Cylindrical* (infinite line/cylinder) → $D(r)\hat{r}$ with cylindrical $r$. *Planar* (infinite sheet/slab) → $D(x)\hat{x}$, odd in $x$ about the symmetry plane.
> 2. **Choose the Gaussian surface** so every piece is either "$\mathbf{D}\parallel d\mathbf{S}$ with $|\mathbf{D}|$ constant" or "$\mathbf{D}\perp d\mathbf{S}$": a concentric sphere; a coaxial cylinder (caps contribute 0); a pillbox straddling the symmetry plane (sides contribute 0).
> 3. **Write the bookkeeping** — *top + bottom + side* — and set flux $= Q_{\text{enc}}$. Cancel the arbitrary $L$ or $A$.
> 4. **Convert**: $\mathbf{E} = \mathbf{D}/\epsilon_0$ (vacuum); attach direction and **units** in brackets.

### 3a. Infinite line charge (cylindrical)

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 340" width="640" height="340" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px"><defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker><marker id="ahs" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs><line x1="250.0" y1="330.0" x2="250.0" y2="12.0" stroke="var(--hi)" stroke-width="4" marker-end="url(#ah)" stroke-linecap="round"/><line x1="250.0" y1="330.0" x2="250.0" y2="12.0" stroke="var(--hi)" stroke-width="4" stroke-linecap="round"/><text x="258.0" y="26.0" text-anchor="start" fill="var(--hi)" style="font-size:13px;">ρₗ [C/m]</text><path d="M140,70 L140,250 A110,28 0 0 0 360,250 L360,70" fill="var(--accent)" fill-opacity="0.10" stroke="currentColor" stroke-width="1.5"/><ellipse cx="250" cy="70" rx="110" ry="28" fill="var(--accent)" fill-opacity="0.18" stroke="currentColor" stroke-width="1.5"/><path d="M140,250 A110,28 0 0 1 360,250" fill="none" stroke="currentColor" stroke-width="1.2" stroke-dasharray="4 4"/><line x1="250.0" y1="70.0" x2="360.0" y2="70.0" stroke="currentColor" stroke-width="1.2" stroke-dasharray="4 3" stroke-linecap="round"/><text x="305.0" y="62.0" text-anchor="middle" fill="currentColor" style="font-size:15px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">r</text><line x1="382.0" y1="70.0" x2="382.0" y2="250.0" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/><line x1="376.0" y1="70.0" x2="388.0" y2="70.0" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/><line x1="376.0" y1="250.0" x2="388.0" y2="250.0" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/><text x="394.0" y="165.0" text-anchor="start" fill="currentColor" style="font-size:15px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">L</text><line x1="195.0" y1="60.0" x2="195.0" y2="25.0" stroke="currentColor" stroke-width="2" marker-end="url(#ah)" stroke-linecap="round"/><text x="195.0" y="18.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">dS</text><line x1="360.0" y1="140.0" x2="400.0" y2="140.0" stroke="currentColor" stroke-width="2" marker-end="url(#ah)" stroke-linecap="round"/><line x1="140.0" y1="140.0" x2="100.0" y2="140.0" stroke="currentColor" stroke-width="2" marker-end="url(#ah)" stroke-linecap="round"/><line x1="360.0" y1="200.0" x2="400.0" y2="200.0" stroke="currentColor" stroke-width="2" marker-end="url(#ah)" stroke-linecap="round"/><line x1="140.0" y1="200.0" x2="100.0" y2="200.0" stroke="currentColor" stroke-width="2" marker-end="url(#ah)" stroke-linecap="round"/><text x="406.0" y="145.0" text-anchor="start" fill="currentColor" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">dS</text><line x1="262.0" y1="115.0" x2="352.0" y2="115.0" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#ah)" opacity="0.9" stroke-linecap="round"/><line x1="238.0" y1="115.0" x2="148.0" y2="115.0" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#ah)" opacity="0.9" stroke-linecap="round"/><line x1="262.0" y1="170.0" x2="352.0" y2="170.0" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#ah)" opacity="0.9" stroke-linecap="round"/><line x1="238.0" y1="170.0" x2="148.0" y2="170.0" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#ah)" opacity="0.9" stroke-linecap="round"/><line x1="262.0" y1="225.0" x2="352.0" y2="225.0" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#ah)" opacity="0.9" stroke-linecap="round"/><line x1="238.0" y1="225.0" x2="148.0" y2="225.0" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#ah)" opacity="0.9" stroke-linecap="round"/><text x="290.0" y="108.0" text-anchor="middle" fill="var(--accent)" style="font-size:13px;">D, E</text><text x="410.0" y="90.0" text-anchor="start" fill="currentColor" style="font-size:13px;font-weight:600;">∮ D·dS = top + bottom + side</text><text x="410.0" y="118.0" text-anchor="start" fill="currentColor" style="font-size:14px;">top:  D ⊥ dS  →  0</text><text x="410.0" y="143.0" text-anchor="start" fill="currentColor" style="font-size:14px;">bottom:  0</text><text x="410.0" y="168.0" text-anchor="start" fill="currentColor" style="font-size:14px;">side:  D · 2πrL</text><text x="410.0" y="205.0" text-anchor="start" fill="currentColor" style="font-size:14px;">Q_enc = ρₗ L</text><text x="410.0" y="240.0" text-anchor="start" fill="currentColor" style="font-size:14px;font-weight:600;">⇒  D = ρₗ / (2πr)   [C/m²]</text><text x="410.0" y="265.0" text-anchor="start" fill="currentColor" style="font-size:14px;font-weight:600;">⇒  E = ρₗ / (2πε₀r) r̂   [V/m]</text></svg><figcaption><strong>Gauss's law with cylindrical symmetry.</strong> Choose a coaxial cylinder of radius r and length L. By symmetry <b>D</b> is radial and depends only on r, so the caps contribute nothing (field parallel to the caps) and the side contributes D·(2πrL). The L cancels against the enclosed charge ρₗL.</figcaption></figure>

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

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 300" width="640" height="300" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px"><defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker><marker id="ahs" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs><line x1="30.0" y1="150.0" x2="270.0" y2="150.0" stroke="var(--hi)" stroke-width="4" stroke-linecap="round"/><text x="45.0" y="142.0" text-anchor="middle" fill="var(--hi)" style="font-size:12px;">+</text><text x="75.0" y="142.0" text-anchor="middle" fill="var(--hi)" style="font-size:12px;">+</text><text x="105.0" y="142.0" text-anchor="middle" fill="var(--hi)" style="font-size:12px;">+</text><text x="135.0" y="142.0" text-anchor="middle" fill="var(--hi)" style="font-size:12px;">+</text><text x="165.0" y="142.0" text-anchor="middle" fill="var(--hi)" style="font-size:12px;">+</text><text x="195.0" y="142.0" text-anchor="middle" fill="var(--hi)" style="font-size:12px;">+</text><text x="225.0" y="142.0" text-anchor="middle" fill="var(--hi)" style="font-size:12px;">+</text><text x="255.0" y="142.0" text-anchor="middle" fill="var(--hi)" style="font-size:12px;">+</text><text x="272.0" y="155.0" text-anchor="start" fill="var(--hi)" style="font-size:14px;">ρₛ</text><rect x="105" y="95" width="90" height="110" fill="var(--accent)" fill-opacity="0.10" stroke="currentColor" stroke-width="1.5"/><text x="202.0" y="90.0" text-anchor="start" fill="currentColor" style="font-size:12px;">cap area A</text><line x1="125.0" y1="95.0" x2="125.0" y2="60.0" stroke="currentColor" stroke-width="2" marker-end="url(#ah)" stroke-linecap="round"/><text x="125.0" y="54.0" text-anchor="middle" fill="currentColor" style="font-size:12px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">dS</text><line x1="125.0" y1="205.0" x2="125.0" y2="240.0" stroke="currentColor" stroke-width="2" marker-end="url(#ah)" stroke-linecap="round"/><line x1="165.0" y1="138.0" x2="165.0" y2="102.0" stroke="var(--accent)" stroke-width="2.4" marker-end="url(#ah)" stroke-linecap="round"/><text x="182.0" y="120.0" text-anchor="middle" fill="var(--accent)" style="font-size:15px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">E</text><line x1="165.0" y1="162.0" x2="165.0" y2="198.0" stroke="var(--accent)" stroke-width="2.4" marker-end="url(#ah)" stroke-linecap="round"/><text x="150.0" y="275.0" text-anchor="middle" fill="currentColor" style="font-size:13px;">2·(D·A) = ρₛ A  ⇒  E = ẑ sgn(z) ρₛ/(2ε₀)</text><rect x="420" y="50" width="120" height="150" fill="var(--hi)" fill-opacity="0.15" stroke="none"/><line x1="420.0" y1="50.0" x2="420.0" y2="200.0" stroke="currentColor" stroke-width="1.1" stroke-dasharray="4 4" opacity="0.6" stroke-linecap="round"/><line x1="540.0" y1="50.0" x2="540.0" y2="200.0" stroke="currentColor" stroke-width="1.1" stroke-dasharray="4 4" opacity="0.6" stroke-linecap="round"/><text x="426.0" y="64.0" text-anchor="start" fill="var(--hi)" style="font-size:13px;">ρ</text><text x="420.0" y="216.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">−W/2</text><text x="540.0" y="216.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">W/2</text><line x1="360.0" y1="200.0" x2="610.0" y2="200.0" stroke="currentColor" stroke-width="1.3" marker-end="url(#ahs)" stroke-linecap="round"/><text x="618.0" y="204.0" text-anchor="start" fill="currentColor" style="font-size:15px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">x</text><line x1="480.0" y1="210.0" x2="480.0" y2="60.0" stroke="currentColor" stroke-width="1.3" marker-end="url(#ahs)" stroke-linecap="round"/><text x="488.0" y="72.0" text-anchor="start" fill="currentColor" style="font-size:14px;">Eₓ</text><path d="M370,245 L420,245 L540,155 L600,155" fill="none" stroke="var(--accent)" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><line x1="480.0" y1="155.0" x2="540.0" y2="155.0" stroke="currentColor" stroke-width="1" stroke-dasharray="3 3" opacity="0.6" stroke-linecap="round"/><text x="486.0" y="149.0" text-anchor="start" fill="currentColor" style="font-size:12px;">ρW/(2ε₀)</text><text x="486.0" y="259.0" text-anchor="start" fill="currentColor" style="font-size:12px;">−ρW/(2ε₀)</text><text x="485.0" y="275.0" text-anchor="middle" fill="currentColor" style="font-size:13px;">inside: Eₓ = ρx/ε₀ ; outside: ±ρW/(2ε₀)</text></svg><figcaption><strong>Planar symmetry: sheet and slab.</strong> Left: a pillbox straddling a charged sheet; both caps carry equal flux D·A and the sides carry none, so 2DA = ρₛA. Right: for a uniform slab the same pillbox argument gives a field that grows linearly inside (more enclosed charge as the caps move out) and saturates outside at the sheet value with ρₛ = ρW.</figcaption></figure>

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

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 400" width="640" height="400" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px"><defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker><marker id="ahs" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs><line x1="60.0" y1="55.0" x2="560.0" y2="55.0" stroke="currentColor" stroke-width="1.2" marker-end="url(#ahs)" stroke-linecap="round"/><text x="568.0" y="59.0" text-anchor="start" fill="currentColor" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">x</text><rect x="180" y="55" width="70" height="24" fill="var(--accent2)" fill-opacity="0.35" stroke="currentColor" stroke-width="1"/><rect x="250" y="31" width="70" height="24" fill="var(--hi)" fill-opacity="0.35" stroke="currentColor" stroke-width="1"/><text x="215.0" y="93.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">−ρ₁ (acceptors)</text><text x="285.0" y="25.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">+ρ₂ (donors)</text><text x="176.0" y="49.0" text-anchor="end" fill="currentColor" style="font-size:11px;">−W₁</text><text x="324.0" y="49.0" text-anchor="start" fill="currentColor" style="font-size:11px;">W₂</text><text x="60.0" y="47.0" text-anchor="start" fill="currentColor" style="font-size:13px;">ρ(x)</text><text x="560.0" y="25.0" text-anchor="end" fill="currentColor" style="font-size:12px;">neutral: ρ₁W₁ = ρ₂W₂</text><line x1="60.0" y1="185.0" x2="560.0" y2="185.0" stroke="currentColor" stroke-width="1.2" marker-end="url(#ahs)" stroke-linecap="round"/><text x="60.0" y="129.0" text-anchor="start" fill="currentColor" style="font-size:13px;">Eₓ of each slab</text><path d="M89.0,151.0 L180.0,151.0 L250.0,219.0 L411.0,219.0" fill="none" stroke="var(--accent2)" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"/><path d="M89.0,219.0 L250.0,219.0 L320.0,151.0 L411.0,151.0" fill="none" stroke="var(--hi)" stroke-width="2.4" stroke-dasharray="6 4" stroke-linejoin="round" stroke-linecap="round"/><text x="96.0" y="145.0" text-anchor="start" fill="var(--accent2)" style="font-size:11px;">+ρ₁W₁/2ε₀</text><text x="341.0" y="145.0" text-anchor="start" fill="var(--hi)" style="font-size:11px;">+ρ₂W₂/2ε₀</text><line x1="60.0" y1="300.0" x2="560.0" y2="300.0" stroke="currentColor" stroke-width="1.2" marker-end="url(#ahs)" stroke-linecap="round"/><text x="60.0" y="286.0" text-anchor="start" fill="currentColor" style="font-size:13px;">total Eₓ</text><path d="M89.0,300.0 L180.0,300.0 L250.0,368.0 L320.0,300.0 L411.0,300.0" fill="none" stroke="var(--accent)" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><text x="256.0" y="372.0" text-anchor="start" fill="currentColor" style="font-size:12px;">−ρ₁W₁/ε₀ = −ρ₂W₂/ε₀</text><text x="138.0" y="318.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">E = 0 outside</text><text x="369.0" y="318.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">E = 0 outside</text></svg><figcaption><strong>A pn junction's depletion field, by superposition of two slabs.</strong> Each charged layer is a slab whose field you already know (linear inside, constant outside). Because the layers carry equal and opposite charge per area, the two outside plateaus cancel and the two inside ramps add: the field is a triangle, strongest at the metallurgical junction and zero outside the depletion region.</figcaption></figure>

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
