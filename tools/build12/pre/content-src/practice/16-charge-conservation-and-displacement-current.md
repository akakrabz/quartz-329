---
title: "Practice — Lecture 16: Charge conservation, displacement current, and Maxwell's equations"
description: "12 practice problems (5 easy, 3 medium, 4 hard) on the continuity equation, displacement current through a surface and in a lossy medium, charging and leaky capacitors, the two-surface MMF argument, the consistency of Maxwell's equations, and the four boundary conditions at tilted interfaces and perfect conductors, each with a folded hint and a worked solution."
tags: [practice, waves]
lecture: 16
---

*Practice for [[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Lecture 16]] · concepts: [[concepts/continuity-equation]] · [[concepts/displacement-current]] · [[concepts/maxwells-equations]] · [[concepts/boundary-conditions]] · all practice: [[practice/index|hub]] · by difficulty: [[practice/easy|easy]] · [[practice/medium|medium]] · [[practice/hard|hard]] · [[practice/topics|by topic]]*

Work each problem on paper first. Open the **hint** only when stuck, and the **solution** only after you have an answer you would hand in. Every answer here has been checked numerically.

## Easy

### 16.1 Charge piling up in a cylinder

> [!easy] Easy · continuity · divergence theorem
> In a region of space the current density is $\mathbf{J} = 2r^2\,\hat{r}-4z\,\hat{z}$ A/m², in cylindrical coordinates with $r$ and $z$ in metres.
>
> (a) Find $\partial\rho/\partial t$ at $r = 0.2$ m and at $r = 1$ m. Is the charge density growing or shrinking at each point?
>
> (b) At what rate does the total charge inside the cylinder $r<0.5$ m, $0<z<2$ m change? Is the cylinder gaining or losing charge?
>
> *Source: Lecture 16 slides, the unit-cube continuity example, re-posed in a cylinder with a sign change.*

> [!hint]- Hint
> Charge conservation at a point: $\partial\rho/\partial t = -\nabla\cdot\mathbf{J}$, with the cylindrical divergence $\dfrac1r\dfrac{\partial}{\partial r}(rJ_r)+\dfrac{\partial J_z}{\partial z}$. For (b), integrate $\partial\rho/\partial t$ over the cylinder with $dV = r\,dr\,d\phi\,dz$.

> [!solution]- Solution
> **(a)** Current flowing *out* of a point drains its charge:
> $$
> \nabla\cdot\mathbf{J} = \frac1r\frac{\partial}{\partial r}\big(r\cdot2r^2\big)+\frac{\partial(-4z)}{\partial z} = 6r-4\ \text{A/m}^3,\qquad \frac{\partial\rho}{\partial t} = -\nabla\cdot\mathbf{J} = 4-6r\ \text{A/m}^3 .
> $$
> At $r = 0.2$ m, $\partial\rho/\partial t = +2.8$ A/m³ (C/m³ per second): the density is **growing**, because the converging $z$ flow brings in more than the radial flow carries away. At $r = 1$ m it is $-2$ A/m³: **shrinking**. The two flows balance at $r = 2/3$ m.
>
> **(b)** Integrate over the cylinder:
> $$
> \frac{dQ}{dt} = \int_0^2\!\!\int_0^{2\pi}\!\!\int_0^{0.5}(4-6r)\,r\,dr\,d\phi\,dz = 2\cdot2\pi\Big[2r^2-2r^3\Big]_0^{0.5} = 4\pi(0.5-0.25) = \pi\ \text{A}\approx3.14\ \text{A}.
> $$
> It is positive: the cylinder is **gaining** charge at $\pi$ C/s.
>
> **Check** face by face, with outward normals. Side $r = 0.5$ m: $J_r = 0.5$ A/m² over $2\pi(0.5)(2) = 2\pi$ m² carries $\pi$ A out. Top $z = 2$ m: $J_z = -8$ A/m² points *into* the cylinder, over $\pi/4$ m², so $2\pi$ A comes in. Bottom $z = 0$: $J_z = 0$. Net outward current $= \pi-2\pi = -\pi$ A $= -dQ/dt$ ✓.
>
> **Watch out:** $\oint\mathbf{J}\cdot d\mathbf{S}$ is the rate of *decrease* of the enclosed charge. A net inflow, as here, means the charge grows.
>
> **Answer.** $\partial\rho/\partial t = 4-6r$ A/m³: $+2.8$ A/m³ (growing) at $r = 0.2$ m and $-2$ A/m³ (shrinking) at $r = 1$ m. $dQ/dt = +\pi\approx3.14$ A: the cylinder gains charge at about 3.14 C/s.

### 16.2 Displacement current through a window

> [!easy] Easy · displacement current · flux
> In a region of free space the electric field is uniform and oscillates in time: $\mathbf{E} = E_0\cos(\omega t)\,(0.6\,\hat{x}+0.8\,\hat{z})$ with $E_0 = 10$ kV/m and $\omega = 2\pi\times10^6$ rad/s. A square window, 10 cm on a side, lies in the plane $z = 0$, with $d\mathbf{S} = \hat{z}\,dS$.
>
> (a) Find the displacement current density $\partial\mathbf{D}/\partial t$.
>
> (b) Find the displacement current $I_d(t)$ through the window, and its amplitude.
>
> (c) At which instants is $\lvert I_d\rvert$ largest, and what is $\mathbf{E}$ at those instants?
>
> *Source: the displacement-current-through-an-area example of the Lecture 13 slides (quoted in Lecture 16), with a sinusoidal, tilted field.*

> [!hint]- Hint
> In free space $\partial\mathbf{D}/\partial t = \epsilon_0\,\partial\mathbf{E}/\partial t$. Only the component along $d\mathbf{S}$ threads the window: $I_d = \dfrac{d}{dt}\displaystyle\int\mathbf{D}\cdot d\mathbf{S}$.

> [!solution]- Solution
> **(a)** Differentiate the field:
> $$
> \frac{\partial\mathbf{D}}{\partial t} = \epsilon_0\frac{\partial\mathbf{E}}{\partial t} = -\epsilon_0\omega E_0\sin(\omega t)\,(0.6\,\hat{x}+0.8\,\hat{z}),\qquad \epsilon_0\omega E_0 = 2\pi\times10^{10}\,\epsilon_0 = 0.556\ \text{A/m}^2 .
> $$
> **(b)** The window has area $A = 0.01$ m², and only the $z$ component crosses it:
> $$
> I_d(t) = \int\frac{\partial\mathbf{D}}{\partial t}\cdot\hat{z}\,dS = -0.8\,\epsilon_0\omega E_0A\sin(\omega t) = -1.6\pi\times10^8\,\epsilon_0\sin(\omega t)\ \text{A} = -4.45\sin(\omega t)\ \text{mA}.
> $$
> The amplitude is 4.45 mA. It is the rate of change of the electric flux $\psi_E = 0.8\,\epsilon_0E_0A\cos(\omega t) = 7.08\times10^{-10}\cos(\omega t)$ C through the window.
>
> **(c)** $\lvert\sin(\omega t)\rvert = 1$ at $t = 0.25,\ 0.75,\ 1.25,\dots$ μs (the period is 1 μs). At those instants $\cos(\omega t) = 0$, so $\mathbf{E} = 0$: the displacement current is largest when the field passes through zero, where it changes fastest. At $t = 0.25$ μs, $I_d = -4.45$ mA, i.e. 4.45 mA through the window in the $-z$ direction.
>
> **Check (units):** [F/m] × [1/s] × [V/m] = (C/V)·(1/s)·(V/m²) = C/(m²·s) = A/m² ✓.
>
> **Watch out:** using the full $\lvert\mathbf{E}\rvert$ instead of $E_z$ gives 5.56 mA, 25% too high. The $x$ component runs along the window and carries nothing through it.
>
> **Answer.** $\partial\mathbf{D}/\partial t = -0.556\sin(\omega t)\,(0.6\,\hat{x}+0.8\,\hat{z})$ A/m²; $I_d = -4.45\sin(\omega t)$ mA, amplitude 4.45 mA; largest at $t = 0.25,\ 0.75,\dots$ μs, when $\mathbf{E} = 0$.

### 16.3 The missing displacement current

> [!easy] Easy · find the error · displacement current · polarization current
> A parallel-plate capacitor with plate area $A = 20$ cm² and gap $d = 0.5$ mm is filled with a perfect dielectric of permittivity $\epsilon = 4\epsilon_0$ and is charged by a constant current $I = 3$ mA. A student computes the displacement current between the plates:
>
> "$C = \epsilon A/d$, so $dV/dt = I/C = Id/(\epsilon A)$. With $E = V/d$, $dE/dt = I/(\epsilon A)$. The displacement current is $I_d = \epsilon_0A\,dE/dt = (\epsilon_0/\epsilon)\,I = 0.75$ mA. So only a quarter of the wire's current continues across the gap, and the MMF around a loop that encircles the gap is a quarter of the MMF around the wire."
>
> What is wrong? Give the correct displacement current, and say what the student's 0.75 mA actually is.
>
> *Source: original.*

