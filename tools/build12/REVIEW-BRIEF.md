# Coherence review of the merged topic pages (build 12)

Five writer batches grew the topic pages under `/home/claude/work/content-src/concepts/` from lecture content (Lectures 1–26) and merged
hand-off blocks written by other batches. You review one theme group for coherence and fix what you find, in place.

Read `/home/claude/work/digest11/RESTRUCTURE-BRIEF.md` (topic-page template) and `/home/claude/work/digest11/TOPIC-MAP.md` (which lecture
sections each page must carry). Pre-restructure lecture pages are in `/home/claude/work/digest11/pre/content-src/` if you need to check
that nothing was lost.

## Check each page of your group for
1. **Duplication** — the same equation, example or trap stated twice (typically once in the original text and once in a merged hand-off).
   Keep the better version; merge attributions ("Lecture 6 §3; Lecture 16 §4").
2. **Order** — template order: key box → Physics → derivation (folded) → figures → Examples → traps → exam → Where it appears → Related →
   Practice (last, generated, untouched). Merged blocks often got appended at the end; move them to where they belong.
3. **Seams** — hand-off text that refers to "this lecture", "above", "§4", or to a figure that is no longer on the page; sentences that
   presuppose context the topic page does not give. Rewrite so the page stands alone.
4. **Consistency** — notation (bold vectors, $\hat n$ from medium 2 into medium 1, phasors with tilde and $j$, $\epsilon_0$), callout types,
   one `> [!key]` at the top, `> [!exam] On exams` once.
5. **Links** — "Where it appears" lists every lecture section the TOPIC-MAP assigns to the page (full-path wikilink with anchor; anchors
   must exist — `grep -n '^## ' <lecture page>`); "Related" links only to existing pages.
6. **Cap** — ≤ 2,000 words by `wc -w`. Four pages are over (loss-tangent 2174, skin-depth 2158, poynting-theorem 2100, phasors 2032):
   bring them under by deduplicating and tightening prose, never by dropping an equation, number, example, trap or figure.
7. **Math** — KaTeX strict: no unicode inside `$…$`, `\lvert\rvert` not `|…|` for absolute values, `\text{}` for words.

Do **not** touch: `**Practice.**` lines, lecture pages, pages outside your group, `practice/`, `assemble.py`. Do not add content that is not
on the pre-restructure lecture pages.

When done run
`python3 /home/claude/work/check.py /home/claude/work/content-src /home/claude/.npm-global/lib/node_modules/markdownlint-cli2/node_modules/katex/dist/katex.min.js`
(must end `OK`; ignore errors in other groups' files only if they are clearly not yours) and, for every lecture whose sections feed your
pages, `python3 /home/claude/work/digest11/loss_check.py L<NN>` (must stay OK; L01 and L06 have one known justified line each).

Final message ≤ 15 lines: pages touched with words before → after, duplicates removed (count), seams fixed, anything you could not resolve.
