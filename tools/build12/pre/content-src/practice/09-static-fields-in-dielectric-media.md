---
title: "Practice — Lecture 9: Static fields in dielectric media"
description: "12 practice problems (5 easy, 3 medium, 4 hard) on the D-first chain through layered and side-by-side dielectrics, refraction of field lines, graded permittivity, bound charge on faces and inside, and dielectric-filled spheres and coaxes, each with a folded hint and a worked solution."
tags: [practice, electrostatics, exam-1]
lecture: 9
---

*Practice for [[1-electrostatics/09-static-fields-in-dielectric-media|Lecture 9]] · concepts: [[concepts/electric-flux-density]] · [[concepts/permittivity]] · [[concepts/polarization]] · [[concepts/boundary-conditions]] · all practice: [[practice/index|hub]] · by difficulty: [[practice/easy|easy]] · [[practice/medium|medium]] · [[practice/hard|hard]] · [[practice/topics|by topic]]*

Work each problem on paper first. Open the **hint** only when stuck, and the **solution** only after you have an answer you would hand in. Every answer here has been checked numerically.

## Easy

### 9.1 Three layers between charged plates

> [!easy] Easy · D-first chain · layered dielectrics
> Two large conducting plates lie on the planes $z = 0$ and $z = 3$ m. The bottom plate carries $\rho_s = -6\epsilon_0$ C/m² on its upper face and is grounded, $V(0) = 0$; the top plate carries $+6\epsilon_0$ C/m² on its lower face. The gap holds three layers: free space for $0<z<1$ m, $\epsilon_r = 2$ for $1<z<2$ m, and $\epsilon_r = 3$ for $2<z<3$ m. (a) Find $\mathbf{D}$, $\mathbf{E}$ and $\mathbf{P}$ in each layer. (b) Find $V(1)$, $V(2)$ and $V(3)$.
>
> *Source: Summer 2020 HE2 #1a, re-parameterized (three layers instead of two).*

> [!hint]- Hint
> The free charge alone fixes $\mathbf{D}$; the layers only decide how $\mathbf{D}$ is turned into $\mathbf{E}$. Read $\mathbf{D}$ off the bottom plate with $\rho_s = \hat{n}\cdot\mathbf{D}$, where $\hat{n}$ points out of the metal.

> [!solution]- Solution
> **D.** Everything depends on $z$ only and the gap holds no free charge, so $D_z$ is the same in all three layers (normal $\mathbf{D}$ is continuous across the two charge-free interfaces). At the bottom plate $\hat{n} = +\hat{z}$ points from the metal into the gap: $\rho_s = \hat{z}\cdot\mathbf{D} = D_z = -6\epsilon_0$. So $\mathbf{D} = -6\epsilon_0\hat{z}$ C/m² $\approx-5.31\times10^{-11}\hat{z}$ C/m² in every layer, pointing from the positive top plate down to the negative bottom plate.
>
> **E and P, layer by layer**, from $\mathbf{E} = \mathbf{D}/(\epsilon_r\epsilon_0)$ and $\mathbf{P} = \mathbf{D}-\epsilon_0\mathbf{E}$:
> $$
> \begin{aligned}
> 0<z<1:&\quad \mathbf{E} = -6\hat{z}\ \text{V/m}, && \mathbf{P} = 0\\
> 1<z<2:&\quad \mathbf{E} = -3\hat{z}\ \text{V/m}, && \mathbf{P} = -6\epsilon_0\hat{z}+3\epsilon_0\hat{z} = -3\epsilon_0\hat{z}\ \text{C/m}^2\\
> 2<z<3:&\quad \mathbf{E} = -2\hat{z}\ \text{V/m}, && \mathbf{P} = -6\epsilon_0\hat{z}+2\epsilon_0\hat{z} = -4\epsilon_0\hat{z}\ \text{C/m}^2
> \end{aligned}
> $$
> **V.** $V(z)-V(0) = -\int_0^zE_z\,dz$, adding layer by layer: $V(1) = 0+6(1) = 6$ V, $V(2) = 6+3(1) = 9$ V, $V(3) = 9+2(1) = 11$ V.
>
> **Check:** at the top plate $\hat{n} = -\hat{z}$ (out of the metal), so $\rho_s = -\hat{z}\cdot\mathbf{D} = +6\epsilon_0$ ✓ — the top charge, never used, comes out right. The potential rises toward the positive plate, and the high-$\epsilon$ layers take the smaller share of the voltage.
>
> **Watch out:** $\mathbf{D}$ has no $\epsilon$ in it. Writing $D_z = -6\epsilon_0/\epsilon_r$ confuses $\mathbf{D}$ with $\epsilon_0\mathbf{E}$, a classic Exam 1 slip.
>
> **Answer.** $\mathbf{D} = -6\epsilon_0\hat{z}$ C/m² in all three layers; $\mathbf{E} = -6\hat{z}$, $-3\hat{z}$, $-2\hat{z}$ V/m; $\mathbf{P} = 0$, $-3\epsilon_0\hat{z}$, $-4\epsilon_0\hat{z}$ C/m²; $V(1) = 6$ V, $V(2) = 9$ V, $V(3) = 11$ V.

### 9.2 Two dielectrics side by side

> [!easy] Easy · side-by-side dielectrics · parallel plates
> Large parallel plates lie on $z = 0$ (grounded) and $z = 2$ mm (held at $+10$ V). The gap is filled with two dielectrics *side by side*: $\epsilon_r = 2$ for $x<0$ and $\epsilon_r = 5$ for $x>0$, so the interface $x = 0$ is perpendicular to the plates. Ignore fringing at the outer edges. (a) Find $\mathbf{E}$ in each half. (b) Find $\mathbf{D}$ in each half, and the free surface charge density on the top plate above each half. (c) Find $\mathbf{P}$ in each half.
>
> *Source: original.*

> [!hint]- Hint
> This time the interface is *parallel* to the field. Which boundary condition does the work there — tangential $\mathbf{E}$ or normal $\mathbf{D}$?

> [!solution]- Solution
> **(a)** Each half is a homogeneous, charge-free layer between the same two plates, so $V = V_0z/d$ satisfies Laplace's equation and both plate potentials in each half. It also satisfies the conditions at the interface $x = 0$: $\mathbf{E}$ points along $\hat{z}$, tangential to the interface, and is the same on both sides ($E_t$ continuous ✓), while $D_x = 0$ on both sides ($D_n$ continuous ✓). By uniqueness this is the field:
> $$
> \mathbf{E} = -\frac{V_0}{d}\hat{z} = -\frac{10}{2\times10^{-3}}\hat{z} = -5000\,\hat{z}\ \text{V/m}\quad\text{in both halves},
> $$
> pointing from the $+10$ V plate down to the grounded one.
>
> **(b)** $\mathbf{D} = \epsilon_r\epsilon_0\mathbf{E}$: $\ -10^4\epsilon_0\hat{z}\approx-88.5\hat{z}$ nC/m² for $x<0$ and $-2.5\times10^4\epsilon_0\hat{z}\approx-221\hat{z}$ nC/m² for $x>0$. On the top plate $\hat{n} = -\hat{z}$ points out of the metal, so $\rho_s = -\hat{z}\cdot\mathbf{D}$: $+88.5$ nC/m² above the $\epsilon_r = 2$ half and $+221$ nC/m² above the $\epsilon_r = 5$ half. The plate's charge is *not* uniform: it piles up where the material polarizes more.
>
> **(c)** $\mathbf{P} = \mathbf{D}-\epsilon_0\mathbf{E} = (\epsilon_r-1)\epsilon_0\mathbf{E}$: $\ -5000\epsilon_0\hat{z}\approx-44.3\hat{z}$ nC/m² for $x<0$ and $-2\times10^4\epsilon_0\hat{z}\approx-177\hat{z}$ nC/m² for $x>0$.
>
> **Check:** the dielectrics' top faces (outward normal $+\hat{z}$) carry bound charge $\rho_{sb} = \mathbf{P}\cdot\hat{z}$, i.e. $-44.3$ and $-177$ nC/m². Free plus bound at the top surface is $88.5-44.3 = 221-177\approx44.3$ nC/m² $= \epsilon_0\lvert\mathbf{E}\rvert$ over *both* halves — the same net charge, hence the same $\mathbf{E}$.
>
> **Watch out:** layers stacked *across* the field share $\mathbf{D}$ (as in 9.1); dielectrics side by side *along* the field share $\mathbf{E}$.
>
> **Answer.** $\mathbf{E} = -5000\hat{z}$ V/m in both halves; $\mathbf{D} = -10^4\epsilon_0\hat{z}\approx-88.5\hat{z}$ nC/m² ($x<0$) and $-2.5\times10^4\epsilon_0\hat{z}\approx-221\hat{z}$ nC/m² ($x>0$); top-plate $\rho_s = +88.5$ and $+221$ nC/m²; $\mathbf{P}\approx-44.3\hat{z}$ and $-177\hat{z}$ nC/m².

