<!-- for concepts/intrinsic-impedance, from Lecture 22 §4–5 (complex η) -->

**Physics (add to the "In a conducting medium" part).** Where the angles come from: $j\omega\mu$ is at 90°, $\sigma + j\omega\epsilon$ at $90^\circ - \tan^{-1}(\sigma/\omega\epsilon)$. $\eta$ (root of the ratio) takes half the difference, $\tau$; $\gamma$ (root of the product) half the sum, $90^\circ - \tau$. Hence $\alpha/\beta = \cot\angle\gamma = \tan\tau$, and $\lvert\gamma\rvert\lvert\eta\rvert = \omega\mu$: conduction raises $\lvert\gamma\rvert$ and lowers $\lvert\eta\rvert$. Beyond the scales $\omega\sqrt{\mu\epsilon}$ and $\sqrt{\mu/\epsilon}$, only $\sigma/\omega\epsilon$ matters.

**τ sets the timing:** $\mathbf{H}$ peaks $\tau/\omega$ after $\mathbf{E}$; in a snapshot it sits $\tau/\beta$ behind, on the source side. Dividing by $\eta$ divides by $\lvert\eta\rvert$ *and* subtracts $\tau$: for the damped wave $\mathbf{H} = \pm\hat y\,(\lvert E_0\rvert/\lvert\eta\rvert)\,e^{\mp\alpha z}\cos(\omega t\mp\beta z + \angle E_0 - \tau)$ ([[concepts/propagation-constant]]).

**From a measured wave (exam step):** $\eta = j\omega\mu/\gamma$ with the medium's $\mu$: $\lvert\eta\rvert = \omega\mu/\lvert\gamma\rvert$, $\tau = 90^\circ - \angle\gamma = \tan^{-1}(\alpha/\beta)$. Example ([[concepts/propagation-constant|decode example]]): $\gamma = 1 + j3$ m⁻¹, $\omega = 3\times10^8$ rad/s, $\mu_0$, so $\omega\mu_0 = 120\pi$ Ω/m and

$$
\begin{gathered}
\eta = \frac{j120\pi}{1 + j3} = \frac{120\pi\,j(1 - j3)}{10} = 12\pi(3 + j)\\[6pt]
= 113.1 + j37.7 = 119.2\,e^{j18.4^\circ}\ \Omega ;
\end{gathered}
$$

check $\tan^{-1}(1/3) = 18.4^\circ$. Then $\tilde{\mathbf{H}} = \hat x\times\hat y\,(6/\eta)\,e^{-\gamma x} = \hat z\,(6/119.2)\,e^{-j18.4^\circ}e^{-\gamma x}$ A/m for $\tilde{\mathbf{E}} = \hat y\,6e^{-\gamma x}$ V/m.

> [!trap] What μ does, and does not, change
> $\mu$ enters $\eta = j\omega\mu/\gamma$, $\sigma = 2\alpha\beta/\omega\mu$ and $\epsilon = (\beta^2 - \alpha^2)/\omega^2\mu$: $\mu_0$ for a magnetic medium spoils all three, but not $\sigma/\omega\epsilon$, so the regime verdict survives. The [[problems/decoding-a-damped-wave|worked problem]] ($\mu = 3\mu_0$) shows the factor of 3.

**Where it appears (add):** [[3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves#5-the-general-formulas-and-how-to-decode-a-damped-wave|Lecture 22 §5]] (complex $\eta$ from $\gamma$; angles).
