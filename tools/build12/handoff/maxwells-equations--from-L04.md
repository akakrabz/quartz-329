<!-- for concepts/maxwells-equations, from Lecture 04 §7 -->
<!-- The integral/differential table is already on the topic page; Lecture 4 §7 adds the "which theorem converts which
     law" column, the EMF/MMF reading, the partial-derivative trap, and the continuity derivation with its identities.
     The vector identities display also lives on concepts/curl (A owns it) — keep one copy or both, your call.
     The continuity derivation could equally go to concepts/continuity-equation (D). -->

**From integral to differential form (Lecture 4 §7).** Each integral law becomes local by the matching theorem plus "true for every surface/volume ⇒ true pointwise":

| integral form | theorem | differential form |
|---|---|---|
| $\oint_C\mathbf{E}\cdot d\mathbf{l} = -\dfrac{\partial}{\partial t}\displaystyle\int_S\mathbf{B}\cdot d\mathbf{S}$ (Faraday) | Stokes | $\nabla\times\mathbf{E} = -\dfrac{\partial\mathbf{B}}{\partial t}$ |
| $\oint_C\mathbf{H}\cdot d\mathbf{l} = \displaystyle\int_S\Big(\mathbf{J}+\dfrac{\partial\mathbf{D}}{\partial t}\Big)\cdot d\mathbf{S}$ (Ampère–Maxwell) | Stokes | $\nabla\times\mathbf{H} = \mathbf{J}+\dfrac{\partial\mathbf{D}}{\partial t}$ |
| $\oint_S\mathbf{D}\cdot d\mathbf{S} = \displaystyle\int_V\rho\,dV$ (Gauss) | divergence | $\nabla\cdot\mathbf{D} = \rho$ |
| $\oint_S\mathbf{B}\cdot d\mathbf{S} = 0$ | divergence | $\nabla\cdot\mathbf{B} = 0$ |

$\oint_C\mathbf{E}\cdot d\mathbf{l}$ is an **EMF** (volts), $\oint_C\mathbf{H}\cdot d\mathbf{l}$ an **MMF** (amperes). Ampère's right side: the static **conduction current** $\mathbf{J}$ plus the dynamic **displacement current** $\partial\mathbf{D}/\partial t$ — Maxwell's addition, and the reason light exists ([[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Lecture 16]] onward).

> [!trap] Partial, not total, time derivatives
> Fields depend on $(x,y,z,t)$: use $\partial/\partial t$. Read a slide's $d/dt$ as $\partial/\partial t$.

> [!derivation]- Charge conservation falls out of Ampère–Maxwell
> Take the divergence of the Ampère–Maxwell equation. Since $\nabla\cdot(\nabla\times\mathbf{H}) = 0$ identically,
> $$
> 0 = \nabla\cdot\mathbf{J} + \frac{\partial}{\partial t}\nabla\cdot\mathbf{D} = \nabla\cdot\mathbf{J} + \frac{\partial\rho}{\partial t}
> \quad\Longrightarrow\quad
> \boxed{\ \nabla\cdot\mathbf{J} = -\frac{\partial\rho}{\partial t}\ }
> $$
> the **continuity equation**: current flowing out of a point drains its charge — conservation is built into Maxwell's equations. Identities for any smooth fields:
> $$
> \nabla\cdot(\nabla\times\mathbf{A}) = 0,\qquad
> \nabla\times(\nabla f) = 0,\qquad
> \nabla\times\nabla\times\mathbf{A} = \nabla(\nabla\cdot\mathbf{A}) - \nabla^2\mathbf{A},\qquad \nabla^2\mathbf{A}\equiv\hat{x}\nabla^2A_x+\hat{y}\nabla^2A_y+\hat{z}\nabla^2A_z .
> $$
> (The identity holds in any coordinates; the component-wise Laplacian on the right is valid for *Cartesian* components only.)

> [!exam] On exams (Lecture 4 share)
> Exam 1 never asks for the dynamic equations, but "which Maxwell equation says …" and the differential ↔ integral conversion of Gauss's law recur; keep $\partial/\partial t$ partial and the continuity sign ($\nabla\cdot\mathbf{J}$ *negative* where charge piles up).

**Where it appears (add).** [[1-electrostatics/04-divergence-and-curl#7-the-differential-form-of-maxwells-equations|Lecture 4 §7]] (differential forms via the two theorems; continuity as a consequence).
