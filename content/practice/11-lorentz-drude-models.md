---
title: "Practice — Lecture 11: Lorentz–Drude models"
description: "8 practice problems (4 easy, 2 medium, 2 hard) on drift velocity and mobility, σ = Nq²τ/m for one or several carrier species, the AC conductivity σ(ω) as a low-pass filter, the Lorentz-model susceptibility χe, polarization current versus conduction current, and the Drude collision time versus the relaxation time ε/σ, each with a folded hint and a worked solution."
tags: [practice, electrostatics]
lecture: 11
---

*Practice for [[1-electrostatics/11-lorentz-drude-models-for-conductivity-and-susceptibility|Lecture 11]] · concepts: [[concepts/conductivity-and-susceptibility-models]] · [[concepts/conductors]] · [[concepts/polarization]] · [[concepts/permittivity]] · all practice: [[practice/index|hub]] · by difficulty: [[practice/easy|easy]] · [[practice/medium|medium]] · [[practice/hard|hard]] · [[practice/topics|by topic]]*

Work each problem on paper first. Open the **hint** only when stuck, and the **solution** only after you have an answer you would hand in. Every answer here has been checked numerically.

## Easy

### 11.1 Drift speed in a house wire

> [!easy] Easy · drift velocity · current density
> A copper wire with cross-sectional area $A = 1.5$ mm² carries a steady current $I = 10$ A in the $+\hat{z}$ direction. Copper has $N = 8.5\times10^{28}$ free electrons per m³, each of charge $-e$. (a) Find the current density $\mathbf{J}$. (b) Find the drift velocity $\mathbf{v}$ of the electrons, magnitude and direction. (c) How long does an electron take to drift 1 m along the wire?
>
> *Source: classic.*

> [!hint]- Hint
> The charge crossing unit area per second is $\mathbf{J} = Nq\mathbf{v}$. Solve for $\mathbf{v}$ with $q = -e$ and let the sign tell you the direction.

> [!solution]- Solution
> (a) The current is spread uniformly over the cross-section, so $J = I/A = 10/(1.5\times10^{-6}) = 6.67\times10^6$ A/m², pointing along $+\hat{z}$.
>
> (b) In one second, every electron within a distance $v$ of a cross-section crosses it, so $\mathbf{J} = Nq\mathbf{v}$ with $q = -e$:
> $$
> \mathbf{v} = \frac{\mathbf{J}}{N(-e)} = -\frac{6.67\times10^{6}}{8.5\times10^{28}\times1.602\times10^{-19}}\,\hat{z} = -4.9\times10^{-4}\,\hat{z}\ \text{m/s}.
> $$
> The electrons crawl at 0.49 mm/s *opposite* to the current: negative charge moving along $-\hat{z}$ is a current along $+\hat{z}$.
>
> (c) $t = (1\ \text{m})/(4.9\times10^{-4}\ \text{m/s}) = 2.0\times10^3$ s, about 34 minutes.
>
> **Why so slow?** The mobile charge density $Ne = 1.36\times10^{10}$ C/m³ is enormous, so a tiny drift already gives $Ne\lvert\mathbf{v}\rvert = 6.67\times10^6$ A/m² ✓.
>
> **Watch out:** the electrons' random thermal velocities are far larger than this drift, but they average to zero and carry no net current. A lamp still lights at once because the *field* travels down the wire at nearly $c$, not the electrons.
>
> **Answer.** $\mathbf{J} = 6.67\times10^6\,\hat{z}$ A/m²; $\mathbf{v} = -4.9\times10^{-4}\,\hat{z}$ m/s (0.49 mm/s, opposite to the current); about $2.0\times10^3$ s ≈ 34 min to drift 1 m.

### 11.2 Conductivity of aluminum from collisions

> [!easy] Easy · Drude model · mobility · conductivity
> Aluminum has $N = 1.8\times10^{29}$ conduction electrons per m³, and each electron collides with the lattice on average once every $\tau = 7.5\times10^{-15}$ s. Using the Drude model with the free-electron mass $m_e$, find (a) the conductivity $\sigma$, (b) the electron mobility, and (c) the drift velocity in the field $\mathbf{E} = 0.1\,\hat{x}$ V/m.
>
> *Source: classic.*

> [!hint]- Hint
> Set $d\mathbf{v}/dt = 0$ in $m\,d\mathbf{v}/dt = q\mathbf{E} - m\mathbf{v}/\tau$, then use $\mathbf{J} = Nq\mathbf{v}$.

> [!solution]- Solution
> In steady state the collisional friction $m\mathbf{v}/\tau$ balances the electric force $q\mathbf{E}$, so $\mathbf{v} = (q\tau/m)\mathbf{E}$ and $\mathbf{J} = Nq\mathbf{v} = (Nq^2\tau/m)\mathbf{E}$. (Starting from rest, $\mathbf{v}$ reaches 63% of this value after one $\tau$, so any field that changes slowly compared with $\tau$ sees the steady drift.)
>
> (a) $\sigma = \dfrac{Ne^2\tau}{m_e} = \dfrac{1.8\times10^{29}\times(1.602\times10^{-19})^2\times7.5\times10^{-15}}{9.109\times10^{-31}} = 3.8\times10^7$ S/m.
>
> (b) Mobility $= \dfrac{e\tau}{m_e} = \dfrac{1.602\times10^{-19}\times7.5\times10^{-15}}{9.109\times10^{-31}} = 1.32\times10^{-3}$ m²/(V·s).
>
> (c) With $q = -e$: $\mathbf{v} = -\dfrac{e\tau}{m_e}\mathbf{E} = -1.32\times10^{-4}\,\hat{x}$ m/s. The electrons drift *against* $\mathbf{E}$, while $\mathbf{J} = \sigma\mathbf{E}$ points along it.
>
> **Check:** $\sigma = Ne\times\text{mobility} = 1.8\times10^{29}\times1.602\times10^{-19}\times1.32\times10^{-3} = 3.8\times10^7$ S/m ✓. Units: $e\tau/m$ is C·s/kg, and since a volt is a kg·m²/(s²·C), that is m²/(V·s) ✓. Against copper ($\sigma = 5.96\times10^7$ S/m, mobility $4.4\times10^{-3}$ m²/(V·s)), aluminum has 2.1 times as many free electrons but each is 3.3 times less mobile, so it conducts less well.
>
> **Answer.** $\sigma = 3.8\times10^7$ S/m; mobility $1.32\times10^{-3}$ m²/(V·s); $\mathbf{v} = -1.32\times10^{-4}\,\hat{x}$ m/s (against $\mathbf{E}$).

