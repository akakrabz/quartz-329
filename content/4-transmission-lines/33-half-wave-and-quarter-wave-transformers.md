---
title: "Lecture 33 — TL circuits with half- and quarter-wave transformers"
description: "With any load, two line lengths need no general formula. A half-wave section repeats the load and flips the sign of V and I. A quarter-wave section inverts the load, Z_in Z_L = Z₀², and forces a load current −jV_in/Z₀ that does not depend on the load."
tags: [lecture, transmission-lines]
lecture: 33
---

*Lecture 33 · course notes §33 (no slide deck for this lecture is in the course folder as of November 11; the decks titled Lecture 31 and 32 cover the notes' §31–32) · prev: [[4-transmission-lines/32-input-impedance-and-microwave-resonators|Lecture 32]] · next: Lecture 34, line impedance, the generalized reflection coefficient and the Smith chart (coming) · worked twin: [[exams/e3-steady-state-lines#s2-a-quarter-wave-section-between-source-and-load|A quarter-wave section between source and load]] · practice: [[practice/33-half-and-quarter-wave-transformers|8 problems]]*

> [!abstract] In one breath
> Replace the short of Lecture 32 by any load $Z_L$ and keep the line length a multiple of a quarter wavelength. Then $e^{\pm j\beta\ell}$ is $-1$ or $\pm j$, and the phasor waves give two rules with no tangent in them. Half wave: $Z_{\text{in}} = Z_L$, with $\tilde V$ and $\tilde I$ reversed in sign. Quarter wave: $Z_{\text{in}}Z_L = Z_0^2$, and the load current is $-j\tilde V_{\text{in}}/Z_0$ whatever the load is. Longer lines are handled by chaining the two rules. Arbitrary lengths wait for Lecture 34.

## 1. The setting

The line of [[4-transmission-lines/28-distributed-circuits-and-bounce-diagrams|Lecture 28]] in sinusoidal steady state, with the coordinates of [[4-transmission-lines/32-input-impedance-and-microwave-resonators#3-phasors-on-the-line-measured-from-the-load|Lecture 32 §3]]: the load $Z_L = R_L+jX_L$ at $d = 0$, the input and its source circuit at $d = \ell$, and

$$
\tilde V(d) = V^+e^{j\beta d}+V^-e^{-j\beta d},\qquad \tilde I(d) = \frac{V^+e^{j\beta d}-V^-e^{-j\beta d}}{Z_0} .
$$

At the load, $\tilde V_L = \tilde V(0) = V^++V^-$ and $\tilde I_L = \tilde I(0) = (V^+-V^-)/Z_0$, with $\tilde V_L = Z_L\tilde I_L$. Here $\tilde V_{\text{in}}\equiv\tilde V(\ell)$, $\tilde I_{\text{in}}\equiv\tilde I(\ell)$ and $Z_{\text{in}} = \tilde V_{\text{in}}/\tilde I_{\text{in}}$. From this lecture on the notes drop the tildes on phasors; this site keeps them.

## 2. The half-wave transformer

For $\ell = \lambda/2$, $e^{\pm j\beta\lambda/2} = e^{\pm j\pi} = -1$:

$$
\tilde V_{\text{in}} = -V^+-V^- = -\tilde V_L,\qquad \tilde I_{\text{in}} = \frac{-V^++V^-}{Z_0} = -\tilde I_L .
$$

> [!key] Half-wave section
> $$
> Z_{\text{in}} = Z_L,\qquad \tilde V_{\text{in}} = -\tilde V_L,\qquad \tilde I_{\text{in}} = -\tilde I_L .
> $$
> The load is repeated at the input, whatever $Z_0$ is. Voltage and current arrive reversed in sign: half a period of delay.

## 3. The quarter-wave transformer

For $\ell = \lambda/4$, $e^{\pm j\beta\lambda/4} = e^{\pm j\pi/2} = \pm j$:

$$
\tilde V_{\text{in}} = jV^+-jV^- = jZ_0\tilde I_L,\qquad \tilde I_{\text{in}} = \frac{jV^++jV^-}{Z_0} = j\frac{\tilde V_L}{Z_0} .
$$

Divide the two:

> [!key] Quarter-wave section
> $$
> \begin{gathered}
> Z_{\text{in}} = \frac{Z_0^2}{Z_L},\\[4pt]
> \tilde I_L = -j\,\frac{\tilde V_{\text{in}}}{Z_0}\quad(\text{current forcing}),\qquad \tilde V_L = Z_L\tilde I_L = -jZ_0\,\tilde I_{\text{in}} .
> \end{gathered}
> $$
> The load is **inverted** about $Z_0$: large becomes small, inductive becomes capacitive, a short becomes an open. The load current depends on the input voltage and $Z_0$ only, not on $Z_L$.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 660 210" width="660" height="210" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px"><defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker><marker id="ahs" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs><line x1="60.0" y1="40.0" x2="230.0" y2="40.0" stroke="var(--accent)" stroke-width="3.2" stroke-linecap="round"/><line x1="60.0" y1="96.0" x2="230.0" y2="96.0" stroke="var(--accent)" stroke-width="3.2" stroke-linecap="round"/><text x="145.0" y="72.0" text-anchor="middle" fill="currentColor" style="font-size:12.5px;">Z₀</text><line x1="230.0" y1="40.0" x2="248.0" y2="40.0" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/><line x1="230.0" y1="96.0" x2="248.0" y2="96.0" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/><rect x="241.0" y="50.0" width="14.0" height="36.0" rx="0" fill="none" stroke="currentColor" stroke-width="1.4"/><text x="264.0" y="72.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;">Z<tspan baseline-shift="sub" style="font-size:9px">L</tspan></text><line x1="60.0" y1="116.0" x2="230.0" y2="116.0" stroke="currentColor" stroke-width="0.9" marker-end="url(#ahs)" stroke-linecap="round"/><line x1="230.0" y1="116.0" x2="60.0" y2="116.0" stroke="currentColor" stroke-width="0.9" marker-end="url(#ahs)" stroke-linecap="round"/><text x="145.0" y="132.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">ℓ = λ/2</text><circle cx="60.0" cy="40.0" r="3.0" fill="currentColor" stroke="currentColor" stroke-width="1.5"/><circle cx="60.0" cy="96.0" r="3.0" fill="currentColor" stroke="currentColor" stroke-width="1.5"/><text x="52.0" y="72.0" text-anchor="end" fill="var(--muted)" style="font-size:11px;">in</text><text x="160.0" y="158.0" text-anchor="middle" fill="currentColor" style="font-size:12.5px;">Z<tspan baseline-shift="sub" style="font-size:9px">in</tspan> = Z<tspan baseline-shift="sub" style="font-size:9px">L</tspan></text><text x="160.0" y="175.0" text-anchor="middle" fill="currentColor" style="font-size:12.5px;">V<tspan baseline-shift="sub" style="font-size:9px">in</tspan> = −V<tspan baseline-shift="sub" style="font-size:9px">L</tspan></text><text x="160.0" y="192.0" text-anchor="middle" fill="currentColor" style="font-size:12.5px;">I<tspan baseline-shift="sub" style="font-size:9px">in</tspan> = −I<tspan baseline-shift="sub" style="font-size:9px">L</tspan></text><line x1="390.0" y1="40.0" x2="560.0" y2="40.0" stroke="var(--accent)" stroke-width="3.2" stroke-linecap="round"/><line x1="390.0" y1="96.0" x2="560.0" y2="96.0" stroke="var(--accent)" stroke-width="3.2" stroke-linecap="round"/><text x="475.0" y="72.0" text-anchor="middle" fill="currentColor" style="font-size:12.5px;">Z₀</text><line x1="560.0" y1="40.0" x2="578.0" y2="40.0" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/><line x1="560.0" y1="96.0" x2="578.0" y2="96.0" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/><rect x="571.0" y="50.0" width="14.0" height="36.0" rx="0" fill="none" stroke="currentColor" stroke-width="1.4"/><text x="594.0" y="72.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;">Z<tspan baseline-shift="sub" style="font-size:9px">L</tspan></text><line x1="390.0" y1="116.0" x2="560.0" y2="116.0" stroke="currentColor" stroke-width="0.9" marker-end="url(#ahs)" stroke-linecap="round"/><line x1="560.0" y1="116.0" x2="390.0" y2="116.0" stroke="currentColor" stroke-width="0.9" marker-end="url(#ahs)" stroke-linecap="round"/><text x="475.0" y="132.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">ℓ = λ/4</text><circle cx="390.0" cy="40.0" r="3.0" fill="currentColor" stroke="currentColor" stroke-width="1.5"/><circle cx="390.0" cy="96.0" r="3.0" fill="currentColor" stroke="currentColor" stroke-width="1.5"/><text x="382.0" y="72.0" text-anchor="end" fill="var(--muted)" style="font-size:11px;">in</text><text x="490.0" y="158.0" text-anchor="middle" fill="currentColor" style="font-size:12.5px;">Z<tspan baseline-shift="sub" style="font-size:9px">in</tspan> Z<tspan baseline-shift="sub" style="font-size:9px">L</tspan> = Z₀²</text><text x="490.0" y="175.0" text-anchor="middle" fill="currentColor" style="font-size:12.5px;">I<tspan baseline-shift="sub" style="font-size:9px">L</tspan> = −j V<tspan baseline-shift="sub" style="font-size:9px">in</tspan> / Z₀</text><text x="490.0" y="192.0" text-anchor="middle" fill="currentColor" style="font-size:12.5px;">V<tspan baseline-shift="sub" style="font-size:9px">L</tspan> = −j Z₀ I<tspan baseline-shift="sub" style="font-size:9px">in</tspan></text></svg><figcaption>The two special lengths. A half-wave section repeats its load and flips the sign of voltage and current. A quarter-wave section inverts the load about Z₀ and fixes the load current from the input voltage alone, whatever the load is.</figcaption></figure>

What the rules say:
- Lecture 32's stubs are the special cases $Z_L = 0$ and $Z_L = \infty$: a quarter-wave shorted stub has $Z_{\text{in}} = Z_0^2/0 = \infty$.
- $Z_L = Z_0$ gives $Z_{\text{in}} = Z_0$ for every length: a matched line.
- A lossless line passes on all the power it takes in: $\tfrac12\text{Re}\{\tilde V_{\text{in}}\tilde I_{\text{in}}^*\} = \tfrac12\text{Re}\{\tilde V_L\tilde I_L^*\}$. Compute it at whichever end is easier.
- **Chaining.** $3\lambda/4 = \lambda/2+\lambda/4$: apply one rule, then the other. Any odd number of quarter waves inverts; any whole number of half waves repeats.
- The rules hold at the one frequency where the length is exactly $\lambda/4$ or $\lambda/2$.

> [!trap] Quarter- and half-wave sections
> - $Z_0^2/Z_L$ is for a quarter wave (and $3\lambda/4$, …) only. At other lengths use Lecture 34.
> - Current forcing uses the **input voltage**: $\tilde I_L = -j\tilde V_{\text{in}}/Z_0$. Find $\tilde V_{\text{in}}$ first, by a divider with $Z_{\text{in}}$ if the source has an internal impedance.
> - The $-j$ and the $-1$ are phase shifts of a quarter and a half period. Dropping them leaves magnitudes right and phasors wrong.
> - With a complex $Z_L$, divide properly: $1/(1+j) = (1-j)/2$.

> [!recipe] A source, a quarter- or half-wave line, a load
> 1. $Z_{\text{in}}$: $Z_0^2/Z_L$ or $Z_L$ (chain the rules for $3\lambda/4$, $\lambda$, …).
> 2. $\tilde V_{\text{in}}$ by voltage division between the source impedance and $Z_{\text{in}}$.
> 3. Quarter wave: $\tilde I_L = -j\tilde V_{\text{in}}/Z_0$, then $\tilde V_L = Z_L\tilde I_L$. Half wave: $\tilde V_L = -\tilde V_{\text{in}}$.
> 4. Power: $P_L = \tfrac12\lvert\tilde I_L\rvert^2R_L$, and check it against the input.

## 4. The notes' examples

> [!example] Example 1 (notes) — inverting a complex load
> $Z_L = 50+j50\ \Omega$ on a quarter-wave line with $Z_0 = 50\ \Omega$:
> $$
> Z_{\text{in}} = \frac{50^2}{50+j50} = \frac{50}{1+j} = 25-j25\ \Omega .
> $$
> An inductive load has become a capacitive input.

> [!example] Example 2 (notes) — current forcing and power
> The same line and load with $\tilde V_{\text{in}} = 100\angle0^\circ$ V at the input. $\tilde I_L = -j\,100/50 = -j2$ A. $\tilde V_L = (50+j50)(-j2) = 100-j100$ V. $P_L = \tfrac12\text{Re}\{\tilde V_L\tilde I_L^*\} = \tfrac12\text{Re}\{(100-j100)(j2)\} = 100$ W. Check: $\tfrac12\lvert\tilde I_L\rvert^2R_L = \tfrac12(4)(50) = 100$ W, and at the input $\tfrac12\text{Re}\{\lvert\tilde V_{\text{in}}\rvert^2/Z_{\text{in}}^*\} = 100$ W.

> [!example] Example 3 (notes) — three quarter waves
> $Z_L = 100\ \Omega$, $\ell = 0.75\lambda$, $Z_0 = 50\ \Omega$; a source $\tilde V_g = j10$ V with $Z_g = 25\ \Omega$ at $d = 0.75\lambda$.
> - Impedance: at $d = 0.5\lambda$ the load repeats, 100 Ω. The last quarter wave inverts it: $Z_{\text{in}} = 50^2/100 = 25\ \Omega$.
> - Divider: $\tilde V_{\text{in}} = j10\cdot\tfrac{25}{25+25} = j5$ V.
> - Half-wave rule from $d = 0.75\lambda$ to $0.25\lambda$: $\tilde V(0.25\lambda) = -j5$ V.
> - Current forcing over the last quarter wave: $\tilde I_L = -j(-j5)/50 = -0.1$ A, so $\tilde V_L = -10$ V.
>
> Check (this site's): the input takes $\tfrac12(5)(0.2) = 0.5$ W and the load dissipates $\tfrac12(0.1)^2(100) = 0.5$ W.

> [!example] Example 4 (notes) — two loads fed through quarter-wave lines
> Two quarter-wave lines, both $Z_0 = 50\ \Omega$, share one input with $\tilde V_{\text{in}} = 5$ V and feed $Z_{L1} = 50\ \Omega$ and $Z_{L2} = 100\ \Omega$. Current forcing gives both loads the same current, $-j5/50 = -j0.1$ A. Then $\tilde V_{L1} = -j5$ V, $\tilde V_{L2} = -j10$ V, and the total power is $\tfrac12(5)(0.1)+\tfrac12(10)(0.1) = 0.75$ W. Unequal loads, equal currents: this is why quarter-wave feeds are used where several elements must carry the same current.

> [!example] Matching with a quarter-wave section (this site's)
> A 200 Ω load on a 50 Ω system reflects with $\Gamma_L = 0.6$. Insert a quarter-wave section with $Z_q = \sqrt{50\cdot200} = 100\ \Omega$: its input is $100^2/200 = 50\ \Omega$, and the 50 Ω line sees a match. Only at the frequency where the section is $\lambda/4$ long.

## 5. Summary

- Half wave: $Z_{\text{in}} = Z_L$; $\tilde V$ and $\tilde I$ change sign.
- Quarter wave: $Z_{\text{in}} = Z_0^2/Z_L$; $\tilde I_L = -j\tilde V_{\text{in}}/Z_0$; $\tilde V_L = -jZ_0\tilde I_{\text{in}}$.
- Chain them for any multiple of $\lambda/4$. Power in equals power to the load.
- Notes' numbers: $50+j50\to25-j25\ \Omega$; 100 V in gives $-j2$ A and 100 W; the $0.75\lambda$ circuit gives $\tilde I_L = -0.1$ A, $\tilde V_L = -10$ V; two forced loads take 0.75 W.
- Next, Lecture 34: lines of any length, with $\Gamma(d)$ and the Smith chart.

Concept pages: [[concepts/quarter-wave-transformer]] · [[concepts/stub-input-impedance]] · [[concepts/characteristic-impedance]].

> [!exam] On exams
> SP18 Exam 3 #4(b): a load on a line that is $\lambda/4$ long at the source frequency, in series with a resistor and a source; find $Z_{\text{in}}$ and $\tilde V_{\text{in}}$ (recipe steps 1 and 2; [[exams/e3-sp18#4-a-line-in-series-with-a-resistor-20-points|guide]]). The half-wave rule is behind "the line looks like a short every $\lambda/2$ from a short" in FA23 #7(c). Lecture 33 is **not on FA26 Midterm 3**, which covers Lectures 1–30 ([[exams/index#the-scope|scope]]).

> [!tip] Practice this lecture
> [[practice/33-half-and-quarter-wave-transformers|8 practice problems]] — 4 easy, 2 medium, 2 hard — each with a folded hint and a worked solution. Start with [[practice/33-half-and-quarter-wave-transformers#331-five-inputs|33.1 Five inputs]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 33 (6 pages): the half-wave and quarter-wave relations, the current-forcing equation, Examples 1–4. No slide deck for this lecture is in the course folder as of November 11. This site's own: the chaining remark, the power checks, the recipe, the matching example, the figure; numbers checked in `tools/build14/checks/L31_33.py`.
