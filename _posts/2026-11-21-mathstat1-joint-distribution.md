---
title: "Mathematical Statistics 1: Ch. 2 Part 1 — Distribution of Two Random Variables"
date: 2026-11-21 09:30:00 +0900
categories: [Study Notes, Mathematical Statistics 1]
tags: [joint distribution, marginal distribution, joint cdf, bivariate]
description: Joint probability density function, marginal densities, and the joint cumulative distribution function of two random variables. Chapter 2, §2.1 of Mathematical Statistics 1.
math: true
mermaid: false
render_with_liquid: false
---

> My handwritten notes do not cover this section (the page of my notes for Chapter 2 starts at conditional distributions), so everything below is **translated from the textbook**, §2.1. It is not my own writing. The parts of the notes that use it are in [Part 3](/posts/mathstat1-conditional-distribution/).
{: .prompt-info }

## 2.1 Distribution of two random variables

In a random experiment there are generally several random variables of interest. We look at how to describe their distribution.

**Example 2.1.1.** A box contains two white balls, three black balls and four red balls. Three balls are drawn together; let $$X$$ and $$Y$$ be the numbers of white and black balls drawn. Then

$$
P(X = x, Y = y) = \frac{\binom{2}{x}\binom{3}{y}\binom{4}{3 - x - y}}{\binom{9}{3}}, \qquad x = 0, 1, 2,\ y = 0, 1, 2, 3,\ x + y \le 3.
$$

The values and probabilities can be arranged in a table (Table 2.1.1). Writing the probabilities as numerators over $$84$$:

- $$X = 0$$: $$Y = 0, 1, 2, 3$$ have $$4, 18, 12, 1$$; row total $$35$$.
- $$X = 1$$: $$Y = 0, 1, 2, 3$$ have $$12, 24, 6, 0$$; row total $$42$$.
- $$X = 2$$: $$Y = 0, 1, 2, 3$$ have $$4, 3, 0, 0$$; row total $$7$$.
- Column totals: $$Y = 0, 1, 2, 3$$ have $$20, 45, 18, 1$$; overall total $$84$$.

The margin of the table on the side shows the probabilities of $$X$$, and the margin along the bottom shows those of $$Y$$.

If the set of ordered pairs $$(X, Y)$$ can take is $$\{(x_j, y_k) : j = 1, 2, \dots,\ k = 1, 2, \dots\}$$, the function

$$
f(x_j, y_k) = P(X = x_j, Y = y_k)
$$

is called the *probability density function* of the discrete two-dimensional (bivariate) random variable $$(X, Y)$$. (A two-dimensional random variable is also called a bivariate random vector.) This function has properties like those for one random variable.

