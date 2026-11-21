---
title: "Mathematical Statistics 1: Homework 3, Chapter 2 Exercises"
date: 2026-11-21 10:20:00 +0900
categories: [Study Notes, Mathematical Statistics 1]
tags: [homework, joint distribution, conditional expectation, covariance, multivariate mgf, independence]
description: Homework 3 of Mathematical Statistics 1, the Chapter 2 part — textbook exercises 2.1 to 2.17 on joint, marginal and conditional distributions, covariance, joint moment generating functions, the multiple correlation coefficient and independence.
math: true
mermaid: false
render_with_liquid: false
---

> The problems are from the Homework 3 sheet ("Chapter 1, exercises 18–25; Chapter 2, all problems") and from the textbook. This post holds the Chapter 2 part; the Chapter 1 part is in [Homework 3, Chapter 1 Exercises](/posts/mathstat1-homework-3-chapter-1/). The answers are my own, translated into English. I checked each result against the problem; the only change is one matrix step in Exercise 2.12(c), marked **Correction**, and a consistency check marked **Added** at the end of 2.17. The structure of every answer is unchanged. This homework uses [Part 1 to Part 5](/posts/mathstat1-joint-distribution/) of Chapter 2.
{: .prompt-info }

### Exercise 2.1

> **Exercise 2.1.** The joint probability density function of random variables $$X$$ and $$Y$$ is $$f_{1,2}(x, y) = 10xy^2\,I_{(0<x<y<1)}$$. Find the following probabilities. (a) $$P(Y \le 1/2)$$ (b) $$P(X + Y \le 1)$$
{: .problem #hw3-2-1 }

**(a)** To find $$P(Y \le \frac{1}{2})$$ we find the marginal probability density function of $$Y$$. Then

$$
f_2(y) = \int_{-\infty}^{\infty}10xy^2\,I_{(0<x<y<1)}\,dx = y^2I_{(0<y<1)}\int_0^y 10x\,dx = 5y^4\,I_{(0<y<1)},
$$

so

$$
P\bigl(Y \le \tfrac{1}{2}\bigr) = \int_{-\infty}^{1/2}f_2(y)\,dy = \int_{-\infty}^{1/2}5y^4I_{(0<y<1)}\,dy = \int_0^{1/2}5y^4\,dy = \frac{1}{32}.
$$

**(b)** For the random variables $$X$$ and $$Y$$, $$P(X + Y \le 1) = P(Y \le 1 - X)$$, so

$$
P(Y \le 1 - X) = \int_{-\infty}^{\infty}\int_{-\infty}^{1-x}f_{1,2}(x, y)\,dy\,dx = \int_{-\infty}^{\infty}\int_{-\infty}^{1-x}10xy^2I_{(0<x<y<1)}\,dy\,dx
= 10\int_0^{1/2}\int_x^{1-x}xy^2\,dy\,dx = \frac{10}{3}\int_0^{1/2}x\bigl\{(1 - x)^3 - x^3\bigr\}dx = \frac{10}{3}\int_0^{1/2}\bigl(x - 3x^2 + 3x^3 - 2x^4\bigr)dx,
$$

$$
= \frac{10}{3}\Bigl(\frac{1}{2}\bigl(\tfrac{1}{2}\bigr)^2 - \bigl(\tfrac{1}{2}\bigr)^3 + \frac{3}{4}\bigl(\tfrac{1}{2}\bigr)^4 - \frac{2}{5}\bigl(\tfrac{1}{2}\bigr)^5\Bigr) = \frac{10}{3}\cdot\frac{11}{320} = \frac{11}{96}.
$$

### Exercise 2.2

> **Exercise 2.2.** The joint probability density function of $$X$$ and $$Y$$ is $$f_{1,2}(x, y) = c\,x^2y\,I_{(0<x<y<1)}$$. Find (a) the constant $$c$$, (b) $$P(Y \le 1/2)$$, (c) $$P(Y \le 2X)$$.
{: .problem #hw3-2-2 }

**(a)** The constant $$c$$ can be found using that the integral of the joint probability density function over the whole of $$\mathbb{R}^2$$ is $$1$$, that is, $$\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}f_{1,2}(x, y)\,dx\,dy = 1$$. Then

$$
\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}c\,x^2y\,I_{(0<x<y<1)}\,dx\,dy = \int_0^1\int_0^y c\,x^2y\,dx\,dy = \int_0^1\frac{1}{3}c\,y^4\,dy = \frac{1}{15}c,
$$

so $$\frac{1}{15}c = 1$$, that is, $$c = 15$$.

**(b)** Using $$P(Y \le \frac{1}{2}) = \int_{-\infty}^{1/2}\int_{-\infty}^{\infty}f_{1,2}(x, y)\,dx\,dy$$,

$$
P\bigl(Y \le \tfrac{1}{2}\bigr) = \int_{-\infty}^{1/2}\int_{-\infty}^{\infty}15x^2y\,I_{(0<x<y<1)}\,dx\,dy = \int_0^{1/2}\int_0^y 15x^2y\,dx\,dy = \int_0^{1/2}5y^4\,dy = \frac{1}{32}.
$$

**(c)** $$P(Y \le 2X) = P\bigl(X \ge \tfrac{1}{2}Y\bigr)$$, so

$$
P(Y \le 2X) = \int_0^1\int_{y/2}^{y}15x^2y\,dx\,dy = \int_0^1\frac{35}{8}y^4\,dy = \frac{7}{8}.
$$

### Exercise 2.3

