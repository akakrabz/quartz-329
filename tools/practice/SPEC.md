# Practice-problem bank — authoring spec (ECE 329, Lectures 2–19)

You are writing practice-problem pages for a Quartz study site for UIUC ECE 329 "Fields and Waves I".
The student who asked for this is behind on lectures and anxious; their own diagnosis is "I did not
solve enough examples". The bank must therefore (1) start genuinely easy and build confidence,
(2) reach real exam difficulty, and (3) be **correct in every number and sign** — a wrong answer key
does more harm than no answer key.

## 1. Files

- Write **only** the page(s) assigned to you, at `/home/claude/work/content-src/practice/<file>.md`
  (exact file names in §9). Do not edit any other page of the site.
- Write a Python verification script per page at `/home/claude/work/practice/checks/L<NN>.py`
  (e.g. `L03.py`), run it, and save its output to `/home/claude/work/practice/checks/L<NN>.out`.
- `sympy` is NOT installed and cannot be installed (no network). Use `numpy` and `scipy` only:
  verify closed forms numerically (evaluate at several parameter values; finite-difference
  derivatives, curls and divergences; `scipy.integrate.quad/dblquad/tplquad` for integrals;
  explicit `np.cross` for every direction). Constants: ε₀ = 8.8541878128e-12 F/m, μ₀ = 4π×10⁻⁷ H/m,
  e = 1.602176634e-19 C, mₑ = 9.1093837e-31 kg, c = 2.99792458e8 m/s.
- **Every number, sign and direction that appears in an answer must be printed by your script.**
  If a result is symbolic, check it numerically at ≥ 2 parameter sets against a brute-force
  computation (numerical integral, finite difference, superposition sum, etc.).

## 2. Problem counts and difficulty

Per lecture page: **12 problems — 5 easy, 3 medium, 4 hard** (Lecture 11: 8 problems — 4 easy,
2 medium, 2 hard). Lectures 16–19 have 12 each. Number them `L.1 … L.12` in order easy → medium → hard.

| tag | what it means | time | hint? | solution length |
|---|---|---|---|---|
| **easy** | one law or definition, ≤ 2 steps; plug-in with understanding, a direct symmetry argument, a units/direction question, or a conceptual multiple-choice item | 2–5 min | optional | 3–10 lines |
| **medium** | a standard exam sub-problem: one modelling decision (which surface/path/coordinates/region), a real integral or a 3–4 step chain | 8–15 min | required | 8–25 lines |
| **hard** | exam-length, multi-part (a)–(d): superposition of several pieces, several regions with matching conditions, a non-trivial integral, a sign-heavy direction analysis, or combining two lectures | 20–40 min | required | 20–60 lines |

Variety on every page: at least **2 conceptual multiple-choice or true/false items** (easy, exam
style, with every distractor explained in the solution), at least **1 "find the error" item**
(show a short student solution with one classic slip — sign, missing ε, wrong n̂, wrong surface —
and ask what is wrong), numeric problems with SI units, and symbolic derivations. At least **one
hard problem per page must be modelled on a real past exam problem** (re-parameterized, cited).

**Scope rule:** a problem for Lecture L may use only material from Lectures 1…L (a student working
in order is never blocked). Lecture L problems should mostly exercise Lecture L itself.

Do not duplicate the ten long worked problems already on the site (`content-src/problems/*.md`)
— variants with a genuinely different geometry or twist are fine.

## 3. Page template (copy exactly, then fill)

```markdown
---
title: "Practice — Lecture 3: Gauss's law at work"
description: "12 practice problems (5 easy, 3 medium, 4 hard) on flux, the three Gauss symmetries, slabs and superposition, each with a folded hint and a worked solution."
tags: [practice, electrostatics, exam-1]
lecture: 3
---

*Practice for [[1-electrostatics/03-gauss-law-at-work|Lecture 3]] · concepts: [[concepts/gauss-law]] · [[concepts/flux]] · all practice: [[practice/index|hub]] · by difficulty: [[practice/easy|easy]] · [[practice/medium|medium]] · [[practice/hard|hard]]*

Work each problem on paper first. Open the **hint** only when stuck, and the **solution** only after you have an answer you would hand in. Every answer here has been checked numerically.

## Easy

### 3.1 Two sheets of charge

> [!easy] Easy · Gauss's law · charge sheets · superposition
> (statement) …
>
> *Source: original.*

> [!solution]- Solution
> (worked solution in LaTeX) …
>
> **Answer.** …

### 3.2 …

## Medium

### 3.6 …

> [!medium] Medium · …
> …

> [!hint]- Hint
> …

> [!solution]- Solution
> …

## Hard

### 3.9 …

> [!hard] Hard · …
> …

> [!hint]- Hint
> …

> [!solution]- Solution
> …

### Sources for this page
One short paragraph listing what was used (course notes examples, FA26 HW numbers, which old exams, Rao, "original").
```

