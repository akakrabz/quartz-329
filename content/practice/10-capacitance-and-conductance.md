---
title: "Practice — Lecture 10: Capacitance and conductance"
description: "12 practice problems (5 easy, 3 medium, 4 hard) on the capacitance of plates, coax and spheres, series and parallel dielectric layers, stored energy computed two ways, dielectric insertion and plate forces at fixed charge or fixed voltage, leakage conductance G = (σ/ε)C and RC self-discharge, two lossy layers with interface charge, and the diode junction capacitance, each with a folded hint and a worked solution."
tags: [practice, electrostatics, exam-1]
lecture: 10
---

*Practice for [[1-electrostatics/10-capacitance-and-conductance|Lecture 10]] · concepts: [[concepts/capacitance]] · [[concepts/conductance]] · [[concepts/electrostatic-energy]] · all practice: [[practice/index|hub]] · by difficulty: [[practice/easy|easy]] · [[practice/medium|medium]] · [[practice/hard|hard]] · [[practice/topics|by topic]]*

Work each problem on paper first. Open the **hint** only when stuck, and the **solution** only after you have an answer you would hand in. Every answer here has been checked numerically.

## Easy

### 10.1 Four capacitances by formula

> [!easy] Easy · capacitance · parallel plates · coax and spheres
> Find the capacitance of each structure (air unless stated; ignore fringing).
> (a) Two parallel plates $10\ \text{cm}\times10\ \text{cm}$, $0.5$ mm apart, with a dielectric of $\epsilon_r = 4$ filling the gap. Give the answer also as a multiple of $\epsilon_0$.
> (b) A coaxial cable with inner radius $a = 0.375$ mm and outer radius $b = 1.5$ mm, filled with $\epsilon_r = 2.25$: find the capacitance per unit length $\mathcal{C}$.
> (c) Two concentric spherical shells of radii $4$ cm and $5$ cm.
> (d) An isolated metal sphere of radius $9$ cm.
>
> *Source: original.*

> [!hint]- Hint
> Each part is one formula from Lecture 10, but watch the details: the plates need $\epsilon = \epsilon_r\epsilon_0$, the coax wants the *natural* log of $b/a$, and an isolated sphere is the concentric pair with $b\to\infty$.

> [!solution]- Solution
> Each formula is the end of Lecture 10's chain $Q\to\mathbf{D}\to\mathbf{E}\to V\to C$; here you only need to plug in carefully.
>
> **(a)** $C = \dfrac{\epsilon A}{d} = \dfrac{4\epsilon_0\,(0.1\ \text{m})^2}{0.5\times10^{-3}\ \text{m}} = 80\epsilon_0\approx708$ pF.
>
> **(b)** $\mathcal{C} = \dfrac{2\pi\epsilon}{\ln(b/a)}$ with $b/a = 4$ and $\ln4 = 1.3863$: $\ \mathcal{C} = \dfrac{2\pi(2.25\epsilon_0)}{1.3863}\approx90.3$ pF/m.
>
> **(c)** $C = 4\pi\epsilon_0\dfrac{ab}{b-a}$ with $\dfrac{ab}{b-a} = \dfrac{(0.04)(0.05)}{0.01} = 0.2$ m: $\ C = 4\pi\epsilon_0\,(0.2\ \text{m})\approx22.3$ pF.
>
> **(d)** Let the outer shell recede to infinity, $b\to\infty$: $C = 4\pi\epsilon_0a = \dfrac{0.09\ \text{m}}{9\times10^9\ \text{m/F}}\approx10.0$ pF. Isolated objects have tiny capacitances: even the whole Earth ($a = 6.37\times10^6$ m) has only about $709\ \mu$F.
>
> **Check (units and scaling):** every result is $\epsilon\times$(a length). Doubling every dimension doubles the capacitance of the plates ($A\times4$, $d\times2$) and of the spheres, but leaves the coax's $\mathcal{C}$ unchanged: it depends only on the ratio $b/a$.
>
> **Watch out:** dropping $\epsilon_r$ in (a) gives 177 pF; using $\log_{10}$ instead of $\ln$ in (b) gives 208 pF/m.
>
> **Answer.** (a) $80\epsilon_0\approx708$ pF; (b) $\mathcal{C}\approx90.3$ pF/m; (c) $22.3$ pF; (d) $10.0$ pF.

### 10.2 Slide in a slab

> [!easy] Easy · multiple choice · dielectric insertion · energy
> An air-filled parallel-plate capacitor, $C_0 = 1$ nF, is charged to $V_0 = 10$ V. A dielectric slab with $\epsilon_r = 4$ that exactly fills the gap is then slid all the way in. Ignore fringing.
>
> **(i)** The battery was disconnected *before* the slab went in. Which statement is **false**?
>
> (a) The voltage falls to 2.5 V.
>
> (b) $\mathbf{D}$ in the gap is unchanged.
>
> (c) The stored energy increases.
>
> (d) $\mathbf{E}$ in the gap falls to a quarter of its value.
>
> **(ii)** The battery stays connected while the slab goes in. Which statement is **false**?
>
> (a) The charge on the plates rises to 40 nC.
>
> (b) $\mathbf{E}$ in the gap is unchanged.
>
> (c) The stored energy becomes four times larger.
>
> (d) The battery supplies exactly the increase in stored energy.
>
> **(iii)** True or false: in case (ii) the stored energy goes up, so you have to push the slab in against an electric force.
>
> *Source: Lecture 10 slides, the fixed-charge/fixed-voltage challenge, extended to energy and force.*

> [!hint]- Hint
> First decide what is fixed: an isolated capacitor keeps its $Q$, a connected one keeps its $V$. The slab makes $C = 4C_0$, which fixes the other quantity; then use $W = Q^2/2C$ or $W = \tfrac12CV^2$, whichever contains the fixed one.

> [!solution]- Solution
> The slab fills the gap, so $C = \epsilon_rC_0 = 4$ nF. Initially $Q_0 = C_0V_0 = 10$ nC and $W_0 = \tfrac12C_0V_0^2 = 50$ nJ.
>
> **(i) $Q$ fixed.** $V = Q_0/C = V_0/4 = 2.5$ V, so (a) is true. $\mathbf{D}$ is set by the free charge alone ($D = \rho_s = Q_0/A$), so (b) is true. $E = V/d$ falls with $V$ to a quarter (equivalently $E = D/\epsilon$ with $\epsilon$ four times larger), so (d) is true. The energy $W = \dfrac{Q_0^2}{2C} = \dfrac{W_0}{4} = 12.5$ nJ *falls*: **(c) is false**. The missing 37.5 nJ is the work the field does on the slab as it pulls it in.
>
> **(ii) $V$ fixed.** $Q = CV_0 = 40$ nC, so (a) is true; $E = V_0/d$ is unchanged, so (b) is true; $W = \tfrac12CV_0^2 = 200$ nJ $= 4W_0$, so (c) is true. The battery moves $\Delta Q = 30$ nC through 10 V and supplies $V_0\,\Delta Q = 300$ nJ, but the stored energy rises by only 150 nJ: **(d) is false**. The other 150 nJ is again work done by the field on the slab.
>
> **(iii) False.** With the slab pushed in a distance $s$, $C(s)$ grows with $s$. The force pulling it further in is
> $$
> F = -\frac{\partial}{\partial s}\Big(\frac{Q^2}{2C}\Big)\Big|_Q = \frac{Q^2}{2C^2}\frac{dC}{ds}\qquad\text{or}\qquad F = +\frac{\partial}{\partial s}\Big(\tfrac12CV^2\Big)\Big|_V = \tfrac12V^2\frac{dC}{ds},
> $$
> the same expression (since $Q = CV$), and positive in both cases. Physically, the fringing field at the edge of the plates pulls on the polarized slab; the energy method finds that force without ever computing the fringing field. At fixed $V$ the stored energy rises only because the battery supplies twice the rise.
>
> **Watch out:** "the energy goes up, so I must do work" forgets the battery. $F = -dW/ds$ holds only for an isolated capacitor.
>
> **Answer.** (i) (c) is false (the energy falls from 50 nJ to 12.5 nJ); (ii) (d) is false (the battery supplies 300 nJ, the stored energy rises by 150 nJ); (iii) false: the slab is pulled in, with or without the battery.

