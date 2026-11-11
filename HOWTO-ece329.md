# ECE 329 notes site — how to build, preview, and host

This folder is a **Quartz 5** site (`quartz.config.yaml`, `quartz.ts`, `content/`, `quartz/static/demos/`, `quartz/styles/custom.scss`).
The notes are plain Markdown with Obsidian-style wikilinks and callouts, so the `content/` folder also opens directly as an Obsidian vault.

## 1. Build and preview (first time)

Requirements: Node ≥ 22, npm ≥ 10.9 (you have Node 22.23), internet access for the two install steps.

```bash
cd "~/Nextcloud/Notes/ECE 329/quartz"
npm ci                        # Quartz's own dependencies
npx quartz plugin install     # clones + builds the @quartz-community plugins listed in quartz.config.yaml
npx quartz build --serve      # http://localhost:8080  (rebuilds on save)
```

`npx quartz build` alone writes the static site to `public/`.

If the plugin step complains about a plugin failing to build on a fresh clone, run `npx quartz plugin install --latest` (it rewrites `quartz.lock.json`).

## 2. Before hosting

Edit `quartz.config.yaml` → `configuration.baseUrl` (currently `CHANGE-ME.example.com/ece329`): your host plus any sub-path, no protocol, no trailing slash. It only affects the sitemap and social-preview URLs, but set it.

If the site lives under a sub-path (e.g. `example.com/ece329/`), build with `npx quartz build --baseDir /ece329`.

## 3. Hosting: the one rule your server needs

Quartz emits `page.html` files but links to them **without** the extension (`/concepts/gauss-law`), and folders are served with a trailing slash. Your web server must try `$uri`, then `$uri.html`, then `$uri/`:

```nginx
# nginx
location / {
    try_files $uri $uri.html $uri/ =404;
}
error_page 404 /404.html;
```

```caddyfile
# Caddy
try_files {path} {path}.html {path}/ =404
```

Apache: `Options -MultiViews` plus `RewriteEngine On; RewriteCond %{REQUEST_FILENAME}.html -f; RewriteRule ^(.*)$ $1.html [L]`.