Tags in frontmatter: `[practice, electrostatics, exam-1]` for Lectures 2–10, `[practice, electrostatics]`
for Lecture 11, `[practice, magnetostatics]` for Lectures 12–15. `lecture:` = the lecture number.
`description:` must state the counts and topics. Concept links in the header line: 2–4 relevant
existing pages from `content-src/concepts/` (check the file exists).

## 4. The problem block — exact rules (a parser builds the difficulty index from these)

1. Heading: `### L.N Short title` (L = lecture number, N = 1…12; title ≤ 6 words, no punctuation
   other than commas/hyphens/apostrophes, no math in headings).
2. The **next** non-blank line is the difficulty callout:
   `> [!easy] Easy · tag · tag`, `> [!medium] Medium · tag · tag`, `> [!hard] Hard · tag · tag`
   — 1–3 short topic tags after the difficulty word, separated by ` · ` (space, middle dot, space).
   Tags are plain words (e.g. `Gauss's law`, `cylindrical symmetry`, `boundary conditions`,
   `Biot–Savart`, `Lenz`, `inductance`, `multiple choice`, `find the error`).
3. The problem statement is inside that callout. Last line of the callout: `> *Source: ….*`
4. Then (medium/hard: required; easy: optional) a hint: `> [!hint]- Hint` (folded).
5. Then always the solution: `> [!solution]- Solution` (folded), ending with a line
   `> **Answer.** …` that states the final result(s) with units (and directions).
6. Separate consecutive callouts with **one blank line** (an unprefixed empty line). Inside a
   callout, a paragraph break is a line containing only `>`. Never nest callouts. Never put a
   blank line inside a callout.

## 5. Writing the statement

- Self-contained: every quantity given with units; geometry described in coordinates
  (e.g. "a sheet on the plane z = 0", "a cylinder of radius a = 2 cm along the z axis"). No figures.
- State the medium ("free space" unless stated) and what to find, part by part: (a), (b), …
- Multiple choice: list options on separate lines `> (a) …` with `>` lines between them if needed.
- Numbers chosen so the arithmetic is clean enough for an exam without a calculator **or** clearly
  marked as a calculator problem. Use ε₀ symbolically when that keeps the numbers clean
  (e.g. charge "$8\pi\epsilon_0$ C" as the course often does).

## 6. Writing the solution (the most important part)

Structure every medium/hard solution as: **Setup** (symmetry, coordinates, which law and why) →
**Work** (each step in LaTeX, display math for main steps) → **Answer** → **Check** (units, a
limit, a symmetry, a boundary condition, or an independent second route). Easy solutions can be
3–6 lines but still say *why*, not just *what*. Add one sentence "**Watch out:** …" when there is a
classic trap. For multiple choice, explain why each wrong option is wrong. For find-the-error,
name the slip, fix it, and give the correct result.

Tone: clear, encouraging, no filler. Second person ("you") is fine.

## 7. Notation and LaTeX conventions (match the site exactly)

- Vectors bold: `\mathbf{E}`, `\mathbf{D}`, `\mathbf{J}`, `\mathbf{r}`; unit vectors `\hat{x}`, `\hat{y}`,
  `\hat{z}`, `\hat{r}`, `\hat\phi`, `\hat\theta`, `\hat{n}`; differential elements `d\mathbf{l}`, `d\mathbf{S}`, `dV`.
- `\epsilon_0`, `\epsilon`, `\epsilon_r` (never `\varepsilon`), `\mu_0`; `\rho` [C/m³], `\rho_s` [C/m²],
  `\rho_l` [C/m] (λ only when quoting an exam, and say so); bound charge `\rho_b`, `\rho_{sb}`;
  `\sigma` = conductivity only; surface current `\mathbf{J}_s` [A/m].
- Cylindrical coordinates $(r,\phi,z)$ with $r$ the distance from the z axis; spherical $(r,\theta,\phi)$.
- Potential differences written explicitly: $V(b)-V(a) = -\int_a^b\mathbf{E}\cdot d\mathbf{l}$. Never write $V_{ab}$.
- Boundary conditions with subscripts 1/2 and $\hat{n}$ pointing **from medium 2 into medium 1**:
  $\hat{n}\cdot(\mathbf{D}_1-\mathbf{D}_2)=\rho_s$, $\hat{n}\times(\mathbf{E}_1-\mathbf{E}_2)=0$,
  $\hat{n}\cdot(\mathbf{B}_1-\mathbf{B}_2)=0$, $\hat{n}\times(\mathbf{H}_1-\mathbf{H}_2)=\mathbf{J}_s$.
