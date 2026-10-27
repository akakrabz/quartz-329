---
title: "Worked problem — Working back from a transmitted wave"
description: "A 50 MHz wave in vacuum travels toward −x onto a magnetic dielectric, and only the transmitted H is given: find Γ, τ, every phasor, the power balance, and the perfect-conductor case. Modelled on Summer 2017 HE3 #3, SP18 Exam 3 #2 and SP19 Exam 3 #3b."
tags: [problem, waves]
---

*Problem · style of Summer 2017 HE3 #3, SP18 Exam 3 #2 and SP19 Exam 3 #3b · uses [[3-maxwell-and-waves/25-wave-reflection-and-transmission|Lecture 25]], [[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation|Lecture 21]] · concepts: [[concepts/reflection-and-transmission]], [[concepts/intrinsic-impedance]]*

> [!question] Problem
> The region $x>0$ is vacuum. The region $x<0$ is a lossless medium with $\mu = 4\mu_0$ and $\epsilon = 2.25\epsilon_0$. A uniform plane wave at $f = 50$ MHz travels through the vacuum toward $-\hat x$ and meets the interface $x = 0$. The transmitted magnetic field in $x<0$ is
> $$
> \mathbf{H}_t(x,t) = \hat z\,\frac{1}{10\pi}\cos(\omega t + \pi x)\ \ \text{A/m}.
> $$
> Use $\eta_0 = 120\pi\ \Omega$ and $c = 3\times10^8$ m/s.
>
> (a) Find $\eta$ and $\beta$ on both sides. Which side is region 1, and which way does $\hat n$ point?
>
> (b) Find $\Gamma$ and $\tau$.
>
> (c) Find $\tilde{\mathbf{E}}_t(x)$, then the incident $\tilde{\mathbf{E}}_i(x)$ and the reflected $\tilde{\mathbf{E}}_r(x)$.
>
> (d) Find $\tilde{\mathbf{H}}_i(x)$ and $\tilde{\mathbf{H}}_r(x)$, and check the boundary condition on tangential $\tilde{\mathbf{H}}$.
>
> (e) Find $\langle\mathbf{S}\rangle$ of all three waves and check the power balance.
>
> (f) The medium in $x<0$ is replaced by a perfect conductor; the incident wave is unchanged. Find $\tilde{\mathbf{E}}_r(x)$ and the surface current $\mathbf{J}_s(t)$.

## (a) Impedances and wavenumbers

$$
\begin{gathered}
\eta_1 = \eta_0 = 120\pi\ \Omega,\\[4pt]
\beta_1 = \frac{\omega}{c} = \frac{2\pi\cdot5\times10^7}{3\times10^8} = \frac\pi3\ \text{rad/m},\\[6pt]
\eta_2 = \eta_0\sqrt{\frac{\mu_r}{\epsilon_r}} = \eta_0\sqrt{\frac{4}{2.25}} = \frac43\eta_0 = 160\pi\ \Omega,\\[6pt]
\beta_2 = \sqrt{\mu_r\epsilon_r}\,\beta_1 = 3\beta_1 = \pi\ \text{rad/m}.
\end{gathered}
$$

$\beta_2 = \pi$ matches the $\pi x$ in $\mathbf{H}_t$. The incident wave comes from the vacuum, so **region 1 is $x>0$**, and $\hat n$ (from region 2 into region 1) is $+\hat x$.

## (b) Γ and τ

$$
\Gamma = \frac{160\pi-120\pi}{160\pi+120\pi} = \frac17,\qquad \tau = 1+\Gamma = \frac87 .
$$

> [!key] Answer (b)
> $\Gamma = 1/7\approx0.143$, $\tau = 8/7\approx1.14$. $\tau>1$ because $\eta_2>\eta_1$.

## (c) The electric fields

$\cos(\omega t+\pi x)$ has phasor $e^{+j\pi x}$, which travels toward $-x$, so $\tilde{\mathbf{H}}_t = \hat z\,\tfrac{1}{10\pi}e^{j\pi x}$ A/m with $\hat u = -\hat x$. Then

$$
\begin{gathered}
\tilde{\mathbf{E}}_t = \eta_2\,\tilde{\mathbf{H}}_t\times\hat u = \frac{160\pi}{10\pi}\,\big(\hat z\times(-\hat x)\big)e^{j\pi x}\\[4pt]
= -\hat y\,16\,e^{j\pi x}\ \text{V/m}.
\end{gathered}
$$

Check: $\tilde{\mathbf{E}}_t\times\tilde{\mathbf{H}}_t^*\propto(-\hat y)\times\hat z = -\hat x$, the travel direction.

$\tau$ and $\Gamma$ relate tangential $\tilde{\mathbf{E}}$ at $x = 0$: $\tilde{\mathbf{E}}_i(0) = \tilde{\mathbf{E}}_t(0)/\tau = -\hat y\,14$ V/m and $\tilde{\mathbf{E}}_r(0) = \Gamma\,\tilde{\mathbf{E}}_i(0) = -\hat y\,2$ V/m. The incident wave travels toward $-x$ ($e^{+j\beta_1x}$), the reflected one toward $+x$ ($e^{-j\beta_1x}$).

