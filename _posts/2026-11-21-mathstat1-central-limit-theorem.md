---
title: "Mathematical Statistics 1: Ch. 5 Part 3 — The Central Limit Theorem"
date: 2026-11-21 13:30:00 +0900
categories: [Study Notes, Mathematical Statistics 1]
tags: [central limit theorem, normal approximation, poisson, gamma, chi-square, multinomial]
description: The central limit theorem for iid random variables and its proof through the moment generating function, normal approximations of the Poisson, gamma and chi-square distributions, and the multivariate central limit theorem with the multinomial example. Chapter 5, §5.1 of Mathematical Statistics 1.
math: true
mermaid: false
render_with_liquid: false
---

> My handwritten notes for Chapter 5 begin with convergence in probability and do not cover the central limit theorem, so this post is **translated from the textbook**, §5.1. It is not my own writing. The exercises are in [Chapter 5 Exercises](/posts/mathstat1-exercises-chapter-5/).
{: .prompt-info }

## 5.1 The central limit theorem

The approximation expressing the cumulative probability of the binomial distribution by the probability of the standard normal distribution,

$$
\sum_{x : a \le \frac{x - np}{\sqrt{np(1-p)}} \le b}\binom{n}{x}p^x(1 - p)^{n-x} \sim \int_a^b\frac{1}{\sqrt{2\pi}}e^{-\frac{1}{2}z^2}\,dz, \qquad n \to \infty,
$$

was introduced in §3.6. For a random sample $$X_1, \dots, X_n$$ from the Bernoulli distribution with defective rate $$p$$, the number of defectives $$X_1 + \cdots + X_n$$ follows $$B(n, p)$$, so for $$Z \sim N(0, 1)$$

$$
\lim_{n\to\infty}P\Bigl(a \le \frac{X_1 + \cdots + X_n - np}{\sqrt{np(1-p)}} \le b\Bigr) = P(a \le Z \le b),
$$

that is, for the sample proportion $$\hat{p} = (X_1 + \cdots + X_n)/n$$, $$\lim P\bigl(a \le \frac{\hat{p} - p}{\sqrt{p(1-p)/n}} \le b\bigr) = P(a \le Z \le b)$$. Probability approximations for a statistic are often given by the standard normal distribution in this way, and the most basic and useful statistic of this kind is the sample mean.

