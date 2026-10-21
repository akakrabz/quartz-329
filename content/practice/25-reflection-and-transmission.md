---
title: "Practice — Lecture 25: Wave reflection and transmission"
description: "12 practice problems (5 easy, 3 medium, 4 hard) on normal incidence: Γ = (η₂ − η₁)/(η₂ + η₁) and τ = 1 + Γ for dielectric, magnetic, lossy and perfectly conducting region 2, signs of the reflected E and H, ε_r and μ_r from measured reflections, matching, incidence from the denser side, the power balance and why τ > 1 is no gain, a wave into lossy ground with exact γ and η, and a circular wave on a mirror; hints on the medium and hard ones, a worked solution for each."
tags: [practice, waves]
lecture: 25
---

*Practice for [[3-maxwell-and-waves/25-wave-reflection-and-transmission|Lecture 25]] · concepts: [[concepts/reflection-and-transmission]] · [[concepts/intrinsic-impedance]] · [[concepts/boundary-conditions]] · [[concepts/poynting-vector]] · all practice: [[practice/index|hub]] · by difficulty: [[practice/easy|easy]] · [[practice/medium|medium]] · [[practice/hard|hard]] · [[practice/topics|by topic]]*

Work each problem on paper first. Open the **hint** only when stuck, and the **solution** only after you have an answer you would hand in. Every answer here has been checked numerically.

The whole page runs on four lines. Region 1 holds the incident wave.
- $\Gamma = \dfrac{\eta_2-\eta_1}{\eta_2+\eta_1}$, $\tau = 1+\Gamma$: ratios of **electric** fields at the interface.
- Each wave's $\tilde{\mathbf{H}} = \hat u\times\tilde{\mathbf{E}}/\eta$, so the $\mathbf{H}$ ratios are $-\Gamma$ (reflected) and $1-\Gamma$ (transmitted).
- Exponent sign from each wave's own $\hat u$: $e^{-j\beta z}$ for $+\hat z$, $e^{+j\beta z}$ for $-\hat z$.
- Power: $\lvert\Gamma\rvert^2$ reflects, $1-\lvert\Gamma\rvert^2$ enters region 2.

## Easy

### 25.1 Four interfaces

> [!easy] Easy · reflection coefficient · transmission coefficient
> A plane wave meets a planar interface head-on. All media are lossless and non-magnetic unless stated. For each pair (region 1 → region 2) find $\Gamma$, $\tau$ and the percentage of the incident power that reflects.
>
> (a) Air → $\epsilon_r = 4$. (b) $\epsilon_r = 4$ → air. (c) Air → $\mu_r = 16$, $\epsilon_r = 4$. (d) Air → perfect conductor.
>
> *Source: original.*

> [!solution]- Solution
> $\eta = \eta_0\sqrt{\mu_r/\epsilon_r}$; only $\eta_2/\eta_1$ matters.
>
> | pair | $\eta_2/\eta_1$ | $\Gamma$ | $\tau$ | reflected $\Gamma^2$ |
> |---|---|---|---|---|
> | (a) | $1/2$ | $-1/3$ | $2/3$ | 11.1 % |
> | (b) | $2$ | $+1/3$ | $4/3$ | 11.1 % |
> | (c) | $2$ | $+1/3$ | $4/3$ | 11.1 % |
> | (d) | $0$ | $-1$ | $0$ | 100 % |
>
> (a) and (b) are the same interface crossed both ways: $\Gamma$ flips sign, $\Gamma^2$ does not. (b) and (c) share $\eta_2/\eta_1 = 2$, so they reflect identically although the media differ.
>
> **Check:** $\Gamma^2+\tau^2\eta_1/\eta_2 = \tfrac19+\tfrac49\cdot2 = 1$ for (a), and $\tfrac19+\tfrac{16}9\cdot\tfrac12 = 1$ for (b), (c).
>
> **Answer.** (a) $\Gamma = -1/3$, $\tau = 2/3$; (b) and (c) $\Gamma = +1/3$, $\tau = 4/3$; 11.1 % reflected in (a)–(c). (d) $\Gamma = -1$, $\tau = 0$, 100 %.

### 25.2 Signs at the interface

> [!easy] Easy · true or false · reflection
> A plane wave in lossless region 1 meets region 2 head-on. True or false?
>
> (a) If $\eta_2<\eta_1$, the reflected $\mathbf{E}$ at the interface points opposite to the incident $\mathbf{E}$.
>
> (b) If $\eta_2<\eta_1$, the reflected $\mathbf{H}$ at the interface points opposite to the incident $\mathbf{H}$.
>
> (c) $\tau = 4/3$ means the transmitted wave carries more power than the incident wave.
>
> (d) At every instant, the total tangential $\mathbf{E}$ just on the incident side equals the transmitted tangential $\mathbf{E}$ just across.
>
> (e) A lossless material with $\mu_r = \epsilon_r = 3$ in vacuum reflects nothing, though waves slow to $c/3$ in it.
>
> *Source: original.*

> [!solution]- Solution
> (a) **True.** $\eta_2<\eta_1$ gives $\Gamma<0$: $\tilde E_r(0) = \Gamma\tilde E_i(0)$ is inverted.
>
> (b) **False.** $\tilde H_r(0)/\tilde H_i(0) = -\Gamma>0$: the reflected $\mathbf{H}$ is *along* the incident one. (The wave reverses, so $\hat u\times\tilde{\mathbf{E}}$ flips once more.)
>
> (c) **False.** $\tau = 4/3$ needs $\eta_2 = 2\eta_1$; the transmitted fraction is $\tau^2\eta_1/\eta_2 = \tfrac{16}{9}\cdot\tfrac12 = \tfrac89$.
>
> (d) **True.** $1+\Gamma = \tau$ is tangential-$\mathbf{E}$ continuity; equal phasors give equal real fields at all $t$.
>
> (e) **True.** $\eta_2 = \eta_0\sqrt{3/3} = \eta_0$, so $\Gamma = 0$. Reflection depends on $\mu/\epsilon$, speed on $\mu\epsilon$.
>
> **Answer.** (a) T, (b) F, (c) F, (d) T, (e) T.

