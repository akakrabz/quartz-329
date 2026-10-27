<!-- for concepts/maxwells-equations, from Lecture 01 §2 -->
<!-- The free-space table and the "how to read" paragraph are already on the topic page; below is what Lecture 1 §2 adds:
     the constants, the two consequences as the lecture states them (statics decouple; waves), quasi-statics, and the
     "number to carry around". Add aliases: "quasi-static approximation", "electrically small". -->

**The lecture's table (free space, in E and B rather than D and H).**

| | Divergence equations | Curl equations |
|---|---|---|
| **electric** | $\nabla\cdot\mathbf{E} = \rho/\epsilon_0$ | $\nabla\times\mathbf{E} = -\dfrac{\partial\mathbf{B}}{\partial t}$ |
| **magnetic** | $\nabla\cdot\mathbf{B} = 0$ | $\nabla\times\mathbf{B} = \mu_0\mathbf{J} + \mu_0\epsilon_0\dfrac{\partial\mathbf{E}}{\partial t}$ |

**Constants.** Free space, differential form, with

$$
\mu_0 \approx 4\pi\times 10^{-7}\ \tfrac{\text{H}}{\text{m}}\ (\text{exact before the 2019 SI redefinition}),\qquad
\epsilon_0 = \frac{1}{\mu_0 c^2}\approx \frac{1}{36\pi\times 10^{9}}\ \tfrac{\text{F}}{\text{m}}\approx 8.854\times10^{-12}\ \tfrac{\text{F}}{\text{m}},\qquad
c = \frac{1}{\sqrt{\mu_0\epsilon_0}}\approx 3\times10^{8}\ \tfrac{\text{m}}{\text{s}}.
$$

The course counts the four off as each is derived ("our first Maxwell equation!" in [[1-electrostatics/02-coulombs-law-superposition-and-gauss|Lecture 2]]).

**Two consequences (Lecture 1 §2).**
1. **Statics decouple.** With no time variation both $\partial/\partial t$ terms vanish and the table splits: *electrostatics* (Lectures 1–11), $\nabla\cdot\mathbf{E}=\rho/\epsilon_0$ and $\nabla\times\mathbf{E}=0$ — a **curl-free** field fixed by charge; *magnetostatics* ([[2-magnetostatics/12-magnetic-force-biot-savart-and-amperes-law|Lecture 12]], [[2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential|Lecture 13]]), $\nabla\cdot\mathbf{B}=0$ and $\nabla\times\mathbf{B}=\mu_0\mathbf{J}$ — a **divergence-free** field fixed by current. [[2-magnetostatics/14-faradays-law-and-induced-emf|Lecture 14]] and [[2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials|Lecture 15]] bring $\partial\mathbf{B}/\partial t$ back.
2. **Waves.** With the time derivatives kept, empty space supports $\mathbf{E},\mathbf{B}\propto\cos\!\big(2\pi f\,(t - z/c)+\phi\big)$ — disturbances travelling at $c$ with wavelength $\lambda = c/f$ ([[3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves|Lecture 18]]), and the reason the course ends with transmission lines and the Smith chart.

**Quasi-statics: when is a circuit "a circuit"?** A source of period $T$ can be treated *statically* — using the instantaneous $\rho$ and $\mathbf{J}$ — when the field crosses the system before the source changes:

$$
T \gg \frac{L}{c}\quad\Longleftrightarrow\quad L \ll \lambda .
$$

This **quasi-static approximation** is the assumption behind lumped-circuit theory (ECE 210): a circuit is a circuit only while *electrically small*. Shrink $\lambda$ (raise the clock) or grow $L$ (a long cable, a PCB trace at GHz) and delays $L/c$ matter — Lectures 27–38. (Lecture 6 §1 states the same condition as $\tau\gg L/c$: the fields at each instant are the static fields of the instantaneous sources, plus a small slowly varying $\mathbf{B}$; excellent for lab circuits below a few MHz.)

> [!tip] A number to carry around
> $c \approx 3\times10^{8}$ m/s $= 300$ m/µs $= 30$ cm/ns. So 1 MHz ↔ 300 m wavelength; 1 GHz ↔ 30 cm; a 3 GHz clock has $\lambda = 10$ cm, which is *not* large compared with a motherboard.

**Where it appears (add).** [[1-electrostatics/01-fields-forces-and-the-maxwell-roadmap#2-the-roadmap-maxwells-equations-on-day-one|Lecture 1 §2]] (roadmap, constants, quasi-statics).
