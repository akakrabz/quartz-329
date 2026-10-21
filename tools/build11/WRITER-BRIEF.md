# Brief for the Lecture 26–30 page writers (ECE 329 study site, build 11)

You write teaching notes for a Quartz 5 study site for UIUC ECE 329 "Fields and Waves I", from the course notes
(Kudeki) only — the student attends lecture and asked that pages follow the notes. Physics correctness of every
equation, sign, direction and number is paramount. **New this build: the student finds the existing pages too
verbose. Write tight.** (Rules in "Concision" below — they override any longer habit you see in the exemplars.)

## Read first
1. Your lecture's notes: `/mnt/user-data/uploads/ECE 329/Notes/329lectNN.pdf`. Page renders already exist in
   `/home/claude/work/digest10/imgNN/p-*.png` — **look at every page image** (margin equations and figures carry
   content); `digest10/lectNN.txt` is the garbled text layer. Glance at the neighbouring lectures' notes
   (`digest10/img26/` … `img31/`) for boundaries.
2. Style/notation exemplars (read fully): the Lecture 25 page
   `/home/claude/work/content-src/3-maxwell-and-waves/25-wave-reflection-and-transmission.md` (the target length and
   style) and the Lecture 24 page. For L27–30 also read Lecture 15 §5 (`2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials.md`,
   transmission-line 𝓛, 𝓒) and Lecture 10 §3 (coax capacitance). Skim `concepts/reflection-and-transmission.md` and the
   worked problem `problems/working-back-from-a-transmitted-wave.md`.
3. Conventions: `/home/claude/stage/SITE-STATUS.md`, "Conventions".
4. Rao text `/home/claude/work/sources/txt/rao.txt` for cross-checks (grep "standing wave", "radiation pressure",
   "transmission line", "characteristic impedance", "bounce", "reflection coefficient", "line voltage").
5. Past exams: `/home/claude/stage/EXAM-CATALOGUE.md` Part 2 (Exam 3 papers): its index lists L24 (all polarization
   items), L25, L26 (standing waves), L27–L30 (transmission lines, bounce diagrams) problems. Scans as PNG: `/home/claude/work/sources/img/<stem>-N.png`.
6. Figure helpers: `/home/claude/work/figs.py` lines 1–86 and 1083–1120; model module `/home/claude/work/figs_l25.py`.

## Division of material (the notes decide; stay inside your lecture and link to the others)
- **L26 Standing waves, radiation pressure** — PEC mirror: incident + reflected → standing E and H (phasor and real
  forms), nodes/antinodes, E and H in time quadrature, ⟨S⟩ = 0, energy sloshing; J_s = n̂×H on the mirror; partial
  reflection (|Γ| < 1): travelling + standing mix, the notes' treatment of |Ẽ| maxima/minima if any (do not invent
  VSWR if the notes do not have it — that is Lecture 36); radiation pressure / force on the mirror (from J_s × B or
  momentum flux, as the notes do), with numbers (sunlight, laser). Whatever else the notes contain.
- **L27 Guided TEM waves on TL systems** — plates inserted into a plane wave → parallel-plate line; V and I from E and H;
  telegrapher's equations from the fields (and from the distributed-circuit model if the notes give it); 𝓛, 𝓒 per
  length (link Lecture 15 §5 and Lecture 10), v = 1/√(𝓛𝓒), Z₀ = √(𝓛/𝓒); d'Alembert solutions V = f(t − z/v) +
  g(t + z/v), I = (f − g)/Z₀; coax and other geometries as the notes give them; power on a line. Stop before
  terminations/reflections at loads if the notes put those in L28.
- **L28 Distributed circuits and bounce diagrams** — generator with Thévenin source and R_g, load R_L; injection
  V⁺ = f·Z₀/(R_g + Z₀); load and generator reflection coefficients Γ = (R − Z₀)/(R + Z₀); the bounce diagram
  (z–t plane), V(z,t) and I(z,t) at a point, steady state as t → ∞ (DC limit check); open/short/matched cases; as the
  notes do it.
