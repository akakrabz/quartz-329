---
title: "Practice — Lecture 26: Standing waves and radiation pressure"
description: "12 practice problems (5 easy, 3 medium, 4 hard) on standing waves in front of a perfect mirror: nodes and antinodes, time quadrature, zero average power and the sloshing energy, a mirror off the origin, the mirror's surface current, partial reflection read from a probe, a Maxwell check of a cos·cos / sin·sin pair, a good-conductor mirror's skin current, heat and push, radiation-pressure numbers for sunlight and lasers, and a field trapped between two mirrors; hints on the medium and hard ones, a worked solution for each."
tags: [practice, waves]
lecture: 26
---

*Practice for [[3-maxwell-and-waves/26-standing-waves-and-radiation-pressure|Lecture 26]] · concepts: [[concepts/standing-waves]] · [[concepts/radiation-pressure]] · [[concepts/reflection-and-transmission]] · [[concepts/skin-depth]] · all practice: [[practice/index|hub]] · by difficulty: [[practice/easy|easy]] · [[practice/medium|medium]] · [[practice/hard|hard]] · [[practice/topics|by topic]]*

Work each problem on paper first. Open the **hint** only when stuck, and the **solution** only after you have an answer you would hand in. Every answer here has been checked numerically.

The whole page runs on four lines (perfect mirror at $z = 0$, wave $\hat x\,E_0\cos(\omega t-\beta z)$ incident from $z<0$):
- $\mathbf{E} = \hat x\,2E_0\sin\beta z\sin\omega t$, $\mathbf{H} = \hat y\,(2E_0/\eta)\cos\beta z\cos\omega t$. $\mathbf{E}$ nodes at the mirror and every $\lambda/2$; $\mathbf{H}$ nodes $\lambda/4$ from them.
- $\langle\mathbf{S}\rangle = 0$ and $\langle w\rangle = \epsilon E_0^2$; the instantaneous $\mathbf{S}$ and $w$ are not zero.
- $\mathbf{J}_s = \hat n\times\mathbf{H}$, $\hat n$ out of the conductor: $\hat x\,(2E_0/\eta)\cos\omega t$.
- Pressure $2\langle S_i\rangle/c$ on a mirror, $\langle S_i\rangle/c$ on an absorber; a beam of power $P$ pushes a mirror with $2P/c$.

## Easy

### 26.1 Nodes in front of a mirror

> [!easy] Easy · standing waves · nodes and antinodes
> A perfect conductor fills $z>0$. The region $z<0$ is a lossless dielectric with $\epsilon_r = 4$, $\mu_r = 1$. The incident wave is $\tilde{\mathbf{E}}_i = \hat x\,10\,e^{-j\beta_1z}$ V/m at $f = 1.25$ GHz. Use $c = 3\times10^8$ m/s, $\eta_0 = 120\pi\ \Omega$.
>
> (a) Find $\lambda$ in the dielectric. (b) List the $\mathbf{E}$ nodes and the $\mathbf{H}$ nodes in $-15\text{ cm}\le z\le0$. (c) Find the amplitudes of $E_x$ and $H_y$ at $z = -1$ cm.
>
> *Source: original.*

> [!solution]- Solution
> (a) $\lambda_1 = \dfrac{c}{f\sqrt{\epsilon_r}} = \dfrac{24\text{ cm}}{2} = 12$ cm, so $\beta_1 = 2\pi/\lambda_1 = 50\pi/3$ rad/m.
>
> (b) $E_x\propto\sin\beta_1z$: nodes at $z = -m\lambda_1/2$. $H_y\propto\cos\beta_1z$: nodes at $z = -(2m+1)\lambda_1/4$.
>
> (c) $\beta_1z = -\pi/6$ and $\eta_1 = \eta_0/2 = 60\pi\ \Omega$:
> $$
> \lvert E_x\rvert = 2E_0\Big\lvert\sin\frac{\pi}{6}\Big\rvert = 10\ \text{V/m},\qquad \lvert H_y\rvert = \frac{2E_0}{\eta_1}\cos\frac{\pi}{6} = \frac{\sqrt3}{6\pi}\ \text{A/m}.
> $$
> **Watch out:** use $\lambda$ in the dielectric (12 cm), not the free-space 24 cm.
>
> **Answer.** (a) $\lambda_1 = 12$ cm. (b) $\mathbf{E}$ nodes at $z = 0$, $-6$, $-12$ cm; $\mathbf{H}$ nodes at $-3$, $-9$, $-15$ cm. (c) $\lvert E_x\rvert = 10$ V/m, $\lvert H_y\rvert = 91.9$ mA/m.

### 26.2 Standing waves true or false

> [!easy] Easy · true or false · standing waves · energy density
> A perfect mirror at $z = 0$ reflects a plane wave arriving from $z<0$ (free space). True or false?
>
> (a) The time-average Poynting vector is zero at every $z<0$.
>
> (b) The instantaneous Poynting vector is zero at every $z<0$ and every $t$.
>
> (c) For a linear wave, at some instant $\tfrac12\epsilon_0\mathbf{E}\cdot\mathbf{E}+\tfrac12\mu_0\mathbf{H}\cdot\mathbf{H} = 0$ throughout $z<0$.
>
> (d) Snapshots of one component against $z$ at several instants are sinusoids of different heights with the same zeros, $\lambda/2$ apart. They could be $E_x$ or $H_y$ here, but not a travelling wave.
>
> (e) $E_x$ at an $\mathbf{E}$ antinode and $H_y$ at an $\mathbf{H}$ antinode peak at the same instants.
>
> (f) A right-circular incident wave comes back right-circular.
>
> *Source: SP17 Exam 3 #1c and FA23 Exam 3 #1(c)–(d) style, reworded and extended.*

