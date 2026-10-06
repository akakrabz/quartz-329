---
title: "Worked problem — Fields across a magnetic interface"
description: "Given H just above a plane between two magnetic media, find H just below, then B and M on both sides, the refraction angles, and the magnetization current on the interface — with a check that free plus bound surface current accounts for the jump in tangential B. The magnetic twin of the dielectric-interface problem (FA26 Exam 1 #3), with its own numbers."
tags: [problem, waves]
---

*Problem · magnetic twin of [[problems/fields-across-a-dielectric-interface]] (style of FA26 Exam 1 #3) · uses [[3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations|Lecture 16]] (boundary conditions), [[3-maxwell-and-waves/17-magnetization-and-maxwells-equations-in-matter|Lecture 17]] (magnetization, $\mathbf{B} = \mu\mathbf{H}$) · concepts: [[concepts/boundary-conditions]], [[concepts/permeability]], [[concepts/magnetization]]*

> [!question] Problem
> Two linear magnetic media meet at the plane $z = 0$: $\mu_1 = 2\mu_0$ for $z>0$ and $\mu_2 = 6\mu_0$ for $z<0$. There is no free current on the interface. Immediately above it the magnetic field intensity is measured to be
> $$
> \mathbf{H}_1 = 4\hat x - 3\hat y - 9\hat z\quad[\text{A/m}].
> $$
> (a) Find $\mathbf{H}_2$, the field immediately below the interface. (b) Find $\mathbf{B}_1$ and $\mathbf{B}_2$. (c) Find $\mathbf{M}_1$ and $\mathbf{M}_2$. (d) Find the angle each field makes with the normal, and check the refraction law. (e) Find the magnetization (bound) surface current on the interface, and check that it accounts for the jump in tangential $\mathbf{B}$.

## Before writing anything: which component is which

The interface is the plane $z = 0$, so the **normal** direction is $\hat z$ and the **tangential** directions are $\hat x$ and $\hat y$. Medium 1 is the upper half-space, so $\hat n = +\hat z$ points from medium 2 into medium 1, as the boundary conditions require. Split the given field:

$$
\mathbf{H}_{1t} = 4\hat x - 3\hat y\quad(\text{magnitude }5),\qquad H_{1n} = -9 .
$$

Two rules govern everything ([[concepts/boundary-conditions]]). **Tangential $\mathbf{H}$ is continuous**, because the interface carries no free current — the twin of tangential $\mathbf{E}$. **Normal $\mathbf{B}$ is continuous**, always, because there is no magnetic charge — the twin of normal $\mathbf{D}$, but with no exception, since there is no magnetic surface charge to make it jump.

## (a) The field below

**Tangential:** $\mathbf{H}_{2t} = \mathbf{H}_{1t} = 4\hat x - 3\hat y$. Copied, no arithmetic.

**Normal:** $B_{1n} = B_{2n}$ with $B_n = \mu H_n$ in each medium:

$$
\mu_1H_{1n} = \mu_2H_{2n}\quad\Longrightarrow\quad H_{2n} = \frac{\mu_1}{\mu_2}H_{1n} = \frac{2\mu_0}{6\mu_0}(-9) = -3 .
$$

> [!key] Answer (a)
> $\mathbf{H}_2 = 4\hat x - 3\hat y - 3\hat z$ [A/m]. Entering the more permeable medium, the normal component of $\mathbf{H}$ shrinks by $\mu_1/\mu_2 = 1/3$; the tangential part is untouched.

> [!trap] The four wrong answers, and the rule each one breaks
> - $\mathbf{H}_2 = \mathbf{H}_1$: normal $\mathbf{H}$ treated as continuous. It is normal $\mathbf{B}$ that is continuous.
> - $\mathbf{H}_2 = \tfrac13\mathbf{H}_1 = \tfrac43\hat x - \hat y - 3\hat z$: the whole vector scaled, i.e. tangential $\mathbf{B}$ treated as continuous.
> - $H_{2n} = 3(-9) = -27$: the ratio inverted. Sanity check: both media share the same $B_n$, so the more permeable one needs the *smaller* $H_n$ to carry it, $\lvert H_{2n}\rvert<\lvert H_{1n}\rvert$.
> - $B_{1n} = \mu_0(-9)$ instead of $2\mu_0(-9)$: $\mathbf{B} = \mu\mathbf{H}$ must use the permeability of the medium you are in — the slip that appears, struck out, in the FA26 key (there with $\epsilon$).

## (b) The flux densities

$\mathbf{B} = \mu\mathbf{H}$ in each medium, each with its own $\mu$:

$$
\mathbf{B}_1 = 2\mu_0(4\hat x - 3\hat y - 9\hat z) = \mu_0\,(8\hat x - 6\hat y - 18\hat z),\qquad
\mathbf{B}_2 = 6\mu_0(4\hat x - 3\hat y - 3\hat z) = \mu_0\,(24\hat x - 18\hat y - 18\hat z).
$$

> [!key] Answer (b)
> $\mathbf{B}_1 = \mu_0(8\hat x - 6\hat y - 18\hat z)$ and $\mathbf{B}_2 = \mu_0(24\hat x - 18\hat y - 18\hat z)$ [T]. With $\mu_0 = 4\pi\times10^{-7}$ H/m, $B_{1z} = B_{2z} = -18\mu_0\approx-2.26\times10^{-5}$ T ($-22.6$ μT); $\lvert\mathbf{B}_1\rvert\approx2.59\times10^{-5}$ T and $\lvert\mathbf{B}_2\rvert\approx4.40\times10^{-5}$ T.

**Built-in check.** The $z$-components agree ($-18\mu_0$ on both sides), as they must, since that was the condition used in (a). The tangential components of $\mathbf{B}$ *do* jump, from $(8,-6)\mu_0$ to $(24,-18)\mu_0$, by the factor $\mu_2/\mu_1 = 3$. If your two $B_z$ values differ, part (a) is wrong; fix it before going on.

## (c) The magnetization

$\mathbf{M} = \mathbf{B}/\mu_0 - \mathbf{H}$, medium by medium, pairing each $\mathbf{B}$ with the $\mathbf{H}$ of the *same* medium:

$$
\mathbf{M}_1 = (8\hat x - 6\hat y - 18\hat z) - (4\hat x - 3\hat y - 9\hat z) = 4\hat x - 3\hat y - 9\hat z,
$$
$$
\mathbf{M}_2 = (24\hat x - 18\hat y - 18\hat z) - (4\hat x - 3\hat y - 3\hat z) = 20\hat x - 15\hat y - 15\hat z .
$$

> [!key] Answer (c)
> $\mathbf{M}_1 = 4\hat x - 3\hat y - 9\hat z$ A/m, $\mathbf{M}_2 = 20\hat x - 15\hat y - 15\hat z$ A/m.

**Shortcut and check.** $\mathbf{M} = \chi_m\mathbf{H} = (\mu_r-1)\mathbf{H}$. With $\chi_{m1} = 1$, $\mathbf{M}_1 = \mathbf{H}_1$ ✓; with $\chi_{m2} = 5$, $\mathbf{M}_2 = 5\mathbf{H}_2 = (20,-15,-15)$ ✓. Each $\mathbf{M}$ is parallel to its own $\mathbf{H}$, as it must be in an isotropic medium. There is no $\mu_0$ anywhere in this part: $\mathbf{M}$ and $\mathbf{H}$ are both in A/m.

> [!trap] Lines that are always wrong
> - $\mathbf{M} = \mu_0\chi_m\mathbf{H}$: the result is in tesla ($\mu_0\cdot4$ A/m $= 5.0\times10^{-6}$ T is not a magnetization). The dielectric formula $\mathbf{P} = \epsilon_0\chi_e\mathbf{E}$ needs its $\epsilon_0$; this one has no $\mu_0$.
> - $\mathbf{M} = \mathbf{B}/\mu-\mathbf{H}$ is identically zero (the twin of $\mathbf{P} = \mathbf{D}-\epsilon\mathbf{E}$).
> - $\mathbf{M} = \mathbf{B}/\mu_0$ forgets to subtract $\mathbf{H}$; here it would double $\mathbf{M}_1$.
> - $\mathbf{B}_2/\mu_0 - \mathbf{H}_1$ pairs fields from different media and means nothing.

## (d) The angles, and the bending of the field

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 300" width="640" height="300" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px"><defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker><marker id="ahs" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs><rect x="15.0" y="40.0" width="320.0" height="120.0" rx="0" fill="var(--accent)" fill-opacity="0.06" stroke="none"/><rect x="15.0" y="160.0" width="320.0" height="130.0" rx="0" fill="var(--accent2)" fill-opacity="0.16" stroke="none"/><line x1="15.0" y1="160.0" x2="335.0" y2="160.0" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><text x="175.0" y="24.0" text-anchor="middle" fill="currentColor" style="font-size:12.5px;font-weight:600;">refraction at a magnetic interface</text><text x="328.0" y="56.0" text-anchor="end" fill="currentColor" style="font-size:12px;">medium 1:  μ₁ = 2μ₀</text><text x="22.0" y="282.0" text-anchor="start" fill="currentColor" style="font-size:12px;">medium 2:  μ₂ = 6μ₀</text><line x1="150.0" y1="160.0" x2="150.0" y2="46.0" stroke="currentColor" stroke-width="1.5" marker-end="url(#ah)" stroke-linecap="round"/><text x="157.0" y="56.0" text-anchor="start" fill="currentColor" style="font-size:14px;font-weight:600;">n̂</text><line x1="150.0" y1="160.0" x2="150.0" y2="224.0" stroke="currentColor" stroke-width="1.1" stroke-dasharray="4 3" opacity="0.6" stroke-linecap="round"/><line x1="95.0" y1="61.0" x2="150.0" y2="160.0" stroke="var(--accent)" stroke-width="3" marker-end="url(#ah)" stroke-linecap="round"/><line x1="150.0" y1="160.0" x2="205.0" y2="193.0" stroke="var(--accent)" stroke-width="3" marker-end="url(#ah)" stroke-linecap="round"/><text x="89.0" y="73.0" text-anchor="end" fill="var(--accent)" style="font-size:13px;font-weight:600;">H<tspan baseline-shift="sub" style="font-size:9px">1</tspan></text><text x="211.0" y="197.0" text-anchor="start" fill="var(--accent)" style="font-size:13px;font-weight:600;">H<tspan baseline-shift="sub" style="font-size:9px">2</tspan></text><path d="M150.0,118.0 L147.6,118.1 L145.3,118.3 L142.9,118.6 L140.6,119.1 L138.3,119.7 L136.1,120.4 L133.9,121.2 L131.7,122.2 L129.6,123.3" fill="none" stroke="currentColor" stroke-width="1.1" stroke-linejoin="round" stroke-linecap="round"/><text x="135.0" y="108.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">θ₁</text><path d="M150.0,190.0 L151.6,190.0 L153.2,189.8 L154.9,189.6 L156.5,189.3 L158.0,188.9 L159.6,188.4 L161.1,187.9 L162.6,187.2 L164.1,186.5 L165.5,185.7 L166.9,184.8 L168.2,183.9 L169.4,182.8 L170.7,181.8 L171.8,180.6 L172.9,179.4 L173.9,178.1 L174.9,176.8 L175.7,175.4" fill="none" stroke="currentColor" stroke-width="1.1" stroke-linejoin="round" stroke-linecap="round"/><text x="170.0" y="208.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">θ₂</text><text x="196.0" y="84.0" text-anchor="start" fill="currentColor" style="font-size:11.5px;">Hₜ = 5 on both sides</text><text x="196.0" y="99.0" text-anchor="start" fill="var(--muted)" style="font-size:10.5px;">(no free surface current)</text><text x="196.0" y="124.0" text-anchor="start" fill="currentColor" style="font-size:11.5px;">μ₁H₁ₙ = μ₂H₂ₙ:</text><text x="196.0" y="140.0" text-anchor="start" fill="currentColor" style="font-size:11.5px;">2(−9) = 6(−3)</text><text x="328.0" y="236.0" text-anchor="end" fill="currentColor" style="font-size:11.5px;">θ₁ = 29.1°,  θ₂ = 59.0°</text><text x="328.0" y="256.0" text-anchor="end" fill="currentColor" style="font-size:11.5px;font-weight:600;">tan θ₁ / tan θ₂ = μ₁/μ₂ = 1/3</text><rect x="350.0" y="40.0" width="280.0" height="120.0" rx="0" fill="var(--accent)" fill-opacity="0.06" stroke="none"/><rect x="350.0" y="160.0" width="280.0" height="130.0" rx="0" fill="var(--accent2)" fill-opacity="0.34" stroke="none"/><line x1="350.0" y1="160.0" x2="630.0" y2="160.0" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><text x="490.0" y="24.0" text-anchor="middle" fill="currentColor" style="font-size:12.5px;font-weight:600;">air over iron (μᵣ = 5000)</text><text x="357.0" y="56.0" text-anchor="start" fill="currentColor" style="font-size:12px;">air</text><text x="357.0" y="282.0" text-anchor="start" fill="currentColor" style="font-size:12px;">iron</text><line x1="470.0" y1="160.0" x2="470.0" y2="186.0" stroke="currentColor" stroke-width="1.1" stroke-dasharray="4 3" opacity="0.6" stroke-linecap="round"/><line x1="362.4" y1="169.4" x2="468.0" y2="161.0" stroke="var(--accent)" stroke-width="3" marker-end="url(#ah)" stroke-linecap="round"/><line x1="470.0" y1="160.0" x2="470.0" y2="56.0" stroke="var(--accent)" stroke-width="3" marker-end="url(#ah)" stroke-linecap="round"/><text x="479.0" y="102.0" text-anchor="start" fill="var(--accent)" style="font-size:11.5px;font-weight:600;">B in air: θ = 0.13°</text><text x="479.0" y="118.0" text-anchor="start" fill="var(--muted)" style="font-size:10.5px;">(leaves almost normally)</text><text x="366.4" y="201.4" text-anchor="start" fill="var(--accent)" style="font-size:11.5px;font-weight:600;">B in iron: θ = 85°</text><text x="490.0" y="236.0" text-anchor="middle" fill="currentColor" style="font-size:12px;font-weight:600;">tan θ<tspan baseline-shift="sub" style="font-size:9px">air</tspan> = tan θ<tspan baseline-shift="sub" style="font-size:9px">iron</tspan> / 5000</text><text x="490.0" y="256.0" text-anchor="middle" fill="var(--muted)" style="font-size:10.5px;">(lengths not to scale)</text></svg><figcaption><strong>How field lines bend where μ changes.</strong> Left: the interface of the worked problem. Tangential <b>H</b> is continuous (no free surface current) and normal <b>B</b> is continuous, so the normal part of <b>H</b> scales by μ₁/μ₂: from −9 above to −3 below, while the tangential part stays 5. Entering the more permeable medium the line tilts away from the normal, and tan θ₁/tan θ₂ = μ₁/μ₂ — the refraction law of Lecture 9 with ε replaced by μ. <b>B</b> is parallel to <b>H</b> in each medium, so B lines bend by the same angles. Right: with iron (μ<sub>r</sub> ≈ 5000) the ratio is so extreme that a line running at 85° to the normal inside the iron leaves into the air at 0.13° — essentially perpendicular. Iron surfaces act for <b>B</b> the way conductor surfaces act for <b>E</b>, which is why the pole faces of a magnet set the direction of the field in its gap.</figcaption></figure>

Measured from the normal: $\tan\theta_1 = \lvert\mathbf{H}_{1t}\rvert/\lvert H_{1n}\rvert = 5/9$ and $\tan\theta_2 = 5/3$, so $\theta_1\approx29.1^\circ$ and $\theta_2\approx59.0^\circ$, and

$$
\frac{\tan\theta_1}{\tan\theta_2} = \frac{5/9}{5/3} = \frac13 = \frac{\mu_1}{\mu_2}\ \checkmark
$$

— the refraction law of [[1-electrostatics/09-static-fields-in-dielectric-media#2-refraction-of-field-lines-at-an-interface|Lecture 9 §2]] with $\epsilon$ replaced by $\mu$. $\mathbf{B}$ is parallel to $\mathbf{H}$ in each medium, so the $B$-lines bend by the same angles: $\lvert\mathbf{B}_{t}\rvert/\lvert B_n\rvert = 10/18 = 5/9$ above and $30/18 = 5/3$ below. The line bends *away* from the normal on entering the more permeable side — toward the surface, as $\mathbf{E}$ did entering the higher-$\epsilon$ side. Push $\mu_2$ to iron's thousands and the line inside runs almost along the surface, while in the weaker medium it stands almost on end: field lines leave iron at right angles ([[3-maxwell-and-waves/17-magnetization-and-maxwells-equations-in-matter#6-boundary-conditions-in-magnetic-media|Lecture 17 §6]]).

## (e) The magnetization current on the interface, and the check

There is no *free* current on $z = 0$, but the tangential component of $\mathbf{M}$ jumps there, from $(4,-3)$ to $(20,-15)$ A/m, so the interface carries a **bound** surface current. Use $\mathbf{J}_{sM} = \mathbf{M}\times\hat n$ on each face, each with the outward normal of *its own* medium (the surface term is this site's addition; see [[3-maxwell-and-waves/17-magnetization-and-maxwells-equations-in-matter#3-the-magnetization-current|Lecture 17 §3]]):

$$
\begin{gathered}
\text{top face of medium 2 }(\text{outward normal }+\hat z):\quad \mathbf{M}_2\times\hat z = (20,-15,-15)\times(0,0,1) = -15\hat x - 20\hat y,\\[4pt]
\text{bottom face of medium 1 }(\text{outward normal }-\hat z):\quad \mathbf{M}_1\times(-\hat z) = -(4,-3,-9)\times(0,0,1) = 3\hat x + 4\hat y .
\end{gathered}
$$

Together, $\mathbf{J}_{sM} = -12\hat x - 16\hat y$ A/m, magnitude 20 A/m — the same as the one-line formula $\hat n\times(\mathbf{M}_1-\mathbf{M}_2) = \hat z\times(-16\hat x + 12\hat y + 6\hat z) = -12\hat x - 16\hat y$.

**The check.** Tangential $\mathbf{B}$ jumps across the interface, and in the *vacuum* form of the boundary condition the jump must be carried by all the current there, free and bound:

$$
\frac{\hat n\times(\mathbf{B}_1-\mathbf{B}_2)}{\mu_0} = \hat z\times(-16\hat x + 12\hat y) = -12\hat x - 16\hat y = \mathbf{J}_s + \mathbf{J}_{sM}\quad(\mathbf{J}_s = 0)\ \checkmark
$$

Two more consistency checks. $\mathbf{J}_{sM}$ is perpendicular to $\mathbf{H}_t$: $(-12)(4) + (-16)(-3) = 0$, because it equals $(\chi_{m1}-\chi_{m2})\,\hat z\times\mathbf{H}_{1t}$. And the jump in the *normal* component of $\mathbf{M}$ (from $-9$ to $-15$) makes no current at all; it shows up instead as the jump of normal $\mathbf{H}$: $H_{1z}-H_{2z} = -6 = -(M_{1z}-M_{2z})$.

> [!key] Answer (e)
> $\mathbf{J}_{sM} = \hat n\times(\mathbf{M}_1-\mathbf{M}_2) = -12\hat x - 16\hat y$ A/m ($\lvert\mathbf{J}_{sM}\rvert = 20$ A/m): $+3\hat x + 4\hat y$ from the face of medium 1 and $-15\hat x - 20\hat y$ from the face of medium 2. Check: $\hat n\times(\mathbf{B}_1-\mathbf{B}_2)/\mu_0 = -12\hat x - 16\hat y$ A/m $= \mathbf{J}_s + \mathbf{J}_{sM}$ ✓.

> [!trap] Sign slips in (e)
> - Using $\hat n = +\hat z$ for both faces gives $(-15,-20) + (-3,-4) = (-18,-24)$ — wrong. Each face takes the outward normal of its own body; that is where the difference $\mathbf{M}_1-\mathbf{M}_2$ comes from.
> - Writing $-\hat n\times(\mathbf{M}_1-\mathbf{M}_2)$ by analogy with $\rho_{sb} = -\hat n\cdot(\mathbf{P}_1-\mathbf{P}_2)$: the magnetic interface current has no minus sign.
> - Concluding that no current flows because "the interface carries no surface current": the problem statement means no *free* current. The bound current is there whenever tangential $\mathbf{M}$ jumps.

## Variant: with a free current on the interface

Suppose the interface also carried a free surface current $\mathbf{J}_s = 2\hat y$ A/m. The normal rule is unchanged ($B_n$ is always continuous), so $H_{2z} = -3$ again. The tangential rule becomes $\hat n\times(\mathbf{H}_1-\mathbf{H}_2) = \mathbf{J}_s$, i.e. $\mathbf{H}_{2t} = \mathbf{H}_{1t} - \mathbf{J}_s\times\hat n$, with $\mathbf{J}_s\times\hat n = 2\hat y\times\hat z = 2\hat x$:

$$
\mathbf{H}_2 = (4-2)\hat x - 3\hat y - 3\hat z = 2\hat x - 3\hat y - 3\hat z\ \text{A/m}.
$$

Check: $\hat z\times(\mathbf{H}_1-\mathbf{H}_2) = \hat z\times(2\hat x - 6\hat z) = 2\hat y$ ✓. In words: the sheet alone makes $\tfrac12\mathbf{J}_s\times\hat n = +1\hat x$ above it and $-1\hat x$ below ([[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential#1-the-current-sheet|Lecture 13]]), so crossing it downward $H_x$ drops by $J_s = 2$. Then $\mathbf{B}_2 = \mu_0(12\hat x - 18\hat y - 18\hat z)$, $\mathbf{M}_2 = 10\hat x - 15\hat y - 15\hat z$ A/m, $\mathbf{J}_{sM} = \hat z\times(\mathbf{M}_1-\mathbf{M}_2) = -12\hat x - 6\hat y$ A/m, and the check now needs both currents:

$$
\frac{\hat n\times(\mathbf{B}_1-\mathbf{B}_2)}{\mu_0} = \hat z\times(-4\hat x + 12\hat y) = -12\hat x - 4\hat y = \underbrace{2\hat y}_{\mathbf{J}_s} + \underbrace{(-12\hat x - 6\hat y)}_{\mathbf{J}_{sM}}\ \checkmark
$$

The angle below changes too: $\tan\theta_2 = \sqrt{13}/3$, $\theta_2\approx50.2^\circ$.

## The pattern behind this problem

For $\mu_1 = \mu_{r1}\mu_0$ above and $\mu_2 = \mu_{r2}\mu_0$ below, with free surface current $\mathbf{J}_s$ on the plane and $\hat n = \hat z$:

$$
\begin{gathered}
\mathbf{H}_{2t} = \mathbf{H}_{1t} - \mathbf{J}_s\times\hat n,\qquad H_{2n} = \frac{\mu_{r1}}{\mu_{r2}}H_{1n},\qquad \mathbf{B}_i = \mu_{ri}\mu_0\mathbf{H}_i,\qquad \mathbf{M}_i = (\mu_{ri}-1)\mathbf{H}_i,\\[4pt]
\mathbf{J}_{sM} = \hat n\times(\mathbf{M}_1-\mathbf{M}_2),\qquad \frac{\hat n\times(\mathbf{B}_1-\mathbf{B}_2)}{\mu_0} = \mathbf{J}_s + \mathbf{J}_{sM}.
\end{gathered}
$$

Hold it next to [[problems/fields-across-a-dielectric-interface#the-general-pattern|the dielectric pattern]]: the same structure with $\mathbf{E}\to\mathbf{H}$, $\mathbf{D}\to\mathbf{B}$, $\mathbf{P}\to\mathbf{M}$, $\epsilon\to\mu$ — split into tangential and normal parts, copy one, scale the other, then $\mathbf{B} = \mu\mathbf{H}$ and $\mathbf{M} = \mathbf{B}/\mu_0-\mathbf{H}$ medium by medium. Two things change. The free source now sits in the *tangential* condition ($\mathbf{J}_s$ shifts $\mathbf{H}_t$), where $\rho_s$ shifted the normal $D_n$. And the bound source on the interface is a current $\hat n\times(\mathbf{M}_1-\mathbf{M}_2)$ with no minus sign, where the dielectric had the charge $-\hat n\cdot(\mathbf{P}_1-\mathbf{P}_2)$. If $\mathbf{B}_1$ is given instead of $\mathbf{H}_1$, divide by $\mu_1$ first; if the interface is $x = 0$, the normal component is $H_x$ — the geometry decides which component scales, not the letter.
