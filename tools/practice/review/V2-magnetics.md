# V2-magnetics: independent re-check of six rewritten problems

Script `V2-magnetics.py`, output `V2-magnetics.out`: **154 PASS, 0 FAIL**. Every number, sign and direction in the six
solutions and **Answer.** lines was recomputed from the problem statements. `build_practice.py`: errors = 0 on L11–L15.
`check.py`: OK.

| # | verdict | note |
|---|---|---|
| 11.8 | FIXED | All numbers correct. These were checked by sheet superposition, a method-of-lines run of continuity + Gauss (J = σE and Drude) and `np.roots`. Minor: the statement now gives copper's carrier mass. |
| 12.10 | OK | Checked by numerical Biot–Savart quadrature for B at P and the general formula at 6 random points; nulls by least squares from 300 random starts (all on y = 0, z = −x/3); proton F and balancing E by `np.cross`. |
| 13.9 | FIXED | Checked by thin-sheet sums against the piecewise H in (a) and (b), n̂×ΔH = J_s, a brentq zero at z = 3 m, and finite-difference curl, divergence and slope jump of A. Minor wording fix in (c). |
| 14.10 | FIXED | Numbers correct: induced-field line integrals along the actual leads with node potentials, shoelace for orientation, Biot–Savart for Lenz. Major: the hint gave the wrong emf sign for clockwise loops. Minor: viewpoint added in the Answer. |
| 15.3 | OK | Checked by finite-difference grad, curl and ∂/∂t at 3 points and times: only (a) matches. Each distractor follows from the slip its explanation names. The gauge function λ = −2y²t and Faraday's law also check out. |
| 15.10 | OK | Checked with `np.cross` sheet fields and the boundary condition; shoelace confirms a clockwise path, so dS = −ẑ. Ψ, L, 𝓛, W_m, 𝓒, 𝓛𝓒 = 9μ₀ε₀ and the (d) factors all agree. A finite-width strip Biot–Savart gives −194.9 ẑ A/m at the centre (2.5 % fringing, same direction). |

## Findings and changes

1. **14.10 hint — major (misleading hint).** The hint said that a loop formed by the leads and the circuit has emf $-d\Psi_s/dt$ whenever it
   encircles the solenoid. Meter 2's loop and meter 3's loop on the +y side both run **clockwise**, so their emf is
   $+d\Psi_s/dt = -2$ V (checked numerically: the clockwise circulation is −2 V). A student who followed the hint would get
   V₂ = +2.4 V and meter 3 = +2 V instead of −1.6 V and −2 V.
   *Change:* the emf is now $-d\Psi_s/dt$ counter-clockwise seen from $+z$, $+d\Psi_s/dt$ clockwise, and zero if the loop
   does not encircle the solenoid.
2. **14.10 Answer (b) — minor (SPEC §7).** "counter-clockwise" had no viewpoint. *Change:* it now reads "counter-clockwise seen from $+z$".
3. **11.8 (c) statement — minor (well-posedness).** Copper's Drude τ = σm/(Ne²) needs a mass. The statement gave only silicon's m*.
   *Change:* "free-electron mass $m_e$" is added to copper's data. The solution already used m_e, so no numbers change.
4. **13.9 (c) solution — minor (wording).** "H = 0 everywhere outside the slabs" literally includes the gap −1 < z < 0,
   where H = 6 A/m. *Change:* it now reads "below and above the pair of slabs (z < −3 and z > 4) and nowhere between, gap included".

No blockers. Every final value, sign, direction, MC key and distractor explanation in the six problems is confirmed.

## Notes (no change needed)

- 11.8(a): an infinite sheet sum for the ripple only converges conditionally. A sharp cut at a zero of ρ leaves an end
  dipole layer, which acts like an applied uniform field. A smooth Gaussian taper centred on a zero of ρ (no symmetry
  assumed) reproduces the page's E_x = −(ρ₀/βε)cos βx to 1e−5. It also gives E_x = 0 on the crest and trough planes, so
  the page's symmetry argument for C = 0 is sound.
- 11.8(d): simulations agree with the page. For copper they give ω = 1.645e16 rad/s and an envelope time constant of 4.84e−14 s
  (254 zero crossings in 2τ). For sea water the slow time constant sits 8.37e−5 below ε/σ; for Si it is 0.340 % below τ_r.
- I checked the cross-references by grep only. 11.6 uses the same m* and τ (so the mobility is 0.122), but its N is
  1e22 rather than 1e20; the claim is about mobility only, so it holds. 13.8(a) is the zero-net-current stack and 15.9
  is the "μ never enters Ampère" toroid. Both match how the text cites them.
- Difficulty labels and scope look reasonable.

## Unresolved

- I could not verify the cited exam numbers against the exams: Summer 2017 HE2 #2a, Summer 2020 HE2 #2a, Summer 2017
  HE2 #1a, Summer 2019 HE2 #2a–b, Summer 2017/2018 HE2 #3, SP18 Exam 2 #1(v) and #3. They look plausible, and I left
  them unchanged.