### 25.3 Into a good conductor

> [!easy] Easy · multiple choice · reflection coefficient · lossy media
> A plane wave in free space meets, head-on, a non-magnetic material with $\epsilon = 9\epsilon_0$ and, at the wave's frequency, $\sigma = 3600\,\omega\epsilon_0$. The reflection coefficient $\Gamma$ for $\mathbf{E}$ is approximately
>
> (a) $0$
>
> (b) $-1/2$
>
> (c) $+1/2$
>
> (d) $-1$
>
> (e) $+1$
>
> (f) cannot be found without $\omega$
>
> *Source: SP17 Exam 3 #2(iv) style, reversed (into the conductor) with new ε and σ.*

> [!solution]- Solution
> $\sigma/\omega\epsilon = 3600/9 = 400\gg1$: a good conductor, so $\sigma+j\omega\epsilon\approx\sigma$ and
> $$
> \eta_2\approx\sqrt{\frac{j\omega\mu_0}{\sigma}} = \eta_0\sqrt{\frac{j\omega\epsilon_0}{\sigma}} = \frac{\eta_0}{60}e^{j45^\circ}\approx6.3\angle45^\circ\ \Omega.
> $$
> $\Gamma = (\eta_2-\eta_0)/(\eta_2+\eta_0)\approx-1+2\eta_2/\eta_0\approx-1$. Exactly, $\Gamma = -0.976+j0.023$, $\lvert\Gamma\rvert = 0.977$: 95.4 % of the power reflects. **(d).**
>
> - (b) uses the lossless $\eta_2 = \eta_0/3$, ignoring $\sigma$.
> - (c) is (b) with $\eta_1$ and $\eta_2$ swapped. (e) swaps them in the correct $\Gamma$: the answer for a wave *leaving* the conductor into air.
> - (a) needs $\eta_2 = \eta_0$.
> - (f) $\sigma$ is given as a multiple of $\omega\epsilon_0$, so $\omega$ cancels.
>
> **Answer.** (d), $\Gamma\approx-1$ ($-0.976+j0.023$).

### 25.4 An amplifying dielectric

> [!easy] Easy · find the error · reflection coefficient · power balance
> The wave $\tilde{\mathbf{E}}_i = \hat x\,5e^{-j\beta_1z}$ V/m in air ($z<0$) meets a lossless non-magnetic dielectric with $\epsilon_r = 16$ ($z>0$). A student writes:
>
> *"$\eta_2 = \eta_0/4 = 30\pi\ \Omega$. $\Gamma = (\eta_1-\eta_2)/(\eta_1+\eta_2) = 90\pi/150\pi = 0.6$ and $\tau = 1+\Gamma = 1.6$, so $\tilde E_t(0) = 8$ V/m: the dielectric amplifies the field."*
>
> Find the slip, give the correct $\Gamma$, $\tau$, $\tilde E_r(0)$ and $\tilde E_t(0)$, and name a one-line check that catches it.
>
> *Source: original.*

> [!solution]- Solution
> **Slip:** the numerator is reversed. $\Gamma$ is "far side minus incident side":
> $$
> \Gamma = \frac{30\pi-120\pi}{30\pi+120\pi} = -0.6,\qquad \tau = 0.4.
> $$
> So $\tilde{\mathbf{E}}_r(0) = -3\hat x$ V/m (inverted, as $\eta_2<\eta_1$ requires) and $\tilde{\mathbf{E}}_t(0) = 2\hat x$ V/m.
>
> **Check that catches it:** the power balance $\Gamma^2+\tau^2\eta_1/\eta_2 = 1$. Correct: $0.36+0.16\times4 = 1$. Student: $0.36+2.56\times4 = 10.6$, over ten times the incident power.
>
> **Answer.** $\Gamma = -0.6$, $\tau = 0.4$; $\tilde{\mathbf{E}}_r(0) = -3\hat x$ V/m, $\tilde{\mathbf{E}}_t(0) = 2\hat x$ V/m; 36 % reflects, 64 % enters.

### 25.5 Permittivity from a reflection

> [!easy] Easy · reflection coefficient · intrinsic impedance
> A plane wave in air meets a lossless non-magnetic dielectric head-on. At the interface the reflected $\mathbf{E}$ has half the incident amplitude and points opposite to it.
>
> (a) Find $\epsilon_r$ of the dielectric. (b) What percentage of the incident power enters it? (c) A magnetic material has the same $\epsilon_r$. Which $\mu_r$ makes it reflect nothing?
>
> *Source: original.*

> [!solution]- Solution
> (a) $\Gamma = -\tfrac12$. Solve $\Gamma = (\eta_2-\eta_1)/(\eta_2+\eta_1)$ for $\eta_2$:
> $$
> \frac{\eta_2}{\eta_1} = \frac{1+\Gamma}{1-\Gamma} = \frac{1/2}{3/2} = \frac13 = \frac{1}{\sqrt{\epsilon_r}}\ \Rightarrow\ \epsilon_r = 9.
> $$
> (b) $1-\Gamma^2 = 75$ %.
>
> (c) $\eta_2 = \eta_0\sqrt{\mu_r/\epsilon_r} = \eta_0$ needs $\mu_r = \epsilon_r = 9$.
>
> **Check:** $(\tfrac13-1)/(\tfrac13+1) = -\tfrac12$ ✓.
>
> **Answer.** (a) $\epsilon_r = 9$; (b) 75 %; (c) $\mu_r = 9$.

