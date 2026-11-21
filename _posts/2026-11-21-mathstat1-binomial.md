---
title: "Mathematical Statistics 1: Ch. 3 Part 1 — Bernoulli and Binomial Distributions"
date: 2026-11-21 11:10:00 +0900
categories: [Study Notes, Mathematical Statistics 1]
tags: [bernoulli, binomial, binomial theorem, bernoulli process, mgf]
description: The Bernoulli distribution, the binomial expansion, and the binomial distribution with its density, moment generating function, mean, variance and representation as a sum of Bernoulli variables. Chapter 3, notes sections 1.1 to 1.3 of Mathematical Statistics 1.
math: true
mermaid: false
render_with_liquid: false
---

> My handwritten notes, translated into English. Chapter 3 of my notes, "Various Distributions", starts with the distributions related to the binomial distribution; this post covers sections 1.1 to 1.3. It corresponds to §3.2 of the textbook. Statements and proofs follow my notes. Material taken from the textbook is collected at the end under "Supplement from the textbook". The exercises are in [Chapter 3 Exercises](/posts/mathstat1-exercises-chapter-3/).
{: .prompt-info }

## 1. Distributions related to the binomial distribution

### 1.1 Bernoulli distribution

> **Notation.** $$X \sim \mathrm{Ber}(p)$$ ($$0 \le p \le 1$$).
{: .definition #def-bernoulli }

**Properties.**

1. Density function:

   $$
   f(x) = p^x(1 - p)^{1-x} \quad (x = 0, 1), \qquad\text{that is,}\qquad f(x) = \begin{cases} p & (x = 1) \\ 1 - p & (x = 0). \end{cases}
   $$

2. MGF: $$M(t) = pe^t + q$$, $$t \in \mathbb{R}$$, $$p + q = 1$$.
3. Moments: $$E(X) = p$$, $$\mathrm{Var}(X) = p(1 - p)$$, $$E(X^k) = p$$ for all $$k \ge 1$$.

*Proof.* (2) $$E(e^{tX}) = pe^t + qe^0 = pe^t + q$$. (3) $$\mathrm{Var}(X) = E(X^2) - (E(X))^2 = p - p^2 = p(1 - p)$$. $$\square$$

### 1.2 Binomial expansion

> **Definition (Binomial coefficient).**
>
> $$
> \binom{\alpha}{k} = \frac{\alpha(\alpha - 1)\cdots(\alpha - k + 1)}{k!} = \frac{(\alpha)_k}{k!}, \qquad \alpha \in \mathbb{C},\ k \ge 0.
> $$
{: .definition #def-binomial-coefficient }

\* $$(\alpha)_k$$ is the *falling factorial* (descending factorial).

cf) $$\binom{\alpha}{0} = 1$$ is defined by the empty product, $$0! = 1$$. In other words, $$\binom{\alpha}{k} = \dfrac{(\alpha)_k}{(k)_k}$$.

\* There is also the *ascending factorial*: $$[\alpha]_k := \alpha(\alpha + 1)\cdots(\alpha + k - 1)$$.

> **Theorem (Binomial theorem and its properties).**
>
> - (1) $$(1 + x)^{\alpha} = \displaystyle\sum_{k=0}^{\infty}\binom{\alpha}{k}x^k$$, $$\alpha \in \mathbb{C}$$, $$\lvert x\rvert < 1$$.
> - (2) $$\displaystyle\sum_{k=0}^{\infty}\binom{\alpha}{k}x^k$$ converges absolutely for $$\lvert x\rvert < 1$$.
> - (3) $$(a + b)^n = \displaystyle\sum_{k=0}^{n}\binom{n}{k}a^kb^{n-k}$$, $$n \in \mathbb{N}$$, $$a, b \in \mathbb{R}$$.
> - (4) $$\dbinom{\alpha}{k-1} + \dbinom{\alpha}{k} = \dbinom{\alpha + 1}{k}$$ (Pascal's theorem).
> - (5) $$\dbinom{-r}{k} = (-1)^k\dbinom{r + k - 1}{k}$$, $$r > 0$$, $$k = 1, 2, \dots$$
{: .theorem #thm-binomial-theorem }

*Proof.* (Sketch.) Prove (2) (ratio test). From (1), show that the left and right sides are equal. (Note: a Taylor series does not always converge to the function; one must check that the error term of the finite expansion goes to $$0$$ as $$n \to \infty$$.)

For (5),

$$
\binom{-r}{k} = \frac{(-r)_k}{k!} = \frac{(-r)(-r - 1)\cdots(-r - k + 1)}{k!} = (-1)^k\frac{[r]_k}{k!} = (-1)^k\binom{r + k - 1}{k}. \qquad \square
$$

### 1.3 Binomial distribution

> **Definition (Bernoulli process).** A sequence of infinitely repeated random variables (a stochastic process) $$X_1, X_2, \dots \overset{iid}{\sim} \mathrm{Ber}(p)$$, $$(X_n, n \ge 1)$$, is called a *Bernoulli process*.
{: .definition #def-bernoulli-process }

> **Notation.** $$X \sim \mathrm{Bin}(n, p)$$, $$n \in \mathbb{N}$$, $$p \in [0, 1]$$.
{: .definition #def-binomial }

**Properties.**

1. PDF: $$f(x) = \dbinom{n}{x}p^x(1 - p)^{n-x}$$, $$x = 0, 1, \dots, n$$.
2. MGF: $$M(t) = (pe^t + q)^n$$, $$t \in \mathbb{R}$$, $$q = 1 - p$$, $$n \in \mathbb{N}$$.
3. $$E(X) = np$$, $$\mathrm{Var}(X) = npq$$.
4. $$X \sim \mathrm{Bin}(n, p) \iff X \overset{d}{=} X_1 + \cdots + X_n$$, $$X_i \overset{iid}{\sim} \mathrm{Ber}(p)$$.
5. (Independent.) If $$X_1 \sim \mathrm{Bin}(n_1, p)$$ and $$X_2 \sim \mathrm{Bin}(n_2, p)$$ are independent, then $$X_1 + X_2 \sim \mathrm{Bin}(n_1 + n_2, p)$$.

*Proof.* (1) By the binomial theorem,

$$
\sum_{x=0}^{n}f(x) = \sum_{x=0}^{n}\binom{n}{x}p^x(1 - p)^{n-x} = (p + (1 - p))^n = 1,
$$

so $$f$$ is a density function.

(2)

$$
M_X(t) = E(e^{tX}) = \sum_{x=0}^{n}e^{tx}\binom{n}{x}p^xq^{n-x} = \sum_{x=0}^{n}\binom{n}{x}(pe^t)^xq^{n-x} = (pe^t + q)^n.
$$

(3)

$$
E(X) = \sum_{x=0}^{n}x\binom{n}{x}p^xq^{n-x} = \sum_{x=1}^{n}x\frac{n!}{x!(n-x)!}p^xq^{n-x} = \sum_{x=1}^{n}\frac{n!}{(x-1)!(n-x)!}p^xq^{n-x}
$$

$$
= np\sum_{x=1}^{n}\frac{(n-1)!}{(x-1)!(n-x)!}p^{x-1}q^{n-x} = np\sum_{t=0}^{n-1}\frac{(n-1)!}{t!(n-1-t)!}p^tq^{n-1-t} = np(p + q)^{n-1} = np \qquad (\because p + q = 1).
$$

$$
\mathrm{Var}(X) = E(X^2) - (E(X))^2 = E\bigl(X(X - 1)\bigr) + E(X) - (E(X))^2,
$$

where $$E(X(X-1)) = n(n-1)p^2$$, $$E(X) = np$$ and $$(E(X))^2 = n^2p^2$$, so $$\mathrm{Var}(X) = np - np^2 = npq$$.

(4) Two ways: ① show that the densities are the same, or show that the MGFs are the same. ② $$X_1 + \cdots + X_n$$ counts the number of heads in $$n$$ tosses of a coin. For $$P(X_1 + \cdots + X_n = k)$$, consider the table of outcomes of $$X_1, \dots, X_n$$: a sequence with $$k$$ successes (probability $$p$$ each) and $$n - k$$ failures (probability $$1 - p$$ each) has probability $$p^kq^{n-k}$$. How many such sequences are possible? $$\binom{n}{k}$$. Therefore

$$
P(X_1 + \cdots + X_n = k) = \binom{n}{k}p^kq^{n-k}. \qquad \square
$$

## Supplement from the textbook

Property 5 above and the representational viewpoint are written in the textbook as follows (§3.2).

**Sampling with replacement.** When each individual is classified into the two kinds $$0$$ or $$1$$ and one is drawn with replacement from a population whose proportion of $$1$$ is $$p$$, the results of the draws $$Z_1, Z_2, \dots, Z_n, \dots$$ are mutually independent and each has the distribution $$P(Z_i = 1) = p$$, $$P(Z_i = 0) = 1 - p$$. This is the Bernoulli distribution, and mutually independent Bernoulli trials observe such variables. Calling $$1$$ and $$0$$ "success" and "failure", the binomial distribution is the distribution of the number of successes in mutually independent Bernoulli trials.

> **Representational definition of the binomial distribution.** (Here $$X \overset{d}{=} Y$$ means "the random variables $$X$$ and $$Y$$ have the same distribution", and the symbol $$\oplus$$ denotes the sum of random variables that are mutually independent or have correlation coefficient $$0$$.)
>
> $$
> \mathrm{Bin}(n, p) \overset{d}{=} \mathrm{Ber}_1(p) \oplus \cdots \oplus \mathrm{Ber}_n(p),
> $$
>
> that is, $$X \sim \mathrm{Bin}(n, p) \Longleftrightarrow X \overset{d}{=} Z_1 + \cdots + Z_n$$, $$Z_i \overset{iid}{\sim} \mathrm{Ber}(p)$$ ($$i = 1, \dots, n$$).
{: .definition #def-binomial-representational }

*Proof of property 5 (Theorem 3.2.1).* By the representational definition and the theorem on sums of independent random variables (Theorem 2.5.11), $$mgf_{X_i}(t) = (pe^t + q)^{n_i}$$ ($$i = 1, 2$$), so $$mgf_{X_1 + X_2}(t) = mgf_{X_1}(t)\,mgf_{X_2}(t) = (pe^t + q)^{n_1 + n_2}$$. The right side is the mgf of $$\mathrm{Bin}(n_1 + n_2, p)$$, so by the uniqueness of the mgf, $$X_1 + X_2 \sim \mathrm{Bin}(n_1 + n_2, p)$$. $$\square$$

**Example 3.2.1.** For mutually independent random variables $$X_1, \dots, X_N$$ following $$\mathrm{Ber}(p)$$ ($$0 < p < 1$$), show that

$$
X_1 + \cdots + X_D \mid X_1 + \cdots + X_N = n \ \sim\ \mathrm{Hypergeo}(N, D, n) \qquad (D \le N),
$$

that is, given $$X_1 + \cdots + X_N = n$$, the conditional distribution of $$X_1 + \cdots + X_D$$ is the hypergeometric distribution of [Part 2](/posts/mathstat1-geometric-negative-binomial/).

*Proof.* From the definition of conditional probability,

$$
P(X_1 + \cdots + X_D = x \mid X_1 + \cdots + X_N = n) = \frac{P(X_1 + \cdots + X_D = x,\ X_{D+1} + \cdots + X_N = n - x)}{P(X_1 + \cdots + X_N = n)}.
$$

Since $$X_1 + \cdots + X_D$$ and $$X_{D+1} + \cdots + X_N$$ are mutually independent and follow $$\mathrm{Bin}(D, p)$$ and $$\mathrm{Bin}(N - D, p)$$, this is

$$
\frac{\binom{D}{x}p^x(1 - p)^{D-x}\binom{N - D}{n - x}p^{n-x}(1 - p)^{N-D-(n-x)}}{\binom{N}{n}p^n(1 - p)^{N-n}} = \binom{D}{x}\binom{N - D}{n - x}\Big/\binom{N}{n},
$$

the probability of the hypergeometric distribution. $$\square$$

**Shape.** The shape of the binomial distribution can be drawn with R (Figure 3.2.1 of the book: $$n = 10$$ with $$p = 0.1, 0.3, 0.5, 0.7, 0.9$$). The probability polygon moves from the left end to the right end as $$p$$ grows, and is symmetric for $$p = 0.5$$.

## References

- 김우철, *수리통계학* (Mathematical Statistics), revised 2nd edition, 민영사, 2021 — Chapter 3, §3.2 (representational definition, Theorem 3.2.1, Example 3.2.1). The supplement is translated from the book.
- Mathematical Statistics 1 (326.311), Seoul National University, Spring 2025. Instructor: Jaeyong Lee (이재용).

[Previous: Chapter 2 Part 5](/posts/mathstat1-multivariate/) · [Overview](/posts/mathstat1-overview/) · [Next](/posts/mathstat1-geometric-negative-binomial/)