> **Exercise 2.3.** The joint probability density function of $$X$$ and $$Y$$ is $$f_{1,2}(x, y) = e^{-y}I_{(0<x<y<\infty)}$$. Find (a) $$P(X \le 1)$$, (b) $$P(X + Y \le 1)$$.
{: .problem #hw3-2-3 }

**(a)**

$$
P(X \le 1) = \int_{-\infty}^{1}\int_{-\infty}^{\infty}f_{1,2}(x, y)\,dy\,dx = \int_0^1\int_x^{\infty}e^{-y}\,dy\,dx = \int_0^1 e^{-x}\,dx = 1 - \frac{1}{e}.
$$

**(b)** $$P(X + Y \le 1) = P(Y \le 1 - X)$$, so

$$
P(X + Y \le 1) = \int_{-\infty}^{\infty}\int_{-\infty}^{1-x}e^{-y}I_{(0<x<y<1)}\,dy\,dx = \int_0^{1/2}\int_x^{1-x}e^{-y}\,dy\,dx = \int_0^{1/2}\bigl(e^{-x} - e^{x-1}\bigr)dx = 1 + \frac{1}{e} - \frac{2}{\sqrt{e}}.
$$

### Exercise 2.4

> **Exercise 2.4.** Find the marginal probability density function of $$X$$ when the joint pdf of $$X$$ and $$Y$$ is (a) $$f_{1,2}(x, y) = 2I_{(0<x<y<1)}$$, (b) $$f_{1,2}(x, y) = e^{-y}I_{(0<x<y<\infty)}$$.
{: .problem #hw3-2-4 }

**(a)** The marginal probability density function is

$$
f_1(x) = \int_{-\infty}^{\infty}f_{1,2}(x, y)\,dy = \int_{-\infty}^{\infty}2I_{(0<x<y<1)}\,dy = I_{(0<x<1)}\int_x^1 2\,dy = (2 - 2x)\,I_{(0<x<1)}.
$$

**(b)** The marginal probability density function is

$$
f_1(x) = \int_{-\infty}^{\infty}e^{-y}I_{(0<x<y<\infty)}\,dy = I_{(x>0)}\int_x^{\infty}e^{-y}\,dy = e^{-x}I_{(x>0)}.
$$

### Exercise 2.5

> **Exercise 2.5.** Find the joint probability density function of $$X$$ and $$Y$$ when their joint cumulative distribution function is
>
> - (a) $$F_{1,2}(x, y) = x^2(1 - e^{-2y})$$ ($$0 \le x < 1$$, $$y \ge 0$$); $$1 - e^{-2y}$$ ($$x \ge 1$$, $$y \ge 0$$); $$0$$ ($$y < 0$$)
> - (b) $$F_{1,2}(x, y) = 1 - 2e^{-y} - e^{-2x} + 2e^{-x-y}$$ ($$0 < x < y$$); $$1 - 2e^{-y} + e^{-2y}$$ ($$0 < y \le x$$); $$0$$ ($$x \le 0$$ or $$y \le 0$$)
{: .problem #hw3-2-5 }

**(a)** The joint probability density function of $$X$$ and $$Y$$ is $$\dfrac{\partial^2}{\partial x\,\partial y}F_{1,2}(x, y)$$ at the points $$(x, y)$$ where it is continuous. Therefore, on the interval $$y < 0$$, $$f_{1,2}(x, y) = 0$$, and when $$0 \le x < 1$$ and $$y \ge 0$$, $$F_{1,2}(x, y) = x^2(1 - e^{-2y})$$, so $$f_{1,2}(x, y) = 4x\,e^{-2y}$$. Also, when $$x \ge 1$$ and $$y \ge 0$$, $$f_{1,2}(x, y) = 0$$. To summarize,

$$
f_{1,2}(x, y) = 2x\,I_{(0 \le x < 1)}\cdot 2e^{-2y}\,I_{(y \ge 0)}.
$$

**(b)** The joint probability density function of $$X$$ and $$Y$$ is $$\dfrac{\partial^2}{\partial x\,\partial y}F_{1,2}(x, y)$$ at the points where it is continuous. Therefore, when $$0 < x < y$$, $$f_{1,2}(x, y) = 2e^{-x-y}$$, and when $$0 < y \le x$$, $$f_{1,2}(x, y) = 0$$, and also when $$x \le 0$$ or $$y \le 0$$, $$f_{1,2}(x, y) = 0$$. That is,

$$
f_{1,2}(x, y) = 2e^{-x-y}\,I_{(0<x<y)}.
$$

### Exercise 2.6

> **Exercise 2.6.** Find the covariance $$\mathrm{Cov}(X, Y)$$ of $$X$$ and $$Y$$ when their joint pdf is $$f_{1,2}(x, y) = x\,e^{-y}I_{(0<x<y<\infty)}$$.
{: .problem #hw3-2-6 }

Let the expectation of $$X$$ be $$\mu_X$$, that of $$Y$$ be $$\mu_Y$$, and that of the random variable $$XY$$ be $$\mu_{XY}$$. We find the covariance of $$X$$ and $$Y$$ from the marginal probability density functions. First,

$$
f_1(x) = \int_{-\infty}^{\infty}f_{1,2}(x, y)\,dy = \int_{-\infty}^{\infty}x\,e^{-y}I_{(0<x<y<\infty)}\,dy = x\,I_{(x>0)}\int_x^{\infty}e^{-y}\,dy = x\,e^{-x}I_{(x>0)},
$$

$$
f_2(y) = \int_{-\infty}^{\infty}f_{1,2}(x, y)\,dx = e^{-y}I_{(y>0)}\int_0^y x\,dx = \tfrac{1}{2}y^2e^{-y}I_{(y>0)}.
$$

Therefore $$\mu_X = \int_{-\infty}^{\infty}x f_1(x)\,dx = \int_0^{\infty}x^2e^{-x}\,dx = 2$$ and $$\mu_Y = \int_{-\infty}^{\infty}y f_2(y)\,dy = \frac{1}{2}\int_0^{\infty}y^3e^{-y}\,dy = \frac{1}{2}\times 6 = 3$$. Also

$$
\mu_{XY} = \int_{-\infty}^{\infty}\int_{-\infty}^{\infty}xy\,f_{1,2}(x, y)\,dx\,dy = \int_0^{\infty}y\,e^{-y}\int_0^y x^2\,dx\,dy = \frac{1}{3}\int_0^{\infty}y^4e^{-y}\,dy = \frac{1}{3}\times 24 = 8.
$$

Therefore $$\mathrm{Cov}(X, Y) = \mu_{XY} - \mu_X\mu_Y = 8 - 3\times 2 = 2$$.

### Exercise 2.7

> **Exercise 2.7.** The joint pdf of $$X$$ and $$Y$$ is $$f_{1,2}(x, y) = e^{-y}I_{(0<x<y<\infty)}$$. Find (a) the joint moment generating function $$M(t_1, t_2)$$ of $$X$$ and $$Y$$, (b) the correlation coefficient $$\mathrm{Corr}(X, Y)$$.
{: .problem #hw3-2-7 }

**(a)** The joint moment generating function of $$X$$ and $$Y$$ is $$M(t_1, t_2) = E(e^{t_1X + t_2Y})$$, so it can be found as follows:

$$
M(t_1, t_2) = \int_{-\infty}^{\infty}\int_{-\infty}^{\infty}e^{t_1x + t_2y}f_{1,2}(x, y)\,dx\,dy = \int_0^{\infty}e^{t_1x}\int_x^{\infty}e^{(t_2 - 1)y}\,dy\,dx = \int_0^{\infty}\frac{1}{1 - t_2}e^{(t_1 + t_2 - 1)x}\,dx = \frac{1}{1 - t_2}\cdot\frac{1}{1 - t_1 - t_2}.
$$

Here, the range in which the given integral converges is $$t_2 < 1$$ and $$t_1 + t_2 < 1$$. That is,

$$
M(t_1, t_2) = \frac{1}{1 - t_2}\cdot\frac{1}{1 - t_1 - t_2} \qquad (t_1 + t_2 < 1,\ t_2 < 1).
$$

**(b)** Since the joint moment generating function of $$X$$ and $$Y$$ is $$M(t_1, t_2) = \frac{1}{1 - t_2}\frac{1}{1 - t_1 - t_2}$$ ($$t_1 + t_2 < 1$$, $$t_2 < 1$$), the joint cumulant generating function is $$C(t_1, t_2) = \log M(t_1, t_2) = -\log(1 - t_2) - \log(1 - t_1 - t_2)$$ ($$t_1 + t_2 < 1$$, $$t_2 < 1$$). That is,

$$
C(t_1, t_2) = \sum_{r=1}^{\infty}\frac{1}{r}t_2^r + \sum_{r=1}^{\infty}\frac{1}{r}(t_1 + t_2)^r = t_2 + \tfrac{1}{2}t_2^2 + o(t_2^2) + t_1 + t_2 + \tfrac{1}{2}(t_1 + t_2)^2 + o\bigl((t_1 + t_2)^2\bigr) = t_1 + 2t_2 + \tfrac{1}{2}t_1^2 + t_1t_2 + t_2^2 + o\bigl((t_1 + t_2)^2\bigr).
$$

Therefore, if the cumulant of order $$1$$ in $$X$$ and order $$1$$ in $$Y$$ is $$C_{1,1}$$, then $$\frac{C_{1,1}}{1!\,1!} = 1$$, so $$C_{1,1} = 1$$. If the second-order cumulant in $$X$$ is $$C_{2,0}$$ and that in $$Y$$ is $$C_{0,2}$$, then $$\frac{C_{2,0}}{2!} = \frac{1}{2}$$ and $$\frac{C_{0,2}}{2!} = 1$$, so $$C_{2,0} = \mathrm{Var}(X) = 1$$ and $$C_{0,2} = \mathrm{Var}(Y) = 2$$. Also $$C_{1,1} = \mathrm{Cov}(X, Y)$$, so

$$
\mathrm{Corr}(X, Y) = \frac{\mathrm{Cov}(X, Y)}{\sqrt{\mathrm{Var}(X)}\sqrt{\mathrm{Var}(Y)}} = \frac{1}{\sqrt{1}\sqrt{2}} = \frac{1}{\sqrt{2}} = \frac{\sqrt{2}}{2}.
$$

### Exercise 2.8

> **Exercise 2.8.** The joint pdf of $$X$$ and $$Y$$ is $$f_{1,2}(x, y) = 10xy^2\,I_{(0<x<y<1)}$$. Find (a) the marginal pdf $$f_2(y)$$ of $$Y$$, (b) the conditional pdf $$f_{1 \mid 2}(x \mid y)$$ of $$X$$ given $$Y = y$$ ($$0 < y < 1$$), (c) $$E(X \mid Y)$$, $$\mathrm{Var}(X \mid Y)$$, (d) $$\mathrm{Var}[E(X \mid Y)]$$, $$E[\mathrm{Var}(X \mid Y)]$$, (e) the marginal pdf $$f_1(x)$$ of $$X$$ and $$\mathrm{Var}(X)$$.
{: .problem #hw3-2-8 }

**(a)** For the marginal probability density function $$f_2(y)$$ of $$Y$$,

$$
f_2(y) = \int_{-\infty}^{\infty}f_{1,2}(x, y)\,dx = \int_{-\infty}^{\infty}10xy^2I_{(0<x<y<1)}\,dx = \int_0^y 10xy^2\,dx\ I_{(0<y<1)} = 5y^4\,I_{(0<y<1)}.
$$

**(b)** Given $$Y = y$$ ($$0 < y < 1$$), $$f_2(y) > 0$$, so the conditional pdf of $$X$$ is $$f_{1 \mid 2}(x \mid y) = \dfrac{f_{1,2}(x, y)}{f_2(y)}$$. Therefore, for $$y$$ with $$0 < y < 1$$,

$$
f_{1 \mid 2}(x \mid y) = \frac{10xy^2I_{(0<x<y<1)}}{5y^4I_{(0<y<1)}} = \frac{2x}{y^2}\,I_{(0<x<y)}.
$$

**(c)** If $$y \le 0$$ or $$y \ge 1$$, then $$f_2(y) = 0$$, so the conditional pdf $$f_{1 \mid 2}(x \mid y)$$ is not defined. Therefore, for the conditional mean $$E(X \mid Y = y)$$ with $$0 < y < 1$$,

$$
E(X \mid Y = y) = \int_{-\infty}^{\infty}x\,f_{1 \mid 2}(x \mid y)\,dx = \int_{-\infty}^{\infty}x\cdot\frac{2x}{y^2}I_{(0<x<y)}\,dx = \frac{1}{y^2}\int_0^y 2x^2\,dx = \frac{2}{3}y.
$$

That is, $$E(X \mid Y) = \frac{2}{3}Y$$. Also, for the conditional expectation $$E(X^2 \mid Y = y)$$ with $$0 < y < 1$$,

$$
E(X^2 \mid Y = y) = \int_{-\infty}^{\infty}x^2f_{1 \mid 2}(x \mid y)\,dx = \int_{-\infty}^{\infty}x^2\cdot\frac{2x}{y^2}I_{(0<x<y)}\,dx = \frac{1}{y^2}\int_0^y 2x^3\,dx = \frac{1}{2}y^2.
$$

Therefore $$E(X^2 \mid Y) = \frac{1}{2}Y^2$$. Then $$\mathrm{Var}(X \mid Y) = E(X^2 \mid Y) - \{E(X \mid Y)\}^2 = \frac{1}{2}Y^2 - \bigl(\frac{2}{3}Y\bigr)^2 = \frac{1}{18}Y^2$$.

**(d)** From the marginal pdf of $$Y$$ we first find $$E(Y)$$ and $$\mathrm{Var}(Y)$$. Then $$E(Y) = \int_{-\infty}^{\infty}y f_2(y)\,dy = \int_{-\infty}^{\infty}5y^5I_{(0<y<1)}\,dy = \int_0^1 5y^5\,dy = \frac{5}{6}$$, and $$E(Y^2) = \int_{-\infty}^{\infty}y^2f_2(y)\,dy = \int_{-\infty}^{\infty}5y^6I_{(0<y<1)}\,dy = \int_0^1 5y^6\,dy = \frac{5}{7}$$. Therefore $$\mathrm{Var}(Y) = E(Y^2) - \{E(Y)\}^2 = \frac{5}{252}$$. Hence

$$
\mathrm{Var}\bigl(E(X \mid Y)\bigr) = \mathrm{Var}\bigl(\tfrac{2}{3}Y\bigr) = \frac{4}{9}\mathrm{Var}(Y) = \frac{5}{567}, \qquad E\bigl(\mathrm{Var}(X \mid Y)\bigr) = E\bigl(\tfrac{1}{18}Y^2\bigr) = \frac{5}{126}.
$$

### Exercise 2.9

> **Exercise 2.9.** The joint pdf of $$X$$ and $$Y$$ is $$f_{1,2}(x, y) = e^{-y}I_{(0<x<y<\infty)}$$. Find (a) the marginal pdf $$f_2(y)$$ of $$Y$$, (b) the conditional pdf $$f_{1 \mid 2}(x \mid y)$$ of $$X$$ given $$Y = y$$ ($$y > 0$$), (c) $$E(X \mid Y)$$, $$\mathrm{Var}(X \mid Y)$$, (d) $$\mathrm{Var}[E(X \mid Y)]$$, $$E[\mathrm{Var}(X \mid Y)]$$, (e) the marginal pdf $$f_1(x)$$ of $$X$$ and $$\mathrm{Var}(X)$$.
{: .problem #hw3-2-9 }

**(a)** $$f_2(y) = \displaystyle\int_{-\infty}^{\infty}f_{1,2}(x, y)\,dx = \int_{-\infty}^{\infty}e^{-y}I_{(0<x<y<\infty)}\,dx = \int_0^y e^{-y}\,dx\ I_{(y>0)} = y\,e^{-y}I_{(y>0)}$$.

**(b)** Given $$Y = y$$ ($$y > 0$$), $$f_2(y) > 0$$, so $$f_{1 \mid 2}(x \mid y) = \dfrac{f_{1,2}(x, y)}{f_2(y)}$$. Therefore, for $$y > 0$$,

$$
f_{1 \mid 2}(x \mid y) = \frac{e^{-y}I_{(0<x<y<\infty)}}{y\,e^{-y}I_{(y>0)}} = \frac{1}{y}\,I_{(0<x<y)}.
$$

**(c)** If $$y \le 0$$, $$f_2(y) = 0$$, so the conditional pdf $$f_{1 \mid 2}(x \mid y)$$ is not defined. Therefore, for $$y > 0$$,

$$
E(X \mid Y = y) = \int_{-\infty}^{\infty}x\,f_{1 \mid 2}(x \mid y)\,dx = \int_{-\infty}^{\infty}\frac{x}{y}I_{(0<x<y)}\,dx = \frac{1}{y}\int_0^y x\,dx = \frac{1}{2}y,
$$

so $$E(X \mid Y) = \frac{1}{2}Y$$. Also, for $$E(X^2 \mid Y = y)$$,

$$
E(X^2 \mid Y = y) = \int_{-\infty}^{\infty}x^2f_{1 \mid 2}(x \mid y)\,dx = \int_{-\infty}^{\infty}x^2\cdot\frac{1}{y}I_{(0<x<y)}\,dx = \frac{1}{y}\int_0^y x^2\,dx = \frac{1}{3}y^2,
$$

so $$E(X^2 \mid Y) = \frac{1}{3}Y^2$$. Then $$\mathrm{Var}(X \mid Y) = E(X^2 \mid Y) - \{E(X \mid Y)\}^2 = \frac{1}{3}Y^2 - \bigl(\frac{1}{2}Y\bigr)^2 = \frac{1}{12}Y^2$$.

**(d)** From the marginal pdf of $$Y$$ we first find $$E(Y)$$ and $$\mathrm{Var}(Y)$$. $$E(Y) = \int_{-\infty}^{\infty}y f_2(y)\,dy = \int_0^{\infty}y^2e^{-y}\,dy = 2$$ and $$E(Y^2) = \int_{-\infty}^{\infty}y^2f_2(y)\,dy = \int_0^{\infty}y^3e^{-y}\,dy = 6$$. So $$\mathrm{Var}(Y) = E(Y^2) - \{E(Y)\}^2 = 2$$. Therefore

$$
\mathrm{Var}\bigl(E(X \mid Y)\bigr) = \mathrm{Var}\bigl(\tfrac{1}{2}Y\bigr) = \tfrac{1}{4}\mathrm{Var}(Y) = \frac{1}{2}, \qquad E\bigl(\mathrm{Var}(X \mid Y)\bigr) = E\bigl(\tfrac{1}{12}Y^2\bigr) = \frac{1}{2}.
$$

**(e)** For the marginal pdf $$f_1(x)$$ of $$X$$, $$f_1(x) = \int_{-\infty}^{\infty}e^{-y}I_{(0<x<y<\infty)}\,dy = \int_x^{\infty}e^{-y}\,dy\ I_{(x>0)} = e^{-x}I_{(x>0)}$$. Also $$\mathrm{Var}(X) = E(\mathrm{Var}(X \mid Y)) + \mathrm{Var}(E(X \mid Y)) = \frac{1}{2} + \frac{1}{2} = 1$$.

### Exercise 2.10

> **Exercise 2.10.** Find $$\mathrm{Var}[E(X \mid Y)]$$ and $$E[\mathrm{Var}(X \mid Y)]$$ when the joint pdf of $$X$$ and $$Y$$ is (a) $$f_{1,2}(x, y) = 2I_{(0<x<y<1)}$$, (b) $$f_{1,2}(x, y) = x\,e^{-y}I_{(0<x<y<\infty)}$$.
{: .problem #hw3-2-10 }

**(a)** For the joint pdf $$f_{1,2}(x, y) = 2I_{(0<x<y<1)}$$, to find $$\mathrm{Var}(E(X \mid Y))$$ and $$E(\mathrm{Var}(X \mid Y))$$ we first find the marginal pdf $$f_2(y)$$ of $$Y$$: $$f_2(y) = \int_{-\infty}^{\infty}2I_{(0<x<y<1)}\,dx = I_{(0<y<1)}\int_0^y 2\,dx = 2y\,I_{(0<y<1)}$$. So for $$y$$ with $$0 < y < 1$$, $$f_{1 \mid 2}(x \mid y) = \dfrac{2I_{(0<x<y<1)}}{2y\,I_{(0<y<1)}} = \dfrac{1}{y}I_{(0<x<y)}$$. Then, given $$Y = y$$ ($$0 < y < 1$$),

$$
E(X \mid Y = y) = \int_{-\infty}^{\infty}x\cdot\frac{1}{y}I_{(0<x<y)}\,dx = \int_0^y\frac{x}{y}\,dx = \frac{1}{2}y, \qquad\text{so } E(X \mid Y) = \tfrac{1}{2}Y.
$$

Also $$E(X^2 \mid Y = y) = \int_{-\infty}^{\infty}x^2\cdot\frac{1}{y}I_{(0<x<y)}\,dx = \int_0^y\frac{x^2}{y}\,dx = \frac{1}{3}y^2$$, so $$E(X^2 \mid Y) = \frac{1}{3}Y^2$$ and $$\mathrm{Var}(X \mid Y) = E(X^2 \mid Y) - \{E(X \mid Y)\}^2 = \frac{1}{12}Y^2$$. Moreover, $$E(Y) = \int_{-\infty}^{\infty}y f_2(y)\,dy = \int_0^1 2y^2\,dy = \frac{2}{3}$$ and $$E(Y^2) = \int_0^1 2y^3\,dy = \frac{1}{2}$$, so $$\mathrm{Var}(Y) = E(Y^2) - \{E(Y)\}^2 = \frac{1}{18}$$. Therefore

$$
E\bigl(\mathrm{Var}(X \mid Y)\bigr) = E\bigl(\tfrac{1}{12}Y^2\bigr) = \frac{1}{24}, \qquad \mathrm{Var}\bigl(E(X \mid Y)\bigr) = \mathrm{Var}\bigl(\tfrac{1}{2}Y\bigr) = \frac{1}{72}.
$$

**(b)** For the joint pdf $$f_{1,2}(x, y) = x\,e^{-y}I_{(0<x<y<\infty)}$$, first the marginal pdf of $$Y$$: $$f_2(y) = \int_{-\infty}^{\infty}x\,e^{-y}I_{(0<x<y<\infty)}\,dx = I_{(y>0)}\int_0^y x\,e^{-y}\,dx = \frac{1}{2}y^2e^{-y}I_{(y>0)}$$. So for $$y > 0$$, $$f_{1 \mid 2}(x \mid y) = \dfrac{x\,e^{-y}I_{(0<x<y<\infty)}}{\frac{1}{2}y^2e^{-y}I_{(y>0)}} = \dfrac{2x}{y^2}I_{(0<x<y)}$$. Then, given $$Y = y$$ ($$y > 0$$),

$$
E(X \mid Y = y) = \int_{-\infty}^{\infty}x\,f_{1 \mid 2}(x \mid y)\,dx = \int_0^y\frac{2x^2}{y^2}\,dx = \frac{2}{3}y, \qquad\text{so } E(X \mid Y) = \tfrac{2}{3}Y,
$$

and $$E(X^2 \mid Y = y) = \int_0^y\frac{2x^3}{y^2}\,dx = \frac{1}{2}y^2$$, so $$E(X^2 \mid Y) = \frac{1}{2}Y^2$$ and $$\mathrm{Var}(X \mid Y) = E(X^2 \mid Y) - \{E(X \mid Y)\}^2 = \frac{1}{18}Y^2$$. Also, $$E(Y) = \int_{-\infty}^{\infty}y f_2(y)\,dy = \int_0^{\infty}\frac{1}{2}y^3e^{-y}\,dy = 3$$ and $$E(Y^2) = \int_0^{\infty}\frac{1}{2}y^4e^{-y}\,dy = 12$$, so $$\mathrm{Var}(Y) = E(Y^2) - \{E(Y)\}^2 = 3$$. Therefore

$$
E\bigl(\mathrm{Var}(X \mid Y)\bigr) = E\bigl(\tfrac{1}{18}Y^2\bigr) = \frac{2}{3}, \qquad \mathrm{Var}\bigl(E(X \mid Y)\bigr) = \mathrm{Var}\bigl(\tfrac{2}{3}Y\bigr) = \frac{4}{3}.
$$

### Exercise 2.11

> **Exercise 2.11.** Find $$\mathrm{Var}[Y + X - E(X \mid Y)]$$ when the joint pdf of $$X$$ and $$Y$$ is (a) $$f_{1,2}(x, y) = 2I_{(0<x<y<1)}$$, (b) $$f_{1,2}(x, y) = 10xy^2I_{(0<x<y<1)}$$.
{: .problem #hw3-2-11 }

Since $$\mathrm{Cov}(Y, X - E(X \mid Y)) = 0$$,

$$
\mathrm{Var}\bigl(Y + X - E(X \mid Y)\bigr) = \mathrm{Var}(Y) + 2\,\mathrm{Cov}\bigl(Y, X - E(X \mid Y)\bigr) + \mathrm{Var}\bigl(X - E(X \mid Y)\bigr) = \mathrm{Var}(Y) + \mathrm{Var}\bigl(X - E(X \mid Y)\bigr),
$$

so it suffices to find $$\mathrm{Var}(Y)$$ and $$\mathrm{Var}(X - E(X \mid Y))$$. Also, $$E(X - E(X \mid Y)) = E(X) - E(E(X \mid Y)) = 0$$, so

$$
\mathrm{Var}\bigl(Y + X - E(X \mid Y)\bigr) = \mathrm{Var}(Y) + E\bigl((X - E(X \mid Y))^2\bigr) = \mathrm{Var}(Y) + E\bigl(\mathrm{Var}(X \mid Y)\bigr).
$$

**(a)** From 2-10 (a), $$\mathrm{Var}(Y) = \frac{1}{18}$$ and $$E(\mathrm{Var}(X \mid Y)) = \frac{1}{24}$$, so $$\mathrm{Var}(Y + X - E(X \mid Y)) = \frac{1}{18} + \frac{1}{24} = \frac{7}{72}$$.

**(b)** From 2-8, $$\mathrm{Var}(Y) = \frac{5}{252}$$ and $$E(\mathrm{Var}(X \mid Y)) = \frac{5}{126}$$, so $$\mathrm{Var}(Y + X - E(X \mid Y)) = \frac{5}{252} + \frac{5}{126} = \frac{5}{84}$$.

### Exercise 2.12

> **Exercise 2.12.** For a one-dimensional random variable $$Y$$ and a $$k$$-dimensional random variable $$X = (X_1, \dots, X_k)^t$$, write $$\mu_2 = E(Y)$$, $$\sigma_{22} = \mathrm{Var}(Y)$$, $$\mu_1 = E(X)$$, $$\Sigma_{11} = \mathrm{Var}(X)$$, $$\sigma_{21} = \mathrm{Cov}(Y, X)$$. When $$\sigma_{22} > 0$$ and the inverse $$\Sigma_{11}^{-1}$$ of $$\Sigma_{11}$$ exists, answer the following.
>
> - **(a)** For an arbitrary constant vector $$c$$ and real number $$d$$, show that $$\mathrm{Cov}\bigl(Y - \mu_2 - \sigma_{21}\Sigma_{11}^{-1}(X - \mu_1),\ c^tX + d\bigr) = 0$$.
> - **(b)** Show that the least squares linear predictor minimizing the mean squared prediction error $$E[\{Y - (a^tX + b)\}^2]$$ when $$Y$$ is predicted by a real-valued linear function $$a^tX + b$$ of $$X$$ is given by $$\mu_2 + \sigma_{21}\Sigma_{11}^{-1}(X - \mu_1)$$.
> - **(c)** Show that $$\max_{a,b}\mathrm{Corr}(Y, a^tX + b) = \bigl(\frac{\sigma_{21}\Sigma_{11}^{-1}\sigma_{12}}{\sigma_{22}}\bigr)^{1/2} = \mathrm{Corr}\bigl(Y, \mu_2 + \sigma_{21}\Sigma_{11}^{-1}(X - \mu_1)\bigr)$$. The correlation coefficient on the right side is called the multiple correlation coefficient between $$Y$$ and $$X = (X_1, \dots, X_k)^t$$, written $$\rho_{Y;X_1,\dots,X_k}$$.
> - **(d)** Show that $$\mathrm{Var}\bigl(Y - \mu_2 - \sigma_{21}\Sigma_{11}^{-1}(X - \mu_1)\bigr) = (1 - \rho^2_{Y;X_1,\dots,X_k})\,\sigma_{22}$$. From this equation, if the least squares linear predictor $$\mu_2 + \sigma_{21}\Sigma_{11}^{-1}(X - \mu_1)$$ is used as the center of the distribution of $$Y$$, the spread $$\sigma_{22}$$ of $$Y$$ can be reduced by $$100 \times \rho^2_{Y;X_1,\dots,X_k}$$ (%). In this sense $$\rho^2_{Y;X_1,\dots,X_k}$$ is called the coefficient of determination.
{: .problem #hw3-2-12 }

**(a)** For an arbitrary constant vector $$c$$ and real number $$d$$ we want to prove $$\mathrm{Cov}(Y - \mu_2 - \sigma_{21}\Sigma_{11}^{-1}(X - \mu_1),\ c^tX + d) = 0$$. By the properties of the covariance matrix,

$$
\begin{aligned}
\mathrm{Cov}\bigl(Y - \mu_2 - \sigma_{21}\Sigma_{11}^{-1}(X - \mu_1),\ c^tX + d\bigr) &= \mathrm{Cov}\bigl(Y - \sigma_{21}\Sigma_{11}^{-1}X,\ X\bigr)c \\
&= \bigl(\mathrm{Cov}(Y, X) - \mathrm{Cov}(\sigma_{21}\Sigma_{11}^{-1}X, X)\bigr)c \\
&= \sigma_{21}c - \sigma_{21}\Sigma_{11}^{-1}\mathrm{Cov}(X, X)c = \sigma_{21}c - \sigma_{21}\Sigma_{11}^{-1}\Sigma_{11}c = \sigma_{21}c - \sigma_{21}c = 0.
\end{aligned}
$$

**(b)** We want to prove that the least squares linear predictor of $$Y$$ is $$\mu_2 + \sigma_{21}\Sigma_{11}^{-1}(X - \mu_1)$$. Write $$L = \mu_2 + \sigma_{21}\Sigma_{11}^{-1}(X - \mu_1)$$. Then

$$
\begin{aligned}
E\bigl\{(Y - (a^tX + b))^2\bigr\} &= E\bigl((Y - L) + (L - a^tX - b)\bigr)^2 \\
&= E(Y - L)^2 + E(L - a^tX - b)^2 + 2E\bigl((Y - L)(L - a^tX - b)\bigr) \\
&= E(Y - L)^2 + E\bigl((\sigma_{21}\Sigma_{11}^{-1} - a^t)X + \mu_2 - \sigma_{21}\Sigma_{11}^{-1}\mu_1 - b\bigr)^2 + 2\,\mathrm{Cov}\bigl(Y - L,\ (\sigma_{21}\Sigma_{11}^{-1} - a^t)X + \mu_2 - \sigma_{21}\Sigma_{11}^{-1}\mu_1 - b\bigr),
\end{aligned}
$$

and by (a), the covariance is $$0$$. Therefore $$E\{(Y - a^tX - b)^2\} = E((Y - L)^2) + E((L - a^tX - b)^2) \ge E((Y - L)^2)$$. Therefore $$\mu_2 + \sigma_{21}\Sigma_{11}^{-1}(X - \mu_1)$$ is the least squares linear predictor of $$Y$$.

**(c)** Using $$\mathrm{Corr}(Y, a^tX + b) = \dfrac{\mathrm{Cov}(Y, a^tX + b)}{\sqrt{\mathrm{Var}(Y)}\sqrt{\mathrm{Var}(a^tX + b)}}$$ we find the multiple correlation coefficient, that is, the maximum of $$\mathrm{Corr}(Y, a^tX + b)$$. Since $$\mathrm{Cov}(Y, a^tX + b) = \mathrm{Cov}(Y, X)a = \sigma_{21}a$$ and $$\mathrm{Var}(a^tX + b) = a^t\Sigma_{11}a$$,

$$
\mathrm{Corr}(Y, a^tX + b) = \frac{\sigma_{21}a}{\sqrt{\sigma_{22}}\sqrt{a^t\Sigma_{11}a}}.
$$

Then $$(\sigma_{21}a)^2 = a^t\sigma_{21}^t\sigma_{21}a$$, so $$\bigl(\mathrm{Corr}(Y, a^tX + b)\bigr)^2 = \dfrac{a^t\sigma_{21}^t\sigma_{21}a}{\sigma_{22}\,a^t\Sigma_{11}a}$$. Consider the constant vector $$p$$ with $$p^tp = a^t\Sigma_{11}a$$, in other words $$p = \Sigma_{11}^{1/2}a$$. Since $$\Sigma_{11}^t = \Sigma_{11}$$ and $$(\Sigma_{11}^{1/2})^t = \Sigma_{11}^{1/2}$$, we have $$a^t = p^t\Sigma_{11}^{-1/2}$$. Hence

$$
\bigl[\mathrm{Corr}(Y, a^tX + b)\bigr]^2 = \frac{(\sigma_{21}a)^2}{\sigma_{22}\,a^t\Sigma_{11}a} = \frac{(\sigma_{21}\Sigma_{11}^{-1/2}p)^2}{\sigma_{22}\,p^tp} = \frac{1}{\sigma_{22}}\cdot\frac{p^t\Sigma_{11}^{-1/2}\sigma_{12}\,\sigma_{21}\Sigma_{11}^{-1/2}p}{p^tp}.
$$

The numerator is a real number, so it equals its trace, and since $$\Sigma_{11}^{-1/2}\sigma_{12}\sigma_{21}\Sigma_{11}^{-1/2}$$ is a matrix of rank one, its largest eigenvalue is its trace, $$\mathrm{tr}(\sigma_{21}\Sigma_{11}^{-1/2}\Sigma_{11}^{-1/2}\sigma_{12}) = \sigma_{21}\Sigma_{11}^{-1}\sigma_{12}$$. Therefore

$$
\bigl[\mathrm{Corr}(Y, a^tX + b)\bigr]^2 \le \frac{\sigma_{21}\Sigma_{11}^{-1}\sigma_{12}}{\sigma_{22}}, \qquad\text{that is,}\qquad \mathrm{Corr}(Y, a^tX + b) \le \Bigl(\frac{\sigma_{21}\Sigma_{11}^{-1}\sigma_{12}}{\sigma_{22}}\Bigr)^{1/2}.
$$

Also, with $$L = \mu_2 + \sigma_{21}\Sigma_{11}^{-1}(X - \mu_1)$$, by (a) $$\mathrm{Cov}(Y, L) = \mathrm{Var}(L)$$, and $$\mathrm{Var}(L) = (\sigma_{21}\Sigma_{11}^{-1})\mathrm{Var}(X)(\sigma_{21}\Sigma_{11}^{-1})^t = \sigma_{21}\Sigma_{11}^{-1}\sigma_{12}$$, so

$$
\mathrm{Corr}(Y, L) = \frac{\mathrm{Cov}(Y, L)}{\sqrt{\mathrm{Var}(Y)}\sqrt{\mathrm{Var}(L)}} = \frac{\mathrm{Var}(L)}{\sqrt{\sigma_{22}}\sqrt{\mathrm{Var}(L)}} = \Bigl(\frac{\sigma_{21}\Sigma_{11}^{-1}\sigma_{12}}{\sigma_{22}}\Bigr)^{1/2},
$$

so the bound is attained and the given equality holds.

**Correction.** In the chain after "$$(\sigma_{21}a)^2$$" the original wrote the numerator as $$\mathrm{tr}(p^t\sigma_{12}\Sigma_{11}^{-1}\sigma_{21}p)$$, which does not multiply as matrices ($$\sigma_{12}$$ is a $$k \times 1$$ vector and $$\Sigma_{11}^{-1}$$ is $$k \times k$$). The correct matrix between $$p^t$$ and $$p$$ is $$\Sigma_{11}^{-1/2}\sigma_{12}\sigma_{21}\Sigma_{11}^{-1/2}$$; the trace argument is kept, and its trace is $$\sigma_{21}\Sigma_{11}^{-1}\sigma_{12}$$, as above.

**(d)** From (c), $$\mathrm{Corr}(Y, L) = \rho_{Y;X_1,\dots,X_k}$$, that is, $$\dfrac{\mathrm{Cov}(Y, L)}{\sqrt{\mathrm{Var}(Y)}\sqrt{\mathrm{Var}(L)}} = \rho_{Y;X_1,\dots,X_k}$$. Then

$$
\mathrm{Var}(Y - L) = \mathrm{Var}(Y) - 2\,\mathrm{Cov}(Y, L) + \mathrm{Var}(L) = \sigma_{22} - 2\rho_{Y;X_1,\dots,X_k}\sqrt{\sigma_{22}}\sqrt{\mathrm{Var}(L)} + \mathrm{Var}(L).
$$

Also $$\mathrm{Var}(L) = \sigma_{21}\Sigma_{11}^{-1}\sigma_{12}$$, and by (c) $$\sqrt{\mathrm{Var}(L)} = \rho_{Y;X_1,\dots,X_k}\sqrt{\sigma_{22}}$$. Therefore

$$
\mathrm{Var}(Y - L) = \sigma_{22} - 2\sigma_{22}\rho^2_{Y;X_1,\dots,X_k} + \sigma_{22}\rho^2_{Y;X_1,\dots,X_k} = \sigma_{22}\bigl(1 - \rho^2_{Y;X_1,\dots,X_k}\bigr).
$$

### Exercise 2.13

> **Exercise 2.13.** In each case determine whether $$X$$ and $$Y$$ are independent when their joint pdf is given, and find the covariance of $$X$$ and $$Y$$ when they are not independent.
>
> - **(a)** $$f_{1,2}(x, y) = 2e^{-x-2y}I_{(x>0,\,y>0)}$$
> - **(b)** $$f_{1,2}(x, y) = 2e^{-x-y}I_{(0<x<y)}$$
> - **(c)** $$f_{1,2}(x, y) = \dfrac{25}{104}(1 + x^4y^4)I_{(-1 \le x \le 1,\,-1 \le y \le 1)}$$
> - **(d)** $$f_{1,2}(x, y) = (1/6)^x(1/3)^y(1/2)^{1-x-y}$$, $$x, y = 0, 1$$, $$x + y = 0, 1$$
{: .problem #hw3-2-13 }

**(a)** Let us find the marginal pdf of each of $$X$$ and $$Y$$ and decide whether they are independent. $$f_1(x) = \int_{-\infty}^{\infty}f_{1,2}(x, y)\,dy = \int_0^{\infty}2e^{-x-2y}\,dy\ I_{(x>0)} = e^{-x}I_{(x>0)}$$ and $$f_2(y) = \int_{-\infty}^{\infty}f_{1,2}(x, y)\,dx = \int_0^{\infty}2e^{-x-2y}\,dx\ I_{(y>0)} = 2e^{-2y}I_{(y>0)}$$. Therefore, for all real $$x, y$$, $$f_{1,2}(x, y) = 2e^{-x-2y}I_{(x>0,\,y>0)} = e^{-x}I_{(x>0)}\cdot 2e^{-2y}I_{(y>0)} = f_1(x)f_2(y)$$, so $$X$$ and $$Y$$ are independent.

**(b)** $$f_1(x) = \int_{-\infty}^{\infty}f_{1,2}(x, y)\,dy = \int_x^{\infty}2e^{-x-y}\,dy\ I_{(x>0)} = 2e^{-2x}I_{(x>0)}$$ and $$f_2(y) = \int_{-\infty}^{\infty}f_{1,2}(x, y)\,dx = \int_0^y 2e^{-x-y}\,dx\ I_{(y>0)} = 2e^{-y}(1 - e^{-y})I_{(y>0)}$$. Then there are real numbers $$x, y$$ with $$f_{1,2}(x, y) \ne f_1(x)f_2(y)$$, so $$X$$ and $$Y$$ are not independent. Then

$$
E(XY) = \int_{-\infty}^{\infty}\int_{-\infty}^{\infty}xy\,f_{1,2}(x, y)\,dx\,dy = \int_0^{\infty}\int_x^{\infty}2xy\,e^{-x-y}\,dy\,dx = \int_0^{\infty}2x(1 + x)e^{-2x}\,dx = 1,
$$

and $$E(X) = \int_{-\infty}^{\infty}x f_1(x)\,dx = \int_0^{\infty}2x\,e^{-2x}\,dx = \frac{1}{2}$$, $$E(Y) = \int_{-\infty}^{\infty}y f_2(y)\,dy = \int_0^{\infty}(2y\,e^{-y} - 2y\,e^{-2y})\,dy = \frac{3}{2}$$. Therefore $$\mathrm{Cov}(X, Y) = E(XY) - E(X)E(Y) = 1 - \frac{1}{2}\times\frac{3}{2} = \frac{1}{4}$$.

**(c)** $$f_1(x) = \int_{-\infty}^{\infty}f_{1,2}(x, y)\,dy = \int_{-1}^{1}\frac{25}{104}(1 + x^4y^4)\,dy\ I_{(-1 \le x \le 1)} = \frac{10}{104}(x^4 + 5)I_{(-1 \le x \le 1)}$$ and $$f_2(y) = \int_{-1}^{1}\frac{25}{104}(1 + x^4y^4)\,dx\ I_{(-1 \le y \le 1)} = \frac{10}{104}(y^4 + 5)I_{(-1 \le y \le 1)}$$. Then there are real numbers $$x, y$$ with $$f_{1,2}(x, y) \ne f_1(x)f_2(y)$$, so $$X$$ and $$Y$$ are not independent. Then

$$
E(XY) = \int_{-\infty}^{\infty}\int_{-\infty}^{\infty}xy\,f_{1,2}(x, y)\,dx\,dy = \int_{-1}^{1}\int_{-1}^{1}\frac{25}{104}xy(1 + x^4y^4)\,dx\,dy = 0,
$$

and $$E(X) = \int_{-\infty}^{\infty}x f_1(x)\,dx = \int_{-1}^{1}\frac{10}{104}x(x^4 + 5)\,dx = 0$$, $$E(Y) = \int_{-1}^{1}\frac{10}{104}y(y^4 + 5)\,dy = 0$$. Therefore $$\mathrm{Cov}(X, Y) = E(XY) - E(X)E(Y) = 0$$.

**(d)** The given joint pdf is the pdf of a discrete random variable. Since $$f_{1,2}(0, 0) = \frac{1}{2}$$, $$f_{1,2}(0, 1) = \frac{1}{3}$$, $$f_{1,2}(1, 0) = \frac{1}{6}$$, the marginal pdf of $$X$$ is $$f_1(x) = \bigl(\frac{5}{6}\bigr)^{1-x}\bigl(\frac{1}{6}\bigr)^x$$ ($$x = 0, 1$$) and that of $$Y$$ is $$f_2(y) = \bigl(\frac{2}{3}\bigr)^{1-y}\bigl(\frac{1}{3}\bigr)^y$$ ($$y = 0, 1$$). Therefore, at $$x = 0$$, $$y = 0$$, $$f_1(0)f_2(0) = \frac{5}{6}\times\frac{2}{3} = \frac{5}{9} \ne f_{1,2}(0, 0) = \frac{1}{2}$$, so $$X$$ and $$Y$$ are not independent. Then $$E(XY) = 0\times 0\times\frac{1}{2} + 0\times 1\times\frac{1}{3} + 1\times 0\times\frac{1}{6} = 0$$, $$E(X) = \frac{5}{6}\times 0 + \frac{1}{6}\times 1 = \frac{1}{6}$$, $$E(Y) = \frac{2}{3}\times 0 + \frac{1}{3}\times 1 = \frac{1}{3}$$. Therefore $$\mathrm{Cov}(X, Y) = E(XY) - E(X)E(Y) = 0 - \frac{1}{6}\times\frac{1}{3} = -\frac{1}{18}$$.

### Exercise 2.14

> **Exercise 2.14.** The joint pdf of $$X$$ and $$Y$$ is $$f_{1,2}(x, y) = 6e^{-x-2y}I_{(0<x<y<\infty)}$$. Answer the following. (a) Find the joint moment generating function $$mgf_{1,2}(t_1, t_2)$$ of $$X$$ and $$Y$$. (b) Find the variance of $$X + Y$$. (c) Find the joint moment generating function $$M_{X,Z}(s, t)$$ of $$X$$ and $$Z = Y - X$$, and decide whether $$X$$ and $$Z$$ are independent.
{: .problem #hw3-2-14 }

**(a)** The joint mgf of $$X$$ and $$Y$$ is $$mgf_{1,2}(t_1, t_2) = E(e^{t_1X + t_2Y})$$, so it can be found as follows:

$$
mgf_{1,2}(t_1, t_2) = \int_{-\infty}^{\infty}\int_{-\infty}^{\infty}e^{t_1x + t_2y}f_{1,2}(x, y)\,dx\,dy = \int_0^{\infty}\int_x^{\infty}6e^{(t_1 - 1)x + (t_2 - 2)y}\,dy\,dx = \frac{1}{1 - \frac{1}{2}t_2}\cdot\frac{1}{1 - \frac{1}{3}(t_1 + t_2)},
$$

and the mgf is defined, the integral converging, for $$t_2 < 2$$, $$t_1 + t_2 < 3$$.

**(b)** For $$t_2 < 2$$, $$t_1 + t_2 < 3$$, the joint cumulant generating function is $$cgf_{1,2}(t_1, t_2) = \log mgf_{1,2}(t_1, t_2) = -\log\bigl(1 - \frac{1}{2}t_2\bigr) - \log\bigl(1 - \frac{1}{3}(t_1 + t_2)\bigr)$$, so

$$
cgf_{1,2}(t_1, t_2) = \tfrac{1}{2}t_2 + \tfrac{1}{2}\bigl(\tfrac{1}{2}t_2\bigr)^2 + o(t_2^2) + \tfrac{1}{3}(t_1 + t_2) + \tfrac{1}{2}\bigl(\tfrac{1}{3}(t_1 + t_2)\bigr)^2 + o\bigl((t_1 + t_2)^2\bigr) = \tfrac{1}{3}t_1 + \tfrac{5}{6}t_2 + \tfrac{1}{18}t_1^2 + \tfrac{1}{9}t_1t_2 + \tfrac{13}{72}t_2^2 + o\bigl((t_1 + t_2)^2\bigr).
$$

Then $$\mathrm{Var}(X + Y) = \mathrm{Var}(X) + 2\,\mathrm{Cov}(X, Y) + \mathrm{Var}(Y)$$, and $$\dfrac{\mathrm{Var}(X)}{2!} = \dfrac{1}{18}$$, $$\dfrac{\mathrm{Cov}(X, Y)}{1!\,1!} = \dfrac{1}{9}$$, $$\dfrac{\mathrm{Var}(Y)}{2!} = \dfrac{13}{72}$$, so $$\mathrm{Var}(X + Y) = \dfrac{1}{9} + 2\cdot\dfrac{1}{9} + \dfrac{13}{36} = \dfrac{25}{36}$$.

**(c)** The joint mgf of $$X$$ and $$Z = Y - X$$ is $$M_{X,Z}(s, t) = E(e^{sX + tZ}) = E(e^{sX + t(Y - X)}) = E(e^{(s-t)X + tY})$$, so for $$t < 2$$ and $$s < 3$$,

$$
M_{X,Z}(s, t) = E\bigl(e^{(s-t)X + tY}\bigr) = mgf_{1,2}(s - t, t) = \frac{1}{1 - \frac{t}{2}}\cdot\frac{1}{1 - \frac{s}{3}}.
$$

Now $$M_X(s) = E(e^{sX}) = \int_{-\infty}^{\infty}e^{sx}f_1(x)\,dx = \int_0^{\infty}e^{sx}\int_x^{\infty}6e^{-x-2y}\,dy\,dx = \dfrac{1}{1 - \frac{s}{3}}$$ ($$s < 3$$), and $$M_Z(t) = E(e^{tY - tX}) = \int_0^{\infty}\int_x^{\infty}6e^{ty - tx}e^{-x-2y}\,dy\,dx = \dfrac{1}{1 - \frac{t}{2}}$$ ($$t < 2$$). Therefore, for $$t < 2$$, $$s < 3$$, $$M_{X,Z}(s, t) = M_X(s)M_Z(t)$$, so $$X$$ and $$Z$$ are independent.

### Exercise 2.15

> **Exercise 2.15.** The joint pdf of $$X_1, X_2, X_3$$ is $$f_{1,2,3}(x_1, x_2, x_3) = 48x_1x_2x_3\,I_{(0<x_1<x_2<x_3<1)}$$. (a) Find the conditional pdf $$f_{1,2 \mid 3}(x_1, x_2 \mid z)$$ of $$X_1$$ and $$X_2$$ given $$X_3 = z$$. (b) Decide whether the three random variables $$X_1, X_2, X_3$$ are mutually independent.
{: .problem #hw3-2-15 }

**(a)** Given $$X_3 = z$$, $$f_{1,2 \mid 3}(x_1, x_2 \mid z) = \dfrac{f_{1,2,3}(x_1, x_2, z)}{f_3(z)}$$, so we find the marginal pdf of $$X_3$$ and then the conditional pdf. Then

$$
f_3(x_3) = \int_{-\infty}^{\infty}\int_{-\infty}^{\infty}f_{1,2,3}(x_1, x_2, x_3)\,dx_1\,dx_2 = I_{(0<x_3<1)}\int_0^{x_3}\int_0^{x_2}48x_1x_2x_3\,dx_1\,dx_2 = 6x_3^5\,I_{(0<x_3<1)}.
$$

Therefore, given $$X_3 = z$$ ($$0 < z < 1$$),

$$
f_{1,2 \mid 3}(x_1, x_2 \mid z) = \frac{48x_1x_2z\,I_{(0<x_1<x_2<z<1)}}{6z^5\,I_{(0<z<1)}} = \frac{8x_1x_2}{z^4}\,I_{(0<x_1<x_2<z)}.
$$

**(b)** We find the three marginal pdfs $$f_1(x_1)$$, $$f_2(x_2)$$, $$f_3(x_3)$$ and decide on independence. Then

$$
f_1(x_1) = \int_{x_1}^{1}\int_{x_2}^{1}48x_1x_2x_3\,dx_3\,dx_2\ I_{(0<x_1<1)} = \bigl(6x_1^5 - 12x_1^3 + 6x_1\bigr)I_{(0<x_1<1)}, \qquad f_2(x_2) = \int_{x_2}^{1}\int_0^{x_2}48x_1x_2x_3\,dx_1\,dx_3\ I_{(0<x_2<1)} = 12x_2^3(1 - x_2^2)\,I_{(0<x_2<1)},
$$

and from (a), $$f_3(x_3) = 6x_3^5I_{(0<x_3<1)}$$. Therefore there are $$x_1, x_2, x_3$$ with $$f_{1,2,3}(x_1, x_2, x_3) \ne f_1(x_1)f_2(x_2)f_3(x_3)$$, so the three random variables $$X_1, X_2, X_3$$ are not mutually independent.

### Exercise 2.16

> **Exercise 2.16.** The joint pdf of $$X_1, X_2, X_3$$ is $$f_{1,2,3}(x, y, z) = 90e^{-(x + 2y + 3z)}I_{(0<x<y<z<\infty)}$$. Answer the following. (a) Find the joint moment generating function $$mgf_{1,2,3}(t_1, t_2, t_3)$$ of the three random variables. (b) Find the variance matrix $$\mathrm{Var}(X)$$ of $$X = (X_1, X_2, X_3)^t$$. (c) Find the variance of $$X_1 + X_2 + X_3$$. (d) Decide whether $$X_1$$, $$X_2 - X_1$$, $$X_3 - X_2$$ are mutually independent.
{: .problem #hw3-2-16 }

**(a)** The joint mgf of the three random variables is $$mgf_{1,2,3}(t_1, t_2, t_3) = E(e^{t_1X_1 + t_2X_2 + t_3X_3})$$, so

$$
\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}e^{t_1x + t_2y + t_3z}f_{1,2,3}(x, y, z)\,dx\,dy\,dz = \int_0^{\infty}\int_x^{\infty}\int_y^{\infty}90e^{(t_1 - 1)x}e^{(t_2 - 2)y}e^{(t_3 - 3)z}\,dz\,dy\,dx = \frac{1}{1 - \frac{t_3}{3}}\cdot\frac{1}{1 - \frac{t_2 + t_3}{5}}\cdot\frac{1}{1 - \frac{t_1 + t_2 + t_3}{6}},
$$

for $$t_3 < 3$$, $$t_2 + t_3 < 5$$, $$t_1 + t_2 + t_3 < 6$$.

**(b)** We find the joint cumulant generating function from the joint mgf and use it to find the variance matrix. For $$t_3 < 3$$, $$t_2 + t_3 < 5$$, $$t_1 + t_2 + t_3 < 6$$,

$$
cgf_{1,2,3}(t_1, t_2, t_3) = -\log\Bigl(1 - \frac{t_3}{3}\Bigr) - \log\Bigl(1 - \frac{t_2 + t_3}{5}\Bigr) - \log\Bigl(1 - \frac{t_1 + t_2 + t_3}{6}\Bigr)
$$

$$
= \tfrac{1}{6}t_1 + \tfrac{11}{30}t_2 + \tfrac{7}{10}t_3 + \tfrac{1}{72}t_1^2 + \tfrac{61}{1800}t_2^2 + \tfrac{161}{1800}t_3^2 + \tfrac{1}{36}t_1t_2 + \tfrac{1}{36}t_3t_1 + \tfrac{61}{900}t_2t_3 + o\bigl((t_1 + t_2 + t_3)^2\bigr).
$$

That is, $$\dfrac{\mathrm{Var}(X_1)}{2!} = \dfrac{1}{72}$$, $$\dfrac{\mathrm{Var}(X_2)}{2!} = \dfrac{61}{1800}$$, $$\dfrac{\mathrm{Var}(X_3)}{2!} = \dfrac{161}{1800}$$, $$\dfrac{\mathrm{Cov}(X_1, X_2)}{1!\,1!} = \dfrac{1}{36}$$, $$\dfrac{\mathrm{Cov}(X_2, X_3)}{1!\,1!} = \dfrac{61}{900}$$, $$\dfrac{\mathrm{Cov}(X_1, X_3)}{1!\,1!} = \dfrac{1}{36}$$. Therefore the variance matrix is

$$
\mathrm{Var}(X) = \begin{pmatrix}\frac{1}{36} & \frac{1}{36} & \frac{1}{36} \\[0.3em] \frac{1}{36} & \frac{61}{900} & \frac{61}{900} \\[0.3em] \frac{1}{36} & \frac{61}{900} & \frac{161}{900}\end{pmatrix}.
$$

**(c)** We find $$\mathrm{Var}(X_1 + X_2 + X_3)$$ using $$X_1 + X_2 + X_3 = (1\ 1\ 1)\begin{pmatrix}X_1 \\ X_2 \\ X_3\end{pmatrix}$$. Let $$\mathbf{1} = \begin{pmatrix}1 \\ 1 \\ 1\end{pmatrix}$$; then $$X_1 + X_2 + X_3 = \mathbf{1}^tX$$, so $$\mathrm{Var}(X_1 + X_2 + X_3) = \mathrm{Var}(\mathbf{1}^tX) = \mathbf{1}^t\mathrm{Var}(X)\mathbf{1} = \dfrac{469}{900}$$.

**(d)** Consider $$X_2 - X_1 = Y$$ and $$X_3 - X_2 = Z$$ as new random variables. If the joint mgf of $$X_1, Y, Z$$ is $$M(s, t, u)$$, then

$$
M(s, t, u) = E\bigl(e^{sX_1 + tY + uZ}\bigr) = E\bigl(e^{sX_1 + t(X_2 - X_1) + u(X_3 - X_2)}\bigr) = E\bigl(e^{(s-t)X_1 + (t-u)X_2 + uX_3}\bigr) = \frac{1}{1 - \frac{u}{3}}\cdot\frac{1}{1 - \frac{t}{5}}\cdot\frac{1}{1 - \frac{s}{6}} \qquad (s < 6,\ t < 5,\ u < 3).
$$

Then $$M_{X_1}(s) = E(e^{sX_1}) = \int_0^{\infty}e^{sx}\int_x^{\infty}\int_y^{\infty}90e^{-x-2y-3z}\,dz\,dy\,dx = \dfrac{1}{1 - \frac{s}{6}}$$ ($$s < 6$$), $$M_Y(t) = E(e^{tX_2 - tX_1}) = \dfrac{1}{1 - \frac{t}{5}}$$ ($$t < 5$$), and $$M_Z(u) = E(e^{uX_3 - uX_2}) = \dfrac{1}{1 - \frac{u}{3}}$$ ($$u < 3$$). Therefore, for $$s < 6$$, $$t < 5$$, $$u < 3$$, $$M(s, t, u) = M_{X_1}(s)M_Y(t)M_Z(u)$$. Therefore $$X_1, Y, Z$$, that is, $$X_1$$, $$X_2 - X_1$$, $$X_3 - X_2$$, are mutually independent.

### Exercise 2.17

> **Exercise 2.17.** The joint pdf of $$X_1, X_2, X_3$$ is $$f_{1,2,3}(x, y, z) = 90e^{-(x + 2y + 3z)}I_{(0<x<y<z<\infty)}$$. Answer the following. (a) Find the conditional pdf $$f_{2,3 \mid 1}(x_2, x_3 \mid x)$$ of $$X_2$$ and $$X_3$$ given $$X_1 = x$$. (b) For $$Y = (X_2, X_3)^t$$, find $$E(Y \mid X_1)$$ and $$\mathrm{Var}(Y \mid X_1)$$. (c) For $$Y = (X_2, X_3)^t$$, find $$\mathrm{Var}[E(Y \mid X_1)]$$ and $$E[\mathrm{Var}(Y \mid X_1)]$$.
{: .problem #hw3-2-17 }

**(a)** The conditional pdf of $$X_2$$ and $$X_3$$ given $$X_1 = x$$ is $$f_{2,3 \mid 1}(y, z \mid x) = \dfrac{f_{1,2,3}(x, y, z)}{f_1(x)}$$ ($$f_1(x) \ne 0$$). Then $$f_1(x) = \int_{-\infty}^{\infty}\int_{-\infty}^{\infty}f_{1,2,3}(x, y, z)\,dy\,dz = I_{(x>0)}\int_x^{\infty}\int_y^{\infty}90e^{-x-2y-3z}\,dz\,dy = 6e^{-6x}I_{(x>0)}$$. Therefore, for a real number $$x > 0$$, given $$X_1 = x$$,

$$
f_{2,3 \mid 1}(y, z \mid x) = \frac{90e^{-x-2y-3z}I_{(0<x<y<z)}}{6e^{-6x}I_{(x>0)}} = 15e^{5x-2y-3z}\,I_{(x<y<z)}.
$$

**(b)** For a real number $$x > 0$$, given $$X_1 = x$$, the conditional cumulant generating function is $$cgf_{2,3 \mid 1}(t, s) = \log mgf_{2,3 \mid 1}(t, s) = \log E(e^{tX_2 + sX_3} \mid X_1 = x)$$, so

$$
\log\Bigl(\int\!\!\int e^{ty + sz}f_{2,3 \mid 1}(y, z \mid x)\,dy\,dz\Bigr) = \log\Bigl(15e^{5x}\int_x^{\infty}\int_y^{\infty}e^{(t-2)y}e^{(s-3)z}\,dz\,dy\Bigr) = \log\Bigl(e^{(t+s)x}\frac{1}{1 - \frac{s}{3}}\frac{1}{1 - \frac{s+t}{5}}\Bigr) \qquad (s < 3,\ s + t < 5).
$$

In other words, for $$s < 3$$ and $$s + t < 5$$,

$$
cgf_{2,3 \mid 1}(t, s) = (t + s)x - \log\Bigl(1 - \frac{s}{3}\Bigr) - \log\Bigl(1 - \frac{s+t}{5}\Bigr) = \Bigl(\frac{1}{5} + x\Bigr)t + \Bigl(\frac{8}{15} + x\Bigr)s + \frac{1}{50}t^2 + \frac{1}{25}st + \frac{17}{225}s^2 + o\bigl((s + t)^2\bigr).
$$

Therefore $$E(X_2 \mid X_1 = x) = \frac{1}{5} + x$$, $$E(X_3 \mid X_1 = x) = \frac{8}{15} + x$$, $$\dfrac{\mathrm{Var}(X_2 \mid X_1 = x)}{2!} = \dfrac{1}{50}$$, $$\dfrac{\mathrm{Var}(X_3 \mid X_1 = x)}{2!} = \dfrac{17}{225}$$, $$\dfrac{\mathrm{Cov}(X_2, X_3 \mid X_1 = x)}{1!\,1!} = \dfrac{1}{25}$$. That is,

$$
E(Y \mid X_1 = x) = \begin{pmatrix}\frac{1}{5} + x \\[0.3em] \frac{8}{15} + x\end{pmatrix}, \qquad \mathrm{Var}(Y \mid X_1 = x) = \begin{pmatrix}\frac{1}{25} & \frac{1}{25} \\[0.3em] \frac{1}{25} & \frac{34}{225}\end{pmatrix},
$$

so $$E(Y \mid X_1) = \begin{pmatrix}\frac{1}{5} + X_1 \\ \frac{8}{15} + X_1\end{pmatrix}$$ and $$\mathrm{Var}(Y \mid X_1) = \begin{pmatrix}\frac{1}{25} & \frac{1}{25} \\ \frac{1}{25} & \frac{34}{225}\end{pmatrix}$$.

**(c)** From the joint cumulant generating function $$cgf_{1,2,3}(t_1, t_2, t_3) = \frac{1}{6}t_1 + \frac{11}{30}t_2 + \frac{7}{10}t_3 + \frac{1}{72}t_1^2 + \frac{61}{1800}t_2^2 + \frac{161}{1800}t_3^2 + \frac{1}{36}t_1t_2 + \frac{1}{36}t_3t_1 + \frac{61}{900}t_2t_3 + o\bigl((t_1 + t_2 + t_3)^2\bigr)$$ in 2.16 (b), we can find $$\mathrm{Var}(E(Y \mid X_1))$$ and $$E(\mathrm{Var}(Y \mid X_1))$$. Then

$$
\mathrm{Var}\bigl(E(Y \mid X_1)\bigr) = \mathrm{Var}\Bigl(\begin{pmatrix}\frac{1}{5} + X_1 \\ \frac{8}{15} + X_1\end{pmatrix}\Bigr) = \mathrm{Var}\begin{pmatrix}X_1 \\ X_1\end{pmatrix} = \begin{pmatrix}\mathrm{Var}(X_1) & \mathrm{Var}(X_1) \\ \mathrm{Var}(X_1) & \mathrm{Var}(X_1)\end{pmatrix},
$$

and from the cumulant generating function, $$\dfrac{\mathrm{Var}(X_1)}{2!} = \dfrac{1}{72}$$, so $$\mathrm{Var}(X_1) = \dfrac{1}{36}$$. Therefore

$$
\mathrm{Var}\bigl(E(Y \mid X_1)\bigr) = \begin{pmatrix}\frac{1}{36} & \frac{1}{36} \\[0.3em] \frac{1}{36} & \frac{1}{36}\end{pmatrix}, \qquad E\bigl(\mathrm{Var}(Y \mid X_1)\bigr) = E\begin{pmatrix}\frac{1}{25} & \frac{1}{25} \\ \frac{1}{25} & \frac{34}{225}\end{pmatrix} = \begin{pmatrix}\frac{1}{25} & \frac{1}{25} \\[0.3em] \frac{1}{25} & \frac{34}{225}\end{pmatrix}.
$$

**Added.** As a check, the sum of the two matrices is $$\begin{pmatrix}\frac{61}{900} & \frac{61}{900} \\ \frac{61}{900} & \frac{161}{900}\end{pmatrix}$$, which is the lower-right block of $$\mathrm{Var}(X)$$ in 2.16 (b), i.e. $$\mathrm{Var}(Y)$$, as the decomposition of the variance matrix requires.

## References

- 김우철, *수리통계학* (Mathematical Statistics), revised 2nd edition, 민영사, 2021 — Chapter 2 exercises 2.1 to 2.17. The exercise statements are translated from the book.
- Mathematical Statistics 1 (326.311), Seoul National University, Spring 2025. Instructor: Jaeyong Lee (이재용). Homework 3 sheet.
- The answers are mine, translated into English. Where a step was wrong it is corrected and marked; the structure of every answer is unchanged.

[Overview](/posts/mathstat1-overview/) · [Homework 3, Chapter 1 Exercises](/posts/mathstat1-homework-3-chapter-1/) · [Chapter 2 Part 5](/posts/mathstat1-multivariate/)
