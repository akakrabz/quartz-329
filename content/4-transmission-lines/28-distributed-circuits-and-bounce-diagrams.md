---
title: "Lecture 28 — Distributed circuits and bounce diagrams"
description: "A transmission line between a Thévenin generator and a resistive load: the generator launches τ_g = Z₀/(R_g + Z₀) of its voltage, each end reflects voltage by Γ = (R − Z₀)/(R + Z₀), and a bounce diagram in the z–t plane adds up the echoes. A step input settles to the DC voltage divider."
tags: [lecture, transmission-lines]
lecture: 28
---

*Lecture 28 · course notes §28 (no slides) · prev: [[4-transmission-lines/27-guided-tem-waves-on-transmission-lines|Lecture 27]] · next: [[4-transmission-lines/29-bounce-diagram-examples|Lecture 29]] · worked problem: [[problems/reading-a-line-from-two-pulses|Reading a line from two pulses]] · practice: [[practice/28-bounce-diagrams|12 problems]]*

> [!abstract] In one breath
> A line ($Z_0$, speed $v$, length $\ell$) joins a Thévenin generator ($f_i$ behind $R_g$) at $z = 0$ to a resistor $R_L$ at $z = \ell$. Circuit laws hold at the two terminals; on the line, $V$ and $I$ are d'Alembert waves. The generator launches $\tau_gf_i$, with $\tau_g = Z_0/(R_g+Z_0)$. Each end reflects voltage by $\Gamma = (R-Z_0)/(R+Z_0)$ and current by $-\Gamma$. A bounce diagram tracks every echo in the $z$–$t$ plane with its weight. $V(z,t)$ is the weighted sum of delayed copies of $f_i$. A step input settles to the DC divider $R_L/(R_g+R_L)$.

## 1. The circuit and the conventions

The notes' problem: a line of characteristic impedance $Z_0$ and speed $v$ runs from $z = 0$ to $z = \ell$ ($v = 1/\sqrt{\mathcal{L}\mathcal{C}}$ and $Z_0 = \sqrt{\mathcal{L}/\mathcal{C}}$ from [[4-transmission-lines/27-guided-tem-waves-on-transmission-lines|Lecture 27]]; $\mathcal{L}$, $\mathcal{C}$ of real lines in [[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials|Lecture 15]] §5). A Thévenin source drives it at $z = 0$: open-circuit voltage $f_i(t)$, resistance $R_g$ (for example a receiving antenna). A resistor $R_L$ terminates it at $z = \ell$ (a receiver). With $f_i(t) = 0$ for $t<0$, find $V(z,t)$ and $I(z,t)$ for $t>0$.

The method: ordinary circuit laws at the element terminals, d'Alembert waves on the line.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 236" width="640" height="236" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px"><defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker><marker id="ahs" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs><circle cx="52.0" cy="118.0" r="15.0" fill="none" stroke="var(--hi)" stroke-width="1.8"/><text x="52.0" y="115.0" text-anchor="middle" fill="var(--hi)" style="font-size:13px;">+</text><text x="52.0" y="130.0" text-anchor="middle" fill="var(--hi)" style="font-size:13px;">−</text><text x="32.0" y="123.0" text-anchor="end" fill="currentColor" style="font-size:13px;">f<tspan baseline-shift="sub" style="font-size:9px">i</tspan>(t)</text><line x1="52.0" y1="103.0" x2="52.0" y2="64.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><line x1="52.0" y1="64.0" x2="82.0" y2="64.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><path d="M82.0,64.0 L86.3,71.0 L95.0,57.0 L103.7,71.0 L112.3,57.0 L121.0,71.0 L129.7,57.0 L134.0,64.0" fill="none" stroke="var(--hi)" stroke-width="2.0" stroke-linejoin="round" stroke-linecap="round"/><text x="108.0" y="50.0" text-anchor="middle" fill="currentColor" style="font-size:13px;">R<tspan baseline-shift="sub" style="font-size:9px">g</tspan></text><line x1="134.0" y1="64.0" x2="170.0" y2="64.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><line x1="52.0" y1="133.0" x2="52.0" y2="172.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><line x1="52.0" y1="172.0" x2="170.0" y2="172.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><line x1="170.0" y1="64.0" x2="520.0" y2="64.0" stroke="currentColor" stroke-width="4.5" stroke-linecap="round"/><line x1="170.0" y1="172.0" x2="520.0" y2="172.0" stroke="currentColor" stroke-width="4.5" stroke-linecap="round"/><text x="514.0" y="55.0" text-anchor="end" fill="var(--muted)" style="font-size:10.5px;">wire 2</text><text x="514.0" y="189.0" text-anchor="end" fill="var(--muted)" style="font-size:10.5px;">wire 1</text><text x="385.0" y="50.0" text-anchor="middle" fill="currentColor" style="font-size:13px;">Z<tspan baseline-shift="sub" style="font-size:9px">0</tspan>, v,  T = ℓ/v</text><line x1="520.0" y1="64.0" x2="576.0" y2="64.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><line x1="576.0" y1="64.0" x2="576.0" y2="88.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><path d="M576.0,88.0 L569.0,93.0 L583.0,103.0 L569.0,113.0 L583.0,123.0 L569.0,133.0 L583.0,143.0 L576.0,148.0" fill="none" stroke="var(--hi)" stroke-width="2.0" stroke-linejoin="round" stroke-linecap="round"/><line x1="576.0" y1="148.0" x2="576.0" y2="172.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><line x1="576.0" y1="172.0" x2="520.0" y2="172.0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><text x="590.0" y="123.0" text-anchor="start" fill="currentColor" style="font-size:13px;">R<tspan baseline-shift="sub" style="font-size:9px">L</tspan></text><text x="214.0" y="84.0" text-anchor="middle" fill="currentColor" style="font-size:14px;">+</text><text x="214.0" y="123.0" text-anchor="middle" fill="currentColor" style="font-size:13px;">V(z,t)</text><text x="214.0" y="163.0" text-anchor="middle" fill="currentColor" style="font-size:14px;">−</text><line x1="188.0" y1="52.0" x2="232.0" y2="52.0" stroke="var(--hi)" stroke-width="1.8" marker-end="url(#ahs)" stroke-linecap="round"/><text x="210.0" y="44.0" text-anchor="middle" fill="var(--hi)" style="font-size:12px;">I(z,t)</text><line x1="232.0" y1="184.0" x2="188.0" y2="184.0" stroke="var(--hi)" stroke-width="1.8" marker-end="url(#ahs)" stroke-linecap="round"/><text x="210.0" y="199.0" text-anchor="middle" fill="var(--hi)" style="font-size:12px;">I(z,t)</text><line x1="320.0" y1="100.0" x2="470.0" y2="100.0" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#ahs)" stroke-linecap="round"/><text x="395.0" y="90.0" text-anchor="middle" fill="var(--accent)" style="font-size:12px;">f(t − z/v),  I = +V/Z<tspan baseline-shift="sub" style="font-size:9px">0</tspan></text><line x1="470.0" y1="138.0" x2="320.0" y2="138.0" stroke="var(--accent2)" stroke-width="2.2" marker-end="url(#ahs)" stroke-linecap="round"/><text x="395.0" y="128.0" text-anchor="middle" fill="var(--accent2)" style="font-size:12px;">g(t + z/v),  I = −V/Z<tspan baseline-shift="sub" style="font-size:9px">0</tspan></text><line x1="170.0" y1="214.0" x2="590.0" y2="214.0" stroke="currentColor" stroke-width="1.2" marker-end="url(#ah)" stroke-linecap="round"/><text x="596.0" y="218.0" text-anchor="start" fill="currentColor" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">z</text><line x1="170.0" y1="210.0" x2="170.0" y2="218.0" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/><text x="170.0" y="205.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">0</text><text x="170.0" y="231.0" text-anchor="middle" fill="var(--muted)" style="font-size:10.5px;">generator</text><line x1="520.0" y1="210.0" x2="520.0" y2="218.0" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/><text x="520.0" y="205.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">ℓ</text><text x="520.0" y="231.0" text-anchor="middle" fill="var(--muted)" style="font-size:10.5px;">load</text></svg><figcaption><strong>The notes' circuit, with the site's references.</strong> V(z,t) is wire 2 relative to wire 1; I(z,t) flows along +z on wire 2 and returns on wire 1. Forward waves carry I = +V/Z<sub>0</sub>, backward waves I = −V/Z<sub>0</sub>.</figcaption></figure>

