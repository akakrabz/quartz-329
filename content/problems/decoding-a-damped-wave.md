---
title: "Worked problem — Decoding a damped wave"
description: "A plane wave's magnetic field, H = ẑ 0.2 eˣ cos(10⁸t + 2x + 60°) A/m, in a medium with μ = 3μ₀. Read off its direction, α, β and γ; find the complex η, the electric field with its phase shift, the medium's σ and ε, and where it sits between a dielectric and a conductor. Modelled on SP17 Exam 3 #3, Summer 2018 HE3 #1b and SP19 Exam 3 #1, re-parameterized: travel along −x, a magnetic medium, α : β = 1 : 2, and H given rather than E (as only the Summer 2018 paper does)."
tags: [problem, waves]
---

*Problem · style of SP17 Exam 3 #3, Summer 2018 HE3 #1b and SP19 Exam 3 #1 · uses [[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves|Lecture 22]], [[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation|Lecture 21]] · concepts: [[concepts/propagation-constant]], [[concepts/intrinsic-impedance]], [[concepts/phasors]]*

> [!question] Problem
> A uniform plane wave travels through a homogeneous medium with permeability $\mu = 3\mu_0$ and unknown real $\epsilon$ and $\sigma$. In the region $x<0$ its magnetic field is
> $$
> \mathbf{H}(x,t) = \hat z\,0.2\,e^{x}\cos(10^8t + 2x + 60^\circ)\ \ \text{A/m},
> $$
> with $x$ in metres and $t$ in seconds. Use $\mu_0 = 4\pi\times10^{-7}$ H/m, $\epsilon_0 = 10^{-9}/36\pi$ F/m, $\gamma\eta = j\omega\mu$ and $\gamma/\eta = \sigma + j\omega\epsilon$. You may use $\tan^{-1}(1/2) = 26.57^\circ$ and $\tan^{-1}(4/3) = 53.13^\circ$.
>
> (a) Which way does the wave travel? Find $\omega$, $f$, $\alpha$, $\beta$ and $\gamma$ with units, and $\lambda$, $v_p$ and $\delta$.
>
> (b) Find $\eta$ in rectangular and polar form.
>
> (c) Write the phasor $\tilde{\mathbf{H}}(x)$. Then find the phasor $\tilde{\mathbf{E}}(x)$ and $\mathbf{E}(x,t)$, direction included.
>
> (d) Find $\sigma$, $\epsilon$ (as a multiple of $\epsilon_0$) and $\sigma/\omega\epsilon$. Is the medium an imperfect dielectric, a good conductor, or neither?
>
> (e) Check (a) by computing $\alpha$ and $\beta$ from $\sigma$, $\epsilon$ and $\mu$ with the general formulas.
>
> (f) How far does the wave travel before its amplitude falls to 10 % of its value at $x = 0$? How many wavelengths is that?

## Before writing anything: which way, and which exponential

