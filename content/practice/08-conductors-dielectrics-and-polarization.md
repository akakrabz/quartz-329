---
title: "Practice — Lecture 8: Conductors, dielectrics, and polarization"
description: "12 practice problems (5 easy, 3 medium, 4 hard) on Ohm's law and resistance in wires and coaxial resistors, relaxation time, conductors in applied fields and charges in cavities, P, D and susceptibility, and bound volume and surface charge in graded slabs, spheres, rods and an electret inside a grounded tube, each with a folded hint and a worked solution."
tags: [practice, electrostatics, exam-1]
lecture: 8
---

*Practice for [[1-electrostatics/08-conductors-dielectrics-and-polarization|Lecture 8]] · concepts: [[concepts/conductors]] · [[concepts/polarization]] · [[concepts/permittivity]] · [[concepts/continuity-equation]] · all practice: [[practice/index|hub]] · by difficulty: [[practice/easy|easy]] · [[practice/medium|medium]] · [[practice/hard|hard]] · [[practice/topics|by topic]]*

Work each problem on paper first. Open the **hint** only when stuck, and the **solution** only after you have an answer you would hand in. Every answer here has been checked numerically.

## Easy

### 8.1 Resistance of a copper wire

> [!easy] Easy · Ohm's law · resistance
> A copper wire ($\sigma = 5.8\times10^{7}$ S/m) of length $\ell = 58$ m and uniform cross-section $A = 1$ mm² $= 10^{-6}$ m² carries a steady current $I = 2$ A. (a) Find its resistance $R$. (b) Find the current density $J$ and the field $E$ inside the wire, and the voltage across its ends. Which way do $\mathbf{E}$, $\mathbf{J}$ and the conduction electrons go? (c) The wire is drawn out to twice its length with its volume unchanged. Find the new resistance.
>
> *Source: classic.*

> [!hint]- Hint
> $V = E\ell$ and $I = JA = \sigma EA$, so $R = V/I$ needs only $\ell$, $\sigma$ and $A$. In (c), what happens to $A$ when $\ell$ doubles at fixed volume?

> [!solution]- Solution
> **(a)** In a uniform wire carrying a steady current the field is uniform and along the wire, so the voltage is $V = E\ell$ and the current is $I = JA = \sigma EA$. Dividing,
> $$
> R = \frac{V}{I} = \frac{\ell}{\sigma A} = \frac{58}{(5.8\times10^{7})(10^{-6})} = 1\ \Omega .
> $$
> **(b)** $J = I/A = 2\times10^{6}$ A/m², and Ohm's law $\mathbf{J} = \sigma\mathbf{E}$ gives $E = J/\sigma\approx0.0345$ V/m $= 34.5$ mV/m. The voltage is $E\ell = 2$ V, which equals $IR$ ✓. $\mathbf{E}$ and $\mathbf{J}$ both point along the current. A conductor *can* hold a field here because it is not in equilibrium: a source keeps driving the current. The electrons have $q<0$ and drift the opposite way.
>
> **(c)** A fixed volume $\ell A$ with $\ell' = 2\ell$ forces $A' = A/2 = 5\times10^{-7}$ m², so $R' = \dfrac{2\ell}{\sigma A/2} = 4R = 4\ \Omega$.
>
> **Watch out:** stretching changes two things. $R\propto\ell/A$, and each factor doubles, so $R$ goes up four times, not two.
>
> **Answer.** (a) $R = 1\ \Omega$. (b) $J = 2\times10^6$ A/m², $E\approx34.5$ mV/m, $V = 2$ V; $\mathbf{E}$ and $\mathbf{J}$ along the current, electrons against it. (c) $R' = 4\ \Omega$.

### 8.2 Four relaxation times

> [!easy] Easy · relaxation time · conductors
> Excess charge is placed inside each of four materials at $t = 0$. (a) Find the relaxation time $\tau = \epsilon/\sigma$ of copper ($\epsilon = \epsilon_0$, $\sigma = 5.8\times10^{7}$ S/m), sea water ($\epsilon = 81\epsilon_0$, $\sigma = 4$ S/m), distilled water ($\epsilon = 81\epsilon_0$, $\sigma = 10^{-4}$ S/m) and glass ($\epsilon = 6\epsilon_0$, $\sigma = 10^{-12}$ S/m). (b) How long does the interior charge density of sea water take to fall to 1% of its initial value? (c) Which of the four behave like conductors for fields that change on a time scale of 1 ms?
>
> *Source: Lecture 8 conductivity table and relaxation-time derivation, new questions.*

> [!hint]- Hint
> Inside a uniform conductor $\rho(t) = \rho(0)\,e^{-t/\tau}$. For (c), compare each $\tau$ with 1 ms.

> [!solution]- Solution
> **(a)** Charge conservation, $\mathbf{J} = \sigma\mathbf{E}$ and $\nabla\cdot\mathbf{E} = \rho/\epsilon$ combine into $\partial\rho/\partial t = -(\sigma/\epsilon)\rho$, so interior charge decays as $e^{-t/\tau}$ with $\tau = \epsilon/\sigma$. It does not vanish; it migrates to the surface.
>
> | material | $\epsilon$ | $\sigma$ [S/m] | $\tau = \epsilon/\sigma$ |
> |---|---|---|---|
> | copper | $\epsilon_0$ | $5.8\times10^{7}$ | $1.53\times10^{-19}$ s |
> | sea water | $81\epsilon_0$ | 4 | $1.79\times10^{-10}$ s $= 0.179$ ns |
> | distilled water | $81\epsilon_0$ | $10^{-4}$ | $7.17\times10^{-6}$ s $= 7.17\ \mu$s |
> | glass | $6\epsilon_0$ | $10^{-12}$ | 53.1 s |
>
> **(b)** $e^{-t/\tau} = 0.01$ gives $t = \tau\ln100\approx4.61\,\tau\approx0.826$ ns.
>
> **(c)** A material behaves as a conductor when its charge relaxes long before the field changes, $\tau\ll1$ ms. Copper, sea water and distilled water qualify; even distilled water relaxes about 139 times faster than 1 ms. Glass, with $\tau\approx53.1$ s, holds charge in place far longer than 1 ms and acts as an insulator.
>
> **Watch out:** use the material's own permittivity. For water $\epsilon = 81\epsilon_0$; dropping the 81 makes $\tau$ 81 times too short.
>
> **Answer.** (a) $1.53\times10^{-19}$ s, $0.179$ ns, $7.17\ \mu$s, $53.1$ s. (b) $\approx0.826$ ns. (c) Copper, sea water and distilled water behave as conductors; glass does not.

### 8.3 Field from a known polarization

> [!easy] Easy · multiple choice · susceptibility
> At a point inside a linear, isotropic dielectric with $\epsilon = 3\epsilon_0$, the polarization is $\mathbf{P}$. The total electric field at that point is
>
> (a) $\mathbf{P}/(3\epsilon_0)$
>
> (b) $\mathbf{P}/(2\epsilon_0)$
>
> (c) $2\mathbf{P}/\epsilon_0$
>
> (d) $\mathbf{P}/\epsilon_0$
>
> (e) $3\mathbf{P}/(2\epsilon_0)$
>
> *Source: original.*

> [!hint]- Hint
> Get $\chi_e$ from $\epsilon_r = 1+\chi_e$, then invert $\mathbf{P} = \epsilon_0\chi_e\mathbf{E}$.

