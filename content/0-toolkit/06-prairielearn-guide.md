---
title: "PrairieLearn guide"
description: "How to use the course's randomized practice questions on pl.vops.ch: signing in, how variants, tries and points work, how to enter answers, the seven assessments and when to use each, and a short note on how to approach each of the 41 questions."
tags: [toolkit, practice, prairielearn]
aliases: ["PrairieLearn", "PL", "pl.vops.ch", "practice exam"]
---

The site's practice problems are fixed and printed. The PrairieLearn questions are **randomized**: every attempt gives new numbers, new orientations and new statement pools, and the server grades your answer at once. Use the site to learn a method and PrairieLearn to check that the method works on numbers you haven't seen.

> [!tip] The link
> **[pl.vops.ch](https://pl.vops.ch)**: sign in with Google, then open **ECE 329 Fields and Waves I → Fall 2026**.

## 1. Getting in

1. Open [pl.vops.ch](https://pl.vops.ch) and choose **Sign in with Google**.
2. On the home page, open **ECE 329 Fields and Waves I**, course instance **Fall 2026**. If it isn't listed, use **Add or remove courses** on the home page to enrol. If it isn't there either, the server's owner has to add your account.
3. The **Assessments** page lists seven sets (§3). Open one, then open a question.

## 2. How a question works

- **Variants.** Each time you open a question you get a *variant* with its own numbers. **Save & Grade** grades the current variant. **New variant** gives you fresh numbers once you have finished or given up on one.
- **Points (practice sets).** A correct variant earns its points (usually 5) up to the question's maximum (usually 15), so full credit means three correct variants. That is deliberate: getting the same method right three times is what makes it stick. Points here count for nothing outside this server.
- **Tries.** Each variant allows 2–3 submissions. After a wrong one, a **hint** may unfold below the question. Try the question once on paper before reading it.
- **The solution.** When a variant is finished, its worked answer appears below the question. Read it even when you were right; it often shows a faster route or a check.
- **Entering numbers.** Most answers must be within **1 %** (a few within 2 %), so carry three or four significant figures and round only at the end. When a part says *signed*, the sign is the direction: give $-12.5$, not $12.5$, for a component along $-\hat z$. Each box shows its unit; enter the number in that unit. "Coefficient of $\epsilon_0$" means you type the number only.
- **Symbolic answers** (Exam 1 practice, problem 1): use `x`, `y`, `z`, `E0` and `epsilon`, write every product with `*`, and powers with `**` (`3*x**2*y`).
- **Select all that apply.** Each statement is marked separately, so partial credit counts. Judge every statement on its own; the number of true statements changes from variant to variant.
- **Matching.** Each item on the left has exactly one partner; partners can repeat.

> [!warning] What PrairieLearn does not cover yet
> The questions stop at **Lecture 19**. For **Lecture 20 (Poynting's theorem)**, which is on Midterm 2, use the site's [[practice/20-poynting-theorem-and-power|Lecture 20 practice set]] and §9 of the [[0-toolkit/05-midterm-2-summary|Midterm 2 summary]].

## 3. The assessments

| assessment | what is in it | lectures | use it |
|---|---|---|---|
| Practice 1 · Exam 1 practice | the five FA26 Exam 1 problem families | 2–10 | review for the final; Exam 1 tools reappear in Midterm 2 |
| Practice 2 · Dielectrics and lossy capacitors | HW4-style layered and lossy capacitors | 6–10 | as above |
| Practice 3 · Magnetostatics | Ampère, current sheets, a solenoid, Faraday | 12–15 | **Midterm 2**, first pass |
| Practice 4 · Concept checks L1–11 | one concept question per lecture | 1–11 | Lecture 11 (Drude) is on Midterm 2 |
| Practice 5 · Concept checks L12–19 | one concept question per lecture | 12–19 | **Midterm 2**: do all eight |
| Practice 6 · Midterm 2 exam-style | nine multi-part problems modelled on past Exam 2 papers | 11–19 | **Midterm 2**, untimed |
| Practice Exam 1 · Midterm 2 practice exam | five problems drawn from pools, **75-minute timer** | 11–19 | **Midterm 2**, timed, last |

**The practice exam** is set up like a real exam: one quick-fire set plus one problem from each of four pools (Ampère and the vector potential, Faraday, inductance, waves), with a 75-minute timer. Each question is worth 20 points if your first submission is right, 14 on the second and 8 on the third. You can start a fresh instance (different draws and numbers) as often as you like. Take it with the page closed and a sheet of scrap paper, then compare its draws with the [[0-toolkit/05-midterm-2-summary#11-the-traps-that-cost-the-most-points|traps list]].

## 4. The questions, and how to approach them

Each note says what the question exercises and the route through it: which law to use, in what order, and what to check. It is a plan, not a hint. The hints that open after a wrong submission go a step further.

### Practice 1 · Exam 1 practice

- **Conservative field: curl, potential, charge density, line integral** (Lectures 4–5). Take the curl component by component first: that tells you whether a potential exists. Build $V$ so that $-\nabla V$ gives back every component, then differentiate it to check. $\rho$ follows from $\epsilon_0\nabla\cdot\mathbf{E}$. Use $V$ for the line integral rather than parametrizing a path; then check the sign: $\int_A^B\mathbf{E}\cdot d\mathbf{l} = V(A)-V(B)$.
- **Gauss's law: non-uniform charged slab** (Lectures 3, 5). Integrate $\rho$ across the thickness for the charge per unit area. Then use the slab's mirror symmetry to place a Gaussian pillbox where the field is known, and get $E$ inside (a function of $x$) and outside (a constant). Integrate $E$ piecewise from $0$ to $b$ for the potential, minding the sign.
- **Boundary conditions at a dielectric interface** (Lectures 6, 8, 9). Split the given field into tangential and normal parts. Each part obeys its own condition across the plane, so carry each across separately. Then $\mathbf{D} = \epsilon\mathbf{E}$ and $\mathbf{P} = \mathbf{D}-\epsilon_0\mathbf{E}$ on each side, and the bound surface charge from the polarizations, with the stated $\hat n$.
- **Coaxial cable with two dielectric layers** (Lectures 3, 8–10). Gauss's law with a cylinder gives $\mathbf{D}$, which knows only about free charge. Divide by each layer's $\epsilon$ for $\mathbf{E}$, then integrate across both layers for the voltage. The capacitance per unit length is charge over voltage.
- **Flux through a plane from two point charges** (Lectures 2–3). Superpose: find each charge's flux through the whole plane on its own, then add them. Watch which way each charge's field crosses the plane relative to the stated $\hat n$.

### Practice 2 · Dielectrics and lossy capacitors

- **Two dielectric layers between parallel plates** (Lectures 6, 9, 10). Start from the measured field. With no free charge on the interface, find the quantity that is continuous across it and use it to get the other slab's field. Get the potentials from $V(z) = -\int_0^zE_z\,dz'$, starting at the grounded plate. The plate charge is $\mathbf{D}$ at the plate, and the capacitance per unit area is charge over voltage.
- **Charge sheet between two grounded plates** (Lectures 6, 7). In each charge-free region $V$ is linear. Pin it with $V = 0$ at both plates and the unknown $V_0$ at the sheet, then let the jump in $D_z$ across the sheet fix $V_0$. The induced charges follow from $\mathbf{D}$ at each plate. Check that the induced charges and the sheet's charge add to zero.
- **Filling a capacitor with a dielectric** (Lectures 8–10). First decide what is held fixed: the plate charge (battery removed) or the voltage (battery connected). That decides whether $\mathbf{D}$ or $\mathbf{E}$ stays the same, and everything else follows from $\mathbf{D} = \epsilon\mathbf{E}$, $\mathbf{P} = \mathbf{D}-\epsilon_0\mathbf{E}$ and $w = \tfrac12\mathbf{D}\cdot\mathbf{E}$. For the conducting fluid, ask what a steady state allows in each case.
- **Lossy capacitor: capacitance, conductance and self-discharge** (Lectures 8, 10). $C$ from the geometry, then $G$ from the same geometry. Compare the two formulas before computing the time constant. Then the charge decays exponentially, and the initial current is the initial charge divided by the time constant.

### Practice 3 · Magnetostatics

- **Ampère's law: magnetic field of a coaxial cable** (Lecture 12). One Amperian circle per region. Most of the work is $I_{\text{enc}}$: what fraction of each conductor's current lies inside the circle, with signs. Then $H_\phi = I_{\text{enc}}/2\pi r$. Redo the outside region for the "same direction" variant.
- **Two parallel current sheets: superposition and force** (Lecture 13). Write each sheet's field on both of its sides with $\tfrac12\mathbf{J}_s\times\hat n$, with $\hat n$ pointing toward the field point. Then add them region by region. For the force on sheet 2, decide whose field acts on it before using $\mathbf{J}_s\times\mathbf{B}$.
- **Long solenoid: field, flux, inductance and stored energy** (Lectures 13, 15). Chain: Ampère gives $H$, then flux through one turn, then $L = N\Psi/I$, then $W = \tfrac12LI^2$, then the $L/R$ time constant. Check $W$ against $\int\tfrac12\mu_0H^2\,dV$.
- **Faraday's law: emf and current in a loop** (Lecture 14). Flux through one turn from $\mathbf{B}\cdot d\mathbf{S}$ with the stated $d\mathbf{S}$, then the emf of $N$ turns, then $I = \mathcal{E}/R$. Read the circulation direction from the sign, and confirm it with Lenz.

### Practice 4 · Concept checks, Lectures 1–11

- **Lorentz force and the velocity selector** (Lectures 1–2). Compute $\mathbf{v}\times\mathbf{B}$ with a determinant, add $\mathbf{E}$ and multiply by $q$. For the power, ask which part of the force can do work. For the selector, test each of the six injection directions: the beam passes undeflected only when the electric and magnetic forces cancel.
- **Two point charges: the null point** (Lecture 2). Decide the region first, using the signs and sizes of the charges, then solve the one equation for the position there. At an off-axis point, add the two Coulomb fields as vectors, component by component.
- **Gauss's law: which symmetry, which surface** (Lecture 3). Match each distribution to its symmetry (spherical, cylindrical, planar) and the field shape that follows. Gauss's law gives the field only when symmetry fixes its direction and makes its size constant on the surface. For the ball and shell, find $Q_{\text{enc}}$ region by region.
- **Divergence and curl of a linear field** (Lecture 4). Divergence and curl straight from the matrix entries. Use Stokes's theorem for the circulation. Then ask which equations the field would have to obey to be a static $\mathbf{E}$, a $\mathbf{B}$, or a steady current, and test it against them.
- **Potential by superposition, work and potential energy** (Lecture 5). Potentials add as scalars. The work of a slow external agent is the change of the charge's potential energy, so only the end points matter. Keep "work by the agent" and "work by the field" apart; they differ by a sign.
- **Magnetic boundary conditions at current sheets** (Lecture 6). Use the two magnetic conditions with $\hat n$ from medium 2 into medium 1: tangential $\mathbf{H}$ jumps by the surface current, normal $\mathbf{B}$ is continuous. Write the cross product out in components every time. To find $\mathbf{J}_s$ from fields, run the same condition backwards.
- **Poisson's equation in a pn junction** (Lecture 7). Overall charge neutrality relates the two depletion widths. Integrating Poisson's equation once gives a field that varies linearly in each layer, peaking at the junction. Integrating again gives the built-in potential, which is the area under the field.
- **A charge inside a conducting shell; relaxation** (Lecture 8). $\mathbf{E} = 0$ in the metal plus Gauss's law fixes the charge on each surface. The field in each region then follows from Gauss's law. For "what changes", ask which surface can feel the cavity charge's position. Relaxation is an exponential with the material's own time constant.
- **Bound charge in an electret slab** (Lectures 8–9). Volume bound charge comes from the divergence of $\mathbf{P}$, and surface bound charge from $\mathbf{P}$ at each face with its outward normal. Add them as a check: the total is fixed. With no free charge anywhere, ask what $\mathbf{D}$ must be, then get $\mathbf{E}$.
- **Pulling capacitor plates apart** (Lecture 10). Again decide first what is fixed: charge or voltage. Then compute $C$ and $W$ before and after. Write the energy balance: your work plus the battery's work equals the change in stored energy. The force comes from the energy, or from $\tfrac12\rho_sE$.
- **Drude and Lorentz models** (Lecture 11). DC conductivity from $Nq^2\tau/m$, then mobility, then drift speed from the field the wire carries. For AC, compare $\omega\tau$ with 1: that one number gives the size and phase of $\sigma(\omega)$. For the Lorentz part, ask where the frequency sits relative to the resonance.

### Practice 5 · Concept checks, Lectures 12–19

- **Biot–Savart for loops of arcs and radial segments** (Lecture 12). Break the loop into pieces and apply Biot–Savart to each piece at O. Decide each piece's contribution from the geometry of $d\mathbf{l}\times\hat R$ before integrating anything, then add with signs from each piece's sense of circulation.
- **Ampère's law by symmetry; toroid; vector potential** (Lecture 13). For each current distribution, find the direction symmetry forces on $\mathbf{H}$ and the Amperian path that follows. For the toroid: a circle inside the core, then integrate $B$ over the rectangular cross-section for the flux. Set the sign by the winding sense.
- **Motional emf of a rotating rod** (Lecture 14). Each piece of the rod moves at a different speed, so integrate $(\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l}$ along it. The direction of $\mathbf{v}\times\mathbf{B}$ says which end the positive charge piles up at. With a load, find the current, and get the power two ways (electrical and mechanical) as a check.
- **Mutual inductance and switching on an RL circuit** (Lecture 15). The solenoid's field inside, then the flux through each pick-up turn (only through that turn's own area), then $M$, then the emf from $dI_1/dt$. For the switch-on, write the circuit equation and its exponential solution, and read the time constant.
- **Displacement current; fields at a perfect conductor** (Lecture 16). Charge conservation links the lead current to $\partial\mathbf{D}/\partial t$ in the gap. Ampère–Maxwell around a circle gives $H_\phi$, inside and beyond the plate radius. At the metal, the field just outside gives the surface charge and surface current. Use the normal pointing out of the conductor.
- **Magnetization, B and H in a magnet; materials; interfaces** (Lecture 17). Get the surface magnetization current from $\mathbf{M}$ and the side wall's normal, then compare it with a solenoid's $nI$. Inside a long magnet, find $\mathbf{B}$ first, then $\mathbf{H} = \mathbf{B}/\mu_0-\mathbf{M}$. Classify materials by the sign and size of $\chi_m$. At an interface, carry the normal $\mathbf{B}$ and tangential $\mathbf{H}$ across separately.
- **Reading a plane-wave pulse** (Lecture 18). Read the direction from the relative sign of the time and position terms, and the speed from the ratio of their coefficients. $\epsilon_r$ follows from the speed. Get $\mathbf{H}$ from $\hat u\times\mathbf{E}/\eta$ with this medium's $\eta$, and find where the peak sits by setting the pulse's argument to its peak value.
- **A cosine current sheet: parameters, fields, Poynting vector** (Lecture 19). Wave parameters from the medium's speed and the frequency. At the field point, evaluate the sheet's delayed current on that side, then $\mathbf{E}$ and $\mathbf{H}$ with their directions. Take $\mathbf{S} = \mathbf{E}\times\mathbf{H}$ and check that it points away from the sheet.

### Practice 6 · Midterm 2 exam-style (also the practice exam's pools)

- **Quick-fire multiple choice** (Lectures 11–19). Six one-concept items. Work each on paper before looking at the choices, because the wrong choices are the usual slips (a dropped ½, a reversed cross product, the wrong $\epsilon$).
- **Two current slabs and a sheet** (Lectures 12–13). Superpose three sources: two slabs and a sheet. Outside a slab, it acts like a sheet carrying its total current per unit width; inside, its own contribution changes linearly. Do each source alone, add at the five points, and sketch $H$ against position to check the jumps and slopes.
- **From a vector potential to B, the current and E** (Lectures 13, 15). $\nabla\cdot\mathbf{A}$ and $\mathbf{B} = \nabla\times\mathbf{A}$ term by term. Then, depending on the variant, the surface current from the jump in tangential $\mathbf{H}$, or the volume current from $\nabla\times\mathbf{H}$. For the time-varying part, use $\mathbf{E} = -\partial\mathbf{A}/\partial t$.
- **Nested solenoids, Lenz, coaxial loop** (Lectures 13–14). Each ideal solenoid contributes only inside itself, so add them region by region. Cancellation is one equation for $I_2$. For the induced emf, find the flux through the loop region by region (each region with its own field), then differentiate. Get the direction from Lenz.
- **A loop moving through a graded field** (Lecture 14). First decide which motions change the flux at all. That depends on the loop's orientation and on the direction of the field's variation. Then write $\Psi(t)$ by integrating $\mathbf{B}$ over the loop at its current position, differentiate, divide by $R$, and find the direction with Lenz.
- **Three voltmeters in a changing flux** (Lecture 14). Find the circuit current from the total emf and resistance. Then, for each meter, apply Faraday's law to the closed path formed by its leads and a branch of the circuit. Account for the resistor drops along the branch and for any flux that path encloses.
- **Inductance and energy of a magnetically filled parallel-plate line** (Lectures 13, 15, 17). The plates are two opposite current sheets, so find $H$ between them and outside. Then $B = \mu H$, the flux through the gap's side cross-section, $L = \Psi/I$, and the energy two ways. Get the magnetization and its surface current from $\mathbf{M} = \chi_m\mathbf{H}$.
- **A pulse on the move through a dielectric** (Lecture 18). Write the field at any $(z, t)$ by shifting the given snapshot by the distance travelled since $t_0$, in the right direction. Each event is then a lookup in the snapshot. The medium follows from the speed, and $\mathbf{H}$ from $\hat u\times\mathbf{E}/\eta$.
- **A current-sheet pulse launches two waves** (Lecture 19). Fix the field directions from $\mathbf{J}_s$ and the side you are on. At a given point and time, evaluate the source waveform at the delayed time. Compare the two sides: $\mathbf{E}$ behaves one way across the sheet and $\mathbf{H}$ the other. A probe record is the waveform delayed; a snapshot is the waveform laid out in space.
- *Pool alternates in the practice exam:* **Mutual inductance and RL** (above, Practice 5) can be drawn in place of the parallel-plate line.

## 5. A way to use it before Midterm 2

1. **Practice 5** first: one variant of each of the eight concept questions, to find your weak lectures.
2. **Practice 6** untimed: one variant of each problem. Redo the ones you missed with **New variant** until one is right first try.
3. **Practice Exam 1** last, timed. Afterwards, sort every lost point as the [[0-toolkit/05-midterm-2-summary#13-how-to-study-for-it-exam-monday-october-19|Midterm 2 plan]] describes, and fix the cheapest pile first.
4. Lecture 20 is not on the server. Do the site's [[practice/20-poynting-theorem-and-power|Lecture 20 set]] instead.
