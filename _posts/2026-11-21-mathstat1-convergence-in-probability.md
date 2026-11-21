---
title: "Mathematical Statistics 1: Ch. 5 Part 1 — Convergence in Probability"
date: 2026-11-21 13:10:00 +0900
categories: [Study Notes, Mathematical Statistics 1]
tags: [convergence in probability, almost sure convergence, law of large numbers, consistency, sample quantile, sample variance, sample correlation]
description: Convergence in probability and almost sure convergence, consistency of estimators, the laws of large numbers, the algebra of convergence in probability, and consistency of the sample variance, the sample correlation coefficient and sample quantiles. Chapter 5, notes section 1 of Mathematical Statistics 1.
math: true
mermaid: false
render_with_liquid: false
---

> My handwritten notes, translated into English. Chapter 5 of my notes, "Approximation of Sampling Distributions", section 1. It corresponds to the first half of §5.2 of the textbook. Statements and proofs follow my notes. Material taken from the textbook is collected at the end under "Supplement from the textbook". The exercises are in [Chapter 5 Exercises](/posts/mathstat1-exercises-chapter-5/).
{: .prompt-info }

## 1. Convergence in probability

### 1.1 Definitions

> **Definition.**
>
> (1) *Convergence in probability.* $$Y_n \xrightarrow{P} Y$$ $$\iff$$ for every $$\epsilon > 0$$, $$\displaystyle\lim_{n\to\infty}P(\lvert Y_n - Y\rvert > \epsilon) = 0$$.
>
> (2) *Almost sure convergence* (convergence almost everywhere, convergence with probability $$1$$). $$Y_n \xrightarrow{a.s.} Y$$ $$\iff$$ $$P\bigl(\omega : \lim_{n\to\infty}Y_n(\omega) = Y(\omega)\bigr) = 1$$.
{: .definition #def-convergence-probability }

\* Pointwise convergence ("convergence at every point") is a *basic* mode; a.s. convergence is pointwise convergence except on a set of probability $$0$$ ("convergence at almost every point, except for a set of probability $$0$$").

**Example.** $$U \sim U(0, 1)$$.

(1) $$f_n(u) = \dfrac{1}{n}$$ for all $$u \in [0, 1]$$, and $$f(u) = 0$$ for all $$u \in [0, 1]$$. Let $$X_n = f_n(U)$$ and $$X = f(U)$$. Then $$X_n \xrightarrow{a.s.} X$$.

*Proof.* 1) $$P(\omega : X_n(\omega) \to X(\omega)) = P(\omega : f_n(U(\omega)) \to f(U(\omega))) = P(\omega : \frac{1}{n} \to 0) = P(\omega \in \Omega) = 1$$ (convergence a.s.; $$X_n(\omega) = \frac{1}{n}$$ converges to $$X(\omega) = 0$$).

2) *Convergence in probability.* Fix an arbitrary $$\epsilon > 0$$. Then $$P(\lvert X_n - X\rvert > \epsilon) = P(\lvert\frac{1}{n} - 0\rvert > \epsilon) = P(\epsilon < \frac{1}{n}) = 0$$ once $$n > 1/\epsilon$$, so the limit is $$0$$. $$\therefore$$ $$X_n \xrightarrow{P} X$$.

(2) For every $$n \in \mathbb{N}$$, $$n$$ can be represented as $$n = \sum_{i=1}^{k}2^i + l$$ where $$l = 0, \dots, 2^{k+1} - 1$$ and $$k, l$$ are uniquely determined. Then set

$$
f_n(u) = 2^{k+1}I\Bigl(\frac{l}{2^{k+1}} < u < \frac{l+1}{2^{k+1}}\Bigr) \quad\text{and}\quad f(u) = 0.
$$

