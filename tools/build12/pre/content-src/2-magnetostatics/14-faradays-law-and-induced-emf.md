---
title: "Lecture 14 — Faraday's law and induced emf"
description: "∇×E = −∂B/∂t: around any closed path the emf ℰ = ∮(E + v×B)·dl equals minus the rate of change of the linked flux, whether B changes, the loop moves or deforms, or it moves through a nonuniform field. Lenz's rule fixes the sign, I = ℰ/R gives the current, and six examples show the new path-dependent 'voltage' — including why two voltmeters on the same nodes can disagree."
tags: [lecture, magnetostatics]
lecture: 14
---

*Lecture 14 · course notes §14 · slides "Faraday's Law" · prev: [[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential|Lecture 13]] · next: [[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials|Lecture 15]] · practice: [[practice/14-faradays-law-and-induced-emf|12 problems]]*

> [!abstract] In one breath
> A time-varying magnetic field makes an electric field that **circulates**, $\nabla\times\mathbf{E} = -\partial\mathbf{B}/\partial t$, so voltage is no longer path-independent. Around a loop $C$ this is the flux rule $\mathcal{E} = -d\Psi/dt$: the **emf** $\mathcal{E}$ is the work per unit charge done by $\mathbf{E}+\mathbf{v}\times\mathbf{B}$ once around $C$, and $\Psi = \int\mathbf{B}\cdot d\mathbf{S}$ is the linked flux. *Why* $\Psi$ changes does not matter; the minus sign (Lenz) makes the induced current fight the change. A conducting loop carries $I = \mathcal{E}/R$, a moving bar becomes a battery, and a voltmeter reads $\int\mathbf{E}\cdot d\mathbf{l}$ *along its own leads* — so two meters on the same nodes can disagree.

## 1. The law, and the flux it is about

<!-- fig:faraday-flux-rule -->

> [!key] Faraday's law
> $$
> \nabla\times\mathbf{E} = -\frac{\partial\mathbf{B}}{\partial t}\qquad\Longleftrightarrow\qquad \oint_C\mathbf{E}\cdot d\mathbf{l} = -\int_S\frac{\partial\mathbf{B}}{\partial t}\cdot d\mathbf{S},
> $$
> for every surface $S$ bounded by every closed, **directed** path $C$, $d\mathbf{S}$ tied to the sense of $C$ by the right-hand rule (the Stokes convention of [[1-electrostatics/06-circulation-and-boundary-conditions|Lecture 6]]). It holds at all points, in all frames. Field definitions unchanged: $\mathbf{E}$ is force per unit *stationary* charge, $\mathbf{B}$ gives the extra $\mathbf{v}\times\mathbf{B}$ per unit moving charge, in whatever frame you use ([[concepts/lorentz-force]]).

The right side is built from the **magnetic flux linking $C$**,

$$
\Psi\equiv\int_S\mathbf{B}\cdot d\mathbf{S}\quad[\text{Wb} = \text{T·m}^2],
$$

