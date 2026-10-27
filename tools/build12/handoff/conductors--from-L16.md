<!-- for concepts/conductors, from Lecture 16 §4 -->
<!-- Batch D → B. The perfect-conductor (PEC) material of Lecture 16 §4. The four dynamic boundary conditions and
     the two slide exercises are handed to A (boundary-conditions--from-L16.md), which keeps the exercises; here only
     the PEC physics and the field picture. The lecture page links [[concepts/conductors]] (no anchor). -->

**Aliases to add:** "perfect conductor", "PEC", "perfect electric conductor".

**Physics (a paragraph for the page, after "The course also takes H = B = 0 inside a PEC"):**

**Perfect conductor in time-varying fields** ([[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations#4-boundary-conditions--same-for-dynamics|Lecture 16 §4]]). Medium 2 a PEC, $\sigma\to\infty$, $\mathbf{E} = 0$ inside. Faraday inside gives $\partial\mathbf{B}/\partial t = -\nabla\times\mathbf{E} = 0$, so no *time-varying* $\mathbf{B}$ exists in it either — the class's reason for setting $\mathbf{H} = 0$ inside (a static $\mathbf{B}$ frozen in is the exception; the course never uses one). With the [[concepts/boundary-conditions|four boundary conditions]] and $\hat n$ out of the metal into medium 1:

> [!key] Fields just outside a perfect conductor ($\hat n$ out of the metal)
> $$
> \hat n\cdot\mathbf{D}_1 = \rho_s,\qquad \hat n\times\mathbf{E}_1 = 0,\qquad \hat n\cdot\mathbf{B}_1 = 0,\qquad \hat n\times\mathbf{H}_1 = \mathbf{J}_s\ \ (\text{equivalently } \mathbf{H}_{1t} = \mathbf{J}_s\times\hat n).
> $$
> $E_{1t} = 0$ and $B_{1n} = 0$: $\mathbf{E}$ meets the surface *normally* and ends on $\rho_s = \hat n\cdot\mathbf{D}_1$; $\mathbf{H}$ runs *tangentially*, carried by the surface current $\mathbf{J}_s = \hat n\times\mathbf{H}_1$. An oblique arrow just outside is neither $\mathbf{E}$ nor $\mathbf{H}$; a tangential one can only be $\mathbf{H}$, a normal one only $\mathbf{E}$ (the slide's picture quiz, answer (e)). A typed slide's "$D_{1n} = \rho$" means $\rho_s$.

**Examples (short; the full slide exercises are on boundary-conditions):**
- $\mathbf{D} = D_0\langle1,-2,2\rangle$ pointing away from a conductor's surface: $\rho_s = \lvert\mathbf{D}\rvert = 3D_0$; $\mathbf{D} = D_0\langle1,0,\sqrt3\rangle$ pointing toward it: $\rho_s = -\lvert\mathbf{D}\rvert = -2D_0$.
- A radiating current sheet backed by a PEC, and the PEC mirror of Lecture 26 ($\mathbf{J}_s = \hat n\times\mathbf{H}$ on the mirror): the same two conditions at work ([[concepts/current-sheet-radiation]], [[concepts/standing-waves]]).

**Trap:**
> [!trap]
> - "$\mathbf{H} = 0$ inside a PEC" is a consequence of Faraday's law for *time-varying* fields plus the course convention, not a property of $\sigma$ alone.
> - $\mathbf{J}_s = \hat n\times\mathbf{H}_1$, not $\mathbf{H}_1\times\hat n$: check with the Lecture 13 sheet, $\mathbf{H} = \tfrac12\mathbf{J}_s\times\hat n$ on each side.

**Exam item:** the PEC cases of the boundary conditions — draw $\hat n$ first, then $\rho_s = \hat n\cdot\mathbf{D}_1$, $\mathbf{J}_s = \hat n\times\mathbf{H}_1$; which field pictures are possible outside a conductor.

**Where it appears (add):** [[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations#4-boundary-conditions--same-for-dynamics|Lecture 16 §4]]; Lecture 25–26 (reflection from a PEC).

**Related (add):** [[concepts/current-sheet-radiation]] · [[concepts/standing-waves]].
