---
title: "Mathematical Statistics 1: Ch. 5 Part 4 — Computing Limiting Distributions and the Delta Method"
date: 2026-11-21 13:40:00 +0900
categories: [Study Notes, Mathematical Statistics 1]
tags: [slutsky, delta method, variance stabilizing, studentized mean, chi-square approximation, sample quantile, fisher transformation]
description: Limiting distributions of the studentized sample mean, the sample variance and standard deviation, the chi-square approximation for the binomial and multinomial distributions, the first-order approximation (delta method), the sample correlation coefficient with Fisher's transformation, and the sample quantile. Chapter 5, §5.3 of Mathematical Statistics 1.
math: true
mermaid: false
render_with_liquid: false
---

> My handwritten notes for Chapter 5 do not cover this section, so this post is **translated from the textbook**, §5.3 after Slutsky's theorem (which is in the [previous part](/posts/mathstat1-convergence-in-distribution/)). It is not my own writing. The exercises are in [Chapter 5 Exercises](/posts/mathstat1-exercises-chapter-5/).
{: .prompt-info }

## 5.3 Computing limiting distributions

**Example 5.3.1 (Limiting distribution of the studentized sample mean).** Let $$\bar{X}_n$$ and $$S_n$$ be the sample mean and sample standard deviation of a random sample of size $$n$$ from a population with mean $$\mu$$ and standard deviation $$\sigma$$ ($$0 < \sigma < +\infty$$). $$\dfrac{\bar{X}_n - \mu}{S_n/\sqrt{n}}$$ is called the *studentized* sample mean. By the central limit theorem and Example 5.2.5, $$\frac{\bar{X}_n - \mu}{\sigma/\sqrt{n}} \xrightarrow{d} Z$$, $$Z \sim N(0, 1)$$, and $$\mathrm{plim}\,S_n = \sigma$$, so by Slutsky's theorem

$$
\frac{\bar{X}_n - \mu}{S_n/\sqrt{n}} = \frac{\bar{X}_n - \mu}{\sigma/\sqrt{n}}\Big/\frac{S_n}{\sigma} \xrightarrow{d} Z/1 = Z, \quad Z \sim N(0, 1).
$$

In particular, when the population is normal, the studentized sample mean follows the $$t$$-distribution with $$n - 1$$ degrees of freedom, so the result means that the $$t$$-distribution with large degrees of freedom is approximated by the standard normal distribution: $$t(n-1) \approx N(0, 1)$$, $$n \to \infty$$. Also, if the population has any positive variance,

$$
\lim P\Bigl(-z_{\alpha/2} < \frac{\bar{X}_n - \mu}{S_n/\sqrt{n}} \le z_{\alpha/2}\Bigr) = 1 - \alpha, \quad\therefore\quad P\{\bar{X}_n - z_{\alpha/2}S_n/\sqrt{n} < \mu < \bar{X}_n + z_{\alpha/2}S_n/\sqrt{n}\} \simeq 1 - \alpha, \ n \to \infty,
$$

so a $$100(1 - \alpha)\%$$ asymptotic confidence interval for the population mean $$\mu$$ is $$\mu \in [\bar{X}_n - z_{\alpha/2}S_n/\sqrt{n},\ \bar{X}_n + z_{\alpha/2}S_n/\sqrt{n})$$.

**Example 5.3.2 (Limiting distribution of the sample variance).** Let $$S_n^2$$ be the sample variance of a random sample of size $$n$$ from a population with mean $$\mu$$ and standard deviation $$\sigma$$ ($$0 < \sigma < +\infty$$). Then

$$
S_n^2 = \frac{1}{n-1}\sum[(X_i - \mu) - (\bar{X}_n - \mu)]^2 = \frac{n}{n-1}\Bigl\{\frac{1}{n}\sum(X_i - \mu)^2 - (\bar{X}_n - \mu)^2\Bigr\}.
$$

With $$Y_i = (X_i - \mu)^2$$ independent with the same distribution, the central limit theorem gives, when $$\mathrm{Var}(Y_1) < +\infty$$, $$\sqrt{n}\bigl(\frac{1}{n}\sum Y_i - E(Y_1)\bigr) \xrightarrow{d} W$$, $$W \sim N(0, \mathrm{Var}(Y_1))$$, and $$E(Y_1) = \sigma^2$$, $$\mathrm{Var}(Y_1) = E[(X_1 - \mu)^4] - \sigma^4$$. So if $$E[(X_1 - \mu)^4] < +\infty$$,

$$
\sqrt{n}\Bigl\{\frac{1}{n}\sum(X_i - \mu)^2 - \sigma^2\Bigr\} \xrightarrow{d} W, \quad W \sim N(0, E[(X_1 - \mu)^4] - \sigma^4).
$$