### 11.3 Which change doubles the conductivity

> [!easy] Easy · multiple choice · Drude model
> A metal has $N$ free carriers per m³, each of charge $q$, mass $m$ and collision frequency $\nu$, and the Drude model gives it the conductivity $\sigma_0$. (For copper, $N = 8.5\times10^{28}$ m⁻³, $q = -e$, $m = m_e$ and $\nu = 4.1\times10^{13}$ s⁻¹ give $\sigma_0 = 5.84\times10^7$ S/m.) Which single change, with everything else held fixed, doubles the conductivity?
>
> (a) Doubling the applied field $\mathbf{E}$.
>
> (b) Doubling the magnitude of the carrier charge $q$.
>
> (c) Halving the collision frequency $\nu$.
>
> (d) Doubling the carrier mass $m$.
>
> (e) Replacing the carriers by carriers of the opposite charge, $q\to-q$.
>
> *Source: original.*

> [!hint]- Hint
> Write $\sigma = Nq^2/(m\nu)$ and ask, option by option, which factor changes and with what power.

> [!solution]- Solution
> The Drude conductivity is $\sigma = \dfrac{Nq^2}{m\nu}$: proportional to $N$ and to $q^2$, inversely proportional to $m$ and to $\nu$, and independent of $\mathbf{E}$.
>
> (a) Wrong. A larger field drives a proportionally larger drift and current — in copper, going from $E = 1$ to 2 V/m raises the drift speed from 4.29 to 8.58 mm/s and $J$ from $5.84\times10^7$ to $1.17\times10^8$ A/m² — but $\sigma = J/E$ stays $5.84\times10^7$ S/m. Ohm's law is linear; $\sigma$ is a property of the material.
>
> (b) Wrong. The charge enters twice — in the force $q\mathbf{E}$ and in $\mathbf{J} = Nq\mathbf{v}$ — so doubling $\lvert q\rvert$ makes $\sigma$ four times larger.
>
> (c) **Right.** Half as many collisions per second means twice as long, $\tau = 1/\nu$, to accelerate between them, hence twice the drift velocity in the same field: $\sigma = 2\sigma_0$.
>
> (d) Wrong. A carrier twice as heavy accelerates half as fast, so $\sigma = \sigma_0/2$.
>
> (e) Wrong. $q^2$ is unchanged, so $\sigma$ is unchanged: the new carriers drift the opposite way, but $\mathbf{J} = Nq\mathbf{v}$ still points along $\mathbf{E}$.
>
> **Answer.** (c): halving $\nu$ doubles $\sigma$.

### 11.4 True or false

> [!easy] Easy · true or false · Lorentz model · Drude model
> Decide whether each statement is true or false, and give a one-line reason.
>
> (i) In the Lorentz model, a static field $\mathbf{E}$ displaces each bound electron along $\mathbf{E}$, so the induced dipole moment $\mathbf{p}$ points opposite to $\mathbf{E}$.
>
> (ii) A perfect dielectric ($\sigma = 0$) with $\chi_e = 2$, in the field $\mathbf{E} = 100\cos(2\pi\cdot50\,t)\,\hat{x}$ V/m, carries no current of any kind.
>
> (iii) A dielectric with $N_d = 5\times10^{28}$ bound electrons per m³ and $\omega_0 = 2\times10^{16}$ rad/s has $\epsilon_r\approx1.4$.
>
> (iv) In copper ($\sigma = 5.8\times10^7$ S/m, $N = 8.5\times10^{28}$ m⁻³), the Drude collision time $\tau$ and the charge-relaxation time $\epsilon_0/\sigma$ of Lecture 8 are the same thing.
>
> (v) At 10 GHz the conductivity of copper ($\nu = 4\times10^{13}$ s⁻¹) is within 1% of its DC value.
>
> *Source: original.*

> [!hint]- Hint
> Each statement rests on one formula: $\mathbf{r} = -e\mathbf{E}/(m\omega_0^2)$ with $\mathbf{p} = -e\mathbf{r}$; $\mathbf{J}_p = \partial\mathbf{P}/\partial t$; $\chi_e = N_de^2/(m\epsilon_0\omega_0^2)$; $\tau = \sigma m_e/(Ne^2)$; $\sigma(\omega) = \sigma_{\text{DC}}/(1+j\omega/\nu)$. A handy number: $e^2/(m_e\epsilon_0) = 3.18\times10^3$ m³/s².

> [!solution]- Solution
> (i) **False.** The electron's charge is $-e$, so the field pulls it *against* $\mathbf{E}$: $\mathbf{r} = -\dfrac{e}{m\omega_0^2}\mathbf{E}$. The dipole points from the electron to the nucleus, $\mathbf{p} = -e\mathbf{r} = \dfrac{e^2}{m\omega_0^2}\mathbf{E}$, i.e. *along* $\mathbf{E}$ — which is why $\chi_e>0$. Both halves of the statement are reversed.
>
> (ii) **False.** As $\mathbf{E}$ changes, the bound electrons move, and that motion is a polarization current $\mathbf{J}_p = \partial\mathbf{P}/\partial t = -\omega\epsilon_0\chi_eE_0\sin(\omega t)\,\hat{x}$ of amplitude $2\pi\times50\times8.854\times10^{-12}\times2\times100 = 5.56\times10^{-7}$ A/m². Only a *static* field gives $\mathbf{J}_p = 0$.
>
> (iii) **True.** $\chi_e = \dfrac{N_d}{\omega_0^2}\cdot\dfrac{e^2}{m_e\epsilon_0} = \dfrac{5\times10^{28}\times3.18\times10^3}{(2\times10^{16})^2} = 0.40$, so $\epsilon_r = 1+\chi_e = 1.40$.
>
> (iv) **False.** The collision time $\tau = \sigma m_e/(Ne^2) = 2.4\times10^{-14}$ s says how fast the carriers respond; the relaxation time $\epsilon_0/\sigma = 1.5\times10^{-19}$ s says how fast excess charge would leave the interior. They differ by a factor $1.6\times10^5$; problem 11.8 shows what that mismatch means.
>
> (v) **True.** $\omega/\nu = 2\pi\times10^{10}/(4\times10^{13}) = 1.6\times10^{-3}$, and $\left\lvert\dfrac{\sigma(\omega)}{\sigma_{\text{DC}}}-1\right\rvert = \dfrac{\omega/\nu}{\sqrt{1+(\omega/\nu)^2}} = 0.16\%$. The electrons reach their drift velocity long before a 10 GHz field reverses.
>
> **Answer.** (i) false, (ii) false, (iii) true, (iv) false, (v) true.

