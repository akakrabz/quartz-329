<!-- for concepts/boundary-conditions, from Lecture 17 §6 -->
<!-- Batch D → A. Lecture 17 §6 "Boundary conditions in magnetic media". The section's recipe ("Problems with
     magnetic media") and the slab-between-sheets example (with fig:mag-slab-between-sheets) are on D's pages
     concepts/permeability and concepts/magnetization — not duplicated here. The lecture page links
     [[concepts/boundary-conditions]] (no anchor). The key display must stay VERBATIM for loss_check.py L17. -->

**Aliases to add:** "magnetic boundary conditions", "refraction of B-lines".

**Key box (VERBATIM; extends the existing "Two magnetic media" bullet):**

> [!key] Magnetic boundary conditions ($\hat n$ from medium 2 into medium 1)
> $$
> \hat n\cdot(\mathbf{B}_1-\mathbf{B}_2) = 0\ \Longrightarrow\ \mu_1H_{1n} = \mu_2H_{2n},\qquad\qquad \hat n\times(\mathbf{H}_1-\mathbf{H}_2) = \mathbf{J}_s\ \ (\text{free}).
> $$
> Without free surface current $\mathbf{H}_t$ (so $\mathbf{B}_t/\mu$) is continuous and $B$- and $H$-lines **refract** alike:
> $$
> \frac{\tan\theta_1}{\tan\theta_2} = \frac{\mu_1}{\mu_2}\qquad(\text{angles from the normal}).
> $$
> Tangential $\mathbf{B}$ jumps by the bound current, $\hat n\times(\mathbf{B}_1-\mathbf{B}_2)/\mu_0 = \mathbf{J}_s + \hat n\times(\mathbf{M}_1-\mathbf{M}_2)$; normal $\mathbf{H}$ jumps too, $H_{1n}-H_{2n} = -(M_{1n}-M_{2n})$ — "$\nabla\cdot\mathbf{H} = 0$" fails here, $\nabla\cdot\mathbf{B} = 0$ never.

**Figure (moved from the lecture page):**

<!-- fig:mag-refraction -->

**Physics (prose for the page):** Lecture 16's conditions are already macroscopic (free $\rho_s$, $\mathbf{J}_s$); with $\mathbf{B} = \mu\mathbf{H}$ they give the box above. This is [[1-electrostatics/09-static-fields-in-dielectric-media#2-refraction-of-field-lines-at-an-interface|Lecture 9's refraction law]] with $\epsilon\to\mu$ (ink: $\mu_1H_{n1} = \mu_2H_{n2}$, $B_{n1} = B_{n2}$); numbers in [[problems/fields-across-a-magnetic-interface]]. Iron, $\mu_r = 5000$: 85° inside leaves at 0.13°, 89.9° at 6.5° — almost normal, like $\mathbf{E}$ at a conductor; hence iron pole pieces in motors and loudspeakers.

**Example (pointer):** the slides' slab of $\mu_r = 100$ between sheets $\mp0.1\hat y$ A/m — $H_t$ continuous across the slab faces (no free $J_s$ on the slab), so $\mathbf{H} = 0.1\hat x$ A/m inside, $\mathbf{B} = 1.26\times10^{-5}\hat x$ T; worked on [[concepts/magnetization]]. The recipe (free currents → $\mathbf{H}$ → $\mathbf{B} = \mu\mathbf{H}$ → $\mathbf{M}$ last) is on [[concepts/permeability]].

**Trap (add a bullet):** normal $\mathbf{H}$ and tangential $\mathbf{B}$ *do* jump at a magnetic interface; only $B_n$ and (without free $J_s$) $H_t$ pass.

**Exam item:** interface problems like FA26 Exam 1 #3 with $\epsilon\to\mu$, $\mathbf{E}\to\mathbf{H}$: write $B_{1n} = B_{2n}$ and $H_{1t} = H_{2t}$, convert with $\mu$ region by region.

**Where it appears (add):** [[3-maxwell-and-waves/17-magnetization-and-maxwells-equations-in-matter#6-boundary-conditions-in-magnetic-media|Lecture 17 §6]].

**Related (add):** [[concepts/permeability]] · [[concepts/magnetization]] · [[concepts/magnetic-materials]].

**Inline formulas the loss check looks for (in the text above):** $\mu_1H_{n1} = \mu_2H_{n2}$, $B_{n1} = B_{n2}$, $\mu_r = 5000$, $\hat n\times(\mathbf{B}_1-\mathbf{B}_2)/\mu_0 = \mathbf{J}_s + \hat n\times(\mathbf{M}_1-\mathbf{M}_2)$, $H_{1n}-H_{2n} = -(M_{1n}-M_{2n})$, $\nabla\cdot\mathbf{H} = 0$, $\nabla\cdot\mathbf{B} = 0$.
