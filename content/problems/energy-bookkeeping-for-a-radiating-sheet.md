---
title: "Worked problem — Energy bookkeeping for a radiating sheet"
description: "A sheet on the plane x = 0 carries −ẑ 3u(t)cos(ωt) A/m at 2 MHz inside a dielectric with εr = 2.25. Find the two waves, the power the current injects (J·E on the sheet, instantaneous and averaged), the average Poynting vector on each side, the energy delivered by 3 µs and where it is stored, and when and how fast energy reaches a window 900 m away. Modelled on Summer 2020 HE3 #2(c)–(d), re-parameterized with a new plane, current direction, waveform, frequency, amplitude and medium."
tags: [problem, waves]
---

*Problem · style of Summer 2020 HE3 #2 (parts c–d) · uses [[3-maxwell-and-waves/20-poynting-theorem-and-monochromatic-waves|Lecture 20]], [[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets|Lecture 19]] · concepts: [[concepts/poynting-theorem]], [[concepts/poynting-vector]], [[concepts/current-sheet-radiation]]*

> [!question] Problem
> An infinitesimally thin sheet in the plane $x = 0$ carries the surface current
> $$
> \begin{gathered}
> \mathbf{J}_s(t) = -\hat z\,3\,u(t)\cos(\omega t)\ \ \text{A/m},\\[4pt]
> \omega = 4\pi\times10^6\ \text{rad/s},
> \end{gathered}
> $$
> where $u(t)$ is the unit step: the current is switched on at full strength at $t = 0$. A lossless, non-magnetic dielectric with $\epsilon_r = 2.25$ fills all space on both sides. Use the exam constants $\epsilon_0 = 10^{-9}/(36\pi)$ F/m and $\mu_0 = 4\pi\times10^{-7}$ H/m, so that $c = 3\times10^8$ m/s and $\eta_0 = 120\pi\ \Omega$ exactly.
> (a) Find $v$, $\eta$, $\beta$ and $\lambda$ in the dielectric, and write $\mathbf{E}$ and $\mathbf{H}$ for $x>0$ and $x<0$ at times $t>0$.
> (b) Find $\mathbf{J}_s\cdot\mathbf{E}$ on the sheet for $t>0$, and its time average. What does its sign mean?
> (c) Find the time-averaged Poynting vector on each side, behind the wavefronts, and check the energy balance at the sheet.
> (d) How much energy per square metre of sheet has the current delivered by $t = 3$ µs? Show that all of it is stored in the fields between the two wavefronts.
> (e) A window of area 1 m² stands parallel to the sheet at $x = 900$ m. From what time does energy cross it, and at what average rate after that?

## Before writing anything: the medium

The sheet result of Lecture 19 holds in any homogeneous lossless medium, with that medium's $v$ and $\eta$:

$$
\begin{gathered}
v = \frac{c}{\sqrt{\epsilon_r}} = \frac{3\times10^8}{1.5} = 2\times10^8\ \text{m/s},\\[4pt]
\eta = \frac{\eta_0}{\sqrt{\epsilon_r}} = \frac{120\pi}{1.5} = 80\pi\approx251\ \Omega .
\end{gathered}
$$

The frequency is $f = \omega/2\pi = 2$ MHz, so the period is $T = 0.5$ µs. Then $\beta = \omega/v = 4\pi\times10^6/(2\times10^8) = 0.02\pi\approx0.0628$ rad/m and $\lambda = 2\pi/\beta = v/f = 100$ m.

## (a) The two waves

