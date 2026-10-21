# Brief: tightening existing lecture pages (ECE 329 study site, build 9)

The student says the site's lecture pages are too verbose. Your job: **cut words, not content.** Every equation,
result, number, direction rule, worked example, trap and exam method stays; what goes is repetition, narration and
padding. You edit only the lecture pages assigned in your prompt
(`/home/claude/work/content-src/<unit>/NN-*.md`).

## Targets (by `wc -w` of the file)
- Lectures 17–23 (5,000–8,000 words now): **≤ 3,500 each** (about −45 % or more).
- Lectures 1–16 (1,800–2,900 now): **−15 % to −25 %**; these are already near the right length — cut padding only.

## What to cut
- Preambles and transitions ("In this section we…", "Let us now…", "Recall that…" when a link follows anyway).
- Sentences that restate an equation in words, or restate the previous sentence/section, or the In-one-breath box.
- "Note that", "It is worth noting", "Importantly", "In other words", hedges, rhetorical questions used as openers.
- The same fact taught twice on one page (keep the better place; link or nothing elsewhere).
- Re-teaching of earlier lectures beyond one line + link.
- Over-long examples: keep the setup, the key steps and the numbers; drop narration around them.
- `### Sources for this page`: compress to ≤ 120 words — which notes/slides pages, Rao sections, what is the site's
  own, and one line "Slips in the course material: see [[0-toolkit/04-errata-in-the-course-materials|errata]]"
  **only if** those slips are already on the errata page (check it: `grep -n "Lecture NN" .../04-errata-in-the-course-materials.md`).
  If a slip described in Sources is *not* on the errata page, keep it (one line each).
- Long derivations that are not folded: fold them (`> [!derivation]- Title`), keeping every step.

## What must not change (checked by script)
- Every heading line (`##`, `###`, `####`) — text exactly as is (other pages link to these anchors).
- Every `<!-- fig:… -->` marker, in order.
- Every display-math block `$$…$$` (content unchanged; you may move it, not edit it — unless it is *wrong*, then
  fix it and report it).
- Every wikilink target present now must still appear at least once (duplicates may go).
- The header line (`*Lecture NN · …*`) and the generated `> [!tip] Practice this lecture` callout: do not touch.
- Front matter: keep; you may shorten `description` to ≤ 2 sentences.
- Inline numbers and results: keep all that are results or example data. Do not round differently.
- Callout types and their teaching role (key/recipe/trap/exam): keep; shorten their text.
- Voice and notation as they are.

## Procedure per page
1. Read the whole page. Decide what is repeated or padding.
2. Rewrite section by section (Edit or Write). Keep paragraphs short.
3. Run `python3 /home/claude/work/digest9/trim_check.py /home/claude/work/digest9/pre-trim/content-src/<path> /home/claude/work/content-src/<path>`
   — must print `OK structure kept` and a word count within target. Fix any FAIL.
4. After all your pages: `python3 /home/claude/work/check.py /home/claude/work/content-src /home/claude/.npm-global/lib/node_modules/markdownlint-cli2/node_modules/katex/dist/katex.min.js`
   must print OK (errors in files that are not yours: ignore; other agents edit in parallel).
5. Re-read each finished page once as a student: does every step still follow? Did a cut remove a reason that a
   later sentence relies on? Restore it if so.

Do not edit any other file. Do not run `practice/build_practice.py` or `assemble.py`.
Final message ≤ 12 lines: per page, words before → after, the trim_check result, anything you were unsure about
cutting or any error you found and fixed.