> [!solution]- Solution
> **(b).** $\epsilon_r = 3$, so $\chi_e = \epsilon_r-1 = 2$. In $\mathbf{P} = \epsilon_0\chi_e\mathbf{E}$ the field is the **total** field, so $\mathbf{E} = \mathbf{P}/(\epsilon_0\chi_e) = \mathbf{P}/(2\epsilon_0)$.
>
> Check with $\mathbf{D}$: $\epsilon\mathbf{E} = \tfrac32\mathbf{P}$, and $\epsilon_0\mathbf{E}+\mathbf{P} = \tfrac12\mathbf{P}+\mathbf{P} = \tfrac32\mathbf{P}$ ✓.
>
> Why the others are wrong:
>
> - (a) comes from $\mathbf{P} = \epsilon\mathbf{E}$, which is the formula for $\mathbf{D}$, not $\mathbf{P}$.
> - (c) comes from $\mathbf{P} = \epsilon_0\mathbf{E}/\chi_e$: the susceptibility is inverted.
> - (d) comes from $\mathbf{P} = \epsilon_0\mathbf{E}$, which drops $\chi_e$ altogether.
> - (e) is $\mathbf{D}/\epsilon_0$, the field the same $\mathbf{D}$ would give in vacuum. In a slab or a symmetric geometry that is the field of the free charges alone, before the bound charge weakens it.
>
> **Answer.** (b) $\mathbf{E} = \mathbf{P}/(2\epsilon_0)$.

### 8.4 Conducting slab in a field

> [!easy] Easy · true or false · conductors
> A neutral conducting slab fills $0<z<2$ cm in free space. Distant fixed charges apply the uniform field $\mathbf{E}_0 = 10\,\hat{z}$ kV/m. Once the slab is in electrostatic equilibrium, mark each statement true or false.
>
> (a) $\mathbf{E} = 0$ everywhere inside the slab.
>
> (b) The face $z = 0$ carries the surface charge density $+88.5$ nC/m².
>
> (c) The two faces carry equal and opposite surface charge densities.
>
> (d) Below the slab ($z<0$) the field is zero, because the slab shields it.
>
> (e) $V(2\text{ cm})-V(0) = -200$ V.
>
> *Source: course notes Lecture 8 (conducting slab in a uniform field), true/false version.*

> [!hint]- Hint
> Electrons drift against $\mathbf{E}_0$. On a conductor $\rho_s = \hat{n}\cdot\mathbf{D}$, with $\hat{n}$ pointing out of the metal.

> [!solution]- Solution
> - **(a) True.** Free electrons keep moving as long as any field acts on them, so in equilibrium the interior field is exactly zero.
> - **(b) False: wrong sign.** The electrons are pushed toward $-z$, so the bottom face is the *negative* one. Formally, at $z = 0$ the normal out of the metal is $\hat{n} = -\hat{z}$, and just below the face $\mathbf{D} = \epsilon_0E_0\hat{z}$, so $\rho_s = \hat{n}\cdot\mathbf{D} = -\epsilon_0E_0 = -88.5$ nC/m².
> - **(c) True.** At $z = 2$ cm, $\hat{n} = +\hat{z}$ and $\rho_s = +\epsilon_0E_0 = +88.5$ nC/m². The faces are equal and opposite, as they must be on a neutral slab.
> - **(d) False.** The induced faces form a pair of opposite sheets. Like a parallel-plate pair, they make $-\mathbf{E}_0$ between them and nothing outside. So the field cancels inside and stays $\mathbf{E}_0 = 10\,\hat{z}$ kV/m on both sides of the slab. The field lines end on the bottom face and start again on the top face.
> - **(e) False.** The slab is an equipotential: $V(2\text{ cm})-V(0) = -\int_0^{0.02}E_z\,dz = 0$, because $E_z = 0$ along the whole path. The value $-200$ V $= -E_0\times(0.02\text{ m})$ is the answer *without* the slab.
>
> **Check:** superpose the applied field and the two induced sheets, each $\dfrac{\rho_s}{2\epsilon_0}\operatorname{sgn}(z-z_0)$. Inside, the bottom sheet is below you and the top sheet above: $E_z = E_0+\dfrac{\rho_s(0)}{2\epsilon_0}-\dfrac{\rho_s(2\text{ cm})}{2\epsilon_0} = E_0-\tfrac12E_0-\tfrac12E_0 = 0$ ✓.
>
> **Answer.** (a) True. (b) False: it is $-88.5$ nC/m². (c) True. (d) False: the field is still 10 kV/m. (e) False: it is 0 V.

### 8.5 Graded slab, find the error

> [!easy] Easy · find the error · bound charge
> A slab occupying $0<z<d$ with $d = 1$ mm, in free space, carries the permanent polarization $\mathbf{P} = P_0(1+z/d)\,\hat{z}$ with $P_0 = 5\ \mu$C/m², and no free charge. A student computes its bound charge:
>
> *"$\rho_b = -\nabla\cdot\mathbf{P} = -dP_z/dz = -P_0/d = -5\times10^{-3}$ C/m³. On the faces $\rho_{sb} = \mathbf{P}\cdot\hat{z}$, so $\rho_{sb}(0) = P_0 = +5\ \mu$C/m² and $\rho_{sb}(d) = 2P_0 = +10\ \mu$C/m². Total per unit area: $\rho_bd+\rho_{sb}(0)+\rho_{sb}(d) = -P_0+P_0+2P_0 = 2P_0 = 10\ \mu$C/m², so the slab carries net bound charge."*
>
> What is wrong? Give the correct bound charges and the correct total.
>
> *Source: original.*

> [!hint]- Hint
> In $\rho_{sb} = \mathbf{P}\cdot\hat{n}$, which way does $\hat{n}$ point on the bottom face? And can polarizing neutral matter create net charge?

> [!solution]- Solution
> **The slip:** in $\rho_{sb} = \mathbf{P}\cdot\hat{n}$, $\hat{n}$ is the **outward** normal of the polarized body. On the bottom face that is $\hat{n} = -\hat{z}$, not $+\hat{z}$:
> $$
> \rho_{sb}(0) = \mathbf{P}(0)\cdot(-\hat{z}) = -P_0 = -5\ \mu\text{C/m}^2 .
> $$
> The rest is right. $\rho_b = -P_0/d = -5\times10^{-3}$ C/m³ is uniform because $P_z$ grows linearly, and over the thickness it adds up to $\rho_bd = -P_0 = -5\ \mu$C/m². The top face, where $\hat{n} = +\hat{z}$, carries $\rho_{sb}(d) = +2P_0 = +10\ \mu$C/m². The total is $-P_0-P_0+2P_0 = 0$.
>
> It *must* vanish. Bound charge is charge displaced inside neutral atoms, so a polarized body that started neutral stays neutral. A nonzero total is a red flag for a wrong normal.
>
> **Check:** with no free charge, planar symmetry makes $D_z$ constant, and it vanishes far from the neutral slab, so $\mathbf{D} = 0$ everywhere. Then $\epsilon_0\mathbf{E} = -\mathbf{P}$ inside the slab and $\mathbf{E} = 0$ outside. Going up through $z = 0$, $\epsilon_0E_z$ jumps from 0 to $-P_0$, which is $\rho_{sb}(0)$ ✓. Through $z = d$ it jumps from $-2P_0$ to 0, by $+2P_0 = \rho_{sb}(d)$ ✓.
>
> **Answer.** The student used $\hat{n} = +\hat{z}$ on the bottom face. Correct: $\rho_b = -5\times10^{-3}$ C/m³, $\rho_{sb}(0) = -5\ \mu$C/m², $\rho_{sb}(d) = +10\ \mu$C/m², and the total bound charge is zero.

## Medium

### 8.6 A coaxial radial resistor

> [!medium] Medium · radial current · resistance
> The region $a<r<b$ between two perfectly conducting coaxial cylinders ($a = 1$ cm, $b = 2$ cm, length $L = 10$ cm) is filled with a material of conductivity $\sigma = 2$ S/m. A steady current $I = 3$ A flows radially from the inner to the outer cylinder; ignore the end faces.
> (a) Find $\mathbf{J}(r)$ and $\mathbf{E}(r)$, and evaluate both at $r = a$ and $r = b$.
> (b) Find $V(a)-V(b)$ and the resistance $R$.
> (c) The same block is used instead with electrodes on its end faces $z = 0$ and $z = L$, so the current flows along $z$. Find this resistance and compare.
>
> *Source: classic.*