## Medium

### 25.6 Same speed, different impedance

> [!medium] Medium · normal incidence · intrinsic impedance · power balance
> Glass ($\mu_0$, $4\epsilon_0$) fills $z>0$; a lossless magnetic material ($4\mu_0$, $\epsilon_0$) fills $z<0$. The 100 MHz wave $\tilde{\mathbf{E}}_i = \hat y\,10\,e^{j\beta_1z}$ V/m travels through the glass toward $-\hat z$. Use $\eta_0 = 120\pi\ \Omega$, $c = 3\times10^8$ m/s.
>
> (a) Find $\eta$ and $\beta$ on both sides. (b) Find $\Gamma$ and $\tau$. (c) Find $\tilde{\mathbf{E}}_r$, $\tilde{\mathbf{H}}_r$, $\tilde{\mathbf{E}}_t$, $\tilde{\mathbf{H}}_t$. (d) What percentage of the power reflects, and why is it not zero although the wave speed is the same on both sides?
>
> *Source: original.*

> [!hint]- Hint
> Region 1 is the glass. The incident and transmitted waves have $\hat u = -\hat z$, the reflected one $+\hat z$; $(-\hat z)\times\hat y = +\hat x$.

> [!solution]- Solution
> **Setup.** Region 1 = glass ($z>0$), region 2 = magnetic ($z<0$).
>
> (a) $\eta_1 = \eta_0/2 = 60\pi\ \Omega$, $\eta_2 = 2\eta_0 = 240\pi\ \Omega$. $\beta_0 = 2\pi f/c = 2\pi/3$; $\sqrt{\mu_r\epsilon_r} = 2$ on both sides, so $\beta_1 = \beta_2 = 4\pi/3$ rad/m.
>
> (b) $\Gamma = \dfrac{240\pi-60\pi}{300\pi} = 0.6$, $\tau = 1.6$.
>
> (c)
> $$
> \begin{aligned}
> \tilde{\mathbf{E}}_r &= \hat y\,6\,e^{-j4\pi z/3}\ \text{V/m}, &\tilde{\mathbf{H}}_r &= \hat z\times\hat y\,\tfrac{6}{60\pi}e^{-j4\pi z/3} = -\hat x\,\tfrac{1}{10\pi}e^{-j4\pi z/3}\ \text{A/m},\\
> \tilde{\mathbf{E}}_t &= \hat y\,16\,e^{j4\pi z/3}\ \text{V/m}, &\tilde{\mathbf{H}}_t &= (-\hat z)\times\hat y\,\tfrac{16}{240\pi}e^{j4\pi z/3} = \hat x\,\tfrac{1}{15\pi}e^{j4\pi z/3}\ \text{A/m}.
> \end{aligned}
> $$
> **Check:** $\tilde{\mathbf{H}}_i = \hat x\,\tfrac{10}{60\pi}e^{j4\pi z/3} = \hat x\,\tfrac{1}{6\pi}e^{j4\pi z/3}$; at $z = 0$, $\tfrac1{6\pi}-\tfrac1{10\pi} = \tfrac1{15\pi}$ ✓ (tangential $\mathbf{H}$ continuous).
>
> (d) $\Gamma^2 = 36$ %; $\tau^2\eta_1/\eta_2 = 2.56/4 = 64$ % enters. In W/m²: $\lvert\langle\mathbf{S}\rangle\rvert = 0.265$ (i), 0.095 (r), 0.170 (t). Speed depends on $\mu_r\epsilon_r$ (4 on both sides), reflection on $\mu_r/\epsilon_r$ ($\tfrac14$ against 4).
>
> **Answer.** (a) $\eta_1 = 60\pi$, $\eta_2 = 240\pi\ \Omega$, $\beta_1 = \beta_2 = 4\pi/3$ rad/m. (b) $\Gamma = 0.6$, $\tau = 1.6$. (c) $\tilde{\mathbf{E}}_r = \hat y\,6e^{-j4\pi z/3}$ V/m, $\tilde{\mathbf{H}}_r = -\hat x\,\tfrac1{10\pi}e^{-j4\pi z/3}$ A/m, $\tilde{\mathbf{E}}_t = \hat y\,16e^{j4\pi z/3}$ V/m, $\tilde{\mathbf{H}}_t = \hat x\,\tfrac1{15\pi}e^{j4\pi z/3}$ A/m. (d) 36 %; $\eta_2\neq\eta_1$.

### 25.7 A plane mirror and its current

> [!medium] Medium · perfect conductor · phasors
> A perfect conductor fills $y<0$. In the air above it the incident wave is $\mathbf{E}_i(y,t) = \hat z\,3\sin(\omega t+\beta y)$ V/m at $f = 300$ MHz. Use $\eta_0 = 120\pi\ \Omega$.
>
> (a) Find $\beta$ and the phasors $\tilde{\mathbf{E}}_i$, $\tilde{\mathbf{H}}_i$. (b) Find $\tilde{\mathbf{E}}_r$, $\tilde{\mathbf{H}}_r$ and $\mathbf{E}_r(y,t)$. (c) Find the surface current $\mathbf{J}_s(t)$ on the wall.
>
> *Source: original.*

> [!hint]- Hint
> A sine becomes $-j$. The incident wave travels toward $-\hat y$. $\Gamma = -1$. $\mathbf{J}_s = \hat n\times\tilde{\mathbf{H}}_1$ with the **total** $\tilde{\mathbf{H}}$ at $y = 0^+$ and $\hat n = +\hat y$ (from the conductor into the air).

