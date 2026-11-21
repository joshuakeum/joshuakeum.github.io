---
title: "Mathematical Statistics 1: Ch. 3 Part 4 — Gamma-Related Distributions"
date: 2026-11-21 11:40:00 +0900
categories: [Study Notes, Mathematical Statistics 1]
tags: [gamma, exponential, chi-square, beta, dirichlet, gamma function, beta function, poisson process, waiting time]
description: The waiting time of a Poisson process, the gamma and beta functions, and the gamma, exponential, chi-square, beta and Dirichlet distributions. Chapter 3, notes section 3 of Mathematical Statistics 1.
math: true
mermaid: false
render_with_liquid: false
---

> My handwritten notes, translated into English. Chapter 3, notes section 3, "Distributions related to the gamma distribution". It corresponds to §3.5 of the textbook. Statements and proofs follow my notes. Material taken from the textbook (the proofs of the mean and variance and of additivity of the gamma distribution) is collected at the end under "Supplement from the textbook". The exercises are in [Chapter 3 Exercises](/posts/mathstat1-exercises-chapter-3/).
{: .prompt-info }

## 3. Distributions related to the gamma distribution

### 3.1 Waiting time of a Poisson process

> **Theorem.** Let $$(N_t, t \ge 0) \sim \mathrm{PP}(\lambda)$$, $$\lambda > 0$$. Also let $$W_r = \min\{t : N_t \ge r\}$$, $$r = 1, 2, \dots$$ Then
>
> - (i) $$W_r \sim \mathrm{Gamma}(r, \tfrac{1}{\lambda})$$ (pdf: $$f(t) = \dfrac{\lambda^rt^{r-1}e^{-\lambda t}}{(r-1)!}$$, $$t > 0$$);
> - (ii) $$W_1, W_2 - W_1, \dots \overset{iid}{\sim} \mathrm{Gamma}(1, \tfrac{1}{\lambda}) = \mathrm{Exp}(\tfrac{1}{\lambda})$$.
{: .theorem #thm-poisson-waiting-time }

cf) $$W_r$$ is the waiting time until the $$r$$-th event. The differences $$W_1, W_2 - W_1, W_3 - W_2, \dots$$ are the interarrival times of the jumps of $$N_t$$.

*Proof.* Let us first find the cdf: $$F(t) = 1 - P(W_r > t)$$. Here

$$
P(W_r > t) = P(N_t \le r - 1) = \sum_{k=0}^{r-1}\frac{e^{-\lambda t}(\lambda t)^k}{k!}, \qquad\therefore\quad F(t) = 1 - \sum_{k=0}^{r-1}\frac{e^{-\lambda t}(\lambda t)^k}{k!}.
$$

Therefore

$$
f(t) = \frac{d}{dt}F(t) = \lambda e^{-\lambda t}\sum_{k=0}^{r-1}\frac{(\lambda t)^k}{k!} - e^{-\lambda t}\sum_{k=1}^{r-1}\frac{\lambda(\lambda t)^{k-1}}{(k-1)!}
= \lambda e^{-\lambda t}\Bigl(\sum_{k=0}^{r-1}\frac{(\lambda t)^k}{k!} - \sum_{k=0}^{r-2}\frac{(\lambda t)^k}{k!}\Bigr)
$$

$$
= \lambda e^{-\lambda t}\frac{(\lambda t)^{r-1}}{(r-1)!} = \frac{e^{-\lambda t}\lambda^rt^{r-1}}{(r-1)!}. \qquad \square
$$

### 3.2 Gamma function

