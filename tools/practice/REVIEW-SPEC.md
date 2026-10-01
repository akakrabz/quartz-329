# Independent verification of a practice page — instructions for the reviewer

You are checking ONE practice-problem page of a study site for UIUC ECE 329 (Fields and Waves I).
Someone else wrote it. The student who will use it is behind and will trust the answer key:
**a wrong number, sign, direction or unit is worse than no answer at all.** Your job is to find
every such error and fix it, independently of the author's own checks.

## Files
- Your page: `/home/claude/work/content-src/practice/<file>.md` (given in your prompt). Edit only this page.
- Format rules (problem-block structure): `/home/claude/work/practice/SPEC.md` §4 (lines 112–127);
  notation and KaTeX rules: §7 (lines 150–181); difficulty rubric: §2 (lines 24–45). Read these
  three short ranges once.
- Site lecture pages (for scope and notation, only if you need them):
  `/home/claude/work/content-src/1-electrostatics/*.md`, `/home/claude/work/content-src/2-magnetostatics/*.md`.
- **Do not open** `/home/claude/work/practice/checks/L<NN>.py` or `.out` (the author's checks):
  your verification must be independent.

## What the lectures cover (scope rule: a Lecture L problem may use only Lectures 1…L)
1 fields via force on a charge, Lorentz force, the four Maxwell equations (integral form) as a roadmap, dl and dS ·
2 Coulomb, superposition, continuous charge (5-step recipe), flux of ε₀E = Q_enc, velocity/mass selectors ·
3 Gauss's law for line/sheet/slab/sphere symmetry, superposition, δ-function densities, ∮B·dS = 0 ·
4 divergence, curl, divergence & Stokes theorems, differential forms of all four Maxwell equations, static E curl-free, continuity ·
5 potential V, E = −∇V, work, eV, V by line integral and by scalar superposition, equipotentials, energy of charges ·
6 circulation/KVL, boundary conditions for E, D, B, H (n̂ from medium 2 into 1), surface charge and current ·
7 Poisson/Laplace in 1-D (planar, cylindrical, spherical), matching conditions, uniqueness, pn junction, vacuum diode ·
8 conductors (E = 0 inside, ρ_s = n̂·D, induced charge), Ohm's law J = σE, R, relaxation time ε/σ, polarization P, D = ε₀E + P, bound charge ·
9 D-first rules in dielectrics, layered/side-by-side media, refraction, graded ε, bound charges ·
10 capacitance, series/parallel layers, energy ½CV² = ∫½εE², force from energy, conductance G = (σ/ε)C, RC discharge, two lossy layers ·
11 Drude (σ = Nq²τ/m, mobility, AC σ(ω)) and Lorentz (χe) models, polarization current ·
12 magnetic force qv×B, force between wires, Biot–Savart, Ampère's law ·
13 current sheets/slabs, solenoids, toroids, vector potential A, current loop and magnetic dipole ·
14 Faraday's law, emf (transformer and motional), Lenz, induced E, voltmeters in changing flux ·
15 inductance (self, mutual), RL circuits, magnetic energy ½LI² = ∫½μH², potentials Φ and A, gauge.

## Procedure (aim for at most ~25 tool calls; do not rewrite the page wholesale)
1. Read the page in full (2–3 Read calls with offset/limit).
2. **Re-solve every problem yourself from its statement.** Write `/home/claude/work/practice/review/R<NN>.py`
   (numpy/scipy only — sympy is not available) with one section per problem that computes every
   final number, sign and direction from the *given data*, preferably by an independent or brute-force
   route (numerical integration of Coulomb/Biot–Savart sums, finite-difference div/curl/grad,
   `np.cross` for every direction, `scipy.integrate` for integrals and ODEs, root-finding for null
   points, energy both as ½CV² and ∫½εE²dV, etc.). Transcribe the page's stated answers into the
   script and print `PASS`/`FAIL` per quantity. Run it and save the output to `R<NN>.out`.
3. Read every solution step: intermediate values, signs, unit vectors, conventions (n̂ from 2 into 1;
   V(b) − V(a) = −∫_a^b E·dl; H = ½ J_s × n̂ with n̂ toward the field point; Biot–Savart dl × R̂ with R̂
   from source to field point; flux sense from the loop's orientation by the right-hand rule;
   ℰ = −dΨ/dt; L = NΨ/I). Also check:
   - the statement is well-posed (all data given, units given, nothing contradictory or over-determined);
   - multiple choice / true–false: the keyed answer is right AND every distractor's explanation is right;
   - find-the-error: the "student work" contains the intended slip (and no unintended second slip), and the correction is right;
   - hints are correct and do not mislead; the **Answer.** line matches the solution body;
   - scope (above) and difficulty label are reasonable (do not relabel unless clearly wrong);
   - the *Source:* line is plausible (do not invent citations; if a cited exam number looks doubtful, say so in your report).
4. **Fix** every problem you find, directly in the page, with minimal edits that keep the block format
   (SPEC §4) and the notation (SPEC §7). Every number you change or add must be printed by `R<NN>.py`.
   Severity: **blocker** = wrong final answer/sign/direction/unit, wrong MC key, ill-posed statement;
   **major** = wrong intermediate step or reasoning, wrong distractor explanation, misleading hint or
   claim, scope violation; **minor** = typo, notation drift, unclear wording. Fix all three kinds
   (minors only when quick). Keep problem numbers and difficulty levels; change a title only if it is wrong.
5. Run both checks and fix anything they report for your page:
   `python3 /home/claude/work/practice/build_practice.py` (block structure; look at your lecture's line)
   and `python3 /home/claude/work/check.py /home/claude/work/content-src /home/claude/.npm-global/lib/node_modules/markdownlint-cli2/node_modules/katex/dist/katex.min.js`
   (links + KaTeX strict; must print OK).
6. Write `/home/claude/work/practice/review/R<NN>.md` (≤ 60 lines): a table `| # | verdict | note |`
   with one row per problem (verdict OK / FIXED / CONCERN), then the findings list with severity and
   what you changed, then anything you could not resolve.
7. Your final message (≤ 10 lines): counts of blockers/majors/minors found and fixed, any open concern.
