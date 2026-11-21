---
title: "Mathematical Statistics 1: Ch. 2 Part 4 — Independence of Random Variables"
date: 2026-11-21 10:00:00 +0900
categories: [Study Notes, Mathematical Statistics 1]
tags: [independence, covariance, correlation, sum of random variables]
description: Independence of two random variables and its equivalent conditions, functions and products of independent random variables, independence versus zero correlation, and the variance of a sum. Chapter 2, §2.4 of Mathematical Statistics 1.
math: true
mermaid: false
render_with_liquid: false
---

> My handwritten notes do not cover this section, so everything below is **translated from the textbook**, §2.4. It is not my own writing. It uses [Part 1](/posts/mathstat1-joint-distribution/), [Part 2](/posts/mathstat1-joint-characteristics/) and [Part 3](/posts/mathstat1-conditional-distribution/).
{: .prompt-info }

## 2.4 Independence of random variables

As an event can be one whose occurrence or non-occurrence has no influence on the likelihood of another event, consider the case in which the random variable $$X$$ taking values in some range has no influence on the likelihood of events about the random variable $$Y$$. That is, for all values of $$a, b, c, d$$,

$$
P(c \le Y \le d \mid a \le X \le b) = P(c \le Y \le d),
$$

that is, no event about $$X$$ is dependent on an event about $$Y$$.