> [!solution]- Solution
> (a) $\beta = \omega/c = 2\pi$ rad/m. $\tilde{\mathbf{E}}_i = -j3\,\hat z\,e^{j2\pi y}$ V/m; $\hat u = -\hat y$, $(-\hat y)\times\hat z = -\hat x$:
> $$
> \tilde{\mathbf{H}}_i = -\hat x\,\frac{-j3}{120\pi}e^{j2\pi y} = \hat x\,\frac{j}{40\pi}e^{j2\pi y}\ \text{A/m}.
> $$
> (b) $\Gamma = -1$, $\hat u = +\hat y$, $\hat y\times\hat z = \hat x$:
> $$
> \tilde{\mathbf{E}}_r = j3\,\hat z\,e^{-j2\pi y}\ \text{V/m},\qquad \tilde{\mathbf{H}}_r = \hat x\,\frac{j}{40\pi}e^{-j2\pi y}\ \text{A/m},
> $$
> so $\mathbf{E}_r = \text{Re}\{j3e^{j(\omega t-2\pi y)}\}\hat z = -\hat z\,3\sin(\omega t-2\pi y)$ V/m.
>
> (c) At $y = 0$: $\tilde{\mathbf{E}} = 0$, $\tilde{\mathbf{H}} = \hat x\,\dfrac{j}{20\pi}$ (doubled, since $\tilde H_r/\tilde H_i = -\Gamma = 1$).
> $$
> \tilde{\mathbf{J}}_s = \hat y\times\hat x\,\frac{j}{20\pi} = -\hat z\,\frac{j}{20\pi}\ \Rightarrow\ \mathbf{J}_s(t) = \hat z\,\frac{1}{20\pi}\sin\omega t\ \text{A/m}.
> $$
> **Check:** $\mathbf{J}_s$ runs along $\mathbf{E}_i(0,t) = \hat z\,3\sin\omega t$ with magnitude $2\cdot3/\eta_0 = 15.9$ mA/m (Lecture 25 §3). Net $\langle\mathbf{S}\rangle$ in the air is zero.
>
> **Answer.** (a) $\beta = 2\pi$ rad/m, $\tilde{\mathbf{E}}_i = -j3\hat z\,e^{j2\pi y}$ V/m, $\tilde{\mathbf{H}}_i = \hat x\,\tfrac{j}{40\pi}e^{j2\pi y}$ A/m. (b) $\tilde{\mathbf{E}}_r = j3\hat z\,e^{-j2\pi y}$ V/m, $\tilde{\mathbf{H}}_r = \hat x\,\tfrac{j}{40\pi}e^{-j2\pi y}$ A/m, $\mathbf{E}_r = -\hat z\,3\sin(\omega t-2\pi y)$ V/m. (c) $\mathbf{J}_s = \hat z\,\tfrac{1}{20\pi}\sin\omega t$ A/m $\approx\hat z\,15.9\sin\omega t$ mA/m.

### 25.8 How good a mirror is copper

> [!medium] Medium · good conductor · reflection coefficient · power balance
> A 10 GHz plane wave in air meets a flat copper wall ($\sigma = 5.8\times10^7$ S/m, $\mu_0$) head-on. Use $\eta_0 = 120\pi\ \Omega$.
>
> (a) Show that copper is a good conductor here, and find $\delta$ and $\eta_2$.
>
> (b) Show that, for real $\eta_1$, the absorbed fraction is $1-\lvert\Gamma\rvert^2 = 4\eta_1\text{Re}\{\eta_2\}/\lvert\eta_1+\eta_2\rvert^2$, and evaluate it.
>
> (c) How much of an incident 100 W/m² does the copper absorb?
>
> *Source: original.*

> [!hint]- Hint
> $\lvert\eta_1+\eta_2\rvert^2-\lvert\eta_2-\eta_1\rvert^2 = 4\eta_1\text{Re}\{\eta_2\}$. Use this rather than computing $\lvert\Gamma\rvert\approx0.9999$ and subtracting.

> [!solution]- Solution
> (a) $\sigma/\omega\epsilon_0 = 1.0\times10^8\gg1$. Lecture 23:
> $$
> \delta = \frac{1}{\sqrt{\pi f\mu_0\sigma}} = 0.661\ \mu\text{m},\qquad \eta_2 = \frac{1+j}{\sigma\delta} = 0.0261(1+j)\ \Omega
> $$
> (the exact $\eta$ of Lecture 22 agrees to $10^{-8}$).
>
> (b) $1-\lvert\Gamma\rvert^2 = \dfrac{\lvert\eta_2+\eta_1\rvert^2-\lvert\eta_2-\eta_1\rvert^2}{\lvert\eta_2+\eta_1\rvert^2} = \dfrac{4\eta_1\text{Re}\{\eta_2\}}{\lvert\eta_1+\eta_2\rvert^2}\approx\dfrac{4\,\text{Re}\{\eta_2\}}{\eta_1} = \dfrac{4\times0.0261}{377} = 2.77\times10^{-4}$.
>
> (c) $100\times2.77\times10^{-4} = 27.7$ mW/m² absorbed; 99.97 W/m² reflected. ($\Gamma = -0.99986+j1.4\times10^{-4}$.)
>
> **Check:** the transmitted side of §4, $\lvert\tau\rvert^2\eta_1\text{Re}\{1/\eta_2\}$, gives the same $2.77\times10^{-4}$.
>
> **Answer.** (a) $\delta = 0.661$ µm, $\eta_2 = 0.0261(1+j)\ \Omega$. (b) $1-\lvert\Gamma\rvert^2 = 2.77\times10^{-4}$ (0.028 %). (c) 27.7 mW/m².

