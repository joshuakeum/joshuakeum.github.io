---
title: "Mathematical Statistics 1: Ch. 4 Part 2 — The t and F Distributions and Sampling from a Normal Population"
date: 2026-11-21 12:20:00 +0900
categories: [Study Notes, Mathematical Statistics 1]
tags: [t distribution, F distribution, chi-square, sample mean, sample variance, confidence interval, cauchy]
description: Student's t-distribution and its properties, the fundamental theorem of the normal distribution (sample mean and sample variance), the confidence interval for the mean, and, from the textbook, the chi-square and F distributions and the comparison of variances and means. Chapter 4, notes section 2 of Mathematical Statistics 1.
math: true
mermaid: false
render_with_liquid: false
---

> My handwritten notes, translated into English. Chapter 4, notes section 2, with the fundamental theorem of the normal distribution. It corresponds to §4.2 of the textbook. Statements and proofs follow my notes. My notes do not cover the chi-square and F distributions in their own sections, nor the intervals for the variance and the comparison of two populations; those are collected at the end under "Supplement from the textbook". The exercises are in [Chapter 4 Exercises](/posts/mathstat1-exercises-chapter-4/).
{: .prompt-info }

## 2. The $$t$$-distribution and the $$F$$-distribution

### 2.1 Student's $$t$$-distribution