> [!hint]- Hint
> In steady state, every cylinder of radius $r$ between the electrodes carries the whole current $I$ through its area $2\pi rL$. Then $\mathbf{E} = \mathbf{J}/\sigma$; integrate $E_r$ from $a$ to $b$.

> [!solution]- Solution
> **Setup.** In steady state $\nabla\cdot\mathbf{J} = 0$: charge cannot pile up anywhere, so the same $I$ crosses every coaxial cylinder of radius $r$ and area $2\pi rL$. By symmetry $\mathbf{J} = J_r(r)\hat{r}$. The formula $R = \ell/(\sigma A)$ cannot be used directly, because the area the current crosses grows with $r$.
>
> **(a)**
> $$
> \mathbf{J} = \frac{I}{2\pi rL}\hat{r},\qquad \mathbf{E} = \frac{\mathbf{J}}{\sigma} = \frac{I}{2\pi\sigma rL}\hat{r}.
> $$
> $J(a) = \dfrac{3}{2\pi(0.01)(0.1)} = \dfrac{1500}{\pi}\approx477$ A/m² and $J(b)\approx239$ A/m²; $E(a)\approx239$ V/m and $E(b)\approx119$ V/m. Both fields point radially outward, from the inner electrode to the outer one, and are twice as strong at $r = a$ as at $r = b$.
>
> **(b)**
> $$
> \begin{aligned}
> V(a)-V(b) &= -\int_b^aE_r\,dr = \int_a^b\frac{I\,dr}{2\pi\sigma Lr} = \frac{I}{2\pi\sigma L}\ln\frac{b}{a}\approx1.65\ \text{V},\\
> R &= \frac{V(a)-V(b)}{I} = \frac{\ln(b/a)}{2\pi\sigma L} = \frac{\ln2}{2\pi(2)(0.1)}\approx0.552\ \Omega .
> \end{aligned}
> $$
> The same $R$ comes from adding thin cylindrical shells in series, $dR = dr/(\sigma\,2\pi rL)$.
>
> **(c)** Along $z$ the cross-section is the annulus, the same at every $z$: $R_{\text{axial}} = \dfrac{L}{\sigma\pi(b^2-a^2)}\approx53.1\ \Omega$. That is about 96 times larger: the axial path is long (10 cm) and narrow, the radial path short (1 cm) and wide.
>
> **Check:** for a thin wall $b = a+t$ with $t\ll a$, $\ln(b/a)\approx t/a$ and $R\to t/(\sigma\,2\pi aL)$. That is length over $\sigma$ times area for a flat sheet of thickness $t$ and area $2\pi aL$ ✓. Also $\nabla\cdot\mathbf{J} = \dfrac1r\dfrac{d}{dr}(rJ_r) = 0$, since $rJ_r$ is constant ✓.
>
> **Watch out:** $\mathbf{J}$ is not uniform here, so no single "$A$" works in $\ell/(\sigma A)$. Whenever the cross-section changes along the current path, integrate $dR = d\ell/(\sigma A)$.
>
> **Answer.** $\mathbf{J} = \dfrac{I}{2\pi rL}\hat{r}$, $\mathbf{E} = \dfrac{I}{2\pi\sigma rL}\hat{r}$: $J\approx477$ and 239 A/m², $E\approx239$ and 119 V/m at $r = a$ and $b$. $V(a)-V(b)\approx1.65$ V and $R = \ln(b/a)/(2\pi\sigma L)\approx0.552\ \Omega$. The axial resistance is $\approx53.1\ \Omega$, about 96 times larger.

### 8.7 A radially polarized ball

> [!medium] Medium · bound charge · spherical symmetry
> A ball of radius $R = 5$ cm in free space carries a permanent radial polarization and no free charge. With $P_0 = 2\ \mu$C/m², consider two profiles inside the ball: profile 1, $\mathbf{P} = P_0\hat{r}$; profile 2, $\mathbf{P} = P_0(r/R)\,\hat{r}$.
> (a) For each profile, find $\rho_b$ inside and $\rho_{sb}$ on the surface, and show that the total bound charge is zero.
> (b) Find $\mathbf{E}$ inside and outside the ball for each profile.
> (c) For profile 2, find $V(0)-V(\infty)$.
>
> *Source: classic.*

> [!hint]- Hint
> Use the spherical divergence $\nabla\cdot\mathbf{P} = \dfrac{1}{r^2}\dfrac{d}{dr}(r^2P_r)$. For the field you do not need to add up the bound charges: how much *free* charge does a sphere of radius $r$ enclose, and what does that tell you about $\mathbf{D}$?

> [!solution]- Solution
> **Setup.** $\mathbf{P} = P_r(r)\hat{r}$, so $\rho_b = -\dfrac{1}{r^2}\dfrac{d}{dr}(r^2P_r)$. On the surface $\hat{n} = \hat{r}$, so $\rho_{sb} = P_r(R)$.
>
> **(a)** Profile 1: $r^2P_r = P_0r^2$, so $\rho_b = -2P_0/r$. That is $-8\times10^{-5}$ C/m³ at the surface and $-1.6\times10^{-4}$ C/m³ at $r = R/2$, growing toward the centre. Profile 2: $r^2P_r = P_0r^3/R$, so $\rho_b = -3P_0/R = -1.2\times10^{-4}$ C/m³, uniform. Both have $P_r(R) = P_0$, so $\rho_{sb} = 2\ \mu$C/m², and the surface holds $4\pi R^2P_0\approx62.8$ nC. The volume charges are
> $$
> \int_0^R\Big(-\frac{2P_0}{r}\Big)4\pi r^2\,dr = -4\pi P_0R^2,\qquad \Big(-\frac{3P_0}{R}\Big)\frac{4\pi R^3}{3} = -4\pi P_0R^2,
> $$
> i.e. $-62.8$ nC in both cases, so the total bound charge is zero ✓. It had to be: by the divergence theorem $\int\rho_b\,dV = -\oint\mathbf{P}\cdot d\mathbf{S}$, exactly minus the surface charge.
>
> **(b)** Gauss's law for $\mathbf{D}$ on a sphere of radius $r$ gives $D_r\,4\pi r^2 = Q_{\text{free,enc}} = 0$, so $\mathbf{D} = 0$ everywhere. Then $\epsilon_0\mathbf{E} = \mathbf{D}-\mathbf{P} = -\mathbf{P}$:
> $$
> \mathbf{E} = -\frac{\mathbf{P}}{\epsilon_0}\quad(r<R),\qquad \mathbf{E} = 0\quad(r>R).
> $$
> Profile 1: $\mathbf{E} = -(P_0/\epsilon_0)\hat{r}\approx-2.26\times10^{5}\,\hat{r}$ V/m, with the same magnitude at every interior point. Profile 2: $\mathbf{E} = -\dfrac{P_0r}{\epsilon_0R}\hat{r}$, which is $-1.13\times10^{5}\,\hat{r}$ V/m at $r = R/2$ and $-2.26\times10^{5}\,\hat{r}$ V/m just inside the surface. Inside, $\mathbf{E}$ points inward, against $\mathbf{P}$; outside the neutral ball there is no field.
>
> **(c)** $\mathbf{E} = 0$ outside, so only the interior contributes:
> $$
> V(0)-V(\infty) = -\int_\infty^0E_r\,dr = \int_0^R\Big(-\frac{P_0r}{\epsilon_0R}\Big)dr = -\frac{P_0R}{2\epsilon_0}\approx-5.65\ \text{kV}.
> $$
> The centre is *lower* than infinity: walking inward, you move along $\mathbf{E}$.
>
> **Check:** use Gauss's law for $\epsilon_0\mathbf{E}$ with the *total* charge instead. For profile 1, a sphere of radius $r$ encloses $\int_0^r(-2P_0/s)\,4\pi s^2\,ds = -4\pi P_0r^2$, so $\epsilon_0E_r\,4\pi r^2 = -4\pi P_0r^2$ and $E_r = -P_0/\epsilon_0$ ✓. That is the same answer the $\mathbf{D}$ route gave in one line.
>
> **Watch out:** $\mathbf{D} = 0$ does not mean $\mathbf{E} = 0$. With no free charge, $\mathbf{E}$ comes entirely from bound charge, and here it is large.
>
> **Answer.** (a) $\rho_b = -2P_0/r$ (profile 1) and $-3P_0/R = -1.2\times10^{-4}$ C/m³ (profile 2); $\rho_{sb} = P_0 = 2\ \mu$C/m² for both, 62.8 nC in all, balanced by $-62.8$ nC in the volume. (b) $\mathbf{E} = -\mathbf{P}/\epsilon_0$ inside and 0 outside: $\approx-2.26\times10^5\,\hat{r}$ V/m throughout the ball for profile 1, $-(P_0r/\epsilon_0R)\,\hat{r}$ for profile 2. (c) $V(0)-V(\infty) = -P_0R/(2\epsilon_0)\approx-5.65$ kV.

