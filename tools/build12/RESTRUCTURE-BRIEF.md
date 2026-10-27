# Restructuring the ECE 329 site around topic pages — writer brief (build 12)

The student wants the site organized by **topic**, not by lecture: the teaching content (derivations, the notes' and
slides' examples, traps, exam notes, figures) moves from the lecture pages into the topic pages under `concepts/`, and
each lecture page becomes a thin **map** that keeps its section headings and points to the topic pages. Scope:
Lectures 1–26. Your batch and its lectures/topics are in `/home/claude/work/digest11/TOPIC-MAP.md` — follow its
assignments exactly. Pre-restructure copies of every file are in `/home/claude/work/digest11/pre/content-src/`.

**Nothing may be lost.** Every equation, result, number, example, direction rule, trap, exam method, figure and link
target that is on a lecture page now must end up on its topic page (or, for the few items the map says so, stay on the
lecture page). Dedupe: where the topic page already says the same thing, keep one version (the better one). A script
(`digest11/loss_check.py`) will flag any display-math block, figure marker or number-bearing inline formula from the
old lecture page that appears nowhere in the new lecture page + topic pages.

## Topic page (the new standard; existing concept pages grow into it)
```
---
title: "…"            (keep)
description: "…"      (1–2 sentences)
tags: [concept, <theme tag>]   (keep existing tags; add nothing new)
aliases: [...]        (keep; add aliases for ideas absorbed from the lecture)
---
> [!key] Definition / key result      (keep or write; the boxed equations)

**Physics.** Prose that teaches the idea, absorbed from the lecture section(s) (≤ ~500 words).

> [!derivation]- Title                (long derivations, folded; every step kept)

<!-- fig:… -->                        (figure markers moved from the lecture page, with blank lines around)

**Examples.** The notes'/slides' examples and the site's own, each with its numbers (label which is which, as the
lecture page did; keep "Slide 24:" / "Notes Example 2:" attributions).

> [!trap] …                           (merged traps, ≤ 2 lines each)

> [!exam] On exams                    (the parts of the lecture's exam box that concern this topic; methods, no keys)

**Where it appears.** [[lecture page#section anchor|Lecture N §k]] … (every lecture that treats it), worked problems.
**Related.** concept links.
**Practice.** … (generated line — do not touch; keep it last)
```
Cap **2,000 words by `wc -w`**. If a topic would exceed it, keep the derivation folded and tighten prose; do not drop
content. Concision rules of `digest10/WRITER-BRIEF.md` ("Concision") apply to any prose you write.

## Lecture page (thin map)
Keep: front matter (shorten `description` to one sentence that says what the lecture covers and that the content is on
the topic pages), the italic header line, `> [!abstract] In one breath`, **every `## N. …` heading with its exact
text**, the `## N. Summary` (trim to ≤ 8 bullets), the `> [!tip] Practice this lecture` box (generated — untouched),
`### Sources for this page` (unchanged). Under each section heading write 2–5 lines: what the lecture does there, the
example it uses (named, with its result in a few words), then `→ Full treatment: [[concepts/<slug>#anchor|Topic title]]`
(anchor optional). Keep the `> [!exam] On exams` box, compressed to ≤ 80 words, pointing at the topic pages' exam
notes. Remove figures (they move), derivations, long examples. Target **≤ 900 words** per lecture page.

## Hand-offs (topics you do not own)
When the map says a section's content goes to a topic page owned by another batch, do **not** edit that page. Write
`/home/claude/work/digest11/handoff/<topic-slug>--from-L<NN>.md` containing the content in topic-page form (the
prose, equations, examples, traps, figure markers, exam items) ready to paste, with a first line
`<!-- for concepts/<slug>, from Lecture NN §k -->`. The owner batch merges handoffs addressed to its topics **at the
end of its run** (check the handoff folder before finishing; if a handoff for your topic is not there yet, wait with
`sleep 180` and re-check, up to 30 minutes; merge whatever has arrived and list in your final message any still missing).
On the lecture page, link to the owner's topic page as usual.

## Rules
- Only lecture pages of your batch, topic pages you own (see the ownership summary), handoff files, and new stubs you
  own. New topic stubs exist already (`concepts/<slug>.md` with "Being written."): replace them.
- Links: full-path wikilinks only to pages that exist; anchors only into headings that exist (check with grep).
  Other agents are renaming nothing, so existing anchors on lecture pages stay valid.
- Notation and callout conventions of `/home/claude/stage/SITE-STATUS.md` ("Conventions"). KaTeX strict; no unicode in `$…$`.
- Do not run `practice/build_practice.py --write` or `assemble.py`.
- Check when done: `python3 /home/claude/work/check.py /home/claude/work/content-src /home/claude/.npm-global/lib/node_modules/markdownlint-cli2/node_modules/katex/dist/katex.min.js`
  (OK; ignore errors in other batches' files) and
  `python3 /home/claude/work/digest11/loss_check.py L<NN>` for each of your lectures (must print `OK` or only items you
  can justify as duplicates), and `wc -w` of every file you touched against the caps.
- Final message ≤ 20 lines: lecture pages (words before → after), topic pages created/grown (words), handoffs written
  and merged, loss-check results, anything unresolved.