### 10.3 Leakage of a long cable

> [!easy] Easy · conductance · coax · relaxation time
> A coaxial cable has capacitance $\mathcal{C} = 100$ pF/m. Its insulation has $\epsilon_r = 2.25$ and a tiny conductivity $\sigma = 1.0\times10^{-14}$ S/m.
> (a) Find the leakage conductance per unit length $\mathcal{G}$.
> (b) Find the leakage conductance $G$ and the insulation resistance $R$ between the conductors for a 1 km length and for a 2 km length.
> (c) A length of the cable is charged and then left with both ends open. Find the time constant of its self-discharge. Does it depend on the length?
>
> *Source: original.*

> [!hint]- Hint
> You never need the radii: $\mathcal{C}$ and $\mathcal{G}$ contain the same geometric factor. For (b), ask whether the leakage paths through different metres of the cable are in series or in parallel.

> [!solution]- Solution
> The insulation fills all the space between the conductors, so $\mathcal{C} = \epsilon\times\dfrac{2\pi}{\ln(b/a)}$ and $\mathcal{G} = \sigma\times\dfrac{2\pi}{\ln(b/a)}$ share the geometric factor, and $\mathcal{G} = (\sigma/\epsilon)\,\mathcal{C}$.
>
> **(a)** $\dfrac{\sigma}{\epsilon} = \dfrac{1.0\times10^{-14}}{2.25\epsilon_0}\approx5.02\times10^{-4}\ \text{s}^{-1}$, so $\mathcal{G}\approx(5.02\times10^{-4})(100\times10^{-12})\approx5.02\times10^{-14}$ S/m.
>
> **(b)** The leakage current flows *radially*, across the insulation, and every metre of cable offers its own path, in parallel with all the others: $G = \mathcal{G}\ell$ grows with length. For 1 km, $G\approx5.02\times10^{-11}$ S and $R = 1/G\approx19.92$ GΩ; for 2 km, $G\approx1.004\times10^{-10}$ S and $R\approx9.961$ GΩ.
>
> **(c)** With nothing connected, $C\,dV/dt = -GV$, so $V\propto e^{-t/\tau}$ with $\tau = C/G = \epsilon/\sigma\approx1992$ s $\approx33.2$ min. Both $C$ and $G$ are proportional to $\ell$, so $\tau$ does not depend on the length (nor on the radii).
>
> **Check:** for 1 km, $C = 100$ nF and $RC = (19.92\ \text{G}\Omega)(100\ \text{nF})\approx1992$ s ✓. And $\mathcal{C} = 2\pi\epsilon/\ln(b/a)$ says this cable has $\ln(b/a) = 1.2517$ ($b/a\approx3.496$); then $\mathcal{G} = 2\pi\sigma/\ln(b/a)$ gives the same $5.02\times10^{-14}$ S/m ✓.
>
> **Watch out:** a wire's resistance *along* its length grows with $\ell$; the insulation resistance *across* a cable falls as $1/\ell$.
>
> **Answer.** (a) $\mathcal{G}\approx5.02\times10^{-14}$ S/m; (b) 1 km: $G\approx5.02\times10^{-11}$ S, $R\approx19.92$ GΩ; 2 km: $G\approx1.004\times10^{-10}$ S, $R\approx9.961$ GΩ; (c) $\tau = \epsilon/\sigma\approx1992$ s $\approx33.2$ min, independent of the length.

### 10.4 Energy density in a dielectric

> [!easy] Easy · find the error · energy density
> A parallel-plate capacitor has square plates $20\ \text{cm}\times20\ \text{cm}$, $1$ mm apart, filled with a dielectric of $\epsilon_r = 5$, and is connected to a 50 V source. A student computes the stored energy:
>
> *"$E = V/d = 50/10^{-3} = 5\times10^4$ V/m. The energy density is $w = \tfrac12\epsilon_0E^2 = 0.0111$ J/m³ and the volume is $Ad = 4\times10^{-5}$ m³, so $W = wAd = 0.443\ \mu$J."*
>
> Find the error, correct the result, and confirm it with $\tfrac12CV^2$.
>
> *Source: original.*

> [!hint]- Hint
> Go through the student's steps one at a time and ask which of them would read exactly the same if the gap were empty. Should it?

> [!solution]- Solution
> **The slip:** in a dielectric the energy density is $w = \tfrac12\epsilon E^2 = \tfrac12\mathbf{D}\cdot\mathbf{E}$ with $\epsilon = \epsilon_r\epsilon_0$, not $\tfrac12\epsilon_0E^2$. The field also stores energy in the polarized material (the stretched dipoles), and $\tfrac12\epsilon_0E^2$ leaves that part out. The first step is fine: with the voltage fixed by the source, $E = V/d$ whatever fills the gap.
>
> **Corrected:**
> $$
> w = \tfrac12(5\epsilon_0)(5\times10^4)^2\approx0.0553\ \text{J/m}^3,\qquad W = wAd\approx2.21\ \mu\text{J}.
> $$
> **Check:** $C = \dfrac{\epsilon A}{d} = \dfrac{5\epsilon_0(0.04)}{10^{-3}} = 200\epsilon_0\approx1.771$ nF, and $\tfrac12CV^2 = \tfrac12(1.771\ \text{nF})(50\ \text{V})^2\approx2.21\ \mu$J ✓. The student's value is $1/\epsilon_r = 0.2$ of the true one.
>
> **Answer.** The energy density must be $\tfrac12\epsilon E^2$ with $\epsilon = 5\epsilon_0$, not $\tfrac12\epsilon_0E^2$: $w\approx0.0553$ J/m³ and $W\approx2.21\ \mu$J (not $0.443\ \mu$J).

### 10.5 Which capacitor leaks first

> [!easy] Easy · multiple choice · RC self-discharge
> Three capacitors use the same slightly conducting dielectric, $\epsilon = 2\epsilon_0$ and $\sigma = 1.0\times10^{-13}$ S/m, which fills all the space between their conductors: (1) parallel plates with $C = 1$ nF; (2) a coaxial cable 100 m long with $\mathcal{C} = 100$ pF/m; (3) a metal sphere of radius 1 m buried in an unbounded block of the material (the second conductor is at infinity). Each is charged and then left disconnected. Which one is the first to lose half of its charge?
>
> (a) The sphere, because its capacitance is by far the smallest.
>
> (b) The cable, because its leakage resistance is by far the smallest.
>
> (c) The parallel plates, because their charge has the shortest distance to travel.
>
> (d) All three at the same moment.
>
> (e) It cannot be decided without the plate spacing and the cable's radii.
>
> *Source: original, extending FA26 HW4 #4 (the lossy sphere) to three shapes.*

> [!hint]- Hint
> Write $Q(t)$ for an isolated leaky capacitor. Which combination of $R$ and $C$ sets the time scale, and what is it in terms of the geometric factor that $C$ and $G$ share?

> [!solution]- Solution
> **(d).** An isolated leaky capacitor obeys $C\,dV/dt = -GV$, so $Q(t) = Q(0)\,e^{-t/\tau}$ with $\tau = C/G = RC$. When one homogeneous material fills the field region, $C = \epsilon\times(\text{geometric factor})$ and $G = \sigma\times(\text{the same factor})$, so for every shape
> $$
> \tau = \frac{\epsilon}{\sigma} = \frac{2\epsilon_0}{10^{-13}}\approx177.1\ \text{s},\qquad t_{1/2} = \tau\ln2\approx122.7\ \text{s}.
> $$
> The individual numbers differ wildly but always pair up. Plates: $C = 1$ nF, $R\approx1.771\times10^{11}\ \Omega$. Cable: $C = 10$ nF, $R\approx1.771\times10^{10}\ \Omega$ (shells in series, $dR = dr/(\sigma\,2\pi r\ell)$). Sphere: $C = 4\pi\epsilon a = 8\pi\epsilon_0\approx222.5$ pF, $G = 4\pi\sigma a\approx1.257\times10^{-12}$ S, $R\approx7.958\times10^{11}\ \Omega$. Every product $RC\approx177.1$ s.
>
> - (a) The sphere has the smallest $C$, but also the largest $R$; the product is unchanged.
> - (b) The cable has the smallest $R$, but also the largest $C$.
> - (c) A shorter path raises $G$, but it raises $C$ by exactly the same factor.
> - (e) The geometric factor cancels in $C/G$, so no dimensions are needed.
>
> **Answer.** (d): all three lose half their charge after $t_{1/2} = (\epsilon/\sigma)\ln2\approx122.7$ s.

