# V2 review: electrostatics problems changed in the earlier review

Scope: only 4.9, 7.9, 8.11, 9.10 and 10.9 (blocks read in isolation; no `checks/*` or `R*.py` opened).
Script: `review/V2-electrostatics.py` → `review/V2-electrostatics.out` (**145 PASS, 0 FAIL**).
Each problem was re-solved from its statement by a different route from the page's:

- **4.9:** finite-difference curl and div of the 3-D field; `quad` line integrals on the polygonal paths; `dblquad` flux of the numerical curl; shoelace orientation; `brentq` for $x_0$ (plus a uniqueness scan).
- **7.9:** $E$ from superposing infinite sheets (no boundary condition imposed, so neutrality gives $E = 0$ outside on its own); $V$ by cumulative integration; the same run for the slabs with no intrinsic layer and for the silicon diode on a micron grid.
- **8.11:** a brute-force 2-D sum of about 400k line charges (field and log-potential); Gauss's law with the *total* charge; `brentq` for the null.
- **9.10:** an E-first linear solve for the induced and bound shell charges; $V$ both by superposing charged shells and by `quad` from infinity.
- **10.9:** a conservative finite-difference Laplace solve; current by quadrature over the lossy hemisphere; power as $\int\sigma E^2\,dV$; discharge with `solve_ivp` plus an event at −50 V.

| # | verdict | note |
|---|---|---|
| 4.9 | OK | All curls, $\rho$ (sign on $y = \pm1, 3$), maxima, routes A/B ($-2$, $+2$ V), Stokes flux ($-4$ V, CCW from $+z$), straight-line 0 V, $x_0 = 4/3$ m (unique), $6/\pi$ V on both routes are correct. Hint, Check and Answer agree. |
| 7.9 | OK | Neutral; $\epsilon_0E_z$ and $\epsilon_0V$ piecewise forms, $V(-1), V(0), V(1) = 6, 12, 18$ (/$\epsilon_0$), $21/\epsilon_0$, $\lvert E\rvert_{\max} = 6/\epsilon_0$ along $-\hat{z}$, no-layer $9/\epsilon_0$, and (d) 3.09 MV/m and 1.08 V are all correct. The quoted junction formula matches Lecture 7, line 89. |
| 8.11 | OK | $\rho_b$, $\rho_{sb}$, $\mp111$ nC/m, $\mathbf{D} = 0$, $\mathbf{E} = -5\times10^6r\,\hat{r}$, $-1$ kV, null at 1 cm, $-7.5\times10^4$, $2.5\times10^4$ and $10^4$ V/m, and tube charges ($-27.8$ nC/m, $-88.5$ nC/m²) are all confirmed by the brute-force sum. The jump checks hold. The cross-reference to 8.8 (point charge in a dielectric sphere) is valid. |
| 9.10 | OK | D/E/P table; free $\rho_s$ (0.398, −0.0995, −0.00884, 0); bound $\rho_{sb}$ and totals (−4, +4, +0.5, −0.5 C); $V_{\text{shell}} = -7/(96\pi\epsilon_0)$, $V(0) = 5/(96\pi\epsilon_0)$; difference $1/(8\pi\epsilon_0)$ – all correct by two routes. |
| 10.9 | FIXED | All numbers were right for an isolated capacitor, but the statement was ill-posed after the polarity reversal (below). |

## Findings

1. **10.9 – blocker (ill-posed statement).** The polarity reversal left the outer shell *ungrounded* (held at −100 V by a source), and the statement never said what lies outside it.
   - Take the usual convention: free space outside, with ground at the potential of infinity. The shell's outer surface then carries $4\pi\epsilon_0b\,V(b)\approx-222.5$ pC, so the shell holds −890.1 pC in all, not the keyed −667.6 pC.
   - In (d), the isolated shell then has capacitance $C+4\pi\epsilon_0b$, so $\tau\approx7.08$ ms, not the keyed 5.313 ms.
   - In the original version the outer shell was grounded, so this question never came up.
   - **Fix:** one sentence added to the statement: "Treat the two spheres as a stand-alone capacitor: no charge sits on the outer surface of the shell, so there is no field outside it." In (d), one sentence added to say why only $C$ enters, and that a distant ground at 0 V would add 2.225 pF and give about 7.08 ms. Both numbers are printed by the script.
   - With this assumption every keyed number stands: $C$, ±667.6 pC, 125.7 nA, 1.257 nS, 795.8 MΩ, 12.57 µW, 5.313 ms, 3.682 ms and 0.531 µC/m². The true/false keys (i) True and (ii) False and their explanations are correct.
2. No other blockers, majors or minors. Signs, directions, $\hat{n}$ conventions, hints, Check lines and Answer lines are consistent in all five problems. Each has a hard label that fits, stays within scope, and is in valid block format.

## Checks run
- `python3 practice/build_practice.py`: L04, L07, L08, L09 and L10 each have 12 problems (5, 3, 4), errors = 0. Overall: 164 problems, 0 errors.
- `python3 check.py …`: `OK` (95 pages, 926 links, 15817 math expressions).

## Not resolved / notes
- I could not verify the cited exam numbers (Summer 2017/2018/2019/2020 HE1, SP18 Exam 1 #5, FA26 HW4 #6), but none of them looks implausible.
- Style only, not changed: the statements of 7.9, 8.11 and 10.9 put (a)–(d) on consecutive callout lines with no `>` separator line. The same style appears elsewhere on these pages.
