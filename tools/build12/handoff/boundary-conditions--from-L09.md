<!-- for concepts/boundary-conditions, from Lecture 09 §2 -->
<!-- Batch B → A. Lecture 9 §2 "Refraction of field lines at an interface": the figure, the key box and the FA26
     problem-3 exam item. Your page's "Two perfect dielectrics" special case already states tan θ1/tan θ2 = ε1/ε2 and
     ρ_sb = P_2n − P_1n; dedupe against it (keep one version). The lecture page links
     [[concepts/boundary-conditions]] (no anchor). -->

**Aliases to add:** "refraction of field lines", "dielectric interface".

**Figure marker (with blank lines around), where the dielectric-interface case is treated:**

<!-- fig:field-refraction -->

**Key box (replaces or extends the "Two perfect dielectrics, no free charge" bullet):**

> [!key] Field lines bend at a dielectric interface
> Two perfect dielectrics, no free charge on the interface; split each side's field into tangential and normal parts:
> $$
> E_{2t} = E_{1t},\qquad \epsilon_2E_{2n} = \epsilon_1E_{1n}\ \Rightarrow\ E_{2n} = \frac{\epsilon_1}{\epsilon_2}E_{1n},
> \qquad\qquad \frac{\tan\theta_1}{\tan\theta_2} = \frac{\epsilon_1}{\epsilon_2}
> $$
> (angles from the normal). Entering the higher-$\epsilon$ medium, the normal component shrinks and the line tilts toward the surface. $\mathbf{D}$, parallel to $\mathbf{E}$, bends by the same angle with the roles swapped: its normal part is continuous, its tangential part scales with $\epsilon$. With free surface charge on the interface, $D_{1n} - D_{2n} = \rho_s$ replaces the second condition ($\hat{n}$ from 2 into 1). The bound surface charge at the interface (with $\rho_s = 0$) is $\rho_{sb} = P_{2n} - P_{1n} = \epsilon_0(E_{1n} - E_{2n})$.

**Prose (one or two sentences after the box):**

This is FA26 Exam 1 problem 3, worked with different numbers in [[problems/fields-across-a-dielectric-interface]], with the checklist of errors: normal $\mathbf{E}$ made continuous, tangential $\mathbf{D}$ made continuous, ratio inverted, $\epsilon_0$ used for $\epsilon$.

**Trap bullets (add to your trap box if not already there):**
> - Normal $\mathbf{E}$ is *not* continuous and tangential $\mathbf{D}$ is *not* continuous at a dielectric interface; the ratio $\epsilon_1/\epsilon_2$ is easily inverted — write $E_{2n} = (\epsilon_1/\epsilon_2)E_{1n}$ and check that the higher-$\epsilon$ side has the smaller $E_n$.
> - Use each side's own $\epsilon$ in $\mathbf{D} = \epsilon\mathbf{E}$, never $\epsilon_0$ for a dielectric.

**Exam item (for your `> [!exam]` box):**
FA26 problem 3 is Lecture 9 §2 verbatim: find $\mathbf{E}_2$ from $\mathbf{E}_1$ ($E_t$ continuous, $E_{2n} = (\epsilon_1/\epsilon_2)E_{1n}$), then $\mathbf{D}_{1,2} = \epsilon_{1,2}\mathbf{E}_{1,2}$, then $\mathbf{P}_{1,2} = \mathbf{D} - \epsilon_0\mathbf{E}$ on each side. Worked in [[problems/fields-across-a-dielectric-interface]]. The most common error: writing $\mathbf{D}$ with an $\epsilon$ in it, i.e. confusing $\mathbf{D}$ with $\mathbf{E}$.

**Where it appears (add):** [[1-electrostatics/09-static-fields-in-dielectric-media#2-refraction-of-field-lines-at-an-interface|Lecture 9 §2]] (refraction of field lines).

**Related (add):** [[concepts/static-fields-in-dielectrics]] · [[concepts/permittivity]] · [[concepts/polarization]].