the same for every surface spanning $C$ because $\nabla\cdot\mathbf{B} = 0$ (two such surfaces form a closed surface with zero net flux — [[1-electrostatics/03-gauss-law-at-work#6-the-magnetic-counterpart--bds--0|Lecture 3 §6]]). The contributing field lines thread the loop like links of a chain, hence "linking". For a loop **fixed** in the measurement frame, $d/dt$ comes outside the integral:

$$
\oint_C\mathbf{E}\cdot d\mathbf{l} = -\frac{d}{dt}\int_S\mathbf{B}\cdot d\mathbf{S} = -\frac{d\Psi}{dt}.
$$

## 2. Moving loops, the emf, and Lenz

If $C$ moves or deforms, $d/dt$ and $\int_S$ no longer commute: part of $d\Psi/dt$ comes from the loop sweeping through the field. The notes (margin, p. 2) show the extra piece is a circulation of $\mathbf{v}\times\mathbf{B}$:

> [!derivation]- The swept band (course notes, Lecture 14 margin)
> Let $S$ span $C$ at time 0 and $C(\Delta t)$ be the displaced loop, each point moved by $\mathbf{v}\Delta t$. The band $\delta S$ swept between $C$ and $C(\Delta t)$ has area elements $d\mathbf{S} = \Delta t\,\mathbf{v}\times d\mathbf{l}$. Spanning $C(\Delta t)$ by $S\cup\delta S$:
> $$
> \frac{\Psi(\Delta t)-\Psi(0)}{\Delta t} = \int_S\frac{\mathbf{B}(\mathbf{r},\Delta t)-\mathbf{B}(\mathbf{r},0)}{\Delta t}\cdot d\mathbf{S} + \oint_C\mathbf{B}\cdot(\mathbf{v}\times d\mathbf{l}),
> $$
> and since $\mathbf{B}\cdot(\mathbf{v}\times d\mathbf{l}) = -(\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l}$ (both the volume of the parallelepiped on $d\mathbf{l}$, $\mathbf{v}$, $\mathbf{B}$, up to sign),
> $$
> \frac{d\Psi}{dt} = \int_S\frac{\partial\mathbf{B}}{\partial t}\cdot d\mathbf{S} - \oint_C(\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l}.
> $$
> $\mathbf{v}$ may vary around $C$ — the loop may stretch or rotate.

With Faraday's law, the form that covers every case:

> [!key] The flux rule, and the emf
> $$
> \boxed{\ \mathcal{E}\equiv\oint_C(\mathbf{E}+\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l} = -\frac{d\Psi}{dt}\ }
> $$
> The left side is the **work per unit charge** done by the Lorentz force on a charge carried once around the directed path $C$ ($\mathbf{v}$ = velocity of the path; a charge's own velocity *along* the path adds nothing, since $(\mathbf{v}_q\times\mathbf{B})\cdot d\mathbf{l} = 0$ when $\mathbf{v}_q\parallel d\mathbf{l}$). Faraday's name, **electromotive force** $\mathcal{E}$, is poor: it is work per charge (volts), not a force. A conducting loop of resistance $R$ carries
> $$
> I = \frac{\mathcal{E}}{R}
> $$
> in the circulation direction (for $\mathcal{E}>0$): inside the wire $\mathbf{J} = \sigma(\mathbf{E}+\mathbf{v}\times\mathbf{B})$, as in a battery-driven resistor, and integrating around a homogeneous loop gives $I\cdot(\text{length}/\sigma A) = \mathcal{E}$.

**Reading it as a circuit.** $RI = -d\Psi/dt$ is KVL for the loop: $RI$ is the sum of voltage **drops** in the direction of $C$, $-d\Psi/dt$ a voltage **rise** in the same direction — a source. Since Maxwell, "emf" means any *source of energy* driving current around a resistive loop: a battery, or a changing linked flux. A non-conducting path has an emf too; it drives no current.

> [!key] Lenz's rule, and the three ways to change Ψ
> The minus sign makes the induced current's field **oppose the change** in flux that made it (the opposite sign would make induced currents grow without bound). $-d\Psi/dt\ne0$ whenever
> 1. $C$ is fixed but $\mathbf{B}$ varies in time (transformer action; the emf is all $\oint\mathbf{E}\cdot d\mathbf{l}$);
> 2. $\mathbf{B}$ is constant but $C$ changes — moves, rotates, changes size (generator action; the emf is all $\oint(\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l}$);
> 3. $\mathbf{B}$ is static but *inhomogeneous* and $C$ moves through it (also motional — a loop *translating rigidly* through a *uniform* static field links a constant flux and has no emf).
>
> Case 2 or 3 seen by an observer riding with the loop is case 1: she sees a time-varying $\mathbf{B}'$ and an electric field $\mathbf{E}' = \mathbf{v}\times\mathbf{B}$. Same emf, two descriptions — the (near) invariance of the Lorentz force between slowly moving frames.

Where does the induced $\mathbf{E}$ come from? The notes' first footnote: extending the relativistic argument of [[2-magnetostatics/12-magnetic-force-biot-savart-and-amperes-law|Lecture 12]] to *time-varying* motion, Coulomb interactions require both a time-varying $\mathbf{B}$ and a time-varying $\mathbf{E}$. Faraday's law relates the two fields; the source of both is the changing **current** $\mathbf{J}$, not the changing $\mathbf{B}$ as such.

## 3. Transformer emf: three examples from the lecture

> [!example] Example 1 — a loop in a decaying field
> $\mathbf{B} = B_0e^{-t/\tau}\hat z$; stationary circle of radius $r = 10$ m in $z = 0$, counter-clockwise seen from $+z$, so $d\mathbf{S} = \hat z\,dS$, $\Psi = B_0e^{-t/\tau}\cdot\pi10^2$ Wb and
> $$
> \mathcal{E} = -\frac{d\Psi}{dt} = \pi\,10^2\,\frac{B_0}{\tau}\,e^{-t/\tau}\ \text{V} > 0 .
> $$
> $I = \mathcal{E}/R$ flows counter-clockwise and makes a $+\hat z$ field inside that *props up* the decaying $B_z$. Lenz ✓.

> [!example] Example 2 — a loop receding from a line current, both ways
> Current $I$ along the $x$ axis makes $\mathbf{B} = \dfrac{\mu_0I}{2\pi r}\hat\phi$, which on the $xy$-plane at $y>0$ is $\dfrac{\mu_0I}{2\pi y}\hat z$ ($r$, $\hat\phi$ cylindrical *about the $x$ axis*). A 2 m × 2 m loop, edges along $x$ and $y$, has its centre at $y = 2t$ m ($\mathbf{v} = 2\hat y$ m/s; valid for $t>\tfrac12$ s, loop entirely above the wire). Counter-clockwise $C$, $d\mathbf{S} = \hat z\,dx\,dy$:
> $$
> \begin{gathered}
> \Psi = \int_{-1}^{1}dx\int_{2t-1}^{2t+1}\frac{\mu_0I}{2\pi y}dy = \frac{\mu_0I}{\pi}\ln\frac{2t+1}{2t-1},\\[6pt]
> \mathcal{E} = -\frac{d\Psi}{dt} = \frac{\mu_0I}{\pi}\cdot\frac{4}{(2t+1)(2t-1)} = \frac{\mu_0I}{\pi\,(t^2-\tfrac14)} .
> \end{gathered}
> $$
> Motional route: $\mathbf{v}\times\mathbf{B} = 2\cdot\dfrac{\mu_0I}{2\pi y}\hat x$, so only the edges parallel to $x$ contribute — near edge ($y = 2t-1$, traversed $+\hat x$, length 2) and far edge ($y = 2t+1$, traversed $-\hat x$):
> $$
> \mathcal{E} = \frac{2\mu_0I}{2\pi(2t-1)}\cdot2 - \frac{2\mu_0I}{2\pi(2t+1)}\cdot2 = \frac{\mu_0I}{\pi(t^2-\tfrac14)}\quad\checkmark
> $$
> Lenz: the $+\hat z$ flux falls; the counter-clockwise current's $+\hat z$ field opposes the decrease. [[problems/emf-of-a-loop-moving-near-a-line-current]] re-parameterizes this one.

> [!example] Example 3 — a generator
> A loop of radius $0.1$ m rotates about the $x$ axis at $f = 60$ Hz in constant $\mathbf{B} = 10\hat z$ T; $R = 12\ \Omega$. The flux peaks, $\Psi_0 = \pi(0.1)^2\cdot10 = 0.1\pi$ Wb, with the loop in $z = 0$; $\Psi(t) = \Psi_0\cos\omega t$, $\omega = 120\pi$ rad/s. $\mathcal{E} = -d\Psi/dt = 120\pi\cdot0.1\pi\sin(120\pi t) = 12\pi^2\sin(120\pi t)$ V, $I = \mathcal{E}/R = \pi^2\sin(120\pi t)$ A, about 10 A peak. Case 2 — constant $\mathbf{B}$, moving $C$ — the power grid in one line. (Loop self-inductance neglected; Lecture 15 says when that is allowed.)

## 4. Motional emf: the sliding bar

<!-- fig:rails-motional-emf -->

> [!example] Example 4 — a bar on rails (course notes)
> Perfectly conducting rails 2 m apart, load $R_2$ at $x = 0$, bar of resistance $R_1 = 1\ \Omega$ sliding at $\mathbf{v} = 3\hat x$ m/s, constant $\mathbf{B} = 1\hat y$ T (into the page in the figure's $xz$ view). $C$ counter-clockwise as drawn: up the bar, back along the top rail, down through $R_2$. Right-hand rule: $d\mathbf{S} = -\hat y$, so $\Psi = -1\times2\times3t = -6t$ Wb and $\mathcal{E} = -d\Psi/dt = +6$ V. The motional term alone gives the same: $(\mathbf{v}\times\mathbf{B})_{\text{bar}} = 3\hat x\times1\hat y = 3\hat z$ V/m, times the 2 m bar.
>
> Faraday's law as the sum of the two resistive pieces (perfect rails: $\mathbf{E}\cdot d\mathbf{l} = 0$ along them):
> $$
> \int_{\text{bar}}(\mathbf{E}+\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l} + \int_{R_2}\mathbf{E}\cdot d\mathbf{l} = 6\ \text{V}.
> $$
> The $\mathbf{v}\times\mathbf{B}$ integral is already 6 V, so the $\mathbf{E}$ integrals cancel: $(E_{z,\text{bar}} - E_{z,R_2})\times2 = 0$ — **the lab electric field is the same in the moving bar as in the stationary load.** With $\mathbf{B}$ constant, $\nabla\times\mathbf{E} = -\partial\mathbf{B}/\partial t = 0$: the lab $\mathbf{E}$ is the curl-free, quasi-static Coulomb field of charge piled up on the rails.
> - $R_2 = 2\ \Omega$: $I = 6/3 = 2$ A; 2 V across the bar, 4 V across the load. Bar: $(E_z + 3)\cdot2 = 2\Rightarrow E_z = -2$ V/m; load: $-2E_z = 4\Rightarrow E_z = -2$ V/m ✓.
> - $R_2 = \infty$ (open): $I = 0$; all 6 V across the gap, $E_z = -3$ V/m everywhere, and in the bar $\mathbf{E} + \mathbf{v}\times\mathbf{B} = 0$ exactly, as it must with no current.
>
> Circuit picture: the bar is a **battery of emf $vB\ell = 6$ V with internal resistance $R_1$**, $+$ terminal at the top (where $\mathbf{v}\times\mathbf{B}$ pushes positive charge). [[problems/sliding-bar-and-the-voltmeter-readings]] reworks it with new numbers.

## 5. When voltage stops being a number: the voltmeter paradox

<!-- fig:voltmeter-paradox -->

> [!example] Example 5 — a loop around a solenoid
> A long solenoid with linearly ramping current, so $-d\Psi/dt = 8$ V constant, passes through a small loop of a 1 Ω resistor (right) and a 3 Ω resistor (left) in series. $I_c = 8\ \text{V}/4\ \Omega = 2$ A; drops of 2 V and 6 V in the direction of the current. From the notes:
> - no battery; the loop is excited *inductively*;
> - a voltmeter across the resistors reads 2 V or 6 V depending on whether its probes pass **right or left of the solenoid**: $\mathbf{E}$ outside the solenoid is not conservative *around* it, so $\int\mathbf{E}\cdot d\mathbf{l}$ between the nodes depends on the path;
> - with constant $dI/dt$ the exterior $\mathbf{E}$ is time-independent and $\mathbf{B}$ at the loop is zero: the emf comes from the changing solenoid current, not a changing local $\mathbf{B}$. $\mathcal{E} = -d\Psi/dt$ is the bookkeeping, not the mechanism.

> [!example] Example 6 — the same loop, dissected
> Square loop, area 1 m², $R_1 = 2\ \Omega$ on one side, $R_2 = 1\ \Omega$ on the opposite side, in $\mathbf{B} = (12-3t)\hat z$ T; nodes A and B at opposite corners. $\Psi = 12-3t$ Wb, $\mathcal{E} = 3$ V, $I = 3/3 = 1$ A counter-clockwise. A to B along the $R_1$ side goes *with* the current: drop $V_1 = +2$ V. Along the $R_2$ side, *against* it: $V_2 = -1$ V. They differ by $3$ V, the loop emf. A voltmeter from A (red lead) to B reads 2 V with leads along the $R_1$ path, $-1$ V along the $R_2$ path, $+0.5$ V along the diagonal: the triangle of diagonal and $R_2$ side encloses half the area, so Faraday gives $1.5\ \text{V} = V_{\text{meter}} + 1\ \text{V}$.

> [!trap] "Voltage" in the presence of a changing flux
> In a time-varying magnetic field the *voltage of a path* $P$, $\int_P(\mathbf{E}+\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l}$ (just $\int_P\mathbf{E}\cdot d\mathbf{l}$ for a stationary path), **depends on the path**; there is no "voltage between A and B". A voltmeter displays the voltage of *its own path*, its probe wires from red lead to black; two meters on the same nodes with differently routed leads differ by the emf of the loop their leads enclose ($-d\Psi/dt$ through it). This deliberately demolishes [[1-electrostatics/05-curl-free-fields-and-the-electrostatic-potential#4-path-independence|Lecture 5 §4]]. Circuit theory survives because in a well-designed circuit the flux through the wiring is negligible — or lumped into an inductor.

## 6. Summary

- $\nabla\times\mathbf{E} = -\partial\mathbf{B}/\partial t$; $\oint_C\mathbf{E}\cdot d\mathbf{l} = -\int_S\partial_t\mathbf{B}\cdot d\mathbf{S}$, $C$ and $d\mathbf{S}$ by the right-hand rule.
- $\Psi = \int_S\mathbf{B}\cdot d\mathbf{S}$ [Wb], the same for every $S$ on $C$; fixed loop: $\oint\mathbf{E}\cdot d\mathbf{l} = -d\Psi/dt$.
- $\mathcal{E}\equiv\oint(\mathbf{E}+\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l} = -d\Psi/dt$ for any loop; $I = \mathcal{E}/R$; KVL: drop $RI$ = rise $-d\Psi/dt$.
- Lenz: induced current opposes the flux change. Causes: $\mathbf{B}(t)$; moving/rotating/stretching $C$; $C$ moving through nonuniform $\mathbf{B}$.
- Moving bar: emf $vB\ell$, a battery with internal resistance; lab $\mathbf{E}$ static, equal in bar and load.
- Voltage is path-dependent; a voltmeter reads $\int\mathbf{E}\cdot d\mathbf{l}$ along its own leads; readings differ by the emf of the lead loop.

Concept pages: [[concepts/faradays-law]] · [[concepts/electromotive-force]] · [[concepts/magnetic-flux]] · [[concepts/conservative-field]].

> [!exam] On exams
> Three recurring tasks. (1) *Compute an emf*: orient $C$, $d\mathbf{S}$ by the right-hand rule, write $\Psi(t)$, differentiate, state the sign and current direction — for a moving loop, check by $\oint(\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l}$ (Example 2 and the rotating loop are the templates). (2) *Direction only*: Lenz — magnet approaching, loop shrinking, field decaying? Say what the flux does and which field would oppose it. (3) *Bar and voltmeter*: the moving conductor is a battery of emf $vB\ell$; voltmeter readings are path integrals, differing by the emf of the loop the leads form. Points are lost for $d\mathbf{S}$ the wrong way (sign), forgetting the rails contribute nothing, and calling $\mathcal{E}$ a force.

> [!tip] Practice this lecture
> [[practice/14-faradays-law-and-induced-emf|12 practice problems]] — 5 easy, 3 medium, 4 hard — each with a folded hint and a worked solution. Start with [[practice/14-faradays-law-and-induced-emf#141-flux-through-a-tilted-loop|14.1 Flux through a tilted loop]]; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.

### Sources for this page
Kudeki notes, Lecture 14 (differential and integral Faraday; linked flux; moving-contour derivation in the margin; emf as work per charge; $I = G\mathcal{E}$; KVL reading; Lenz and its footnote; three causes, frame change; footnote 1 on the cause of induced $\mathbf{E}$; Examples 1–6 with all numbers). Shao, Lecture 14 slides (conservative-field recap; Lenz demos with magnet, coil, copper ring; disk-vs-bowl surfaces; shrinking-loop challenge; rails as a battery; EMF beside MMF). Slips in the course material: see [[0-toolkit/04-errata-in-the-course-materials|errata]].