## Medium

### 10.6 Two layers between charged plates

> [!medium] Medium · layered dielectrics · series capacitance · energy
> Two large conducting plates lie on the planes $z = 0$ and $z = 3$ mm. The bottom plate carries $\rho_s = +4\times10^4\epsilon_0$ C/m² on its upper face; the top plate carries $-4\times10^4\epsilon_0$ C/m² on its lower face and is grounded, $V(3\ \text{mm}) = 0$. The layer $0<z<1$ mm is a dielectric with $\epsilon = 4\epsilon_0$; the rest of the gap, $1<z<3$ mm, is air.
> (a) Find $\mathbf{D}$, $\mathbf{E}$ and $\mathbf{P}$ in both layers.
> (b) Find $V(1\ \text{mm})$ and $V(0)$.
> (c) Find the capacitance per unit area $C/A$ from $Q/V$, and check it with the series formula.
> (d) Find the stored energy per unit area two ways, $\tfrac12(C/A)V^2$ and $\int\tfrac12\epsilon E^2\,dz$, and the fraction of it stored in the air.
>
> *Source: Summer 2020 HE2 #1a, re-parameterized (dielectric moved to the bottom layer, polarity reversed, energy added).*

> [!hint]- Hint
> The free charge alone fixes $\mathbf{D}$, and it is the same in both layers; the layers only decide how $\mathbf{D}$ turns into $\mathbf{E}$. For the potential, integrate $E_z$ down from the grounded plate.

> [!solution]- Solution
> **Setup.** Everything depends on $z$ only and the gap holds no free charge, so $D_z$ is the same in both layers. At the bottom plate $\hat{n} = +\hat{z}$ points out of the metal, and $\rho_s = \hat{z}\cdot\mathbf{D}$.
>
> **(a)** $\mathbf{D} = 4\times10^4\epsilon_0\,\hat{z}\approx3.54\times10^{-7}\,\hat{z}$ C/m² in both layers. Then $\mathbf{E} = \mathbf{D}/\epsilon$ and $\mathbf{P} = \mathbf{D}-\epsilon_0\mathbf{E}$:
> $$
> \begin{aligned}
> 0<z<1\ \text{mm}:&\quad \mathbf{E}_1 = 10^4\,\hat{z}\ \text{V/m}, && \mathbf{P}_1 = 3\times10^4\epsilon_0\,\hat{z}\approx0.266\,\hat{z}\ \mu\text{C/m}^2\\
> 1<z<3\ \text{mm}:&\quad \mathbf{E}_2 = 4\times10^4\,\hat{z}\ \text{V/m}, && \mathbf{P}_2 = 0
> \end{aligned}
> $$
> **(b)** From $V(b)-V(a) = -\int_a^b\mathbf{E}\cdot d\mathbf{l}$, $V(z) = V(3\ \text{mm})+\int_z^{3\,\text{mm}}E_z\,dz$. Through the air: $V(1\ \text{mm}) = (4\times10^4)(2\times10^{-3}) = 80$ V. Through the dielectric: $V(0) = 80+(10^4)(10^{-3}) = 90$ V.
>
> **(c)** The positive plate holds $\rho_s$ per unit area and sits $V = 90$ V above the negative one:
> $$
> \frac CA = \frac{\rho_s}{V} = \frac{4\times10^4\epsilon_0}{90} = \frac{4000}{9}\epsilon_0\approx3.935\ \text{nF/m}^2.
> $$
> The layers are crossed in succession ($\mathbf{D}$ common), so they add in series: $\dfrac AC = \dfrac{d_1}{\epsilon_1}+\dfrac{d_2}{\epsilon_2} = \dfrac{(0.25+2)\ \text{mm}}{\epsilon_0}$, so $C/A = \epsilon_0/(0.00225\ \text{m})\approx444.4\epsilon_0$ ✓.
>
> **(d)** $\tfrac12\dfrac CAV^2 = \tfrac12\cdot\dfrac{4000}{9}\epsilon_0\cdot90^2 = 1.8\times10^6\epsilon_0\approx15.94\ \mu$J/m². Layer by layer, $\int\tfrac12\epsilon E^2\,dz$ gives
> $$
> \tfrac12(4\epsilon_0)(10^4)^2(10^{-3}) = 2\times10^5\epsilon_0\approx1.771\ \mu\text{J/m}^2,\qquad \tfrac12\epsilon_0(4\times10^4)^2(2\times10^{-3}) = 1.6\times10^6\epsilon_0\approx14.17\ \mu\text{J/m}^2,
> $$
> which add up to $1.8\times10^6\epsilon_0$ ✓. The air holds $8/9\approx0.889$ of the energy. That is no accident: with $\mathbf{D}$ common, each layer stores $\tfrac12DV_i$ per unit area, so the energy splits exactly like the voltage, 80 V out of 90 V.
>
> **Check:** at the top plate $\hat{n} = -\hat{z}$ points out of the metal, so $\rho_s = -\hat{z}\cdot\mathbf{D} = -4\times10^4\epsilon_0$ ✓, the given charge. The dielectric's faces carry bound charge $\rho_{sb} = \mathbf{P}_1\cdot\hat{n}$: $-3\times10^4\epsilon_0$ at the bottom and $+3\times10^4\epsilon_0$ at the top. The jump of $\epsilon_0E_z$ at $z = 1$ mm, $\epsilon_0(4\times10^4-10^4) = 3\times10^4\epsilon_0$, is exactly that bound sheet ✓.
>
> **Watch out:** $E$ is largest in the *low*-$\epsilon$ layer. The thin dielectric takes only 10 V of the 90 V; a dielectric layer in series with an air gap raises $C$ only modestly.
>
> **Answer.** (a) $\mathbf{D} = 4\times10^4\epsilon_0\hat{z}\approx3.54\times10^{-7}\hat{z}$ C/m² in both layers; $\mathbf{E}_1 = 10^4\hat{z}$ V/m, $\mathbf{E}_2 = 4\times10^4\hat{z}$ V/m; $\mathbf{P}_1 = 3\times10^4\epsilon_0\hat{z}\approx0.266\hat{z}\ \mu$C/m², $\mathbf{P}_2 = 0$. (b) $V(1\ \text{mm}) = 80$ V, $V(0) = 90$ V. (c) $C/A = (4000/9)\epsilon_0\approx3.935$ nF/m². (d) $W/A = 1.8\times10^6\epsilon_0\approx15.94\ \mu$J/m², $8/9$ of it in the air.

### 10.7 One slab, two placements

> [!medium] Medium · series and parallel · layered dielectrics
> An air-filled parallel-plate capacitor has plates of area $A = 100$ cm² a distance $d = 2$ mm apart; call its capacitance $C_0$. You have one dielectric slab ($\epsilon_r = 3$) whose volume is half that of the gap, and two ways to place it:
> **S (stacked):** thickness $d/2$, covering the whole plate area, lying on the lower plate;
> **P (side by side):** full thickness $d$, covering half of the plate area.
> (a) Find $C_S$ and $C_P$ as multiples of $C_0$, and in pF.
> (b) Show that $C_P\ge C_S$ for every $\epsilon_r\ge1$. When are they equal?
> (c) With 100 V across the plates, find $E$ in the dielectric and in the air for each placement, and compare with the empty capacitor.
> (d) The same contest in a coax: a cable with $a = 1$ mm and $b = 4$ mm has the $\epsilon_r = 3$ dielectric filling the half $0<\phi<\pi$ of the space between the conductors, and air in the other half. Find $\mathcal{C}$, and the ratio of the surface charge densities on the inner conductor under the dielectric and under the air.
>
> *Source: classic, new numbers; part (d) from Lecture 10, section 4.*

> [!hint]- Hint
> Look at each dielectric–air interface. Does the field cross it or run along it? Which boundary condition then makes $\mathbf{D}$, or $\mathbf{E}$, the same on both sides, and does that put the two regions in series or in parallel?