> [!solution]- Solution
> Linear case: $\mathbf{E} = \hat x\,2E_0\sin\beta z\sin\omega t$, $\mathbf{H} = \hat y\,(2E_0/\eta_0)\cos\beta z\cos\omega t$.
>
> (a) **True.** $\langle\mathbf{S}\rangle\propto\text{Re}\{-j\} = 0$: equal power flows both ways.
>
> (b) **False.** $\mathbf{S} = \hat z\,(E_0^2/\eta_0)\sin2\beta z\sin2\omega t$; zero only at multiples of $\lambda/4$ or when $\sin2\omega t = 0$.
>
> (c) **False.** $w = 2\epsilon_0E_0^2(\sin^2\beta z\sin^2\omega t+\cos^2\beta z\cos^2\omega t)$. When $\mathbf{E} = 0$ everywhere ($\sin\omega t = 0$), $\mathbf{H}$ is at its peak. $w$ vanishes only at isolated planes: $\mathbf{E}$ nodes when $\cos\omega t = 0$, $\mathbf{H}$ nodes when $\sin\omega t = 0$.
>
> (d) **True.** A travelling wave's zeros move by $v\Delta t$; fixed zeros mean standing. $E_x$ and $H_y$ have the same shape, shifted by $\lambda/4$; without the mirror's position the plot cannot tell them apart.
>
> (e) **False.** $E_x\propto\sin\omega t$, $H_y\propto\cos\omega t$: a quarter period apart.
>
> (f) **False.** $\Gamma = -1$ flips both components, so $\mathbf{E}$ at the mirror turns the same way; the travel reverses, so the hand flips to left.
>
> **Answer.** (a) T, (b) F, (c) F, (d) T, (e) F, (f) F.

### 26.3 Travelling, standing or both

> [!easy] Easy · multiple choice · standing waves · partial reflection
> A plane wave in air ($z>0$) travels toward $-\hat z$ and meets a flat boundary at $z = 0$. For each material filling $z<0$, which describes the total field in the air?
>
> (i) a perfect conductor; (ii) a lossless dielectric with $\epsilon_r = 4$, $\mu_r = 1$; (iii) a lossless material with $\epsilon_r = \mu_r = 5$.
>
> (a) all travelling
>
> (b) all standing
>
> (c) part travelling, part standing
>
> (d) part travelling, part evanescent
>
> (e) none of these
>
> For (ii), also give the largest and smallest $\lvert\tilde{\mathbf{E}}\rvert$ in the air, in units of the incident amplitude $E_0$.
>
> *Source: SP19 Exam 3 #3c style, three media instead of one.*

> [!solution]- Solution
> $\Gamma = (\eta_2-\eta_0)/(\eta_2+\eta_0)$ decides.
>
> (i) $\eta_2 = 0$, $\Gamma = -1$: equal and opposite waves. **(b)**.
>
> (ii) $\eta_2 = \eta_0/2$, $\Gamma = -1/3$: a travelling wave of amplitude $(1-\lvert\Gamma\rvert)E_0$ plus a standing wave. **(c)**. $\lvert\tilde{\mathbf{E}}\rvert$ ripples between $(1\pm\lvert\Gamma\rvert)E_0$, i.e. $\tfrac23E_0$ (at the interface, since $\Gamma<0$) and $\tfrac43E_0$.
>
> (iii) $\eta_2 = \eta_0\sqrt{5/5} = \eta_0$, $\Gamma = 0$: no reflection. **(a)**.
>
> (d) never applies: at normal incidence on these media nothing decays in the air. (e) is not needed.
>
> **Answer.** (i) (b); (ii) (c), $\lvert\tilde{\mathbf{E}}\rvert$ from $\tfrac23E_0$ to $\tfrac43E_0$; (iii) (a).

### 26.4 A laser on a small mirror

> [!easy] Easy · find the error · radiation pressure
> A 3 W laser beam with a 2 mm² cross-section hits a perfect mirror of area 4 cm² head-on and reflects straight back. A student writes:
>
> *"$\langle S_i\rangle = 3/(2\times10^{-6}) = 1.5\times10^6$ W/m². Pressure $2\langle S_i\rangle/c = 10^{-2}$ Pa. Force = pressure × mirror area $= 10^{-2}\times4\times10^{-4} = 4\ \mu$N."*
>
> Find the slip. Give the correct force on the mirror, and on a black absorber in its place. Use $c = 3\times10^8$ m/s.
>
> *Source: original.*

> [!solution]- Solution
> **Slip:** the pressure acts only where the beam lands. Multiply by the beam's area:
> $$
> F = \frac{2\langle S_i\rangle}{c}A_{\text{beam}} = \frac{2P}{c} = \frac{6}{3\times10^8} = 20\ \text{nN}.
> $$
> The student's 4 µN is $A_{\text{mirror}}/A_{\text{beam}} = 200$ times too big. An absorber stops the momentum without reversing it: $P/c = 10$ nN.
>
> **Check:** the beam brings momentum $P/c$ per second whatever its width, so the force cannot depend on the spot size.
>
> **Answer.** The mirror's area was used instead of the beam's. 20 nN on the mirror, 10 nN on the absorber.

### 26.5 Sunlight at Mars

> [!easy] Easy · radiation pressure · intensity
> At Mars's distance from the Sun, sunlight carries about $\langle S_i\rangle = 600$ W/m². Treat it as one linearly polarized plane wave at normal incidence. Use $c = 3\times10^8$ m/s, $\eta_0 = 120\pi\ \Omega$.
>
> (a) Find the radiation pressure on a perfect mirror and on a black absorber. (b) Find the force on a 20 m × 20 m sail of each kind. (c) Find $E_0$ and the peak surface current on the mirror.
>
> *Source: original.*

