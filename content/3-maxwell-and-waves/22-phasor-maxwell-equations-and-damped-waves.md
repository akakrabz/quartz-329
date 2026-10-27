---
title: "Lecture 22 — Maxwell's equations in phasor form and damped waves in conducting media"
description: "Phasor Maxwell equations, the replacement jωε → σ + jωε, damped plane waves with γ = α + jβ and complex η, and the four regimes; the content lives on the topic pages linked from each section."
tags: [lecture, waves]
lecture: 22
---

*Lecture 22 · course notes §22 · **slides: not yet available — this page is built from the course notes** · prev: [[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation|Lecture 21]] · next: [[3-maxwell-and-waves/23-imperfect-dielectrics-and-good-conductors|Lecture 23]] · worked problem: [[problems/decoding-a-damped-wave|Decoding a damped wave]] · practice: [[practice/22-damped-waves-in-conducting-media|12 problems]]*

> [!abstract] In one breath
> With $\partial/\partial t\to j\omega$, Maxwell's equations become algebra for the phasors of [[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation|Lecture 21]] and reproduce the waves of [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves|Lecture 18]]. Conductivity turns $j\omega\epsilon$ into $\sigma + j\omega\epsilon$: the **propagation constant** $\gamma = \alpha + j\beta$ and **intrinsic impedance** $\eta$ go complex, the amplitude falls by $1/e$ per **penetration depth** $\delta = 1/\alpha$, and $\mathbf{H}$ lags $\mathbf{E}$ by $\tau = \angle\eta$. The ratio $\sigma/\omega\epsilon$ ([[1-electrostatics/08-conductors-dielectrics-and-polarization|Lecture 8]]'s relaxation time against $1/\omega$) sorts imperfect dielectrics from good conductors ([[3-maxwell-and-waves/23-imperfect-dielectrics-and-good-conductors|Lecture 23]]).

## 1. Maxwell's equations at one frequency

$\partial/\partial t\to j\omega$ in every law; the divergence laws follow from the curl laws plus continuity; a uniform conductor carries no oscillating charge.

