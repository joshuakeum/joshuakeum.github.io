---
title: "Mathematical Statistics 1: Ch. 2 Part 3 — Conditional Distribution and Expectation"
date: 2026-11-21 09:50:00 +0900
categories: [Study Notes, Mathematical Statistics 1]
tags: [conditional distribution, conditional expectation, best predictor, linear prediction, evve]
description: Conditional pdf and cdf, conditional expectation, conditional mean and variance, the repeated expectation theorem, the best predictor, the EVVE rule and linear prediction. Chapter 2, §2.3 of Mathematical Statistics 1.
math: true
mermaid: false
render_with_liquid: false
---

> My handwritten notes, translated into English. They cover section 3 of Chapter 2 in my notes (conditional distribution, conditional expectation, conditional mean and variance, linear prediction), which corresponds to §2.3 of the textbook. Statements and proofs follow my notes; I only corrected expressions that were mathematically wrong. The textbook material that my notes leave out is collected at the end under "Supplement from the textbook". It uses [Part 1](/posts/mathstat1-joint-distribution/) and [Part 2](/posts/mathstat1-joint-characteristics/).
{: .prompt-info }

## Notes

### 3.1 Conditional distribution

> **Definition (Conditional probability density function).** Let $$f_{1,2}$$ be the joint pdf of $$(X_1, X_2)$$ and $$f_1, f_2$$ the marginal pdfs of $$X_1$$ and $$X_2$$. When $$X_2 = x_2$$ is given, the conditional pdf of $$X_1$$ is
>
> $$
> f_{1 \mid 2}(x_1 \mid x_2) = \frac{f_{1,2}(x_1, x_2)}{f_2(x_2)}.
> $$
>
> Here $$f_2(x_2) > 0$$ is required.
{: .definition #def-conditional-pdf }

**Meaning.**

1. $$P(X_1 \in A \mid X_2 = x_2) = \displaystyle\int_A f_{1 \mid 2}(x_1 \mid x_2)\,dx_1$$. $$\leftarrow$$ the purpose of conditional probability functions.

   ① If $$(X_1, X_2)$$ is discrete and $$f_2(x_2) > 0$$,

   $$
   f_{1 \mid 2}(x_1 \mid x_2) = \frac{f_{1,2}(x_1, x_2)}{f_2(x_2)} = \frac{P(X_1 = x_1, X_2 = x_2)}{P(X_2 = x_2)} = P(X_1 = x_1 \mid X_2 = x_2).
   $$

   ② $$P(X_1 \in A \mid X_2 = x_2) = \sum_{x_1 \in A} f_{1 \mid 2}(x_1 \mid x_2)$$.

   If $$(X_1, X_2)$$ is continuous, then even if $$f_2(x_2) > 0$$, $$f_{1 \mid 2}(x_1 \mid x_2)$$ has no real meaning as a probability. $$\rightarrow$$ The conditional pdf $$f_{1 \mid 2}(x_1 \mid x_2)$$ is the probability in a small neighborhood of $$x_2$$:

   $$
   P(X_1 \in A \mid x_2 \le X_2 \le x_2 + \Delta x_2) = \frac{P(X_1 \in A,\ x_2 \le X_2 \le x_2 + \Delta x_2)}{P(x_2 \le X_2 \le x_2 + \Delta x_2)}
   = \frac{\int_A \frac{1}{\Delta x_2}\int_{x_2}^{x_2 + \Delta x_2} f_{1,2}(x_1, t)\,dt\,dx_1}{\frac{1}{\Delta x_2}\int_{x_2}^{x_2 + \Delta x_2} f_2(t)\,dt}
   \approx \frac{\int_A f_{1,2}(x_1, x_2)\,dx_1}{f_2(x_2)} = \int_A \frac{f_{1,2}(x_1, x_2)}{f_2(x_2)}\,dx_1 = \int_A f_{1 \mid 2}(x_1 \mid x_2)\,dx_1,
   $$

   where "$$\approx$$" is the mean value theorem of integration (MVT of integration).

2. Let $$G(x) := P(X_1 \in A,\ X_2 \le x)$$ and $$F(x) := P(X_2 \le x)$$ ($$\rightarrow$$ the cdf of $$X_2$$). Then

   $$
   P(X_1 \in A \mid x_2 \le X_2 \le x_2 + \Delta x_2) = \frac{P(X_1 \in A,\ x_2 \le X_2 \le x_2 + \Delta x_2)}{P(x_2 \le X_2 \le x_2 + \Delta x_2)}
   = \frac{G(x_2 + \Delta x_2) - G(x_2)}{F(x_2 + \Delta x_2) - F(x_2)} \quad (\text{if } P(X_2 = x_2) = 0)
   \approx \frac{dG(x_2)}{dF(x_2)}.
   $$

   $$\rightarrow$$ the Radon–Nikodym derivative.

> **Theorem (Properties of conditional pdfs).**
>
> - (i) $$f_{1 \mid 2}(x_1 \mid x_2) \ge 0$$ for all $$x_1, x_2$$.
> - (ii) $$\displaystyle\sum_{x_1} f_{1 \mid 2}(x_1 \mid x_2) = 1$$ (discrete), $$\displaystyle\int f_{1 \mid 2}(x_1 \mid x_2)\,dx_1 = 1$$ (continuous), for all $$x_2$$ such that $$f_2(x_2) > 0$$.
{: .theorem #thm-conditional-pdf-properties }

> **Definition (Conditional cdf).**
>
> $$
> F_{1 \mid 2}(x_1 \mid x_2) =
> \begin{cases}
> \displaystyle\sum_{x \le x_1} P(X_1 = x \mid X_2 = x_2) & \text{(discrete)} \\[0.8em]
> \displaystyle\int_{-\infty}^{x_1} f_{1 \mid 2}(x \mid x_2)\,dx & \text{(continuous)}
> \end{cases}
> $$
>
> for all $$x_2$$ such that $$f_2(x_2) > 0$$.
{: .definition #def-conditional-cdf }

Note. $$F_{1 \mid 2}(x_1 \mid x_2) \overset{\Delta}{=} P(X_1 \le x_1 \mid X_2 = x_2)$$.

**Example 7.** $$(X, Y) \sim f_{1,2}(x, y) = e^{-y}I_{(0<x<y<\infty)}$$. (The region is the part of the first quadrant above the line $$y = x$$.)

$$
f_Y(y) = \int_0^y e^{-y}\,dx = y\,e^{-y}I_{(y>0)}, \qquad
f_{1 \mid 2}(x \mid y) = \frac{f_{1,2}(x, y)}{f_Y(y)} = \frac{e^{-y}I_{(0<x<y<\infty)}}{y\,e^{-y}I_{(y>0)}} = \frac{1}{y}I_{(0<x<y)}.
$$

$$\therefore\ X \mid Y = y \sim \mathcal{U}(0, y)$$ (uniform).

### 3.2 Conditional expectation

> **Definition (Conditional expectation).**
>
> $$
> E\bigl(u(X_1, X_2) \mid X_1 = x_1\bigr) :=
> \begin{cases}
> \displaystyle\sum_{x_2} u(x_1, x_2)\,f_{2 \mid 1}(x_2 \mid x_1) \\[0.8em]
> \displaystyle\int u(x_1, x_2)\,f_{2 \mid 1}(x_2 \mid x_1)\,dx_2.
> \end{cases}
> $$
{: .definition #def-conditional-expectation }

> **Theorem (Properties of conditional expectation).**
>
> - (i) $$E(aX_2 + b \mid X_1 = x_1) = a\,E(X_2 \mid X_1 = x_1) + b$$, $$a, b \in \mathbb{R}$$. Also $$E\bigl(c(X_1)X_2 \mid X_1 = x_1\bigr) = c(x_1)\,E(X_2 \mid X_1 = x_1)$$.
> - (ii) (Linearity.) $$E\bigl(u(X_2) + v(X_2) \mid X_1 = x_1\bigr) = E\bigl(u(X_2) \mid X_1 = x_1\bigr) + E\bigl(v(X_2) \mid X_1 = x_1\bigr)$$.
> - (iii) (Positivity.) $$u(x_2) \ge 0$$ for all $$x_2$$ $$\Rightarrow$$ $$E\bigl(u(X_2) \mid X_1 = x_1\bigr) \ge 0$$ for all $$x_1$$ such that it exists.
{: .theorem #thm-conditional-expectation-properties }

### 3.3 Conditional mean and variance

> **Definition (Conditional mean and variance).**
>
> - (i) $$E(X_2 \mid X_1 = x_1)$$.
> - (ii) $$\mathrm{Var}(X_2 \mid X_1 = x_1) = E\Bigl(\bigl(X_2 - E(X_2 \mid X_1 = x_1)\bigr)^2 \,\Big\vert\, X_1 = x_1\Bigr)$$.
{: .definition #def-conditional-mean-variance }

Note (meaning of the notation). $$E(X_2 \mid X_1)$$ is a new random variable (a function of $$X_1$$).

> **Theorem (Properties of conditional average and variance).**
>
> - (a) $$\mathrm{Var}(X_2 \mid X_1 = x_1) = E(X_2^2 \mid X_1 = x_1) - \{E(X_2 \mid X_1 = x_1)\}^2$$.
> - (b) (Repeated expectation value theorem.) If $$E\lvert X_2\rvert < \infty$$, then $$E\bigl(E(X_2 \mid X_1)\bigr) = E(X_2)$$.
> - (c) (Best predictor.)
>   - (i) $$\displaystyle\operatorname*{argmin}_{u(X_1)} E\bigl(X_2 - u(X_1)\bigr)^2 = E(X_2 \mid X_1)$$.
>   - (ii) For $$v(X_1)$$ such that $$E\,v(X_1)^2 < \infty$$, $$\mathrm{Cov}\bigl(X_2 - E(X_2 \mid X_1),\ v(X_1)\bigr) = 0$$.
> - (d) (EVVE rule.) $$\mathrm{Var}(X_2) = E\bigl(\mathrm{Var}(X_2 \mid X_1)\bigr) + \mathrm{Var}\bigl(E(X_2 \mid X_1)\bigr)$$.
{: .theorem #thm-conditional-average-variance }

*Proof.* (b) When continuous,

$$
E\bigl(E(X_2 \mid X_1)\bigr) = \int E(X_2 \mid X_1 = x_1)\,f_{X_1}(x_1)\,dx_1 = \iint x_2\,f_{2 \mid 1}(x_2 \mid x_1)\,dx_2\,f_1(x_1)\,dx_1 = \iint x_2\,f_{1,2}(x_1, x_2)\,dx_2\,dx_1 = E(X_2).
$$

(c) (i) When $$X_2$$ is predicted by $$X_1$$, the best predictor (as a function) is $$E(X_2 \mid X_1)$$. $$\rightarrow$$ But usually we do not know the joint distribution well. Prove (ii) first and then (i).

(ii) (Picture: the space of functions of $$X_1$$ (the space of the $$v(X_1)$$'s) drawn as a plane; $$X_2$$ is a vector outside it, $$E(X_2 \mid X_1)$$ is its foot on the plane, and $$X_2 - E(X_2 \mid X_1)$$ is the segment between them.) $$X_2 - E(X_2 \mid X_1)$$ is always orthogonal with $$v(X_1)$$. $$\rightarrow$$ In other words, the space of random variables can be handled as a vector space.

> **Theorem (Linear prediction).** Let $$0 < \mathrm{Var}(X_1),\ \mathrm{Var}(X_2) < \infty$$.
>
> - (a) $$\displaystyle\operatorname*{argmin}_{a + bX_1} E\bigl(X_2 - (a + bX_1)\bigr)^2 = \mu_2 + \sigma_{21}\sigma_{11}^{-1}(X_1 - \mu_1) = \mu_2 + \rho\,\sigma_2\,\frac{X_1 - \mu_1}{\sigma_1}$$, and
>
>   $$
>   \min_{a + bX_1} E\bigl(X_2 - (a + bX_1)\bigr)^2 = \sigma_{22} - \sigma_{21}\sigma_{11}^{-1}\sigma_{12} = \sigma_2^2(1 - \rho^2).
>   $$
>
>   Here $$\sigma_{21} = \mathrm{Cov}(X_1, X_2)$$, $$\sigma_{11} = \mathrm{Var}(X_1)$$, $$\sigma_i = \sqrt{\mathrm{Var}(X_i)}$$, $$\mu_i = E X_i$$ ($$i = 1, 2$$) $$\leftarrow$$ the prediction error.
> - (b) For some constants $$a, b$$, if $$E(X_2 \mid X_1) = a + bX_1$$, then $$E(X_2 \mid X_1) = \mu_2 + \rho\,\sigma_2\,\dfrac{X_1 - \mu_1}{\sigma_1}$$.
{: .theorem #thm-linear-prediction }

Note. What constant predicts $$X$$ best? $$\operatorname*{argmin}_c E(X - c)^2 = \mu = EX$$, and $$\min_c E(X - c)^2 = \sigma^2 = \mathrm{Var}(X)$$.

*Proof.* (a)

$$
\begin{aligned}
E\bigl(X_2 - (a + bX_1)\bigr)^2 &= E\bigl(X_2 - \mu_2 + \mu_2 - (a + bX_1) + (a + b\mu_1) - (a + b\mu_1)\bigr)^2 \\
&= E(X_2 - \mu_2)^2 + E\bigl(b(X_1 - \mu_1)\bigr)^2 - 2E\,b(X_2 - \mu_2)(X_1 - \mu_1) + 2(\mu_2 - a - b\mu_1)E(X_2 - \mu_2) - 2(\mu_2 - a - b\mu_1)E\bigl(b(X_1 - \mu_1)\bigr) + (\mu_2 - a - b\mu_1)^2 \\
&= \mathrm{Var}(X_2) + b^2\mathrm{Var}(X_1) - 2b\,\mathrm{Cov}(X_2, X_1) + (\mu_2 - a - b\mu_1)^2 \\
&= \sigma_2^2 + b^2\sigma_1^2 - 2b\sigma_{12} + (\mu_2 - b\mu_1 - a)^2 \\
&\ge \sigma_2^2 + b^2\sigma_1^2 - 2b\sigma_{12} \qquad (\text{when } a = \mu_2 - b\mu_1) \\
&= \Bigl(b\sigma_1 - \frac{\sigma_{12}}{\sigma_1}\Bigr)^2 + \sigma_2^2 - \frac{\sigma_{12}^2}{\sigma_1^2} \ \ge\ \sigma_2^2 - \frac{\sigma_{12}\sigma_{21}}{\sigma_{11}} \qquad (\text{when } b = \sigma_{12}/\sigma_{11}).
\end{aligned}
$$

$$\therefore\ a = \mu_2 - \mu_1\dfrac{\sigma_{12}}{\sigma_{11}}$$, and the predictor is $$\mu_2 - \mu_1\dfrac{\sigma_{12}}{\sigma_{11}} + \dfrac{\sigma_{12}}{\sigma_{11}}X_1 = \mu_2 + \dfrac{\sigma_{12}}{\sigma_{11}}(X_1 - \mu_1)$$. $$\square$$

**Correction.** The last expression was written with a minus sign, $$\mu_2 - \frac{\sigma_{12}}{\sigma_{11}}(X_1 - \mu_1)$$; the line just before it gives the plus sign, which is also the one in the statement of the theorem.


## Supplement from the textbook

> The parts below are in the textbook (§2.3) but not in my notes. They are translated from the book and are not my own writing.
{: .prompt-info }

**Conditional pdf, discrete case.** For a discrete $$(X, Y)$$ with joint pdf $$f_{1,2}(x, y)$$ and marginal pdf $$f_1(x)$$ of $$X$$, the function $$f_{2 \mid 1}(y \mid x) = \dfrac{f_{1,2}(x, y)}{f_1(x)} = \dfrac{P(X = x, Y = y)}{P(X = x)} = P(Y = y \mid X = x)$$ is the conditional pdf of $$Y$$ given $$X = x$$. It is defined for the values $$x$$ with $$P(X = x) > 0$$, so in the discrete case the conditional probability given a possible value is always defined.

**Example 2.3.1.** In Example 2.1.1 (two white, three black and four red balls; three balls drawn; $$X$$ white, $$Y$$ black), the conditional probabilities of $$Y$$ given that no white ball was drawn ($$X = 0$$) are $$P(Y = y \mid X = 0) = P(X = 0, Y = y)/P(X = 0)$$, $$y = 0, 1, 2, 3$$, namely $$\tfrac{4}{35}, \tfrac{18}{35}, \tfrac{12}{35}, \tfrac{1}{35}$$, which add up to $$1$$.

**Continuous case, in the book's words.** When $$(X, Y)$$ is continuous, $$P(c \le Y \le d,\ X = x) = 0$$ and $$P(X = x) = 0$$, so the definition of conditional probability of §1.2 cannot be used for the condition $$X = x$$. But for $$h > 0$$ one can consider $$P(c \le Y \le d \mid x \le X \le x + h) = \dfrac{P(c \le Y \le d,\ x \le X \le x + h)}{P(x \le X \le x + h)}$$. If the joint pdf $$f_{1,2}$$ and the marginal pdf $$f_1$$ are continuous, then as $$h \to 0$$,

$$
\frac{1}{h}P(c \le Y \le d,\ x \le X \le x + h) = \frac{1}{h}\int_x^{x+h}\Bigl\{\int_c^d f_{1,2}(s, y)\,dy\Bigr\}ds \to \int_c^d f_{1,2}(x, y)\,dy, \qquad \frac{1}{h}P(x \le X \le x + h) = \frac{1}{h}\int_x^{x+h}f_1(s)\,ds \to f_1(x),
$$

so for $$f_1(x) > 0$$ the function $$f_{2 \mid 1}(y \mid x) = f_{1,2}(x, y)/f_1(x)$$ satisfies $$\lim_{h \downarrow 0}P(c \le Y \le d \mid x \le X \le x + h) = \int_c^d f_{2 \mid 1}(y \mid x)\,dy$$. The left limit is defined as $$P(c \le Y \le d \mid X = x)$$, and $$f_{2 \mid 1}(y \mid x)$$ is the conditional pdf of $$Y$$ given $$X = x$$.

**Example 2.3.2.** From Examples 2.1.2 and 2.1.4, $$f_{1,2}(x, y) = 2e^{-x-y}I_{(0 \le x \le y)}$$ and $$f_1(x) = 2e^{-2x}I_{(x \ge 0)}$$. Hence, given $$X = x$$ ($$x \ge 0$$), $$f_{2 \mid 1}(y \mid x) = e^{-(y - x)}I_{(y \ge x)}$$, and

$$
P(Y \ge c \mid X = x) = \int_c^{\infty}e^{-(y - x)}I_{(y \ge x)}\,dy = \int_{c \vee x}^{\infty}e^{-(y - x)}\,dy = e^{-(c \vee x - x)}.
$$

> **Theorem 2.3.1 (Properties of conditional probability).**
>
> $$
> P(a \le X \le b,\ c \le Y \le d) =
> \begin{cases}
> \displaystyle\sum_{a \le x \le b}P(c \le Y \le d \mid X = x)f_1(x) & \text{(discrete)} \\[0.8em]
> \displaystyle\int_a^b P(c \le Y \le d \mid X = x)f_1(x)\,dx & \text{(continuous)}.
> \end{cases}
> $$
{: .theorem #thm-conditional-probability-total }

*Proof.* The discrete case is proved in the same way, so we prove the continuous case:

$$
\int_a^b P(c \le Y \le d \mid X = x)f_1(x)\,dx = \int_a^b\Bigl\{\int_c^d f_{2 \mid 1}(y \mid x)\,dy\Bigr\}f_1(x)\,dx = \int_a^b\int_c^d f_{1,2}(x, y)\,dy\,dx = P(a \le X \le b,\ c \le Y \le d). \qquad \square
$$

**Example 2.3.3.** For $$f_{1,2}(x, y) = 2e^{-x-y}I_{(0 \le x \le y)}$$, with $$f_1(x) = 2e^{-2x}I_{(x \ge 0)}$$ and $$P(Y \ge c \mid X = x) = e^{-(c \vee x - x)}$$,

$$
P(X \ge 2, Y \ge 3) = \int_2^{\infty}e^{-(3 \vee x - x)}2e^{-2x}\,dx = \int_2^3 2e^{-3-x}\,dx + \int_3^{\infty}2e^{-2x}\,dx = 2e^{-5} - e^{-6},
$$

the same as the result of Example 2.1.2.

**Example 2.3.4.** For $$f_{1,2}(x, y) = 120xy(1 - x - y)I_{(x \ge 0,\ y \ge 0,\ x + y \le 1)}$$ and $$f_1(x) = 20x(1 - x)^3I_{(0 \le x \le 1)}$$, the conditional pdf of $$Y$$ given $$X = x$$ is $$f_{2 \mid 1}(y \mid x) = \dfrac{6y(1 - x - y)}{(1 - x)^3}I_{(0 \le y \le 1 - x)}$$, and the conditional mean is

$$
\mu_{2 \mid 1}(x) = E(Y \mid X = x) = \int_0^{1-x}y\cdot 6y(1 - x - y)/(1 - x)^3\,dy = (1 - x)/2.
$$

**Conditional expectation and conditional variance in the book.** Given $$X = x$$, for a real-valued function $$g(x, y)$$, $$E(g(X, Y) \mid X = x) = \sum_y g(x, y)f_{2 \mid 1}(y \mid x)$$ or $$\int g(x, y)f_{2 \mid 1}(y \mid x)\,dy$$ if it is a real number. With $$\mu_{2 \mid 1}(x) = E(Y \mid X = x)$$, the conditional variance is $$\mathrm{Var}(Y \mid X = x) = E[(Y - \mu_{2 \mid 1}(x))^2 \mid X = x]$$, also written $$\sigma^2_{2 \mid 1}(x)$$.

**Proof of the calculation formula $$\mathrm{Var}(Y \mid X = x) = E(Y^2 \mid X = x) - \{E(Y \mid X = x)\}^2$$.**

$$
\begin{aligned}
\mathrm{Var}(Y \mid X = x) &= E[(Y - \mu_{2 \mid 1}(x))^2 \mid X = x] = E[Y^2 - 2\mu_{2 \mid 1}(x)Y + \mu_{2 \mid 1}^2(x) \mid X = x] \\
&= E(Y^2 \mid X = x) - 2\mu_{2 \mid 1}^2(x) + \mu_{2 \mid 1}^2(x) = E(Y^2 \mid X = x) - \{E(Y \mid X = x)\}^2. \qquad \square
\end{aligned}
$$

**Example 2.3.5.** In Example 2.3.4, $$E(Y^2 \mid X = x) = \int_0^{1-x}y^2\cdot 6y(1 - x - y)/(1 - x)^3\,dy$$, so $$\mathrm{Var}(Y \mid X = x) = E(Y^2 \mid X = x) - \{E(Y \mid X = x)\}^2 = (1 - x)^2/20$$.

**The conditional expectation as a random variable.** $$\mu_{2 \mid 1}(x) = E(Y \mid X = x)$$ is a function of $$x$$, so $$\mu_{2 \mid 1}(X)$$ is a new random variable taking the values $$\mu_{2 \mid 1}(x)$$ according to the distribution of $$X$$; it is written $$E(Y \mid X)$$, and in the same way $$\mathrm{Var}(Y \mid X) = \sigma^2_{2 \mid 1}(X)$$. In general, if $$h(x) = E[g(Y) \mid X = x]$$, then $$E[g(Y) \mid X] = h(X)$$.

**Example 2.3.6.** From Examples 2.3.4 and 2.3.5, $$E(Y \mid X) = (1 - X)/2$$ and $$\mathrm{Var}(Y \mid X) = (1 - X)^2/20$$.

**Proof of the properties of conditional expectation as a random variable.** Let $$(X, Y)$$ be continuous (the discrete case replaces integrals by sums).

(b) Let $$Z = Y - E(Y \mid X)$$. By the properties of conditional expectation and (a), $$E(Z \mid X) = E(Y \mid X) - E\{E(Y \mid X) \mid X\} = E(Y \mid X) - E(Y \mid X) = 0$$ and $$E(Z) = E[E(Z \mid X)] = 0$$. By the calculation formula for covariance,

$$
\mathrm{Cov}(Z, v(X)) = E(Zv(X)) - E(Z)E(v(X)) = E\{E(Zv(X) \mid X)\} = E\{v(X)E(Z \mid X)\} = 0. \qquad \square
$$

**Example 2.3.7.** For $$f_{1,2}(x, y) = 120xy(1 - x - y)I_{(x \ge 0,\ y \ge 0,\ x + y \le 1)}$$, $$E(Y \mid X) = (1 - X)/2$$, so $$E[E(Y \mid X)] = (1 - E(X))/2 = 1/3 = E(Y)$$, because $$E(X) = E(Y) = 1/3$$. Also $$\mathrm{Cov}(Y - E(Y \mid X), X) = E[\{Y - (1 - X)/2\}X] = E(XY) - (E(X) - E(X^2))/2 = \tfrac{2}{21} - (\tfrac{1}{3} - \tfrac{1}{7})/2 = 0$$.

**Remark (regression function).** The conditional mean $$E(Y \mid X)$$ has a special meaning for describing the relation between $$Y$$ and $$X$$: as the next theorem says, it is the function of $$X$$ that predicts $$Y$$ "best", and it is usually called the *regression function*.

> **Theorem 2.3.5 (Least squares predictor).** Among functions $$u(X)$$ of $$X$$, the one minimizing $$E[(Y - u(X))^2]$$ is $$E(Y \mid X)$$, i.e.
>
> $$
> E[(Y - E(Y \mid X))^2] \le E[(Y - u(X))^2] \quad \forall u(X),
> $$
>
> and the minimum of the mean squared prediction error is $$E[(Y - E(Y \mid X))^2] = E[\mathrm{Var}(Y \mid X)]$$.
{: .theorem #thm-least-squares-predictor }

*Proof.* The key is to decompose the prediction error into a sum of two uncorrelated random variables: $$Y - u(X) = (Y - E(Y \mid X)) \oplus (E(Y \mid X) - u(X))$$ (the symbol $$\oplus$$ is used when the correlation between the summands is $$0$$). Put $$v(X) = E(Y \mid X) - u(X)$$. Then

$$
(Y - u(X))^2 = (Y - E(Y \mid X))^2 + 2(Y - E(Y \mid X))v(X) + v^2(X),
$$

and $$E[(Y - E(Y \mid X))v(X)] = \mathrm{Cov}(Y - E(Y \mid X), v(X)) = 0$$, so $$E[(Y - u(X))^2] = E[(Y - E(Y \mid X))^2] + E[v^2(X)] \ge E[(Y - E(Y \mid X))^2]$$. Moreover, with $$W = (Y - E(Y \mid X))^2$$, $$E(W \mid X) = \mathrm{Var}(Y \mid X)$$, so $$E[(Y - E(Y \mid X))^2] = E(W) = E[E(W \mid X)] = E[\mathrm{Var}(Y \mid X)]$$. $$\square$$

> **Theorem 2.3.6 (Decomposition of the variance).** $$\mathrm{Var}(Y) = E[\mathrm{Var}(Y \mid X)] + \mathrm{Var}[E(Y \mid X)]$$.
{: .theorem #thm-variance-decomposition }

*Proof.* Let $$\mu = E(Y)$$. The deviation decomposes as $$Y - \mu = (Y - E(Y \mid X)) \oplus (E(Y \mid X) - \mu)$$. Since $$E[(Y - E(Y \mid X))(E(Y \mid X) - \mu)] = \mathrm{Cov}(Y - E(Y \mid X), E(Y \mid X)) = 0$$, $$E[(Y - \mu)^2] = E[(Y - E(Y \mid X))^2] + E[(E(Y \mid X) - \mu)^2]$$, and since $$E[E(Y \mid X)] = E(Y) = \mu$$, $$\mathrm{Var}(Y) = E[\mathrm{Var}(Y \mid X)] + \mathrm{Var}[E(Y \mid X)]$$. $$\square$$

**Example 2.3.8.** For $$f_{1,2}(x, y) = 120xy(1 - x - y)I_{(x \ge 0,\ y \ge 0,\ x + y \le 1)}$$: $$E(Y \mid X) = (1 - X)/2$$, $$\mathrm{Var}(Y \mid X) = (1 - X)^2/20$$, $$E(X) = 1/3$$, $$E(X^2) = 1/7$$, $$\mathrm{Var}(X) = 2/63$$. Therefore

$$
\mathrm{Var}[E(Y \mid X)] + E[\mathrm{Var}(Y \mid X)] = \mathrm{Var}(X)/4 + [E(X^2) - 2E(X) + 1]/20 = \frac{2}{63},
$$

which agrees with $$\mathrm{Var}(Y) = 2/63$$ of Example 2.2.4.

**Picture of the three theorems.** Theorems 2.3.4, 2.3.5 and 2.3.6 can be visualized by a right triangle in the space of random variables: $$Y - E(Y) = (Y - E(Y \mid X)) \oplus (E(Y \mid X) - E(Y))$$, where the right angle expresses that the two parts are uncorrelated. This decomposition of the deviation $$Y - E(Y)$$ divides the reason why the response $$Y$$ takes different values into the part due to the explanatory variable $$X$$, $$(E(Y \mid X) - E(Y))$$, and the rest, $$(Y - E(Y \mid X))$$. This idea is the basis of the regression analysis and analysis of variance introduced in Chapter 10.

## References

- 김우철, *수리통계학* (Mathematical Statistics), revised 2nd edition, 민영사, 2021 — Chapter 2, §2.3.
- Mathematical Statistics 1 (326.311), Seoul National University, Spring 2025. Instructor: Jaeyong Lee (이재용). My handwritten lecture notes, Chapter 2 section 3.
- The notes are translated without changing their wording; remarks written in the margins are kept. The proof of part (a) of the linear prediction theorem ends in a sign slip, corrected where marked. The proofs of parts (c)(i) and (d) of the conditional average and variance theorem are not written out in my notes; they are in the supplement (Theorems 2.3.5 and 2.3.6 of the book).

[Previous](/posts/mathstat1-joint-characteristics/) · [Overview](/posts/mathstat1-overview/) · [Next](/posts/mathstat1-independence/)