> [!hint]- Hint
> Inside a dielectric, the displacement current density is the time derivative of which field, $\epsilon_0\mathbf{E}$ or $\mathbf{D}$? Gauss's law at a plate gives $D$ directly from the plate charge.

> [!solution]- Solution
> **The slip:** the displacement current density is $\partial\mathbf{D}/\partial t$, and inside the dielectric $\mathbf{D} = \epsilon\mathbf{E} = \epsilon_0\mathbf{E}+\mathbf{P}$, not $\epsilon_0\mathbf{E}$. The student kept only the vacuum part and dropped $\partial\mathbf{P}/\partial t$. (The rest of the work, $dE/dt = I/(\epsilon A)$, is right.)
>
> **Fix:**
> $$
> I_d = A\frac{\partial D}{\partial t} = \epsilon A\frac{dE}{dt} = \epsilon A\cdot\frac{I}{\epsilon A} = I = 3\ \text{mA},
> $$
> a displacement current density of $I/A = 1.5$ A/m². Gauss's law gives the same result without any $\epsilon$: just inside the plate $D = \rho_s = Q/A$, so $\partial D/\partial t = (dQ/dt)/A = I/A$, whatever fills the gap.
>
> The student's 0.75 mA is the vacuum term $\epsilon_0A\,dE/dt$. The other 2.25 mA is the **polarization current** $A\,\partial P/\partial t = (\epsilon-\epsilon_0)A\,dE/dt$ of the bound charges, which really do move ([[1-electrostatics/11-lorentz-drude-models-for-conductivity-and-susceptibility|Lecture 11]]). Both belong to $\partial\mathbf{D}/\partial t$, and together they carry the full 3 mA across the gap, so the MMF around a loop encircling the gap (larger than the plates) equals the MMF around the wire.
>
> **Answer.** The student used $\epsilon_0\mathbf{E}$ instead of $\mathbf{D} = \epsilon\mathbf{E}$. The displacement current is $I_d = I = 3$ mA (1.5 A/m²): 0.75 mA vacuum term plus 2.25 mA polarization current. The two MMFs are equal.

### 16.4 What changes when fields vary

> [!easy] Easy · true or false · displacement current · continuity
> True or false?
>
> (a) When fields vary in time, $\oint_C\mathbf{H}\cdot d\mathbf{l}$ equals the conduction current through *any* surface bounded by $C$.
>
> (b) A displacement current can exist in a perfect vacuum, where no charge moves.
>
> (c) Taking the divergence of the Ampère–Maxwell law and using Gauss's law gives the continuity equation.
>
> (d) Faraday's law, on its own, guarantees $\nabla\cdot\mathbf{B} = 0$.
>
> (e) At an interface carrying a surface current, the jump in tangential $\mathbf{H}$ picks up an extra term from $\partial\mathbf{D}/\partial t$ when the fields vary in time.
>
> *Source: original (Lecture 16 course notes).*

> [!hint]- Hint
> For each statement ask what the static law said, and whether the new term $\partial\mathbf{D}/\partial t$ (or any time derivative) changes it.

> [!solution]- Solution
> **(a) False.** The right side of the Ampère–Maxwell law is the conduction *plus* displacement current through the surface. The conduction current alone depends on the surface: for a charging capacitor, a disk pierced by the wire carries $I$, while a bag passing through the gap carries no conduction current at all; there the whole $I$ is displacement current. Only $\mathbf{J}+\partial\mathbf{D}/\partial t$ has zero divergence, so only its flux is the same for every surface on $C$.
>
> **(b) True.** $\partial\mathbf{D}/\partial t = \epsilon_0\,\partial\mathbf{E}/\partial t$ is nonzero in vacuum whenever $\mathbf{E}$ changes. Nothing moves: it is a source of $\mathbf{H}$ that behaves like a current, and it is what lets electromagnetic waves cross empty space.
>
> **(c) True.** $0 = \nabla\cdot(\nabla\times\mathbf{H}) = \nabla\cdot\mathbf{J}+\dfrac{\partial}{\partial t}\nabla\cdot\mathbf{D} = \nabla\cdot\mathbf{J}+\dfrac{\partial\rho}{\partial t}$. This is exactly why Maxwell's term is required.
>
> **(d) False.** The divergence of Faraday's law gives $\dfrac{\partial}{\partial t}(\nabla\cdot\mathbf{B}) = -\nabla\cdot(\nabla\times\mathbf{E}) = 0$: $\nabla\cdot\mathbf{B}$ cannot *change*. A static field such as $\mathbf{B} = B_0(x\hat{x}+y\hat{y}+z\hat{z})$, with $\nabla\cdot\mathbf{B} = 3B_0$, passes this test. That $\nabla\cdot\mathbf{B}$ is zero takes the extra fact that there is no magnetic charge (equivalently, that it was zero for the static fields we started from).
>
> **(e) False.** On a thin rectangle of width $w$ straddling the interface, the flux of $\partial\mathbf{D}/\partial t$ is proportional to $w$ and vanishes as $w\to0$; only a *surface* current survives the limit. The four boundary conditions are the same as in statics.
>
> **Answer.** (a) False; (b) True; (c) True; (d) False; (e) False.

### 16.5 Fields just outside a metal ball

> [!easy] Easy · multiple choice · boundary conditions · conductors
> A perfectly conducting sphere of radius 1 m is centred at the origin, with free space outside. At the point $P = (0,\,0.6,\,0.8)$ m on its surface, four vectors are proposed as the electric or the magnetic field just outside the metal at some instant: (1) $3\hat{y}+4\hat{z}$, (2) $5\hat{x}$, (3) $4\hat{y}-3\hat{z}$, (4) $5\hat{z}$. Which classification is correct?
>
> (a) (1) can only be $\mathbf{E}$; (2) and (3) can only be $\mathbf{H}$; (4) can be neither
>
> (b) (1) and (4) can only be $\mathbf{E}$; (2) and (3) can only be $\mathbf{H}$
>
> (c) (1) can only be $\mathbf{H}$; (2) and (3) can only be $\mathbf{E}$; (4) can be neither
>
> (d) any of the four can be $\mathbf{E}$; (2) and (3) can also be $\mathbf{H}$
>
> (e) (1) can only be $\mathbf{E}$; (2) can only be $\mathbf{H}$; (3) and (4) can be neither
>
> Then take vector (1) as $\mathbf{E}$ in kV/m and vector (3) as $\mathbf{H}$ in A/m, and find $\rho_s$ and $\mathbf{J}_s$ at $P$.
>
> *Source: Lecture 16 slides, the perfect-conductor challenge question, re-posed on a sphere with vectors.*

> [!hint]- Hint
> Inside a perfect conductor $\mathbf{E} = 0$ and (in this course) $\mathbf{H} = 0$, so just outside $\hat{n}\times\mathbf{E} = 0$ and $\hat{n}\cdot\mathbf{B} = 0$. On a sphere centred at the origin, $\hat{n}$ at a surface point is the position vector divided by the radius — not $\hat{z}$.

> [!solution]- Solution
> **(a).** At $P$ the normal out of the metal is $\hat{n} = (0,\,0.6,\,0.8)$. The metal (medium 2) holds no field, so the boundary conditions leave $\hat{n}\times\mathbf{E} = 0$ ($\mathbf{E}$ purely normal, ending on surface charge) and $\hat{n}\cdot\mathbf{B} = 0$ ($\mathbf{H}$ purely tangential, carried by surface current).
>
> - (1) $= 5\hat{n}$: purely normal, so $\mathbf{E}$ only.
> - (2) $\hat{n}\cdot\hat{x} = 0$: purely tangential, so $\mathbf{H}$ only.
> - (3) $\hat{n}\cdot(4\hat{y}-3\hat{z}) = 2.4-2.4 = 0$: tangential, so $\mathbf{H}$ only.
> - (4) $\hat{n}\cdot5\hat{z} = 4$: it has a normal part $4\hat{n}$ and a tangential part $5\hat{z}-4\hat{n} = -2.4\hat{y}+1.8\hat{z}$ (magnitude 3). Oblique, so neither.
>
> Why the others fail: (b) treats $\hat{z}$ as "straight out of the surface", a flat-floor habit; the sphere's normal at $P$ is tilted $36.9^\circ$ from $\hat{z}$. (c) swaps the roles: $\mathbf{E}$ ends *on* the surface, $\mathbf{H}$ runs *along* it. (d) forgets that $\hat{n}\times\mathbf{E} = 0$ still holds for time-varying fields: Faraday's law on a thin loop straddling the surface encloses no flux in the limit. (e) misses that (3) is perpendicular to $\hat{n}$.
>
> **Surface sources.** $\rho_s = \hat{n}\cdot\mathbf{D} = \epsilon_0\times5$ kV/m $= 5000\,\epsilon_0\approx44.3$ nC/m², positive since $\mathbf{E}$ points away from the surface. $\mathbf{J}_s = \hat{n}\times\mathbf{H} = (0,\,0.6,\,0.8)\times(0,\,4,\,-3) = (-1.8-3.2,\,0,\,0) = -5\hat{x}$ A/m.
>
> **Check:** $\mathbf{J}_s\times\hat{n} = (-5\hat{x})\times(0.6\hat{y}+0.8\hat{z}) = 4\hat{y}-3\hat{z}$, the tangential $\mathbf{H}$ we started from ✓.
>
> **Answer.** (a). $\rho_s = 5000\,\epsilon_0\approx44.3$ nC/m² and $\mathbf{J}_s = -5\hat{x}$ A/m.

