---
title: "Mathematical Statistics 1: Chapter 5 Exercises"
date: 2026-11-21 14:00:00 +0900
categories: [Study Notes, Mathematical Statistics 1]
tags: [exercises, central limit theorem, limiting distribution, convergence in probability, order statistics, delta method, variance stabilizing, sample quantile, bounded in probability]
description: Worked exercises 5.1 to 5.18 for Chapter 5 of Mathematical Statistics 1 — normal approximation, limits of extreme order statistics, uniform convergence of cdfs, boundedness in probability, variance stabilizing transformations, and the limiting distribution of sample quantiles.
math: true
mermaid: false
render_with_liquid: false
---

> The exercise statements are from the textbook. The answers to 5.1 to 5.12 are my own, translated into English as I wrote them, with the logic, definitions and small steps I left out filled in; 5.2(b) and 5.13 to 5.18 were not in my notes, so their answers are written out here from scratch. These exercises use [Parts 1 to 5](/posts/mathstat1-convergence-in-probability/) of Chapter 5. $$\Phi$$ is the cdf of $$N(0, 1)$$ and $$z_p = \Phi^{-1}(p)$$.
{: .prompt-info }

### Exercise 5.1

> **Exercise 5.1.** When a random variable $$X$$ follows the chi-squared distribution $$\chi^2(32)$$ with $$32$$ degrees of freedom, use the central limit theorem to find an approximate value of $$P(20 < X < 40)$$, and compare it with the value found with R.
{: .problem #ex5-1 }

Since $$X \sim \chi^2(32)$$, $$X \overset{d}{=} \sum_{i=1}^{32}X_i$$ with $$X_i \overset{iid}{\sim} \chi^2(1)$$, $$E(X_i) = 1$$, $$\mathrm{Var}(X_i) = 2$$. So $$E(X) = 32$$, $$\mathrm{Var}(X) = 64$$, and by the central limit theorem

$$
P(20 < X < 40) = P\Bigl(-\frac{12}{8} < \frac{X - 32}{\sqrt{2\times32}} < \frac{8}{8}\Bigr) \simeq \Phi(1) - \Phi(-1.5) = 0.8413 - 0.0668 = 0.7745.
$$

With R, `pchisq(40, 32) - pchisq(20, 32)` $$= 0.7947$$. The approximation $$0.7745$$ is close to the exact value.

### Exercise 5.2

> **Exercise 5.2.** When a random variable $$X$$ follows $$\mathrm{Poisson}(25)$$, use the central limit theorem to find approximate values of the following probabilities, and compare them with the values found with R. (a) $$P(19 < X \le 33)$$ (b) $$P(19.5 < X < 33.5)$$
{: .problem #ex5-2 }

Since $$X \sim \mathrm{Poisson}(25)$$, $$X \overset{d}{=} \sum_{i=1}^{25}X_i$$ with $$X_i \overset{iid}{\sim} \mathrm{Poisson}(1)$$, so $$E(X) = \mathrm{Var}(X) = 25$$.

**(a)**

$$
P(19 < X \le 33) = P\Bigl(\frac{19 - 25}{\sqrt{25}} < \frac{X - 25}{\sqrt{25}} \le \frac{33 - 25}{\sqrt{25}}\Bigr) \simeq \Phi(1.6) - \Phi(-1.2) = 0.9452 - 0.1151 = 0.8301.
$$

**(b)** In the same way, with the continuity correction (the event $$19.5 < X < 33.5$$ is the same event as $$19 < X \le 33$$ because $$X$$ takes integer values),

$$
P(19.5 < X < 33.5) \simeq \Phi\Bigl(\frac{33.5 - 25}{5}\Bigr) - \Phi\Bigl(\frac{19.5 - 25}{5}\Bigr) = \Phi(1.7) - \Phi(-1.1) = 0.9554 - 0.1357 = 0.8198.
$$

With R, `ppois(33, 25) - ppois(19, 25)` $$= 0.8166$$ for both (a) and (b), since they are the same event. The approximation in (b) ($$0.8198$$) is much closer to it than the approximation in (a) ($$0.8301$$), which shows the effect of the continuity correction.

### Exercise 5.3

> **Exercise 5.3.** For a random sample $$X_1, \dots, X_n$$ from the population with pdf $$f(x; \theta) = e^{-(x-\theta)}I_{(\theta,+\infty)}(x)$$ ($$\theta$$ a real number), let $$Y_n = \min_{1\le i\le n}X_i$$. Show that $$\mathrm{plim}\,Y_n = \theta$$.
{: .problem #ex5-3 }

Here $$Y_n = X_{(1)}$$. By the pdf of the smallest order statistic, with $$F(x) = (1 - e^{-(x-\theta)})I_{(x>\theta)}$$ the population cdf,

$$
f_{Y_n}(x) = \frac{n!}{0!\,(n-1)!}f(x; \theta)(1 - F(x))^{n-1} = n\bigl(1 + (e^{-(x-\theta)} - 1)I_{(x>\theta)}\bigr)^{n-1}e^{-(x-\theta)}I_{(x>\theta)} = ne^{-n(x-\theta)}I_{(x>\theta)},
$$

and the cdf is $$F_{Y_n}(x) = (1 - e^{-n(x-\theta)})I_{(x>\theta)}$$. For any $$\epsilon > 0$$ (we have $$Y_n > \theta$$ with probability $$1$$),

$$
\lim_{n\to\infty}P(\lvert Y_n - \theta\rvert \ge \epsilon) = \lim_{n\to\infty}P\bigl((Y_n \le \theta - \epsilon) \cup (Y_n \ge \theta + \epsilon)\bigr) = \lim_{n\to\infty}\bigl(0 + e^{-n\epsilon}\bigr) = 0.
$$

Therefore $$\mathrm{plim}\,Y_n = \theta$$.

### Exercise 5.4

> **Exercise 5.4.** For a random sample $$X_1, \dots, X_n$$ from the beta distribution $$\mathrm{Beta}(1, \alpha)$$, let $$Y_n = \max_{1\le i\le n}X_i$$. Find the limiting distribution of $$n^{1/\alpha}(1 - Y_n)$$.
{: .problem #ex5-4 }

Here $$Y_n = X_{(n)}$$ and $$X_i \sim \mathrm{Beta}(1, \alpha)$$ has pdf $$f(x) = \dfrac{\Gamma(1+\alpha)}{\Gamma(1)\Gamma(\alpha)}(1-x)^{\alpha-1}I_{(0<x<1)} = \alpha(1-x)^{\alpha-1}I_{(0<x<1)}$$ and cdf $$F(x) = (1 - (1-x)^{\alpha})I_{(0<x<1)} + I_{(x\ge1)}$$. For $$0 < y < 1$$,

$$
P(Y_n \le y) = P\Bigl(\bigcap_{i=1}^{n}(X_i \le y)\Bigr) = \{P(X_1 \le y)\}^n = \{1 - (1 - y)^{\alpha}\}^n.
$$

For $$y > 0$$ and $$n$$ large enough that $$n^{-1/\alpha}y < 1$$,

$$
\lim_{n\to\infty}P\bigl(n^{1/\alpha}(1 - Y_n) \le y\bigr) = \lim_{n\to\infty}P\bigl(Y_n \ge 1 - n^{-1/\alpha}y\bigr) = \lim_{n\to\infty}\Bigl(1 - \bigl\{1 - (1 - (1 - n^{-1/\alpha}y))^{\alpha}\bigr\}^n\Bigr) = \lim_{n\to\infty}\Bigl(1 - \bigl(1 - \tfrac{1}{n}y^{\alpha}\bigr)^n\Bigr) = 1 - e^{-y^{\alpha}}, \quad y > 0.
$$

(For $$y \le 0$$ the probability is $$0$$.) That is, $$n^{1/\alpha}(1 - Y_n) \xrightarrow{d} \mathrm{Weibull}(\alpha, 1)$$, whose pdf is $$\alpha y^{\alpha-1}e^{-y^{\alpha}}I_{(y>0)}$$.

### Exercise 5.5

> **Exercise 5.5.** For a random sample $$X_1, \dots, X_n$$ from the population with pdf $$f(x) = \alpha x^{-\alpha-1}I_{[1,\infty)}(x)$$, let $$Y_n = \max_{1\le i\le n}X_i$$. Find the limiting distribution of $$n^{-1/\alpha}Y_n$$.
{: .problem #ex5-5 }

The cdf is $$F(x) = (1 - x^{-\alpha})I_{(x\ge1)}$$. Then $$P(Y_n \le y) = \{P(X_1 \le y)\}^n = \{1 - y^{-\alpha}\}^n$$ for $$y \ge 1$$. For $$x > 0$$ (so that $$n^{1/\alpha}x \ge 1$$ for large $$n$$),

$$
\lim_{n\to\infty}P(n^{-1/\alpha}Y_n \le x) = \lim_{n\to\infty}P(Y_n \le n^{1/\alpha}x) = \lim_{n\to\infty}\bigl(1 - (n^{1/\alpha}x)^{-\alpha}\bigr)^n = \lim_{n\to\infty}\Bigl(1 - \frac{1}{n}x^{-\alpha}\Bigr)^n = e^{-x^{-\alpha}}, \quad x > 0,
$$

and the probability is $$0$$ for $$x < n^{-1/\alpha}$$, hence $$0$$ in the limit for $$x \le 0$$. So the limiting cdf is $$e^{-x^{-\alpha}}I_{(x>0)}$$, and the limiting pdf is

$$
f(x) = \alpha x^{-\alpha-1}e^{-x^{-\alpha}}I_{(x>0)}
$$

(the Fréchet distribution).

### Exercise 5.6

> **Exercise 5.6.** For a random sample $$X_1, \dots, X_n$$ from the standard exponential distribution $$\mathrm{Exp}(1)$$, let $$Y_n = \max_{1\le i\le n}X_i$$. Find the limiting distribution of $$Y_n - \log n$$.
{: .problem #ex5-6 }

The pdf is $$f(x) = e^{-x}I_{(x>0)}$$ and the cdf is $$F(x) = (1 - e^{-x})I_{(x>0)}$$. Then $$P(Y_n \le y) = (1 - e^{-y})^nI_{(y>0)}$$. For any real $$y$$ (with $$y > -\log n$$, which holds for large $$n$$),

$$
P(Y_n - \log n \le y) = P(Y_n \le \log n + y) = \Bigl(1 - \frac{1}{n}e^{-y}\Bigr)^n \longrightarrow e^{-e^{-y}}.
$$

That is, $$Y_n - \log n \xrightarrow{d} Z$$ with cdf $$e^{-e^{-y}}$$, $$-\infty < y < \infty$$ (the Gumbel distribution).

### Exercise 5.7

> **Exercise 5.7.** For a random sample $$X_1, \dots, X_n$$ from the beta distribution $$\mathrm{Beta}(\alpha, 1)$$ ($$\alpha > 0$$), let $$Y_n = \min_{1\le i\le n}X_i$$. Find the value of $$r$$ for which the limiting distribution of $$n^rY_n$$ ($$r > 0$$) exists, and find the limiting distribution.
{: .problem #ex5-7 }

For $$X_i \sim \mathrm{Beta}(\alpha, 1)$$ the pdf is $$f(x) = \dfrac{\Gamma(\alpha+1)}{\Gamma(\alpha)}x^{\alpha-1}I_{(0<x<1)} = \alpha x^{\alpha-1}I_{(0<x<1)}$$ and the cdf is $$F(x) = x^{\alpha}I_{(0<x<1)} + I_{(x\ge1)}$$. Then

$$
P(Y_n \le y) = 1 - P(Y_n > y) = 1 - \{P(X_1 > y)\}^n,
$$

where $$P(X_1 > y) = 0$$ for $$y \ge 1$$, $$P(X_1 > y) = 1 - y^{\alpha}$$ for $$0 < y < 1$$, and $$P(X_1 > y) = 1$$ for $$y \le 0$$. So

$$
P(n^rY_n \le y) = P\Bigl(Y_n \le \frac{y}{n^r}\Bigr) = \begin{cases}1 & (y \ge n^r) \\ 1 - \bigl(1 - n^{-\alpha r}y^{\alpha}\bigr)^n & (0 < y < n^r) \\ 0 & (y \le 0).\end{cases}
$$

For fixed $$y > 0$$, writing $$\bigl(1 - n^{-\alpha r}y^{\alpha}\bigr)^n = \Bigl\{\bigl(1 - n^{-\alpha r}y^{\alpha}\bigr)^{n^{\alpha r}y^{-\alpha}}\Bigr\}^{y^{\alpha}n^{1-\alpha r}}$$, where the inside tends to $$e^{-1}$$ (as $$n^{-\alpha r}y^{\alpha} \to 0$$), we have

- if $$\alpha r > 1$$: $$y^{\alpha}n^{1-\alpha r} \to 0$$, so the power tends to $$1$$ and $$P(n^rY_n \le y) \to 0$$ (the probability escapes to infinity, so there is no limiting distribution);
- if $$0 < \alpha r < 1$$: $$y^{\alpha}n^{1-\alpha r} \to \infty$$, so the power tends to $$0$$ and $$P(n^rY_n \le y) \to 1$$ for every $$y > 0$$ (the limit is the degenerate distribution at $$0$$);
- if $$\alpha r = 1$$: the exponent is $$y^{\alpha}$$ and $$P(n^rY_n \le y) \to 1 - e^{-y^{\alpha}}$$.

So the nondegenerate limiting distribution exists exactly for $$r = 1/\alpha$$, and it is the Weibull distribution: $$n^{1/\alpha}Y_n \xrightarrow{d} Z$$ with cdf $$(1 - e^{-y^{\alpha}})I_{(y>0)}$$ and pdf $$\alpha y^{\alpha-1}e^{-y^{\alpha}}I_{(y>0)}$$.

### Exercise 5.8

> **Exercise 5.8.** For a random sample $$U_1, \dots, U_n$$ from the uniform distribution $$U(0, 1)$$, let $$X_n = \min_{1\le i\le n}U_i$$, $$Y_n = \max_{1\le i\le n}U_i$$, $$R_n = Y_n - X_n$$. (a) Show that $$\mathrm{plim}(X_n, Y_n)^t = (0, 1)^t$$. (b) Find the limiting distribution of $$n(1 - R_n)$$.
{: .problem #ex5-8 }

By the order statistics of the uniform distribution, $$X_n \sim \mathrm{Beta}(1, n)$$ and $$Y_n \sim \mathrm{Beta}(n, 1)$$, so

$$
E(X_n) = \frac{1}{n+1}, \quad \mathrm{Var}(X_n) = \frac{n}{(n+1)^2(n+2)}, \qquad E(Y_n) = \frac{n}{n+1}, \quad \mathrm{Var}(Y_n) = \frac{n}{(n+1)^2(n+2)},
$$

and the pdf of the range is $$f_{R_n}(y) = n(n-1)y^{n-2}(1-y)I_{(0<y<1)}$$ (Exercise 4.16).

**(a)** $$\lim E(X_n) = 0$$, $$\lim\mathrm{Var}(X_n) = 0$$, so by the lemma (if $$\mathrm{Var}(Y_n) \to 0$$ and $$E(Y_n) \to a$$ then $$Y_n \xrightarrow{P} a$$), $$\mathrm{plim}\,X_n = 0$$. In the same way $$\lim E(Y_n) = 1$$, $$\lim\mathrm{Var}(Y_n) = 0$$ give $$\mathrm{plim}\,Y_n = 1$$. Therefore $$\mathrm{plim}(X_n, Y_n)^t = (0, 1)^t$$ (convergence in probability of a vector is componentwise).

**(b)** The cdf of $$R_n$$ is $$F_{R_n}(y) = \bigl(ny^{n-1}(1-y) + y^n\bigr)I_{(0<y<1)} + I_{(y\ge1)}$$. For $$x > 0$$ and $$n > x$$,

$$
P(n(1 - R_n) \le x) = P\Bigl(R_n \ge 1 - \frac{x}{n}\Bigr) = 1 - n\Bigl(1 - \frac{x}{n}\Bigr)^{n-1}\frac{x}{n} - \Bigl(1 - \frac{x}{n}\Bigr)^n \longrightarrow 1 - xe^{-x} - e^{-x}, \quad x > 0.
$$

That is, $$n(1 - R_n) \xrightarrow{d} \mathrm{Gamma}(2, 1)$$, whose cdf is $$1 - (1 + x)e^{-x}$$ ($$x > 0$$).

### Exercise 5.9

> **Exercise 5.9.** For random variables $$X_n$$ and $$Z$$ with $$X_n \xrightarrow{d} Z$$, when the cdf of $$Z$$ is continuous at every real number, show that
>
> $$
> \lim_{n\to\infty}\sup_x\lvert P(X_n \le x) - P(Z \le x)\rvert = 0.
> $$
{: .problem #ex5-9 }

① $$X_n \xrightarrow{d} Z$$ means, with $$F_n$$ the cdf of $$X_n$$ and $$F_Z$$ the cdf of $$Z$$, $$\lim F_n(x) = F_Z(x)$$ at all continuity points of $$F_Z$$; ② $$F_Z$$ is continuous at every $$x \in \mathbb{R}$$, so $$\lim F_n(x) = F_Z(x)$$ for all $$x \in \mathbb{R}$$.

Write $$F = F_Z$$. For an arbitrary natural number $$K > 1$$, let $$x_j = \inf\{x : F(x) \ge j/K\}$$, $$j = 1, \dots, K-1$$. As $$F$$ is continuous, for every $$y \in (0, 1)$$ there is $$x$$ with $$F(x) = y$$; hence $$F(x_j) = j/K$$. Set $$x_0 = -\infty$$ and $$x_K = +\infty$$ (so $$F(x_0) = 0$$, $$F(x_K) = 1$$, and also $$F_n(x_0) = 0 = F(x_0)$$, $$F_n(x_K) = 1 = F(x_K)$$).

Then for any $$j \in \{0, 1, \dots, K-1\}$$, if $$x_j \le x < x_{j+1}$$, then since $$F_n$$ is monotone increasing, $$F_n(x_j) \le F_n(x) \le F_n(x_{j+1})$$, and $$F(x_{j+1}) - \frac{1}{K} = F(x_j) \le F(x) \le F(x_{j+1}) = F(x_j) + \frac{1}{K}$$. Therefore

$$
F_n(x_j) - F(x_j) - \frac{1}{K} \le F_n(x) - F(x) \le F_n(x_{j+1}) - F(x_{j+1}) + \frac{1}{K},
$$

so

$$
\sup_{x_j\le x<x_{j+1}}\lvert F_n(x) - F(x)\rvert \le \max\bigl(\lvert F_n(x_j) - F(x_j)\rvert,\ \lvert F_n(x_{j+1}) - F(x_{j+1})\rvert\bigr) + \frac{1}{K},
$$

and taking the maximum over $$j$$,

$$
\sup_x\lvert F_n(x) - F(x)\rvert \le \max_{1\le j\le K-1}\lvert F_n(x_j) - F(x_j)\rvert + \frac{1}{K}
$$

(the terms at $$x_0$$ and $$x_K$$ are $$0$$). Letting $$n \to \infty$$,

$$
\lim_{n\to\infty}\sup_x\lvert F_n(x) - F(x)\rvert \le \max_{1\le j\le K-1}\lim_{n\to\infty}\lvert F_n(x_j) - F(x_j)\rvert + \frac{1}{K} = \frac{1}{K},
$$

because $$X_n \xrightarrow{d} Z$$ and $$F$$ is continuous, so $$\lim\lvert F_n(x_j) - F(x_j)\rvert = 0$$ for each $$j = 1, \dots, K-1$$ (a finite maximum). Hence $$0 \le \overline{\lim}\,\sup_x\lvert F_n(x) - F(x)\rvert \le \frac{1}{K}$$ for every $$K = 1, 2, \dots$$, and therefore $$\lim_{n\to\infty}\sup_x\lvert F_n(x) - F(x)\rvert = 0$$.

### Exercise 5.10

> **Exercise 5.10.** For a sequence of random variables $$X_n$$ ($$n = 1, 2, \dots$$), if $$\lim_{k\to\infty}\sup_nP(\lvert X_n\rvert > k) = 0$$, then $$X_n$$ is said to be *bounded in probability*, written $$X_n = O_P(1)$$, $$n \to \infty$$. For $$Z_n$$ with $$\mathrm{plim}\,Z_n = 0$$ we write $$Z_n = o_P(1)$$, $$n \to \infty$$. Show that if $$X_n = O_P(1)$$, $$Y_n = O_P(1)$$, $$Z_n = o_P(1)$$, then (a) $$X_n + Y_n = O_P(1)$$, (b) $$X_nY_n = O_P(1)$$, (c) $$Z_nX_n = o_P(1)$$, (d) $$Z_n = O_P(1)$$.
{: .problem #ex5-10 }

**(a)** By the assumption, $$\lim_{k\to\infty}\sup_nP(\lvert X_n\rvert > k) = 0$$ and $$\lim_{k\to\infty}\sup_nP(\lvert Y_n\rvert > k) = 0$$. Since $$(\lvert X_n + Y_n\rvert > k) \subseteq (\lvert X_n\rvert > \frac{k}{2}) \cup (\lvert Y_n\rvert > \frac{k}{2})$$,

$$
P(\lvert X_n + Y_n\rvert > k) \le P\bigl(\lvert X_n\rvert > \tfrac{k}{2}\bigr) + P\bigl(\lvert Y_n\rvert > \tfrac{k}{2}\bigr),
$$

so $$\sup_nP(\lvert X_n + Y_n\rvert > k) \le \sup_nP(\lvert X_n\rvert > \frac{k}{2}) + \sup_nP(\lvert Y_n\rvert > \frac{k}{2})$$, and the right side tends to $$0$$ as $$k \to \infty$$. Hence $$X_n + Y_n = O_P(1)$$.

**(b)** Since $$(\lvert X_nY_n\rvert > k) \subseteq (\lvert X_n\rvert > \sqrt{k}) \cup (\lvert Y_n\rvert > \sqrt{k})$$,

$$
\sup_nP(\lvert X_nY_n\rvert > k) \le \sup_nP(\lvert X_n\rvert > \sqrt{k}) + \sup_nP(\lvert Y_n\rvert > \sqrt{k}) \xrightarrow{k\to\infty} 0,
$$

so $$X_nY_n = O_P(1)$$.

**(c)** For given $$\epsilon > 0$$ and any $$K > 0$$,

$$
P(\lvert X_nZ_n\rvert > \epsilon) \le P(\lvert X_n\rvert \le K,\ \lvert Z_nX_n\rvert > \epsilon) + P(\lvert X_n\rvert > K) \le P\bigl(\lvert Z_n\rvert > \tfrac{\epsilon}{K}\bigr) + P(\lvert X_n\rvert > K) \le P\bigl(\lvert Z_n\rvert > \tfrac{\epsilon}{K}\bigr) + \sup_nP(\lvert X_n\rvert > K).
$$

Therefore

$$
\lim_{n\to\infty}P(\lvert X_nZ_n\rvert > \epsilon) \le \lim_{n\to\infty}P\bigl(\lvert Z_n\rvert > \tfrac{\epsilon}{K}\bigr) + \sup_nP(\lvert X_n\rvert > K) = 0 + \sup_nP(\lvert X_n\rvert > K),
$$

where the first limit is $$0$$ since $$\mathrm{plim}\,Z_n = 0$$. Since $$K$$ is arbitrary and $$\lim_{K\to\infty}\sup_nP(\lvert X_n\rvert > K) = 0$$, we get $$\lim_{n\to\infty}P(\lvert X_nZ_n\rvert > \epsilon) = 0$$, that is, $$Z_nX_n = o_P(1)$$.

**(d)** (Convergence in probability implies boundedness in probability.) For given $$\epsilon > 0$$: since $$\lim_{n\to\infty}P(\lvert Z_n\rvert > 1) = 0$$, there is $$N$$ such that $$P(\lvert Z_n\rvert > 1) < \epsilon$$ for all $$n > N$$. Meanwhile, for each $$i \in \{1, \dots, N\}$$, a single random variable satisfies $$\lim_{x\to\infty}P(\lvert Z_i\rvert > x) = 0$$ (the tail of a probability), so there is $$k_i$$ with $$P(\lvert Z_i\rvert > k_i) < \epsilon$$. Let $$K = \max\{1, k_1, \dots, k_N\}$$. Then for all $$k \ge K$$, $$P(\lvert Z_n\rvert > k) < \epsilon$$ for every $$n \le N$$ (by the choice of $$k_i$$) and for every $$n > N$$ (since $$P(\lvert Z_n\rvert > k) \le P(\lvert Z_n\rvert > 1) < \epsilon$$). Hence $$\sup_nP(\lvert Z_n\rvert > k) \le \epsilon$$ for $$k \ge K$$, and $$\lim_{k\to\infty}\sup_nP(\lvert Z_n\rvert > k) = 0$$, that is, $$Z_n = O_P(1)$$.

### Exercise 5.11

> **Exercise 5.11.** If $$X_n \xrightarrow{d} Z$$ and the cdfs of $$X_n$$ and $$Z$$ are continuous at every real number, show that $$X_n = O_P(1)$$, $$n \to \infty$$.
{: .problem #ex5-11 }

By the assumption, $$\lim F_{X_n}(x) = F_Z(x)$$ for all $$x$$, so $$\lim_{n\to\infty}P(\lvert X_n\rvert > k) = P(\lvert Z\rvert > k)$$ for every $$k > 0$$ (as $$P(\lvert X_n\rvert > k) = 1 - F_{X_n}(k) + F_{X_n}(-k)$$ at points where the cdf is continuous). Also $$\lim_{k\to\infty}P(\lvert Z\rvert > k) = 0$$.

Given $$\epsilon > 0$$, there is $$k_0$$ with $$P(\lvert Z\rvert > k_0) < \frac{1}{2}\epsilon$$. And by the uniform convergence of Exercise 5.9 (or simply by the limit above) there is $$N$$ such that for $$n > N$$, $$\lvert P(\lvert X_n\rvert > k_0) - P(\lvert Z\rvert > k_0)\rvert < \frac{1}{2}\epsilon$$. Therefore

$$
\sup_{n>N}P(\lvert X_n\rvert > k_0) \le P(\lvert Z\rvert > k_0) + \lvert P(\lvert X_n\rvert > k_0) - P(\lvert Z\rvert > k_0)\rvert < \epsilon.
$$

Meanwhile, for each $$i \in \{1, \dots, N\}$$, $$\lim_{x\to\infty}P(\lvert X_i\rvert > x) = 0$$ (the tail of a probability), so there is $$k_i$$ with $$P(\lvert X_i\rvert > k_i) < \epsilon$$. Let $$K = \max\{k_0, k_1, \dots, k_N\}$$. Then for $$k \ge K$$, $$\max_{1\le n\le N}P(\lvert X_n\rvert > k) \le \max_nP(\lvert X_n\rvert > k_n) < \epsilon$$ and $$\sup_{n>N}P(\lvert X_n\rvert > k) \le \sup_{n>N}P(\lvert X_n\rvert > k_0) < \epsilon$$. Hence $$\sup_nP(\lvert X_n\rvert > k) \le \epsilon$$ for all $$k \ge K$$, that is, $$X_n = O_P(1)$$.

### Exercise 5.12

> **Exercise 5.12.** For the sample mean $$\bar{X}_n$$ of a random sample $$X_1, \dots, X_n$$ from $$\mathrm{Poisson}(\lambda)$$, find a variance stabilizing transformation $$g$$ with $$\sqrt{n}(g(\bar{X}_n) - g(\lambda)) \xrightarrow{d} Z$$, $$Z \sim N(0, 1)$$, and explain how to find an asymptotic confidence interval for $$\lambda$$ using this result.
{: .problem #ex5-12 }

By the central limit theorem, $$\sqrt{n}\dfrac{\bar{X}_n - \mu}{\sigma} \xrightarrow{d} N(0, 1)$$, and for $$\mathrm{Poisson}(\lambda)$$, $$\mu = \lambda$$, $$\sigma^2 = \lambda$$, so $$\sqrt{n}(\bar{X}_n - \lambda) \xrightarrow{d} N(0, \lambda)$$. By the delta method, for a differentiable $$g$$ with continuous derivative,

$$
\sqrt{n}(g(\bar{X}_n) - g(\lambda)) \xrightarrow{d} N\bigl(0, (g'(\lambda))^2\lambda\bigr).
$$

For the variance to be $$1$$ we need $$(g'(\lambda))^2\lambda = 1$$, that is, $$g'(\lambda) = \dfrac{1}{\sqrt{\lambda}}$$, so

$$
g(\lambda) = 2\sqrt{\lambda}, \qquad \sqrt{n}\bigl(2\sqrt{\bar{X}_n} - 2\sqrt{\lambda}\bigr) \xrightarrow{d} N(0, 1).
$$

*Asymptotic confidence interval.* For $$0 < p < \frac{1}{2}$$ (the lower quantile $$z_p = \Phi^{-1}(p)$$ and $$z_{1-p} = -z_p$$),

$$
\lim P\bigl(\Phi^{-1}(p) \le \sqrt{n}(g(\bar{X}_n) - g(\lambda)) \le \Phi^{-1}(1 - p)\bigr) = 1 - 2p,
$$

that is, with $$z = \Phi^{-1}(1-p) = -\Phi^{-1}(p) = z_{1-p}$$,

$$
P\Bigl(\sqrt{\bar{X}_n} - \frac{z}{2\sqrt{n}} \le \sqrt{\lambda} \le \sqrt{\bar{X}_n} + \frac{z}{2\sqrt{n}}\Bigr) \simeq 1 - 2p.
$$

Therefore an asymptotic $$100(1 - 2p)\%$$ confidence interval for $$\lambda$$ is

$$
\Bigl[\Bigl(\max\bigl\{0, \sqrt{\bar{X}_n} - \tfrac{z}{2\sqrt{n}}\bigr\}\Bigr)^2,\ \Bigl(\sqrt{\bar{X}_n} + \tfrac{z}{2\sqrt{n}}\Bigr)^2\Bigr].
$$

For example $$p = 0.025$$, $$z = 1.96$$ gives the $$95\%$$ interval.

### Exercise 5.13

> **Exercise 5.13.** For the sample proportion $$\hat{p}_n = \sum_{i=1}^{n}X_i/n$$ from a random sample $$X_1, \dots, X_n$$ from $$\mathrm{Bernoulli}(p)$$, find a variance stabilizing transformation $$g$$ with $$\sqrt{n}(g(\hat{p}_n) - g(p)) \xrightarrow{d} Z$$, $$Z \sim N(0, 1)$$, and explain how to find an asymptotic confidence interval for $$p$$ using this result.
{: .problem #ex5-13 }

(My own answer; it was not in my notes.) By the central limit theorem, $$\sqrt{n}(\hat{p}_n - p) \xrightarrow{d} N(0, p(1-p))$$. By the delta method, for a differentiable $$g$$ with continuous derivative, $$\sqrt{n}(g(\hat{p}_n) - g(p)) \xrightarrow{d} N(0, (g'(p))^2p(1-p))$$. We need $$(g'(p))^2p(1-p) = 1$$, that is, $$g'(p) = \dfrac{1}{\sqrt{p(1-p)}}$$. Since $$\dfrac{d}{dp}\,2\arcsin\sqrt{p} = 2\cdot\dfrac{1}{\sqrt{1-p}}\cdot\dfrac{1}{2\sqrt{p}} = \dfrac{1}{\sqrt{p(1-p)}}$$,

$$
g(p) = 2\arcsin\sqrt{p}, \qquad \sqrt{n}\bigl(2\arcsin\sqrt{\hat{p}_n} - 2\arcsin\sqrt{p}\bigr) \xrightarrow{d} N(0, 1).
$$

*Asymptotic confidence interval.* For the upper $$\alpha/2$$ quantile $$z_{\alpha/2}$$,

$$
P\Bigl(-z_{\alpha/2} \le \sqrt{n}\bigl(2\arcsin\sqrt{\hat{p}_n} - 2\arcsin\sqrt{p}\bigr) \le z_{\alpha/2}\Bigr) \simeq 1 - \alpha,
$$

that is, $$\arcsin\sqrt{p}$$ lies in $$\arcsin\sqrt{\hat{p}_n} \pm \dfrac{z_{\alpha/2}}{2\sqrt{n}}$$. Since $$p = \sin^2(\arcsin\sqrt{p})$$ is increasing in $$\arcsin\sqrt{p} \in [0, \pi/2]$$, an asymptotic $$100(1-\alpha)\%$$ confidence interval for $$p$$ is

$$
\Bigl[\sin^2\Bigl(\max\bigl\{0, \arcsin\sqrt{\hat{p}_n} - \tfrac{z_{\alpha/2}}{2\sqrt{n}}\bigr\}\Bigr),\ \sin^2\Bigl(\min\bigl\{\tfrac{\pi}{2}, \arcsin\sqrt{\hat{p}_n} + \tfrac{z_{\alpha/2}}{2\sqrt{n}}\bigr\}\Bigr)\Bigr].
$$

### Exercise 5.14

> **Exercise 5.14.** In independent Bernoulli trials $$X_1, \dots, X_n, \dots$$ with success rate $$p$$ ($$0 < p < 1$$), let $$W_r$$ be the number of trials up to the $$r$$-th success, and $$\hat{p}_r = r/W_r$$. (a) Find the limiting distribution of $$\sqrt{r}(\hat{p}_r - p)$$ as $$r \to \infty$$. (b) Find a variance stabilizing transformation $$g$$ with $$\sqrt{r}(g(\hat{p}_r) - g(p)) \xrightarrow{d} N(0, 1)$$ as $$r \to \infty$$, and explain how to find an approximate $$95\%$$ confidence interval for $$p$$ for large $$r$$ using this result.
{: .problem #ex5-14 }

(My own answer; it was not in my notes.)

**(a)** By the representational definition of the negative binomial distribution, $$W_r \overset{d}{=} Z_1 + \cdots + Z_r$$ with $$Z_i \overset{iid}{\sim} \mathrm{Geo}(p)$$, $$E(Z_1) = 1/p$$, $$\mathrm{Var}(Z_1) = (1-p)/p^2$$. By the central limit theorem,

$$
\sqrt{r}\Bigl(\frac{W_r}{r} - \frac{1}{p}\Bigr) \xrightarrow{d} N\Bigl(0, \frac{1-p}{p^2}\Bigr).
$$

Now $$\hat{p}_r = r/W_r = h(W_r/r)$$ with $$h(x) = 1/x$$, $$h(1/p) = p$$, $$h'(1/p) = -p^2$$, so by the delta method

$$
\sqrt{r}(\hat{p}_r - p) \xrightarrow{d} N\Bigl(0, p^4\cdot\frac{1-p}{p^2}\Bigr) = N\bigl(0, p^2(1-p)\bigr).
$$

**(b)** By the delta method for $$g$$, $$\sqrt{r}(g(\hat{p}_r) - g(p)) \xrightarrow{d} N(0, (g'(p))^2p^2(1-p))$$. We need $$g'(p) = \dfrac{1}{p\sqrt{1-p}}$$. With $$s = \sqrt{1-p}$$, $$p = 1 - s^2$$, $$dp = -2s\,ds$$,

$$
\int\frac{dp}{p\sqrt{1-p}} = \int\frac{-2s\,ds}{(1-s^2)s} = -2\int\frac{ds}{1-s^2} = -\log\frac{1+s}{1-s} = \log\frac{1 - \sqrt{1-p}}{1 + \sqrt{1-p}}.
$$

So

$$
g(p) = \log\frac{1 - \sqrt{1-p}}{1 + \sqrt{1-p}}, \qquad \sqrt{r}(g(\hat{p}_r) - g(p)) \xrightarrow{d} N(0, 1).
$$

*Approximate $$95\%$$ confidence interval.* $$P\bigl(\lvert\sqrt{r}(g(\hat{p}_r) - g(p))\rvert \le 1.96\bigr) \simeq 0.95$$, so $$g(p) \in [c_1, c_2]$$ with $$c_1 = g(\hat{p}_r) - \dfrac{1.96}{\sqrt{r}}$$, $$c_2 = g(\hat{p}_r) + \dfrac{1.96}{\sqrt{r}}$$. The function $$g$$ is negative and increasing on $$(0, 1)$$; solving $$g(p) = c$$ gives $$\sqrt{1-p} = \dfrac{1 - e^{c}}{1 + e^{c}}$$, that is, $$p = 1 - \Bigl(\dfrac{1 - e^c}{1 + e^c}\Bigr)^2 = \dfrac{4e^c}{(1 + e^c)^2}$$ for $$c < 0$$. Therefore the approximate $$95\%$$ confidence interval for $$p$$ is

$$
\Bigl[\frac{4e^{c_1}}{(1 + e^{c_1})^2},\ \frac{4e^{c_2}}{(1 + e^{c_2})^2}\Bigr] \qquad(\text{with the upper end taken as } 1 \text{ if } c_2 \ge 0).
$$

### Exercise 5.15

> **Exercise 5.15.** In the process of finding the limiting distribution of the sample quantile in Example 5.3.8, for the random variables defined by $$Y_n = \dfrac{1}{n}Z_1 + \cdots + \dfrac{1}{n-r_n+1}Z_{r_n}$$, $$Z_i \overset{iid}{\sim} \mathrm{Exp}(1)$$, and $$W_n = \sqrt{n}\dfrac{Y_n - (-\log(1-\alpha))}{\sqrt{\alpha/(1-\alpha)}}$$, explain that (a) $$cgf_{Y_n}(s) \underset{n\to\infty}{\sim} -s\log(1-\alpha) + \dfrac{s^2}{2n}\dfrac{\alpha}{1-\alpha}$$; (b) $$cgf_{W_n}(t) = cgf_{Y_n}(\sqrt{n}t/\sqrt{\alpha/(1-\alpha)}) + \sqrt{n}t\log(1-\alpha)/\sqrt{\alpha/(1-\alpha)}$$; (c) $$cgf_{W_n}(t) \underset{n\to\infty}{\sim} \dfrac{1}{2}t^2$$.
{: .problem #ex5-15 }

(My own answer; it was not in my notes.) Write $$\alpha_n = r_n/n$$, so $$\alpha_n \to \alpha \in (0, 1)$$, and as in Example 5.3.8 we treat $$\alpha_n$$ as $$\alpha$$ in the centering (this needs $$\sqrt{n}(\alpha_n - \alpha) \to 0$$, which is what "$$r_n \sim \alpha n$$" is used for here). Let

$$
\mu_n = \sum_{i=1}^{r_n}\frac{1}{n-i+1}, \qquad v_n = \sum_{i=1}^{r_n}\frac{1}{(n-i+1)^2}.
$$

By the Euler–Maclaurin / integral comparison, $$\mu_n = \log\dfrac{n}{n-r_n} + O(\tfrac{1}{n}) = -\log(1-\alpha_n) + O(\tfrac{1}{n})$$ and $$v_n = \dfrac{1}{n-r_n} - \dfrac{1}{n} + O(\tfrac{1}{n^2}) = \dfrac{1}{n}\dfrac{\alpha_n}{1-\alpha_n} + O(\tfrac{1}{n^2})$$.

**(a)** The cgf of $$Z_i \sim \mathrm{Exp}(1)$$ is $$-\log(1 - u)$$, $$u < 1$$, so for $$Y_n = \sum_{i=1}^{r_n}\frac{1}{n-i+1}Z_i$$ (independent summands),

$$
cgf_{Y_n}(s) = -\sum_{i=1}^{r_n}\log\Bigl(1 - \frac{s}{n-i+1}\Bigr) = \sum_{i=1}^{r_n}\Bigl\{\frac{s}{n-i+1} + \frac{s^2}{2(n-i+1)^2} + \frac{s^3}{3(n-i+1)^3} + \cdots\Bigr\}
$$

$$
= s\mu_n + \frac{s^2}{2}v_n + R_n(s), \qquad \lvert R_n(s)\rvert \le C\lvert s\rvert^3\sum_{i=1}^{r_n}\frac{1}{(n-i+1)^3} = O\Bigl(\frac{\lvert s\rvert^3}{n^2}\Bigr),
$$

valid when $$\lvert s\rvert/(n - r_n + 1) < 1/2$$. Hence for $$s$$ fixed, or of order $$\sqrt{n}$$ (as in (b)), $$R_n(s) \to 0$$ and

$$
cgf_{Y_n}(s) \underset{n\to\infty}{\sim} -s\log(1-\alpha) + \frac{s^2}{2n}\frac{\alpha}{1-\alpha}.
$$

**(b)** For a linear function $$a + bY$$ of $$Y$$, $$cgf_{a+bY}(t) = at + cgf_Y(bt)$$. With $$W_n = \dfrac{\sqrt{n}}{\sigma}Y_n - \dfrac{\sqrt{n}}{\sigma}(-\log(1-\alpha))$$, $$\sigma = \sqrt{\alpha/(1-\alpha)}$$,

$$
cgf_{W_n}(t) = cgf_{Y_n}\Bigl(\frac{\sqrt{n}\,t}{\sigma}\Bigr) + \frac{\sqrt{n}\,t}{\sigma}\log(1 - \alpha),
$$

which is the stated formula.

**(c)** Substitute $$s = \sqrt{n}t/\sigma$$ in (a): the first term is $$-\dfrac{\sqrt{n}t}{\sigma}\log(1-\alpha)$$, which cancels the second term of (b), and the quadratic term is $$\dfrac{s^2}{2n}\dfrac{\alpha}{1-\alpha} = \dfrac{t^2}{2\sigma^2}\sigma^2 = \dfrac{1}{2}t^2$$. Therefore $$cgf_{W_n}(t) \underset{n\to\infty}{\sim} \dfrac{1}{2}t^2$$, that is, $$mgf_{W_n}(t) \to e^{t^2/2}$$, the mgf of $$N(0, 1)$$, so $$W_n \xrightarrow{d} N(0, 1)$$.

### Exercise 5.16

> **Exercise 5.16.** Under the same assumptions as in Example 5.3.8, for $$r_n \underset{n\to\infty}{\sim} \alpha n$$, $$s_n \underset{n\to\infty}{\sim} \beta n$$ ($$0 < \alpha < \beta < 1$$), derive the limiting joint distribution of the sample quantiles $$X_{(r_n)}$$ and $$X_{(s_n)}$$, and from it derive the limiting distribution of the sample interquartile range $$X_{(s_n)} - X_{(r_n)}$$ ($$r_n \sim n/4$$, $$s_n \sim 3n/4$$).
{: .problem #ex5-16 }

(My own answer; it was not in my notes.) With $$h(y) = F^{-1}(1 - e^{-y})$$, $$X_{(r)} \overset{d}{=} h(Y_r)$$, where $$Y_r = \sum_{i=1}^{r}\frac{1}{n-i+1}Z_i$$ jointly in $$r$$, $$Z_i \overset{iid}{\sim} \mathrm{Exp}(1)$$. Put $$a = -\log(1-\alpha)$$, $$b = -\log(1-\beta)$$ and

$$
Y_{r_n} = \sum_{i=1}^{r_n}\frac{Z_i}{n-i+1}, \qquad Y_{s_n} - Y_{r_n} = \sum_{i=r_n+1}^{s_n}\frac{Z_i}{n-i+1},
$$

which are independent. By Exercise 5.15, $$\sqrt{n}(Y_{r_n} - a) \xrightarrow{d} N\bigl(0, \frac{\alpha}{1-\alpha}\bigr)$$, and in the same way $$\sqrt{n}(Y_{s_n} - Y_{r_n} - (b - a)) \xrightarrow{d} N\bigl(0, \frac{\beta}{1-\beta} - \frac{\alpha}{1-\alpha}\bigr)$$ (the variance sum $$\sum_{r_n<i\le s_n}(n-i+1)^{-2} \sim \frac{1}{n}\bigl(\frac{1}{1-\beta} - \frac{1}{1-\alpha}\bigr)$$, and $$\frac{\beta}{1-\beta} - \frac{\alpha}{1-\alpha} = \frac{1}{1-\beta} - \frac{1}{1-\alpha}$$). By independence and the cgf argument of Exercise 5.15, jointly

$$
\sqrt{n}\begin{pmatrix}Y_{r_n} - a \\ Y_{s_n} - b\end{pmatrix} \xrightarrow{d} N_2\Bigl(0, \begin{pmatrix}\frac{\alpha}{1-\alpha} & \frac{\alpha}{1-\alpha} \\ \frac{\alpha}{1-\alpha} & \frac{\beta}{1-\beta}\end{pmatrix}\Bigr)
$$

(since $$\mathrm{Cov}(Y_{r_n}, Y_{s_n}) = \mathrm{Var}(Y_{r_n})$$). By the delta method with $$\dot{h}(a) = \dfrac{1-\alpha}{f(\xi_\alpha)}$$, $$\dot{h}(b) = \dfrac{1-\beta}{f(\xi_\beta)}$$, where $$\xi_\alpha = F^{-1}(\alpha)$$, $$\xi_\beta = F^{-1}(\beta)$$, and $$f = \dot{F}$$,

$$
\sqrt{n}\begin{pmatrix}X_{(r_n)} - \xi_\alpha \\ X_{(s_n)} - \xi_\beta\end{pmatrix} \xrightarrow{d} N_2\Bigl(0, \begin{pmatrix}\sigma_{11} & \sigma_{12} \\ \sigma_{12} & \sigma_{22}\end{pmatrix}\Bigr),
$$

$$
\sigma_{11} = \frac{\alpha(1-\alpha)}{f(\xi_\alpha)^2}, \quad \sigma_{22} = \frac{\beta(1-\beta)}{f(\xi_\beta)^2}, \quad \sigma_{12} = \frac{\alpha(1-\beta)}{f(\xi_\alpha)f(\xi_\beta)}.
$$

*Interquartile range.* For $$\alpha = \frac{1}{4}$$, $$\beta = \frac{3}{4}$$ with $$f_1 = f(F^{-1}(1/4))$$, $$f_3 = f(F^{-1}(3/4))$$, the difference is a linear function $$(-1, 1)$$ of the pair, so

$$
\sqrt{n}\bigl\{(X_{(s_n)} - X_{(r_n)}) - (F^{-1}(\tfrac{3}{4}) - F^{-1}(\tfrac{1}{4}))\bigr\} \xrightarrow{d} N\bigl(0, \sigma_{11} + \sigma_{22} - 2\sigma_{12}\bigr),
$$

$$
\sigma_{11} + \sigma_{22} - 2\sigma_{12} = \frac{3}{16f_1^2} + \frac{3}{16f_3^2} - \frac{2}{16f_1f_3} = \frac{1}{16}\Bigl(\frac{3}{f_1^2} + \frac{3}{f_3^2} - \frac{2}{f_1f_3}\Bigr).
$$

### Exercise 5.17

> **Exercise 5.17.** In the model of the logistic distribution $$L(\mu, \sigma)$$ with pdf $$f(x; \mu, \sigma) = \dfrac{1}{\sigma}\dfrac{e^{-(x-\mu)/\sigma}}{(1 + e^{-(x-\mu)/\sigma})^2}I_{(-\infty,+\infty)}(x)$$, we want to make inference on $$\mu, \sigma$$ with the statistics defined from the sample quantiles $$X_{([n/4])}, X_{([n/2])}, X_{([3n/4])}$$ of a random sample $$X_1, \dots, X_n$$ ($$n \ge 2$$): $$\hat{\mu}_n = X_{([n/2])}$$, $$\hat{\sigma}_n = (X_{([3n/4])} - X_{([n/4])})/(2\log3)$$. Find the limiting distribution of $$\sqrt{n}\dfrac{\hat{\mu}_n - \mu}{\hat{\sigma}_n}$$ as the sample size $$n \to \infty$$, and explain how to find an approximate $$95\%$$ confidence interval for $$\mu$$ using this result.
{: .problem #ex5-17 }

(My own answer; it was not in my notes.) The cdf is $$F(x) = \dfrac{1}{1 + e^{-(x-\mu)/\sigma}}$$, so $$F^{-1}(u) = \mu + \sigma\log\dfrac{u}{1-u}$$. The median is $$F^{-1}(1/2) = \mu$$ and the quartiles are $$F^{-1}(1/4) = \mu - \sigma\log3$$, $$F^{-1}(3/4) = \mu + \sigma\log3$$. The pdf at the median is $$f(\mu) = \dfrac{1}{\sigma}\cdot\dfrac{1}{4} = \dfrac{1}{4\sigma}$$.

*Consistency of $$\hat{\sigma}_n$$.* By the consistency of sample quantiles (Example 5.2.7), $$X_{([n/4])} \xrightarrow{P} \mu - \sigma\log3$$ and $$X_{([3n/4])} \xrightarrow{P} \mu + \sigma\log3$$, so $$\hat{\sigma}_n \xrightarrow{P} \dfrac{2\sigma\log3}{2\log3} = \sigma$$.

*Limit of $$\hat{\mu}_n$$.* By Example 5.3.8 with $$\alpha = \frac{1}{2}$$,

$$
\sqrt{n}(\hat{\mu}_n - \mu) \xrightarrow{d} N\Bigl(0, \frac{\frac{1}{2}\cdot\frac{1}{2}}{f(\mu)^2}\Bigr) = N\Bigl(0, \frac{1/4}{1/(16\sigma^2)}\Bigr) = N(0, 4\sigma^2).
$$

By Slutsky's theorem,

$$
\sqrt{n}\frac{\hat{\mu}_n - \mu}{\hat{\sigma}_n} \xrightarrow{d} \frac{N(0, 4\sigma^2)}{\sigma} = N(0, 4), \qquad\text{that}\ \text{is}\qquad \sqrt{n}\frac{\hat{\mu}_n - \mu}{2\hat{\sigma}_n} \xrightarrow{d} N(0, 1).
$$

*Confidence interval.* $$P\Bigl(-1.96 \le \sqrt{n}\dfrac{\hat{\mu}_n - \mu}{2\hat{\sigma}_n} \le 1.96\Bigr) \simeq 0.95$$, so an approximate $$95\%$$ confidence interval for $$\mu$$ is

$$
\Bigl[\hat{\mu}_n - 3.92\frac{\hat{\sigma}_n}{\sqrt{n}},\ \hat{\mu}_n + 3.92\frac{\hat{\sigma}_n}{\sqrt{n}}\Bigr].
$$

### Exercise 5.18

> **Exercise 5.18.** In the model of the double exponential distribution $$DE(\mu, \sigma)$$ with pdf $$f(x; \mu, \sigma) = \dfrac{1}{2\sigma}e^{-\lvert x-\mu\rvert/\sigma}I_{(-\infty,+\infty)}(x)$$, let the sample median and the sample mean absolute deviation based on a random sample $$X_1, \dots, X_n$$ ($$n \ge 2$$) be $$\hat{\mu}_n = X_{([n/2])}$$, $$\hat{\sigma}_n = \dfrac{1}{n}\sum_{i=1}^{n}\lvert X_i - X_{([n/2])}\rvert$$. (a) Show that $$\hat{\sigma}_n \xrightarrow{P} \sigma$$. (b) Find the limiting distribution of $$\sqrt{n}\dfrac{\hat{\mu}_n - \mu}{\hat{\sigma}_n}$$ as $$n \to \infty$$, and explain how to find an approximate $$95\%$$ confidence interval for $$\mu$$ using this result.
{: .problem #ex5-18 }

(My own answer; it was not in my notes.) The cdf is $$F(x) = \frac{1}{2}e^{(x-\mu)/\sigma}$$ for $$x < \mu$$ and $$1 - \frac{1}{2}e^{-(x-\mu)/\sigma}$$ for $$x \ge \mu$$, so $$F^{-1}(1/2) = \mu$$ and $$f(\mu) = \dfrac{1}{2\sigma}$$. Also $$E\lvert X_1 - \mu\rvert = \displaystyle\int\lvert x - \mu\rvert\frac{1}{2\sigma}e^{-\lvert x-\mu\rvert/\sigma}\,dx = \int_0^{\infty}\frac{t}{\sigma}e^{-t/\sigma}\,dt = \sigma$$.

**(a)** By the triangle inequality, $$\bigl\lvert\lvert X_i - \hat{\mu}_n\rvert - \lvert X_i - \mu\rvert\bigr\rvert \le \lvert\hat{\mu}_n - \mu\rvert$$ for every $$i$$, so

$$
\Bigl\lvert\hat{\sigma}_n - \frac{1}{n}\sum_{i=1}^{n}\lvert X_i - \mu\rvert\Bigr\rvert \le \lvert\hat{\mu}_n - \mu\rvert \xrightarrow{P} 0,
$$

where $$\hat{\mu}_n \xrightarrow{P} F^{-1}(1/2) = \mu$$ by Example 5.2.7. By the law of large numbers, $$\frac{1}{n}\sum\lvert X_i - \mu\rvert \xrightarrow{P} E\lvert X_1 - \mu\rvert = \sigma$$. Therefore $$\hat{\sigma}_n \xrightarrow{P} \sigma$$.

**(b)** By Example 5.3.8 with $$\alpha = \frac{1}{2}$$,

$$
\sqrt{n}(\hat{\mu}_n - \mu) \xrightarrow{d} N\Bigl(0, \frac{1/4}{f(\mu)^2}\Bigr) = N(0, \sigma^2),
$$

and by (a) and Slutsky's theorem,

$$
\sqrt{n}\frac{\hat{\mu}_n - \mu}{\hat{\sigma}_n} = \sqrt{n}\frac{\hat{\mu}_n - \mu}{\sigma}\Big/\frac{\hat{\sigma}_n}{\sigma} \xrightarrow{d} N(0, 1).
$$

Therefore $$P\Bigl(-1.96 \le \sqrt{n}\dfrac{\hat{\mu}_n - \mu}{\hat{\sigma}_n} \le 1.96\Bigr) \simeq 0.95$$, and an approximate $$95\%$$ confidence interval for $$\mu$$ is

$$
\Bigl[\hat{\mu}_n - 1.96\frac{\hat{\sigma}_n}{\sqrt{n}},\ \hat{\mu}_n + 1.96\frac{\hat{\sigma}_n}{\sqrt{n}}\Bigr].
$$

## References

- 김우철, *수리통계학* (Mathematical Statistics), revised 2nd edition, 민영사, 2021 — Chapter 5 exercises 5.1 to 5.18. The exercise statements are translated from the book.
- Mathematical Statistics 1 (326.311), Seoul National University, Spring 2025. Instructor: Jaeyong Lee (이재용).
- The answers to 5.1 to 5.12 are mine, translated into English; 5.2(b) and 5.13 to 5.18 are written out from scratch because they were not in my notes.

[Overview](/posts/mathstat1-overview/) · [Chapter 4 Exercises](/posts/mathstat1-exercises-chapter-4/) · [Chapter 5 Part 5](/posts/mathstat1-simulation/)