> [!solution]- Solution
> (a) Mirror: $2\langle S_i\rangle/c = 1200/(3\times10^8) = 4\ \mu$Pa. Absorber: $\langle S_i\rangle/c = 2\ \mu$Pa.
>
> (b) Times 400 m²: 1.6 mN and 0.8 mN.
>
> (c) $\langle S_i\rangle = E_0^2/2\eta_0$, so $E_0 = \sqrt{2\cdot120\pi\cdot600} = 673$ V/m, and $J_s = 2E_0/\eta_0 = 3.57$ A/m at its peak.
>
> **Check:** $\epsilon_0E_0^2 = 4\ \mu$Pa, Lecture 26's $\langle P_{rad}\rangle = \epsilon_0E_0^2$ for a mirror.
>
> **Answer.** (a) 4 µPa (mirror), 2 µPa (absorber). (b) 1.6 mN, 0.8 mN. (c) $E_0\approx673$ V/m; $J_s$ peaks at 3.57 A/m.

## Medium

### 26.6 A mirror off the origin

> [!medium] Medium · standing waves · perfect conductor
> Free space fills $z<d$ with $d = 37.5$ cm; a perfect conductor fills $z>d$. The incident wave is $\mathbf{E}_i = \hat y\,5\cos(\omega t-\beta z)$ V/m at $f = 300$ MHz. Use $\eta_0 = 120\pi\ \Omega$, $c = 3\times10^8$ m/s.
>
> (a) Find the reflected $\mathbf{E}_r(z,t)$.
>
> (b) Show that $\mathbf{E} = \hat y\,10\sin\beta(z-d)\,\sin(\omega t-\beta d)$, and find $\mathbf{H}(z,t)$.
>
> (c) List the $\mathbf{E}$ and $\mathbf{H}$ nodes in $-50\text{ cm}<z\le d$.
>
> (d) Find $\mathbf{J}_s(t)$ on the mirror.
>
> (e) At $z = 0$, find the amplitudes of $E_y$ and $H_x$, and the first $t>0$ at which $\lvert E_y\rvert$ peaks.
>
> *Source: original.*

> [!hint]- Hint
> $\Gamma = -1$ holds **at the mirror**: $\mathbf{E}_r(d,t) = -\mathbf{E}_i(d,t)$, with $\mathbf{E}_r$ travelling toward $-\hat z$. Here $\beta d = 3\pi/4$. Use $\cos A-\cos B = -2\sin\tfrac{A+B}{2}\sin\tfrac{A-B}{2}$.

> [!solution]- Solution
> **Setup.** $\beta = \omega/c = 2\pi$ rad/m, $\lambda = 1$ m, $\beta d = 3\pi/4$.
>
> (a) A $-\hat z$ wave equal to $-\mathbf{E}_i$ at $z = d$:
> $$
> \mathbf{E}_r = -\hat y\,5\cos(\omega t+\beta z-2\beta d) = -\hat y\,5\cos\big(\omega t+2\pi z-\tfrac{3\pi}{2}\big) = \hat y\,5\sin(\omega t+2\pi z)\ \text{V/m}.
> $$
> (b) $A = \omega t-\beta z$, $B = \omega t+\beta z-2\beta d$: $\tfrac{A+B}{2} = \omega t-\beta d$ and $\tfrac{A-B}{2} = -\beta(z-d)$, so $5(\cos A-\cos B)$ gives the stated $\mathbf{E}$. For $\mathbf{H} = \hat u\times\mathbf{E}/\eta_0$: $\hat z\times\hat y = -\hat x$, and $(-\hat z)\times(-\hat y) = -\hat x$, so $\mathbf{H} = -\hat x\,\tfrac{5}{\eta_0}(\cos A+\cos B)$:
> $$
> \mathbf{H} = -\hat x\,\frac{1}{12\pi}\cos\beta(z-d)\,\cos(\omega t-\beta d)\ \text{A/m}.
> $$
> (c) $\mathbf{E}$ nodes ($\sin\beta(z-d) = 0$): $z = 37.5$ cm (the mirror) and $-12.5$ cm. $\mathbf{H}$ nodes ($\cos\beta(z-d) = 0$): $z = 12.5$ cm and $-37.5$ cm.
>
> (d) $\hat n = -\hat z$ (conductor into air), $(-\hat z)\times(-\hat x) = \hat y$:
> $$
> \mathbf{J}_s = -\hat z\times\mathbf{H}(d,t) = \hat y\,\frac{1}{12\pi}\cos\big(\omega t-\tfrac{3\pi}{4}\big)\ \text{A/m}.
> $$
> (e) $\beta(0-d) = -3\pi/4$: $\lvert E_y\rvert = 10\sin\tfrac{3\pi}{4} = 7.07$ V/m, $\lvert H_x\rvert = \tfrac{1}{12\pi}\lvert\cos\tfrac{3\pi}{4}\rvert = 18.8$ mA/m. $\lvert\sin(\omega t-\tfrac{3\pi}{4})\rvert = 1$ first at $\omega t = \pi/4$: $t = 1/8f = 0.417$ ns.
>
> **Check:** $\mathbf{J}_s = 2\mathbf{E}_i(d,t)/\eta_0$, along the incident $\mathbf{E}$ at the wall, as on the page.
>
> **Answer.** (a) $\mathbf{E}_r = \hat y\,5\sin(\omega t+2\pi z)$ V/m. (b) $\mathbf{H} = -\hat x\,\tfrac{1}{12\pi}\cos(2\pi z-\tfrac{3\pi}{4})\cos(\omega t-\tfrac{3\pi}{4})$ A/m. (c) $\mathbf{E}$ nodes at 37.5 and $-12.5$ cm; $\mathbf{H}$ nodes at 12.5 and $-37.5$ cm. (d) $\mathbf{J}_s = \hat y\,26.5\cos(\omega t-\tfrac{3\pi}{4})$ mA/m. (e) 7.07 V/m, 18.8 mA/m; $t = 0.417$ ns.