### 8.8 Point charge in a dielectric sphere

> [!medium] Medium · bound charge · Gauss's law for D
> A point charge $q = 8$ nC sits at the centre of a solid dielectric sphere of radius $R = 3$ cm and permittivity $\epsilon = 4\epsilon_0$; outside is free space.
> (a) Find $\mathbf{D}$, $\mathbf{E}$ and $\mathbf{P}$ everywhere, and evaluate $E$ just inside and just outside $r = R$.
> (b) Find $\rho_b$ for $0<r<R$ and $\rho_{sb}$ on $r = R$. How much bound charge sits on the surface?
> (c) The dielectric is neutral, so this surface charge must be balanced somewhere. Apply Gauss's law for $\epsilon_0\mathbf{E}$ to a small sphere around $q$ to find where.
> (d) Check that $\epsilon_0[E_r(R^+)-E_r(R^-)]$ equals $\rho_{sb}$.
>
> *Source: classic.*

> [!hint]- Hint
> $\mathbf{D}$ depends only on the free charge, so it is the same as with no dielectric at all. Gauss's law for $\epsilon_0\mathbf{E}$, on the other hand, counts free *and* bound charge.

> [!solution]- Solution
> **Setup.** Spherical symmetry. A Gaussian sphere of radius $r$ encloses only the free charge $q$, whatever the material, so $\mathbf{D} = \dfrac{q}{4\pi r^2}\hat{r}$ for all $r>0$. Then $\mathbf{E} = \mathbf{D}/\epsilon$ region by region.
>
> **(a)**
> $$
> \mathbf{E} = \begin{cases}\dfrac{q}{4\pi\epsilon r^2}\hat{r}, & r<R\\ \dfrac{q}{4\pi\epsilon_0r^2}\hat{r}, & r>R\end{cases}\qquad
> \mathbf{P} = \mathbf{D}-\epsilon_0\mathbf{E} = \Big(1-\frac{\epsilon_0}{\epsilon}\Big)\mathbf{D} = \frac34\,\frac{q}{4\pi r^2}\hat{r}\quad(r<R),
> $$
> and $\mathbf{P} = 0$ outside. The same $\mathbf{P}$ follows from $\epsilon_0\chi_e\mathbf{E}$ with $\chi_e = 3$. At the surface $D(R)\approx7.07\times10^{-7}$ C/m², $E(R^-)\approx2.00\times10^4$ V/m and $E(R^+)\approx7.99\times10^4$ V/m, both along $+\hat{r}$.
>
> **(b)** $r^2P_r = \tfrac34\,q/(4\pi)$ is constant, so $\rho_b = -\dfrac{1}{r^2}\dfrac{d}{dr}(r^2P_r) = 0$ throughout $0<r<R$. On the surface $\hat{n} = \hat{r}$:
> $$
> \rho_{sb} = P_r(R) = \frac34\,\frac{q}{4\pi R^2}\approx5.31\times10^{-7}\ \text{C/m}^2 = 531\ \text{nC/m}^2,
> $$
> a total of $\tfrac34q = 6$ nC.
>
> **(c)** On a sphere of any radius $r<R$, however small, $\epsilon_0E_r\,4\pi r^2 = q\,\epsilon_0/\epsilon = 2$ nC. So the total charge at the centre is 2 nC, not 8 nC: a bound point charge of $-6$ nC sits on top of $q$, because the negative ends of the dipoles crowd around it. The total bound charge is $-6+6 = 0$ ✓.
>
> **(d)** $E(R^+)-E(R^-)\approx5.99\times10^4$ V/m, and $\epsilon_0$ times this is $\approx5.31\times10^{-7}$ C/m² $= \rho_{sb}$ ✓. Meanwhile $D_r$ is continuous at $r = R$, as it must be with no free surface charge ✓.
>
> **Check:** outside, the bound charges ($-6$ nC at the centre, $+6$ nC spread uniformly over the surface) cancel, so the field is that of $q$ alone ✓. A dielectric sphere centred on a charge is invisible from outside.
>
> **Watch out:** "$\rho_b = 0$ inside" does not mean there is no bound charge inside. It is concentrated at $r = 0$, where $\nabla\cdot\mathbf{P}$ is singular, just like the point charge's own density.
>
> **Answer.** (a) $\mathbf{D} = q\hat{r}/(4\pi r^2)$ everywhere; $\mathbf{E} = q\hat{r}/(4\pi\epsilon r^2)$ inside and $q\hat{r}/(4\pi\epsilon_0r^2)$ outside, $\approx2.00\times10^4$ and $7.99\times10^4$ V/m at $R^-$ and $R^+$; $\mathbf{P} = \tfrac34\,q\hat{r}/(4\pi r^2)$ inside. (b) $\rho_b = 0$; $\rho_{sb}\approx531$ nC/m², 6 nC in all. (c) A bound point charge of $-6$ nC at the centre, leaving a net 2 nC there. (d) $\epsilon_0\times5.99\times10^4$ V/m $\approx5.31\times10^{-7}$ C/m² $= \rho_{sb}$ ✓.

## Hard

### 8.9 Charge in a conducting shell's cavity

> [!hard] Hard · conductors · induced charge · potential
> A thick, isolated conducting shell occupies $b\le r\le c$ with $b = 2$ cm and $c = 4$ cm, and carries net charge $Q_s = -5$ nC. A point charge $q = +3$ nC sits at the centre of the cavity $r<b$. Everything is in free space.
> (a) Find the total charge and the surface charge density on the inner surface $r = b$ and on the outer surface $r = c$.
> (b) Find $\mathbf{E}$ in the cavity, in the metal and outside, and evaluate it at $r = 1$, 3 and 5 cm.
> (c) Taking $V(\infty) = 0$, find the potential of the shell and $V$ at $r = 1$ cm.
> (d) The charge $q$ is moved 1 cm off centre, still inside the cavity. Which of your answers to (a)–(c) change, and how?
> (e) With $q$ back at the centre, the shell is connected to ground. Find the new charge on each surface, the charge that flows through the ground wire, and the new $V(1\text{ cm})$.
>
> *Source: classic.*

> [!hint]- Hint
> Draw a Gaussian sphere *inside the metal*: $\mathbf{E} = 0$ there, so it encloses zero net charge. That fixes the inner surface, and charge conservation fixes the outer one. For potentials, integrate inward from infinity; the metal is a single equipotential.