> **Probability density function of a discrete bivariate random vector.**
>
> - (a) $$f(x, y) \ge 0$$ for all $$x, y$$, and $$f(x, y) = 0$$ for $$(x, y) \ne (x_j, y_k)$$.
> - (b) $$\sum_x \sum_y f(x, y) = \sum_{j=1}^{\infty}\sum_{k=1}^{\infty} f(x_j, y_k) = 1$$.
> - (c) $$\sum_{x : a \le x \le b}\ \sum_{y : c \le y \le d} f(x, y) = P(a \le X \le b,\ c \le Y \le d)$$.
{: .definition #def-joint-pdf-discrete }

When both $$X$$ and $$Y$$ take values in intervals of real numbers and their probabilities are given by integrals, the ordered pair $$(X, Y)$$ is called a continuous two-dimensional random variable or bivariate random vector, and the function $$f$$ determining the probabilities of $$(X, Y)$$, that is

$$
\iint_{x : a \le x \le b,\ y : c \le y \le d} f(x, y)\,dx\,dy = P(a \le X \le b,\ c \le Y \le d) \quad (a < b,\ c < d),
$$

is called the probability density function of $$(X, Y)$$.

> **Probability density function of a continuous bivariate random vector.**
>
> - (a) $$f(x, y) \ge 0$$ for all $$x, y$$.
> - (b) $$\displaystyle\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty} f(x, y)\,dy\,dx = 1$$.
> - (c) $$\displaystyle\int_a^b\int_c^d f(x, y)\,dy\,dx = P(a \le X \le b,\ c \le Y \le d)$$ ($$a < b$$, $$c < d$$).
{: .definition #def-joint-pdf-continuous }

(A double integral means the iterated integral taken in the order in which the differentials appear: $$\int_a^b\int_c^d f(x,y)\,dy\,dx = \int_a^b\bigl\{\int_c^d f(x,y)\,dy\bigr\}dx$$.)

**Example 2.1.2.** Find the constant $$c$$ for which $$f(x, y) = c\,e^{-x-y}I_{(0 \le x \le y)}$$ is a probability density function, and, if it is the pdf of $$(X, Y)$$, find $$P(X \ge 2, Y \ge 3)$$.

*Solution.* The total probability must be $$1$$:

$$
\int_{-\infty}^{\infty}\int_{-\infty}^{\infty} f(x, y)\,dy\,dx = \int_0^{\infty}\int_x^{\infty} c\,e^{-x-y}\,dy\,dx = c\int_0^{\infty} e^{-2x}\,dx = \frac{c}{2} = 1.
$$

So $$c = 2$$. Writing "$$y \ge 3$$ and $$y \ge x$$" as $$y \ge 3 \vee x$$ (here $$a \vee b$$ is the larger of $$a$$ and $$b$$, and $$a \wedge b$$ the smaller),

$$
\int_3^{\infty} 2e^{-x-y}I_{(0 \le x \le y)}\,dy = 2e^{-x}\bigl[-e^{-y}\bigr]_{3 \vee x}^{\infty} = 2e^{-x - 3 \vee x},
$$

$$
P(X \ge 2, Y \ge 3) = \int_2^{\infty} 2e^{-x - 3 \vee x}\,dx = \int_2^3 2e^{-x-3}\,dx + \int_3^{\infty} 2e^{-2x}\,dx = 2e^{-3}\bigl[-e^{-x}\bigr]_2^3 + \bigl[-e^{-2x}\bigr]_3^{\infty} = 2e^{-5} - e^{-6} \approx 0.011.
$$

## Marginal distributions

Given two random variables $$X, Y$$, one can consider the distribution of the ordered pair $$(X, Y)$$ as well as the distributions of $$X$$ and of $$Y$$. The distribution of $$(X, Y)$$ is called the *joint* probability distribution, and the distributions of $$X$$ and of $$Y$$ the *marginal* probability distributions.

As in Example 2.1.1, here is how to find the marginal distributions from the joint distribution:

$$
P(a \le X \le b) = P(a \le X \le b,\ -\infty < Y < +\infty) =
\begin{cases}
\displaystyle\sum_{x : a \le x \le b}\sum_y f(x, y) & ((X, Y) \text{ discrete}) \\[0.8em]
\displaystyle\int_a^b\int_{-\infty}^{+\infty} f(x, y)\,dy\,dx & ((X, Y) \text{ continuous}).
\end{cases}
$$

So the function $$f_1$$ defined by

$$
f_1(x) =
\begin{cases}
\sum_y f(x, y) & ((X, Y) \text{ discrete}) \\
\int_{-\infty}^{+\infty} f(x, y)\,dy & ((X, Y) \text{ continuous})
\end{cases}
$$

gives the probability of $$X$$ as $$P(a \le X \le b) = \sum_{x : a \le x \le b} f_1(x)$$ or $$\int_a^b f_1(x)\,dx$$. That is, $$f_1$$ is the pdf of $$X$$; to distinguish it from the pdf of $$(X, Y)$$, it is called the *marginal pdf* of $$X$$, while the pdf of $$(X, Y)$$ is the *joint pdf*.

> **Joint and marginal probability density functions.** If the joint pdf of the bivariate random vector $$(X, Y)$$ is $$f(x, y)$$, the marginal pdfs $$f_1(x)$$ and $$f_2(y)$$ of $$X$$ and $$Y$$ are
>
> $$
> f_1(x) = \sum_y f(x, y), \quad f_2(y) = \sum_x f(x, y) \quad ((X, Y) \text{ discrete}),
> $$
>
> $$
> f_1(x) = \int_{-\infty}^{+\infty} f(x, y)\,dy, \quad f_2(y) = \int_{-\infty}^{+\infty} f(x, y)\,dx \quad ((X, Y) \text{ continuous}).
> $$
{: .definition #def-marginal-pdf }

**Example 2.1.3.** In Example 2.1.1 the joint pdf of $$(X, Y)$$ is $$f(x, y) = \binom{2}{x}\binom{3}{y}\binom{4}{3-x-y}\big/\binom{9}{3}$$, $$x = 0,1,2$$, $$y = 0,1,2,3$$, $$x + y \le 3$$, and the marginal pdfs are as follows, agreeing with the margins of Table 2.1.1:

$$
f_1(x) = \sum_y f(x, y) = \binom{2}{x}\sum_{y=0}^{3-x}\binom{3}{y}\binom{4}{3-x-y}\Big/\binom{9}{3} = \binom{2}{x}\binom{7}{3-x}\Big/\binom{9}{3}, \quad x = 0, 1, 2,
$$

$$
f_2(y) = \sum_x f(x, y) = \binom{3}{y}\sum_{x=0}^{2 \wedge (3-y)}\binom{2}{x}\binom{4}{3-y-x}\Big/\binom{9}{3} = \binom{3}{y}\binom{6}{3-y}\Big/\binom{9}{3}, \quad y = 0, 1, 2, 3.
$$

(For $$m \ge l$$, $$n \ge l$$, $$\sum_{y=0}^{l}\binom{m}{y}\binom{n}{l-y} = \binom{m+n}{l}$$, the coefficient of $$t^l$$ in $$(1+t)^m(1+t)^n = (1+t)^{m+n}$$.)

**Example 2.1.4.** In Example 2.1.2 the joint pdf of $$(X, Y)$$ is $$f(x, y) = 2e^{-x-y}I_{(0 \le x \le y)}$$, and the marginal pdfs are

$$
f_1(x) = \int_x^{\infty} 2e^{-x-y}\,dy\, I_{(0 \le x)} = 2e^{-2x}I_{(0 \le x)}, \qquad
f_2(y) = \int_0^{y} 2e^{-x-y}\,dx\, I_{(0 \le y)} = 2e^{-y}(1 - e^{-y})I_{(0 \le y)}.
$$

## Joint cumulative distribution function

As for one random variable, there are several ways to express the joint distribution of two random variables. The function

$$
F(x, y) = P(X \le x,\ Y \le y), \qquad -\infty < x < +\infty,\ -\infty < y < +\infty,
$$

which gives the joint cumulative probability of $$X$$ and $$Y$$, is called the *joint cumulative distribution function* of $$(X, Y)$$, and it determines the joint distribution in correspondence with the joint pdf as follows.

> **Joint cdf and joint pdf.**
>
> - (a) *(Discrete.)* If the values $$X, Y$$ can take are $$x_1 < x_2 < \cdots < x_m < \cdots$$ and $$y_1 < y_2 < \cdots < y_n < \cdots$$, then
>
>   $$
>   F(x_m, y_n) = P(X \le x_m,\ Y \le y_n) = \sum_{j=1}^{m}\sum_{k=1}^{n} f(x_j, y_k),
>   $$
>
>   $$
>   f(x_j, y_k) = P(X = x_j,\ Y = y_k) = \{F(x_j, y_k) - F(x_{j-1}, y_k)\} - \{F(x_j, y_{k-1}) - F(x_{j-1}, y_{k-1})\}.
>   $$
>
> - (b) *(Continuous.)* $$F(x, y) = P(X \le x, Y \le y) = \displaystyle\int_{-\infty}^{x}\int_{-\infty}^{y} f(t, u)\,du\,dt$$, and at a point $$(x, y)$$ where $$f$$ is continuous,
>
>   $$
>   f(x, y) = \frac{\partial^2}{\partial x\,\partial y}F(x, y).
>   $$
{: .definition #def-joint-cdf }

**Example 2.1.5.** In Example 2.1.2 the joint cdf of $$(X, Y)$$ is $$F(x, y) = \int_{-\infty}^{x}\int_{-\infty}^{y} 2e^{-t-u}I_{(0 \le t \le u)}\,du\,dt$$. Since

$$
\int_{-\infty}^{y} 2e^{-t-u}I_{(0 \le t \le u)}\,du = 2e^{-t}\int_t^{y} e^{-u}\,du\, I_{(y \ge t \ge 0)} = 2e^{-t}(e^{-t} - e^{-y})I_{(y \ge t \ge 0)},
$$

$$
F(x, y) = \int_{-\infty}^{x} 2e^{-t}(e^{-t} - e^{-y})I_{(0 \le t \le y)}\,dt = \int_0^{x \wedge y} 2(e^{-2t} - e^{-t-y})\,dt\, I_{(x \wedge y \ge 0)} = \bigl\{1 - e^{-2x \wedge y} + 2e^{-y}(e^{-x \wedge y} - 1)\bigr\}I_{(x \ge 0,\ y \ge 0)}.
$$

As for pdfs, to distinguish the cdf of $$(X, Y)$$ from the cdf of each variable, the cdf of each variable is called its *marginal cdf*:

$$
F_1(x) = P(X \le x), \qquad F_2(y) = P(Y \le y).
$$

By the continuity of probability measure, $$P(X \le x) = P(X \le x, Y < +\infty) = \lim_{y \to +\infty}P(X \le x, Y \le y)$$, so the marginal cdfs are obtained from the joint cdf as

$$
F_1(x) = \lim_{y \to +\infty}F(x, y), \qquad F_2(y) = \lim_{x \to +\infty}F(x, y).
$$

**Example 2.1.6.** From the joint cdf $$F(x, y) = \{1 - e^{-2x \wedge y} + 2e^{-y}(e^{-x \wedge y} - 1)\}I_{(x \ge 0,\, y \ge 0)}$$ of Example 2.1.5, the marginal cdfs are

$$
F_1(x) = \lim_{y \to +\infty}F(x, y) = (1 - e^{-2x})I_{(x \ge 0)}, \qquad
F_2(y) = \lim_{x \to +\infty}F(x, y) = (1 + e^{-2y} - 2e^{-y})I_{(y \ge 0)}.
$$

Differentiating them gives, at the points of continuity, the marginal pdfs of Example 2.1.4, $$f_1(x) = 2e^{-2x}I_{(x \ge 0)}$$ and $$f_2(y) = 2e^{-y}(1 - e^{-y})I_{(y \ge 0)}$$.

> **Theorem 2.1.1 (Properties of the joint cdf).**
>
> - (a) *(Monotonicity.)* (i) $$F(x, y) \le F(x + h, y)$$ and $$F(x, y) \le F(x, y + k)$$ for all $$h > 0$$, $$k > 0$$. (ii) $$F(x_2, y_2) - F(x_1, y_2) - F(x_2, y_1) + F(x_1, y_1) \ge 0$$ for all $$x_1 < x_2$$, $$y_1 < y_2$$.
> - (b) *(Total variation.)* $$\lim_{x \to -\infty}F(x, b) = 0$$, $$\lim_{y \to -\infty}F(a, y) = 0$$ and $$\lim_{x \to +\infty,\ y \to +\infty}F(x, y) = 1$$ for all $$a, b$$.
> - (c) *(Right-continuity.)* $$\lim_{h \downarrow 0}F(x + h, y) = F(x, y)$$ and $$\lim_{k \downarrow 0}F(x, y + k) = F(x, y)$$ for all $$x, y$$.
{: .theorem #thm-joint-cdf-properties }

*Proof.* (a)(i), (b) and (c) are proved in the same way as for one random variable. (a)(ii) is clear from

$$
P(x_1 < X \le x_2,\ y_1 < Y \le y_2) = F(x_2, y_2) - F(x_1, y_2) - F(x_2, y_1) + F(x_1, y_1). \qquad \square
$$

As for one random variable, the joint cdf has the following left limit, and may fail to be left-continuous:

$$
F(x-, y) = \lim_{h \downarrow 0}F(x - h, y) = P(X < x,\ Y \le y).
$$

So the size of the jump of the joint cdf in the left direction is

$$
P(X = x,\ Y \le y) = P(X \le x, Y \le y) - P(X < x, Y \le y) = F(x, y) - F(x-, y).
$$

## References

- 김우철, *수리통계학* (Mathematical Statistics), revised 2nd edition, 민영사, 2021 — Chapter 2, §2.1 (Examples 2.1.1 to 2.1.6, Theorem 2.1.1). Translated from the book; not from my notes.
- Mathematical Statistics 1 (326.311), Seoul National University, Spring 2025. Instructor: Jaeyong Lee (이재용).

[Previous: Chapter 1 Part 5](/posts/mathstat1-inequalities/) · [Overview](/posts/mathstat1-overview/) · [Next](/posts/mathstat1-joint-characteristics/)
