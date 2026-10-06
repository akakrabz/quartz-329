# tools/practice — the practice bank's tooling and verification record

- `build_practice.py` — validates `content/practice/NN-*.md` and, with `--write`, regenerates
  `practice/index.md`, `easy.md`, `medium.md`, `hard.md`, `topics.md` and the practice links on the
  lecture pages, the unit index tables and the concept pages. Idempotent; run it after every change.
  Usage: `python3 tools/practice/build_practice.py [--src content] [--write]`.
- `SPEC.md` — the authoring spec the problems were written to (counts, difficulty rubric, block
  format, solution style, notation, sources). Paths inside it refer to the original workspace.
- `REVIEW-SPEC.md` — the independent-verification procedure each page went through.
- `checks/LNN.py` + `.out` — the authors' verification scripts, written with the first drafts.
  Some problems were changed afterwards (8.11 replaced; 4.9, 7.9, 9.10, 10.9, 11.8, 12.10, 13.9,
  14.10, 15.3, 15.10, 16.11, 16.12 re-parameterized; 17.10(c) corrected), so these scripts no longer
  match those problems.
- `review/RNN.py` + `.out` + `.md` — the independent reviewers' scripts and reports: every problem
  re-solved from its statement alone (numpy/scipy), PASS/FAIL against the page's stated values.
  These match the pages as delivered.
- `review/V2-*.py` + `.out` + `.md` — a third, independent check of the problems changed in review.
- `review/CITATIONS-WAVE1.md` — the exam-citation fixes on pages 02–08.

Scripts need Python 3 with numpy and scipy (and PyYAML for build_practice.py).