> [!key] Conventions (Lectures 28–30)
> - $z = 0$ is the generator end, $z = \ell$ the load end; $+z$ points toward the load. One-way delay $T = \ell/v$.
> - $V(z,t)$ is wire 2 (upper) relative to wire 1. $I(z,t)$ flows along $+z$ on wire 2 and returns on wire 1.
> - On the line, the d'Alembert pair of [[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves#4-the-1d-wave-equation-and-its-solutions|Lecture 18 §4]], now for $V$ and $I$:
> $$
> \begin{gathered}
> V(z,t) = f\Big(t-\frac zv\Big) + g\Big(t+\frac zv\Big),\\[4pt]
> I(z,t) = \frac{1}{Z_0}\Big[f\Big(t-\frac zv\Big) - g\Big(t+\frac zv\Big)\Big].
> \end{gathered}
> $$
> A forward wave carries $I = +V/Z_0$, a backward wave $I = -V/Z_0$.
> - $\Gamma_L$, $\Gamma_g$: reflected over incident **voltage**, at the load and at the generator. For current the ratio is $-\Gamma$.
> - $\tau_g$: launched forward voltage over the generator's open-circuit voltage.
> - Bounce diagram: $z$ across (generator on the left), $t$ downward, each segment labelled with its voltage weight.

Notation: the notes write $Z_o$ and use both $l$ and $\ell$; $T$ is the site's shorthand for their $\ell/v$.

## 2. The load reflection coefficient