### 9.3 Laplace in a graded dielectric

> [!easy] Easy · multiple choice · inhomogeneous media
> A perfect dielectric whose permittivity varies with position, $\epsilon = \epsilon(x,y,z)$, fills a region that contains no free charge. Under static conditions, which equation must hold everywhere in the region, whatever the profile $\epsilon(x,y,z)$?
>
> (a) $\nabla^2V = 0$
>
> (b) $\nabla\cdot\mathbf{E} = 0$
>
> (c) $\nabla\cdot(\epsilon\nabla V) = 0$
>
> (d) $\nabla\cdot\mathbf{P} = 0$
>
> (e) None of these
>
> *Source: SP18 Exam 1 #1(i) style.*

> [!hint]- Hint
> Start from the one law that holds in any medium without free charge, and substitute $\mathbf{E} = -\nabla V$. At which step would you need $\epsilon$ to be constant?

> [!solution]- Solution
> **(c).** With no free charge $\nabla\cdot\mathbf{D} = 0$, and $\mathbf{D} = \epsilon\mathbf{E} = -\epsilon\nabla V$, so $\nabla\cdot(\epsilon\nabla V) = 0$ always. Expanded, it reads $\epsilon\nabla^2V+\nabla\epsilon\cdot\nabla V = 0$.
>
> Test the other options on Lecture 9's graded example, $\epsilon = 4\epsilon_0/(4-z)$ with $D_z = 2\epsilon_0$, where $E_z = 2(1-z/4)$ V/m:
>
> - (a) is false: getting $\nabla^2V$ means pulling $\epsilon$ out of the divergence, which needs $\epsilon$ constant. Here $\nabla^2V = -dE_z/dz = +\tfrac12$ V/m² $\ne0$.
> - (b) is false: $\epsilon_0\nabla\cdot\mathbf{E}$ counts *all* charge, and a graded medium carries bound charge. Here $\nabla\cdot\mathbf{E} = -\tfrac12$ V/m², i.e. $\rho_b = -\epsilon_0/2$ C/m³.
> - (d) is false for the same reason: $\nabla\cdot\mathbf{P} = -\rho_b = +\epsilon_0/2$ C/m³ $\ne0$.
> - (e) is false because (c) holds.
>
> Options (a), (b) and (d) do hold in special cases where $\nabla\epsilon\perp\mathbf{E}$ (dielectrics side by side, as in 9.2), but not in general. This is Lecture 9's rule: no Laplace or Poisson in an inhomogeneous medium.
>
> **Answer.** (c) $\nabla\cdot(\epsilon\nabla V) = 0$.

### 9.4 Which way does the field bend

> [!easy] Easy · multiple choice · refraction
> A thick glass plate ($\epsilon_r = 4$) with a flat face lies in air, and the face carries no free charge. Just outside the face the field is uniform, of magnitude $E_0$, and makes $45^\circ$ with the normal to the face. Which statement about the field just inside the glass is true?
>
> (a) It bends toward the normal, and its magnitude is less than $E_0$.
>
> (b) It bends away from the normal, and its magnitude is less than $E_0$.
>
> (c) It bends away from the normal, and its magnitude is greater than $E_0$.
>
> (d) It does not bend; its magnitude is $E_0/4$.
>
> (e) It bends toward the normal, and $\lvert\mathbf{D}\rvert$ is the same on both sides.
>
> *Source: original.*

> [!hint]- Hint
> Split the field into its part along the face and its part along the normal. One part is copied across the face; the other is scaled. Which one, and by what factor?

> [!solution]- Solution
> **(b).** Tangential $\mathbf{E}$ is continuous: $E_t = E_0\sin45^\circ = E_0/\sqrt2$ on both sides. Normal $\mathbf{D}$ is continuous (no free charge): $\epsilon_0E_0\cos45^\circ = 4\epsilon_0E_n$, so $E_n = E_0/(4\sqrt2)$ inside. Hence
> $$
> \tan\theta_2 = \frac{E_t}{E_n} = 4\ \Rightarrow\ \theta_2\approx76.0^\circ,\qquad \lvert\mathbf{E}_2\rvert = E_0\sqrt{\tfrac12+\tfrac1{32}}\approx0.729\,E_0 .
> $$
> The line tilts from $45^\circ$ to $76^\circ$ from the normal — away from it, toward the face — and the field is weaker.
>
> - (a) Bending toward the normal happens on entering a *lower*-$\epsilon$ medium ($\tan\theta_1/\tan\theta_2 = \epsilon_1/\epsilon_2$).
> - (c) $E_t$ is unchanged and $E_n$ shrinks, so $\lvert\mathbf{E}\rvert$ can only decrease.
> - (d) Dividing the whole vector by 4 also shrinks $E_t$, violating $\hat{n}\times(\mathbf{E}_1-\mathbf{E}_2) = 0$. Only at normal incidence is $E = E_0/4$.
> - (e) Wrong direction, and $\lvert\mathbf{D}\rvert$ grows: $D_n$ is unchanged but $D_t$ is multiplied by 4, so $\lvert\mathbf{D}_2\rvert\approx2.92\,\epsilon_0E_0$.
>
> **Answer.** (b): the field line bends away from the normal (to about $76^\circ$), and $\lvert\mathbf{E}\rvert$ drops to about $0.729\,E_0$.

### 9.5 A coated wire, find the error

> [!easy] Easy · find the error · Gauss's law for D
> A long copper wire of radius $a = 1$ mm on the $z$ axis carries free charge $\rho_l = 10$ nC/m. It is coated with plastic ($\epsilon_r = 2.5$) out to $r = b = 2$ mm, with air beyond. A student finds the field just outside the coating like this:
>
> *"Gauss's law with the coating's permittivity: $\epsilon\oint\mathbf{E}\cdot d\mathbf{S} = Q_{\text{enc}}$ with $\epsilon = 2.5\epsilon_0$. On a cylinder of radius $r$ and length $L$, $2.5\epsilon_0E\cdot2\pi rL = \rho_lL$, so $E = \rho_l/(2\pi\cdot2.5\epsilon_0r)$ for every $r>a$. At $r = b^+$: $E = 36.0$ kV/m, radially outward."*
>
> What is wrong? Find the correct field just outside ($r = b^+$) and just inside ($r = b^-$) the coating.
>
> *Source: original.*

> [!hint]- Hint
> Through which material does a Gaussian cylinder of radius $b^+$ pass? Which form of Gauss's law needs no $\epsilon$ at all?

