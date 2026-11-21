---
title: "Mathematical Statistics 1: Ch. 5 Part 5 — Approximation by Simulation"
date: 2026-11-21 13:50:00 +0900
categories: [Study Notes, Mathematical Statistics 1]
tags: [simulation, random numbers, monte carlo, confidence interval, inverse transform, pi]
description: Generating random numbers from a distribution with the inverse cdf, Monte Carlo integration, and approximating a variance and the number pi by simulation, with asymptotic confidence intervals for the sample proportion. Chapter 5, §5.4 of Mathematical Statistics 1.
math: true
mermaid: false
render_with_liquid: false
---

> My handwritten notes for Chapter 5 do not cover this section, so this post is **translated from the textbook**, §5.4. It is not my own writing. The exercises are in [Chapter 5 Exercises](/posts/mathstat1-exercises-chapter-5/).
{: .prompt-info }

## 5.4 Approximation by simulation

In this section we see how to approximate the distribution of a statistic, or to study its properties, using the observed values of random samples. Observed values of a random variable with a particular distribution are commonly called *random numbers*, and recent statistical packages have functions that can generate them.

The basis for generating random numbers is observed values from the uniform distribution $$U(0, 1)$$, called *uniform random numbers* (Appendix III describes the R function that generates them). From such uniform random numbers, using the probability integral transformation of Theorem 4.3.3, random numbers from an arbitrary distribution can be generated.

**Example 5.4.1 (Generating random numbers from the logistic distribution).** The pdf and cdf of the logistic distribution $$L(0, 1)$$ are

$$
f(z) = \frac{e^z}{(1 + e^z)^2}, \quad F(z) = 1 - \frac{1}{1 + e^z}, \qquad -\infty < z < +\infty,
$$

so the inverse of the cdf is $$F^{-1}(u) = \log\dfrac{u}{1 - u}$$. Therefore by Theorem 4.3.3, for $$U \sim U(0, 1)$$, $$Z = \log\dfrac{U}{1 - U} \sim L(0, 1)$$, which gives random numbers from $$L(0, 1)$$. Also $$\sigma Z + \mu = \sigma\log\frac{U}{1-U} + \mu \sim L(\mu, \sigma)$$ gives the general logistic distribution $$L(\mu, \sigma)$$.

In the same way, for $$U \sim U(0, 1)$$, $$-\log(1 - U) \sim \mathrm{Exp}(1)$$ and $$\sigma\{-\log(1 - U)\} \sim \mathrm{Exp}(\sigma)$$ generate random numbers from the exponential distribution, and with the inverse $$\Phi^{-1}(u)$$ of the standard normal cdf, $$\Phi^{-1}(U) \sim N(0, 1)$$ and $$\sigma\Phi^{-1}(U) + \mu \sim N(\mu, \sigma^2)$$ generate random numbers from the normal distribution. The function that generates random numbers from many distributions in this way is packaged in R (Appendix III).