> **Definition (Independence of two random variables).** If, for two random variables $$X, Y$$,
>
> $$
> P(a \le X \le b,\ c \le Y \le d) = P(a \le X \le b)\,P(c \le Y \le d), \quad \forall a, b, c, d\ (a < b,\ c < d) \tag{2.4.1}
> $$
>
> holds, the random variables $$X$$ and $$Y$$ are called *mutually independent*.
{: .definition #def-independence-random-variables }

> **Theorem 2.4.1 (Independence of random variables).** The following conditions are all necessary and sufficient conditions for the random variables $$X$$ and $$Y$$ to be mutually independent. (Here $$cdf$$, $$pdf$$, $$mgf$$ denote the cumulative distribution function, the probability density function and the moment generating function.)
>
> - (a) (cdf) $$cdf_{1,2}(x, y) = cdf_1(x)\,cdf_2(y)$$ for all $$x, y$$.
> - (b) (pdf) $$pdf_{1,2}(x, y) = pdf_1(x)\,pdf_2(y)$$ for all $$x, y$$.
> - (c) (mgf) $$mgf_{1,2}(t_1, t_2) = mgf_1(t_1)\,mgf_2(t_2)$$ for all $$t_i$$ with $$-h_i < t_i < h_i$$ ($$\exists h_i > 0$$) ($$i = 1, 2$$). (Condition (c) is equivalent to the others when the mgf exists.)
> - (d) (probability measure) $$P(X \in A,\ Y \in B) = P(X \in A)\,P(Y \in B)$$ for all $$A, B$$. (Here $$X \in A$$ means $$\{s : X(s) \in A\}$$, the inverse image.)
{: .theorem #thm-independence-random-variables }

*Proof.* That (a) and (b) are equivalent is clear from the relation between a cumulative distribution function and a probability density function. When the mgf exists, the mgf and the pdf correspond one-to-one, so it is also clear that (b) and (c) are equivalent. Also, since a probability measure and a pdf correspond one-to-one, (b) and (d) are equivalent.

On the other hand, integrating or summing the pdf over an interval gives the probability over the interval, so if (b) holds then (2.4.1) holds. Conversely, if (2.4.1) holds for $$a = c = -n$$, $$b = x$$, $$d = y$$ ($$n = 1, 2, \dots$$), then taking the limit in $$n$$ gives (a) by the continuity of probability measure. $$\square$$

**Example 2.4.1.** If the joint pdf of $$X$$ and $$Y$$ is $$f_{1,2}(x, y) = 2e^{-x-2y}I_{(x \ge 0,\ y \ge 0)}$$, the marginal pdfs are

$$
f_1(x) = \int_{-\infty}^{+\infty}2e^{-x-2y}I_{(x \ge 0,\ y \ge 0)}\,dy = e^{-x}I_{(x \ge 0)}, \qquad
f_2(y) = \int_{-\infty}^{+\infty}2e^{-x-2y}I_{(x \ge 0,\ y \ge 0)}\,dx = 2e^{-2y}I_{(y \ge 0)}.
$$

From these, $$f_{1,2}(x, y) = 2e^{-x-2y}I_{(x \ge 0)}I_{(y \ge 0)} = f_1(x)f_2(y)$$ for all $$x, y$$, so $$X$$ and $$Y$$ are mutually independent.

**Example 2.4.2.** In Examples 2.1.2 and 2.1.4 the joint pdf of $$X$$ and $$Y$$ is $$f_{1,2}(x, y) = 2e^{-x-y}I_{(0 \le x \le y)}$$ and the marginal pdfs are $$f_1(x) = 2e^{-2x}I_{(x \ge 0)}$$, $$f_2(y) = 2e^{-y}(1 - e^{-y})I_{(y \ge 0)}$$. Since $$f_{1,2}(x, y) = f_1(x)f_2(y)$$ clearly fails, $$X$$ and $$Y$$ are not mutually independent.

Random variables that are not independent, as in Example 2.4.2, are called *mutually dependent*; to establish a dependent relation one must find one example for which the identities of Theorem 2.4.1 do not hold.

On the other hand, in establishing independence through pdfs as in Example 2.4.1, one need not find the marginal pdfs. That is, instead of (b) of Theorem 2.4.1 one may apply the following (b′).

- (b′) There exist a function $$g_1(x)$$ of $$x$$ alone and a function $$g_2(y)$$ of $$y$$ alone such that $$pdf_{1,2}(x, y) = g_1(x)g_2(y)$$ for all $$x, y$$.

In the continuous case, when (b′) holds, integrating both sides over all $$x$$ and $$y$$ gives

$$
\int_{-\infty}^{+\infty}g_1(x)\,dx\int_{-\infty}^{+\infty}g_2(y)\,dy = \int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}pdf_{1,2}(x, y)\,dy\,dx = 1,
$$

so (b) follows from the equality

$$
g_1(x)g_2(y) = \Bigl\{g_1(x)\Big/\int_{-\infty}^{+\infty}g_1(x)\,dx\Bigr\}\Bigl\{g_2(y)\Big/\int_{-\infty}^{+\infty}g_2(y)\,dy\Bigr\} = pdf_1(x)\,pdf_2(y).
$$

For example, in Example 2.4.1, without finding the marginal pdfs, $$f_{1,2}(x, y) = 2e^{-x-2y}I_{(x \ge 0,\ y \ge 0)} = e^{-x}I_{(x \ge 0)}\,e^{-2y}I_{(y \ge 0)}\cdot 2 = g_1(x)g_2(y)$$ shows that $$X$$ and $$Y$$ are mutually independent. When using the cdf or the mgf as well, independence can be judged without finding the marginal cdfs or mgfs on the right side of (a) or (c) of Theorem 2.4.1.

> **Theorem 2.4.2 (Functions of independent random variables).** If the random variables $$X, Y$$ are mutually independent, then their respective functions $$g_1(X)$$ and $$g_2(Y)$$ are also mutually independent.
{: .theorem #thm-functions-independent }

*Proof.* Write the inverse image of a function $$g$$ as $$g^{-1}(A) = \{x : g(x) \in A\}$$. Then

$$
(g_1(X) \in A,\ g_2(Y) \in B) = (X \in g_1^{-1}(A),\ Y \in g_2^{-1}(B)), \quad (g_1(X) \in A) = (X \in g_1^{-1}(A)), \quad (g_2(Y) \in B) = (Y \in g_2^{-1}(B)).
$$

Since $$X, Y$$ are independent, by (d) of Theorem 2.4.1, $$P(X \in g_1^{-1}(A),\ Y \in g_2^{-1}(B)) = P(X \in g_1^{-1}(A))\,P(Y \in g_2^{-1}(B))$$. Therefore $$P(g_1(X) \in A,\ g_2(Y) \in B) = P(g_1(X) \in A)\,P(g_2(Y) \in B)$$, so $$g_1(X)$$ and $$g_2(Y)$$ are also mutually independent. $$\square$$

> **Theorem 2.4.3 (Expectation of the product of independent random variables).** If the random variables $$X$$ and $$Y$$ are mutually independent, then $$E[g_1(X)g_2(Y)] = E[g_1(X)]\,E[g_2(Y)]$$. (This theorem assumes that the expectations of $$g_1(X), g_2(Y)$$ are real numbers.)
{: .theorem #thm-product-expectation }

*Proof.* The continuous case is as follows; the discrete case can be proved with sums in place of integrals.

$$
\begin{aligned}
E[g_1(X)g_2(Y)] &= \int_{-\infty}^{+\infty}\Bigl\{\int_{-\infty}^{+\infty}g_1(x)g_2(y)\,pdf_{1,2}(x, y)\,dy\Bigr\}dx \\
&= \int_{-\infty}^{+\infty}g_1(x)\,pdf_1(x)\Bigl\{\int_{-\infty}^{+\infty}g_2(y)\,pdf_2(y)\,dy\Bigr\}dx \\
&= \int_{-\infty}^{+\infty}g_1(x)\,pdf_1(x)\,dx\int_{-\infty}^{+\infty}g_2(y)\,pdf_2(y)\,dy = E[g_1(X)]\,E[g_2(Y)]. \qquad \square
\end{aligned}
$$

> **Theorem 2.4.4 (Independence and correlation).** If the random variables $$X$$ and $$Y$$ are mutually independent, then $$\mathrm{Cov}(X, Y) = 0$$. (This theorem assumes that the covariance of the two variables is a real number.)
{: .theorem #thm-independence-correlation }

*Proof.* It follows from the calculation formula $$\mathrm{Cov}(X, Y) = E(XY) - [E(X)][E(Y)]$$ and Theorem 2.4.3. $$\square$$

**Example 2.4.3 (the correlation coefficient is $$0$$ but the variables are not independent).** If the joint pdf of $$X$$ and $$Y$$ is

$$
f_{1,2}(x, y) = \frac{9}{40}\bigl(1 + x^2y^2\bigr)I_{(-1 \le x \le 1,\ -1 \le y \le 1)},
$$

the marginal pdfs are $$f_1(x) = \frac{3}{20}(3 + x^2)I_{(-1 \le x \le 1)}$$ and $$f_2(y) = \frac{3}{20}(3 + y^2)I_{(-1 \le y \le 1)}$$. In this case $$X$$ and $$Y$$ are clearly not independent, but $$E(X) = 0$$, $$E(Y) = 0$$, $$E(XY) = 0$$, so $$\mathrm{Cov}(X, Y) = 0$$. That is, the converse of Theorem 2.4.4 does not always hold.

> **Theorem 2.4.5 (Variance of a sum of random variables).** (This theorem assumes that the variance of each variable is a real number.)
>
> - (a) $$\mathrm{Var}(X + Y) = \mathrm{Var}(X) + \mathrm{Var}(Y) + 2\,\mathrm{Cov}(X, Y)$$.
> - (b) If $$X$$ and $$Y$$ are mutually independent, then $$\mathrm{Var}(X + Y) = \mathrm{Var}(X) + \mathrm{Var}(Y)$$.
{: .theorem #thm-variance-sum }

*Proof.* Let the means of $$X, Y$$ be $$\mu_1, \mu_2$$. From the definition of variance and the linearity of expectation,

$$
\mathrm{Var}(X + Y) = E[(X + Y - \mu_1 - \mu_2)^2] = E[(X - \mu_1)^2 + (Y - \mu_2)^2 + 2(X - \mu_1)(Y - \mu_2)] = \mathrm{Var}(X) + \mathrm{Var}(Y) + 2\,\mathrm{Cov}(X, Y).
$$

If $$X$$ and $$Y$$ are mutually independent, (b) follows from Theorem 2.4.4 and (a). $$\square$$

## References

- 김우철, *수리통계학* (Mathematical Statistics), revised 2nd edition, 민영사, 2021 — Chapter 2, §2.4 (Theorems 2.4.1 to 2.4.5, Examples 2.4.1 to 2.4.3). Translated from the book; not from my notes.
- Mathematical Statistics 1 (326.311), Seoul National University, Spring 2025. Instructor: Jaeyong Lee (이재용).

[Previous](/posts/mathstat1-conditional-distribution/) · [Overview](/posts/mathstat1-overview/) · [Next](/posts/mathstat1-multivariate/)
