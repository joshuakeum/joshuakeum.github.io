---
title: "Mathematical Statistics 1: Ch. 5 Part 2 — Convergence in Distribution"
date: 2026-11-21 13:20:00 +0900
categories: [Study Notes, Mathematical Statistics 1]
tags: [convergence in distribution, limiting distribution, scheffe, mgf convergence, poisson approximation, slutsky, continuous mapping]
description: Convergence in distribution and its definition through the cdf, why the continuity points matter, how to prove it through densities and moment generating functions, and, from the textbook, Slutsky's theorem and the continuous mapping theorem. Chapter 5, notes section 2 of Mathematical Statistics 1.
math: true
mermaid: false
render_with_liquid: false
---

> My handwritten notes, translated into English. Chapter 5, notes section 2. It corresponds to the second half of §5.2 and the beginning of §5.3 of the textbook. Statements and proofs follow my notes. Material taken from the textbook is collected at the end under "Supplement from the textbook". The exercises are in [Chapter 5 Exercises](/posts/mathstat1-exercises-chapter-5/).
{: .prompt-info }

## 2. Convergence in distribution

### 2.1 Definition of convergence in distribution

> **Definition (Convergence in distribution).** "The distribution of $$X_n$$ converges to that of $$X$$":
>
> $$
> X_n \rightsquigarrow X, \qquad X_n \xrightarrow[n\to\infty]{d} X, \qquad F_n \rightsquigarrow F, \qquad F_n \xrightarrow[n\to\infty]{d} F
> $$
>
> $$\iff$$ for every point $$x$$ at which $$F(x)$$ is continuous, $$\displaystyle\lim_{n\to\infty}F_n(x) = F(x)$$.
{: .definition #def-convergence-distribution }

For large $$n$$, $$F_n \simeq F$$.

*Question: why is it not required at all points $$x$$?* cf) Why was it not defined at all $$x$$? Consider $$U(0, \frac{1}{n}) \rightsquigarrow \delta_0$$ ($$\delta_0$$ is the Dirac measure: probability $$1$$ at $$0$$). Here

$$
F_n(x) = \begin{cases}0 & (x \le 0) \\ nx & (0 < x < \frac{1}{n}) \\ 1 & (x \ge \frac{1}{n}),\end{cases}
\qquad
F_n(x) \xrightarrow{n\to\infty} \begin{cases}0 & (x < 0) \\ 1 & (x > 0).\end{cases}
$$

This is not a cdf (it is not right-continuous at $$0$$)! The cdf we have in mind is $$F(x) = \begin{cases}0 & (x < 0) \\ 1 & (x \ge 0).\end{cases}$$ For all $$x \in C_F$$ (the continuity points of $$F$$) the convergence holds; at points where $$F$$ is not continuous, the limit may differ, and $$F$$ can be made right-continuous so that it is a cdf.

**Example.** $$X_1, \dots, X_n \overset{iid}{\sim} U(0, \theta)$$, $$\theta > 0$$. Prove $$n(\theta - X_{(n)}) \rightsquigarrow \mathrm{Exp}(\theta)$$ $$\iff$$ $$X_{(n)} \approx \theta - \dfrac{1}{n}\mathrm{Exp}(\theta)$$ (approximation of the distribution).

*Proof.* $$P(n(\theta - X_{(n)}) \le t) \to 1 - e^{-t/\theta}$$ for all $$t > 0$$. Therefore

$$
P(X_{(n)} \ge \theta - \tfrac{1}{n}t) = 1 - P(X_{(n)} < \theta - \tfrac{1}{n}t) = 1 - P(X_1, \dots, X_n < \theta - \tfrac{1}{n}t) = 1 - \bigl(P(X_1 < \theta - \tfrac{t}{n})\bigr)^n
$$

$$
= 1 - \Bigl(\frac{\theta - \frac{t}{n}}{\theta}\Bigr)^n = 1 - \Bigl(1 - \frac{t}{n\theta}\Bigr)^n \xrightarrow{n\to\infty} 1 - e^{-t/\theta}. \qquad\square
$$

### 2.2 Methods for proving convergence in distribution