Also by the central limit theorem and the law of large numbers, $$\sqrt{n}(\bar{X}_n - \mu) \xrightarrow{d} Z$$, $$Z \sim N(0, \sigma^2)$$, $$\mathrm{plim}(\bar{X}_n - \mu) = 0$$, so by Slutsky's theorem and Theorem 5.2.1, $$\sqrt{n}(\bar{X}_n - \mu)(\bar{X}_n - \mu) \xrightarrow{d} 0 \times Z = 0$$, that is, $$\mathrm{plim}\,\sqrt{n}(\bar{X}_n - \mu)^2 = 0$$. Therefore, if $$E[(X_1 - \mu)^4] < +\infty$$,

$$
\sqrt{n}\Bigl(\frac{1}{n}\sum(X_i - \bar{X})^2 - \sigma^2\Bigr) = \sqrt{n}\Bigl\{\frac{1}{n}\sum(X_i - \mu)^2 - \sigma^2\Bigr\} - \sqrt{n}(\bar{X}_n - \mu)^2 \xrightarrow{d} W - 0 = W.
$$

Hence if $$\rho_4 = E\bigl[\bigl(\frac{X_1 - \mu}{\sigma}\bigr)^4\bigr] - 3$$ (the *kurtosis* of the population, a measure of how densely the distribution is concentrated near the mean, equal to $$0$$ for a normal population),

$$
\sqrt{n}(S_n^2 - \sigma^2) = \sqrt{n}\Bigl\{\frac{1}{n}\sum(X_i - \bar{X})^2 - \sigma^2\Bigr\} + \frac{1}{\sqrt{n}}S_n^2 \xrightarrow{d} W, \quad W \sim N(0, (\rho_4 + 2)\sigma^4).
$$

**Limiting distribution of a vector.** For a sequence of random vectors $$X_n = (X_{n1}, \dots, X_{nk})^t$$ and $$Z = (Z_1, \dots, Z_k)^t$$, $$\lim P(X_{n1} \le x_1, \dots, X_{nk} \le x_k) = P(Z_1 \le x_1, \dots, Z_k \le x_k)$$ at all points $$x$$ at which the joint cdf of $$Z$$ is continuous means $$X_n \xrightarrow{d} Z$$ (Theorem 5.3.2: for a continuous function $$g$$, $$X_n \xrightarrow{d} Z$$ implies $$g(X_n) \xrightarrow{d} g(Z)$$).

**Example 5.3.3 (Chi-squared approximation of the binomial distribution).** From the normal approximation of the binomial distribution, for $$X_n \sim B(n, p)$$ ($$0 < p < 1$$), $$\frac{X_n - np}{\sqrt{np(1-p)}} \xrightarrow{d} Z \sim N(0, 1)$$, and since the square is continuous, $$\frac{(X_n - np)^2}{np(1-p)} \xrightarrow{d} W \sim \chi^2(1)$$. With $$X_{n1} = X_n$$, $$X_{n2} = n - X_n$$, $$p_1 = p$$, $$p_2 = 1 - p$$, $$(X_{n1}, X_{n2})^t \sim \mathrm{Multi}(n, (p_1, p_2)^t)$$ and

$$
\frac{(X_{n1} - np_1)^2}{np_1} + \frac{(X_{n2} - np_2)^2}{np_2} = \frac{(X_n - np)^2}{np} + \frac{(n - X_n - n(1-p))^2}{n(1-p)} = \frac{(X_n - np)^2}{np(1-p)},
$$

so $$\sum_{j=1}^{2}\frac{(X_{nj} - np_j)^2}{np_j} \xrightarrow{d} W$$, $$W \sim \chi^2(1)$$.

**Example 5.3.4 (Chi-squared approximation of the multinomial distribution).** Generalizing, for $$(X_{n1}, \dots, X_{nk})^t \sim \mathrm{Multi}(n, (p_1, \dots, p_k)^t)$$ ($$p_1 + \cdots + p_k = 1$$, $$p_i > 0$$),

$$
\sum_{j=1}^{k}\frac{(X_{nj} - np_j)^2}{np_j} \xrightarrow{d} W, \quad W \sim \chi^2(k - 1).
$$