(The functions $$f_1, f_2, \dots$$ are: $$f_1$$ is $$2$$ on the left half-interval and $$0$$ elsewhere, $$f_2$$ is $$2$$ on the right half; $$f_3, f_4, f_5, f_6$$ are $$4$$ on successive quarter-intervals; and so on.) Let $$X_n = f_n(U)$$ and $$X = f(U)$$. Would $$X_n(\omega) \xrightarrow{a.s.} X(\omega)$$? For each $$\omega$$, $$X_n(\omega)$$ is a sequence like $$(0, 2, 0, 0 \mid 0, 4, 0, 0, 0 \mid \cdots)$$: in each block of $$2^{k+1}$$ terms exactly one term is nonzero, equal to $$2^{k+1}$$, so $$X_n(\omega)$$ does not converge to $$0$$. $$\therefore$$ $$P(\omega : X_n(\omega) \to X(\omega)) = P(\emptyset) = 0$$.

However, would $$X_n \xrightarrow{P} X$$? Fix $$\epsilon > 0$$. Then $$P(\lvert X_n - X\rvert > \epsilon) = P(\lvert X_n\rvert > \epsilon) = P(X_n \ne 0) = \dfrac{1}{2^{k+1}} \xrightarrow{n\to\infty} 0$$.

$$\therefore$$ $$X_n \xrightarrow{P} X$$ but $$X_n \xrightarrow{a.s.} X$$ fails. (As $$X_n$$ converges in probability to $$X$$, convergence a.s. does not follow.)

