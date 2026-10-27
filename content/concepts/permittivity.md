---
title: "Permittivity, susceptibility, and D = εE"
description: "For linear dielectrics P = ε₀χeE, so D = ε₀(1 + χe)E = εE with ε = εrε₀. One number replaces the whole polarization story; typical εr values; what changes and what does not when a dielectric is inserted."
tags: [concept, electrostatics, exam-1]
aliases: ["dielectric constant", "relative permittivity", "electric susceptibility", "constitutive relation", "linear dielectric", "slab between charged plates"]
---

> [!key] Constitutive relation of a linear, isotropic dielectric
> $$
> \mathbf{P} = \epsilon_0\chi_e\,\mathbf{E}\quad\Longrightarrow\quad
> \mathbf{D} = \epsilon_0\mathbf{E} + \epsilon_0\chi_e\mathbf{E} = \epsilon_0(1+\chi_e)\,\mathbf{E} = \epsilon\,\mathbf{E},
> \qquad \epsilon = \epsilon_r\epsilon_0,\quad \epsilon_r = 1+\chi_e .
> $$
> $\chi_e\ge0$: dimensionless **electric susceptibility**; $\epsilon_r$: dimensionless **relative permittivity** ("dielectric constant"); $\epsilon$: **permittivity** [F/m], $\epsilon_0 = 8.854\times10^{-12}$ F/m $\approx 10^{-9}/36\pi$. The $\mathbf{E}$ in $\mathbf{P} = \epsilon_0\chi_e\mathbf{E}$ is the **total** field in the material — applied plus the polarization's own — not the applied field alone. Typical $\epsilon_r$: vacuum 1, air 1.0006, glass 4–10, dry-to-wet soil 5–10, silicon 11–12, distilled water 81.

**Physics.** For most materials at ordinary fields, $\mathbf{P}$ is proportional to the total field, and the whole bound-charge story of [[concepts/polarization|Polarization P and bound charge]] collapses into one number. With $\epsilon$ known, use $\mathbf{D} = \epsilon\mathbf{E}$ and the free charges; recover $\mathbf{P} = \mathbf{D} - \epsilon_0\mathbf{E} = (\epsilon_r-1)\epsilon_0\mathbf{E} = (1-1/\epsilon_r)\mathbf{D}$ if asked. (Anisotropic crystals — tensor $\epsilon$, $\mathbf{P}$ not parallel to $\mathbf{E}$ — are not treated; plasmas, $\chi_e<0$, are deferred to ECE 350.) Where $\chi_e$ comes from — bound electrons on springs, $\chi_e = N_de^2/(m\epsilon_0\omega_0^2)$, flat up to optical frequencies — is the Lorentz model of [[concepts/conductivity-and-susceptibility-models|Lorentz–Drude models of σ and χe]].

**Where the ε goes.** Everywhere $\epsilon_0$ appeared in a vacuum formula whose field region is filled with the dielectric: Coulomb's law and the point-charge potential ($Q/4\pi\epsilon r$), Poisson's equation ($-\rho/\epsilon$), capacitance ($\epsilon A/d$, $2\pi\epsilon/\ln(b/a)$), energy density ($\tfrac12\epsilon E^2$). Gauss's law is best used in its $\mathbf{D}$ form, $\oint\mathbf{D}\cdot d\mathbf{S} = Q_{\text{free}}$, which needs no $\epsilon$ at all.

**What changes when a dielectric is inserted.** With the *free charge held fixed*, $\mathbf{D}$ is unchanged and $\mathbf{E}$ drops by $\epsilon_r$ (so does $V$; $C$ rises by $\epsilon_r$). With the *voltage held fixed*, $\mathbf{E}$ is unchanged and $\mathbf{D}$, $\rho_s$ and $Q$ rise by $\epsilon_r$ ($C$ rises by $\epsilon_r$ either way — [[concepts/capacitance|Capacitance]]). The habit for the rest of the unit: **$\mathbf{D}$ is fixed by the free charge; $\mathbf{E}$ is reduced by $\epsilon_r$; $\mathbf{P}$ makes up the difference.**

**Interfaces and inhomogeneous media.** Between $\epsilon_1$ and $\epsilon_2$ (no free charge): $E_t$ and $D_n$ continuous, so $E_{2n} = (\epsilon_1/\epsilon_2)E_{1n}$, $D_{2t} = (\epsilon_2/\epsilon_1)D_{1t}$ and lines refract with $\tan\theta_1/\tan\theta_2 = \epsilon_1/\epsilon_2$ ([[concepts/boundary-conditions|Boundary conditions at an interface]]). Laplace's and Poisson's equations hold only where $\epsilon_r$ is independent of position; layered and graded media are solved on [[concepts/static-fields-in-dielectrics|Static fields in dielectrics]].

**Examples.**

