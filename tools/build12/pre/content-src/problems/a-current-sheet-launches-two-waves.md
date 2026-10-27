---
title: "Worked problem — A current sheet launches two waves"
description: "A sheet of current Jₛ(t) ẑ on the plane x = 0, embedded in a dielectric with εr = 4, launches one plane wave toward +x and one toward −x. Find the direction and coefficient of H for each, the E that goes with them, a labelled snapshot at t = 6 ns, what a probe records, and the Poynting vector. Modelled on SP18 Exam 2 #5, re-parameterized with a new sheet plane, current direction, waveform and medium."
tags: [problem, waves]
---

*Problem · style of SP18 Exam 2 #5 (20 pts) · uses [[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets|Lecture 19]], [[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential|Lecture 13]] · concepts: [[concepts/current-sheet-radiation]], [[concepts/poynting-vector]], [[concepts/boundary-conditions]]*

> [!question] Problem
> An infinitesimally thin sheet in the plane $x = 0$ carries the surface current $\mathbf{J}_s = J_s(t)\,\hat z$ [A/m]. A lossless, non-magnetic dielectric with $\epsilon_r = 4$ fills all space on both sides. The current is zero for $t<0$, rises linearly to 6 A/m at $t = 2$ ns, drops abruptly to $-2$ A/m, stays there until $t = 4$ ns, and is zero afterwards. Use $c = 3\times10^8$ m/s.
> (a) The sheet launches a forward wave ($x>0$) and a reverse wave ($x<0$). Write the magnetic field of each in the form $\mathbf{H} = (\text{coefficient})\,J_s(t\mp x/v)\,(\text{unit vector})$, giving $v$ and the coefficient with its sign.
> (b) Find the electric field of each wave, with $\eta$.
> (c) Sketch the component of $\mathbf{H}$ found in (a) against $x$ at $t = 6$ ns, with labelled scales. Sketch $E_z$ at the same instant.
> (d) A probe at $x = -0.45$ m records $H_y(t)$. Sketch the record.
> (e) Find the Poynting vector at $x = 0.75$ m, $t = 6$ ns, and say where that energy came from.

## Before writing anything: the medium and the directions

The sheet result of Lecture 19 holds in any homogeneous lossless medium, with that medium's $v$ and $\eta$:

$$
v = \frac{c}{\sqrt{\epsilon_r}} = 1.5\times10^8\ \text{m/s} = 0.15\ \text{m/ns},\qquad \eta = \frac{\eta_0}{\sqrt{\epsilon_r}} = \frac{376.7}{2} = 188.4\ \Omega\ \ (\approx60\pi).
$$

**Which way do the waves go?** Away from the sheet: toward $+\hat x$ for $x>0$ and $-\hat x$ for $x<0$. So the normal toward the field point is $\hat n = +\hat x$ on the forward side and $\hat n = -\hat x$ on the reverse side, and the arguments are $t - x/v$ and $t + x/v$.

## (a) The magnetic field of each wave

Use the Lecture 13 rule $\mathbf{H} = \tfrac12\mathbf{J}_s\times\hat n$, delayed by the travel time:

- forward ($x>0$): $\tfrac12\,\hat z\times\hat x = +\tfrac12\hat y$;
- reverse ($x<0$): $\tfrac12\,\hat z\times(-\hat x) = -\tfrac12\hat y$.

> [!key] Answer (a)
> $$
> \mathbf{H} = +\frac12\,J_s\Big(t - \frac xv\Big)\,\hat y\quad(x>0),\qquad \mathbf{H} = -\frac12\,J_s\Big(t + \frac xv\Big)\,\hat y\quad(x<0),\qquad v = 0.15\ \text{m/ns}.
> $$
> Check with the jump condition, $\hat n\times(\mathbf{H}_1 - \mathbf{H}_2) = \mathbf{J}_s$ with region 1 = $x>0$ and $\hat n = \hat x$: at $x = 0$, $\hat x\times(\tfrac12J_s + \tfrac12J_s)\hat y = J_s\,\hat x\times\hat y = +J_s\hat z$ ✓.

