---
title: "Mathematical Statistics 1: Homework 2"
date: 2026-11-21 09:10:00 +0900
categories: [Study Notes, Mathematical Statistics 1]
tags: [homework, cdf, density, expectation, moment generating function, median]
description: Homework 2 of Mathematical Statistics 1 — textbook Chapter 1 exercises 7 to 12 and 14 to 17, Examples 1.5.6 and 1.5.7, discontinuities of a CDF, existence of a random variable with a given CDF, and symmetric distributions.
math: true
mermaid: false
render_with_liquid: false
---

> The problems are from the Homework 2 sheet of Mathematical Statistics 1 and from the textbook. The answers are my own, translated into English. Small slips in an answer are corrected and each correction is marked **Correction**; a step that was missing is marked **Added**. The structure of every answer is unchanged. This homework uses [Part 3](/posts/mathstat1-random-variables-cdf/) and [Part 4](/posts/mathstat1-expectation-mgf/) of the notes.
{: .prompt-info }

## The homework sheet

1. Textbook, Chapter 1, exercises 7, 8, 9, 10, 11, 12, 14, 15, 16, 17.
2. Read Example 1.5.6 of the textbook and describe it in your own words.
3. Read Example 1.5.7 of the textbook and describe it in your own words.
4. Show that the set of discontinuities of a cumulative distribution function $$F$$ is countable.
5. Let $$F : \mathbb{R} \to (0,1)$$ satisfy (i) $$F$$ is nondecreasing; (ii) $$\lim_{x \to -\infty} F(x) = 0$$, $$\lim_{x \to \infty} F(x) = 1$$; (iii) $$F$$ is right-continuous, i.e. $$\lim_{x \downarrow x_0} F(x) = F(x_0)$$; and in addition (iv) the inverse function $$F^{-1}$$ exists. Show that there is a random variable having $$F$$ as its cumulative distribution function.
6. A random variable $$X$$ is *symmetric about* $$\alpha$$ if $$P(X \ge \alpha + x) = P(X \le \alpha - x)$$ for all $$x \in \mathbb{R}$$. If $$X$$ is symmetric about $$\alpha$$ and continuous, show that its density function $$f$$ satisfies $$f(\alpha - x) = f(\alpha + x)$$ for all $$x \in \mathbb{R}$$.

## Textbook exercises

### Exercise 1.7