## Medium

### 11.5 Sea water's two ions

> [!medium] Medium · find the error · several species · mobility
> Model sea water as equal densities $N = 3.0\times10^{26}$ m⁻³ (about 0.5 mol/L) of Na⁺ and Cl⁻ ions. The mobility (drift speed per unit field, not a permeability) is $\mu_+ = 4.0\times10^{-8}$ m²/(V·s) for Na⁺ and $\mu_- = 6.0\times10^{-8}$ m²/(V·s) for Cl⁻; the ion masses are $m_+ = 3.8\times10^{-26}$ kg and $m_- = 5.9\times10^{-26}$ kg. A student computes the conductivity:
>
> *"Na⁺ drifts along $\mathbf{E}$ and Cl⁻ drifts against $\mathbf{E}$, so their currents oppose: $\sigma = Ne(\mu_+-\mu_-) = 3.0\times10^{26}\times1.602\times10^{-19}\times(-2.0\times10^{-8}) = -0.96$ S/m."*
>
> (a) What is wrong? Find the correct $\sigma$ and the fraction of the current carried by each ion.
> (b) Find the collision time $\tau$ and the collision frequency $\nu$ of each ion species.
> (c) Is the DC conductivity still valid at 10 GHz?
>
> *Source: original.*

> [!hint]- Hint
> Write each species' contribution as $\mathbf{J}_s = N_sq_s\mathbf{v}_s$ and keep track of *two* signs: the direction of $\mathbf{v}_s$ and the sign of $q_s$. For (b), the mobility is $e\tau/m$.

> [!solution]- Solution
> **Setup.** Each species obeys its own force balance, $\mathbf{v}_s = (q_s\tau_s/m_s)\mathbf{E}$, and contributes $\mathbf{J}_s = N_sq_s\mathbf{v}_s$; the total current is the sum.
>
> (a) **The slip:** the student let the opposite *velocities* cancel but forgot that the Cl⁻ *charge* is negative too. For Cl⁻, $\mathbf{v}_- = -\mu_-\mathbf{E}$ and $q = -e$, so
> $$
> \mathbf{J}_- = N(-e)(-\mu_-\mathbf{E}) = +Ne\mu_-\mathbf{E},
> $$
> along $\mathbf{E}$, just like $\mathbf{J}_+ = Ne\mu_+\mathbf{E}$. The two currents add — in $\sigma = \sum_sN_sq_s^2/(m_s\nu_s)$ the charge enters squared:
> $$
> \sigma = Ne(\mu_++\mu_-) = 3.0\times10^{26}\times1.602\times10^{-19}\times1.0\times10^{-7} = 4.8\ \text{S/m}.
> $$
> Na⁺ contributes $Ne\mu_+ = 1.92$ S/m (40% of the current) and Cl⁻ contributes $Ne\mu_- = 2.88$ S/m (60%).
>
> (b) Since mobility $= e\tau/m$, $\tau = (\text{mobility})\times m/e$:
> $$
> \tau_+ = \frac{4.0\times10^{-8}\times3.8\times10^{-26}}{1.602\times10^{-19}} = 9.5\times10^{-15}\ \text{s},\qquad \tau_- = \frac{6.0\times10^{-8}\times5.9\times10^{-26}}{1.602\times10^{-19}} = 2.2\times10^{-14}\ \text{s},
> $$
> so $\nu_+ = 1/\tau_+ = 1.05\times10^{14}$ s⁻¹ and $\nu_- = 1/\tau_- = 4.5\times10^{13}$ s⁻¹.
>
> (c) At 10 GHz, $\omega/\nu = 2\pi\times10^{10}\times\tau$ is $5.96\times10^{-4}$ for Na⁺ and $1.39\times10^{-3}$ for Cl⁻. Both are far below 1, so each species' $\sigma_s/(1+j\omega/\nu_s)$ is still essentially its DC value: yes, $\sigma = 4.8$ S/m holds at 10 GHz.
>
> **Check:** the power delivered per unit volume, $\mathbf{J}\cdot\mathbf{E} = \sigma E^2$, must be positive in a passive medium. The student's $\sigma<0$ would make sea water a generator; $\sigma = 4.8$ S/m dissipates. The species formula agrees too: $Ne^2/(m_+\nu_+) = 1.92$ S/m, the same Na⁺ share as $Ne\mu_+$ ✓.
>
> **Answer.** Both currents point along $\mathbf{E}$ (negative charge moving against $\mathbf{E}$ is current along it), so they add: $\sigma = Ne(\mu_++\mu_-) = 4.8$ S/m, carried 40% by Na⁺ and 60% by Cl⁻. $\tau_+ = 9.5\times10^{-15}$ s, $\nu_+ = 1.05\times10^{14}$ s⁻¹; $\tau_- = 2.2\times10^{-14}$ s, $\nu_- = 4.5\times10^{13}$ s⁻¹. At 10 GHz $\omega/\nu\le1.39\times10^{-3}$, so the DC value still holds.

### 11.6 A conductor as a low-pass filter

> [!medium] Medium · AC conductivity · Drude model · phasors
> An n-type silicon sample has $N = 1.0\times10^{22}$ conduction electrons per m³, effective mass $m^\ast = 0.26\,m_e$ and collision time $\tau = 1.8\times10^{-13}$ s.
> (a) Find the electron mobility and the DC conductivity $\sigma_{\text{DC}}$.
> (b) A uniform field $E_0\hat{x}$ is switched on at $t = 0$. Find the drift velocity $\mathbf{v}(t)$ and the time after which it is within 1% of its final value.
> (c) For a sinusoidal field, show that $\sigma(\omega) = \sigma_{\text{DC}}/(1+j\omega/\nu)$ with $\nu = 1/\tau$. Evaluate $\sigma$ at $\omega = \nu$ (complex value, magnitude, phase) and find how long after each peak of the field the current peaks.
> (d) Up to what frequency $f$ does $\lvert\sigma(\omega)-\sigma_{\text{DC}}\rvert\le0.01\,\sigma_{\text{DC}}$ hold? Compare with copper, $\nu = 4.1\times10^{13}$ s⁻¹.
>
> *Source: original.*

