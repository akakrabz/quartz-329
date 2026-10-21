# Independent review of a Lecture 26–30 page set (ECE 329 study site, build 11) — reviewer instructions

Someone else wrote one lecture's pages for a Quartz study site for UIUC ECE 329 "Fields and Waves I": the
lecture page, its new/extended concept pages, one worked problem and 3–5 SVG figures. The student is behind
and will trust every equation, sign and number. **Find every error, ambiguity and gap, and fix it with minimal
edits.** There were no slides for these lectures; the pages were built from the course notes (Kudeki), the
course textbook (Rao) for cross-checks, and past-exam catalogues.

## Your files (the writer's; you may edit them)
For lecture NN (given in your prompt): `/home/claude/work/content-src/3-maxwell-and-waves/NN-*.md` or `/home/claude/work/content-src/4-transmission-lines/NN-*.md`, the concept
pages and worked problem listed in `/home/claude/work/digest10/WRITER-BRIEF.md` ("Your files" table; the
worked-problem file is the newest file in `content-src/problems/` that the lecture page links to), the figure
module `/home/claude/work/figs_lNN.py` (figures in `/home/claude/work/figs/<prefix>-*.html`). Also read the
writer's `digest10/COVERAGE-LNN.md` and `digest10/ERRATA-LNN.md`. **Do not read the writer's
`digest10/verify_LNN.py` until your own verification is done** — yours must be independent.

## Sources to check against
- The course notes `/mnt/user-data/uploads/ECE 329/Notes/329lectNN.pdf` — view the page renders in
  `/home/claude/work/digest10/imgNN/` (or render with `pdftoppm -r 110 -png`). Check the coverage map item by item:
  is anything in the notes missing from the page, or misrepresented?
- Rao text `/home/claude/work/sources/txt/rao.txt` for cross-checks of formulas and handbook values.
- Past exams: `/home/claude/stage/EXAM-CATALOGUE.md` (Part 2: Exam 3 papers).
  The `On exams` callout must describe methods, not reproduce answer keys; the worked problem must be
  re-parameterized (new numbers and at least one changed detail) — compare it with the exam scans in
  `/home/claude/work/sources/img/` to make sure no key carries over.
- Neighbouring lecture pages (24–30) for consistency of notation and of the division of material
  (WRITER-BRIEF "Division of material"), and the site conventions in `/home/claude/stage/SITE-STATUS.md`.

## Procedure
1. Read the lecture page, its concept pages and the worked problem in full.
2. **Re-derive every equation and recompute every number** in a script of your own,
   `/home/claude/work/digest10/review_LNN.py` (numpy/scipy; no sympy) with output `review_LNN.out`:
   closed forms checked numerically (finite differences of fields against Maxwell's equations, quadrature
   for time averages against ½Re{ÃB̃*}, `np.cross` for every direction, exact complex γ and η against every
   approximation quoted, every material value against a handbook value you state). Print PASS/FAIL per item.
3. Check physics and teaching: signs and directions (E×H along the travel; H = k̂×E/η; the sheet formulas
   E = −(η/2)J_s(t−|ξ|/v), H = ½J_s(t−|ξ|/v)×n̂ with n̂ toward the field point), time-average factors of ½,
   e^{−αz} for fields vs e^{−2αz} for power, phase of η and which field lags, regime conditions with the
   medium's own ε, scope (L20: no phasors; L21: lossless only), claims that are true only approximately
   stated as such, and anything misleading. Check that every figure agrees with the text (look at it: render
   the figure HTML to PNG with playwright, light and dark; check labels, arrows, curves computed from formulas).
4. Check notation and formatting rules (WRITER-BRIEF "Rules"), and run
   `python3 /home/claude/work/check.py /home/claude/work/content-src /home/claude/.npm-global/lib/node_modules/markdownlint-cli2/node_modules/katex/dist/katex.min.js`
   (must print OK; errors in other lectures' files are not yours).
5. **Fix** everything you find with minimal edits (keep structure and voice). Severity: **blocker** = wrong
   equation, number, sign, direction or unit; a figure that contradicts the text; a copied exam key;
   **major** = misleading or incomplete reasoning, scope violation, missing notes content, a claim stated as
   exact that is approximate; **minor** = wording, typos, formatting. Fix all blockers and majors; minors when
   quick. Re-run figure modules you change (`python3 /home/claude/work/figs_lNN.py`) and your script.
6. Write `/home/claude/work/digest10/REVIEW-LNN.md` (≤ 60 lines): a findings table (severity, where, what, fix),
   coverage verdict, anything unresolved.
7. Final message (≤ 12 lines): counts of blockers/majors/minors found and fixed, open concerns.

Other agents are working at the same time: practice-problem writers read (but do not edit) your lecture page;
the other three reviewers edit only their own lecture's files. Edit only your lecture's files.

## Build 11 additions
- Concision limits from `digest10/WRITER-BRIEF.md` ("Concision": lecture ≤ 3,000 words by `wc -w`, concept ≤ 500, worked
  problem ≤ 900); cut padding you find while fixing.
- L26: check the standing-wave fields against the PEC boundary condition and the curl equations numerically; ⟨S⟩ = 0;
  J_s on the mirror by n̂ × H; radiation-pressure numbers against a handbook solar constant.
- L27: 𝓛, 𝓒, v, Z₀ for every geometry quoted (𝓛𝓒 = με for a homogeneous filling); telegrapher's equations by finite
  differences; the direction convention for I.
- L28–30: **re-simulate every bounce diagram independently** (FDTD of the telegrapher's equations or exact wave
  bookkeeping) and compare V(z,t), I(z,t) at every quoted point/time and the t → ∞ DC limit; check that L29 and L30 use
  the L28 page's conventions (generator end, z direction, Γ_L, Γ_g, sign of I) — report any mismatch between pages to the
  coordinator in your final message rather than editing another lecture's page.
