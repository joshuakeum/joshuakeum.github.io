---
title: "Mathematical Statistics 1: Ch. 4 Part 1 — Transformation of Random Variables and Sampling"
date: 2026-11-21 12:10:00 +0900
categories: [Study Notes, Mathematical Statistics 1]
tags: [transformation, jacobian, change of variables, sampling, statistic, sampling distribution]
description: Finding the density of a function of a random variable, the change-of-variables theorem with the Jacobian, and the framework of sampling, statistics and sampling distributions. Chapter 4, notes sections 0 and 1 of Mathematical Statistics 1.
math: true
mermaid: false
render_with_liquid: false
---

> My handwritten notes, translated into English. Chapter 4 of my notes, "Sampling Distributions", sections 0 and 1. They correspond to §4.1 of the textbook. Statements and proofs follow my notes. Material taken from the textbook is collected at the end under "Supplement from the textbook". The exercises are in [Chapter 4 Exercises](/posts/mathstat1-exercises-chapter-4/).
{: .prompt-info }

## 0. Transformation of random variables

**Our objective.** When the density function of a random variable $$X$$ is given as $$f_X$$, find the density function $$f_Y$$ of $$Y = u(X)$$.

**Idea.**

1. (Discrete.) $$P(Y = y) = \displaystyle\sum_{x : u(x) = y}P(X = x)$$.
2. (Continuous.) $$P(Y \in [y, y + dy]) \simeq \displaystyle\sum_{x \in u^{-1}(y)}P(X \in [x, x + dx])$$.

**Example.** $$X$$ is the number of tosses of a coin until the first head appears:

$$
P(X = x) = \Bigl(\frac{1}{2}\Bigr)^{x-1}\Bigl(\frac{1}{2}\Bigr) = \Bigl(\frac{1}{2}\Bigr)^x \quad (x = 1, 2, \dots).
$$

Let $$Y = X - 1$$, the number of tosses between the head and the next head, that is, the number of tails before the first head. Then

$$
f_Y(y) = P(Y = y) = P(X - 1 = y) = P(X = y + 1) = \Bigl(\frac{1}{2}\Bigr)^{y+1}, \qquad y = 0, 1, 2, \dots
$$

**Example.** The sum of two independent Poisson variables. Let $$X_1, X_2$$ be independent with

$$
X_1 \sim f_{X_1}(x_1) = \frac{e^{-\lambda_1}\lambda_1^{x_1}}{x_1!}, \quad X_2 \sim f_{X_2}(x_2) = \frac{e^{-\lambda_2}\lambda_2^{x_2}}{x_2!}, \qquad x_1, x_2 = 0, 1, 2, \dots,\ \lambda_1, \lambda_2 > 0.
$$

With $$Y = X_1 + X_2$$,

$$
P(Y = y) = P(X_1 + X_2 = y) = \sum_{(x_1, x_2) : x_1 + x_2 = y}f_{X_1}(x_1)f_{X_2}(x_2) = \sum_{x_1=0}^{y}f_{X_1}(x_1)f_{X_2}(y - x_1)
$$

$$
= \sum_{x_1=0}^{y}\frac{e^{-\lambda_1}\lambda_1^{x_1}}{x_1!}\cdot\frac{e^{-\lambda_2}\lambda_2^{y-x_1}}{(y - x_1)!} = \frac{e^{-\lambda_1-\lambda_2}}{y!}\sum_{x_1=0}^{y}\frac{y!}{x_1!(y - x_1)!}\Bigl(\frac{\lambda_1}{\lambda_2}\Bigr)^{x_1}\lambda_2^y
$$

$$
= \frac{\lambda_2^ye^{-(\lambda_1+\lambda_2)}}{y!}\Bigl(1 + \frac{\lambda_1}{\lambda_2}\Bigr)^y = \frac{e^{-(\lambda_1+\lambda_2)}(\lambda_1 + \lambda_2)^y}{y!} \qquad (y = 0, 1, 2, \dots).
$$

$$\therefore$$ $$X_1 + X_2 \sim \mathrm{Poi}(\lambda_1 + \lambda_2)$$.