> [!solution]- Solution
> **The slip:** $\epsilon\oint\mathbf{E}\cdot d\mathbf{S} = Q$ holds only when one uniform $\epsilon$ fills the whole Gaussian surface, and a cylinder of radius $b^+$ lies in air, not in plastic. The safe route is Gauss's law for $\mathbf{D}$, which counts free charge and needs no $\epsilon$:
> $$
> D_r\cdot2\pi rL = \rho_lL\ \Rightarrow\ \mathbf{D} = \frac{\rho_l}{2\pi r}\hat{r}\quad(r>a,\ \text{in the coating and in the air alike}).
> $$
> Then $\mathbf{E} = \mathbf{D}/\epsilon$ with the $\epsilon$ *of the point where you stand*. With $D(b) = \rho_l/(2\pi b)\approx0.796\ \mu$C/m²:
> $$
> E(b^-) = \frac{\rho_l}{2\pi(2.5\epsilon_0)b}\approx36.0\ \text{kV/m},\qquad E(b^+) = \frac{\rho_l}{2\pi\epsilon_0b}\approx89.9\ \text{kV/m}.
> $$
> The student's number is right — for the inside of the coating.
>
> **Check:** the jump comes from bound charge on the coating's outer face, $\rho_{sb} = \mathbf{P}\cdot\hat{r} = (1-1/2.5)D(b)\approx0.477\ \mu$C/m², and indeed $\epsilon_0(89.9-36.0)$ kV/m $\approx0.477\ \mu$C/m² ✓.
>
> **Answer.** The student used the coating's $\epsilon$ on a surface that lies in air. Correct values: $E(b^+)\approx89.9$ kV/m and $E(b^-)\approx36.0$ kV/m, both along $+\hat{r}$.

## Medium

### 9.6 Graded dielectric at fixed voltage

> [!medium] Medium · graded permittivity · bound charge
> Large conducting plates lie on $z = 0$ and $z = 1$ m. The bottom plate is held at $V = 6$ V and the top plate is grounded. The gap is filled with a graded dielectric, $\epsilon_r(z) = (1+z)^2$ with $z$ in meters, rising from 1 at the bottom plate to 4 at the top; it carries no free charge.
>
> (a) Why can't you solve this with Laplace's equation, and what is constant instead? (b) Find $\mathbf{D}$ and the free surface charge density on each plate. (c) Find $\mathbf{E}(z)$ and $V(z)$, and evaluate $V(0.5\ \text{m})$. (d) Find $\mathbf{P}(z)$, the bound volume charge density $\rho_b(z)$, and the bound surface charge density on each face of the dielectric. Show that the total bound charge (per square meter of plate) is zero.
>
> *Source: course notes Lecture 9, Example 4 (graded dielectric), re-parameterized with the voltage given instead of the charge.*

> [!hint]- Hint
> $\nabla\cdot\mathbf{D} = 0$ with $\mathbf{D} = D_z(z)\hat{z}$ makes $D_z$ a constant even though $\epsilon$ varies. Write $E_z = D_z/\epsilon(z)$, integrate from plate to plate, and let the 6 V fix $D_z$.

> [!solution]- Solution
> **(a) Setup.** Laplace's equation comes from pulling $\epsilon$ out of $\nabla\cdot(\epsilon\nabla V) = 0$, which is illegal when $\epsilon$ varies along the field. What survives is Gauss's law: no free charge and dependence on $z$ only give $dD_z/dz = 0$, so **$D_z$ is one constant across the whole gap**.
>
> **(b)** With $E_z = D_z/[\epsilon_0(1+z)^2]$,
> $$
> V(1)-V(0) = -\int_0^1\frac{D_z\,dz}{\epsilon_0(1+z)^2} = -\frac{D_z}{\epsilon_0}\Big[1-\frac12\Big] = -\frac{D_z}{2\epsilon_0}.
> $$
> Setting this equal to $0-6 = -6$ V gives $D_z = 12\epsilon_0$: $\mathbf{D} = 12\epsilon_0\hat{z}$ C/m² $\approx1.06\times10^{-10}\hat{z}$ C/m². Plate charges from $\rho_s = \hat{n}\cdot\mathbf{D}$ with $\hat{n}$ out of the metal: $+12\epsilon_0$ C/m² on the bottom plate ($\hat{n} = +\hat{z}$) and $-12\epsilon_0$ C/m² on the top plate ($\hat{n} = -\hat{z}$).
>
> **(c)** $E_z = \dfrac{12}{(1+z)^2}$ V/m: 12 V/m at the bottom, 3 V/m at the top. Then
> $$
> V(z) = 6-\int_0^z\frac{12\,dz'}{(1+z')^2} = 6-\frac{12z}{1+z}\ \text{V},\qquad V(0.5) = 6-4 = 2\ \text{V}.
> $$
> A homogeneous filling would give a straight line and 3 V at the midplane; here most of the voltage drops in the low-$\epsilon$ bottom half.
>
> **(d)** $P_z = D_z-\epsilon_0E_z = 12\epsilon_0\Big[1-\dfrac{1}{(1+z)^2}\Big]$ C/m², rising from 0 at the bottom face to $9\epsilon_0$ at the top. Then
> $$
> \rho_b = -\frac{dP_z}{dz} = -\frac{24\epsilon_0}{(1+z)^3}\ \text{C/m}^3\qquad(-24\epsilon_0\ \text{at}\ z = 0,\ -3\epsilon_0\ \text{at}\ z = 1\ \text{m}).
> $$
> Faces, $\rho_{sb} = \mathbf{P}\cdot\hat{n}$ with $\hat{n}$ out of the dielectric: top ($\hat{n} = +\hat{z}$) $+9\epsilon_0$ C/m²; bottom ($\hat{n} = -\hat{z}$) $-P_z(0) = 0$. The bulk holds $\int_0^1\rho_b\,dz = -[P_z(1)-P_z(0)] = -9\epsilon_0$ per m². Total: $-9\epsilon_0+9\epsilon_0+0 = 0$ ✓.
>
> **Check:** Gauss's law for *all* charge: $\epsilon_0E_z(z)$ must equal the free plus bound charge below height $z$, and indeed $12\epsilon_0+0-12\epsilon_0\big[1-(1+z)^{-2}\big] = 12\epsilon_0/(1+z)^2$ ✓.
>
> **Watch out:** a graded dielectric carries bound charge in its *bulk* even though it holds no free charge; in a uniform one, $\rho_b$ would vanish.
>
> **Answer.** $D_z$ is constant: $\mathbf{D} = 12\epsilon_0\hat{z}$ C/m²; plates $+12\epsilon_0$ (bottom) and $-12\epsilon_0$ C/m² (top). $\mathbf{E} = \dfrac{12}{(1+z)^2}\hat{z}$ V/m, $V(z) = 6-\dfrac{12z}{1+z}$ V, $V(0.5) = 2$ V. $\mathbf{P} = 12\epsilon_0\big[1-(1+z)^{-2}\big]\hat{z}$ C/m², $\rho_b = -24\epsilon_0/(1+z)^3$ C/m³, $\rho_{sb} = +9\epsilon_0$ C/m² on the top face and 0 on the bottom face; total bound charge zero.

### 9.7 Charged sheet on a dielectric interface

> [!medium] Medium · piecewise Laplace · interface charge
> Grounded conducting plates lie on $z = 0$ and $z = 3$ m. A dielectric with $\epsilon_r = 2$ fills $0<z<1$ m and free space fills $1<z<3$ m. A uniform free sheet $\rho_s = 10\epsilon_0$ C/m² lies on the interface $z = 1$ m.
>
> (a) Find $V(1)$, and $\mathbf{E}$ and $\mathbf{D}$ in both regions. (b) Find the free surface charge density on each plate. (c) Find $\mathbf{P}$ in the dielectric and the bound surface charge density on both of its faces; verify the jump of $\epsilon_0E_z$ at $z = 1$ m. (d) Keeping the sheet and the grounded bottom plate, to what potential must the top plate be raised for the region $1<z<3$ m to become field-free? What are the plate charges then?
>
> *Source: FA26 HW4 #2 (course notes Lecture 9, Example 3), re-parameterized; part (d) original.*

> [!hint]- Hint
> Each region is homogeneous, so $V$ is a straight line in each; with both plates at 0 V the only unknown is $V_0 = V(1)$. The sheet sets the jump of $D_z$, not of $E_z$. For (d): what does "field-free above" say about $D_z$ above the sheet?