> **Theorem 5.4.1 (Approximating a definite integral with random numbers).** For $$U_1, \dots, U_n \overset{iid}{\sim} U(0, 1)$$ and a function $$g(x)$$ continuous on $$[a, b]$$,
>
> $$
> X_i = (b - a)U_i + a \overset{iid}{\sim} U(a, b) \quad (i = 1, \dots, n), \qquad \mathrm{plim}\,\frac{b - a}{n}\sum_{i=1}^{n}g(X_i) = \int_a^bg(x)\,dx.
> $$
{: .theorem #thm-monte-carlo }

*Proof.* $$X_1, \dots, X_n$$ are independent with pdf $$\frac{1}{b-a}I_{(a,b)}(x)$$, so $$E[g(X_1)] = \frac{1}{b-a}\int_a^bg(x)\,dx$$. By the law of large numbers, $$\mathrm{plim}\,\frac{b-a}{n}\sum g(X_i) = (b - a)E[g(X_1)] = \int_a^bg(x)\,dx$$. $$\square$$

The method of finding an approximate value of a definite integral with the convergence in probability of Theorem 5.4.1 is called *Monte Carlo integration*. With independently generated uniform random numbers $$u_1, \dots, u_n$$,

$$
y_i = (b - a)g((b - a)u_i + a) \ (i = 1, \dots, n), \qquad \int_a^bg(x)\,dx \simeq \frac{1}{n}\sum_{i=1}^{n}y_i, \quad n \to \infty.
$$

Since this uses the observed values of $$Y_i = (b - a)g((b - a)U_i + a)$$ to infer $$E(Y_1)$$, the precision of the approximation can be expressed by an asymptotic confidence interval for $$E(Y_1)$$.

**Example 5.4.2.** By the integration formula, the definite integral $$\int_1^3x^2\,dx$$ equals $$26/3$$. With independently generated uniform random numbers $$u_1, \dots, u_n$$ from $$U(0, 1)$$, let $$x_i = 2u_i + 1$$, $$y_i = 2x_i^2$$ ($$i = 1, \dots, n$$); then $$\int_1^3x^2\,dx \simeq \frac{2}{n}\sum x_i^2 = \frac{1}{n}\sum y_i$$. Using random numbers generated with the R package, the approximate value and the $$95\%$$ asymptotic confidence interval of this integral are as follows (Table 5.4.1, $$\int_1^3x^2\,dx = 8.666\ldots$$). As the number of random numbers $$n$$ grows, the precision of the approximation improves.

- $$n = 100$$: $$\bar{y} = 8.7612$$, interval $$(7.8241,\ 9.6983)$$
- $$n = 1000$$: $$\bar{y} = 8.5633$$, interval $$(8.2728,\ 8.8538)$$
- $$n = 10000$$: $$\bar{y} = 8.6515$$, interval $$(8.5604,\ 8.7426)$$
- $$n = 100000$$: $$\bar{y} = 8.6473$$, interval $$(8.6185,\ 8.6762)$$

(the interval is $$\bar{y} \mp 1.96s_y/\sqrt{n}$$).

**Example 5.4.3 (Variance of the logistic distribution).** The logistic distribution $$L(0, 1)$$ is symmetric about $$x = 0$$ and its variance is

$$
\int_{-\infty}^{+\infty}x^2\frac{e^x}{(1 + e^x)^2}\,dx = \frac{\pi^2}{3}
$$

(by integration by parts and expansion in an infinite series, $$\int_{-\infty}^{+\infty}x^2\frac{e^x}{(1+e^x)^2}\,dx = 4\int_0^{\infty}\frac{e^{-x}}{1 + e^{-x}}x\,dx = 4\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n^2}$$, and the value of the series follows from the Fourier series $$x^2 = \frac{1}{3}\pi^2 + 4\sum_{n=1}^{\infty}\frac{(-1)^n}{n^2}\cos(nx)$$, $$-\pi \le x \le \pi$$, at $$x = 0$$). On the other hand, by Example 5.4.1, for $$U \sim U(0, 1)$$, $$X = \log\frac{U}{1 - U} \sim L(0, 1)$$, so with independently generated uniform random numbers $$u_1, \dots, u_n$$, $$x_i = \log\frac{u_i}{1 - u_i}$$, $$y_i = x_i^2$$,

$$
\int_{-\infty}^{+\infty}x^2\frac{e^x}{(1 + e^x)^2}\,dx = E(X^2) \simeq \frac{1}{n}\sum x_i^2 = \frac{1}{n}\sum y_i.
$$

The approximate value and $$95\%$$ asymptotic confidence interval of $$\pi^2/3 = 3.289\ldots$$ (Table 5.4.2):

- $$n = 100$$: $$\bar{y} = 2.9775$$, interval $$(2.0043,\ 3.9506)$$
- $$n = 1000$$: $$\bar{y} = 3.3375$$, interval $$(2.9799,\ 3.6951)$$
- $$n = 10000$$: $$\bar{y} = 3.3201$$, interval $$(3.2034,\ 3.4369)$$
- $$n = 100000$$: $$\bar{y} = 3.2949$$, interval $$(3.2584,\ 3.3313)$$

**Example 5.4.4 (Limiting distribution of the sample proportion).** For $$n$$ independent Bernoulli trials with rate $$p$$ ($$0 < p < 1$$), the results $$X_1, \dots, X_n$$ and the sample proportion $$\hat{p}_n = (X_1 + \cdots + X_n)/n$$ satisfy, by the law of large numbers and the central limit theorem,