> **Theorem.** $$X_n \xrightarrow{a.s.} X \Rightarrow X_n \xrightarrow{P} X$$, but not conversely. (Proof in graduate school.)
{: .theorem #thm-as-implies-prob }

### 1.2 Consistency

> **Definition (Consistency).** Let $$X_1, \dots, X_n \overset{iid}{\sim} f(x \mid \theta)$$, where $$\theta \in \Theta$$. Also define $$T = T(X_1, \dots, X_n)$$ as the estimate of $$\eta = \eta(\theta)$$. Then $$T$$ has *consistency* for $$\eta = \eta(\theta)$$ $$\iff$$ $$T(X_1, \dots, X_n) \xrightarrow{P} \eta(\theta)$$ for all $$\theta$$.
{: .definition #def-consistency }

### 1.3 Law of large numbers

> **Theorem (Strong law of large numbers).** Let $$X_1, X_2, \dots \overset{iid}{\sim} F$$. Also suppose $$\mu = EX_1$$ exists. Then
>
> $$
> \bar{X} = \frac{1}{n}\sum_{i=1}^{n}X_i \xrightarrow{a.s.} \mu.
> $$
{: .theorem #thm-slln }

*Proof.* Here, set $$\mathrm{Var}(X_1) < \infty$$ and prove $$\bar{X} \xrightarrow{P} \mu$$. Given $$\epsilon > 0$$, show $$\lim_{n\to\infty}P(\lvert\bar{X} - \mu\rvert > \epsilon) = 0$$. By Chebyshev's inequality,

$$
P(\lvert\bar{X} - \mu\rvert > \epsilon) \le \frac{1}{\epsilon^2}\mathrm{Var}(\bar{X}) = \frac{\sigma^2}{n\epsilon^2} \qquad (\sigma^2 = \mathrm{Var}(X_1)),
$$

$$\therefore$$ $$\lim_{n\to\infty}P(\lvert\bar{X} - \mu\rvert > \epsilon) = 0$$. $$\square$$

### 1.4 Operations on convergence in probability

> **Properties.**
>
> (a) Let $$X_n \xrightarrow{P} X$$ and $$Y_n \xrightarrow{P} Y$$. Then
>
> 1. $$X_n \pm Y_n \xrightarrow{P} X \pm Y$$.
> 2. $$X_nY_n \xrightarrow{P} XY$$.
> 3. $$\dfrac{X_n}{Y_n} \xrightarrow{P} \dfrac{X}{Y}$$ if $$Y \ne 0$$ w.p. $$1$$.
> 4. $$\binom{X_n}{Y_n} \xrightarrow{P} \binom{X}{Y}$$.
>
> (b) Let $$X_n \xrightarrow{P} X$$ and $$g$$ be continuous. Then $$g(X_n) \xrightarrow{P} g(X)$$.
>
> (c) (a) and (b) hold for $$\xrightarrow{a.s.}$$, also.
{: .theorem #thm-prob-operations }

*Proof.* (a) 4) Fix $$\epsilon > 0$$. Show

$$
P\Bigl(\Bigl\lVert\binom{X_n}{Y_n} - \binom{X}{Y}\Bigr\rVert > \epsilon\Bigr) \xrightarrow{P} 0.
$$

Then

$$
P\Bigl(\sqrt{(X_n - X)^2 + (Y_n - Y)^2} > \epsilon\Bigr) \le P\Bigl(\lvert X_n - X\rvert > \frac{\epsilon}{\sqrt{2}}\ \text{or}\ \lvert Y_n - Y\rvert > \frac{\epsilon}{\sqrt{2}}\Bigr)
$$

(because $$\lvert X_n - X\rvert \le \frac{\epsilon}{\sqrt{2}}$$ and $$\lvert Y_n - Y\rvert \le \frac{\epsilon}{\sqrt{2}}$$ $$\Leftrightarrow$$ $$\lvert X_n - X\rvert^2 + \lvert Y_n - Y\rvert^2 \le \epsilon^2$$ is implied)

$$
\le P\Bigl(\lvert X_n - X\rvert > \frac{\epsilon}{\sqrt{2}}\Bigr) + P\Bigl(\lvert Y_n - Y\rvert > \frac{\epsilon}{\sqrt{2}}\Bigr) = 0 + 0 \quad\text{(in the limit)}.
$$

(b) Suppose $$X = a$$ w.p. $$1$$ and let $$g$$ be continuous at $$x = a$$. Fix $$\epsilon > 0$$. Show $$P(\lvert g(X_n) - g(X)\rvert > \epsilon) \to 0$$. As $$g$$ is continuous at $$x = a$$, there exists $$\delta > 0$$ such that $$\lvert g(x) - g(a)\rvert < \epsilon$$ if $$\lvert x - a\rvert < \delta$$. Therefore

$$
P(\lvert g(X_n) - g(X)\rvert > \epsilon) \le P(\lvert X_n - a\rvert \ge \delta) \xrightarrow{n\to\infty} 0.
$$

(For a general random variable $$X$$, think about how to do it, using $$\epsilon$$–$$\delta$$.)

*Direct proof of (a) 1) to 3).* ((b) proves (a) 1) to 3), as these are all continuous functions.) (a) 1) Given $$\epsilon > 0$$, we need to show $$P(\lvert X_n + Y_n - (X + Y)\rvert > \epsilon) \xrightarrow{n\to\infty} 0$$. Then

$$
P(\lvert X_n + Y_n - (X + Y)\rvert > \epsilon) \le P\Bigl(\lvert X_n - X\rvert > \frac{\epsilon}{2}\ \text{or}\ \lvert Y_n - Y\rvert > \frac{\epsilon}{2}\Bigr) \le P\Bigl(\lvert X_n - X\rvert > \frac{\epsilon}{2}\Bigr) + P\Bigl(\lvert Y_n - Y\rvert > \frac{\epsilon}{2}\Bigr) \xrightarrow{n\to\infty} 0.
$$

2) 3) can also be proved the same way. (Suppose $$X = a$$, $$Y = b$$ w.p. $$1$$.) $$\square$$

**Example 7 (Consistency of the sample variance).** $$X_1, \dots, X_n \overset{iid}{\sim} (\mu, \sigma^2)$$, $$\mu \in \mathbb{R}$$, $$\sigma^2 > 0$$, $$S^2 = \dfrac{1}{n-1}\sum_{i=1}^{n}(X_i - \bar{X})^2$$. Then $$S^2 \xrightarrow{P} \sigma^2$$ and $$S = \sqrt{S^2} \xrightarrow{P} \sigma$$.

