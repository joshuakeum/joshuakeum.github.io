---
title: "Measure Theory and Real Analysis: 2C Measures and Their Properties"
date: 2026-11-14 13:50:00 +0900
categories: [Study Notes, Measure Theory and Real Analysis]
tags: [measure, counting measure, dirac measure, measure space, subadditivity, continuity of measure, exercises]
description: The definition and examples of measures, measure spaces, monotonicity, countable subadditivity, the measure of increasing unions and decreasing intersections and of a union, with worked exercises 1 to 8, 10 and 12. Section 2C of Axler's Measure, Integration & Real Analysis.
math: true
mermaid: false
render_with_liquid: false
---

> Typeset from my handwritten notes for section 2C of Axler's *Measure,
> Integration & Real Analysis*. The exercise statements are the textbook's;
> the answers are mine, as I wrote them. Part of the
> [course overview](/posts/measure-theory-overview/).
{: .prompt-info }

## Notes

> **Definition (Measure).** Suppose $$X$$ is a set and $$\mathcal{S}$$ is a
> $$\sigma$$-algebra on $$X$$. A *measure* on $$(X, \mathcal{S})$$ is a
> function $$\mu : \mathcal{S} \to [0, \infty]$$ such that $$\mu(\emptyset) = 0$$
> and
>
> $$
> \mu\Bigl( \bigcup_{k=1}^{\infty} E_k \Bigr) = \sum_{k=1}^{\infty} \mu(E_k)
> $$
>
> for every disjoint sequence $$E_1, E_2, \dots$$ of sets in $$\mathcal{S}$$
> ($$=$$ countable additivity).
{: .definition #def-measure }

**Example.** If $$X$$ is a set, then the *counting measure* is the measure
$$\mu$$ defined on the $$\sigma$$-algebra of all subsets of $$X$$ by setting
$$\mu(E) = n(E)$$, where $$n(E)$$ is the number of elements of $$E$$.

\* If $$E$$ is not finite, $$n(E) = \infty$$.

**Example.** Suppose $$X$$ is a set, $$\mathcal{S}$$ is a $$\sigma$$-algebra on
$$X$$ and $$c \in X$$. The *Dirac measure* $$\delta_c$$ on
$$(X, \mathcal{S})$$ is defined as follows:

$$
\delta_c(E) =
\begin{cases}
1 & \text{if } c \in E, \\
0 & \text{if not.}
\end{cases}
$$

**Example.** Suppose $$X$$ is a set, $$\mathcal{S}$$ is a $$\sigma$$-algebra on
$$X$$, and $$w : X \to [0, \infty]$$ is a function. Define a measure $$\mu$$ on
$$(X, \mathcal{S})$$ by

$$
\mu(E) = \sum_{x \in E} w(x) \qquad \text{for } E \in \mathcal{S}.
$$

\* Note:
$$\displaystyle\sum_{x \in E} w(x) = \sup\Bigl\{ \sum_{x \in D} w(x) :
D \subseteq E \text{ and } D \text{ is finite} \Bigr\}$$.

**Example.** Suppose $$\mathcal{S}$$ is the $$\sigma$$-algebra on $$\mathbb{R}$$
consisting of all subsets of $$\mathbb{R}$$. Then the function
$$w(E) = \lvert E\rvert$$ for any $$E \subseteq \mathbb{R}$$ is not a measure,
since it is not finitely additive.

**Example.** However, supposing $$\mathcal{B}$$ is the $$\sigma$$-algebra on
$$\mathbb{R}$$ consisting of all Borel subsets of $$\mathbb{R}$$,
$$\mu(E) = \lvert E\rvert$$ is a measure on $$(\mathbb{R}, \mathcal{B})$$, as
we will show in 2D.

> **Definition (Measure space).** A *measure space* is an ordered triple
> $$(X, \mathcal{S}, \mu)$$ where $$X$$ is a set, $$\mathcal{S}$$ is a
> $$\sigma$$-algebra on $$X$$, and $$\mu$$ is a measure on
> $$(X, \mathcal{S})$$.
{: .definition #def-measure-space }

> **Theorem (Measure preserves order).** Suppose $$(X, \mathcal{S}, \mu)$$ is
> a measure space and $$D, E \in \mathcal{S}$$ are such that $$D \subseteq E$$.
> Then
>
> - **(a)** $$\mu(D) \le \mu(E)$$;
> - **(b)** $$\mu(E \setminus D) = \mu(E) - \mu(D)$$ provided that
>   $$\mu(D) < \infty$$.
{: .theorem #thm-measure-order }

*Proof.* (a) $$E = D \cup (E \setminus D)$$ with
$$D \cap (E \setminus D) = \emptyset$$.

$$\therefore$$ By countable additivity,
$$\mu(D) \le \mu(D) + \mu(E \setminus D) = \mu(E)$$.

(b) $$\mu(E \setminus D) = \mu(E) - \mu(D)$$ if $$\mu(D) < \infty$$, from the
equation above. $$\square$$

> **Theorem (Countable subadditivity).** Suppose $$(X, \mathcal{S}, \mu)$$ is
> a measure space and $$E_1, E_2, \dots \in \mathcal{S}$$. Then
>
> $$
> \mu\Bigl( \bigcup_{k} E_k \Bigr) \le \sum_{k} \mu(E_k).
> $$
{: .theorem #thm-countable-subadditivity }

*Proof.* Let $$D_1 = \emptyset$$, $$D_2 = E_1$$,
$$D_3 = \bigcup_{k=1}^{2} E_k$$, $$\dots$$,
$$D_n = \bigcup_{k=1}^{n-1} E_k$$, $$\dots$$ for $$k \ge 2$$.

Then $$C_k = E_k \setminus D_k$$ is a disjoint sequence of subsets where
$$\bigcup_k C_k = \bigcup_k E_k$$ and $$C_k \subseteq E_k$$. Thus
$$\mu(C_k) \le \mu(E_k)$$ for all $$k$$.

$$\therefore\ \mu\bigl( \bigcup_k E_k \bigr) = \mu\bigl( \bigcup_k C_k \bigr)
= \sum_k \mu(C_k) \le \sum_k \mu(E_k)$$. $$\square$$

> **Theorem (Measure of an increasing union).** Suppose
> $$(X, \mathcal{S}, \mu)$$ is a measure space and
> $$E_1 \subseteq E_2 \subseteq \cdots$$ is an increasing sequence of sets in
> $$\mathcal{S}$$. Then
>
> $$
> \mu\Bigl( \bigcup_{k} E_k \Bigr) = \lim_{k \to \infty} \mu(E_k).
> $$
{: .theorem #thm-increasing-union }

*Proof.* If $$\mu(E_k) = \infty$$ for some $$k$$, then $$\infty = \infty$$
holds. Thus we only consider when $$\mu(E_k) < \infty$$ for all
$$k \in \mathbb{Z}^+$$.

For convenience, define $$E_0 = \emptyset$$.

$$\therefore\ \bigcup_k E_k = \bigcup_j (E_j \setminus E_{j-1})$$ where
$$\{E_j \setminus E_{j-1}\}$$ is a sequence of disjoint sets.

$$
\begin{aligned}
\therefore\ \mu\Bigl( \bigcup_k E_k \Bigr)
&= \sum_k \mu(E_k \setminus E_{k-1})
 = \lim_{k \to \infty} \sum_{j=1}^{k} \mu(E_j \setminus E_{j-1}) \\
&= \lim_{k \to \infty} \sum_{j=1}^{k} \bigl\{ \mu(E_j) - \mu(E_{j-1}) \bigr\}
 = \lim_{k \to \infty} \mu(E_k). \qquad \square
\end{aligned}
$$

> **Theorem (Measure of a decreasing intersection).** Suppose
> $$(X, \mathcal{S}, \mu)$$ is a measure space and
> $$E_1 \supseteq E_2 \supseteq \cdots$$ is a decreasing sequence of sets in
> $$\mathcal{S}$$, with $$\mu(E_1) < \infty$$. Then
>
> $$
> \mu\Bigl( \bigcap_{k} E_k \Bigr) = \lim_{k \to \infty} \mu(E_k).
> $$
{: .theorem #thm-decreasing-intersection }

*Proof.* $$E_1 \setminus \bigcap_k E_k = \bigcup_k (E_1 \setminus E_k)$$ and
$$E_1 \setminus E_1 \subseteq E_1 \setminus E_2 \subseteq \cdots$$.

$$\therefore\ \mu\bigl( E_1 \setminus \bigcap_k E_k \bigr)
= \lim_{k \to \infty} \mu(E_1 \setminus E_k)$$.

$$\therefore\ \mu\bigl( \bigcap_k E_k \bigr) = \lim_{k \to \infty} \mu(E_k)$$
where $$\mu(E_1) < \infty$$. $$\square$$

> **Theorem (Measure of a union).** Suppose $$(X, \mathcal{S}, \mu)$$ is a
> measure space and $$D, E \in \mathcal{S}$$ with
> $$\mu(D \cap E) < \infty$$. Then
> $$\mu(D \cup E) = \mu(D) + \mu(E) - \mu(D \cap E)$$.
{: .theorem #thm-measure-union }

*Proof.* $$D \cup E = (D \setminus (D \cap E)) \cup (E \setminus (D \cap E))
\cup (D \cap E)$$.

$$
\begin{aligned}
\therefore\ \mu(D \cup E)
&= \mu(D \setminus (D \cap E)) + \mu(E \setminus (D \cap E))
   + \mu(D \cap E) \\
&= \mu(D) + \mu(E) - \mu(D \cap E) \quad \text{if } \mu(D \cap E) < \infty.
   \qquad \square
\end{aligned}
$$

## Exercises

> **Exercise 1.** Explain why there does not exist a measure space
> $$(X, \mathcal{S}, \mu)$$ with the property that
> $$\{\mu(E) : E \in \mathcal{S}\} = [0, 1)$$.
{: .problem #ex-2c-1 }

*Solution.* Suppose there exists a measure space $$(X, \mathcal{S}, \mu)$$ with
$$\{\mu(E) : E \in \mathcal{S}\} = [0, 1)$$.

Since $$\emptyset \in \mathcal{S}$$, $$X \in \mathcal{S}$$, and thus
$$0 \le \mu(X) < 1$$.

Let $$\mu(X) = c$$ with $$0 \le c < 1$$.

Then $$\forall E \in \mathcal{S}$$, $$E \subseteq X$$ and thus
$$\mu(E) \le \mu(X) = c$$.

But since $$\{\mu(E) : E \in \mathcal{S}\} = [0, 1)$$, there exists
$$p \in [0, 1)$$ with $$c < p < 1$$ attained as $$\mu(E) = p$$ for some
$$E \in \mathcal{S}$$, so $$\mu(E) = p > c = \mu(X)$$, which is a
contradiction.

$$\therefore$$ There does not exist any measure space such that
$$\{\mu(E) : E \in \mathcal{S}\} = [0, 1)$$.

Let $$2^{\mathbb{Z}^+}$$ denote the $$\sigma$$-algebra on $$\mathbb{Z}^+$$
consisting of all subsets of $$\mathbb{Z}^+$$.

> **Exercise 2.** Suppose $$\mu$$ is a measure on
> $$(\mathbb{Z}^+, 2^{\mathbb{Z}^+})$$. Prove that there is a sequence
> $$w_1, w_2, \dots$$ in $$[0, \infty]$$ such that
>
> $$
> \mu(E) = \sum_{k \in E} w_k
> $$
>
> for every set $$E \subseteq \mathbb{Z}^+$$.
{: .problem #ex-2c-2 }

*Solution.* Since $$E \subseteq \mathbb{Z}^+$$, every $$E$$ is countable.

Thus, setting $$w_k = \mu(\{k\})$$, $$\mu(E) = \sum_{k \in E} w_k$$.

Indeed, $$E = \bigcup_{k \in E} \{k\}$$ is a countable disjoint union of the
sets $$\{k\}$$ (all in $$2^{\mathbb{Z}^+}$$), so by countable additivity (and
$$\mu(\emptyset) = 0$$ for finite $$E$$, using the sequence of the $$\{k\}$$
followed by $$\emptyset, \emptyset, \dots$$)
$$\mu(E) = \sum_{k \in E} \mu(\{k\}) = \sum_{k \in E} w_k$$.

> **Exercise 3.** Give an example of a measure $$\mu$$ on
> $$(\mathbb{Z}^+, 2^{\mathbb{Z}^+})$$ such that
> $$\{\mu(E) : E \subseteq \mathbb{Z}^+\} = [0, 1]$$.
{: .problem #ex-2c-3 }

*Solution.* $$\mu(\{k\}) = \dfrac{1}{2^k}$$, that is,
$$\mu(E) = \sum_{k \in E} \dfrac{1}{2^k}$$ (a measure, by the weight example,
with $$w_k = 2^{-k}$$).

Then $$\mu(E) \in [0, 1]$$ since $$\mu(E) \le \mu(\mathbb{Z}^+) =
\sum_{k=1}^{\infty} 2^{-k} = 1$$. Conversely, every $$x \in [0, 1]$$ has a
binary expansion $$x = \sum_{k=1}^{\infty} \varepsilon_k 2^{-k}$$ with
$$\varepsilon_k \in \{0, 1\}$$, so $$x = \mu(E)$$ for
$$E = \{k : \varepsilon_k = 1\}$$.

> **Exercise 4.** Give an example of a measure space $$(X, \mathcal{S}, \mu)$$
> such that
>
> $$
> \{\mu(E) : E \in \mathcal{S}\} = \{\infty\} \cup \bigcup_{k=0}^{\infty}
> [3k, 3k + 1].
> $$
{: .problem #ex-2c-4 }

*Solution.* $$X = \mathbb{Z}^+$$, $$\mathcal{S} = 2^{\mathbb{Z}^+}$$,

$$
\mu(\{k\}) =
\begin{cases}
\dfrac{1}{2^t} & k = 2t, \\[0.5em]
3 & k = 2t + 1.
\end{cases}
$$

($$\mu$$ is the measure of the weight example.) For $$E \subseteq \mathbb{Z}^+$$,
let $$m$$ be the number of odd elements of $$E$$ and $$s$$ the sum of
$$2^{-t}$$ over its even elements $$2t$$. Then $$s \in [0, 1]$$ (the even
weights $$2^{-t}$$, $$t \ge 1$$, sum to $$1$$, and every value in $$[0, 1]$$ is a
subsum, as in Exercise 3), and $$\mu(E) = 3m + s$$, which is $$\infty$$ if
$$m = \infty$$ and lies in $$[3m, 3m + 1]$$ if $$m$$ is finite. Every value
$$3m + s$$ with $$m \in \{0, 1, 2, \dots\}$$ and $$s \in [0, 1]$$ occurs (take
$$m$$ odd numbers and a set of even numbers with sum $$s$$), and $$\infty$$
occurs with infinitely many odd numbers. Hence
$$\{\mu(E)\} = \{\infty\} \cup \bigcup_{k=0}^{\infty} [3k, 3k + 1]$$.

> **Exercise 5.** Suppose $$(X, \mathcal{S}, \mu)$$ is a measure space such
> that $$\mu(X) < \infty$$. Prove that if $$\mathcal{A}$$ is a set of disjoint
> sets in $$\mathcal{S}$$ such that $$\mu(A) > 0$$ for every
> $$A \in \mathcal{A}$$, then $$\mathcal{A}$$ is a countable set.
{: .problem #ex-2c-5 }

*Solution.* For every $$A \in \mathcal{A}$$, $$A \subseteq X$$ and thus

$$
0 < \sum_{A \in \mathcal{A}} \mu(A) = \mu\Bigl( \bigcup_{A \in \mathcal{A}} A
\Bigr) \le \mu(X) < \infty.
$$

(Here the sum over $$\mathcal{A}$$ is the supremum of the finite subsums, and
for a finite $$\mathcal{A}' \subseteq \mathcal{A}$$ the finite additivity gives
$$\sum_{A \in \mathcal{A}'} \mu(A) = \mu(\bigcup_{A \in \mathcal{A}'} A)
\le \mu(X)$$.)

$$\therefore$$ $$\mathcal{A}$$ is countable. Indeed, for $$n \in \mathbb{Z}^+$$
let $$\mathcal{A}_n = \{A \in \mathcal{A} : \mu(A) > \frac{1}{n}\}$$. If
$$\mathcal{A}_n$$ contained $$N$$ sets, then $$\frac{N}{n} <
\sum_{A \in \mathcal{A}_n}\mu(A) \le \mu(X)$$ for those finitely many sets, so
$$N < n\mu(X)$$, and $$\mathcal{A}_n$$ is finite. Since
$$\mathcal{A} = \bigcup_{n} \mathcal{A}_n$$, $$\mathcal{A}$$ is a countable
union of finite sets, hence countable.

> **Exercise 6.** Find all $$c \in [3, \infty)$$ such that there exists a
> measure space $$(X, \mathcal{S}, \mu)$$ with
>
> $$
> \{\mu(E) : E \in \mathcal{S}\} = [0, 1] \cup [3, c].
> $$
{: .problem #ex-2c-6 }

*Solution.* $$c = 4$$. (Symmetricity.)

Suppose such a measure space exists. The largest value in the range is $$c$$,
and since $$\mu$$ preserves order, $$\mu(X) = c$$. For every $$E \in
\mathcal{S}$$, $$\mu(X \setminus E) = c - \mu(E)$$ (all values are finite), so
the range is symmetric: $$x$$ is in the range if and only if $$c - x$$ is.
Mapping $$x \mapsto c - x$$ takes the range $$[0, 1] \cup [3, c]$$ to
$$[c - 1, c] \cup [0, c - 3]$$, and this must equal $$[0, 1] \cup [3, c]$$.
Comparing the lower interval, $$c - 3 = 1$$, so $$c = 4$$ (and then
$$c - 1 = 3$$ matches).

Conversely, $$c = 4$$ occurs: let $$X = \{0\} \cup \mathbb{Z}^+$$,
$$\mathcal{S} = 2^X$$, $$\mu(\{0\}) = 3$$ and $$\mu(\{k\}) = 2^{-k}$$ for
$$k \in \mathbb{Z}^+$$. Then $$\mu(E) \in [0, 1]$$ if $$0 \notin E$$ (every value
occurs, by Exercise 3) and $$\mu(E) \in [3, 4]$$ if $$0 \in E$$, so the range is
$$[0, 1] \cup [3, 4]$$.

> **Exercise 7.** Give an example of a measure space $$(X, \mathcal{S}, \mu)$$
> such that
>
> $$
> \{\mu(E) : E \in \mathcal{S}\} = [0, 1] \cup [3, \infty].
> $$
{: .problem #ex-2c-7 }

*Solution.* Let $$q_1, q_2, \dots$$ be the enumeration of $$\mathbb{Q}$$. Let
$$X = [0, 1] \cup \mathbb{Q}$$ and $$\mathcal{S}$$ the Borel subsets of $$X$$,

$$
\mu(A) = \lvert A \setminus \mathbb{Q}\rvert + \sum_{q_i \in A} (i + 2).
$$

($$\mu$$ is a measure: the first term is outer measure on Borel sets, a measure
by 2D, and the second term is the measure of the weight example with weights
$$w(q_i) = i + 2$$; a sum of two measures is a measure.) Here
$$A \setminus \mathbb{Q} \subseteq [0, 1]$$, so the first term takes every value
in $$[0, 1]$$. The second term takes the values of all subsums of
$$3, 4, 5, \dots$$: every integer $$n \ge 3$$ and $$0$$ (for finite $$A$$), and
$$\infty$$ (for infinite $$A \cap \mathbb{Q}$$). Since the two terms can be
chosen independently, the range is
$$[0, 1] \cup \bigcup_{n=3}^{\infty} [n, n + 1] \cup \{\infty\}
= [0, 1] \cup [3, \infty]$$.

> **Exercise 8.** Give an example of a set $$X$$, a $$\sigma$$-algebra
> $$\mathcal{S}$$ of subsets of $$X$$, a set $$\mathcal{A}$$ of subsets of
> $$X$$ such that the smallest $$\sigma$$-algebra on $$X$$ containing
> $$\mathcal{A}$$ is $$\mathcal{S}$$, and two measures $$\mu$$ and $$\nu$$ on
> $$(X, \mathcal{S})$$ such that $$\mu(A) = \nu(A)$$ for all
> $$A \in \mathcal{A}$$ and $$\mu(X) = \nu(X) < \infty$$, but
> $$\mu \ne \nu$$.
{: .problem #ex-2c-8 }

*Solution.* $$X = \{1, 2, 3, 4\}$$, $$\mathcal{S} = 2^X$$,
$$\mathcal{A} = \bigl\{ \{1, 2\}, \{1, 3\}, \{2, 4\}, \{3, 4\} \bigr\}$$,
$$\mu = \delta_1 + \delta_4$$ and $$\nu = \delta_2 + \delta_3$$ (Dirac
measures).

Then $$\mu(X) = \nu(X) = 2 < \infty$$ and
$$\mu(A) = \nu(A) = 1$$ for every $$A \in \mathcal{A}$$ (each set of
$$\mathcal{A}$$ contains exactly one of $$1, 4$$ and exactly one of $$2, 3$$).
The smallest $$\sigma$$-algebra containing $$\mathcal{A}$$ is $$2^X$$:
$$\{1\} = \{1, 2\} \cap \{1, 3\}$$, $$\{2\} = \{1, 2\} \cap \{2, 4\}$$,
$$\{3\} = \{1, 3\} \cap \{3, 4\}$$, $$\{4\} = \{2, 4\} \cap \{3, 4\}$$ (an
intersection is a complement of a union of complements), so every singleton and
hence every subset belongs to it.

But $$\mu \ne \nu$$, since $$\mu(\{1\}) = 1 \ne 0 = \nu(\{1\})$$.

> **Exercise 10.** Give an example of a measure space $$(X, \mathcal{S}, \mu)$$
> and a decreasing sequence $$E_1 \supseteq E_2 \supseteq \cdots$$ of sets in
> $$\mathcal{S}$$ such that
>
> $$
> \mu\Bigl( \bigcap_{k=1}^{\infty} E_k \Bigr) \ne \lim_{k \to \infty}
> \mu(E_k).
> $$
{: .problem #ex-2c-10 }

*Solution.* $$X = \mathbb{R}$$, $$\mathcal{S}$$ is the set of all Borel subsets
of $$\mathbb{R}$$, and $$\mu$$ is the outer measure.

$$E_k = (k, \infty)$$.

$$\mu\bigl( \bigcap_k E_k \bigr) = \mu(\emptyset) = 0$$, but
$$\lim_{k \to \infty} \mu(E_k) = \infty$$.

> **Exercise 12.** Suppose $$X$$ is a set and $$\mathcal{S}$$ is the
> $$\sigma$$-algebra of all subsets $$E$$ of $$X$$ such that $$E$$ is countable
> or $$X \setminus E$$ is countable. Give a complete description of the set of
> all measures on $$(X, \mathcal{S})$$.
{: .problem #ex-2c-12 }

*Solution.* If $$X$$ is countable, then $$\mu$$ is uniquely determined by the
values $$\mu(\{x\})$$ of all $$x \in X$$ (every subset of $$X$$ is countable,
and $$\mu(E) = \sum_{x \in E} \mu(\{x\})$$ as in Exercise 2; any weights
$$\mu(\{x\}) \in [0, \infty]$$ give a measure).

Otherwise, it needs an additional value of $$\mu(X)$$, which must be at least

$$
\sum_{x \in X} \mu(\{x\}) = \sup_{\substack{X' \subseteq X \\ X' \text{ is countable}}}
\sum_{x \in X'} \mu(\{x\}).
$$

Note: $$\sum_{x \in X} \mu(\{x\})$$ is not a countable sum and therefore is
**not** $$\mu(X)$$.

Explicitly, let $$X$$ be uncountable, $$w(x) = \mu(\{x\})$$, and
$$T = \{x : w(x) > 0\}$$. A countable set $$E$$ has
$$\mu(E) = \sum_{x \in E} w(x)$$. For a set $$E$$ with countable complement
(co-countable):

- If $$T$$ is countable, then $$X \setminus T$$ is co-countable with
  $$\mu(\{x\}) = 0$$ for all its points, and for a co-countable
  $$E$$ the set $$(X \setminus T) \setminus E$$ is countable of measure $$0$$,
  so $$\mu(E \setminus T) = \mu(X \setminus T) =: \gamma \in [0, \infty]$$. Hence
  $$\mu(E) = \sum_{x \in E} w(x) + \gamma$$ for every co-countable $$E$$.
  Here $$\mu(X) = \sum_{x \in X} w(x) + \gamma$$, so when
  $$\sum_{x \in X} w(x) < \infty$$ the additional value $$\mu(X)$$ (which is
  $$\ge \sum_{x \in X} w(x)$$) determines $$\gamma$$.
  Conversely, for any $$w$$ with countable $$T$$ and any
  $$\gamma \in [0, \infty]$$ this formula defines a measure (it is the weight
  measure plus $$\gamma$$ times the measure that is $$0$$ on countable sets and
  $$1$$ on co-countable sets).
- If $$T$$ is uncountable, then for some $$n$$ there are uncountably many $$x$$
  with $$w(x) > \frac{1}{n}$$, so every co-countable $$E$$ contains infinitely
  many of them and $$\mu(E) = \infty$$. Conversely, $$\mu(E) =
  \sum_{x \in E} w(x)$$ for countable $$E$$ and $$\mu(E) = \infty$$ for
  co-countable $$E$$ is a measure (if a disjoint union is co-countable, exactly
  one of the sets is co-countable and both sides are $$\infty$$; otherwise all
  of them are countable).

## References

- Sheldon Axler, *Measure, Integration & Real Analysis* — Section 2C and
  Exercises 2C. The exercise statements are quoted from the book.
- The notes and the exercise answers are mine, typeset from my handwritten
  notebook. The structure of each answer is unchanged; small slips in the
  answers are corrected, and answers that stopped short are completed along
  the same lines. I did not attempt Exercises 9 and 11, so they are not here.