> [!trap] Where part (a) loses points
> - One normal for both sides. $\hat n$ points toward the field point, so it flips, and so does $\mathbf{H}$.
> - $\hat x\times\hat z$ instead of $\hat z\times\hat x$: the rule is $\mathbf{J}_s\times\hat n$, current first.
> - Coefficient $\pm1$ instead of $\pm\tfrac12$: each side gets half the jump.
> - Using $c$: the waves travel at 0.15 m/ns in this dielectric, not 0.3 m/ns.

## (b) The electric field

At the sheet $\mathbf{E} = -\tfrac\eta2\mathbf{J}_s$, the same on both sides (tangential $\mathbf{E}$ is continuous), delayed by $\lvert x\rvert/v$:

> [!key] Answer (b)
> $$
> \mathbf{E} = -\frac\eta2\,J_s\Big(t\mp\frac xv\Big)\,\hat z\quad(x\gtrless0),\qquad \frac\eta2 = 94.2\ \Omega .
> $$
> Direction check: forward, $(-\hat z)\times(+\hat y) = -(\hat z\times\hat y) = +\hat x$ ✓; reverse, $(-\hat z)\times(-\hat y) = \hat z\times\hat y = -\hat x$ ✓. Both point away from the sheet. Ratio: $\lvert\mathbf{E}\rvert/\lvert\mathbf{H}\rvert = (\eta/2)/(1/2) = \eta$ ✓.

## (c) The snapshot at t = 6 ns

A feature emitted at source time $t'$ is, at $t = 6$ ns, a distance $0.15\,(6 - t')$ m from the sheet. The landmarks of the source are:

| source time $t'$ | source current | distance at 6 ns |
|---|---|---|
| 0 ns (start of the ramp: the front) | 0 | 0.9 m |
| 2 ns (top of the ramp, then the step) | 6 A/m, then −2 A/m | 0.6 m |
| 4 ns (end of the plateau) | −2 A/m, then 0 | 0.3 m |

On the forward side $H_y = +\tfrac12J_s$, so working inward from the front:

- $x>0.9$ m: nothing has arrived, $H_y = 0$.
- $0.6<x<0.9$ m: the ramp. $J_s$ grows from 0 (at 0.9 m) to 6 A/m (at 0.6 m), so $H_y = \tfrac12\cdot3\,(6 - x/0.15)$ A/m runs from 0 to $+3$ A/m. In space the ramp is mirrored: it grows toward the sheet.
- $x = 0.6$ m: the step, from $+3$ A/m to $-1$ A/m.
- $0.3<x<0.6$ m: the plateau, $H_y = \tfrac12(-2) = -1$ A/m.
- $0<x<0.3$ m: the source has been off since 4 ns, so $H_y = 0$.

On the reverse side $H_y = -\tfrac12J_s(t + x/v)$, the mirror image with the sign flipped: 0 beyond $-0.9$ m, a ramp from 0 to $-3$ A/m between $-0.9$ and $-0.6$ m, a step to $+1$ A/m, the plateau at $+1$ A/m to $-0.3$ m, then zero.

$E_z = -\tfrac\eta2J_s$ is the same on both sides: $-565$ V/m at the top of the ramp ($|x|\to0.6$ m from outside), $+188$ V/m on the plateau ($0.3<\lvert x\rvert<0.6$ m), zero within 0.3 m and beyond 0.9 m.

<!-- fig:sheet-problem-snapshot -->

> [!key] Answer (c)
> $H_y(x, 6\ \text{ns})$ is **odd** in $x$. On $x>0$: 0 for $x<0.3$ m, $-1$ A/m for $0.3<x<0.6$ m, a jump to $+3$ A/m at 0.6 m, a linear return to 0 at the front, 0.9 m. On $x<0$: the same with the opposite sign. $E_z(x, 6\ \text{ns})$ is **even**: $+188$ V/m on the plateau and a ramp from $-565$ V/m to 0 between 0.6 and 0.9 m from the sheet. Spot check at $x = 0.75$ m: $t - x/v = 6 - 5 = 1$ ns, $J_s = 3$ A/m, $H_y = +1.5$ A/m, $E_z = -283$ V/m.