> [!example] Example — the slab between charged plates, three ways
> Sheets $+\rho_{s0}$ (below) and $-\rho_{s0}$ (above) give $\mathbf{E}_a = \hat{z}\,\rho_{s0}/\epsilon_0$ in the gap, now filled with a dielectric of susceptibility $\chi_e$.
> - *Self-consistently:* $P = \epsilon_0\chi_eE$ puts $\pm\rho_{sb} = \pm P$ on the faces, whose field $E_p = -P/\epsilon_0 = -\chi_eE$ opposes $\mathbf{E}_a$. So $E = E_a - \chi_eE$:
> $$
> E = \frac{E_a}{1+\chi_e} = \frac{\rho_{s0}}{\epsilon_0(1+\chi_e)} = \frac{\rho_{s0}}{\epsilon},\qquad \rho_{sb} = \frac{\chi_e}{1+\chi_e}\,\rho_{s0}.
> $$
> - *Via $\mathbf{D}$:* free charge unchanged, so $D = \rho_{s0}$ as without the dielectric (Gauss for free charge, or $D_n$ continuous at faces with no *free* charge), and $E = D/\epsilon$. One line.
> - *Limits:* $\chi_e = 0$ is vacuum ($\mathbf{P}=0$); $\chi_e\to\infty$ drives $E\to0$ — conductor-like.

> [!example] Example — copper plates: vacuum, then a fluid, then salt water (HW4 #5)
> Charged copper plates make $\mathbf{E} = 3\hat{z}$ V/m in the vacuum gap, zero elsewhere. (a) $\mathbf{D} = 3\epsilon_0\hat{z}$ C/m², $\mathbf{P} = 0$. (b) Bottom plate: $\rho_s = \hat{z}\cdot\mathbf{D} = 3\epsilon_0$ C/m². (c) Insulating fluid, $\epsilon = 81\epsilon_0$, plate charges unchanged: $\mathbf{D}$ unchanged, $\mathbf{E} = \mathbf{D}/\epsilon = \tfrac{1}{27}\hat{z}$ V/m, $\mathbf{P} = \mathbf{D} - \epsilon_0\mathbf{E} = \tfrac{80}{27}\epsilon_0\hat{z}$ C/m² — the fluid's bound charge cancels 80/81 of the plates' field. (d) Salt makes the fluid conduct ($\sigma\approx4$ S/m): ions drift to the plates until the interior field is *zero*; steady state $\mathbf{E} = \mathbf{D} = \mathbf{P} = 0$ in the fluid — the capacitor is shorted. Conductor versus dielectric in one experiment ([[concepts/conductors|Conductors in electrostatics]]).

> [!trap]
> - $\mathbf{D} = \epsilon\mathbf{E}$ uses the permittivity *of the region where you evaluate it*; the FA26 key's struck-out $-10\epsilon_0$ (instead of $2\epsilon_0\cdot(-10)$) is this slip.
> - $\epsilon_r$ and $\chi_e$ differ by 1; $\epsilon_r = 6$ means $\chi_e = 5$.
> - "$\epsilon\oint\mathbf{E}\cdot d\mathbf{S} = Q$" holds only when one uniform $\epsilon$ fills the whole surface; $\oint\mathbf{D}\cdot d\mathbf{S} = Q_{\text{free}}$ always does.
> - $\mathbf{P} = \mathbf{D} - \epsilon\mathbf{E}$ is identically zero; $\mathbf{P} = \chi_e\mathbf{E}$ lacks an $\epsilon_0$.

> [!exam] On exams
> FA26 3(c): $\mathbf{P}$ on both sides of a dielectric interface — $\mathbf{P} = \mathbf{D} - \epsilon_0\mathbf{E} = (\epsilon_r-1)\epsilon_0\mathbf{E}$. Worked in [[problems/fields-across-a-dielectric-interface|Worked problem — Fields across a dielectric interface]] and [[problems/two-layer-coaxial-capacitor|Worked problem — Two-layer coaxial capacitor]].

**Where it appears.** [[1-electrostatics/08-conductors-dielectrics-and-polarization#5-linear-dielectrics-χe-εr-and-ε|Lecture 8 §5]] (defined; the slab three ways; HW4 #5), [[1-electrostatics/09-static-fields-in-dielectric-media|Lecture 9]] (used throughout), [[1-electrostatics/10-capacitance-and-conductance|Lecture 10]] (every capacitance), [[problems/fields-across-a-dielectric-interface|Worked problem — Fields across a dielectric interface]], [[problems/two-layer-coaxial-capacitor|Worked problem — Two-layer coaxial capacitor]].

**Related.** [[concepts/polarization|Polarization P and bound charge]] · [[concepts/electric-flux-density|Electric flux density D]] · [[concepts/static-fields-in-dielectrics|Static fields in dielectrics]] · [[concepts/conductivity-and-susceptibility-models|Lorentz–Drude models of σ and χe]] · [[concepts/boundary-conditions|Boundary conditions at an interface]] · [[concepts/capacitance|Capacitance]].

**Practice.** [[practice/topics#fields-in-dielectric-media|Fields in dielectric media]] (16 problems) — for example [[practice/09-static-fields-in-dielectric-media#91-three-layers-between-charged-plates|9.1 Three layers between charged plates]] (easy), [[practice/09-static-fields-in-dielectric-media#96-graded-dielectric-at-fixed-voltage|9.6 Graded dielectric at fixed voltage]] (medium), [[practice/09-static-fields-in-dielectric-media#99-glass-slab-in-an-oblique-field|9.9 Glass slab in an oblique field]] (hard).
