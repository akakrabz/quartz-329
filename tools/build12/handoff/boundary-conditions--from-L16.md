<!-- for concepts/boundary-conditions, from Lecture 16 §4 -->
<!-- Batch D → A. Lecture 16 §4 "Boundary conditions — 'same for dynamics'". The perfect-conductor material is
     also handed to B (conductors--from-L16.md); keep the PEC bullet here short and link [[concepts/conductors]].
     The lecture page links [[concepts/boundary-conditions]] (no anchor). Figure marker included (moved off the
     lecture page). Items marked VERBATIM must keep their LaTeX exactly for digest11/loss_check.py L16. -->

**Aliases to add:** "dynamic boundary conditions", "boundary conditions for time-varying fields".

**Key box (VERBATIM display; replaces or sits beside the existing one — the lecture's version carries the dynamic justification):**

> [!key] The four boundary conditions ($\hat n$ from medium 2 into medium 1; the notes' $\pm$ superscripts mean the same)
> $$
> \begin{gathered}
> \hat n\cdot(\mathbf{D}_1-\mathbf{D}_2) = \rho_s,\qquad \hat n\cdot(\mathbf{B}_1-\mathbf{B}_2) = 0,\\[4pt]
> \hat n\times(\mathbf{E}_1-\mathbf{E}_2) = 0,\qquad \hat n\times(\mathbf{H}_1-\mathbf{H}_2) = \mathbf{J}_s .
> \end{gathered}
> $$
> They hold for time-varying fields exactly as for static ones. The first and third come from [[1-electrostatics/06-circulation-and-boundary-conditions|Lecture 6]]; the second is $\oint\mathbf{B}\cdot d\mathbf{S} = 0$ on a vanishing pillbox (no magnetic charge, no jump); the fourth is Ampère–Maxwell on a thin rectangle straddling the interface — the $\partial\mathbf{D}/\partial t$ flux vanishes with the width $w$, as the $\partial\mathbf{B}/\partial t$ flux did in Lecture 6, and only a *surface* current $\mathbf{J}_s$ survives (the notes defer the detailed justification to Lecture 19). [[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential|Lecture 13]]'s current sheet is the fourth condition in action: $\mathbf{H}$ jumps by $J_s$.

**Figure (moved from the lecture page):**

<!-- fig:pec-boundary-fields -->

**Physics / special cases (two special cases carry most of the course from Lecture 16 on):**

- **Two perfect dielectrics** ($\sigma = 0$, so $\mathbf{J}_s = 0$; no free charge, so $\rho_s = 0$): $D_n$, $E_t$, $B_n$, $H_t$ all continuous. The fields still refract ([[1-electrostatics/09-static-fields-in-dielectric-media|Lecture 9]]): $E_n$ and $D_t$ change by the permittivity ratio where $\epsilon_1\neq\epsilon_2$. With different permeabilities, $B = \mu H$ turns continuity of $B_n$ into $\mu_1H_{1n} = \mu_2H_{2n}$ — twin of $\epsilon_1E_{1n} = \epsilon_2E_{2n}$, in ink on the slide and taken up in [[3-maxwell-and-waves/17-magnetization-and-maxwells-equations-in-matter|Lecture 17]].
- **Surface of a perfect conductor** (medium 2, $\sigma\to\infty$, $\mathbf{E} = 0$ inside): Faraday inside gives $\partial\mathbf{B}/\partial t = -\nabla\times\mathbf{E} = 0$, so no *time-varying* $\mathbf{B}$ exists in it either — the class's reason for setting $\mathbf{H} = 0$ inside. Then $E_{1t} = 0$ and $B_{1n} = 0$: $\mathbf{E}$ meets the surface *normally* and ends on $\rho_s = \hat n\cdot\mathbf{D}_1$; $\mathbf{H}$ runs *tangentially*, carried by $\mathbf{J}_s = \hat n\times\mathbf{H}_1$, equivalently $\mathbf{H}_{1t} = \mathbf{J}_s\times\hat n$. (A typed slide's "$D_{1n} = \rho$" means $\rho_s$.) Full treatment: [[concepts/conductors]].

**Examples (slides, worked in class):**

> [!example] Two slide exercises (Lecture 16)
> *Surface charge from $\mathbf{D}$ on a conductor.* (a) $\mathbf{D} = D_0\langle1,-2,2\rangle$ pointing *away* from the surface: $\hat n$ (out of the conductor) is $\langle1,-2,2\rangle/3$, so $\rho_s = \hat n\cdot\mathbf{D} = D_0(1+4+4)/3 = 3D_0$. (b) $\mathbf{D} = D_0\langle1,0,\sqrt3\rangle$ pointing *toward* the surface: $\hat n = -\langle1,0,\sqrt3\rangle/2$ and $\rho_s = -2D_0$ — negative charge, field lines ending on it. Shortcut: $\mathbf{D}$ pointing away gives $\rho_s = \lvert\mathbf{D}\rvert$; pointing in, $\rho_s = -\lvert\mathbf{D}\rvert$.
> *Which pictures are possible just outside a perfect conductor?* An oblique arrow: neither $\mathbf{E}$ nor $\mathbf{H}$. A tangential arrow: $\mathbf{H}$ only ($B_{1n} = 0$, $\hat n\times\mathbf{H}_1 = \mathbf{J}_s$). A normal arrow: $\mathbf{E}$ only ($E_{1t} = 0$, $\hat n\cdot\mathbf{D}_1 = \rho_s$). Answer (e), circled in class.

**Trap (merge with the existing "No differential laws at an interface" bullet):**

> [!trap] At a boundary, use the integral forms
> The slide's bold closing rule: **never** use the differential Maxwell equations at a boundary — the fields are discontinuous and their derivatives are δ-functions. Apply the integral laws to a pillbox or thin loop, shrink, read off the jump. (The mnemonic $\nabla\to\hat n$, field → its difference, $\rho\to\rho_s$, $\mathbf{J}\to\mathbf{J}_s$, drop time derivatives — is the result of doing that, not a substitute.)

**Exam item (from Lecture 16's exam box):**

> [!exam] On exams
> Boundary conditions with surface current: $\hat n\times(\mathbf{H}_1-\mathbf{H}_2) = \mathbf{J}_s$ and the perfect-conductor cases, $\hat n$ drawn first — Exam 1 problem 3's rubric with four conditions instead of two. Later, every reflection problem is condition-matching at an interface.

**Where it appears (add):** [[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations#4-boundary-conditions--same-for-dynamics|Lecture 16 §4]] (declared valid for time-varying fields; PEC cases; slide exercises); [[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets#4-the-same-result-from-boundary-conditions-slides|Lecture 19 §4]] (a radiating sheet: $E_t$ continuous, $H_t$ jumps by $J_s$; [[concepts/current-sheet-radiation]]).

**Related (add):** [[concepts/current-sheet-radiation]] · [[concepts/maxwells-equations]].

**Inline formulas the loss check looks for (all in the text above):** $\partial\mathbf{B}/\partial t = -\nabla\times\mathbf{E} = 0$, $E_{1t} = 0$, $B_{1n} = 0$, $\rho_s = \hat n\cdot\mathbf{D}_1$, $\mathbf{J}_s = \hat n\times\mathbf{H}_1$, $D_{1n} = \rho$, $\mu_1H_{1n} = \mu_2H_{2n}$, $\epsilon_1E_{1n} = \epsilon_2E_{2n}$, the two exercises' vectors and results, $\hat n\times\mathbf{H}_1 = \mathbf{J}_s$, $\hat n\cdot\mathbf{D}_1 = \rho_s$.