> [!hint]- Hint
> The Drude equation $m^\ast\,d\mathbf{v}/dt = q\mathbf{E} - m^\ast\mathbf{v}/\tau$ is a first-order linear system with time constant $\tau$, exactly like an RC circuit. For (c), replace $d/dt$ by $j\omega$; for (d), compute $\lvert1/(1+jx)-1\rvert$ with $x = \omega/\nu$.

> [!solution]- Solution
> **Setup.** Each conduction electron obeys $m^\ast\dfrac{d\mathbf{v}}{dt} = -e\mathbf{E} - \dfrac{m^\ast}{\tau}\mathbf{v}$: the Drude equation with the effective mass $m^\ast = 0.26\,m_e = 2.37\times10^{-31}$ kg in place of $m_e$.
>
> (a) Mobility $= \dfrac{e\tau}{m^\ast} = \dfrac{1.602\times10^{-19}\times1.8\times10^{-13}}{2.37\times10^{-31}} = 0.122$ m²/(V·s), i.e. 1220 cm²/(V·s) in semiconductor units. Then $\sigma_{\text{DC}} = Ne\times\text{mobility} = 1.0\times10^{22}\times1.602\times10^{-19}\times0.122 = 195$ S/m.
>
> (b) With $\mathbf{v}(0) = 0$ the solution is a charging curve:
> $$
> \mathbf{v}(t) = -\frac{e\tau E_0}{m^\ast}\left(1-e^{-t/\tau}\right)\hat{x} = -0.122\,E_0\left(1-e^{-t/\tau}\right)\hat{x}\ \text{m/s}\qquad(E_0\ \text{in V/m}).
> $$
> It is within 1% of its final value once $e^{-t/\tau} = 0.01$: $t = \tau\ln100 = 4.6\,\tau = 8.3\times10^{-13}$ s.
>
> (c) Write $\mathbf{E}(t) = \text{Re}\{\tilde{\mathbf{E}}e^{j\omega t}\}$, so $d/dt\to j\omega$; with $q = -e$,
> $$
> j\omega m^\ast\tilde{\mathbf{v}} = q\tilde{\mathbf{E}} - m^\ast\nu\tilde{\mathbf{v}}\ \Rightarrow\ \tilde{\mathbf{J}} = Nq\tilde{\mathbf{v}} = \frac{Nq^2}{m^\ast(\nu+j\omega)}\tilde{\mathbf{E}} = \frac{\sigma_{\text{DC}}}{1+j\omega/\nu}\tilde{\mathbf{E}}.
> $$
> This is the transfer function of an RC low-pass filter with $RC\to\tau$: the carriers' inertia keeps them from following a field that reverses before they reach their drift speed. At $\omega = \nu = 1/\tau = 5.56\times10^{12}$ rad/s ($f = 0.88$ THz):
> $$
> \sigma = \frac{\sigma_{\text{DC}}}{1+j} = \frac{\sigma_{\text{DC}}}{2}(1-j) = 97.5(1-j)\ \text{S/m},\qquad \lvert\sigma\rvert = \frac{\sigma_{\text{DC}}}{\sqrt2} = 138\ \text{S/m},\qquad \angle\sigma = -45^\circ.
> $$
> So $J(t) = 138\,E_0\cos(\omega t-45^\circ)$: the current lags the field by $45^\circ$, one eighth of a period, and peaks $T/8 = (\pi/4)\tau = 1.41\times10^{-13}$ s after each field peak.
>
> (d) With $x = \omega/\nu$,
> $$
> \frac{\lvert\sigma-\sigma_{\text{DC}}\rvert}{\sigma_{\text{DC}}} = \left\lvert\frac{1}{1+jx}-1\right\rvert = \frac{x}{\sqrt{1+x^2}} = 0.01\ \Rightarrow\ x = 0.0100005,
> $$
> so $f_{\max} = x\nu/(2\pi) = 8.8$ GHz for this silicon, and 65 GHz for copper, whose electrons collide more often and therefore settle faster. Most of the 1% is phase: at $f_{\max}$ the magnitude ratio is still $\lvert\sigma\rvert/\sigma_{\text{DC}} = 0.99995$, while the phase is $-0.57^\circ$.
>
> **Check:** $\omega\to0$ returns $\sigma_{\text{DC}}$, and at the corner $\omega = \nu$ the magnitude is down by $\sqrt2$ with a $-45^\circ$ phase — the 3-dB point of every first-order low-pass. Also $Ne^2\tau/m^\ast = 195$ S/m agrees with $Ne\times$ mobility from (a) ✓.
>
> **Answer.** Mobility 0.122 m²/(V·s), $\sigma_{\text{DC}} = 195$ S/m; $\mathbf{v} = -0.122\,E_0(1-e^{-t/\tau})\,\hat{x}$ m/s, within 1% after $4.6\tau = 8.3\times10^{-13}$ s; at $\omega = \nu = 5.56\times10^{12}$ rad/s, $\sigma = 97.5(1-j)$ S/m, $\lvert\sigma\rvert = 138$ S/m at $-45^\circ$, and the current peaks $1.41\times10^{-13}$ s after the field; within 1% of the DC value up to 8.8 GHz (copper: 65 GHz).

## Hard

### 11.7 Conductor-like or dielectric-like