→ Full treatment: [[concepts/phasor-maxwell-equations|Maxwell's equations in phasor form]]

## 2. No conductivity: the Helmholtz equation and Lecture 18's waves

$\nabla^2\tilde{\mathbf{E}} + \omega^2\mu\epsilon\tilde{\mathbf{E}} = 0$; $e^{\mp\gamma z}$ gives $\gamma = j\beta$, and phasor Faraday $\tilde H_y = \pm\tilde E_x/\eta$, $\eta = \omega\mu/\beta$. Example: $\hat y\,2\cos(2\pi\times10^8t + \tfrac{4\pi}{3}x)$ V/m in $\epsilon_r = 4$ has $\mathbf{H} = -\hat z\,10.6\cos(\ldots)$ mA/m, toward $-x$.

→ Full treatment: [[concepts/phasor-maxwell-equations|Maxwell's equations in phasor form]]

## 3. Conducting media: one replacement

$j\omega\epsilon\to\sigma + j\omega\epsilon$ in Ampère's law: $\gamma = \sqrt{j\omega\mu(\sigma + j\omega\epsilon)}$, $\eta = \sqrt{j\omega\mu/(\sigma + j\omega\epsilon)}$, $\gamma\eta = j\omega\mu$, $\gamma/\eta = \sigma + j\omega\epsilon$; complex conductivity or complex permittivity $\epsilon_c = \epsilon - j\sigma/\omega$; crossover $f = \sigma/2\pi\epsilon$ (18 kHz for Lecture 10's medium, 0.9 GHz for sea water); damped wave equation in time.

→ Full treatment: [[concepts/propagation-constant|Propagation constant]] · [[concepts/phasor-maxwell-equations|Maxwell's equations in phasor form]] (the two readings)

## 4. The damped plane wave

$\mathbf{E} = \hat x\lvert E_0\rvert e^{\mp\alpha z}\cos(\omega t\mp\beta z + \angle E_0)$, $\mathbf{H}$ divided by $\lvert\eta\rvert$ and lagging by $\tau$; $\beta$ sets $\lambda$ and the node speed $v_p$, $\alpha$ the penetration depth $\delta = 1/\alpha$ (field 37 %, power 13.5 %), $\tau$ the timing.

→ Full treatment: [[concepts/propagation-constant|Propagation constant]] · [[concepts/intrinsic-impedance|Intrinsic impedance]] (complex $\eta$) · [[concepts/skin-depth|Skin depth]]

## 5. The general formulas, and how to decode a damped wave

$\beta^2 - \alpha^2 = \omega^2\mu\epsilon$, $2\alpha\beta = \omega\mu\sigma$; closed forms for $\alpha$, $\beta$, $\lvert\eta\rvert$, $\tau = \tfrac12\tan^{-1}(\sigma/\omega\epsilon)$; six-step decoding recipe. Example: $\hat y\,6e^{-x}\cos(3\times10^8t - 3x)$ V/m gives $\gamma = 1 + j3$ m⁻¹, $\eta = 12\pi(3 + j)\ \Omega$, $\sigma = 15.9$ mS/m, $\epsilon = 8\epsilon_0$.

→ Full treatment: [[concepts/propagation-constant|Propagation constant]] · [[concepts/intrinsic-impedance|Intrinsic impedance]]

## 6. Four regimes at a glance

Perfect dielectric, imperfect dielectric ($\alpha\approx\tfrac\sigma2\sqrt{\mu/\epsilon}$), good conductor ($\gamma\approx(1 + j)\sqrt{\pi f\mu\sigma}$), perfect conductor; binomial shortcuts; $\delta$ against frequency ($(2/\sigma)\sqrt{\epsilon/\mu}$ at high $f$, $1/\sqrt{\pi f\mu\sigma}$ at low); regime from a wave ($\beta\ge\alpha$, $\lambda<2\pi\delta$); a crossover example where both shortcuts fail.

→ Full treatment: [[concepts/loss-tangent|Loss tangent]] (regimes, shortcuts) · [[concepts/skin-depth|Skin depth]] ($\delta$ against frequency) · [[concepts/propagation-constant|Propagation constant]]

## 7. Lecture 19's current sheet in a conducting medium

$j\beta\to\gamma$ in the boundary-condition argument: $\tilde{\mathbf{E}} = -\hat x\,\tfrac{\eta J_0}{2}e^{-\gamma\lvert z\rvert}$, $\tilde{\mathbf{H}} = \mp\hat y\,\tfrac{J_0}{2}e^{-\gamma\lvert z\rvert}$; both waves fade, $\mathbf{E}$ leads $\mathbf{H}$ by $\tau$, the sheet gives up $\tfrac14J_0^2\text{Re}\{\eta\}$ ($36\pi\approx113$ W/m² in §5's medium).

→ Full treatment: [[concepts/current-sheet-radiation|Radiation from a current sheet]]

## 8. When the conductivity depends on frequency

Drude $\sigma(\omega) = \sigma_{\text{DC}}/(1 + j\omega/\nu)$ in $\gamma$, $\eta$: copper stays DC-like to 1 GHz; a collisionless plasma's imaginary $\sigma$ gives Lecture 21's dispersion relation above $\omega_p$ and an evanescent, power-free field below it ($f_p\approx9$ MHz for $10^{12}$ m⁻³).

→ Full treatment: [[concepts/conductivity-and-susceptibility-models|Conductivity and susceptibility models]] · [[concepts/dispersion-relation|Dispersion relation]]

## 9. Connections

**Unit 4:** a coax with lossy filling has the medium's $\gamma$ exactly, $\sqrt{j\omega\mathcal{L}(\mathcal{G} + j\omega\mathcal{C})}$, since $\mathcal{L}\mathcal{C} = \mu\epsilon$, $\mathcal{G}/\mathcal{C} = \sigma/\epsilon$.

→ Full treatment: [[concepts/propagation-constant|Propagation constant]] (transmission-line twin)

## 10. Summary

$\partial/\partial t\to j\omega$, $j\omega\epsilon\to\sigma + j\omega\epsilon$; $\gamma\eta = j\omega\mu$, $\gamma/\eta = \sigma + j\omega\epsilon$; $\delta = 1/\alpha$; $\mathbf{H}$ lags by $\tau = \tfrac12\tan^{-1}(\sigma/\omega\epsilon)<45^\circ$; $\alpha/\beta = \tan\tau$.

> [!exam] On exams
> Examined: decode a damped wave (SP17 #3, Summer 2018 HE3 #1b, SP19 #1), $\gamma$ and $\eta$ from one lossless field (SP18 #2a–c), regime reasoning (can $\beta\ll\alpha$?), with $\gamma\eta = j\omega\mu$, $\gamma/\eta = \sigma + j\omega\epsilon$ printed on the stem. Traps: $\mu\neq\mu_0$, the sign of $\tau$, Np/m against rad/m. Methods: [[concepts/propagation-constant|Propagation constant]]; [[problems/decoding-a-damped-wave|worked problem]].

> [!tip] Practice this lecture
> [[practice/22-damped-waves-in-conducting-media|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/22-damped-waves-in-conducting-media#221-phasor-maxwell-true-or-false|22.1 Phasor Maxwell, true or false]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 22 (8 pp.): $\partial/\partial t\to j\omega$ and the margin Maxwell sets; the lossless derivation; the replacement, boxed $\gamma$, $\eta$ and margin formulas; the damped wave, $v_p$ as node speed; the four cases by binomial expansion; penetration-depth limits; the snapshot figure (redrawn). No slides were available. Rao (2009) §§5.3–5.4: closed forms for $\alpha$, $\beta$; the neper; the sheet in a material medium; dispersion. This site's own: the continuity row, divergence and $\tilde\rho$ arguments, readings of $\sigma + j\omega\epsilon$, angle identities, recipe, traps, every example (checked by `verify_L22.py`), the plasma section, the transmission-line twin, all figures. Slips in the course material: see [[0-toolkit/04-errata-in-the-course-materials|errata]].