Copy `public/` to the web root (or the sub-path). Opening `public/index.html` directly from disk (file://) does not work — search, graph and page previews fetch JSON over HTTP.

External requests the site makes at page load: Google Fonts (theme fonts) and jsdelivr (KaTeX CSS, loaded by the latex plugin). Analytics are disabled. To go fully self-hosted later, set `theme.fontOrigin: local` and vendor the KaTeX CSS.

## 4. Writing conventions (so new pages match)

- One page per lecture in `content/<unit>/NN-slug.md`; frontmatter `title`, `description`, `tags`, `lecture`.
- Concept pages in `content/concepts/`, problems in `content/problems/`, demos in `content/demos/`.
- Past-exam guides in `content/exams/` (build 14): they say what each part asks and how to do it, link to twins, and never reproduce a paper or its key; key slips go on the errata page.
- Link with full paths: `[[concepts/gauss-law|Gauss's law]]`, `[[1-electrostatics/03-gauss-law-at-work#3-the-three-symmetries|Lecture 3 §3]]`. Inside tables escape the pipe: `[[page\|text]]`.
- Math: `$…$` inline, `$$…$$` on its own lines (every line prefixed with `> ` inside a callout). Use `\lvert x\rvert` instead of `|x|` inside tables. No custom macros — the vault must also render in Obsidian.
- Callouts: the standard Obsidian types plus this site's own `key`, `recipe`, `trap`, `exam`, `intuition`, `derivation` (styled in `quartz/styles/custom.scss`). Append `-` to the type to fold by default.
- Figures: inline `<figure class="ece-fig">…SVG…</figure>` blocks with **no blank lines inside**; strokes use `currentColor` and the CSS variables `--accent`, `--accent2`, `--hi`, `--muted` so they follow dark mode. The generator for the existing figures is in `tools/figs.py`.
- Demos: standalone HTML in `quartz/static/demos/<name>/index.html`, embedded with `<iframe src="/static/demos/<name>/">` inside `<div class="ece-demo">`.
- Explorer order comes from file names (numeric prefixes), see `quartz.ts`; titles stay clean.
- Practice pages (`content/practice/NN-*.md`) follow a fixed problem-block format so the hub and the difficulty/topic lists can be generated from them — see §7.

## 5. Checking a page without building

`tools/check.py` (Python 3, needs PyYAML and the local KaTeX copy path set at the top) validates every wikilink and heading anchor and compiles every equation with KaTeX in strict mode — the same checks run before this delivery. `tools/assemble.py` inlines figures from `tools/figs/` into pages that contain `<!-- fig:name -->` markers, if you keep the figures separate.

`tools/practice/build_practice.py` validates the practice pages (numbering, difficulty order, callout sequence, counts in the description, topic tags) and, with `--write`, regenerates the practice hub, the easy/medium/hard and topic lists, and the practice links on lecture, unit and concept pages (§7).

## 6. What's here (build 14, 2026-11-11 — Midterm 3 review + Lectures 31–33 + the Lecture 27–32 slide decks; organized by topic; Lectures 1–33 + practice bank + Midterm 2 and 3 summaries + PrairieLearn guide)

- **Build 14 (Midterm 3, exam November 16):**
  - **Scope and framing.** The announcement says the exam covers Lectures 1–30 and Homeworks 1–11, with no Smith chart; one 4″×6″ card, closed book, no calculators. It gives no weighting. The student, who is in the class, expects it to be **mostly post-Midterm 2 material (Lectures 21–30, HW8–HW11)**, and the four Spring/Fall Exam 3 papers in the folder are all post-Midterm 2 material. The pages keep these two statements separate: the announcement is quoted verbatim, the expectation is attributed to the student and the past papers, and Lectures 1–20 are treated as background the new problems rely on. Lectures 31–33 are after the scope: their pages stay, each marked "not on FA26 Midterm 3".
  - **`content/exams/`** (new folder): `index.md` is the Midterm 3 review hub — the announcement quoted and "what to expect" beside it, where each item of its study hint lives on the site, the past-paper tables (with the points on Lectures 31–34 labelled as outside this exam), which papers to work timed, the ten recurring Lecture 21–30 problem types with method pages and twins, and a short table of the earlier tools those problems use. One guide per paper (`e3-fa23`, `e3-sp19`, `e3-sp18`, `e3-sp17`: what each part asks, method, traps, twins; the keys are not reproduced; the out-of-scope problem of each carries a note), `e3-summer-hour-exams` (the four Summer papers by type, one worked twin) and `e3-steady-state-lines` (the Lecture 31–33 past-exam type, five worked twins S1–S5; not on Midterm 3).
  - **`0-toolkit/09-midterm-3-summary.md`**: equations of Lectures 21–30 (§1–8); §9, the tools from earlier lectures that these problems use (with Lectures 1–10 in a folded, secondary box); traps; an index card built around Lectures 21–30 with one corner for the earlier formulas; HW8–10 by problem (HW1–4 by set in a folded box, HW5–7 by link); a Wednesday-to-Monday plan with one short slot for the earlier tools; a practice list in the same proportion.
  - **Lectures 31–33** from the course notes, then reconciled with the slide decks: `4-transmission-lines/31-…`, `32-…`, `33-…`, three topic pages (`concepts/line-resonances`, `stub-input-impedance`, `quarter-wave-transformer`), four figures (`tools/figs_l31.py` → `tools/figs/res-*.html`), and practice sets 31–33 with **eight** problems each (4 easy, 2 medium, 2 hard; `EXPECT` in `build_practice.py`), 368 problems in all. No separate worked-problem pages were written for 31–33: the twins S1–S5 serve.
  - **Slides synced November 10–11:** Lecture 30 (annotated through slide 11) added to the Lecture 30 page as *Slides, Lecture 30* callouts (coefficient derivation and power, the splitter challenge, the three-line cascade, the shunt-plus-series junction, time-domain reflectometry). The annotated Lecture 27 and 29 decks confirmed the pages (headers and Sources updated; Lecture 29's Example 3 now uses the sign corrected in class). The decks titled "Lecture 31" and "Lectures 32" split the material differently from the notes (deck 31 = phasors and standing waves on stubs, then the notes' §31 resonances, then a first Smith-chart slide; deck 32 = the notes' §32; their page footers read 32 and 33): each lecture page's header and Sources say which slides it uses. No deck for the notes' §33. The Smith-chart slides wait for Lecture 34. There are no lecture recordings for this course.
  - **Errata:** a new section "Past Exam 3 solution keys" (SP18 #3(d), SP19 #1(d)), six HW9-solution rows, one Lecture 31 notes row, the Lecture 29 slide-14 row updated (corrected in class), one Lecture 30 slide-8 ink row.
  - **Checks** (`tools/build14/checks/`, each with its `.out`): `exam3_keys.py` re-solves the computed parts of all eight Exam 3 papers (83 checks: 81 agree, 2 key slips); `twins.py` + `review_twins.py` (the twins, two routes); `hw9.py` (the HW9 solution set; 6 slips); `hub_counts.py`; `summary3.py`; `L31_33.py` (lecture and topic pages); `slides27_32.py` (everything taken from the new decks, bounce diagrams by simulation); `tlsim.py` is the time-domain line simulator they share. Practice sets: `tools/practice/checks/L31–L33.py` and, independently, `tools/practice/review/R31–R33.py` (eigenmodes of the discretized line, leapfrog FDTD, a lumped ladder, `tlsim`).
  - **Not done:** Lectures 34–38 (Smith chart, VSWR, matching, distribution networks) are still outlined only. **HW11 is in the exam's scope but was not in the course folder**, so it is not mapped; when it arrives, add its rows to the summary's §12 and remove the note on the hub. HW10 is mapped by method only (its solutions were not in the folder). HW1–HW4 are mapped by set, not by problem.
  - No page of build 14 is based on open homework: HW11 and later were never read; HW10 (closed November 5) appears only as one-line methods in the summary's §12.
  - To add another past paper: write `content/exams/e3-<term>.md` on the pattern of `e3-sp19.md`, add its row to the papers table and to `hub_counts.py`, and re-solve it in `exam3_keys.py` first.

- **Build 13:** the Lecture 20–29 slide decks (annotated where available) were integrated into the existing pages as *Slides, Lecture …* callouts and exam notes; brief, ink map, checks and errata hand-offs are in `tools/build13/`.

- **Build 12:** the site is organized by **topic**. 72 topic pages under `content/concepts/` (14 new) carry the teaching content of Lectures 1–26 — key box, Physics, folded derivation, figures, the course's examples, traps, exam notes, "Where it appears", Related, Practice; Lecture pages 1–26 are ≤ 900-word maps that keep their section headings and point to the topic pages. `concepts/index.md` is the themed "Topics" index; the home page leads with it and lists lectures under "By lecture"; unit indexes carry a "Topics in this unit" box. Briefs, the section→topic map, the pre-restructure snapshot and the loss checker are in `tools/build12/` (`cd tools/build12 && python3 loss_check.py L20` checks nothing from the old Lecture 20 page was lost; it was run on the pre-assembly source, so in the repo — where figures are inlined — the `<!-- fig -->` marker lines show as misses and can be ignored). To add material for a lecture ≤ 26: write it on the topic page, add a pointer line to the lecture map; to add a topic page: `concepts/index.md` row + home-page theme line + unit-index box + `CONCEPT_TOPICS` in `tools/practice/build_practice.py`, then `--write`.

- **Build 11:** Lecture 26 (standing waves, radiation pressure) and Unit 4 Lectures 27–30 (TEM lines, bounce diagrams, examples, multi-line circuits) from the course notes, with concept pages, worked problems, figures and practice sets 26–30 (344 problems in all); bounce-diagram numbers checked by independent line simulations (`tools/lecture-checks/`, `tools/practice/review/`). The Unit 4 index is a practice-linked table like the other units' (`4-transmission-lines/index.md` is now in `UNIT_INDEXES`).
- **Build 10:** Lectures 24 (signal transmission, group velocity, polarization) and 25 (reflection and transmission) from the course notes, with concept pages, worked problems, figures and practice sets 24–25 (284 problems in all); every lecture and the longest concept pages tightened (−28 % words overall, structure and equations unchanged — `tools/build10/trim_check.py`); length caps for new pages in `tools/build10/WRITER-BRIEF.md` (Concision).
- Home page with the course map and conventions.
- Toolkit: **Midterm 2 equation summary** (build 7; its scope line now links the Lecture 20–23 summaries), coordinates & differential elements, vector-calculus cheat sheet, units & constants (build 8 adds S, J·E, phasors, β, α in Np/m and dB, γ, δ and the loss tangent), errata in the course materials (Lectures 1–23).
- Unit 1, Lectures 1–11 written in full (1–10 is the Exam 1 scope; 11 is the Lorentz–Drude lecture).
- Unit 2, Lectures 12–15 written in full, with the **electrostatics ↔ magnetostatics dictionary** on the unit page.
- Unit 3, Lectures 16–23 written in full. **New in build 8: Lectures 20–23**, written from the course notes alone because the slides were not yet available (each page's header says so): 20, Poynting's theorem (energy bookkeeping, Joule heating, the resistive wire, time averages, the radiating sheet's energy budget); 21, monochromatic waves and phasors (β, λ, v_p, dispersion relations including the plasma, phasor notation, ⟨S⟩ = ½Re{Ẽ×H̃*}); 22, Maxwell's equations in phasor form and damped waves (γ = α + jβ, complex η, decoding a damped wave); 23, imperfect dielectrics and good conductors (loss tangent, regime formulas, skin depth, seawater and copper). Lectures 24–26 outlined on the index page. Unit 4 outlined.
- 50 concept pages (build 8 added Poynting's theorem, phasors, dispersion relation, propagation constant, loss tangent and skin depth, and extended the Poynting vector, plane waves, intrinsic impedance and the conductivity models); each ends with a **Practice** line pointing at its problems.
- 17 worked problems (build 8: energy bookkeeping for a radiating sheet; phasor E and power from a given H; decoding a damped wave; a radio wave into moist ground) — all re-parameterized from past-exam families.
- **Practice bank** (`content/practice/`): 260 problems for Lectures 2–23 (12 per lecture, 8 for Lecture 11): 109 easy, 65 medium, 86 hard, each with a folded hint and a worked solution, 49 of them modelled on past exams. Build 8 adds the Lecture 20–23 sets and the topics Poynting's theorem and power, phasors, damped waves in conducting media, and good conductors.
- 1 interactive demo (point charges + Gaussian loop); 74 original figures (`tools/figs/`; generated by `tools/figs.py`, and for Lectures 17–23 by `tools/figs_l17.py` … `figs_l30.py`, which import the helpers from `figs.py`).

Every page passes `tools/check.py` (build 14: 197 pages, 5796 wikilinks/anchors, 39382 KaTeX expressions; at build 8 it was 132 pages, 2957 and 29600+). Every practice answer was checked numerically by its author's script (`tools/practice/checks/`) and re-solved from the statement alone by an independent reviewer's script (`tools/practice/review/R*.py`). The Lecture 17–23 pages, figures, concept pages and worked problems were checked by their writers' scripts and then reviewed independently (`tools/lecture-checks/`; for Lectures 20–23 about 1,200 independent checks, all passing after the fixes). The Lecture 20–23 reviews found 1 blocker (a reversed sign in the Lecture 23 energy-balance sentence) and 6 majors (far-field conditions missing on the 1/r antenna formulas; "S swings between 0 and 2⟨S⟩" true only for linear polarization; "β ≥ α in every passive medium", which fails for a collisionless plasma below cutoff; a wrong λ-versus-δ regime test; approximate entries written as equalities in the regime table; a seawater |η| label off by orders of magnitude), all fixed; the practice reviews found no wrong answer (one misleading check line and a dozen minor wording or rounding fixes). For Lecture 19 the review fixed a reversed statement in the slide-11 figure caption and a wrong claim about adding the power flows of counter-propagating waves, removed SP18 Exam 2 answers that had been quoted, and re-parameterized the worked problem so the exam key cannot carry over. For Lectures 17–18: no wrong physics was found; the reviews fixed one rounded number, several misleading or misattributed statements, and flagged slide values that disagree with handbook data (now on the errata page). In the Lecture 16–18 practice sets the review caught one wrong answer line (17.10(c), the jump in tangential **B**) and fixed it.

**Lectures 20–23 without slides.** The pages follow the course notes' numbering and content; Rao's textbook was used for cross-checks and handbook values, and the Exam 3 papers on hand (SP17, SP18, SP19, FA23; Summer 2017–2020 HE3; the Summer 2020 final) for the *On exams* callouts. What is missing is whatever the instructor adds on the slides (their examples, emphasis and in-class ink). When the slides appear, compare them with each page's *Sources* list and add slide examples the same way as for Lectures 16–19.

No page or problem in builds 5–8 is based on FA26 HW6 (open homework when it was written); it was read only to make sure nothing duplicates it.

The course's own canvas demos (`Suppliment/Websites/*.html`, `smithchart.html`) were **not** copied into the public tree: they are saved from the course's login-only site and carry no license. They can be dropped into `quartz/static/demos/course-apps/` for a private build.

## 7. The practice bank: adding or changing problems

Each practice page is `content/practice/NN-slug.md` with frontmatter `title`, `description` (must contain "N practice problems (a easy, b medium, c hard)"), `tags`, `lecture: N`. Problems are numbered `L.1 … L.n`, easy first, then medium, then hard, under `## Easy` / `## Medium` / `## Hard`. Each problem is exactly:

```markdown
### 3.1 Two sheets of charge

> [!easy] Easy · Gauss's law · charge sheets · superposition
> (statement, every quantity with units)
>
> *Source: original.*

> [!hint]- Hint
> (required for medium and hard)

> [!solution]- Solution
> (Setup → Work → Answer → Check)
>
> **Answer.** (final results with units and directions)
```

One to three topic tags after the difficulty word, separated by ` · `. A new tag must be given a topic in `RULES` (or listed in `IGNORE`) at the top of `tools/practice/build_practice.py` — the script refuses to write otherwise. After editing:

```bash
python3 tools/practice/build_practice.py --write   # validate, regenerate hub/lists, refresh the links
python3 tools/check.py content <path/to/katex.min.js>
```

`tools/practice/SPEC.md` is the authoring spec the problems were written to (difficulty rubric, notation, solution style); `REVIEW-SPEC.md` is the independent-verification procedure. Re-parameterize anything taken from an exam (new numbers and at least one changed detail) and never copy a key's text.

