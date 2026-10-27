---
title: "Worked problem — Energy bookkeeping for a radiating sheet"
description: "A sheet on the plane x = 0 carries −ẑ 3u(t)cos(ωt) A/m at 2 MHz inside a dielectric with εr = 2.25. Find the two waves, the power the current injects (J·E on the sheet, instantaneous and averaged), the average Poynting vector on each side, the energy delivered by 3 µs and where it is stored, and when and how fast energy reaches a window 900 m away. Modelled on Summer 2020 HE3 #2(c)–(d), re-parameterized with a new plane, current direction, waveform, frequency, amplitude and medium."
tags: [problem, waves]
---

*Problem · style of Summer 2020 HE3 #2 (parts c–d) · uses [[3-maxwell-and-waves/20-poynting-theorem-and-monochromatic-waves|Lecture 20]], [[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets|Lecture 19]] · concepts: [[concepts/poynting-theorem]], [[concepts/poynting-vector]], [[concepts/current-sheet-radiation]]*

> [!question] Problem
> An infinitesimally thin sheet in the plane $x = 0$ carries the surface current
> $$
> \begin{gathered}
> \mathbf{J}_s(t) = -\hat z\,3\,u(t)\cos(\omega t)\ \ \text{A/m},\\[4pt]
> \omega = 4\pi\times10^6\ \text{rad/s},
> \end{gathered}
> $$
> where $u(t)$ is the unit step: the current is switched on at full strength at $t = 0$. A lossless, non-magnetic dielectric with $\epsilon_r = 2.25$ fills all space on both sides. Use the exam constants $\epsilon_0 = 10^{-9}/(36\pi)$ F/m and $\mu_0 = 4\pi\times10^{-7}$ H/m, so that $c = 3\times10^8$ m/s and $\eta_0 = 120\pi\ \Omega$ exactly.
> (a) Find $v$, $\eta$, $\beta$ and $\lambda$ in the dielectric, and write $\mathbf{E}$ and $\mathbf{H}$ for $x>0$ and $x<0$ at times $t>0$.
> (b) Find $\mathbf{J}_s\cdot\mathbf{E}$ on the sheet for $t>0$, and its time average. What does its sign mean?
> (c) Find the time-averaged Poynting vector on each side, behind the wavefronts, and check the energy balance at the sheet.
> (d) How much energy per square metre of sheet has the current delivered by $t = 3$ µs? Show that all of it is stored in the fields between the two wavefronts.
> (e) A window of area 1 m² stands parallel to the sheet at $x = 900$ m. From what time does energy cross it, and at what average rate after that?

## Before writing anything: the medium

The sheet result of Lecture 19 holds in any homogeneous lossless medium, with that medium's $v$ and $\eta$:

$$
\begin{gathered}
v = \frac{c}{\sqrt{\epsilon_r}} = \frac{3\times10^8}{1.5} = 2\times10^8\ \text{m/s},\\[4pt]
\eta = \frac{\eta_0}{\sqrt{\epsilon_r}} = \frac{120\pi}{1.5} = 80\pi\approx251\ \Omega .
\end{gathered}
$$

The frequency is $f = \omega/2\pi = 2$ MHz, so the period is $T = 0.5$ µs. Then $\beta = \omega/v = 4\pi\times10^6/(2\times10^8) = 0.02\pi\approx0.0628$ rad/m and $\lambda = 2\pi/\beta = v/f = 100$ m.

## (a) The two waves