> [!solution]- Solution
> **Setup.** $C_0 = \epsilon_0A/d = 5\epsilon_0\approx44.27$ pF. The only modelling decision is which field quantity the dielectric–air interface makes common.
>
> **(a)** *Stacked.* The field crosses the interface $z = d/2$, which carries no free charge, so $D_n$ is continuous: $\mathbf{D}$ is common and the voltage drops add, a **series** connection:
> $$
> \frac1{C_S} = \frac{d/2}{\epsilon_r\epsilon_0A}+\frac{d/2}{\epsilon_0A}\ \Rightarrow\ C_S = \frac{2\epsilon_r}{1+\epsilon_r}C_0 = 1.5\,C_0\approx66.41\ \text{pF}.
> $$
> *Side by side.* The interface is perpendicular to the plates, so the field runs along it; $E_t$ is continuous, $E = V/d$ is common and the charges add, a **parallel** connection:
> $$
> C_P = \frac{\epsilon_r\epsilon_0(A/2)}{d}+\frac{\epsilon_0(A/2)}{d} = \frac{1+\epsilon_r}{2}C_0 = 2\,C_0\approx88.54\ \text{pF}.
> $$
> **(b)**
> $$
> C_P-C_S = C_0\Big[\frac{1+\epsilon_r}{2}-\frac{2\epsilon_r}{1+\epsilon_r}\Big] = C_0\,\frac{(\epsilon_r-1)^2}{2(1+\epsilon_r)}\ \ge0,
> $$
> zero only for $\epsilon_r = 1$ (no dielectric at all); here the difference is $0.5\,C_0$. In words: the parallel placement gives the arithmetic mean of 1 and $\epsilon_r$, the series placement the harmonic mean, which is never larger. The gap grows fast: for $\epsilon_r = 81$, $C_S\approx1.976\,C_0$ (the air layer in series keeps it below $2C_0$) while $C_P = 41\,C_0$.
>
> **(c)** *Stacked:* $Q = C_SV = 6.64$ nC, $D = Q/A\approx6.64\times10^{-7}$ C/m² in both layers, so $E = D/(3\epsilon_0) = 25$ kV/m in the dielectric and $E = D/\epsilon_0 = 75$ kV/m in the air; check: $25\ \text{V}+75\ \text{V} = 100$ V ✓. *Side by side:* $E = V/d = 50$ kV/m in both halves; the plate charge density $\rho_s = \epsilon E$ is $1.33\ \mu$C/m² against the dielectric and $0.443\ \mu$C/m² against the air. The empty capacitor has 50 kV/m. So the stacked slab *raises* the field in the remaining air by half, from 50 to 75 kV/m, because the air must now hold 75 V across half the gap; the side-by-side slab leaves $E$ alone and only adds charge.
>
> **(d)** The interfaces $\phi = 0$ and $\phi = \pi$ contain the radial direction, so a radial $\mathbf{E}$ runs along them: $\mathbf{E}$ is common, $V = V_0\ln(b/r)/\ln(b/a)$ in both halves, and the halves are in parallel. Each half is half of a fully filled cable:
> $$
> \mathcal{C} = \frac{\pi\epsilon_1}{\ln(b/a)}+\frac{\pi\epsilon_2}{\ln(b/a)} = \frac{\pi(3\epsilon_0+\epsilon_0)}{\ln4} = \frac{4\pi\epsilon_0}{\ln4}\approx80.3\ \text{pF/m}.
> $$
> On the inner conductor $\rho_s = \epsilon E_r(a)$ with the same $E_r(a)$ under both halves, so the ratio is $3:1$: the charge crowds toward the dielectric.
>
> **Check:** in every common-$\mathbf{E}$ case, $\mathbf{D}$ is tangential to the interface, so $D_n = 0$ on both sides, as it must be with no free charge there; in the stacked case $\mathbf{E}$ has no tangential component, so $E_t$ is trivially continuous ✓.
>
> **Answer.** (a) $C_S = 1.5C_0\approx66.41$ pF, $C_P = 2C_0\approx88.54$ pF ($C_0 = 5\epsilon_0\approx44.27$ pF). (b) $C_P-C_S = C_0(\epsilon_r-1)^2/[2(1+\epsilon_r)]\ge0$, equal only for $\epsilon_r = 1$. (c) Stacked: 25 kV/m in the dielectric, 75 kV/m in the air; side by side: 50 kV/m everywhere, the same as the empty capacitor. (d) $\mathcal{C} = 4\pi\epsilon_0/\ln4\approx80.3$ pF/m; ratio $3:1$.

### 10.8 Diode junction capacitance

> [!medium] Medium · diode · small-signal capacitance
> An abrupt silicon pn junction ($\epsilon = 11.7\epsilon_0$) has area $A = 1$ mm². The p side ($x<0$) has $N_A = 10^{23}$ m⁻³ acceptors and the n side ($x>0$) has $N_D = 10^{22}$ m⁻³ donors. In the depletion approximation the layer $-W_1<x<0$ carries $\rho = -eN_A$ and the layer $0<x<W_2$ carries $\rho = +eN_D$; write $\rho_1 = eN_A$ and $\rho_2 = eN_D$ for the magnitudes, and let $V = V(W_2)-V(-W_1)$ be the total potential difference across the depletion region.
> (a) For $V = 1$ V find $W_1+W_2$, $W_1$ and $W_2$. Which side holds most of the depletion region?
> (b) Find the charge $Q = \rho_2W_2A$ on each side and the small-signal capacitance $C = dQ/dV$ at $V = 1$ V.
> (c) Repeat for $V = 4$ V. How does $C$ scale with $V$?
> (d) A classmate takes $C = Q/V$. What does that give at 1 V, and why is it wrong here?
>
> *Source: course notes, Lecture 10 (junction capacitance), silicon numbers.*

> [!hint]- Hint
> Neutrality, $\rho_1W_1 = \rho_2W_2$, fixes the ratio of the two widths; the voltage across the triangle-shaped field profile fixes their sum. For $C$, differentiate $Q(V)$ rather than dividing.

> [!solution]- Solution
> **Setup.** Poisson's equation ([[1-electrostatics/07-poisson-and-laplace|Lecture 7]]) gives a field that vanishes at both edges of the depletion region and peaks in magnitude at $x = 0$, where $\lvert E\rvert = \rho_1W_1/\epsilon = \rho_2W_2/\epsilon$, equal because the region is neutral. The drop is the area of that triangle, $V = \rho_2W_2(W_1+W_2)/(2\epsilon)$. Eliminating $W_2$ with $\rho_1W_1 = \rho_2W_2$:
> $$
> W_1+W_2 = \sqrt{2\epsilon V\Big(\frac1{\rho_1}+\frac1{\rho_2}\Big)}.
> $$
> **(a)** $\rho_1 = eN_A\approx1.602\times10^4$ C/m³, $\rho_2 = eN_D\approx1602$ C/m³, $1/\rho_1+1/\rho_2\approx6.87\times10^{-4}$ m³/C and $\epsilon\approx1.036\times10^{-10}$ F/m, so at 1 V, $W_1+W_2\approx0.3772\ \mu$m. Neutrality gives $W_1/W_2 = \rho_2/\rho_1 = 0.1$, so $W_2 = \tfrac{10}{11}(W_1+W_2)\approx0.343\ \mu$m and $W_1\approx0.0343\ \mu$m. The depletion region lies almost entirely ($10/11\approx0.909$) on the lightly doped n side: with fewer charges per unit volume, a wider layer is needed to hold the same charge.
>
> **(b)** $Q = \rho_2W_2A = (1602)(0.343\times10^{-6})(10^{-6})\approx0.549$ nC. Since $W_2\propto\sqrt V$, $Q\propto\sqrt V$ and $dQ/dV = Q/(2V)$:
> $$
> C = \frac{dQ}{dV} = A\sqrt{\frac{\epsilon\rho_1\rho_2}{2V(\rho_1+\rho_2)}} = \frac{\epsilon A}{W_1+W_2}\approx274.7\ \text{pF}.
> $$
> **(c)** At 4 V the width doubles: $W_1+W_2\approx0.7543\ \mu$m ($W_1\approx0.0686\ \mu$m, $W_2\approx0.686\ \mu$m), $Q\approx1.10$ nC, and $C = \epsilon A/(W_1+W_2)\approx137.3$ pF, half the 1 V value: $C\propto V^{-1/2}$. This is how a varactor diode works as a voltage-controlled capacitor.
>
> **(d)** $Q/V\approx549.3$ pF at 1 V, exactly twice the slope. A small signal $\delta V$ on top of the bias moves the charge by $\delta Q = (dQ/dV)\,\delta V$, so the slope is what a circuit sees; the secant $Q/V$ equals the slope only for a linear capacitor.
>
> **Check:** $C = \epsilon A/(W_1+W_2)$ is the parallel-plate formula with the depletion width as the gap, and at 1 V it gives $(1.036\times10^{-10})(10^{-6})/(0.3772\times10^{-6})\approx274.7$ pF, the same as the slope ✓.
>
> **Watch out:** in silicon use $\epsilon = 11.7\epsilon_0$; the lecture writes the junction formulas with $\epsilon_0$.
>
> **Answer.** (a) $W_1+W_2\approx0.3772\ \mu$m, $W_1\approx0.0343\ \mu$m, $W_2\approx0.343\ \mu$m (10/11 of it on the n side). (b) $Q\approx0.549$ nC, $C\approx274.7$ pF. (c) $W_1+W_2\approx0.7543\ \mu$m, $Q\approx1.10$ nC, $C\approx137.3$ pF: $C\propto V^{-1/2}$. (d) $Q/V\approx549.3$ pF, twice the small-signal $C$.