> [!key] Answer (c)
> $$
> \begin{gathered}
> \tilde{\mathbf{E}}_t = -\hat y\,16\,e^{j\pi x},\qquad \tilde{\mathbf{E}}_i = -\hat y\,14\,e^{j\pi x/3},\\[4pt]
> \tilde{\mathbf{E}}_r = -\hat y\,2\,e^{-j\pi x/3}\ \ \text{V/m}.
> \end{gathered}
> $$

> [!trap] Where (c) loses points
> - Copying the lecture's exponent signs. Here the incident wave has $e^{+j\beta_1x}$; read each sign from its $\hat u$.
> - Dividing the $\mathbf{H}$ amplitude by $\tau$. $\tau$ is for $\mathbf{E}$; $\tilde H_t/\tilde H_i = 1-\Gamma = 6/7$.

## (d) The magnetic fields

$\tilde{\mathbf{H}} = \hat u\times\tilde{\mathbf{E}}/\eta_1$, with $\hat u = -\hat x$ for the incident wave and $+\hat x$ for the reflected one:

$$
\begin{gathered}
\tilde{\mathbf{H}}_i = \frac{(-\hat x)\times(-\hat y)\,14}{120\pi}e^{j\pi x/3}\\[4pt]
= \hat z\,\frac{7}{60\pi}e^{j\pi x/3}\ \text{A/m},\\[8pt]
\tilde{\mathbf{H}}_r = \frac{\hat x\times(-\hat y)\,2}{120\pi}e^{-j\pi x/3}\\[4pt]
= -\hat z\,\frac{1}{60\pi}e^{-j\pi x/3}\ \text{A/m}.
\end{gathered}
$$

The amplitudes are 37.1 and 5.31 mA/m. At $x = 0$, $(14-2)/120\pi = 1/10\pi = \tilde H_{tz}(0)$: tangential $\tilde{\mathbf{H}}$ is continuous (no surface current). And $\tilde H_r/\tilde H_i = -1/7 = -\Gamma$.

## (e) Power

$$
\begin{gathered}
\langle\mathbf{S}_i\rangle = -\hat x\,\frac{14^2}{2\cdot120\pi} = -\hat x\,\frac{49}{60\pi},\\[6pt]
\langle\mathbf{S}_r\rangle = +\hat x\,\frac{2^2}{2\cdot120\pi} = +\hat x\,\frac{1}{60\pi},\\[6pt]
\langle\mathbf{S}_t\rangle = -\hat x\,\frac{16^2}{2\cdot160\pi} = -\hat x\,\frac{4}{5\pi}\ \ \text{W/m}^2 .
\end{gathered}
$$

Balance: $\tfrac{49}{60\pi}-\tfrac{1}{60\pi} = \tfrac{48}{60\pi} = \tfrac4{5\pi}$. $\Gamma^2 = 1/49$ (2.0 %) reflects; $\tau^2\eta_1/\eta_2 = \tfrac{64}{49}\cdot\tfrac34 = \tfrac{48}{49}$ is transmitted, despite $\tau>1$.

> [!key] Answer (e)
> $\langle\mathbf{S}_i\rangle = -260\,\hat x$, $\langle\mathbf{S}_r\rangle = +5.31\,\hat x$, $\langle\mathbf{S}_t\rangle = -255\,\hat x$ mW/m².

## (f) A perfect conductor instead

$\eta_2\to0$ gives $\Gamma = -1$, so $\tilde{\mathbf{E}}_r = +\hat y\,14\,e^{-j\pi x/3}$ V/m and $\tilde{\mathbf{H}}_r = \hat x\times\hat y\,\tfrac{14}{120\pi}e^{-j\pi x/3} = \hat z\,\tfrac{7}{60\pi}e^{-j\pi x/3}$ A/m. At $x = 0$ the total $\tilde{\mathbf{E}}$ vanishes and the total $\tilde{\mathbf{H}}$ is $\hat z\,7/30\pi$. With $\hat n = +\hat x$:

$$
\tilde{\mathbf{J}}_s = \hat n\times\tilde{\mathbf{H}}_1 = \hat x\times\hat z\,\frac{7}{30\pi} = -\hat y\,\frac{7}{30\pi}\ \text{A/m}.
$$

> [!key] Answer (f)
> $\tilde{\mathbf{E}}_r = \hat y\,14\,e^{-j\pi x/3}$ V/m; $\mathbf{J}_s(t) = -\hat y\,\tfrac{7}{30\pi}\cos\omega t$ A/m $= -\hat y\,74.3\cos\omega t$ mA/m. It flows along the incident $\mathbf{E}$ at the surface, with magnitude $2\lvert\tilde{\mathbf{E}}_i(0)\rvert/\eta_1$.

## The pattern

1. $\eta$, $\beta$ on both sides; the given $\beta$ checks the medium.
2. The given field's phasor, then its partner from $\hat u$ and $\eta_2$.
3. Back through $\tau$ (electric field only), forward with $\Gamma$.
4. Each $\tilde{\mathbf{H}} = \hat u\times\tilde{\mathbf{E}}/\eta$; check continuity.
5. Powers and the balance.

Summer 2017 HE3 #3 runs these steps for dielectric to vacuum along $+z$, with $\mathbf{E}_t$ given; SP18 Exam 3 #2 runs steps 1–3 along $+y$; SP19 Exam 3 #3b is part (f) for a circular wave. This version travels toward $-x$, enters a magnetic medium (so $\tau>1$) and gives $\mathbf{H}$.