> [!solution]- Solution
> **Setup.** With $q$ at the centre everything is spherically symmetric. In equilibrium $\mathbf{E} = 0$ in the metal, and all of the shell's charge sits on its two surfaces.
>
> **(a)** A Gaussian sphere of radius $b<r<c$ lies in the metal, where $\mathbf{D} = 0$, so it encloses no net charge: $q+Q_{\text{inner}} = 0$ and $Q_{\text{inner}} = -q = -3$ nC. The rest of the shell's charge is on the outside: $Q_{\text{outer}} = Q_s-Q_{\text{inner}} = Q_s+q = -2$ nC. By symmetry both layers are uniform:
> $$
> \rho_s(b) = \frac{-3\times10^{-9}}{4\pi(0.02)^2}\approx-597\ \text{nC/m}^2,\qquad \rho_s(c) = \frac{-2\times10^{-9}}{4\pi(0.04)^2}\approx-99.5\ \text{nC/m}^2 .
> $$
>
> **(b)** Gauss's law with the enclosed charge in each region:
> $$
> \mathbf{E} = \begin{cases}\dfrac{q}{4\pi\epsilon_0r^2}\hat{r}, & r<b\\ 0, & b<r<c\\ \dfrac{q+Q_s}{4\pi\epsilon_0r^2}\hat{r}, & r>c\end{cases}
> $$
> With $q/(4\pi\epsilon_0)\approx27.0$ V·m and $(q+Q_s)/(4\pi\epsilon_0)\approx-18.0$ V·m: $E_r(1\text{ cm})\approx2.70\times10^5$ V/m, pointing outward; $E_r(3\text{ cm}) = 0$; $E_r(5\text{ cm})\approx-7.19\times10^3$ V/m, pointing inward because the outside of the shell is negative.
>
> **(c)** Outside, the field is that of a point charge $q+Q_s$, so the outer surface, and with it the whole metal, is at
> $$
> V(c) = \frac{q+Q_s}{4\pi\epsilon_0c}\approx-449\ \text{V}.
> $$
> Inside the cavity $V(r)-V(b) = -\int_b^rE_r\,dr' = \dfrac{q}{4\pi\epsilon_0}\Big(\dfrac1r-\dfrac1b\Big)$, so
> $$
> V(1\text{ cm}) = V(b)+\frac{q}{4\pi\epsilon_0}\Big(\frac{1}{0.01}-\frac{1}{0.02}\Big)\approx-449+1348\approx899\ \text{V}.
> $$
>
> **(d)** Moving $q$ changes only what happens *inside the cavity*:
> - The inner surface still carries $-q = -3$ nC in total, since the Gaussian sphere in the metal is unchanged. But it is no longer uniform: it is densest on the side nearest $q$.
> - The outer surface still carries $-2$ nC, and it stays uniform. The metal screens the cavity: $q$ and the inner surface charge together produce no field beyond $r = b$ (that is how $\mathbf{E} = 0$ in the metal is achieved). So the outer charge spreads as it would on an isolated sphere, uniformly.
> - Hence $\mathbf{E} = 0$ in the metal, the field outside and the shell potential of $-449$ V are all unchanged. The cavity field is no longer radial about the centre, and the formula for $V(1\text{ cm})$ in (c) no longer applies.
>
> **(e)** Grounding sets $V(c) = 0$, and since $V(c) = Q_{\text{outer}}/(4\pi\epsilon_0c)$, the outer surface must lose all its charge. The inner surface still holds $-3$ nC, so the shell's net charge is now $-3$ nC instead of $-5$ nC: $+2$ nC flows *from* ground *onto* the shell. Physically, electrons carrying $-2$ nC leave through the wire. Outside, $\mathbf{E} = 0$. In the cavity only the reference changes:
> $$
> V(1\text{ cm}) = 0+\frac{q}{4\pi\epsilon_0}\Big(\frac{1}{0.01}-\frac{1}{0.02}\Big)\approx1348\ \text{V}.
> $$
>
> **Check:** $V(1\text{ cm})-V_{\text{shell}}\approx899-(-449)\approx1348$ V in both (c) and (e). Grounding shifts the potential of the whole interior by the same 449 V without touching the cavity field ✓.
>
> **Watch out:** the shell's charge does not simply sit on its outer surface. Whatever its net charge, the inner surface carries exactly $-q$.
>
> **Answer.** (a) Inner surface $-3$ nC ($\approx-597$ nC/m²), outer surface $-2$ nC ($\approx-99.5$ nC/m²). (b) $\mathbf{E} = q\hat{r}/(4\pi\epsilon_0r^2)$ for $r<b$, 0 in the metal, $(q+Q_s)\hat{r}/(4\pi\epsilon_0r^2)$ for $r>c$: $2.70\times10^5$ V/m outward at 1 cm, 0 at 3 cm, $7.19\times10^3$ V/m inward at 5 cm. (c) $V_{\text{shell}}\approx-449$ V, $V(1\text{ cm})\approx899$ V. (d) Only the inner surface's distribution and the cavity field change; the surface totals, the outer layer, the field outside and $V_{\text{shell}}$ do not. (e) Outer surface 0, inner surface $-3$ nC; $+2$ nC flows onto the shell from ground; $V(1\text{ cm})\approx1348$ V.

### 8.10 Relaxation of a charge wave

> [!hard] Hard · relaxation time · continuity · Gauss's law
> An infinite homogeneous medium has $\epsilon = 9\epsilon_0$ and $\sigma = 900\epsilon_0$ S/m. At $t = 0$ it contains the free charge density $\rho(x,0) = 18\epsilon_0\cos(3x)$ C/m³ ($x$ in meters), and there is no applied field.
> (a) Find $\rho(x,t)$. When has the density everywhere fallen to 1% of its initial value?
> (b) Find $\mathbf{E}(x,t)$ and $\mathbf{J}(x,t)$.
> (c) Verify that $\rho$ and $\mathbf{J}$ satisfy the continuity equation, and describe the direction of the current near $x = 0$. Where does the positive charge of the lump $\lvert x\rvert<\pi/6$ go?
> (d) Evaluate $E_x$ at $x = \pi/6$ m and $\rho$ at $x = 0$, both at $t = 10$ ms.
> (e) If the initial density were $18\epsilon_0\cos(30x)$ instead, how would the decay time and the field amplitude change?
>
> *Source: Summer 2017 HE2 #2a style, re-parameterized (dielectric host, amplitude and axis changed).*

> [!hint]- Hint
> Combine $\partial\rho/\partial t+\nabla\cdot\mathbf{J} = 0$, $\mathbf{J} = \sigma\mathbf{E}$ and $\nabla\cdot\mathbf{E} = \rho/\epsilon$: every point obeys the same first-order equation in time. For $\mathbf{E}$, integrate Gauss's law in $x$; the symmetry of $\rho$ about $x = 0$ fixes the constant.