- **L29 Bounce diagram examples** — the notes' worked examples (e.g. sinusoidal-burst and pulse excitations, impulse
  response, the 900 m line), each re-worked with the site's figures; reading V(z,t) and I(z,t) off the diagram;
  no new theory beyond what L28 sets up (link it).
- **L30 Multi-line circuits** — junctions between lines of different Z₀ (and loads in parallel at a junction):
  reflection and transmission coefficients at the junction (Γ = (Z_eff − Z₀)/(Z_eff + Z₀), τ = 1 + Γ), bounce diagrams
  across two lines, the notes' examples. Stop before sinusoidal steady state (Lecture 31).

## Your files (only these)
| L | lecture page (replace the stub) | figures module, prefix | concept pages | worked problem | verify script |
|---|---|---|---|---|---|
| 26 | `3-maxwell-and-waves/26-standing-waves-and-radiation-pressure.md` | `figs_l26.py`, `stand-` | **new** `concepts/standing-waves.md`, `concepts/radiation-pressure.md` | `problems/<slug>.md` | `digest10/verify_L26.py` |
| 27 | `4-transmission-lines/27-guided-tem-waves-on-transmission-lines.md` | `figs_l27.py`, `tl-` | **new** `concepts/telegraphers-equations.md`, `concepts/characteristic-impedance.md` | `problems/<slug>.md` | `digest10/verify_L27.py` |
| 28 | `4-transmission-lines/28-distributed-circuits-and-bounce-diagrams.md` | `figs_l28.py`, `bounce-` | **new** `concepts/bounce-diagram.md` | `problems/<slug>.md` | `digest10/verify_L28.py` |
| 29 | `4-transmission-lines/29-bounce-diagram-examples.md` | `figs_l29.py`, `bex-` | none | `problems/<slug>.md` | `digest10/verify_L29.py` |
| 30 | `4-transmission-lines/30-multi-line-circuits.md` | `figs_l30.py`, `mline-` | none | `problems/<slug>.md` | `digest10/verify_L30.py` |

Stubs exist for every page above. Use `#anchors` only into pages that were already written before you started (not
into another writer's new page). Also write `digest10/COVERAGE-LNN.md` (every notes item → section, or why omitted) and
`digest10/ERRATA-LNN.md` (slips in the notes, page + one-line correction, verified by script where numeric).
Worked problem: one, modelled on a past-exam problem from the catalogue if one fits (re-parameterized: new numbers and
at least one changed detail; never copy a key) or a classic problem.
For L27–30 the folder is `4-transmission-lines/` and the tags are `[lecture, transmission-lines]`.

## Concision (the student's request — follow strictly)
- **Lecture page ≤ 3,000 words by `wc -w` (math included); concept pages ≤ 500; worked problem ≤ 900.**
- One idea per sentence. No preambles ("In this section…", "Let us now…"), no restating what an equation already
  says, no "note that"/"it is worth noting", no rhetorical questions as section openers, no motivational filler.
- Equations and short bullet lists carry results; prose only for reasoning that is not in the equations.
- Each fact once per page. Do not re-teach earlier lectures — link them (`[[…|Lecture 21]]`).
- In one breath ≤ 100 words. Traps: bullets, ≤ 2 lines each. On exams callout ≤ 120 words, methods not keys.
- Examples: the notes' examples, plus at most one site example per section, each ≤ 120 words.
- Long derivations folded (`> [!derivation]- …`).
- `### Sources for this page` ≤ 100 words: notes pages, Rao sections, what is the site's own; slips go on
  `ERRATA-LNN.md` (they will be moved to the errata page) and get one line in Sources.

## Rules
- Front matter: keep the stub's title; `description` 1–2 sentences; `tags: [lecture, waves]` (L27–30: `[lecture, transmission-lines]`); `lecture: NN`.
  Header line in italics exactly like Lecture 25's (`*Lecture NN · course notes §NN (no slides) · prev: … · next: … · worked problem: …*`) with prev/next links (prev = previous lecture page; next = next lecture page — all of 26–30 exist as stubs; L30's next = "Lecture 31, periodic oscillations in lossless TL circuits (coming)"). Then `> [!abstract] In one breath`,
  numbered `## N.` sections, `## N. Summary`, a concept-links line, `> [!exam] On exams`, `### Sources for this page`.
