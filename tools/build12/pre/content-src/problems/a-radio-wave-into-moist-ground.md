---
title: "Worked problem — A radio wave into moist ground"
description: "A 100 kHz plane wave travels straight down into moist soil (σ = 10⁻² S/m, εr = 10). Classify the soil, find δ, λ, vₚ and η, write E and H with real cosines, find the time-average power at the surface and 25 m down, the loss in dB per metre and the depth where 1 % of the power is left, and pick a frequency that meets a 40 dB budget over 100 m. Modelled on Summer 2018 and 2019 HE3 #3b, re-parameterized with a new medium, frequency and direction of travel."
tags: [problem, waves]
---

*Problem · style of Summer 2018 HE3 #3b and Summer 2019 HE3 #3b (classify, then compute) · uses [[3-maxwell-and-waves/23-imperfect-dielectrics-and-good-conductors|Lecture 23]], [[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves|Lecture 22]], [[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation|Lecture 21]] · concepts: [[concepts/loss-tangent]], [[concepts/skin-depth]], [[concepts/intrinsic-impedance]], [[concepts/poynting-vector]]*

> [!question] Problem
> A uniform plane wave of frequency $f = 100$ kHz travels straight down into flat, moist ground. Let $\hat y$ point up, with the surface at $y = 0$ and soil filling $y<0$: $\mu = \mu_0$, $\epsilon = 10\epsilon_0$, $\sigma = 10^{-2}$ S/m. Just below the surface the electric field phasor is $\tilde{\mathbf{E}}(0) = \hat x$ 1 V/m. Use $\epsilon_0\approx10^{-9}/36\pi$ F/m and $\mu_0 = 4\pi\times10^{-7}$ H/m; parts (a)–(c) need no calculator.
>
> (a) Is the soil an imperfect dielectric or a good conductor at 100 kHz? Why?
>
> (b) Find $\alpha$, $\beta$, the skin depth $\delta$, the wavelength $\lambda$ and the phase velocity $v_p$ in the soil.
>
> (c) Find $\eta$, magnitude and phase. Write the phasors $\tilde{\mathbf{E}}(y)$ and $\tilde{\mathbf{H}}(y)$ for $y\le0$, and the real fields $\mathbf{E}(y,t)$ and $\mathbf{H}(y,t)$.
>
> (d) Find the time-average Poynting vector at the surface and 25 m down. What is the loss in dB per metre, and at what depth is the power 1 % of its surface value?
>
> (e) A sensor buried 100 m down can tolerate a total loss of 40 dB in the soil. What is the highest frequency that works? Is the soil still a good conductor there, and what does going lower cost?

## Before writing anything: the regime picks the formulas

Every formula in parts (b)–(d) depends on which row of the Lecture 23 table applies, so the classification comes first. The wave travels toward $-\hat y$ (down). Its phasor therefore carries $e^{+\gamma y} = e^{\alpha y}e^{j\beta y}$, which shrinks as $y$ becomes more negative. Distances into the soil are $d = -y$.

## (a) Classify

The loss tangent at 100 kHz, using $\epsilon_0\approx10^{-9}/36\pi$:

$$
\begin{gathered}
\frac{\sigma}{\omega\epsilon} = \frac{\sigma\cdot36\pi\times10^{9}}{2\pi f\,\epsilon_r}\\[4pt]
= \frac{18\times10^{9}\times10^{-2}}{10^{5}\times10} = 180\gg1 .
\end{gathered}
$$

> [!key] Answer (a)
> A **good conductor**. The conduction current is 180 times the displacement current. (With $\epsilon_0 = 8.854\times10^{-12}$ F/m the ratio is 179.75.) In relaxation-time terms, $\epsilon/\sigma = 8.9$ ns, against a period of 10 µs.

> [!trap] Where part (a) loses points
> - Using $\epsilon_0$ instead of $10\epsilon_0$ gives 1,800. That happens to give the same verdict here, but not near the crossover frequency, which is 18 MHz for this soil.
> - Using $f$ instead of $\omega$ makes the ratio $2\pi$ times too large, 1,130.
> - Calling soil "a dielectric" because it is not a metal. Only the ratio decides.

## (b) α, β, δ, λ and the phase velocity

In a good conductor $\alpha = \beta = \sqrt{\pi f\mu\sigma}$:

$$
\begin{gathered}
\pi f\mu_0\sigma = \pi\cdot10^{5}\cdot4\pi\times10^{-7}\cdot10^{-2} = 4\pi^2\times10^{-4}\\[4pt]
\Longrightarrow\quad\alpha = \beta = 2\pi\times10^{-2} = 0.0628\ \text{m}^{-1}.
\end{gathered}
$$

