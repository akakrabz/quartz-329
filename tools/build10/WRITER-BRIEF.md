# Brief for the Lecture 24–25 page writers (ECE 329 study site, build 9)

You write teaching notes for a Quartz 5 study site for UIUC ECE 329 "Fields and Waves I", from the course notes
(Kudeki) only — the student attends lecture and asked that pages follow the notes. Physics correctness of every
equation, sign, direction and number is paramount. **New this build: the student finds the existing pages too
verbose. Write tight.** (Rules in "Concision" below — they override any longer habit you see in the exemplars.)

## Read first
1. Your lecture's notes: `/mnt/user-data/uploads/ECE 329/Notes/329lectNN.pdf`. Page renders already exist in
   `/home/claude/work/digest9/imgNN/p-*.png` — **look at every page image** (margin equations and figures carry
   content); `digest9/lectNN.txt` is the garbled text layer. Glance at the neighbouring lectures' first pages
   (`digest9/img26/`, `digest8/img23/`) for boundaries.
2. Style/notation exemplar (read fully, but note it is longer than you should be): the Lecture 16 page
   `/home/claude/work/content-src/3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations.md`
   (good length) and the Lecture 21 page `.../21-monochromatic-waves-and-phasor-notation.md` (phasor notation you
   must match — but it is ~2.5× too long). Skim `concepts/phasors.md` and one worked problem
   (`problems/decoding-a-damped-wave.md`).
3. Conventions: `/home/claude/stage/SITE-STATUS.md`, "Conventions".
4. Rao text `/home/claude/work/sources/txt/rao.txt` for cross-checks (grep "group velocity", "polarization",
   "circular", "reflection coefficient", "transmission coefficient", "normal incidence").
5. Past exams: `/home/claude/stage/EXAM-CATALOGUE.md` Part 2 (Exam 3 papers): its index lists L24 (all polarization
   items) and L25 (reflection) problems. Scans as PNG: `/home/claude/work/sources/img/<stem>-N.png`.
6. Figure helpers: `/home/claude/work/figs.py` lines 1–86 and 1083–1120; model module `/home/claude/work/figs_l21.py`.

