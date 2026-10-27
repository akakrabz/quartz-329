---
title: "Lecture 25 — Wave reflection and transmission"
description: "A plane wave meeting a planar interface head-on splits into a reflected and a transmitted wave. Continuity of tangential E and H gives Γ = (η₂ − η₁)/(η₂ + η₁) and τ = 1 + Γ, and the reflected and transmitted powers add up to the incident power."
tags: [lecture, waves]
lecture: 25
---

*Lecture 25 · course notes §25 (no slides) · prev: [[3-maxwell-and-waves/24-signal-transmission-and-circular-polarization|Lecture 24]] · next: [[3-maxwell-and-waves/26-standing-waves-and-radiation-pressure|Lecture 26]] · worked problem: [[problems/working-back-from-a-transmitted-wave|Working back from a transmitted wave]] · practice: [[practice/25-reflection-and-transmission|12 problems]]*

> [!abstract] In one breath
> A plane wave hits the plane $z = 0$ head-on. On its own it would violate the boundary conditions there, so a reflected wave travels back into region 1 and a transmitted wave continues into region 2. Continuity of tangential $\tilde{\mathbf{E}}$ and $\tilde{\mathbf{H}}$ fixes their amplitudes: $\Gamma = (\eta_2-\eta_1)/(\eta_2+\eta_1)$ and $\tau = 1+\Gamma$. Equal impedances transmit everything. A perfect conductor ($\eta_2 = 0$) reflects everything, with $\Gamma = -1$. The fraction of the power reflected is $\lvert\Gamma\rvert^2$; the rest enters region 2.

## 1. Three waves at a planar interface

The notes' setup:
- region 1, $z<0$: a perfect dielectric, $\mu_1$, $\epsilon_1$, $\sigma_1 = 0$;
- region 2, $z>0$: $\mu_2$, $\epsilon_2$, $\sigma_2$;
- no surface charge or current on $z = 0$, except in the perfect-conductor limit $\sigma_2\to\infty$ (§3).

A source far away at $z\to-\infty$ sends an $\hat x$-polarized wave toward $+z$. Alone, it would put $\tilde E_x = E_0$ just left of $z = 0$ and nothing just right of it, a jump that tangential $\mathbf{E}$ is not allowed. So the notes postulate two more waves, with unknown amplitudes.

<!-- fig:refl-setup -->

> [!key] The three waves
> $$
> \begin{gathered}
> \tilde{\mathbf{E}}_i = \hat x\,E_0e^{-j\beta_1z},\qquad \tilde{\mathbf{H}}_i = \hat y\,\frac{E_0}{\eta_1}e^{-j\beta_1z},\\[6pt]
> \tilde{\mathbf{E}}_r = \hat x\,\Gamma E_0e^{j\beta_1z},\qquad \tilde{\mathbf{H}}_r = -\hat y\,\frac{\Gamma E_0}{\eta_1}e^{j\beta_1z},\\[6pt]
> \tilde{\mathbf{E}}_t = \hat x\,\tau E_0e^{-\gamma_2z},\qquad \tilde{\mathbf{H}}_t = \hat y\,\frac{\tau E_0}{\eta_2}e^{-\gamma_2z}.
> \end{gathered}
> $$
> Region 1: $\eta_1 = \sqrt{\mu_1/\epsilon_1}$, $\beta_1 = \omega\sqrt{\mu_1\epsilon_1}$. Region 2: $\gamma_2 = \alpha_2+j\beta_2 = \sqrt{j\omega\mu_2(\sigma_2+j\omega\epsilon_2)}$ and $\eta_2 = \sqrt{j\omega\mu_2/(\sigma_2+j\omega\epsilon_2)}$, both from [[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves|Lecture 22]]. $\Gamma$ is the **reflection coefficient** and $\tau$ the **transmission coefficient**; both may be complex.

