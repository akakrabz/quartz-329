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

## 6. What's here (build 6, 2026-10-07 — Lectures 1–19 + practice bank)

- Home page with the course map and conventions.
- Toolkit: coordinates & differential elements, vector-calculus cheat sheet, units & constants (now with M, m, χm/μr, v and η), errata in the course materials (Lectures 1–19).
- Unit 1, Lectures 1–11 written in full (1–10 is the Exam 1 scope; 11 is the Lorentz–Drude lecture).
- Unit 2, Lectures 12–15 written in full, with the **electrostatics ↔ magnetostatics dictionary** on the unit page.
- Unit 3, Lectures 16–19 written in full (build 5: 17, magnetization current and Maxwell's equations in matter; 18, the wave equation and plane TEM waves; **new in build 6: 19**, d'Alembert solutions and radiation from current sheets — the sheet's fields both ways, cosine currents with β, λ, v_p, and the instantaneous Poynting vector); Lectures 20–26 outlined on the index page. Unit 4 outlined.
- 44 concept pages (build 6 added current-sheet radiation and the Poynting vector; build 5 magnetization, permeability, wave equation, plane waves, intrinsic impedance); each ends with a **Practice** line pointing at its problems.
- 13 worked problems (build 6: a current sheet launches two waves, modelled on SP18 Exam 2 #5; build 5: fields across a magnetic interface, a pulse on the move) — all re-parameterized.
- **Practice bank** (`content/practice/`): 212 problems for Lectures 2–19 (12 per lecture, 8 for Lecture 11): 89 easy, 53 medium, 70 hard, each with a folded hint and a worked solution, 33 of them modelled on past exams. Build 5 added the Lecture 16–18 sets; **build 6 adds Lecture 19** and the topic "current-sheet radiation and the Poynting vector".
- 1 interactive demo (point charges + Gaussian loop); 55 original figures (`tools/figs/`; generated by `tools/figs.py`, and for Lectures 17–19 by `tools/figs_l17.py`, `figs_l18.py`, `figs_l19.py`, which import the helpers from `figs.py`).

Every page passed `tools/check.py` (113 pages, 2301 wikilinks/anchors, 22100 KaTeX expressions). Every practice answer was checked numerically by its author's script (`tools/practice/checks/`) and re-solved from the statement alone by an independent reviewer's script (`tools/practice/review/R*.py`); the problems changed in review were checked again. The Lecture 17–19 pages, figures, concept pages and worked problems were checked by their writers' scripts and then reviewed independently (`tools/lecture-checks/`). For Lecture 19 the review fixed a reversed statement in the slide-11 figure caption and a wrong claim about adding the power flows of counter-propagating waves, removed SP18 Exam 2 answers that had been quoted, and re-parameterized the worked problem so the exam key cannot carry over. For Lectures 17–18: no wrong physics was found; the reviews fixed one rounded number, several misleading or misattributed statements, and flagged slide values that disagree with handbook data (now on the errata page). In the new practice sets the review caught one wrong answer line (17.10(c), the jump in tangential **B**) and fixed it.

No page or problem in builds 5–6 is based on FA26 HW6 (open homework); it was read only to make sure nothing duplicates it.

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