By the multivariate central limit theorem, with $$X_n = (X_{n1}, \dots, X_{nk})^t$$ and $$p = (p_1, \dots, p_k)^t$$, $$(X_n - np)/\sqrt{n} \xrightarrow{d} X \sim N_k(0, D(p_j) - pp^t)$$. To use Theorem 5.3.2, let $$Y_{nj} = X_{nj}$$, $$\mu_j = p_j$$ ($$j = 1, \dots, r$$), $$Y_n = (Y_{n1}, \dots, Y_{nr})^t$$, $$\mu = (\mu_1, \dots, \mu_r)^t$$, $$r = k - 1$$. Then $$(Y_n - n\mu)/\sqrt{n} \xrightarrow{d} Z \sim N_r(0, \Sigma)$$, $$\Sigma = D(\mu_j) - \mu\mu^t$$. The quadratic form $$z^t\Sigma^{-1}z$$ is a continuous function, so $$\{(Y_n - n\mu)/\sqrt{n}\}^t\Sigma^{-1}\{(Y_n - n\mu)/\sqrt{n}\} \xrightarrow{d} Z^t\Sigma^{-1}Z$$, and by Theorem 4.4.5, for $$Z \sim N_r(0, \Sigma)$$, $$Z^t\Sigma^{-1}Z \sim \chi^2(r)$$, $$r = k - 1$$. Using the inverse formula for a special matrix ($$(I + ab^t)^{-1} = I + cab^t$$, $$c = -1/(1 + b^ta)$$), $$\Sigma^{-1} = (D(\mu_j) - \mu\mu^t)^{-1} = D^{-1}(\mu_j) + \frac{1}{p_k}11^t$$, so

$$
\{(Y_n - n\mu)/\sqrt{n}\}^t\Sigma^{-1}\{(Y_n - n\mu)/\sqrt{n}\} = \sum_{j=1}^{k-1}\frac{(Y_{nj} - n\mu_j)^2}{n\mu_j} + \frac{(X_{nk} - np_k)^2}{np_k}, \quad\therefore\quad \sum_{j=1}^{k}\frac{(X_{nj} - np_j)^2}{np_j} \xrightarrow{d} W \sim \chi^2(k - 1).
$$

