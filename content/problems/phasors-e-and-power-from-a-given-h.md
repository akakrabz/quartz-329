---
title: "Worked problem — Phasors, E and power from a given H"
description: "A plane wave in a lossless, non-magnetic dielectric is given by its magnetic field: a cosine plus a phase-shifted sine, travelling toward −z. Read off f, λ, vₚ, the direction, εr and η; write the phasor H̃; get Ẽ by multiplying by η and rotating; return to E(z,t); and find the time-average power, term by term and through a window. Modelled on Summer 2019 HE3 #1a and SP17 Exam 3 #4, re-parameterized: H is given instead of E, the medium is a dielectric, the wave travels along −z, and the amplitudes and phases are new."
tags: [problem, waves]
---

*Problem · style of Summer 2019 HE3 #1a and SP17 Exam 3 #4 · uses [[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation|Lecture 21]], [[3-maxwell-and-waves/20-poynting-theorem-and-monochromatic-waves|Lecture 20]], [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves|Lecture 18]] · concepts: [[concepts/phasors]], [[concepts/plane-waves]], [[concepts/intrinsic-impedance]], [[concepts/poynting-vector]]*

> [!question] Problem
> A uniform plane wave travels through a lossless, non-magnetic dielectric. Its magnetic field is
> $$
> \begin{gathered}
> \mathbf{H}(z, t) = 0.3\cos(2\pi\times10^8\,t + 2\pi z)\,\hat x\\
> - 0.4\sin\big(2\pi\times10^8\,t + 2\pi z - \tfrac\pi4\big)\,\hat y\ \ \text{A/m},
> \end{gathered}
> $$
> with $t$ in seconds and $z$ in metres. Use $c = 3\times10^8$ m/s and $\eta_0 = 120\pi\ \Omega$.
>
> (a) Find $f$, $T$, $\lambda$, $v_p$ and the direction of travel. Then find $\epsilon_r$ and $\eta$.
>
> (b) Write the phasor $\tilde{\mathbf{H}}(z)$.
>
> (c) Find the phasor $\tilde{\mathbf{E}}(z)$, and check that $\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*$ points along the travel.
>
> (d) Write $\mathbf{E}(z, t)$.
>
> (e) Find the time-average power density carried by each of the two terms of $\mathbf{H}$ on its own, and by the whole wave.
>
> (f) How much time-average power crosses a 50 cm × 50 cm window in the plane $z = -3$ m? Find the instantaneous Poynting vector at the origin at $t = 0$, and compare it with the average.

## Before writing anything: decode the expression