> [!solution]- Solution
> **Setup.** The medium is uniform, so $\epsilon$ and $\sigma$ come out of every divergence. Everything depends on $x$ only, so $\mathbf{E} = E_x(x,t)\hat{x}$ and $\mathbf{J} = J_x(x,t)\hat{x}$.
>
> **(a)** $\dfrac{\partial\rho}{\partial t} = -\nabla\cdot\mathbf{J} = -\sigma\nabla\cdot\mathbf{E} = -\dfrac{\sigma}{\epsilon}\rho$. Each point decays on its own, with the same time constant:
> $$
> \rho(x,t) = 18\epsilon_0\cos(3x)\,e^{-t/\tau},\qquad \tau = \frac{\epsilon}{\sigma} = \frac{9\epsilon_0}{900\epsilon_0} = 0.01\ \text{s}.
> $$
> The shape is frozen and only the amplitude shrinks. It reaches 1% at $t = \tau\ln100\approx46.1$ ms.
>
> **(b)** In one dimension Gauss's law reads $\epsilon\,\partial E_x/\partial x = \rho$, so
> $$
> E_x = \frac{18\epsilon_0}{9\epsilon_0\cdot3}\sin(3x)\,e^{-t/\tau}+C(t) = \frac23\sin(3x)\,e^{-100t}\ \text{V/m}.
> $$
> $C = 0$: $\rho$ is even in $x$, which makes $E_x$ odd, so $E_x(0) = 0$. A nonzero $C$ would be a uniform applied field, and there is none. Then
> $$
> J_x = \sigma E_x = 900\epsilon_0\cdot\frac23\sin(3x)\,e^{-100t} = 600\epsilon_0\sin(3x)\,e^{-100t}\ \text{A/m}^2,
> $$
> an amplitude of $\approx5.31\times10^{-9}$ A/m² (the conductivity is only $\approx7.97\times10^{-9}$ S/m).
>
> **(c)** $\dfrac{\partial\rho}{\partial t} = -1800\epsilon_0\cos(3x)\,e^{-100t}$ and $\dfrac{\partial J_x}{\partial x} = 3\cdot600\epsilon_0\cos(3x)\,e^{-100t} = +1800\epsilon_0\cos(3x)\,e^{-100t}$, which add to zero ✓. Just right of $x = 0$, $\sin(3x)>0$ and $J_x>0$; just left of it, $J_x<0$. So the current flows *away* from the crest at $x = 0$, in both directions.
>
> The lump $\lvert x\rvert<\pi/6$ holds $\displaystyle\int_{-\pi/6}^{\pi/6}18\epsilon_0\cos(3x)\,dx = 12\epsilon_0$ C per square meter of the $yz$ plane. It drains into the neighbouring negative lumps and neutralizes them. Each spatial period holds zero net charge, so the medium ends up neutral everywhere; no charge has to be pushed to a surface.
>
> **(d)** $E_x(\pi/6,\,10\text{ ms}) = \tfrac23\sin(\pi/2)\,e^{-1}\approx0.245$ V/m, and $\rho(0,\,10\text{ ms}) = 18\epsilon_0e^{-1}\approx6.62\epsilon_0$ C/m³.
>
> **(e)** $\tau = \epsilon/\sigma$ contains no length, so the decay is exactly as fast as before ($\tau$ is still 10 ms). The field amplitude $\rho_0/(k\epsilon)$, with $k$ the coefficient of $x$, drops tenfold to $\approx0.0667$ V/m. Each lump is ten times narrower, so it holds ten times less charge per unit area and needs ten times less current, and hence field, to drain in the same time.
>
> **Check:** the units of $\rho_0/(k\epsilon)$ are $\dfrac{\text{C/m}^3}{(1/\text{m})(\text{F/m})} = \dfrac{\text{C}}{\text{F}\cdot\text{m}} = \text{V/m}$ ✓. As $\sigma\to0$, $\tau\to\infty$ and the charge stays put, as in an insulator ✓.
>
> **Answer.** (a) $\rho = 18\epsilon_0\cos(3x)\,e^{-100t}$ C/m³ with $\tau = 10$ ms; 1% after $\approx46.1$ ms. (b) $\mathbf{E} = \tfrac23\sin(3x)\,e^{-100t}\,\hat{x}$ V/m, $\mathbf{J} = 600\epsilon_0\sin(3x)\,e^{-100t}\,\hat{x}$ A/m². (c) Continuity holds. Current flows away from $x = 0$ in both directions, carrying the $12\epsilon_0$ C/m² of each positive lump into the neighbouring negative lumps. (d) $\approx0.245$ V/m and $\approx6.62\epsilon_0$ C/m³. (e) Same $\tau$; the field amplitude is ten times smaller, $\approx0.0667$ V/m.

### 8.11 Electret rod in a grounded tube

> [!hard] Hard · bound charge · conductors · cylindrical symmetry
> A long cylindrical electret of radius $a = 2$ cm lies along the $z$ axis. It carries no free charge, and its polarization is frozen in: $\mathbf{P} = P_0(r/a)\,\hat{r}$ for $r<a$, with $P_0 = 10^5\epsilon_0$ C/m² $\approx0.885\ \mu$C/m², whatever field is applied. A thin conducting tube of radius $b = 5$ cm, coaxial with the electret, is grounded. Everything else is free space.
> (a) Find $\rho_b$ in the electret, $\rho_{sb}$ on its surface, and the total bound charge per unit length.
> (b) Find $\mathbf{D}$ and $\mathbf{E}$ for $0<r<b$, and evaluate $\mathbf{E}$ at $r = 1$ cm and just inside $r = a$. Why is $\mathbf{D} = 0$ in the electret although $\mathbf{E}\neq0$ there?
> (c) Find the charge per unit length induced on each surface of the tube, the field outside the tube, and the potential of the axis relative to the tube, $V(0)-V(b)$.
> (d) A free line charge $\rho_l = 1000\pi\epsilon_0$ C/m $\approx27.8$ nC/m is now placed on the axis. Find $\mathbf{D}$ and $\mathbf{E}$ everywhere, the radius inside the electret at which $\mathbf{E} = 0$, and the charge per unit length on each surface of the tube.
>
> *Source: original.*

> [!hint]- Hint
> In cylindrical coordinates $\rho_b = -\dfrac1r\dfrac{d}{dr}(rP_r)$. Gauss's law for $\mathbf{D}$ counts only *free* charge, and then $\epsilon_0\mathbf{E} = \mathbf{D}-\mathbf{P}$. For the tube, a Gaussian cylinder inside the metal fixes the inner surface. For the outer surface, ask what a net charge per unit length would do to $V$ between the tube and distant ground.