At $z = \ell$ the resistor fixes $V/I$ (the notes' $V_L/I_L$, load voltage over load current):

$$
\frac{V(\ell,t)}{I(\ell,t)} = Z_0\,\frac{f(t-T)+g(t+T)}{f(t-T)-g(t+T)} = R_L .
$$

Solve for $g$, then replace $t$ by $t-T$:

> [!key] Load reflection coefficient
> $$
> \begin{gathered}
> g(t+T) = \Gamma_L\,f(t-T),\\[4pt]
> g(t) = \Gamma_L\,f(t-2T),\\[4pt]
> \Gamma_L = \frac{R_L-Z_0}{R_L+Z_0},\\[8pt]
> V(z,t) = f\Big(t-\frac zv\Big) + \Gamma_Lf\Big(t+\frac zv-2T\Big),\\[4pt]
> I(z,t) = \frac{1}{Z_0}\Big[f\Big(t-\frac zv\Big)\\[2pt]
> -\ \Gamma_Lf\Big(t+\frac zv-2T\Big)\Big].
> \end{gathered}
> $$
> The backward wave is the forward one scaled by $\Gamma_L$ and delayed by the round trip $2(\ell-z)/v$ from $z$ to the load and back.

This is [[3-maxwell-and-waves/25-wave-reflection-and-transmission|Lecture 25]]'s $\Gamma = (\eta_2-\eta_1)/(\eta_2+\eta_1)$, with $Z_0$ for the incident side's $\eta_1$ and $R_L$ for $\eta_2$. The reflected current carries $-\Gamma_L$, as the reflected $\mathbf{H}$ carries $-\Gamma$.

## 3. The generator: injection and reflection

KVL around the source loop at $z = 0$, with §2's $V$ and $I$:

$$
\begin{gathered}
f_i(t) = R_g\,I(0,t) + V(0,t)\\[4pt]
= \frac{R_g}{Z_0}\big[f(t)-\Gamma_Lf(t-2T)\big]\\[4pt]
+\ f(t) + \Gamma_Lf(t-2T).
\end{gathered}
$$

**First epoch, $0<t<2T$.** Nothing has come back yet: $f(t-2T) = 0$. Then $f_i = (1+R_g/Z_0)f$, so

$$
f(t) = \tau_g\,f_i(t),\qquad \tau_g = \frac{Z_0}{R_g+Z_0}.
$$

$\tau_g$ is the **injection coefficient**. It is a voltage divider: until the first echo returns, the line looks like a resistor $Z_0$ (the notes' footnote).

**Later epochs.** Regroup the KVL as

$$
f_i(t) = \Big(1+\frac{R_g}{Z_0}\Big)f(t) + \Big(1-\frac{R_g}{Z_0}\Big)\Gamma_Lf(t-2T),
$$

where $f(t-2T)$ is already known from the epoch before. Solve for $f(t)$:

> [!key] Injection and generator reflection
> $$
> \begin{gathered}
> f(t) = \tau_g\,f_i(t) + \Gamma_g\Gamma_L\,f(t-2T),\\[6pt]
> \tau_g = \frac{Z_0}{R_g+Z_0},\qquad \Gamma_g = \frac{R_g-Z_0}{R_g+Z_0}.
> \end{gathered}
> $$
> The wave leaving $z = 0$ is the fresh injection plus the returning wave reflected with $\Gamma_g$, the **source reflection coefficient**. $\Gamma_g$ is $\Gamma_L$ with $R_L$ replaced by $R_g$: the same process at the other end. Also $\tau_g = (1-\Gamma_g)/2$.

The notes do this one epoch at a time with $f_i = \delta(t)$: for $2T<t<4T$, $f(t) = \tau_g\delta(t) + \Gamma_g\Gamma_L\tau_g\delta(t-2T)$. The recursion above covers every epoch at once.

> [!intuition] Why the generator reflects through its resistance alone
> By superposition, the source's own output is already the injected $\tau_gf_i$. A returning wave therefore sees the ideal source as a short, leaving $R_g$ alone (Rao §7.4).

## 4. Impulse response and the bounce diagram

With $f_i = \delta(t)$, $V(z,t)$ is the **impulse response**, which the notes call $h_z(t)$. Iterating the recursion gives $f(t) = \tau_g\sum_n(\Gamma_L\Gamma_g)^n\delta(t-2nT)$, and §2 then gives:

> [!key] Impulse response
> $$
> \begin{gathered}
> V(z,t) = \tau_g\sum_{n=0}^{\infty}(\Gamma_L\Gamma_g)^n\Big[\delta\Big(t-\frac zv-2nT\Big)\\[2pt]
> +\ \Gamma_L\,\delta\Big(t+\frac zv-2(n+1)T\Big)\Big],\\[10pt]
> I(z,t) = \frac{\tau_g}{Z_0}\sum_{n=0}^{\infty}(\Gamma_L\Gamma_g)^n\Big[\delta\Big(t-\frac zv-2nT\Big)\\[2pt]
> -\ \Gamma_L\,\delta\Big(t+\frac zv-2(n+1)T\Big)\Big].
> \end{gathered}
> $$

Terms shrink as $(\Gamma_L\Gamma_g)^n$. Passive resistors give $\lvert\Gamma\rvert\le1$, so usually only the first few terms matter. They decay slowly if $\lvert\Gamma_L\Gamma_g\rvert$ is near 1, and never if both ends reflect totally ($\lvert\Gamma_L\Gamma_g\rvert = 1$, a lossless resonant circuit: Lecture 31).

The bounce diagram draws these terms instead of writing them out.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 410" width="640" height="410" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px"><defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker><marker id="ahs" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs><line x1="92.0" y1="62.0" x2="446.0" y2="62.0" stroke="currentColor" stroke-width="1.3" marker-end="url(#ah)" stroke-linecap="round"/><text x="452.0" y="66.0" text-anchor="start" fill="currentColor" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">z</text><line x1="92.0" y1="62.0" x2="92.0" y2="389.5" stroke="currentColor" stroke-width="1.3" marker-end="url(#ah)" stroke-linecap="round"/><text x="92.0" y="405.5" text-anchor="middle" fill="currentColor" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">t</text><line x1="412.0" y1="62.0" x2="412.0" y2="377.0" stroke="currentColor" stroke-width="1.0" stroke-dasharray="3 3" opacity="0.6" stroke-linecap="round"/><text x="92.0" y="52.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">0</text><text x="412.0" y="52.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">ℓ</text><text x="96.0" y="32.0" text-anchor="start" fill="var(--muted)" style="font-size:12px;">generator: Γ<tspan baseline-shift="sub" style="font-size:9px">g</tspan>, τ<tspan baseline-shift="sub" style="font-size:9px">g</tspan></text><text x="416.0" y="32.0" text-anchor="end" fill="var(--muted)" style="font-size:12px;">load: Γ<tspan baseline-shift="sub" style="font-size:9px">L</tspan></text><line x1="408.0" y1="112.0" x2="416.0" y2="112.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="422.0" y="116.0" text-anchor="start" fill="var(--muted)" style="font-size:11.5px;">T</text><line x1="88.0" y1="162.0" x2="96.0" y2="162.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="82.0" y="166.0" text-anchor="end" fill="var(--muted)" style="font-size:11.5px;">2T</text><line x1="408.0" y1="212.0" x2="416.0" y2="212.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="422.0" y="216.0" text-anchor="start" fill="var(--muted)" style="font-size:11.5px;">3T</text><line x1="88.0" y1="262.0" x2="96.0" y2="262.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="82.0" y="266.0" text-anchor="end" fill="var(--muted)" style="font-size:11.5px;">4T</text><line x1="408.0" y1="312.0" x2="416.0" y2="312.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="422.0" y="316.0" text-anchor="start" fill="var(--muted)" style="font-size:11.5px;">5T</text><line x1="88.0" y1="362.0" x2="96.0" y2="362.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="82.0" y="366.0" text-anchor="end" fill="var(--muted)" style="font-size:11.5px;">6T</text><line x1="92.0" y1="62.0" x2="412.0" y2="112.0" stroke="var(--accent)" stroke-width="2.4" marker-end="url(#ah)" stroke-linecap="round"/><text x="284.0" y="83.0" text-anchor="middle" fill="var(--accent)" style="font-size:12.5px;">τ<tspan baseline-shift="sub" style="font-size:9px">g</tspan></text><line x1="412.0" y1="112.0" x2="92.0" y2="162.0" stroke="var(--accent2)" stroke-width="2.4" marker-end="url(#ah)" stroke-linecap="round"/><text x="220.0" y="133.0" text-anchor="middle" fill="var(--accent2)" style="font-size:12.5px;">τ<tspan baseline-shift="sub" style="font-size:9px">g</tspan>Γ<tspan baseline-shift="sub" style="font-size:9px">L</tspan></text><line x1="92.0" y1="162.0" x2="412.0" y2="212.0" stroke="var(--accent)" stroke-width="2.4" marker-end="url(#ah)" stroke-linecap="round"/><text x="284.0" y="183.0" text-anchor="middle" fill="var(--accent)" style="font-size:12.5px;">τ<tspan baseline-shift="sub" style="font-size:9px">g</tspan>Γ<tspan baseline-shift="sub" style="font-size:9px">L</tspan>Γ<tspan baseline-shift="sub" style="font-size:9px">g</tspan></text><line x1="412.0" y1="212.0" x2="92.0" y2="262.0" stroke="var(--accent2)" stroke-width="2.4" marker-end="url(#ah)" stroke-linecap="round"/><text x="220.0" y="233.0" text-anchor="middle" fill="var(--accent2)" style="font-size:12.5px;">τ<tspan baseline-shift="sub" style="font-size:9px">g</tspan>Γ<tspan baseline-shift="sub" style="font-size:9px">L</tspan><tspan baseline-shift="super" style="font-size:9px">2</tspan>Γ<tspan baseline-shift="sub" style="font-size:9px">g</tspan></text><line x1="92.0" y1="262.0" x2="412.0" y2="312.0" stroke="var(--accent)" stroke-width="2.4" marker-end="url(#ah)" stroke-linecap="round"/><text x="284.0" y="283.0" text-anchor="middle" fill="var(--accent)" style="font-size:12.5px;">τ<tspan baseline-shift="sub" style="font-size:9px">g</tspan>Γ<tspan baseline-shift="sub" style="font-size:9px">L</tspan><tspan baseline-shift="super" style="font-size:9px">2</tspan>Γ<tspan baseline-shift="sub" style="font-size:9px">g</tspan><tspan baseline-shift="super" style="font-size:9px">2</tspan></text><line x1="412.0" y1="312.0" x2="92.0" y2="362.0" stroke="var(--accent2)" stroke-width="2.4" marker-end="url(#ah)" stroke-linecap="round"/><text x="220.0" y="333.0" text-anchor="middle" fill="var(--accent2)" style="font-size:12.5px;">τ<tspan baseline-shift="sub" style="font-size:9px">g</tspan>Γ<tspan baseline-shift="sub" style="font-size:9px">L</tspan><tspan baseline-shift="super" style="font-size:9px">3</tspan>Γ<tspan baseline-shift="sub" style="font-size:9px">g</tspan><tspan baseline-shift="super" style="font-size:9px">2</tspan></text><line x1="188.0" y1="62.0" x2="188.0" y2="377.0" stroke="var(--hi)" stroke-width="1.4" stroke-dasharray="5 4" stroke-linecap="round"/><text x="188.0" y="52.0" text-anchor="middle" fill="var(--hi)" style="font-size:12px;">z<tspan baseline-shift="sub" style="font-size:9px">p</tspan></text><circle cx="188.0" cy="77.0" r="3.8" fill="var(--hi)" stroke="none" stroke-width="1.5"/><circle cx="188.0" cy="147.0" r="3.8" fill="var(--hi)" stroke="none" stroke-width="1.5"/><circle cx="188.0" cy="177.0" r="3.8" fill="var(--hi)" stroke="none" stroke-width="1.5"/><circle cx="188.0" cy="247.0" r="3.8" fill="var(--hi)" stroke="none" stroke-width="1.5"/><circle cx="188.0" cy="277.0" r="3.8" fill="var(--hi)" stroke="none" stroke-width="1.5"/><circle cx="188.0" cy="347.0" r="3.8" fill="var(--hi)" stroke="none" stroke-width="1.5"/><text x="530.0" y="32.0" text-anchor="middle" fill="currentColor" style="font-size:12.5px;font-weight:600;">V<tspan baseline-shift="sub" style="font-size:9px"></tspan>(z<tspan baseline-shift="sub" style="font-size:9px">p</tspan>, t)</text><text x="530.0" y="50.0" text-anchor="middle" fill="var(--muted)" style="font-size:10.5px;">drawn for Γ<tspan baseline-shift="sub" style="font-size:9px">L</tspan> = −½, Γ<tspan baseline-shift="sub" style="font-size:9px">g</tspan> = ½</text><line x1="530.0" y1="62.0" x2="530.0" y2="389.5" stroke="currentColor" stroke-width="1.2" marker-end="url(#ah)" stroke-linecap="round"/><text x="530.0" y="405.5" text-anchor="middle" fill="currentColor" style="font-size:13px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">t</text><line x1="442.0" y1="77.0" x2="526.0" y2="77.0" stroke="var(--hi)" stroke-width="0.9" stroke-dasharray="1 4" opacity="0.7" stroke-linecap="round"/><line x1="530.0" y1="77.0" x2="592.0" y2="77.0" stroke="currentColor" stroke-width="2.0" marker-end="url(#ahs)" stroke-linecap="round"/><text x="602.0" y="81.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">0.3T</text><line x1="442.0" y1="147.0" x2="526.0" y2="147.0" stroke="var(--hi)" stroke-width="0.9" stroke-dasharray="1 4" opacity="0.7" stroke-linecap="round"/><line x1="530.0" y1="147.0" x2="499.0" y2="147.0" stroke="currentColor" stroke-width="2.0" marker-end="url(#ahs)" stroke-linecap="round"/><text x="602.0" y="151.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">1.7T</text><line x1="442.0" y1="177.0" x2="526.0" y2="177.0" stroke="var(--hi)" stroke-width="0.9" stroke-dasharray="1 4" opacity="0.7" stroke-linecap="round"/><line x1="530.0" y1="177.0" x2="514.5" y2="177.0" stroke="currentColor" stroke-width="2.0" marker-end="url(#ahs)" stroke-linecap="round"/><text x="602.0" y="181.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">2.3T</text><line x1="442.0" y1="247.0" x2="526.0" y2="247.0" stroke="var(--hi)" stroke-width="0.9" stroke-dasharray="1 4" opacity="0.7" stroke-linecap="round"/><line x1="530.0" y1="247.0" x2="537.8" y2="247.0" stroke="currentColor" stroke-width="2.0" marker-end="url(#ahs)" stroke-linecap="round"/><text x="602.0" y="251.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">3.7T</text><line x1="442.0" y1="277.0" x2="526.0" y2="277.0" stroke="var(--hi)" stroke-width="0.9" stroke-dasharray="1 4" opacity="0.7" stroke-linecap="round"/><line x1="530.0" y1="277.0" x2="533.9" y2="277.0" stroke="currentColor" stroke-width="2.0" marker-end="url(#ahs)" stroke-linecap="round"/><text x="602.0" y="281.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">4.3T</text><line x1="442.0" y1="347.0" x2="526.0" y2="347.0" stroke="var(--hi)" stroke-width="0.9" stroke-dasharray="1 4" opacity="0.7" stroke-linecap="round"/><line x1="530.0" y1="347.0" x2="528.1" y2="347.0" stroke="currentColor" stroke-width="2.0" marker-end="url(#ahs)" stroke-linecap="round"/><text x="602.0" y="351.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">5.7T</text></svg><figcaption><strong>Bounce diagram for an impulse input.</strong> Each segment is one travelling impulse, labelled with its voltage weight; ×Γ<sub>L</sub> at the load, ×Γ<sub>g</sub> at the generator. The dashed line at z<sub>p</sub> = 0.3ℓ meets them at z<sub>p</sub>/v + 2nT (forward) and 2T − z<sub>p</sub>/v + 2nT (backward): V(z<sub>p</sub>, t), right.</figcaption></figure>

- One slanted segment per travelling impulse. It crosses the line in time $T$, its lifetime.
- Weights: $\tau_g$ on the first segment, then $\times\Gamma_L$ at each load reflection and $\times\Gamma_g$ at each generator reflection.
- Forward segment $n$, weight $\tau_g(\Gamma_L\Gamma_g)^n$, passes $z$ at $t = z/v+2nT$. Backward segment $n$, weight $\tau_g\Gamma_L(\Gamma_L\Gamma_g)^n$, passes $z$ at $t = 2T-z/v+2nT$.

> [!recipe] Reading V and I off a bounce diagram
> 1. Draw a vertical line at the observation point $z_p$.
> 2. Each crossing is one impulse of $V(z_p,t)$, at the crossing time, with the segment's weight.
> 3. $I(z_p,t)$: the same impulses divided by $Z_0$, with the sign flipped on backward segments.
> 4. Any other input: replace each $\delta(t-t_k)$ by $f_i(t-t_k)$, since $\delta(t-t_k)*f_i(t) = f_i(t-t_k)$. For a step $V_0u(t)$, $V(z_p,t)$ is $V_0$ times the running sum of the weights crossed so far.
> 5. At an end, the arriving segment and its reflection cross together: add both, e.g. $(1+\Gamma_L)w$ at the load.

> [!example] Example — reading one point (this site's numbers)
> $Z_0 = 60\ \Omega$, $R_g = 180\ \Omega$, $R_L = 20\ \Omega$: $\tau_g = \tfrac14$, $\Gamma_g = \tfrac12$, $\Gamma_L = -\tfrac12$. Weights: $\tfrac14$, $-\tfrac18$, $-\tfrac1{16}$, $\tfrac1{32}$, … At $z = \ell/2$:
> $$
> \begin{gathered}
> h_{\ell/2}(t) = \tfrac14\delta(t-\tfrac T2) - \tfrac18\delta(t-\tfrac{3T}2)\\
> - \tfrac1{16}\delta(t-\tfrac{5T}2) + \tfrac1{32}\delta(t-\tfrac{7T}2) + \ldots,\\[6pt]
> Z_0I\big(\tfrac\ell2,t\big) = \tfrac14\delta(t-\tfrac T2) + \tfrac18\delta(t-\tfrac{3T}2)\\
> - \tfrac1{16}\delta(t-\tfrac{5T}2) - \tfrac1{32}\delta(t-\tfrac{7T}2) + \ldots
> \end{gathered}
> $$
> The second and fourth impulses travel backward, so their current signs flip.

## 5. Step inputs and the DC limit

For $f_i = V_0u(t)$ each crossing adds a step, so $V(z,t)$ is a staircase. As $t\to\infty$, sum the geometric series ($\lvert\Gamma_L\Gamma_g\rvert<1$):

> [!key] DC limit of a step response (this site's derivation)
> $$
> \begin{gathered}
> V(z,\infty) = V_0\,\tau_g\,\frac{1+\Gamma_L}{1-\Gamma_L\Gamma_g} = V_0\,\frac{R_L}{R_g+R_L},\\[8pt]
> I(z,\infty) = \frac{V_0}{Z_0}\,\tau_g\,\frac{1-\Gamma_L}{1-\Gamma_L\Gamma_g} = \frac{V_0}{R_g+R_L},
> \end{gathered}
> $$
> the same at every $z$. In DC the line is just two wires, and the circuit is the lumped divider. The notes reach this by example in [[4-transmission-lines/29-bounce-diagram-examples|Lecture 29]]. Use it to check any step-driven diagram.

> [!derivation]- The algebra
> $$
> \begin{gathered}
> 1-\Gamma_L\Gamma_g = \frac{(R_L+Z_0)(R_g+Z_0)-(R_L-Z_0)(R_g-Z_0)}{(R_L+Z_0)(R_g+Z_0)}\\[6pt]
> = \frac{2Z_0(R_L+R_g)}{(R_L+Z_0)(R_g+Z_0)},\\[8pt]
> \tau_g(1+\Gamma_L) = \frac{2Z_0R_L}{(R_g+Z_0)(R_L+Z_0)},\\[6pt]
> \tau_g(1-\Gamma_L) = \frac{2Z_0^2}{(R_g+Z_0)(R_L+Z_0)}.
> \end{gathered}
> $$
> Divide the last two lines by the first.

> [!example] Example — the same circuit, 12 V step (this site's numbers)
> - First wave: $12\tau_g = 3$ V. Weights $3$, $-1.5$, $-0.75$, $0.375$, … V.
> - Load, $(1+\Gamma_L)\times$ each arrival: $V(\ell,t) = 1.5$ V on $(T,3T)$, $1.125$ V on $(3T,5T)$, then $1.219$, $1.195$, …
> - Midpoint: $3$, $1.5$, $0.75$, $1.125$, $1.3125$, … V, one step per $T$ from $T/2$.
> - DC: $12\cdot\tfrac{20}{180+20} = 1.2$ V, and $I = 12/200 = 60$ mA.
> - $\Gamma_L\Gamma_g = -\tfrac14<0$, so the staircase overshoots and undershoots on its way.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 330" width="640" height="330" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px"><defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker><marker id="ahs" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs><text x="20.0" y="20.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;font-weight:600;">12 V step: weights (V)</text><line x1="40.0" y1="58.0" x2="222.0" y2="58.0" stroke="currentColor" stroke-width="1.2" marker-end="url(#ah)" stroke-linecap="round"/><text x="226.0" y="62.0" text-anchor="start" fill="currentColor" style="font-size:12px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">z</text><line x1="40.0" y1="58.0" x2="40.0" y2="301.2" stroke="currentColor" stroke-width="1.2" marker-end="url(#ah)" stroke-linecap="round"/><text x="40.0" y="316.2" text-anchor="middle" fill="currentColor" style="font-size:12px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">t</text><line x1="200.0" y1="58.0" x2="200.0" y2="293.6" stroke="currentColor" stroke-width="1.0" stroke-dasharray="3 3" opacity="0.6" stroke-linecap="round"/><text x="38.0" y="50.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">Γ<tspan baseline-shift="sub" style="font-size:9px">g</tspan> = ½</text><text x="202.0" y="50.0" text-anchor="end" fill="var(--muted)" style="font-size:11px;">Γ<tspan baseline-shift="sub" style="font-size:9px">L</tspan> = −½</text><line x1="40.0" y1="58.0" x2="200.0" y2="96.0" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#ah)" stroke-linecap="round"/><text x="152.0" y="76.6" text-anchor="middle" fill="var(--accent)" style="font-size:11.5px;">+3</text><line x1="200.0" y1="96.0" x2="40.0" y2="134.0" stroke="var(--accent2)" stroke-width="2.2" marker-end="url(#ah)" stroke-linecap="round"/><text x="80.0" y="116.5" text-anchor="middle" fill="var(--accent2)" style="font-size:11.5px;">−1.5</text><line x1="40.0" y1="134.0" x2="200.0" y2="172.0" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#ah)" stroke-linecap="round"/><text x="152.0" y="152.6" text-anchor="middle" fill="var(--accent)" style="font-size:11.5px;">−0.75</text><line x1="200.0" y1="172.0" x2="40.0" y2="210.0" stroke="var(--accent2)" stroke-width="2.2" marker-end="url(#ah)" stroke-linecap="round"/><text x="80.0" y="192.5" text-anchor="middle" fill="var(--accent2)" style="font-size:11.5px;">+0.375</text><line x1="40.0" y1="210.0" x2="200.0" y2="248.0" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#ah)" stroke-linecap="round"/><text x="152.0" y="228.6" text-anchor="middle" fill="var(--accent)" style="font-size:11.5px;">+0.1875</text><line x1="200.0" y1="248.0" x2="40.0" y2="286.0" stroke="var(--accent2)" stroke-width="2.2" marker-end="url(#ah)" stroke-linecap="round"/><text x="80.0" y="268.5" text-anchor="middle" fill="var(--accent2)" style="font-size:11.5px;">−0.09375</text><line x1="120.0" y1="58.0" x2="120.0" y2="293.6" stroke="var(--hi)" stroke-width="1.2" stroke-dasharray="5 4" stroke-linecap="round"/><text x="120.0" y="50.0" text-anchor="middle" fill="var(--hi)" style="font-size:11px;">ℓ/2</text><text x="208.0" y="100.0" text-anchor="start" fill="var(--muted)" style="font-size:10.5px;">T</text><text x="208.0" y="176.0" text-anchor="start" fill="var(--muted)" style="font-size:10.5px;">3T</text><text x="208.0" y="252.0" text-anchor="start" fill="var(--muted)" style="font-size:10.5px;">5T</text><text x="34.0" y="138.0" text-anchor="end" fill="var(--muted)" style="font-size:10.5px;">2T</text><text x="34.0" y="214.0" text-anchor="end" fill="var(--muted)" style="font-size:10.5px;">4T</text><text x="34.0" y="290.0" text-anchor="end" fill="var(--muted)" style="font-size:10.5px;">6T</text><text x="300.0" y="20.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;font-weight:600;">V(z, t) for f<tspan baseline-shift="sub" style="font-size:9px">i</tspan> = 12u(t) V</text><line x1="300.0" y1="290.0" x2="608.0" y2="290.0" stroke="currentColor" stroke-width="1.2" marker-end="url(#ah)" stroke-linecap="round"/><text x="612.0" y="294.0" text-anchor="start" fill="currentColor" style="font-size:11.5px;">t/T</text><line x1="300.0" y1="290.0" x2="300.0" y2="42.0" stroke="currentColor" stroke-width="1.2" marker-end="url(#ah)" stroke-linecap="round"/><line x1="300.0" y1="290.0" x2="300.0" y2="294.0" stroke="currentColor" stroke-width="1.0" stroke-linecap="round"/><text x="300.0" y="306.0" text-anchor="middle" fill="var(--muted)" style="font-size:10.5px;">0</text><line x1="374.0" y1="290.0" x2="374.0" y2="294.0" stroke="currentColor" stroke-width="1.0" stroke-linecap="round"/><text x="374.0" y="306.0" text-anchor="middle" fill="var(--muted)" style="font-size:10.5px;">2</text><line x1="448.0" y1="290.0" x2="448.0" y2="294.0" stroke="currentColor" stroke-width="1.0" stroke-linecap="round"/><text x="448.0" y="306.0" text-anchor="middle" fill="var(--muted)" style="font-size:10.5px;">4</text><line x1="522.0" y1="290.0" x2="522.0" y2="294.0" stroke="currentColor" stroke-width="1.0" stroke-linecap="round"/><text x="522.0" y="306.0" text-anchor="middle" fill="var(--muted)" style="font-size:10.5px;">6</text><line x1="596.0" y1="290.0" x2="596.0" y2="294.0" stroke="currentColor" stroke-width="1.0" stroke-linecap="round"/><text x="596.0" y="306.0" text-anchor="middle" fill="var(--muted)" style="font-size:10.5px;">8</text><line x1="296.0" y1="290.0" x2="300.0" y2="290.0" stroke="currentColor" stroke-width="1.0" stroke-linecap="round"/><text x="293.0" y="294.0" text-anchor="end" fill="var(--muted)" style="font-size:10.5px;">0</text><line x1="296.0" y1="200.0" x2="300.0" y2="200.0" stroke="currentColor" stroke-width="1.0" stroke-linecap="round"/><text x="293.0" y="204.0" text-anchor="end" fill="var(--hi)" style="font-size:10.5px;">1.2</text><line x1="296.0" y1="140.0" x2="300.0" y2="140.0" stroke="currentColor" stroke-width="1.0" stroke-linecap="round"/><text x="293.0" y="144.0" text-anchor="end" fill="var(--muted)" style="font-size:10.5px;">2</text><line x1="296.0" y1="65.0" x2="300.0" y2="65.0" stroke="currentColor" stroke-width="1.0" stroke-linecap="round"/><text x="293.0" y="69.0" text-anchor="end" fill="var(--muted)" style="font-size:10.5px;">3</text><line x1="300.0" y1="200.0" x2="596.0" y2="200.0" stroke="var(--hi)" stroke-width="1.4" stroke-dasharray="6 4" stroke-linecap="round"/><text x="596.0" y="218.0" text-anchor="end" fill="var(--hi)" style="font-size:11px;">DC: 12·R<tspan baseline-shift="sub" style="font-size:9px">L</tspan>/(R<tspan baseline-shift="sub" style="font-size:9px">g</tspan> + R<tspan baseline-shift="sub" style="font-size:9px">L</tspan>) = 1.2 V</text><path d="M300.0,290.0 L318.5,290.0 L318.6,65.0 L355.5,65.0 L355.6,177.5 L392.5,177.5 L392.6,233.8 L429.5,233.8 L429.6,205.6 L466.5,205.6 L466.6,191.6 L503.5,191.6 L503.6,198.6 L540.5,198.6 L540.6,202.1 L577.5,202.1 L577.6,200.4 L596.0,200.4" fill="none" stroke="var(--accent)" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"/><path d="M300.0,290.0 L337.0,290.0 L337.1,177.5 L411.0,177.5 L411.1,205.6 L485.0,205.6 L485.1,198.6 L559.0,198.6 L559.1,200.4 L596.0,200.4" fill="none" stroke="var(--accent2)" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"/><line x1="420.0" y1="70.0" x2="444.0" y2="70.0" stroke="var(--accent)" stroke-width="2.4" stroke-linecap="round"/><text x="450.0" y="74.0" text-anchor="start" fill="currentColor" style="font-size:11.5px;">z = ℓ/2</text><line x1="520.0" y1="70.0" x2="544.0" y2="70.0" stroke="var(--accent2)" stroke-width="2.4" stroke-linecap="round"/><text x="550.0" y="74.0" text-anchor="start" fill="currentColor" style="font-size:11.5px;">z = ℓ (load)</text></svg><figcaption><strong>Example: Z<sub>0</sub> = 60 Ω, R<sub>g</sub> = 180 Ω, R<sub>L</sub> = 20 Ω, 12 V step.</strong> Each crossing adds its weight, so V(z,t) is a staircase. Γ<sub>L</sub>Γ<sub>g</sub> = −¼ makes it overshoot and undershoot the DC value, at every z. Checked against an FDTD run.</figcaption></figure>

The DC shortcut needs an input that settles to a constant. A switched-on sine does not settle (Lecture 29; Lecture 31).

## 6. Special terminations

Rao §7.4 lists the load cases; the notes use $\Gamma_g = 0$ and $\Gamma_g = -1$ in Lecture 29.

| end | resistor | coefficients | on the line |
|---|---|---|---|
| matched load | $R_L = Z_0$ | $\Gamma_L = 0$ | no echo: the line looks infinitely long |
| open load | $R_L\to\infty$ | $\Gamma_L = +1$ | $I(\ell,t) = 0$; $V(\ell,t)$ is twice the arriving voltage |
| shorted load | $R_L = 0$ | $\Gamma_L = -1$ | $V(\ell,t) = 0$; $I(\ell,t)$ is twice the arriving current |
| matched generator | $R_g = Z_0$ | $\Gamma_g = 0$, $\tau_g = \tfrac12$ | echoes are absorbed at $z = 0$; the diagram ends at $t = 2T$ |
| ideal source | $R_g = 0$ | $\Gamma_g = -1$, $\tau_g = 1$ | $V(0,t) = f_i(t)$ at all times |

> [!trap] Bounce-diagram traps
> - $\Gamma_g$ uses $R_g$ alone; the source voltage enters only through $\tau_g$.
> - $\tau_g = Z_0/(R_g+Z_0)$ is not Lecture 25's $\tau = 1+\Gamma$; here $\tau_g = (1-\Gamma_g)/2$.
> - Backward waves carry $I = -V/Z_0$; a current diagram uses $-\Gamma_L$ and $-\Gamma_g$.
> - $V/I = Z_0$ holds for a single forward wave, not for the total $V/I$ (unless nothing reflects).

## 7. Summary

- Circuit laws at the terminals, d'Alembert waves in between. Forward: $I = V/Z_0$; backward: $I = -V/Z_0$.
- Load: $g(t) = \Gamma_Lf(t-2T)$, $\Gamma_L = (R_L-Z_0)/(R_L+Z_0)$. Generator: $f(t) = \tau_gf_i(t) + \Gamma_g\Gamma_Lf(t-2T)$, with $\tau_g = Z_0/(R_g+Z_0)$ and $\Gamma_g = (R_g-Z_0)/(R_g+Z_0)$.
- Bounce diagram: $z$ across, $t$ down; weights $\tau_g$, then $\times\Gamma_L$ and $\times\Gamma_g$ at the ends. Read $V$ at $z_p$ from the crossings of a vertical line; current flips sign on backward segments.
- Any input: weighted, delayed copies of $f_i$. Step input: staircase to $V_0R_L/(R_g+R_L)$ and $V_0/(R_g+R_L)$.
- Next, [[4-transmission-lines/29-bounce-diagram-examples|Lecture 29]]: the notes' worked examples.

Concept pages: [[concepts/bounce-diagram]] · [[concepts/characteristic-impedance]] · [[concepts/telegraphers-equations]] · [[concepts/reflection-and-transmission]] · [[concepts/superposition]].

> [!exam] On exams
> Every spring/fall Exam 3 on hand (SP17–FA23) and the Summer 2020 final has a bounce-diagram problem; Lecture 29 covers the plotting parts. Lecture 28 parts:
> - $\tau_g$, $\Gamma_g$, $\Gamma_L$ from the resistors (SP17 E3 #5a, SP18 E3 #3a, FA23 E3 #3(a)(i)); SP19 E3 #4c–d also asks for the current coefficients, $-\Gamma$.
> - A labelled diagram over a time window (SP17 #5b, SP18 #3b, S20 FE #5a): arrival times, then multiply at each end.
> - Steady state under a step (FA23 #5a–b, SP19 #4g, S20 FE #5d): the DC divider.
> - Inverse problems: $R_g$, $R_L$, $v$ from pulses seen at one point (SP17 #2(v)–(vi), FA23 #4). See the worked problem.

> [!tip] Practice this lecture
> [[practice/28-bounce-diagrams|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/28-bounce-diagrams#281-three-coefficients|28.1 Three coefficients]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 28 (8 pages): the circuit, the load condition and $\Gamma_L$, the KVL at $z = 0$ with $\tau_g$ and its footnote, the two-epoch impulse response, $\Gamma_g$, the bounce diagram, the series and the convolution remark. Rao (2009) §7.4 for cross-checks. This site's own: the conventions box, the all-epoch recursion, $\tau_g = (1-\Gamma_g)/2$, the reading recipe, the DC-limit proof, the terminations table, the examples and figures; numbers checked by an FDTD simulation. One slip in the notes (the sign of a delay, p. 8) is on the errata page.
