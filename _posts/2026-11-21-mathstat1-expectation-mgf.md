---
title: "Mathematical Statistics 1: Ch. 1 Part 4 — Expectation, Moments and Generating Functions"
date: 2026-11-21 08:40:00 +0900
categories: [Study Notes, Mathematical Statistics 1]
tags: [expectation, variance, mgf, cumulant, moments]
description: Expectation and its properties, variance, skewness and kurtosis, moment generating functions, and cumulant generating functions. Chapter 1, notes section 4 of Mathematical Statistics 1.
math: true
mermaid: false
render_with_liquid: false
---

> My handwritten notes, translated into English. Section 4 of Chapter 1 in my notes. It corresponds to §1.4 and the second half of §1.5 of the textbook. Statements and proofs follow my notes; I only corrected expressions that were mathematically wrong. Material taken from the textbook is collected at the end under "Supplement from the textbook".
{: .prompt-info }

## 4.1 Expectation

> **Definition (Expectation of a random variable $$X$$).** $$X \sim f$$, $$f$$: the density function.
>
> - (a) ($$X$$ continuous.) Under the condition $$\int \lvert x\rvert  f(x)\,dx < \infty$$, define $$E(X) := \int x f(x)\,dx$$.
> - (b) ($$X$$ discrete.) Under the condition $$\sum_x \lvert x\rvert  f(x) < \infty$$, define $$E(X) := \sum_x x f(x)$$.
{: .definition #def-expectation }

\* The definition above is not perfect: it does not reflect the cases that are neither continuous nor discrete.

cf)

$$
E(X) := \int x\,dF(x) \quad \text{(Stieltjes integration)}
= \int x\,dP_X(x) = \int x\,P_X(dx),
$$

where the Stieltjes integral is defined as the limit of $$\sum_{i=1}^{n} x_i \bigl(F(x_i) - F(x_{i-1})\bigr)$$, and $$P_X$$ is the distribution of $$X$$.

cf) When $$\mu$$ is a measure, the integral with respect to $$\mu$$ is defined as $$\int f(x)\,\mu(dx) = \int f\,d\mu(x)$$. $$\rightarrow$$ From measure theory.

cf) When a density function exists for $$X \sim f$$,

$$
E(g(X)) = \int g(x) f(x)\,dx = \int g(x)\,F(dx) \quad (F \text{ is the CDF of } X)
= \int g(x)\,P_X(dx) = \int g\,dP_X(x).
$$

\* From now on, write $$f(x)\,dx = P_X(dx)$$ ($$= F(dx)$$). $$\downarrow$$ From Riemann–Stieltjes integration. $$P_X$$ is a measure.

cf) Assume $$E(X) < \infty$$. For an integral $$\int_{-\infty}^{\infty} h(x)\,dx$$ to be defined without ambiguity, the condition $$\int_{-\infty}^{\infty} \lvert h(x)\rvert \,dx < \infty$$ is necessary. (Think of $$\int_{-\infty}^{\infty} \frac{x}{1+x^2}\,dx$$.)

$$
\int_0^{\infty} \frac{x}{1+x^2}\,dx = \frac{1}{2}\int_0^{\infty} \frac{1}{1+t}\,dt = \infty.
$$

Then what is $$\int_{-\infty}^{\infty} \frac{x}{1+x^2}\,dx$$? $$\rightarrow$$ $$0$$? (expected: $$\lim_{t \to \infty} \int_{-t}^{t} \frac{x}{1+x^2}\,dx = 0$$.) Otherwise? ($$\infty - \infty$$?)

$$
\int_{-\infty}^{0} \frac{x}{1+x^2}\,dx + \int_0^{\infty} \frac{x}{1+x^2}\,dx = -\int_0^{\infty} \frac{x}{1+x^2}\,dx + \int_0^{\infty} \frac{x}{1+x^2}\,dx = -\infty + \infty
$$

$$\rightarrow$$ the value is not well defined, which causes great confusion.

\* Not every distribution has an expectation. $$X \sim f(x) = \frac{1}{\pi}\cdot\frac{1}{1+x^2}$$ (pdf). $$\rightarrow$$ The expectation $$\int x \cdot \frac{1}{\pi}\cdot\frac{1}{1+x^2}\,dx$$ does not exist (this is the Cauchy distribution: a representative counterexample).