Apply the recipe of [[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets#4-the-same-result-from-boundary-conditions-slides|Lecture 19]]: $\mathbf{E} = -\tfrac\eta2\mathbf{J}_s(t - \lvert x\rvert/v)$ and $\mathbf{H} = \tfrac12\mathbf{J}_s(t - \lvert x\rvert/v)\times\hat n$, with $\hat n = +\hat x$ for $x>0$ and $-\hat x$ for $x<0$. Delaying the source by $\lvert x\rvert/v$ turns $\cos\omega t$ into $\cos(\omega t - \beta\lvert x\rvert)$ and $u(t)$ into $u(t - \lvert x\rvert/v)$.

- $\mathbf{E}$: $-\tfrac\eta2(-\hat z\,3) = +\hat z\,\tfrac32\eta = +\hat z\,120\pi$ V/m in amplitude, on both sides. A current along $-\hat z$ gives an $\mathbf{E}$ along $+\hat z$: the field opposes the current.
- $\mathbf{H}$ for $x>0$: $\tfrac12(-\hat z\,3)\times\hat x = -\tfrac32(\hat z\times\hat x) = -1.5\,\hat y$ A/m in amplitude.
- $\mathbf{H}$ for $x<0$: $\tfrac12(-\hat z\,3)\times(-\hat x) = +1.5\,\hat y$ A/m.

> [!key] Answer (a)
> $v = 2\times10^8$ m/s, $\eta = 80\pi\approx251\ \Omega$, $\beta = 0.02\pi$ rad/m, $\lambda = 100$ m, and for $x\gtrless0$
> $$
> \begin{gathered}
> \mathbf{E} = \hat z\,120\pi\,u\Big(t\mp\frac xv\Big)\cos(\omega t\mp\beta x)\ \ \text{V/m},\\[4pt]
> \mathbf{H} = \mp\hat y\,1.5\,u\Big(t\mp\frac xv\Big)\cos(\omega t\mp\beta x)\ \ \text{A/m}.
> \end{gathered}
> $$
> Checks. Direction: $\hat z\times(-\hat y) = +\hat x$ for $x>0$ and $\hat z\times(+\hat y) = -\hat x$ for $x<0$, away from the sheet on both sides ✓. Ratio: $120\pi/1.5 = 80\pi = \eta$ ✓. Jump at the sheet, with region 1 = $x>0$ and $\hat n = \hat x$: $\hat x\times(\mathbf{H}_1 - \mathbf{H}_2) = \hat x\times(-3\,\hat y)\cos\omega t = -\hat z\,3\cos\omega t = \mathbf{J}_s$ ✓.

## (b) The power the current injects

On the sheet $\mathbf{E}$ is the same from both sides (tangential $\mathbf{E}$ is continuous): $\mathbf{E}(0,t) = \hat z\,120\pi\cos\omega t$ for $t>0$. So

$$
\begin{aligned}
\mathbf{J}_s\cdot\mathbf{E} &= \big(-\hat z\,3\cos\omega t\big)\cdot\big(\hat z\,120\pi\cos\omega t\big)\\
&= -360\pi\cos^2(\omega t)\ \ \text{W/m}^2 .
\end{aligned}
$$

With $\langle\cos^2\rangle = \tfrac12$:

> [!key] Answer (b)
> $$
> \begin{gathered}
> \mathbf{J}_s\cdot\mathbf{E} = -360\pi\cos^2\omega t\ \ \text{W/m}^2,\\[4pt]
> \langle\mathbf{J}_s\cdot\mathbf{E}\rangle = -180\pi\approx-565\ \text{W/m}^2 .
> \end{gathered}
> $$
> The peak is $360\pi\approx1131$ W/m². In general $\langle\mathbf{J}_s\cdot\mathbf{E}\rangle = -\eta J_0^2/4$ for a sheet current of amplitude $J_0$. The sign is negative at every instant (except the zeros of $\cos\omega t$), so the sheet is a **source**. Whatever drives the current pushes it against $\mathbf{E}$, and on average it delivers 565 W to every square metre of sheet. That power goes into the field.

> [!trap] Where part (b) loses points
> - The exam calls $\langle\mathbf{J}_s\cdot\mathbf{E}\rangle$ "the average Joule heating rate". At a source that rate is negative. A positive answer means a sign slip in $\mathbf{E}$: $\mathbf{E}$ must oppose $\mathbf{J}_s$.
> - Units: $\mathbf{J}_s\cdot\mathbf{E}$ is (A/m)(V/m) = W/m², power per unit area of sheet, not W/m³.
> - Forgetting the ½ from $\langle\cos^2\rangle$, or using $\eta_0$ instead of the dielectric's $\eta$.

## (c) The average Poynting vector, and the balance

Behind the fronts ($\lvert x\rvert<vt$), part (a) gives

$$
\begin{aligned}
\mathbf{S} &= \big(120\pi\,\hat z\big)\times\big(\mp1.5\,\hat y\big)\cos^2(\omega t\mp\beta x)\\
&= \pm\hat x\,180\pi\cos^2(\omega t\mp\beta x)\ \ \text{W/m}^2 .
\end{aligned}
$$

> [!key] Answer (c)
> $$
> \langle\mathbf{S}\rangle = \pm\hat x\,90\pi\approx\pm\hat x\,283\ \text{W/m}^2\qquad(x\gtrless0),
> $$
> behind the fronts. That is $\eta J_0^2/8$ on each side. **Balance:** $90\pi + 90\pi = 180\pi = \langle-\mathbf{J}_s\cdot\mathbf{E}\rangle$ ✓. It holds at every instant too. At $x = 0^\pm$ each face carries $180\pi\cos^2\omega t$ outward, and the two together equal $-\mathbf{J}_s\cdot\mathbf{E} = 360\pi\cos^2\omega t$. That is the sheet form of Poynting's theorem, $\hat n\cdot(\mathbf{S}_1 - \mathbf{S}_2) = -\mathbf{J}_s\cdot\mathbf{E}$ ([[3-maxwell-and-waves/20-poynting-theorem-and-monochromatic-waves#6-the-notes-example-monochromatic-waves-from-a-cosine-sheet|Lecture 20 §6]]).

## (d) The energy delivered by 3 µs, and where it is

**Delivered.** By $t = 3$ µs the current has run for exactly 6 periods. Over whole periods $\int\cos^2\omega t\,dt = t/2$, so per square metre of sheet

$$
\begin{aligned}
W_{\text{in}} &= \int_0^{3\ \mu\text{s}}(-\mathbf{J}_s\cdot\mathbf{E})\,dt\\
&= 360\pi\times\frac{3\times10^{-6}}{2}\ \text{J/m}^2\\
&= 540\pi\ \mu\text{J/m}^2\approx1.70\ \text{mJ/m}^2 ,
\end{aligned}
$$

which is also $\langle-\mathbf{J}_s\cdot\mathbf{E}\rangle\times3\ \mu\text{s} = 180\pi\times3\times10^{-6}$.

**Where it is.** At 3 µs the fronts are at $\lvert x\rvert = vt = 600$ m, and nothing has reached beyond them. Apply the integral form of Poynting's theorem to a box of unit cross-section with faces at $x = \pm L$, beyond the fronts ($L>600$ m). On those faces $\mathbf{S}$ has been zero all along, and the only exchange inside is at the sheet. So $dW/dt = -\mathbf{J}_s\cdot\mathbf{E}$ at every instant: everything the current has delivered is still stored in the box, all of it in the region $\lvert x\rvert<600$ m.

**Check by integrating $w$.** For a single travelling wave $w_e = w_m$, so $w = \epsilon E^2 = \epsilon(120\pi)^2\cos^2(\omega t - \beta\lvert x\rvert)$. With $\epsilon = 2.25\epsilon_0 = 10^{-9}/(16\pi)$ F/m, the average density is

$$
\begin{aligned}
\langle w\rangle = \tfrac12\epsilon E_0^2 &= \tfrac12\cdot\frac{10^{-9}}{16\pi}\cdot(120\pi)^2\ \text{J/m}^3\\
&= 450\pi\times10^{-9}\ \text{J/m}^3\approx1.41\ \mu\text{J/m}^3 .
\end{aligned}
$$

At $t = 3$ µs, $\omega t = 12\pi$, so $\cos^2(\omega t - \beta x) = \cos^2(\beta x)$. The 600 m on each side hold exactly 6 wavelengths, over which $\cos^2$ averages to ½. Each side therefore holds $\langle w\rangle\times600\ \text{m} = 270\pi\ \mu$J/m², and the two sides together hold $540\pi\ \mu\text{J/m}^2\approx1.70$ mJ/m² ✓.

<!-- fig:poy-problem-energy -->

> [!key] Answer (d)
> $W_{\text{in}} = 540\pi\ \mu$J/m² $\approx1.70$ mJ per square metre of sheet, stored as field energy between the two fronts at $x = \pm600$ m, $270\pi\ \mu$J/m² $\approx0.85$ mJ/m² on each side. The equality is not special to whole periods. At any $t$, both sides together hold $\tfrac12\eta J_0^2\big[t/2 + \sin(2\omega t)/(4\omega)\big]$, which is exactly $\int_0^t(-\mathbf{J}_s\cdot\mathbf{E})\,dt$ (panel 2 of the figure). Note also $\langle S\rangle/\langle w\rangle = 90\pi/(450\pi\times10^{-9}) = 2\times10^8$ m/s $= v$: the energy moves out at the wave speed.

## (e) The window at x = 900 m

The front left the sheet at $t = 0$ and travels at $v$, so it reaches $x = 900$ m at $t = 900/(2\times10^8) = 4.5$ µs. Before that, $\mathbf{S} = 0$ there. After that the window sees the steady oscillation, with $\langle\mathbf{S}\rangle = +\hat x\,90\pi$ W/m² along its normal.

> [!key] Answer (e)
> Energy first crosses the window at $t = 4.5$ µs. From then on it crosses at an average rate of $90\pi\times1\ \text{m}^2\approx283$ W, in pulses at $2f = 4$ MHz: the instantaneous rate is $180\pi\cos^2(\omega t - \beta\cdot900\ \text{m})$ W, between 0 and 565 W.

## Variant: the same sheet in vacuum

Remove the dielectric. Then $\eta = 120\pi\ \Omega$ and $v = 3\times10^8$ m/s. $\mathbf{H}$ keeps its amplitude of 1.5 A/m, because it is set by the jump $J_s$ whatever the medium. $\mathbf{E}$ grows to $180\pi\approx565$ V/m, the average flux on each side to $135\pi\approx424$ W/m², and the injected power to $270\pi\approx848$ W/m². With the same current, a higher-impedance medium takes more power from the sheet, just as a current source delivers $I^2R$ to a larger resistor.

## The pattern behind this problem

$$
\begin{gathered}
\langle-\mathbf{J}_s\cdot\mathbf{E}\rangle = \frac{\eta J_0^2}{4},\\[4pt]
\langle S\rangle_{\text{each side}} = \frac{\eta J_0^2}{8},\\[4pt]
W_{\text{stored}} = \int_0^t(-\mathbf{J}_s\cdot\mathbf{E})\,dt ,
\end{gathered}
$$

where $W_{\text{stored}}$ is the field energy between the two fronts, per square metre of sheet.

Write the fields with the Lecture 19 recipe, take $\mathbf{J}_s\cdot\mathbf{E}$ on the sheet (negative: a source), average with $\langle\cos^2\rangle = \tfrac12$, and split the injected power equally between the two sides. When the source has been on for a finite time, a box whose faces lie beyond the fronts shows that everything delivered is still stored. The exam instance (Summer 2020 HE3 #2) puts a sine current along $\hat y$ on the plane $z = 0$ in free space, and asks for the average of $\mathbf{J}_s\cdot\mathbf{E}$ and the average power per unit area carried into $z>0$, as numbers.