- Magnetics: $\mathbf{H} = \mathbf{B}/\mu_0$ in free space; Biot–Savart $d\mathbf{B} = \dfrac{\mu_0 I\,d\mathbf{l}\times\hat R}{4\pi R^2}$ with $\hat R$
  from the source element to the field point; sheet $\mathbf{H} = \tfrac12\mathbf{J}_s\times\hat n$ ($\hat n$ toward the field point);
  flux $\Psi = \int_S\mathbf{B}\cdot d\mathbf{S}$ [Wb] with $d\mathbf{S}$ from the loop's sense by the right-hand rule;
  emf $\mathcal{E} = \oint(\mathbf{E}+\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l} = -d\Psi/dt$; inductance $L = N\Psi/I$;
  per-unit-length $\mathcal{L}$, $\mathcal{C}$, $\mathcal{G}$ (script); "counter-clockwise" always with a viewpoint ("seen from $+z$").
- Units in square brackets or words after results: `$E = 3$ V/m`, `$[\text{C/m}^2]$`.
- **KaTeX only, no custom macros.** Allowed: `\dfrac`, `\tfrac`, `\text{}`, `\boxed{}`, `\begin{aligned}…\end{aligned}`,
  `\begin{cases}…\end{cases}`, `\operatorname{sgn}`, `\lvert\rvert`, `\,`. Do **not** use `\begin{align}`,
  `\varepsilon`, `\bm`, `\vec` (use `\mathbf`), unicode characters inside math (write `\mu`, not μ),
  `\textbf` inside math. Display math inside a callout:
  ```
  > $$
  > E = \frac{\rho_s}{2\epsilon_0}
  > $$
  ```
  (the `$$` lines alone, each prefixed `> `). Inline math `$…$` stays on one line.
- Tables: escape a literal `|` as `\|`; use `\lvert x\rvert` for absolute values inside tables.
- Wikilinks are full paths: `[[1-electrostatics/05-curl-free-fields-and-the-electrostatic-potential|Lecture 5]]`,
  `[[concepts/gauss-law]]`. Only link to pages that exist; anchors must match a real heading slug.

## 8. Sources you may draw on (cite each problem's source in its `*Source:*` line)