> [!solution]- Solution
> **Setup.** The $\mathbf{D}$-first shortcut cannot work alone here: how the sheet's flux splits between the two plates is unknown until the potentials are matched. So solve Laplace's equation in each homogeneous region (straight lines) and stitch the pieces with the boundary condition at $z = 1$ m.
>
> **(a)** With $V_0 = V(1)$: below, $V = V_0z$, $\mathbf{E} = -V_0\hat{z}$, $\mathbf{D} = -2\epsilon_0V_0\hat{z}$; above, $V = V_0(3-z)/2$, $\mathbf{E} = +\tfrac12V_0\hat{z}$, $\mathbf{D} = +\tfrac12\epsilon_0V_0\hat{z}$. At $z = 1$ m take medium 1 above and medium 2 below, so $\hat{n} = +\hat{z}$:
> $$
> \hat{z}\cdot(\mathbf{D}_1-\mathbf{D}_2) = \tfrac12\epsilon_0V_0+2\epsilon_0V_0 = 10\epsilon_0\ \Rightarrow\ V_0 = 4\ \text{V}.
> $$
> Below: $\mathbf{E} = -4\hat{z}$ V/m, $\mathbf{D} = -8\epsilon_0\hat{z}$ C/m². Above: $\mathbf{E} = +2\hat{z}$ V/m, $\mathbf{D} = +2\epsilon_0\hat{z}$ C/m². Both point away from the positive sheet.
>
> **(b)** $\rho_s = \hat{n}\cdot\mathbf{D}$ with $\hat{n}$ out of the metal: bottom plate $\hat{z}\cdot(-8\epsilon_0\hat{z}) = -8\epsilon_0$ C/m²; top plate $-\hat{z}\cdot(2\epsilon_0\hat{z}) = -2\epsilon_0$ C/m². They add to $-10\epsilon_0 = -\rho_s$: every flux line from the sheet ends on a plate. The bottom plate, both nearer and behind the higher-$\epsilon$ layer, takes four fifths.
>
> **(c)** $\mathbf{P} = \mathbf{D}-\epsilon_0\mathbf{E} = -8\epsilon_0\hat{z}+4\epsilon_0\hat{z} = -4\epsilon_0\hat{z}$ C/m² in the dielectric ($\mathbf{P} = 0$ in free space). Faces: top ($z = 1^-$, $\hat{n} = +\hat{z}$) $\rho_{sb} = -4\epsilon_0$ C/m²; bottom ($z = 0^+$, $\hat{n} = -\hat{z}$) $\rho_{sb} = +4\epsilon_0$ C/m². At $z = 1$ m, $\epsilon_0E_z$ jumps by $\epsilon_0[2-(-4)] = 6\epsilon_0$, exactly the free plus bound charge there, $10\epsilon_0-4\epsilon_0$ ✓.
>
> **(d)** Field-free above means $\mathbf{D} = 0$ there, so the jump condition sends all of the sheet's flux down: $D_z = -\rho_s = -10\epsilon_0$ below, hence $E_z = -10\epsilon_0/(2\epsilon_0) = -5$ V/m and $V(1) = 5$ V. With no field above, the top plate sits at the sheet's potential: **$V(3) = 5$ V**. Plate charges: $-10\epsilon_0$ C/m² on the bottom plate, $0$ on the top plate.
>
> **Check:** $V(3)-V(0) = -\int_0^3E_z\,dz = 5(1)+0(2) = 5$ V ✓, and for the grounded case $-\int_0^3E_z\,dz = 4(1)-2(2) = 0$ ✓.
>
> **Watch out:** writing the jump as $\epsilon_0(E_{z,\text{above}}-E_{z,\text{below}}) = \rho_s$ forgets the bound charge on the dielectric's face and gives $V_0 = 20/3$ V instead of 4 V.
>
> **Answer.** (a) $V(1) = 4$ V; below $\mathbf{E} = -4\hat{z}$ V/m, $\mathbf{D} = -8\epsilon_0\hat{z}$ C/m²; above $\mathbf{E} = 2\hat{z}$ V/m, $\mathbf{D} = 2\epsilon_0\hat{z}$ C/m². (b) $-8\epsilon_0$ C/m² at $z = 0$ and $-2\epsilon_0$ C/m² at $z = 3$ m. (c) $\mathbf{P} = -4\epsilon_0\hat{z}$ C/m²; $\rho_{sb} = -4\epsilon_0$ C/m² (top face) and $+4\epsilon_0$ C/m² (bottom face). (d) $V(3) = 5$ V; plate charges $-10\epsilon_0$ C/m² (bottom) and 0 (top).

### 9.8 Charged surface of a dielectric rod

> [!medium] Medium · cylindrical symmetry · interface charge · bound charge
> A long dielectric rod of radius 2 m ($\epsilon_r = 4$) lies along the $z$ axis in free space. A uniform free line charge $\rho_l$ lies on the axis, and the rod's surface $r = 2$ m carries a uniform free surface charge $\rho_s$. The field points radially outward everywhere; just inside the surface it is $\mathbf{E} = 3\hat{r}$ V/m and just outside it is $\mathbf{E} = 8\hat{r}$ V/m.
>
> (a) Find $\rho_s$. (b) Find $\rho_l$. (c) Find the bound surface charge density on the rod's surface and the bound line charge that hugs the axis, and show that the rod's total bound charge is zero. (d) Find $V(1\ \text{m})-V(4\ \text{m})$.
>
> *Source: SP18 Exam 1 #4, re-parameterized and extended.*

> [!hint]- Hint
> At $r = 2$ m the free sheet sets the jump of $D_r$, not of $\epsilon_0E_r$: $\rho_s = D_r(\text{outside})-D_r(\text{inside})$. A Gaussian cylinder that stays inside the rod encloses only $\rho_l$. For (d), split the integral at $r = 2$ m.

> [!solution]- Solution
> **Setup.** Cylindrical symmetry: $\mathbf{D} = D_r(r)\hat{r}$. At $r = 2$ m take medium 1 = air (outside) and medium 2 = rod, so $\hat{n} = \hat{r}$.
>
> **(a)** $\rho_s = \hat{r}\cdot(\mathbf{D}_1-\mathbf{D}_2) = \epsilon_0(8)-4\epsilon_0(3) = -4\epsilon_0$ C/m² $\approx-3.54\times10^{-11}$ C/m².
>
> **(b)** A Gaussian cylinder of radius $r<2$ m encloses only $\rho_l$: $D_r = \rho_l/(2\pi r)$, so $E_r = \rho_l/(2\pi\cdot4\epsilon_0r)$. At $r = 2^-$, $3 = \rho_l/(16\pi\epsilon_0)$, so $\rho_l = 48\pi\epsilon_0$ C/m $\approx1.34\times10^{-9}$ C/m, and inside the rod $E_r = 6/r$ V/m.
>
> Cross-check outside: $D_r = \dfrac{\rho_l+2\pi(2)\rho_s}{2\pi r} = \dfrac{48\pi\epsilon_0-16\pi\epsilon_0}{2\pi r} = \dfrac{16\epsilon_0}{r}$, so $E_r = 16/r$ V/m and $E(2^+) = 8$ V/m ✓.
>
> **(c)** Inside, $\mathbf{P} = \mathbf{D}-\epsilon_0\mathbf{E} = \Big(\dfrac{24\epsilon_0}{r}-\dfrac{6\epsilon_0}{r}\Big)\hat{r} = \dfrac{18\epsilon_0}{r}\hat{r}$. On the surface ($\hat{n} = +\hat{r}$): $\rho_{sb} = P_r(2) = 9\epsilon_0$ C/m², i.e. $9\epsilon_0\cdot2\pi(2) = 36\pi\epsilon_0$ C per meter of rod. In the bulk $rP_r$ is constant, so $\rho_b = -\frac1r\frac{d}{dr}(rP_r) = 0$ — except on the axis, where $\mathbf{P}$ blows up. The bound charge inside a thin cylinder of radius $r_0$ around the axis is minus the outward flux of $\mathbf{P}$: $-2\pi r_0P_r(r_0) = -36\pi\epsilon_0$ C/m, whatever $r_0$. That is the bound line charge $-\tfrac{\chi_e}{\epsilon_r}\rho_l = -\tfrac34(48\pi\epsilon_0)$ that a dielectric wraps around any embedded free charge. Total bound: $36\pi\epsilon_0-36\pi\epsilon_0 = 0$ ✓.
>
> Check at the surface: free plus bound is $-4\epsilon_0+9\epsilon_0 = 5\epsilon_0 = \epsilon_0(8-3)$ ✓, the jump of $\epsilon_0E_r$.
>
> **(d)** From $V(4)-V(1) = -\int_1^4E_r\,dr$:
> $$
> V(1)-V(4) = \int_1^2\frac{6}{r}dr+\int_2^4\frac{16}{r}dr = 6\ln2+16\ln2 = 22\ln2\approx15.2\ \text{V}.
> $$
> Positive, as it must be: the potential falls along an outward field.
>
> **Watch out:** $\epsilon_0(E_{\text{out}}-E_{\text{in}}) = 5\epsilon_0$ is the *total* (free plus bound) surface charge; the free charge comes from the jump in $D_r$.
>
> **Answer.** $\rho_s = -4\epsilon_0\approx-3.54\times10^{-11}$ C/m²; $\rho_l = 48\pi\epsilon_0\approx1.34\times10^{-9}$ C/m; $\rho_{sb} = +9\epsilon_0$ C/m² on the surface ($+36\pi\epsilon_0$ C/m) and a bound line charge $-36\pi\epsilon_0$ C/m on the axis, total zero; $V(1)-V(4) = 22\ln2\approx15.2$ V.