## Medium

### 16.6 Conduction versus displacement in soil

> [!medium] Medium · displacement current · relaxation time · Ohm's law
> Moist soil has conductivity $\sigma = 0.01$ S/m and permittivity $\epsilon = 9\epsilon_0$. A uniform field $\mathbf{E} = E_0\cos(\omega t)\,\hat{x}$ with $E_0 = 20$ V/m acts inside it.
>
> (a) Write the conduction current density $\mathbf{J}$ and the displacement current density $\partial\mathbf{D}/\partial t$. Which one peaks first?
>
> (b) Find the ratio of their amplitudes and the frequency $f_c$ at which they are equal. Compare $1/(2\pi f_c)$ with the relaxation time of the soil.
>
> (c) Which current dominates at 1 MHz (AM radio) and at 2 GHz (mobile phones), and by what factor?
>
> (d) At $f = f_c$, write the total current density $\mathbf{J}+\partial\mathbf{D}/\partial t$ as a single cosine, and give its amplitude.
>
> (Calculator problem.)
>
> *Source: classic, new material and numbers.*

> [!hint]- Hint
> $\mathbf{J} = \sigma\mathbf{E}$ keeps in step with the field. $\partial\mathbf{D}/\partial t = \epsilon\,\partial\mathbf{E}/\partial t$ brings down a factor $\omega$ and turns the cosine into a sine. For (d), $\cos x-\sin x$ can be written as a single cosine.

> [!solution]- Solution
> **Setup.** In a lossy medium both terms on the right of $\nabla\times\mathbf{H} = \mathbf{J}+\partial\mathbf{D}/\partial t$ are present: free charges drift ($\sigma\mathbf{E}$), and the flux density changes ($\epsilon\,\partial\mathbf{E}/\partial t$).
>
> **(a)**
> $$
> \mathbf{J} = \sigma E_0\cos(\omega t)\,\hat{x} = 0.2\cos(\omega t)\,\hat{x}\ \text{A/m}^2,\qquad \frac{\partial\mathbf{D}}{\partial t} = -\omega\epsilon E_0\sin(\omega t)\,\hat{x} = \omega\epsilon E_0\cos\!\Big(\omega t+\frac{\pi}{2}\Big)\hat{x}.
> $$
> The displacement current peaks a quarter period *before* the field and the conduction current: it leads by $90^\circ$, because it follows the rate of change of $\mathbf{E}$, which is largest where $\mathbf{E}$ crosses zero.
>
> **(b)** The ratio of the amplitudes is
> $$
> \frac{\lvert\partial\mathbf{D}/\partial t\rvert}{\lvert\mathbf{J}\rvert} = \frac{\omega\epsilon}{\sigma},\qquad \text{equal at}\ \ \omega_c = \frac{\sigma}{\epsilon} = \frac{0.01}{9\times8.854\times10^{-12}} = 1.25\times10^8\ \text{rad/s},\qquad f_c = \frac{\omega_c}{2\pi} = 20.0\ \text{MHz}.
> $$
> So $1/(2\pi f_c) = \epsilon/\sigma = 7.97$ ns, exactly the relaxation time of [[1-electrostatics/08-conductors-dielectrics-and-polarization|Lecture 8]]. A material acts as a conductor for fields that change slowly compared with its relaxation time, and as a dielectric for fields that change faster.
>
> **(c)** The ratio is $f/f_c$. At 1 MHz it is 0.0501: conduction dominates by a factor of 20.0. At 2 GHz it is 100: displacement dominates by a factor of 100. The same soil is a conductor for AM radio and a lossy dielectric for a phone signal.
>
> **(d)** At $f_c$, $\omega\epsilon = \sigma$, so
> $$
> \mathbf{J}+\frac{\partial\mathbf{D}}{\partial t} = \sigma E_0\big[\cos(\omega t)-\sin(\omega t)\big]\hat{x} = \sqrt2\,\sigma E_0\cos\!\Big(\omega t+\frac{\pi}{4}\Big)\hat{x} = 0.283\cos\!\Big(\omega t+\frac{\pi}{4}\Big)\hat{x}\ \text{A/m}^2 .
> $$
> **Check:** at $t = 0$ both forms give 0.2 A/m² ✓. The amplitude is $\sqrt2\times0.2 = 0.283$ A/m², not $0.2+0.2 = 0.4$: the two peaks come a quarter period apart. At any frequency the amplitude is $E_0\sqrt{\sigma^2+\omega^2\epsilon^2}$.
>
> **Answer.** (a) $\mathbf{J} = 0.2\cos(\omega t)\,\hat{x}$ A/m²; $\partial\mathbf{D}/\partial t = -\omega\epsilon E_0\sin(\omega t)\,\hat{x}$, leading by $90^\circ$. (b) Ratio $\omega\epsilon/\sigma$; $f_c = 20.0$ MHz, and $1/(2\pi f_c) = \epsilon/\sigma = 7.97$ ns, the relaxation time. (c) Conduction wins by 20.0 at 1 MHz; displacement wins by 100 at 2 GHz. (d) $0.283\cos(\omega t+\pi/4)\,\hat{x}$ A/m².

### 16.7 Charging plates with a dielectric core

> [!medium] Medium · displacement current · Ampère's law · side-by-side dielectrics
> A capacitor has circular plates of radius $a = 4$ cm in the planes $z = 0$ and $z = d = 2$ mm, centred on the $z$ axis. A constant current $I = 0.5$ A charges it: the current arrives along $+\hat{z}$ through a thin lead on the axis below the bottom plate and leaves along $+\hat{z}$ through a lead above the top plate. Ignore fringing.
>
> (a) With air between the plates, find the displacement current density in the gap, and $\mathbf{H}$ in the gap at distance $r$ from the axis, both for $r<a$ and for $r>a$. Evaluate $H$ at $r = 2$ cm and at $r = 8$ cm.
>
> (b) Now a coaxial disk of dielectric, $\epsilon = 3\epsilon_0$ and radius $a/2 = 2$ cm, fills the gap near the axis (air elsewhere), and the same current charges the capacitor. What fraction of the displacement current crosses the dielectric? Find $H$ at $r = 2$ cm and at $r = 8$ cm now.
>
> *Source: classic (the charging capacitor), with a dielectric core added.*

> [!hint]- Hint
> Ampère–Maxwell on a circle of radius $r$ in the gap: $H_\phi\cdot2\pi r$ equals the displacement current through the flat disk it bounds (no wire crosses that disk). In (b) the plates are still equipotentials, so $E$ is the same in the dielectric and in the air beside it — but $D$ is not.

