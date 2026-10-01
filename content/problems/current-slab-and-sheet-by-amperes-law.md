---
title: "Worked problem — A current slab and a current sheet, by Ampère's law"
description: "H everywhere for a uniform current slab next to an antiparallel current sheet: symmetry, Ampère rectangles, superposition, the boundary condition at the sheet, the plane where H vanishes, and the force per unit area on the sheet. The magnetic twin of the charged-slab problem."
tags: [problem, magnetostatics]
---

*Problem · style of an Ampère's-law exam problem (the magnetic twin of FA26 Exam 1 #2) · uses [[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential|Lecture 13]] and [[2-magnetostatics/12-magnetic-force-biot-savart-and-amperes-law|Lecture 12]] · concepts: [[concepts/amperes-law]], [[concepts/magnetic-field]], [[concepts/boundary-conditions]], [[concepts/superposition]]*

> [!question] Problem
> A slab occupying $-2\ \text{mm}<x<2\ \text{mm}$ (infinite in $y$ and $z$) carries the uniform current density $\mathbf{J} = J_0\hat z$ with $J_0 = 2000$ A/m². A thin sheet at $x = 6$ mm carries the surface current $\mathbf{J}_s = -4\,\hat z$ A/m. Free space everywhere.
> (a) Find $\mathbf{H}$ due to the slab alone, for all $x$. (b) Find $\mathbf{H}$ due to the sheet alone. (c) Superpose, and sketch $H_y(x)$. (d) Verify the boundary condition at $x = 6$ mm and find where (if anywhere) $\mathbf{H} = 0$. (e) Find the force per unit area on the sheet, and say whether it is attracted to or repelled from the slab.

## (a) The slab

**Symmetry.** The current is along $z$ and depends only on $x$, so each filament's field circles it in the $xy$-plane; pairing filaments at $\pm$ equal distances from any field point kills the $x$-components. Hence $\mathbf{H} = H_y(x)\hat y$, and by the odd symmetry of the slab about $x = 0$, $H_y(-x) = -H_y(x)$, $H_y(0) = 0$.

**Loop.** A rectangle in the $xy$-plane of height $L$ (along $y$), from $-x$ to $+x$. The two sides parallel to $\hat y$ each contribute $H_y(x)L$ (the field reverses with $x$, and so does the direction of travel); the sides along $\hat x$ contribute nothing ($\mathbf{H}\perp d\mathbf{l}$).

**Inside** ($|x|<2$ mm): $I_{\text{enc}} = J_0\cdot2x\cdot L$, so $2H_yL = 2J_0xL$ and $H_y = J_0x$. **Outside** ($|x|\ge2$ mm): $I_{\text{enc}} = J_0WL$ with $W = 4$ mm, so $H_y = J_0W/2 = 2000\times0.002 = 4$ A/m.

> [!key] Answer (a)
> $$
> \mathbf{H}_{\text{slab}} = \begin{cases}\hat y\,(2000\,x)\ \text{A/m} & |x|<2\ \text{mm}\ (x\ \text{in m}),\\ \hat y\,4\,\text{sgn}(x)\ \text{A/m} & |x|\ge2\ \text{mm}.\end{cases}
> $$
> A ramp of slope $J_0$ that saturates at $\pm J_0W/2$; continuous at the faces. Direction check at $x>0$: current $+\hat z$, field point at $+\hat x$, $\hat z\times\hat x = +\hat y$ ✓ (right-hand rule).

## (b) The sheet

$\mathbf{H} = \tfrac12\mathbf{J}_s\times\hat n$ with $\hat n$ pointing from the sheet toward the field point. For $x>6$ mm, $\hat n = \hat x$: $\tfrac12(-4\hat z)\times\hat x = -2\hat y$. For $x<6$ mm, $\hat n = -\hat x$: $\tfrac12(-4\hat z)\times(-\hat x) = +2\hat y$.