## Hard

### 10.9 Leaky spheres, one lossy half

> [!hard] Hard · conductance · spheres · relaxation time
> Two concentric, perfectly conducting spheres: the inner one, of radius $a = 1$ cm, is grounded, $V(a) = 0$; the outer shell, of radius $b = 2$ cm, is held at $V(b) = -V_0 = -100$ V by a source. The region $a<r<b$ is filled with a material of permittivity $\epsilon = 3\epsilon_0$ throughout. Its lower half ($z<0$) is also slightly conducting, $\sigma = 1.0\times10^{-8}$ S/m; its upper half ($z>0$) is a perfect insulator. Treat the two spheres as a stand-alone capacitor: no charge sits on the outer surface of the shell, so there is no field outside it.
> (a) True or false, with a reason: (i) the inner sphere carries positive charge; (ii) only the lower half conducts, so the charge on the inner sphere sits on its lower hemisphere.
> (b) Find $V(r)$ and $\mathbf{E}$ for $a<r<b$, and show that this field meets every condition, including those on the plane $z = 0$ where the two halves meet. Find the capacitance $C$ and the charge on each conductor.
> (c) Find the steady leakage current (magnitude and direction), the conductance $G$, the resistance and the power dissipated. Compare $G$ with $(\sigma/\epsilon)C$ and explain the difference.
> (d) The source is disconnected, leaving the outer shell isolated. Find the time constant of the decay of $V(b)$ and the time it takes to reach $-50$ V. Why is it not $\epsilon/\sigma$?
>
> *Source: SP18 Exam 1 #5, re-parameterized and extended (polarity reversed, lossy lower half only, discharge time).*

> [!hint]- Hint
> On the plane $z = 0$ a radial vector lies *in* the plane. So a radial $\mathbf{E}$ is tangential there, and a radial $\mathbf{J}$ never crosses the plane. The field is then the ordinary concentric-sphere field, but current flows only through the lower hemisphere.

> [!solution]- Solution
> **(a)** (i) **True.** $V(a) = 0$ is higher than $V(b) = -100$ V, and $\mathbf{E}$ points from high to low potential, here outward ($+\hat{r}$). On the inner sphere $\hat{n} = +\hat{r}$ points out of the metal, so $\rho_s = \hat{r}\cdot\mathbf{D} = \epsilon E_r(a)>0$: the inner sphere carries $+Q$ and the outer shell $-Q$. Grounding fixes the potential, not the charge: the ground wire supplies whatever charge keeps $V(a) = 0$.
> (ii) **False.** The charge follows $\mathbf{D}$, not the current. $\epsilon$ is the same in both halves and, as (b) shows, so is the radial field; hence $\rho_s = \epsilon E_r(a) = 6\times10^4\epsilon_0\approx0.531\ \mu\text{C/m}^2$ all over the inner sphere. The conductivity only decides where current flows: in the upper half $\mathbf{J} = 0$ although $\mathbf{E}\ne0$.
>
> **(b) Setup.** Try a potential that depends on $r$ only. In each half, $V = A-B/r$ solves Laplace's equation $\dfrac1{r^2}\dfrac{d}{dr}\Big(r^2\dfrac{dV}{dr}\Big) = 0$; matching $V(a) = 0$ and $V(b) = -V_0$,
> $$
> V(r) = -V_0\,\frac{1/a-1/r}{1/a-1/b} = -200+\frac{2}{r}\ \text{V},\qquad \mathbf{E} = -\frac{dV}{dr}\hat{r} = \frac{V_0ab}{(b-a)r^2}\hat{r} = \frac{2}{r^2}\hat{r}\ \text{V/m}\quad(r\text{ in m}),
> $$
> so $E_r(a) = 2\times10^4$ V/m and $E_r(b) = 5\times10^3$ V/m: outward, from the positive sphere to the negative shell. On the plane $z = 0$ (normal $\hat{z}$), $\hat{r}$ lies in the plane, so $\mathbf{E}$ is purely tangential and the same on both sides ($E_t$ continuous ✓), and $D_z = J_z = 0$ on both sides: no interface charge is needed, and no current crosses the plane, so none ever accumulates there ✓. Both conductors are equipotentials ✓. By uniqueness this is the field, exactly as if the whole region were insulating. Since $\epsilon$ is the same everywhere,
> $$
> C = 4\pi\epsilon\frac{ab}{b-a} = 4\pi(3\epsilon_0)(0.02\ \text{m})\approx6.676\ \text{pF},\qquad Q = CV_0\approx667.6\ \text{pC},
> $$
> with $+667.6$ pC on the inner sphere and $-667.6$ pC on the outer shell. (Gauss's law on a sphere $a<r<b$: $\oint\mathbf{D}\cdot d\mathbf{S} = 4\pi r^2\epsilon E_r = +Q$ ✓, the inner sphere's charge.)
>
> **(c)** In the lower half $\mathbf{J} = \sigma\mathbf{E}$; in the upper half $\mathbf{J} = 0$. Through the lower hemisphere of any radius $r$ (outward normal $\hat{r}$, area $2\pi r^2$):
> $$
> I_{\text{out}} = \sigma E_r\cdot2\pi r^2 = 2\pi\sigma\frac{abV_0}{b-a}\approx125.7\ \text{nA},
> $$
> the same at every $r$ (steady current, $\nabla\cdot\mathbf{J} = 0$). So 125.7 nA flows *outward*, from the inner sphere through the lossy half into the outer shell; the ground wire feeds the inner sphere and the source drains the shell. Then
> $$
> G = \frac{125.7\ \text{nA}}{100\ \text{V}} = 2\pi\sigma\frac{ab}{b-a}\approx1.257\ \text{nS},\qquad R = \frac1G\approx795.8\ \text{M}\Omega,\qquad P = GV_0^2\approx12.57\ \mu\text{W}.
> $$
> Compare $(\sigma/\epsilon)C\approx2.513$ nS, twice as much. The rule $G = (\sigma/\epsilon)C$ needs $\sigma$ and $\epsilon$ to fill the *same* region: here $C$ gets the full geometric factor $4\pi ab/(b-a)$ (dielectric everywhere) but $G$ only half of it (conducting half only), so $G = \tfrac12(\sigma/\epsilon)C$.
>
> **(d)** With the source gone, the shell's charge leaks through $G$: $C\,dV/dt = -GV$, so $V(b) = -V_0e^{-t/\tau}$ with
> $$
> \tau = \frac CG = \frac{2\epsilon}{\sigma}\approx5.313\ \text{ms},\qquad t_{1/2} = \tau\ln2\approx3.682\ \text{ms}.
> $$
> The material's own relaxation time is $\epsilon/\sigma\approx2.656$ ms, half of $\tau$: the whole dielectric stores the field, but only half of it can drain the charge. (During the decay the field keeps its radial shape; the argument of (b) holds at every instant.) Only $C$ enters because the shell's outer surface carries no charge, as stated; if the shell also faced a distant ground at 0 V, its capacitance $4\pi\epsilon_0b\approx2.225$ pF to that ground would add to $C$ and give $\tau\approx7.08$ ms.
>
> **Check:** $\tau = RC = (795.8\ \text{M}\Omega)(6.676\ \text{pF})\approx5.313$ ms ✓, and $P = GV_0^2$ is also $IV_0 = (125.7\ \text{nA})(100\ \text{V})\approx12.57\ \mu$W ✓.
>
> **Watch out:** "the field is spherically symmetric, so the current is too" is wrong: $\mathbf{E}$ is symmetric, but $\mathbf{J} = \sigma\mathbf{E}$ exists only where $\sigma\ne0$.
>
> **Answer.** (a) (i) True: the grounded inner sphere carries $+Q$; (ii) false: $\rho_s = \epsilon E_r(a)\approx0.531\ \mu$C/m² is uniform over the inner sphere. (b) $V = -200+2/r$ V and $\mathbf{E} = (2/r^2)\hat{r}$ V/m ($r$ in m; $2\times10^4$ V/m at $a$, $5\times10^3$ V/m at $b$, outward); $C\approx6.676$ pF; $+667.6$ pC on the inner sphere, $-667.6$ pC on the shell. (c) 125.7 nA, outward (from the inner sphere to the shell); $G\approx1.257$ nS $= \tfrac12(\sigma/\epsilon)C$, $R\approx795.8$ MΩ, $P\approx12.57\ \mu$W. (d) $\tau = 2\epsilon/\sigma\approx5.313$ ms; $V(b)$ reaches $-50$ V after $t_{1/2}\approx3.682$ ms.