> [!solution]- Solution
> **Setup.** Cylindrical symmetry: every field is radial and depends on $r$ only. On a coaxial Gaussian cylinder of radius $r$ and length $L$, $D_r\,2\pi rL$ equals the *free* charge enclosed and $\epsilon_0E_r\,2\pi rL$ the *total* (free plus bound) charge enclosed. $\mathbf{P}$ is given and stays fixed, whatever the fields do.
>
> **(a)** With $rP_r = P_0r^2/a$,
> $$
> \rho_b = -\frac1r\frac{d}{dr}\Big(\frac{P_0r^2}{a}\Big) = -\frac{2P_0}{a} = -10^7\epsilon_0\ \text{C/m}^3\approx-88.5\ \mu\text{C/m}^3,
> $$
> the same everywhere in the electret. On its surface $\hat{n} = \hat{r}$, so $\rho_{sb} = P_r(a) = P_0 = 10^5\epsilon_0$ C/m² $\approx0.885\ \mu$C/m². Per unit length the volume holds $\rho_b\pi a^2 = -2\pi aP_0 = -4000\pi\epsilon_0$ C/m $\approx-111$ nC/m, and the surface $2\pi a\rho_{sb} = +4000\pi\epsilon_0$ C/m $\approx+111$ nC/m. The total bound charge is zero ✓, as it must be for matter that was neutral before it was polarized.
>
> **(b)** There is no free charge inside the tube, so a Gaussian cylinder of any radius $r<b$ encloses none: $D_r\,2\pi rL = 0$, and $\mathbf{D} = 0$ for $0<r<b$. Then $\epsilon_0\mathbf{E} = \mathbf{D}-\mathbf{P} = -\mathbf{P}$:
> $$
> \mathbf{E} = -\frac{P_0r}{\epsilon_0a}\hat{r} = -5\times10^{6}\,r\,\hat{r}\ \text{V/m}\quad(r<a,\ r\text{ in m}),\qquad \mathbf{E} = 0\quad(a<r<b).
> $$
> At $r = 1$ cm, $\mathbf{E} = -5\times10^4\,\hat{r}$ V/m; just inside $r = a$, $\mathbf{E} = -10^5\,\hat{r}$ V/m. The field points inward, against $\mathbf{P}$.
>
> $\mathbf{D}$ and $\mathbf{E}$ have different sources. $\nabla\cdot\mathbf{D} = \rho$ counts free charge only, and with this symmetry Gauss's law pins $\mathbf{D}$ to zero. $\mathbf{E}$ counts all charge: the negative bound charge filling the electret pulls the field inward, while the positive surface layer, like any uniform cylindrical shell, makes no field inside itself. In $\mathbf{D} = \epsilon_0\mathbf{E}+\mathbf{P}$ the two terms cancel exactly. A linear dielectric could not do this: with $\mathbf{P} = \epsilon_0\chi_e\mathbf{E}$, $\mathbf{D} = 0$ would force $\mathbf{E} = \mathbf{P} = 0$. An electret's $\mathbf{P}$ needs no field to sustain it.
>
> **(c)** In the metal $\mathbf{D} = 0$, so a Gaussian cylinder inside the tube's wall encloses no free charge: the inner surface carries none. Equivalently, $\rho_s = \hat{n}\cdot\mathbf{D} = -D_r(b^-) = 0$, with $\hat{n} = -\hat{r}$ pointing out of the metal. Outside the tube $E_r = \lambda/(2\pi\epsilon_0r)$, where $\lambda$ is the outer surface's charge per unit length (everything inside it adds up to zero). Between the tube and a distant radius $R$ the potential would then change by $\dfrac{\lambda}{2\pi\epsilon_0}\ln\dfrac{R}{b}$, which grows without limit, so a tube held at the potential of distant ground must have $\lambda = 0$. The tube carries **no charge**, and $\mathbf{D} = \mathbf{E} = 0$ outside it: the neutral electret's field never leaves the electret.
>
> The potential inside is still not uniform. With $\mathbf{E} = 0$ in the gap,
> $$
> V(0)-V(b) = -\int_b^0E_r\,dr = \int_0^aE_r\,dr = -\frac{P_0}{\epsilon_0a}\,\frac{a^2}{2} = -\frac{P_0a}{2\epsilon_0} = -\frac{10^5(0.02)}{2} = -1000\ \text{V}.
> $$
> The axis sits 1 kV *below* the tube, although no charge was induced: walking inward from $r = a$, you move along $\mathbf{E}$.
>
> **(d)** $\mathbf{P}$ is frozen, so $\rho_b$ and $\rho_{sb}$ are exactly those of (a). The free charge enclosed is now $\rho_l$ for every $0<r<b$, and $\rho_l/(2\pi) = 500\epsilon_0$ C/m:
> $$
> \mathbf{D} = \frac{\rho_l}{2\pi r}\hat{r} = \frac{500\epsilon_0}{r}\hat{r}\ \text{C/m}^2,\qquad
> \mathbf{E} = \frac{\mathbf{D}-\mathbf{P}}{\epsilon_0} = \begin{cases}\Big(\dfrac{500}{r}-5\times10^{6}\,r\Big)\hat{r}\ \text{V/m}, & r<a\\ \dfrac{500}{r}\hat{r}\ \text{V/m}, & a<r<b\end{cases}
> $$
> ($r$ in m). Inside the electret $E_r = 0$ where $500/r_0 = 5\times10^6r_0$, i.e. $r_0 = 1$ cm $= a/2$. Nearer the axis the line charge wins and $\mathbf{E}$ points outward; between 1 cm and $a$ the electret wins and $\mathbf{E}$ points inward, reaching $-7.5\times10^4\,\hat{r}$ V/m just inside $r = a$. Just outside $r = a$ the field is $+2.5\times10^4\,\hat{r}$ V/m, falling to $+10^4\,\hat{r}$ V/m at the tube.
>
> On the tube's inner surface ($\hat{n} = -\hat{r}$), $\rho_s = -D_r(b) = -10^4\epsilon_0$ C/m² $\approx-88.5$ nC/m², which is $-\rho_l = -1000\pi\epsilon_0\approx-27.8$ nC/m per unit length, as the Gaussian cylinder in the metal demands. Inside the outer surface the charges now add up to $\rho_l+0-\rho_l = 0$, so the outer surface stays uncharged and $\mathbf{D} = \mathbf{E} = 0$ outside. The $-27.8$ nC/m came up the ground wire.
>
> **Check:** Gauss's law for $\epsilon_0\mathbf{E}$, counting free and bound charge, gives the null directly. A cylinder of radius $r_0$ encloses $\rho_l+\rho_b\pi r_0^2 = 1000\pi\epsilon_0-10^7\pi\epsilon_0r_0^2$ per unit length, which vanishes at $r_0^2 = 10^{-4}$ m² ✓. At $r = a$, $\epsilon_0[E_r(a^+)-E_r(a^-)]$ is $\epsilon_0(0+10^5)$ in (b) and $\epsilon_0(2.5\times10^4+7.5\times10^4)$ in (d): $10^5\epsilon_0 = \rho_{sb}$ both times ✓. Meanwhile $D_r$ is continuous there, because the electret's surface holds no free charge ✓. With $P_0\to0$, (d) reduces to the coax field $\rho_l/(2\pi\epsilon_0r)$ ✓.
>
> **Watch out:** an electret is not a linear dielectric. In 8.8 the linear dielectric wrapped the free charge in bound charge $-(\chi_e/\epsilon_r)q$. Here $\mathbf{P}$ cannot respond, so adding $\rho_l$ creates no new bound charge, and $\mathbf{E} = (\mathbf{D}-\mathbf{P})/\epsilon_0$, not $\mathbf{D}/\epsilon$.
>
> **Answer.** (a) $\rho_b = -2P_0/a = -10^7\epsilon_0$ C/m³ $\approx-88.5\ \mu$C/m³ and $\rho_{sb} = P_0\approx0.885\ \mu$C/m²; per unit length $-4000\pi\epsilon_0$ C/m in the volume and $+4000\pi\epsilon_0$ C/m on the surface ($\approx\mp111$ nC/m), total zero. (b) $\mathbf{D} = 0$ for $r<b$; $\mathbf{E} = -\mathbf{P}/\epsilon_0 = -5\times10^6r\,\hat{r}$ V/m in the electret ($-5\times10^4\,\hat{r}$ V/m at 1 cm, $-10^5\,\hat{r}$ V/m at $a^-$) and 0 in the gap. (c) No charge on either surface of the tube, $\mathbf{E} = 0$ outside it, and $V(0)-V(b) = -P_0a/(2\epsilon_0) = -1$ kV. (d) $\mathbf{D} = (500\epsilon_0/r)\,\hat{r}$ C/m² for $r<b$; $\mathbf{E} = (500/r-5\times10^6r)\,\hat{r}$ V/m in the electret, zero at $r = 1$ cm, and $(500/r)\,\hat{r}$ V/m in the gap; inner surface $-\rho_l\approx-27.8$ nC/m ($-10^4\epsilon_0\approx-88.5$ nC/m²), outer surface 0, and $\mathbf{D} = \mathbf{E} = 0$ outside.

### 8.12 Rod polarized across its axis

> [!hard] Hard · bound charge · superposition · boundary conditions
> A long dielectric rod of radius $a = 1$ cm lies along the $z$ axis in free space. It carries a uniform permanent polarization $\mathbf{P} = P_0\hat{x}$, perpendicular to its axis, with $P_0 = 1\ \mu$C/m², and no free charge. Use cylindrical coordinates $(r,\phi,z)$.
> (a) Find $\rho_b$, $\rho_{sb}(\phi)$ on $r = a$, and the total bound charge per unit length.
> (b) Model the rod as two overlapping cylinders of uniform charge density $+\rho$ and $-\rho$, the positive one shifted by a small distance $d$ along $+x$, with $\rho d = P_0$. Using the field of a uniformly charged cylinder, find $\mathbf{E}$ and $\mathbf{D}$ inside the rod.
> (c) Outside, each cylinder acts as a line charge on its own axis. Show that the potential outside is $V = \dfrac{P_0a^2\cos\phi}{2\epsilon_0r}$, find $\mathbf{E}$ there, and evaluate it at $(x,y) = (3\text{ cm},0)$ and $(0,3\text{ cm})$.
> (d) Verify the boundary conditions at $r = a$ for every $\phi$.
> (e) Compare the interior field with that of a slab polarized normal to its faces, and with that of a uniformly polarized sphere, $-\mathbf{P}/(3\epsilon_0)$.
>
> *Source: classic (uniformly polarized cylinder).*

> [!hint]- Hint
> Inside a cylinder of uniform charge $\rho$, Gauss's law gives $\mathbf{E} = \dfrac{\rho}{2\epsilon_0}\times$ (the perpendicular vector from that cylinder's own axis to the field point). Write both contributions as vectors and add: the position-dependent parts cancel. Outside, a line charge has $V = -\dfrac{\rho_l}{2\pi\epsilon_0}\ln r+\text{const}$.