> **Notation.** $$T \sim t(r)$$, $$r > 0$$.
{: .definition #def-t-distribution }

**Properties.**

1. *Definition.* Let $$W \sim N(0, 1)$$, $$V \sim \chi^2(r) = \mathrm{Gamma}(\tfrac{r}{2}, 2)$$, and $$W \perp V$$. Then

   $$
   T := \frac{W}{\sqrt{V/r}} \sim t(r).
   $$
2. *Pdf.*

   $$
   f(t) = \frac{1}{\sqrt{r}}\cdot\frac{\Gamma\bigl(\frac{r+1}{2}\bigr)}{\Gamma(\frac{1}{2})\Gamma(\frac{r}{2})}\cdot\frac{1}{\bigl(1 + \frac{t^2}{r}\bigr)^{\frac{r+1}{2}}}, \qquad t \in \mathbb{R}.
   $$
3. $$t(1) = \mathrm{Cauchy}(0, 1)$$.
4. $$E(T) = 0$$ for $$r > 1$$, and $$\mathrm{Var}(T) = \dfrac{r}{r-2}$$ when $$r > 2$$.
5. $$f_r(t) \xrightarrow{r \to \infty} N(t \mid 0, 1)$$, where $$f_r(t)$$ is the pdf of $$t(r)$$.

*Proof.* ② By definition, $$W = T\sqrt{U/r}$$, $$V = U$$. Therefore

$$
\left\lvert\frac{\partial(W, V)}{\partial(T, U)}\right\rvert = \left\lvert\det\begin{pmatrix}\sqrt{U/r} & -\dfrac{T}{\sqrt{4Ur}} \\ 0 & 1\end{pmatrix}\right\rvert = \sqrt{U/r}.
$$

Hence

$$
f_{W,V}(w, v)\,dw\,dv = \frac{1}{\sqrt{2\pi}}e^{-\frac{1}{2}w^2}\cdot\frac{1}{\Gamma(\frac{r}{2})2^{\frac{r}{2}}}v^{\frac{r}{2}-1}e^{-\frac{v}{2}}\,dw\,dv \qquad (w \in \mathbb{R},\ v > 0)
$$

$$
= \frac{1}{\sqrt{2\pi}}e^{-\frac{u}{2r}t^2}\cdot\frac{1}{\Gamma(\frac{r}{2})2^{\frac{r}{2}}}u^{\frac{r}{2}-1}e^{-\frac{u}{2}}\sqrt{\frac{u}{r}}\,dt\,du = f_{T,U}(t, u)\,dt\,du \qquad (t \in \mathbb{R},\ u > 0).
$$

$$\therefore$$

$$
f_{T,U}(t, u) = \frac{1}{\sqrt{2\pi r}\,\Gamma(\frac{r}{2})2^{\frac{r}{2}}}u^{\frac{r+1}{2}-1}e^{-\frac{1}{2}u(\frac{t^2}{r}+1)}.
$$

$$\therefore$$

$$
f_T(t) = \int_{-\infty}^{\infty}f_{T,U}(t, u)\,du = \frac{1}{\sqrt{2\pi r}\,\Gamma(\frac{r}{2})2^{\frac{r}{2}}}\int_0^{\infty}u^{\frac{r+1}{2}-1}e^{-\frac{1}{2}u(\frac{t^2}{r}+1)}\,du
$$

(a Gamma integral)

$$
= \frac{1}{\sqrt{2\pi r}\,\Gamma(\frac{r}{2})2^{\frac{r}{2}}}\cdot\frac{\Gamma(\frac{r+1}{2})}{\bigl[\frac{1}{2}\bigl(1 + \frac{t^2}{r}\bigr)\bigr]^{\frac{r+1}{2}}}.
$$

③ Substituting $$r = 1$$ gives $$\dfrac{1}{\pi}\dfrac{1}{1 + t^2}$$: the Cauchy distribution.

④ $$E(T) = \displaystyle\int_{-\infty}^{\infty}tf_r(t)\,dt$$. Since $$f_r(t)$$ is a symmetric (even) function, if $$\displaystyle\int\lvert t\rvert f_r(t)\,dt < \infty$$, then $$E(T) = 0$$.

$$
\int_{-\infty}^{\infty}\lvert t\rvert f_r(t)\,dt = 2\int_0^{\infty}t\frac{\Gamma(\frac{r+1}{2})}{\Gamma(\frac{1}{2})\Gamma(\frac{r}{2})}\cdot\frac{1}{\sqrt{r}}\cdot\frac{1}{\bigl(1 + \frac{t^2}{r}\bigr)^{\frac{r+1}{2}}}\,dt = C\int_0^{\infty}\frac{t}{\bigl(1 + \frac{t^2}{r}\bigr)^{\frac{r+1}{2}}}\,dt.
$$

The integrability is determined by the tail (how fast the integrand decays): the integrand behaves like $$C\dfrac{t}{t^{r+1}\cdot r^{-(r+1)/2}} \simeq C\dfrac{1}{t^r}$$.

If $$r > 1$$, $$\displaystyle\int_{-\infty}^{\infty}\lvert t\rvert f_r(t)\,dt < \infty$$, and if $$0 < r \le 1$$, $$\displaystyle\int_{-\infty}^{\infty}\lvert t\rvert f_r(t)\,dt = \infty$$.

\* *Rigorous proof.* Split

$$
\int_0^{\infty}\frac{t}{\bigl(1 + \frac{t^2}{r}\bigr)^{\frac{r+1}{2}}}\,dt = \int_0^1\frac{t}{\bigl(1 + \frac{t^2}{r}\bigr)^{\frac{r+1}{2}}}\,dt + \int_1^{\infty}\frac{t}{\bigl(1 + \frac{t^2}{r}\bigr)^{\frac{r+1}{2}}}\,dt,
$$

where the first integral is finite (the integral of a continuous function over $$[0, 1]$$), and for the second, for $$t \ge \max(1, \sqrt{r})$$,

$$
\frac{r^{\frac{r+1}{2}}}{2^{\frac{r+1}{2}}}\cdot\frac{1}{t^r} \le \frac{t}{\bigl(1 + \frac{t^2}{r}\bigr)^{\frac{r+1}{2}}} \le r^{\frac{r+1}{2}}\cdot\frac{1}{t^r},
$$

so the tail is comparable with $$\dfrac{1}{t^r}$$, which is integrable at infinity exactly when $$r > 1$$.

For $$\mathrm{Var}(T)$$, $$T = \dfrac{W}{\sqrt{V/r}}$$. When $$r > 1$$ (more precisely, when the second moment exists),

$$
\mathrm{Var}(T) = E(T^2) = E\Bigl(\frac{W^2}{V/r}\Bigr) = rE(W^2)E\Bigl(\frac{1}{V}\Bigr) \qquad (W \perp V).
$$

Here $$E(W^2) = 1$$ and $$E\bigl(\frac{1}{V}\bigr) = \dfrac{1}{r-2}$$ when $$r > 2$$ ($$\chi^2$$ distribution). Hence $$\mathrm{Var}(T) = \dfrac{r}{r-2}$$.

⑤ Use Stirling's approximation: the Cauchy distribution $$\sim$$ the $$t$$-distribution $$\sim$$ the standard normal distribution as $$r$$ increases. $$\square$$

### 2.2 Fundamental theorem of the normal distribution

> **Theorem (Fundamental theorem of the normal distribution).** Let $$X_1, \dots, X_n \overset{iid}{\sim} N(\mu, \sigma^2)$$, $$\mu \in \mathbb{R}$$, $$\sigma > 0$$. Then the following hold.
>
> 1. $$\bar{X} = \dfrac{1}{n}\sum X_i \sim N\bigl(\mu, \dfrac{\sigma^2}{n}\bigr)$$.
> 2. Defining $$S^2 = \dfrac{1}{n-1}\sum(X_i - \bar{X})^2$$, $$S^2 \perp \bar{X}$$.
> 3. $$\dfrac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1}$$.
{: .theorem #thm-fundamental-normal }

*Proof.* (1) Already known by the preceding characteristics of the normal distribution.

(2) Let us show that $$\bar{X}$$ and $$(X_1 - \bar{X}, X_2 - \bar{X}, \dots, X_n - \bar{X})$$ are independent. With $$\bar{t} = \frac{1}{n}\sum t_i$$,

$$
M_{\bar{X},\,X_1-\bar{X},\dots,X_n-\bar{X}}(s, t_1, \dots, t_n) = E\,e^{s\bar{X} + t_1(X_1-\bar{X}) + \cdots + t_n(X_n-\bar{X})} = E\,e^{\bar{X}(s - \sum t_i) + \sum t_iX_i}
$$

$$
= E\,e^{\sum(\frac{s}{n} + t_i - \bar{t})X_i} = \prod_{i=1}^{n}M_{X_i}\Bigl(\frac{s}{n} + t_i - \bar{t}\Bigr) = \prod_{i=1}^{n}e^{\mu(\frac{s}{n} + t_i - \bar{t}) + \frac{1}{2}\sigma^2(\frac{s}{n} + t_i - \bar{t})^2}
$$

$$
= e^{\mu s + \frac{1}{2}\sigma^2\frac{s^2}{n}}\prod_{i=1}^{n}e^{\frac{1}{2}\sigma^2(t_i - \bar{t})^2},
$$

a product of a function of $$s$$ and a function of $$(t_1, \dots, t_n)$$, so $$\bar{X}$$ and $$(X_1 - \bar{X}, \dots, X_n - \bar{X})$$ are independent, and $$S^2$$ is a function of the latter. Hence $$S^2 \perp \bar{X}$$.

(3) Write

$$
\underbrace{\frac{\sum(X_i - \mu)^2}{\sigma^2}}_{\sim\,\chi^2_n} = \frac{\sum(X_i - \bar{X})^2}{\sigma^2} + \underbrace{\frac{n(\bar{X} - \mu)^2}{\sigma^2}}_{\sim\,\chi^2_1}.
$$

Also $$(X_i - \bar{X}) \perp \bar{X}$$ for all $$i$$. Therefore the mgfs multiply:

$$
M_{\frac{\sum(X_i-\mu)^2}{\sigma^2}}(t) = M_{\frac{\sum(X_i-\bar{X})^2}{\sigma^2}}(t)\,M_{\frac{n(\bar{X}-\mu)^2}{\sigma^2}}(t), \qquad (1 - 2t)^{-\frac{n}{2}} = M_{\frac{\sum(X_i-\bar{X})^2}{\sigma^2}}(t)\,(1 - 2t)^{-\frac{1}{2}},
$$

$$\therefore$$ $$M_{\frac{\sum(X_i-\bar{X})^2}{\sigma^2}}(t) = (1 - 2t)^{-\frac{n-1}{2}}$$, $$\therefore$$ $$\dfrac{\sum(X_i - \bar{X})^2}{\sigma^2} \sim \chi^2_{n-1}$$. $$\square$$

> **Corollary.** $$X_1, \dots, X_n \overset{iid}{\sim} N(\mu, \sigma^2)$$ $$\Rightarrow$$ $$\dfrac{\bar{X} - \mu}{S/\sqrt{n}} \sim t(n-1)$$, where $$(n-1)S^2 = \sum(X_i - \bar{X})^2$$.
{: .theorem #cor-t-statistic }

*Proof.* $$\dfrac{\bar{X} - \mu}{\sigma/\sqrt{n}} \sim N(0, 1)$$ and $$\dfrac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1}$$, and they are independent. $$\therefore$$

$$
\frac{\frac{\bar{X}-\mu}{\sigma/\sqrt{n}}}{\sqrt{\frac{(n-1)S^2/\sigma^2}{(n-1)}}} = \frac{\bar{X} - \mu}{S/\sqrt{n}} \sim t(n-1). \qquad \square
$$

> **Theorem (Confidence interval for $$\mu$$).** Let $$X_1, \dots, X_n \overset{iid}{\sim} N(\mu, \sigma^2)$$, $$\mu \in \mathbb{R}$$, $$\sigma > 0$$. Then
>
> $$
> P\Bigl(\Bigl\lvert\frac{\bar{X} - \mu}{S/\sqrt{n}}\Bigr\rvert < t_{\frac{\alpha}{2}}(n-1)\Bigr) = 1 - \alpha,
> $$
>
> where $$t_{\alpha/2}(n-1)$$ is the upper $$\alpha/2$$ quantile of $$t(n-1)$$. So $$\Bigl(\bar{X} - t_{\frac{\alpha}{2}}(n-1)\dfrac{S}{\sqrt{n}},\ \bar{X} + t_{\frac{\alpha}{2}}(n-1)\dfrac{S}{\sqrt{n}}\Bigr)$$ is a $$100(1 - \alpha)\%$$ confidence interval of $$\mu$$.
{: .theorem #thm-ci-mean }

## Supplement from the textbook

**Chi-square distribution (§4.2).** For independent $$X_1, \dots, X_r \sim N(0, 1)$$, each $$X_i^2 \sim \mathrm{Gamma}(1/2, 2)$$ (Example 4.1.4(c)), so $$Y = X_1^2 + \cdots + X_r^2 \sim \mathrm{Gamma}(r/2, 2)$$, with pdf $$\frac{1}{\Gamma(r/2)2^{r/2}}y^{r/2-1}e^{-y/2}I_{(0,\infty)}(y)$$. This is the chi-squared distribution with $$r$$ degrees of freedom, $$Y \sim \chi^2(r)$$; for $$r$$ a natural number, $$Y \overset{d}{=} X_1^2 + \cdots + X_r^2$$, $$X_i \overset{iid}{\sim} N(0, 1)$$. The upper $$\alpha$$ quantile $$\chi^2_{\alpha}(r)$$ satisfies $$P(Y > \chi^2_{\alpha}(r)) = \alpha$$; for example $$\chi^2_{0.990}(5) = 0.554$$, $$\chi^2_{0.975}(5) = 0.831$$, $$\chi^2_{0.025}(5) = 12.833$$, $$\chi^2_{0.010}(5) = 15.086$$. Since $$X \sim \mathrm{Gamma}(\nu, \beta) \Leftrightarrow 2X/\beta \sim \chi^2(2\nu)$$, the upper $$\alpha$$ quantile of $$\mathrm{Gamma}(\nu, \beta)$$ is $$\beta\chi^2_{\alpha}(2\nu)/2$$.

**Example 4.2.2.** The upper $$0.05$$ quantile of $$\mathrm{Gamma}(2, 3)$$ is $$3\chi^2_{0.05}(4)/2 = 3 \times 9.488/2 = 14.232$$.

> **Theorem 4.2.1 (Properties of the chi-squared distribution).** (a) If $$Y \sim \chi^2(r)$$, then $$E(Y) = r$$ and $$\mathrm{Var}(Y) = 2r$$. (b) The mgf is $$(1 - 2t)^{-r/2}$$, $$t < 1/2$$. (c) If $$Y_1 \sim \chi^2(r_1)$$, $$Y_2 \sim \chi^2(r_2)$$ are independent, then $$Y_1 + Y_2 \sim \chi^2(r_1 + r_2)$$.
{: .theorem #thm-textbook-4-2-1 }

**The $$t$$-distribution (Example 4.2.3).** The textbook derives the same pdf as in 2.1 above through the transformation $$(Z, V) \to (X, Y)$$ with $$Z = X\sqrt{Y/r}$$, $$V = Y$$. Upper quantiles: $$t_{0.10}(5) = 1.476$$, $$t_{0.05}(5) = 2.015$$, $$t_{0.025}(5) = 2.571$$, $$t_{0.005}(5) = 4.032$$, and by symmetry $$t_{1-\alpha}(r) = -t_{\alpha}(r)$$.

**The $$F$$-distribution (Example 4.2.4).** For independent $$V_1 \sim \chi^2(r_1)$$, $$V_2 \sim \chi^2(r_2)$$, let $$X = \dfrac{V_1/r_1}{V_2/r_2}$$. Taking $$Y = V_2$$, the inverse is $$v_1 = r_1xy/r_2$$, $$v_2 = y$$, with Jacobian $$r_1y/r_2$$, and integrating out $$y$$,

$$
pdf_X(x) = \frac{\Gamma\bigl(\frac{r_1+r_2}{2}\bigr)}{\Gamma(\frac{r_1}{2})\Gamma(\frac{r_2}{2})}\Bigl(\frac{r_1}{r_2}\Bigr)^{r_1/2}x^{r_1/2-1}\Bigl(1 + \frac{r_1x}{r_2}\Bigr)^{-(r_1+r_2)/2}I_{(x>0)}.
$$

This is the *$$F$$-distribution* with $$(r_1, r_2)$$ degrees of freedom, $$X \sim F(r_1, r_2)$$: $$F(r_1, r_2) \overset{d}{=} \dfrac{\chi^2(r_1)/r_1}{\chi^2(r_2)/r_2}$$ with the two chi-squares independent. Its upper $$\alpha$$ quantile $$F_{\alpha}(r_1, r_2)$$ satisfies $$P(X > F_{\alpha}(r_1, r_2)) = \alpha$$; for example $$F_{0.05}(5, 10) = 3.330$$, $$F_{0.025}(5, 10) = 4.240$$, $$F_{0.01}(5, 10) = 5.640$$.

> **Theorem 4.2.5 (Properties of the $$F$$-distribution).** (a) If $$X \sim F(r_1, r_2)$$, then $$1/X \sim F(r_2, r_1)$$, so $$F_{1-\alpha}(r_1, r_2) = 1/F_{\alpha}(r_2, r_1)$$. (b) If $$X \sim t(r)$$, then $$X^2 \sim F(1, r)$$, so $$t^2_{\alpha/2}(r) = F_{\alpha}(1, r)$$.
{: .theorem #thm-textbook-4-2-5 }

*Proof.* (a) $$1/X \overset{d}{=} \dfrac{V_2/r_2}{V_1/r_1}$$. (b) $$X^2 \overset{d}{=} \dfrac{Z^2}{V/r}$$ with $$Z^2 \sim \chi^2(1)$$ independent of $$V$$. $$\square$$

**Example 4.2.5.** $$F_{0.975}(5, 10) = 1/F_{0.025}(10, 5) = 1/6.620 = 0.151$$ and $$t_{0.025}(5)^2 = 2.571^2 = 6.610 = F_{0.05}(1, 5)$$.

> **Theorem 4.2.4 (Inference on the population variance).** For a random sample from $$N(\mu, \sigma^2)$$,
>
> $$
> P\Bigl\{\frac{n-1}{\chi^2_{\alpha/2}(n-1)}S^2 \le \sigma^2 \le \frac{n-1}{\chi^2_{1-\alpha/2}(n-1)}S^2\Bigr\} = 1 - \alpha.
> $$
{: .theorem #thm-textbook-4-2-4 }

*Proof.* Since $$(n-1)S^2/\sigma^2 \sim \chi^2(n-1)$$, $$P\{\chi^2_{1-\alpha/2}(n-1) \le (n-1)S^2/\sigma^2 \le \chi^2_{\alpha/2}(n-1)\} = 1 - \alpha$$; solve for $$\sigma^2$$. $$\square$$

> **Theorem 4.2.6 (Comparison of the variances of two normal populations).** For independent random samples $$X_{11}, \dots, X_{1n_1}$$ from $$N(\mu_1, \sigma_1^2)$$ and $$X_{21}, \dots, X_{2n_2}$$ from $$N(\mu_2, \sigma_2^2)$$ with sample variances $$S_1^2$$, $$S_2^2$$,
>
> $$
> \frac{S_1^2/\sigma_1^2}{S_2^2/\sigma_2^2} \sim F(n_1 - 1, n_2 - 1), \qquad P\Bigl\{\frac{S_1^2}{S_2^2}\frac{1}{F_{\alpha/2}(n_1-1, n_2-1)} \le \frac{\sigma_1^2}{\sigma_2^2} \le \frac{S_1^2}{S_2^2}F_{\alpha/2}(n_2-1, n_1-1)\Bigr\} = 1 - \alpha.
> $$
{: .theorem #thm-textbook-4-2-6 }

*Proof.* By the fundamental theorem, $$(n_i - 1)S_i^2/\sigma_i^2 \sim \chi^2(n_i - 1)$$, and $$S_1^2 \perp S_2^2$$; use the definition of the $$F$$-distribution and Theorem 4.2.5. $$\square$$

**Several normal populations (Theorem 4.2.7).** In the one-way classification model $$X_{ij} = \mu_i + e_{ij}$$, $$e_{ij} \overset{iid}{\sim} N(0, \sigma^2)$$, $$i = 1, \dots, k$$, $$j = 1, \dots, n_i$$, with $$\bar{X}_i = \sum_jX_{ij}/n_i$$, $$\bar{X} = \sum_{i,j}X_{ij}/n$$, $$\bar{\mu} = \sum_in_i\mu_i/n$$, $$n = n_1 + \cdots + n_k$$: (a) $$\sum_in_i(\bar{X}_i - \bar{X} - (\mu_i - \bar{\mu}))^2/\sigma^2 \sim \chi^2(k-1)$$; (b) $$\sum_{i,j}(X_{ij} - \bar{X}_i)^2/\sigma^2 \sim \chi^2(n-k)$$; (c) the two are independent. Therefore, with $$\hat{\sigma}^2 = \sum_{i,j}(X_{ij} - \bar{X}_i)^2/(n-k)$$,

$$
\frac{1}{k-1}\sum_{i=1}^{k}n_i\bigl(\bar{X}_i - \bar{X} - (\mu_i - \bar{\mu})\bigr)^2\Big/\hat{\sigma}^2 \sim F(k-1, n-k), \qquad P\Bigl\{\sum_{i=1}^{k}n_i\bigl(\mu_i - \bar{\mu} - (\bar{X}_i - \bar{X})\bigr)^2 \le (k-1)\hat{\sigma}^2F_{\alpha}(k-1, n-k)\Bigr\} = 1 - \alpha.
$$

For $$k = 2$$ this reduces to $$\Bigl\{\dfrac{\bar{X}_2 - \bar{X}_1 - (\mu_2 - \mu_1)}{\sqrt{n_1^{-1} + n_2^{-1}}\,\hat{\sigma}}\Bigr\}^2 \sim F(1, n_1 + n_2 - 2)$$, using $$F_{\alpha}(1, n_1 + n_2 - 2) = t^2_{\alpha/2}(n_1 + n_2 - 2)$$.

## References

- 김우철, *수리통계학* (Mathematical Statistics), revised 2nd edition, 민영사, 2021 — Chapter 4, §4.2 (Examples 4.2.1 to 4.2.5, Theorems 4.2.1 to 4.2.7). The supplement is translated from the book.
- Mathematical Statistics 1 (326.311), Seoul National University, Spring 2025. Instructor: Jaeyong Lee (이재용).

[Previous](/posts/mathstat1-transformations-sampling/) · [Overview](/posts/mathstat1-overview/) · [Next](/posts/mathstat1-order-statistics/)