### 26.7 Energy in a quarter-wave cell

> [!medium] Medium · energy density · Poynting vector · standing waves
> A lossless dielectric ($\epsilon_r = 2.25$, $\mu_r = 1$) fills $z<0$; a perfect conductor fills $z>0$. The 2 GHz wave $\mathbf{E}_i = \hat x\,30\cos(\omega t-\beta_1z)$ V/m is incident. Use $\eta_0 = 120\pi\ \Omega$, $c = 3\times10^8$ m/s, $\epsilon_0 = 10^{-9}/36\pi$ F/m.
>
> (a) Find the largest instantaneous $\lvert\mathbf{S}\rvert$, one place and instant where it occurs, and its direction there.
>
> (b) Find $\langle w\rangle$.
>
> (c) Show that the energy per m² between the mirror and the nearest $\mathbf{H}$ node does not change with time, and find it.
>
> (d) Where is that energy at $\omega t = 0$, and where at $\omega t = \pi/2$?
>
> *Source: original.*

> [!hint]- Hint
> Use Lecture 26's $\mathbf{S} = \hat z\,(E_0^2/\eta_1)\sin2\beta_1z\sin2\omega t$ and $w = 2\epsilon_1E_0^2[\sin^2\beta_1z\sin^2\omega t+\cos^2\beta_1z\cos^2\omega t]$. Over a quarter wavelength, $\int\sin^2\beta_1z\,dz = \int\cos^2\beta_1z\,dz = \lambda_1/8$.