> **Theorem 5.1.1 (Central limit theorem).** Let the random variables $$X_1, \dots, X_n$$ be independent with the same distribution and $$\mathrm{Var}(X_1)$$ a positive real number, and
>
> $$
> E(X_1) = \mu, \quad \mathrm{Var}(X_1) = \sigma^2 \quad (0 < \sigma < +\infty).
> $$
>
> Then for a random variable $$Z \sim N(0, 1)$$,
>
> $$
> \lim_{n\to\infty}P\Bigl(\frac{(X_1 + \cdots + X_n)/n - \mu}{\sigma/\sqrt{n}} \le x\Bigr) = P(Z \le x) \qquad \forall x : -\infty < x < +\infty.
> $$
{: .theorem #thm-clt }

*Proof.* The theorem holds in general under the given conditions, but its proof is beyond this book's level, so we treat only the case where the mgf of $$X_1$$ exists, as an additional condition. Instead of approximating the cumulative probability of the standardized sample mean $$\sqrt{n}(\bar{X}_n - \mu)/\sigma$$, we show that its mgf can be approximated by $$mgf_Z(t) = \exp(t^2/2)$$. (In general it is known that if the cdf of $$Z$$ is continuous, then $$\lim mgf_{Z_n}(t) = mgf_Z(t)$$ for all $$t$$ with $$\lvert t\rvert < h$$ ($$\exists h > 0$$) implies $$\lim P(Z_n \le x) = P(Z \le x)$$ for all $$x$$.) That is, we show

$$
\lim_{n\to\infty}mgf_{\sqrt{n}(\bar{X}_n - \mu)/\sigma}(t) = mgf_Z(t) = \exp(t^2/2).
$$

By the definition of the mgf and the property of sums of independent random variables (Theorem 2.5.11),

$$
mgf_{\sqrt{n}(\bar{X}_n-\mu)/\sigma}(t) = E\Bigl[\exp\Bigl\{\frac{t}{\sqrt{n}}\Bigl(\frac{X_1 - \mu}{\sigma} + \cdots + \frac{X_n - \mu}{\sigma}\Bigr)\Bigr\}\Bigr] = \Bigl\{E\Bigl[\exp\Bigl(\frac{t}{\sqrt{n}}\frac{X_1 - \mu}{\sigma}\Bigr)\Bigr]\Bigr\}^n = \bigl[mgf_{(X_1-\mu)/\sigma}(t/\sqrt{n})\bigr]^n.
$$

Here if $$m(s) = mgf_{(X_1-\mu)/\sigma}(s)$$, then by the properties of the mgf and Taylor's theorem

$$
m\Bigl(\frac{t}{\sqrt{n}}\Bigr) = m(0) + \frac{m^{(1)}(0)}{1!}\frac{t}{\sqrt{n}} + \frac{m^{(2)}(0)}{2!}\Bigl(\frac{t}{\sqrt{n}}\Bigr)^2 + R_{n,t} = 1 + E\Bigl(\frac{X_1 - \mu}{\sigma}\Bigr)\frac{t}{\sqrt{n}} + E\Bigl[\Bigl(\frac{X_1 - \mu}{\sigma}\Bigr)^2\Bigr]\frac{t^2}{2n} + R_{n,t},
$$

where $$R_{n,t}\bigm/\bigl(\frac{t}{\sqrt{n}}\bigr)^2 \to 0$$. Hence $$m(t/\sqrt{n}) = 1 + \frac{1}{2}\frac{t^2}{n} + R_{n,t}$$ with $$\lim nR_{n,t} = 0$$. Therefore (using $$\log(1 + x) = x + R(x)$$, $$\lim_{x\to0}R(x)/x = 0$$)

$$
\log mgf_{\sqrt{n}(\bar{X}_n-\mu)/\sigma}(t) = n\log\Bigl(1 + \frac{1}{2}\frac{t^2}{n} + R_{n,t}\Bigr) = n\Bigl\{\frac{1}{2}\frac{t^2}{n} + r_{n,t}\Bigr\}, \quad \lim nr_{n,t} = 0,
$$

so $$\lim mgf_{\sqrt{n}(\bar{X}_n-\mu)/\sigma}(t) = \exp(t^2/2)$$. $$\square$$

**Example 5.1.1.**

(a) *(Normal approximation of the Poisson distribution.)* For independent $$X_1, \dots, X_n \sim \mathrm{Poisson}(\lambda)$$, $$E(X_1) = \mathrm{Var}(X_1) = \lambda$$ ($$0 < \lambda < +\infty$$), so

$$
\lim P\Bigl(\frac{(X_1 + \cdots + X_n)/n - \lambda}{\sqrt{\lambda/n}} \le x\Bigr) = P(Z \le x), \quad Z \sim N(0, 1).
$$

Since $$X_1 + \cdots + X_n \sim \mathrm{Poisson}(n\lambda)$$, $$\lim\sum_{k : \frac{k - n\lambda}{\sqrt{n\lambda}} \le x}\frac{e^{-n\lambda}(n\lambda)^k}{k!} = \int_{-\infty}^x\frac{1}{\sqrt{2\pi}}e^{-z^2/2}\,dz$$. Hence if $$Y_n \sim \mathrm{Poisson}(n)$$ and $$n$$ is large enough, with the cdf $$\Phi$$ of the standard normal distribution,

$$
P(a < Y_n \le b) \simeq \Phi\Bigl(\frac{b - n}{\sqrt{n}}\Bigr) - \Phi\Bigl(\frac{a - n}{\sqrt{n}}\Bigr).
$$

(This approximation is possible because the convergence to the normal distribution in the central limit theorem is uniform; see Exercise 5.9.)

(b) *(Normal approximation of the gamma or chi-squared distribution.)* For independent $$X_1, \dots, X_n \sim \mathrm{Gamma}(\alpha, \beta)$$, $$E(X_1) = \alpha\beta$$, $$\mathrm{Var}(X_1) = \alpha\beta^2$$, so $$\lim P\bigl(\frac{(X_1 + \cdots + X_n)/n - \alpha\beta}{\sqrt{\alpha\beta^2/n}} \le x\bigr) = P(Z \le x)$$. If $$Y_n \sim \chi^2(n)$$, then $$Y_n \overset{d}{=} X_1 + \cdots + X_n$$, $$X_i \overset{iid}{\sim} \chi^2(1) = \mathrm{Gamma}(1/2, 2)$$, so $$\lim P\bigl(\frac{Y_n - n}{\sqrt{2n}} \le x\bigr) = P(Z \le x)$$, and for large $$n$$, $$P(a < Y_n \le b) \simeq \Phi\bigl(\frac{b - n}{\sqrt{2n}}\bigr) - \Phi\bigl(\frac{a - n}{\sqrt{2n}}\bigr)$$.

The central limit theorem also holds for multivariate random variables and plays a key role in approximating the sampling distributions of many statistics. Its proof is the same as in one dimension.

> **Theorem 5.1.2 (Central limit theorem for the multivariate case).** If $$X_1 = (X_{11}, \dots, X_{1k})^t, \dots, X_n = (X_{n1}, \dots, X_{nk})^t$$ are independent with the same distribution and the variance matrix $$\mathrm{Var}(X_1)$$ exists, with
>
> $$
> E(X_1) = \mu, \quad \mathrm{Var}(X_1) = \Sigma,
> $$
>
> then for $$Z = (Z_1, \dots, Z_k)^t \sim N_k(0, \Sigma)$$,
>
> $$
> \lim_{n\to\infty}P\bigl\{\sqrt{n}((X_{1j} + \cdots + X_{nj})/n - \mu_j) \le x_j,\ j = 1, \dots, k\bigr\} = P(Z_1 \le x_1, \dots, Z_k \le x_k) \quad \forall x_j.
> $$
{: .theorem #thm-clt-multivariate }

(In abbreviated form, $$\lim P\{\sqrt{n}((X_1 + \cdots + X_n)/n - \mu) \le x\} = P(Z \le x)$$ for all $$x \in \mathbb{R}^k$$, $$Z \sim N_k(0, \Sigma)$$.)

**Example 5.1.2 (Multivariate normal approximation of the multinomial distribution).** By the representational definition, $$X_n = (X_{n1}, \dots, X_{nk})^t \sim \mathrm{Multi}(n, (p_1, \dots, p_k)^t)$$ satisfies $$X_n \overset{d}{=} Z_1 + \cdots + Z_n$$, $$Z_i \overset{iid}{\sim} \mathrm{Multi}(1, (p_1, \dots, p_k)^t)$$. With $$D(p_j)$$ the diagonal matrix with diagonal elements $$p_1, \dots, p_k$$, Theorem 3.2.2 gives $$E(Z_1) = p = (p_1, \dots, p_k)^t$$ and $$\mathrm{Var}(Z_1) = D(p_j) - pp^t$$. Therefore by the central limit theorem

$$
\lim P\{(X_n - np)/\sqrt{n} \le x\} = P(Z \le x), \quad Z \sim N_k(0, D(p_j) - pp^t).
$$

Note that the variance matrix $$D(p_j) - pp^t$$ is a singular matrix with no inverse.

## References

- 김우철, *수리통계학* (Mathematical Statistics), revised 2nd edition, 민영사, 2021 — Chapter 5, §5.1 (Theorems 5.1.1 and 5.1.2, Examples 5.1.1 and 5.1.2). Translated from the book; not from my notes.
- Mathematical Statistics 1 (326.311), Seoul National University, Spring 2025. Instructor: Jaeyong Lee (이재용).

[Previous](/posts/mathstat1-convergence-in-distribution/) · [Overview](/posts/mathstat1-overview/) · [Next](/posts/mathstat1-limiting-distributions/)