> **Exercise 1.7.** The cumulative distribution function of a random variable $$X$$ is
>
> $$
> F(x) =
> \begin{cases}
> 0 & x < 0 \\
> x/4 + 1/4 & 0 \le x < 2 \\
> 1 & x \ge 2
> \end{cases}
> $$
>
> and $$C_k = \{x : 1/k \le x \le 2 - 1/k\}$$, $$D_k = \{x : -1/k < x < 1 + 1/k\}$$ ($$k = 1, 2, \dots$$). Find the following events and probabilities.
>
> - (a) $$\lim_{k \to \infty} C_k$$ and $$P(X \in \lim_{k \to \infty} C_k)$$
> - (b) $$\lim_{k \to \infty} D_k$$ and $$P(X \in \lim_{k \to \infty} D_k)$$
{: .problem #hw2-1-7 }

**(a)** For every natural number $$k$$, $$\frac{1}{k} \ge \frac{1}{k+1}$$, so $$C_k \subseteq C_{k+1}$$. In other words, $$C_1 \subseteq C_2 \subseteq \cdots \subseteq C_k \subseteq C_{k+1} \subseteq \cdots$$.

Therefore what we want is $$\lim_{k \to \infty} C_k = \bigcup_{k=1}^{\infty} C_k$$, and by the continuity of probability measure,

$$
P\Bigl(X \in \lim_{k \to \infty} C_k\Bigr) = P\Bigl(\bigcup_{k=1}^{\infty} C_k\Bigr) = \lim_{k \to \infty} P(C_k).
$$

In other words, we need $$\bigcup_{k=1}^{\infty} C_k$$ and $$\lim_{k \to \infty} P(C_k)$$.

For every natural number $$k$$, $$C_k \subseteq (0,2)$$, and if $$x \in (0,2)$$, there is an $$n \in \mathbb{N}$$ with $$\frac{1}{n} \le x \le 2 - \frac{1}{n}$$. Hence $$\bigcup_{k=1}^{\infty} C_k = \lim_{k \to \infty} C_k = \{x : 0 < x < 2\}$$.

Also, for any natural number $$k$$, $$P(C_k) = P\{x : \tfrac{1}{k} \le x \le 2 - \tfrac{1}{k}\} = F(2 - \tfrac{1}{k}) - \lim_{x \to \frac{1}{k}-} F(x)$$. Since $$0 < \frac{1}{k} < 2$$ and $$0 < 2 - \frac{1}{k} < 2$$, $$\lim_{x \to \frac{1}{k}-} F(x) = F(\tfrac{1}{k}) = \frac{1}{4k} + \frac{1}{4}$$.

$$
\therefore\ P(C_k) = F\bigl(2 - \tfrac{1}{k}\bigr) - F\bigl(\tfrac{1}{k}\bigr)
= \tfrac{1}{4}\bigl(2 - \tfrac{1}{k}\bigr) + \tfrac{1}{4} - \bigl(\tfrac{1}{4k} + \tfrac{1}{4}\bigr) = \tfrac{1}{2} - \tfrac{1}{2k}.
$$

Therefore $$\lim_{k \to \infty} P(C_k) = \lim_{k \to \infty}\bigl(\tfrac{1}{2} - \tfrac{1}{2k}\bigr) = \tfrac{1}{2}$$.

**(b)** For every natural number $$k$$, $$\frac{1}{k} \ge \frac{1}{k+1}$$, so $$D_k \supseteq D_{k+1}$$. In other words, $$D_1 \supseteq D_2 \supseteq \cdots \supseteq D_k \supseteq D_{k+1} \supseteq \cdots$$.

Therefore what we want is $$\lim_{k \to \infty} D_k = \bigcap_{k=1}^{\infty} D_k$$, and by the continuity of probability measure,

$$
P\Bigl(X \in \lim_{k \to \infty} D_k\Bigr) = P\Bigl(\bigcap_{k=1}^{\infty} D_k\Bigr) = \lim_{k \to \infty} P(D_k).
$$

For every natural number $$k$$, $$(0,1) \subseteq D_k$$, and if $$x \in (-\infty, 0) \cup (1, \infty)$$, there is an $$n \in \mathbb{N}$$ with $$x \notin (-\frac{1}{n}, 1 + \frac{1}{n})$$. Hence $$\bigcap_{k=1}^{\infty} D_k = \lim_{k \to \infty} D_k = \{x : 0 \le x \le 1\}$$.

Also, for any natural number $$k$$, $$P(D_k) = P\{x : -\tfrac{1}{k} < x < 1 + \tfrac{1}{k}\} = \lim_{x \to (1 + \frac{1}{k})-} F(x) - F(-\tfrac{1}{k})$$. Since $$-1 \le -\frac{1}{k} < 0$$ and $$0 < 1 + \frac{1}{k} \le 2$$, $$\lim_{x \to (1 + \frac{1}{k})-} F(x) = \frac{1}{4}(1 + \frac{1}{k}) + \frac{1}{4} = \frac{1}{2} + \frac{1}{4k}$$.

$$
\therefore\ P(D_k) = \tfrac{1}{2} + \tfrac{1}{4k} - 0 = \tfrac{1}{2} + \tfrac{1}{4k}.
$$

Therefore $$\lim_{k \to \infty} P(D_k) = \lim_{k \to \infty}\bigl(\tfrac{1}{2} + \tfrac{1}{4k}\bigr) = \tfrac{1}{2}$$.

### Exercise 1.8

> **Exercise 1.8.** Find the probability density function of $$X$$ when its cumulative distribution function is as follows.
>
> - (a) $$F(x) = 0$$ for $$x < 1$$, and $$F(x) = 1 - (1/2)^k$$ for $$k \le x < k + 1$$ ($$k = 1, 2, \dots$$)
> - (b) $$F(x) = 0$$ ($$x < 0$$), $$x^2$$ ($$0 \le x < 1$$), $$1$$ ($$x \ge 1$$)
> - (c) $$F(x) = 0$$ ($$x < 0$$), $$1 - e^{-x^2}$$ ($$x \ge 0$$)
{: .problem #hw2-1-8 }

**(a)** To find the density function of $$X$$ we have to check whether $$X$$ is a discrete random variable, a continuous random variable, or neither.

For any $$k \in \mathbb{N}$$, $$P(X = k) = F(k) - \lim_{x \to k-} F(x) = \bigl(1 - (\tfrac{1}{2})^k\bigr) - \bigl(1 - (\tfrac{1}{2})^{k-1}\bigr) = (\tfrac{1}{2})^k$$. Also, for any $$p \in \{t : t \in \mathbb{R},\ t \notin \mathbb{N}\}$$, if $$p < 1$$, $$P(X = p) = F(p) - \lim_{x \to p-} F(x) = 0 - 0 = 0$$, and if $$p > 1$$, there is a natural number $$n$$ with $$n \le p < n + 1$$, so $$P(X = p) = F(p) - \lim_{x \to p-} F(x) = \bigl(1 - (\tfrac{1}{2})^{n}\bigr) - \bigl(1 - (\tfrac{1}{2})^{n}\bigr) = 0$$.

In other words, when $$x \in \mathbb{N}$$, $$P(X = x) \ne 0$$, and when $$x \notin \mathbb{N}$$, $$P(X = x) = 0$$, and since the set of points with $$P(X = x) \ne 0$$ is countable, $$X$$ is a discrete random variable.

Then the density function $$f$$ of the discrete random variable $$X$$ is $$P(X = x)$$. Therefore

$$
f(x) = P(X = x) =
\begin{cases}
(\tfrac{1}{2})^x & (x \in \mathbb{N}) \\
0 & (x \notin \mathbb{N}).
\end{cases}
$$

**Correction.** In the case $$p > 1$$ the original wrote the exponent as $$p$$ in $$(\tfrac12)^p$$; it is the integer $$n$$ with $$n \le p < n+1$$, as above, since $$F$$ is constant on $$[n, n+1)$$.

**(b)** For the cumulative distribution function $$F$$ of $$X$$, define $$f(x) = 2x\, I_{[0,1)}(x)$$. Then, letting $$G(x) = \int_{-\infty}^{x} f(t)\,dt$$, there is a random variable $$X'$$ having $$G$$ as its cumulative distribution function, and if $$F(x) = G(x)$$, then by the uniqueness of the cumulative distribution function, $$f$$ is a probability density function of $$F$$.

Therefore, to show that there is a random variable $$X'$$ having $$G$$ as its cumulative distribution function, we show that $$F = G$$. Here, $$G(x)$$ is, if $$x < 0$$, $$G(x) = \int_{-\infty}^{x} 0\,dt = 0$$; if $$0 \le x < 1$$, $$G(x) = \int_{-\infty}^{0} 0\,dt + \int_0^x 2t\,dt = x^2$$; and if $$x \ge 1$$, $$G(x) = \int_{-\infty}^{0} 0\,dt + \lim_{k \to 1-}\int_0^k 2t\,dt + \int_1^x 0\,dt = 1$$.

That is, $$G(x) = 0$$ ($$x < 0$$), $$x^2$$ ($$0 \le x < 1$$), $$1$$ ($$x \ge 1$$).

Also, since by the conditions of the problem $$X$$ having $$F$$ as its cumulative distribution function was assumed to exist, showing $$F = G$$ is enough, and then by the uniqueness of the cumulative distribution function there is a random variable with $$G$$ as its cumulative distribution function, and $$f$$ is the density function of $$F$$. In other words, it suffices to show $$F = G$$. For any $$t \in \mathbb{R}$$, $$G(t) = F(t)$$. Therefore $$f$$ is a probability density function of $$F$$.

**(c)** For the cumulative distribution function $$F(x) = 0$$ ($$x < 0$$), $$1 - e^{-x^2}$$ ($$x \ge 0$$), define $$f(x) = 2x e^{-x^2} I_{[x \ge 0]}$$. Let $$G(x) = \int_{-\infty}^{x} f(t)\,dt$$. As in (b), it suffices to show $$F = G$$. If $$x < 0$$, $$G(x) = \int_{-\infty}^{x} 0\,dt = 0$$, and if $$x \ge 0$$, $$\int_{-\infty}^{x} f(t)\,dt = \int_{-\infty}^{0} 0\,dt + \int_0^x 2t e^{-t^2}\,dt = 1 - e^{-x^2}$$. That is, for any $$t \in \mathbb{R}$$, $$G(t) = F(t)$$. Therefore $$f$$ is a probability density function of $$F$$.

### Exercise 1.9

> **Exercise 1.9.** Find the constant $$c$$ and the cumulative distribution function of $$X$$ when its probability density function is
>
> - (a) $$f(x) = c\,(2/3)^x$$, $$x = 0, 1, 2, \dots$$
> - (b) $$f(x) = c\,x^2(1 - x)\, I_{(0,1)}(x)$$
> - (c) $$f(x) = c\, e^{-2\lvert x\rvert}$$, $$-\infty < x < +\infty$$
{: .problem #hw2-1-9 }

**(a)** Since the set of $$x$$ with $$f(x) \ne 0$$ is countable, $$X$$ is a discrete random variable. Therefore the cumulative distribution function of $$X$$ can be found as $$F(x) = P(X \le x) = \sum_{t \in \mathbb{Z}_+,\, t \le x} f(t)$$.

Here $$\lim_{x \to \infty} F(x) = \sum_{x=0}^{\infty} f(x) = 1$$, and we want to find the constant of proportionality $$c$$ using $$\sum_{x=0}^{\infty} f(x) = 1$$. Since $$\sum_{x=0}^{\infty} f(x)$$ is an infinite geometric series with first term $$c$$ and common ratio $$\frac{2}{3}$$,

$$
\sum_{x=0}^{\infty} f(x) = \sum_{x=0}^{\infty} c\,\bigl(\tfrac{2}{3}\bigr)^x = \frac{c}{1 - \frac{2}{3}} = 3c = 1.
$$

$$\therefore\ c = \frac{1}{3}$$.

Also, when $$x < 0$$, $$F(x) = \sum_{t \in \mathbb{Z}_+,\, t \le x} f(t) = 0$$. When $$x \ge 0$$, there is a non-negative integer $$n$$ with $$n \le x < n + 1$$, and then

$$
F(x) = \sum_{t=0}^{n} f(t) = \sum_{t=0}^{n} \tfrac{1}{3}\bigl(\tfrac{2}{3}\bigr)^t = \frac{\frac{1}{3}\bigl(1 - (\frac{2}{3})^{n+1}\bigr)}{1 - \frac{2}{3}} = 1 - \bigl(\tfrac{2}{3}\bigr)^{n+1}.
$$

In other words, the cumulative distribution function is, for a non-negative integer $$n$$,

$$
F(x) =
\begin{cases}
0 & (x < 0) \\
1 - (\frac{2}{3})^{n+1} & (n \le x < n + 1).
\end{cases}
$$

**(b)** The cumulative distribution function of $$X$$ can be found as $$F(x) = P(X \le x) = \int_{-\infty}^{x} f(t)\,dt$$. Also, we want to find $$c$$ through $$\lim_{x \to \infty} F(x) = 1$$, that is, $$\lim_{x \to \infty}\int_{-\infty}^{x} f(t)\,dt = 1$$.

If $$x \le 0$$, $$F(x) = \int_{-\infty}^{x} f(t)\,dt = \int_{-\infty}^{x} 0\,dt = 0$$. If $$0 < x < 1$$,

$$
F(x) = \int_{-\infty}^{0} 0\,dt + \int_0^x c\,t^2(1 - t)\,dt = c\,x^3\bigl(\tfrac{1}{3} - \tfrac{1}{4}x\bigr),
$$

and if $$x \ge 1$$, $$F(x) = \int_{-\infty}^{0} 0\,dt + \int_0^1 c\,t^2(1 - t)\,dt + \int_1^{\infty} 0\,dt = \frac{1}{12}c$$.

Therefore $$\lim_{x \to \infty} F(x) = \frac{1}{12}c = 1$$, so $$c = 12$$. The cumulative distribution function of $$X$$ is

$$
F(x) =
\begin{cases}
0 & (x \le 0) \\
4x^3 - 3x^4 & (0 < x < 1) \\
1 & (x \ge 1).
\end{cases}
$$

**Correction.** The original wrote the middle line as $$4x^3 - 3x^2$$; with $$c = 12$$, $$12x^3(\frac13 - \frac14 x) = 4x^3 - 3x^4$$.

**(c)** The probability density function of $$X$$ is $$f(x) = c\,e^{-2\lvert x\rvert} = c\,e^{2x} I_{(x<0)} + c\,e^{-2x} I_{(x \ge 0)}$$. The cumulative distribution function of $$X$$ can be found as $$F(x) = P(X \le x) = \int_{-\infty}^{x} f(t)\,dt$$. We want to find $$c$$ through $$\lim_{x \to \infty} F(x) = 1$$, that is, $$\lim_{x \to \infty}\int_{-\infty}^{x} f(t)\,dt = 1$$.

If $$x < 0$$, $$F(x) = \int_{-\infty}^{x} c\,e^{2t}\,dt = \frac{1}{2}c\,e^{2x}$$, and if $$x \ge 0$$,

$$
F(x) = \int_{-\infty}^{0} c\,e^{2t}\,dt + \int_0^x c\,e^{-2t}\,dt = c - \tfrac{1}{2}c\,e^{-2x}.
$$

Therefore $$\lim_{x \to \infty} F(x) = c = 1$$, so $$c = 1$$. The cumulative distribution function of $$X$$ is

$$
F(x) =
\begin{cases}
\frac{1}{2}e^{2x} & (x < 0) \\
1 - \frac{1}{2}e^{-2x} & (x \ge 0).
\end{cases}
$$

### Exercise 1.10

> **Exercise 1.10.** Find the range of the positive number $$\alpha$$ for which the expectation of $$X$$ exists, i.e. $$E(X) < +\infty$$, when the probability density function of $$X$$ is $$f(x) = \alpha\, x^{-\alpha - 1} I_{(1,\infty)}(x)$$.
{: .problem #hw2-1-10 }

To find the range of the positive number $$\alpha$$ for which $$E(\lvert X\rvert) < \infty$$, by the definition of expectation we need the range of the positive number $$\alpha$$ for which $$\int_{-\infty}^{\infty} \lvert x\rvert f(x)\,dx < \infty$$.

$$
\int_{-\infty}^{\infty} \lvert x\rvert f(x)\,dx = \int_{-\infty}^{1} x \cdot 0\,dx + \lim_{t \to 1+}\int_t^{\infty} x\,(\alpha x^{-\alpha - 1})\,dx = \lim_{t \to 1+}\int_t^{\infty} \alpha\, x^{-\alpha}\,dx.
$$

That is, we need the range of $$\alpha$$ with $$\lim_{t \to 1+}\int_t^{\infty} \alpha x^{-\alpha}\,dx < \infty$$.

If $$\alpha \ne 1$$,

$$
\lim_{t \to 1+}\int_t^{\infty} \alpha x^{-\alpha}\,dx = \lim_{t \to 1+}\Bigl[\frac{\alpha}{1 - \alpha}x^{1-\alpha}\Bigr]_t^{\infty} = \lim_{k \to \infty}\lim_{t \to 1+}\Bigl[\frac{\alpha}{1 - \alpha}x^{1-\alpha}\Bigr]_t^{k}
= \frac{\alpha}{1 - \alpha}\lim_{k \to \infty}k^{1-\alpha} - \frac{\alpha}{1 - \alpha}.
$$

Here, if $$0 < \alpha < 1$$, then $$1 - \alpha > 0$$, so $$\lim_{k \to \infty}k^{1-\alpha} = \infty$$, and if $$\alpha > 1$$, $$\lim_{k \to \infty}k^{1-\alpha} = \lim_{k \to \infty}\frac{1}{k^{\alpha - 1}} = 0$$.

That is, $$\lim_{k \to \infty}k^{1-\alpha}$$ converges only when $$\alpha > 1$$, so only in that range $$\int_{-\infty}^{\infty} \lvert x\rvert f(x)\,dx$$ converges, to $$\frac{\alpha}{\alpha - 1}$$.

Also, if $$\alpha = 1$$, $$\lim_{t \to 1+}\int_t^{\infty}\frac{1}{x}\,dx = \lim_{k \to \infty}\lim_{t \to 1+}(\log k - \log t) = \lim_{k \to \infty}\log k = \infty$$, so $$\int_{-\infty}^{\infty} \lvert x\rvert f(x)\,dx$$ diverges.

Therefore the positive numbers $$\alpha$$ with $$\int_{-\infty}^{\infty} \lvert x\rvert f(x)\,dx < \infty$$ are $$\alpha > 1$$, and only in that case does the random variable $$X$$ have an expectation.

### Exercise 1.11

> **Exercise 1.11.**
>
> - (a) Show that for a random variable $$X$$ and any positive number $$k$$, $$k\,P(X > k) \le E\bigl(X\,I(X > k)\bigr)$$.
> - (b) Show that when a continuous random variable $$X$$ taking the value $$0$$ or positive values has an expectation, i.e. $$E(X) < +\infty$$, $$\lim_{x \to +\infty} x\,P(X > x) = 0$$.
> - (c) Show that when a continuous random variable $$X$$ taking the value $$0$$ or positive values has an expectation and its cumulative distribution function $$F$$ is differentiable at every point, $$EX = \int_0^{+\infty}(1 - F(x))\,dx$$.
{: .problem #hw2-1-11 }

**(a)** For a random variable $$X$$ and any positive number $$k$$ we want to prove the inequality $$k\,P(X > k) \le E(X\,I(X > k))$$. Since $$P(X > k) = E(I(X > k))$$, it suffices to prove $$k\,E(I(X > k)) \le E(X\,I(X > k))$$.

Then $$E(X\,I(X > k)) - k\,E(I(X > k)) = E(X\,I(X > k)) - E(k\,I(X > k)) = E\bigl((X - k)\,I(X > k)\bigr)$$, and for the random variable $$(X - k)\,I(X > k)$$, when $$X > k$$ we have $$X - k \ge 0$$, and when $$X \le k$$ it is $$0 \ge 0$$, so $$(X - k)\,I(X > k) \ge 0$$. Therefore $$E\bigl((X - k)\,I(X > k)\bigr) \ge 0$$, so $$E(X\,I(X > k)) \ge k\,E(I(X > k))$$.

**(b)** For a continuous random variable $$X$$ taking the value $$0$$ or positive values with $$E(X) < \infty$$, we want to show $$\lim_{x \to \infty}x\,P(X > x) = 0$$. By the given condition, $$\int_{-\infty}^{\infty} x f(x)\,dx < \infty$$, and when $$x < 0$$, $$P(X = x) = 0$$, so $$\int_{-\infty}^{\infty} x f(x)\,dx = \int_0^{\infty} x f(x)\,dx < \infty$$. Also, from (a), $$\lim_{x \to \infty} x\,P(X > x) \le \lim_{x \to \infty} E(X\,I(X > x))$$.

Also $$P(X > x) \ge 0$$, and if $$x < 0$$ then $$P(X = x) = 0$$, so $$x\,P(X > x) \ge 0$$ for every real $$x$$, that is, $$\lim_{x \to \infty} x\,P(X > x) \ge 0$$. Therefore it suffices to show $$\lim_{x \to \infty} E(X\,I(X > x)) = 0$$. Let $$a = \int_0^{\infty} x f(x)\,dx$$. Then $$a = \lim_{x \to \infty}\int_0^x t f(t)\,dt < \infty$$, so

$$
\lim_{x \to \infty} E(X\,I(X > x)) = \lim_{x \to \infty}\int_0^{\infty} t f(t)\,I_{(t > x)}\,dt = \lim_{x \to \infty}\int_x^{\infty} t f(t)\,dt
= \lim_{x \to \infty}\Bigl(\int_0^{\infty} t f(t)\,dt - \int_0^{x} t f(t)\,dt\Bigr) = \int_0^{\infty} t f(t)\,dt - \lim_{x \to \infty}\int_0^{x} t f(t)\,dt = a - a = 0.
$$

Therefore $$\lim_{x \to \infty} E(X\,I(X > x)) = 0$$, so $$0 \le \lim_{x \to \infty} x\,P(X > x) \le \lim_{x \to \infty}E(X\,I(X > x)) = 0$$, and so $$\lim_{x \to \infty} x\,P(X > x) = 0$$.

**(c)** For a continuous random variable $$X$$ taking the value $$0$$ or positive values, whose expectation exists and whose cumulative distribution function $$F$$ is differentiable at every point, we want to show $$E(X) = \int_0^{\infty}(1 - F(x))\,dx$$. By (b), $$\lim_{x \to \infty} x\,P(X > x) = 0$$, so $$\lim_{x \to \infty} x\,P(X > x) = \lim_{x \to \infty} x\,(1 - P(X \le x)) = \lim_{x \to \infty} x\,(1 - F(x)) = 0$$.

Then, by integration by parts,

$$
\lim_{x \to \infty}\int_0^{x}\bigl(-t f(t)\bigr)\,dt = \lim_{x \to \infty} x\,(1 - F(x)) - \lim_{x \to \infty}\int_0^{x}(1 - F(t))\,dt = -\int_0^{\infty}(1 - F(t))\,dt.
$$

In other words, $$\int_0^{\infty}(1 - F(t))\,dt = \int_0^{\infty} t f(t)\,dt = E(X)$$.

**Correction.** The integration variable inside the integrals was written $$x$$, the same letter as the upper limit; it is written $$t$$ above.

### Exercise 1.12

> **Exercise 1.12.** Find (a) $$E(X)$$, $$\mathrm{Var}(X)$$ and (b) $$E(2X + 3)$$, $$\mathrm{Var}(2X + 3)$$ when the probability density function of $$X$$ is $$f(x) = \frac{2}{9}(2 - x)(1 + x)\,I_{[-1,2]}(x)$$.
{: .problem #hw2-1-12 }

**(a)** We want $$E(X)$$ and $$\mathrm{Var}(X)$$. These are $$E(X) = \int_{-\infty}^{\infty} x f(x)\,dx$$ and $$\mathrm{Var}(X) = \int_{-\infty}^{\infty}(x - E(X))^2 f(x)\,dx$$.

$$
E(X) = \int_{-\infty}^{\infty} x\cdot\bigl(\tfrac{2}{9}(2 - x)(1 + x)\,I_{[-1,2]}\bigr)dx = \frac{2}{9}\int_{-1}^{2} x(1 + x)(2 - x)\,dx = \frac{2}{9}\Bigl[x^2 + \tfrac{1}{3}x^3 - \tfrac{1}{4}x^4\Bigr]_{-1}^{2} = \frac{1}{2},
$$

and

$$
\mathrm{Var}(X) = \int_{-\infty}^{\infty}\bigl(x - \tfrac{1}{2}\bigr)^2\cdot\tfrac{2}{9}(2 - x)(1 + x)\,I_{[-1,2]}\,dx
= \frac{2}{9}\int_{-1}^{2}\bigl(x - \tfrac{1}{2}\bigr)^2(2 - x)(1 + x)\,dx = \frac{9}{20}.
$$

**(b)** We want $$E(2X + 3)$$ and $$\mathrm{Var}(2X + 3)$$. By the linearity of expectation, $$E(2X + 3) = 2E(X) + 3$$, and by the properties of variance, $$\mathrm{Var}(2X + 3) = 4\,\mathrm{Var}(X)$$. Therefore $$E(2X + 3) = 2E(X) + 3 = 2 \times \frac{1}{2} + 3 = 4$$ and $$\mathrm{Var}(2X + 3) = 4\,\mathrm{Var}(X) = 4 \times \frac{9}{20} = \frac{9}{5}$$.

### Exercise 1.14

> **Exercise 1.14.** For a continuous random variable $$X$$, if there is a unique $$m$$ with $$P(X \le m) = 1/2$$, $$m$$ is called the median of the distribution of $$X$$. For a continuous random variable $$X$$ with a unique median and $$E(\lvert X\rvert) < +\infty$$, show that
>
> $$
> E(\lvert X - a\rvert) = E(\lvert X - m\rvert) + 2\int_m^a (a - x) f(x)\,dx,
> $$
>
> and from this show that the value of $$a$$ minimizing $$E[\lvert X - a\rvert]$$ is the median $$m$$. (Hint: when $$a > m$$, $$\lvert x - a\rvert - \lvert x - m\rvert = (a - m)\{I(x \le m) - I(x > m)\} + 2(a - x)I(m < x \le a)$$.)
{: .problem #hw2-1-14 }

For a continuous random variable with a unique median $$m$$ and $$E(\lvert X\rvert) < \infty$$ we first want to prove $$E(\lvert X - a\rvert) = E(\lvert X - m\rvert) + 2\int_m^a (a - x) f(x)\,dx$$. Let $$f(x)$$ be the probability density function of $$X$$.

Since $$m$$ is unique, $$P(X \le m) = \frac{1}{2}$$ holds for exactly one $$m$$, and:

- when $$a > m$$, $$\lvert x - a\rvert - \lvert x - m\rvert = (a - m)\{I(x \le m) - I(x > m)\} + 2(a - x)\,I(m < x \le a)$$;
- when $$a = m$$, $$\lvert x - a\rvert - \lvert x - m\rvert = \lvert x - m\rvert - \lvert x - m\rvert = 0$$;
- when $$a < m$$, $$\lvert x - a\rvert - \lvert x - m\rvert = (a - m)\{I(x \le m) - I(x > m)\} + 2(x - a)\,I(a < x \le m)$$.

Then, when $$a > m$$,

$$
\begin{aligned}
E(\lvert X - a\rvert) - E(\lvert X - m\rvert) &= \int_{-\infty}^{\infty}\lvert x - a\rvert f(x)\,dx - \int_{-\infty}^{\infty}\lvert x - m\rvert f(x)\,dx \\
&= \int_{-\infty}^{\infty}\bigl(\lvert x - a\rvert - \lvert x - m\rvert\bigr) f(x)\,dx \\
&= \int_{-\infty}^{\infty}\Bigl[(a - m)\{I(x \le m) - I(x > m)\} + 2(a - x)\,I(m < x \le a)\Bigr] f(x)\,dx \\
&= \int_{-\infty}^{m}(a - m) f(x)\,dx - \int_m^{\infty}(a - m) f(x)\,dx + 2\int_m^{a}(a - x) f(x)\,dx.
\end{aligned}
$$

Also, $$P(X \le m) = \int_{-\infty}^{m} f(x)\,dx = \frac{1}{2}$$, so $$\int_m^{\infty} f(x)\,dx = P(X > m) = 1 - P(X \le m) = \frac{1}{2}$$. Hence

$$
E(\lvert X - a\rvert) - E(\lvert X - m\rvert) = \frac{a - m}{2} - \frac{a - m}{2} + 2\int_m^{a}(a - x) f(x)\,dx = 2\int_m^{a}(a - x)\,f(x)\,dx.
$$

When $$a < m$$ also,

$$
\begin{aligned}
E(\lvert X - a\rvert) - E(\lvert X - m\rvert) &= \int_{-\infty}^{\infty}\bigl(\lvert x - a\rvert - \lvert x - m\rvert\bigr) f(x)\,dx
= \int_{-\infty}^{\infty}\Bigl[(a - m)\{I(x \le m) - I(x > m)\} + 2(x - a)\,I(a < x \le m)\Bigr] f(x)\,dx \\
&= \int_{-\infty}^{m}(a - m) f(x)\,dx - \int_m^{\infty}(a - m) f(x)\,dx + 2\int_a^{m}(x - a) f(x)\,dx = \frac{a - m}{2} - \frac{a - m}{2} + 2\int_m^{a}(a - x) f(x)\,dx.
\end{aligned}
$$

When $$a = m$$, $$E(\lvert X - a\rvert) - E(\lvert X - m\rvert) = 0 = 2\int_m^{a}(a - x) f(x)\,dx$$.

Therefore, for every real number $$a$$, $$E(\lvert X - a\rvert) - E(\lvert X - m\rvert) = 2\int_m^{a}(a - x) f(x)\,dx$$, so

$$
E(\lvert X - a\rvert) = E(\lvert X - m\rvert) + 2\int_m^{a}(a - x) f(x)\,dx.
$$

Next we show that the value of $$a$$ minimizing $$E(\lvert X - a\rvert)$$ is the median $$m$$. If the cumulative distribution function of $$X$$ is $$F$$, then since $$E(\lvert X - a\rvert) - E(\lvert X - m\rvert) = 2\int_m^{a}(a - x) f(x)\,dx$$,

$$
\frac{d}{da}E(\lvert X - a\rvert) = \frac{d}{da}\,2\int_m^{a}(a - x) f(x)\,dx = 2\,\frac{d}{da}\Bigl(a\int_m^{a} f(x)\,dx - \int_m^{a} x f(x)\,dx\Bigr)
= 2\Bigl(\int_m^{a} f(x)\,dx + a f(a) - a f(a)\Bigr) = 2\bigl(F(a) - F(m)\bigr).
$$

Here the point with $$F(x) = \frac{1}{2}$$ is unique, namely $$m$$, and since $$F$$ is non-decreasing, for any real number $$x$$ with $$x < m$$, $$F(x) < F(m) = \frac{1}{2}$$, and if $$x > m$$, $$F(x) > F(m) = \frac{1}{2}$$. In other words, $$\frac{d}{da}E(\lvert X - a\rvert) = 2(F(a) - F(m)) = 0$$ holds only at $$a = m$$, and since the derivative is negative for $$a < m$$ and positive for $$a > m$$, $$E(\lvert X - a\rvert)$$ attains its minimum at $$a = m$$.

**Correction.** (1) The line "$$\int(\lvert x - m\rvert - \lvert x - a\rvert) f$$" for $$E(\lvert X - a\rvert) - E(\lvert X - m\rvert)$$ had the two absolute values in the wrong order; it is $$\int(\lvert x - a\rvert - \lvert x - m\rvert) f$$, as above. (2) The terms $$\frac12 - \frac12$$ were missing the common factor $$(a - m)$$. (3) The derivative of $$2\int_m^a (a - x) f(x)\,dx$$ is $$2(F(a) - F(m))$$; the original had lost the factor $$2$$, which does not change where it vanishes. (4) "$$P(X \le m) \le \frac12$$" is $$P(X \le m) = \frac12$$, the definition of the median.

### Exercise 1.15

> **Exercise 1.15.** Find the moment generating function of $$X$$ when its probability density function is
>
> $$
> f(x) =
> \begin{cases}
> \frac{1}{2}e^{x}, & x < 0 \\
> e^{-2x}, & x > 0.
> \end{cases}
> $$
{: .problem #hw2-1-15 }

When the probability density function $$f$$ of $$X$$ exists and $$f(x) = \frac{1}{2}e^{x}$$ ($$x < 0$$), $$e^{-2x}$$ ($$x > 0$$), we want the moment generating function of $$X$$. Writing $$M_X(t)$$ for it, we check whether there is a positive real number $$h$$ with $$M_X(t) = E(e^{tX}) < \infty$$ for $$\lvert t\rvert < h$$, and then find $$M_X(t)$$.

By the definition of expectation,

$$
M_X(t) = E(e^{tX}) = \int_{-\infty}^{\infty} e^{tx} f(x)\,dx = \int_{-\infty}^{0} e^{tx}\cdot\tfrac{1}{2}e^{x}\,dx + \int_0^{\infty} e^{tx}\cdot e^{-2x}\,dx = \frac{1}{2}\int_{-\infty}^{0} e^{(t+1)x}\,dx + \int_0^{\infty} e^{(t-2)x}\,dx.
$$

For a positive number $$h < 1$$, consider any real number $$t$$ with $$\lvert t\rvert < h$$. Then $$t > -1$$ and $$t < 2$$, so

$$
M_X(t) = \frac{1}{2}\lim_{k \to \infty}\Bigl[\frac{1}{t+1}e^{(t+1)x}\Bigr]_{-k}^{0} + \lim_{k \to \infty}\Bigl[\frac{1}{t-2}e^{(t-2)x}\Bigr]_0^{k}
= \frac{1}{2(t+1)}\lim_{k \to \infty}\Bigl(1 - \frac{1}{e^{(t+1)k}}\Bigr) - \frac{1}{2-t}\lim_{k \to \infty}\Bigl(\frac{1}{e^{(2-t)k}} - 1\Bigr) = \frac{1}{2(t+1)} + \frac{1}{2-t},
$$

which converges. That is, for any real number $$t$$ with $$\lvert t\rvert < h$$ there is a positive number $$h$$ with $$M_X(t) < \infty$$; $$M_X(t)$$ exists for $$\lvert t\rvert < h$$, and the moment generating function is

$$
M_X(t) = \frac{1}{2(t+1)} + \frac{1}{2-t} = \frac{t + 4}{2(t+1)(2-t)}.
$$

### Exercise 1.16

> **Exercise 1.16.** Find the moment generating function, the mean and the variance of $$X$$ when its probability density function is $$f(x) = \frac{1}{2}e^{-\lvert x\rvert}$$, $$-\infty < x < +\infty$$.
{: .problem #hw2-1-16 }

When the probability density function $$f$$ of $$X$$ exists and $$f(x) = \frac{1}{2}e^{-\lvert x\rvert}$$, first we find the moment generating function. Writing $$M_X(t)$$ for it, we check whether there is a positive real number $$h$$ with $$M_X(t) = E(e^{tX}) < \infty$$ for $$\lvert t\rvert < h$$, and then find $$M_X(t)$$.

By the definition of expectation,

$$
M_X(t) = E(e^{tX}) = \int_{-\infty}^{\infty} e^{tx}\Bigl(\frac{1}{2}e^{-\lvert x\rvert}\Bigr)dx = \frac{1}{2}\int_{-\infty}^{0} e^{(t+1)x}\,dx + \frac{1}{2}\int_0^{\infty} e^{(t-1)x}\,dx.
$$

For a positive number $$h < 1$$, consider any real number $$t$$ with $$\lvert t\rvert < h$$. Then $$t > -1$$ and $$t < 1$$, so

$$
M_X(t) = \frac{1}{2}\lim_{k \to \infty}\Bigl[\frac{1}{t+1}e^{(t+1)x}\Bigr]_{-k}^{0} + \frac{1}{2}\lim_{k \to \infty}\Bigl[\frac{1}{t-1}e^{(t-1)x}\Bigr]_0^{k}
= \frac{1}{2(t+1)} + \frac{1}{2(1-t)} = \frac{1}{1 - t^2} < \infty.
$$

That is, for any real number $$t$$ with $$\lvert t\rvert < h$$ there is a positive number $$h$$ with $$M_X(t) < \infty$$; $$M_X(t)$$ exists for $$\lvert t\rvert < h$$, and the moment generating function is $$M_X(t) = \dfrac{1}{1 - t^2}$$.

Now we find the mean and the variance of $$X$$. By the properties of the moment generating function, $$E(X) = \dfrac{d}{dt}M_X(t)\Big\vert_{t=0}$$ and $$E(X^2) = \dfrac{d^2}{dt^2}M_X(t)\Big\vert_{t=0}$$, and by the properties of variance, $$\mathrm{Var}(X) = E(X^2) - (E(X))^2$$. Therefore

$$
E(X) = \frac{d}{dt}\Bigl(\frac{1}{1 - t^2}\Bigr)\Big|_{t=0} = \frac{2t}{(1 - t^2)^2}\Big|_{t=0} = 0,
\qquad
E(X^2) = \frac{d^2}{dt^2}\Bigl(\frac{1}{1 - t^2}\Bigr)\Big|_{t=0} = \frac{2(1 + 3t^2)}{(1 - t^2)^3}\Big|_{t=0} = 2.
$$

Therefore $$E(X) = 0$$ and $$\mathrm{Var}(X) = E(X^2) - (E(X))^2 = 2$$.

**Correction.** At the head of this answer the original restated the density of Exercise 1.15 ($$\frac12 e^x$$ for $$x < 0$$, $$e^{-2x}$$ for $$x > 0$$); the density of Exercise 1.16 is $$\frac12 e^{-\lvert x\rvert}$$, which is what the computation uses.

### Exercise 1.17

> **Exercise 1.17.** The moment generating function of a random variable $$X$$ is known to exist, and $$E(X^{2r}) = (2r)!/2^r r!$$ ($$r = 1, 2, 3, \dots$$), $$E(X^{2r-1}) = 0$$ ($$r = 1, 2, 3, \dots$$). Find the moment generating function of $$X$$.
{: .problem #hw2-1-17 }

Since the moment generating function of $$X$$ is known to exist, writing $$M_X(t)$$ for it, there is a positive number $$h$$ with $$M_X(t) = \sum_{k=0}^{\infty}\frac{E(X^k)}{k!}t^k$$ for every real number $$t$$ with $$\lvert t\rvert < h$$. Therefore, considering such an $$h$$, for every real $$t$$ with $$\lvert t\rvert < h$$,

$$
M_X(t) = \sum_{k=0}^{\infty}\frac{E(X^k)}{k!}t^k = 1 + \sum_{r=1}^{\infty}\frac{E(X^{2r})}{(2r)!}t^{2r} + \sum_{r=1}^{\infty}\frac{E(X^{2r-1})}{(2r-1)!}t^{2r-1}
= 1 + \sum_{r=1}^{\infty}\frac{1}{(2r)!}\cdot\frac{(2r)!}{2^r r!}t^{2r} + \sum_{r=1}^{\infty}\frac{0}{(2r-1)!}t^{2r-1}
= 1 + \sum_{r=1}^{\infty}\frac{1}{2^r}\cdot\frac{1}{r!}t^{2r} = \sum_{r=0}^{\infty}\frac{1}{r!}\Bigl(\frac{t^2}{2}\Bigr)^r.
$$

Also, $$e^x = \sum_{n=0}^{\infty}\frac{1}{n!}x^n$$, so for every real number $$t$$ with $$\lvert t\rvert < h$$, $$M_X(t) = \sum_{r=0}^{\infty}\frac{1}{r!}\bigl(\frac{t^2}{2}\bigr)^r = e^{t^2/2}$$.

## Additional problems

### Problem 2 — the moment generating function and moments of the standard exponential distribution

> **Problem 2 (Example 1.5.6).** The probability density function of $$X$$ is $$f(x) = e^{-x}I_{(x>0)}$$ (the standard exponential distribution). Find its moment generating function and its moments.
{: .problem #hw2-p2 }

Let $$f(x) = e^{-x}I_{(x>0)}$$ and let $$M_X(t)$$ be the moment generating function of $$X$$. We want to show $$E(X^k) = k!$$ for every natural number $$k$$.

$$
M_X(t) = E(e^{tX}) = \int_{-\infty}^{\infty} e^{tx} f(x)\,dx = \int_{-\infty}^{\infty} e^{tx}e^{-x}I_{(x>0)}\,dx = \int_0^{\infty} e^{(t-1)x}\,dx.
$$

For a positive number $$h < 1$$, consider any real number $$t$$ with $$\lvert t\rvert < h$$. Then $$t < 1$$, so

$$
M_X(t) = \lim_{k \to \infty}\Bigl[\frac{1}{t-1}e^{(t-1)x}\Bigr]_0^{k} = \frac{1}{t-1}\lim_{k \to \infty}\Bigl(\frac{1}{e^{(1-t)k}} - 1\Bigr) = \frac{1}{1-t} < \infty.
$$

For a positive number $$h$$ satisfying this, for every real number $$t$$ with $$\lvert t\rvert < h$$, $$M_X(t) = \sum_{k=0}^{\infty}\frac{E(X^k)}{k!}t^k$$ and $$M_X(t) = \frac{1}{1-t} = \sum_{k=0}^{\infty}t^k$$, so

$$
\sum_{k=0}^{\infty}\frac{E(X^k)}{k!}t^k = \sum_{k=0}^{\infty}t^k = \sum_{k=0}^{\infty}\frac{k!}{k!}t^k.
$$

Therefore, for every natural number $$k$$, $$\dfrac{E(X^k)}{k!} = \dfrac{k!}{k!}$$, so $$E(X^k) = k!$$.

### Problem 3 — the moment generating function determines the distribution

> **Problem 3 (Example 1.5.7).** The moment generating function of a random variable $$X$$ is known to exist and its moments are $$E(X^k) = 2^k k!$$. Find the moment generating function and the probability density function of $$X$$.
{: .problem #hw2-p3 }

Writing $$M_X(t)$$ for the moment generating function of $$X$$, there is a positive number $$h$$ with $$M_X(t) = \sum_{k=0}^{\infty}\frac{E(X^k)}{k!}t^k$$ for every real number $$t$$ with $$\lvert t\rvert < h$$. Then

$$
M_X(t) = \sum_{k=0}^{\infty}\frac{1}{k!}\cdot 2^k\cdot k!\cdot t^k = \sum_{k=0}^{\infty}(2t)^k,
$$

and if $$h < \frac{1}{2}$$, then $$\lvert 2t\rvert < 1$$, so $$M_X(t) = \sum_{k=0}^{\infty}(2t)^k = \dfrac{1}{1 - 2t}$$.

On the other hand, let a random variable $$Y$$ have the probability density function $$f(x) = \frac{1}{2}e^{-x/2}I_{(x>0)}$$, and let $$M_Y(t)$$ be its moment generating function. Then

$$
M_Y(t) = E(e^{tY}) = \int_{-\infty}^{\infty} e^{tx}f(x)\,dx = \frac{1}{2}\int_0^{\infty} e^{(t - \frac{1}{2})x}\,dx,
$$

and for $$t < \frac{1}{2}$$ this integral converges. That is, for $$t < \frac{1}{2}$$,

$$
M_Y(t) = \frac{1}{2}\Bigl[\frac{1}{t - \frac{1}{2}}e^{(t - \frac{1}{2})x}\Bigr]_0^{\infty} = \frac{1}{1 - 2t}.
$$

Therefore, considering a positive number $$h < \frac{1}{2}$$, for every real number $$t$$ with $$\lvert t\rvert < h$$, $$M_X(t) = M_Y(t) = \dfrac{1}{1 - 2t}$$, so by the uniqueness of the moment generating function, $$f(x)$$ is a probability density function of $$X$$.

### Problem 4 — the discontinuities of a CDF form a countable set

> **Problem 4.** Show that the set of discontinuities of a cumulative distribution function $$F$$ is countable.
{: .problem #hw2-p4 }

Let $$F$$ be the cumulative distribution function of a random variable $$X$$, and let $$A \subseteq \mathbb{R}$$ be the set of discontinuities of $$F$$. It suffices to show that $$A$$ is at most countable. By the characterization theorem of the cumulative distribution function, $$F$$ is non-decreasing on the whole real line. In other words, $$F(x) \le F(y)$$ for all $$x < y$$ ($$x, y \in \mathbb{R}$$).

For any element $$k$$ of $$A$$, define $$\lim_{x \to k+}F(x) = F(k+)$$ and $$\lim_{x \to k-}F(x) = F(k-)$$. Since a cumulative distribution function is right-continuous, $$F(k+) = F(k)$$. Also, $$F(x)$$ is discontinuous at $$x = k$$, so $$F(k) \ne F(k-)$$. Then for any real number $$\varepsilon > 0$$, $$k - \varepsilon < k$$, so $$F(k - \varepsilon) \le F(k)$$. Therefore, for every element $$k$$ of $$A$$, $$F(k-) < F(k) = F(k+)$$.

Then, for each element $$k$$, by the denseness of the rational numbers there is a rational number $$r_k \in \mathbb{Q}$$ with $$F(k-) < r_k < F(k+)$$.

Also, for two real elements $$p, q$$ of $$A$$ with $$p < q$$, for any real number $$\varepsilon' > 0$$ with $$p \le q - \varepsilon'$$ we have $$F(p) \le F(q - \varepsilon')$$, so $$F(p) \le F(q-)$$. Hence $$F(p-) < r_p < F(p+) \le F(q-) < r_q < F(q+)$$, so if $$p < q$$, then $$r_p < r_q$$.

Then let the function $$f : p \mapsto r_p$$ ($$\forall p \in A$$). This function $$f$$ is a one-to-one correspondence between $$A$$ and some subset of $$\mathbb{Q}$$, so $$A$$ is equivalent to some subset of $$\mathbb{Q}$$. Therefore, since $$\mathbb{Q}$$ is a countable set, $$A$$ is at most countable.

### Problem 5 — existence of a random variable with a given CDF

> **Problem 5.** Let $$F : \mathbb{R} \to (0,1)$$ be nondecreasing, with $$\lim_{x \to -\infty}F(x) = 0$$, $$\lim_{x \to \infty}F(x) = 1$$, right-continuous, and suppose that its inverse $$F^{-1}$$ exists. Show that there is a random variable having $$F$$ as its cumulative distribution function.
{: .problem #hw2-p5 }

Let $$X$$ be a random variable whose cumulative distribution function is

$$
G(x) =
\begin{cases}
0 & (x < 0) \\
x & (0 \le x < 1) \\
1 & (x \ge 1).
\end{cases}
$$

Define a random variable $$Y$$ by $$Y(c) = F^{-1}(X(c))$$ for every element $$c$$ of the sample space $$\mathcal{C}$$; we want to show that its cumulative distribution function is $$F(x)$$. That is, it suffices to show $$F(x) = P(Y \le x)$$.

When $$F$$ satisfies the four given conditions, let $$F(\mathbb{R}) = \{F(x) : x \in \mathbb{R}\}$$ be the range of $$F$$. Then $$F$$ is nondecreasing and $$\lim_{x \to -\infty}F(x) = 0$$, $$\lim_{x \to \infty}F(x) = 1$$, so $$F(\mathbb{R}) \subseteq (0,1)$$. Here $$F$$ is a bijection, so the set $$F(\mathbb{R}) = (0,1)$$.

Also, since the inverse function $$F^{-1}$$ of $$F$$ exists, the function $$F : \mathbb{R} \to F(\mathbb{R})$$ is a one-to-one correspondence. Therefore, for any two real numbers $$x, y$$ with $$x < y$$, $$F(x) \ne F(y)$$, and since $$F$$ is nondecreasing, $$F(x) < F(y)$$. In other words, by the existence of the inverse function, for any real number $$p \in F(\mathbb{R}) = (0,1)$$ there is a unique real number $$t$$ with $$F(t) = p$$.

Therefore, since the cumulative distribution function of $$X$$ is defined on the whole real line, for any real number $$p \in (0,1)$$ there is an element $$c$$ of $$\mathcal{C}$$ with $$X(c) = p$$, and for that $$c$$, $$Y(c) = F^{-1}(X(c)) = F^{-1}(p) = t$$.

Now we prove $$F(x) = P(Y \le x)$$. Then $$P(Y \le x) = P(F^{-1}(X) \le x) = P(X \le F(x)) = G(F(x))$$, and since $$F(\mathbb{R}) = (0,1)$$, $$0 < F(x) < 1$$. Therefore $$P(Y \le x) = G(F(x)) = F(x)$$. That is, the random variable $$Y$$ has the cumulative distribution function $$F(x)$$.

**Added.** (1) A random variable with the distribution function $$G$$ exists: take $$\mathcal{C} = (0,1)$$ with the uniform probability $$P(dx) = dx$$ and $$X(c) = c$$. (2) $$F^{-1}$$ is defined only on $$(0,1)$$, and $$X$$ takes the values $$0$$ or $$1$$ only with probability $$0$$; $$Y$$ may be defined arbitrarily there (say, $$0$$), which does not affect $$P(Y \le x)$$. (3) The step $$P(F^{-1}(X) \le x) = P(X \le F(x))$$ uses that $$F$$ is strictly increasing: $$F^{-1}(u) \le x \Longleftrightarrow u \le F(x)$$.

### Problem 6 — symmetric distributions

> **Problem 6.** If $$X$$ is symmetric about $$\alpha$$ and continuous, show that its density function $$f$$ satisfies $$f(\alpha - x) = f(\alpha + x)$$ for all $$x \in \mathbb{R}$$.
{: .problem #hw2-p6 }

For a continuous random variable $$X$$ that is symmetric about $$\alpha$$ and whose density function $$f$$ exists and is continuous, we want to show $$f(\alpha - x) = f(\alpha + x)$$ for all real $$x$$. By the condition, for all real $$x$$, $$P(X \ge \alpha + x) = P(X \le \alpha - x)$$, so $$1 - P(X < \alpha + x) = P(X \le \alpha - x)$$. In other words, if $$F$$ is the cumulative distribution function of $$X$$, then $$1 - \lim_{t \to (\alpha + x)-}F(t) = F(\alpha - x)$$.

Then, since $$f$$ is continuous, $$F$$ is also continuous, and therefore $$\lim_{t \to (\alpha + x)-}F(t) = F(\alpha + x)$$. That is, $$1 - F(\alpha + x) = F(\alpha - x)$$, and since $$F(x) = \int_{-\infty}^{x}f(t)\,dt$$, differentiating both sides gives $$-f(\alpha + x) = -f(\alpha - x)$$. That is, for all real $$x$$, $$f(\alpha + x) = f(\alpha - x)$$.

**Added.** If $$f$$ is not assumed continuous, a density is determined only up to a set of probability $$0$$, so the same computation (with $$F' = f$$ almost everywhere) gives $$f(\alpha + x) = f(\alpha - x)$$ for almost every $$x$$.

## References

- 김우철, *수리통계학* (Mathematical Statistics), revised 2nd edition, 민영사, 2021 — Chapter 1 exercises 1.7 to 1.12 and 1.14 to 1.17, Examples 1.5.6 and 1.5.7. The exercise statements are translated from the book.
- Mathematical Statistics 1 (326.311), Seoul National University, Spring 2025. Instructor: Jaeyong Lee (이재용). Homework 2 sheet.
- The answers are mine, translated into English. Small slips are corrected where marked; the structure of every answer is unchanged.

[Overview](/posts/mathstat1-overview/) · [Homework 3, Chapter 1 exercises](/posts/mathstat1-homework-3-chapter-1/)