- Callouts: key / recipe / trap / exam / intuition / derivation / example / abstract. No nested callouts. Every
  line inside a callout starts with `> ` (including `> $$`).
- Notation: bold vectors `\mathbf{E}`; hats; `\epsilon_0`, `\mu_0` (never `\varepsilon`, never `\vec`); `\eta`;
  phasors with tilde `\tilde{\mathbf{E}}`; `j`; conjugate `^*`; `\langle\cdot\rangle`; units after results;
  boundary conditions with subscripts 1/2 and $\hat n$ from medium 2 into medium 1. Use site notation and say once
  what the notes write if different.
- KaTeX only; `gathered`/`aligned` for multi-line display math; phone-width lines; `\|` in tables, `\lvert\rvert`;
  no unicode inside `$…$`.
- Full-path wikilinks; link only to existing pages; explicit back-links (line Γ ↔ wave Γ of Lecture 25; Z₀ ↔ η; 𝓛, 𝓒 ↔ Lecture 15; standing wave ↔ Lecture 25's
  PEC limit; V, I waves ↔ d'Alembert of Lecture 18).
- Your own words and drawings; notes' examples may be presented with their numbers.
- Do not open any Fall 2026 homework files.
- Verify every number, sign and direction with your script (numpy/scipy; no sympy); save `.out`. L26: standing-wave
  fields satisfy the boundary condition and Maxwell's curl equations numerically; ⟨S⟩ = 0; pressure numbers. L27:
  telegrapher's equations by finite differences; 𝓛𝓒 = με. L28–30: **simulate every bounce diagram** with an
  independent time-stepping of the lines (e.g. FDTD of the telegrapher's equations, or exact lattice bookkeeping)
  and compare V(z,t), I(z,t) at the points the page quotes, and the t → ∞ DC limit.

## Figures (2–4, compact)
- Module `/home/claude/work/figs_lNN.py` starting `from figs import *` and `from figs import _odot, _otimes, _sub, _tint`,
  ending with `if __name__ == "__main__":` calling your figure functions (writes `/home/claude/work/figs/<name>.html`).
  Insert with `<!-- fig:prefix-… -->` on its own line with blank lines around. Captions ≤ 50 words.
- `currentColor` and `var(--accent)`, `var(--accent2)`, `var(--hi)`, `var(--muted)`; escape `<`/`>` in SVG text;
  plots computed with numpy; arrow directions checked by explicit cross products (comment which).
- Visual check (required): `cd /home/claude/work && python3 -c "import assemble; assemble.DST='/home/claude/work/preview/yNN/content'; assemble.main()"`,
  `node preview/preview.mjs preview/yNN/content preview/yNN/out && cp -r preview/out8/fonts preview/out8/katex.min.css preview/preview.css preview/yNN/out/`,
  then screenshot your page and figures light + dark with playwright (model `/home/claude/work/preview/shots8.py`)
  and look at them.

## Checks before you finish
- `python3 /home/claude/work/check.py /home/claude/work/content-src /home/claude/.npm-global/lib/node_modules/markdownlint-cli2/node_modules/katex/dist/katex.min.js`
  must print OK (others edit their own files in parallel; ignore errors in files not yours).
- `wc -w` of your files within the limits above.
- Do not run `practice/build_practice.py --write`; do not run `assemble.py` without the private DST.
- Final message ≤ 20 lines: files, word counts, figures, worked problem (modelled on which exam), what the verify
  script checks, notes slips, doubts.