## Hard

### 9.9 Glass slab in an oblique field

> [!hard] Hard · refraction · bound charge · potential
> A large glass slab ($\epsilon_r = 3$) occupies $0<z<3$ cm in air; there is no free charge anywhere near it. Below the slab ($z<0$) the field is uniform, $\mathbf{E}_0 = 40\hat{x}+30\hat{z}$ V/m.
>
> (a) Find $\mathbf{E}$, $\mathbf{D}$ and $\mathbf{P}$ inside the slab, and the angle the field makes with the normal $\hat{z}$ in the air and in the glass.
>
> (b) Find the field above the slab ($z>3$ cm), and explain the result.
>
> (c) Find the bound surface charge density on each face of the slab, and show that these two sheets alone account for the change of $\mathbf{E}$ inside.
>
> (d) The field line through $A = (0,0,0)$ crosses the slab and leaves its top face at a point $B$. Find $B$ and $V(B)-V(A)$, and check the voltage along a second path. Where would this field line have reached the height $z = 3$ cm without the slab?
>
> *Source: original.*

> [!hint]- Hint
> At each face copy the tangential part of $\mathbf{E}$ and keep $D_z$ unchanged (no free charge). Inside the slab $\mathbf{E}$ is uniform, so field lines are straight there and $V(B)-V(A) = -\mathbf{E}\cdot(\mathbf{r}_B-\mathbf{r}_A)$.

> [!solution]- Solution
> **Setup.** Both faces are planes $z = \text{const}$, so $\hat{n} = \hat{z}$: the tangential part is the $x$ (and $y$) component, the normal part is $E_z$. At each face take medium 1 above and medium 2 below.
>
> **(a)** Bottom face, $z = 0$: $E_x$ is copied, $E_x = 40$ V/m; $D_z$ is continuous, $3\epsilon_0E_z = \epsilon_0(30)$, so $E_z = 10$ V/m.
> $$
> \mathbf{E} = 40\hat{x}+10\hat{z}\ \text{V/m},\qquad \mathbf{D} = 3\epsilon_0\mathbf{E} = \epsilon_0(120\hat{x}+30\hat{z})\ \text{C/m}^2,\qquad \mathbf{P} = \mathbf{D}-\epsilon_0\mathbf{E} = \epsilon_0(80\hat{x}+20\hat{z})\ \text{C/m}^2 .
> $$
> Numerically $\mathbf{D}\approx(1.06\hat{x}+0.266\hat{z})\times10^{-9}$ C/m² and $\mathbf{P}\approx(7.08\hat{x}+1.77\hat{z})\times10^{-10}$ C/m². Angles from the normal: in air $\tan\theta_1 = 40/30$, $\theta_1\approx53.1^\circ$; in glass $\tan\theta_2 = 40/10 = 4$, $\theta_2\approx76.0^\circ$. Check: $\tan\theta_1/\tan\theta_2 = 1/3 = \epsilon_{\text{air}}/\epsilon_{\text{glass}}$ ✓; the line bends away from the normal on entering the glass.
>
> **(b)** Top face, $z = 3$ cm: $E_x = 40$ V/m is copied again, and $\epsilon_0E_z = 3\epsilon_0(10)$ gives $E_z = 30$ V/m. So $\mathbf{E} = 40\hat{x}+30\hat{z}$ V/m $= \mathbf{E}_0$ above the slab: the field leaves exactly as it came in, like light through a window pane. The second face applies the first face's conditions in reverse, so the two refractions undo each other.
>
> **(c)** $\rho_{sb} = \mathbf{P}\cdot\hat{n}$ with $\hat{n}$ out of the glass: top face ($+\hat{z}$) $+20\epsilon_0\approx+1.77\times10^{-10}$ C/m², bottom face ($-\hat{z}$) $-20\epsilon_0$ C/m². The bulk has none ($\mathbf{P}$ is uniform), and $P_x$ leaves no charge on these faces ($\mathbf{P}\cdot\hat{n}$ ignores it). Two infinite sheets, $+20\epsilon_0$ above $-20\epsilon_0$, make $-\dfrac{20\epsilon_0}{\epsilon_0}\hat{z} = -20\hat{z}$ V/m between them and nothing outside. Added to $\mathbf{E}_0$: inside $40\hat{x}+(30-20)\hat{z} = 40\hat{x}+10\hat{z}$ ✓, outside $\mathbf{E}_0$ unchanged ✓. Sheets make only normal fields, which is why $E_x$ is untouched.
>
> **(d)** Inside, the field line runs straight along $(40,0,10)$: 4 cm sideways for every 1 cm up. Rising 3 cm it moves 12 cm, so $B = (12\ \text{cm},0,3\ \text{cm})$. Then
> $$
> V(B)-V(A) = -\mathbf{E}\cdot(\mathbf{r}_B-\mathbf{r}_A) = -(40)(0.12)-(10)(0.03) = -4.8-0.3 = -5.1\ \text{V}.
> $$
> Second path: up the $z$ axis inside the glass, $-E_z(0.03\ \text{m}) = -0.3$ V, then along $x$ just under the top face, $-E_x(0.12\ \text{m}) = -4.8$ V; total $-5.1$ V ✓ (path independence). Along the line itself, $\lvert\mathbf{E}\rvert\times\text{length} = \sqrt{1700}\times\sqrt{0.12^2+0.03^2} = 5.1$ V ✓. Without the slab the line would keep the direction $(40,0,30)$ and reach $z = 3$ cm at $x = 4$ cm; the glass drags it 8 cm sideways.
>
> **Watch out:** dividing the whole vector $\mathbf{E}_0$ by $\epsilon_r = 3$ would also shrink $E_x$, breaking the continuity of tangential $\mathbf{E}$; only the normal component is divided.
>
> **Answer.** (a) $\mathbf{E} = 40\hat{x}+10\hat{z}$ V/m, $\mathbf{D} = \epsilon_0(120\hat{x}+30\hat{z})$ C/m², $\mathbf{P} = \epsilon_0(80\hat{x}+20\hat{z})$ C/m²; $\theta\approx53.1^\circ$ in air, $76.0^\circ$ in glass. (b) $\mathbf{E} = 40\hat{x}+30\hat{z}$ V/m $= \mathbf{E}_0$. (c) $\rho_{sb} = +20\epsilon_0$ C/m² on the top face and $-20\epsilon_0$ C/m² on the bottom face; their field is $-20\hat{z}$ V/m inside, zero outside. (d) $B = (12\ \text{cm},0,3\ \text{cm})$, $V(B)-V(A) = -5.1$ V; without the slab the line would reach $x = 4$ cm.

### 9.10 Sphere, shell and two dielectric layers