### 10.10 Pulling capacitor plates apart

> [!hard] Hard · energy · force · fixed charge vs fixed voltage
> Two square plates of area $A = 0.02$ m² face each other in air. The lower plate is fixed on $z = 0$ and grounded; the upper plate, at height $z = x$, can be moved and is connected to the + terminal of a 500 V battery. Initially $x = x_1 = 1$ mm. Ignore fringing.
> (a) Find $C$, $Q$ and the stored energy $W$ at $x_1$.
> (b) The battery is disconnected, and you slowly pull the upper plate up to $x_2 = 3$ mm. Find the new voltage and stored energy, the work you do, and the electric force on the upper plate (magnitude and direction). Confirm the force a second way, from the charge on the upper plate and the field it sits in.
> (c) Start again from (a), but this time the battery stays connected while you pull from $x_1$ to $x_2$. Find the final $C$, $Q$ and $W$, the charge returned to the battery, the work done by the battery and the work done by you.
> (d) In case (c), find the force on the upper plate at $x_1$ and at $x_2$. Why is the force at $x_1$ the same as in (b)?
>
> *Source: classic, new numbers.*

> [!hint]- Hint
> Write the stored energy as a function of $x$ in each case. Isolated plates: $W = Q^2/2C(x)$, and energy conservation is simply (your work) $= \Delta W$. Battery connected: the battery's work $V_0\,\Delta Q$ belongs in the energy balance too.