Allowed: "original"; course notes examples (re-parameterized); FA26 homework (re-parameterized);
old exams (re-parameterized: change numbers and at least one geometric detail so the official key
does not apply; never copy an answer key's text); Rao's textbook (reworded, new numbers); classic
textbook problems (reworded). Cite like `*Source: FA26 HW2 #5, new numbers.*`,
`*Source: SP18 Exam 1 #1(iv) style.*`, `*Source: Summer 2019 HE1 #3, re-parameterized.*`,
`*Source: Rao, drill problem style.*`, `*Source: classic.*`, `*Source: original.*`.

Files (read what helps; images are readable with the Read tool):
- Site lecture pages (the definitive notation and scope): `/home/claude/work/content-src/1-electrostatics/*.md`,
  `/home/claude/work/content-src/2-magnetostatics/*.md`; concept pages `/home/claude/work/content-src/concepts/*.md`.
- Digests of the course notes and annotated slides (lecture examples, challenge questions, conventions):
  `/home/claude/work/notes*/DIGEST*.md`, `/home/claude/work/slides*/DIGEST*.md`, `/home/claude/work/digests/`.
- FA26 homework and solutions (text): `/home/claude/work/sources/txt/329fall26hw{1,2,3,4}.txt` and `…sol.txt`
  (HW1 ≈ L1–3, HW2 ≈ L3–6, HW3 ≈ L6–9, HW4 ≈ L9–12). PDFs in `/mnt/user-data/uploads/ECE 329/Homework/`.
- Old exams: text `/home/claude/work/sources/txt/329sp18_exam1.txt` (electrostatics + a little magnetics, MC),
  `329sp18_exam1_sol.txt`, `329sp18_exam2.txt` (MC on wires/Faraday/potentials/sheet BC, toroid flux & emf,
  parallel-plate inductance), `329sum20he1sol.txt`, `329sum20he2sol.txt` (handwritten answers, OCR garbled);
  scanned solutions as page images in `/home/claude/work/sources/img/` (`329sp18_exam2_sol-*.png`,
  `329sum1{7,8,9}he1sol-*.png` ≈ electrostatics L2–8, `329sum1{7,8,9}he2sol-*.png` ≈ L8–15).
  FA26 Exam 1 transcription: `/home/claude/work/exam/FA26-exam1-transcription.md` (already used by the site's worked problems).
- Rao, *Fundamentals of Electromagnetics for ECE* (2009), text: `/home/claude/work/sources/txt/rao.txt`
  (symbols are garbled by extraction; drill problems carry answers; odd-numbered answers at the end).
  Verify anything taken from it yourself.

## 9. Assignments (file names)

| L | file | lecture page |
|---|---|---|
| 2 | `practice/02-coulombs-law-superposition-and-gauss.md` | `1-electrostatics/02-coulombs-law-superposition-and-gauss` |
| 3 | `practice/03-gauss-law-at-work.md` | `1-electrostatics/03-gauss-law-at-work` |
| 4 | `practice/04-divergence-and-curl.md` | `1-electrostatics/04-divergence-and-curl` |
| 5 | `practice/05-electrostatic-potential.md` | `1-electrostatics/05-curl-free-fields-and-the-electrostatic-potential` |
| 6 | `practice/06-circulation-and-boundary-conditions.md` | `1-electrostatics/06-circulation-and-boundary-conditions` |
| 7 | `practice/07-poisson-and-laplace.md` | `1-electrostatics/07-poisson-and-laplace` |
| 8 | `practice/08-conductors-dielectrics-and-polarization.md` | `1-electrostatics/08-conductors-dielectrics-and-polarization` |
| 9 | `practice/09-static-fields-in-dielectric-media.md` | `1-electrostatics/09-static-fields-in-dielectric-media` |
| 10 | `practice/10-capacitance-and-conductance.md` | `1-electrostatics/10-capacitance-and-conductance` |
| 11 | `practice/11-lorentz-drude-models.md` | `1-electrostatics/11-lorentz-drude-models-for-conductivity-and-susceptibility` |
| 12 | `practice/12-magnetic-force-biot-savart-and-ampere.md` | `2-magnetostatics/12-magnetic-force-biot-savart-and-amperes-law` |
| 13 | `practice/13-current-sheets-solenoids-and-vector-potential.md` | `2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential` |
| 14 | `practice/14-faradays-law-and-induced-emf.md` | `2-magnetostatics/14-faradays-law-and-induced-emf` |
| 15 | `practice/15-inductance-and-magnetic-energy.md` | `2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials` |
| 16 | `practice/16-charge-conservation-and-displacement-current.md` | `3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations` |
| 17 | `practice/17-magnetization-and-maxwell-in-matter.md` | `3-maxwell-and-waves/17-magnetization-and-maxwells-equations-in-matter` |
| 18 | `practice/18-wave-equation-and-plane-waves.md` | `3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves` |
| 19 | `practice/19-radiation-from-current-sheets.md` | `3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets` |

Frontmatter tags for Lectures 16–19: `[practice, waves]`.

## 10. Coverage checklists (cover every bullet at least once; ideas are suggestions)

**L2 Coulomb, superposition, continuous charge, Gauss's birth, Lorentz-force selectors.** Vector Coulomb force; E of several point charges; null point between charges; flux of a point charge through a closed surface / one cube face / a cube with the charge at a corner (Q/24 for the far faces); five-step integrals: ring on axis, finite line segment (bisector and general point), semicircular arc at its centre, disk on axis with its two limits; dipole on axis and bisector and the 1/D³ far field; velocity selector (E = vB), mass selector radius; uniform line of charge field by integration vs Gauss.

**L3 Gauss at work.** Flux through tilted/curved surfaces; sphere (uniform, shell, ρ(r) profiles), cylinder (uniform, shell, ρ(r)), sheet/two sheets/slab (uniform and graded); superposition of building blocks (slab + sheet, coax ± charges, sphere with off-centre cavity → uniform field); total charge from δ-function densities; flux through a disk from a point charge (solid angle); ∮B·dS = 0 consequences.

**L4 Divergence, curl, theorems.** ∇·D → ρ in Cartesian/cylindrical/spherical; ∇×E and "can this be electrostatic?"; verify divergence theorem on a cube/sphere and Stokes on a square/quarter-disk; surface charge from a jump in a piecewise D; identities ∇·∇× = 0, ∇×∇ = 0; continuity ∇·J = −∂ρ/∂t computations (rate of change of charge in a region).

**L5 Potential.** V of point-charge sets, work qΔV, electron-volts; E = −∇V at a point; potential difference along paths in a given E (straight vs staircase path, path independence check); V from E for sphere/cylinder/slab with a chosen reference; V on the axis of ring/disk by scalar superposition; equipotentials; energy of assembling charges; "is this E conservative → find V".

**L6 Circulation and boundary conditions.** ∮E·dl = 0 checks (KVL); D/E across dielectric interfaces with and without ρₛ; refraction angles; oblique interfaces (n̂ not along an axis); conductor surface (ρₛ = n̂·D, E ⟂); the magnetic pair (Bₙ continuous, Hₜ jumps by Jₛ) at a sheet current; bound surface charge at an interface; which components are continuous (MC).

**L7 Poisson and Laplace.** 1-D Laplace in planar/cylindrical/spherical with two boundary values → V, E, ρₛ on plates; Poisson with uniform and graded ρ between plates (max of V, field at plates); two-region problems with matching V and D; vacuum diode / pn junction numbers; check a given V satisfies Laplace/Poisson and find ρ; wedge V(φ); uniqueness reasoning.

**L8 Conductors, dielectrics, polarization.** R = ℓ/(σA), J, E in wires and radial/coax geometries; relaxation time ε/σ and decay of interior charge; conductor in a field (induced ρₛ), cavity with a charge (induced charges); P = ε₀χₑE, D = ε₀E + P; bound charges ρ_b = −∇·P, ρ_sb = P·n̂ for given P (sphere, cylinder, slab with graded P) with total bound charge zero; point charge in a dielectric sphere.

**L9 Fields in dielectric media.** D-first chain in layered plates (given ρₛ or given V); side-by-side dielectrics (E common); coax/sphere with dielectric layers; refraction at interfaces; graded ε(x) or ε(r); bound charges at each face and inside; capacitance-free voltage computations; exam-style "interface with ρₛ, find E, D, P on both sides".

**L10 Capacitance and conductance.** C for plates/coax/spheres/isolated sphere (numbers); series vs parallel dielectric layers; energy ½CV² and ∫½εE²dV agree; constant-Q vs constant-V dielectric insertion; G = (σ/ε)C and R of leaky structures; RC self-discharge; two lossy layers in series (interface charge in steady state); diode small-signal C; force on plates from energy.

**L11 Lorentz–Drude (8 problems).** Drift velocity, mobility, σ from N, q, m, τ; several species; AC σ(ω) magnitude and phase at ω = ν; χₑ from N_d, ω₀; polarization current ∂P/∂t for a sinusoidal field and its ratio to conduction current; Drude τ vs relaxation τ.

**L12 Magnetic force, Biot–Savart, Ampère.** qv×B forces (vectors), circular motion radius/period, crossed fields; force per length between wires (attract/repel); B of long wire, direction; total current from J or Jₛ (δ-function currents); Biot–Savart: loop centre, square loop centre, finite segment, semicircle + straight leads; Ampère: thick wire with J(r), hollow conductor, coax with arbitrary currents, enclosed-current signs; force on a rectangular loop near a wire; hollow wire with off-axis hole (uniform field).

**L13 Sheets, solenoids, vector potential, loop.** Field of one/two/three current sheets (½Jₛ×n̂ with directions); slab with uniform and graded J; solenoid B, flux, nested solenoids; toroid N I/(2πr); Hₜ jump checks; A for a uniform B (A = ½B×r), B from a given A (curl), Coulomb-gauge check; A of a long wire; loop on axis, Helmholtz pair, far-field 1/r³; finite solenoid on axis.

**L14 Faraday, emf, Lenz, motional, voltmeters.** Flux through tilted loops; emf for B(t) given; Lenz directions (magnets, shrinking/expanding loops, decaying fields); motional emf of a bar, both routes; rotating loop/generator; rotating rod ½BωL²; loop entering/leaving a field region (piecewise emf, force); nonuniform B(x) moving loop; induced E inside/outside a solenoid with dI/dt; magnetic braking with mass; voltmeter readings in a changing flux (two meters, different leads).

**L15 Inductance, energy, potentials.** L of solenoid/toroid (rectangular cross-section)/coax/parallel plates; N² scaling; RL decay and rise (τ = L/R), energy at t; mutual inductance wire–loop, coaxial solenoids; energy density and energy by ∫½μH²dV; L from energy (internal inductance of a wire μ/8π per m); 𝓛𝓒 = με checks; two-wire line; potentials: E = −∇Φ − ∂A/∂t, B = ∇×A from given (Φ, A), gauge-transformation invariance; SP18 Exam 2 style toroid flux/emf and parallel-plate line inductance with scaling questions.

**L16 Charge conservation, displacement current, Maxwell's equations, dynamic boundary conditions.** Continuity in integral and differential form (rate of change of charge in a cube/sphere/cylinder from a given J; ∂ρ/∂t at a point; current leaving a region of decaying charge, with the Lecture 8 relaxation link); displacement current density ∂D/∂t for a given E(t) (uniform, sinusoidal in time) and the displacement current through an area; displacement vs conduction current in a lossy medium (ratio of amplitudes for E₀cos ωt — no phasors); the charging capacitor (displacement current between the plates equals the wire current; H between circular plates by Ampère–Maxwell); the two-surface/MMF argument (variants of the draining charge, not a copy of the site's worked problem); taking the divergence of Ampère–Maxwell and of Faraday (why ∇·B = 0 and Gauss's law are consistent with the curl equations); checking a given (E, B) pair against all four Maxwell equations in free space with given ρ, J (keep it non-wave-like, e.g. quasi-static fields or a field with sources); the four boundary conditions for time-varying fields at an interface (sheet current, surface charge, oblique n̂); perfect conductor: which fields can exist just outside, ρ_s = n̂·D and J_s = n̂×H for given exterior fields; MC/TF on what is new in Lecture 16 vs. statics.

**L17 Magnetization, Maxwell's equations in matter.** Magnetic moment $\mathbf{m} = I\mathbf{A}$ of a loop or orbiting charge (direction by the right-hand rule), torque $\mathbf{m}\times\mathbf{B}$ and which way it turns the loop; $\mathbf{M} = N\mathbf{m}$ [A/m] from a density of moments; magnetization current $\mathbf{J}_M = \nabla\times\mathbf{M}$ for a given non-uniform $\mathbf{M}$ (Cartesian and cylindrical) and surface current $\mathbf{J}_{sM} = \mathbf{M}\times\hat n$ on the faces, with the net bound current through a cross-section equal to zero; a uniformly magnetized rod as a solenoid ($nI\to M$), its $\mathbf{B}$ inside; $\mathbf{H} = \mathbf{B}/\mu_0-\mathbf{M}$ and the decomposition $\mathbf{J} = \mathbf{J}_f+\partial\mathbf{P}/\partial t+\nabla\times\mathbf{M}$; linear media $\mathbf{M} = \chi_m\mathbf{H}$, $\mathbf{B} = \mu\mathbf{H}$, $\mu_r$ (numbers for dia-, para-, ferromagnets; MC/TF on which is which and why); solenoid/toroid/coax with a magnetic core or a partial core ($H$ from free current, then $B$, $M$, bound currents, $L\propto\mu$); hysteresis loop reading ($B_r$, $H_c$, saturation; TF); boundary conditions with $\mu_1\neq\mu_2$ ($B_n$ continuous, $H_t$ jumps by the *free* $J_s$, $\mu_1H_{1n} = \mu_2H_{2n}$), refraction $\tan\theta_1/\tan\theta_2 = \mu_1/\mu_2$ and lines leaving iron almost normally, bound surface current $\hat n\times(\mathbf{M}_1-\mathbf{M}_2)$ at an interface; the slab between current sheets (free $\mathbf{H}$ by superposition, then $\mathbf{B}$, $\mathbf{M}$, bound currents on the faces) in new geometries; polarization ↔ magnetization twin problems. Do not duplicate the site's worked problem `problems/fields-across-a-magnetic-interface.md` or the Lecture 17 page's slab example numbers.

**L18 Wave equation, plane TEM waves.** Source-free Maxwell equations and the steps of the wave-equation derivation (which assumption enters where; MC on what fails without $\partial\mathbf{D}/\partial t$, with $\rho\neq0$, or with non-uniform $\epsilon$); checking whether a given $E_x(z,t)$ satisfies the 1-D wave equation and finding $v$; reading direction and speed from arguments such as $t-z/v$, $t+0.02x$, $(0.05y-t)^2$, $\cos(\omega t-\beta z)$ written as real cosines (slowness vs speed, term-order traps); $v = 1/\sqrt{\mu\epsilon}$, $\eta = \sqrt{\mu/\epsilon}$, $\eta_0\approx120\pi$ Ω, $c\approx300$ m/µs; $\mathbf{H}$ from $\mathbf{E}$ and the reverse with $\mathbf{H} = \hat u\times\mathbf{E}/\eta$ for $x$- and $y$-polarized waves travelling toward $\pm z$ and along other axes (write the cross product out), $\lvert\mathbf{B}\rvert = \lvert\mathbf{E}\rvert/v$; why a $z$-polarized wave cannot travel along $z$; moving pulses (a waveform given at one place versus time or at one instant versus position: the snapshot at another time, what a probe records, mirrored vs not); two counter-propagating pulses overlapping (E adds, H subtracts); $v$ and $\eta$ in a lossless dielectric or magnetic medium, $\epsilon_r$ from a measured speed or $\eta$; the cable link $1/\sqrt{\mathcal{L}\mathcal{C}} = v$ and $\sqrt{\mathcal{L}/\mathcal{C}} = \eta\times$ geometry. Out of scope: the current-sheet amplitude $\eta J_s/2$ (Lecture 19), phasors, the Poynting theorem and power (Lecture 20; $\mathbf{E}\times\mathbf{H}$ only as the direction rule). Wavelength may be used only if the problem defines it (the spatial period of a snapshot). Do not duplicate the site's worked problem `problems/a-pulse-on-the-move.md`; a variant of SP18 Exam 2 #4 must differ in waveform, numbers and direction from both the exam and that worked problem.

**L19 d'Alembert solutions, radiation from current sheets.** Uniform plane TEM waves (E and H transverse, E×H along the travel, planes of constant phase; MC/TF on which given fields are TEM plane waves); fields radiated by an infinite current sheet $\mathbf{J}_s(t)$ in any plane and orientation: $\mathbf{E} = -\tfrac{\eta}{2}\mathbf{J}_s(t-\lvert\xi\rvert/v)$ on both sides, $\mathbf{H} = \tfrac12\mathbf{J}_s(t-\lvert\xi\rvert/v)\times\hat n$ with $\hat n$ away from the sheet (check both against the boundary conditions of Lecture 16 and against Lecture 13's static sheet); snapshots versus position and records versus time for given waveforms (rect, ramp, triangle, cosine), including the delay $\lvert\xi\rvert/v$ and the mirror symmetry of the two waves; sheets in a dielectric ($v$, $\eta$ change, amplitude $\eta J_s/2$); two parallel sheets (superposition of their waves, timing of overlap); the inverse problem (find $J_s(t)$ from a measured field); sinusoidal sheet currents written as real cosines with $\omega$, $f$, $\beta = \omega/v$, $\lambda = 2\pi/\beta$, phase velocity; reading $\beta$, $\lambda$, $f$ and direction from $\cos(\omega t\mp\beta z)$; the instantaneous Poynting vector $\mathbf{S} = \mathbf{E}\times\mathbf{H}$ [W/m²] for the sheet's waves (direction, value, time dependence — no Poynting theorem, no averages beyond what the Lecture 19 page shows); Lorentz-force ratio of magnetic to electric force on a charge in a plane wave ($v/c$). Out of scope: phasors, complex η, Poynting's theorem, lossy media. Do not duplicate the site's worked problem `problems/a-current-sheet-launches-two-waves.md`; one hard problem should be SP18 Exam 2 #5 style, re-parameterized so its sheet plane, current direction, waveform and numbers differ from both the exam and that worked problem.

## 11. Exemplars (style anchors — numbers verified; you may reuse one if it fits your lecture)

```markdown
### 3.1 Two sheets of charge

> [!easy] Easy · Gauss's law · charge sheets · superposition
> Two infinite sheets lie in free space: $\rho_{s1} = +4$ nC/m² on the plane $z = 0$ and $\rho_{s2} = -1$ nC/m² on the plane $z = 2$ m. Find $\mathbf{E}$ in the three regions $z<0$, $0<z<2$ m and $z>2$ m.
>
> *Source: original.*

> [!solution]- Solution
> A single sheet $\rho_s$ on $z = z_0$ makes $\mathbf{E} = \dfrac{\rho_s}{2\epsilon_0}\operatorname{sgn}(z-z_0)\,\hat{z}$: pointing away from a positive sheet, toward a negative one, the same magnitude at every distance. Superpose:
> $$
> E_z = \frac{1}{2\epsilon_0}\Big[\rho_{s1}\operatorname{sgn}(z) + \rho_{s2}\operatorname{sgn}(z-2)\Big].
> $$
> $z<0$: $E_z = \dfrac{-4+1}{2\epsilon_0}\times10^{-9} = -169$ V/m. $\quad 0<z<2$: $E_z = \dfrac{4+1}{2\epsilon_0}\times10^{-9} = +282$ V/m. $\quad z>2$: $E_z = \dfrac{4-1}{2\epsilon_0}\times10^{-9} = +169$ V/m.
>
> **Check:** crossing $z = 0$ upward, $\epsilon_0E_z$ jumps by $(5+3)/2 = 4$ nC/m² $= \rho_{s1}$; crossing $z = 2$, by $(3-5)/2 = -1$ nC/m² $= \rho_{s2}$ — the boundary condition of Lecture 6.
>
> **Answer.** $\mathbf{E} = -169\,\hat{z}$ V/m for $z<0$, $+282\,\hat{z}$ V/m between the sheets, $+169\,\hat{z}$ V/m for $z>2$ m.

### 12.7 A wire with a nonuniform current

> [!medium] Medium · Ampère's law · cylindrical symmetry
> A long straight wire of radius $a = 1$ mm along the $z$ axis carries the current density $\mathbf{J} = J_0\dfrac{r}{a}\hat{z}$ for $r<a$, with $J_0 = 3\times10^6$ A/m². (a) Find the total current. (b) Find $\mathbf{H}$ inside and outside the wire. (c) Evaluate $H$ at $r = 0.5$ mm and $r = 2$ mm.
>
> *Source: classic.*

> [!hint]- Hint
> The current through a circle of radius $r$ is $\int_0^r J(r')\,2\pi r'\,dr'$ — not $J\cdot\pi r^2$, because $J$ varies with $r$.

> [!solution]- Solution
> **Setup.** Cylindrical symmetry and the right-hand rule give $\mathbf{H} = H_\phi(r)\hat\phi$; Ampère on a circle of radius $r$: $H_\phi\cdot2\pi r = I_{\text{enc}}(r)$.
>
> (a) $I = \displaystyle\int_0^a J_0\frac{r'}{a}\,2\pi r'\,dr' = \frac{2\pi J_0a^2}{3} = 2\pi\ \text{A}\approx6.28$ A.
>
> (b) Inside: $I_{\text{enc}} = \dfrac{2\pi J_0r^3}{3a}$, so $H_\phi = \dfrac{J_0r^2}{3a}$. Outside: $H_\phi = \dfrac{I}{2\pi r} = \dfrac{J_0a^2}{3r}$.
>
> (c) $H(0.5\text{ mm}) = \dfrac{J_0a}{12} = 250$ A/m; $\ H(2\text{ mm}) = \dfrac{J_0a}{6} = 500$ A/m.
>
> **Check:** both forms give $J_0a/3$ at $r = a$ (no surface current, no jump), and $\dfrac1r\dfrac{d}{dr}(rH_\phi) = J_0r/a = J_z$ inside ✓.
>
> **Answer.** $I = 2\pi J_0a^2/3\approx6.28$ A; $\mathbf{H} = \hat\phi\,J_0r^2/(3a)$ for $r<a$ and $\hat\phi\,J_0a^2/(3r)$ for $r>a$; 250 A/m and 500 A/m.

### 14.11 Magnetic braking

> [!hard] Hard · motional emf · Lenz · energy
> A bar of mass $m = 0.1$ kg slides without friction on two horizontal rails $\ell = 0.5$ m apart, joined at one end by a resistor $R = 0.2\ \Omega$ (bar and rails have negligible resistance). A uniform field $B = 0.4$ T is perpendicular to the plane of the rails. At $t = 0$ the bar moves away from the resistor at $v_0 = 3$ m/s and is then left alone.
> (a) Find the current and the magnetic force on the bar as functions of its speed $v$, with directions.
> (b) Find $v(t)$ and the distance the bar travels before stopping.
> (c) Show that the total energy dissipated in $R$ equals the initial kinetic energy.
>
> *Source: classic.*

> [!hint]- Hint
> The emf is $vB\ell$, the current $vB\ell/R$, and the force on the current-carrying bar is $I\ell B$ opposing the motion — so Newton's law becomes $m\,dv/dt = -kv$.

> [!solution]- Solution
> **(a)** Motional emf $\mathcal{E} = vB\ell$, current $I = vB\ell/R$. The force on the bar is $I\boldsymbol{\ell}\times\mathbf{B}$, of magnitude $I\ell B = \dfrac{B^2\ell^2}{R}v$ and, by Lenz, directed *against* the velocity (the loop's flux grows; the induced current must resist the growth). At $t = 0$: $I = 3$ A, $F = 0.6$ N.
>
> **(b)** Newton: $m\dfrac{dv}{dt} = -\dfrac{B^2\ell^2}{R}v$, so
> $$
> v(t) = v_0e^{-t/\tau},\qquad \tau = \frac{mR}{B^2\ell^2} = \frac{0.1\times0.2}{0.16\times0.25} = 0.5\ \text{s}.
> $$
> Distance: $\displaystyle\int_0^\infty v\,dt = v_0\tau = 1.5$ m.
>
> **(c)** $\displaystyle\int_0^\infty I^2R\,dt = \frac{B^2\ell^2v_0^2}{R}\int_0^\infty e^{-2t/\tau}dt = \frac{B^2\ell^2v_0^2}{R}\cdot\frac{\tau}{2} = \tfrac12mv_0^2 = 0.45$ J ✓.
>
> **Watch out:** the magnetic force does no work on the charges; the kinetic energy becomes heat through the electric field in the resistor.
>
> **Answer.** $I = vB\ell/R$, $F = B^2\ell^2v/R$ opposing the motion; $v = 3e^{-2t}$ m/s; 1.5 m; 0.45 J dissipated = initial kinetic energy.
```

## 12. Before you finish

1. Run your check script; every number on the page must appear in its output.
2. Run `python3 /home/claude/work/check.py /home/claude/work/content-src /home/claude/.npm-global/lib/node_modules/markdownlint-cli2/node_modules/katex/dist/katex.min.js`
   and fix every error reported for **your** files (errors in other files are not yours).
3. Re-read your page once as the anxious student would: is each easy problem really easy? Is each
   hint helpful without giving the answer away? Does each solution say *why*?
4. Reply with: the file path(s), a table of your problems (number, title, difficulty, tags, source),
   the path of the check script and output, and any doubts or anything you could not verify.

## 13. Lectures 16–18 (build 5)

- FA26 HW6 (`sources/txt` has no copy on purpose) is **open homework**: do not base any problem on it, re-parameterized or not. FA26 HW5 is closed; its text and solutions are in `/home/claude/work/sources/txt/329fall26hw5.txt` and `329fall26hw5sol.txt` and may be used like the other homework (re-parameterized).
- Lecture 17–18 scope and notation come from the site pages `3-maxwell-and-waves/17-…md`, `18-…md` once written, and from the digests in `/home/claude/work/digest6/`.
- No phasors before Lecture 21: time-harmonic fields are written as real cosines; no complex η, no Poynting vector before Lecture 20 (instantaneous E×H may be mentioned only if the Lecture 18 page introduces it).