> **Definition (Gamma function).**
>
> $$
> \Gamma(x) = \int_0^{\infty}t^{x-1}e^{-t}\,dt, \qquad x > 0; \qquad \Gamma(1) = 1.
> $$
{: .definition #def-gamma-function }

> **Lemma.** $$\Gamma(x) < \infty$$ for all $$x > 0$$.
{: .theorem #lem-gamma-finite }

*Proof.* By yourself.

> **Theorem (Properties).**
>
> - (1) $$\Gamma(x + 1) = x\Gamma(x)$$, $$x > 0$$.
> - (2) $$\Gamma(n + 1) = n!$$, $$n = 1, 2, \dots$$
> - (3) $$\log\Gamma(x)$$ is convex on $$(0, \infty)$$.
{: .theorem #thm-gamma-function-properties }

*Proof.* (1) Integration by parts.

(2) $$\Gamma(1) = \int_0^{\infty}e^{-t}\,dt = 1$$, $$\Gamma(2) = 1\cdot\Gamma(1)$$, $$\Gamma(3) = 2\Gamma(2) = 2 \times 1 \times \Gamma(1)$$, $$\dots$$ Therefore $$\Gamma(n + 1) = n!\,\Gamma(1) = n!$$.

(3) Use Hölder's inequality. $$\square$$

### 3.3 Beta function

> **Definition (Beta function).** $$B(x, y) := \displaystyle\int_0^1t^{x-1}(1 - t)^{y-1}\,dt$$, $$x, y > 0$$.
{: .definition #def-beta-function }

> **Theorem.**
>
> - (1) $$B(x, y)$$ is integrable no matter what $$x, y > 0$$ are given.
> - (2) $$\Gamma(x) = 2\displaystyle\int_0^{\infty}s^{2x-1}e^{-s^2}\,ds$$, $$x > 0$$.
> - (3) $$2\displaystyle\int_0^{\pi/2}(\sin\theta)^{2x-1}(\cos\theta)^{2y-1}\,d\theta = \dfrac{\Gamma(x)\Gamma(y)}{\Gamma(x + y)}$$.
> - (4) $$B(x, y) = \dfrac{\Gamma(x)\Gamma(y)}{\Gamma(x + y)}$$.
> - (5) $$\Gamma(\tfrac{1}{2}) = \sqrt{\pi}$$.
> - (6) $$\displaystyle\int_{-\infty}^{\infty}e^{-s^2}\,ds = \sqrt{\pi}$$ and $$\displaystyle\int_{-\infty}^{\infty}e^{-\frac{1}{2}s^2}\,ds = \sqrt{2\pi}$$.
{: .theorem #thm-beta-function }

*Proof.* (2) Substituting $$t = s^2$$,

$$
\Gamma(x) = \int_0^{\infty}t^{x-1}e^{-t}\,dt = \int_0^{\infty}(s^2)^{x-1}e^{-s^2}\,2s\,ds = 2\int_0^{\infty}s^{2x-1}e^{-s^2}\,ds.
$$

(3) Let

$$
I = \iint_{s, t \ge 0}e^{-s^2-t^2}s^{2x-1}t^{2y-1}\,ds\,dt = \int_0^{\infty}e^{-s^2}s^{2x-1}\,ds\int_0^{\infty}e^{-t^2}t^{2y-1}\,dt = \frac{1}{4}\Gamma(x)\Gamma(y).
$$

In polar coordinates ($$r\sin\theta = s$$, $$r\cos\theta = t$$, $$ds\,dt = r\,dr\,d\theta$$),

$$
I = \int_0^{\pi/2}\int_0^{\infty}re^{-r^2}(r\sin\theta)^{2x-1}(r\cos\theta)^{2y-1}\,dr\,d\theta = \int_0^{\pi/2}(\sin\theta)^{2x-1}(\cos\theta)^{2y-1}\,d\theta\int_0^{\infty}r^{2x+2y-1}e^{-r^2}\,dr
$$

$$
= \frac{1}{2}\Gamma(x + y)\int_0^{\pi/2}(\sin\theta)^{2x-1}(\cos\theta)^{2y-1}\,d\theta.
$$

$$\therefore\ 2\displaystyle\int_0^{\pi/2}(\sin\theta)^{2x-1}(\cos\theta)^{2y-1}\,d\theta = \dfrac{\Gamma(x)\Gamma(y)}{\Gamma(x + y)}$$.

(4) $$B(x, y) = \displaystyle\int_0^1t^{x-1}(1 - t)^{y-1}\,dt$$; substituting $$t = \sin^2\theta$$, $$dt = 2\sin\theta\cos\theta\,d\theta$$,

$$
B(x, y) = \int_0^{\pi/2}\sin^{2x-2}\theta\,\cos^{2y-2}\theta\cdot 2\sin\theta\cos\theta\,d\theta = 2\int_0^{\pi/2}(\cos\theta)^{2y-1}(\sin\theta)^{2x-1}\,d\theta = \frac{\Gamma(x)\Gamma(y)}{\Gamma(x + y)}.
$$

(5) Put $$x = y = \tfrac{1}{2}$$ in (3): $$2\int_0^{\pi/2}d\theta = \pi = \dfrac{\Gamma(\frac{1}{2})^2}{\Gamma(1)}$$, so $$\Gamma(\tfrac{1}{2})^2 = \pi$$ ($$\because \Gamma(1) = 1$$).

(6) $$\Gamma(\tfrac{1}{2}) = 2\displaystyle\int_0^{\infty}e^{-s^2}\,ds = \int_{-\infty}^{\infty}e^{-s^2}\,ds$$ ($$\because$$ even function). $$\square$$

### 3.4 Gamma distribution

> **Notation.** $$X \sim \mathrm{Ga}(\alpha, \beta)$$, $$\alpha, \beta > 0$$. Here $$\alpha$$ is the shape parameter and $$\beta$$ is the scale parameter. cf) $$\lambda = \frac{1}{\beta}$$ is the rate parameter. (Looking at the pdf, one can see what effect each parameter has.)
{: .definition #def-gamma-distribution }

**Properties.**

1. PDF: $$f(x) = \dfrac{1}{\Gamma(\alpha)\beta^{\alpha}}x^{\alpha-1}e^{-x/\beta}$$, $$x > 0$$.
2. MGF: $$M_X(t) = (1 - \beta t)^{-\alpha}$$, $$t < \dfrac{1}{\beta}$$.
3. $$E(X) = \alpha\beta$$, $$\mathrm{Var}(X) = \alpha\beta^2$$, $$E(X^k) = [\alpha]_k\beta^k$$, where $$[\alpha]_k = \alpha(\alpha + 1)\cdots(\alpha + k - 1)$$.
4. (CGF) $$C_X(t) = -\alpha\log(1 - \beta t)$$, $$t < \dfrac{1}{\beta}$$; $$C_r = (r - 1)!\,\alpha\beta^r$$ ($$r \ge 1$$).
5. ① If $$X_i \overset{indep}{\sim} \mathrm{Ga}(\alpha_i, \beta)$$, $$i = 1, \dots, k$$, then $$X_1 + \cdots + X_k \sim \mathrm{Ga}(\alpha_1 + \cdots + \alpha_k, \beta)$$.

   ② $$X \sim \mathrm{Ga}(r, \beta)$$, $$r \in \mathbb{N}$$ $$\iff$$ $$X \overset{d}{=} Z_1 + \cdots + Z_r$$, $$Z_i \overset{iid}{\sim} \mathrm{Ga}(1, \beta)$$.
6. $$X \sim \mathrm{Ga}(\alpha, \lambda) \Rightarrow cX \sim \mathrm{Ga}(\alpha, \lambda/c)$$ ($$c > 0$$), where the second parameter is the rate $$\lambda$$.
7. $$\mathrm{Ga}(1, \lambda) = \mathrm{Exp}(\lambda)$$ $$\to$$ the definition of the exponential distribution. $$\mathrm{Ga}(\tfrac{\nu}{2}, \lambda = \tfrac{1}{2}) = \chi^2(\nu)$$ ($$\nu > 0$$) $$\to$$ the definition of the $$\chi^2$$-distribution.

cf) The pdf in the two parametrizations:

$$
f_{\alpha, \beta}(x) = \frac{1}{\Gamma(\alpha)\beta^{\alpha}}x^{\alpha-1}e^{-x/\beta}, \qquad f_{\alpha, \lambda}(x) = \frac{\lambda^{\alpha}}{\Gamma(\alpha)}x^{\alpha-1}e^{-\lambda x}.
$$

*Proof.* (2) The MGF:

$$
M_X(t) = E(e^{tX}) = \int_{-\infty}^{\infty}e^{tx}\frac{1}{\Gamma(\alpha)\beta^{\alpha}}x^{\alpha-1}e^{-x/\beta}\,dx = \frac{1}{\Gamma(\alpha)}\cdot\frac{1}{\beta^{\alpha}}\int_0^{\infty}e^{tx - \frac{x}{\beta}}x^{\alpha-1}\,dx = \frac{1}{\Gamma(\alpha)}\cdot\frac{1}{\beta^{\alpha}}\Gamma(\alpha)\Bigl(\frac{1}{\beta} - t\Bigr)^{-\alpha} = (1 - \beta t)^{-\alpha}. \qquad \square
$$

### 3.5 Exponential distribution

> **Notation.** $$X \sim \mathrm{Exp}(\beta)$$, $$\beta > 0$$. $$\beta$$: scale, $$\lambda$$: rate.
{: .definition #def-exponential }

**Properties.**

1. (Definition) $$\mathrm{Exp}(\beta) = \mathrm{Ga}(1, \beta)$$.
2. (PDF) $$f(x) = \dfrac{1}{\beta}e^{-x/\beta}$$, $$x > 0$$ (equivalently $$f(x) = \lambda e^{-\lambda x}$$, $$x > 0$$, $$\lambda = \frac{1}{\beta}$$).
3. (CDF) $$F(x) = 1 - e^{-x/\beta}$$, $$x \ge 0$$.
4. Survival function: $$P(X > x) = e^{-x/\beta}$$ ($$x \ge 0$$). (This is the definition of the survival function.)
5. $$M_X(t) = \dfrac{1}{1 - \beta t}$$, $$t < \dfrac{1}{\beta}$$; $$C_X(t) = -\log(1 - \beta t)$$.
6. $$E(X) = \beta$$, $$\mathrm{Var}(X) = \beta^2$$.

### 3.6 $$\chi^2$$-distribution

> **Definition.** $$\chi^2(r) = \mathrm{Ga}(\tfrac{r}{2}, 2)$$ (the second parameter is the scale parameter), where $$r$$ is the degrees of freedom (d.o.f.), $$r > 0$$.
{: .definition #def-chi-square }

**Properties.**

1. (PDF) $$f(x) = \dfrac{1}{\Gamma(r/2)2^{r/2}}x^{\frac{r}{2}-1}e^{-\frac{1}{2}x}$$, $$x > 0$$.
2. $$M_X(t) = (1 - 2t)^{-r/2}$$, $$t < \dfrac{1}{2}$$; $$C_X(t) = -\dfrac{r}{2}\log(1 - 2t)$$.
3. $$E(X) = r$$, $$\mathrm{Var}(X) = 2r$$.
4. If $$X_i \overset{indep}{\sim} \chi^2(r_i)$$, $$i = 1, \dots, k$$, then $$X_1 + \cdots + X_k \sim \chi^2(r_1 + \cdots + r_k)$$. Also $$X \sim \chi^2(r) \iff X \overset{d}{=} Z_1 + \cdots + Z_r$$, $$Z_i \overset{iid}{\sim} \chi^2(1)$$.

### 3.7 Beta distribution

> **Notation.** $$X \sim \mathrm{Beta}(\alpha, \beta)$$, $$\alpha, \beta > 0$$.
{: .definition #def-beta-distribution }

**Properties.**

1. (PDF) $$f(x) = \dfrac{\Gamma(\alpha + \beta)}{\Gamma(\alpha)\Gamma(\beta)}x^{\alpha-1}(1 - x)^{\beta-1}$$, $$x \in (0, 1)$$. (The constant is $$1/B(\alpha, \beta)$$.)
2. $$E(X) = \dfrac{\alpha}{\alpha + \beta}$$, $$\mathrm{Var}(X) = \dfrac{\alpha\beta}{(\alpha + \beta)^2(\alpha + \beta + 1)}$$.
3. If $$X_1 \sim \mathrm{Ga}(\alpha, 1)$$ and $$X_2 \sim \mathrm{Ga}(\beta, 1)$$ and $$X_1 \perp X_2$$, then $$X_1 + X_2 \perp \dfrac{X_1}{X_1 + X_2}$$, $$X_1 + X_2 \sim \mathrm{Ga}(\alpha + \beta, 1)$$ and $$\dfrac{X_1}{X_1 + X_2} \sim \mathrm{Beta}(\alpha, \beta)$$.

*Proof.* (3) Let $$Y_1 = \dfrac{X_1}{X_1 + X_2}$$ and $$Y_2 = X_1 + X_2$$. The joint density of $$(X_1, X_2)$$ is

$$
f_{X_1, X_2}(x_1, x_2) = \frac{1}{\Gamma(\alpha)}x_1^{\alpha-1}e^{-x_1}\frac{1}{\Gamma(\beta)}x_2^{\beta-1}e^{-x_2}I_{(x_1 > 0,\ x_2 > 0)} = \frac{1}{\Gamma(\alpha)\Gamma(\beta)}x_1^{\alpha-1}x_2^{\beta-1}e^{-x_1-x_2}I_{(x_1 > 0,\ x_2 > 0)}.
$$

With $$x_1 = y_1y_2$$ and $$x_2 = y_2 - y_1y_2 = (1 - y_1)y_2$$, the Jacobian is

$$
\det\begin{pmatrix}y_2 & y_1 \\ -y_2 & 1 - y_1\end{pmatrix} = y_2(1 - y_1) + y_1y_2 = y_2.
$$

Therefore

$$
f_{Y_1, Y_2}(y_1, y_2) = \frac{1}{\Gamma(\alpha)\Gamma(\beta)}(y_1y_2)^{\alpha-1}\bigl((1 - y_1)y_2\bigr)^{\beta-1}e^{-y_2}\cdot y_2\,I_{(0 < y_1 < 1,\ y_2 > 0)}
$$

$$
= \frac{\Gamma(\alpha + \beta)}{\Gamma(\alpha)\Gamma(\beta)}y_1^{\alpha-1}(1 - y_1)^{\beta-1}I_{(0 < y_1 < 1)}\cdot\frac{1}{\Gamma(\alpha + \beta)}y_2^{\alpha+\beta-1}e^{-y_2}I_{(y_2 > 0)} = f_{Y_1}(y_1)f_{Y_2}(y_2).
$$

$$\therefore$$ $$Y_1, Y_2$$ are independent, $$Y_1 \sim \mathrm{Beta}(\alpha, \beta)$$ and $$Y_2 \sim \mathrm{Ga}(\alpha + \beta, 1)$$. (This result alone also proves that the Beta density integrates to $$1$$, that is, that it is a pdf.) $$\square$$

### 3.8 Dirichlet distribution

> **Notation.** $$(Y_1, \dots, Y_k) \sim \mathrm{Dir}(\alpha_1, \dots, \alpha_{k+1})$$, $$\alpha_1, \dots, \alpha_{k+1} > 0$$.
{: .definition #def-dirichlet }

**Properties.**

1. (PDF)

   $$
   f_{Y_1, \dots, Y_k}(y_1, \dots, y_k) = \frac{\Gamma(\alpha_1 + \cdots + \alpha_{k+1})}{\Gamma(\alpha_1)\cdots\Gamma(\alpha_{k+1})}y_1^{\alpha_1-1}\cdots y_k^{\alpha_k-1}(1 - y_1 - \cdots - y_k)^{\alpha_{k+1}-1},
   $$

   $$y_1, \dots, y_k > 0$$, $$0 < \sum_{i=1}^{k}y_i < 1$$.
2. With $$\alpha_0 := \sum_{i=1}^{k+1}\alpha_i$$,

   $$
   E(Y_1) = \frac{\alpha_1}{\alpha_0}, \qquad \mathrm{Var}(Y_1) = \frac{\alpha_1(\alpha_2 + \cdots + \alpha_{k+1})}{\alpha_0^2(\alpha_0 + 1)}, \qquad \mathrm{Cov}(Y_1, Y_2) = -\frac{\alpha_1\alpha_2}{\alpha_0^2(\alpha_0 + 1)}.
   $$
3. If $$X_i \overset{indep}{\sim} \mathrm{Ga}(\alpha_i, 1)$$, $$i = 1, \dots, k + 1$$, and

   $$
   (Y_1, \dots, Y_k) = \Bigl(\frac{X_1}{\sum_{i=1}^{k+1}X_i}, \dots, \frac{X_k}{\sum_{i=1}^{k+1}X_i}\Bigr) \quad\text{and}\quad Y_{k+1} = \sum_{i=1}^{k+1}X_i,
   $$

   then $$(Y_1, \dots, Y_k) \sim \mathrm{Dir}(\alpha_1, \dots, \alpha_{k+1})$$, $$Y_{k+1} \sim \mathrm{Ga}\bigl(\sum_{i=1}^{k+1}\alpha_i, 1\bigr)$$ and $$(Y_1, \dots, Y_k) \perp Y_{k+1}$$.

## Supplement from the textbook

**Mean and variance of the gamma distribution (Theorem 3.5.2).** Substituting $$x/\beta = y$$, the expectations of $$X$$ and $$X^2$$ are

$$
\int_0^{\infty}x\frac{1}{\Gamma(\alpha)\beta^{\alpha}}x^{\alpha-1}e^{-x/\beta}\,dx = \frac{\beta}{\Gamma(\alpha)}\int_0^{\infty}y^{\alpha}e^{-y}\,dy = \frac{\Gamma(\alpha + 1)}{\Gamma(\alpha)}\beta = \alpha\beta, \qquad E(X^2) = \frac{\Gamma(\alpha + 2)}{\Gamma(\alpha)}\beta^2 = \alpha(\alpha + 1)\beta^2,
$$

so $$E(X) = \alpha\beta$$ and $$\mathrm{Var}(X) = \alpha(\alpha + 1)\beta^2 - (\alpha\beta)^2 = \alpha\beta^2$$.

**Additivity (property 5).** By Theorem 2.5.11 and the mgf, $$mgf_{X_1 + X_2}(t) = (1 - \beta t)^{-\alpha_1}(1 - \beta t)^{-\alpha_2} = (1 - \beta t)^{-\alpha_1 - \alpha_2}$$, $$t < 1/\beta$$, which is the mgf of $$\mathrm{Ga}(\alpha_1 + \alpha_2, \beta)$$; by the uniqueness of the mgf, $$X_1 + X_2 \sim \mathrm{Ga}(\alpha_1 + \alpha_2, \beta)$$.

**Exponential distribution (Theorem 3.5.1).** In a Poisson process with occurrence rate $$\lambda$$, the time $$W_1$$ until the first occurrence satisfies $$(W_1 > t) = (N_t = 0)$$, so $$P(W_1 > t) = e^{-\lambda t}$$ and the pdf is $$\lambda e^{-\lambda x}I_{(x \ge 0)}$$; the textbook writes $$W_1 \sim \mathrm{Exp}(1/\lambda)$$. Its mgf is $$(1 - t/\lambda)^{-1}$$, $$t < \lambda$$, the cumulant generating function $$-\log(1 - t/\lambda) = t/\lambda + (t/\lambda)^2/2 + \cdots$$ gives $$E(W_1) = 1/\lambda$$ and $$\mathrm{Var}(W_1) = 1/\lambda^2$$. The shape of the gamma density depends mainly on $$r$$ (for $$r = 0.5$$, $$\lambda = 1$$ the density decreases steeply from a vertical asymptote at $$0$$; for $$r = 3$$, $$\lambda = 1$$ it is a hump with its peak at $$2$$), which is why $$r$$ is called the shape parameter and $$\beta = 1/\lambda$$ the scale parameter. The gamma distribution with natural-number shape can also be defined representationally: $$\mathrm{Gamma}(r, \beta) \overset{d}{=} \mathrm{Exp}_1(\beta) \oplus \cdots \oplus \mathrm{Exp}_r(\beta)$$.

## References

- 김우철, *수리통계학* (Mathematical Statistics), revised 2nd edition, 민영사, 2021 — Chapter 3, §3.5 (Theorems 3.5.1 and 3.5.2). The supplement is translated from the book.
- Mathematical Statistics 1 (326.311), Seoul National University, Spring 2025. Instructor: Jaeyong Lee (이재용).

[Previous](/posts/mathstat1-poisson/) · [Overview](/posts/mathstat1-overview/) · [Next](/posts/mathstat1-normal/)