The argument $10^8t + 2x$ has the same sign on $t$ and on $x$, so the wave travels toward $-\hat x$ (Lecture 18's reading rule). Its amplitude $0.2e^{x}$ shrinks as $x$ becomes more negative, so it decays in the direction it travels, as a wave in a passive medium must. The two readings agree, which is the first check.

In phasor form this is the $-x$ version of $e^{-\gamma z}$: the field is proportional to $e^{+\gamma x} = e^{\alpha x}e^{j\beta x}$, and $\text{Re}\{e^{j\beta x}e^{j\omega t}\}$ gives the $\cos(\omega t + \beta x)$ of the statement.

## (a) Direction, γ, and the lengths

Read the coefficients: $\omega$ multiplies $t$, $\beta$ multiplies $x$ inside the cosine, and $\alpha$ multiplies the distance travelled in the exponential.

- $\omega = 10^8$ rad/s, so $f = \omega/2\pi = 15.9$ MHz.
- $e^{x} = e^{-1\cdot\lvert x\rvert}$ for $x<0$, so $\alpha = 1$ Np/m.
- $\beta = 2$ rad/m.
- $\gamma = \alpha + j\beta = 1 + j2$ m⁻¹ $= \sqrt5\,e^{j63.43^\circ}$ m⁻¹, since $\tan^{-1}2 = 90^\circ - 26.57^\circ = 63.43^\circ$.
- $\lambda = 2\pi/\beta = \pi$ m $= 3.14$ m, $v_p = \omega/\beta = 5\times10^7$ m/s, $\delta = 1/\alpha = 1$ m.

> [!key] Answer (a)
> The wave travels toward $-\hat x$. $\omega = 10^8$ rad/s, $f = 15.9$ MHz, $\alpha = 1$ Np/m, $\beta = 2$ rad/m, $\gamma = 1 + j2$ m⁻¹ $= \sqrt5\,e^{j63.4^\circ}$ m⁻¹. $\lambda = \pi$ m $\approx3.14$ m, $v_p = 5.0\times10^7$ m/s, $\delta = 1$ m.

> [!trap] Where part (a) loses points
> - **α = −1.** The exponent is $+x$ because the wave travels toward $-x$. $\alpha$ itself is positive by definition; the sign of the exponent carries the direction.
> - **Direction from the exponential alone.** $e^{x}$ grows toward $+x$, which only says the wave *decays* toward $-x$. The cosine argument gives the direction, and the two must agree.
> - **The 60° in β.** It is a constant phase, not part of $\beta$. Keep it in degrees, or convert it to $\pi/3$, but do not mix it with $\beta x$ (radians).
> - **$v_p = c/\sqrt{\mu_r\epsilon_r}$.** That holds only in a lossless medium. Here $v_p = \omega/\beta$, read straight off the wave.

## (b) The intrinsic impedance

Use $\eta = j\omega\mu/\gamma$ with the medium's $\mu$:

$$
\begin{gathered}
\omega\mu = 10^8\times3\times4\pi\times10^{-7} = 120\pi\ \ \Omega/\text{m},\\[6pt]
\eta = \frac{j120\pi}{1 + j2} = \frac{120\pi\,j(1 - j2)}{5} = 24\pi(2 + j)\ \ \Omega .
\end{gathered}
$$

The polar form comes faster from magnitudes and angles: $\lvert\eta\rvert = \omega\mu/\lvert\gamma\rvert = 120\pi/\sqrt5 = 168.6\ \Omega$ and $\tau = 90^\circ - 63.43^\circ = 26.57^\circ$, which is also $\tan^{-1}(\alpha/\beta) = \tan^{-1}(1/2)$.

> [!key] Answer (b)
> $\eta = 24\pi(2 + j) = 150.8 + j75.4\ \Omega = 168.6\,e^{j26.6^\circ}\ \Omega$.
> Check: $\gamma\eta = (1 + j2)\times24\pi(2 + j) = 24\pi\times5j = j120\pi = j\omega\mu$ ✓.

## (c) The phasors and the electric field

**The given field as a phasor.** Keep the amplitude, the phase and the space dependence, and drop $e^{j\omega t}$:

$$
\tilde{\mathbf{H}}(x) = \hat z\,0.2\,e^{j60^\circ}e^{(1 + j2)x}\ \ \text{A/m}.
$$

Check: $\text{Re}\{\tilde{\mathbf{H}}e^{j\omega t}\} = \hat z\,0.2e^{x}\cos(10^8t + 2x + 60^\circ)$ ✓.

**E from H.** The wave travels along $\hat u = -\hat x$, and $\tilde{\mathbf{E}} = \eta\,\tilde{\mathbf{H}}\times\hat u$. The direction is $\hat z\times(-\hat x) = -\hat y$. The amplitude is multiplied by $\lvert\eta\rvert$, so $0.2\times168.6 = 33.7$ V/m, and the phase gains $\tau$, so $60^\circ + 26.57^\circ = 86.57^\circ$:

$$
\begin{gathered}
\tilde{\mathbf{E}}(x) = -\hat y\,0.2\,\eta\,e^{j60^\circ}e^{(1 + j2)x}\\[4pt]
= -\hat y\,33.7\,e^{j86.6^\circ}e^{(1 + j2)x}\ \ \text{V/m}.
\end{gathered}
$$

Two checks:
- *Direction:* $\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*\propto(-\hat y)\times\hat z = -\hat x$, the direction of travel ✓.
- *Faraday's law:* $\nabla\times\tilde{\mathbf{E}} = \hat z\,d\tilde E_y/dx = \hat z\,\gamma\tilde E_y = -\hat z\,0.2\,\gamma\eta\,e^{j60^\circ}e^{\gamma x}$. With $\gamma\eta = j\omega\mu$ this is $-j\omega\mu\tilde{\mathbf{H}}$ ✓.

> [!key] Answer (c)
> $$
> \begin{gathered}
> \tilde{\mathbf{H}} = \hat z\,0.2\,e^{j60^\circ}e^{(1 + j2)x}\ \text{A/m},\\[6pt]
> \tilde{\mathbf{E}} = -\hat y\,33.7\,e^{j86.6^\circ}e^{(1 + j2)x}\ \text{V/m},\\[6pt]
> \mathbf{E}(x,t) = -\hat y\,33.7\,e^{x}\cos(10^8t + 2x + 86.6^\circ)\ \ \text{V/m}.
> \end{gathered}
> $$
> These hold for $x<0$. $\mathbf{E}$ leads $\mathbf{H}$ by $\tau = 26.6^\circ$. The same field can be written $\hat y\,33.7\,e^{x}\cos(10^8t + 2x - 93.4^\circ)$ V/m.

> [!trap] The phase and the direction of E
> - **Subtracting τ.** Going from $\tilde{\mathbf{E}}$ to $\tilde{\mathbf{H}}$ you divide by $\eta$ and subtract $\tau$. Here you go from $\tilde{\mathbf{H}}$ to $\tilde{\mathbf{E}}$, so you multiply by $\eta$ and add $\tau$. A wrong sign gives $33.4^\circ$ instead of $86.6^\circ$.
> - **The lossless η.** $\sqrt{\mu/\epsilon}$ and $\eta_0$ are both wrong here: the first ignores $\sigma$, the second ignores the medium altogether.
> - **The sign of the direction.** $\hat z\times(-\hat x) = -\hat y$. A remembered picture of "$\mathbf{E}$ along $\hat y$ when $\mathbf{H}$ is along $\hat z$" misses that the wave travels toward $-x$.

## (d) The medium

Square $\gamma$ and divide by $j\omega\mu$; this is $\gamma/\eta$, because $\gamma/\eta = \gamma^2/(\gamma\eta)$:

$$
\begin{gathered}
\gamma^2 = (1 + j2)^2 = -3 + j4,\\[6pt]
\frac\gamma\eta = \frac{\gamma^2}{j\omega\mu} = \frac{-3 + j4}{j120\pi} = \frac{4 + j3}{120\pi} = \sigma + j\omega\epsilon .
\end{gathered}
$$

So $\sigma = 4/120\pi = 1/30\pi = 0.0106$ S/m. The imaginary part gives $\omega\epsilon = 3/120\pi$, so $\epsilon = 3/(120\pi\times10^8) = 7.96\times10^{-11}$ F/m. In units of $\epsilon_0 = 10^{-9}/36\pi$ that is exactly $9\epsilon_0$. The ratio is

$$
\frac{\sigma}{\omega\epsilon} = \frac43 = \tan53.13^\circ = \tan2\tau\ \ \checkmark
$$

A 3-4-5 triangle sits inside $\gamma^2$, which is why the numbers come out clean.

Neither shortcut of Lecture 23 is accurate at this ratio. The imperfect-dielectric formula gives $\alpha\approx(\sigma/2)\sqrt{\mu/\epsilon} = 2/\sqrt3 = 1.15$ Np/m, 15 % high. The good-conductor formula gives $\alpha\approx\beta\approx\sqrt{\omega\mu\sigma/2} = \sqrt2 = 1.41$, which is 41 % high for $\alpha$ and 29 % low for $\beta$.

> [!key] Answer (d)
> $\sigma = 1/30\pi\approx10.6$ mS/m, $\epsilon = 9\epsilon_0\approx7.96\times10^{-11}$ F/m, $\sigma/\omega\epsilon = 4/3$. The medium is **in between**: the conduction current is $4/3$ of the displacement current, so it is neither an imperfect dielectric ($\sigma/\omega\epsilon\ll1$) nor a good conductor ($\sigma/\omega\epsilon\gg1$). Only the exact formulas work here.

## (e) Check with the general formulas

Go the other way, from $\sigma$, $\epsilon$ and $\mu$ to $\alpha$ and $\beta$. First the two building blocks:

$$
\begin{gathered}
\omega\sqrt{\mu\epsilon} = 10^8\sqrt{3\mu_0\cdot9\epsilon_0} = \frac{10^8\sqrt{27}}{3\times10^8} = \sqrt3\ \ \text{rad/m},\\[6pt]
\sqrt{1 + \Big(\frac43\Big)^2} = \frac53 .
\end{gathered}
$$

Then

$$
\begin{gathered}
\alpha = \frac{\sqrt3}{\sqrt2}\Big[\frac53 - 1\Big]^{1/2} = \frac{\sqrt3}{\sqrt2}\sqrt{\frac23} = 1\ \text{Np/m}\ \checkmark,\\[6pt]
\beta = \frac{\sqrt3}{\sqrt2}\Big[\frac53 + 1\Big]^{1/2} = \frac{\sqrt3}{\sqrt2}\sqrt{\frac83} = 2\ \text{rad/m}\ \checkmark,\\[6pt]
\lvert\eta\rvert = \frac{\sqrt{\mu/\epsilon}}{(25/9)^{1/4}} = \frac{120\pi/\sqrt3}{\sqrt{5/3}} = \frac{120\pi}{\sqrt5}\ \checkmark,\\[6pt]
\tau = \tfrac12\tan^{-1}\tfrac43 = 26.57^\circ\ \checkmark .
\end{gathered}
$$

> [!key] Answer (e)
> The general formulas return $\alpha = 1$ Np/m, $\beta = 2$ rad/m, $\lvert\eta\rvert = 168.6\ \Omega$ and $\tau = 26.6^\circ$, the values read off the wave.

## (f) How far the wave gets

The amplitude is $0.2e^{x}$ A/m, and it falls to 10 % of its $x = 0$ value where $e^{x} = 0.1$, at $x = -\ln10 = -2.30$ m. That is $2.30/\pi = 0.73$ wavelengths. Over one full wavelength the amplitude is multiplied by $e^{-\alpha\lambda} = e^{-\pi} = 0.043$.

> [!key] Answer (f)
> 2.30 m, about $0.73\lambda$. A full wavelength takes the amplitude down to 4.3 %. This is between the two limits: an imperfect dielectric keeps nearly all of it over a wavelength, and a good conductor keeps $e^{-2\pi} = 0.19\,\%$.

## Variant: the μ = μ₀ trap

Suppose you overlook $\mu = 3\mu_0$ and use $\mu_0$. Then $\omega\mu_0 = 40\pi$ and $\eta = j40\pi/(1 + j2) = 8\pi(2 + j)$, with $\lvert\eta\rvert = 56.2\ \Omega$, three times too small. $\mathbf{E}$ comes out three times too small (11.2 V/m). From (d), $\sigma = 4/40\pi = 31.8$ mS/m and $\epsilon = 27\epsilon_0$, both three times too large. Two things survive: $\tau = 26.6^\circ$, and $\sigma/\omega\epsilon = 4/3$. Neither contains $\mu$, so the regime verdict comes out right, but every magnitude in (b)–(d) is off by the factor $\mu_r$.

## The pattern behind this problem

1. **Read** the direction from the signs, then $\omega$, $\beta$ and $\alpha$, giving $\gamma = \alpha + j\beta$.
2. **η** $= j\omega\mu/\gamma$, with the medium's $\mu$. In polar form, $\lvert\eta\rvert = \omega\mu/\lvert\gamma\rvert$ and $\tau = \tan^{-1}(\alpha/\beta)$.
3. **The other field** from $\tilde{\mathbf{H}} = \hat u\times\tilde{\mathbf{E}}/\eta$ or $\tilde{\mathbf{E}} = \eta\,\tilde{\mathbf{H}}\times\hat u$. Use the cross product for the direction, and $\pm\tau$ for the phase.
4. **The medium** from $\gamma^2/j\omega\mu = \sigma + j\omega\epsilon$, and the regime from $\sigma/\omega\epsilon = 2\alpha\beta/(\beta^2 - \alpha^2)$.

This is the recipe of [[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves#5-the-general-formulas-and-how-to-decode-a-damped-wave|Lecture 22 §5]]. Each exam instance runs part of it with its own numbers:

- SP17 Exam 3 #3 gives $\mathbf{E}$ in a non-magnetic medium, travelling toward $+x$, with $\gamma$ itself on a 3-4-5 triangle.
- Summer 2018 HE3 #1b gives a time-domain $\mathbf{H}$ with $\mu_0$, travelling toward $+z$, with $\alpha:\beta = 1:\sqrt3$.
- SP19 Exam 3 #1 gives a phasor $\tilde{\mathbf{E}}$ with $\mu = 2\mu_0$, travelling toward $+y$, also with $\alpha:\beta = 1:\sqrt3$.

This version travels toward $-x$, in a medium with $\mu_r = 3$. Its $\alpha:\beta = 1:2$ puts the 3-4-5 triangle into $\gamma^2$ rather than $\gamma$, and it adds the general-formula check and the decay distance.