> [!hard] Hard · polarization current · Lorentz model · relaxation time
> A material with frequency-independent conductivity $\sigma$ and susceptibility $\chi_e$ fills a region where the field is uniform, $\mathbf{E} = E_0\cos(\omega t)\,\hat{x}$.
> (a) Write the conduction current density $\mathbf{J}_c$ and the polarization current density $\mathbf{J}_p$. Which leads, and by how much? Find the amplitude ratio $\lvert\mathbf{J}_p\rvert/\lvert\mathbf{J}_c\rvert$ and the crossover frequency $f_x$ at which the two amplitudes are equal.
> (b) *Glass.* Model its bound electrons as Lorentz oscillators with $N_d = 4.0\times10^{28}$ m⁻³ and $\omega_0 = 1.0\times10^{16}$ rad/s; its conductivity is $\sigma = 1.0\times10^{-12}$ S/m. Find $\chi_e$, $\epsilon_r$ and $f_x$. Is glass conductor-like or dielectric-like at 60 Hz? Why may you use the static $\chi_e$ at 60 Hz?
> (c) *Sea water:* $\sigma = 4$ S/m, $\epsilon_r = 81$. Find $f_x$ and $\lvert\mathbf{J}_p\rvert/\lvert\mathbf{J}_c\rvert$ at 20 kHz and at 10 GHz.
> (d) A parallel-plate capacitor filled with either material is a leaky capacitor ([[1-electrostatics/10-capacitance-and-conductance|Lecture 10]]) with $G/C = \sigma/\epsilon$, so its capacitive and conductive currents are equal at $f_r = 1/(2\pi\tau_r)$, where $\tau_r = \epsilon/\sigma$ is the relaxation time of [[1-electrostatics/08-conductors-dielectrics-and-polarization|Lecture 8]]. Find $\tau_r$ and $f_r$ for both materials. Why is $f_r\ne f_x$? Express $f_x/f_r$ in terms of $\epsilon_r$.
>
> *Source: original.*

> [!hint]- Hint
> $\mathbf{P} = \epsilon_0\chi_e\mathbf{E}$, so $\mathbf{J}_p = \epsilon_0\chi_e\,\partial\mathbf{E}/\partial t$, and the time derivative of a cosine is a sine: a $90^\circ$ shift. In (d), the capacitor's current per unit area is $\epsilon\,\partial E/\partial t = \partial D/\partial t = \epsilon_0\,\partial E/\partial t + \partial P/\partial t$ — which part of that is not $\mathbf{J}_p$?

