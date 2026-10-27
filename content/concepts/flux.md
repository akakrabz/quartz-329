---
title: "Flux"
description: "The surface integral of the normal component of a field — 'how many field lines pierce the surface' — and the two cases where it is trivial to evaluate."
tags: [concept, electrostatics, exam-1]
aliases: ["electric flux", "surface integral", "flux integral"]
---

> [!key] Definition
> The flux of $\mathbf{F}$ through a small flat patch $\Delta\mathbf{S}$ (magnitude = area, direction = chosen normal $\hat{n}$) is
> $$
> \Delta\psi = \mathbf{F}\cdot\Delta\mathbf{S} = (\mathbf{F}\cdot\hat{n})\,\Delta S = F\cos\alpha\,\Delta S = F_n\,\Delta S .
> $$
> A curved surface is tiled with flat patches and summed — the surface integral:
> $$
> \psi = \sum_j \mathbf{F}_j\cdot\Delta\mathbf{S}_j \;\longrightarrow\; \psi = \int_S \mathbf{F}\cdot d\mathbf{S} .
> $$
> Electric flux is in coulombs, $\psi_E = \oint_S \mathbf{D}\cdot d\mathbf{S} = Q_{\text{enc}} \quad [\text{C}]$ for a closed surface ([[concepts/gauss-law|Gauss's law]]); magnetic flux $\psi_B = \int\mathbf{B}\cdot d\mathbf{S}$ is in webers ([[concepts/magnetic-flux|Magnetic flux Ψ]]).

**Physics.** Only the normal component pokes through: the flux depends on arrow density ($\lvert\mathbf{F}\rvert$), tilt ($\cos\alpha$) and size ($\Delta S$). Count the field lines that pass through the surface, with sign: along $\hat{n}$ counts $+$, against counts $-$.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 230" width="640" height="230" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px"><defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker><marker id="ahs" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs><line x1="20.0" y1="45.0" x2="300.0" y2="45.0" stroke="var(--accent)" stroke-width="1.6" marker-end="url(#ah)" opacity="0.55" stroke-linecap="round"/><line x1="340.0" y1="45.0" x2="620.0" y2="45.0" stroke="var(--accent)" stroke-width="1.6" marker-end="url(#ah)" opacity="0.55" stroke-linecap="round"/><line x1="20.0" y1="73.0" x2="300.0" y2="73.0" stroke="var(--accent)" stroke-width="1.6" marker-end="url(#ah)" opacity="0.55" stroke-linecap="round"/><line x1="340.0" y1="73.0" x2="620.0" y2="73.0" stroke="var(--accent)" stroke-width="1.6" marker-end="url(#ah)" opacity="0.55" stroke-linecap="round"/><line x1="20.0" y1="101.0" x2="300.0" y2="101.0" stroke="var(--accent)" stroke-width="1.6" marker-end="url(#ah)" opacity="0.55" stroke-linecap="round"/><line x1="340.0" y1="101.0" x2="620.0" y2="101.0" stroke="var(--accent)" stroke-width="1.6" marker-end="url(#ah)" opacity="0.55" stroke-linecap="round"/><line x1="20.0" y1="129.0" x2="300.0" y2="129.0" stroke="var(--accent)" stroke-width="1.6" marker-end="url(#ah)" opacity="0.55" stroke-linecap="round"/><line x1="340.0" y1="129.0" x2="620.0" y2="129.0" stroke="var(--accent)" stroke-width="1.6" marker-end="url(#ah)" opacity="0.55" stroke-linecap="round"/><line x1="20.0" y1="157.0" x2="300.0" y2="157.0" stroke="var(--accent)" stroke-width="1.6" marker-end="url(#ah)" opacity="0.55" stroke-linecap="round"/><line x1="340.0" y1="157.0" x2="620.0" y2="157.0" stroke="var(--accent)" stroke-width="1.6" marker-end="url(#ah)" opacity="0.55" stroke-linecap="round"/><line x1="20.0" y1="185.0" x2="300.0" y2="185.0" stroke="var(--accent)" stroke-width="1.6" marker-end="url(#ah)" opacity="0.55" stroke-linecap="round"/><line x1="340.0" y1="185.0" x2="620.0" y2="185.0" stroke="var(--accent)" stroke-width="1.6" marker-end="url(#ah)" opacity="0.55" stroke-linecap="round"/><ellipse cx="160" cy="115" rx="10" ry="70" fill="var(--accent2)" fill-opacity="0.25" stroke="currentColor" stroke-width="1.6"/><line x1="160.0" y1="115.0" x2="230.0" y2="115.0" stroke="currentColor" stroke-width="2.4" marker-end="url(#ah)" stroke-linecap="round"/><text x="222.0" y="105.0" text-anchor="middle" fill="currentColor" style="font-size:15px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">n̂</text><text x="160.0" y="210.0" text-anchor="middle" fill="currentColor" style="font-size:14px;">ψ = E · A  (max)</text><ellipse cx="480" cy="115" rx="10" ry="70" transform="rotate(-40 480 115)" fill="var(--accent2)" fill-opacity="0.25" stroke="currentColor" stroke-width="1.6"/><line x1="480.0" y1="115.0" x2="533.6" y2="70.0" stroke="currentColor" stroke-width="2.4" marker-end="url(#ah)" stroke-linecap="round"/><text x="543.2" y="68.7" text-anchor="start" fill="currentColor" style="font-size:15px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">n̂</text><path d="M518,115 A38,38 0 0 0 509.1,90.6" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linejoin="round" stroke-linecap="round"/><text x="530.0" y="101.0" text-anchor="middle" fill="currentColor" style="font-size:15px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">α</text><text x="480.0" y="210.0" text-anchor="middle" fill="currentColor" style="font-size:14px;">ψ = E A cos α = Eₙ A</text><text x="320.0" y="22.0" text-anchor="middle" fill="var(--accent)" style="font-size:13px;">uniform E</text></svg><figcaption><strong>Flux = how many field lines pierce the patch.</strong> Only the component of the field along the patch normal n̂ counts: Δψ = <b>E</b>·Δ<b>S</b> = (E cos α) ΔS. Tilting the patch by α reduces the flux by cos α; edge-on (α = 90°) nothing passes through.</figcaption></figure>

> [!tip] The "trick that works sometimes" — and it is the whole method
> 1. Field **uniform in magnitude** and **everywhere parallel to $d\mathbf{S}$** over a piece of surface → that piece contributes $F\cdot A$.
> 2. Field **parallel to the surface** (perpendicular to $d\mathbf{S}$) → that piece contributes **zero**.
>
> Every Gauss's-law surface in this course (sphere, coaxial cylinder, pillbox) is assembled from pieces of these two kinds.

**Orientation.** A closed surface's normal is **outward**, no choice, and its flux integral is written $\oint_S$. An open surface needs a *chosen* $\hat{n}$; flip it and the flux changes sign. A point charge's flux through an infinite plane that doesn't contain it is $\pm Q/2$ (half-space argument, [[concepts/gauss-law|Gauss's law]]).

