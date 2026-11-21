---
title: "Mathematical Statistics 1: Ch. 3 Part 5 — Normal Distribution and Summary of Distributions"
date: 2026-11-21 11:50:00 +0900
categories: [Study Notes, Mathematical Statistics 1]
tags: [normal distribution, standard normal, quantile, summary of distributions]
description: The normal distribution and its properties, the standard normal cdf and quantiles, and summaries of the pdfs, representational definitions and generating functions of the distributions of Chapter 3. Chapter 3, §3.6 of Mathematical Statistics 1.
math: true
mermaid: false
render_with_liquid: false
---

> My handwritten notes for Chapter 3 end with the Dirichlet distribution and do not cover the normal distribution, so this post is **translated from the textbook**, §3.6 and the two summary pages that end the chapter. It is not my own writing. The exercises are in [Chapter 3 Exercises](/posts/mathstat1-exercises-chapter-3/).
{: .prompt-info }

## 3.6 Normal distribution

The approximation expressing the cumulative probability of the binomial distribution by an integral (the De Moivre–Laplace theorem)

$$
\sum_{x : a \le \frac{x - np}{\sqrt{np(1 - p)}} \le b}\binom{n}{x}p^x(1 - p)^{n-x} \sim \int_a^b\frac{1}{\sqrt{2\pi}}e^{-\frac{1}{2}z^2}\,dz, \qquad n \to \infty
$$

involves the function

$$
\phi(z) = \frac{1}{\sqrt{2\pi}}e^{-\frac{1}{2}z^2}, \qquad -\infty < z < +\infty,
$$

whose integral value is $$1$$ (found with polar coordinates), and which is called the pdf of the *standard normal distribution*. In general, the function

$$
\frac{1}{\sigma}\phi\Bigl(\frac{x - \mu}{\sigma}\Bigr) = \frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{1}{2}\frac{(x - \mu)^2}{\sigma^2}}, \qquad -\infty < x < +\infty\ (\mu \text{ real},\ \sigma \text{ positive})
$$

is the pdf of the *normal distribution*, written $$N(\mu, \sigma^2)$$. The probabilities of the normal distribution can be computed with the R language (Appendix III), and the shape can be drawn (Figure 3.6.1: $$N(-5, 1)$$, $$N(-5, 3)$$, $$N(5, 1)$$, $$N(5, 3)$$). The shape is a bell-shaped curve symmetric about $$x = \mu$$, with $$\sigma$$ expressing the degree of spread of the distribution.