> [!solution]- Solution
> **Setup.** Free carriers give $\mathbf{J}_c = \sigma\mathbf{E}$; bound electrons give $\mathbf{J}_p = \partial\mathbf{P}/\partial t$ with $\mathbf{P} = \epsilon_0\chi_e\mathbf{E}$, valid while $\omega\ll\omega_0$. Call the material conductor-like when $\lvert\mathbf{J}_c\rvert>\lvert\mathbf{J}_p\rvert$ and dielectric-like when $\lvert\mathbf{J}_p\rvert>\lvert\mathbf{J}_c\rvert$.
>
> **(a)** Differentiate $\mathbf{P}$:
> $$
> \mathbf{J}_c = \sigma E_0\cos(\omega t)\,\hat{x},\qquad \mathbf{J}_p = -\omega\epsilon_0\chi_eE_0\sin(\omega t)\,\hat{x} = \omega\epsilon_0\chi_eE_0\cos(\omega t+90^\circ)\,\hat{x}.
> $$
> $\mathbf{J}_c$ is in phase with $\mathbf{E}$; $\mathbf{J}_p$ leads both by $90^\circ$ — it is largest where $\mathbf{E}$ changes fastest, at the zeros of $\mathbf{E}$. The amplitude ratio is
> $$
> \frac{\lvert\mathbf{J}_p\rvert}{\lvert\mathbf{J}_c\rvert} = \frac{\omega\epsilon_0\chi_e}{\sigma} = \frac{f}{f_x},\qquad f_x = \frac{\sigma}{2\pi\epsilon_0\chi_e}.
> $$
> Below $f_x$ the material is conductor-like, above it dielectric-like.
>
> **(b)** $\dfrac{N_de^2}{m_e\epsilon_0} = 4.0\times10^{28}\times3.18\times10^3 = 1.273\times10^{32}$ s⁻², so
> $$
> \chi_e = \frac{1.273\times10^{32}}{(1.0\times10^{16})^2} = 1.27,\qquad \epsilon_r = 2.27,\qquad f_x = \frac{1.0\times10^{-12}}{2\pi\times8.854\times10^{-12}\times1.27} = 0.0141\ \text{Hz}.
> $$
> At 60 Hz, $\lvert\mathbf{J}_p\rvert/\lvert\mathbf{J}_c\rvert = 60/0.0141 = 4.2\times10^3$: glass is thoroughly dielectric-like, and its conduction matters only for fields that are essentially static. The static $\chi_e$ is fine because $\omega_0/(2\pi) = 1.59\times10^{15}$ Hz $\gg$ 60 Hz: the bound electrons follow the field without lag (even at $\omega = 0.01\,\omega_0$ the Lorentz response differs from its static value by only 0.01%). The resonance sits at the free-space wavelength $2\pi c/\omega_0 = 188$ nm, in the ultraviolet — which is why glass is clear in visible light but opaque in the UV.
>
> **(c)** $\chi_e = \epsilon_r-1 = 80$, so
> $$
> f_x = \frac{4}{2\pi\times8.854\times10^{-12}\times80} = 0.90\ \text{GHz}.
> $$
> At 20 kHz, $\lvert\mathbf{J}_p\rvert/\lvert\mathbf{J}_c\rvert = 2.2\times10^{-5}$: conduction wins by a factor $4.5\times10^4$ and sea water is a conductor. At 10 GHz the ratio is 11: sea water is dielectric-like. The DC $\sigma$ still applies there, since the ions have $\omega/\nu\le1.39\times10^{-3}$ (problem 11.5). (Water's large $\chi_e$ comes from its polar molecules turning in the field rather than from Lorentz oscillators; in reality it starts to fall in the microwave range, which this constant-$\chi_e$ model ignores.)
>
> **(d)** Sea water: $\tau_r = \epsilon/\sigma = 81\times8.854\times10^{-12}/4 = 1.79\times10^{-10}$ s and $f_r = 1/(2\pi\tau_r) = 0.888$ GHz. Glass: $\tau_r = 2.27\times8.854\times10^{-12}/(1.0\times10^{-12}) = 20.1$ s and $f_r = 0.00791$ Hz. The two crossovers differ because the capacitor's current density is
> $$
> \epsilon\frac{\partial\mathbf{E}}{\partial t} = \frac{\partial\mathbf{D}}{\partial t} = \epsilon_0\frac{\partial\mathbf{E}}{\partial t} + \frac{\partial\mathbf{P}}{\partial t}:
> $$
> besides the bound-charge current $\mathbf{J}_p$ it contains a vacuum term with no charges behind it. Hence
> $$
> \frac{f_x}{f_r} = \frac{\sigma/(2\pi\epsilon_0\chi_e)}{\sigma/(2\pi\epsilon_0\epsilon_r)} = \frac{\epsilon_r}{\chi_e} = 1+\frac{1}{\chi_e}.
> $$
> Sea water: $81/80 = 1.0125$ — the vacuum term is only $1/\epsilon_r = 1.2\%$ of $\partial\mathbf{D}/\partial t$, so $f_r\approx f_x$. Glass: $2.27/1.27 = 1.79$ — the vacuum term is 44% of $\partial\mathbf{D}/\partial t$, and $f_r$ lies well below $f_x$.
>
> **Check:** $G/C = \sigma/\epsilon$ for any plate area and gap (both scale as $A/d$), so $f_r$ is a material property like $f_x$, and at $f = f_r$, $\omega C = G$ makes $\lvert C\,dV/dt\rvert = \lvert GV\rvert$ ✓. The ratio $f/f_x$ also behaves sensibly near the crossover: for sea water at 1 GHz it is $1/0.899 = 1.11$, just past equality ✓.
>
> **Watch out:** real glass also has ionic polarization at low frequency, so its measured $\epsilon_r$ at 60 Hz exceeds the electron-only 2.27; a larger $\chi_e$ only strengthens the conclusion of (b). (The model's $\sqrt{\epsilon_r} = 1.51$ is close to glass's optical refractive index, where only the electrons respond; you will meet $n = \sqrt{\epsilon_r}$ in Unit 3.)
>
> **Answer.** (a) $\mathbf{J}_c = \sigma E_0\cos(\omega t)\,\hat{x}$, in phase with $\mathbf{E}$; $\mathbf{J}_p = -\omega\epsilon_0\chi_eE_0\sin(\omega t)\,\hat{x}$, leading by $90^\circ$; $\lvert\mathbf{J}_p\rvert/\lvert\mathbf{J}_c\rvert = \omega\epsilon_0\chi_e/\sigma = f/f_x$ with $f_x = \sigma/(2\pi\epsilon_0\chi_e)$. (b) $\chi_e = 1.27$, $\epsilon_r = 2.27$, $f_x = 0.0141$ Hz; dielectric-like at 60 Hz (ratio $4.2\times10^3$). (c) $f_x = 0.90$ GHz; ratio $2.2\times10^{-5}$ at 20 kHz (conductor-like) and 11 at 10 GHz (dielectric-like). (d) Sea water $\tau_r = 1.79\times10^{-10}$ s, $f_r = 0.888$ GHz; glass $\tau_r = 20.1$ s, $f_r = 0.00791$ Hz; $f_x/f_r = \epsilon_r/\chi_e$ (1.0125 and 1.79), because $\partial\mathbf{D}/\partial t$ includes the vacuum term $\epsilon_0\,\partial\mathbf{E}/\partial t$.

### 11.8 Relaxation time versus collision time

> [!hard] Hard · relaxation time · Drude model · plasma oscillation
> [[1-electrostatics/08-conductors-dielectrics-and-polarization|Lecture 8]] showed that excess charge inside a conductor decays as $e^{-t/\tau_r}$ with $\tau_r = \epsilon/\sigma$. This problem tests that result against the Drude model.
> (a) A uniform conducting medium ($\sigma$, $\epsilon$) holds at $t = 0$ the charge density $\rho(x,0) = \rho_0\sin\beta x$, independent of $y$ and $z$, and no field is applied from outside. Assuming $\mathbf{J} = \sigma\mathbf{E}$ at every instant, use the continuity equation and Gauss's law to find $\rho(x,t)$ and $E_x(x,t)$. On which planes is $E_x = 0$?
> (b) The medium is lightly doped n-type silicon: $\epsilon = 11.7\epsilon_0$, with $N = 1.0\times10^{20}$ conduction electrons per m³, effective mass $m^\ast = 0.26\,m_e$ and collision time $\tau = 1.8\times10^{-13}$ s. Take $\rho_0 = 46.8\epsilon_0$ C/m³ and $\beta = 2$ rad/m. Find $\sigma$, $\tau_r$ and the amplitude of $E_x$ at $t = 0$. At $x = 0$, where $\rho = 0$, find $\mathbf{E}$, $\mathbf{J}$ and the electrons' drift velocity $\mathbf{v}$ at $t = 0$. Where is the charge going?
> (c) For copper ($\sigma = 5.8\times10^7$ S/m, $N = 8.5\times10^{28}$ m⁻³, $\epsilon = \epsilon_0$, free-electron mass $m_e$), compare $\tau_r$ with the Drude collision time $\tau$, and make the same comparison for the silicon of (b). Why does this make the result of (a) suspect for copper but not for the silicon?
> (d) Replace $\mathbf{J} = \sigma\mathbf{E}$ by the Drude law $\tau\,\partial\mathbf{J}/\partial t + \mathbf{J} = \sigma\mathbf{E}$. Show that $\tau\,\partial^2\rho/\partial t^2 + \partial\rho/\partial t + (\sigma/\epsilon)\rho = 0$. Solve it for copper and for sea water ($\sigma = 4$ S/m, $\epsilon = 81\epsilon_0$, ion collision time $\tau = 1.5\times10^{-14}$ s): how does the charge disappear in each, and on what time scale? When is $\tau_r = \epsilon/\sigma$ the right answer?
>
> *Source: Summer 2017 HE2 #2a style (charge relaxation), re-parameterized and extended with the Drude law.*

> [!hint]- Hint
> In one dimension Gauss's law is $\partial E_x/\partial x = \rho/\epsilon$ and continuity is $\partial\rho/\partial t + \partial J_x/\partial x = 0$. Integrating Gauss's law leaves a constant: fix it on a plane about which $\rho$ is symmetric, where $E_x$ must vanish. For (d), multiply the Drude equation $m\,d\mathbf{v}/dt = q\mathbf{E} - m\mathbf{v}/\tau$ by $Nq/m$ to get the law for $\mathbf{J}$, take $\partial/\partial x$ of it, use the same two equations, and try $\rho\propto e^{st}$.

> [!solution]- Solution
> **Setup.** Everything depends on $x$ and $t$ only, so $\mathbf{E} = E_x\hat{x}$ and $\mathbf{J} = J_x\hat{x}$. Two field laws hold whatever the material: Gauss, $\partial E_x/\partial x = \rho/\epsilon$, and continuity, $\partial\rho/\partial t = -\partial J_x/\partial x$. Only the material law linking $\mathbf{J}$ to $\mathbf{E}$ changes between (a) and (d).
>
> **(a)** With $J_x = \sigma E_x$:
> $$
> \frac{\partial\rho}{\partial t} = -\sigma\frac{\partial E_x}{\partial x} = -\frac{\sigma}{\epsilon}\rho\quad\Rightarrow\quad\rho(x,t) = \rho_0\sin(\beta x)\,e^{-t/\tau_r},\qquad\tau_r = \frac{\epsilon}{\sigma}.
> $$
> Integrating Gauss's law in $x$:
> $$
> E_x(x,t) = -\frac{\rho_0}{\beta\epsilon}\cos(\beta x)\,e^{-t/\tau_r} + C(t).
> $$
> The ripple is symmetric about each crest, $x = \pi/(2\beta)$, and each trough, $x = -\pi/(2\beta)$. With no applied field, $E_x$ must therefore be odd about those planes and vanish on them. There $\cos(\beta x) = 0$, so $C = 0$. Hence $E_x = 0$ on the planes $x = (2n+1)\pi/(2\beta)$, the crests and troughs of $\rho$, and $\lvert E_x\rvert$ is largest on the planes $x = n\pi/\beta$ where $\rho = 0$ ($n$ any integer).
>
> **Watch out:** the field vanishes where $\lvert\rho\rvert$ is largest, not where $\rho = 0$. Gauss's law ties the local $\rho$ to the *slope* of $E_x$; the value of $E_x$ is set by the charge on either side.
>
> **(b)** The mobility is $e\tau/m^\ast = 0.122$ m²/(V·s), as in problem 11.6, so
> $$
> \sigma = \frac{Ne^2\tau}{m^\ast} = 1.95\ \text{S/m},\qquad \tau_r = \frac{\epsilon}{\sigma} = \frac{11.7\times8.854\times10^{-12}}{1.95} = 5.31\times10^{-11}\ \text{s}\ (53\ \text{ps}).
> $$
> The amplitude is $\rho_0/(\beta\epsilon) = 46.8\epsilon_0/(2\times11.7\epsilon_0) = 2$ V/m, so $E_x(x,0) = -2\cos(2x)$ V/m. At $x = 0$:
> $$
> \mathbf{E} = -2\,\hat{x}\ \text{V/m},\qquad \mathbf{J} = \sigma\mathbf{E} = -3.90\,\hat{x}\ \text{A/m}^2,\qquad \mathbf{v} = \frac{\mathbf{J}}{N(-e)} = +0.244\,\hat{x}\ \text{m/s}.
> $$
> The current at $x = 0$ flows along $-\hat{x}$, from the crest at $x = \pi/4 = 0.785$ m toward the trough at $x = -\pi/4$ m. Charge leaves the crests and fills the troughs, flattening the ripple — that is why $\rho$ decays. The electrons that carry this current drift the other way, along $+\hat{x}$: out of the trough, where they are in excess, into the crest, where they are missing. The ripple is a tiny disturbance ($\rho_0/e = 2.6\times10^9$ m⁻³ against $N = 1.0\times10^{20}$ m⁻³), so $N$ and $\sigma$ are unchanged.
>
> **(c)** For copper, $\tau_r = \epsilon_0/\sigma = 8.854\times10^{-12}/(5.8\times10^7) = 1.5\times10^{-19}$ s, while $\tau = \sigma m_e/(Ne^2) = 2.4\times10^{-14}$ s is $1.6\times10^5$ times longer. The silicon is the other way round: $\tau_r = 5.31\times10^{-11}$ s is 295 times $\tau = 1.8\times10^{-13}$ s. But $\mathbf{J} = \sigma\mathbf{E}$ is the *steady state* of the Drude equation, reached only after a few $\tau$. In the silicon the ripple takes hundreds of collision times to relax, so the electrons drift at their steady velocity throughout and (a) holds. In copper, (a) applies $\mathbf{J} = \sigma\mathbf{E}$ on a time scale $\tau_r$ on which the electrons have not even begun to reach their drift velocity, so its answer cannot be trusted.
>
> **(d)** Multiplying the Drude equation by $Nq/m$ gives $\partial\mathbf{J}/\partial t = (Nq^2/m)\mathbf{E} - \mathbf{J}/\tau$, i.e. $\tau\,\partial\mathbf{J}/\partial t + \mathbf{J} = \sigma\mathbf{E}$. Take $\partial/\partial x$ and substitute $\partial J_x/\partial x = -\partial\rho/\partial t$ and $\sigma\,\partial E_x/\partial x = \sigma\rho/\epsilon$:
> $$
> \tau\frac{\partial^2\rho}{\partial t^2} + \frac{\partial\rho}{\partial t} + \frac{\sigma}{\epsilon}\rho = 0.
> $$
> Trying $\rho\propto e^{st}$ gives
> $$
> s^2 + \frac{s}{\tau} + \frac{\sigma}{\epsilon\tau} = 0,\qquad s = -\frac{1}{2\tau}\pm\sqrt{\frac{1}{4\tau^2}-\frac{\sigma}{\epsilon\tau}}.
> $$
> The carriers' inertia has turned the first-order decay into a damped second-order system. The roots are complex (underdamped) when $4\sigma\tau/\epsilon>1$, i.e. when $\tau_r<4\tau$.
>
> *Copper.* Here $\sigma/(\epsilon_0\tau) = Ne^2/(m_e\epsilon_0) = 2.705\times10^{32}$ s⁻² — the collision time cancels. Call it $\omega_p^2$, so $\omega_p = 1.64\times10^{16}$ rad/s. Since $4\sigma\tau/\epsilon_0 = 6.3\times10^5\gg1$,
> $$
> s = -\frac{1}{2\tau}\pm j\sqrt{\omega_p^2-\frac{1}{4\tau^2}} = -2.06\times10^{13}\pm j\,1.64\times10^{16}\ \text{s}^{-1}.
> $$
> The charge does not quietly relax in $1.5\times10^{-19}$ s: it *oscillates* at the plasma frequency $f_p = \omega_p/(2\pi) = 2.6\times10^{15}$ Hz (ultraviolet), and the oscillation dies out as $e^{-t/(2\tau)}$, with time constant $2\tau = 4.8\times10^{-14}$ s — about 127 oscillations per time constant ($\omega_p\tau = 398$). The time for the charge to disappear is set by the collisions, not by $\epsilon_0/\sigma$.
>
> *Sea water.* Now $\sigma/\epsilon = 4/(81\epsilon_0) = 5.58\times10^9$ s⁻¹ and $1/\tau = 6.67\times10^{13}$ s⁻¹, so $4\sigma\tau/\epsilon = 3.3\times10^{-4}\ll1$: overdamped, with two real roots
> $$
> s_1 = -6.67\times10^{13}\ \text{s}^{-1}\approx-\frac{1}{\tau},\qquad s_2 = -5.58\times10^{9}\ \text{s}^{-1}\approx-\frac{\sigma}{\epsilon}.
> $$
> The fast root is the ions' own velocity transient, over within a few $\tau$; after it the charge decays as $e^{s_2t}$ with time constant $1/\lvert s_2\rvert = 1.79\times10^{-10}$ s, equal to $\epsilon/\sigma = 0.18$ ns to within $8.4\times10^{-5}$ (relative). Lecture 8's answer is right here.
>
> *When is $\epsilon/\sigma$ right?* When the charge relaxes slowly compared with the collisions, $\tau_r\gg\tau$ (even a non-oscillating decay needs $\tau_r>4\tau$). Sea water passes ($\tau_r = 1.79\times10^{-10}$ s against $4\tau = 6\times10^{-14}$ s). So does the silicon of (b): $\tau_r = 5.31\times10^{-11}$ s against $4\tau = 7.2\times10^{-13}$ s, and its slow root gives a time constant of $5.29\times10^{-11}$ s, only 0.34% below $\tau_r$. Copper fails by a wide margin ($\tau_r = 1.53\times10^{-19}$ s against $4\tau = 9.69\times10^{-14}$ s). Good conductors are exactly the materials whose $\epsilon/\sigma$ is too short to be physical.
>
> **Check:** in (a), $\partial\rho/\partial t = -\rho/\tau_r$ and $\partial J_x/\partial x = \sigma\rho/\epsilon = \rho/\tau_r$ cancel, as continuity requires, and $\rho_0/(\beta\epsilon)$ has units $\dfrac{\text{C/m}^3}{(1/\text{m})(\text{F/m})} = \text{V/m}$ ✓. Letting $\tau\to0$ in the $\rho$ equation gives $\partial\rho/\partial t + (\sigma/\epsilon)\rho = 0$, the result of (a) — so (a) is the no-inertia limit of (d). The wavenumber $\beta$ appears nowhere in the equation for $s$, so a ripple of any wavelength decays (or oscillates) the same way, as in (a). Units: $\sigma/(\epsilon\tau)$ is (1/s)(1/s) = s⁻², as $\omega_p^2$ must be ✓.
>
> **Answer.** (a) $\rho = \rho_0\sin(\beta x)\,e^{-t/\tau_r}$, $E_x = -\dfrac{\rho_0}{\beta\epsilon}\cos(\beta x)\,e^{-t/\tau_r}$, $\tau_r = \epsilon/\sigma$; $E_x = 0$ on the crest and trough planes $x = (2n+1)\pi/(2\beta)$. (b) $\sigma = 1.95$ S/m, $\tau_r = 5.31\times10^{-11}$ s, amplitude 2 V/m; at $x = 0$, $\mathbf{E} = -2\,\hat{x}$ V/m, $\mathbf{J} = -3.90\,\hat{x}$ A/m² and $\mathbf{v} = +0.244\,\hat{x}$ m/s: charge flows from the crest at $x = \pi/4$ m toward the trough at $x = -\pi/4$ m, carried by electrons drifting the other way. (c) Copper: $\tau_r = 1.5\times10^{-19}$ s against $\tau = 2.4\times10^{-14}$ s ($1.6\times10^5$ times longer), so $\mathbf{J} = \sigma\mathbf{E}$ cannot hold on the time scale $\tau_r$; silicon: $\tau_r = 295\,\tau$, so it can. (d) Copper: underdamped plasma oscillation at $\omega_p = 1.64\times10^{16}$ rad/s ($f_p = 2.6\times10^{15}$ Hz), decaying with time constant $2\tau = 4.8\times10^{-14}$ s. Sea water: overdamped; after a transient of a few $\tau$, $\rho$ decays with time constant $1.79\times10^{-10}$ s $\approx\epsilon/\sigma$. The relaxation time $\epsilon/\sigma$ is right only when $\tau_r\gg\tau$.

### Sources for this page
Formulas and sign conventions follow the course notes for Lecture 11 (Drude force balance, mobility, $\mathbf{J} = Nq\mathbf{v}$, the species sum, the phasor $\sigma(\omega)$, the Lorentz oscillator, the static $\chi_e$ and the polarization current), with the relaxation time of Lecture 8 and the leaky capacitor of Lecture 10 brought in for 11.7 and 11.8. Classic textbook exercises with new numbers: the drift speed in a household wire (11.1) and the Drude estimate of a metal's conductivity (11.2). Problem 11.8 is modelled on the charge-relaxation problem Summer 2017 HE2 #2a ($\rho = \cos 3z$ in a conductor, find $\rho(t)$ and $E_z$). It is re-parameterized as a sine ripple in lightly doped silicon, and the Drude law extends it to the classic textbook point that $\epsilon/\sigma$ fails in a good conductor, where the charge instead undergoes plasma oscillations. Problems 11.3–11.7 are original. Lecture 11 is not on Exam 1, and no old exam tests the Drude or Lorentz model directly.

*Previous: [[practice/10-capacitance-and-conductance|Lecture 10 practice]] · next: [[practice/12-magnetic-force-biot-savart-and-ampere|Lecture 12 practice]] · [[practice/index|all practice]]*