*Proof.* By the strong law of large numbers, $$\bar{X} \xrightarrow{P} \mu$$ and $$\frac{1}{n}\sum_{i=1}^{n}X_i^2 \xrightarrow{P} \mu^2 + \sigma^2$$. Thus

$$
S^2 = \frac{1}{n-1}\sum_{i=1}^{n}(X_i - \bar{X})^2 = \frac{n}{n-1}\cdot\frac{1}{n}\sum_{i=1}^{n}(X_i - \bar{X})^2 = \frac{n}{n-1}\Bigl(\frac{1}{n}\sum X_i^2 - \bar{X}^2\Bigr) \xrightarrow{P} 1\cdot\sigma^2 = \sigma^2,
$$

since $$\frac{1}{n}\sum X_i^2 \xrightarrow{P} \mu^2 + \sigma^2$$ and $$\bar{X}^2 \xrightarrow{P} \mu^2$$. Also, as $$g(x) = \sqrt{x}$$ is continuous, $$S = \sqrt{S^2} \xrightarrow{P} \sqrt{\sigma^2} = \sigma$$. $$\square$$

**Example 8 (Consistency of the sample correlation coefficient).** $$\binom{X_1}{Y_1}, \dots, \binom{X_n}{Y_n}$$ is a random sample from a population with correlation coefficient $$\rho = \mathrm{Cov}(X_1, Y_1)$$ (in the standardized setting). Alternatively,

$$
\binom{X_1}{Y_1}, \dots, \binom{X_n}{Y_n} \sim \left(\binom{\mu_1}{\mu_2}, \begin{pmatrix}\sigma_1^2 & \rho\sigma_1\sigma_2 \\ \rho\sigma_1\sigma_2 & \sigma_2^2\end{pmatrix}\right).
$$

Define the sample correlation coefficient as

$$
\hat{\rho} = \frac{\sum(X_i - \bar{X})(Y_i - \bar{Y})}{\sqrt{\sum(X_i - \bar{X})^2 \times \sum(Y_i - \bar{Y})^2}}.
$$

Then $$\hat{\rho} \xrightarrow{P} \rho$$.

*Proof.* By the law of large numbers,

$$
\begin{pmatrix}\bar{X} \\ \bar{Y} \\ \frac{1}{n}\sum X_i^2 \\ \frac{1}{n}\sum Y_i^2 \\ \frac{1}{n}\sum X_iY_i\end{pmatrix} \xrightarrow{P} \begin{pmatrix}EX_1 \\ EY_1 \\ EX_1^2 \\ EY_1^2 \\ EX_1Y_1\end{pmatrix} = \begin{pmatrix}\mu_1 \\ \mu_2 \\ \mu_1^2 + \sigma_1^2 \\ \mu_2^2 + \sigma_2^2 \\ \mu_1\mu_2 + \rho\sigma_1\sigma_2\end{pmatrix}.
$$

Writing $$\hat{\rho} = \dfrac{\frac{1}{n}\sum X_iY_i - \bar{X}\bar{Y}}{\sqrt{(\frac{1}{n}\sum X_i^2 - \bar{X}^2)(\frac{1}{n}\sum Y_i^2 - \bar{Y}^2)}}$$,

$$
\hat{\rho} \xrightarrow{P} \frac{\mu_1\mu_2 + \rho\sigma_1\sigma_2 - \mu_1\mu_2}{\sqrt{(\mu_1^2 + \sigma_1^2 - \mu_1^2)(\mu_2^2 + \sigma_2^2 - \mu_2^2)}} = \rho \qquad (\because g(t_1, t_2, t_3, t_4, t_5) = \tfrac{t_5 - t_1t_2}{\sqrt{(t_3 - t_1^2)(t_4 - t_2^2)}}\ \text{is continuous}). \qquad\square
$$

