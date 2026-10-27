---
title: "Topics"
description: "The site organized by idea rather than by lecture: every topic page teaches one thing in full — definition, derivation, the notes' examples, traps, exam notes — and links to the lectures that introduce it and the practice problems that test it."
tags: [concept]
aliases: ["Concepts", "concept glossary", "topic index"]
---

The lectures tell the story in order; the **topic pages** are where the content lives. Each one is self-contained: the key equation, the derivation (folded), the course's examples with their numbers, the traps, what exams do with it, and a **Practice** line pointing at the problems that use it. Lecture pages are maps onto these. Open the graph view (top right) to see how topics connect.

## Fields and the toolkit
*How fields are defined and measured, and the vector tools every later page uses.*

- [[concepts/electric-field|Electric field E]] — force per unit charge; the field as the thing that is there whether or not a test charge is
- [[concepts/lorentz-force|Lorentz force]] — F = q(E + v×B): what each field does to a moving charge, and why the magnetic part does no work
- [[concepts/maxwells-equations|Maxwell's equations]] — the four equations in integral and differential form, what each says, statics as the special case
- [[concepts/differential-elements|Differential elements dl, dS, dV]] — dl, dS, dV in the three coordinate systems; which to use for which source
- [[concepts/superposition|Superposition]] — fields and potentials add; how to break a source into pieces you already know
- [[concepts/five-step-recipe|The 5-step recipe for fields of charge distributions]] — turning a continuous charge distribution into an integral, step by step
- [[concepts/charge-density|Charge densities and δ-functions]] — ρ, ρ_s, ρ_l and δ-functions; how a sheet or line is written as a volume density
- [[concepts/current-distributions|Current distributions: J, J_s, I]] — J, J_s and I; δ-functions for sheets and wires; reading a current through a surface
- [[concepts/helmholtz-theorem|Helmholtz's theorem]] — a field is fixed by its divergence and curl: why the four Maxwell equations are enough

## Electrostatics
*Charges at rest: Coulomb, Gauss, the potential, boundary conditions, Poisson.*

- [[concepts/coulombs-law|Coulomb's law]] — the inverse-square force and the field of a point charge
- [[concepts/flux|Flux]] — counting field lines through a surface: ∫D·dS, with the sign set by the chosen normal
- [[concepts/gauss-law|Gauss's law]] — ∮D·dS = Q_enc, and when symmetry turns it into a one-line formula
- [[concepts/symmetric-charge-distributions|Symmetric charge distributions]] — line, sheet, slab, sphere, cylinder: the fields every exam assumes you know
- [[concepts/divergence|Divergence]] — flux per unit volume; ∇·D = ρ
- [[concepts/curl|Curl]] — circulation per unit area; the paddle-wheel picture
- [[concepts/divergence-theorem|Divergence theorem]] — ∮F·dS = ∫∇·F dV: the bridge from integral to differential laws
- [[concepts/stokes-theorem|Stokes' theorem]] — ∮F·dl = ∫(∇×F)·dS, and the loop version of path independence
- [[concepts/conservative-field|Conservative (curl-free) fields and the potential]] — curl-free ⇔ path-independent ⇔ a potential exists; the static E
- [[concepts/electrostatic-potential|Electrostatic potential V]] — V as energy per charge, E = −∇V, V from E and from charge
- [[concepts/boundary-conditions|Boundary conditions at an interface]] — what jumps and what is continuous at an interface, with n̂ from medium 2 into 1; refraction; perfect conductors
- [[concepts/poissons-equation|Poisson's and Laplace's equations]] — ∇²V = −ρ/ε and its one-dimensional solutions, layer by layer
- [[concepts/pn-junction|The pn junction]] — the depletion layer as a Poisson problem, and the junction as a nonlinear capacitor

## Materials, capacitors and conduction
*What conductors and dielectrics do to static fields, and the circuit elements that result.*

- [[concepts/conductors|Conductors in electrostatics]] — E = 0 inside, charge on the surface, Ohm's law, relaxation time, the perfect conductor in time-varying fields
- [[concepts/polarization|Polarization P and bound charge]] — P, bound charges −∇·P and P·n̂, and the field they produce
- [[concepts/electric-flux-density|Electric flux density D]] — D = ε₀E + P: the field that counts only free charge
- [[concepts/permittivity|Permittivity, susceptibility, and D = εE]] — χ_e, ε_r, ε: linear dielectrics and the handbook numbers
- [[concepts/static-fields-in-dielectrics|Static fields in dielectrics]] — D-first rules, refraction, layered and graded media, a dielectric-coated sphere
- [[concepts/capacitance|Capacitance]] — C = Q/V by the two recipes; plates, coax, spheres, layers in series and parallel
- [[concepts/conductance|Conductance and the leaky capacitor]] — the leaky capacitor: G = (σ/ε)C and the RC self-discharge
- [[concepts/electrostatic-energy|Electrostatic energy]] — ½CV² and ½εE² per cubic metre; forces from energy
- [[concepts/conductivity-and-susceptibility-models|Lorentz–Drude models of σ and χe]] — Drude and Lorentz: where σ and χ_e come from, and how they change with frequency

## Magnetostatics
*Steady currents and the fields they make.*

- [[concepts/magnetic-field|Magnetic field: B and H]] — B from the force on a moving charge; H; why a current attracts a moving charge
- [[concepts/biot-savart-law|Biot–Savart law]] — the field of a current element and of wires, arcs and loops
- [[concepts/amperes-law|Ampère's law]] — ∮H·dl = I_enc, and the symmetric cases it solves in one line
- [[concepts/current-sheets-and-slabs|Current sheets and slabs]] — H = ½J_s×n̂ on each side of a sheet; the slab's linear interior
- [[concepts/solenoids-and-toroids|Solenoids and toroids]] — H = nI inside, zero outside; the toroid's 1/r field
- [[concepts/vector-potential|Vector potential]] — B = ∇×A, Coulomb gauge, A of wires and sheets, E = −∇V − ∂A/∂t
- [[concepts/magnetic-dipole|The current loop and the magnetic dipole]] — a current loop far away: m = IA, torque m×B, the 1/r³ field
- [[concepts/magnetic-flux|Magnetic flux Ψ]] — Ψ = ∫B·dS, with ∮B·dS = 0 and no magnetic charge

## Induction and inductance
*Changing flux, emf, and the magnetic twins of capacitance and energy.*

- [[concepts/faradays-law|Faraday's law]] — ∮E·dl = −dΨ/dt: transformer emf, Lenz's rule, the induced electric field
- [[concepts/electromotive-force|Electromotive force (emf) and path-dependent voltage]] — what an emf is, moving loops, Lenz, and why Kirchhoff's voltage law needs it
- [[concepts/motional-emf|Motional emf and the voltmeter paradox]] — the sliding bar, the rotating rod, and the voltmeter paradox
- [[concepts/inductance|Inductance]] — L = NΨ/I, the Ampère chain for computing it, RL circuits
- [[concepts/magnetic-energy|Magnetic energy]] — ½LI² and ½μH² per cubic metre
- [[concepts/transmission-line-parameters|Transmission-line parameters 𝓛, 𝓒, 𝓖]] — 𝓛, 𝓒, 𝓖 per unit length, 𝓛𝓒 = με, and the look-ahead to Z₀

## Maxwell's equations and magnetic matter
*The displacement current completes the equations; magnetization brings them into matter.*

- [[concepts/continuity-equation|Continuity equation (charge conservation)]] — charge conservation: ∇·J = −∂ρ/∂t
- [[concepts/displacement-current|Displacement current]] — ∂D/∂t completes Ampère's law; the charging capacitor
- [[concepts/magnetization|Magnetization M and magnetization current]] — M, the magnetization current ∇×M and M×n̂, H = B/μ₀ − M, the P ↔ M dictionary
- [[concepts/permeability|Permeability, susceptibility, and B = μH]] — χ_m, μ_r, μ: linear magnetic media and the solenoid with a core
- [[concepts/magnetic-materials|Dia-, para- and ferromagnetism]] — dia-, para- and ferromagnets, hysteresis, the handbook values

## Plane waves
*Source-free solutions of Maxwell's equations, the sheets that launch them, and the power they carry.*

- [[concepts/wave-equation|Wave equation]] — source-free Maxwell → ∇²E = με ∂²E/∂t², and its d'Alembert solutions
- [[concepts/plane-waves|Plane waves]] — uniform plane TEM waves: E, H, the travel direction, reading snapshots and records
- [[concepts/intrinsic-impedance|Intrinsic impedance]] — η = √(μ/ε): H from E; complex η in lossy media
- [[concepts/current-sheet-radiation|Radiation from a current sheet]] — E = −(η/2)J_s(t − |ξ|/v) on both sides; a sheet in a lossy medium
- [[concepts/poynting-vector|Poynting vector]] — S = E×H: power per unit area and the direction it flows
- [[concepts/poynting-theorem|Poynting's theorem]] — the energy ledger: stored energy, flux through the boundary, Joule heating
- [[concepts/time-average-power|Time averages and average power]] — ⟨cos²⟩ = ½, ⟨S⟩ = E₀²/2η, averages straight from phasors
- [[concepts/monochromatic-waves|Monochromatic waves: ω, β, λ, v_p]] — ω, β, λ, v_p and the direction of travel of cos(ωt ∓ βz)
- [[concepts/dispersion-relation|Dispersion relation and phase velocity]] — ω against β: dielectrics, sound, the plasma and its cutoff
- [[concepts/phasors|Phasors]] — Re{Ãe^{jωt}}, d/dt → jω, plane-wave phasors and the partner field

## Waves in lossy media
*Conductivity turns β into γ = α + jβ: damping, skin depth, the two regimes.*

- [[concepts/phasor-maxwell-equations|Maxwell's equations in phasor form]] — Maxwell's equations at one frequency; the Helmholtz equation
- [[concepts/propagation-constant|Propagation constant]] — γ = α + jβ = √(jωμ(σ + jωε)): decoding a damped wave
- [[concepts/loss-tangent|Loss tangent]] — σ/ωε decides the regime: imperfect dielectric or good conductor
- [[concepts/skin-depth|Skin depth]] — δ = 1/√(πfμσ), η = (1+j)/(σδ), and why submarines are called at very low frequency

## Polarization, reflection, standing waves
*What a wave does at an interface, and how its field vector can rotate.*

- [[concepts/group-velocity|Group velocity]] — v_g = dω/dβ carries the message; dispersion spreads it
- [[concepts/wave-polarization|Wave polarization]] — linear, circular, elliptical; which hand, and the power of each component
- [[concepts/reflection-and-transmission|Reflection and transmission coefficients]] — Γ = (η₂ − η₁)/(η₂ + η₁), τ = 1 + Γ, the power balance, the perfect-conductor limit
- [[concepts/standing-waves|Standing waves]] — incident plus reflected at a mirror: nodes, antinodes, no net power
- [[concepts/radiation-pressure|Radiation pressure]] — 2⟨S⟩/c on a mirror, ⟨S⟩/c on an absorber

## Transmission lines
*Maxwell's equations reduced to voltages and currents on two conductors.*

- [[concepts/telegraphers-equations|Telegrapher's equations]] — V and I on a line obey Faraday and Ampère in circuit form
- [[concepts/characteristic-impedance|Characteristic impedance]] — Z₀ = √(𝓛/𝓒): the V/I ratio of one travelling wave
- [[concepts/bounce-diagram|Bounce diagram]] — tracking reflections at both ends of a line in the z–t plane

The electrostatic ↔ magnetostatic pairs (Coulomb ↔ Biot–Savart, Gauss ↔ Ampère, $V$ ↔ $\mathbf{A}$, $C$ ↔ $L$, …) are collected in the [[2-magnetostatics/index#the-dictionary-electrostatics--magnetostatics|dictionary]] on the Unit 2 page; the polarization ↔ magnetization pairs are on [[concepts/magnetization|Magnetization M and magnetization current]]. Following the course week by week? Use the [[index#by-lecture|lecture map]] on the home page.