> **Theorem.**
>
> (1) *Convergence of the density functions* (both discrete and continuous): $$f_{X_n}(x) \to f_X(x)$$ for all $$x$$ $$\Rightarrow$$ $$X_n \xrightarrow{d} X$$. (Scheffé's theorem.)
>
> (2) *Convergence of the mgf* (graduate level): $$M_{X_n}(t) \to M_X(t)$$ for all $$t$$ with $$\lvert t\rvert < \epsilon$$, $$\epsilon > 0$$ $$\Rightarrow$$ $$X_n \xrightarrow{d} X$$.
{: .theorem #thm-methods-convergence-distribution }

*Proof.* (1) We assume that $$f_{X_n} \Rightarrow f_X$$ (uniform convergence) and also assume $$f_{X_n}$$ and $$f_X$$ are defined on $$[a, b]$$. Now we have to show $$\lvert F_n(x) - F(x)\rvert \to 0$$ for all $$x$$. Then

$$
\lvert\text{left}\rvert = \Bigl\lvert\int_a^xf_{X_n}(t)\,dt - \int_a^xf(t)\,dt\Bigr\rvert \le \int_a^x\lvert f_{X_n}(t) - f(t)\rvert\,dt \le (x - a)\sup_{t\in[a,b]}\lvert f_{X_n}(t) - f(t)\rvert \longrightarrow 0. \qquad\square
$$

**Example.** $$t(n) \to N(0, 1)$$. ($$\because$$ $$n \to \infty \Rightarrow t(x \mid n) \to N(x \mid 0, 1)$$.)

**Example.** When $$n \to \infty$$, $$np_n \to \mu > 0$$ $$\Rightarrow$$ $$\mathrm{Bin}(n, p_n) \to \mathrm{Poisson}(\mu)$$.

(1) Pdf convergence. (2) Mgf convergence. Let $$X_n \sim \mathrm{Bin}(n, p_n)$$. Then

$$
M_{X_n}(t) = (p_ne^t + q_n)^n, \quad q_n = 1 - p_n, \qquad = (1 - p_n(1 - e^t))^n = \Bigl(1 - \frac{np_n}{n}(1 - e^t)\Bigr)^n = \Bigl(1 - \frac{\mu + o(1)}{n}(1 - e^t)\Bigr)^n \longrightarrow e^{\mu(e^t - 1)}.
$$

**Example (Normal approximation of the binomial distribution).** (Do it yourself.) $$X_n \sim \mathrm{Bin}(n, p_n)$$, $$p_n \to p \in (0, 1)$$. Then

$$
\frac{X_n - np_n}{\sqrt{np_n(1 - p_n)}} \rightsquigarrow N(0, 1).
$$

*Proof.* Use mgf.

## Supplement from the textbook

**Why the limit may have a non-continuous cdf (Example 5.2.1).** A coin is tossed; if it comes up heads a number is chosen at random between $$0$$ and $$1 + n^{-1}$$ and shown, and if tails, $$1 + n^{-1}$$ is shown. Then $$X_n$$ has

$$
cdf_{X_n}(x) = \begin{cases}0, & x < 0 \\ \frac{1}{2}\frac{1}{1+n^{-1}}x, & 0 \le x < 1 + n^{-1} \\ 1, & x \ge 1 + n^{-1}\end{cases}
\qquad\text{and}\qquad G(x) = \lim_{n\to\infty}cdf_{X_n}(x) = \begin{cases}0, & x < 0 \\ \frac{1}{2}x, & 0 \le x \le 1 \\ 1, & x > 1,\end{cases}
$$

which is not right-continuous at $$x = 1$$ and hence not a cdf. Modifying it at $$x = 1$$ gives the cdf $$F(x) = 0$$ ($$x < 0$$), $$\frac{1}{2}x$$ ($$0 \le x < 1$$), $$1$$ ($$x \ge 1$$) of the experiment in which, for tails, the number $$1$$ is shown; then $$\lim cdf_{X_n}(x) = F(x)$$ for all $$x \ne 1$$.

> **Limiting distribution (textbook definition).** For a sequence $$X_n$$ and $$Z$$, if $$\lim P(X_n \le x) = P(Z \le x)$$ holds at every point $$x$$ at which $$cdf_Z$$ is continuous, the distribution of $$Z$$ is the *limiting distribution* or *asymptotic distribution* of the distributions of $$X_n$$, written $$X_n \xrightarrow{d} Z$$.
{: .definition #def-limiting-distribution }

**Example 5.2.2 (Poisson approximation of the binomial distribution).** For $$X_n \sim B(n, \lambda/n)$$ ($$0 < \lambda/n < 1$$) and $$X \sim \mathrm{Poisson}(\lambda)$$, $$P(X_n = k) = \binom{n}{k}(\frac{\lambda}{n})^k(1 - \frac{\lambda}{n})^{n-k} \to \frac{1}{k!}\lambda^ke^{-\lambda} = P(X = k)$$. Both take values $$0$$ or natural numbers, so $$cdf_{X_n}(x) = \sum_{k : 0 \le k \le x}P(X_n = k) \to cdf_X(x)$$ at every point; that is, $$B(n, \lambda/n) \approx \mathrm{Poisson}(\lambda)$$, $$n \to \infty$$.

**Example 5.2.3 (Order statistics of the uniform distribution).** For $$U_{(1)} < \cdots < U_{(n)}$$ from $$U(0, 1)$$, $$P\{n(1 - U_{(n)}) \le x\} = 1 - P\{U_{(n)} < 1 - \frac{x}{n}\}$$, and $$P\{U_{(n)} < 1 - \frac{x}{n}\} = (1 - \frac{x}{n})^n$$ for $$0 < x \le n$$, which tends to $$e^{-x}$$ ($$x > 0$$) and equals $$1$$ for $$x \le 0$$. Hence $$\lim P\{n(1 - U_{(n)}) \le x\} = 1 - e^{-x}$$ ($$x \ge 0$$), $$0$$ ($$x < 0$$), that is, $$n(1 - U_{(n)}) \xrightarrow{d} Z$$, $$Z \sim \mathrm{Exp}(1)$$.

> **Theorem 5.2.1 (Limiting distribution that is a constant).** For a sequence $$X_n$$ and a constant $$c$$,
>
> $$
> X_n \xrightarrow{d} X,\ P(X = c) = 1 \iff \lim_{n\to\infty}P(\lvert X_n - c\rvert \ge \epsilon) = 0\ \ \forall\epsilon > 0.
> $$
{: .theorem #thm-constant-limit }

*Proof.* If $$P(X = c) = 1$$, then $$cdf_X(x) = 0$$ ($$x < c$$), $$1$$ ($$x \ge c$$), which is continuous at every point except $$x = c$$. ($$\Rightarrow$$) By the definition, $$\lim cdf_{X_n}(x) = cdf_X(x)$$ for all $$x \ne c$$, so for every $$\epsilon > 0$$: $$\lim P(X_n \le c - \epsilon) = cdf_X(c - \epsilon) = 0$$ and $$0 \le \lim P(X_n \ge c + \epsilon) \le \lim P(X_n > c + \epsilon/2) = 1 - cdf_X(c + \epsilon/2) = 0$$; hence $$\lim P(\lvert X_n - c\rvert \ge \epsilon) = 0$$. ($$\Leftarrow$$) $$0 \le cdf_{X_n}(c - \epsilon) = P(X_n \le c - \epsilon) \le P(\lvert X_n - c\rvert \ge \epsilon) \to 0$$ and $$0 \le 1 - cdf_{X_n}(c + \epsilon) = P(X_n > c + \epsilon) \le P(\lvert X_n - c\rvert \ge \epsilon) \to 0$$, so $$\lim cdf_{X_n}(x) = cdf_X(x)$$ for all $$x \ne c$$. $$\square$$

(This is why the textbook defines convergence in probability to a constant $$c$$, $$\mathrm{plim}\,X_n = c$$, by the condition of this theorem.)

> **Theorem 5.3.1 (Slutsky's theorem).** For random variables $$X_n, Y_n$$ ($$n = 1, 2, \dots$$), $$Z$$ and a real constant $$c$$, if $$X_n \xrightarrow{d} Z$$ and $$\mathrm{plim}\,Y_n = c$$, then
>
> - (a) $$X_n + Y_n \xrightarrow{d} Z + c$$, (b) $$X_n - Y_n \xrightarrow{d} Z - c$$, (c) $$Y_nX_n \xrightarrow{d} cZ$$, (d) $$X_n/Y_n \xrightarrow{d} Z/c$$ ($$c \ne 0$$).
{: .theorem #thm-slutsky }

*Proof (when the cdf of $$Z$$ is continuous).* (a) For $$\epsilon > 0$$, $$P(X_n + Y_n \le z) = P(X_n + Y_n \le z, \lvert Y_n - c\rvert < \epsilon) + P(X_n + Y_n \le z, \lvert Y_n - c\rvert \ge \epsilon) \le P(X_n \le z - c + \epsilon) + P(\lvert Y_n - c\rvert \ge \epsilon)$$, so $$\overline{\lim}\,P(X_n + Y_n \le z) \le P(Z \le z - c + \epsilon) \xrightarrow{\epsilon\downarrow0} P(Z + c \le z)$$. In the same way, $$P(X_n + Y_n > z) \le P(X_n > z - c - \epsilon) + P(\lvert Y_n - c\rvert \ge \epsilon)$$ gives $$\overline{\lim}\,P(X_n + Y_n > z) \le P(Z > z - c - \epsilon)$$, so $$\underline{\lim}\,P(X_n + Y_n \le z) \ge P(Z \le z - c - \epsilon) \to P(Z + c \le z)$$. Therefore $$\lim P(X_n + Y_n \le z) = P(Z + c \le z)$$. (b) follows from (a), as $$\mathrm{plim}(-Y_n) = -c$$. (c) First let $$c = 0$$: for $$\epsilon > 0$$ and $$k > 0$$, $$P(\lvert Y_nX_n\rvert \ge \epsilon) \le P(\lvert X_n\rvert > k) + P(k\lvert Y_n\rvert \ge \epsilon) \le P(X_n > k) + P(X_n \le -k) + P(\lvert Y_n\rvert \ge \epsilon/k)$$, so $$0 \le \overline{\lim}\,P(\lvert Y_nX_n\rvert \ge \epsilon) \le P(Z > k) + P(Z \le -k) \xrightarrow{k\uparrow\infty} 0$$, that is, $$\mathrm{plim}\,Y_nX_n = 0$$. For general $$c$$, $$(Y_n - c)X_n \xrightarrow{P} 0$$ and $$cX_n \xrightarrow{d} cZ$$, so by (a), $$Y_nX_n = (Y_n - c)X_n + cX_n \xrightarrow{d} cZ$$. (d) $$\mathrm{plim}\,1/Y_n = 1/c$$, and (c) applies. $$\square$$

> **Theorem 5.3.2 (Continuous function and limiting distribution).** For $$X_n = (X_{n1}, \dots, X_{nk})^t \xrightarrow{d} Z = (Z_1, \dots, Z_k)^t$$ and a continuous function $$g$$, $$g(X_n) \xrightarrow{d} g(Z)$$. (The proof is beyond the level of the book.)
{: .theorem #thm-continuous-mapping }

**Limiting distribution of a vector.** $$X_n \xrightarrow{d} Z$$ for $$X_n = (X_{n1}, \dots, X_{nk})^t$$ means $$\lim P(X_{n1} \le x_1, \dots, X_{nk} \le x_k) = P(Z_1 \le x_1, \dots, Z_k \le x_k)$$ at every point $$x$$ at which the joint cdf of $$Z$$ is continuous.

## References

- 김우철, *수리통계학* (Mathematical Statistics), revised 2nd edition, 민영사, 2021 — Chapter 5, §5.2 (Examples 5.2.1 to 5.2.3, Theorem 5.2.1) and §5.3 (Theorems 5.3.1 and 5.3.2). The supplement is translated from the book.
- Mathematical Statistics 1 (326.311), Seoul National University, Spring 2025. Instructor: Jaeyong Lee (이재용).

[Previous](/posts/mathstat1-convergence-in-probability/) · [Overview](/posts/mathstat1-overview/) · [Next](/posts/mathstat1-central-limit-theorem/)