> [!hard] Hard · spherical symmetry · conductors · bound charge
> A spherically symmetric arrangement is in electrostatic equilibrium:
>
> - $r\le1$ m: a conducting sphere carrying net free charge $Q_1 = +5$ C;
> - $1<r<2$ m: a perfect dielectric with $\epsilon_r = 5$;
> - $2\le r\le3$ m: a conducting shell carrying net free charge $-6$ C;
> - $3<r<4$ m: a perfect dielectric coating with $\epsilon_r = 2$;
> - $r>4$ m: free space.
>
> (a) Find $\mathbf{D}$, $\mathbf{E}$ and $\mathbf{P}$ in all five regions. (b) Find the free surface charge density at $r = 1$, 2, 3 and 4 m. (c) Find the bound surface charge density on each face of the two dielectric layers, and check that each layer is neutral. (d) Find the potentials of the shell and of the centre, relative to infinity. Which conductor is at the higher potential?
>
> *Source: Summer 2019 HE1 (conflict) #3a, re-parameterized (new charges and permittivities, outer dielectric coating added); same layout as Summer 2018 HE1 #3a and Summer 2019 HE1 #3a; FA26 HW4 #6 is the cylindrical analogue.*

> [!hint]- Hint
> Inside each conductor $\mathbf{E} = \mathbf{D} = \mathbf{P} = 0$, so a Gaussian sphere drawn inside the metal of the shell encloses zero net charge — that fixes the charge on the shell's inner surface. Everywhere else $\mathbf{D} = \dfrac{Q_{\text{enc}}}{4\pi r^2}\hat{r}$ with $Q_{\text{enc}}$ the enclosed **free** charge; then $\mathbf{E} = \mathbf{D}/\epsilon$ region by region. For (d), integrate $E_r$ inward from infinity through every region.