> [!trap] Drawing the source shape unchanged
> The most common wrong sketch copies $J_s(t)$ onto the $+x$ axis with $t$ replaced by $x$, so the ramp rises away from the sheet. The front left first and has travelled farthest, so on the forward side the order is reversed in space. On the reverse side it is not, but the sign of $H_y$ is flipped. Fix two or three landmarks with the table above before you draw.

## (d) What a probe at x = −0.45 m records

On the reverse side $H_y = -\tfrac12J_s(t + x/v)$. At $x = -0.45$ m the delay is $0.45/0.15 = 3$ ns, so $H_y(-0.45\ \text{m}, t) = -\tfrac12J_s(t - 3\ \text{ns})$: the source waveform, halved, inverted and delayed, with its time order kept (a record is always the source in time order).

> [!key] Answer (d)
> Zero until $t = 3$ ns; a linear fall to $-3$ A/m at 5 ns; a step to $+1$ A/m, held until 7 ns; zero afterwards. For example $H_y = -0.75$ A/m at 3.5 ns and $+1$ A/m at 6 ns.

## (e) The Poynting vector

At $x = 0.75$ m and $t = 6$ ns, part (c) gives $E_z = -\tfrac\eta2(3) = -282.5$ V/m and $H_y = +1.5$ A/m:

$$
\mathbf{S} = \mathbf{E}\times\mathbf{H} = (-282.5\,\hat z)\times(1.5\,\hat y) = -423.8\,(\hat z\times\hat y) = +423.8\,\hat x\ \ \text{W/m}^2 = \frac{\eta}{4}J_s^2\,\hat x\quad\text{with } J_s = 3\ \text{A/m}.
$$

It points away from the sheet, as it must for an outgoing wave. The field at this point left the sheet at $t' = 1$ ns, when $J_s = 3$ A/m. At that moment the current was giving up $-\mathbf{J}_s\cdot\mathbf{E} = \tfrac\eta2J_s^2 = 94.2\times9 = 848$ W/m² to the field, and half of it, 424 W/m², went into each wave.

> [!key] Answer (e)
> $\mathbf{S}(0.75\ \text{m}, 6\ \text{ns})\approx+424\,\hat x$ W/m². It is half of the power per unit area the sheet current delivered at $t' = 1$ ns, $\tfrac\eta2J_s^2 = 848$ W/m²; the other half went into the reverse wave. (At $x = -0.75$ m the same instant gives $-424\,\hat x$ W/m².) The largest $\lvert\mathbf{S}\rvert$ in the snapshot is just outside $\lvert x\rvert = 0.6$ m, where $J_s$ was 6 A/m: $\eta\cdot36/4 = 1.70$ kW/m². Why $\mathbf{E}\times\mathbf{H}$ is a power density is Poynting's theorem, Lecture 20.

## Variant: the same sheet in vacuum

Remove the dielectric. Then $v = 0.3$ m/ns and $\eta = \eta_0\approx377\ \Omega$. $\mathbf{H}$ is unchanged in size and direction: it is set by the jump $J_s$, whatever the medium. $\mathbf{E}$ doubles ($\eta_0/2 = 188$ V/m per A/m of current), and every distance in the snapshot doubles: at $t = 6$ ns the front is at 1.8 m. So a current sheet fixes $\mathbf{H}$, and the medium decides $\mathbf{E}$ and the speed.

## The pattern behind this problem

$$
\mathbf{H} = \tfrac12\mathbf{J}_s\Big(t - \frac dv\Big)\times\hat n,\qquad \mathbf{E} = -\frac\eta2\mathbf{J}_s\Big(t - \frac dv\Big),\qquad \mathbf{S} = \mathbf{E}\times\mathbf{H}\parallel+\hat n .
$$

Write $\mathbf{J}_s$ as a vector, apply $\tfrac12\mathbf{J}_s\times\hat n$ separately on each side, give $\mathbf{E}$ the same value on both sides opposite to the current, and delay everything by distance over speed. For a snapshot, place the source landmarks at $v(t - t')$ from the sheet, mirrored on each side. The exam instance (SP18 Exam 2 #5) puts the sheet on $y = 0$ with the current along $-\hat x$ in free space, and asks for the same three things: the unit vector and the signed coefficient of $\mathbf{H}$ on each side, then a labelled sketch at one instant.