Apply the recipe of [[3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets#4-the-same-result-from-boundary-conditions-slides|Lecture 19]]: $\mathbf{E} = -\tfrac\eta2\mathbf{J}_s(t - \lvert x\rvert/v)$ and $\mathbf{H} = \tfrac12\mathbf{J}_s(t - \lvert x\rvert/v)\times\hat n$, with $\hat n = +\hat x$ for $x>0$ and $-\hat x$ for $x<0$. Delaying the source by $\lvert x\rvert/v$ turns $\cos\omega t$ into $\cos(\omega t - \beta\lvert x\rvert)$ and $u(t)$ into $u(t - \lvert x\rvert/v)$.

- $\mathbf{E}$: $-\tfrac\eta2(-\hat z\,3) = +\hat z\,\tfrac32\eta = +\hat z\,120\pi$ V/m in amplitude, on both sides. A current along $-\hat z$ gives an $\mathbf{E}$ along $+\hat z$: the field opposes the current.
- $\mathbf{H}$ for $x>0$: $\tfrac12(-\hat z\,3)\times\hat x = -\tfrac32(\hat z\times\hat x) = -1.5\,\hat y$ A/m in amplitude.
- $\mathbf{H}$ for $x<0$: $\tfrac12(-\hat z\,3)\times(-\hat x) = +1.5\,\hat y$ A/m.

> [!key] Answer (a)
> $v = 2\times10^8$ m/s, $\eta = 80\pi\approx251\ \Omega$, $\beta = 0.02\pi$ rad/m, $\lambda = 100$ m, and for $x\gtrless0$
> $$
> \begin{gathered}
> \mathbf{E} = \hat z\,120\pi\,u\Big(t\mp\frac xv\Big)\cos(\omega t\mp\beta x)\ \ \text{V/m},\\[4pt]
> \mathbf{H} = \mp\hat y\,1.5\,u\Big(t\mp\frac xv\Big)\cos(\omega t\mp\beta x)\ \ \text{A/m}.
> \end{gathered}
> $$
> Checks. Direction: $\hat z\times(-\hat y) = +\hat x$ for $x>0$ and $\hat z\times(+\hat y) = -\hat x$ for $x<0$, away from the sheet on both sides ✓. Ratio: $120\pi/1.5 = 80\pi = \eta$ ✓. Jump at the sheet, with region 1 = $x>0$ and $\hat n = \hat x$: $\hat x\times(\mathbf{H}_1 - \mathbf{H}_2) = \hat x\times(-3\,\hat y)\cos\omega t = -\hat z\,3\cos\omega t = \mathbf{J}_s$ ✓.

## (b) The power the current injects

On the sheet $\mathbf{E}$ is the same from both sides (tangential $\mathbf{E}$ is continuous): $\mathbf{E}(0,t) = \hat z\,120\pi\cos\omega t$ for $t>0$. So

$$
\begin{aligned}
\mathbf{J}_s\cdot\mathbf{E} &= \big(-\hat z\,3\cos\omega t\big)\cdot\big(\hat z\,120\pi\cos\omega t\big)\\
&= -360\pi\cos^2(\omega t)\ \ \text{W/m}^2 .
\end{aligned}
$$

With $\langle\cos^2\rangle = \tfrac12$:

> [!key] Answer (b)
> $$
> \begin{gathered}
> \mathbf{J}_s\cdot\mathbf{E} = -360\pi\cos^2\omega t\ \ \text{W/m}^2,\\[4pt]
> \langle\mathbf{J}_s\cdot\mathbf{E}\rangle = -180\pi\approx-565\ \text{W/m}^2 .
> \end{gathered}
> $$
> The peak is $360\pi\approx1131$ W/m². In general $\langle\mathbf{J}_s\cdot\mathbf{E}\rangle = -\eta J_0^2/4$ for a sheet current of amplitude $J_0$. The sign is negative at every instant (except the zeros of $\cos\omega t$), so the sheet is a **source**. Whatever drives the current pushes it against $\mathbf{E}$, and on average it delivers 565 W to every square metre of sheet. That power goes into the field.

> [!trap] Where part (b) loses points
> - The exam calls $\langle\mathbf{J}_s\cdot\mathbf{E}\rangle$ "the average Joule heating rate". At a source that rate is negative. A positive answer means a sign slip in $\mathbf{E}$: $\mathbf{E}$ must oppose $\mathbf{J}_s$.
> - Units: $\mathbf{J}_s\cdot\mathbf{E}$ is (A/m)(V/m) = W/m², power per unit area of sheet, not W/m³.
> - Forgetting the ½ from $\langle\cos^2\rangle$, or using $\eta_0$ instead of the dielectric's $\eta$.

## (c) The average Poynting vector, and the balance

Behind the fronts ($\lvert x\rvert<vt$), part (a) gives

$$
\begin{aligned}
\mathbf{S} &= \big(120\pi\,\hat z\big)\times\big(\mp1.5\,\hat y\big)\cos^2(\omega t\mp\beta x)\\
&= \pm\hat x\,180\pi\cos^2(\omega t\mp\beta x)\ \ \text{W/m}^2 .
\end{aligned}
$$

> [!key] Answer (c)
> $$
> \langle\mathbf{S}\rangle = \pm\hat x\,90\pi\approx\pm\hat x\,283\ \text{W/m}^2\qquad(x\gtrless0),
> $$
> behind the fronts. That is $\eta J_0^2/8$ on each side. **Balance:** $90\pi + 90\pi = 180\pi = \langle-\mathbf{J}_s\cdot\mathbf{E}\rangle$ ✓. It holds at every instant too. At $x = 0^\pm$ each face carries $180\pi\cos^2\omega t$ outward, and the two together equal $-\mathbf{J}_s\cdot\mathbf{E} = 360\pi\cos^2\omega t$. That is the sheet form of Poynting's theorem, $\hat n\cdot(\mathbf{S}_1 - \mathbf{S}_2) = -\mathbf{J}_s\cdot\mathbf{E}$ ([[3-maxwell-and-waves/20-poynting-theorem-and-monochromatic-waves#6-the-notes-example-monochromatic-waves-from-a-cosine-sheet|Lecture 20 §6]]).

## (d) The energy delivered by 3 µs, and where it is

**Delivered.** By $t = 3$ µs the current has run for exactly 6 periods. Over whole periods $\int\cos^2\omega t\,dt = t/2$, so per square metre of sheet

$$
\begin{aligned}
W_{\text{in}} &= \int_0^{3\ \mu\text{s}}(-\mathbf{J}_s\cdot\mathbf{E})\,dt\\
&= 360\pi\times\frac{3\times10^{-6}}{2}\ \text{J/m}^2\\
&= 540\pi\ \mu\text{J/m}^2\approx1.70\ \text{mJ/m}^2 ,
\end{aligned}
$$

which is also $\langle-\mathbf{J}_s\cdot\mathbf{E}\rangle\times3\ \mu\text{s} = 180\pi\times3\times10^{-6}$.

**Where it is.** At 3 µs the fronts are at $\lvert x\rvert = vt = 600$ m, and nothing has reached beyond them. Apply the integral form of Poynting's theorem to a box of unit cross-section with faces at $x = \pm L$, beyond the fronts ($L>600$ m). On those faces $\mathbf{S}$ has been zero all along, and the only exchange inside is at the sheet. So $dW/dt = -\mathbf{J}_s\cdot\mathbf{E}$ at every instant: everything the current has delivered is still stored in the box, all of it in the region $\lvert x\rvert<600$ m.

**Check by integrating $w$.** For a single travelling wave $w_e = w_m$, so $w = \epsilon E^2 = \epsilon(120\pi)^2\cos^2(\omega t - \beta\lvert x\rvert)$. With $\epsilon = 2.25\epsilon_0 = 10^{-9}/(16\pi)$ F/m, the average density is

$$
\begin{aligned}
\langle w\rangle = \tfrac12\epsilon E_0^2 &= \tfrac12\cdot\frac{10^{-9}}{16\pi}\cdot(120\pi)^2\ \text{J/m}^3\\
&= 450\pi\times10^{-9}\ \text{J/m}^3\approx1.41\ \mu\text{J/m}^3 .
\end{aligned}
$$

At $t = 3$ µs, $\omega t = 12\pi$, so $\cos^2(\omega t - \beta x) = \cos^2(\beta x)$. The 600 m on each side hold exactly 6 wavelengths, over which $\cos^2$ averages to ½. Each side therefore holds $\langle w\rangle\times600\ \text{m} = 270\pi\ \mu$J/m², and the two sides together hold $540\pi\ \mu\text{J/m}^2\approx1.70$ mJ/m² ✓.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 500" width="640" height="500" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px"><defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker><marker id="ahs" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs><text x="20.0" y="22.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;font-weight:600;">1  Energy density w(x) at t = 3 µs  (w<tspan baseline-shift="sub" style="font-size:9px">e</tspan> = w<tspan baseline-shift="sub" style="font-size:9px">m</tspan>, so w = εE²)</text><text x="20.0" y="40.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">dashed: the cycle average ⟨w⟩ = εE₀²/2 = 1.41 µJ/m³, half the peak</text><line x1="338.0" y1="51.0" x2="338.0" y2="206.0" stroke="var(--hi)" stroke-width="2" stroke-dasharray="4 3" stroke-linecap="round"/><line x1="56.0" y1="206.0" x2="622.0" y2="206.0" stroke="currentColor" stroke-width="1.3" marker-end="url(#ah)" stroke-linecap="round"/><text x="626.0" y="210.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">x</text><line x1="139.0" y1="203.0" x2="139.0" y2="209.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><line x1="238.5" y1="203.0" x2="238.5" y2="209.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><line x1="338.0" y1="203.0" x2="338.0" y2="209.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><line x1="437.5" y1="203.0" x2="437.5" y2="209.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><line x1="537.0" y1="203.0" x2="537.0" y2="209.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="139.0" y="222.0" text-anchor="middle" fill="var(--muted)" style="font-size:10px;">−600</text><text x="238.5" y="222.0" text-anchor="middle" fill="var(--muted)" style="font-size:10px;">−300</text><text x="338.0" y="222.0" text-anchor="middle" fill="var(--muted)" style="font-size:10px;">0</text><text x="437.5" y="222.0" text-anchor="middle" fill="var(--muted)" style="font-size:10px;">300</text><text x="537.0" y="222.0" text-anchor="middle" fill="var(--muted)" style="font-size:10px;">600</text><text x="624.0" y="222.0" text-anchor="start" fill="var(--muted)" style="font-size:10.5px;">m</text><path d="M338.0,70.0 L338.9,74.0 L339.8,85.4 L344.2,185.1 L345.3,200.8 L346.3,206.0 L347.2,202.4 L348.1,191.2 L352.4,91.6 L353.5,75.6 L354.1,71.4 L354.6,70.0 L355.5,74.1 L356.4,85.6 L360.7,183.6 L361.8,200.0 L362.8,205.9 L363.2,205.5 L363.7,203.0 L364.7,191.0 L369.0,91.4 L370.1,75.5 L370.7,71.3 L371.2,70.0 L372.1,74.2 L373.0,85.8 L377.3,183.9 L378.4,200.1 L379.4,205.9 L379.8,205.4 L380.3,202.9 L381.3,190.8 L385.6,91.2 L386.7,75.3 L387.2,71.3 L387.8,70.0 L388.7,74.3 L389.6,86.0 L393.9,184.1 L394.9,199.3 L395.9,205.8 L396.3,205.6 L396.9,202.8 L397.9,190.6 L402.2,90.9 L403.3,75.2 L404.3,70.0 L405.2,73.6 L406.2,86.2 L410.4,182.6 L411.4,198.4 L412.4,205.7 L412.8,205.8 L413.4,203.4 L414.4,191.9 L418.8,90.7 L419.9,75.1 L420.9,70.0 L421.4,70.9 L421.9,74.5 L422.9,88.0 L426.9,181.1 L427.8,196.3 L428.7,204.7 L429.2,206.0 L429.8,204.4 L430.9,193.1 L435.4,90.5 L436.5,75.0 L437.5,70.0 L438.0,71.3 L438.6,75.5 L439.7,91.5 L444.1,192.5 L445.1,203.7 L445.7,205.9 L446.1,205.5 L447.1,197.9 L448.1,181.8 L452.2,87.0 L453.2,74.0 L454.1,70.0 L454.6,71.4 L455.2,75.6 L456.3,91.7 L460.6,191.3 L461.6,203.1 L462.2,205.8 L462.6,205.7 L463.6,198.8 L464.6,183.3 L468.8,86.8 L469.8,73.9 L470.7,70.0 L471.7,74.9 L472.8,90.3 L477.2,191.5 L478.2,203.2 L478.7,205.5 L479.1,205.9 L480.1,199.7 L481.2,183.1 L485.4,86.6 L486.4,73.8 L487.3,70.0 L488.2,74.1 L489.2,87.3 L493.3,182.0 L494.3,198.0 L495.3,205.6 L495.7,205.9 L496.3,203.6 L497.3,192.3 L501.7,91.3 L502.8,75.4 L503.3,71.3 L503.9,70.0 L504.9,75.1 L506.0,90.7 L510.5,193.3 L511.6,204.5 L512.1,206.0 L512.7,204.6 L513.6,196.1 L514.5,180.8 L518.5,87.8 L519.5,74.4 L520.0,70.8 L520.5,70.0 L521.5,75.2 L522.6,90.9 L526.9,190.6 L527.9,202.8 L528.4,205.4 L528.8,206.0 L529.8,200.3 L530.9,184.1 L535.2,86.0 L536.1,74.3 L537.0,70.0 L537.0,206.0 L610.0,206.0" fill="none" stroke="var(--accent2)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/><path d="M338.0,70.0 L337.1,74.0 L336.2,85.4 L331.8,185.1 L330.7,200.8 L329.7,206.0 L328.8,202.4 L327.9,191.2 L323.6,91.6 L322.5,75.6 L321.9,71.4 L321.4,70.0 L320.5,74.1 L319.6,85.6 L315.3,183.6 L314.2,200.0 L313.2,205.9 L312.8,205.5 L312.3,203.0 L311.3,191.0 L307.0,91.4 L305.9,75.5 L305.3,71.3 L304.8,70.0 L303.9,74.2 L303.0,85.8 L298.7,183.9 L297.6,200.1 L296.6,205.9 L296.2,205.4 L295.7,202.9 L294.7,190.8 L290.4,91.2 L289.3,75.3 L288.8,71.3 L288.2,70.0 L287.3,74.3 L286.4,86.0 L282.1,184.1 L281.1,199.3 L280.1,205.8 L279.7,205.6 L279.1,202.8 L278.1,190.6 L273.8,90.9 L272.7,75.2 L271.7,70.0 L270.8,73.6 L269.8,86.2 L265.6,182.6 L264.6,198.4 L263.6,205.7 L263.2,205.8 L262.6,203.4 L261.6,191.9 L257.2,90.7 L256.1,75.1 L255.1,70.0 L254.6,70.9 L254.1,74.5 L253.1,88.0 L249.1,181.1 L248.2,196.3 L247.3,204.7 L246.8,206.0 L246.2,204.4 L245.1,193.1 L240.6,90.5 L239.5,75.0 L238.5,70.0 L238.0,71.3 L237.4,75.5 L236.3,91.5 L231.9,192.5 L230.9,203.7 L230.3,205.9 L229.9,205.5 L228.9,197.9 L227.9,181.8 L223.8,87.0 L222.8,74.0 L221.9,70.0 L221.4,71.4 L220.8,75.6 L219.7,91.7 L215.4,191.3 L214.4,203.1 L213.8,205.8 L213.4,205.7 L212.4,198.8 L211.4,183.3 L207.2,86.8 L206.2,73.9 L205.3,70.0 L204.3,74.9 L203.2,90.3 L198.8,191.5 L197.8,203.2 L197.3,205.5 L196.9,205.9 L195.9,199.7 L194.8,183.1 L190.6,86.6 L189.6,73.8 L188.7,70.0 L187.8,74.1 L186.8,87.3 L182.7,182.0 L181.7,198.0 L180.7,205.6 L180.3,205.9 L179.7,203.6 L178.7,192.3 L174.3,91.3 L173.2,75.4 L172.7,71.3 L172.1,70.0 L171.1,75.1 L170.0,90.7 L165.5,193.3 L164.4,204.5 L163.9,206.0 L163.3,204.6 L162.4,196.1 L161.5,180.8 L157.5,87.8 L156.5,74.4 L156.0,70.8 L155.5,70.0 L154.5,75.2 L153.4,90.9 L149.1,190.6 L148.1,202.8 L147.6,205.4 L147.2,206.0 L146.2,200.3 L145.1,184.1 L140.8,86.0 L139.9,74.3 L139.0,70.0 L139.0,206.0 L66.0,206.0" fill="none" stroke="var(--accent2)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/><line x1="139.0" y1="138.0" x2="537.0" y2="138.0" stroke="var(--hi)" stroke-width="1.5" stroke-dasharray="6 4" stroke-linecap="round"/><line x1="66.0" y1="206.0" x2="66.0" y2="53.7" stroke="currentColor" stroke-width="1.2" marker-end="url(#ah)" stroke-linecap="round"/><text x="71.0" y="57.7" text-anchor="start" fill="currentColor" style="font-size:12px;">µJ/m³</text><line x1="63.0" y1="206.0" x2="69.0" y2="206.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="60.0" y="210.0" text-anchor="end" fill="var(--muted)" style="font-size:10.5px;">0</text><line x1="63.0" y1="138.0" x2="69.0" y2="138.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="60.0" y="142.0" text-anchor="end" fill="var(--muted)" style="font-size:10.5px;">1.41</text><line x1="63.0" y1="70.0" x2="69.0" y2="70.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="60.0" y="74.0" text-anchor="end" fill="var(--muted)" style="font-size:10.5px;">2.83</text><text x="543.0" y="89.0" text-anchor="start" fill="var(--accent2)" style="font-size:10.5px;">front</text><text x="543.0" y="102.0" text-anchor="start" fill="var(--accent2)" style="font-size:10.5px;">x = vt</text><text x="133.0" y="89.0" text-anchor="end" fill="var(--accent2)" style="font-size:10.5px;">front</text><text x="133.0" y="102.0" text-anchor="end" fill="var(--accent2)" style="font-size:10.5px;">x = −vt</text><text paint-order="stroke" stroke="var(--paper)" stroke-width="4" stroke-linejoin="round" x="343.0" y="56.4" text-anchor="start" fill="var(--hi)" style="font-size:10.5px;">sheet</text><text x="20.0" y="268.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;font-weight:600;">2  Energy per m² of sheet, 0 to 3 µs</text><line x1="72.0" y1="452.0" x2="392.0" y2="452.0" stroke="currentColor" stroke-width="1.3" marker-end="url(#ah)" stroke-linecap="round"/><text x="396.0" y="456.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">t</text><line x1="82.0" y1="449.0" x2="82.0" y2="455.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><line x1="181.3" y1="449.0" x2="181.3" y2="455.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><line x1="280.7" y1="449.0" x2="280.7" y2="455.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><line x1="380.0" y1="449.0" x2="380.0" y2="455.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="82.0" y="468.0" text-anchor="middle" fill="var(--muted)" style="font-size:10px;">0</text><text x="181.3" y="468.0" text-anchor="middle" fill="var(--muted)" style="font-size:10px;">1</text><text x="280.7" y="468.0" text-anchor="middle" fill="var(--muted)" style="font-size:10px;">2</text><text x="380.0" y="468.0" text-anchor="middle" fill="var(--muted)" style="font-size:10px;">3</text><text x="394.0" y="468.0" text-anchor="start" fill="var(--muted)" style="font-size:10.5px;">µs</text><line x1="82.0" y1="452.0" x2="82.0" y2="282.9" stroke="currentColor" stroke-width="1.2" marker-end="url(#ah)" stroke-linecap="round"/><text x="87.0" y="286.9" text-anchor="start" fill="currentColor" style="font-size:12px;">mJ/m²</text><line x1="79.0" y1="452.0" x2="85.0" y2="452.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="76.0" y="456.0" text-anchor="end" fill="var(--muted)" style="font-size:10.5px;">0</text><line x1="79.0" y1="406.3" x2="85.0" y2="406.3" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="76.0" y="410.3" text-anchor="end" fill="var(--muted)" style="font-size:10.5px;">0.5</text><line x1="79.0" y1="360.6" x2="85.0" y2="360.6" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="76.0" y="364.6" text-anchor="end" fill="var(--muted)" style="font-size:10.5px;">1.0</text><line x1="79.0" y1="314.9" x2="85.0" y2="314.9" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="76.0" y="318.9" text-anchor="end" fill="var(--muted)" style="font-size:10.5px;">1.5</text><path d="M82.0,452.0 L86.0,448.2 L89.0,446.4 L91.7,445.6 L97.9,445.3 L101.1,444.1 L104.1,441.8 L110.3,435.7 L113.3,433.7 L116.3,432.8 L122.7,432.4 L125.7,431.3 L128.7,429.1 L135.1,422.8 L138.1,420.7 L141.1,419.8 L147.6,419.5 L150.5,418.4 L153.5,416.2 L160.0,409.8 L163.0,407.8 L165.9,406.9 L172.4,406.5 L175.4,405.5 L178.4,403.3 L184.8,396.9 L187.8,394.9 L190.8,394.0 L197.2,393.6 L200.0,392.7 L202.7,390.8 L209.1,384.4 L212.4,382.1 L215.6,381.1 L222.1,380.7 L224.8,379.7 L227.5,377.8 L234.0,371.5 L237.2,369.2 L239.9,368.2 L246.4,367.8 L249.6,366.8 L252.4,364.9 L258.8,358.6 L262.0,356.2 L265.3,355.2 L271.7,354.8 L274.5,353.9 L277.2,352.0 L283.6,345.6 L286.9,343.3 L290.1,342.3 L296.6,341.9 L299.3,341.0 L302.5,338.6 L309.0,332.3 L311.7,330.4 L314.4,329.4 L320.9,329.1 L324.1,328.0 L326.9,326.1 L333.3,319.8 L336.5,317.5 L339.3,316.5 L345.7,316.1 L348.7,315.2 L351.7,313.2 L357.9,307.1 L360.9,304.8 L364.1,303.6 L370.3,303.2 L373.0,302.5 L376.0,300.7 L380.0,296.9" fill="none" stroke="var(--hi)" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"/><circle cx="106.8" cy="439.1" r="3.6" fill="var(--accent2)" stroke="none" stroke-width="1.5"/><circle cx="131.7" cy="426.1" r="3.6" fill="var(--accent2)" stroke="none" stroke-width="1.5"/><circle cx="156.5" cy="413.2" r="3.6" fill="var(--accent2)" stroke="none" stroke-width="1.5"/><circle cx="181.3" cy="400.3" r="3.6" fill="var(--accent2)" stroke="none" stroke-width="1.5"/><circle cx="206.2" cy="387.4" r="3.6" fill="var(--accent2)" stroke="none" stroke-width="1.5"/><circle cx="231.0" cy="374.4" r="3.6" fill="var(--accent2)" stroke="none" stroke-width="1.5"/><circle cx="255.8" cy="361.5" r="3.6" fill="var(--accent2)" stroke="none" stroke-width="1.5"/><circle cx="280.7" cy="348.6" r="3.6" fill="var(--accent2)" stroke="none" stroke-width="1.5"/><circle cx="305.5" cy="335.7" r="3.6" fill="var(--accent2)" stroke="none" stroke-width="1.5"/><circle cx="330.3" cy="322.7" r="3.6" fill="var(--accent2)" stroke="none" stroke-width="1.5"/><circle cx="355.2" cy="309.8" r="3.6" fill="var(--accent2)" stroke="none" stroke-width="1.5"/><circle cx="380.0" cy="296.9" r="3.6" fill="var(--accent2)" stroke="none" stroke-width="1.5"/><text x="96.9" y="303.9" text-anchor="start" fill="var(--hi)" style="font-size:11px;font-weight:600;">line: delivered by the current, ∫(−J<tspan baseline-shift="sub" style="font-size:9px">s</tspan>·E) dt</text><text x="96.9" y="319.4" text-anchor="start" fill="var(--accent2)" style="font-size:11px;font-weight:600;">dots: stored in |x| &lt; vt, ∫w dx</text><text x="380.0" y="288.6" text-anchor="middle" fill="var(--hi)" style="font-size:10.5px;">1.70</text><text x="520.0" y="268.0" text-anchor="middle" fill="currentColor" style="font-size:11.5px;font-weight:600;">fields next to the sheet</text><text x="520.0" y="283.0" text-anchor="middle" fill="currentColor" style="font-size:11.5px;font-weight:600;">while cos ωt &gt; 0</text><line x1="520.0" y1="308.0" x2="520.0" y2="412.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="520.0" y1="320.0" x2="520.0" y2="350.0" stroke="var(--hi)" stroke-width="1.6" marker-end="url(#ahs)" stroke-linecap="round"/><line x1="520.0" y1="364.0" x2="520.0" y2="394.0" stroke="var(--hi)" stroke-width="1.6" marker-end="url(#ahs)" stroke-linecap="round"/><text x="520.0" y="426.0" text-anchor="middle" fill="var(--hi)" style="font-size:10.5px;">J<tspan baseline-shift="sub" style="font-size:9px">s</tspan> along −ẑ</text><line x1="550.0" y1="382.0" x2="550.0" y2="338.0" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#ahs)" stroke-linecap="round"/><text x="550.0" y="398.0" text-anchor="middle" fill="var(--accent)" style="font-size:11px;font-weight:700;">E</text><line x1="490.0" y1="382.0" x2="490.0" y2="338.0" stroke="var(--accent)" stroke-width="2.2" marker-end="url(#ahs)" stroke-linecap="round"/><text x="490.0" y="398.0" text-anchor="middle" fill="var(--accent)" style="font-size:11px;font-weight:700;">E</text><circle cx="578.0" cy="360.0" r="6.0" fill="none" stroke="var(--accent2)" stroke-width="1.4"/><circle cx="578.0" cy="360.0" r="1.8" fill="var(--accent2)" stroke="none" stroke-width="1.5"/><circle cx="462.0" cy="360.0" r="6.0" fill="none" stroke="var(--accent2)" stroke-width="1.4"/><line x1="458.3" y1="356.3" x2="465.7" y2="363.7" stroke="var(--accent2)" stroke-width="1.4" stroke-linecap="round"/><line x1="458.3" y1="363.7" x2="465.7" y2="356.3" stroke="var(--accent2)" stroke-width="1.4" stroke-linecap="round"/><text x="578.0" y="382.0" text-anchor="middle" fill="var(--accent2)" style="font-size:11px;font-weight:700;">H</text><text x="462.0" y="382.0" text-anchor="middle" fill="var(--accent2)" style="font-size:11px;font-weight:700;">H</text><line x1="590.0" y1="330.0" x2="624.0" y2="330.0" stroke="currentColor" stroke-width="2.2" marker-end="url(#ahs)" stroke-linecap="round"/><line x1="450.0" y1="330.0" x2="416.0" y2="330.0" stroke="currentColor" stroke-width="2.2" marker-end="url(#ahs)" stroke-linecap="round"/><text x="607.0" y="322.0" text-anchor="middle" fill="currentColor" style="font-size:11px;font-weight:700;">S</text><text x="433.0" y="322.0" text-anchor="middle" fill="currentColor" style="font-size:11px;font-weight:700;">S</text><line x1="458.0" y1="468.0" x2="484.0" y2="468.0" stroke="currentColor" stroke-width="1.3" marker-end="url(#ahs)" stroke-linecap="round"/><text x="488.0" y="472.0" text-anchor="start" fill="currentColor" style="font-size:11px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">x</text><line x1="458.0" y1="468.0" x2="458.0" y2="442.0" stroke="currentColor" stroke-width="1.3" marker-end="url(#ahs)" stroke-linecap="round"/><text x="463.0" y="446.0" text-anchor="start" fill="currentColor" style="font-size:11px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">z</text><circle cx="458.0" cy="468.0" r="4.5" fill="none" stroke="currentColor" stroke-width="1.4"/><line x1="455.2" y1="465.2" x2="460.8" y2="470.8" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/><line x1="455.2" y1="470.8" x2="460.8" y2="465.2" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/><text x="450.0" y="472.0" text-anchor="end" fill="currentColor" style="font-size:11px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">y</text><text x="502.0" y="472.0" text-anchor="start" fill="var(--muted)" style="font-size:10px;">(y into the page)</text></svg><figcaption><strong>The worked problem's energy ledger at t = 3 µs.</strong> A sheet on x = 0 carries <b>J</b><sub>s</sub> = −ẑ 3u(t)cos(ωt) A/m at 2 MHz in a dielectric with ε<sub>r</sub> = 2.25 (v = 200 m/µs, λ = 100 m). Panel 1, computed from w = εE<sup>2</sup> with E = (ηJ<sub>0</sub>/2)cos(ωt − β|x|): the field fills |x| &lt; 600 m, twelve humps of energy density per side, and nothing has reached beyond the fronts. Averaged over a cycle the density is 1.41 µJ/m³ (dashed). Panel 2: the energy the current has given up, the integral of −<b>J</b><sub>s</sub>·<b>E</b> (line), and the energy found by integrating w over the region the waves have reached (dots) are the same at every instant: 1.70 mJ per square metre of sheet at 3 µs. That is Poynting's theorem in integral form for a box whose faces lie beyond the fronts, where <b>S</b> = 0. The icon shows the directions while cos ωt &gt; 0, when the current points down (−ẑ): <b>E</b> up (+ẑ, opposite to the current) on both sides, <b>H</b> = −ŷ (⊙) on the right and +ŷ (⊗) on the left, and <b>S</b> = <b>E</b> × <b>H</b> pointing away from the sheet.</figcaption></figure>

> [!key] Answer (d)
> $W_{\text{in}} = 540\pi\ \mu$J/m² $\approx1.70$ mJ per square metre of sheet, stored as field energy between the two fronts at $x = \pm600$ m, $270\pi\ \mu$J/m² $\approx0.85$ mJ/m² on each side. The equality is not special to whole periods. At any $t$, both sides together hold $\tfrac12\eta J_0^2\big[t/2 + \sin(2\omega t)/(4\omega)\big]$, which is exactly $\int_0^t(-\mathbf{J}_s\cdot\mathbf{E})\,dt$ (panel 2 of the figure). Note also $\langle S\rangle/\langle w\rangle = 90\pi/(450\pi\times10^{-9}) = 2\times10^8$ m/s $= v$: the energy moves out at the wave speed.

## (e) The window at x = 900 m

The front left the sheet at $t = 0$ and travels at $v$, so it reaches $x = 900$ m at $t = 900/(2\times10^8) = 4.5$ µs. Before that, $\mathbf{S} = 0$ there. After that the window sees the steady oscillation, with $\langle\mathbf{S}\rangle = +\hat x\,90\pi$ W/m² along its normal.

> [!key] Answer (e)
> Energy first crosses the window at $t = 4.5$ µs. From then on it crosses at an average rate of $90\pi\times1\ \text{m}^2\approx283$ W, in pulses at $2f = 4$ MHz: the instantaneous rate is $180\pi\cos^2(\omega t - \beta\cdot900\ \text{m})$ W, between 0 and 565 W.

## Variant: the same sheet in vacuum

Remove the dielectric. Then $\eta = 120\pi\ \Omega$ and $v = 3\times10^8$ m/s. $\mathbf{H}$ keeps its amplitude of 1.5 A/m, because it is set by the jump $J_s$ whatever the medium. $\mathbf{E}$ grows to $180\pi\approx565$ V/m, the average flux on each side to $135\pi\approx424$ W/m², and the injected power to $270\pi\approx848$ W/m². With the same current, a higher-impedance medium takes more power from the sheet, just as a current source delivers $I^2R$ to a larger resistor.

## The pattern behind this problem

$$
\begin{gathered}
\langle-\mathbf{J}_s\cdot\mathbf{E}\rangle = \frac{\eta J_0^2}{4},\\[4pt]
\langle S\rangle_{\text{each side}} = \frac{\eta J_0^2}{8},\\[4pt]
W_{\text{stored}} = \int_0^t(-\mathbf{J}_s\cdot\mathbf{E})\,dt ,
\end{gathered}
$$

where $W_{\text{stored}}$ is the field energy between the two fronts, per square metre of sheet.

Write the fields with the Lecture 19 recipe, take $\mathbf{J}_s\cdot\mathbf{E}$ on the sheet (negative: a source), average with $\langle\cos^2\rangle = \tfrac12$, and split the injected power equally between the two sides. When the source has been on for a finite time, a box whose faces lie beyond the fronts shows that everything delivered is still stored. The exam instance (Summer 2020 HE3 #2) puts a sine current along $\hat y$ on the plane $z = 0$ in free space, and asks for the average of $\mathbf{J}_s\cdot\mathbf{E}$ and the average power per unit area carried into $z>0$, as numbers.