> **Theorem (Properties of expectation).**
>
> - (1) $$X$$: a random variable, $$g$$: a function, $$F$$: the CDF of $$X$$, with $$\int \lvert g(x)\rvert \,F(dx) < \infty$$, and $$g$$ a real-valued function. Then
>
>   $$
>   E(g(X)) := \int g(x)\,F(dx) = \int g(x)\,dF(x).
>   $$
>
>   $$\rightarrow$$ a new random variable: a transformation of a random variable.
> - (2) $$E(aX + b) = aE(X) + b$$.
> - (3) (Linearity) If $$a, b \in \mathbb{R}$$ and $$g_1, g_2$$ are functions, then
>
>   $$
>   E\bigl(a g_1(X) + b g_2(X)\bigr) = a E(g_1(X)) + b E(g_2(X)),
>   $$
>
>   where the left side and the right side exist.
>
>   Note: $$E(X)$$ is the center of the distribution of $$X$$ (center of mass).
> - (4) (Positivity) $$g(x) \ge 0$$ for all $$x$$ $$\Rightarrow$$ $$E(g(X)) \ge 0$$.
{: .theorem #thm-expectation-properties }

*Proof.* (1) The case where $$X$$ is discrete. Let $$Y = g(X)$$. Then ($$f_Y$$: the PMF of $$Y$$)

$$
\begin{aligned}
E(Y) &= \sum_y y f_Y(y) = \sum_y y P(Y = y) \\
&= \sum_y \Bigl( y \sum_{x : g(x) = y} P(X = x) \Bigr) = \sum_y \sum_{x : g(x) = y} y\,P(X = x) \\
&= \sum_x g(x) P(X = x) = \sum_x g(x) f_X(x) = \int g\,dF(x).
\end{aligned}
$$

## 4.2 Variance, standard deviation, skewness and kurtosis

> **Definition (Variance and standard deviation).** $$X$$: a random variable.
>
> $$
> \mathrm{Var}(X) := E\bigl(X - E(X)\bigr)^2 \quad \rightarrow \text{ the unit differs from that of } X,
> $$
>
> $$
> \mathrm{Sd}(X) := \sqrt{\mathrm{Var}(X)} \quad \rightarrow \text{ matches the unit.}
> $$
{: .definition #def-variance }

> **Theorem (Properties of mean and variance).** Assume $$\mathrm{Var}(X) < \infty$$.
>
> - (1) $$\mathrm{Var}(X) \ge 0$$.
> - (2) $$\mathrm{Var}(X) = 0 \Longleftrightarrow P(X = \mu) = 1$$, where $$E(X) = \mu$$.
> - (3) $$\mathrm{Var}(X) = E(X^2) - \{E(X)\}^2$$.
> - (4) $$\mathrm{Var}(aX + b) = a^2 \mathrm{Var}(X)$$ if $$a, b \in \mathbb{R}$$.
{: .theorem #thm-variance-properties }

*Proof.* (1) (When $$X$$ has a pdf.) $$\mathrm{Var}(X) = E(X - \mu)^2$$ where $$\mu = E(X)$$, so

$$
\mathrm{Var}(X) = \int (x - \mu)^2 f(x)\,dx \ge 0, \qquad f: \text{the pdf of } X.
$$

(2) ($$\Leftarrow$$) $$\mathrm{Var}(X) = E(X - \mu)^2 = (\mu - \mu)^2 = 0$$.

($$\Rightarrow$$) For every $$n$$,

$$
0 = \mathrm{Var}(X) = E\bigl((X - \mu)^2\bigr) \ge E\bigl((X - \mu)^2\, I(|X - \mu| \ge \tfrac{1}{n})\bigr)
\quad (\because\ (X - \mu)^2 \ge (X - \mu)^2\, I(|X - \mu| \ge \tfrac{1}{n})).
$$

$$
\therefore\ \mathrm{Var}(X) \ge E\bigl((X - \mu)^2\, I(|X - \mu| \ge \tfrac{1}{n})\bigr)
\ge E\bigl(\tfrac{1}{n^2}\, I(|X - \mu| \ge \tfrac{1}{n})\bigr)
= \tfrac{1}{n^2}\, P(|X - \mu| \ge \tfrac{1}{n}) \ge 0.
$$

So $$P(\lvert X - \mu\rvert  \ge \tfrac{1}{n}) = 0$$ for all $$n$$, and

$$
P(X = \mu) = P\Bigl(\bigcap_{n=1}^{\infty} [\,|X - \mu| < \tfrac{1}{n}\,]\Bigr) = \lim_{n \to \infty} P(|X - \mu| < \tfrac{1}{n}) = 1.
$$

(3) $$\mathrm{Var}(X) = E(X - \mu)^2 = E(X^2) - 2\mu E(X) + \mu^2 = E(X^2) - \mu^2$$.

> **Definition (Skewness and kurtosis).** $$X$$: a random variable, $$\mu = E(X)$$, $$\sigma^2 = \mathrm{Var}(X)$$.
>
> - (1) Asymmetry (skewness): $$E\bigl(\bigl(\tfrac{X - \mu}{\sigma}\bigr)^3\bigr)$$.
> - (2) Degree of peakedness (kurtosis): $$E\bigl(\bigl(\tfrac{X - \mu}{\sigma}\bigr)^4\bigr)$$ or $$E\bigl(\bigl(\tfrac{X - \mu}{\sigma}\bigr)^4\bigr) - 3$$, the value that makes the normal distribution the baseline $$0$$.
{: .definition #def-skewness-kurtosis }

**Example.** Skewness $$< 0$$: the left tail is long. Skewness $$> 0$$: the right tail is long. For kurtosis, compare with the normal distribution: a higher kurtosis means thicker tails; a lower kurtosis means thinner tails. \* Kurtosis is not about the sharpness of the center, but about the thickness of the tails!

## 4.3 Moment generating functions

> **Definition.**
>
> - (1) **Moment.** When $$E(\lvert X\rvert ^r) < \infty$$, $$E(X^r)$$ is called the $$r$$-th moment of $$X$$ ($$r \in \mathbb{N}$$).
> - (2) **Moment generating function (MGF).** If $$\exists h > 0$$ s.t. $$E(e^{tX}) < \infty$$ for all $$\lvert t\rvert  < h$$ ($$\rightarrow$$ it is enough that it exists near $$0$$), then $$M_X(t) = E(e^{tX})$$ ($$\lvert t\rvert  < h$$) is called the MGF.
{: .definition #def-mgf }

> **Theorem (Properties of the MGF).**
>
> - (1) $$\bigstar$$ The MGF generates the moments. Let $$M_X(t)$$ exist for an arbitrary random variable $$X$$. Then
>   - (a) $$E(\lvert X\rvert ^r) < \infty$$ for all $$r \in \mathbb{N}$$ (all moments exist).
>   - (b) $$E(X^r) = M_X^{(r)}(0)$$.
>   - (c) For some $$\varepsilon > 0$$, $$M_X(t) = \sum_{r=0}^{\infty} \dfrac{E(X^r)}{r!}\, t^r$$ for all $$\lvert t\rvert  < \varepsilon$$.
> - (2) (Uniqueness of the MGF.) If the MGFs of two random variables $$X$$ and $$Y$$ exist near $$0$$ and they are equal, in other words, if there exists $$\varepsilon > 0$$ such that $$M_X(t) = M_Y(t)$$ for all $$\lvert t\rvert  < \varepsilon$$, then the distributions of $$X$$ and $$Y$$ are the same ($$P(X \in B) = P(Y \in B)$$ for all $$B \subseteq \mathbb{R}$$). The proof is omitted (too hard).
{: .theorem #thm-mgf-properties }

*Proof.* (1) There exists $$h$$ with $$M_X(t) < \infty$$ for all $$\lvert t\rvert  < h$$.

(a) We want to show $$E(\lvert X\rvert ^r) < \infty$$ for $$r \in \mathbb{N}$$. Since $$e^{\lvert tX\rvert } = \sum_{k=0}^{\infty} \frac{\lvert tX\rvert ^k}{k!}$$,

$$
\frac{|tX|^r}{r!} \le e^{|tX|} \le e^{tX} + e^{-tX}.
$$

$$
\therefore\ E\Bigl(\frac{|tX|^r}{r!}\Bigr) \le E\,e^{|tX|} \le E\,e^{tX} + E\,e^{-tX} = M_X(t) + M_X(-t).
$$

$$
\therefore\ E(|X|^r) \le \frac{r!}{|t|^r}\bigl(M_X(t) + M_X(-t)\bigr) < \infty.
$$

(c) We want to show $$M_X(t) = \sum_{r=0}^{\infty} \frac{E(X^r)}{r!}\, t^r$$. $$\rightarrow$$ We must show $$\lim_{n \to \infty} \sum_{r=0}^{n} \frac{E(X^r)}{r!}\, t^r = M_X(t)$$. That is, we must show

$$
\Bigl|\, \sum_{r=0}^{n-1} \frac{E(X^r)}{r!}\, t^r - M_X(t) \Bigr| \xrightarrow{\ n \to \infty\ } 0.
$$

*Note.* If $$f$$ is $$n$$ times continuously differentiable on $$(a - h, a + h)$$ (the $$n$$-th derivative is continuous), then

$$
f(x) = \sum_{r=0}^{n-1} \frac{f^{(r)}(a)}{r!}(x - a)^r + R_n(x, a), \qquad
R_n(x, a) = \frac{(x - a)^n}{(n-1)!}\int_0^1 (1 - u)^{n-1} f^{(n)}\bigl(a + u(x - a)\bigr)\,du.
$$

Then

$$
e^{tX} = \sum_{r=0}^{n-1} \frac{(tX)^r}{r!} + \frac{(tX)^n}{(n-1)!}\int_0^1 (1 - u)^{n-1} e^{utX}\,du.
$$

$$
\therefore\ \Bigl|\, e^{tX} - \sum_{r=0}^{n-1} \frac{(tX)^r}{r!} \Bigr|
= \frac{|tX|^n}{(n-1)!}\int_0^1 (1 - u)^{n-1} e^{utX}\,du
\le \frac{|tX|^n}{(n-1)!}\, e^{|tX|}\int_0^1 (1 - u)^{n-1}\,du
= \frac{|tX|^n}{n!}\, e^{|tX|} \le \frac{1}{n}\, e^{3|tX|} \le \frac{1}{n}\bigl(e^{3tX} + e^{-3tX}\bigr).
$$

(The step $$\frac{y^n}{n!}\, e^{y} \le \frac1n e^{3y}$$ for $$y \ge 0$$ uses $$\frac{y^n}{n!} = \frac{y}{n}\cdot\frac{y^{n-1}}{(n-1)!} \le \frac{1}{n}\, y\, e^{y} \le \frac1n e^{2y}$$.)

$$
\therefore\ \Bigl|\, M_X(t) - \sum_{r=0}^{n-1} \frac{E(X^r)}{r!}\, t^r \Bigr|
= E\Bigl(\Bigl|\, e^{tX} - \sum_{r=0}^{n-1} \frac{(tX)^r}{r!} \Bigr|\Bigr)
\le \frac{1}{n}\, E\bigl(e^{3tX} + e^{-3tX}\bigr) = \frac{1}{n}\bigl(M_X(3t) + M_X(-3t)\bigr).
$$

$$\therefore$$ If $$\lvert 3t\rvert  < h$$, the value goes to $$0$$ as $$n \to \infty$$.

**Example (standard normal distribution).** $$X \sim \frac{1}{\sqrt{2\pi}}\, e^{-x^2/2}$$, $$x \in \mathbb{R}$$.

Note: $$\int_{-\infty}^{\infty} e^{-x^2/2}\,dx = I = \sqrt{2\pi}$$.

*Proof.* With the substitution $$x = r\sin\theta$$, $$y = r\cos\theta$$ ($$\theta \in [0, 2\pi)$$, $$r > 0$$),

$$
I^2 = \int_{-\infty}^{\infty} e^{-x^2/2}\,dx \int_{-\infty}^{\infty} e^{-y^2/2}\,dy
= \iint_C e^{-\frac{1}{2}(x^2 + y^2)}\,dx\,dy
= \int_0^{\infty}\!\int_0^{2\pi} e^{-r^2/2}\, r\,d\theta\,dr
= 2\pi \int_0^{\infty} r e^{-r^2/2}\,dr = 2\pi.
$$

$$\rightarrow$$ $$M_X(t) = ?$$

$$
\begin{aligned}
M_X(t) = E\,e^{tX} &= \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} e^{tx} e^{-x^2/2}\,dx
= \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} e^{-\frac{1}{2}(x^2 - 2tx + t^2)}\, e^{\frac{1}{2}t^2}\,dx \\
&= \frac{e^{t^2/2}}{\sqrt{2\pi}}\int_{-\infty}^{\infty} e^{-\frac{1}{2}(x - t)^2}\,dx = e^{t^2/2}
\quad \Bigl(\because \int_{-\infty}^{\infty} e^{-\frac{1}{2}x^2}\,dx = \sqrt{2\pi}\Bigr).
\end{aligned}
$$

$$
\therefore\ M_X(t) = e^{t^2/2} = \sum_{r=0}^{\infty} \frac{(t^2/2)^r}{r!} = \sum_{r=0}^{\infty} \frac{t^{2r}}{2^r r!}
= 1 + \tfrac{1}{2}t^2 + \tfrac{1}{8}t^4 + o(t^4)
= \sum_{r=0}^{\infty} \frac{(2r)!}{2^r r!}\cdot\frac{t^{2r}}{(2r)!}.
$$

$$
\rightarrow\quad s = 2r:\ E(X^s) = \frac{(2r)!}{2^r r!}; \qquad s = 2r + 1:\ E(X^s) = 0.
$$

**Note.** Even if the moments of all orders exist, the MGF may not exist. $$\rightarrow$$ The log-normal distribution.

**Example.** $$f(x) = \frac{1}{\sqrt{2\pi}}\, e^{-\frac{1}{2}(\log x)^2}\cdot\frac{1}{x}$$ ($$x > 0$$). Then

$$
E\,e^{tX} = \int_0^{\infty} e^{tx}\,\frac{1}{\sqrt{2\pi}}\, e^{-\frac{1}{2}(\log x)^2}\,\frac{1}{x}\,dx
= \frac{1}{\sqrt{2\pi}}\int_0^{\infty} \frac{1}{x}\, e^{tx - \frac{1}{2}(\log x)^2}\,dx.
$$

$$\rightarrow$$ If $$t > 0$$, $$e^{tx - \frac{1}{2}(\log x)^2}$$ grows quickly. $$\Rightarrow$$ The integral is infinite, so there is no MGF.

But

$$
E(X^r) = \int_0^{\infty} x^r\,\frac{1}{\sqrt{2\pi}}\, e^{-\frac{1}{2}(\log x)^2}\,\frac{1}{x}\,dx
= \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} e^{rk}\, e^{-\frac{1}{2}k^2}\,dk \quad (\log x = k)
= \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} e^{rk - \frac{1}{2}k^2}\,dk,
$$

$$\rightarrow$$ which is integrable.

> **Theorem (Property of the MGF).** If the MGF of $$X$$ is $$M_X(t)$$, then $$M_{aX + b}(t) = e^{bt} M_X(at)$$, $$a, b \in \mathbb{R}$$.
{: .theorem #thm-mgf-linear }

## 4.4 Cumulant generating functions

> **Definition.**
>
> - (1) When the MGF $$M_X(t)$$ of $$X$$ exists for $$\lvert t\rvert  < h$$ ($$h > 0$$), $$C_X(t) = \log M_X(t)$$ is called the *cumulant generating function* (cgf) of $$X$$.
> - (2) $$C_X(t) = \sum_{r=0}^{\infty} \dfrac{C_r(X)}{r!}\, t^r$$ for $$\lvert t\rvert  < h$$. $$C_r(X)$$ is called the $$r$$-th *cumulant* of $$X$$.
{: .definition #def-cgf }

> **Theorem (Properties of the cgf).** When the MGF of a random variable $$X$$ exists, let $$m_k$$ be the $$k$$-th moment of $$X$$ and $$C_k$$ the $$k$$-th cumulant of $$X$$. Then $$m_0 = 1$$, $$C_0 = 0$$, and
>
> $$
> m_k = \sum_{j=0}^{k-1} \binom{k-1}{j}\, C_{k-j}\, m_j \quad (k \ge 1),
> \qquad
> C_k = m_k - \sum_{j=1}^{k-1} \binom{k-1}{j}\, C_{k-j}\, m_j \quad (k \ge 2).
> $$
{: .theorem #thm-cgf-properties }

\* The MGF moves exponentially, so the moments are hard to find. $$\rightarrow$$ Find the cumulants through the cgf, and then usually go back to the moments.

**Example.** The standard normal distribution: MGF $$\Rightarrow$$ $$e^{t^2/2}$$ $$\rightarrow$$ cgf $$\Rightarrow$$ $$\tfrac{1}{2}t^2$$.

cf)

$$
\begin{aligned}
m_0 &= 1, \\
m_1 &= \tbinom{0}{0} C_1 m_0 = C_1, \\
m_2 &= \tbinom{1}{0} C_2 m_0 + \tbinom{1}{1} C_1 m_1 = C_2 + C_1^2, \\
m_3 &= \tbinom{2}{0} C_3 m_0 + \tbinom{2}{1} C_2 m_1 + \tbinom{2}{2} C_1 m_2 = C_3 + 3C_1 C_2 + C_1^3, \\
m_4 &= C_4 + 4C_1 C_3 + 3C_2^2 + 6C_1^2 C_2 + C_1^4.
\end{aligned}
$$

**Example (Poisson distribution).** $$X \sim \mathrm{Po}(\lambda)$$, $$\lambda > 0$$ $$\Longleftrightarrow$$ $$f_X(x) = \frac{\lambda^x e^{-\lambda}}{x!}$$, $$x \in \mathbb{Z}_+$$. Then

$$
M_X(t) = E\,e^{tX} = \sum_{x=0}^{\infty} e^{tx}\,\frac{\lambda^x}{x!}\, e^{-\lambda}
= e^{-\lambda}\sum_{x=0}^{\infty} \frac{(\lambda e^t)^x}{x!} = e^{\lambda(e^t - 1)} \quad \forall t \in \mathbb{R}.
$$

$$\hookrightarrow$$ $$M_X(t) = e^{\lambda(e^t - 1)} = \sum_{r=0}^{\infty} \frac{(\lambda(e^t - 1))^r}{r!} = \sum_{r=0}^{\infty} \frac{\lambda^r}{r!}\Bigl(\sum_{s=1}^{\infty} \frac{t^s}{s!}\Bigr)^r$$ $$\rightarrow$$ so complex :(

$$
\therefore\ C_X(t) = \log M_X(t) = \lambda(e^t - 1) = \lambda\sum_{r=1}^{\infty} \frac{t^r}{r!}.
\qquad \rightarrow\ C_0 = 0,\ \lambda = C_1 = C_2 = \cdots
$$

$$
\therefore\ m_0 = 1,\ m_1 = \lambda,\ m_2 = \lambda^2 + \lambda,\ m_3 = \lambda^3 + 3\lambda^2 + \lambda,\ m_4 = \lambda^4 + 6\lambda^3 + 7\lambda^2 + \lambda.
$$

\* **Fact** (Apostol, Theorem 4.25). Let $$f(z) = \sum_{n=0}^{\infty} a_n z^n$$ for $$\lvert z\rvert  < r$$ and $$g(z) = \sum_{n=0}^{\infty} b_n z^n$$ for $$\lvert z\rvert  < R$$ ($$r, R > 0$$). If $$\lvert z\rvert  < R$$ and $$\sum_{n=0}^{\infty} \lvert b_n z^n\rvert  < r$$, then

$$
f(g(z)) = \sum_{k=0}^{\infty} c_k z^k, \qquad c_k = \sum_{n=0}^{\infty} a_n b_k(n), \quad g(z)^n = \sum_{k=0}^{\infty} b_k(n)\, z^k.
$$

\* **Fact.** If $$P(s) = \sum_{k=0}^{\infty} p_k s^k$$, then $$Q(s) = e^{P(s)} = \sum_{k=0}^{\infty} q_k s^k$$ where

$$
q_0 = e^{p_0}, \qquad q_k = \frac{1}{k}\sum_{j=0}^{k-1} (k - j)\, p_{k-j}\, q_j \quad (k \ge 1).
$$

$$\rightarrow$$ *Sketch of the proof of this property of the cgf.* $$\dfrac{d}{ds} Q(s) = e^{P(s)} \dfrac{d}{ds} P(s)$$.

$$
\therefore\ \sum_{k=1}^{\infty} k q_k s^{k-1} = \sum_{k=0}^{\infty} k p_k s^{k-1} \cdot \sum_{k=0}^{\infty} q_k s^k.
$$

$$\rightarrow$$ Roughly, match the coefficients on both sides:

$$
(k + 1)\, q_{k+1} = \sum_{j=0}^{k} q_j\,(k + 1 - j)\, p_{k+1-j}, \qquad k \in \mathbb{Z}_+.
$$

$$\rightarrow$$ $$\cdots$$ (The professor said: "Roughly, you can do the rest better, right?")

**Reference.**

① **Characteristic function.** $$\phi_X(t) = E\,e^{itX}$$ $$\rightarrow$$ can be defined for every random variable (because $$\lvert e^{itX}\rvert  = 1$$). $$\rightarrow$$ It has almost all the properties of the MGF (it is integrable, so uniqueness is guaranteed, etc.).

② **Laplace transform.** When $$X \ge 0$$ with probability $$1$$, $$L_X(t) = E\,e^{-tX}$$ ($$t \ge 0$$).

③ **Pgf: probability generating function.** When $$X$$ takes non-negative integer values, $$G_X(s) := E\,s^X = \sum_{x=0}^{\infty} s^x P(X = x)$$ (a power series whose coefficients are probabilities).

## Supplement from the textbook

> The parts below are in the textbook (§1.4) but not in my notes. They are translated from the book and are not my own writing.
{: .prompt-info }

**Proof of property (4) of the variance.** Let $$E(X) = \mu$$ and $$Y = aX + b$$. Then $$E(Y) = a\mu + b$$ and

$$
\mathrm{Var}(Y) = E\bigl[(Y - E(Y))^2\bigr] = E\bigl[(aX + b - a\mu - b)^2\bigr] = a^2 E\bigl[(X - \mu)^2\bigr] = a^2 \mathrm{Var}(X). \qquad \square
$$

**Example 1.4.3 and 1.4.4 (variances of the uniform and the triangular distribution).** (a) $$f_1(x) = I_{[0,1]}(x)$$: $$\mu = \int_0^1 x\,dx = \tfrac{1}{2}$$, $$E(X^2) = \int_0^1 x^2\,dx = \tfrac{1}{3}$$, so $$\mathrm{Var}(X) = \tfrac{1}{3} - (\tfrac{1}{2})^2 = \tfrac{1}{12}$$. (b) $$f_2(x) = (2 - 4\lvert x - \tfrac{1}{2}\rvert)\,I_{[0,1]}(x)$$: $$\mu = \tfrac{1}{2}$$, $$E(X^2) = \int_0^{1/2} x^2(4x)\,dx + \int_{1/2}^{1} x^2(4 - 4x)\,dx = \tfrac{7}{24}$$, so $$\mathrm{Var}(X) = \tfrac{7}{24} - \tfrac{1}{4} = \tfrac{1}{24}$$. Both have mean $$\tfrac12$$, but the triangular distribution, concentrated near the mean, has the smaller variance.

**Example 1.4.5 (standardization).** If $$E(X) = \mu$$ and $$\mathrm{Sd}(X) = \sigma > 0$$, let $$Z = \dfrac{X - E(X)}{\sqrt{\mathrm{Var}(X)}} = \dfrac{X - \mu}{\sigma}$$. By the properties of expectation and variance, $$E(Z) = \dfrac{E(X) - \mu}{\sigma} = 0$$ and $$\mathrm{Var}(Z) = \dfrac{\mathrm{Var}(X)}{\sigma^2} = 1$$. $$Z$$ is called the *standardized* variable of $$X$$. Note that there are distributions whose mean or variance cannot be defined as a real number (the Cauchy distribution above).

## References

- 김우철, *수리통계학* (Mathematical Statistics), revised 2nd edition, 민영사, 2021 — Chapter 1.
- Mathematical Statistics 1 (326.311), Spring 2025. Instructor: Jaeyong Lee (이재용). My handwritten lecture notes, Chapter 1.
- The notes are translated without changing their wording; remarks written in the margins of the notes are kept. Where a statement in the notes was mathematically wrong it is corrected in the text.

[Previous](/posts/mathstat1-random-variables-cdf/) · [Overview](/posts/mathstat1-overview/) · [Next](/posts/mathstat1-inequalities/)
