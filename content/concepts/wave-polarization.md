---
title: "Wave polarization"
description: "The path a plane wave's E vector traces at a fixed point: a line, circle or ellipse, set by two perpendicular components' amplitudes and phase difference. Right or left by the notes' rule: thumb along the travel, fingers with the rotation."
tags: [concept, waves]
aliases: ["circular polarization", "linear polarization", "elliptical polarization", "right-circular", "left-circular", "helicity"]
---

> [!key] Definition
> At a fixed point, the $\mathbf{E}$ of a plane wave travelling along $\hat u$ traces a line, circle or ellipse perpendicular to $\hat u$. For $\tilde{\mathbf{E}} = (A\hat x + Be^{j\phi}\hat y)e^{-j\beta z}$ with $A, B\ge0$:
>
> | polarization | condition |
> |---|---|
> | linear | $\phi = 0$ or $\pi$, or $A = 0$, or $B = 0$ |
> | right-circular | $A = B$, $\phi = -\pi/2$: $(\hat x - j\hat y)e^{-j\beta z}$ |
> | left-circular | $A = B$, $\phi = +\pi/2$: $(\hat x + j\hat y)e^{-j\beta z}$ |
> | elliptical | otherwise; right-handed if $\sin\phi<0$, left if $\sin\phi>0$ |
>
> **Handedness** (Kudeki): with the thumb along $\hat u$, the fingers of the right (left) hand curl the way $\mathbf{E}$ rotates. Seen looking along $\hat u$, right-handed turns clockwise. For travel along $-z$, swap right and left in the table.

**Reading a phasor.**
1. $\hat u$ from the exponent ($e^{+j\beta x}$ travels toward $-\hat x$).
2. $\mathbf{E}(0) = \text{Re}\{\tilde{\mathbf{E}}\}$ and $\mathbf{E}(T/4) = -\text{Im}\{\tilde{\mathbf{E}}\}$, where the exponent is 1.
3. $\hat u\cdot[\mathbf{E}(0)\times\mathbf{E}(T/4)]$ positive: right; negative: left; zero: linear.

Equivalently, the vector turns from the leading axis toward the lagging one. An overall complex factor never changes the polarization; $\mathbf{H} = \hat u\times\mathbf{E}/\eta$ shares it.

**Bases.** Any polarization is a weighted sum of an orthogonal pair: $\hat x = \tfrac12(\hat x - j\hat y) + \tfrac12(\hat x + j\hat y)$ and $\hat y = \tfrac1{2j}[(\hat x + j\hat y) - (\hat x - j\hat y)]$. Photons of a right- (left-) circular wave carry spin $+\hbar$ ($-\hbar$).

**Power.** In a lossless medium $\langle\mathbf{S}\rangle = \lvert\tilde{\mathbf{E}}\rvert^2\hat u/2\eta$: component powers add, whatever the phase. A circular wave carries twice one component's power, with constant instantaneous $\mathbf{S}$.

**Examples.**
- $(\hat z + j\hat y)e^{j\beta x}$ (notes' Example 1) travels toward $-x$ and turns from $y$ toward $z$: left-circular.
- A sheet current $\cos\omega t\,\hat x + \sin\omega t\,\hat y$ on $z = 0$ radiates right-circular into $z>0$ and left-circular into $z<0$.
- Two crossed sheets a quarter wave apart: [[problems/two-sheets-a-quarter-wave-apart]].

> [!trap]
> - $\hat x - j\hat y$ is right-circular only for travel along $+z$.
> - Other axes: components in cyclic order ($\hat y, \hat z$ for $\pm x$ travel; $\hat z, \hat x$ for $\pm y$), or the table's hand flips.
> - "Circular" needs equal amplitudes and a 90° phase difference; either alone is not enough.

**Where it appears.** [[3-maxwell-and-waves/24-signal-transmission-and-circular-polarization|Lecture 24]] (defined); [[3-maxwell-and-waves/21-monochromatic-waves-and-phasor-notation|Lecture 21]] (phasors); [[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets|Lecture 19]] (sheets as sources). Every Lecture 24 exam item on hand tests it.

**Practice.** [[practice/topics#group-velocity-and-wave-polarization|Group velocity and wave polarization]] (13 problems) — for example [[practice/24-group-velocity-and-polarization#241-crests-and-envelope-in-a-plasma|24.1 Crests and envelope in a plasma]] (easy), [[practice/24-group-velocity-and-polarization#246-from-two-snapshots-to-a-phasor|24.6 From two snapshots to a phasor]] (medium), [[practice/24-group-velocity-and-polarization#249-building-a-right-circular-wave|24.9 Building a right-circular wave]] (hard).

Related: [[concepts/phasors]] · [[concepts/plane-waves]] · [[concepts/poynting-vector]] · [[concepts/group-velocity]].