> [!solution]- Solution
> **Setup.** $\eta_1 = 80\pi\ \Omega$, $\lambda_1 = 10$ cm, $\beta_1 = 20\pi$ rad/m, $\epsilon_1 = 2.25\epsilon_0$.
>
> (a) $\lvert\mathbf{S}\rvert_{\max} = E_0^2/\eta_1 = 900/80\pi = 3.58$ W/m², where $\lvert\sin2\beta_1z\rvert = \lvert\sin2\omega t\rvert = 1$. At $z = -\lambda_1/8 = -1.25$ cm and $\omega t = \pi/4$: $\mathbf{S} = -\hat z\,3.58$ W/m², away from the mirror.
>
> (b) $\langle w\rangle = \epsilon_1E_0^2 = 2.25\cdot\dfrac{10^{-9}}{36\pi}\cdot900 = 1.79\times10^{-8}$ J/m³, at every $z$.
>
> (c) The cell is $-\lambda_1/4<z<0$:
> $$
> W = 2\epsilon_1E_0^2\Big[\frac{\lambda_1}{8}\sin^2\omega t+\frac{\lambda_1}{8}\cos^2\omega t\Big] = \frac{\epsilon_1E_0^2\lambda_1}{4} = 4.48\times10^{-10}\ \text{J/m}^2.
> $$
> No $t$ left. Reason: $\sin2\beta_1z = 0$ at both ends, so $\mathbf{S} = 0$ there and no energy crosses them.
>
> (d) $\omega t = 0$: $\mathbf{E} = 0$, all magnetic, peaked at the mirror ($\mathbf{H}$ antinode). $\omega t = \pi/2$: $\mathbf{H} = 0$, all electric, peaked at $z = -2.5$ cm ($\mathbf{E}$ antinode). For $0<\omega t<\pi/2$, $S_z<0$ inside the cell: the energy moves out from the mirror; it returns for $\pi/2<\omega t<\pi$.
>
> **Check:** $\partial w/\partial t = -\partial S_z/\partial z$ at every $z$ and $t$ (Poynting's theorem without losses).
>
> **Answer.** (a) 3.58 W/m², e.g. at $z = -1.25$ cm, $\omega t = \pi/4$, along $-\hat z$. (b) $1.79\times10^{-8}$ J/m³. (c) $\epsilon_1E_0^2\lambda_1/4 = 4.48\times10^{-10}$ J/m², constant. (d) Magnetic, at the mirror ($\omega t = 0$); electric, at $z = -2.5$ cm ($\omega t = \pi/2$).

### 26.8 Ripple in front of a dielectric

> [!medium] Medium · partial reflection · reflection coefficient
> Air fills $z<0$; a lossless non-magnetic dielectric fills $z>0$. A wave arrives from the air along $+\hat z$. A probe moved through $z<0$ reads the amplitude of $E_x$: it ripples between 5 V/m and 10 V/m, with minima at $z = 0$, $-10$ cm, $-20$ cm, …. Use $\eta_0 = 120\pi\ \Omega$, $c = 3\times10^8$ m/s.
>
> (a) Find the incident amplitude $E_0$, and $\Gamma$ with its sign.
>
> (b) Find $\epsilon_r$ and $f$.
>
> (c) Find the net $\langle\mathbf{S}\rangle$ in the air and the fraction of the incident power that enters the dielectric.
>
> (d) Could a lossless non-magnetic dielectric put a **maximum** at $z = 0$?
>
> *Source: original.*

> [!hint]- Hint
> $\lvert\tilde E_x\rvert = E_0\lvert1+\Gamma e^{j2\beta_0z}\rvert$ lies between $(1-\lvert\Gamma\rvert)E_0$ and $(1+\lvert\Gamma\rvert)E_0$; at $z = 0$ it is $\lvert1+\Gamma\rvert E_0$. Adjacent minima are $\lambda/2$ apart.

> [!solution]- Solution
> (a) $(1+\lvert\Gamma\rvert)E_0 = 10$ and $(1-\lvert\Gamma\rvert)E_0 = 5$: $E_0 = 7.5$ V/m, $\lvert\Gamma\rvert = 1/3$. A minimum at $z = 0$ needs $\lvert1+\Gamma\rvert = 1-\lvert\Gamma\rvert$: $\Gamma = -1/3$.
>
> (b) $\eta_2 = \eta_0\dfrac{1+\Gamma}{1-\Gamma} = \dfrac{\eta_0}{2}$, so $\epsilon_r = 4$. Minima 10 cm apart: $\lambda_0 = 20$ cm, $f = c/\lambda_0 = 1.5$ GHz.
>
> (c) Same at every $z<0$:
> $$
> \langle\mathbf{S}\rangle = \hat z\,(1-\lvert\Gamma\rvert^2)\frac{E_0^2}{2\eta_0} = \hat z\,\frac{8}{9}\cdot\frac{56.25}{240\pi} = \hat z\,66.3\ \text{mW/m}^2.
> $$
> Fraction entering: $1-\lvert\Gamma\rvert^2 = 8/9 = 88.9$ %.
>
> (d) No. A maximum at $z = 0$ needs $\Gamma>0$, i.e. $\eta_2>\eta_0$, i.e. $\epsilon_r<1$ ($\Gamma = +1/3$ would need $\epsilon_r = 1/4$).
>
> **Check:** transmitted side, $\lvert\tau E_0\rvert^2/2\eta_2 = 5^2/(2\cdot60\pi) = 66.3$ mW/m² ✓.
>
> **Watch out:** the ripple's period is $\lambda/2$. Taking 10 cm as $\lambda$ gives a wrong $f = 3$ GHz.
>
> **Answer.** (a) $E_0 = 7.5$ V/m, $\Gamma = -1/3$. (b) $\epsilon_r = 4$, $f = 1.5$ GHz. (c) $\hat z\,66.3$ mW/m²; 88.9 % enters. (d) No: it would need $\epsilon_r = 1/4$.

## Hard

### 26.9 Is it a standing wave

> [!hard] Hard · standing waves · nodes and antinodes · perfect conductor
> A source-free, lossless, non-magnetic medium carries
> $$
> \mathbf{E} = \hat x\,120\cos(20\pi y)\cos\omega t\ \text{V/m},\qquad \mathbf{H} = \hat z\,H_0\sin(20\pi y)\sin\omega t\ \text{A/m},
> $$
> with $\omega = 3\pi\times10^9$ rad/s. Use $\mu_0 = 4\pi\times10^{-7}$ H/m, $\epsilon_0 = 10^{-9}/36\pi$ F/m.
>
> (a) From Faraday's law find $H_0$ (with sign); then from Ampère–Maxwell find $\epsilon_r$.
>
> (b) Write the fields as two travelling waves: direction, amplitude, $\lambda$ and $\mathbf{H}$ of each.
>
> (c) Find $\langle\mathbf{S}\rangle$ and $\langle w\rangle$.
>
> (d) A perfect conductor is to fill $y\ge y_1$ without changing the fields in $y<y_1$. Find the smallest $y_1>0$ and $\mathbf{J}_s(t)$ there.
>
> (e) Why can the conductor's face not be at $y = 0$?
>
> *Source: SP17 Exam 3 #1b, re-parameterized (a dielectric, E as cos·cos, unknown amplitude and medium, parts b–e added).*

> [!hint]- Hint
> Only $\partial/\partial y$ acts: $\nabla\times\mathbf{E} = -\hat z\,\partial_yE_x$ and $\nabla\times\mathbf{H} = \hat x\,\partial_yH_z$. Match the $y$ and $t$ factors on both sides. For (b), $2\cos a\cos b = \cos(a-b)+\cos(a+b)$. For (d), the face must be an $\mathbf{E}$ node.

> [!solution]- Solution
> **(a)** Faraday, $\nabla\times\mathbf{E} = -\mu_0\,\partial\mathbf{H}/\partial t$:
> $$
> \hat z\,2400\pi\sin(20\pi y)\cos\omega t = -\hat z\,\mu_0\omega H_0\sin(20\pi y)\cos\omega t\ \Rightarrow\ H_0 = -\frac{2400\pi}{1200\pi^2} = -\frac{2}{\pi}\ \text{A/m}.
> $$
> Ampère–Maxwell, $\nabla\times\mathbf{H} = \epsilon\,\partial\mathbf{E}/\partial t$:
> $$
> \hat x\,20\pi H_0\cos(20\pi y)\sin\omega t = -\hat x\,120\epsilon\omega\cos(20\pi y)\sin\omega t\ \Rightarrow\ \epsilon = -\frac{20\pi H_0}{120\omega} = \frac{10^{-9}}{9\pi} = 4\epsilon_0.
> $$
> So $\epsilon_r = 4$. **Check:** $\omega\sqrt{\mu_0\epsilon} = 2\omega/c = 20\pi$ ✓, and $120/\lvert H_0\rvert = 60\pi = \eta_1$ ✓. Both divergences vanish.
>
> **(b)** $\lambda = 10$ cm, $\eta_1 = 60\pi\ \Omega$:
> $$
> \mathbf{E} = \hat x\,60\cos(\omega t-20\pi y)+\hat x\,60\cos(\omega t+20\pi y)\ \text{V/m}.
> $$
> Toward $+\hat y$: $\mathbf{H} = \hat y\times\hat x\,\tfrac{60}{60\pi}\cos(\cdot) = -\hat z\,\tfrac{1}{\pi}\cos(\omega t-20\pi y)$. Toward $-\hat y$: $+\hat z\,\tfrac{1}{\pi}\cos(\omega t+20\pi y)$. Sum: $-\hat z\,\tfrac{2}{\pi}\sin(20\pi y)\sin\omega t$ ✓.
>
> **(c)** Equal waves both ways: $\langle\mathbf{S}\rangle = 0$ (instantaneously $\mathbf{S} = \hat y\,\tfrac{60}{\pi}\sin(40\pi y)\sin2\omega t$). $\langle w\rangle = \epsilon_1\cdot60^2 = \tfrac{4}{\pi}\times10^{-7} = 1.27\times10^{-7}$ J/m³ at every $y$.
>
> **(d)** $\cos(20\pi y_1) = 0$: $y_1 = 2.5$ cm. There $\mathbf{H} = -\hat z\,\tfrac{2}{\pi}\sin\omega t$ and $\hat n = -\hat y$:
> $$
> \mathbf{J}_s = -\hat y\times\Big(-\hat z\,\frac{2}{\pi}\sin\omega t\Big) = \hat x\,\frac{2}{\pi}\sin\omega t\ \text{A/m}.
> $$
> **Check:** the $+\hat y$ wave at $y_1$ is $\hat x\,60\sin\omega t$, and $2\cdot60/\eta_1 = 2/\pi$, along it ✓.
>
> **(e)** At $y = 0$, $E_x = 120\cos\omega t$ (antinode) and $\mathbf{H} = 0$: an "open", not a "short". A conductor there would force $E_x = 0$ and change the fields.
>
> **Answer.** (a) $H_0 = -2/\pi\approx-0.637$ A/m, $\epsilon_r = 4$. (b) $\hat x\,60\cos(\omega t\mp20\pi y)$ V/m toward $\pm\hat y$, $\lambda = 10$ cm, with $\mathbf{H} = \mp\hat z\,\tfrac{1}{\pi}\cos(\omega t\mp20\pi y)$ A/m. (c) $\langle\mathbf{S}\rangle = 0$, $\langle w\rangle = 1.27\times10^{-7}$ J/m³. (d) $y_1 = 2.5$ cm, $\mathbf{J}_s = \hat x\,0.637\sin\omega t$ A/m. (e) $y = 0$ is an $\mathbf{E}$ antinode.

### 26.10 A good-conductor mirror

> [!hard] Hard · good conductor · skin depth · radiation pressure
> A 1 GHz wave in air, $\mathbf{E}_i = \hat x\,100\cos(\omega t-\beta z)$ V/m, meets a flat aluminium wall ($\sigma = 3.5\times10^7$ S/m, $\epsilon_0$, $\mu_0$) filling $z>0$. Use $\eta_0 = 120\pi\ \Omega$, $c = 3\times10^8$ m/s, $\epsilon_0 = 10^{-9}/36\pi$ F/m. Calculator allowed.
>
> (a) Show that aluminium is a good conductor here; find $\delta$ and $R_s$.
>
> (b) Find the effective surface current and the current density at the surface, $\lvert\tilde{\mathbf{J}}(0)\rvert$.
>
> (c) Find the power absorbed per m² and the absorbed fraction of $\langle S_i\rangle$.
>
> (d) Find the time-average radiation pressure, its peak value and its direction.
>
> *Source: original (Lecture 26 §5–6, new metal and frequency).*

> [!hint]- Hint
> The depth integral of $\tilde{\mathbf{J}}$ is the perfect mirror's $\hat x\,2E_0/\eta_0$, whatever $\sigma$. With $\tilde{\mathbf{J}}(z) = \tilde{\mathbf{J}}_s\gamma e^{-\gamma z}$ and $\lvert\gamma\rvert = \sqrt2/\delta$, the heat per m² is $\tfrac12R_s\lvert\tilde{\mathbf{J}}_s\rvert^2$.

> [!solution]- Solution
> **(a)** $\omega\epsilon_0 = 1/18$ S/m, so $\sigma/\omega\epsilon_0 = 6.3\times10^8\gg1$.
> $$
> \delta = \frac{1}{\sqrt{\pi f\mu_0\sigma}} = 2.69\ \mu\text{m},\qquad R_s = \frac{1}{\sigma\delta} = 10.6\ \text{m}\Omega.
> $$
> **(b)** $\tilde{\mathbf{J}}_s = \hat x\,\dfrac{2E_0}{\eta_0} = \hat x\,\dfrac{5}{3\pi} = \hat x\,0.531$ A/m. At the surface:
> $$
> \lvert\tilde{\mathbf{J}}(0)\rvert = \lvert\tilde{\mathbf{J}}_s\rvert\lvert\gamma\rvert = 0.531\times\frac{\sqrt2}{2.69\times10^{-6}} = 2.79\times10^5\ \text{A/m}^2.
> $$
> **(c)** $\tfrac12R_s\lvert\tilde{\mathbf{J}}_s\rvert^2 = \tfrac12(0.0106)(0.531)^2 = 1.49$ mW/m². With $\langle S_i\rangle = 100^2/240\pi = 13.26$ W/m², the fraction is $4R_s/\eta_0 = 1.13\times10^{-4}$.
>
> **(d)** $\langle P_{rad}\rangle = 2\langle S_i\rangle/c = 88.4$ nPa, along $\hat x\times\hat y = +\hat z$ (into the wall). Instantaneously, Lecture 26 §6's perfect-mirror form $\tfrac12\mu_0H_y^2(0,t) = (4\langle S_i\rangle/c)\cos^2\omega t$ (valid since $\lvert\eta_2\rvert\ll\eta_0$): peak 177 nPa.
>
> **Check:** integrating the exact fields (exact $\gamma_2$, $\eta_2$, $\tau$) gives $\lvert\int\tilde{\mathbf{J}}\,dz\rvert = 0.5305$ A/m, the same 1.49 mW/m², a 176.8 nPa peak, and $\langle P_{rad}\rangle = 88.41$ nPa $= (1+\lvert\Gamma\rvert^2)\langle S_i\rangle/c$, within 0.006 % of the mirror value.
>
> **Watch out:** $\tilde{\mathbf{J}}_s$ is fixed by $E_0$; $\lvert\tilde{\mathbf{J}}(0)\rvert$ grows as $\sigma$ grows, because the same current squeezes into a thinner layer.
>
> **Answer.** (a) $\sigma/\omega\epsilon_0 = 6.3\times10^8$; $\delta = 2.69$ µm, $R_s = 10.6$ mΩ. (b) $\hat x\,0.531$ A/m; $2.79\times10^5$ A/m². (c) 1.49 mW/m², a fraction $1.13\times10^{-4}$ of 13.26 W/m². (d) 88.4 nPa average, 177 nPa peak, along $+\hat z$.

### 26.11 Pushing a sail with a laser

> [!hard] Hard · radiation pressure · intensity
> A ground-based, linearly polarized laser ($\lambda = 1\ \mu$m, $P = 30$ kW) lights a sail of area 3 m² and mass 1 g at normal incidence; the beam covers the sail uniformly. Use $c = 3\times10^8$ m/s, $\eta_0 = 120\pi\ \Omega$, $h = 6.63\times10^{-34}$ J·s. Ignore gravity.
>
> (a) Find $E_0$ of the beam and the peak surface current if the sail is a perfect mirror.
>
> (b) Find the force and acceleration for a perfect mirror, and for a sail that reflects 90 % of the power and absorbs the rest.
>
> (c) How much power does the 90 % sail absorb?
>
> (d) Find the photon rate; show that photon momenta give the mirror force.
>
> (e) Find each sail's speed one hour after starting from rest.
>
> *Source: original.*

> [!hint]- Hint
> Momentum view: the beam brings momentum $P/c$ per second. An absorber keeps it; a mirror reverses it; a partial reflector reverses only the reflected share. A photon carries energy $\hbar\omega = hc/\lambda$ and momentum $\hbar\omega/c = h/\lambda$.

> [!solution]- Solution
> **(a)** $\langle S_i\rangle = 30\,000/3 = 10^4$ W/m². $E_0 = \sqrt{2\eta_0\langle S_i\rangle} = 2.75$ kV/m; $J_s = 2E_0/\eta_0 = 14.6$ A/m peak.
>
> **(b)** Mirror: $F = 2P/c = 0.2$ mN, $a = F/m = 0.2$ m/s². 90 % sail: $P/c$ arrives and is stopped, $0.9P/c$ leaves backwards, so $F = 1.9P/c = 0.19$ mN and $a = 0.19$ m/s².
>
> **(c)** $0.1\times30$ kW $= 3$ kW (1 kW/m²).
>
> **(d)** $hc/\lambda = 1.99\times10^{-19}$ J, so $1.51\times10^{23}$ photons/s, each with $h/\lambda = 6.63\times10^{-28}$ N·s. A mirror reverses each one:
> $$
> F = 2\times1.51\times10^{23}\times6.63\times10^{-28} = 2\times10^{-4}\ \text{N},
> $$
> the 0.2 mN of (b) ✓.
>
> **(e)** $v = at$: $0.2\times3600 = 720$ m/s and $0.19\times3600 = 684$ m/s.
>
> **Check:** absorbing 10 % of the power costs only 5 % of the push; the 2 in $2P/c$ is the recoil.
>
> **Watch out:** the sail's area never enters the force, only the intercepted power.
>
> **Answer.** (a) $E_0 = 2.75$ kV/m, $J_s = 14.6$ A/m. (b) Mirror 0.2 mN, 0.2 m/s²; 90 % sail 0.19 mN, 0.19 m/s². (c) 3 kW. (d) $1.51\times10^{23}$ photons/s; $2\times1.51\times10^{23}\times6.63\times10^{-28} = 0.2$ mN. (e) 720 m/s and 684 m/s.

### 26.12 Trapped between two mirrors

> [!hard] Hard · standing waves · radiation pressure · perfect conductor
> Perfect conductors fill $z\le0$ and $z\ge L$, $L = 15$ cm, with air between. The field between them has the page's form, $\mathbf{E} = \hat x\,2E_0\sin\beta z\sin\omega t$, $\mathbf{H} = \hat y\,(2E_0/\eta_0)\cos\beta z\cos\omega t$, with $E_0 = 50$ V/m and $\beta = \omega/c$. Use $\eta_0 = 120\pi\ \Omega$, $c = 3\times10^8$ m/s, $\epsilon_0 = 10^{-9}/36\pi$ F/m.
>
> (a) Which frequencies are allowed? Give the lowest three.
>
> (b) For the third, write $\mathbf{E}$ and $\mathbf{H}$ with numbers and list the interior $\mathbf{E}$ and $\mathbf{H}$ nodes.
>
> (c) Find $\mathbf{J}_s(t)$ on both walls.
>
> (d) Find the time-average pressure on each wall with its direction, and the stored energy per m² of wall.
>
> (e) Write the field as two travelling waves. At the second frequency, do the walls' currents flow the same way or opposite ways?
>
> *Source: original.*

> [!hint]- Hint
> The wall at $z = L$ must sit at an $\mathbf{E}$ node. On each wall $\mathbf{J}_s = \hat n\times\mathbf{H}$ with $\hat n$ out of that conductor into the air: $+\hat z$ at $z = 0$, $-\hat z$ at $z = L$. The instantaneous pressure is $\tfrac12\mu_0\lvert\mathbf{H}\rvert^2$ at the wall (Lecture 26 §6), pushing into the conductor.

> [!solution]- Solution
> **(a)** $\sin\beta L = 0$: $\beta L = m\pi$, $f_m = mc/2L = m\times1$ GHz. Lowest: 1, 2, 3 GHz.
>
> **(b)** $m = 3$: $\omega = 6\pi\times10^9$ rad/s, $\beta = 20\pi$ rad/m, $\lambda = 10$ cm, $2E_0/\eta_0 = 5/6\pi = 0.265$ A/m:
> $$
> \mathbf{E} = \hat x\,100\sin(20\pi z)\sin\omega t\ \text{V/m},\qquad \mathbf{H} = \hat y\,\frac{5}{6\pi}\cos(20\pi z)\cos\omega t\ \text{A/m}.
> $$
> $\mathbf{E}$ nodes at 5 and 10 cm (plus the walls); $\mathbf{H}$ nodes at 2.5, 7.5 and 12.5 cm.
>
> **(c)** $\mathbf{H}(0,t) = \hat y\,\tfrac{5}{6\pi}\cos\omega t$; $\mathbf{H}(L,t) = \hat y\,\tfrac{5}{6\pi}\cos3\pi\cos\omega t = -\hat y\,\tfrac{5}{6\pi}\cos\omega t$:
> $$
> \mathbf{J}_s(0) = \hat z\times\mathbf{H}(0,t) = -\hat x\,\frac{5}{6\pi}\cos\omega t,\qquad \mathbf{J}_s(L) = -\hat z\times\mathbf{H}(L,t) = -\hat x\,\frac{5}{6\pi}\cos\omega t\ \text{A/m}.
> $$
> **(d)** On each wall $\langle P\rangle = \tfrac14\mu_0\big(\tfrac{5}{6\pi}\big)^2 = \epsilon_0E_0^2 = 2.21\times10^{-8}$ Pa, outward: $-\hat z$ on the $z = 0$ wall, $+\hat z$ on the $z = L$ wall. (At $z = L$: $\mathbf{J}_s\times\tfrac12\mu_0\mathbf{H}\propto(-\hat x)\times(-\hat y) = +\hat z$.) Stored energy $\langle w\rangle L = \epsilon_0E_0^2L = 3.32$ nJ/m², constant in time since $L$ holds a whole number of $\lambda/4$ cells.
>
> **(e)** $\mathbf{E} = \hat x\,50\cos(\omega t-\beta z)-\hat x\,50\cos(\omega t+\beta z)$ V/m. Each wave carries $\langle S\rangle = 50^2/240\pi = 3.32$ W/m²; each wall reflects it with $\Gamma = -1$ and so feels $2\langle S\rangle/c = 2.21\times10^{-8}$ Pa ✓. For $m = 2$, $\cos\beta L = +1$, so $\mathbf{H}(L,t) = \mathbf{H}(0,t)$ and $\mathbf{J}_s(L) = -\mathbf{J}_s(0)$: opposite ways.
>
> **Check:** Faraday holds with $\beta = \omega/c$, and $\mathbf{E} = 0$ on both walls at all $t$.
>
> **Answer.** (a) $f_m = m\times1$ GHz: 1, 2, 3 GHz. (b) $\mathbf{E} = \hat x\,100\sin(20\pi z)\sin\omega t$ V/m, $\mathbf{H} = \hat y\,0.265\cos(20\pi z)\cos\omega t$ A/m, $\omega = 6\pi\times10^9$ rad/s; $\mathbf{E}$ nodes 5, 10 cm, $\mathbf{H}$ nodes 2.5, 7.5, 12.5 cm. (c) Both walls: $\mathbf{J}_s = -\hat x\,0.265\cos\omega t$ A/m. (d) $2.21\times10^{-8}$ Pa outward on each; 3.32 nJ/m². (e) $\pm\hat z$ waves of 50 V/m; opposite ways.

### Sources for this page
Course notes, Lecture 26: the standing-wave phasors and real fields, nodes and the short/open picture, $\langle\mathbf{S}\rangle = 0$, the mirror current, the effective surface current and surface resistance, and the radiation-pressure box with its momentum notes, used throughout with new numbers. The site's Lecture 26 page: instantaneous $\mathbf{S}$ and $w$, the partial-reflection ripple, the instantaneous pressure, the partial reflector's $(1+\lvert\Gamma\rvert^2)\langle S_i\rangle/c$. Old exams, re-parameterized: SP17 Exam 3 #1c and FA23 Exam 3 #1(c)–(d) (26.2, reworded true/false with new items); SP19 Exam 3 #3c (26.3, three media); SP17 Exam 3 #1b (26.9: a dielectric, cos·cos form, unknown $H_0$ and $\epsilon_r$, conductor placement and $\mathbf{J}_s$ added). Aluminium's conductivity: Rao, Table 5.1. Original: 26.1, 26.4–26.8, 26.10–26.12.

*Previous: [[practice/25-reflection-and-transmission|Lecture 25 practice]] · next: [[practice/27-transmission-line-basics|Lecture 27 practice]] · [[practice/index|all practice]]*
