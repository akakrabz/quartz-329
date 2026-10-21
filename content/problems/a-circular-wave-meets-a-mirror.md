---
title: "Worked problem — A circular wave meets a mirror"
description: "A circular 1.5 GHz wave hits a perfect conductor: reflected wave and hand, total fields and nodes, instantaneous S and w, surface current and pressure. Modelled on SP19 Exam 3 #3, SP17 Exam 3 #1b–c and FA23 Exam 3 #1(c)."
tags: [problem, waves]
---

*Problem · style of SP19 Exam 3 #3, SP17 Exam 3 #1b–c and FA23 Exam 3 #1(c) · uses [[3-maxwell-and-waves/26-standing-waves-and-radiation-pressure|Lecture 26]], [[3-maxwell-and-waves/25-wave-reflection-and-transmission|Lecture 25]], [[3-maxwell-and-waves/24-signal-transmission-and-circular-polarization|Lecture 24]] · concepts: [[concepts/standing-waves]], [[concepts/radiation-pressure]]*

> [!question] Problem
> The region $y>0$ is vacuum; a perfect conductor fills $y<0$. The incident wave at $f = 1.5$ GHz is
> $$
> \begin{gathered}
> \mathbf{E}_i = 60\pi\big[\hat x\cos(\omega t+\beta y)\\
> +\ \hat z\sin(\omega t+\beta y)\big]\ \text{V/m}.
> \end{gathered}
> $$
> Use $\eta_0 = 120\pi\ \Omega$ and $c = 3\times10^8$ m/s.
>
> (a) Find $\tilde{\mathbf{E}}_i$, its direction and hand, and the reflected $\tilde{\mathbf{E}}_r$ and its hand.
>
> (b) Find the total $\mathbf{E}(y,t)$ and $\mathbf{H}(y,t)$. Is the field in $y>0$ travelling, standing, or both? Where are the nodes? Check Faraday's law.
>
> (c) Find the instantaneous $\mathbf{S}(y,t)$ and energy density $w(y,t)$. Is $w$ ever zero?
>
> (d) Find $\mathbf{J}_s(t)$ and the radiation pressure, averaged and instantaneous.

## (a) Incident and reflected phasors

