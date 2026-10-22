# Two beginner-friendly infographics: "Wave propagation in free space" (ECE 329 site, HW8 problem 5)

The student's assignment (HW8 #5) asks them to *use a generative-AI tool to create at least two beginner-friendly,
comprehensive infographics* on **wave propagation in free space**, each with the major ideas/relationships, the
equations, diagrams, labels and **at least one worked example** — then the student evaluates them. You produce the two
infographics as site figures. **Do your honest best** (correct physics, clear labels); do not plant errors, and do not
write any evaluation — that part is the student's.

The two versions must be *substantially different* (the assignment requires two different prompts or tools):
- **Version A — "Anatomy of a plane wave"** (reference-poster style): one big labelled diagram of an x-polarized plane
  wave travelling toward +z in free space (E along x, H along y, E×H along z; a snapshot showing λ); a panel of the core
  relations — wave equation, f(t − z/c) and direction reading, v = c = 1/√(μ₀ε₀) ≈ 3×10⁸ m/s, η₀ = √(μ₀/ε₀) ≈ 377 Ω,
  H = ẑ×E/η₀, λ = c/f, β = 2π/λ = ω/c, S = E×H, ⟨S⟩ = E₀²/2η₀; a "units" strip; and a boxed worked example:
  100 MHz, E₀ = 3 V/m → λ = 3 m, β = 2.094 rad/m, H₀ = 7.96 mA/m, ⟨S⟩ = 11.9 mW/m², with the full E and H expressions.
- **Version B — "From antenna to receiver: a wave's journey"** (narrative/flow style, for a first-year): 4–5 numbered
  stations with small sketches: (1) a current (sheet/antenna) launches the wave — E opposes the current (E = −η₀J_s/2
  for a sheet), (2) it travels at c — a delay z/c, "300 m per microsecond", (3) it carries power — ⟨S⟩ = E₀²/2η₀, the
  1/r² spreading of an isotropic source, (4) it is read by a receiver — H = E/η₀ fixed, direction from the sign in
  (t − z/c); plus a worked example as a story: a 50 kW isotropic transmitter at 10 km → ⟨S⟩ = 39.8 μW/m², E₀ = 0.173 V/m,
  H₀ = 0.459 mA/m, delay 33.3 μs. Include a short "common mistakes" strip (e.g. c vs v in a dielectric; peak vs average
  power; reading direction from the sign). Different layout, typography emphasis and colour use from A.

## Rules
- Write `/home/claude/work/figs_hw8.py` starting `from figs import *` and `from figs import _odot, _otimes, _sub, _tint`,
  ending with `if __name__ == "__main__":` calling `fig_info_anatomy()` and `fig_info_journey()`; running it writes
  `/home/claude/work/figs/info-wave-anatomy.html` and `/home/claude/work/figs/info-wave-journey.html` via `figure()`.
  Model modules: `/home/claude/work/figs_l24.py`, `figs_l25.py`; helpers `figs.py` lines 1–86 and 1083–1120.
- Size: viewBox about 760×(900–1200); must read at 820 px wide and still be legible at phone width (the site scales
  the SVG). Use ≥ 13 px text for body, ≥ 18 px for headings. `currentColor` + `var(--accent)`, `var(--accent2)`,
  `var(--hi)`, `var(--muted)`, `_tint` for panels — dark-mode safe. Escape `<`/`>` in SVG text. Subscripts via
  `_sub`. Plots (the snapshot) computed with numpy. Captions ≤ 60 words, saying it is an AI-generated infographic made
  for HW8 #5 and which prompt style produced it.
- Every number in both infographics must be computed in `/home/claude/work/hw8/verify_info.py` (numpy) with PASS lines,
  output saved to `verify_info.out`; every direction by `np.cross`.
- Visual check (required): assemble a private copy of a page that embeds both figures and screenshot light/dark/phone:
  write `/home/claude/work/hw8/preview-page.md` containing only the two `<!-- fig:info-wave-anatomy -->` /
  `<!-- fig:info-wave-journey -->` markers with a title frontmatter, copy it to
  `/home/claude/work/preview/hw8src/preview-page.md`, run
  `cd /home/claude/work && python3 -c "import assemble; assemble.SRC='/home/claude/work/preview/hw8src'; assemble.DST='/home/claude/work/preview/hw8/content'; assemble.main()"`
  (if `assemble.SRC` is not a thing, read assemble.py and adapt), then
  `node preview/preview.mjs preview/hw8/content preview/hw8/out && cp -r preview/out8/fonts preview/out8/katex.min.css preview/preview.css preview/hw8/out/`
  and screenshot with playwright (model `/home/claude/work/preview/shots8.py`) at 820 and 380 px, light and dark. Look
  at every screenshot; fix overlaps/clipping.
- Do not edit any file outside `/home/claude/work/figs_hw8.py`, `/home/claude/work/figs/info-*.html`,
  `/home/claude/work/hw8/`, `/home/claude/work/preview/hw8*`.
- Final message ≤ 15 lines: the two files, what each contains, the verify result, and the exact prompt text you
  would say produced each version (one short paragraph each — the student must report prompts).
