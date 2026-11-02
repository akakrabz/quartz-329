"""Agent C checks: slides Lectures 25-26 (reflection, standing waves)."""
import numpy as np

ok_all = True


def chk(name, cond):
    global ok_all
    ok_all &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name)


x, y, z = np.eye(3)
eta0 = 120 * np.pi
c = 299792458.0


def gamma(e1, e2):
    return (e2 - e1) / (e2 + e1)


# slide 8: medium 2 = 3 eps0, 3 mu0 (ink)
eta2 = np.sqrt(3 / 3) * eta0
G = gamma(eta0, eta2)
chk("s8 matched: Gamma=0, tau=1", abs(G) < 1e-12 and abs(1 + G - 1) < 1e-12)
v2 = c / np.sqrt(3 * 3)
chk("s8 v2 = c/3", np.isclose(v2, c / 3))
lam0 = 1.0
chk("s8 lambda2 = lambda0/3", np.isclose(lam0 / np.sqrt(9), lam0 / 3))

# slide 9: PEC, eta2 -> 0
G = gamma(eta0, 1e-12)
chk("s9 PEC: Gamma=-1, tau=0", np.isclose(G, -1) and abs(1 + G) < 1e-12)

# slide 11 example: eps_r = 9/4 behind free space
E0 = np.sqrt(120 * np.pi)
eta2 = eta0 / np.sqrt(9 / 4)
chk("s11 eta2 = 2/3 eta0", np.isclose(eta2, 2 / 3 * eta0))
G = gamma(eta0, eta2)
tau = 1 + G
chk("s11 Gamma=-1/5, tau=4/5", np.isclose(G, -0.2) and np.isclose(tau, 0.8))
Ei, Hi = E0 * x, E0 / eta0 * y
Er, Hr = G * E0 * x, -G * E0 / eta0 * y      # site/slide reference
Et, Ht = tau * E0 * x, tau * E0 / eta2 * y
Si = 0.5 * np.real(np.cross(Ei, np.conj(Hi)))
Sr = 0.5 * np.real(np.cross(Er, np.conj(Hr)))
St = 0.5 * np.real(np.cross(Et, np.conj(Ht)))
chk("s11 <Si> = 0.5 z", np.allclose(Si, 0.5 * z))
chk("s11 <Sr> = -0.02 z", np.allclose(Sr, -0.02 * z))
chk("s11 <St> = 0.48 z", np.allclose(St, 0.48 * z))
chk("s11 balance 0.5 = 0.02 + 0.48", np.isclose(Si[2], -Sr[2] + St[2]))
chk("s11 Er along -x, Hr along +y (Gamma<0)",
    np.allclose(np.sign(Er), -x) and np.allclose(np.sign(Hr), y))
# slide-11 figure (Er +x, Hr -y) is the Gamma>0 picture
chk("s11 figure orientation needs Gamma>0 (sign mismatch)",
    np.sign(G) < 0 and np.allclose(np.cross(x, -y), -z))
chk("s11 H_r ratio = -Gamma", np.isclose(Hr[1] / Hi[1], -G))

# slide 15: real-time standing wave, complex E1+
rng = np.random.default_rng(1)
Ep = 1.7 * np.exp(1j * 0.6)
eta1, beta, w = 377.0, 2.0, 3.0
zz = rng.uniform(-5, 0, 50)
tt = rng.uniform(0, 5, 50)
Ephas = Ep * (np.exp(-1j * beta * zz) - np.exp(1j * beta * zz))
Hphas = Ep / eta1 * (np.exp(-1j * beta * zz) + np.exp(1j * beta * zz))
Et_ = np.real(Ephas * np.exp(1j * w * tt))
Ht_ = np.real(Hphas * np.exp(1j * w * tt))
ph = np.angle(Ep)
chk("s15 E = 2|E1+| sin(bz) sin(wt+ph)",
    np.allclose(Et_, 2 * abs(Ep) * np.sin(beta * zz) * np.sin(w * tt + ph)))
chk("s15 H = (2/eta)|E1+| cos(bz) cos(wt+ph)",
    np.allclose(Ht_, 2 * abs(Ep) / eta1 * np.cos(beta * zz) * np.cos(w * tt + ph)))

# slide 17: S = E x H, average zero
S = np.array([np.cross(a * x, b * y) for a, b in zip(Et_, Ht_)])
Sform = abs(Ep) ** 2 / eta1 * np.sin(2 * beta * zz) * np.sin(2 * (w * tt + ph))
chk("s17 S = |E|^2/eta sin2bz sin2(wt+ph) z", np.allclose(S[:, 2], Sform)
    and np.allclose(S[:, :2], 0))