> [!key] Answer (b)
> $\mathbf{H}_{\text{sheet}} = +2\hat y$ A/m for $x<6$ mm and $-2\hat y$ A/m for $x>6$ mm. Magnitude $|J_s|/2$, independent of distance, reversed across the sheet.

> [!trap] Sign of the sheet field
> With a *negative* $J_s$ it is easy to flip the answer. Do the cross product on one side explicitly — $\hat z\times\hat x = \hat y$, then multiply by $-4/2$ — rather than remembering "$+$ on the right".

## (c) Superposition

Add region by region ($x$ in mm; $H$ in A/m):

| region | slab | sheet | total $H_y$ |
|---|---|---|---|
| $x<-2$ | $-4$ | $+2$ | $-2$ |
| $-2<x<2$ | $2000x$ ($x$ in m) | $+2$ | $2000x + 2$ |
| $2<x<6$ | $+4$ | $+2$ | $+6$ |
| $x>6$ | $+4$ | $-2$ | $+2$ |

The ramp runs from $-2$ at $x = -2$ mm to $+6$ at $x = +2$ mm (slope still $J_0$ — the sheet adds a constant), stays at 6 up to the sheet, and drops to 2 beyond it.

## (d) The boundary condition, and the zero of H

At $x = 6$ mm, with $\hat n = \hat x$ pointing into region 1 ($x>6$): $\hat n\times(\mathbf{H}_1-\mathbf{H}_2) = \hat x\times(2\hat y - 6\hat y) = -4\hat z = \mathbf{J}_s$ ✓. The tangential field jumps by exactly the surface current; the normal component is zero on both sides, so $B_n$ is trivially continuous. At the slab faces nothing jumps — there is no surface current there — and the table confirms it ($-2\to-2$ at $x = -2$ mm, $6\to6$ at $x = 2$ mm).

$\mathbf{H} = 0$ where $2000x + 2 = 0$: $x = -1$ mm, inside the slab. (At $x = 0$, where the slab's own field vanishes, the total is the sheet's $+2$ A/m.)

> [!key] Answer (d)
> Boundary condition satisfied, with $H_t$ jumping by $J_s = -4$ A/m across the sheet. $\mathbf{H} = 0$ on the plane $x = -1$ mm only.

## (e) Force on the sheet

The force on a current element is $I\,d\mathbf{l}\times\mathbf{B}$; per unit area of a sheet that is $\mathbf{f} = \mathbf{J}_s\times\mathbf{B}_{\text{other}}$, where $\mathbf{B}_{\text{other}}$ is the field of *everything except the sheet itself* (a sheet exerts no net force on itself; its own field is $\pm$ on its two sides and averages to zero). At $x = 6$ mm the slab's field is $\mathbf{B} = \mu_0\,(4\ \text{A/m})\,\hat y\approx5.0\ \mu\text{T}\,\hat y$, so

$$
\mathbf{f} = (-4\hat z)\times(4\mu_0\hat y) = -16\mu_0\,(\hat z\times\hat y) = +16\mu_0\,\hat x = 2.0\times10^{-5}\ \text{N/m}^2 .
$$

> [!key] Answer (e)
> $\mathbf{f} = +16\mu_0\hat x\approx2.0\times10^{-5}$ N/m², pointing *away* from the slab: the sheet is **repelled**, as antiparallel currents must be ([[2-magnetostatics/12-magnetic-force-biot-savart-and-amperes-law|Lecture 12 §1]]).

> [!trap] The pattern behind this problem
> It is the charged-slab problem of Exam 1 with the dictionary applied: $\rho_0\to J_0$, $D_x\to H_y$, pillbox → rectangle, "charge enclosed" → "current enclosed", $D_n$ jumps by $\rho_s$ → $H_t$ jumps by $J_s$. The three places points are lost are the same too: the direction (right-hand rule, done explicitly), the region bookkeeping (a table), and forgetting that a sheet's own field does not act on it.