> [!key] Answer (b)
> $$
> \begin{gathered}
> \alpha = 0.0628\ \text{Np/m},\qquad \beta = 0.0628\ \text{rad/m},\\[4pt]
> \delta = \frac{1}{0.02\pi} = \frac{50}{\pi} = 15.9\ \text{m},\\[4pt]
> \lambda = 2\pi\delta = 100\ \text{m},\qquad v_p = \lambda f = 10^{7}\ \text{m/s}.
> \end{gathered}
> $$
> Equivalently $v_p = \omega\delta = 2\pi\times10^{5}\times50/\pi = 10^{7}$ m/s, which is $c/30$. The exact Lecture 22 formulas give $\delta = 15.96$ m and $\lambda = 99.7$ m, within 0.3 %. If the soil had no conductivity, the same $\epsilon_r = 10$ would give $\lambda = c/(f\sqrt{10})\approx950$ m. Conduction shortens the wavelength almost tenfold and slows the wave just as much.

## (c) η and the fields

$$
\begin{gathered}
\lvert\eta\rvert = \sqrt{\frac{\omega\mu_0}{\sigma}} = \sqrt{\frac{2\pi\times10^{5}\cdot4\pi\times10^{-7}}{10^{-2}}}\\[4pt]
= \sqrt{8\pi^2} = 2\sqrt2\,\pi = 8.89\ \Omega,\qquad \tau = 45^\circ .
\end{gathered}
$$

Check with the compact form: $\sigma\delta = 10^{-2}\times50/\pi = 1/(2\pi)$ S, so $\eta = (1+j)/(\sigma\delta) = 2\pi(1+j)\ \Omega$, whose magnitude is $2\sqrt2\,\pi$ ✓.

The magnetic field comes from $\tilde{\mathbf{H}} = \hat u\times\tilde{\mathbf{E}}/\eta$ with $\hat u = -\hat y$. Since $(-\hat y)\times\hat x = -(\hat y\times\hat x) = +\hat z$, $\tilde{\mathbf{H}}$ points along $+\hat z$.

> [!key] Answer (c)
> $$
> \begin{gathered}
> \eta = 2\pi(1+j) = 8.89\,e^{j\pi/4}\ \Omega,\\[4pt]
> \tilde{\mathbf{E}}(y) = \hat x\,e^{\alpha y}e^{j\beta y}\ \text{V/m}\qquad(y\le0),\\[4pt]
> \tilde{\mathbf{H}}(y) = \hat z\,\frac{1}{2\sqrt2\,\pi}\,e^{-j\pi/4}\\[2pt]
> \times e^{\alpha y}e^{j\beta y}\ \text{A/m},\\[4pt]
> \mathbf{E}(y,t) = \hat x\,e^{\alpha y}\cos(\omega t + \beta y)\ \text{V/m},\\[4pt]
> \mathbf{H}(y,t) = \hat z\,0.1125\,e^{\alpha y}\\[2pt]
> \times\cos\Big(\omega t + \beta y - \frac\pi4\Big)\ \text{A/m},
> \end{gathered}
> $$
> with $\omega = 2\pi\times10^{5}$ rad/s, $\alpha = \beta = 0.0628$ m⁻¹ and $y$ in metres. Direction check: $\hat x\times\hat z = -\hat y$, down ✓. $\mathbf{H}$ lags $\mathbf{E}$ by 45°, an eighth of a period (1.25 µs).

> [!trap] Signs in part (c)
> - The exponent. A downward wave is $e^{+\gamma y}$; writing $e^{-\gamma y}$ would make it grow with depth and travel up.
> - The direction of $\mathbf{H}$. Rotate with $\hat u = -\hat y$, not $+\hat y$, and confirm with $\mathbf{E}\times\mathbf{H}$.
> - The phase. $1/\eta = e^{-j\pi/4}/\lvert\eta\rvert$, so $\mathbf{H}$ *lags*: $-\pi/4$ inside its cosine.

## (d) Power at the surface and below

$$
\begin{gathered}
\langle\mathbf{S}\rangle = \tfrac12\text{Re}\{\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*\} = \tfrac12\,(\hat x\times\hat z)\,\text{Re}\Big\{\frac{1}{\eta^*}\Big\}\,e^{2\alpha y}\\[4pt]
= -\hat y\,\frac{\cos\tau}{2\lvert\eta\rvert}\,e^{2\alpha y} = -\hat y\,\frac{1}{8\pi}\,e^{2\alpha y}\ \ \text{W/m}^2,
\end{gathered}
$$

because $\cos\tau/(2\lvert\eta\rvert) = (1/\sqrt2)/(4\sqrt2\,\pi) = 1/(8\pi)$.

- At the surface: $1/(8\pi) = 39.8$ mW/m², downward.
- At $y = -25$ m: $e^{2\alpha y} = e^{-2\times0.02\pi\times25} = e^{-\pi} = 0.043$, so 1.72 mW/m². Only 4.3 % is left.
- Loss in dB: $8.686\,\alpha = 8.686\times0.0628 = 0.546$ dB per metre, the same number for the field and for the power. At 25 m that is 13.6 dB, and $10\log_{10}e^{\pi} = 13.6$ ✓.
- 1 % of the power: $e^{-2\alpha d} = 0.01$ gives $d = \ln100/(2\alpha) = 4.605/0.1257 = 36.6$ m, or $20\ \text{dB}/0.546$ dB/m.

