---
title: "Measure Theory and Real Analysis: 3A Integration with Respect to a Measure"
date: 2026-11-14 14:20:00 +0900
categories: [Study Notes, Measure Theory and Real Analysis]
tags: [integration, lower lebesgue sum, monotone convergence theorem, simple functions, fatou's lemma, dominated monotone, exercises]
description: S-partitions and lower Lebesgue sums, the integral of a nonnegative function, the Monotone Convergence Theorem, additivity of integration, the integral of a real-valued function and its properties, with worked exercises 1 to 4, 7, 8, 10 to 12, 16 to 18 and 20. Section 3A of Axler's Measure, Integration & Real Analysis.
math: true
mermaid: false
render_with_liquid: false
---

> Typeset from my handwritten notes for section 3A of Axler's *Measure,
> Integration & Real Analysis*. The exercise statements are the textbook's;
> the answers are mine, as I wrote them. Where an answer of mine stopped
> short, the end is completed along the same lines. Part of the
> [course overview](/posts/measure-theory-overview/).
{: .prompt-info }

## Notes

> **Definition ($$\mathcal{S}$$-partition).** Suppose $$\mathcal{S}$$ is a
> $$\sigma$$-algebra on a set $$X$$. An *$$\mathcal{S}$$-partition* of $$X$$ is
> a finite collection $$A_1, \dots, A_m$$ where for every $$i \in \{1, \dots,
> m\}$$, $$A_i \in \mathcal{S}$$ and for $$i \ne j$$, $$A_i \cap A_j = \emptyset$$,
> such that $$A_1 \cup \cdots \cup A_m = X$$.
{: .definition #def-s-partition }

The next definition recalls the definition of the lower Riemann sum. However,
we now work with an arbitrary measure and hence $$X$$ need not be a subset of
$$\mathbb{R}$$. Also, even in the case when $$X = [a, b]$$ and $$\mu$$ is
Lebesgue measure on the Borel subsets of $$[a, b]$$, the $$\mathcal{S}$$-partition
need not be Borel subsets of $$[a, b]$$ but only need to be subintervals of
$$[a, b]$$.

> **Definition (Lower Lebesgue sum).** Suppose $$(X, \mathcal{S}, \mu)$$ is a
> measure space, $$f : X \to [0, \infty]$$ is $$\mathcal{S}$$-measurable, and
> $$P$$ is an $$\mathcal{S}$$-partition $$A_1, \dots, A_m$$ of $$X$$. The *lower
> Lebesgue sum* $$\mathcal{L}(f, P)$$ is defined by
>
> $$
> \mathcal{L}(f, P) = \sum_{j=1}^{m} \mu(A_j) \inf_{A_j} f.
> $$
{: .definition #def-lower-lebesgue-sum }

**Example.** Define $$X = [0, 1]$$, $$\mathcal{S}$$ the set of all Borel subsets
of $$X$$ and $$\mu$$ the Lebesgue measure on $$X$$. Let

$$
f = \begin{cases} 1 & x \notin \mathbb{Q} \\ 0 & x \in \mathbb{Q}. \end{cases}
$$

Consider the partition $$P = \{[0, 1] \cap \mathbb{Q},\ [0, 1] \setminus
\mathbb{Q}\}$$. Then

$$
\mathcal{L}(f, P) = \mu([0, 1] \cap \mathbb{Q}) \inf_{[0,1] \cap \mathbb{Q}} f +
\mu([0, 1] \setminus \mathbb{Q}) \inf_{[0,1] \setminus \mathbb{Q}} f = 0 \times 0 + 1
\times 1 = 1.
$$

Also, consider the partition $$P = \{[0, \frac{1}{2}], (\frac{1}{2}, 1]\}$$. Then

$$
\mathcal{L}(f, P) = \mu([0, \tfrac{1}{2}]) \inf_{[0, 1/2]} f + \mu((\tfrac{1}{2}, 1])
\inf_{(1/2, 1]} f = \tfrac{1}{2} \times 0 + \tfrac{1}{2} \times 0 = 0.
$$

Each $$\mathcal{S}$$-partition $$A_1, \dots, A_m$$ of $$X$$ leads to an
approximation of $$f$$ from below by the $$\mathcal{S}$$-measurable simple
function $$\sum_{j=1}^{m} (\inf_{A_j} f)\chi_{A_j}$$, suggesting that
$$\sum_{j=1}^{m} \mu(A_j) \inf_{A_j} f$$ is the proper approximation from below
of our intuitive notion of $$\int f\,d\mu$$.

> **Definition (Integral of a nonnegative function).** Suppose
> $$(X, \mathcal{S}, \mu)$$ is a measure space and $$f : X \to [0, \infty]$$ is
> $$\mathcal{S}$$-measurable. The *integral* of $$f$$ with respect to $$\mu$$,
> denoted $$\int f\,d\mu$$, is defined by
>
> $$
> \int f\,d\mu = \sup\{\mathcal{L}(f, P) : P \text{ is an } \mathcal{S}\text{-partition
> of } X\}.
> $$
{: .definition #def-integral-nonnegative }

$$\circledast$$ We want the definition above to hold:

1. $$\forall E \in \mathcal{S}$$, $$\int \chi_E\,d\mu = \mu(E)$$.
2. $$\int (f + g)\,d\mu = \int f\,d\mu + \int g\,d\mu$$, which will be proved
   later.

> **Theorem (Integral of a characteristic function).** Suppose
> $$(X, \mathcal{S}, \mu)$$ is a measure space and $$E \in \mathcal{S}$$. Then
> $$\int \chi_E\,d\mu = \mu(E)$$.
{: .theorem #thm-integral-characteristic }

*Proof.* If $$P$$ is the $$\mathcal{S}$$-partition of $$X$$ comprised of $$E$$ and
$$X \setminus E$$, then clearly $$\mathcal{L}(\chi_E, P) = \mu(E)$$. Thus,
$$\int \chi_E\,d\mu \ge \mu(E)$$.

Now, suppose $$P$$ is an $$\mathcal{S}$$-partition $$A_1, \dots, A_m$$ of $$X$$.
Then, $$\mu(A_j) \inf_{A_j}\chi_E$$ equals $$\mu(A_j)$$ if $$A_j \subseteq E$$ and
equals $$0$$ otherwise.

$$
\therefore\ \mathcal{L}(\chi_E, P) = \sum_{j : A_j \subseteq E} \mu(A_j) =
\mu\Bigl( \bigcup_{j : A_j \subseteq E} A_j \Bigr) \le \mu(E).
$$

Thus, $$\int \chi_E\,d\mu \le \mu(E)$$, and hence
$$\mu(E) = \int \chi_E\,d\mu$$. $$\square$$

> **Theorem (Integration is order preserving).** Suppose $$(X, \mathcal{S},
> \mu)$$ is a measure space and $$f, g : X \to [0, \infty]$$ are
> $$\mathcal{S}$$-measurable functions such that $$f(x) \le g(x)$$ $$\forall x
> \in X$$. Then $$\int f\,d\mu \le \int g\,d\mu$$.
{: .theorem #thm-integral-order }

*Proof.* Suppose $$P$$ is an $$\mathcal{S}$$-partition $$A_1, \dots, A_m$$ of
$$X$$. Then $$\inf_{A_j} f \le \inf_{A_j} g$$ for each $$j = 1, \dots, m$$.
Thus, $$\mathcal{L}(f, P) \le \mathcal{L}(g, P)$$. Hence $$\int f\,d\mu \le
\int g\,d\mu$$. $$\square$$

> **Theorem (Integrals via finite simple functions).** Suppose
> $$(X, \mathcal{S}, \mu)$$ is a measure space and $$f : X \to [0, \infty]$$ is
> $$\mathcal{S}$$-measurable. Then
>
> $$
> \int f\,d\mu = \sup\Bigl\{ \sum_{j=1}^{m} c_j\mu(A_j) : A_1, \dots, A_m
> \text{ are disjoint sets in } \mathcal{S},\ c_1, \dots, c_m \in [0, \infty)
> \text{ and } f(x) \ge \sum_{j=1}^{m} c_j\chi_{A_j}(x)\ \forall x \in X \Bigr\}.
> $$
{: .theorem #thm-integral-simple }

*Proof.* Write $$(\ast)$$ for the supremum on the right side.

($$\ge$$) Suppose $$A_1, \dots, A_m$$ are disjoint sets in $$\mathcal{S}$$ and
$$c_1, \dots, c_m \in [0, \infty)$$ with $$f \ge \sum_j c_j\chi_{A_j}$$. Take the
$$\mathcal{S}$$-partition $$P = \{A_1, \dots, A_m, X \setminus \bigcup_j A_j\}$$.
Then $$\inf_{A_j} f \ge c_j$$ and the last set contributes $$\ge 0$$, so
$$\mathcal{L}(f, P) \ge \sum_{j=1}^{m} c_j\mu(A_j)$$. Thus,
$$\int f\,d\mu \ge (\ast)$$.

($$\le$$) Let $$P$$ be an $$\mathcal{S}$$-partition $$A_1, \dots, A_m$$ of $$X$$.
Consider the sets $$A_j$$ with $$\inf_{A_j} f < \infty$$ and take
$$c_j = \inf_{A_j} f$$; then $$f \ge \sum_j c_j\chi_{A_j}$$, so
$$\sum_j c_j\mu(A_j) \le (\ast)$$. The only remaining case is when there exists
$$A_j$$ with $$\mu(A_j) > 0$$ and $$\inf_{A_j} f = \infty$$, which means that
$$f(x) = \infty$$ $$\forall x \in A_j$$. For arbitrary $$t > 0$$, we can take
$$m = 1$$, $$A_1 = A_j$$ and $$c_1 = t$$. Thus, $$(\ast) \ge t\mu(A_j)$$ for all
$$t$$, so $$(\ast) = \infty \ge \mathcal{L}(f, P)$$. In either case
$$\mathcal{L}(f, P) \le (\ast)$$, and taking the supremum over $$P$$ gives
$$\int f\,d\mu \le (\ast)$$. $$\square$$

> **Theorem (Monotone Convergence Theorem).** Suppose $$(X, \mathcal{S}, \mu)$$
> is a measure space and $$0 \le f_1 \le f_2 \le \cdots$$ is an increasing
> sequence of $$\mathcal{S}$$-measurable functions. Define $$f : X \to
> [0, \infty]$$ by $$f(x) = \lim_{k \to \infty} f_k(x)$$. Then
>
> $$
> \lim_{k \to \infty} \int f_k\,d\mu = \int f\,d\mu.
> $$
{: .theorem #thm-mct }

*Proof.* $$f$$ is $$\mathcal{S}$$-measurable. As $$\forall x \in X$$,
$$f_k(x) \le f(x)$$, we have $$\int f_k\,d\mu \le \int f\,d\mu$$ $$\forall k \in
\mathbb{Z}^+$$. Therefore, $$\lim_{k \to \infty} \int f_k\,d\mu \le \int f\,d\mu$$.

To prove the other direction, suppose $$A_1, \dots, A_m$$ are disjoint sets in
$$\mathcal{S}$$ and $$c_1, \dots, c_m \in [0, \infty)$$ are s.t. $$f(x) \ge
\sum_{j=1}^{m} c_j\chi_{A_j}(x)$$ $$\forall x \in X$$.

Let $$t \in (0, 1)$$. For $$k \in \mathbb{Z}^+$$, let
$$E_k = \{x \in X : f_k(x) \ge t\sum_{j=1}^{m} c_j\chi_{A_j}(x)\}$$. Then,
$$E_1 \subseteq E_2 \subseteq \cdots$$ is an increasing sequence of sets in
$$\mathcal{S}$$ whose union equals $$X$$. Thus,
$$\lim_{k \to \infty} \mu(A_j \cap E_k) = \mu(A_j)$$ for each
$$j \in \{1, \dots, m\}$$. By definition of $$E_k$$, if $$k \in \mathbb{Z}^+$$,
$$f_k(x) \ge \sum_{j=1}^{m} t c_j\chi_{A_j \cap E_k}(x)$$ $$\forall x \in X$$.

$$\therefore\ \int f_k\,d\mu \ge t\sum_{j=1}^{m} c_j\mu(A_j \cap E_k)$$ (by the
previous theorem). Taking the limit as $$k \to \infty$$,

$$
\lim_{k \to \infty} \int f_k\,d\mu \ge t\sum_{j=1}^{m} c_j\mu(A_j).
$$

Take the limit as $$t \to 1^-$$: $$\lim_{k \to \infty} \int f_k\,d\mu \ge
\sum_{j=1}^{m} c_j\mu(A_j)$$. Take the supremum of the inequality above over
all $$\mathcal{S}$$-partitions $$A_1, \dots, A_m$$ of $$X$$ and all
$$c_1, \dots, c_m \in [0, \infty)$$ s.t. $$f(x) \ge \sum_{j=1}^{m}
c_j\chi_{A_j}(x)$$ $$\forall x \in X$$, we have
$$\lim_{k \to \infty} \int f_k\,d\mu \ge \int f\,d\mu$$, completing the proof.
$$\square$$

> **Lemma (Integral-type sums for simple functions).** Suppose
> $$(X, \mathcal{S}, \mu)$$ is a measure space. Suppose $$a_1, \dots, a_m,
> b_1, \dots, b_n \in [0, \infty]$$ and $$A_1, \dots, A_m, B_1, \dots, B_n \in
> \mathcal{S}$$ are s.t. $$\sum_{j=1}^{m} a_j\chi_{A_j} = \sum_{k=1}^{n}
> b_k\chi_{B_k}$$. Then $$\sum_{j=1}^{m} a_j\mu(A_j) = \sum_{k=1}^{n}
> b_k\mu(B_k)$$.
{: .theorem #lem-integral-type-sums }

*Proof.* Assume $$A_1 \cup \cdots \cup A_m = X$$. Suppose $$A_1$$ and $$A_2$$ are
not disjoint. Then, write $$a_1\chi_{A_1} + a_2\chi_{A_2} = a_1\chi_{A_1 \setminus
A_2} + a_2\chi_{A_2 \setminus A_1} + (a_1 + a_2)\chi_{A_1 \cap A_2}$$. Now,
$$\mu(A_1) = \mu(A_1 \setminus A_2) + \mu(A_1 \cap A_2)$$ and
$$\mu(A_2) = \mu(A_2 \setminus A_1) + \mu(A_1 \cap A_2)$$, so
$$a_1\mu(A_1) + a_2\mu(A_2) = a_1\mu(A_1 \setminus A_2) + a_2\mu(A_2 \setminus A_1)
+ (a_1 + a_2)\mu(A_1 \cap A_2)$$. Thus, if we replace the sets $$A_1, A_2$$ with
$$A_1 \setminus A_2$$, $$A_1 \cap A_2$$, $$A_2 \setminus A_1$$, we still have the
unchanged value of the sum $$\sum_{j=1}^{m} a_j\mu(A_j)$$, only with the sets
disjoint!

In other words, we can convert the list $$A_1, \dots, A_m$$ into a disjoint list
of subsets without changing the value of $$\sum_{j=1}^{m} a_j\chi_{A_j}$$. Also,
it works for the coefficients $$a_1, \dots, a_m$$. Converting it into the
standard one: such some procedure can be used with the standard representation
$$\sum_{k=1}^{n} b_k\chi_{B_k}$$, converting it to the standard representation.
Thus, we see that by $$\sum_{j=1}^{m} a_j\chi_{A_j} = \sum_{k=1}^{n}
b_k\chi_{B_k}$$, implying the equality $$\sum_{j=1}^{m} a_j\mu(A_j) =
\sum_{k=1}^{n} b_k\mu(B_k)$$. $$\square$$

> **Theorem (Integral of a linear combination of characteristic functions).**
> Suppose $$(X, \mathcal{S}, \mu)$$ is a measure space, $$E_1, \dots, E_n \in
> \mathcal{S}$$, and $$c_1, \dots, c_n \in [0, \infty]$$. Then
>
> $$
> \int \Bigl( \sum_{k=1}^{n} c_k\chi_{E_k} \Bigr) d\mu = \sum_{k=1}^{n}
> c_k\mu(E_k).
> $$
{: .theorem #thm-integral-linear-combination }

*Note:* $$E_1, \dots, E_n$$ are not required to be disjoint.

*Proof.* Direct result from the lemma above and the integral of a
characteristic function (beforehand). $$\square$$

> **Theorem (Additivity of integration).** Suppose $$(X, \mathcal{S}, \mu)$$ is
> a measure space and $$f, g : X \to [0, \infty]$$ are $$\mathcal{S}$$-measurable
> functions. Then
>
> $$
> \int (f + g)\,d\mu = \int f\,d\mu + \int g\,d\mu.
> $$
{: .theorem #thm-additivity-integration }

*Proof.* Let $$f_1, f_2, \dots$$ and $$g_1, g_2, \dots$$ be increasing sequences
of $$\mathcal{S}$$-measurable simple functions with $$f_k \to f$$ and
$$g_k \to g$$ pointwise (approximation by simple functions). Then
$$f_1 + g_1, f_2 + g_2, \dots$$ is an increasing sequence of simple functions
converging to $$f + g$$, and by the Monotone Convergence Theorem and the
integral of a linear combination of characteristic functions,

$$
\int (f + g)\,d\mu = \lim_{k \to \infty} \int (f_k + g_k)\,d\mu = \lim_{k \to
\infty} \int f_k\,d\mu + \lim_{k \to \infty} \int g_k\,d\mu = \int f\,d\mu +
\int g\,d\mu. \qquad\square
$$

We know that the lower Riemann integral is not additive. For example, if
$$f = \chi_{[0,1] \cap \mathbb{Q}}$$ and $$g = \chi_{[0,1] \setminus \mathbb{Q}}$$,
then $$L(f, [0, 1]) = 0$$ and $$L(g, [0, 1]) = 0$$ but $$L(f + g, [0, 1]) = 1$$.
However, setting $$\lambda$$ as a Lebesgue measure on the Borel subsets of
$$[0, 1]$$, $$\int f\,d\lambda = 0$$ and $$\int g\,d\lambda = 1$$, and thus
$$\int (f + g)\,d\lambda = 1$$. We have just seen that the integral with respect
to a measure has considerably nicer behavior than the lower Riemann integral,
called "additivity".

> **Definition ($$f^+$$ and $$f^-$$).** Suppose $$f : X \to [-\infty, \infty]$$ is
> a function. Define functions $$f^+, f^- : X \to [0, \infty]$$ by
>
> $$
> f^+(x) = \begin{cases} f(x) & \text{if } f(x) \ge 0 \\ 0 & \text{if } f(x) <
> 0 \end{cases}
> \qquad
> f^-(x) = \begin{cases} 0 & \text{if } f(x) \ge 0 \\ -f(x) & \text{if } f(x) <
> 0. \end{cases}
> $$
{: .definition #def-f-plus-minus }

*Note:* $$f(x) = f^+(x) - f^-(x)$$ and $$\lvert f(x)\rvert = f^+(x) + f^-(x)$$.

> **Definition (Integral of a real-valued function).** Suppose
> $$(X, \mathcal{S}, \mu)$$ is a measure space and $$f : X \to [-\infty, \infty]$$
> is an $$\mathcal{S}$$-measurable function such that at least one of
> $$\int f^+\,d\mu$$ and $$\int f^-\,d\mu$$ is finite. The *integral* of $$f$$
> with respect to $$\mu$$, denoted $$\int f\,d\mu$$, is defined by
>
> $$
> \int f\,d\mu = \int f^+\,d\mu - \int f^-\,d\mu.
> $$
{: .definition #def-integral-real }

*Note:* The condition $$\int \lvert f\rvert\,d\mu < \infty$$ is equivalent to
$$\int f^+\,d\mu < \infty$$ and $$\int f^-\,d\mu < \infty$$.

**Example.** Suppose $$\lambda$$ is a Lebesgue measure on $$\mathbb{R}$$ and
$$f : \mathbb{R} \to \mathbb{R}$$ is the function defined by

$$
f(x) = \begin{cases} 1 & \text{if } x \ge 0 \\ -1 & \text{if } x < 0. \end{cases}
$$

Then $$\int f\,d\lambda$$ is not defined because $$\int f^+\,d\lambda = \infty$$
and $$\int f^-\,d\lambda = \infty$$.

> **Theorem (Integration is homogeneous).** Suppose $$(X, \mathcal{S}, \mu)$$ is
> a measure space and $$f : X \to [-\infty, \infty]$$ is a function such that
> $$\int f\,d\mu$$ is defined. If $$c \in \mathbb{R}$$, then
> $$\int cf\,d\mu = c\int f\,d\mu$$.
{: .theorem #thm-homogeneous }

*Proof.* First consider the case where $$f$$ is a nonnegative function and
$$c \ge 0$$. If $$P$$ is an $$\mathcal{S}$$-partition of $$X$$, then clearly
$$\mathcal{L}(cf, P) = c\mathcal{L}(f, P)$$. $$\therefore\ \int cf\,d\mu =
c\int f\,d\mu$$.

Now consider the general case where $$f$$ takes values in $$[-\infty, \infty]$$.
Suppose $$c \ge 0$$. Then,

$$
\int cf\,d\mu = \int (cf)^+\,d\mu - \int (cf)^-\,d\mu = \int cf^+\,d\mu - \int
cf^-\,d\mu = c\Bigl( \int f^+\,d\mu - \int f^-\,d\mu \Bigr) = c\int f\,d\mu.
$$

Now, suppose $$c < 0$$. Then $$-c > 0$$ and

$$
\int cf\,d\mu = \int (cf)^+\,d\mu - \int (cf)^-\,d\mu = \int (-c)f^-\,d\mu -
\int (-c)f^+\,d\mu = (-c)\Bigl( \int f^-\,d\mu - \int f^+\,d\mu \Bigr) =
c\int f\,d\mu. \qquad\square
$$

> **Theorem (Additivity of integration).** Suppose $$(X, \mathcal{S}, \mu)$$ is
> a measure space and $$f, g : X \to \mathbb{R}$$ are $$\mathcal{S}$$-measurable
> functions such that $$\int \lvert f\rvert\,d\mu < \infty$$ and
> $$\int \lvert g\rvert\,d\mu < \infty$$. Then
> $$\int (f + g)\,d\mu = \int f\,d\mu + \int g\,d\mu$$.
{: .theorem #thm-additivity-real }

*Proof.* $$(f + g)^+ - (f + g)^- = f + g = (f^+ - f^-) + (g^+ - g^-)$$.
$$\therefore\ (f + g)^+ + f^- + g^- = (f + g)^- + f^+ + g^+$$. Both sides are sums
of nonnegative functions, and hence integrating w.r.t. $$\mu$$ gives

$$
\int (f + g)^+\,d\mu + \int f^-\,d\mu + \int g^-\,d\mu = \int (f + g)^-\,d\mu +
\int f^+\,d\mu + \int g^+\,d\mu.
$$

$$\therefore\ \int (f + g)^+\,d\mu - \int (f + g)^-\,d\mu = \int f^+\,d\mu -
\int f^-\,d\mu + \int g^+\,d\mu - \int g^-\,d\mu$$, since all integrals are finite
($$(f + g)^+ \le f^+ + g^+ < \infty$$ and $$(f + g)^- \le f^- + g^- < \infty$$).
This can now be rewritten to our desired equation. $$\square$$

> **Theorem (Integration is order-preserving).** Suppose
> $$(X, \mathcal{S}, \mu)$$ is a measure space and $$f, g : X \to \mathbb{R}$$
> are $$\mathcal{S}$$-measurable functions such that $$\int f\,d\mu$$ and
> $$\int g\,d\mu$$ are defined. Suppose that $$f(x) \le g(x)$$ $$\forall x \in X$$.
> Then $$\int f\,d\mu \le \int g\,d\mu$$.
{: .theorem #thm-order-real }

*Proof.* The cases where $$\int f\,d\mu = \pm\infty$$ or $$\int g\,d\mu = \pm\infty$$
are trivial. Thus we assume that $$\int \lvert f\rvert\,d\mu < \infty$$ and
$$\int \lvert g\rvert\,d\mu < \infty$$. Then,
$$\int g\,d\mu - \int f\,d\mu = \int (g - f)\,d\mu$$ from the additivity and
homogeneity of Lebesgue integration. Here, as $$g(x) - f(x) \ge 0$$ $$\forall x
\in X$$, $$\int (g - f)\,d\mu \ge 0$$ and thus $$\int g\,d\mu \ge \int f\,d\mu$$.
$$\square$$

> **Theorem (Absolute value of integral $$\le$$ integral of absolute value).**
> Suppose $$(X, \mathcal{S}, \mu)$$ is a measure space and $$f : X \to
> [-\infty, \infty]$$ is an $$\mathcal{S}$$-measurable function such that
> $$\int f\,d\mu$$ is defined. Then $$\lvert \int f\,d\mu\rvert \le \int \lvert
> f\rvert\,d\mu$$.
{: .theorem #thm-absolute-value }

*Proof.* Because $$\int f\,d\mu$$ is defined, $$f$$ is an $$\mathcal{S}$$-measurable
function and at least one of $$\int f^+\,d\mu$$ and $$\int f^-\,d\mu$$ is finite.
Therefore,

$$
\Bigl\lvert \int f\,d\mu \Bigr\rvert = \Bigl\lvert \int f^+\,d\mu - \int f^-\,d\mu
\Bigr\rvert \le \int f^+\,d\mu + \int f^-\,d\mu = \int \lvert f\rvert\,d\mu.
\qquad\square
$$

## Exercises

> **Exercise 1.** Suppose $$(X, \mathcal{S}, \mu)$$ is a measure space and
> $$f : X \to [0, \infty]$$ is an $$\mathcal{S}$$-measurable function such that
> $$\int f\,d\mu < \infty$$. Explain why $$\inf_E f = 0$$ for each set
> $$E \in \mathcal{S}$$ with $$\mu(E) = \infty$$.
{: .problem #ex-3a-1 }

*Solution.* Consider a set $$E \in \mathcal{S}$$ with $$\mu(E) = \infty$$.
Suppose $$\inf_E f > 0$$.

1) If $$\inf_E f = \infty$$, let $$P = \{E, X \setminus E\}$$. Then

$$
\mathcal{L}(f, P) = \mu(E)\inf_E f + \mu(X \setminus E)\inf_{X \setminus E} f \ge
\mu(E)\inf_E f = \infty \times \infty = \infty.
$$

$$\therefore\ \int f\,d\mu = \infty$$, which is contradictory.

2) If $$\inf_E f = t$$ with $$t \in \mathbb{R}$$ and $$t > 0$$, let
$$P = \{E, X \setminus E\}$$. Then

$$
\mathcal{L}(f, P) = \mu(E)\inf_E f + \mu(X \setminus E)\inf_{X \setminus E} f \ge
\mu(E)\inf_E f = \infty \times t = \infty.
$$

$$\therefore\ \int f\,d\mu = \infty$$, which is contradictory.

$$\therefore\ \inf_E f = 0$$.

> **Exercise 2.** Suppose $$X$$ is a set, $$\mathcal{S}$$ is a $$\sigma$$-algebra on
> $$X$$, and $$c \in X$$. Define the Dirac measure $$\delta_c$$ on
> $$(X, \mathcal{S})$$ by $$\delta_c(E) = 1$$ if $$c \in E$$ and $$0$$ if
> $$c \notin E$$. Prove that if $$f : X \to [0, \infty]$$ is
> $$\mathcal{S}$$-measurable, then $$\int f\,d\delta_c = f(c)$$. [Careful:
> $$\{c\}$$ may not be in $$\mathcal{S}$$.]
{: .problem #ex-3a-2 }

*Solution.* As $$c \in X$$, then clearly there is a set $$E \in \mathcal{S}$$ s.t.
$$c \in E$$ (for example, $$E = X$$). For every $$\mathcal{S}$$-partition $$P$$ of
$$X$$ into $$A_1, \dots, A_m$$ with $$A_1, \dots, A_m \in \mathcal{S}$$, thus,

$$
\mathcal{L}(f, P) = \sum_{i=1}^{m} \delta_c(A_i)\inf_{A_i} f = \sum_{c \in A_i}
\inf_{x \in A_i} f(x).
$$

As we only consider the set in the partition that contains $$c$$ (exactly one
set $$A_i \ni c$$, by disjointness), $$\mathcal{L}(f, P) = \inf_{A_i} f \le f(c)$$.
Also, taking the partition $$\{f^{-1}([f(c), \infty]),\ X \setminus
f^{-1}([f(c), \infty])\}$$ (in $$\mathcal{S}$$ since $$f$$ is
$$\mathcal{S}$$-measurable, and the first set contains $$c$$), we get
$$\mathcal{L}(f, P) = f(c)$$. Hence
$$\sup\bigl\{\inf_{x \in A_i} f(x) : c \in A_i\bigr\} = f(c)$$.

$$\therefore\ \int f\,d\delta_c = f(c)$$.

> **Exercise 3.** Suppose $$(X, \mathcal{S}, \mu)$$ is a measure space and
> $$f : X \to [0, \infty]$$ is an $$\mathcal{S}$$-measurable function. Prove that
> $$\int f\,d\mu > 0$$ if and only if $$\mu(\{x \in X : f(x) > 0\}) > 0$$.
{: .problem #ex-3a-3 }

*Solution.* ① If $$\mu(\{x \in X : f(x) > 0\}) > 0$$, it is trivial that
$$\int f\,d\mu > 0$$. (Since $$\{f > 0\} = \bigcup_n \{f > \frac{1}{n}\}$$, some
$$A = \{f > \frac{1}{n}\}$$ has $$\mu(A) > 0$$, and the partition $$\{A, X
\setminus A\}$$ gives $$\int f\,d\mu \ge \frac{1}{n}\mu(A) > 0$$.)

② If $$\int f\,d\mu > 0$$, then there exists a partition $$A_1, \dots, A_m$$ with
positive lower Lebesgue sum: $$\sum_{i=1}^{m} \mu(A_i)\inf_{x \in A_i} f(x) > 0$$.

$$\therefore\ \exists$$ some $$i \in \{1, \dots, m\}$$ s.t. $$\mu(A_i) > 0$$ and
$$\inf_{x \in A_i} f(x) > 0$$.

$$\therefore\ \mu(\{x \in X : f(x) > 0\}) \ge \mu(A_i) > 0$$.

> **Exercise 4.** Give an example of a Borel measurable function
> $$f : [0, 1] \to (0, \infty)$$ such that $$L(f, [0, 1]) = 0$$.
{: .problem #ex-3a-4 }

*Solution.*

$$
f(x) = \begin{cases} \dfrac{1}{n} & \text{if } x = \dfrac{m}{n} \in \mathbb{Q}\ (\text{in
lowest terms}, n \ge 1), \\[0.5em] 1 & \text{otherwise.} \end{cases}
$$

Then $$f > 0$$, $$f$$ is Borel measurable (it is $$1$$ except on the countable
set $$\mathbb{Q} \cap [0, 1]$$), and every subinterval of $$[0, 1]$$ contains
rationals with arbitrarily large denominators, so the infimum of $$f$$ on every
subinterval is $$0$$. Hence every lower Riemann sum is $$0$$ and
$$L(f, [0, 1]) = 0$$.

> **Exercise 7.** Suppose $$X$$ is a set, $$\mathcal{S}$$ is the $$\sigma$$-algebra
> of all subsets of $$X$$, and $$w : X \to [0, \infty]$$ is a function. Define a
> measure $$\mu$$ on $$(X, \mathcal{S})$$ by $$\mu(E) = \sum_{x \in E} w(x)$$ for
> $$E \subseteq X$$. Prove that if $$f : X \to [0, \infty]$$ is a function, then
> $$\int f\,d\mu = \sum_{x \in X} w(x)f(x)$$, where the infinite sums above are
> defined as the supremum of all sums over finite subsets of $$E$$ (first sum) or
> $$X$$ (second sum).
{: .problem #ex-3a-7 }

*Solution.* For every $$\mathcal{S}$$-partition $$P$$ of $$X$$ into
$$A_1, \dots, A_m$$, we have

$$
\mathcal{L}(f, P) = \sum_{i=1}^{m} \mu(A_i)\inf_{x \in A_i} f(x) \le \sum_{i=1}^{m}
\sum_{x \in A_i} w(x)f(x) = \sum_{x \in X} w(x)f(x).
$$

Now, since $$\sum_{x \in X} f(x)w(x) = \sup_{A \subseteq X,\ \lvert A\rvert < \infty}
\sum_{x \in A} f(x)w(x)$$, $$\sum_{x \in A} f(x)w(x)$$ can be arbitrarily close to
the infinite sum. Every such $$A$$ can be converted to the partition $$P$$ with
$$\{x_1\}, \{x_2\}, \dots, \{x_m\}$$ (as $$A$$ is finite) where $$A = \{x_1,
\dots, x_m\}$$ (together with the remaining set $$X \setminus A$$):

$$
\sum_{x \in A} f(x)w(x) \le \sum_{i=1}^{m} f(x_i)w(x_i) \le \mathcal{L}(f, P).
$$

$$\therefore\ \sum_{x \in X} f(x)w(x) \le \int f\,d\mu$$.

$$\therefore\ \int f\,d\mu = \sum_{x \in X} w(x)f(x)$$.

> **Exercise 8.** Suppose $$\lambda$$ denotes Lebesgue measure on $$\mathbb{R}$$.
> Give an example of a sequence $$f_1, f_2, \dots$$ of simple Borel measurable
> functions from $$\mathbb{R}$$ to $$[0, \infty)$$ such that
> $$\lim_{k \to \infty} f_k(x) = 0$$ for every $$x \in \mathbb{R}$$ but
> $$\lim_{k \to \infty} \int f_k\,d\lambda = 1$$.
{: .problem #ex-3a-8 }

*Solution.* Consider an infinite sequence of disjoint sets
$$A_1, \dots \subseteq \mathbb{R}$$ with non-zero (finite) measure in
$$\mathbb{R}$$, for example $$A_n = [n, n+1)$$. Define

$$
f_n(x) = \frac{1}{\lambda(A_n)}\chi_{A_n}(x).
$$

Here, $$\int f_n\,d\lambda = 1$$ $$\forall n \in \mathbb{Z}^+$$, but if
$$x \in \mathbb{R}$$, $$x$$ is either not in any $$A_n$$ (so $$f_n(x) = 0$$
$$\forall n$$) or $$x$$ is in some $$A_i$$, meaning that $$f_n(x) = 0$$
$$\forall n > i$$.

$$\therefore\ \lim_{n \to \infty} f_n(x) = 0$$ $$\forall x \in \mathbb{R}$$.

> **Exercise 10.** Suppose $$(X, \mathcal{S}, \mu)$$ is a measure space and
> $$f_1, f_2, \dots$$ is a sequence of nonnegative $$\mathcal{S}$$-measurable
> functions. Define $$f : X \to [0, \infty]$$ by $$f(x) = \sum_{k=1}^{\infty}
> f_k(x)$$. Prove that $$\int f\,d\mu = \sum_{k=1}^{\infty} \int f_k\,d\mu$$.
{: .problem #ex-3a-10 }

*Solution.* Let $$g_1 = f_1$$, $$g_2 = f_1 + f_2, \dots, g_n = \sum_{k=1}^{n}
f_k$$. Apply the Monotone Convergence Theorem: $$g_n$$ is an increasing sequence
of nonnegative $$\mathcal{S}$$-measurable functions converging to $$f$$, so
$$\int f\,d\mu = \lim_n \int g_n\,d\mu = \lim_n \sum_{k=1}^{n} \int f_k\,d\mu =
\sum_{k=1}^{\infty} \int f_k\,d\mu$$ (using additivity of integration).

> **Exercise 11.** Suppose $$(X, \mathcal{S}, \mu)$$ is a measure space and
> $$f_1, f_2, \dots$$ are $$\mathcal{S}$$-measurable functions from $$X$$ to
> $$\mathbb{R}$$ such that $$\sum_{k=1}^{\infty} \int \lvert f_k\rvert\,d\mu <
> \infty$$. Prove that there exists $$E \in \mathcal{S}$$ such that
> $$\mu(X \setminus E) = 0$$ and $$\lim_{k \to \infty} f_k(x) = 0$$ for every
> $$x \in E$$.
{: .problem #ex-3a-11 }

*Solution.* WLOG, assume $$f_k$$'s are nonnegative functions (replace $$f_k$$ by
$$\lvert f_k\rvert$$). Let $$f = \sum_{k=1}^{\infty} f_k$$. Now we have (by
Exercise 10) $$\int f\,d\mu = \sum_k \int f_k\,d\mu < \infty$$. Here, denote
$$E = \{x \in X : f(x) < \infty\}$$, which is in $$\mathcal{S}$$.

Then, since $$\int f\,d\mu < \infty$$, considering the partition $$P$$ of $$X$$
into $$E$$ and $$X \setminus E$$,
$$\mu(E)\inf_E f + \mu(X \setminus E)\inf_{X \setminus E} f < \infty$$.

Here, by the construction of $$E$$, $$\inf_{X \setminus E} f = \infty$$ and thus
$$\mu(X \setminus E) = 0$$.

And $$\forall x \in E$$, $$\sum_k f_k(x) < \infty$$, meaning
$$\lim_{k \to \infty} f_k(x) = 0$$.

> **Exercise 12.** Show that there exists a Borel measurable function
> $$f : \mathbb{R} \to (0, \infty)$$ such that $$\int \chi_I f\,d\lambda = \infty$$
> for every nonempty open interval $$I \subseteq \mathbb{R}$$, where $$\lambda$$
> denotes Lebesgue measure on $$\mathbb{R}$$.
{: .problem #ex-3a-12 }

*Solution.* Consider the function
$$g(x) = \sum_{q_n \in \mathbb{Q}} \dfrac{1}{4^n\lvert x - q_n\rvert}$$, where
$$q_1, q_2, \dots$$ is some enumeration of the rationals (the function of 2E,
Exercise 14).

Take $$A(\beta) = \bigcup_{q_n \in \mathbb{Q}} [q_n - \beta^n, q_n + \beta^n]$$
for some $$\beta \in (\frac{1}{4}, 1)$$. Then, $$\forall x \notin A(\beta)$$,
$$g(x) \le \sum_n \dfrac{1}{(4\beta)^n} < \infty$$.

Let $$A_N = \bigcup_{n \ge N} [q_n - \beta^n, q_n + \beta^n]$$. Then
$$\lvert A_N\rvert \le \sum_{n \ge N} 2\beta^n \to 0$$ and, as above,
$$g(x) < \infty$$ for $$x \notin \mathbb{Q}$$ and $$x \notin A_N$$ for some $$N$$
(the terms with $$n < N$$ are finite for $$x \notin \mathbb{Q}$$, and the tail is
bounded by $$\sum_{n \ge N} (4\beta)^{-n}$$). So $$Z = \{g = \infty\} \subseteq
\mathbb{Q} \cup \bigcap_N A_N$$ and $$\lvert Z\rvert = 0$$.

Define $$f = g$$ on $$\mathbb{R} \setminus Z$$ and $$f = 1$$ on $$Z$$. Then
$$f : \mathbb{R} \to (0, \infty)$$ is Borel measurable. For a nonempty open
interval $$I$$, pick $$q_n \in I$$. As $$f = g \ge \dfrac{1}{4^n\lvert x -
q_n\rvert}$$ off the null set $$Z$$ (and the integral of $$\dfrac{1}{\lvert x -
q_n\rvert}$$ over a neighborhood of $$q_n$$ is $$\infty$$),
$$\int \chi_I f\,d\lambda = \infty$$.

> **Exercise 16.** Suppose $$\mathcal{S}$$ and $$\mathcal{T}$$ are
> $$\sigma$$-algebras on a set $$X$$ and $$\mathcal{S} \subseteq \mathcal{T}$$.
> Suppose $$\mu_1$$ is a measure on $$(X, \mathcal{S})$$, $$\mu_2$$ is a measure
> on $$(X, \mathcal{T})$$, and $$\mu_1(E) = \mu_2(E)$$ for all
> $$E \in \mathcal{S}$$. Prove that if $$f : X \to [0, \infty]$$ is
> $$\mathcal{S}$$-measurable, then $$\int f\,d\mu_1 = \int f\,d\mu_2$$.
{: .problem #ex-3a-16 }

*Solution.* Consider any $$\mathcal{T}$$-partition $$P$$ of $$X$$ into
$$A_1, \dots, A_m$$. Let $$c_i = \inf_{x \in A_i} f(x)$$, then assume
$$c_1 < c_2 < \cdots < c_m \le c_{m+1} = \infty$$ WLOG. Then

$$
\mathcal{L}(f, P) = \sum_{i=1}^{m} c_i\mu_2(A_i) = \sum_{i=1}^{m}\sum_{j=i}^{m}
c_i\mu_2\bigl(A_i \cap f^{-1}([c_j, c_{j+1}))\bigr)
\le \sum_{i=1}^{m}\sum_{j=i}^{m} c_j\mu_2\bigl(A_i \cap f^{-1}([c_j,
c_{j+1}))\bigr)
$$

$$
= \sum_{j=1}^{m} c_j\sum_{i=1}^{j} \mu_2\bigl(A_i \cap f^{-1}([c_j, c_{j+1}))\bigr)
= \sum_{j=1}^{m} c_j\mu_2\bigl(f^{-1}([c_j, c_{j+1}))\bigr) = \mathcal{L}(f, P'),
$$

where $$P'$$ is the $$\mathcal{S}$$-partition of $$X$$ into
$$f^{-1}([c_j, c_{j+1}))$$ for $$j = 1, \dots, m$$ (and $$f^{-1}([0, c_1))$$,
which contributes $$0$$ to the sum), and the last sum is
$$\sum_j c_j\mu_1\bigl(f^{-1}([c_j, c_{j+1}))\bigr)$$ because these sets are in
$$\mathcal{S}$$. Since $$\inf_{f^{-1}([c_j, c_{j+1}))} f \ge c_j$$, this sum is at
most $$\mathcal{L}(f, P'')$$ with respect to $$\mu_1$$ for the $$\mathcal{S}$$-partition
$$P''$$, hence at most $$\int f\,d\mu_1$$.

Clearly, any $$\mathcal{T}$$-partition has a lower Lebesgue sum at most that of
some $$\mathcal{S}$$-partition. Thus $$\int f\,d\mu_2 \le \int f\,d\mu_1$$. Since
any $$\mathcal{S}$$-partition is also a $$\mathcal{T}$$-partition and
$$\mu_1 = \mu_2$$ on $$\mathcal{S}$$, $$\int f\,d\mu_1 \le \int f\,d\mu_2$$.
Therefore $$\int f\,d\mu_1 = \int f\,d\mu_2$$.

> **Exercise 17.** Suppose that $$(X, \mathcal{S}, \mu)$$ is a measure space and
> $$f_1, f_2, \dots$$ is a sequence of nonnegative $$\mathcal{S}$$-measurable
> functions on $$X$$. Define a function $$f : X \to [0, \infty]$$ by
> $$f(x) = \liminf_{k \to \infty} f_k(x)$$.
>
> (a) Show that $$f$$ is an $$\mathcal{S}$$-measurable function.
>
> (b) Prove that $$\int f\,d\mu \le \liminf_{k \to \infty} \int f_k\,d\mu$$.
>
> [The result in (b) is called Fatou's Lemma.]
{: .problem #ex-3a-17 }

*Solution.* (a) $$f(x) = \lim_{m \to \infty}\inf_{k \ge m} f_k(x)$$ is
$$\mathcal{S}$$-measurable as $$f_1, f_2, \dots$$ is a sequence of
$$\mathcal{S}$$-measurable functions on $$X$$ (infima and increasing limits of
measurable functions are measurable).

(b) Say that $$g_n(x) = \inf_{k \ge n} f_k(x)$$. Then $$g_n(x)$$ is increasing,
so by the Monotone Convergence Theorem $$\int f\,d\mu = \lim_{n \to \infty}
\int g_n\,d\mu$$.

Now, we know that $$\forall k \ge n$$, $$g_n \le f_k$$, hence
$$\int g_n\,d\mu \le \int f_k\,d\mu$$, that is,
$$\int g_n\,d\mu \le \inf_{k \ge n} \int f_k\,d\mu$$, and therefore
$$\lim_{n \to \infty} \int g_n\,d\mu \le \liminf_{n \to \infty} \int f_n\,d\mu$$.
$$\square$$ — Fatou's Lemma.

> **Exercise 18.** Give an example of a sequence $$x_1, x_2, \dots$$ of real
> numbers such that $$\lim_{n \to \infty} \sum_{k=1}^{n} x_k$$ exists in
> $$\mathbb{R}$$, but $$\int x\,d\mu$$ is not defined, where $$\mu$$ is counting
> measure on $$\mathbb{Z}^+$$ and $$x$$ is the function from $$\mathbb{Z}^+$$ to
> $$\mathbb{R}$$ defined by $$x(k) = x_k$$.
{: .problem #ex-3a-18 }

*Solution.* Any conditionally convergent series (by Riemann's rearrangement
theorem) works; for example $$x_k = \dfrac{(-1)^{k}}{k}$$. The series
$$\sum_k x_k$$ converges, but $$\int x^+\,d\mu = \sum_{j} \dfrac{1}{2j} = \infty$$
and $$\int x^-\,d\mu = \sum_{j} \dfrac{1}{2j - 1} = \infty$$ (integration with
respect to counting measure is summation), so $$\int x\,d\mu$$ is not defined.

> **Exercise 20.** Suppose $$(X, \mathcal{S}, \mu)$$ is a measure space and
> $$f_1, f_2, \dots$$ is a monotone (meaning either increasing or decreasing)
> sequence of $$\mathcal{S}$$-measurable functions. Define
> $$f : X \to [-\infty, \infty]$$ by $$f(x) = \lim_{k \to \infty} f_k(x)$$.
> Prove that if $$\int \lvert f_1\rvert\,d\mu < \infty$$, then
> $$\lim_{k \to \infty} \int f_k\,d\mu = \int f\,d\mu$$.
{: .problem #ex-3a-20 }

*Solution.* Define $$f_k^+(x) = \max(f_k(x), 0)$$ and
$$f_k^-(x) = \max(-f_k(x), 0)$$. Then $$f_k = f_k^+ - f_k^-$$ and each $$f_k^+$$
and $$f_k^-$$ are monotone. Also, there exists $$f^+(x) = \lim_{k \to \infty}
f_k^+(x)$$ and $$f^-(x) = \lim_{k \to \infty} f_k^-(x)$$. Trivially,
$$f = f^+ - f^-$$.

We have $$\infty > \int \lvert f_1\rvert\,d\mu = \int (f_1^+ + f_1^-)\,d\mu$$.

Now, if $$f_k$$ increases, it is the monotone convergence theorem (applied to
$$f_k - f_1 \ge 0$$, with $$\int f_1\,d\mu$$ finite), and if $$f_k$$ decreases,
consider $$g_k = f_1 - f_k$$ which increases (and is nonnegative).

$$\therefore\ \int (f_1 - f)\,d\mu = \int f_1\,d\mu - \lim_{k \to \infty}
\int f_k\,d\mu$$.

$$\therefore\ \int f\,d\mu = \lim_{k \to \infty} \int f_k\,d\mu$$
($$\because \int \lvert f_1\rvert\,d\mu < \infty$$).

## References

- Sheldon Axler, *Measure, Integration & Real Analysis* — Section 3A and
  Exercises 3A. The exercise statements are quoted from the book.
- The notes and the exercise answers are mine, typeset from my handwritten
  notebook. The structure of each answer is unchanged; small slips in the
  answers are corrected, and answers that stopped short are completed along
  the same lines. I did not attempt Exercises 5, 6, 9, 13 to 15, 17(c) and 19,
  so they are not here.