## Hard

### 25.9 Out of the glass

> [!hard] Hard · transmission coefficient · phasors · power balance
> A lossless dielectric ($\mu_0$, $9\epsilon_0$) fills $z>0$; vacuum fills $z<0$. A 50 MHz wave travels through the dielectric toward $-\hat z$ and meets $z = 0$. The transmitted field in the vacuum is $\mathbf{E}_t(z,t) = \hat y\,3\sin(\omega t+\beta z)$ V/m. Use $\eta_0 = 120\pi\ \Omega$, $c = 3\times10^8$ m/s.
>
> (a) Find $\eta$ and $\beta$ on both sides, and $\Gamma$, $\tau$.
>
> (b) Find $\tilde{\mathbf{E}}_t$ and $\tilde{\mathbf{H}}_t$.
>
> (c) Find $\tilde{\mathbf{E}}_i$, $\tilde{\mathbf{E}}_r$, $\tilde{\mathbf{H}}_i$, $\tilde{\mathbf{H}}_r$; check tangential $\tilde{\mathbf{H}}$ at $z = 0$.
>
> (d) Find $\langle\mathbf{S}\rangle$ of all three waves and check the power balance.
>
> (e) Write $\mathbf{E}_r(z,t)$.
>
> *Source: Summer 2017 HE3 #3c–f, re-parameterized.*

> [!hint]- Hint
> The wave comes from the dielectric, so that is region 1. Convert the sine first ($-j$). Then $\tilde{\mathbf{E}}_i(0) = \tilde{\mathbf{E}}_t(0)/\tau$ and $\tilde{\mathbf{E}}_r(0) = \Gamma\tilde{\mathbf{E}}_i(0)$; each exponent sign comes from that wave's own $\hat u$.

> [!solution]- Solution
> **Setup.** Region 1: dielectric ($z>0$). Incident and transmitted $\hat u = -\hat z$, reflected $+\hat z$. $(-\hat z)\times\hat y = \hat x$, $\hat z\times\hat y = -\hat x$.
>
> (a) $\eta_1 = \eta_0/3 = 40\pi\ \Omega$, $\eta_2 = 120\pi\ \Omega$; $\beta_2 = \omega/c = \pi/3$, $\beta_1 = 3\beta_2 = \pi$ rad/m.
> $$
> \Gamma = \frac{120\pi-40\pi}{160\pi} = \frac12,\qquad \tau = \frac32.
> $$
> (b) $\tilde{\mathbf{E}}_t = -j3\,\hat y\,e^{j\pi z/3}$ V/m, $\tilde{\mathbf{H}}_t = \hat x\,\dfrac{-j3}{120\pi}e^{j\pi z/3} = -\hat x\,\dfrac{j}{40\pi}e^{j\pi z/3}$ A/m.
>
> (c) $\tilde E_i(0) = -j3/\tfrac32 = -j2$, $\tilde E_r(0) = \tfrac12(-j2) = -j$:
> $$
> \begin{aligned}
> \tilde{\mathbf{E}}_i &= -j2\,\hat y\,e^{j\pi z}\ \text{V/m}, &\tilde{\mathbf{H}}_i &= -\hat x\,\tfrac{j}{20\pi}e^{j\pi z}\ \text{A/m},\\
> \tilde{\mathbf{E}}_r &= -j\,\hat y\,e^{-j\pi z}\ \text{V/m}, &\tilde{\mathbf{H}}_r &= +\hat x\,\tfrac{j}{40\pi}e^{-j\pi z}\ \text{A/m}.
> \end{aligned}
> $$
> At $z = 0$: $-\tfrac{j}{20\pi}+\tfrac{j}{40\pi} = -\tfrac{j}{40\pi} = \tilde H_{tx}(0)$ ✓.
>
> (d) $\lvert\langle\mathbf{S}\rangle\rvert = \lvert\tilde E\rvert^2/2\eta$:
> $$
> \langle\mathbf{S}_i\rangle = -\hat z\,\frac{1}{20\pi},\quad \langle\mathbf{S}_r\rangle = +\hat z\,\frac{1}{80\pi},\quad \langle\mathbf{S}_t\rangle = -\hat z\,\frac{3}{80\pi}\ \ \text{W/m}^2,
> $$
> i.e. 15.9, 3.98 and 11.9 mW/m². $\tfrac4{80\pi}-\tfrac1{80\pi} = \tfrac3{80\pi}$ ✓: 25 % reflects, 75 % $= \tau^2\eta_1/\eta_2 = \tfrac94\cdot\tfrac13$ passes.
>
> (e) $\mathbf{E}_r = \text{Re}\{-je^{j(\omega t-\pi z)}\}\hat y = \hat y\sin(\omega t-\pi z)$ V/m.
>
> **Watch out:** $\Gamma>0$ here because $\eta$ rises leaving the denser side; $\tau = 3/2$ is still only 75 % of the power.
>
> **Answer.** (a) $\eta_1 = 40\pi$, $\eta_2 = 120\pi\ \Omega$, $\beta_1 = \pi$, $\beta_2 = \pi/3$ rad/m, $\Gamma = 1/2$, $\tau = 3/2$. (b) $\tilde{\mathbf{E}}_t = -j3\hat y\,e^{j\pi z/3}$ V/m, $\tilde{\mathbf{H}}_t = -\hat x\,\tfrac{j}{40\pi}e^{j\pi z/3}$ A/m. (c) $\tilde{\mathbf{E}}_i = -j2\hat y\,e^{j\pi z}$, $\tilde{\mathbf{E}}_r = -j\hat y\,e^{-j\pi z}$ V/m; $\tilde{\mathbf{H}}_i = -\hat x\,\tfrac{j}{20\pi}e^{j\pi z}$, $\tilde{\mathbf{H}}_r = \hat x\,\tfrac{j}{40\pi}e^{-j\pi z}$ A/m. (d) $-15.9\hat z$, $+3.98\hat z$, $-11.9\hat z$ mW/m². (e) $\mathbf{E}_r = \hat y\sin(\omega t-\pi z)$ V/m.

