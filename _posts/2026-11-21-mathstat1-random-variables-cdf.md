---
title: "Mathematical Statistics 1: Ch. 1 Part 3 — Random Variables, CDFs and Density Functions"
date: 2026-11-21 08:30:00 +0900
categories: [Study Notes, Mathematical Statistics 1]
tags: [random variable, cdf, pdf, discrete, continuous]
description: Random variables and their distributions, the cumulative distribution function and its characterization, discrete and continuous random variables and density functions. Chapter 1, notes section 3 of Mathematical Statistics 1.
math: true
mermaid: false
render_with_liquid: false
---

> My handwritten notes, translated into English. Section 3 of Chapter 1 in my notes. It corresponds to §1.3 and the first half of §1.5 of the textbook. Statements and proofs follow my notes; I only corrected expressions that were mathematically wrong. Material taken from the textbook is collected at the end under "Supplement from the textbook".
{: .prompt-info }

## 3.1 Random variables

> **Definition (Probability space).** $$(\mathcal{C}, \mathbb{B}, P)$$ is the space defined by the probability measure $$P$$ and the sample space $$\mathcal{C}$$ (strictly speaking, with its $$\sigma$$-field $$\mathbb{B}$$).
{: .definition #def-probability-space }

> **Definition (Random variable).**
>
> - (1) $$X$$ is a random variable defined on $$\mathcal{C}$$ $$\Longleftrightarrow$$ $$X$$ is a real-valued function defined on $$\mathcal{C}$$, i.e. $$X : \mathcal{C} \to \mathbb{R}$$.
> - (2) (Space of $$X$$.) The space of $$X$$ $$\Longleftrightarrow$$ the range of $$X$$ $$\Longleftrightarrow$$ $$\{X(\omega)\}$$ for all $$\omega \in \mathcal{C}$$.
> - (3) (Distribution of $$X$$.) $$\rightarrow$$ Having the same probability distribution $$\ne$$ being the same random variable.
>
>   $$
>   P_X(B) := P(X^{-1}(B)) = P(X \in B) \quad \forall B \subseteq \mathbb{R}
>   \qquad \bigl( = P(\{\omega \in \mathcal{C} : X(\omega) \in B\}) \bigr).
>   $$
{: .definition #def-random-variable }

Simply: $$(\mathcal{C}, P) \xrightarrow{\ X\ } (\mathbb{R}, P_X)$$, and for $$B \subseteq \mathbb{R}$$ the preimage $$X^{-1}(B)$$ is sent back by $$X^{-1}$$, so that $$P_X(B) = P(X^{-1}(B))$$.

\* $$P$$: the probability of the background probability space. $$P$$ and $$P_X$$ are different.

But... $$X^{-1}(B)$$ has to be in $$\mathbb{B}$$ (the $$\sigma$$-field) for the probability to be definable (the strict definition), and $$B$$ has to be a Borel set. $$X$$ is *measurable*!

**Example.** (Tossing a coin twice.) $$\mathcal{C} = \{HH, HT, TH, TT\}$$ and $$X$$ maps $$HH \mapsto 2$$, $$HT, TH \mapsto 1$$, $$TT \mapsto 0$$.

$$
P(HH) = \cdots = P(TT) = \tfrac{1}{4}, \qquad
P_X(\{0\}) = \tfrac{1}{4},\ P_X(\{1\}) = \tfrac{1}{2},\ P_X(\{2\}) = \tfrac{1}{4}.
$$

$$P$$ and $$P_X$$ are totally different! $$P$$ is defined on the sample space; $$P_X$$ lives on the real numbers, not on the sample space. From now on, the distribution we talk about is $$P_X$$!

## 3.2 CDFs and density functions

> **Definition (Cumulative distribution function).** $$\rightarrow$$ It is always defined for every random variable!
> The cumulative distribution function (CDF) of a random variable $$X$$ is the function $$F_X : \mathbb{R} \to \mathbb{R}$$ defined by
>
> $$
> F_X(x) = P(X \le x), \qquad x \in \mathbb{R}.
> $$
{: .definition #def-cdf }

> **Theorem (Characterization of CDFs).** A function $$F : \mathbb{R} \to \mathbb{R}$$ is the CDF of some random variable $$X$$ $$\Longleftrightarrow$$
>
> - (1) $$F$$ is non-decreasing. (Note the definition; cf. strictly increasing.)
> - (2) $$\lim_{x \to -\infty} F(x) = 0$$ and $$\lim_{x \to \infty} F(x) = 1$$.
> - (3) $$F$$ is right-continuous, i.e. $$\lim_{x \to x_0+} F(x) = F(x_0)$$ for all $$x_0 \in \mathbb{R}$$.
{: .theorem #thm-cdf-characterization }

*Proof* ($$\Rightarrow$$).

(1) When $$x_1 < x_2$$, $$F(x_1) = P(X \le x_1) \le P(X \le x_2) = F(x_2)$$ ($$\because\ \{X \le x_1\} \subseteq \{X \le x_2\}$$).

(2) $$\lim_{x \to \infty} F(x) = 1$$ $$\Longleftrightarrow$$ $$F(x_n) \to 1$$ for every sequence $$\{x_n\}$$ diverging to $$+\infty$$.

Take an increasing sequence $$\{x_n\}$$ diverging to $$+\infty$$. Then, by continuity of probability,

$$
\lim_{n \to \infty} F(x_n) = \lim_{n \to \infty} P(X \le x_n) = P\Bigl(\bigcup_{n=1}^{\infty} [X \le x_n]\Bigr) = P_X(\mathbb{R}) = 1.
$$

Going to $$-\infty$$ is proved similarly.

(3) For any sequence $$\{x_n\} \to x_0+$$ (decreasing), it suffices to show $$\lim_{n \to \infty} F(x_n) = F(x_0)$$.

$$
\lim_{n \to \infty} F(x_n) = \lim_{n \to \infty} P(X \le x_n) = P\Bigl(\bigcap_{n=1}^{\infty} [X \le x_n]\Bigr) = P(X \le x_0) = F(x_0).
$$

($$\Longleftarrow$$) Difficult, so not proved here. *Idea:* take the probability space $$[0,1]$$ with $$P(dx) = dx$$ (the uniform distribution) and map it to $$\mathbb{R}$$ by $$F^{-1}$$. \* The inverse of an increasing function: $$F^{-1}(u) = \inf\{x : F(x) \ge u\}$$. Then one can show that $$F$$ is the CDF of $$X = F^{-1}(U)$$.

Note: when $$F$$ is strictly increasing and continuous, $$P(F^{-1}(U) \le x) = F(x)$$.

> **Theorem.** If two random variables $$X_1$$ and $$X_2$$ have the same CDF $$F$$, then the probability distributions of $$X_1$$ and $$X_2$$ are the same, i.e. $$P_{X_1} = P_{X_2}$$.
{: .theorem #thm-same-cdf }

*Proof.* Too hard (not proved here). The picture: $$(\mathcal{C}_1, P_1) \xrightarrow{X_1} (\mathbb{R}, P_{X_1})$$ and $$(\mathcal{C}_2, P_2) \xrightarrow{X_2} (\mathbb{R}, P_{X_2})$$. A probability distribution must be defined on all (Borel) subsets of $$\mathbb{R}$$. But this theorem says that probability distributions can be identified by the cumulative distribution function alone! From now on, let's think only of the CDF!

Note. Originally, to show that two probability distributions coincide, one would have to show $$P_{X_1}(B) = P_{X_2}(B)$$ for all $$B \subseteq \mathbb{R}$$. But now it is enough to show $$F_{X_1}(x) = F_{X_2}(x)$$ for all $$x \in \mathbb{R}$$. That is,

$$
F_{X_1}(x) = P_{X_1}((-\infty, x]) = P(X_1 \le x) = P(X_2 \le x) = P_{X_2}((-\infty, x]) = F_{X_2}(x).
$$

It suffices to prove it only for sets of this form!

> **Theorem (Properties of the CDF).**
>
> - (a) $$0 \le F(x) \le 1$$ for all $$x \in \mathbb{R}$$.
> - (b) $$P(a < X \le b) = F(b) - F(a)$$ for all $$a < b$$.
> - (c) For every $$x^* \in \mathbb{R}$$, the left limit of $$F$$ exists, i.e. $$F(x^*-) = \lim_{x \uparrow x^*} F(x)$$ exists (not continuity; only that the limit exists!).
> - (d) $$P(X = x) = F(x) - F(x-)$$.
{: .theorem #thm-cdf-properties }

*Proof of (c).* Take a sequence $$x_n < x^*$$ with $$\lim x_n = x^*$$. Then

$$
\lim_{n \to \infty} F(x_n) = \lim_{n \to \infty} P(X \le x_n) = P\Bigl(\bigcup_{n=1}^{\infty} [X \le x_n]\Bigr) = P(X < x^*) = F(x^*-).
$$

> **Definition (Discrete random variable).**
>
> - (1) If a random variable $$X$$ is a function $$X : (\mathcal{C}, P) \to (\mathbb{D}, P_X)$$ and $$\mathbb{D}$$ is countable (corresponding to $$\mathbb{N}$$!), $$X$$ is called discrete.
> - (2) The *probability density function* (PDF) of $$X$$ is defined as $$f : \mathbb{D} \to \mathbb{R}$$, $$f(x) = P(X = x)$$, $$x \in \mathbb{D}$$.
>
> Note: the PDF of a discrete random variable is also called a *probability mass function* (PMF).
{: .definition #def-discrete }

> **Theorem (Properties of discrete random variables).** Let $$X$$ be a discrete random variable and $$f$$ the PDF of $$X$$.
>
> - (a) For all $$B \subseteq \mathbb{R}$$, $$P(X \in B) = \sum_{x \in B} f(x) = \sum_{x \in B} P(X = x)$$. That is, the probability for $$X$$ can be expressed as a sum of $$f$$.
> - (b) If $$X_1$$ and $$X_2$$ are discrete random variables and their density functions coincide, their probability distributions are the same. (The CDF is not needed!)
{: .theorem #thm-discrete-properties }

> **Definition (Continuous random variable and probability density function).** For a random variable $$X : (\mathcal{C}, P) \to \mathbb{R}$$, if for some integrable function (\*) $$f \ge 0$$,
>
> $$
> P(X \in B) = \int_B f(x)\,dx \qquad \forall B \subseteq \mathbb{R},
> $$
>
> then $$f$$ is called the probability density function of $$X$$ and $$X$$ a continuous random variable.
{: .definition #def-continuous }

Note. Some books define $$X$$ to be continuous when the CDF $$F$$ is continuous, but this is a not-well-known definition. The correct definition (from measure theory): $$X$$ is continuous $$\Longleftrightarrow$$ $$F$$ is **absolutely continuous**.
cf) continuous $$\supseteq$$ uniformly continuous $$\supseteq$$ absolutely continuous.

> **Theorem (Properties of continuous random variables).** If $$X$$ is continuous and $$f$$ is the density function of $$X$$, then
>
> $$
> F_X(x) = P(X \le x) = \int_{-\infty}^{x} f(t)\,dt.
> $$
>
> $$\rightarrow$$ If $$f$$ is continuous at $$x$$, $$F_X'(x) = f(x)$$. (If it is not continuous, this is not necessarily so.)
>
> \* The CDF of a continuous distribution is differentiable except at countably many points (a set of Lebesgue measure 0).
{: .theorem #thm-continuous-properties }

**Example (discrete variable).** $$X$$: the number of heads in two coin tosses.

- $$x = 0$$: $$f(0) = \tfrac{1}{4}$$
- $$x = 1$$: $$f(1) = \tfrac{1}{2}$$
- $$x = 2$$: $$f(2) = \tfrac{1}{4}$$

(The CDF is a step function with jumps $$\tfrac14, \tfrac12, \tfrac14$$ at $$0, 1, 2$$.) \* Let's practice putting $$-\infty$$ as the lower limit of every integral!

**Example (continuous variable).** The sample space is $$\mathcal{C} = \{(x,y) : x^2 + y^2 \le 1\}$$, a disk. For $$C \subseteq \mathcal{C}$$, $$P(C) = A(C)/A(\mathcal{C})$$ ($$A$$ is the area of the set). Set up the probability space. $$R$$ is the distance from the origin to $$(x,y)$$ (here $$(x,y)$$ is chosen randomly from $$\mathcal{C}$$).

$$
F_R(r) = P(R \le r) = \frac{\pi r^2}{\pi} = r^2 \quad (0 \le r \le 1),
\qquad
F_R(r) =
\begin{cases}
0 & (r \le 0), \\
r^2 & (0 \le r \le 1), \\
1 & (r \ge 1).
\end{cases}
$$

$$
\therefore\ f(r) = F_R'(r) =
\begin{cases}
0 & (r \le 0), \\
2r & (0 < r < 1), \\
0 & (r > 1).
\end{cases}
$$

$$\rightarrow$$ At $$1$$ the density function is not defined. (Whatever value is taken at $$1$$, integrating it gives $$F$$, so infinitely many density functions exist.)

**Example (neither continuous nor discrete).** Toss a coin; if it is heads, $$X = 1$$; if tails, let $$X$$ be a number chosen at random from $$[0,1]$$.

$$
P(X \le x) =
\begin{cases}
0 & (x \le 0), \\
P(H)P(X \le x \mid H) + P(T)P(X \le x \mid T) & (0 \le x < 1), \\
P(H)P(X \le x \mid H) + P(T)P(X \le x \mid T) & (x \ge 1)
\end{cases}
=
\begin{cases}
0 & (x \le 0), \\
\tfrac{1}{2} \cdot 0 + \tfrac{1}{2}\, x = \tfrac{1}{2}x & (0 \le x < 1), \\
\tfrac{1}{2} \cdot 1 + \tfrac{1}{2} \cdot 1 = 1 & (x \ge 1).
\end{cases}
$$

(The CDF $$F_X$$ rises linearly from $$0$$ to $$\tfrac12$$ on $$[0,1)$$ and jumps to $$1$$ at $$x = 1$$.)

## Supplement from the textbook

> The parts below are in the textbook (§1.3) but not in my notes. They are translated from the book and are not my own writing.
{: .prompt-info }

**Example 1.3.3 (tossing a coin until heads).** The sample space is $$\mathcal{C} = \{H, TH, TTH, TTTH, \dots\}$$. If $$X$$ is the number of tosses, then $$X$$ takes every positive integer and $$P(X = 1) = P(H) = \tfrac{1}{2}$$, $$P(X = 2) = P(TH) = \tfrac{1}{4}$$, $$P(X = 3) = P(TTH) = \tfrac{1}{8}, \dots$$, i.e. $$P(X = x) = (1/2)^x$$, $$x = 1, 2, \dots$$.

**Basic properties of a pdf.** For a discrete random variable, (a) $$f(x) \ge 0$$ for all $$x$$, with $$f(x) = 0$$ unless $$x$$ is one of the values $$x_1, x_2, \dots$$; (b) $$\sum_x f(x) = \sum_k f(x_k) = 1$$; (c) $$\sum_{x : a < x \le b} f(x) = P(a < X \le b)$$. For a continuous random variable, (a) $$f(x) \ge 0$$ for all $$x$$; (b) $$\int_{-\infty}^{\infty} f(x)\,dx = 1$$; (c) $$\int_a^b f(x)\,dx = P(a < X \le b)$$.

For a continuous random variable $$P(X = a) = \int_a^a f(x)\,dx = 0$$, and the value $$f(a)$$ is not $$P(X = a)$$; only the approximation $$P(a < X \le a + \Delta x) \approx f(a)\,\Delta x$$ holds for small $$\Delta x$$. With the indicator function $$I_A(x) = 1$$ ($$x \in A$$), $$0$$ ($$x \notin A$$), a density such as the one below is written compactly.

**Example 1.3.5.** Find the constant $$c$$ for which $$f(x) = c\,x(1 - x)$$ ($$0 < x < 1$$), $$0$$ otherwise, is a pdf, and compute $$P(\tfrac{1}{2} \le X \le \tfrac{3}{4})$$.

*Solution.* The total probability must be $$1$$: $$\int_0^1 c\,x(1 - x)\,dx = c\bigl[\tfrac{x^2}{2} - \tfrac{x^3}{3}\bigr]_0^1 = \tfrac{c}{6} = 1$$, so $$c = 6$$ and $$f(x) = 6x(1 - x)\,I_{[0,1]}(x)$$. Then

$$
P\bigl(\tfrac{1}{2} \le X \le \tfrac{3}{4}\bigr) = \int_{1/2}^{3/4} 6x(1 - x)\,dx = \bigl[3x^2 - 2x^3\bigr]_{1/2}^{3/4} = \tfrac{27}{32} - \tfrac{16}{32} = \tfrac{11}{32}.
$$

## References

- 김우철, *수리통계학* (Mathematical Statistics), revised 2nd edition, 민영사, 2021 — Chapter 1.
- Mathematical Statistics 1 (326.311), Spring 2025. Instructor: Jaeyong Lee (이재용). My handwritten lecture notes, Chapter 1.
- The notes are translated without changing their wording; remarks written in the margins of the notes are kept. Where a statement in the notes was mathematically wrong it is corrected in the text.

[Previous](/posts/mathstat1-conditional-probability/) · [Overview](/posts/mathstat1-overview/) · [Next](/posts/mathstat1-expectation-mgf/)