**Superposition.** Flux is linear in the field, so fluxes of separate sources add.

**Two theorems about it.** [[concepts/gauss-law|Gauss's law]] (flux of $\mathbf{D}$ out of a closed surface = enclosed charge) is physics; the [[concepts/divergence-theorem|divergence theorem]] (flux out = volume integral of the divergence) is mathematics.

> [!trap]
> - Flux through an *open* surface has the sign of *your* $\hat{n}$; say which you chose.
> - $F\cdot A$ is legal only where $\mathbf{F}$ is both constant in magnitude and normal to the surface — a sphere around an off-centre charge satisfies Gauss's law but not this.

> [!exam] On exams
> Flux through faces of boxes, hemispheres and planes by symmetry and $\pm Q/2$ bookkeeping; outward $d\mathbf{S}$ on Gaussian surfaces (FA26 problems 2 and 4).

**Where it appears.** [[1-electrostatics/03-gauss-law-at-work#1-flux-counting-arrows-through-a-surface|Lecture 3 §1]] (definition and intuition), [[2-magnetostatics/14-faradays-law-and-induced-emf|Lecture 14]] (Faraday's law, $\mathcal{E} = -d\Psi/dt$ — see [[concepts/magnetic-flux|Magnetic flux Ψ]]), [[problems/flux-through-a-plane-from-two-charges|Worked problem — Flux through a plane from two point charges]].

**Related.** [[concepts/differential-elements|Differential elements dl, dS, dV]] · [[concepts/gauss-law|Gauss's law]] · [[concepts/divergence-theorem|Divergence theorem]] · [[concepts/magnetic-flux|Magnetic flux Ψ]].

**Practice.** [[practice/topics#gausss-law-and-flux|Gauss's law and flux]] (18 problems) — for example [[practice/03-gauss-law-at-work#31-two-sheets-of-charge|3.1 Two sheets of charge]] (easy), [[practice/03-gauss-law-at-work#37-point-charge-flux-through-a-disk|3.7 Point-charge flux through a disk]] (medium), [[practice/03-gauss-law-at-work#312-flux-bookkeeping-line-and-sheet|3.12 Flux bookkeeping, line and sheet]] (hard).
