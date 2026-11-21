---
title: "Mathematical Statistics 1: Ch. 2 Part 2 — Characteristics of a Joint Distribution"
date: 2026-11-21 09:40:00 +0900
categories: [Study Notes, Mathematical Statistics 1]
tags: [covariance, correlation, joint moments, joint mgf, joint cumulants]
description: Expectation of a function of two random variables, covariance and correlation, joint moments, the joint moment generating function and joint cumulants. Chapter 2, §2.2 of Mathematical Statistics 1.
math: true
mermaid: false
render_with_liquid: false
---

> My handwritten notes do not cover this section, so everything below is **translated from the textbook**, §2.2. It is not my own writing. The notes pick up again at conditional distributions in [Part 3](/posts/mathstat1-conditional-distribution/).
{: .prompt-info }

## 2.2 Characteristics of a joint distribution

The mean, variance or standard deviation of two random variables $$X, Y$$ give information about the corresponding marginal distributions, but they do not describe characteristics of the joint distribution such as the relation between the two variables. Such characteristics are expressed through expectations.

> **Expectation for a joint distribution.** If the pdf of the bivariate random vector $$(X, Y)$$ is $$f(x, y)$$ and $$g(x, y)$$ is a real-valued function, and
>
> $$
> \begin{cases}
> \sum_x\sum_y g(x, y)f(x, y) & ((X, Y) \text{ discrete}) \\[0.5em]
> \displaystyle\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty} g(x, y)f(x, y)\,dy\,dx & ((X, Y) \text{ continuous})
> \end{cases}
> $$
>
> is defined as a real number, its value is called the expectation of $$g(X, Y)$$ and is written $$E[g(X, Y)]$$.
{: .definition #def-joint-expectation }

**Example 2.2.1.** If the pdf of $$(X, Y)$$ is $$f(x, y) = 120xy(1 - x - y)I_{(x \ge 0,\ y \ge 0,\ x + y \le 1)}$$, find $$E(XY)$$.

*Solution.*

$$
E(XY) = \iint_{\substack{0 \le x,\ 0 \le y \\ x + y \le 1}} xy\cdot 120xy(1 - x - y)\,dy\,dx
= \int_0^1\Bigl\{120x^2\int_0^{1-x}y^2(1 - x - y)\,dy\Bigr\}dx = 10\int_0^1 x^2(1 - x)^4\,dx = 10\int_0^1(1 - t)^2t^4\,dt = \frac{2}{21}.
$$

As for one random variable, the following properties hold, which is clear from the properties of the corresponding double sums and double integrals.

> **Theorem 2.2.1 (Properties of expectation for a joint distribution).**
>
> - (a) *(Linearity.)* $$E[c_1g_1(X, Y) + c_2g_2(X, Y)] = c_1E[g_1(X, Y)] + c_2E[g_2(X, Y)]$$ ($$c_1, c_2$$ constants).
> - (b) *(Monotonicity.)* If $$g_1(X, Y) \le g_2(X, Y)$$, then $$E[g_1(X, Y)] \le E[g_2(X, Y)]$$.
{: .theorem #thm-joint-expectation-properties }

(These hold on the premise that each expectation is defined as a real number.)

By the definition, the expectation of a function depending on only one random variable is an expectation with respect to the marginal distribution. For example, in the continuous case the expectation of a function $$g(X)$$ of $$X$$ alone is

$$
E[g(X)] = \int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty} g(x)f(x, y)\,dy\,dx = \int_{-\infty}^{+\infty}g(x)\Bigl\{\int_{-\infty}^{+\infty}f(x, y)\,dy\Bigr\}dx = \int_{-\infty}^{+\infty}g(x)f_1(x)\,dx.
$$

**Example 2.2.2.** In Example 2.2.1, the expectation of $$X$$ is

$$
E(X) = \iint x\cdot 120xy(1 - x - y)\,dy\,dx = \int_0^1 x\Bigl\{120x\int_0^{1-x}y(1 - x - y)\,dy\Bigr\}dx = \int_0^1 x\cdot 20x(1 - x)^3\,dx = \int_0^1 20(1 - t)^2t^3\,dt = \frac{1}{3}.
$$

As this calculation shows, the marginal pdf of $$X$$ is $$f_1(x) = 120x\int_0^{1-x}y(1 - x - y)\,dy\,I_{(0 \le x \le 1)} = 20x(1 - x)^3I_{(0 \le x \le 1)}$$, and $$E(X)$$ is the expectation with respect to this marginal distribution.

## Covariance and correlation coefficient

The most used characteristics describing the relation between two random variables are the covariance and the correlation coefficient.

> **Covariance and correlation coefficient.**
>
> - (a) *(Covariance.)* Let the mean and standard deviation of $$X$$ be $$\mu_1$$ and $$\sigma_1$$, and those of $$Y$$ be $$\mu_2$$ and $$\sigma_2$$. The expectation of $$(X - \mu_1)(Y - \mu_2)$$ is called the covariance of $$X$$ and $$Y$$, written $$\mathrm{Cov}(X, Y)$$, $$\sigma_{X,Y}$$ or $$\sigma_{1,2}$$:
>
>   $$
>   \mathrm{Cov}(X, Y) = E[(X - \mu_1)(Y - \mu_2)].
>   $$
>
> - (b) *(Correlation coefficient.)* When the standard deviations $$\sigma_1, \sigma_2$$ of the two variables are not $$0$$, the covariance of $$X$$ and $$Y$$ divided by the product of the two standard deviations is the correlation coefficient of $$X$$ and $$Y$$, written $$\mathrm{Corr}(X, Y)$$:
>
>   $$
>   \mathrm{Corr}(X, Y) = \frac{\mathrm{Cov}(X, Y)}{\sqrt{\mathrm{Var}(X)}\sqrt{\mathrm{Var}(Y)}}.
>   $$
{: .definition #def-covariance-correlation }

The covariance gives information about the direction and amount of the change of the two variables from their respective means. If, when one variable is larger than its mean, the other variable is also likely to be larger than its mean, the value of $$(X - \mu_1)(Y - \mu_2)$$ is likely to be a large positive value, so the covariance will be a large positive number; if they are likely to change in opposite directions, the covariance will be negative.

The covariance, which describes the direction and size of the change relation, has the drawback that its size depends on the units of measurement of each variable, so it is hard to tell whether it comes from the units or from the amount of change. For this reason, the correlation coefficient is considered as a characteristic independent of the units of measurement, by dividing by the standard deviation of each variable.

> **Theorem 2.2.2 (Properties of covariance and calculation formula).**
>
> - (a) $$\mathrm{Cov}(X, Y) = \mathrm{Cov}(Y, X)$$, $$\mathrm{Cov}(X, X) = \mathrm{Var}(X)$$.
> - (b) $$\mathrm{Cov}(aX + b,\ cY + d) = ac\,\mathrm{Cov}(X, Y)$$ ($$a, b, c, d$$ constants).
> - (c) $$\mathrm{Cov}(X, Y) = E(XY) - [E(X)][E(Y)]$$.
{: .theorem #thm-covariance-properties }

(These hold on the premise that the expectations and covariance on the right side are real numbers.)

*Proof.* (a) is clear from the definition of the covariance. Let the means of $$X, Y$$ be $$\mu_1, \mu_2$$; then $$E(aX + b) = a\mu_1 + b$$ and $$E(cY + d) = c\mu_2 + d$$.

(b) Let $$V = aX + b$$, $$W = cY + d$$. Then $$V - E(V) = a(X - \mu_1)$$ and $$W - E(W) = c(Y - \mu_2)$$, so

$$
\mathrm{Cov}(V, W) = E[\{V - E(V)\}\{W - E(W)\}] = E[a(X - \mu_1)c(Y - \mu_2)] = ac\,\mathrm{Cov}(X, Y).
$$

(c) By the definition of covariance and the linearity of expectation,

$$
\mathrm{Cov}(X, Y) = E[(X - \mu_1)(Y - \mu_2)] = E[XY - \mu_1Y - X\mu_2 + \mu_1\mu_2] = E(XY) - 2\mu_1\mu_2 + \mu_1\mu_2 = E(XY) - [E(X)][E(Y)]. \qquad \square
$$

**Example 2.2.3.** In Examples 2.2.1 and 2.2.2, with $$f(x, y) = 120xy(1 - x - y)I_{(x \ge 0,\ y \ge 0,\ x + y \le 1)}$$, $$E(XY) = \frac{2}{21}$$ and $$E(X) = \frac{1}{3}$$. In the same way $$E(Y) = \frac{1}{3}$$, and by the calculation formula,

$$
\mathrm{Cov}(X, Y) = E(XY) - [E(X)][E(Y)] = \frac{2}{21} - \frac{1}{3}\cdot\frac{1}{3} = -\frac{1}{63}.
$$

**Example 2.2.4.** With the same pdf, the marginal pdf of $$X$$ is $$f_1(x) = 20x(1 - x)^3I_{(0 \le x \le 1)}$$ and $$E(X) = \frac{1}{3}$$, so

$$
\mathrm{Var}(X) = E(X^2) - \{E(X)\}^2 = \int_0^1 x^2\cdot 20x(1 - x)^3\,dx - \Bigl(\frac{1}{3}\Bigr)^2 = \frac{1}{7} - \frac{1}{9} = \frac{2}{63}.
$$

In the same way $$\mathrm{Var}(Y) = \frac{2}{63}$$, and since $$\mathrm{Cov}(X, Y) = -\frac{1}{63}$$ by Example 2.2.3, the correlation coefficient is

$$
\mathrm{Corr}(X, Y) = \frac{-1/63}{\sqrt{2/63}\sqrt{2/63}} = -\frac{1}{2}.
$$

> **Theorem 2.2.3 (Properties of the correlation coefficient).** Let the mean and standard deviation of $$X$$ be $$\mu_1$$ and $$\sigma_1$$ ($$\sigma_1 > 0$$), those of $$Y$$ be $$\mu_2$$ and $$\sigma_2$$ ($$\sigma_2 > 0$$), and the correlation coefficient of $$X, Y$$ be $$\rho$$. Then
>
> - (a) $$\mathrm{Var}\Bigl(\dfrac{Y - \mu_2}{\sigma_2} - \rho\,\dfrac{X - \mu_1}{\sigma_1}\Bigr) = 1 - \rho^2$$.
> - (b) $$-1 \le \rho \le 1$$.
> - (c) $$\rho = 1 \Longleftrightarrow P\Bigl(\dfrac{Y - \mu_2}{\sigma_2} = \dfrac{X - \mu_1}{\sigma_1}\Bigr) = 1$$, and $$\rho = -1 \Longleftrightarrow P\Bigl(\dfrac{Y - \mu_2}{\sigma_2} = -\dfrac{X - \mu_1}{\sigma_1}\Bigr) = 1$$.
{: .theorem #thm-correlation-properties }

*Proof.* (a) Since $$E\bigl(\frac{Y - \mu_2}{\sigma_2} - \rho\frac{X - \mu_1}{\sigma_1}\bigr) = 0$$,

$$
\begin{aligned}
\mathrm{Var}\Bigl(\frac{Y - \mu_2}{\sigma_2} - \rho\frac{X - \mu_1}{\sigma_1}\Bigr)
&= E\Bigl[\Bigl(\frac{Y - \mu_2}{\sigma_2} - \rho\frac{X - \mu_1}{\sigma_1}\Bigr)^2\Bigr] \\
&= E\Bigl[\Bigl(\frac{Y - \mu_2}{\sigma_2}\Bigr)^2\Bigr] - 2\rho E\Bigl[\Bigl(\frac{Y - \mu_2}{\sigma_2}\Bigr)\Bigl(\frac{X - \mu_1}{\sigma_1}\Bigr)\Bigr] + \rho^2E\Bigl[\Bigl(\frac{X - \mu_1}{\sigma_1}\Bigr)^2\Bigr] \\
&= 1 - 2\rho\frac{\mathrm{Cov}(Y, X)}{\sigma_2\sigma_1} + \rho^2 = 1 - \rho^2.
\end{aligned}
$$

(b) A variance is at least $$0$$, so by (a), $$1 - \rho^2 \ge 0$$. Hence $$-1 \le \rho \le 1$$.

(c) When $$\rho = \pm 1$$ the variance in (a) is $$0$$, so (c) follows from Theorem 1.6.4 (a random variable with variance $$0$$ equals its mean with probability $$1$$). $$\square$$

As in Theorem 2.2.3, the correlation coefficient of $$X, Y$$ is written $$\rho_{X,Y}$$ or $$\rho_{1,2}$$, or $$\rho$$ when there is no confusion. Expressing the range of the correlation coefficient in Theorem 2.2.3 through the covariance and the standard deviations gives the following inequality:

$$
\lvert\mathrm{Cov}(X, Y)\rvert \le \sqrt{\mathrm{Var}(X)}\sqrt{\mathrm{Var}(Y)}.
$$

(In general $$\lvert E(VW)\rvert \le \sqrt{E(V^2)}\sqrt{E(W^2)}$$ holds, called the Cauchy–Schwarz inequality.)

As Theorem 2.2.3 shows, the larger the absolute value of the correlation coefficient, the closer the distribution of $$(X, Y)$$ lies to the line $$\frac{y - \mu_2}{\sigma_2} = \rho\frac{x - \mu_1}{\sigma_1}$$. In this sense the correlation coefficient is a characteristic of the linear relation between two variables.

## Joint moments and the joint moment generating function

As the covariance and the correlation coefficient describe the linear relation between two variables, the characteristics of the joint distribution include the joint moments.

> **Joint moment.** When $$E(\lvert X^rY^s\rvert) < +\infty$$,
>
> $$
> E(X^rY^s) =
> \begin{cases}
> \sum_x\sum_y x^ry^sf(x, y) & ((X, Y) \text{ discrete}) \\
> \displaystyle\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}x^ry^sf(x, y)\,dy\,dx & ((X, Y) \text{ continuous})
> \end{cases}
> $$
>
> is called the $$(r, s)$$-th joint moment of order $$(r + s)$$ of $$(X, Y)$$, written $$m_{r,s}(X, Y)$$ or $$m_{r,s}$$.
{: .definition #def-joint-moment }

As for one random variable, consider a generating function of these joint moments. From the power series of the exponential function,

$$
e^{t_1X}e^{t_2Y} = \sum_{r=0}^{\infty}\frac{(t_1X)^r}{r!}\sum_{s=0}^{\infty}\frac{(t_2Y)^s}{s!} = \sum_{r=0}^{\infty}\sum_{s=0}^{\infty}\frac{X^rY^s}{r!s!}t_1^rt_2^s,
$$

and if the expectation of the right side could be taken term by term,

$$
E\bigl(e^{t_1X + t_2Y}\bigr) = \sum_{r=0}^{\infty}\sum_{s=0}^{\infty}\frac{E(X^rY^s)}{r!s!}t_1^rt_2^s.
$$

For this reason the joint moment generating function is defined as follows. A function so defined not only generates the joint moments, but also determines the joint distribution.

> **Joint moment generating function.** If $$E(e^{t_1X + t_2Y})$$ is a real number for $$t_1, t_2$$ in open intervals containing $$0$$, the function
>
> $$
> M(t_1, t_2) = E\bigl(e^{t_1X + t_2Y}\bigr), \quad -h_1 < t_1 < h_1,\ -h_2 < t_2 < h_2 \quad (\exists h_1 > 0,\ h_2 > 0)
> $$
>
> is called the joint moment generating function of $$(X, Y)$$.
{: .definition #def-joint-mgf }

> **Theorem 2.2.4 (Properties of the joint moment generating function).**
>
> - (a) *(Generation of joint moments.)* If the joint mgf of the bivariate random vector $$(X, Y)$$ exists, i.e. $$M(t_1, t_2) = E(e^{t_1X + t_2Y}) < +\infty$$ for $$-h_1 < t_1 < h_1$$, $$-h_2 < t_2 < h_2$$ ($$\exists h_1 > 0$$, $$h_2 > 0$$), then all joint moments of $$(X, Y)$$ exist and
>
>   $$
>   E(X^rY^s) = \Bigl[\frac{\partial^{r+s}}{\partial t_1^r\partial t_2^s}M(t_1, t_2)\Bigr]_{\substack{t_1 = 0 \\ t_2 = 0}}, \qquad
>   M(t_1, t_2) = \sum_{r=0}^{\infty}\sum_{s=0}^{\infty}\frac{E(X^rY^s)}{r!s!}t_1^rt_2^s.
>   $$
>
> - (b) *(Determination of the distribution.)* If the joint mgfs $$M_{X_1,X_2}(t_1, t_2)$$ and $$M_{Y_1,Y_2}(t_1, t_2)$$ of two bivariate random vectors $$(X_1, X_2)$$ and $$(Y_1, Y_2)$$ exist and agree on open intervals containing $$0$$, i.e. $$M_{X_1,X_2}(t_1, t_2) = M_{Y_1,Y_2}(t_1, t_2)$$ for all $$t_i$$ with $$-h_i < t_i < h_i$$ ($$\exists h_i > 0$$) ($$i = 1, 2$$), then the probability distributions of $$(X_1, X_2)$$ and $$(Y_1, Y_2)$$ agree; that is, their joint pdfs and joint cdfs agree.
{: .theorem #thm-joint-mgf-properties }

As for one random variable, when the joint mgf $$M(t_1, t_2)$$ exists,

$$
C(t_1, t_2) = \log M(t_1, t_2) = \log E\bigl(e^{t_1X + t_2Y}\bigr), \quad -h_i < t_i < h_i\ (\exists h_i > 0)\ (i = 1, 2)
$$

is called the *joint cumulant generating function* of $$(X, Y)$$, and in its power series expansion

$$
C(t_1, t_2) = \sum_{r=0}^{\infty}\sum_{s=0}^{\infty}\frac{C^{(r,s)}(0,0)}{r!s!}t_1^rt_2^s, \qquad C^{(r,s)}(0, 0) = \Bigl[\frac{\partial^{r+s}}{\partial t_1^r\partial t_2^s}C(t_1, t_2)\Bigr]_{\substack{t_1 = 0 \\ t_2 = 0}},
$$

the coefficient $$C^{(r,s)}(0, 0)$$ of $$t_1^rt_2^s/r!s!$$ is called the $$(r, s)$$-th joint cumulant of order $$(r + s)$$ of $$(X, Y)$$, written $$c_{r,s}(X, Y)$$ or $$c_{r,s}$$. The relation between the joint cumulants $$c_{r,s}$$ and the joint moments $$m_{j,k}$$ is found from

$$
\log\Bigl(1 + \sum_{\substack{j,k \ge 0 \\ j + k \ge 1}}\frac{m_{j,k}}{j!k!}t_1^jt_2^k\Bigr) = \sum_{\substack{r,s \ge 0 \\ r + s \ge 1}}\frac{c_{r,s}}{r!s!}t_1^rt_2^s.
$$

Using the power series $$\log(1 + A) = A - A^2/2 + A^3/3 - \cdots$$ ($$-1 < A < 1$$) with $$A = (m_{1,0}t_1 + m_{0,1}t_2) + (m_{2,0}t_1^2/2! + m_{1,1}t_1t_2 + m_{0,2}t_2^2/2!) + \cdots$$, and arranging the result in order of $$t_1, t_2$$:

$$
\begin{aligned}
c_{1,0} &= m_{1,0} = E(X), & c_{0,1} &= m_{0,1} = E(Y), \\
c_{2,0} &= m_{2,0} - (m_{1,0})^2 = E(X^2) - [E(X)]^2 = \mathrm{Var}(X), \\
c_{1,1} &= m_{1,1} - m_{1,0}m_{0,1} = E(XY) - [E(X)][E(Y)] = \mathrm{Cov}(X, Y), \\
c_{0,2} &= m_{0,2} - (m_{0,1})^2 = E(Y^2) - [E(Y)]^2 = \mathrm{Var}(Y).
\end{aligned}
$$

So the cumulants of first and second order are, respectively, the means and the variances or covariance.

**Example 2.2.5.** In Example 2.1.2 the joint pdf of $$(X, Y)$$ is $$f(x, y) = 2e^{-x-y}I_{(0 \le x \le y)}$$, so its joint mgf is

$$
M(t_1, t_2) = \int_{-\infty}^{\infty}\int_{-\infty}^{\infty}e^{t_1x + t_2y}f(x, y)\,dy\,dx = \int_0^{\infty}\int_x^{\infty}e^{t_1x + t_2y}2e^{-x-y}\,dy\,dx
= \int_0^{\infty}2e^{-(1 - t_1)x}\Bigl[-\frac{1}{1 - t_2}e^{-(1 - t_2)y}\Bigr]_x^{\infty}dx = \frac{1}{1 - t_2}\int_0^{\infty}2e^{-(2 - t_1 - t_2)x}\,dx = \frac{1}{1 - t_2}\cdot\frac{2}{2 - t_1 - t_2},
$$

for $$t_2 < 1$$, $$t_1 + t_2 < 2$$. Expanding the joint cumulant generating function in a power series, for $$t_1 + t_2 < 2$$, $$t_2 < 1$$,

$$
C(t_1, t_2) = -\log(1 - t_2) - \log\bigl(1 - (t_1 + t_2)/2\bigr)
= \{t_2 + t_2^2/2 + \cdots\} + \{(t_1 + t_2)/2 + [(t_1 + t_2)/2]^2/2 + \cdots\}
= \{(1/2)t_1 + (3/2)t_2\} + \{(1/4)t_1^2/2 + (1/4)t_1t_2 + (5/4)t_2^2/2\} + \cdots
$$

Therefore $$E(X) = c_{1,0} = \frac{1}{2}$$, $$E(Y) = c_{0,1} = \frac{3}{2}$$, $$\mathrm{Var}(X) = c_{2,0} = \frac{1}{4}$$, $$\mathrm{Cov}(X, Y) = c_{1,1} = \frac{1}{4}$$, $$\mathrm{Var}(Y) = c_{0,2} = \frac{5}{4}$$, and from these $$\mathrm{Corr}(X, Y) = \dfrac{\mathrm{Cov}(X, Y)}{\sqrt{\mathrm{Var}(X)}\sqrt{\mathrm{Var}(Y)}} = \dfrac{1}{\sqrt{5}}$$.

As for pdfs, to distinguish the mgf of each variable from the joint mgf of $$X$$ and $$Y$$, the mgf of each variable is called its *marginal mgf*:

$$
M_X(s) = E(e^{sX}), \quad -h_1 < s < h_1\ (\exists h_1 > 0), \qquad
M_Y(t) = E(e^{tY}), \quad -h_2 < t < h_2\ (\exists h_2 > 0),
$$

and their logarithms are the marginal cumulant generating functions. They are obtained from the corresponding joint functions as

$$
M_X(s) = M_{X,Y}(s, 0), \quad C_X(s) = C_{X,Y}(s, 0), \qquad M_Y(t) = M_{X,Y}(0, t), \quad C_Y(t) = C_{X,Y}(0, t).
$$

**Example 2.2.6.** For the pdf of Example 2.1.2, the marginal pdf of $$X$$ is $$f_1(x) = 2e^{-2x}I_{(x \ge 0)}$$ by Example 2.1.4, so the marginal mgf of $$X$$ is

$$
M_X(s) = \int_0^{\infty}e^{sx}2e^{-2x}\,dx = (1 - s/2)^{-1}, \qquad s < 2,
$$

which agrees with $$M_{X,Y}(s, 0)$$ of Example 2.2.5.

## References

- 김우철, *수리통계학* (Mathematical Statistics), revised 2nd edition, 민영사, 2021 — Chapter 2, §2.2 (Examples 2.2.1 to 2.2.6, Theorems 2.2.1 to 2.2.4). Translated from the book; not from my notes.
- Mathematical Statistics 1 (326.311), Seoul National University, Spring 2025. Instructor: Jaeyong Lee (이재용).

[Previous](/posts/mathstat1-joint-distribution/) · [Overview](/posts/mathstat1-overview/) · [Next](/posts/mathstat1-conditional-distribution/)