> [!solution]- Solution
> **Setup.** By symmetry $\mathbf{H} = H_\phi(r)\,\hat\phi$. Take $C$ a circle of radius $r$ in the gap, counter-clockwise seen from $+z$, and the flat disk it bounds as $S$: no conduction current crosses it, so $H_\phi\cdot2\pi r = \int_S\partial\mathbf{D}/\partial t\cdot d\mathbf{S}$.
>
> **(a)** The bottom plate gains positive charge at the rate $I$, so $\mathbf{D} = (Q/\pi a^2)\,\hat{z}$ in the gap (Gauss's law at the plate) and
> $$
> \frac{\partial\mathbf{D}}{\partial t} = \frac{I}{\pi a^2}\,\hat{z} = \frac{0.5}{\pi(0.04)^2}\,\hat{z} = \frac{312.5}{\pi}\,\hat{z} = 99.5\,\hat{z}\ \text{A/m}^2,
> $$
> uniform and in total exactly $I$: the lead current continues across the gap as displacement current. Ampère–Maxwell then gives
> $$
> H_\phi = \frac{1}{2\pi r}\cdot\frac{I}{\pi a^2}\cdot\pi r^2 = \frac{Ir}{2\pi a^2}\quad(r<a),\qquad H_\phi = \frac{I}{2\pi r}\quad(r>a),
> $$
> counter-clockwise seen from $+z$. Numbers: $H(2\ \text{cm}) = I/(4\pi a) = 3.125/\pi = 0.995$ A/m and $H(8\ \text{cm}) = 0.995$ A/m — equal because $a/2$ and $2a$ happen to give the same value; the maximum, $I/(2\pi a) = 1.99$ A/m, is at the plate edge. At $r = 8$ cm the field in the gap is the same as 8 cm from a lead: outside the plates, a circle cannot tell whether the current through it is conduction or displacement current.
>
> **(b)** Both regions sit between the same two equipotential plates, so $E$ and $dE/dt$ are common to them, while $D = \epsilon E$ is three times larger in the core:
> $$
> I = \frac{dE}{dt}\Big[3\epsilon_0\cdot\pi\Big(\frac a2\Big)^2+\epsilon_0\cdot\pi\Big(a^2-\frac{a^2}{4}\Big)\Big] = \frac{dE}{dt}\,\epsilon_0\pi a^2\Big(\frac34+\frac34\Big).
> $$
> The core and the air ring carry equal shares: **half** of the displacement current crosses the dielectric, which covers a quarter of the area (199 A/m² there against 66.3 A/m² in the air). At $r = 2$ cm, the edge of the core,
> $$
> H_\phi = \frac{I/2}{2\pi(0.02)} = \frac{I}{2\pi a} = \frac{6.25}{\pi} = 1.99\ \text{A/m},
> $$
> twice the air value, while at $r = 8$ cm the circle still encloses the full $I$: $H = 0.995$ A/m, unchanged.
>
> **Check:** in the air ring the enclosed displacement current is $\tfrac I2+\tfrac I2\cdot\dfrac{r^2-a^2/4}{3a^2/4}$, which reaches $I$ at $r = a$, so $H(a) = I/(2\pi a)$ with or without the core ✓. In between, $H$ dips slightly (1.88 A/m at $r = 3$ cm), because the enclosed current grows more slowly than $r$ there. The differential form agrees with (a): $\dfrac1r\dfrac{d}{dr}(rH_\phi) = \dfrac{I}{\pi a^2} = \partial D_z/\partial t$ ✓.
>
> **Watch out:** taking $D$ (rather than $E$) as common to the two regions would put the same displacement current density everywhere and miss the effect entirely. $D$ is common to layers stacked *across* the field; here the two regions sit side by side.
>
> **Answer.** (a) $\partial\mathbf{D}/\partial t = 99.5\,\hat{z}$ A/m²; $\mathbf{H} = \dfrac{Ir}{2\pi a^2}\hat\phi$ for $r<a$ and $\dfrac{I}{2\pi r}\hat\phi$ for $r>a$ (counter-clockwise seen from $+z$); $H = 0.995$ A/m at both 2 cm and 8 cm. (b) One half; $H(2\ \text{cm}) = 1.99$ A/m (doubled), $H(8\ \text{cm}) = 0.995$ A/m (unchanged).

### 16.8 Charges and currents on a coax

> [!medium] Medium · boundary conditions · conductors · surface charge
> A coaxial cable lies along the $z$ axis: a perfectly conducting inner wire of radius $a = 2$ mm and a perfectly conducting outer conductor whose inner surface is at $r = b = 6$ mm, with free space between. At a certain instant the fields just outside the metal, at two points in the plane $z = 0$, are
>
> at $P = (1.2,\,1.6,\,0)$ mm on the inner wire: $\mathbf{E} = 18\hat{x}+24\hat{y}$ kV/m and $\mathbf{H} = -24\hat{x}+18\hat{y}$ A/m;
>
> at $Q = (-3.6,\,-4.8,\,0)$ mm on the outer conductor: $\mathbf{E} = -6\hat{x}-8\hat{y}$ kV/m and $\mathbf{H} = 8\hat{x}-6\hat{y}$ A/m.
>
> (a) Find the unit normal $\hat{n}$ to use at $P$ and at $Q$, and check that these fields are allowed just outside a perfect conductor.
>
> (b) Find $\rho_s$ and $\mathbf{J}_s$ at $P$ and at $Q$.
>
> (c) The fields have the cable's cylindrical symmetry. Find the charge per unit length and the total current on each conductor, and comment.
>
> *Source: original (the slides' surface-charge exercise, extended to surface currents on a coax).*

> [!hint]- Hint
> $\hat{n}$ always points out of the metal, into the region where the fields are. On the inner wire that is away from the axis; on the outer conductor it is *toward* the axis.

> [!solution]- Solution
> **Setup.** With $\mathbf{E} = 0$ and $\mathbf{H} = 0$ in the metal (medium 2), the boundary conditions reduce to $\rho_s = \hat{n}\cdot\mathbf{D}$ and $\mathbf{J}_s = \hat{n}\times\mathbf{H}$, with $\hat{n}$ pointing from the metal into the gap.
>
> **(a)** $\lvert P\rvert = 2$ mm $= a$, and $\hat{n}_P = \hat{r} = (0.6,\,0.8,\,0)$. $\lvert Q\rvert = 6$ mm $= b$, where $\hat{r} = (-0.6,\,-0.8,\,0)$; but the gap lies toward the axis, so $\hat{n}_Q = -\hat{r} = (0.6,\,0.8,\,0)$ — the same vector as at $P$. Allowed? $\mathbf{E}_P = 30\,\hat{n}_P$ kV/m and $\mathbf{E}_Q = -10\,\hat{n}_Q$ kV/m are purely normal, and $\hat{n}_P\cdot\mathbf{H}_P = -14.4+14.4 = 0$, $\hat{n}_Q\cdot\mathbf{H}_Q = 4.8-4.8 = 0$: both $\mathbf{H}$'s are tangential ✓.
>
> **(b)**
> $$
> \rho_s(P) = \epsilon_0\,\hat{n}_P\cdot\mathbf{E}_P = 30\,000\,\epsilon_0 = 265.6\ \text{nC/m}^2,\qquad \rho_s(Q) = \epsilon_0\,\hat{n}_Q\cdot\mathbf{E}_Q = -10\,000\,\epsilon_0 = -88.5\ \text{nC/m}^2,
> $$
> $$
> \mathbf{J}_s(P) = \hat{n}_P\times\mathbf{H}_P = \big[0.6(18)-0.8(-24)\big]\hat{z} = 30\,\hat{z}\ \text{A/m},\qquad \mathbf{J}_s(Q) = \hat{n}_Q\times\mathbf{H}_Q = \big[0.6(-6)-0.8(8)\big]\hat{z} = -10\,\hat{z}\ \text{A/m}.
> $$
> **(c)** By symmetry each density is uniform around its conductor:
> $$
> \rho_{l,\text{in}} = 2\pi a\,\rho_s(P) = 120\pi\epsilon_0 = +3.34\ \text{nC/m},\quad \rho_{l,\text{out}} = 2\pi b\,\rho_s(Q) = -3.34\ \text{nC/m};\qquad I_{\text{in}} = 2\pi a(30) = 0.12\pi = 0.377\ \text{A},\quad I_{\text{out}} = 2\pi b(-10) = -0.377\ \text{A}.
> $$
> Equal and opposite: the outer conductor carries the return current, along $-\hat{z}$, and the opposite charge. A cylinder around the whole cable encloses no net charge and no net current, so the fields vanish outside the cable.
>
> **Check** (Gauss and Ampère in the gap): $E_r(a) = \rho_{l,\text{in}}/(2\pi\epsilon_0a) = 30$ kV/m and $E_r(b) = 10$ kV/m; $H_\phi(a) = I_{\text{in}}/(2\pi a) = 30$ A/m and $H_\phi(b) = 10$ A/m — exactly the magnitudes given at $P$ and $Q$ ✓. The voltage between the conductors is $V(a)-V(b) = \int_a^bE_r\,dr = (30\ \text{kV/m})\,a\ln3 = 65.9$ V, and $\rho_{l,\text{in}}/(65.9\ \text{V}) = 50.6$ pF/m $= 2\pi\epsilon_0/\ln(b/a)$, the coax capacitance of [[1-electrostatics/10-capacitance-and-conductance|Lecture 10]] ✓.
>
> **Watch out:** taking $\hat{n} = +\hat{r}$ on the outer conductor flips both of its results, to $+88.5$ nC/m² and $+10\hat{z}$ A/m. That would be a cable with net charge and net current, which would have fields outside it.
>
> **Answer.** (a) $\hat{n}_P = \hat{n}_Q = 0.6\hat{x}+0.8\hat{y}$; $\mathbf{E}$ is normal and $\mathbf{H}$ tangential at both points. (b) $\rho_s(P) = 265.6$ nC/m², $\mathbf{J}_s(P) = 30\hat{z}$ A/m; $\rho_s(Q) = -88.5$ nC/m², $\mathbf{J}_s(Q) = -10\hat{z}$ A/m. (c) $\pm3.34$ nC/m and 0.377 A, along $+\hat{z}$ on the inner wire and $-\hat{z}$ on the outer conductor: equal and opposite, so there is no field outside.

## Hard

### 16.9 A leaky capacitor and its leads

> [!hard] Hard · displacement current · relaxation time · conductance
> A parallel-plate capacitor has circular plates of radius $a = 5$ cm in the planes $z = 0$ and $z = d = 1$ mm (fringing negligible). The gap is filled with a slightly conducting dielectric, $\epsilon = 4\epsilon_0$ and $\sigma = 2000\,\epsilon_0\approx1.77\times10^{-8}$ S/m. Thin leads run along the $z$ axis, up from the centre of the top plate and down from the centre of the bottom plate, to a resistor $R = 10$ MΩ far away. At $t = 0$ the top plate is at $V_0 = 100$ V relative to the bottom plate; the capacitor then discharges, through $R$ and through its own dielectric. (Calculator problem.)
>
> (a) Find $C$, the leakage resistance $R_\ell$ of the dielectric, the relaxation time $\epsilon/\sigma$, and $V(t)$.
>
> (b) Find, with directions, the lead current $I_R(t)$, the conduction current density $\mathbf{J}$ and the displacement current density $\partial\mathbf{D}/\partial t$ in the gap. Show that $\mathbf{J}+\partial\mathbf{D}/\partial t$ is uniform over the plates and carries exactly $I_R$. Evaluate the three densities at $t = 0$.
>
> (c) Use the Ampère–Maxwell law to find $\mathbf{H}$ in the gap for $r<a$ and for $r>a$, and evaluate $H$ at $r = 2.5$ cm at $t = 0$.
>
> (d) If the leads are cut, a conduction current still crosses the gap. What is $\mathbf{H}$ then, and why?
>
> *Source: original.*

> [!hint]- Hint
> Charge balance for the top plate: it loses charge through the lead *and* through the dielectric, $-dQ/dt = I_R+I_\ell$. In the gap $\mathbf{J} = \sigma\mathbf{E}$ points from the positive plate to the negative one, while $\partial\mathbf{D}/\partial t$ points the other way, because $\mathbf{D}$ is shrinking.

> [!solution]- Solution
> **Setup.** Let the top plate be at potential $V(t)$ with charge $+Q = CV$. In the gap $\mathbf{E} = -(V/d)\,\hat{z}$ and $\mathbf{D} = -(Q/A)\,\hat{z}$, both uniform, with $A = \pi a^2 = 7.854\times10^{-3}$ m².
>
> **(a)** $C = \epsilon A/d = 278$ pF. The dielectric is a resistor of length $d$ and cross-section $A$: $R_\ell = d/(\sigma A) = 7.19$ MΩ. Note $R_\ell C = \epsilon/\sigma = 4\epsilon_0/(2000\,\epsilon_0) = 2$ ms, the relaxation time of [[1-electrostatics/08-conductors-dielectrics-and-polarization|Lecture 8]] (this is $G/C = \sigma/\epsilon$ from [[1-electrostatics/10-capacitance-and-conductance|Lecture 10]]). The top plate's charge balance, $C\,dV/dt = -V/R-V/R_\ell$, gives
> $$
> V(t) = V_0e^{-t/\tau},\qquad \frac1\tau = \frac{1}{RC}+\frac{\sigma}{\epsilon} = 359.5+500 = 859.5\ \text{s}^{-1},\qquad \tau = 1.16\ \text{ms}.
> $$
> **(b)** Positive charge leaves the top plate up the upper lead, passes through $R$, and enters the bottom plate from below: the current is along $+\hat{z}$ in both leads, $I_R = V/R = 10\,e^{-t/\tau}$ μA. In the gap,
> $$
> \mathbf{J} = \sigma\mathbf{E} = -\frac{\sigma V}{d}\,\hat{z}\quad(\text{down; in total } I_\ell = V/R_\ell),\qquad \frac{\partial\mathbf{D}}{\partial t} = -\frac{1}{A}\frac{dQ}{dt}\,\hat{z} = +\frac{I_R+I_\ell}{A}\,\hat{z}\quad(\text{up}).
> $$
> Adding, $\mathbf{J}+\partial\mathbf{D}/\partial t = (I_R/A)\,\hat{z}$: uniform, along $+\hat{z}$, and carrying exactly the lead current. At $t = 0$: $I_\ell = 13.9$ μA, $\mathbf{J} = -1.771\,\hat{z}$ mA/m², $\partial\mathbf{D}/\partial t = +3.044\,\hat{z}$ mA/m², and the sum is $+1.273\,\hat{z}$ mA/m² $= I_R/A$ ✓. The total current $\mathbf{J}+\partial\mathbf{D}/\partial t$ runs up the lower lead, across the gap and up the upper lead without a break; it has zero divergence, as the divergence of the Ampère–Maxwell law requires.
>
> **(c)** Circle of radius $r$ in the gap, counter-clockwise seen from $+z$, flat disk as the surface:
> $$
> H_\phi\cdot2\pi r = \frac{I_R}{A}\,\pi r^2\ \ \Rightarrow\ \ \mathbf{H} = \frac{I_Rr}{2\pi a^2}\,\hat\phi\quad(r<a),\qquad \mathbf{H} = \frac{I_R}{2\pi r}\,\hat\phi\quad(r>a).
> $$
> At $r = 2.5$ cm and $t = 0$: $H = \dfrac{10^{-5}\times0.025}{2\pi(0.05)^2} = 15.9$ μA/m (31.8 μA/m at the plate edge). Only the lead current matters; the leakage current is invisible to $\mathbf{H}$.
>
> **Check (two surfaces):** take a circle of radius 7 cm around the upper lead, above the capacitor. The flat disk it bounds is pierced by the lead: MMF $= I_R = 10$ μA at $t = 0$. A bag hanging down from the same circle and crossing the gap is pierced by no wire; it collects conduction $-13.9$ μA and displacement $+23.9$ μA: again 10 μA ✓.
>
> **(d)** With the leads cut, $I_R = 0$ and $V$ decays with the relaxation time $\epsilon/\sigma = 2$ ms. Now $\partial\mathbf{D}/\partial t = -\mathbf{J}$ at every point, so $\nabla\times\mathbf{H} = 0$ everywhere and, by the symmetry, $\mathbf{H} = 0$. Counting the conduction current alone would give $H = 22.1$ μA/m at $r = 2.5$ cm at $t = 0$; the displacement current gives exactly the opposite. The capacitor discharges through itself without making any magnetic field.
>
> **Watch out:** $\mathbf{J}$ and $\partial\mathbf{D}/\partial t$ point in opposite directions here. Adding their magnitudes, or forgetting $\mathbf{J}$, gives the wrong source for $\mathbf{H}$. In the limit $\sigma\to0$ you recover the ordinary capacitor: $\mathbf{J} = 0$ and $\partial\mathbf{D}/\partial t = (I_R/A)\,\hat{z}$.
>
> **Answer.** (a) $C = 278$ pF, $R_\ell = 7.19$ MΩ, $\epsilon/\sigma = 2$ ms, $V = 100\,e^{-t/\tau}$ V with $\tau = 1.16$ ms. (b) $I_R = 10\,e^{-t/\tau}$ μA along $+\hat{z}$; $\mathbf{J}$ along $-\hat{z}$, $\partial\mathbf{D}/\partial t$ along $+\hat{z}$, and their sum is $(I_R/\pi a^2)\,\hat{z}$; at $t = 0$ these are $-1.771$, $+3.044$ and $+1.273$ mA/m². (c) $\mathbf{H} = I_Rr/(2\pi a^2)\,\hat\phi$ for $r<a$ and $I_R/(2\pi r)\,\hat\phi$ for $r>a$; 15.9 μA/m at 2.5 cm at $t = 0$. (d) $\mathbf{H} = 0$: conduction and displacement current cancel at every point.

### 16.10 MMF around a discharging pair

> [!hard] Hard · displacement current · solid angle · Biot–Savart
> Two small metal spheres sit on the $z$ axis at $z = +b$ and $z = -b$, with $b = 3$ cm, joined by a thin straight resistive wire along the axis. The upper sphere holds $+Q(t)$ and the lower one $-Q(t)$, with $Q(t) = Q_0e^{-t/\tau}$, $Q_0 = 10$ nC and $\tau = 5$ μs, as the pair discharges through the wire. Free space; treat the spheres as point charges and ignore any charge on the wire. $C$ is the circle of radius $a = 4$ cm in the plane $z = 0$, centred on the axis and traversed counter-clockwise seen from $+z$.
>
> (a) Find the current $I(t)$ in the wire and its direction.
>
> (b) Find the MMF $\oint_C\mathbf{H}\cdot d\mathbf{l}$ from the Ampère–Maxwell law, using the flat disk bounded by $C$.
>
> (c) Repeat with a cup: the cylinder $r = a$, $-L<z<0$, closed by the disk $z = -L$, $r<a$, with $L = 5$ cm. Why is there no conduction term this time?
>
> (d) Check (b) with the Biot–Savart law for the wire.
>
> (e) A second circle $C'$, also of radius 4 cm, centred on the axis and counter-clockwise seen from $+z$, lies in the plane $z = 6$ cm, above the upper sphere. No current crosses the flat disk it bounds. Find its MMF at $t = 0$ (calculator). What would the static Ampère's law say?
>
> *Source: Lecture 16 slides, the draining-charge MMF example, re-posed with two charges, a finite wire and a cup-shaped surface.*

> [!hint]- Hint
> A point charge $q$ sends the fraction $\tfrac12(1-\cos\theta_0)$ of its flux through a disk that subtends a cone of half-angle $\theta_0$ at the charge. For the cup, apply Gauss's law to the closed surface "disk + cup", and keep track of which way $C$ orients each piece.

> [!solution]- Solution
> **Setup.** $\text{MMF} = \oint_C\mathbf{H}\cdot d\mathbf{l} = \displaystyle\int_S\mathbf{J}\cdot d\mathbf{S}+\frac{d}{dt}\int_S\mathbf{D}\cdot d\mathbf{S}$ for *any* surface $S$ bounded by $C$, with $d\mathbf{S}$ oriented from $C$ by the right-hand rule ("upward").
>
> **(a)** Charge conservation for a surface around the upper sphere: $I = -dQ/dt = (Q_0/\tau)e^{-t/\tau} = 2\,e^{-t/\tau}$ mA, flowing from the positive sphere down to the negative one, i.e. along $-\hat{z}$ in the wire.
>
> **(b) Flat disk,** $d\mathbf{S} = \hat{z}\,dS$. *Conduction:* the wire crosses the disk going down, $\int\mathbf{J}\cdot d\mathbf{S} = -I$. *Displacement:* each charge is $b = 3$ cm from the disk, which it sees as a cone of half-angle $\theta_0$ with $\cos\theta_0 = b/\sqrt{a^2+b^2} = 3/5$. The field of $+Q$ (above) crosses the disk downward, and so does the field of $-Q$ (below), which points toward it:
> $$
> \psi_E = -\frac Q2(1-\cos\theta_0)-\frac Q2(1-\cos\theta_0) = -Q(1-\cos\theta_0) = -0.4\,Q,\qquad \frac{d\psi_E}{dt} = -0.4\frac{dQ}{dt} = +0.4\,I,
> $$
> $$
> \text{MMF} = -I+0.4\,I = -0.6\,I = -I\cos\theta_0 = -1.2\ \text{mA at}\ t = 0 .
> $$
> It is negative: $\mathbf{H}$ circulates clockwise seen from $+z$, as the right-hand rule for a downward current says.
>
> **(c) Cup.** The wire runs inside the region enclosed by "disk + cup" and ends on the lower sphere, which is inside it too ($L>b$), so the wire never crosses the cup: no conduction term. Gauss's law for that closed surface, with outward normals, reads $\psi_{\text{disk}}+\psi_{\text{cup,out}} = -Q$ (the lower sphere's charge). $C$ orients the cup *into* the enclosed region, opposite to its outward normal, so
> $$
> \psi_{\text{cup}} = -\psi_{\text{cup,out}} = \psi_{\text{disk}}+Q = 0.6\,Q,\qquad \text{MMF} = \frac{d}{dt}(0.6\,Q) = -0.6\,I .
> $$
> The same answer ✓ (a direct numerical integration gives $0.376\,Q$ through the side wall and $0.224\,Q$ through the bottom). The disk sees the wire; the cup sees the charge of the lower sphere changing instead. The static Ampère's law would have given $-I$ for the disk and $0$ for the cup.
>
> **(d)** For a straight segment seen from a point at perpendicular distance $a$, $H = \dfrac{I}{4\pi a}(\sin\alpha_2-\sin\alpha_1)$, with the angles to the two ends measured from the perpendicular. Here $\sin\alpha_2 = -\sin\alpha_1 = b/\sqrt{a^2+b^2} = 0.6$, and the current flows along $-\hat{z}$:
> $$
> H_\phi = -\frac{I}{4\pi a}(2\times0.6) = -\frac{0.6\,I}{2\pi a}\quad\Big(-\frac{15}{\pi} = -4.77\ \text{mA/m at}\ t = 0\Big),\qquad \oint_C\mathbf{H}\cdot d\mathbf{l} = 2\pi aH_\phi = -0.6\,I .
> $$
> It agrees with (b) ✓. The wire alone gives the whole field: the displacement current of each sphere's shrinking Coulomb field is radial and spherically symmetric about that sphere, and makes no $\mathbf{H}$.
>
> **(e)** For $C'$ at $z = 6$ cm the upper sphere is 3 cm below the disk and the lower one 9 cm below it: $\cos\theta_1 = 3/5$ and $\cos\theta_2 = 9/\sqrt{97} = 0.914$. Now the field of $+Q$ crosses the disk upward and that of $-Q$ downward:
> $$
> \psi_E = \frac Q2(1-\cos\theta_1)-\frac Q2(1-\cos\theta_2) = (0.2-0.0431)\,Q = 0.157\,Q,\qquad \text{MMF}' = 0.157\frac{dQ}{dt} = -0.157\,I = -0.314\ \text{mA at}\ t = 0 .
> $$
> The static Ampère's law would say zero, since no current crosses the disk; the whole MMF here is displacement current. Biot–Savart agrees: $\tfrac I2(\cos\theta_1-\cos\theta_2) = -0.157\,I$.
>
> **Check (limits):** as $a\to0$ the MMF around $C$ tends to $-I$, the bare wire. As $a\to\infty$, $\cos\theta_0\to0$ and the MMF tends to 0: a huge disk catches half the flux of each sphere, and the resulting displacement current cancels the wire current.
>
> **Answer.** (a) $I = 2\,e^{-t/\tau}$ mA along $-\hat{z}$. (b) $\text{MMF} = -I+0.4\,I = -I\cos\theta_0 = -0.6\,I$, i.e. $-1.2$ mA at $t = 0$ (clockwise seen from $+z$). (c) The same, with no conduction term: $d(0.6\,Q)/dt = -0.6\,I$. (d) $H_\phi = -0.6\,I/(2\pi a) = -4.77$ mA/m at $t = 0$, and $2\pi aH_\phi = -0.6\,I$ ✓. (e) $-0.157\,I = -0.314$ mA at $t = 0$, where the static Ampère's law would say 0.

### 16.11 A region with no conduction current

> [!hard] Hard · displacement current · divergence · Faraday's law
> In a region $V$ of free space there is no conduction current: $\mathbf{J} = 0$ at every point of $V$ at all times (any charge in $V$ is held in place).
>
> (a) For contrast, suppose first that a conduction current $\mathbf{J} = J_0(x\hat{x}+y\hat{y})$, with $J_0 = 2$ μA/m² and coordinates in metres, did flow in $V$. Take the divergence of the Ampère–Maxwell law and find $\partial\rho/\partial t$. Which of these could then hold throughout $V$: (i) $\partial\mathbf{D}/\partial t = 0$; (ii) $\nabla\cdot\mathbf{D} = 0$ at all times; (iii) $\nabla\times\mathbf{H} = \mathbf{J}$; (iv) $\nabla\times\mathbf{H} = 0$?
>
> (b) From here on $\mathbf{J} = 0$, as stated. Let $V$ be the cube $\lvert x\rvert,\lvert y\rvert,\lvert z\rvert<1$ m. Three displacement fields are proposed for $0<t<T$, with $D_0 = 2$ nC/m², $T = 1$ ms and coordinates in metres:
> $$
> \mathbf{D}_A = D_0\frac tT(x\hat{x}+y\hat{y}),\qquad \mathbf{D}_B = D_0\Big(x\hat{x}+y\hat{y}+\frac tT\hat{z}\Big),\qquad \mathbf{D}_C = D_0\frac tT(y\hat{x}+x\hat{y}).
> $$
> For each, find $\rho$ and decide whether it is compatible with $\mathbf{J} = 0$.
>
> (c) For $\mathbf{D}_C$, find $\mathbf{H}$, given that it points along $\hat{z}$, depends only on $x$ and $y$, and vanishes on the $z$ axis. Evaluate it at $(1,0,0)$ m and $(0,1,0)$ m.
>
> (d) Show that $\mathbf{E} = \mathbf{D}_C/\epsilon_0$ and $\mathbf{B} = \mu_0\mathbf{H}$ satisfy all four Maxwell equations in $V$ with $\rho = 0$ and $\mathbf{J} = 0$. Which of the four is not automatic?
>
> (e) Taking the divergence of Faraday's law constrains $\mathbf{B}$ in the same way. A classmate proposes $\mathbf{B}_1 = B_0\dfrac tT(x\hat{x}+y\hat{y})$ and the static $\mathbf{B}_2 = B_0(x\hat{x}+y\hat{y})$ for $V$. Which one does Faraday's law rule out, and what rules out the other?
>
> *Source: SP18 Exam 2 #1(iv), re-parameterized (a spreading current in place of J = 0, and new options) and extended with candidate fields for J = 0, H and a full Maxwell check.*

> [!hint]- Hint
> The divergence of any curl is zero, and Gauss's law turns $\nabla\cdot\mathbf{D}$ into $\rho$. For (c), $\nabla\times(H_z\hat{z}) = \dfrac{\partial H_z}{\partial y}\hat{x}-\dfrac{\partial H_z}{\partial x}\hat{y}$: match both components to $\partial\mathbf{D}_C/\partial t$ and integrate.

> [!solution]- Solution
> **(a)** The divergence of a curl is zero, and Gauss's law turns $\nabla\cdot\mathbf{D}$ into $\rho$:
> $$
> 0 = \nabla\cdot(\nabla\times\mathbf{H}) = \nabla\cdot\mathbf{J}+\frac{\partial}{\partial t}\nabla\cdot\mathbf{D} = \nabla\cdot\mathbf{J}+\frac{\partial\rho}{\partial t},\qquad \frac{\partial\rho}{\partial t} = -\nabla\cdot\mathbf{J} = -2J_0 = -4\ \mu\text{A/m}^3 .
> $$
> The current spreads out from the $z$ axis, so the charge density drains away at 4 μA/m³ (C/m³ per second) everywhere in $V$.
>
> - (i) **Cannot hold:** $\nabla\cdot(\partial\mathbf{D}/\partial t) = \partial\rho/\partial t\neq0$, so $\partial\mathbf{D}/\partial t$ cannot vanish throughout $V$.
> - (ii) **Cannot hold:** $\rho = \nabla\cdot\mathbf{D}$ changes in time, so it can be zero at one instant at most.
> - (iii) **Cannot hold:** this is the static Ampère's law. Its divergence demands $\nabla\cdot\mathbf{J} = 0$, which fails here because charge leaves every point — the inconsistency that Maxwell's term repairs.
> - (iv) **Can hold**, if $\partial\mathbf{D}/\partial t = -\mathbf{J} = -J_0(x\hat{x}+y\hat{y})$: its divergence, $-2J_0$, is exactly the required $\partial\rho/\partial t$. The displacement current then cancels the conduction current at every point, as in the leaky capacitor of 16.9(d) with its leads cut. Faraday's law is satisfied too: $x\hat{x}+y\hat{y}$ has no curl, so $\mathbf{E}$ stays curl-free and $\mathbf{B}$ static.
>
> **(b)** With $\mathbf{J} = 0$ the identity in (a) leaves $\partial\rho/\partial t = 0$: a field is compatible only if its charge density does not change.
> - $\mathbf{D}_A$: $\rho = \nabla\cdot\mathbf{D}_A = 2D_0t/T$, growing at $\partial\rho/\partial t = 2D_0/T = 4$ μA/m³. That would need $\nabla\cdot\mathbf{J} = -4$ μA/m³, a current converging on the $z$ axis (the reverse of (a)): **not compatible**. Equivalently, $\partial\mathbf{D}_A/\partial t$ has a nonzero divergence, so it cannot be the curl of any $\mathbf{H}$.
> - $\mathbf{D}_B$: $\rho = 2D_0 = 4$ nC/m³, constant in time: **compatible** — charge at rest plus a uniform field ramping along $z$, matched by $\mathbf{H} = \frac{D_0}{2T}(-y\hat{x}+x\hat{y})$, whose curl is $(D_0/T)\,\hat{z}$.
> - $\mathbf{D}_C$: $\rho = D_0\frac tT\Big(\dfrac{\partial y}{\partial x}+\dfrac{\partial x}{\partial y}\Big) = 0$: **compatible**.
>
> **(c)** $\partial\mathbf{D}_C/\partial t = \dfrac{D_0}{T}(y\hat{x}+x\hat{y})$. Matching the components of $\nabla\times(H_z\hat{z})$:
> $$
> \frac{\partial H_z}{\partial y} = \frac{D_0}{T}\,y,\qquad -\frac{\partial H_z}{\partial x} = \frac{D_0}{T}\,x\qquad\Rightarrow\qquad H_z = \frac{D_0}{2T}\big(y^2-x^2\big)+\text{const},
> $$
> and the constant is zero because $\mathbf{H} = 0$ on the $z$ axis. Numerically $D_0/(2T) = 10^{-6}$, so with $x$ and $y$ in metres $\mathbf{H} = 10^{-6}(y^2-x^2)\,\hat{z}$ A/m: $\mathbf{H}(1,0,0) = -1\,\hat{z}$ μA/m and $\mathbf{H}(0,1,0) = +1\,\hat{z}$ μA/m.
>
> **(d)** Gauss: $\nabla\cdot\mathbf{D}_C = 0 = \rho$ ✓. No magnetic charge: $\nabla\cdot\mathbf{B} = \mu_0\,\partial H_z/\partial z = 0$ ✓. Ampère–Maxwell: $\nabla\times\mathbf{H} = \partial\mathbf{D}_C/\partial t = \mathbf{J}+\partial\mathbf{D}/\partial t$ ✓, by construction. **Faraday's law is the one that is not automatic:** $\nabla\times\mathbf{E} = \dfrac{D_0t}{\epsilon_0T}\Big(\dfrac{\partial x}{\partial x}-\dfrac{\partial y}{\partial y}\Big)\hat{z} = 0$, and $-\partial\mathbf{B}/\partial t = 0$ only because $\mathbf{H}$ does not depend on time ✓. That is thanks to the linear ramp. Had $\mathbf{D}$ grown like $t^2$ or $\sin\omega t$, $\mathbf{H}$ would change in time, and Faraday's law would demand a curl in $\mathbf{E}$ that $\mathbf{D}_C$ does not have: changing $\mathbf{E}$ makes $\mathbf{H}$, changing $\mathbf{H}$ makes $\mathbf{E}$ — the coupling that leads to waves.
>
> **Check (Stokes):** take the unit square in the plane $x = 0$ with corners $(0,0,0)$, $(0,1,0)$, $(0,1,1)$, $(0,0,1)$, traversed in that order (normal $+\hat{x}$). The displacement current through it is $\int_0^1\!\int_0^1\frac{D_0}{T}\,y\,dy\,dz = 1$ μA. Around it, only the two edges along $z$ count, each 1 m long: $H_z(0,1)\times1\ \text{m}-H_z(0,0)\times1\ \text{m} = 1$ μA ✓.
>
> **(e)** $\nabla\cdot(\nabla\times\mathbf{E}) = 0$ gives $\dfrac{\partial}{\partial t}(\nabla\cdot\mathbf{B}) = 0$. $\mathbf{B}_1$ has $\nabla\cdot\mathbf{B}_1 = 2B_0t/T$, which changes in time: **Faraday's law rules it out** — no $\mathbf{E}$ has a curl equal to $-\partial\mathbf{B}_1/\partial t$, whose divergence is $-2B_0/T\neq0$. $\mathbf{B}_2$ has $\nabla\cdot\mathbf{B}_2 = 2B_0$, constant, so Faraday's law is satisfied (with any static, curl-free $\mathbf{E}$). What rules $\mathbf{B}_2$ out is $\nabla\cdot\mathbf{B} = 0$ itself: its field lines would start on magnetic charge inside $V$, and none has ever been observed.
>
> **Answer.** (a) $\partial\rho/\partial t = -\nabla\cdot\mathbf{J} = -4$ μA/m³; (i)–(iii) cannot hold; (iv) can, with $\partial\mathbf{D}/\partial t = -\mathbf{J}$ cancelling the conduction current. (b) $\mathbf{D}_A$: $\rho = 2D_0t/T$, changing at 4 μA/m³, impossible; $\mathbf{D}_B$: $\rho = 4$ nC/m³, static, allowed; $\mathbf{D}_C$: $\rho = 0$, allowed. (c) $\mathbf{H} = \dfrac{D_0}{2T}(y^2-x^2)\,\hat{z} = 10^{-6}(y^2-x^2)\,\hat{z}$ A/m: $-1\,\hat{z}$ μA/m at $(1,0,0)$ and $+1\,\hat{z}$ μA/m at $(0,1,0)$. (d) All four hold; Faraday's law holds only because the linear ramp makes $\mathbf{H}$ static. (e) Faraday's law rules out $\mathbf{B}_1$; $\mathbf{B}_2$ passes Faraday's law but violates $\nabla\cdot\mathbf{B} = 0$ (it would need magnetic charge).

### 16.12 Four conditions at a tilted interface

> [!hard] Hard · boundary conditions · oblique interface · current sheet
> The plane $2x-y+2z = 0$ separates two dielectrics, both with $\mu = \mu_0$: medium 1 (the side $2x-y+2z>0$) has $\epsilon_1 = 2\epsilon_0$, and medium 2 has $\epsilon_2 = 5\epsilon_0$. The interface carries free surface charge and surface current. At an instant $t_0$, at the point $P$ at the origin, the free surface charge density is $\rho_s = 3000\,\epsilon_0$ C/m² ($\approx26.6$ nC/m²), the surface current density is $\mathbf{J}_s = \hat{x}+4\hat{y}+\hat{z}$ A/m, and just on the medium-2 side of $P$
> $$
> \mathbf{E}_2 = 4\hat{x}+\hat{y}+\hat{z}\ \text{kV/m},\qquad \mathbf{H}_2 = 5\hat{x}+4\hat{z}\ \text{A/m}.
> $$
>
> (a) Find $\hat{n}$ (from medium 2 into medium 1), check that $\mathbf{J}_s$ lies in the interface, and split $\mathbf{E}_2$ and $\mathbf{H}_2$ into normal and tangential parts.
>
> (b) Find $\mathbf{E}_1$ and $\mathbf{D}_1$ just on the medium-1 side of $P$.
>
> (c) Find $\mathbf{H}_1$ and $\mathbf{B}_1$.
>
> (d) Find the bound surface charge density at $P$ and the total (free plus bound) surface charge density, and check the total against $\epsilon_0\hat{n}\cdot(\mathbf{E}_1-\mathbf{E}_2)$.
>
> (e) The fields change with time. Explain why neither $\partial\mathbf{D}/\partial t$ nor $\partial\mathbf{B}/\partial t$ appears in any of the four conditions you used.
>
> *Source: SP18 Exam 2 #1(vi) style (H across a current sheet), extended to all four conditions on a tilted interface between dielectrics.*

> [!hint]- Hint
> For any vector $\mathbf{X}$, the normal part is $(\hat{n}\cdot\mathbf{X})\,\hat{n}$ and the tangential part is the rest. $\mathbf{E}_t$ and $B_n$ carry over unchanged; $D_n$ jumps by $\rho_s$; and when $\mathbf{J}_s$ lies in the interface, $\hat{n}\times(\mathbf{H}_1-\mathbf{H}_2) = \mathbf{J}_s$ is solved by $\mathbf{H}_{1t}-\mathbf{H}_{2t} = \mathbf{J}_s\times\hat{n}$.

> [!solution]- Solution
> **(a)** The gradient of $2x-y+2z$ points toward medium 1: $\hat{n} = \tfrac13(2\hat{x}-\hat{y}+2\hat{z})$. $\hat{n}\cdot\mathbf{J}_s = \tfrac13(2-4+2) = 0$ ✓. Then
> $$
> \hat{n}\cdot\mathbf{E}_2 = \tfrac13(8-1+2) = 3\ \text{kV/m}:\qquad \mathbf{E}_{2n} = 2\hat{x}-\hat{y}+2\hat{z},\qquad \mathbf{E}_{2t} = 2\hat{x}+2\hat{y}-\hat{z}\ \ \text{(kV/m)};
> $$
> $$
> \hat{n}\cdot\mathbf{H}_2 = \tfrac13(10+0+8) = 6\ \text{A/m}:\qquad \mathbf{H}_{2n} = 4\hat{x}-2\hat{y}+4\hat{z},\qquad \mathbf{H}_{2t} = \hat{x}+2\hat{y}\ \ \text{(A/m)}.
> $$
> **(b)** $\hat{n}\times(\mathbf{E}_1-\mathbf{E}_2) = 0$ gives $\mathbf{E}_{1t} = \mathbf{E}_{2t}$. $\hat{n}\cdot(\mathbf{D}_1-\mathbf{D}_2) = \rho_s$ gives the normal part:
> $$
> 2\epsilon_0E_{1n}-5\epsilon_0(3000) = 3000\,\epsilon_0\ \Rightarrow\ E_{1n} = 9\ \text{kV/m},\qquad \mathbf{E}_1 = 9\hat{n}+\mathbf{E}_{2t} = (6\hat{x}-3\hat{y}+6\hat{z})+(2\hat{x}+2\hat{y}-\hat{z}) = 8\hat{x}-\hat{y}+5\hat{z}\ \text{kV/m}.
> $$
> $\mathbf{D}_1 = 2\epsilon_0\mathbf{E}_1 = \epsilon_0(16\hat{x}-2\hat{y}+10\hat{z})\times10^3$ C/m² $\approx141.7\hat{x}-17.7\hat{y}+88.5\hat{z}$ nC/m² (for comparison, $\mathbf{D}_2 = \epsilon_0(20\hat{x}+5\hat{y}+5\hat{z})\times10^3$ C/m²).
>
> **(c)** $\hat{n}\cdot(\mathbf{B}_1-\mathbf{B}_2) = 0$ with $\mu_0$ on both sides: $H_{1n} = H_{2n} = 6$ A/m. For the tangential part,
> $$
> \mathbf{J}_s\times\hat{n} = \tfrac13(\hat{x}+4\hat{y}+\hat{z})\times(2\hat{x}-\hat{y}+2\hat{z}) = \tfrac13(9\hat{x}+0\,\hat{y}-9\hat{z}) = 3\hat{x}-3\hat{z}\ \text{A/m},
> $$
> $$
> \mathbf{H}_1 = \mathbf{H}_{2n}+\mathbf{H}_{2t}+\mathbf{J}_s\times\hat{n} = (4\hat{x}-2\hat{y}+4\hat{z})+(\hat{x}+2\hat{y})+(3\hat{x}-3\hat{z}) = 8\hat{x}+\hat{z}\ \text{A/m},
> $$
> and $\mathbf{B}_1 = \mu_0\mathbf{H}_1\approx10.05\hat{x}+1.257\hat{z}$ μT.
>
> **Check:** $\hat{n}\times(\mathbf{H}_1-\mathbf{H}_2) = \tfrac13(2\hat{x}-\hat{y}+2\hat{z})\times(3\hat{x}-3\hat{z}) = \tfrac13(3\hat{x}+12\hat{y}+3\hat{z}) = \hat{x}+4\hat{y}+\hat{z} = \mathbf{J}_s$ ✓, and $\hat{n}\cdot\mathbf{H}_1 = \tfrac13(16+0+2) = 6$ A/m ✓.
>
> **(d)** $\mathbf{P}_1 = (\epsilon_1-\epsilon_0)\mathbf{E}_1 = \epsilon_0\mathbf{E}_1$ and $\mathbf{P}_2 = 4\epsilon_0\mathbf{E}_2$. Each dielectric's bound surface charge is $\mathbf{P}\cdot\hat{n}_{\text{out}}$, and at the interface the outward normal of medium 2 is $+\hat{n}$ while that of medium 1 is $-\hat{n}$:
> $$
> \rho_{sb} = \hat{n}\cdot\mathbf{P}_2-\hat{n}\cdot\mathbf{P}_1 = 4\epsilon_0(3000)-\epsilon_0(9000) = 3000\,\epsilon_0\approx26.6\ \text{nC/m}^2 .
> $$
> Total: $\rho_s+\rho_{sb} = 6000\,\epsilon_0\approx53.1$ nC/m². Check: $\epsilon_0\hat{n}\cdot(\mathbf{E}_1-\mathbf{E}_2) = \epsilon_0(9000-3000) = 6000\,\epsilon_0$ ✓ — Gauss's law for $\epsilon_0\mathbf{E}$ counts free and bound charge alike.
>
> **(e)** Each condition comes from an integral law applied to a vanishing pillbox or loop. Gauss's law for $\mathbf{D}$ and $\oint\mathbf{B}\cdot d\mathbf{S} = 0$ contain no time derivatives at all. Faraday's law and the Ampère–Maxwell law on a thin rectangle of width $w$ straddling the interface contain the fluxes of $\partial\mathbf{B}/\partial t$ and $\partial\mathbf{D}/\partial t$ through the rectangle; for finite fields these are proportional to $w$ and vanish as $w\to0$. Only the surface current, which crosses the rectangle however thin it is, survives. So the same four conditions hold at every instant, static or not.
>
> **Answer.** (a) $\hat{n} = \tfrac13(2\hat{x}-\hat{y}+2\hat{z})$; $\mathbf{E}_2 = (2\hat{x}-\hat{y}+2\hat{z})+(2\hat{x}+2\hat{y}-\hat{z})$ kV/m and $\mathbf{H}_2 = (4\hat{x}-2\hat{y}+4\hat{z})+(\hat{x}+2\hat{y})$ A/m (normal + tangential). (b) $\mathbf{E}_1 = 8\hat{x}-\hat{y}+5\hat{z}$ kV/m, $\mathbf{D}_1 = \epsilon_0(16\hat{x}-2\hat{y}+10\hat{z})\times10^3$ C/m². (c) $\mathbf{H}_1 = 8\hat{x}+\hat{z}$ A/m, $\mathbf{B}_1\approx10.05\hat{x}+1.257\hat{z}$ μT. (d) $\rho_{sb} = 3000\,\epsilon_0\approx26.6$ nC/m²; total $6000\,\epsilon_0\approx53.1$ nC/m². (e) The pillbox laws contain no time derivative, and the time-derivative fluxes through the thin rectangle vanish with its width.

### Sources for this page
Course notes and slides for Lecture 16: the unit-cube continuity example of the slides (16.1, re-posed in a cylinder with a sign change), the perfect-conductor challenge question (16.5, re-posed on a sphere with vectors) and the draining-charge MMF example (16.10, re-posed with two charges, a finite wire and a cup-shaped surface, so that it differs from the site's worked problem [[problems/mmf-around-a-draining-charge]]). The Lecture 13 slides, as quoted in Lecture 16: the displacement current through an area (16.2, with a sinusoidal, tilted field). Old exams: SP18 Exam 2 #1(iv) (16.11, re-parameterized with a spreading current in place of $\mathbf{J} = 0$ and new options, and extended with candidate fields for $\mathbf{J} = 0$, $\mathbf{H}$ and a full Maxwell check), and the style of SP18 Exam 2 #1(vi), $\mathbf{H}$ across a current sheet (16.12, extended to all four conditions on a tilted interface between dielectrics). Classic problems with new material, numbers or a twist: conduction versus displacement current in a lossy medium (16.6) and the charging capacitor (16.7, with a dielectric core added). Original: 16.3 and 16.9; 16.4, drawn from the Lecture 16 course notes; and 16.8, which extends the slides' surface-charge exercise to surface currents on a coax.

*Previous: [[practice/15-inductance-and-magnetic-energy|Lecture 15 practice]] · next: [[practice/17-magnetization-and-maxwell-in-matter|Lecture 17 practice]] · [[practice/index|all practice]]*