> [!key] Answer (d)
> $\langle\mathbf{S}\rangle = -\hat y\,39.8\,e^{2\alpha y}$ mW/m²: 39.8 mW/m² at the surface and 1.72 mW/m² 25 m down. The loss is 0.546 dB/m. The power is down to 1 % at 36.6 m, where the field is down to 10 %.

**Where did the missing power go?** Into heat in the soil. At depth $s$ the field amplitude is $e^{-\alpha s}$ V/m, so between the surface and 25 m the Joule heating per unit area of ground is

$$
\begin{gathered}
\int_0^{25\ \text{m}}\tfrac12\sigma\,e^{-2\alpha s}\,ds = \tfrac12\sigma\,\frac{1 - e^{-\pi}}{2\alpha}\\[4pt]
= \frac{0.005\times0.957}{0.1257} = 38.1\ \text{mW/m}^2,
\end{gathered}
$$

which is exactly $39.8 - 1.7$ mW/m² ✓. This is the time-averaged Poynting theorem of Lecture 20.

<!-- fig:cond-problem-depth -->

## (e) A frequency for 40 dB at 100 m

The budget allows $40/100 = 0.4$ dB/m, so $\alpha\le0.4/8.686 = 0.0461$ Np/m. In a good conductor $\alpha = \sqrt{\pi f\mu\sigma}$, so

$$
f\le\frac{\alpha^2}{\pi\mu_0\sigma} = \frac{(0.0461)^2}{\pi\cdot4\pi\times10^{-7}\cdot10^{-2}} = 53.7\ \text{kHz}.
$$

A quicker route uses the $\sqrt f$ scaling. At 100 kHz, 100 m is exactly one wavelength, so it costs the $54.6$ dB that any good conductor charges per wavelength. To bring that down to 40 dB, the frequency must fall by $(40/54.6)^2 = 0.537$.

> [!key] Answer (e)
> At most **53.7 kHz**. There $\sigma/\omega\epsilon = 180\times100/53.7 = 335$, so the soil is still a good conductor and the formula applies. (The exact $\alpha$ gives 39.9 dB at 100 m.) The cost is the one the notes name for submarines: a lower carrier carries less bandwidth, so data are slower. The antenna also grows, since the free-space wavelength rises from 3.0 km to 5.6 km.

## Variant: the same soil at 10 MHz

Now $\sigma/\omega\epsilon = 1.8$: **neither** regime applies, and the exact Lecture 22 formulas (or the polar forms of Lecture 23 §2) are needed. With $\theta = \tan^{-1}1.8 = 60.9^\circ$, $\tau = \theta/2 = 30.5^\circ$, $\lvert\eta\rvert = 83.1\ \Omega$, $\alpha = 0.482$ Np/m (4.18 dB/m) and $\beta = 0.819$ rad/m. The good-conductor formula would give $\alpha = 0.628$ Np/m, 30 % too high. The imperfect-dielectric formula would give 0.596 Np/m, 24 % too high. Note too that $\alpha<\beta$ still holds, as it must, since $\alpha/\beta = \tan30.5^\circ = 0.59$.

## The pattern behind this problem

1. Compute $\sigma/\omega\epsilon$ with the medium's $\epsilon$; it picks the formulas.
2. In a good conductor everything follows from $\delta = 1/\sqrt{\pi f\mu\sigma}$: $\alpha = \beta = 1/\delta$, $\lambda = 2\pi\delta$, $v_p = \omega\delta$, $\eta = (1+j)/(\sigma\delta)$.
3. $\tilde{\mathbf{H}} = \hat u\times\tilde{\mathbf{E}}/\eta$, so $\mathbf{H}$ lags by $\tau$. Check $\mathbf{E}\times\mathbf{H}$.
4. $\langle\mathbf{S}\rangle = \hat u\,\lvert E_0\rvert^2\cos\tau\,e^{-2\alpha d}/(2\lvert\eta\rvert)$. Use $e^{-2\alpha d}$ for power, and $8.686\,\alpha$ for dB per metre.

The exam instance (Summer 2018 HE3 #3b, repeated in 2019) uses seawater, $\epsilon = 81\epsilon_0$ and $\sigma = 4$ S/m, at 1 kHz, with the wave travelling toward $-z$. It asks for the same classification, $\delta$ without a calculator, $\lambda$, $v_p$, and the power density 10 m in given the surface value. The steps are the four above; the numbers are the notes' Example 3, worked on the [[3-maxwell-and-waves/23-imperfect-dielectrics-and-good-conductors|Lecture 23]] page.