Both terms share the phase $\phi = 2\pi\times10^8\,t + 2\pi z$, so this is one wave with two perpendicular components, not two waves. The coefficient of $t$ is $\omega$, the coefficient of $z$ is $\beta$, and the relative sign of the two terms gives the direction ([[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation#1-monochromatic-waves-one-frequency-two-periodicities|Lecture 21 §1]]). The sine and the $-\pi/4$ only affect the phase of the $\hat y$ component.

## (a) Frequency, wavelength, speed, direction and medium

- $\omega = 2\pi\times10^8$ rad/s, so $f = 100$ MHz and $T = 1/f = 10$ ns.
- $\beta = 2\pi$ rad/m, so $\lambda = 2\pi/\beta = 1$ m.
- $v_p = \omega/\beta = 10^8$ m/s. Check: $\lambda f = 1\ \text{m}\times10^8\ \text{Hz}$.
- The $t$ and $z$ terms have the **same** sign, so the wave travels toward $-z$: $\hat u = -\hat z$.

In a non-magnetic medium $c/v_p = \sqrt{\mu_r\epsilon_r} = \sqrt{\epsilon_r}$:

> [!key] Answer (a)
> $f = 100$ MHz, $T = 10$ ns, $\lambda = 1$ m, $v_p = 1.0\times10^8$ m/s $= c/3$, travelling toward $-\hat z$.
> $$
> \begin{gathered}
> \sqrt{\epsilon_r} = \frac{c}{v_p} = 3\ \Rightarrow\ \epsilon_r = 9,\\[4pt]
> \eta = \frac{\eta_0}{\sqrt{\epsilon_r}} = \frac{120\pi}{3} = 40\pi\approx125.7\ \Omega .
> \end{gathered}
> $$

> [!trap] Where part (a) loses points
> - Reading "$+2\pi z$" as travel toward $+z$. Opposite signs of the $t$ and $z$ terms mean $+z$; the same signs mean $-z$.
> - Using $\eta_0$. The wave is in a dielectric, so $\eta = \eta_0/\sqrt{\epsilon_r}$.
> - Forgetting what "non-magnetic" buys you. A speed gives only $\mu_r\epsilon_r = 9$; it takes $\mu_r = 1$ to conclude $\epsilon_r = 9$ (see the variant at the end).

## (b) The phasor H̃

Convert term by term ([[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation#3-phasors-a-rotating-arrow-and-its-shadow|Lecture 21 §3]]). The $\hat x$ term is a cosine with phase $+2\pi z$: its phasor is $0.3e^{j2\pi z}$. The $\hat y$ term is minus a sine. A sine picks up $-j$, so
$$
\begin{gathered}
-0.4\sin\big(\omega t + 2\pi z - \tfrac\pi4\big)\\
\updownarrow\\
-0.4\,(-j)\,e^{-j\pi/4}e^{j2\pi z} = 0.4\,j\,e^{-j\pi/4}e^{j2\pi z}\\
= 0.4\,e^{j\pi/4}e^{j2\pi z},
\end{gathered}
$$
because $j = e^{j\pi/2}$ and $\pi/2 - \pi/4 = \pi/4$.

> [!key] Answer (b)
> $$
> \tilde{\mathbf{H}}(z) = \big(0.3\,\hat x + 0.4\,e^{j\pi/4}\,\hat y\big)\,e^{j2\pi z}\ \ \text{A/m}.
> $$
> Spot check at $z = 0$, $t = 0$: the given $H_y$ is $-0.4\sin(-\pi/4) = +0.283$ A/m, and $\text{Re}\{0.4e^{j\pi/4}\} = 0.4\cos(\pi/4) = 0.283$ A/m ✓. In cosine form, $H_y = 0.4\cos(\omega t + 2\pi z + \pi/4)$: the $\hat y$ component leads the $\hat x$ component by 45°.

> [!trap] Two sign flips in one term
> The minus in front and the $-j$ of the sine cancel to $+j$, and $j\,e^{-j\pi/4} = e^{+j\pi/4}$. Drop the minus and you get $0.4e^{-j3\pi/4}$; forget the $-j$ and you get $0.4e^{+j3\pi/4}$; forget both and you get $0.4e^{-j\pi/4}$. Each is off by 90° or 180°, and one spot check at a convenient instant catches all three.

## (c) The phasor Ẽ: multiply by η and rotate

For one wave in a lossless medium, $\tilde{\mathbf{E}} = \eta\,\tilde{\mathbf{H}}\times\hat u$ with $\hat u = -\hat z$ ([[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation#5-the-partner-field-divide-by-η-and-rotate|Lecture 21 §5]]). The two unit vectors rotate as
$$
\begin{gathered}
\hat x\times(-\hat z) = -(\hat x\times\hat z) = +\hat y,\\[2pt]
\hat y\times(-\hat z) = -(\hat y\times\hat z) = -\hat x .
\end{gathered}
$$
The complex factors ride along unchanged, because $\eta$ is real.

> [!key] Answer (c)
> $$
> \begin{aligned}
> \tilde{\mathbf{E}}(z) &= 40\pi\,\big(0.3\,\hat y - 0.4\,e^{j\pi/4}\,\hat x\big)\,e^{j2\pi z}\\
> &= \big(-16\pi\,e^{j\pi/4}\,\hat x + 12\pi\,\hat y\big)\,e^{j2\pi z}\ \ \text{V/m},
> \end{aligned}
> $$
> that is, about $\big(-50.3\,e^{j\pi/4}\hat x + 37.7\,\hat y\big)e^{j2\pi z}$ V/m. Check the direction with the complex Poynting vector. Of the four cross products in $\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*$, the two with $\hat x\times\hat x$ and $\hat y\times\hat y$ vanish, and the phase factors cancel in the other two:
> $$
> \begin{aligned}
> \tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^* &= 40\pi\big[(0.3)^2\,\hat y\times\hat x - (0.4)^2\,\hat x\times\hat y\big]\\
> &= -40\pi\,(0.25)\,\hat z = -10\pi\,\hat z\ \ \text{W/m}^2,
> \end{aligned}
> $$
> along $-\hat z$ ✓. Also $\lvert\tilde{\mathbf{E}}\rvert/\lvert\tilde{\mathbf{H}}\rvert = 20\pi/0.5 = 40\pi = \eta$ ✓.

> [!trap] Rotating the wrong way
> Using $\hat u = +\hat z$ (or $\hat z\times\tilde{\mathbf{H}}$) flips both components of $\tilde{\mathbf{E}}$, and then $\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*$ comes out along $+\hat z$, against the travel found in (a). The check costs one line; do it.

## (d) Back to the time domain

Multiply by $e^{j\omega t}$ and take the real part, term by term. With $\omega = 2\pi\times10^8$ rad/s:

> [!key] Answer (d)
> $$
> \begin{aligned}
> \mathbf{E}(z, t) = &-16\pi\cos\big(\omega t + 2\pi z + \tfrac\pi4\big)\,\hat x\\
> &+ 12\pi\cos(\omega t + 2\pi z)\,\hat y\ \ \text{V/m},
> \end{aligned}
> $$
> with amplitudes $16\pi\approx50.3$ V/m and $12\pi\approx37.7$ V/m. Cross-check in the time domain: $\eta\,\mathbf{H}\times(-\hat z)$ applied to the cosine form of $\mathbf{H}$ gives the same two terms.

## (e) Time-average power

Use $\langle\mathbf{S}\rangle = \tfrac12\text{Re}\{\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*\}$ ([[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation#7-time-averages-straight-from-phasors|Lecture 21 §7]]). From (c), $\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^* = -10\pi\,\hat z$, so the whole wave carries $-5\pi\,\hat z$ W/m². Term by term, for one wave in a lossless medium $\langle\mathbf{S}\rangle = \tfrac12\eta\lvert\tilde H_0\rvert^2\,\hat u$:

| part of $\mathbf{H}$ | amplitude | $\tfrac12\eta\lvert\tilde H\rvert^2$ |
|---|---|---|
| the $\hat x$ term alone | 0.3 A/m | $\tfrac12(40\pi)(0.09) = 1.8\pi\approx5.65$ W/m² |
| the $\hat y$ term alone | 0.4 A/m | $\tfrac12(40\pi)(0.16) = 3.2\pi\approx10.05$ W/m² |
| the whole wave | $\lvert\tilde{\mathbf{H}}\rvert = 0.5$ A/m | $\tfrac12(40\pi)(0.25) = 5\pi\approx15.71$ W/m² |

> [!key] Answer (e)
> $\langle\mathbf{S}\rangle_x = -1.8\pi\,\hat z\approx-5.65\,\hat z$ W/m², $\langle\mathbf{S}\rangle_y = -3.2\pi\,\hat z\approx-10.05\,\hat z$ W/m², and the whole wave carries $\langle\mathbf{S}\rangle = -5\pi\,\hat z\approx-15.7\,\hat z$ W/m², the sum of the two. The powers of perpendicular components add because their cross terms contain $\hat x\times\hat x$ and $\hat y\times\hat y$, which vanish whatever the 45° phase between them. Lecture 20's route agrees: here $\mathbf{S} = -\eta\lvert\mathbf{H}\rvert^2\hat z$ at every instant, and $\langle\lvert\mathbf{H}\rvert^2\rangle = \tfrac12(0.3^2 + 0.4^2) = 0.125$ (A/m)².

> [!trap] Power slips
> - Dropping the $\tfrac12$: $\eta\lvert\tilde{\mathbf{H}}\rvert^2 = 10\pi$ is the size of $\tilde{\mathbf{S}}$, not of $\langle\mathbf{S}\rangle$.
> - Adding amplitudes before squaring: $(0.3 + 0.4)^2 = 0.49$, not $0.3^2 + 0.4^2 = 0.25$.
> - Giving the power as a positive number with no direction. It flows toward $-\hat z$.

## (f) Through a window, and at one instant

The window has area $0.25$ m² and faces along $\pm\hat z$. In a lossless medium $\langle\mathbf{S}\rangle$ is the same at every $z$, so the plane $z = -3$ m makes no difference:
$$
\langle P\rangle = \lvert\langle\mathbf{S}\rangle\rvert\times A = 5\pi\times0.25 = 1.25\pi\approx3.93\ \text{W},
$$
crossing toward $-z$.

At the origin at $t = 0$, $\phi = 0$:
$$
\begin{aligned}
\mathbf{H}(0, 0) &= 0.3\,\hat x - 0.4\sin(-\tfrac\pi4)\,\hat y\\
&= 0.300\,\hat x + 0.283\,\hat y\ \ \text{A/m},\\[4pt]
\mathbf{E}(0, 0) &= -16\pi\cos\tfrac\pi4\,\hat x + 12\pi\,\hat y\\
&= -35.5\,\hat x + 37.7\,\hat y\ \ \text{V/m}.
\end{aligned}
$$
Then
$$
\begin{gathered}
\mathbf{S} = \mathbf{E}\times\mathbf{H}\\
= (-35.5)(0.283)\,\hat x\times\hat y + (37.7)(0.300)\,\hat y\times\hat x\\
= (-10.05 - 11.31)\,\hat z = -21.4\,\hat z\ \ \text{W/m}^2 .
\end{gathered}
$$

> [!key] Answer (f)
> $\langle P\rangle\approx3.93$ W through the window. At the origin at $t = 0$, $\mathbf{S} = -21.4\,\hat z$ W/m², larger than the average $-15.7\,\hat z$ W/m². The instantaneous value is $-\eta\lvert\mathbf{H}(t)\rvert^2\hat z$; it pulses at twice the frequency between about $-4.2$ and $-27.2$ W/m² and averages to $-5\pi$. It never reverses, because a single travelling wave always carries energy forward. It never drops to zero either, because the two components are not in phase: when one passes through zero the other does not.

## Variant: the same H in a magnetic medium

Suppose the medium had $\mu_r = 4$ and $\epsilon_r = 2.25$. Then $\mu_r\epsilon_r = 9$, so $\omega$, $\beta$, $\lambda$, $v_p$ and the direction are exactly as in (a): **the expression cannot tell the two media apart.** But $\eta = \eta_0\sqrt{\mu_r/\epsilon_r} = 120\pi\times\tfrac43 = 160\pi\approx503\ \Omega$, four times the non-magnetic value. $\tilde{\mathbf{E}}$ is four times larger, and so is the power: $\langle\mathbf{S}\rangle = -20\pi\,\hat z\approx-62.8\,\hat z$ W/m². The speed fixes the product $\mu_r\epsilon_r$, while $\eta$ needs the ratio $\mu_r/\epsilon_r$. SP17 Exam 3 #2(iii) uses a magnetic material for exactly this reason.

## The pattern behind this problem

1. Decode the phase: $\omega$, $\beta$, and the direction from the relative sign.
2. Phasor, term by term: a sine picks up $-j$, a minus sign is a factor $-1$, and extra phases become $e^{j\theta}$.
3. Partner field: $\tilde{\mathbf{E}} = \eta\tilde{\mathbf{H}}\times\hat u$ (or $\tilde{\mathbf{H}} = \hat u\times\tilde{\mathbf{E}}/\eta$), checked by $\tilde{\mathbf{E}}\times\tilde{\mathbf{H}}^*\parallel\hat u$.
4. Power: $\tfrac12\eta\lvert\tilde{\mathbf{H}}\rvert^2$ or $\lvert\tilde{\mathbf{E}}\rvert^2/2\eta$ along $\hat u$. Perpendicular components add their powers, whatever their phases.

The exam instances follow the same four steps. Summer 2019 HE3 #1a gives a free-space $\mathbf{E}$ with a $\hat y$ cosine and a $\hat z$ sine of $(\omega t + \beta x)$, and asks for $\tilde{\mathbf{E}}$, $\tilde{\mathbf{H}}$, the direction, the power of one component and then of the whole wave. SP17 Exam 3 #4a–b gives a cosine and a phase-shifted sine in symbols. Neither key is reproduced here; the numbers, medium, direction and given field above are different.