> **Theorem 5.3.3 (Computing a limiting distribution with the first-order approximation, the delta method).** For random vectors $$X_n = (X_{n1}, \dots, X_{nk})^t$$ ($$n = 1, 2, \dots$$), $$Z = (Z_1, \dots, Z_k)^t$$ and a vector $$\theta = (\theta_1, \dots, \theta_k)^t$$,
>
> $$
> \sqrt{n}(X_n - \theta) \xrightarrow{d} Z,
> $$
>
> and if the first-order partial derivative $$\dot{g}(\theta)$$ of a function $$g(\theta)$$ is continuous (in one dimension $$\dot{g}(\theta) = dg(\theta)/d\theta$$, in several dimensions $$\dot{g}(\theta) = (\partial g(\theta)/\partial\theta_1, \dots, \partial g(\theta)/\partial\theta_k)^t$$), then
>
> $$
> \sqrt{n}(g(X_n) - g(\theta)) \xrightarrow{d} (\dot{g}(\theta))^tZ.
> $$
{: .theorem #thm-delta-method }

*Proof.* We prove only the one-dimensional case. Since $$g(\theta)$$ is differentiable, there is $$r(x)$$ with $$g(x) = g(\theta) + \{\dot{g}(\theta) + r(x)\}(x - \theta)$$, $$r(x) \to 0$$ as $$x \to \theta$$. Then for every $$\epsilon > 0$$ there is $$\delta > 0$$ with $$(\lvert X_n - \theta\rvert < \delta) \subseteq (\lvert r(X_n)\rvert < \epsilon)$$, so $$P(\lvert r(X_n)\rvert \ge \epsilon) \le P(\lvert X_n - \theta\rvert \ge \delta)$$. Since $$\sqrt{n}(X_n - \theta) \xrightarrow{d} Z$$, by Slutsky's theorem and Theorem 5.2.1, $$X_n - \theta = \frac{1}{\sqrt{n}}\times\sqrt{n}(X_n - \theta) \xrightarrow{d} 0 \times Z = 0$$, that is, $$\mathrm{plim}\,X_n = \theta$$ and $$\lim P(\lvert X_n - \theta\rvert \ge \delta) = 0$$. Therefore $$\mathrm{plim}\,r(X_n) = 0$$. Since $$\sqrt{n}(g(X_n) - g(\theta)) = (\dot{g}(\theta) + r(X_n))\sqrt{n}(X_n - \theta)$$ and $$\mathrm{plim}(\dot{g}(\theta) + r(X_n)) = \dot{g}(\theta)$$, Slutsky's theorem gives $$\sqrt{n}(g(X_n) - g(\theta)) \xrightarrow{d} \dot{g}(\theta)Z$$. $$\square$$

**Example 5.3.5 (Limiting distribution of the sample standard deviation).** Under $$E[(X_1 - \mu)^4] < +\infty$$, $$\sqrt{n}(S_n^2 - \sigma^2) \xrightarrow{d} W \sim N(0, (\rho_4 + 2)\sigma^4)$$. The sample standard deviation is $$S_n = \sqrt{S_n^2}$$ and the derivative of $$g(x) = \sqrt{x}$$ is $$\dot{g}(x) = 1/(2\sqrt{x})$$, so by Theorem 5.3.3

$$
\sqrt{n}(\sqrt{S_n^2} - \sqrt{\sigma^2}) \xrightarrow{d} \frac{1}{2\sqrt{\sigma^2}}W, \quad\therefore\quad \sqrt{n}(S_n - \sigma) \xrightarrow{d} Z, \quad Z \sim N(0, (\rho_4 + 2)\sigma^2/4).
$$

**Example 5.3.6 (Limiting distribution of the sample correlation coefficient).** Let $$(X_1, Y_1)^t, \dots, (X_n, Y_n)^t$$ ($$n > 2$$) be a random sample from a bivariate population with means $$\mu_1, \mu_2$$, variances $$\sigma_1^2, \sigma_2^2$$ and correlation coefficient $$\rho$$ ($$-1 < \rho < 1$$), and

$$
\hat{\rho}_n = \frac{\sum(X_i - \bar{X})(Y_i - \bar{Y})}{\sqrt{\sum(X_i - \bar{X})^2}\sqrt{\sum(Y_i - \bar{Y})^2}}.
$$

Replacing $$X_i, Y_i$$ with $$\frac{X_i - \mu_1}{\sigma_1}, \frac{Y_i - \mu_2}{\sigma_2}$$ does not change its value, so we may assume $$\mu_1 = \mu_2 = 0$$, $$\sigma_1 = \sigma_2 = 1$$. Writing $$\overline{(XY)}_n = \sum X_iY_i/n$$ etc., $$\hat{\rho}_n = g(\bar{X}_n, \bar{Y}_n, \overline{(XY)}_n, \overline{(X^2)}_n, \overline{(Y^2)}_n)$$ with $$g(t_1, t_2, t_3, t_4, t_5) = (t_3 - t_1t_2)(t_4 - t_1^2)^{-1/2}(t_5 - t_2^2)^{-1/2}$$, a function of the mean of $$Z_i = (X_i, Y_i, X_iY_i, X_i^2, Y_i^2)^t$$. If the variance matrix of $$Z_1$$ exists (that is, $$E(X_1^4), E(Y_1^4) < +\infty$$), $$\sqrt{n}\bigl(\frac{1}{n}\sum Z_i - E(Z_1)\bigr) \xrightarrow{d} V$$, $$V \sim N_5(0, \mathrm{Var}(Z_1))$$. With $$\theta = E(Z_1) = (0, 0, \rho, 1, 1)^t$$, $$\rho = g(\theta)$$, and $$\dot{g}(\theta) = (0, 0, 1, -\rho/2, -\rho/2)^t$$, Theorem 5.3.3 gives

$$
\sqrt{n}(\hat{\rho}_n - \rho) \xrightarrow{d} (\dot{g}(\theta))^tV \sim N\bigl(0, \mathrm{Var}[(\dot{g}(\theta))^tZ_1]\bigr), \quad (\dot{g}(\theta))^tZ_1 = X_1Y_1 - \tfrac{\rho}{2}X_1^2 - \tfrac{\rho}{2}Y_1^2,
$$

so $$\sqrt{n}(\hat{\rho}_n - \rho) \xrightarrow{d} W$$, $$W \sim N\bigl(0, \mathrm{Var}(X_1Y_1 - \frac{\rho}{2}X_1^2 - \frac{\rho}{2}Y_1^2)\bigr)$$.

**Example 5.3.7 (Sample correlation coefficient and variance stabilizing transformation).** If the population is a bivariate normal distribution, by Example 4.4.3, $$Y_1 - \rho X_1\vert_{X_1 = x_1} \sim N(0, 1 - \rho^2)$$; since the conditional distribution does not depend on $$X_1 = x_1$$, $$Y_1 - \rho X_1$$ is independent of $$X_1$$. With $$\mu_1 = \mu_2 = 0$$, $$\sigma_1 = \sigma_2 = 1$$ and $$T = (Y_1 - \rho X_1)/\sqrt{1 - \rho^2}$$, $$X_1$$ and $$T$$ are independent standard normal, and substituting $$Y_1 = \rho X_1 + \sqrt{1 - \rho^2}T$$,

$$
X_1Y_1 - \tfrac{\rho}{2}X_1^2 - \tfrac{\rho}{2}Y_1^2 = \tfrac{\rho}{2}(1 - \rho^2)X_1^2 + (1 - \rho^2)^{3/2}X_1T - \tfrac{\rho}{2}(1 - \rho^2)T^2,
$$

whose variance is $$(1 - \rho^2)^2$$. Therefore $$\sqrt{n}(\hat{\rho}_n - \rho) \xrightarrow{d} W$$, $$W \sim N(0, (1 - \rho^2)^2)$$. For a function $$g(\hat{\rho}_n)$$, Theorem 5.3.3 gives $$\sqrt{n}(g(\hat{\rho}_n) - g(\rho)) \xrightarrow{d} \dot{g}(\rho)W \sim N(0, [\dot{g}(\rho)]^2(1 - \rho^2)^2)$$. A transformation $$g(\hat{\rho}_n)$$ that makes the variance of the limiting distribution independent of $$\rho$$ is a *variance stabilizing transformation* of $$\hat{\rho}_n$$. In particular

$$
g(\hat{\rho}_n) = \frac{1}{2}\log\frac{1 + \hat{\rho}_n}{1 - \hat{\rho}_n}
$$

is called *Fisher's transformation*; then $$[\dot{g}(\rho)]^2(1 - \rho^2)^2 = 1$$ and $$\sqrt{n}(g(\hat{\rho}_n) - g(\rho)) \xrightarrow{d} Z$$, $$Z \sim N(0, 1)$$.

**Example 5.3.8 (Limiting distribution of the sample quantile).** In Example 5.2.7 we saw the convergence in probability of the sample quantile $$X_{(r_n)}$$ ($$r_n \sim \alpha n$$, $$0 < \alpha < 1$$). Under the same conditions we find its limiting distribution. With $$F^{-1}$$ the inverse of the population cdf and $$h(y) = F^{-1}(1 - e^{-y})$$ ($$y > 0$$), $$X_{(r_n)} \overset{d}{=} h\bigl(\frac{1}{n}Z_1 + \cdots + \frac{1}{n - r_n + 1}Z_{r_n}\bigr)$$, $$Z_i \overset{iid}{\sim} \mathrm{Exp}(1)$$. Let

$$
Y_n = \frac{1}{n}Z_1 + \cdots + \frac{1}{n - r_n + 1}Z_{r_n}, \qquad E(Y_n) \sim -\log(1 - \alpha), \quad \mathrm{Var}(Y_n) \sim \frac{1}{n}\frac{\alpha}{1 - \alpha}.
$$

By approximating the mgf of $$W_n = \sqrt{n}\frac{Y_n - (-\log(1 - \alpha))}{\sqrt{\alpha/(1 - \alpha)}}$$ (see Exercise 5.15), $$\lim mgf_{W_n}(t) = \exp(\frac{1}{2}t^2) = mgf_W(t)$$, $$W \sim N(0, 1)$$, so $$W_n \xrightarrow{d} W$$ and $$\sqrt{n}(Y_n - (-\log(1 - \alpha))) \xrightarrow{d} \sqrt{\alpha/(1 - \alpha)}\,W$$. Therefore by Theorem 5.3.3, when $$h$$ is differentiable,

$$
\sqrt{n}\{h(Y_n) - h(-\log(1 - \alpha))\} \xrightarrow{d} \dot{h}(-\log(1 - \alpha))\sqrt{\alpha/(1 - \alpha)}\,W.
$$

Under these conditions $$\dot{h}(-\log(1 - \alpha)) = (1 - \alpha)/f(F^{-1}(\alpha))$$, $$f = \dot{F}$$, so

$$
\sqrt{n}\{X_{(r_n)} - F^{-1}(\alpha)\} \xrightarrow{d} Z, \quad Z \sim N\Bigl(0, \frac{\alpha(1 - \alpha)}{[f(F^{-1}(\alpha))]^2}\Bigr)
$$

(the condition holds if the pdf is given by $$f(x) = dF(x)/dx$$ and $$f(F^{-1}(\alpha)) > 0$$).

## References

- 김우철, *수리통계학* (Mathematical Statistics), revised 2nd edition, 민영사, 2021 — Chapter 5, §5.3 (Examples 5.3.1 to 5.3.8, Theorem 5.3.3). Translated from the book; not from my notes.
- Mathematical Statistics 1 (326.311), Seoul National University, Spring 2025. Instructor: Jaeyong Lee (이재용).

[Previous](/posts/mathstat1-central-limit-theorem/) · [Overview](/posts/mathstat1-overview/) · [Next](/posts/mathstat1-simulation/)
