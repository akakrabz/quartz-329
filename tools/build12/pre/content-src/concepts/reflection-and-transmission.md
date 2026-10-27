---
title: "Reflection and transmission coefficients"
description: "A plane wave hitting a planar interface head-on gives a reflected and a transmitted wave with Γ = (η₂ − η₁)/(η₂ + η₁) and τ = 1 + Γ times the incident electric field; a fraction |Γ|² of the power reflects."
tags: [concept, waves]
aliases: ["reflection coefficient", "transmission coefficient", "normal incidence", "impedance matching"]
---

> [!key] Definition (normal incidence, region 1 lossless)
> $$
> \begin{gathered}
> \Gamma = \frac{\tilde E_r(0)}{\tilde E_i(0)} = \frac{\eta_2-\eta_1}{\eta_2+\eta_1},\\[6pt]
> \tau = \frac{\tilde E_t(0)}{\tilde E_i(0)} = 1+\Gamma = \frac{2\eta_2}{\eta_2+\eta_1}.
> \end{gathered}
> $$
> Region 1 holds the incident wave; $\eta_2$ is complex if region 2 is lossy. Of the incident power, $\lvert\Gamma\rvert^2$ reflects and $1-\lvert\Gamma\rvert^2 = \lvert\tau\rvert^2\eta_1\text{Re}\{1/\eta_2\}$ is transmitted.

**Physics.** One wave alone cannot satisfy the boundary conditions at the interface ([[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Lecture 16]], [[1-electrostatics/06-circulation-and-boundary-conditions|Lecture 6]]). A reflected and a transmitted wave make tangential $\mathbf{E}$ and $\mathbf{H}$ continuous. $\mathbf{E}$ gives $1+\Gamma = \tau$, and $\mathbf{H}$ gives $1-\Gamma = \tau\eta_1/\eta_2$. Only the impedances matter: equal $\eta$'s reflect nothing, whatever $\mu$ and $\epsilon$ are separately. For real $\eta$'s, a larger $\eta_2$ reflects $\mathbf{E}$ in phase ($\Gamma>0$, $\tau>1$); a smaller one inverts it. The reflected $\mathbf{H}$ carries $-\Gamma$, because that wave travels backward and $\tilde{\mathbf{H}} = \hat u\times\tilde{\mathbf{E}}/\eta$.

**Limits.**
- Perfect conductor, $\eta_2\to0$: $\Gamma = -1$, $\tau = 0$. The total $\mathbf{E}$ vanishes at the surface, and a surface current $\mathbf{J}_s = \hat n\times\mathbf{H}_1$ of magnitude $2\lvert E_0\rvert/\eta_1$ flows along the incident $\mathbf{E}$.
- Matched, $\eta_2 = \eta_1$: $\Gamma = 0$, $\tau = 1$.
- Non-magnetic dielectrics: $\Gamma = (n_1-n_2)/(n_1+n_2)$.

**Examples.**
- Vacuum onto $\epsilon_r = 2.25$ (the notes' Example 1): $\Gamma = -1/5$, $\tau = 4/5$; 4 % of the power reflects.
- Out of the same glass into vacuum: $\Gamma = +1/5$, $\tau = 6/5$; again 4 %.
- Air onto seawater at 1 kHz: $\Gamma\approx-0.9998$, and 0.033 % of the power enters.
- [[problems/working-back-from-a-transmitted-wave]]: vacuum onto $\mu_r = 4$, $\epsilon_r = 2.25$ gives $\Gamma = 1/7$, $\tau = 8/7$.

> [!trap]
> - $\tau>1$ is not a power gain; power also depends on the $\eta$'s.
> - $\Gamma$ and $\tau$ are for $\mathbf{E}$. For $\mathbf{H}$ the ratios are $-\Gamma$ and $1-\Gamma$.
> - Swap the regions and $\Gamma$ changes sign.
> - A lossy region 2 needs the complex $\eta_2$.

**Where it appears.** [[3-maxwell-and-waves/25-wave-reflection-and-transmission|Lecture 25]] (derivation, special cases, power balance); [[3-maxwell-and-waves/26-standing-waves-and-radiation-pressure|Lecture 26]] (the standing wave of $\Gamma = -1$, reflection from a good conductor, radiation pressure); [[4-transmission-lines/index|Unit 4]] (the same $\Gamma$ at line junctions and loads, with characteristic impedances in place of $\eta$).

**Practice.** [[practice/topics#reflection-and-transmission-at-an-interface|Reflection and transmission at an interface]] (20 problems) — for example [[practice/25-reflection-and-transmission#251-four-interfaces|25.1 Four interfaces]] (easy), [[practice/25-reflection-and-transmission#256-same-speed-different-impedance|25.6 Same speed, different impedance]] (medium), [[practice/25-reflection-and-transmission#259-out-of-the-glass|25.9 Out of the glass]] (hard).

Related: [[concepts/boundary-conditions]] · [[concepts/intrinsic-impedance]] · [[concepts/poynting-vector]] · [[concepts/plane-waves]].