$$
\mathrm{plim}\,\hat{p}_n = p, \qquad \frac{\hat{p}_n - p}{\sqrt{p(1-p)/n}} \xrightarrow{d} Z, \quad Z \sim N(0, 1).
$$

Therefore by Slutsky's theorem and Theorem 5.3.2, $$\dfrac{\hat{p}_n - p}{\sqrt{\hat{p}_n(1 - \hat{p}_n)/n}} \xrightarrow{d} Z$$, and

$$
\lim P\Bigl(-z_{\alpha/2} \le \frac{\hat{p}_n - p}{\sqrt{\hat{p}_n(1 - \hat{p}_n)/n}} \le z_{\alpha/2}\Bigr) = 1 - \alpha, \quad\therefore\quad \lim P\bigl\{\hat{p}_n - z_{\alpha/2}\sqrt{\hat{p}_n(1 - \hat{p}_n)/n} \le p \le \hat{p}_n + z_{\alpha/2}\sqrt{\hat{p}_n(1 - \hat{p}_n)/n}\bigr\} = 1 - \alpha.
$$

From this, a $$100(1 - \alpha)\%$$ asymptotic confidence interval for the population proportion $$p$$ is $$p \in \bigl[\hat{p}_n - z_{\alpha/2}\sqrt{\hat{p}_n(1 - \hat{p}_n)/n},\ \hat{p}_n + z_{\alpha/2}\sqrt{\hat{p}_n(1 - \hat{p}_n)/n}\bigr]$$.

**Example 5.4.5 (Approximating $$\pi$$ with the limiting distribution of the sample proportion).** Observing the point $$(U_1, U_2)$$ for two independent $$U(0, 1)$$ random variables $$U_1, U_2$$ is thought of as dropping a point at random into the unit square. The probability that the point falls into the quarter disc is $$P(U_1^2 + U_2^2 \le 1) = \pi/4$$. Repeating the experiment independently, by the law of large numbers the relative frequency of points falling in the quarter disc approaches $$\pi/4$$. So with independently generated uniform random numbers $$u_{11}, u_{12}; \dots; u_{n1}, u_{n2}$$, $$x_i = u_{i1}^2 + u_{i2}^2$$, the observed value of the sample proportion $$\hat{p}_n = \frac{1}{n}\sum I_{(x_i \le 1)}$$ approximates $$p = P(U_1^2 + U_2^2 \le 1) = \pi/4$$, and $$4\hat{p}_n$$ approximates $$4p = \pi$$; the asymptotic confidence interval of Example 5.4.4 shows the precision of the approximation. The approximate value of $$4p = \pi$$ ($$3.14159\ldots$$) and the $$95\%$$ asymptotic confidence interval (Table 5.4.3):

- $$n = 100$$: $$4\hat{p}_n = 3.3600$$, interval $$(3.0755,\ 3.6445)$$
- $$n = 1000$$: $$4\hat{p}_n = 3.1320$$, interval $$(3.0308,\ 3.2331)$$
- $$n = 10000$$: $$4\hat{p}_n = 3.1344$$, interval $$(3.1024,\ 3.1664)$$
- $$n = 100000$$: $$4\hat{p}_n = 3.1452$$, interval $$(3.1351,\ 3.1552)$$

(the interval is $$4\hat{p}_n \mp 4 \times 1.96\sqrt{\hat{p}_n(1 - \hat{p}_n)/n}$$).

## References

- 김우철, *수리통계학* (Mathematical Statistics), revised 2nd edition, 민영사, 2021 — Chapter 5, §5.4 (Examples 5.4.1 to 5.4.5, Theorem 5.4.1). Translated from the book; not from my notes.
- Mathematical Statistics 1 (326.311), Seoul National University, Spring 2025. Instructor: Jaeyong Lee (이재용).

[Previous](/posts/mathstat1-limiting-distributions/) · [Overview](/posts/mathstat1-overview/) · [Chapter 5 Exercises](/posts/mathstat1-exercises-chapter-5/)