> [!solution]- Solution
> **Setup.** Spherical symmetry: $\mathbf{D} = D_r(r)\hat{r}$, and Gauss's law for free charge gives $D_r = Q_{\text{enc}}/(4\pi r^2)$. The enclosed free charge is $+5$ C for $1<r<2$ m and $5-6 = -1$ C for $r>3$ m; in the metal everything is zero.
>
> **(a)** With $\mathbf{E} = \mathbf{D}/(\epsilon_r\epsilon_0)$ and $\mathbf{P} = (1-1/\epsilon_r)\mathbf{D}$ ($r$ in meters):
>
> | region | $\mathbf{D}$ [C/m²] | $\mathbf{E}$ [V/m] | $\mathbf{P}$ [C/m²] |
> |---|---|---|---|
> | $r<1$ (metal) | 0 | 0 | 0 |
> | $1<r<2$, $\epsilon_r = 5$ | $\dfrac{5}{4\pi r^2}\hat{r}$ | $\dfrac{1}{4\pi\epsilon_0r^2}\hat{r}$ | $\dfrac{1}{\pi r^2}\hat{r}$ |
> | $2<r<3$ (metal) | 0 | 0 | 0 |
> | $3<r<4$, $\epsilon_r = 2$ | $-\dfrac{1}{4\pi r^2}\hat{r}$ | $-\dfrac{1}{8\pi\epsilon_0r^2}\hat{r}$ | $-\dfrac{1}{8\pi r^2}\hat{r}$ |
> | $r>4$ (air) | $-\dfrac{1}{4\pi r^2}\hat{r}$ | $-\dfrac{1}{4\pi\epsilon_0r^2}\hat{r}$ | 0 |
>
> **(b)** Free charge sits only on conductor surfaces: $\rho_s = Q/\text{area}$, equivalently $\hat{r}\cdot(\mathbf{D}_1-\mathbf{D}_2)$ with medium 1 outside.
>
> - $r = 1$ m: all of $Q_1$, $\rho_s = 5/(4\pi)\approx0.398$ C/m².
> - $r = 2$ m (inner surface of the shell): a Gaussian sphere inside the shell's metal encloses zero, so this surface holds $-5$ C: $\rho_s = -5/(16\pi)\approx-0.0995$ C/m².
> - $r = 3$ m (outer surface of the shell): the rest, $-6-(-5) = -1$ C: $\rho_s = -1/(36\pi)\approx-0.00884$ C/m².
> - $r = 4$ m (coating–air): no free charge, $\rho_s = 0$; $D_r$ is continuous there.
>
> **(c)** $\rho_{sb} = \mathbf{P}\cdot\hat{n}$ with $\hat{n}$ the outward normal *of the dielectric*: $-\hat{r}$ on an inner face, $+\hat{r}$ on an outer face.
>
> - Inner layer: at $r = 1$, $-P_r(1) = -\dfrac{1}{\pi}\approx-0.318$ C/m², total $\times4\pi(1)^2 = -4$ C; at $r = 2$, $+P_r(2) = \dfrac{1}{4\pi}\approx0.0796$ C/m², total $+4$ C. Neutral ✓.
> - Coating: at $r = 3$, $-P_r(3) = +\dfrac{1}{72\pi}\approx0.00442$ C/m², total $+0.5$ C; at $r = 4$, $+P_r(4) = -\dfrac{1}{128\pi}\approx-0.00249$ C/m², total $-0.5$ C. Neutral ✓.
>
> In both layers $r^2P_r$ is constant, so $\rho_b = -\frac{1}{r^2}\frac{d}{dr}(r^2P_r) = 0$ and all bound charge sits on the faces. Each layer's inner and outer faces carry $-(1-1/\epsilon_r)$ and $+(1-1/\epsilon_r)$ times the free charge it encloses: $\mp\tfrac45(5) = \mp4$ C for the inner layer and $\mp\tfrac12(-1) = \pm0.5$ C for the coating.
>
> **(d)** With $V(\infty) = 0$, $V(r) = \int_r^\infty E_r\,dr'$. The shell is an equipotential, so evaluate it at $r = 3$ m:
> $$
> V_{\text{shell}} = \int_3^4\frac{-dr}{8\pi\epsilon_0r^2}+\int_4^\infty\frac{-dr}{4\pi\epsilon_0r^2} = -\frac{1}{8\pi\epsilon_0}\Big(\frac13-\frac14\Big)-\frac{1}{16\pi\epsilon_0} = -\frac{7}{96\pi\epsilon_0}\approx-2.62\times10^{9}\ \text{V}.
> $$
> The centre is inside the core, at the core's potential; add the rise across the inner dielectric (the metal regions contribute nothing):
> $$
> V(0) = V_{\text{shell}}+\int_1^2\frac{dr}{4\pi\epsilon_0r^2} = -\frac{7}{96\pi\epsilon_0}+\frac{1}{8\pi\epsilon_0} = \frac{5}{96\pi\epsilon_0}\approx1.87\times10^{9}\ \text{V}.
> $$
> The core is higher, by $\dfrac{1}{8\pi\epsilon_0}\approx4.49\times10^9$ V; it even sits above zero while the shell sits below. The core is positive and the field between the two conductors points outward, from core to shell. (The enormous voltages come from the course's coulomb-sized charges; the structure is what matters.)
>
> **Check:** at $r = 4$ m only bound charge sits on the surface, and it alone makes $E_r$ jump: $\epsilon_0[E_r(4^+)-E_r(4^-)] = -\dfrac{1}{64\pi}+\dfrac{1}{128\pi} = -\dfrac{1}{128\pi}$ C/m² $= 0+\rho_{sb}(4)$ ✓.
>
> **Watch out:** the shell's $-6$ C does not all sit on its outer surface. The inner surface must carry $-5$ C to end the flux from the core, or the field inside the metal would not vanish; only $-1$ C is left for the outer surface.
>
> **Answer.** (a) Zero in both metals; $\mathbf{D} = 5\hat{r}/(4\pi r^2)$ C/m², $\mathbf{E} = \hat{r}/(4\pi\epsilon_0r^2)$ V/m, $\mathbf{P} = \hat{r}/(\pi r^2)$ C/m² for $1<r<2$ m; $\mathbf{D} = -\hat{r}/(4\pi r^2)$, $\mathbf{E} = -\hat{r}/(8\pi\epsilon_0r^2)$, $\mathbf{P} = -\hat{r}/(8\pi r^2)$ for $3<r<4$ m; $\mathbf{D} = -\hat{r}/(4\pi r^2)$, $\mathbf{E} = -\hat{r}/(4\pi\epsilon_0r^2)$, $\mathbf{P} = 0$ for $r>4$ m ($r$ in m). (b) $\rho_s = 5/(4\pi)$, $-5/(16\pi)$, $-1/(36\pi)$ and $0$ C/m² at $r = 1$, 2, 3, 4 m. (c) $\rho_{sb} = -1/\pi$, $+1/(4\pi)$, $+1/(72\pi)$, $-1/(128\pi)$ C/m² at $r = 1$, 2, 3, 4 m (totals $-4$, $+4$, $+0.5$, $-0.5$ C). (d) $V_{\text{shell}} = -7/(96\pi\epsilon_0)\approx-2.62\times10^9$ V, $V(0) = 5/(96\pi\epsilon_0)\approx1.87\times10^9$ V; the core is higher.

### 9.11 Graded coax with uniform field

> [!hard] Hard · graded permittivity · coaxial cable · bound charge
> A coaxial cable has an inner conductor of radius $a$ and an outer conductor of inner radius $b$. Its insulation is graded: $\epsilon(r) = \epsilon_a\,a/r$ for $a<r<b$.
>
> (a) Show that the field magnitude between the conductors does not depend on $r$, and express it through the voltage $V_0 = V(a)-V(b)$.
>
> (b) Take $a = 1$ mm, $b = 3$ mm, $\epsilon_a = 6\epsilon_0$ (so $\epsilon_r$ falls from 6 at the inner conductor to 2 at the outer one) and $V_0 = 200$ V. Find $\mathbf{E}$, $\mathbf{D}(r)$ and the free charge per unit length $\rho_l$ on the inner conductor.
>
> (c) Find $\mathbf{P}(r)$, the bound volume charge density $\rho_b(r)$, and the bound surface charge densities on the inner and outer faces of the insulation. Show that the total bound charge per unit length is zero.
>
> (d) A cable with the same radii and voltage but homogeneous insulation has its largest field at $r = a$. Find that field and compare.
>
> *Source: classic (graded cable insulation).*

> [!hint]- Hint
> Gauss's law for $\mathbf{D}$ does not care about $\epsilon(r)$: $D_r = \rho_l/(2\pi r)$ always. Divide by $\epsilon(r)$. For $\rho_b$ use the cylindrical divergence $-\frac1r\frac{d}{dr}(rP_r)$, and remember that $\mathbf{P}\cdot\hat{n}$ uses the outward normal of the insulation, which is $-\hat{r}$ at $r = a$.

> [!solution]- Solution
> **(a) Setup.** Long and cylindrically symmetric, so $\mathbf{D} = D_r(r)\hat{r}$; a Gaussian cylinder of radius $r$ and length $L$ encloses free charge $\rho_lL$ whatever the insulation does:
> $$
> D_r = \frac{\rho_l}{2\pi r},\qquad E_r = \frac{D_r}{\epsilon(r)} = \frac{\rho_l}{2\pi r}\cdot\frac{r}{\epsilon_aa} = \frac{\rho_l}{2\pi\epsilon_aa},
> $$
> independent of $r$. Then $V_0 = V(a)-V(b) = \int_a^bE_r\,dr = E_r(b-a)$, so $E = V_0/(b-a)$ and $\rho_l = 2\pi\epsilon_aa\,V_0/(b-a)$.
>
> **(b)** $E = \dfrac{200}{2\times10^{-3}} = 1.0\times10^5$ V/m, so $\mathbf{E} = 10^5\hat{r}$ V/m (100 kV/m) at every radius. $\rho_l = 2\pi(6\epsilon_0)(10^{-3})(10^5)\approx3.34\times10^{-8}$ C/m $= 33.4$ nC/m. $\mathbf{D} = \dfrac{\rho_l}{2\pi r}\hat{r} = \dfrac{6\epsilon_0aE}{r}\hat{r}\approx\dfrac{5.31\times10^{-9}}{r}\hat{r}$ C/m² ($r$ in m): $5.31\ \mu$C/m² at $r = a$ and $1.77\ \mu$C/m² at $r = b$.
>
> **(c)** $P_r = D_r-\epsilon_0E = \epsilon_0E\Big(\dfrac{6a}{r}-1\Big)$: $5\epsilon_0E\approx4.43\ \mu$C/m² at $r = a$ and $\epsilon_0E\approx0.885\ \mu$C/m² at $r = b$. Since $rP_r = \epsilon_0E(6a-r)$,
> $$
> \rho_b = -\frac1r\frac{d}{dr}(rP_r) = +\frac{\epsilon_0E}{r}\qquad(0.885\ \text{mC/m}^3\ \text{at}\ r = a,\ 0.295\ \text{mC/m}^3\ \text{at}\ r = b).
> $$
> Faces: inner ($\hat{n} = -\hat{r}$) $\rho_{sb}(a) = -P_r(a) = -5\epsilon_0E\approx-4.43\ \mu$C/m²; outer ($\hat{n} = +\hat{r}$) $\rho_{sb}(b) = +P_r(b) = \epsilon_0E\approx+0.885\ \mu$C/m². Per unit length, using $\rho_l = 12\pi\epsilon_0aE$ and $b = 3a$:
> $$
> \underbrace{-5\epsilon_0E\cdot2\pi a}_{-\frac56\rho_l}+\underbrace{\epsilon_0E\cdot2\pi b}_{+\frac12\rho_l}+\underbrace{\int_a^b\frac{\epsilon_0E}{r}\,2\pi r\,dr}_{+\frac13\rho_l} = \Big(-\tfrac56+\tfrac12+\tfrac13\Big)\rho_l = 0,
> $$
> i.e. $-27.8$, $+16.7$ and $+11.1$ nC/m. The positive bulk charge makes sense: a field that keeps the same strength on ever larger cylinders needs ever more enclosed (total) charge, $\epsilon_0E\cdot2\pi r$ per unit length.
>
> **(d)** Homogeneous insulation: $E_r = \rho_l/(2\pi\epsilon r)$ and $V_0 = \dfrac{\rho_l}{2\pi\epsilon}\ln\dfrac ba$, so $E_{\max} = E(a) = \dfrac{V_0}{a\ln(b/a)} = \dfrac{200}{10^{-3}\ln3}\approx1.82\times10^5$ V/m, whatever $\epsilon$ is. The graded cable runs at $1.0\times10^5$ V/m everywhere, so its peak field is lower by the factor $2/\ln3\approx1.82$. Putting the high-$\epsilon$ material where $D$ is largest is why high-voltage cables use graded insulation.
>
> **Check:** Gauss's law with all charge at radius $r$: $\rho_l-\tfrac56\rho_l+2\pi\epsilon_0E(r-a) = 2\pi\epsilon_0Er$ (using $\tfrac16\rho_l = 2\pi\epsilon_0Ea$), which is $\epsilon_0E$ times $2\pi r$ ✓.
>
> **Watch out:** on the inner face the insulation's outward normal is $-\hat{r}$, so $\rho_{sb}(a) = -P_r(a)$ is negative — the bound layer hugging a positive conductor is always of the opposite sign.
>
> **Answer.** (a) $E = \rho_l/(2\pi\epsilon_aa) = V_0/(b-a)$, independent of $r$. (b) $\mathbf{E} = 1.0\times10^5\hat{r}$ V/m; $\rho_l\approx33.4$ nC/m; $\mathbf{D}\approx(5.31\times10^{-9}/r)\hat{r}$ C/m² (from 5.31 to 1.77 $\mu$C/m²). (c) $P_r = \epsilon_0E(6a/r-1)$ (from 4.43 to 0.885 $\mu$C/m²); $\rho_b = \epsilon_0E/r$ (from 0.885 to 0.295 mC/m³); $\rho_{sb}(a)\approx-4.43\ \mu$C/m², $\rho_{sb}(b)\approx+0.885\ \mu$C/m²; per unit length $-\tfrac56\rho_l+\tfrac12\rho_l+\tfrac13\rho_l = 0$. (d) $1.82\times10^5$ V/m with homogeneous insulation, 1.82 times the graded cable's field.

### 9.12 Charged sphere floating in oil

> [!hard] Hard · side-by-side dielectrics · spherical geometry · uniqueness
> A metal sphere of radius $a = 10$ cm carrying free charge $Q = 30$ nC floats half-submerged in a large bath of oil ($\epsilon_r = 2$). Its centre is at the origin, on the flat oil surface $z = 0$: oil fills $z<0$ outside the sphere, and air fills $z>0$.
>
> (a) Show that a field of the form $\mathbf{E} = \dfrac{A}{r^2}\hat{r}$ ($r$ measured from the centre), *the same* in the oil and in the air, satisfies every boundary condition — on the oil surface and on the metal — and find $A$.
>
> (b) Find $\mathbf{D}$ in the air and in the oil, and the free surface charge density on the upper and lower hemispheres. How is $Q$ shared between them?
>
> (c) Find $\mathbf{P}$ in the oil and the bound charge on the oil's surfaces: where it touches the sphere, and on the flat surface $z = 0$. Show that the *total* (free plus bound) surface charge density is the same on both hemispheres.
>
> (d) Find the potential of the sphere relative to infinity, and compare with the same sphere entirely in air and entirely in oil.
>
> *Source: classic (sphere half-immersed in a dielectric), new numbers.*

> [!hint]- Hint
> The oil surface passes through the centre, so a radial field lies *along* it everywhere: only the tangential condition does any work there, and it holds if $A$ is the same above and below. With $\mathbf{E}$ common, $\mathbf{D}$ is not: apply $\oint\mathbf{D}\cdot d\mathbf{S} = Q$ to a sphere made of an air hemisphere and an oil hemisphere. Lecture 7's uniqueness theorem says a field that meets every condition is *the* field.

> [!solution]- Solution
> **(a) Setup.** Seen from the sphere, the oil and the air sit side by side — the spherical version of 9.2 — so try a common $\mathbf{E}$ and check every condition:
>
> - *Oil surface* ($z = 0$, $r>a$, $\hat{n} = \hat{z}$): there $\hat{r}$ lies in the plane, so $\mathbf{E}$ is purely tangential and equal on both sides, $\hat{z}\times(\mathbf{E}_1-\mathbf{E}_2) = 0$ ✓. Both $\mathbf{D}$'s are tangential too, so $\hat{z}\cdot(\mathbf{D}_1-\mathbf{D}_2) = 0$ ✓, as required with no free charge on the oil surface.
> - *Metal* ($r = a$): $\mathbf{E}\parallel\hat{r}$ is normal to the surface ✓, and $V = A/r$ is the same all over $r = a$ ✓ (an equipotential).
> - In each homogeneous half, $V = A/r$ satisfies Laplace's equation ✓, and $\mathbf{E}\to0$ at infinity ✓.
>
> By uniqueness, this is the field. To find $A$, apply Gauss's law for $\mathbf{D}$ to a sphere of radius $r>a$, with $\mathbf{D} = \epsilon_0\mathbf{E}$ on the air half and $2\epsilon_0\mathbf{E}$ on the oil half:
> $$
> \oint\mathbf{D}\cdot d\mathbf{S} = 2\pi r^2\cdot\frac{\epsilon_0A}{r^2}+2\pi r^2\cdot\frac{2\epsilon_0A}{r^2} = 6\pi\epsilon_0A = Q\ \Rightarrow\ A = \frac{Q}{2\pi(\epsilon_0+\epsilon)} = \frac{Q}{6\pi\epsilon_0}\approx180\ \text{V}\cdot\text{m}.
> $$
> At the sphere, $E(a) = A/a^2\approx1.80\times10^4$ V/m.
>
> **(b)** $\mathbf{D}_{\text{air}} = \dfrac{\epsilon_0A}{r^2}\hat{r}$ and $\mathbf{D}_{\text{oil}} = \dfrac{2\epsilon_0A}{r^2}\hat{r}$. On the metal $\rho_s = \hat{r}\cdot\mathbf{D}(a)$: $\epsilon_0E(a)\approx159$ nC/m² on the upper hemisphere and $2\epsilon_0E(a)\approx318$ nC/m² on the lower. Times the hemisphere area $2\pi a^2$: **10 nC above, 20 nC below**. The charge is shared in the ratio $\epsilon_0:\epsilon = 1:2$ — it crowds toward the oil.
>
> **(c)** $\mathbf{P}_{\text{oil}} = \mathbf{D}-\epsilon_0\mathbf{E} = \dfrac{\epsilon_0A}{r^2}\hat{r}$ ($\mathbf{P} = 0$ in air). Where the oil touches the sphere its outward normal is $-\hat{r}$: $\rho_{sb} = -\epsilon_0E(a)\approx-159$ nC/m², $-10$ nC in all. On the flat surface $z = 0^-$ (outward normal $+\hat{z}$), $\mathbf{P}\cdot\hat{z} = 0$ because $\mathbf{P}\parallel\hat{r}$ lies in that plane: no bound charge there. In the bulk $r^2P_r$ is constant, so $\rho_b = 0$. The net surface charge on the lower hemisphere is $318-159 = 159$ nC/m², the same as on the upper one ✓. So the *total* charge on the sphere is uniform, $10+10 = 20$ nC, and a uniform 20 nC sphere in vacuum gives $\dfrac{20\ \text{nC}}{4\pi\epsilon_0r^2}$, which is exactly $A/r^2$ ✓. That is the deeper reason the field is spherically symmetric although the material is not.
>
> (The oil as a whole is neutral: the matching $+10$ nC of bound charge sits on the bath's distant walls, too spread out to matter here.)
>
> **(d)** $V(a) = \displaystyle\int_a^\infty\frac{A}{r^2}dr = \frac Aa = \frac{Q}{6\pi\epsilon_0a}\approx1.80$ kV. All in air it would be $\dfrac{Q}{4\pi\epsilon_0a}\approx2.70$ kV; all in oil $\dfrac{Q}{8\pi\epsilon_0a}\approx1.35$ kV. Half in oil gives exactly two thirds of the air value: the sphere sees the average permittivity $(\epsilon_0+\epsilon)/2 = 1.5\epsilon_0$.
>
> **Answer.** (a) $A = Q/[2\pi(\epsilon_0+\epsilon)] = Q/(6\pi\epsilon_0)\approx180$ V·m; $\mathbf{E} = (A/r^2)\hat{r}$ in both media, $E(a)\approx18.0$ kV/m. (b) $\mathbf{D} = \epsilon_0A\hat{r}/r^2$ (air) and $2\epsilon_0A\hat{r}/r^2$ (oil); $\rho_s\approx159$ nC/m² (upper) and $318$ nC/m² (lower); 10 nC above, 20 nC below. (c) $\mathbf{P} = \epsilon_0A\hat{r}/r^2$ in oil; $\rho_{sb}\approx-159$ nC/m² ($-10$ nC) on the oil touching the sphere, 0 on the flat surface, $\rho_b = 0$; net 159 nC/m² on both hemispheres. (d) $V\approx1.80$ kV (all in air 2.70 kV, all in oil 1.35 kV).

### Sources for this page
Course notes, Lecture 9: the $\mathbf{D}$-first chain, and Example 3 (charged sheet between grounded plates) and Example 4 (graded dielectric), re-parameterized in 9.7 and 9.6. FA26 homework: HW4 #2 behind 9.7, and HW4 #6, the cylindrical analogue of 9.10. Old exams: Summer 2020 HE2 #1a (9.1) and SP18 Exam 1 #4 (9.8), re-parameterized; SP18 Exam 1 #1(i), whose style 9.3 follows; and Summer 2019 HE1 (conflict) #3a (9.10), re-parameterized, which has the same layout as Summer 2018 HE1 #3a and Summer 2019 HE1 #3a. Classic textbook problems with new numbers: the graded coaxial cable (9.11) and the sphere half-immersed in a dielectric (9.12). Problems 9.2, 9.4, 9.5 and 9.9 are original.

*Previous: [[practice/08-conductors-dielectrics-and-polarization|Lecture 8 practice]] · next: [[practice/10-capacitance-and-conductance|Lecture 10 practice]] · [[practice/index|all practice]]*