### 25.10 Into lossy ground

> [!hard] Hard · lossy media · transmission · Joule heating
> Air fills $z<0$. The ground ($z>0$) is non-magnetic with $\epsilon = 2\epsilon_0$ and, at $\omega = 3\times10^8$ rad/s, loss tangent $\sigma/\omega\epsilon = \sqrt3$. The incident wave is $\tilde{\mathbf{E}}_i = \hat x\,10\,e^{-jz}$ V/m. Use $\epsilon_0 = 10^{-9}/36\pi$ F/m ($\eta_0 = 120\pi\ \Omega$, $c = 3\times10^8$ m/s). Calculator allowed.
>
> (a) Find $\sigma$, and $\gamma_2$, $\eta_2$ exactly.
>
> (b) Find $\Gamma$ and $\tau$ in polar form.
>
> (c) Find $\tilde{\mathbf{E}}_t(z)$ and $\tilde{\mathbf{H}}_t(z)$.
>
> (d) Find the fractions of the incident power reflected and transmitted. Check the transmitted power against the Joule heating $\int_0^\infty\tfrac12\sigma\lvert\tilde{\mathbf{E}}_t\rvert^2dz$.
>
> *Source: original (exact γ and η as in SP19 Exam 3 #1, now behind an interface).*

> [!hint]- Hint
> $\sigma+j\omega\epsilon = j\omega\epsilon(1-j\sqrt3) = j\omega\epsilon\cdot2e^{-j60^\circ}$. Then $\eta_2 = \sqrt{\mu_0/\epsilon}/\sqrt{2e^{-j60^\circ}}$ and $\gamma_2 = j\omega\mu_0/\eta_2$. A loss tangent of $\sqrt3$ is in neither limit of Lecture 23.

> [!solution]- Solution
> **(a)** $\sigma = \sqrt3\,\omega\epsilon = \sqrt3\cdot3\times10^8\cdot\dfrac{2\times10^{-9}}{36\pi} = \dfrac{\sqrt3}{60\pi} = 9.19$ mS/m.
> $$
> \eta_2 = \frac{\eta_0/\sqrt2}{\sqrt2\,e^{-j30^\circ}} = 60\pi\,e^{j30^\circ}\ \Omega,\qquad \gamma_2 = \frac{j\omega\mu_0}{\eta_2} = j\frac{\omega}{c}\frac{\eta_0}{\eta_2} = 2e^{j60^\circ} = 1+j\sqrt3\ \text{m}^{-1}.
> $$
> **(b)** With $\eta_2/\eta_0 = \tfrac12e^{j30^\circ}$:
> $$
> \Gamma = \frac{e^{j30^\circ}-2}{e^{j30^\circ}+2} = \frac{-3+2j}{5+2\sqrt3} = -0.354+j0.236 = 0.426\angle146.3^\circ,\qquad \tau = 1+\Gamma = 0.646+j0.236 = 0.687\angle20.1^\circ.
> $$
> **(c)** $\hat u = \hat z$, $\hat z\times\hat x = \hat y$:
> $$
> \tilde{\mathbf{E}}_t = \hat x\,6.87\,e^{j20.1^\circ}e^{-z}e^{-j\sqrt3z}\ \text{V/m},\qquad \tilde{\mathbf{H}}_t = \hat y\,\frac{6.87}{60\pi}e^{j(20.1^\circ-30^\circ)}e^{-(1+j\sqrt3)z} = \hat y\,36.5\,e^{-j9.9^\circ}e^{-(1+j\sqrt3)z}\ \text{mA/m}.
> $$
> **(d)** $\lvert\Gamma\rvert^2 = 13/(5+2\sqrt3)^2 = 0.181$: 18.1 % reflects, 81.9 % enters. With $\langle S_i\rangle = 100/240\pi = 0.1326$ W/m²,
> $$
> \langle S_t\rangle(0^+) = \tfrac12\lvert\tau E_0\rvert^2\,\text{Re}\{1/\eta_2\} = \tfrac12(47.26)\frac{\cos30^\circ}{60\pi} = 0.1086\ \text{W/m}^2 = 0.819\times0.1326\ ✓.
> $$
> Joule heating: $\displaystyle\int_0^\infty\tfrac12\sigma\lvert\tau E_0\rvert^2e^{-2z}dz = \frac{\sigma\lvert\tau E_0\rvert^2}{4} = \frac{9.19\times10^{-3}\times47.26}{4} = 0.1086$ W/m² ✓: everything that enters becomes heat.
>
> **Check:** tangential $\tilde{\mathbf{H}}$ at $z = 0$: $(1-\Gamma)E_0/\eta_0 = 0.0359-j0.0063 = \tau E_0/\eta_2$ A/m ✓.
>
> **Answer.** (a) $\sigma = \sqrt3/60\pi = 9.19$ mS/m, $\gamma_2 = 1+j\sqrt3$ m⁻¹, $\eta_2 = 60\pi e^{j30^\circ}\ \Omega$. (b) $\Gamma = 0.426\angle146.3^\circ$, $\tau = 0.687\angle20.1^\circ$. (c) $\tilde{\mathbf{E}}_t = \hat x\,6.87e^{j20.1^\circ}e^{-(1+j\sqrt3)z}$ V/m, $\tilde{\mathbf{H}}_t = \hat y\,36.5e^{-j9.9^\circ}e^{-(1+j\sqrt3)z}$ mA/m. (d) 18.1 % reflected, 81.9 % (0.1086 W/m²) transmitted, equal to the Joule heating.

### 25.11 A circular wave on a mirror

> [!hard] Hard · perfect conductor · circular polarization · handedness
> A perfect conductor fills $y>0$. In the air ($y<0$) the incident wave is
> $$
> \mathbf{E}_i(y,t) = \hat z\,4\cos(\omega t-\pi y)-\hat x\,4\sin(\omega t-\pi y)\ \ \text{V/m}.
> $$
> Use $\eta_0 = 120\pi\ \Omega$, $c = 3\times10^8$ m/s.
>
> (a) Find $f$, the phasor $\tilde{\mathbf{E}}_i$, and its polarization with handedness.
>
> (b) Find $\tilde{\mathbf{E}}_r$, $\mathbf{E}_r(y,t)$ and the reflected handedness.
>
> (c) Find $\mathbf{J}_s(t)$ on the wall and describe its motion.
>
> (d) Find $\langle\mathbf{S}\rangle$ of both waves. How much power does the wall absorb?
>
> *Source: SP19 Exam 3 #3b, re-parameterized (travel +y, ẑ and x̂ components, new amplitude; parts c–d added).*

> [!hint]- Hint
> $\Gamma = -1$ for each component. Handedness by Lecture 24's test $\hat u\cdot[\mathbf{E}(0)\times\mathbf{E}(T/4)]$ at the wall ($>0$ right, $<0$ left); the reflected wave has $\hat u = -\hat y$. For $\mathbf{J}_s$, $\hat n = -\hat y$.

> [!solution]- Solution
> **(a)** $\beta = \pi$ rad/m, $\lambda = 2$ m, $f = c/\lambda = 150$ MHz. $\sin\to-j$: $\tilde{\mathbf{E}}_i = 4(\hat z+j\hat x)e^{-j\pi y}$ V/m. Equal amplitudes, 90° apart: circular. At $y = 0$: $\mathbf{E}(0) = 4\hat z$, $\mathbf{E}(T/4) = -4\hat x$;
> $$
> \hat y\cdot[4\hat z\times(-4\hat x)] = -16<0\ \Rightarrow\ \text{left-circular}.
> $$
> **(b)** $\tilde{\mathbf{E}}_r = -4(\hat z+j\hat x)e^{j\pi y}$ V/m, so $\mathbf{E}_r = -\hat z\,4\cos(\omega t+\pi y)+\hat x\,4\sin(\omega t+\pi y)$ V/m. At $y = 0$: $\mathbf{E}(0) = -4\hat z$, $\mathbf{E}(T/4) = 4\hat x$; $(-\hat y)\cdot[(-4\hat z)\times4\hat x] = +16$: **right-circular**. Same rotation in time at the wall, opposite travel, so the hand flips.
>
> **(c)** $\tilde{\mathbf{H}} = \hat u\times\tilde{\mathbf{E}}/\eta_0$:
> $$
> \tilde{\mathbf{H}}_i = \frac{\hat x-j\hat z}{30\pi}e^{-j\pi y},\qquad \tilde{\mathbf{H}}_r = \frac{\hat x-j\hat z}{30\pi}e^{j\pi y}\ \ \text{A/m}.
> $$
> At $y = 0^-$: $\tilde{\mathbf{E}} = 0$, $\tilde{\mathbf{H}} = (\hat x-j\hat z)/15\pi$. With $\hat n = -\hat y$ (conductor into air):
> $$
> \tilde{\mathbf{J}}_s = (-\hat y)\times\frac{\hat x-j\hat z}{15\pi} = \frac{\hat z+j\hat x}{15\pi}\ \Rightarrow\ \mathbf{J}_s(t) = \frac{1}{15\pi}\big(\hat z\cos\omega t-\hat x\sin\omega t\big)\ \text{A/m}.
> $$
> Constant magnitude $1/15\pi = 21.2$ mA/m, rotating with $\mathbf{E}_i(0,t)$ ($\tilde{\mathbf{J}}_s = 2\tilde{\mathbf{E}}_i(0)/\eta_0$).
>
> **(d)** Each component carries $4^2/(2\cdot120\pi) = 1/15\pi$; the powers add: $\langle\mathbf{S}_i\rangle = \hat y\,\dfrac{2}{15\pi} = 42.4\,\hat y$ mW/m², $\langle\mathbf{S}_r\rangle = -42.4\,\hat y$ mW/m². Net zero: the wall absorbs nothing ($\tau = 0$).
>
> **Check:** a dielectric with $\epsilon_r = 9$ instead gives $\Gamma = -\tfrac12$ for both components: a right-circular reflection of amplitude 2 V/m, and a left-circular transmitted wave of amplitude 2 V/m.
>
> **Answer.** (a) 150 MHz, $\tilde{\mathbf{E}}_i = 4(\hat z+j\hat x)e^{-j\pi y}$ V/m, left-circular. (b) $\tilde{\mathbf{E}}_r = -4(\hat z+j\hat x)e^{j\pi y}$ V/m, $\mathbf{E}_r = -\hat z\,4\cos(\omega t+\pi y)+\hat x\,4\sin(\omega t+\pi y)$ V/m, right-circular. (c) $\mathbf{J}_s = \tfrac{1}{15\pi}(\hat z\cos\omega t-\hat x\sin\omega t)$ A/m, 21.2 mA/m rotating. (d) $\pm42.4\,\hat y$ mW/m²; none absorbed.

### 25.12 Identifying a material

> [!hard] Hard · reflection coefficient · intrinsic impedance · power balance
> Air fills $z<0$; an unknown lossless material fills $z>0$. At $f = 100$ MHz the incident wave is $\mathbf{E}_i = \hat x\,10\cos(\omega t-\beta_0z)$ V/m. Probes measure the reflected wave $\mathbf{E}_r = \hat x\,2\cos(\omega t+\beta_0z)$ V/m and, inside the material, an undamped transmitted wave with spatial period 1.5 m. Use $\eta_0 = 120\pi\ \Omega$, $c = 3\times10^8$ m/s.
>
> (a) Find $\Gamma$, $\tau$ and $\eta_2$.
>
> (b) Find $\mu_r$ and $\epsilon_r$, using $\gamma\eta = j\omega\mu$ and $\gamma/\eta = j\omega\epsilon$.
>
> (c) Write $\mathbf{E}_t(z,t)$ and $\mathbf{H}_t(z,t)$ and check the power balance.
>
> (d) Keeping $\epsilon_r$, which $\mu_r$ would make the material reflectionless?
>
> *Source: SP18 Exam 3 #2a–d style, run backward (the material is the unknown).*

> [!hint]- Hint
> $\Gamma$ is $\tilde E_r(0)/\tilde E_i(0)$, sign included. Invert the $\Gamma$ formula for $\eta_2$. A lossless medium has $\gamma_2 = j\beta_2$ with $\beta_2 = 2\pi/(\text{period})$.

> [!solution]- Solution
> **(a)** At $z = 0$: $\Gamma = 2/10 = +0.2$, $\tau = 1.2$.
> $$
> \eta_2 = \eta_1\frac{1+\Gamma}{1-\Gamma} = 1.5\,\eta_0 = 180\pi\ \Omega.
> $$
> **(b)** $\beta_0 = 2\pi/3$, $\beta_2 = 2\pi/1.5 = 4\pi/3$ rad/m. $\mu_2 = \gamma_2\eta_2/j\omega = \beta_2\eta_2/\omega$ and $\epsilon_2 = \beta_2/(\omega\eta_2)$; divide by $\mu_0 = \beta_0\eta_0/\omega$ and $\epsilon_0 = \beta_0/(\omega\eta_0)$:
> $$
> \mu_r = \frac{\beta_2}{\beta_0}\frac{\eta_2}{\eta_0} = 2\times1.5 = 3,\qquad \epsilon_r = \frac{\beta_2}{\beta_0}\frac{\eta_0}{\eta_2} = \frac{2}{1.5} = \frac43.
> $$
> **(c)** $\hat u = \hat z$, $\hat z\times\hat x = \hat y$:
> $$
> \mathbf{E}_t = \hat x\,12\cos(\omega t-4\pi z/3)\ \text{V/m},\qquad \mathbf{H}_t = \hat y\,\frac{12}{180\pi}\cos(\omega t-4\pi z/3) = \hat y\,\frac{1}{15\pi}\cos(\omega t-4\pi z/3)\ \text{A/m}.
> $$
> $\langle S_i\rangle = \dfrac{100}{240\pi} = \dfrac{5}{12\pi}$, $\langle S_r\rangle = \dfrac{4}{240\pi} = \dfrac{1}{60\pi}$, $\langle S_t\rangle = \dfrac{144}{360\pi} = \dfrac{2}{5\pi}$ W/m² (132.6, 5.3, 127.3 mW/m²). $\dfrac{25-1}{60\pi} = \dfrac{2}{5\pi}$ ✓: 4 % reflects.
>
> **(d)** $\eta_2 = \eta_0$ needs $\mu_r = \epsilon_r = 4/3$.
>
> **Check:** forward, $\eta_0\sqrt{3/(4/3)} = 1.5\eta_0$ and $\sqrt{3\cdot4/3} = 2 = \beta_2/\beta_0$ ✓.
>
> **Watch out:** with the sign dropped ($\Gamma = -0.2$) you would get $\mu_r = 4/3$, $\epsilon_r = 3$, the two swapped. The phase of $\mathbf{E}_r$ carries that information.
>
> **Answer.** (a) $\Gamma = 0.2$, $\tau = 1.2$, $\eta_2 = 180\pi\ \Omega$. (b) $\mu_r = 3$, $\epsilon_r = 4/3$. (c) $\mathbf{E}_t = \hat x\,12\cos(\omega t-4\pi z/3)$ V/m, $\mathbf{H}_t = \hat y\,\tfrac{1}{15\pi}\cos(\omega t-4\pi z/3)$ A/m (21.2 mA/m); 132.6 = 5.3 + 127.3 mW/m². (d) $\mu_r = 4/3$.

### Sources for this page
Course notes, Lecture 25: the three-wave setup, the boxed $\Gamma$ and $\tau$, the special cases and Example 1's power check, used throughout with new media. Old exams, all re-parameterized: SP17 Exam 3 #2(iv) (25.3, now into the conductor, with new $\epsilon$ and $\sigma$); Summer 2017 HE3 #3c–f (25.9: $\epsilon_r = 9$, travel $-\hat z$, $\hat y$-polarized sine, $\mathbf{H}$ and powers added); SP19 Exam 3 #3b (25.11: travel $+\hat y$, new components and amplitude, surface current and power added); SP18 Exam 3 #2a–d (25.12, run backward to identify the material). The exact $\gamma$, $\eta$ of 25.10 use SP19 Exam 3 #1's $1+j\sqrt3$ in a new setting. Copper's conductivity: Rao, Table 5.1. Original: 25.1, 25.2, 25.4–25.8, 25.10.

*Previous: [[practice/24-group-velocity-and-polarization|Lecture 24 practice]] · next: [[practice/26-standing-waves-and-radiation-pressure|Lecture 26 practice]] · [[practice/index|all practice]]*