## Division of material
- **L24 Signal transmission, circular polarization** — narrowband AM signal m(t)cos ωt in a non-dispersive medium
  (travels undistorted); in a dispersive medium the envelope travels at the group velocity v_g = dω/dβ while the
  carrier phase travels at v_p = ω/β (the notes' derivation via a Taylor expansion of β(ω) about the carrier);
  v_g for the notes' dispersion relations (plasma: v_p v_g = c²); then polarization: linear, circular, elliptical
  from two perpendicular components with a phase difference; how to tell right/left-handed (state the notes'
  convention exactly and say the IEEE/optics conventions differ only if the notes do); time-average power of a
  circularly polarized wave; whatever else the notes contain. Link back to L21 (phasors, dispersion relation).
- **L25 Wave reflection and transmission** — normal incidence on a planar interface z = 0, region 1 lossless,
  region 2 with μ₂, ε₂, σ₂: incident, reflected, transmitted phasors; boundary conditions → Γ = (η₂ − η₁)/(η₂ + η₁),
  τ = 1 + Γ = 2η₂/(η₂ + η₁) (use the notes' symbols, say once if they differ from the site's); power balance
  (⟨S⟩ incident = reflected + transmitted, with the η's); the σ₂ → ∞ (perfect conductor) limit Γ = −1 and the
  surface current; whatever else the notes contain. The total field in region 1 as a standing wave and radiation
  pressure are **Lecture 26** — mention in one line and stop.

## Your files (only these)
| L | lecture page (replace the stub) | figures module, prefix | concept pages | worked problem | verify script |
|---|---|---|---|---|---|
| 24 | `3-maxwell-and-waves/24-signal-transmission-and-circular-polarization.md` | `figs_l24.py`, `pol-` | **new** `concepts/group-velocity.md`, `concepts/wave-polarization.md` | `problems/<slug>.md` | `digest9/verify_L24.py` |
| 25 | `3-maxwell-and-waves/25-wave-reflection-and-transmission.md` | `figs_l25.py`, `refl-` | **new** `concepts/reflection-and-transmission.md` | `problems/<slug>.md` | `digest9/verify_L25.py` |

Stubs exist. Also write `digest9/COVERAGE-LNN.md` (every notes item → section, or why omitted) and
`digest9/ERRATA-LNN.md` (slips in the notes, page + one-line correction, verified by script where numeric).
Worked problem: one, modelled on a past-exam problem from the catalogue if one fits (re-parameterized: new numbers
and at least one changed detail; never copy a key).

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
- Front matter: keep the stub's title; `description` 1–2 sentences; `tags: [lecture, waves]`; `lecture: NN`.
  Header line in italics like Lecture 23's: course notes §NN · prev/next links (prev = previous lecture page;
  next for L25 = "Lecture 26, standing waves and radiation pressure (coming)"). Then `> [!abstract] In one breath`,
  numbered `## N.` sections, `## N. Summary`, a concept-links line, `> [!exam] On exams`, `### Sources for this page`.
- Callouts: key / recipe / trap / exam / intuition / derivation / example / abstract. No nested callouts. Every
  line inside a callout starts with `> ` (including `> $$`).
- Notation: bold vectors `\mathbf{E}`; hats; `\epsilon_0`, `\mu_0` (never `\varepsilon`, never `\vec`); `\eta`;
  phasors with tilde `\tilde{\mathbf{E}}`; `j`; conjugate `^*`; `\langle\cdot\rangle`; units after results;
  boundary conditions with subscripts 1/2 and $\hat n$ from medium 2 into medium 1. Use site notation and say once
  what the notes write if different.
- KaTeX only; `gathered`/`aligned` for multi-line display math; phone-width lines; `\|` in tables, `\lvert\rvert`;
  no unicode inside `$…$`.
- Full-path wikilinks; link only to existing pages; explicit back-links (Γ ↔ boundary conditions of Lecture 16/6;
  v_g ↔ dispersion relation of Lecture 21; polarization ↔ ⟨S⟩ of perpendicular components in Lecture 20/21).
- Your own words and drawings; notes' examples may be presented with their numbers.
- Do not open any Fall 2026 homework files.
- Verify every number, sign and direction with your script (numpy/scipy; no sympy); save `.out`. For L24: rotate
  the field vector numerically over a period to fix handedness; group delay of a simulated AM pulse through a
  dispersive medium vs dω/dβ. For L25: boundary conditions satisfied numerically, power balance, PEC limit.

## Figures (2–4, compact)
- Module `/home/claude/work/figs_lNN.py` starting `from figs import *` and `from figs import _odot, _otimes, _sub, _tint`,
  ending with `if __name__ == "__main__":` calling your figure functions (writes `/home/claude/work/figs/<name>.html`).
  Insert with `<!-- fig:prefix-… -->` on its own line with blank lines around. Captions ≤ 50 words.
- `currentColor` and `var(--accent)`, `var(--accent2)`, `var(--hi)`, `var(--muted)`; escape `<`/`>` in SVG text;
  plots computed with numpy; arrow directions checked by explicit cross products (comment which).
- Visual check (required): `cd /home/claude/work && python3 -c "import assemble; assemble.DST='/home/claude/work/preview/xNN/content'; assemble.main()"`,
  `node preview/preview.mjs preview/xNN/content preview/xNN/out && cp -r preview/out8/fonts preview/out8/katex.min.css preview/preview.css preview/xNN/out/`,
  then screenshot your page and figures light + dark with playwright (model `/home/claude/work/preview/shots8.py`)
  and look at them.

## Checks before you finish
- `python3 /home/claude/work/check.py /home/claude/work/content-src /home/claude/.npm-global/lib/node_modules/markdownlint-cli2/node_modules/katex/dist/katex.min.js`
  must print OK (others edit their own files in parallel; ignore errors in files not yours).
- `wc -w` of your files within the limits above.
- Do not run `practice/build_practice.py --write`; do not run `assemble.py` without the private DST.
- Final message ≤ 20 lines: files, word counts, figures, worked problem (modelled on which exam), what the verify
  script checks, notes slips, doubts.
