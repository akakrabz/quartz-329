<!-- for concepts/conductivity-and-susceptibility-models, from Lecture 22 §8 -->

**When the conductivity depends on frequency (waves).** The Drude conductivity

$$
\sigma(\omega) = \frac{Nq^2}{m(\nu + j\omega)} = \frac{\sigma_{\text{DC}}}{1 + j\omega/\nu} .
$$

The [[concepts/propagation-constant|propagation constant]] and [[concepts/intrinsic-impedance|intrinsic impedance]] still follow from $\sigma(\omega) + j\omega\epsilon$, but $\text{Re}\{\gamma/\eta\}$ and $\text{Im}\{\gamma/\eta\}/\omega$ give only *effective* $\sigma$, $\epsilon$: an imaginary part of $\sigma$ looks exactly like a change in $\epsilon$.

- **Metals.** Copper's $\nu\approx4\times10^{13}$ s⁻¹ keeps $\sigma(\omega)$ within $1.6\times10^{-4}$ of DC at 1 GHz: real $\sigma$ is safe at every radio and microwave frequency.
- **A collisionless plasma** ($\nu\to0$, the ionosphere). $\sigma = Nq^2/(j\omega m)$ is imaginary; the current lags the field by 90° (inertia) and partly cancels the displacement current,

$$
\sigma + j\omega\epsilon_0 = j\omega\epsilon_0\Big(1 - \frac{\omega_p^2}{\omega^2}\Big),\qquad \omega_p^2 = \frac{Nq^2}{m\epsilon_0},
$$

so $\gamma^2 = -(\omega^2 - \omega_p^2)/c^2$.
  - **Above $\omega_p$:** $\gamma = j\sqrt{\omega^2 - \omega_p^2}/c$, no attenuation: the plasma [[concepts/dispersion-relation|dispersion relation]] in one line. $\eta = \omega\mu_0/\beta$ is real, above $\eta_0$.
  - **Below it:** $\gamma = \sqrt{\omega_p^2 - \omega^2}/c$ is real: decay without spatial oscillation (*evanescent*). $\eta$ is imaginary, so $\mathbf{E}$, $\mathbf{H}$ are 90° apart, carrying no average power ([[concepts/time-average-power]]). Not loss ($\text{Re}\{\sigma\} = 0$): the plasma reflects ([[concepts/reflection-and-transmission]]).
- $N = 10^{12}$ m⁻³ (daytime ionospheric peak): $f_p\approx9$ MHz ($f_p\approx9\sqrt N$ Hz). At 5 MHz, $\delta = 6.4$ m; at 20 MHz, $\beta = 0.375$ rad/m against vacuum's 0.419 rad/m.
- Only $\text{Re}\{\sigma\}$ heats: $\langle\mathbf{J}\cdot\mathbf{E}\rangle = \tfrac12\text{Re}\{\sigma\}\lvert\tilde{\mathbf{E}}\rvert^2$; with collisions $\text{Re}\{\sigma_{\text{DC}}/(1 + j\omega/\nu)\} = \sigma_{\text{DC}}/(1 + \omega^2/\nu^2)$.

**Where it appears (add):** [[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves#8-when-the-conductivity-depends-on-frequency|Lecture 22 §8]] (Drude $\sigma(\omega)$ in $\gamma$, $\eta$; the plasma above and below $\omega_p$).