> [!solution]- Solution
> **(a)** $C = \dfrac{\epsilon_0A}{x_1} = 20\epsilon_0\approx177.1$ pF, $Q = CV_0 = 10^4\epsilon_0\approx88.54$ nC, $W = \tfrac12CV_0^2 = 2.5\times10^6\epsilon_0\approx22.14\ \mu$J.
>
> **(b) Fixed $Q$.** $W(x) = \dfrac{Q^2}{2C(x)} = \dfrac{Q^2x}{2\epsilon_0A}$ grows linearly with $x$. At $x_2 = 3x_1$: $V = Q/C(x_2) = 3V_0 = 1500$ V and $W = 66.41\ \mu$J. With no battery, your work is the whole increase, $66.41-22.14 = 44.27\ \mu$J.
> The force of the field on the upper plate is
> $$
> F_z = -\frac{dW}{dx}\Big|_Q = -\frac{Q^2}{2\epsilon_0A} = -\frac{W(x_1)}{x_1}\approx-22.14\ \text{mN},
> $$
> downward (attractive) and independent of $x$. Pulling against a constant 22.14 mN through 2 mm costs $44.27\ \mu$J ✓.
> *Second way:* the lower plate carries $-Q$, i.e. $\rho_s = -Q/A$, and the field of that sheet alone above it is $\dfrac{\rho_s}{2\epsilon_0}\hat{z} = -\dfrac{Q}{2\epsilon_0A}\hat{z}$. The upper plate's charge $+Q$ sits in that field: $F_z = -\dfrac{Q^2}{2\epsilon_0A}$ ✓.
>
> **(c) Fixed $V$.** $C(x_2) = \epsilon_0A/x_2\approx59.03$ pF, $Q_2 = C(x_2)V_0\approx29.51$ nC, $W_2 = \tfrac12C(x_2)V_0^2\approx7.378\ \mu$J. Now the stored energy *falls*, $\Delta W\approx-14.76\ \mu$J, and $\Delta Q\approx-59.03$ nC flows back into the battery, which therefore does work $V_0\,\Delta Q\approx-29.51\ \mu$J: it *absorbs* $29.51\ \mu$J (it is being charged). Energy conservation, (your work) + (battery's work) $= \Delta W$, with $V_0\,\Delta Q = 2\Delta W$ exactly (both are proportional to $\Delta C$):
> $$
> W_{\text{you}} = \Delta W-V_0\,\Delta Q = -\Delta W\approx14.76\ \mu\text{J}.
> $$
> So the battery absorbs twice the drop in stored energy: one share from the field, one share from you.
>
> **(d)** With $V$ fixed, the balance $F_{\text{you}}\,dx+V_0\,dQ = dW$ with $V_0\,dQ = 2\,dW$ gives $F_{\text{you}} = -dW/dx$, so the field's force is
> $$
> F_z = +\frac{dW}{dx}\Big|_V = -\frac{\epsilon_0AV_0^2}{2x^2}:\qquad F_z(x_1)\approx-22.14\ \text{mN},\qquad F_z(x_2)\approx-2.459\ \text{mN}.
> $$
> At $x_1$ the plates hold the same charge, hence the same field, as at the start of (b): the force depends only on the present state, not on what is connected to the plates, and the two energy recipes ($-dW/dx$ at fixed $Q$, $+dW/dx$ at fixed $V$) are two ways of computing the same thing. As the plates separate the charge drains back into the battery and the force weakens as $1/x^2$, whereas at fixed $Q$ it stays at 22.14 mN.
>
> **Check:** $\displaystyle\int_{x_1}^{x_2}\frac{\epsilon_0AV_0^2}{2x^2}\,dx = \tfrac12C(x_1)V_0^2-\tfrac12C(x_2)V_0^2 = 22.14-7.378\approx14.76\ \mu$J, your work in (c) ✓.
>
> **Watch out:** using the full gap field $Q/(\epsilon_0A)$ for the force gives 44.27 mN, twice too much: a plate is not pushed by its own field, only by the other plate's.
>
> **Answer.** (a) $C = 20\epsilon_0\approx177.1$ pF, $Q = 10^4\epsilon_0\approx88.54$ nC, $W\approx22.14\ \mu$J. (b) $V = 1500$ V, $W\approx66.41\ \mu$J, your work $\approx44.27\ \mu$J; $F_z\approx-22.14$ mN (attractive, constant). (c) $C\approx59.03$ pF, $Q\approx29.51$ nC, $W\approx7.378\ \mu$J; 59.03 nC returns to the battery, which absorbs $29.51\ \mu$J; your work $\approx14.76\ \mu$J. (d) $-22.14$ mN at $x_1$ (the same state as in (b)), $-2.459$ mN at $x_2$.

### 10.11 Two lossy layers in series

> [!hard] Hard · conductance · interface charge · transients
> Large parallel plates of area $A = 0.01$ m² lie on $z = 0$ and $z = 2$ mm. The gap holds two imperfect dielectrics: layer 1 ($0<z<1$ mm) with $\epsilon_1 = 2\epsilon_0$ and $\sigma_1 = 4\times10^{-10}$ S/m, and layer 2 ($1<z<2$ mm) with $\epsilon_2 = 4\epsilon_0$ and $\sigma_2 = 1\times10^{-10}$ S/m. At $t = 0$ a battery is connected that holds the lower plate at $V_0 = 10$ V and the upper plate at 0. Ignore fringing.
> (a) In the steady state, find the current $I$, the current density $\mathbf{J}$, the fields $\mathbf{E}_1$ and $\mathbf{E}_2$, and the voltage across each layer.
> (b) Still in the steady state, find $\mathbf{D}$ in each layer and the free surface charge density on the lower plate, on the upper plate and on the interface $z = 1$ mm. Check the total.
> (c) Just after the switch ($t = 0^+$) the interface is still uncharged. Find $\mathbf{E}_1$, $\mathbf{E}_2$ and the voltage $V_1$ across layer 1 at $t = 0^+$. Then use charge conservation at the interface to find $V_1(t)$ and its time constant.
> (d) Show that the steady conductance is not $(\sigma/\epsilon)C$ for either layer's $\sigma/\epsilon$. What condition on the materials would make the interface charge, and the transient, disappear?
>
> *Source: classic (the two-layer lossy capacitor), new numbers.*

> [!hint]- Hint
> Steady means nothing changes, so the same $J$ must cross both layers: they act as resistors in series. At $t = 0^+$ no charge has reached the interface yet, so $D_z$ is continuous there instead: capacitors in series. In between, the interface charge grows at the rate $J_1-J_2$.

> [!solution]- Solution
> **(a) Steady state.** Nothing changes, so the current density arriving at the interface equals the one leaving it: $J_1 = J_2 = J$. The layers are resistors in series, $R_i = d_i/(\sigma_iA)$:
> $$
> R_1 = 0.25\ \text{G}\Omega,\quad R_2 = 1\ \text{G}\Omega,\quad I = \frac{V_0}{R_1+R_2} = \frac{10\ \text{V}}{1.25\ \text{G}\Omega} = 8\ \text{nA},\quad J = \frac IA = 8\times10^{-7}\ \text{A/m}^2.
> $$
> $\mathbf{J}$ points along $+\hat{z}$, from the 10 V plate to the grounded one. $\mathbf{E}_1 = \mathbf{J}/\sigma_1 = 2000\,\hat{z}$ V/m and $\mathbf{E}_2 = \mathbf{J}/\sigma_2 = 8000\,\hat{z}$ V/m, so layer 1 holds 2 V and layer 2 holds 8 V: a resistive divider.
>
> **(b)** $\mathbf{D}_1 = \epsilon_1\mathbf{E}_1 = 4000\epsilon_0\hat{z}\approx3.54\times10^{-8}\hat{z}$ C/m² and $\mathbf{D}_2 = \epsilon_2\mathbf{E}_2 = 32000\epsilon_0\hat{z}\approx2.83\times10^{-7}\hat{z}$ C/m², so $\mathbf{D}$ is *not* continuous. With $\hat{n}$ pointing from medium 2 into medium 1 ($\hat{n} = -\hat{z}$), the interface carries
> $$
> \rho_s = \hat{n}\cdot(\mathbf{D}_1-\mathbf{D}_2) = D_2-D_1 = 28000\epsilon_0\approx2.48\times10^{-7}\ \text{C/m}^2 = J\Big(\frac{\epsilon_2}{\sigma_2}-\frac{\epsilon_1}{\sigma_1}\Big).
> $$
> Lower plate ($\hat{n} = +\hat{z}$ out of the metal): $\rho_s = D_1 = +4000\epsilon_0$. Upper plate ($\hat{n} = -\hat{z}$): $\rho_s = -D_2 = -32000\epsilon_0$. Total: $(4000+28000-32000)\epsilon_0 = 0$ ✓. The plates no longer carry equal and opposite charges; the difference sits on the interface.
>
> **(c) At $t = 0^+$** the currents are finite, so no charge has had time to collect on the interface: $\epsilon_1E_1 = \epsilon_2E_2$, i.e. $E_1 = 2E_2$. With $E_1d_1+E_2d_2 = V_0$ this gives $E_1(0^+)\approx6667$ V/m, $E_2(0^+)\approx3333$ V/m and $V_1(0^+)\approx6.667$ V, a capacitive divider, $V_1(0^+) = \dfrac{C_2}{C_1+C_2}V_0$ with $C_i = \epsilon_iA/d_i$. Now $J_1 = \sigma_1E_1\approx2.667\ \mu$A/m² arrives at the interface but only $J_2 = \sigma_2E_2\approx0.3333\ \mu$A/m² leaves, so positive charge builds up there, heading for the $+28000\epsilon_0$ of (b).
> *Transient.* Charge conservation at the interface, plus the two field conditions:
> $$
> \frac{d\rho_s}{dt} = \sigma_1E_1-\sigma_2E_2,\qquad \rho_s = \epsilon_2E_2-\epsilon_1E_1,\qquad E_1d_1+E_2d_2 = V_0.
> $$
> Eliminating $\rho_s$ and $E_2$ in favour of $V_1 = E_1d_1$:
> $$
> \Big(\frac{\epsilon_1}{d_1}+\frac{\epsilon_2}{d_2}\Big)\frac{dV_1}{dt}+\Big(\frac{\sigma_1}{d_1}+\frac{\sigma_2}{d_2}\Big)V_1 = \frac{\sigma_2}{d_2}V_0,
> $$
> a first-order equation with time constant (here $d_1 = d_2$)
> $$
> \tau = \frac{\epsilon_1/d_1+\epsilon_2/d_2}{\sigma_1/d_1+\sigma_2/d_2} = \frac{C_1+C_2}{G_1+G_2} = \frac{(2+4)\epsilon_0}{(4+1)\times10^{-10}\ \text{S/m}}\approx0.1063\ \text{s},
> $$
> where $G_i = \sigma_iA/d_i$. Its solution runs from the capacitive divider to the resistive one:
> $$
> V_1(t) = 2+4.67\,e^{-t/\tau}\ \text{V}.
> $$
> This is the circuit of two cells in series, each a capacitance $C_i$ in parallel with a conductance $G_i$. Note that $\tau$ lies between the layers' own relaxation times, $\epsilon_1/\sigma_1\approx44.27$ ms and $\epsilon_2/\sigma_2\approx354.2$ ms.
>
> **(d)** At $t = 0^+$ the structure is two capacitors in series, $C = A\big/(d_1/\epsilon_1+d_2/\epsilon_2)\approx118.1$ pF. Then $(\sigma_1/\epsilon_1)C\approx2.667$ nS and $(\sigma_2/\epsilon_2)C\approx0.3333$ nS, while the actual steady $G = 1/(1.25\ \text{G}\Omega) = 0.8$ nS matches neither: $G = (\sigma/\epsilon)C$ assumes a single $\sigma/\epsilon$ throughout. From (b), the interface charge $J(\epsilon_2/\sigma_2-\epsilon_1/\sigma_1)$ vanishes exactly when
> $$
> \frac{\epsilon_1}{\sigma_1} = \frac{\epsilon_2}{\sigma_2},
> $$
> equal relaxation times, e.g. $\sigma_1 = 2\times10^{-10}$ S/m and $\sigma_2 = 4\times10^{-10}$ S/m with these permittivities. Then the capacitive and resistive dividers agree ($V_1 = 6.667$ V at $t = 0^+$ and forever), there is no transient, and $G = (\sigma/\epsilon)C$ holds again.
>
> **Check:** $V_1(t)$ starts at the capacitive-divider value 6.667 V and settles at the resistive-divider value 2 V of (a) ✓; integrating $d\rho_s/dt = J_1-J_2$ numerically from $\rho_s = 0$ reproduces this curve and ends at $28000\epsilon_0$ ✓.
>
> **Watch out:** $D_n$ is continuous only across an interface without free charge. Between two lossy layers in the steady state there generally is free charge; the condition that survives is the continuity of $J_n$.
>
> **Answer.** (a) $I = 8$ nA, $\mathbf{J} = 8\times10^{-7}\hat{z}$ A/m², $\mathbf{E}_1 = 2000\hat{z}$ V/m, $\mathbf{E}_2 = 8000\hat{z}$ V/m; 2 V across layer 1 and 8 V across layer 2. (b) $\mathbf{D}_1 = 4000\epsilon_0\hat{z}$, $\mathbf{D}_2 = 32000\epsilon_0\hat{z}$ C/m²; $\rho_s = +4000\epsilon_0$ (lower plate), $-32000\epsilon_0$ (upper plate), $+28000\epsilon_0\approx2.48\times10^{-7}$ C/m² (interface); total zero. (c) $E_1(0^+)\approx6667$ V/m, $E_2(0^+)\approx3333$ V/m, $V_1(0^+)\approx6.667$ V; $\tau = (C_1+C_2)/(G_1+G_2)\approx0.1063$ s and $V_1(t) = 2+4.67e^{-t/\tau}$ V. (d) $G = 0.8$ nS versus 2.667 nS and 0.3333 nS; no interface charge if and only if $\epsilon_1/\sigma_1 = \epsilon_2/\sigma_2$.

### 10.12 Lossy coax driven through a resistor

> [!hard] Hard · conductance · RC transients · energy
> A coaxial cable of length $\ell = 10$ m has inner radius $a = 1$ mm and outer radius $b = 4$ mm and is filled with a lossy dielectric, $\epsilon_r = 2.5$, $\sigma = 1.0\times10^{-9}$ S/m; its far end is open. At $t = 0$ its near end is connected through a series resistor $R_s = 10$ MΩ to a $V_s = 12$ V source, with the inner conductor on the + side. The time scales here are so long that the cable acts as a lumped element.
> (a) Find $\mathcal{C}$ and $\mathcal{G}$, and the cable's total $C$, $G$ and $R = 1/G$.
> (b) Write the equation for the cable voltage $V(t)$, and find its time constant and the final voltage $V_\infty$. Why is $V_\infty$ less than 12 V?
> (c) In the steady state, find the stored energy per metre and in total, both from $\tfrac12\mathcal{C}V_\infty^2$ and by integrating $\tfrac12\epsilon E^2$ over the cross-section. Within what radius is half of the energy stored?
> (d) Long after (b), the source is disconnected and both ends of the cable are left open. How long does the voltage take to fall to 1 V?
>
> *Source: Summer 2019 HE2 #1, re-parameterized.*

> [!hint]- Hint
> Use Lecture 10's circuit model: the cable is $C$ in parallel with $G$, and the current into it is $C\,dV/dt+GV$. Write Kirchhoff's current law where $R_s$ meets the cable. After the disconnection only the cable's own $G$ is left.

> [!solution]- Solution
> **(a)** $\ln(b/a) = \ln4\approx1.3863$. For a single homogeneous filling,
> $$
> \mathcal{C} = \frac{2\pi\epsilon}{\ln(b/a)} = \frac{2\pi(2.5\epsilon_0)}{1.3863}\approx100.3\ \text{pF/m},\qquad \mathcal{G} = \frac{2\pi\sigma}{\ln(b/a)} = \frac{2\pi(10^{-9})}{1.3863}\approx4.532\ \text{nS/m}.
> $$
> ($\mathcal{G}$ directly: $\mathbf{J} = \sigma\mathbf{E} = \dfrac{\sigma V}{r\ln(b/a)}\hat{r}$, and the current per metre, $J_r\cdot2\pi r$, is the same through every cylinder $a<r<b$.) For 10 m: $C\approx1.003$ nF, $G\approx45.32$ nS, $R\approx22.06$ MΩ. Check: $G/C = \sigma/\epsilon\approx45.18\ \text{s}^{-1}$ ✓.
>
> **(b)** The source current $(V_s-V)/R_s$ either charges the cable or leaks through it:
> $$
> \frac{V_s-V}{R_s} = C\frac{dV}{dt}+GV\quad\Rightarrow\quad C\frac{dV}{dt}+\Big(G+\frac1{R_s}\Big)V = \frac{V_s}{R_s}.
> $$
> So $V(t) = V_\infty\big(1-e^{-t/\tau_1}\big)$ with
> $$
> \tau_1 = \frac{C}{G+1/R_s} = C\,(R\parallel R_s)\approx6.904\ \text{ms},\qquad V_\infty = V_s\frac{R}{R+R_s}\approx8.257\ \text{V},
> $$
> where $R\parallel R_s\approx6.881$ MΩ. In the steady state no current charges the cable, but $GV_\infty\approx0.3743\ \mu$A still leaks through the insulation. That current also flows through $R_s$, so $R_s$ and $R$ form a voltage divider and $V_\infty<12$ V. (Check: $(V_s-V_\infty)/R_s$ equals $GV_\infty$ ✓; the leakage dissipates $GV_\infty^2\approx3.09\ \mu$W.)
>
> **(c)** The steady field is $\mathbf{E} = \dfrac{V_\infty}{r\ln(b/a)}\hat{r}$. Per metre,
> $$
> W' = \int_a^b\tfrac12\epsilon E^2\,2\pi r\,dr = \frac{\pi\epsilon V_\infty^2}{\ln^2(b/a)}\int_a^b\frac{dr}{r} = \frac{\pi\epsilon V_\infty^2}{\ln(b/a)} = \tfrac12\mathcal{C}V_\infty^2\approx3.42\ \text{nJ/m},
> $$
> and $W = \tfrac12CV_\infty^2\approx34.2$ nJ for the whole cable. Half of the energy lies within the radius $c$ for which $\int_a^c dr/r$ is half of $\int_a^b dr/r$: $\ln(c/a) = \tfrac12\ln(b/a)$, so $c = \sqrt{ab} = 2$ mm. That inner ring, $a<r<2$ mm, is only $0.2$ of the cross-section, yet it holds half the energy, because the field is strongest next to the inner conductor.
>
> **(d)** Disconnected, the cable discharges through its own insulation: $C\,dV/dt = -GV$, so $V = V_\infty e^{-t/\tau_2}$ with $\tau_2 = C/G = \epsilon/\sigma\approx22.14$ ms, independent of the length and the radii. It reaches 1 V when
> $$
> t = \tau_2\ln\frac{V_\infty}{1\ \text{V}},\qquad \ln\frac{V_\infty}{1\ \text{V}}\approx2.111,\qquad t\approx46.73\ \text{ms}.
> $$
> **Check:** $\tau_1<\tau_2$, as it must be: while the source is connected, $C$ sees the Thevenin resistance $R\parallel R_s\approx6.881$ MΩ; afterwards it sees only $R\approx22.06$ MΩ.
>
> **Watch out:** the charging time constant is neither $\epsilon/\sigma$ nor $R_sC$: the source resistor and the leakage act in parallel on $C$.
>
> **Answer.** (a) $\mathcal{C}\approx100.3$ pF/m, $\mathcal{G}\approx4.532$ nS/m; $C\approx1.003$ nF, $G\approx45.32$ nS, $R\approx22.06$ MΩ. (b) $C\,dV/dt+(G+1/R_s)V = V_s/R_s$; $\tau_1\approx6.904$ ms, $V_\infty\approx8.257$ V (a divider of $R_s$ and $R$). (c) $3.42$ nJ/m and $34.2$ nJ in total; half of it within $r = \sqrt{ab} = 2$ mm. (d) $\tau_2 = \epsilon/\sigma\approx22.14$ ms; 1 V after $\approx46.73$ ms.

### Sources for this page
Course notes and slides, Lecture 10: the fixed-charge/fixed-voltage challenge (extended in 10.2), the shared geometric factor behind $G = (\sigma/\epsilon)C$ and the relaxation time (used in 10.3 and 10.5), the half-angle coax (10.7d) and the junction capacitance (10.8). FA26 HW4 #4, the lossy sphere, which 10.5 extends to three shapes. Old exams, re-parameterized: Summer 2020 HE2 #1a (10.6: dielectric moved to the bottom layer, polarity reversed, energy added), SP18 Exam 1 #5 (10.9, also extended: polarity reversed, lossy lower half only, discharge time) and Summer 2019 HE2 #1 (10.12). Classic textbook problems with new numbers: the two placements of one slab (10.7), pulling the plates apart (10.10) and the two-layer lossy capacitor (10.11). Problems 10.1, 10.3, 10.4 and 10.5 are original.

*Previous: [[practice/09-static-fields-in-dielectric-media|Lecture 9 practice]] · next: [[practice/11-lorentz-drude-models|Lecture 11 practice]] · [[practice/index|all practice]]*
