# Content-loss review of trimmed pages (build 9)

Other agents cut the lecture pages listed in your prompt by 33–56 % to make them less verbose (rules they followed:
`/home/claude/work/digest9/TRIM-BRIEF.md`). Pre-trim copies: `/home/claude/work/digest9/pre-trim/content-src/<same path>`.
Your job: make sure nothing a student needs was lost and no meaning changed. Do not undo the trimming.

For each page:
1. Diff old vs new (`diff <(fold -w 200 -s OLD) <(fold -w 200 -s NEW)` or read both side by side, section by section).
2. List every result, example number, sign/direction rule, reason ("why"), trap, exam method and connection that is in
   the old page and **in no form** in the new page. Decide for each: (a) a repeat of something still on the page or a
   linked page → fine; (b) a real loss → restore it in ≤ 1 short sentence/clause/table cell at the right place.
3. Read every rewritten sentence that carries physics: did compression change its meaning (sign, condition,
   "only when", approximation stated as exact, a qualifier dropped)? Fix it.
4. Keep growth small: at most +10 % words per page. Run
   `python3 /home/claude/work/digest9/trim_check.py <old> <new>` (must stay "OK structure kept"; exception: the
   L23 page's header line was edited on purpose — a FAIL there about the header line only is expected).
5. `python3 /home/claude/work/check.py /home/claude/work/content-src /home/claude/.npm-global/lib/node_modules/markdownlint-cli2/node_modules/katex/dist/katex.min.js` must print OK.

Do not touch the `> [!tip] Practice this lecture` box or the header line. Edit only your pages.
Write `/home/claude/work/digest9/LOSS-<pages>.md` (≤ 40 lines: per page, items restored, meaning fixes, judged-fine
repeats worth mentioning). Final message ≤ 10 lines.