> [!solution]- Solution
> **(a)** $\mathbf{P}$ is uniform, so $\rho_b = -\nabla\cdot\mathbf{P} = 0$. On the curved surface $\hat{n} = \hat{r} = \cos\phi\,\hat{x}+\sin\phi\,\hat{y}$, so
> $$
> \rho_{sb} = \mathbf{P}\cdot\hat{r} = P_0\cos\phi,
> $$
> positive on the side $\mathbf{P}$ points toward ($\phi = 0$) and negative on the far side. Per unit length, $\displaystyle\int_0^{2\pi}P_0\cos\phi\;a\,d\phi = 0$ ✓.
>
> **(b)** Let $\mathbf{r}_\perp = x\hat{x}+y\hat{y}$. The positive cylinder has its axis at $x = d/2$ and the negative one at $x = -d/2$, so at any point inside both,
> $$
> \mathbf{E} = \frac{\rho}{2\epsilon_0}\Big(\mathbf{r}_\perp-\frac d2\hat{x}\Big)-\frac{\rho}{2\epsilon_0}\Big(\mathbf{r}_\perp+\frac d2\hat{x}\Big) = -\frac{\rho d}{2\epsilon_0}\hat{x} = -\frac{P_0}{2\epsilon_0}\hat{x}.
> $$
> The position-dependent parts cancel, so the interior field is **uniform**: $\approx-5.65\times10^4\,\hat{x}$ V/m, opposite to $\mathbf{P}$. The thin crescents where the cylinders do not overlap have thickness $d\cos\phi$ and density $\pm\rho$, i.e. $\rho d\cos\phi = P_0\cos\phi$ per unit area: exactly the surface charge of (a). Inside, $\mathbf{D} = \epsilon_0\mathbf{E}+\mathbf{P} = \tfrac12P_0\hat{x} = 5\times10^{-7}\,\hat{x}$ C/m².
>
> **(c)** Outside, the cylinders act as line charges $\pm\rho_l = \pm\rho\pi a^2$ on their axes. Let $r_\pm\approx r\mp\tfrac d2\cos\phi$ be the distances to the two lines. Then
> $$
> V = -\frac{\rho_l}{2\pi\epsilon_0}\big(\ln r_+-\ln r_-\big)\approx\frac{\rho_l\,d\cos\phi}{2\pi\epsilon_0r} = \frac{P_0a^2\cos\phi}{2\epsilon_0r},
> $$
> using $\rho_ld = \pi a^2\rho d = \pi a^2P_0$, the dipole moment per unit length ($\mathbf{P}$ times the cross-section). Then $\mathbf{E} = -\nabla V$:
> $$
> \mathbf{E} = \frac{P_0a^2}{2\epsilon_0r^2}\big(\cos\phi\,\hat{r}+\sin\phi\,\hat\phi\big),\qquad r>a .
> $$
> This is a two-dimensional dipole field, falling as $1/r^2$. At $(3\text{ cm},0)$, $r = 3a$ and $\phi = 0$, so $\mathbf{E} = \dfrac{P_0}{18\epsilon_0}\hat{x}\approx6.27\times10^3\,\hat{x}$ V/m. At $(0,3\text{ cm})$, $\phi = 90^\circ$ and $\hat\phi = -\hat{x}$, so $\mathbf{E}\approx-6.27\times10^3\,\hat{x}$ V/m.
>
> **(d)** Just inside, $\mathbf{E} = -\dfrac{P_0}{2\epsilon_0}\hat{x} = -\dfrac{P_0}{2\epsilon_0}\big(\cos\phi\,\hat{r}-\sin\phi\,\hat\phi\big)$. Just outside ($r = a$), $\mathbf{E} = \dfrac{P_0}{2\epsilon_0}\big(\cos\phi\,\hat{r}+\sin\phi\,\hat\phi\big)$.
>
> - Tangential: $E_\phi = \dfrac{P_0}{2\epsilon_0}\sin\phi$ on both sides ✓.
> - Normal, total charge: $\epsilon_0(E_{r,\text{out}}-E_{r,\text{in}}) = P_0\cos\phi = \rho_{sb}$ ✓.
> - Normal $\mathbf{D}$, free charge: outside $\epsilon_0E_r = \tfrac12P_0\cos\phi$; inside $\epsilon_0E_r+P_r = -\tfrac12P_0\cos\phi+P_0\cos\phi = \tfrac12P_0\cos\phi$. So $D_r$ is continuous, as it must be with no free surface charge ✓.
>
> At $\phi = 0$ the field just outside is $\approx+5.65\times10^4\,\hat{x}$ V/m, the *reverse* of the interior field. At $\phi = 90^\circ$ it is $\approx-5.65\times10^4\,\hat{x}$ V/m, the same as inside, because there it is purely tangential.
>
> **(e)** The interior field of a body with uniform $\mathbf{P}$ is $-\mathbf{P}/\epsilon_0$ for a slab polarized normal to its faces (Lecture 8's dipole-lattice result), $-\mathbf{P}/(2\epsilon_0)$ for this rod, and $-\mathbf{P}/(3\epsilon_0)$ for a sphere: factors 1, $\tfrac12$, $\tfrac13$. In the slab the bound charge forms two infinite sheets squarely across the field. In the rod and the sphere it is spread over curved surfaces, so the depolarizing field it makes inside is weaker.
>
> **Check:** the uniform interior field gives $V = \dfrac{P_0}{2\epsilon_0}x = \dfrac{P_0r\cos\phi}{2\epsilon_0}$ inside, which at $r = a$ equals the exterior $V = \dfrac{P_0a\cos\phi}{2\epsilon_0}$ ✓. The potential is continuous across the surface.
>
> **Watch out:** $\mathbf{E} = -\mathbf{P}/\epsilon_0$ is a *slab* result. Using it here would double the interior field.
>
> **Answer.** (a) $\rho_b = 0$, $\rho_{sb} = P_0\cos\phi$, zero net charge per unit length. (b) $\mathbf{E} = -\dfrac{P_0}{2\epsilon_0}\hat{x}\approx-5.65\times10^4\,\hat{x}$ V/m (uniform) and $\mathbf{D} = \tfrac12P_0\hat{x} = 5\times10^{-7}\,\hat{x}$ C/m². (c) $\mathbf{E} = \dfrac{P_0a^2}{2\epsilon_0r^2}\big(\cos\phi\,\hat{r}+\sin\phi\,\hat\phi\big)$: $\approx+6.27\times10^3\,\hat{x}$ V/m at $(3\text{ cm},0)$ and $\approx-6.27\times10^3\,\hat{x}$ V/m at $(0,3\text{ cm})$. (d) $E_\phi$ and $D_r$ are continuous, and $\epsilon_0$ times the jump in $E_r$ is $P_0\cos\phi$. (e) $-\mathbf{P}/\epsilon_0$, $-\mathbf{P}/(2\epsilon_0)$ and $-\mathbf{P}/(3\epsilon_0)$ for slab, rod and sphere.

### Sources for this page
Lecture 8 itself: the conductivity table and relaxation-time derivation (8.2), and the conducting slab in a uniform field (8.4, recast as true/false). Classic textbook problems with new numbers: the copper wire (8.1), the coaxial resistor with radial current (8.6), the radially polarized ball (8.7), a point charge at the centre of a dielectric sphere (8.8), a charge in the cavity of a thick conducting shell (8.9) and the rod polarized across its axis (8.12). Old exam: Summer 2017 HE2 #2a (relaxation of $\rho = \cos 3z$ C/m³ in a conductor with $\epsilon_0$) behind 8.10, re-parameterized with a dielectric host, a new amplitude and the $x$ axis. Problems 8.3, 8.5 and 8.11 (the electret in a grounded tube) are original.

*Previous: [[practice/07-poisson-and-laplace|Lecture 7 practice]] · next: [[practice/09-static-fields-in-dielectric-media|Lecture 9 practice]] · [[practice/index|all practice]]*