> **Theorem 3.6.1 (Properties of the normal distribution).**
>
> - (a) If $$X \sim N(\mu, \sigma^2)$$, then $$E(X) = \mu$$ and $$\mathrm{Var}(X) = \sigma^2$$.
> - (b) If $$X \sim N(\mu, \sigma^2)$$, its moment generating function is $$mgf_X(t) = e^{\mu t + \frac{1}{2}\sigma^2t^2}$$, $$-\infty < t < +\infty$$.
> - (c) If $$X_1 \sim N(\mu_1, \sigma_1^2)$$, $$X_2 \sim N(\mu_2, \sigma_2^2)$$ and $$X_1, X_2$$ are mutually independent, then $$X_1 + X_2 \sim N(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)$$.
{: .theorem #thm-normal-properties }

*Proof.* (a) Substituting $$\frac{x - \mu}{\sigma} = z$$ and using $$\phi(z) = \frac{1}{\sqrt{2\pi}}e^{-\frac{1}{2}z^2}$$,

$$
E(X) = \int_{-\infty}^{+\infty}x\frac{1}{\sigma}\phi\Bigl(\frac{x - \mu}{\sigma}\Bigr)dx = \sigma\int_{-\infty}^{+\infty}z\phi(z)\,dz + \mu.
$$

Substituting $$z^2/2 = y$$, $$\int_{-\infty}^{+\infty}z\phi(z)\,dz = -\frac{1}{\sqrt{2\pi}}\int_0^{+\infty}e^{-y}\,dy + \frac{1}{\sqrt{2\pi}}\int_0^{+\infty}e^{-y}\,dy = 0$$, so $$E(X) = \mu$$. In the same way

$$
\mathrm{Var}(X) = \int_{-\infty}^{+\infty}(x - \mu)^2\frac{1}{\sigma}\phi\Bigl(\frac{x - \mu}{\sigma}\Bigr)dx = \sigma^2\int_{-\infty}^{+\infty}z^2\phi(z)\,dz, \qquad \int_{-\infty}^{+\infty}z^2\phi(z)\,dz = 2\int_0^{+\infty}z^2\phi(z)\,dz = \frac{2}{\sqrt{2\pi}}\int_0^{+\infty}\sqrt{2y}\,e^{-y}\,dy = \frac{2\Gamma(3/2)}{\sqrt{\pi}}.
$$

Here $$2\Gamma(3/2) = 2\Gamma(1/2 + 1) = 2(1/2)\Gamma(1/2) = \sqrt{\pi}$$, so $$\int_{-\infty}^{+\infty}z^2\phi(z)\,dz = 1$$ and $$\mathrm{Var}(X) = \sigma^2$$.

(b) Substituting $$\frac{x - \mu}{\sigma} = z$$,

$$
mgf_X(t) = \int_{-\infty}^{+\infty}e^{tx}\frac{1}{\sigma}\phi\Bigl(\frac{x - \mu}{\sigma}\Bigr)dx = \int_{-\infty}^{+\infty}e^{t(\sigma z + \mu)}\phi(z)\,dz.
$$

Substituting $$z - \sigma t = y$$,

$$
\int_{-\infty}^{+\infty}e^{t\sigma z}\phi(z)\,dz = \int_{-\infty}^{+\infty}\frac{1}{\sqrt{2\pi}}e^{-\frac{1}{2}(z - \sigma t)^2}\,dz\ e^{\frac{1}{2}\sigma^2t^2} = e^{\frac{1}{2}\sigma^2t^2}\int_{-\infty}^{+\infty}\frac{1}{\sqrt{2\pi}}e^{-\frac{1}{2}y^2}\,dy = e^{\frac{1}{2}\sigma^2t^2},
$$

so $$mgf_X(t) = e^{\mu t + \frac{1}{2}\sigma^2t^2}$$, $$-\infty < t < +\infty$$.

(c) From the theorem on sums of independent random variables (Theorem 2.5.11) and (b), $$mgf_{X_1 + X_2}(t) = mgf_{X_1}(t)mgf_{X_2}(t) = \exp\{(\mu_1 + \mu_2)t + \frac{1}{2}(\sigma_1^2 + \sigma_2^2)t^2\}$$. The right side is the mgf of the $$N(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)$$ distribution, so by the uniqueness of the mgf, $$X_1 + X_2 \sim N(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)$$. $$\square$$

> **Theorem 3.6.2 (Representational definition of the normal distribution).**
>
> - (a) If $$X \sim N(\mu, \sigma^2)$$, then for constants $$a, b$$, $$aX + b \sim N(a\mu + b, a^2\sigma^2)$$.
> - (b) $$X \sim N(\mu, \sigma^2) \Longleftrightarrow \dfrac{X - \mu}{\sigma} \sim N(0, 1) \Longleftrightarrow X \overset{d}{=} \sigma Z + \mu$$, $$Z \sim N(0, 1)$$.
{: .theorem #thm-normal-representational }

*Proof.* (a) The mgf of $$aX + b$$ is $$mgf_{aX+b}(t) = E[e^{t(aX + b)}] = mgf_X(at)e^{bt}$$, so $$mgf_{aX+b}(t) = \exp\{bt + \mu(at) + \frac{1}{2}\sigma^2(at)^2\} = \exp\{(a\mu + b)t + \frac{1}{2}(a^2\sigma^2)t^2\}$$. The right side is the mgf of the $$N(a\mu + b, a^2\sigma^2)$$ distribution, so by the uniqueness of the mgf, $$aX + b \sim N(a\mu + b, a^2\sigma^2)$$, and (b) is a special case of (a). $$\square$$

From these properties, the cumulative probability of the normal distribution can be found using the standard normal distribution. Writing the cdf of the standard normal distribution as

$$
\Phi(x) = \int_{-\infty}^{x}\frac{1}{\sqrt{2\pi}}e^{-z^2/2}\,dz,
$$

the cumulative probability of $$X \sim N(\mu, \sigma^2)$$ is

$$
P(X \le x) = P\Bigl(\frac{X - \mu}{\sigma} \le \frac{x - \mu}{\sigma}\Bigr) = \Phi\Bigl(\frac{x - \mu}{\sigma}\Bigr).
$$

These cumulative probabilities can be computed with R (Appendix III), and those of the standard normal distribution are given as a table in Appendix IV. For example, from the table, $$\Phi(1.64) = 0.9495$$, $$\Phi(1.65) = 0.9505$$, $$\Phi(1.96) = 0.9750$$. Since the standard normal distribution is symmetric about $$0$$ (Figure 3.6.2), $$\Phi(-z) = 1 - \Phi(z)$$. That is, the cumulative probability below a negative number can be found: $$\Phi(-1.96) = 1 - \Phi(1.96) = 0.0250$$.

**Example 3.6.1.** When $$X \sim N(3, 4)$$, use the table of Appendix IV to find (a) $$P(5 < X \le 7)$$, (b) $$P(1 < X \le 4)$$, (c) $$P(X > 0)$$.

*Solution.* Since $$Z = \frac{X - 3}{\sqrt{4}} \sim N(0, 1)$$,

- (a) $$P(5 < X \le 7) = \Phi\bigl(\frac{7 - 3}{2}\bigr) - \Phi\bigl(\frac{5 - 3}{2}\bigr) = \Phi(2.0) - \Phi(1.0) = 0.9772 - 0.8413 = 0.1359$$.
- (b) $$P(1 < X \le 4) = \Phi\bigl(\frac{4 - 3}{2}\bigr) - \Phi\bigl(\frac{1 - 3}{2}\bigr) = \Phi(0.5) - \Phi(-1.0) = \Phi(0.5) - (1 - \Phi(1.0)) = 0.6915 - (1 - 0.8413) = 0.5328$$.
- (c) $$P(X > 0) = 1 - P(X \le 0) = 1 - \Phi\bigl(\frac{0 - 3}{2}\bigr) = 1 - \Phi(-0.5) = \Phi(0.5) = 0.6915$$.

**Upper quantile.** For $$Z \sim N(0, 1)$$, the value $$z_{\alpha}$$ satisfying $$P(Z > z_{\alpha}) = \alpha$$ ($$0 < \alpha < 1$$) is called the *upper $$\alpha$$ quantile* of the standard normal distribution (Figure 3.6.3). It can be found with R or the table of Appendix IV; for example $$z_{0.025} = 1.96$$, $$z_{0.05} = 1.645$$. So by Theorem 3.6.2, the upper $$\alpha$$ quantile of the normal distribution $$N(\mu, \sigma^2)$$ is $$\mu + \sigma z_{\alpha}$$; that is, if $$X \sim N(\mu, \sigma^2)$$, then $$P(X > \mu + \sigma z_{\alpha}) = \alpha$$.

**Example 3.6.2.** When $$X \sim N(3, 4)$$, find the quantiles $$q_{0.95}$$ and $$q_{0.025}$$ with (a) $$P(X \le q_{0.95}) = 0.95$$, (b) $$P(X \le q_{0.025}) = 0.025$$.

*Solution.* (a) Since $$P(X > q_{0.95}) = 0.05$$, $$q_{0.95} = 3 + 2z_{0.05} = 6.290$$. (b) Since $$P(X > q_{0.025}) = 0.975$$, $$q_{0.025} = 3 + 2z_{0.975} = 3 - 2z_{0.025} = -0.92$$.

> **Properties of the normal distribution.**
>
> - (1) $$N(\mu, \sigma^2) \overset{d}{=} \sigma N(0, 1) + \mu$$.
> - (2) $$aN(\mu, \sigma^2) + b \overset{d}{=} N(a\mu + b, a^2\sigma^2)$$.
> - (3) $$N(\mu_1, \sigma_1^2) \oplus N(\mu_2, \sigma_2^2) \overset{d}{=} N(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)$$.
{: .theorem #thm-normal-summary }

## Summary: the distributions of Chapter 3

**Probability density functions and representational definitions** (the book's summary page).

- **Binomial** $$B(n, p)$$, $$0 \le p \le 1$$: $$f(x) = \binom{n}{x}p^x(1 - p)^{n-x}$$, $$x = 0, 1, \dots, n$$. Representation: $$X \sim B(n, p) \Leftrightarrow X \overset{d}{=} Z_1 + \cdots + Z_n$$, $$Z_i \overset{iid}{\sim} \mathrm{Bernoulli}(p)$$.
- **Bernoulli** $$\mathrm{Bernoulli}(p)$$, $$0 \le p \le 1$$: $$f(x) = p^x(1 - p)^{1-x}$$, $$x = 0, 1$$. It is $$B(1, p)$$.
- **Negative binomial** $$\mathrm{Negbin}(r, p)$$, $$0 < p < 1$$, $$r$$ natural: $$f(x) = \binom{x - 1}{r - 1}p^r(1 - p)^{x - r}$$, $$x = r, r + 1, \dots$$. Representation: $$X \overset{d}{=} Z_1 + \cdots + Z_r$$, $$Z_i \overset{iid}{\sim} \mathrm{Geo}(p)$$.
- **Geometric** $$\mathrm{Geo}(p)$$, $$0 < p < 1$$: $$f(x) = (1 - p)^{x-1}p$$, $$x = 1, 2, \dots$$. It is $$\mathrm{Negbin}(1, p)$$.
- **Poisson** $$\mathrm{Poisson}(\lambda)$$, $$\lambda \ge 0$$: $$f(x) = e^{-\lambda}\lambda^x/x!$$, $$x = 0, 1, \dots$$.
- **Multinomial** $$\mathrm{Multi}(n, (p_1, \dots, p_k)^t)$$, $$p_j \ge 0$$, $$\sum p_j = 1$$: $$f(x_1, \dots, x_k) = \binom{n}{x_1\cdots x_k}p_1^{x_1}\cdots p_k^{x_k}$$, $$x_i = 0, \dots, n$$, $$x_1 + \cdots + x_k = n$$. Representation: $$X \overset{d}{=} Z_1 + \cdots + Z_n$$, $$Z_i \overset{iid}{\sim} \mathrm{Multi}(1, p)$$.
- **Gamma** $$\mathrm{Gamma}(\alpha, \beta)$$, $$\alpha > 0$$, $$\beta > 0$$: $$f(x) = \dfrac{1}{\Gamma(\alpha)\beta^{\alpha}}x^{\alpha-1}e^{-x/\beta}I_{(0,\infty)}(x)$$. For $$\alpha = r$$ natural: $$X \overset{d}{=} Z_1 + \cdots + Z_r$$, $$Z_i \overset{iid}{\sim} \mathrm{Exp}(\beta)$$.
- **Exponential** $$\mathrm{Exp}(1/\lambda)$$, $$\lambda > 0$$: $$f(x) = \lambda e^{-\lambda x}I_{(0,\infty)}(x)$$. It is $$\mathrm{Gamma}(1, 1/\lambda)$$.
- **Normal** $$N(\mu, \sigma^2)$$, $$\mu$$ real, $$\sigma > 0$$: $$f(x) = \dfrac{1}{\sqrt{2\pi}\sigma}e^{-\frac{1}{2}\frac{(x - \mu)^2}{\sigma^2}}$$. Representation: $$X \overset{d}{=} \sigma Z + \mu$$, $$Z \sim N(0, 1)$$.

**Moment and cumulant generating functions** (the book's summary page).

- **Binomial:** mgf $$(pe^t + q)^n$$, $$q = 1 - p$$, $$-\infty < t < +\infty$$; cgf $$n\log\{1 + p(e^t - 1)\}$$.
- **Negative binomial:** mgf $$\{pe^t(1 - qe^t)^{-1}\}^r$$, $$t < -\log q$$; cgf $$-r\log(1 - p^{-1}(1 - e^{-t}))$$.
- **Poisson:** mgf $$e^{-\lambda + \lambda e^t}$$, $$-\infty < t < +\infty$$; cgf $$-\lambda + \lambda e^t = \sum_{k=1}^{\infty}\lambda t^k/k!$$.
- **Multinomial:** mgf $$(p_1e^{t_1} + \cdots + p_ke^{t_k})^n$$; cgf $$n\log\{1 + \sum_{j=1}^{k}p_j(e^{t_j} - 1)\}$$.
- **Gamma:** mgf $$(1 - \beta t)^{-\alpha}$$, $$t < 1/\beta$$; cgf $$-\alpha\log(1 - \beta t) = \alpha\sum_{k=1}^{\infty}\frac{1}{k}\beta^kt^k$$.
- **Normal:** mgf $$e^{\mu t + \frac{1}{2}\sigma^2t^2}$$, $$-\infty < t < +\infty$$; cgf $$\mu t + \frac{1}{2}\sigma^2t^2$$.

## References

- 김우철, *수리통계학* (Mathematical Statistics), revised 2nd edition, 민영사, 2021 — Chapter 3, §3.6 (Examples 3.6.1 and 3.6.2, Theorems 3.6.1 and 3.6.2) and the two summary pages. Translated from the book; not from my notes.
- Mathematical Statistics 1 (326.311), Seoul National University, Spring 2025. Instructor: Jaeyong Lee (이재용).

[Previous](/posts/mathstat1-gamma-beta/) · [Overview](/posts/mathstat1-overview/) · [Chapter 3 Exercises](/posts/mathstat1-exercises-chapter-3/)