> **Lemma.** When $$n \to \infty$$, if $$\mathrm{Var}(Y_n) \to 0$$ and $$E(Y_n) \to a \in \mathbb{R}$$, then $$Y_n \xrightarrow{P} a$$.
{: .theorem #lem-var-to-zero }

*Proof.* For given $$\epsilon > 0$$, let us show $$P(\lvert Y_n - a\rvert > \epsilon) \to 0$$. By Chebyshev,

$$
P(\lvert Y_n - a\rvert > \epsilon) \le \frac{1}{\epsilon^2}E(Y_n - a)^2 = \frac{1}{\epsilon^2}\bigl(\mathrm{Var}(Y_n) + (EY_n - a)^2\bigr) \to 0. \qquad\square
$$

**Example (the maximum of uniform variables).** Say $$X_1, \dots, X_n \overset{iid}{\sim} U(0, \theta)$$, $$\theta > 0$$. Let $$Y_n = \max\{X_1, \dots, X_n\} = X_{(n)}$$. Then $$Y_n \xrightarrow{P} \theta$$.

*Proof.* Let $$U_1, \dots, U_n \overset{iid}{\sim} U(0, 1)$$. Then $$(X_1, \dots, X_n) \overset{d}{=} \theta(U_1, \dots, U_n)$$, so $$X_{(n)} \overset{d}{=} \theta U_{(n)}$$. Here $$U_{(n)} \sim \mathrm{Beta}(n, 1)$$, so $$\dfrac{X_{(n)}}{\theta} \sim \mathrm{Beta}(n, 1)$$. Then $$EY_n = \theta E(\mathrm{Beta}(n, 1)) = \dfrac{\theta n}{n+1} \to \theta$$, and $$\mathrm{Var}\,Y_n = \theta^2\mathrm{Var}(\mathrm{Beta}(n, 1)) = \dfrac{\theta^2n}{(n+1)^2(n+2)} \to 0$$. $$\therefore$$ $$Y_n \xrightarrow{P} \theta$$ by the lemma. $$\square$$

**Example (Convergence of order statistics).** Let $$X_1, \dots, X_n \overset{iid}{\sim} F$$, where $$F$$ is the cdf of $$X_1$$.

\* $$F$$: continuous and strictly increasing.

For a given $$\alpha \in (0, 1)$$, let $$F^{-1}(\alpha)$$ be the $$\alpha$$ quantile of the population. If $$r_n \sim \alpha n$$, then $$X_{(r_n)} \xrightarrow{P} F^{-1}(\alpha)$$.

*Proof.* [Sketch] Let $$h(y) = F^{-1}(1 - e^{-y})$$. Since $$Z \sim \mathrm{Exp}(1) \Rightarrow 1 - e^{-Z} \sim U(0, 1) \Rightarrow F^{-1}(1 - e^{-Z}) \sim F$$ (use this!), with $$Z_1, \dots, Z_n \overset{iid}{\sim} \mathrm{Exp}(1)$$ we have $$(h(Z_1), \dots, h(Z_n)) \overset{d}{=} (X_1, \dots, X_n)$$, so

$$
X_{(r_n)} \overset{d}{=} h(Z_{(r_n)}).
$$

Then $$r_n = Z_{(r_n)} \overset{d}{=} \dfrac{1}{n}Z_1 + \dfrac{1}{n-1}Z_2 + \cdots + \dfrac{1}{n - r_n + 1}Z_{r_n}$$. (Here $$r_n$$ on the left denotes the exponential order statistic, whose representation is the Rényi representation.)

*Statement.* $$r_n \xrightarrow{P} -\log(1 - \alpha)$$.

① $$E\,r_n = E\Bigl(\sum_{i=1}^{r_n}\dfrac{1}{n+1-i}Z_i\Bigr) = \dfrac{1}{n}\sum_{i=0}^{r_n-1}\dfrac{1}{1 - \frac{i}{n}}E(Z_i) \xrightarrow{n\to\infty} \int_0^{\alpha}\dfrac{1}{1-x}\,dx = -\log(1 - \alpha)$$ (check by myself).

② $$\mathrm{Var}(r_n)$$: (similar process) $$\sim \dfrac{1}{n}\int_0^{\alpha}\dfrac{dx}{(1-x)^2} = \dfrac{1}{n}\dfrac{\alpha}{1-\alpha} \to 0$$.

By ① and ②, $$r_n \xrightarrow{P} -\log(1 - \alpha)$$. $$\therefore$$ $$X_{(r_n)} = h(r_n) \xrightarrow{P} h(-\log(1 - \alpha)) = F^{-1}(\alpha)$$, as $$h$$ is continuous. $$\square$$

## Supplement from the textbook

**Weak law of large numbers (Theorem 5.2.2).** If $$X_1, \dots, X_n$$ are independent with the same distribution and $$E(X_1)$$ is defined as a real number, then $$\mathrm{plim}\,\frac{1}{n}\sum_{i=1}^{n}X_i = E(X_1)$$. (The textbook proves the case $$\mathrm{Var}(X_1) < +\infty$$ with Chebyshev's inequality, as above.) Applying it to the indicator $$I_A$$: the relative frequency $$\frac{1}{n}\sum I_A(X_i)$$ converges in probability to $$P(X_1 \in A)$$.

**Convergence in probability of vectors.** For $$X_n = (X_{n1}, \dots, X_{nk})^t$$ and a constant vector $$c$$, $$X_n \xrightarrow{P} c$$ means $$\lim P(\lVert X_n - c\rVert \ge \epsilon) = 0$$ for every $$\epsilon > 0$$ (Theorem 5.2.3: equivalently each component converges in probability, since $$\max_i\lvert X_{ni} - c_i\rvert \le \lVert X_n - c\rVert \le k\max_i\lvert X_{ni} - c_i\rvert$$). By this, the law of large numbers holds for random vectors (Theorem 5.2.4).

**Theorem 5.2.5 (Continuous function and convergence in probability).** If $$\mathrm{plim}\,X_n = c$$ for a vector and a real-valued function $$g$$ is continuous at $$c$$, then $$\mathrm{plim}\,g(X_n) = g(c)$$. *Proof.* By continuity, for every $$\epsilon > 0$$ there is $$\delta > 0$$ with $$(\lVert X_n - c\rVert < \delta) \subseteq (\lvert g(X_n) - g(c)\rvert < \epsilon)$$, so $$P(\lvert g(X_n) - g(c)\rvert \ge \epsilon) \le P(\lVert X_n - c\rVert \ge \delta) \to 0$$.

**Theorem 5.2.6 (Convergence in probability and the four arithmetic operations).** If $$X_n \xrightarrow{P} a$$ and $$Y_n \xrightarrow{P} b$$, then $$\mathrm{plim}(X_n \pm Y_n) = a \pm b$$, $$\mathrm{plim}\,X_nY_n = ab$$, $$\mathrm{plim}\,X_n/Y_n = a/b$$ ($$b \ne 0$$). The proof applies Theorem 5.2.5 to $$(x, y) \mapsto x + y, x - y, xy, x/y$$.

**Theorem 5.2.1 (A limit that is a constant).** $$X_n \xrightarrow{d} X$$ with $$P(X = c) = 1$$ if and only if $$\lim P(\lvert X_n - c\rvert \ge \epsilon) = 0$$ for every $$\epsilon > 0$$; so convergence in distribution to a constant is the same as convergence in probability to it (proof in [Part 2](/posts/mathstat1-convergence-in-distribution/)).

**Theorem 5.2.7.** For random variables with a finite variance, $$\lim\mathrm{Var}(X_n) = 0$$ and $$\lim E(X_n) = a$$ imply $$\mathrm{plim}\,X_n = a$$ (the lemma above). *Proof.* By Markov's inequality, $$P(\lvert X_n - a\rvert \ge \epsilon) \le E[(X_n - a)^2]/\epsilon^2$$, and $$E[(X_n - a)^2] = \mathrm{Var}(X_n) + \{E(X_n) - a\}^2 \to 0$$.

**Example 5.2.4 (Sample moments).** The $$r$$-th sample moment $$\hat{m}_r = \frac{1}{n}\sum X_i^r$$ converges in probability to the population moment $$m_r = E(X_1^r)$$ if $$E(\lvert X_1^k\rvert) < +\infty$$ ($$r \le k$$); so the vector $$(\hat{m}_1, \dots, \hat{m}_k)^t$$ converges to the moment vector of the population.

**Example 5.2.6.** For $$U_{(n)}$$ of a $$U(0, 1)$$ sample, $$pdf_{U_{(n)}}(x) = nx^{n-1}I_{(0,1)}(x)$$, $$E(U_{(n)}) = n/(n+1) \to 1$$, $$\mathrm{Var}(U_{(n)}) = n/(n+2) - (n/(n+1))^2 \to 0$$, so $$\mathrm{plim}\,U_{(n)} = 1$$.

**Example 5.2.7 (Sample quantile).** If the population is continuous with a strictly increasing cdf, the $$\alpha$$ quantile $$F^{-1}(\alpha)$$ is estimated by the sample quantile $$X_{(r_n)}$$ with $$r_n \sim \alpha n$$. By Theorem 4.3.4, $$X_{(r_n)} \overset{d}{=} h(\frac{1}{n}Z_1 + \cdots + \frac{1}{n-r_n+1}Z_{r_n})$$, $$h(y) = F^{-1}(1 - e^{-y})$$. With $$Y_n = \frac{1}{n}Z_1 + \cdots + \frac{1}{n-r_n+1}Z_{r_n}$$, $$E(Y_n) = \frac{1}{n} + \cdots + \frac{1}{n-r_n+1} \sim -\log(1-\alpha)$$ and $$\mathrm{Var}(Y_n) = \frac{1}{n^2} + \cdots + \frac{1}{(n-r_n+1)^2} \sim \frac{1}{n}\frac{\alpha}{1-\alpha}$$ by approximating the sums with the integrals $$\int_0^{\alpha}\frac{dx}{1-x}$$ and $$\frac{1}{n}\int_0^{\alpha}\frac{dx}{(1-x)^2}$$. Hence $$\mathrm{plim}\,Y_n = -\log(1-\alpha)$$, and for continuous $$h$$, $$h(Y_n) \xrightarrow{d} F^{-1}(\alpha)$$; by Theorem 5.2.1, $$\mathrm{plim}\,X_{(r_n)} = F^{-1}(\alpha)$$. (The definition of the sample quantile used here differs from the sample median of Example 4.1.2; it is a simplified definition for large samples.)

**Example 5.2.5 (Sample variance and standard deviation).** The sample variance $$S_n^2 = \frac{n}{n-1}\{\frac{1}{n}\sum X_i^2 - (\frac{1}{n}\sum X_i)^2\}$$ is a function of two sample moments; by the law of large numbers and Theorem 5.2.6, $$\mathrm{plim}\,S_n^2 = \sigma^2$$, and since the square root is continuous, $$\mathrm{plim}\,S_n = \sigma$$.

## References

- 김우철, *수리통계학* (Mathematical Statistics), revised 2nd edition, 민영사, 2021 — Chapter 5, §5.2 (Theorems 5.2.1 to 5.2.7, Examples 5.2.4 to 5.2.7). The supplement is translated from the book.
- Mathematical Statistics 1 (326.311), Seoul National University, Spring 2025. Instructor: Jaeyong Lee (이재용).

[Previous: Chapter 4 Part 4](/posts/mathstat1-multivariate-normal/) · [Overview](/posts/mathstat1-overview/) · [Next](/posts/mathstat1-convergence-in-distribution/)