> **Theorem (Property).** Let $$Y = u(X)$$, where $$u$$ is a one-to-one correspondence that is continuously differentiable. Then
>
> $$
> f_Y(y) = f_X\bigl(u^{-1}(y)\bigr)\Bigl\lvert\det\Bigl(\frac{\partial u^{-1}(y)}{\partial y}\Bigr)\Bigr\rvert,
> $$
>
> where $$\dfrac{\partial u^{-1}(y)}{\partial y}$$ is the Jacobian matrix.
{: .theorem #thm-change-of-variables }

*Proof.* Use the change-of-variables formula:

$$
\int_Af_X(x)\,dx = \int_{u(A)}f_X\bigl(u^{-1}(y)\bigr)\Bigl\lvert\det\Bigl(\frac{\partial u^{-1}(y)}{\partial y}\Bigr)\Bigr\rvert\,dy = \int_{u(A)}f_Y(y)\,dy. \qquad \square
$$

**How to remember.**

$$
f(x)\,dx = f\bigl(u^{-1}(y)\bigr)\Bigl\lvert\det\frac{\partial u^{-1}(y)}{\partial y}\Bigr\rvert\,dy \quad (= f_Y(y)\,dy).
$$

The left side is a probability. (The absolute value is there because we do not consider the direction.)

**Example (1).** $$X \sim f_X(x) = 2x\,I_{(0<x<1)}$$. What is the density function of $$Y = X^2$$?

(1) Use $$f_X(x)\,dx = f_Y(y)\,dy$$. With $$y = x^2$$, $$x = \sqrt{y}$$, $$dx = \dfrac{1}{2\sqrt{y}}\,dy$$:

$$
f_X(x)\,dx = 2x\,I_{(0<x<1)}\,dx = 2\sqrt{y}\,I_{(0<\sqrt{y}<1)}\cdot\frac{1}{2\sqrt{y}}\,dy = I_{(0<\sqrt{y}<1)}\,dy = I_{(0<y<1)}\,dy,
$$

so $$f_Y(y) = I_{(0<y<1)}$$.

(2) Find the cdf of $$Y$$ first, then differentiate. $$F_X(x) = x^2I_{(0<x<1)} + I_{(x \ge 1)}$$, so for $$y > 0$$,

$$
F_Y(y) = P(Y \le y) = P(X^2 \le y) = P(X \le \sqrt{y}) = \begin{cases} 0 & (y \le 0) \\ y & (0 < y < 1) \\ 1 & (y \ge 1) \end{cases}
\quad\Rightarrow\quad f_Y(y) = \begin{cases} 0 & (y \le 0) \\ 1 & (0 < y < 1) \\ 0 & (y \ge 1) \end{cases} = I_{(0<y<1)}.
$$

> **Theorem (Properties of a many-to-one $$u$$).** Let $$Y = u(X)$$, where $$u : \mathcal{X} \to \mathcal{Y}$$ is a $$K$$-to-$$1$$ function (differentiable). Let $$\mathcal{X} = \bigcup_{i=1}^{K}\mathcal{X}_i$$ where the $$\mathcal{X}_i$$ are disjoint, and let $$u_i := u\vert_{\mathcal{X}_i}$$, which is a one-to-one correspondence. Then
>
> $$
> f_Y(y) = \sum_{i=1}^{K}f_X\bigl(u_i^{-1}(y)\bigr)\Bigl\lvert\det\Bigl(\frac{\partial u_i^{-1}(y)}{\partial y}\Bigr)\Bigr\rvert.
> $$
{: .theorem #thm-change-of-variables-many-to-one }

**How to remember.**

$$
f(x)\,dx = f(x)I_{(x \in \mathcal{X})}\,dx = \sum_{i=1}^{K}f(x)I_{(x \in \mathcal{X}_i)}\,dx \qquad (\text{pieces on which } u \text{ is one-to-one}).
$$

**Example.** $$X \sim f_X(x) = \dfrac{1}{2}I_{(-1<x<1)}$$. What is the density function of $$Y = X^2$$?

$$
f_X(x)\,dx = \frac{1}{2}I_{(-1<x<1)}\,dx = \frac{1}{2}I_{(-1<x\le0)}\,dx + \frac{1}{2}I_{(0<x<1)}\,dx
$$

$$
= \frac{1}{2}I_{(-1<-\sqrt{y}\le0)}\frac{1}{2\sqrt{y}}\,dy + \frac{1}{2}I_{(0<\sqrt{y}<1)}\frac{1}{2\sqrt{y}}\,dy = \frac{1}{4\sqrt{y}}I_{(0<y<1)}\,dy + \frac{1}{4\sqrt{y}}I_{(0<y<1)}\,dy = \frac{1}{2\sqrt{y}}I_{(0<y<1)}\,dy.
$$

$$\therefore$$ $$f_Y(y) = \dfrac{1}{2\sqrt{y}}I_{(0<y<1)}$$.

## 1. Sampling and statistics

Sampling draws a sample $$x_1, \dots, x_n$$ from the population; inference goes back from the sample to the population.

**Statistical inference (frequentist inference).**

1. *Modeling.* Set up a set of assumed distributions:

   $$
   \mathcal{M} = \bigl\{f(\cdot\,; \theta) : \theta \in \Theta\bigr\} \quad (\text{the model}),
   $$

   where $$\theta$$ is the parameter and $$\Theta$$ is the parameter space (the set of possible parameters). Examples: $$\{N(\mu, \sigma^2) : \mu \in \mathbb{R},\ \sigma > 0\}$$ and $$\{\mathrm{Bin}(n, p) : p \in (0, 1)\}$$, $$n \in \mathbb{N}$$.
2. *Sampling.* Fix the sampling method: $$X_1, \dots, X_n \overset{iid}{\sim} f(x; \theta)$$.
3. Define a function of the sample for inference (a *statistic*): $$T(X_1, \dots, X_n)$$. Examples: $$\bar{X}$$, $$S^2 = \dfrac{1}{n-1}\sum(X_i - \bar{X})^2$$, $$\mathrm{med}(X)$$, etc.
4. Find the distribution of $$T(X_1, \dots, X_n)$$ (the *sampling distribution*).

   - $$X_1, \dots, X_n \overset{iid}{\sim} \mathrm{Ber}(p)$$ $$\to$$ $$\sum_{i=1}^{n}X_i \sim \mathrm{Bin}(n, p)$$.
   - $$X_1, \dots, X_n \overset{iid}{\sim} \mathrm{Poi}(\lambda)$$, $$\lambda > 0$$: $$\sum_{i=1}^{n}X_i \sim \mathrm{Poi}(n\lambda)$$.
   - $$X_1, \dots, X_n \overset{iid}{\sim} N(\mu, \sigma^2)$$: $$\bar{X} \sim N\bigl(\mu, \dfrac{\sigma^2}{n}\bigr)$$.
5. Do statistical inference using the sampling distribution (estimation: point estimation and interval estimation; hypothesis testing). $$\to$$ Content of Mathematical Statistics 2.

**Approximation of sampling distributions.**

1. Except for a few simple cases, it is not possible to find the sampling distribution exactly.
2. Approximate the sampling distribution for sample size $$n \to \infty$$.
   - (i) Asymptotic approximation ($$n \to \infty$$).
   - (ii) Monte Carlo approximation: generate the sample infinitely many times on a computer and approximate the sampling distribution (it is weak in extrapolation).

## Supplement from the textbook

**Random sample and statistic (§4.1).** A *random sample* from the population distribution with pdf $$f(x; \theta)$$, $$\theta \in \Omega$$, means $$X_1, X_2, \dots, X_n \overset{iid}{\sim} f(x; \theta)$$. A statistic $$u(X_1, \dots, X_n)$$ is a function of the random sample whose value is determined once the values of the sample are given. The parameter is a known characteristic of the population distribution, written $$\theta$$, and the set of possible parameters is the parameter space $$\Omega$$. The textbook justifies assuming independent, identically distributed observations by noting that, as the population size grows, sampling without replacement behaves almost the same as sampling with replacement (the binomial approximation of the hypergeometric distribution).

**Example 4.1.1.** (a) For a survey of the defective rate, the population distribution is $$\mathrm{Bernoulli}(p)$$; the unknown rate $$p$$ is the parameter and $$\Omega = \{p : 0 \le p \le 1\}$$. (b) For the number of plankton per unit volume of river water, a $$\mathrm{Poisson}(\lambda)$$ model with $$\Omega = \{\lambda : \lambda \ge 0\}$$. (c) For the distribution of errors in science experiments, $$N(\mu, \sigma^2)$$ with $$\theta = (\mu, \sigma^2)^t$$ and $$\Omega = \{(\mu, \sigma^2)^t : -\infty < \mu < +\infty,\ \sigma^2 > 0\}$$.

**Example 4.1.2.** For a $$\mathrm{Bernoulli}(p)$$ sample, the number of defectives $$X_1 + \cdots + X_n$$ and the sample proportion $$\hat{p} = (X_1 + \cdots + X_n)/n$$ are statistics. The sample mean $$\bar{X} = \frac{1}{n}(X_1 + \cdots + X_n)$$ and the sample variance $$S^2 = \frac{1}{n-1}\sum_{i=1}^{n}(X_i - \bar{X})^2$$ are used to estimate the population mean and variance. Ordering a continuous sample as $$X_{(1)} < \cdots < X_{(n)}$$ gives the order statistics, and the sample median is $$X_{(m+1)}$$ when $$n = 2m + 1$$ and $$(X_{(m)} + X_{(m+1)})/2$$ when $$n = 2m$$.

**Example 4.1.3.** (a) For a $$\mathrm{Bernoulli}(p)$$ sample, $$X_1 + \cdots + X_n \sim \mathrm{Bin}(n, p)$$, so $$P(\hat{p} = k/n) = \binom{n}{k}p^k(1 - p)^{n-k}$$, $$E(\hat{p}) = p$$, $$\mathrm{Var}(\hat{p}) = p(1 - p)/n$$: the distribution of $$\hat{p}$$ concentrates around $$p$$ as the sample size grows. (b) For a $$\mathrm{Poisson}(\lambda)$$ sample, $$X_1 + \cdots + X_n \sim \mathrm{Poisson}(n\lambda)$$, $$E(\bar{X}) = \lambda$$, $$\mathrm{Var}(\bar{X}) = \lambda/n$$.

**Example 4.1.4.** (a) For independent $$X_1 \sim \mathrm{Bin}(n_1, p)$$, $$X_2 \sim \mathrm{Bin}(n_2, p)$$, $$P(X_1 + X_2 = y) = \sum_{x_1 + x_2 = y}\binom{n_1}{x_1}\binom{n_2}{x_2}p^y(1 - p)^{n_1+n_2-y} = \binom{n_1 + n_2}{y}p^y(1 - p)^{n_1+n_2-y}$$, agreeing with Theorem 3.2.1. (b) The Poisson case is the computation in section 0 above. (c) For $$X \sim N(0, 1)$$ and $$Y = X^2$$, differentiating the cdf, $$\frac{d}{dy}\{P(X \le \sqrt{y}) - P(X \le -\sqrt{y})\} = \frac{1}{2}y^{-1/2}\{pdf_X(\sqrt{y}) + pdf_X(-\sqrt{y})\} = \frac{1}{\sqrt{2\pi}}y^{-1/2}e^{-y/2}$$, $$y > 0$$, which is the $$\mathrm{Gamma}(1/2, 2)$$ density because $$\Gamma(1/2) = \sqrt{\pi}$$.

> **Theorem 4.1.1 (One-to-one transformation of continuous variables).** Let $$X = (X_1, \dots, X_k)^t$$ be a $$k$$-dimensional continuous random variable and $$u = (u_1, \dots, u_k)^t : \mathcal{X} \to \mathcal{Y}$$ a function such that (a) $$P(X \in \mathcal{X}) = 1$$; (b) $$u$$ is one-to-one from $$\mathcal{X}$$ onto $$\mathcal{Y}$$; (c) $$\mathcal{X}$$ is open in $$\mathbb{R}^k$$ and $$u$$ is differentiable with continuous first partial derivatives and Jacobian $$J_u(x) = \det\bigl(\frac{\partial}{\partial x_i}u_j(x)\bigr) \ne 0$$ for all $$x \in \mathcal{X}$$. Then $$Y = u(X)$$ has density $$pdf_Y(y) = pdf_X(u^{-1}(y))\lvert J_{u^{-1}}(y)\rvert$$, $$y \in \mathcal{Y}$$; equivalently $$pdf_Y(y) = pdf_X(x)\bigl\lvert\det\bigl(\frac{\partial y}{\partial x}\bigr)\bigr\rvert^{-1}$$, $$y = u(x) \in \mathcal{Y}$$.
{: .theorem #thm-textbook-4-1-1 }

**Example 4.1.5 (location and scale).** If $$Z$$ has pdf $$f(z)$$, then for $$\sigma > 0$$ and real $$\mu$$, $$X = \sigma Z + \mu$$ has pdf $$\frac{1}{\sigma}f\bigl(\frac{x - \mu}{\sigma}\bigr)$$; $$\mu$$ is the location parameter and $$\sigma$$ the scale parameter. Examples of $$X \overset{d}{=} \sigma Z + \mu$$: the normal distribution $$N(\mu, \sigma^2)$$ with $$Z \sim N(0, 1)$$; the logistic distribution $$L(\mu, \sigma)$$ with $$f(z) = e^z/(1 + e^z)^2$$; the double exponential distribution $$DE(\mu, \sigma)$$ with $$f(z) = \frac{1}{2}e^{-\lvert z\rvert}$$; the Cauchy distribution $$C(\mu, \sigma)$$ with $$f(z) = \frac{1}{\pi}\frac{1}{1 + z^2}$$; the exponential distribution $$\mathrm{Exp}(\sigma) \overset{d}{=} \sigma\mathrm{Exp}(1)$$; and the gamma distribution $$\mathrm{Gamma}(\alpha, \beta) \overset{d}{=} \beta\mathrm{Gamma}(\alpha, 1)$$.

**Example 4.1.6.** For independent $$X_1 \sim \mathrm{Gamma}(\alpha_1, \beta)$$, $$X_2 \sim \mathrm{Gamma}(\alpha_2, \beta)$$ let $$Y_1 = X_1/(X_1 + X_2)$$, $$Y_2 = X_1 + X_2$$. The inverse is $$x_1 = y_1y_2$$, $$x_2 = y_2(1 - y_1)$$ with Jacobian $$y_2$$, so

$$
pdf_{Y_1, Y_2}(y_1, y_2) = \frac{1}{\Gamma(\alpha_1)\Gamma(\alpha_2)\beta^{\alpha_1+\alpha_2}}y_1^{\alpha_1-1}(1 - y_1)^{\alpha_2-1}I_{(0,1)}(y_1)\,y_2^{\alpha_1+\alpha_2-1}e^{-y_2/\beta}I_{(0,\infty)}(y_2).
$$

It is a product of a function of $$y_1$$ and a function of $$y_2$$, so $$Y_1 \perp Y_2$$, $$Y_1 \sim \mathrm{Beta}(\alpha_1, \alpha_2)$$ and $$Y_2 \sim \mathrm{Gamma}(\alpha_1 + \alpha_2, \beta)$$. This gives the definition $$\mathrm{Beta}(\alpha_1, \alpha_2) \overset{d}{=} \mathrm{Gamma}(\alpha_1)/(\mathrm{Gamma}(\alpha_1, \beta) \oplus \mathrm{Gamma}(\alpha_2, \beta))$$ and the identity $$\int_0^1x^{\alpha_1-1}(1 - x)^{\alpha_2-1}dx = \Gamma(\alpha_1)\Gamma(\alpha_2)/\Gamma(\alpha_1 + \alpha_2)$$.

**Example 4.1.7.** For independent $$X_1, X_2$$ with the common pdf $$I_{(0,1)}(x)$$, put $$Y = (X_1 + X_2)/2$$, $$Z = (X_1 - X_2)/2$$. The inverse is $$x_1 = y + z$$, $$x_2 = y - z$$ with $$\lvert J\rvert = 2$$, the joint pdf is $$2I_{(0 < y+z < 1,\ 0 < y-z < 1)}$$, and integrating over $$z$$ gives

$$
pdf_Y(y) = 4y\,I_{(0,1/2]}(y) + 4(1 - y)\,I_{(1/2,1)}(y) = (2 - 4\lvert y - 1/2\rvert)I_{(0,1)}(y),
$$

the *triangular distribution*. The general uniform distribution is $$U(a, b) \overset{d}{=} (b - a)U(0, 1) + a$$.

**Example 4.1.8 (polar coordinates).** For independent $$X, Y \sim N(0, 1)$$ with $$X = R\cos\Theta$$, $$Y = R\sin\Theta$$, the Jacobian is $$r$$, so $$pdf_{R,\Theta}(r, \theta) = re^{-r^2/2}I_{[0,\infty)}(r)\frac{1}{2\pi}I_{[0,2\pi)}(\theta)$$. Thus $$R$$ and $$\Theta$$ are independent, $$R^2/2 \sim \mathrm{Exp}(1)$$ and $$\Theta \sim U[0, 2\pi)$$.

**Example 4.1.9.** For independent $$X_i \sim \mathrm{Gamma}(\alpha_i, \beta)$$ ($$i = 1, \dots, k+1$$) and $$Y_i = X_i/(X_1 + \cdots + X_{k+1})$$ ($$i = 1, \dots, k$$), with $$Y_{k+1} = X_1 + \cdots + X_{k+1}$$ the Jacobian is $$y_{k+1}^k$$ and

$$
pdf_{Y_1, \dots, Y_k}(y_1, \dots, y_k) = \frac{\Gamma(\alpha_1 + \cdots + \alpha_{k+1})}{\Gamma(\alpha_1)\cdots\Gamma(\alpha_{k+1})}\Bigl\{\prod_{i=1}^{k}y_i^{\alpha_i-1}\Bigr\}(1 - y_1 - \cdots - y_k)^{\alpha_{k+1}-1}I_{(y_1>0,\dots,y_k>0,\ y_1+\cdots+y_k<1)},
$$

the Dirichlet distribution $$\mathrm{Dirichlet}(\alpha_1, \dots, \alpha_{k+1})$$.

> **Theorem 4.1.2 (Many-to-one transformation of continuous variables).** If in Theorem 4.1.1 the function $$u$$ is $$m$$-to-one, that is, $$\mathcal{X}$$ is a union of disjoint open sets $$\mathcal{X}_1, \dots, \mathcal{X}_m$$ such that the restriction $$u^r$$ to each $$\mathcal{X}_r$$ is one-to-one onto $$\mathcal{Y}$$ with the conditions of Theorem 4.1.1, then $$pdf_Y(y) = \sum_{r=1}^{m}pdf_X((u^r)^{-1}(y))\lvert J_{(u^r)^{-1}}(y)\rvert = \sum_{x : u(x) = y}pdf_X(x)\bigl\lvert\det\bigl(\frac{\partial u(x)}{\partial x}\bigr)\bigr\rvert^{-1}$$, $$y \in \mathcal{Y}$$.
{: .theorem #thm-textbook-4-1-2 }

**Example 4.1.10.** For $$X \sim U(-1, 1)$$ and $$Y = X^2$$: $$pdf_Y(y) = \sum_{x : x^2 = y}\frac{1}{2}\lvert 2x\rvert^{-1}I_{(0,1)}(y) = \frac{1}{2\sqrt{y}}I_{(0,1)}(y)$$.

**Example 4.1.11.** For $$X = (X_1, X_2)^t$$ with pdf $$\frac{1}{\pi}I_{(0 < x_1^2 + x_2^2 < 1)}$$, $$Y_1 = X_1^2 + X_2^2$$, $$Y_2 = X_1^2/(X_1^2 + X_2^2)$$. The map is four-to-one with $$\lvert\det(\partial y/\partial x)\rvert = 4\sqrt{y_2(1 - y_2)}$$, so $$pdf_Y(y_1, y_2) = I_{(0,1)}(y_1)\frac{1}{\pi}y_2^{-1/2}(1 - y_2)^{-1/2}I_{(0,1)}(y_2)$$: $$Y_1 \sim U(0, 1)$$, $$Y_2 \sim \mathrm{Beta}(1/2, 1/2)$$, independent.

## References

- 김우철, *수리통계학* (Mathematical Statistics), revised 2nd edition, 민영사, 2021 — Chapter 4, §4.1 (Examples 4.1.1 to 4.1.11, Theorems 4.1.1 and 4.1.2). The supplement is translated from the book.
- Mathematical Statistics 1 (326.311), Seoul National University, Spring 2025. Instructor: Jaeyong Lee (이재용).

[Previous: Chapter 3 Part 5](/posts/mathstat1-normal/) · [Overview](/posts/mathstat1-overview/) · [Next](/posts/mathstat1-t-f-distribution/)
