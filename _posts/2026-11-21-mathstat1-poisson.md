---
title: "Mathematical Statistics 1: Ch. 3 Part 3 — Poisson Distribution"
date: 2026-11-21 11:30:00 +0900
categories: [Study Notes, Mathematical Statistics 1]
tags: [poisson, poisson process, poisson approximation, occurrence rate]
description: Rutherford's alpha-particle experiment, the Poisson approximation of the binomial distribution, and the proof that the number of occurrences of a Poisson process is Poisson distributed. Chapter 3, notes section 2 of Mathematical Statistics 1.
math: true
mermaid: false
render_with_liquid: false
---

> My handwritten notes, translated into English. Chapter 3, notes section 2. It corresponds to §3.4 of the textbook. Statements and proofs follow my notes. Material taken from the textbook (the proof of the Poisson approximation, the definition of the Poisson process, the properties of the Poisson distribution, and the examples) is collected at the end under "Supplement from the textbook". The exercises are in [Chapter 3 Exercises](/posts/mathstat1-exercises-chapter-3/).
{: .prompt-info }

## 2. Poisson distribution

**Example (Rutherford's $$\alpha$$-particle diffraction experiment).** $$\mathrm{Ra}^{226}_{88} \to \mathrm{Rn}^{222}_{86} + \alpha$$, where $$\alpha = {}^{4}_{2}\mathrm{He}^{2+}$$. Count the number of $$\alpha$$-particles emitted during $$7.5$$ seconds. The counts, drawn as a histogram, follow the Poisson distribution very well.

\* Let $$p$$ be the probability that one $$\alpha$$-particle is emitted during the $$7.5$$ seconds, and let

$$
X = \text{the number of } \alpha\text{-particles emitted during } 7.5 \text{ seconds} \ \sim\ \mathrm{Bin}(n, p) \quad (n \to \infty) \ \approx\ \mathrm{Poi}(\lambda = np).
$$

> **Theorem (Poisson approximation).**
>
> $$
> \lim_{\substack{n \to \infty \\ np_n \to \lambda}}\binom{n}{x}p_n^x(1 - p_n)^{n-x} = \frac{\lambda^xe^{-\lambda}}{x!}, \qquad x = 0, 1, 2, \dots
> $$
{: .theorem #thm-poisson-approximation }

> **Theorem.** If $$(N_t) \sim \mathrm{PP}(\lambda)$$ (a Poisson process), then $$N_t \sim \mathrm{Poisson}(\lambda t)$$, $$t \ge 0$$.
{: .theorem #thm-poisson-process-distribution }

> **Lemma (solutions of a differential equation).** The solution of $$y'(x) = ay(x) + b$$ is
>
> $$
> y(x) = y(0)e^{ax} + \int_0^x e^{a(x-s)}b(s)\,ds.
> $$
{: .theorem #lem-ode }

*Proof.* Let $$g(n, t) = P(N_t = n)$$, $$t \ge 0$$, $$n = 0, 1, 2, \dots$$ We have to show that

$$
g(n, t) = \frac{e^{-\lambda t}(\lambda t)^n}{n!}.
$$

(1) Let us show that $$g(0, t) = e^{-\lambda t}$$. We have $$g(0, 0) = P(N_0 = 0) = 1$$, and

$$
\frac{d}{dt}g(0, t) = \lim_{h \to 0}\frac{g(0, t + h) - g(0, t)}{h} = \lim_{h \to 0}\frac{1}{h}\bigl(P(N_{t+h} = 0) - P(N_t = 0)\bigr) = \lim_{h \to 0}\frac{1}{h}\bigl(P(N_t = 0, N_{t+h} - N_t = 0) - P(N_t = 0)\bigr)
$$

$$
= \lim_{h \to 0}\frac{1}{h}\bigl(P(N_t = 0)P(N_h = 0) - P(N_t = 0)\bigr) = g(0, t)\lim_{h \to 0}\frac{P(N_h = 0) - 1}{h} = g(0, t)\lim_{h \to 0}\frac{-\lambda h + o(h)}{h} = g(0, t)\cdot(-\lambda).
$$

\* Here $$P(N_h = 0) = 1 - \lambda h + o(h)$$. Hence $$\dfrac{d}{dt}g(0, t) = g(0, t)\cdot(-\lambda)$$. By the lemma,

$$
g(0, t) = g(0, 0)e^{-\lambda t} + \int_0^te^{-\lambda(t-s)}\cdot 0\,ds = g(0, 0)e^{-\lambda t} = e^{-\lambda t}.
$$

(2) Now let us show that $$g(n, t) = \dfrac{e^{-\lambda t}(\lambda t)^n}{n!}$$. We have $$g(n, 0) = P(N_0 = n) = 0$$ (when $$n \ge 1$$), and

$$
\frac{\partial}{\partial t}g(n, t) = \lim_{h \to 0}\frac{1}{h}\bigl(P(N_{t+h} = n) - P(N_t = n)\bigr)
$$

$$
= \lim_{h \to 0}\frac{1}{h}\Bigl\{P(N_t = n)P(N_h = 0) + P(N_t = n - 1)P(N_h = 1) + P(N_t \le n - 2)P(N_h \ge 2) - P(N_t = n)\Bigr\}
$$

$$
= \lim_{h \to 0}\frac{1}{h}\Bigl\{g(n, t)\bigl(1 - \lambda h + o(h) - 1\bigr) + g(n - 1, t)\bigl(\lambda h + o(h)\bigr) + g(\cdot)\,o(h)\Bigr\} = \lambda\bigl(g(n - 1, t) - g(n, t)\bigr).
$$

By the lemma,

$$
g(n, t) = g(n, 0)e^{-\lambda t} + \int_0^te^{-\lambda(t-s)}\lambda g(n - 1, s)\,ds = \lambda e^{-\lambda t}\int_0^te^{\lambda s}g(n - 1, s)\,ds.
$$

Therefore

$$
g(1, t) = \lambda e^{-\lambda t}\int_0^te^{\lambda s}g(0, s)\,ds = \lambda e^{-\lambda t}\int_0^te^{\lambda s}e^{-\lambda s}\,ds = \lambda te^{-\lambda t},
$$

$$
g(2, t) = \lambda e^{-\lambda t}\int_0^te^{\lambda s}(\lambda s)e^{-\lambda s}\,ds = \frac{\lambda^2t^2e^{-\lambda t}}{2} = \frac{(\lambda t)^2e^{-\lambda t}}{2!},
$$

and so on. $$\square$$

## Supplement from the textbook

**Proof idea of the Poisson approximation (§3.4).** For the binomial distribution $$\mathrm{Bin}(n, p)$$ with $$n$$ large and $$p$$ small,

$$
\binom{n}{x}p^x(1 - p)^{n-x} = \frac{n}{n}\Bigl(1 - \frac{1}{n}\Bigr)\cdots\Bigl(1 - \frac{x - 1}{n}\Bigr)\frac{(np)^x}{x!}\Bigl(1 - \frac{np}{n}\Bigr)^{n-x} \simeq \frac{(np)^xe^{-np}}{x!}.
$$

The limit used is $$\lim_{n \to \infty,\ a_n \to a}(1 + a_n/n)^n = e^a$$, that is, $$\lim n\log(1 + a_n/n) = a$$.

**Example 3.4.1.** A baseball player hit $$2$$ home runs per $$100$$ at-bats last season. Find the probability that this season he hits $$15$$ home runs in $$400$$ at-bats. The probability of $$15$$ in $$\mathrm{Bin}(400, 0.02)$$ is, with the Poisson approximation,

$$
\binom{400}{15}0.02^{15}0.98^{385} \simeq e^{-400 \times 0.02}(400 \times 0.02)^{15}/15! \simeq 0.0090.
$$

The function $$f(x) = e^{-\lambda}\lambda^x/x!$$, $$x = 0, 1, 2, \dots$$ ($$\lambda > 0$$) is the pdf of the *Poisson distribution*, written $$X \sim \mathrm{Poisson}(\lambda)$$. For $$\lambda = 1, 3, 5, 7$$ the probability polygon is a decreasing curve for $$\lambda = 1$$ and a hump whose peak moves to the right as $$\lambda$$ increases.

> **Theorem 3.4.1 (Properties of the Poisson distribution).**
>
> - (a) If $$X \sim \mathrm{Poisson}(\lambda)$$, its moment generating function is $$mgf_X(t) = e^{-\lambda + \lambda e^t}$$, $$-\infty < t < +\infty$$.
> - (b) If $$X \sim \mathrm{Poisson}(\lambda)$$, then $$E(X) = \lambda$$ and $$\mathrm{Var}(X) = \lambda$$.
> - (c) If $$X_1 \sim \mathrm{Poisson}(\lambda_1)$$, $$X_2 \sim \mathrm{Poisson}(\lambda_2)$$ and $$X_1, X_2$$ are mutually independent, then $$X_1 + X_2 \sim \mathrm{Poisson}(\lambda_1 + \lambda_2)$$.
{: .theorem #thm-poisson-properties }

*Proof.* (a) $$E(e^{tX}) = \sum_{x=0}^{\infty}e^{tx}e^{-\lambda}\lambda^x/x! = e^{-\lambda}\sum_{x=0}^{\infty}(\lambda e^t)^x/x! = e^{-\lambda + \lambda e^t}$$.

(b) The cumulant generating function is $$cgf_X(t) = -\lambda + \lambda e^t = \lambda t + \frac{\lambda}{2!}t^2 + \frac{\lambda}{3!}t^3 + \cdots$$, so $$E(X) = \dot{cgf}_X(0) = \lambda$$ and $$\mathrm{Var}(X) = \ddot{cgf}_X(0) = \lambda$$.

(c) By the theorem on sums of independent random variables (Theorem 2.5.11) and (a), $$mgf_{X_1 + X_2}(t) = mgf_{X_1}(t)mgf_{X_2}(t) = e^{-(\lambda_1 + \lambda_2) + (\lambda_1 + \lambda_2)e^t}$$, which is the mgf of $$\mathrm{Poisson}(\lambda_1 + \lambda_2)$$; by the uniqueness of the mgf, $$X_1 + X_2 \sim \mathrm{Poisson}(\lambda_1 + \lambda_2)$$. $$\square$$

**Poisson process.** The Poisson distribution is commonly used as a probability model for such things as the number of plankton in a fixed volume of water in a river, or the number of accesses requested to a computer server during a fixed time.

> **Poisson process.** Let $$N_t$$ be the number of occurrences of a particular phenomenon from time $$0$$ to $$t$$. If the following conditions are satisfied, $$\{N_t : t \ge 0\}$$ is called a *Poisson process* with occurrence rate $$\lambda$$, written $$(N_t) \sim \mathrm{PP}(\lambda)$$.
>
> - (a) *(Stationarity.)* $$N_t$$ and $$N_{s+t} - N_s$$ have the same distribution, and $$N_0 = 0$$.
> - (b) *(Independent increments.)* $$N_t$$ and $$N_{t+h} - N_t$$ ($$h > 0$$) are mutually independent.
> - (c) *(Proportionality.)* $$P(N_h = 1) = \lambda h + o(h)$$, $$h \to 0$$, where $$\lambda$$ is a positive proportionality constant and $$\lim_{h \to 0}o(h)/h = 0$$.
> - (d) *(Rareness.)* $$P(N_h \ge 2) = o(h)$$, $$h \to 0$$.
{: .definition #def-poisson-process }

The proof above uses exactly these conditions: independent increments and stationarity give $$P(N_t = n, N_{t+h} - N_t = 0) = P(N_t = n)P(N_h = 0)$$, and proportionality and rareness give $$P(N_h = 1) = \lambda h + o(h)$$, $$P(N_h \ge 2) = o(h)$$. The idea behind the theorem: divide $$(0, t]$$ into $$n$$ intervals; $$N_{it/n} - N_{(i-1)t/n}$$ is approximately $$\mathrm{Ber}(\lambda t/n)$$, they are independent, so $$N_t$$ is approximately $$\mathrm{Bin}(n, \lambda t/n)$$, and by the Poisson approximation it is $$\mathrm{Poisson}(\lambda t)$$ for $$n$$ large.

**Example 3.4.2.** In a process producing wire whose average number of defects per unit length is $$0.05$$, when a Poisson process is valid as a model for the number of defects, find the probability that a wire of length $$100$$ units has $$10$$ or more defects. $$N_{100}$$ follows the Poisson distribution with mean $$\lambda t = 0.05 \times 100 = 5$$, and computing with R,

$$
P(N_{100} \ge 10) = 1 - P(N_{100} \le 9) = 1 - \mathrm{ppois}(9, 5) = 0.032.
$$

## References

- 김우철, *수리통계학* (Mathematical Statistics), revised 2nd edition, 민영사, 2021 — Chapter 3, §3.4 (Examples 3.4.1 and 3.4.2, Theorems 3.4.1 and 3.4.2). The supplement is translated from the book.
- Mathematical Statistics 1 (326.311), Seoul National University, Spring 2025. Instructor: Jaeyong Lee (이재용).

[Previous](/posts/mathstat1-geometric-negative-binomial/) · [Overview](/posts/mathstat1-overview/) · [Next](/posts/mathstat1-gamma-beta/)