Each pair is one plane wave obeying [[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation|Lecture 21]]'s rule $\tilde{\mathbf{H}} = \hat u\times\tilde{\mathbf{E}}/\eta$. The reflected wave travels along $\hat u = -\hat z$. Its exponent is therefore $e^{+j\beta_1z}$, and its $\tilde{\mathbf{H}}$ carries a minus sign: $(-\hat z)\times\hat x = -\hat y$. The transmitted wave decays as $e^{-\alpha_2z}$ unless $\sigma_2 = 0$.

Notation: the notes write $E_o$, $\eta_o$, $\epsilon_o$; this page writes $E_0$, $\eta_0$, $\epsilon_0$. Here $\tau$ is the transmission coefficient, as in the notes. On the Lecture 22–23 pages $\tau$ was the phase of $\eta$, which this page writes $\angle\eta$.

## 2. Matching tangential E and H: Γ and τ

At $z = 0$ every exponential equals 1, and all six fields are tangential. A finite $\sigma_2$ carries only volume current, so $\mathbf{J}_s = 0$. The boundary conditions of [[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Lecture 16]] (first derived in [[1-electrostatics/06-circulation-and-boundary-conditions|Lecture 6]]), with $\hat n = -\hat z$ from region 2 into region 1 (the notes' margin uses the equivalent $\pm$ form), then require continuous $\tilde E_x$ and $\tilde H_y$.

> [!key] Reflection and transmission coefficients
> $$
> \begin{gathered}
> \tilde E_x:\quad (1+\Gamma)E_0 = \tau E_0,\\[4pt]
> \tilde H_y:\quad (1-\Gamma)\frac{E_0}{\eta_1} = \tau\frac{E_0}{\eta_2},\\[8pt]
> \Gamma = \frac{\eta_2-\eta_1}{\eta_2+\eta_1},\qquad \tau = 1+\Gamma = \frac{2\eta_2}{\eta_2+\eta_1}.
> \end{gathered}
> $$
> Put $\tau = 1+\Gamma$ into the second line and solve for $\Gamma$. Both are ratios of **electric** fields at $z = 0$. The notes' advice: memorize $\Gamma$, and remember $\tau$ as "one plus $\Gamma$".

What the formulas say:
- Real $\eta$'s: $\eta_2>\eta_1$ gives $\Gamma>0$ and $\tau>1$; $\eta_2<\eta_1$ gives $\Gamma<0$ and $\tau<1$. Always $-1<\Gamma<1$ and $0<\tau<2$.
- A lossy region 2 has a complex $\eta_2$, so $\Gamma$ and $\tau$ are complex: the interface shifts the phase. Since $\text{Re}\{\eta_2\}\ge0$, $\lvert\Gamma\rvert\le1$ always.
- The magnetic-field ratios at $z = 0$ are $\tilde H_r/\tilde H_i = -\Gamma$ and $\tilde H_t/\tilde H_i = 1-\Gamma = \tau\eta_1/\eta_2$.
- Non-magnetic media ($\mu_1 = \mu_2$) have $\eta\propto1/n$ with $n = \sqrt{\epsilon_r}$, so $\Gamma = (n_1-n_2)/(n_1+n_2)$.
- Swapping two lossless media flips the sign of $\Gamma$ and keeps $\Gamma^2$.

<!-- fig:refl-gamma-tau -->

> [!trap] Γ and τ
> - $\tau>1$ is not a gain. The power also depends on the $\eta$'s (§4).
> - The reflected $\tilde{\mathbf{H}}$ goes with $-\Gamma$, not $\Gamma$.
> - $\eta_2-\eta_1$ is "far side minus incident side". Swap them and $\Gamma$ changes sign.
> - In a lossy region 2, use the complex $\eta_2$, not $\sqrt{\mu_2/\epsilon_2}$.

> [!recipe] A normal-incidence problem
> 1. Find the incident side (region 1) and each wave's direction $\hat u$.
> 2. Compute $\eta_1$, $\eta_2$ (complex if lossy), $\beta_1$ and $\gamma_2$.
> 3. Compute $\Gamma$ and $\tau = 1+\Gamma$.
> 4. Write each $\tilde{\mathbf{E}}$: interface amplitude $E_0$, $\Gamma E_0$ or $\tau E_0$, exponent sign from $\hat u$. Given the transmitted wave instead, $E_0 = \tilde E_t(0)/\tau$.
> 5. $\tilde{\mathbf{H}} = \hat u\times\tilde{\mathbf{E}}/\eta$ for each wave; check that tangential $\tilde{\mathbf{H}}$ is continuous.
> 6. $\langle\mathbf{S}\rangle$ for each wave, and the power balance (§4).

## 3. Special cases

The notes list three.

1. **Perfect conductor, $\sigma_2\to\infty$.** Then $\eta_2\to0$, so $\Gamma = -1$ and $\tau = 0$. Nothing enters region 2 and everything reflects: a mirror. At $z = 0$ the total fields are $\tilde{\mathbf{E}} = \hat xE_0(1+\Gamma) = 0$ and $\tilde{\mathbf{H}} = \hat y\,2E_0/\eta_1$. That tangential $\tilde{\mathbf{H}}$ needs a surface current (Lecture 16):
   $$
   \tilde{\mathbf{J}}_s = \hat n\times\tilde{\mathbf{H}}_1 = (-\hat z)\times\hat y\,\frac{2E_0}{\eta_1} = \hat x\,\frac{2E_0}{\eta_1}.
   $$
   Lecture 26 derives this current from a good conductor, shows that the total field in region 1 is a standing wave, and computes the radiation pressure on the mirror.
2. **Matched impedances, $\eta_2 = \eta_1$.** $\Gamma = 0$ and $\tau = 1$: no reflection. Identical media are the notes' case. Any pair with $\mu_2/\epsilon_2 = \mu_1/\epsilon_1$ also works, for example $\mu_r = \epsilon_r$ against vacuum.
3. **Lossless region 2, $\sigma_2 = 0$.** Some power reflects unless $\eta_2 = \eta_1$. An anti-glare coating reduces it: a layer of impedance $\sqrt{\eta_1\eta_2}$, a quarter of the wavelength *inside the layer* thick. This is "impedance matching", explained with transmission lines in [[4-transmission-lines/index|Unit 4]].

> [!example] Example — coating a lens (this site's numbers)
> Glass with $\epsilon_r = 2.25$ ($n = 1.5$, the medium of Example 1 in §4) in air gives $\Gamma = (1-1.5)/(1+1.5) = -0.2$: 4 % of the light power reflects at each surface. The coating needs $\eta_c = \sqrt{\eta_0\cdot\eta_0/1.5}$, so $n_c = \sqrt{1.5} = 1.22$. For green light ($\lambda_0 = 550$ nm) the layer is $\lambda_0/(4n_c) = 112$ nm thick.

## 4. Power balance

Each wave's time-average power follows from $\langle\mathbf{S}\rangle = \tfrac12\text{Re}\{\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*\}$ (Lecture 21).

> [!key] Time-average Poynting vectors (region 1 lossless)
> $$
> \begin{gathered}
> \langle\mathbf{S}_i\rangle = \hat z\,\frac{\lvert E_0\rvert^2}{2\eta_1},\qquad \langle\mathbf{S}_r\rangle = -\hat z\,\lvert\Gamma\rvert^2\,\frac{\lvert E_0\rvert^2}{2\eta_1},\\[6pt]
> \langle\mathbf{S}_t\rangle = \hat z\,\lvert\tau\rvert^2\,\frac{\lvert E_0\rvert^2}{2}\,\text{Re}\Big\{\frac{1}{\eta_2}\Big\}\,e^{-2\alpha_2z},\\[8pt]
> 1 = \lvert\Gamma\rvert^2 + \lvert\tau\rvert^2\,\eta_1\,\text{Re}\Big\{\frac{1}{\eta_2}\Big\}.
> \end{gathered}
> $$
> The last line is $\lvert\langle\mathbf{S}_i\rangle\rvert = \lvert\langle\mathbf{S}_r\rangle\rvert + \lvert\langle\mathbf{S}_t\rangle\rvert$ at $z = 0^+$. A fraction $\lvert\Gamma\rvert^2$ of the power reflects and $1-\lvert\Gamma\rvert^2$ enters region 2. For a lossless region 2 the balance reads $1 = \Gamma^2 + \tau^2\eta_1/\eta_2$.

$\text{Re}\{1/\eta_2\} = \cos\angle\eta_2/\lvert\eta_2\rvert$ is Lecture 22's lossy-medium factor.

> [!derivation]- Why the balance holds, lossy region 2 included
> Lossless case: §2 gives $\eta_1/\eta_2 = (1-\Gamma)/(1+\Gamma)$, so $\tau^2\eta_1/\eta_2 = (1+\Gamma)(1-\Gamma) = 1-\Gamma^2$.
>
> General case: the total fields in region 1 are $\tilde E_x = E_0(e^{-j\beta_1z}+\Gamma e^{j\beta_1z})$ and $\tilde H_y = (E_0/\eta_1)(e^{-j\beta_1z}-\Gamma e^{j\beta_1z})$. Their product is
> $$
> \begin{gathered}
> \tilde E_x\tilde H_y^* = \frac{\lvert E_0\rvert^2}{\eta_1}\big(1-\lvert\Gamma\rvert^2 + w - w^*\big),\\[4pt]
> w = \Gamma e^{j2\beta_1z}.
> \end{gathered}
> $$
> $w - w^* = 2j\,\text{Im}\{w\}$ is imaginary, so the net flux in region 1 is $(1-\lvert\Gamma\rvert^2)\lvert E_0\rvert^2/2\eta_1$ at every $z$: incident minus reflected, with no cross term. Tangential $\tilde{\mathbf{E}}$ and $\tilde{\mathbf{H}}$ are continuous at $z = 0$, so this flux equals $\langle S_t\rangle$ at $z = 0^+$.

> [!example] Example 1 (notes) — vacuum onto a dielectric
> $\tilde{\mathbf{E}}_i = \hat x\sqrt{120\pi}\,e^{-j\beta_1z}$ V/m in vacuum meets a medium with $\mu = \mu_0$, $\epsilon = \tfrac94\epsilon_0$ at $z = 0$.
> - $\eta_2 = \eta_0/\sqrt{9/4} = \tfrac23\eta_0$, so $\Gamma = (\tfrac23-1)/(\tfrac23+1) = -\tfrac15$ and $\tau = \tfrac45$.
> - $\tilde{\mathbf{E}}_r = -\tfrac15\hat x\sqrt{120\pi}\,e^{j\beta_1z}$ and $\tilde{\mathbf{H}}_r = +\tfrac15\hat y\,(\sqrt{120\pi}/\eta_0)\,e^{j\beta_1z}$: a negative $\Gamma$ reverses both from the $\Gamma>0$ figure.
> - $\tilde{\mathbf{E}}_t = \tfrac45\hat x\sqrt{120\pi}\,e^{-j\beta_2z}$ and $\tilde{\mathbf{H}}_t = \tfrac45\hat y\,\sqrt{120\pi}/(\tfrac23\eta_0)\,e^{-j\beta_2z}$, with $\beta_2 = 1.5\beta_1$.
> - With $\eta_0 = 120\pi\ \Omega$ (the notes write $\approx$): $\langle\mathbf{S}_i\rangle = \tfrac12\hat z$, $\langle\mathbf{S}_r\rangle = -\tfrac12\cdot\tfrac1{25}\hat z = -0.02\hat z$ and $\langle\mathbf{S}_t\rangle = \tfrac12\cdot\tfrac{16}{25}\cdot\tfrac32\hat z = 0.48\hat z$ W/m².
> - $0.02 + 0.48 = 0.5$: 4 % reflects, 96 % is transmitted.

<!-- fig:refl-interface-snapshot -->

> [!example] Example — air onto seawater at 1 kHz (this site's numbers)
> Seawater ($\sigma = 4$ S/m) at 1 kHz is a good conductor with $\delta = 7.96$ m and $\eta_2 = (1+j)/(\sigma\delta) = 0.0314(1+j)\ \Omega$ ([[3-maxwell-and-waves/23-imperfect-dielectrics-and-good-conductors|Lecture 23]]). Then $\Gamma = -0.99983 + j0.00017$, and $1-\lvert\Gamma\rvert^2 = 3.3\times10^{-4}$. Only 0.033 % of the incident power enters the sea, and that part then decays as $e^{-2z/\delta}$. A good conductor is almost a mirror; Lecture 26 takes the limit.

## 5. Summary

- Incident, reflected and transmitted phasors: $\hat x$ components $E_0e^{-j\beta_1z}$, $\Gamma E_0e^{j\beta_1z}$ and $\tau E_0e^{-\gamma_2z}$. Each $\tilde{\mathbf{H}}$ is $\hat u\times\tilde{\mathbf{E}}/\eta$, so the reflected $\tilde{\mathbf{H}}$ carries $-\Gamma$.
- Continuity of tangential $\tilde{\mathbf{E}}$ and $\tilde{\mathbf{H}}$ (no $\mathbf{J}_s$ for finite $\sigma_2$): $\Gamma = (\eta_2-\eta_1)/(\eta_2+\eta_1)$ and $\tau = 1+\Gamma = 2\eta_2/(\eta_2+\eta_1)$.
- Perfect conductor: $\Gamma = -1$, $\tau = 0$, $\tilde{\mathbf{J}}_s = \hat x\,2E_0/\eta_1$. Matched: $\Gamma = 0$, $\tau = 1$. Lossless region 2: partial reflection, reduced by a quarter-wave coating of impedance $\sqrt{\eta_1\eta_2}$.
- Power: $1 = \lvert\Gamma\rvert^2 + \lvert\tau\rvert^2\eta_1\text{Re}\{1/\eta_2\}$. Glass reflects 4 %.
- Next, [[3-maxwell-and-waves/26-standing-waves-and-radiation-pressure|Lecture 26]]: the standing wave in region 1, and radiation pressure.

Concept pages: [[concepts/reflection-and-transmission]] · [[concepts/boundary-conditions]] · [[concepts/intrinsic-impedance]] · [[concepts/poynting-vector]] · [[concepts/plane-waves]].

> [!exam] On exams
> Four Exam 3 problems on hand. Summer 2017 HE3 #3c–f and SP18 Exam 3 #2d–e give the *transmitted* wave and ask for $\Gamma$, $\tau$ and the incident and reflected phasors: divide by $\tau$, multiply by $\Gamma$, mind each exponent's sign and the $-\Gamma$ on $\tilde{\mathbf{H}}_r$. SP19 Exam 3 #3b reflects a circularly polarized wave from a perfect conductor: $\Gamma = -1$ for each component, with the travel reversed ([[3-maxwell-and-waves/24-signal-transmission-and-circular-polarization|Lecture 24]] for handedness). SP17 Exam 3 #2(iv) sends a wave from a lossy medium into air: compute both $\eta$'s; the $\Gamma$ formula holds with a complex $\eta_1$ too. Numbers use $\eta_0 = 120\pi\ \Omega$; the Spring papers allow no calculator.

> [!tip] Practice this lecture
> [[practice/25-reflection-and-transmission|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/25-reflection-and-transmission#251-four-interfaces|25.1 Four interfaces]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 25 (6 pages): the setup with the boundary conditions in the margin, the three postulated waves, the two matching conditions with the boxed $\Gamma$ and $\tau$, the three special cases with the quarter-wave footnote, and Example 1 with its power check. Rao (2009) §5.6, eqs. 5.101–5.105, for cross-checks. This site's own: the figures, the recipe, the lossy-case power proof, the $n$-form of $\Gamma$, the surface current (derived in the notes' Lecture 26), the coating and seawater examples; numbers checked by script. Slips in the notes (typos, a margin figure drawn for $\Gamma>0$) are on the errata page.