T = 2 * np.pi / w
tg = np.linspace(0, T, 4001)[:-1]
for z0 in (-0.3, -1.1):
    Sz = abs(Ep) ** 2 / eta1 * np.sin(2 * beta * z0) * np.sin(2 * (w * tg + ph))
    chk(f"s17 <S>=0 at z={z0}", abs(Sz.mean()) < 1e-12)

# slide 16 ink: E max at lambda/4 odd, E zero at m lambda/2, H max at m lambda/2
lam = 2 * np.pi / beta
zE0 = -np.arange(4) * lam / 2
zEm = -(2 * np.arange(4) + 1) * lam / 4
chk("s16 E nodes at -m lam/2", np.allclose(np.sin(beta * zE0), 0))
chk("s16 E antinodes at -(2m+1)lam/4", np.allclose(abs(np.sin(beta * zEm)), 1))
chk("s16 H antinodes at -m lam/2, nodes at -(2m+1)lam/4",
    np.allclose(abs(np.cos(beta * zE0)), 1) and np.allclose(np.cos(beta * zEm), 0))

# slide 18: Js = n x H1, n = -z (from PEC into medium 1)
n = -z
Hdir = y
Js_dir = np.cross(n, Hdir)
chk("s18 Js along +x", np.allclose(Js_dir, x))
# screen frame of slide 18 figure: y up, z right -> x into page
up, right, outp = np.array([0, 1, 0]), np.array([1, 0, 0]), np.array([0, 0, 1])
chk("s18 figure: x = y cross z is into page",
    np.allclose(np.cross(up, right), -outp))
# sheet radiation E = -(eta/2) Js(t - |z|/v); compare slide's t - z/v_p
v = w / beta


def Js(t):
    return 2 * abs(Ep) / eta1 * np.cos(w * t + ph)


zneg = rng.uniform(-5, -0.01, 50)
Ecorrect = -(eta1 / 2) * Js(tt - abs(zneg) / v)
Eslide_final = -abs(Ep) * np.cos(w * tt + beta * zneg + ph)
Eslide_mid = -(eta1 / 2) * Js(tt - zneg / v)
chk("s18 -(eta/2)Js(t+z/v) = -|E|cos(wt+bz+ph) (slide's final form)",
    np.allclose(Ecorrect, Eslide_final))
chk("s18 slide's Js(t - z/v_p) differs (slip): gives wt - bz",
    not np.allclose(Eslide_mid, Eslide_final)
    and np.allclose(Eslide_mid, -abs(Ep) * np.cos(w * tt - beta * zneg + ph)))
zpos = rng.uniform(0.01, 5, 50)
Erad_pos = -(eta1 / 2) * Js(tt - zpos / v)
Einc_pos = abs(Ep) * np.cos(w * tt - beta * zpos + ph)
chk("s18 radiated +z part cancels incident in z>0", np.allclose(Erad_pos + Einc_pos, 0))
# slide 18 writes H(z,t) without cos(bz): only true at z = 0
chk("s18 'H(z,t)' is H(0,t); zero at z=-lam/4",
    np.isclose(np.cos(beta * 0), 1) and abs(np.cos(beta * (-lam / 4))) < 1e-12)

# slide 4 figure: a_n up, H_t1 > H_t2 to the right -> Js into page
chk("s4 a_n x (H1-H2) into page (Js drawn otimes)",
    np.allclose(np.cross(up, right), -outp))

# summary slide 19 / slide 3: Gamma>0 picture, Sr along -z
chk("s19 Gamma>0: Er +x, Hr -y, Sr = -z", np.allclose(np.cross(x, -y), -z))

# ink slips: slide 8 denominator, slide 10 crest label
e1 = 1.0
for e2 in (0.5, 2.0):
    chk(f"s8 ink (e2-e1)/(e2+e2) != Gamma for e2={e2}",
        not np.isclose((e2 - e1) / (2 * e2), gamma(e1, e2)))
zc = -5 * lam / 4
chk("s10 ink: crest between lam and 3lam/2 is 5lam/4 (not 5lam/2)",
    np.isclose(abs(np.sin(beta * zc)), 1) and abs(np.sin(beta * (-5 * lam / 2))) < 1e-12)

print("ALL PASS" if ok_all else "SOME FAIL")
