---
title: "Mathematical Statistics 1: Ch. 3 Part 2 — Geometric, Negative Binomial, Hypergeometric and Multinomial Distributions"
date: 2026-11-21 11:20:00 +0900
categories: [Study Notes, Mathematical Statistics 1]
tags: [geometric, negative binomial, hypergeometric, multinomial, memoryless, waiting time]
description: The geometric distribution and its memoryless property, the negative binomial distribution as a sum of geometric variables, the hypergeometric distribution and its binomial approximation, and the multinomial distribution. Chapter 3, notes sections 1.4 to 1.7 of Mathematical Statistics 1.
math: true
mermaid: false
render_with_liquid: false
---

> My handwritten notes, translated into English. Chapter 3, notes sections 1.4 to 1.7. They correspond to §3.1 and §3.3 of the textbook and part of §3.2. Statements and proofs follow my notes. Material taken from the textbook is collected at the end under "Supplement from the textbook". In my notes the geometric and negative binomial variables count the *failures* before the success (support starting at $$0$$); the textbook, and the [exercises](/posts/mathstat1-exercises-chapter-3/), count the *trials* (support starting at $$1$$ and $$r$$). The two are related by $$W_r = X + r$$.
{: .prompt-info }

### 1.4 Geometric distribution

> **Notation.** $$X \sim \mathrm{Geo}(p)$$, $$p \in [0, 1]$$. For $$p = 0$$, $$X = \infty$$ with probability $$1$$.
>
> **Meaning.** Toss a coin with probability $$p$$ of heads infinitely many times; $$X$$ is the number of tails before the first head.
{: .definition #def-geometric }

**Properties.**

1. PDF: $$P(X = x) = f(x) = q^xp$$, $$x = 0, 1, 2, \dots$$
2. MGF: $$M_X(t) = \dfrac{p}{1 - qe^t}$$, $$t < -\log q$$.
3. $$E(X) = \dfrac{q}{p}$$, $$\mathrm{Var}(X) = \dfrac{q}{p^2}$$.
4. Let $$W_1 := \min\{n : X_1 + \cdots + X_n \ge 1\}$$, $$X_i \overset{iid}{\sim} \mathrm{Ber}(p)$$ (the number of the trial at which the first head appears, that is, the number of coin tosses up to the first head). Then $$W_1 - 1 \sim \mathrm{Geo}(p)$$.
5. **Memoryless property of the geometric distribution.** If $$X \sim \mathrm{Geo}(p)$$, then

   $$
   P(X > m + n \mid X > m) = P(X \ge n) \qquad \forall n, m \in \mathbb{N}.
   $$

   (Very important. The proof is just a computation.)

*Proof.* (1) Show $$\sum_{x=0}^{\infty}f(x) = 1$$: $$\sum_{x=0}^{\infty}q^xp = p/(1 - q) = 1$$ by the Lemma in (3).

(2)

$$
M_X(t) = E(e^{tX}) = \sum_{x=0}^{\infty}e^{tx}q^xp = p\sum_{x=0}^{\infty}(qe^t)^x = \frac{p}{1 - qe^t} \qquad (\lvert qe^t\rvert < 1).
$$

(3) **Lemma.** $$\dfrac{1}{1 - q} = \displaystyle\sum_{x=0}^{\infty}q^x$$ ($$-1 < q < 1$$).

$$\to$$ By the fundamental theorem on power series (term-by-term differentiation),

$$
\frac{1}{(1 - q)^2} = \sum_{x=0}^{\infty}xq^{x-1}, \qquad \frac{2}{(1 - q)^3} = \sum_{x=0}^{\infty}x(x - 1)q^{x-2} \qquad (-1 < q < 1).
$$

Using these, $$E(X)$$ and $$\mathrm{Var}(X)$$ can be found. $$\square$$

### 1.5 Negative binomial distribution

> **Notation.** $$X \sim \mathrm{Negbin}(r, p)$$, $$r = 1, 2, \dots$$, $$p \in [0, 1]$$.
>
> **Meaning.** In a Bernoulli process with success probability $$p$$, the number of failures that occur until the $$r$$-th success.
{: .definition #def-negative-binomial }

**Properties.**

1. PDF: $$f(x) = \dbinom{x + r - 1}{x}p^r(1 - p)^x$$, $$x = 0, 1, 2, \dots$$
2. MGF: $$M_X(t) = \Bigl(\dfrac{p}{1 - qe^t}\Bigr)^r$$, $$t < -\log q$$, $$q = 1 - p$$.
3. $$X \sim \mathrm{Negbin}(r, p) \iff X \overset{d}{=} W_r - r$$, where $$W_r = \min\{n : X_1 + \cdots + X_n \ge r\}$$.
4. $$X \sim \mathrm{Negbin}(r, p) \iff X \overset{d}{=} X_1 + \cdots + X_r$$, $$X_i \overset{iid}{\sim} \mathrm{Geo}(p)$$.
5. $$E(X) = r\dfrac{q}{p}$$, $$\mathrm{Var}(X) = r\dfrac{q}{p^2}$$.
6. Let $$X_1 \sim \mathrm{Negbin}(r_1, p)$$ and $$X_2 \sim \mathrm{Negbin}(r_2, p)$$. If $$X_1 \perp X_2$$, then $$X_1 + X_2 \sim \mathrm{Negbin}(r_1 + r_2, p)$$ and

   $$
   P(X_1 = x \mid X_1 + X_2 = t) = \frac{\binom{x + r_1 - 1}{x}\binom{t + r_2 - x - 1}{t - x}}{\binom{t + r_1 + r_2 - 1}{t}}.
   $$

*Proof.* ① Show that $$f$$ is a density function.

$$
p^{-r} = (1 + (p - 1))^{-r} = \sum_{x=0}^{\infty}\binom{-r}{x}(p - 1)^x = \sum_{x=0}^{\infty}\frac{(-r)(-r-1)\cdots(-r-x+1)}{(x)_x}(p - 1)^x = \sum_{x=0}^{\infty}\frac{(-1)^x[r]_x}{(x)_x}(p - 1)^x = \sum_{x=0}^{\infty}\binom{x + r - 1}{x}(1 - p)^x.
$$

Multiplying both sides by $$p^r$$, $$\sum_{x=0}^{\infty}\binom{x + r - 1}{x}(1 - p)^xp^r = 1$$.

④ (1) Use the MGF. (2) Use the Bernoulli process. $$X \overset{d}{=} W_r - r$$ (waiting time) $$= (W_1 - 1) + (W_2 - W_1 - 1) + \cdots + (W_r - W_{r-1} - 1)$$.

$$
P(W_1 - 1 = y_1, \dots, W_r - W_{r-1} - 1 = y_r) = q^{y_1}p \cdots q^{y_r}p = q^{\sum_{i=1}^{r}y_i}p^r = \Bigl(\prod_{i=1}^{r-1}P(W_{i+1} - W_i - 1 = y_{i+1})\Bigr)P(W_1 - 1 = y_1).
$$

$$\therefore$$ $$W_1 - 1$$, $$W_{i+1} - W_i - 1$$ are independent ($$i = 1, \dots, r - 1$$), and $$W_1 - 1$$, $$W_{i+1} - W_i - 1$$ are $$\overset{iid}{\sim} \mathrm{Geo}(p)$$. $$\square$$

### 1.6 Hypergeometric distribution

**Definition and notation.** A box holds $$N$$ balls: $$M$$ red balls and $$N - M$$ white balls. Draw a sample of $$n$$ balls, and let $$X$$ be the number of red balls. Then

$$
P(X = x) = \frac{\binom{M}{x}\binom{N - M}{n - x}}{\binom{N}{n}}, \qquad x = \max(0, M + n - N) \sim \min(n, M).
$$

Write $$X \sim \mathrm{Hypergeo}(N, M, n)$$.

**Properties.**

① Characteristics.

$$
E(X) = \frac{M}{N}n, \qquad \mathrm{Var}(X) = \frac{N - n}{N - 1}\cdot n\cdot\frac{M}{N}\Bigl(1 - \frac{M}{N}\Bigr),
$$

with $$p = M/N$$ and $$q = 1 - M/N$$. The factor $$\frac{N - n}{N - 1} \to 1$$ as $$N \to \infty$$ (finite population correction).

② Approximation by the binomial distribution.

$$
\lim_{N \to \infty}P(X = x) = P(B = x), \qquad B \sim \mathrm{Bin}(n, p),\ p = M/N.
$$

*Proof.* ① Start the proof under the assumption $$n \le \min(M, N - M)$$. ② Do it yourself.

### 1.7 Multinomial distribution

**Basics and meaning.** $$(X_1, \dots, X_k) \sim \mathrm{Multi}(n, (p_1, \dots, p_k))$$, $$p_i \ge 0$$, $$\sum p_i = 1$$. There are $$k$$ possible outcomes $$\{1, \dots, k\}$$. In one trial, the probability that $$i$$ occurs is $$p_i$$. Let $$X_i$$ be the number of times $$i$$ occurred in $$n$$ trials; then we say $$(X_1, \dots, X_k) \sim \mathrm{Multi}(n, (p_1, \dots, p_k))$$.

**Properties.**

① Density function.

$$
P(X_1 = x_1, \dots, X_k = x_k) = \binom{n}{x_1, \dots, x_k}p_1^{x_1}\cdots p_k^{x_k} = \frac{n!}{x_1!x_2!\cdots x_k!}p_1^{x_1}\cdots p_k^{x_k}.
$$

\* Other notations: for economy, some write it excluding the $$k$$-th result.

② MGF.

$$
M_{X_1, \dots, X_k}(t_1, \dots, t_k) = (p_1e^{t_1} + \cdots + p_ke^{t_k})^n, \qquad -\infty < t_1, \dots, t_k < \infty.
$$

③ If $$(X_1, \dots, X_k) \sim \mathrm{Multi}(n, (p_1, \dots, p_k))$$, the following hold.

- (a) $$X_i \sim \mathrm{Bin}(n, p_i)$$.
- (b) $$(X_1, X_2, n - X_1 - X_2) \sim \mathrm{Trinomial}\bigl(n, (p_1, p_2, 1 - (p_1 + p_2))\bigr)$$.
- (c) $$(X_2, \dots, X_k) \mid X_1 = x_1 \ \sim\ \mathrm{Multi}\Bigl(n - x_1, \Bigl(\dfrac{p_2}{1 - p_1}, \dots, \dfrac{p_k}{1 - p_1}\Bigr)\Bigr)$$.

④ $$E(X_i) = np_i$$, $$\mathrm{Var}(X_i) = np_i(1 - p_i)$$, $$\mathrm{Cov}(X_i, X_j) = -np_ip_j$$ ($$i \ne j$$).

cf) Multinomial expansion.

$$
(p_1 + \cdots + p_k)^n = \sum_{\substack{x_i \ge 0 \\ \sum_{i=1}^{k}x_i = n}}\binom{n}{x_1, \dots, x_k}p_1^{x_1}\cdots p_k^{x_k}.
$$

## Supplement from the textbook

**Geometric and negative binomial in the textbook (§3.3).** Observe mutually independent Bernoulli trials with success rate $$p$$ and let $$W_1$$ be the number of *trials* up to the first success. Then $$P(W_1 = x) = (1 - p)^{x-1}p$$, $$x = 1, 2, \dots$$; this is the geometric distribution, written $$W_1 \sim \mathrm{Geo}(p)$$ (the name comes from $$\sum_{x=1}^{\infty}q^{x-1}$$ being a geometric series). With $$W_r$$ the number of trials up to the $$r$$-th success,

$$
P(W_r = x) = \binom{x - 1}{r - 1}p^r(1 - p)^{x-r}, \qquad x = r, r + 1, \dots,
$$

the negative binomial distribution $$W_r \sim \mathrm{Negbin}(r, p)$$. In the textbook convention,

- $$E(W_1) = 1/p$$, $$\mathrm{Var}(W_1) = q/p^2$$, $$mgf_{W_1}(t) = (1 - qe^t)^{-1}e^tp$$, $$t < -\log q$$;
- $$E(W_r) = r/p$$, $$\mathrm{Var}(W_r) = rq/p^2$$, $$mgf_{W_r}(t) = \{pe^t(1 - qe^t)^{-1}\}^r$$, $$t < -\log q$$;
- the differences $$W_1, W_2 - W_1, \dots, W_r - W_{r-1}$$ are $$\overset{iid}{\sim} \mathrm{Geo}(p)$$, so $$\mathrm{Negbin}(r, p) \overset{d}{=} \mathrm{Geo}_1(p) \oplus \cdots \oplus \mathrm{Geo}_r(p)$$; and if $$X_1 \sim \mathrm{Negbin}(r_1, p)$$, $$X_2 \sim \mathrm{Negbin}(r_2, p)$$ are independent, $$X_1 + X_2 \sim \mathrm{Negbin}(r_1 + r_2, p)$$.

The cumulant generating function of $$W_1$$ is $$cgf_{W_1}(t) = t - \log\bigl\{1 - \frac{q}{p}(e^t - 1)\bigr\}$$, and expanding it with $$-\log(1 - A) = A + A^2/2 + \cdots$$ gives $$cgf_{W_1}(t) = \frac{1}{p}t + \frac{1}{2}\frac{q}{p^2}t^2 + \cdots$$, hence the mean and variance. The name "negative binomial" comes from the expansion $$(1 + t)^{-r} = \sum_{k=0}^{\infty}\frac{(r + k - 1)!}{k!(r - 1)!}(-t)^k$$, $$-1 < t < 1$$, shown above in 1.5. The probabilities can be computed with R (Appendix III); in Figure 3.3.1 the probability bars start at $$x = r$$, rise to a peak near $$(r - 1)/p$$, and fall off.

**Hypergeometric distribution (§3.1).** Choosing $$n$$ "at random" from a population of $$N$$ individuals means taking them one at a time with equal probability, without putting back what was taken: *sampling without replacement*, called *simple random sampling*. If $$D$$ of the $$N$$ are ones (the population proportion is $$p = D/N$$) and $$X$$ is the number of ones in the sample of size $$n$$, then $$f(x) = \binom{D}{x}\binom{N - D}{n - x}\big/\binom{N}{n}$$, written $$X \sim H(n; N, D)$$; this is $$\mathrm{Hypergeo}(N, M, n)$$ with $$M = D$$. Its mean is

$$
E(X) = \sum_x x\binom{D}{x}\binom{N - D}{n - x}\Big/\binom{N}{n} = D\sum_x\binom{D - 1}{x - 1}\binom{N - D}{n - x}\Big/\binom{N}{n} = D\binom{N - 1}{n - 1}\Big/\binom{N}{n} = \frac{nD}{N},
$$

where the third equality follows by comparing the coefficients of $$t^{n-1}$$ in $$(1 + t)^{D-1}(1 + t)^{N-D} = (1 + t)^{N-1}$$. In the same way $$E[X(X - 1)] = n(n - 1)D(D - 1)/(N(N - 1))$$, and

$$
\mathrm{Var}(X) = E[X(X - 1)] + E(X) - (E(X))^2 = \frac{N - n}{N - 1}\,n\frac{D}{N}\Bigl(1 - \frac{D}{N}\Bigr).
$$

**Example 3.1.1.** For quality control, a lot of $$N = 60$$ items is rejected when the number of defective items in a simple random sample of $$n = 5$$ exceeds a tolerance. If the actual defective rate is $$10\%$$, that is, $$D = 6$$, what tolerance $$c$$ makes the probability of rejecting the lot at most $$1\%$$? We need $$\sum_{x=0}^{c}\binom{6}{x}\binom{54}{5-x}\big/\binom{60}{5} \ge 0.99$$. The cumulative probabilities of $$H(5; 60, 6)$$ are:

- $$c = 0$$: $$0.57905$$
- $$c = 1$$: $$0.92648$$
- $$c = 2$$: $$0.99461$$
- $$c = 3$$: $$0.99985$$
- $$c = 4$$: $$0.99999$$
- $$c = 5$$: $$1.00000$$

so $$c = 2$$: accept the lot when the number of defective items is at most $$2$$.

**Approximation.** When $$N$$ is large relative to $$n$$,

$$
\binom{D}{x}\binom{N - D}{n - x}\Big/\binom{N}{n} = \binom{n}{x}\frac{D(D - 1)\cdots(D - x + 1)}{N(N - 1)\cdots(N - x + 1)}\cdot\frac{(N - D)\cdots(N - D - n + x + 1)}{(N - x)\cdots(N - n + 1)} \approx \binom{n}{x}\Bigl(\frac{D}{N}\Bigr)^x\Bigl(1 - \frac{D}{N}\Bigr)^{n-x},
$$

the probability for sampling with replacement: as $$N$$ becomes large, the effect of sampling without replacement disappears.

**Multinomial distribution (§3.2).** Drawing with replacement from a population classified into $$k$$ types with proportions $$p_1, \dots, p_k$$ is a sequence of mutually independent multinomial trials. If one draw is $$Z_i = (Z_{i1}, \dots, Z_{ik})^t$$, then $$P(Z_{i1} = z_1, \dots, Z_{ik} = z_k) = p_1^{z_1}\cdots p_k^{z_k}$$, $$z_j = 0, 1$$, $$z_1 + \cdots + z_k = 1$$; that is, $$Z_i \sim \mathrm{Multi}(1, (p_1, \dots, p_k)^t)$$. For $$k = 2$$, $$\mathrm{Multi}(n, (p, 1 - p)^t)$$ is the joint distribution of $$X$$ and $$n - X$$ for $$X \sim \mathrm{Bin}(n, p)$$.

> **Representational definition of the multinomial distribution.**
>
> $$
> \mathrm{Multi}(n, p) \overset{d}{=} \mathrm{Multi}_1(1, p) \oplus \cdots \oplus \mathrm{Multi}_n(1, p),
> $$
>
> that is, $$X \sim \mathrm{Multi}(n, (p_1, \dots, p_k)^t) \Longleftrightarrow X \overset{d}{=} Z_1 + \cdots + Z_n$$, $$Z_i \overset{iid}{\sim} \mathrm{Multi}(1, (p_1, \dots, p_k)^t)$$.
{: .definition #def-multinomial-representational }

*Proof of ② and ④ (Theorem 3.2.2).* By the representational definition and Theorem 2.5.11, $$E(X) = nE(Z_1)$$, $$\mathrm{Var}(X) = n\mathrm{Var}(Z_1)$$, $$mgf_X(t) = (mgf_{Z_1}(t))^n$$. Since $$P(Z_{1l} = 1) = p_l$$ and $$Z_{1l}Z_{1m} = 0$$ for $$l \ne m$$, $$E(Z_{1l}) = p_l$$ and $$\mathrm{Cov}(Z_{1l}, Z_{1m}) = E(Z_{1l}Z_{1m}) - E(Z_{1l})E(Z_{1m}) = -p_lp_m$$ ($$l \ne m$$), and $$mgf_{Z_1}(t) = p_1e^{t_1} + \cdots + p_ke^{t_k}$$. $$\square$$

## References

- 김우철, *수리통계학* (Mathematical Statistics), revised 2nd edition, 민영사, 2021 — Chapter 3, §§3.1 to 3.3 (Example 3.1.1, Theorems 3.2.2, 3.3.1, 3.3.2). The supplement is translated from the book.
- Mathematical Statistics 1 (326.311), Seoul National University, Spring 2025. Instructor: Jaeyong Lee (이재용).

[Previous](/posts/mathstat1-binomial/) · [Overview](/posts/mathstat1-overview/) · [Next](/posts/mathstat1-poisson/)