$\beta = \omega/c = 10\pi$ rad/m, $\lambda = 20$ cm. A sine has phasor factor $-j$:
$$
\tilde{\mathbf{E}}_i = 60\pi(\hat x - j\hat z)e^{j\beta y}\ \text{V/m}.
$$
$e^{+j\beta y}$ means travel along $\hat u = -\hat y$. Hand, by [[3-maxwell-and-waves/24-signal-transmission-and-circular-polarization#4-right-or-left-the-notes-rule|Lecture 24 §4]]'s recipe: $\mathbf{E}(0)\propto\hat x$, $\mathbf{E}(T/4)\propto\hat z$, $\hat x\times\hat z = -\hat y$, and $\hat u\cdot(-\hat y) = +1$: **right-circular**.

$\Gamma = -1$ for each component, and the reflected wave travels along $+\hat y$:
$$
\tilde{\mathbf{E}}_r = -60\pi(\hat x - j\hat z)e^{-j\beta y}\ \text{V/m}.
$$
Now $\mathbf{E}(0)\propto-\hat x$, $\mathbf{E}(T/4)\propto-\hat z$, $(-\hat x)\times(-\hat z) = -\hat y$, and $\hat y\cdot(-\hat y) = -1$: **left-circular**. The rotation at the mirror is unchanged; the travel reverses, so the hand flips.

## (b) Total fields

$\tilde{\mathbf{H}} = \hat u\times\tilde{\mathbf{E}}/\eta_0$ for each wave ($60\pi/120\pi = \tfrac12$):
$$
\begin{gathered}
\tilde{\mathbf{H}}_i = \frac{(-\hat y)\times\tilde{\mathbf{E}}_i}{120\pi} = \tfrac12(\hat z + j\hat x)e^{j\beta y},\\[4pt]
\tilde{\mathbf{H}}_r = \frac{\hat y\times\tilde{\mathbf{E}}_r}{120\pi} = \tfrac12(\hat z + j\hat x)e^{-j\beta y}\ \text{A/m}.
\end{gathered}
$$
Summing with $e^{j\theta}\mp e^{-j\theta} = 2j\sin\theta,\ 2\cos\theta$: $\tilde{\mathbf{E}} = 120\pi\sin\beta y\,(\hat z + j\hat x)$, $\tilde{\mathbf{H}} = \cos\beta y\,(\hat z + j\hat x)$. In time:

> [!key] Answer (b)
> $$
> \begin{gathered}
> \hat a(t) = \hat z\cos\omega t - \hat x\sin\omega t,\\[4pt]
> \mathbf{E} = 120\pi\sin\beta y\ \hat a(t)\ \text{V/m},\\[4pt]
> \mathbf{H} = \cos\beta y\ \hat a(t)\ \text{A/m}.
> \end{gathered}
> $$
> All standing: every component is a function of $y$ times a function of $t$. $\mathbf{E}$ nodes at $y = 0, 10, 20,\dots$ cm; $\mathbf{H}$ nodes at $y = 5, 15, 25,\dots$ cm.

Faraday ($y$-dependence only): $\nabla\times\mathbf{E} = \hat x\,\partial_yE_z - \hat z\,\partial_yE_x = 120\pi\beta\cos\beta y\,\hat b$ and $-\mu_0\partial_t\mathbf{H} = \mu_0\omega\cos\beta y\,\hat b$, with $\hat b = \hat x\cos\omega t + \hat z\sin\omega t$. They agree: $120\pi\beta = \eta_0\omega/c = \mu_0\omega$.

## (c) Flux and energy

$\mathbf{E}$ and $\mathbf{H}$ both lie along $\hat a(t)$, so they are parallel and
$$
\mathbf{S} = \mathbf{E}\times\mathbf{H} = 0\quad\text{at every } y \text{ and } t.
$$
$\lvert\hat a\rvert = 1$ and $\epsilon_0(120\pi)^2 = \mu_0$, so
$$
\begin{gathered}
w = \tfrac12\epsilon_0(120\pi)^2\sin^2\beta y + \tfrac12\mu_0\cos^2\beta y\\[4pt]
= \tfrac12\mu_0 = 2\pi\times10^{-7}\ \text{J/m}^3 .
\end{gathered}
$$

> [!key] Answer (c)
> $\mathbf{S} = 0$ and $w = 2\pi\times10^{-7}\approx6.28\times10^{-7}$ J/m³, the same at every $y$ and $t$. It is never zero.

> [!trap] Where (c) loses points
> - Copying the linear result. The pair $E_x$, $H_z$ alone gives $S_y = +30\pi\sin2\beta y\sin2\omega t$, the pair $E_z$, $H_x$ gives $-30\pi\sin2\beta y\sin2\omega t$; they cancel at every instant.
> - Each pair's $w$ has zeros; the two pairs fill each other's gaps.

## (d) Surface current and pressure

$\hat n = +\hat y$ (conductor into vacuum) and $\mathbf{H}(0,t) = \hat a(t)$:
$$
\begin{gathered}
\mathbf{J}_s = \hat y\times(\hat z\cos\omega t - \hat x\sin\omega t)\\[4pt]
= \hat x\cos\omega t + \hat z\sin\omega t\ \ \text{A/m}.
\end{gathered}
$$
That is $2\mathbf{E}_i(0,t)/\eta_0$: a 1 A/m current turning with the incident field.

Pressure (Lecture 26 §6): $P_{rad}(t) = \tfrac12\mu_0\lvert\mathbf{H}(0,t)\rvert^2$, with $\lvert\mathbf{H}(0,t)\rvert = 1$ A/m always. The push is along $-\hat n = -\hat y$, into the conductor.

Average check: each component carries $(60\pi)^2/(2\cdot120\pi) = 15\pi$ W/m², so $\langle S_i\rangle = 30\pi\approx94.2$ W/m² and $2\langle S_i\rangle/c = 60\pi/(3\times10^8) = 2\pi\times10^{-7}$ N/m².

> [!key] Answer (d)
> $\mathbf{J}_s = \hat x\cos\omega t + \hat z\sin\omega t$ A/m. $\mathbf{P}_{rad} = -\hat y\,2\pi\times10^{-7}$ N/m² $\approx-\hat y\,0.628\ \mu$Pa at every instant, equal to $w$ of (c). A linear wave with the same $\langle S_i\rangle$ gives the same average, pulsing as $\cos^2\omega t$.

## The pattern

1. Phasor, travel direction, hand; $\Gamma = -1$ per component; $\tilde{\mathbf{H}} = \hat u\times\tilde{\mathbf{E}}/\eta$ for each wave.
2. Sum; standing if every term is (function of position) × (function of time).
3. $\mathbf{S}$ and $w$ from the real fields, averages from the phasors.
4. $\mathbf{J}_s = \hat n\times\mathbf{H}$, $\hat n$ out of the conductor; pressure $\tfrac12\mu_0\lvert\mathbf{H}\rvert^2$, average $2\langle S_i\rangle/c$.

SP19 Exam 3 #3 asks for the reflected field and the kind of total field, with the wave along $-x$; SP17 #1b–c and FA23 #1(c) ask Maxwell, net-power and energy-density true/false items. This version changes the axis, amplitude and hand, and adds $\mathbf{S}(t)$, $w$, $\mathbf{J}_s$ and the pressure.
