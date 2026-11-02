# Integrating the Lecture 20–29 slides into the ECE 329 site (build 13)

The student uploaded the course's lecture slides (instructor Shao) for Lectures 20–29 — annotated with the in-class
ink where available. The site's Lecture 20–29 pages were written from Kudeki's course notes alone ("slides: not yet
available"). Your job: **add what the slides contribute that the site does not already have**, as small, targeted edits.
This is **not** a rewrite. The student's words: "Integrate some of the content on these slides, whatever might be
useful. This shouldn't be an entire site rewrite, just some editing and additions."

## Files
- Slides: `/home/claude/lect/pdf/ann-<deck>.pdf` (annotated, in-class ink) and `blank-<deck>.pdf` (no ink). Text layer:
  `/home/claude/lect/txt/<same>.txt` (pages separated by form feeds). Use the **annotated** deck when it exists
  (L27 and L29 exist only blank). Ink matters: render the pages you need, e.g.
  `pdftoppm -r 110 -png -f 7 -l 7 /home/claude/lect/pdf/ann-Lect20-Poynting.pdf /tmp/claude-0/-home-claude/770cd07e-d432-56ac-9487-eb6a1bddcb01/scratchpad/<you>-p` and Read the PNG.
  Read every page of your decks once (text layer first; render a page whenever it has ink, a figure, or math the
  text layer garbles). Ink-heavy pages (annotated vs blank difference): see `/home/claude/lect/INK.txt`.
- Site (working copy — edit here): `/home/claude/site13/content/`. Pages have figures **inlined** as
  `<figure class="ece-fig">…</figure>` raw-HTML blocks — never edit inside them. Never edit the generated
  `**Practice.** …` lines or the `> [!tip] Practice this lecture` boxes. Unmodified snapshot: `/home/claude/site13/content-pre/`.
- Conventions: `/home/claude/lect/SITE-STATUS.md` ("Conventions" section). Topic-page template and lecture-map rules:
  `/home/claude/lect/RESTRUCTURE-BRIEF.md`. Errata table format: `0-toolkit/04-errata-in-the-course-materials.md`.

## What counts as useful (add) vs not (skip)
Add:
1. **Slide examples and in-class worked problems** with their numbers (the inked solutions): as
   `> [!example] Slides, Lecture <deck> (slide N) — <short title>` callouts in the topic page's **Examples** part, paraphrased,
   result stated, any step the ink shows that the site lacks. If the site already has the same example from the notes, add
   one line ("also slides 21–22a, slide 19") instead of a duplicate.
2. **The instructor's emphasis**: boxed/circled results, "a question we may ask on an exam" slides, challenge questions
   (state the question and the answer the ink gives, or the method if no ink), and any summary-slide point the site lacks →
   into the page's `> [!exam] On exams` box or a trap, briefly.
3. **Notation/convention differences** between slides and site (e.g. â_z vs ẑ, a different sign or reference direction,
   a different symbol for the same thing): one line, where a student would trip over it.
4. **Slide slips** (wrong sign, missing factor, inconsistent plot): do NOT edit the errata page; append rows to
   `/home/claude/lect/handoff/errata-<you>.md` in the errata table's column format (`| L<deck> slide N | as written |
   should be | why it matters |`), each verified by script.
Skip: anything the site already states; generic slide text; reproducing slide figures (describe in words if needed); long
derivations already folded on the topic page.

## Where to write
- **Topic pages you own** (list in your task): additions go in the template's places (Physics / Examples / traps / exam).
  Keep each page's total addition ≤ ~300 words; tighten nearby prose if a page would balloon. Keep "Where it appears"
  correct (add the slide deck if useful: "slides 22b–23, slides 19–23").
- **Lecture pages you own**:
  - Lectures 20–26 are *maps*: change the header line's `**slides: not yet available — this page is built from the course
    notes**` / `(no slides)` to name the deck, e.g. `slides "Lectures 21–22a" (annotated, Oct 14)`; in sections where the
    slides add an example or emphasis, add **one** line (`Slides 21–22a, slides 15–18: … → [[concepts/…#…|…]]`); add the
    deck to `### Sources for this page` (one line: deck name, slide count, what was used). Keep each map ≤ 950 words.
  - Lectures 27–29 are full lecture pages: same header/Sources change; put slide examples in the relevant section (as
    `> [!example] Slides … ` callouts) or on the concept page, whichever the page's structure suggests. Lecture 30 has no slides.
- The slides split lectures differently from the notes (e.g. "21–22a" = fields in materials + a current sheet in a material
  + phasor solution). Map content by topic, not by lecture number.

## Quality rules
- Every number you add is computed in `/home/claude/lect/checks/<you>.py` (numpy; `PASS`/`FAIL` lines; run it, all PASS).
  Directions by `np.cross`.
- Site notation: bold vectors, hats (x̂ not â_x), ε₀, phasors with tilde and j, n̂ from medium 2 into 1, the site's line
  conventions (L28 box). KaTeX strict: no unicode inside `$…$` (write `\epsilon`, `\eta`, `\lvert\cdot\rvert`); `$$` on
  their own lines (`> ` prefix inside callouts); full-path wikilinks to existing pages; anchors that exist.
- Paraphrase slide prose; equations and numbers may be reproduced. Concise: no filler, no restating what the page says.
- Run `python3 /home/claude/work/check.py /home/claude/site13/content /opt/npm-tools/node_modules/katex/dist/katex.min.js`
  at the end (must print `OK`; errors in files you do not own are not yours — say so).
- Do not touch files you do not own. Other agents edit other topic pages concurrently.

## Final message (≤ 15 lines)
Per page: what was added (slide numbers), words before → after; errata rows written; check results; anything unclear in
the slides you could not resolve (with slide number).
