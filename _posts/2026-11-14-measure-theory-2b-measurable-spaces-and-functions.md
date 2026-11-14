---
title: "Measure Theory and Real Analysis: 2B Measurable Spaces and Functions"
date: 2026-11-14 13:40:00 +0900
categories: [Study Notes, Measure Theory and Real Analysis]
tags: [sigma-algebra, borel sets, measurable functions, inverse image, exercises]
description: Nonexistence of an extension of length to all subsets of R, sigma-algebras, Borel sets, inverse images, measurable functions and their closure properties, with worked exercises 1, 3, 4, 5, 9 to 19, 22 and 29. Section 2B of Axler's Measure, Integration & Real Analysis.
math: true
mermaid: false
render_with_liquid: false
---

> Typeset from my handwritten notes for section 2B of Axler's *Measure,
> Integration & Real Analysis*. The exercise statements are the textbook's;
> the answers are mine, as I wrote them. My answer to Exercise 19 is
> unfinished, so it is followed by a clearly marked expansion that is not
> mine. Part of the [course overview](/posts/measure-theory-overview/).
{: .prompt-info }

## Notes

> **Theorem (Nonexistence of extension of length to all subsets of
> $$\mathbb{R}$$).** There does not exist a function $$\mu$$ with all the
> following properties.
>
> - **(a)** $$\mu$$ is a function from the set of subsets of $$\mathbb{R}$$ to
>   $$[0,\infty]$$.
> - **(b)** $$\mu(I) = \ell(I)$$ for every open interval $$I$$ of
>   $$\mathbb{R}$$.
> - **(c)** $$\mu\bigl(\bigcup_{k=1}^{\infty} A_k\bigr) =
>   \sum_{k=1}^{\infty} \mu(A_k)$$ for every disjoint sequence
>   $$A_1, A_2, \dots$$ of subsets of $$\mathbb{R}$$ ($$=$$ countable
>   additivity; limits use this property).
> - **(d)** $$\mu(t + A) = \mu(A)$$ for every $$A \subseteq \mathbb{R}$$ and
>   every $$t \in \mathbb{R}$$ ($$=$$ translation invariance).
{: .theorem #thm-nonexistence }

*Proof.* Suppose there **exists** such a function $$\mu$$.

Observe $$\mu(\emptyset) = 0$$ from (b), as
$$\mu(\emptyset) = \ell(\emptyset) = 0$$.

If $$A \subseteq B \subseteq \mathbb{R}$$, then
$$B = A \cup (B \setminus A) \cup \emptyset \cup \emptyset \cup \cdots$$.

Thus,

$$
\mu(B) = \mu(A) + \mu(B \setminus A) + \mu(\emptyset) + \cdots
= \mu(A) + \mu(B \setminus A) \ge \mu(A).
$$

If $$a, b \in \mathbb{R}$$ with $$a < b$$, then
$$(a,b) \subseteq [a,b] \subseteq (a - \varepsilon, b + \varepsilon)$$ for all
$$\varepsilon > 0$$.

Thus, $$b - a \le \mu([a,b]) \le b - a + 2\varepsilon$$ for all
$$\varepsilon > 0$$. Hence, $$\mu([a,b]) = b - a$$.

If $$A_1, A_2, \dots$$ is a sequence of subsets of $$\mathbb{R}$$, then
$$A_1,\ A_2 \setminus A_1,\ A_3 \setminus (A_1 \cup A_2),\ \dots$$ is a
disjoint sequence of subsets of $$\mathbb{R}$$ whose union is
$$\bigcup_{k=1}^{\infty} A_k$$.

Thus,

$$
\begin{aligned}
\mu\Bigl( \bigcup_{k=1}^{\infty} A_k \Bigr)
&= \mu\bigl( A_1 \cup (A_2 \setminus A_1)
   \cup (A_3 \setminus (A_1 \cup A_2)) \cup \cdots \bigr) \\
&= \mu(A_1) + \mu(A_2 \setminus A_1)
   + \mu(A_3 \setminus (A_1 \cup A_2)) + \cdots
   \quad \text{(countable additivity)} \\
&\le \sum_{k=1}^{\infty} \mu(A_k)
   \quad \cdots \text{ countable subadditivity.}
\end{aligned}
$$

Here, we find that $$\mu$$ has all the properties of outer measure. But,
following the proof of nonadditivity of outer measure in this function
$$\mu$$, we obtain that there exist disjoint subsets $$A, B$$ of
$$\mathbb{R}$$ such that $$\mu(A \cup B) \ne \mu(A) + \mu(B)$$.

Thus, this contradicts (c) of the theorem. $$\square$$

Here we concluded that (a) $$\sim$$ (d) cannot exist at the same time.
Giving up one among the properties, we are forced to let go (a),
constructing a new collection: $$\sigma$$-algebra. Experience shows that
$$\sigma$$-algebra is sufficient to take limits.

> **Definition ($$\sigma$$-algebra).** Suppose $$X$$ is a set and
> $$\mathcal{S}$$ is a collection of subsets of $$X$$. If $$\mathcal{S}$$
> satisfies as follows, it is defined a "$$\sigma$$-algebra" on $$X$$.
>
> - $$\emptyset \in \mathcal{S}$$
> - If $$E \in \mathcal{S}$$, then $$X \setminus E \in \mathcal{S}$$
> - If $$E_1, E_2, \dots$$ is a sequence of elements of $$\mathcal{S}$$, then
>   $$\bigcup_{k=1}^{\infty} E_k \in \mathcal{S}$$.
{: .definition #def-sigma-algebra }

**Example.** Suppose $$X$$ is a set. Consider
$$\mathcal{E} = \{E \subseteq X : E \text{ is countable or } X \setminus E
\text{ is countable}\}$$. Is $$\mathcal{E}$$ a $$\sigma$$-algebra on $$X$$?

$$\Rightarrow$$

- $$\emptyset$$ is countable so $$\emptyset \in \mathcal{E}$$.
- If $$E$$ is countable, $$X \setminus (X \setminus E) = E$$
  $$\therefore\ X \setminus E \in \mathcal{E}$$. If $$E$$ is uncountable and
  $$E \in \mathcal{E}$$, it means that $$X \setminus E \in \mathcal{E}$$.
- Suppose $$E_1, E_2, \dots$$ is a sequence of elements of $$\mathcal{E}$$.

  1) If $$E_1, E_2, \dots$$ are all countable, $$\bigcup_{n=1}^{\infty} E_n$$ is
  also countable $$\therefore\ \bigcup_{n=1}^{\infty} E_n \in \mathcal{E}$$.

  2) If $$E_1, E_2, \dots$$ are all uncountable, $$X \setminus E_k$$ are all
  countable. $$\therefore\ X \setminus \bigl( \bigcup_{k=1}^{\infty} E_k \bigr)$$
  is also countable. $$\therefore\ \bigcup_{k=1}^{\infty} E_k \in \mathcal{E}$$.

  3) If some $$E_k$$'s are countable and others are not, classify into two
  sequences $$E_{1c}, E_{2c}, \dots$$ and $$E_{1u}, E_{2u}, \dots$$ with
  $$E_{1c}, E_{2c}, \dots$$ are countable and
  $$X \setminus E_{1u}, X \setminus E_{2u}, \dots$$ are countable.

  $$
  \bigcup_{k=1}^{\infty} E_k
  = \Bigl( \bigcup_{i=1}^{\infty} E_{ic} \Bigr)
  \cup \Bigl( \bigcup_{j=1}^{\infty} E_{ju} \Bigr)
  $$

  $$
  X \setminus \bigcup E_k
  = \Bigl( X \setminus \bigcup E_{ic} \Bigr)
  \cap \Bigl( X \setminus \bigcup E_{ju} \Bigr).
  $$

  Here, since $$X \setminus \bigcup E_{ju}$$ is countable, the intersection of
  any set with a countable set must be countable. Thus
  $$X \setminus \bigcup E_k$$ is countable.

  $$\therefore\ \bigcup E_k \in \mathcal{E}$$.

> **Theorem ($$\sigma$$-algebras are closed under countable intersection).**
> Suppose $$\mathcal{S}$$ is a $$\sigma$$-algebra on a set $$X$$. Then
>
> - **(a)** $$X \in \mathcal{S}$$
> - **(b)** If $$D, E \in \mathcal{S}$$, then $$D \cup E$$, $$D \cap E$$,
>   $$D \setminus E$$ are in $$\mathcal{S}$$.
> - **(c)** If $$E_1, E_2, \dots$$ is a sequence of elements of
>   $$\mathcal{S}$$, then $$\bigcap E_k \in \mathcal{S}$$.
{: .theorem #thm-countable-intersection }

*Proof.* (a) is trivial since $$\emptyset \in \mathcal{S}$$.

(b) is also clear from the definition of $$\sigma$$-algebra.

(c) Since $$X \setminus E_1, X \setminus E_2, \dots$$ is also a sequence of
elements of $$\mathcal{S}$$,

$$
\bigcup (X \setminus E_k) = X \setminus \bigcap E_k
$$

is also in $$\mathcal{S}$$. Thus, $$\bigcap E_k \in \mathcal{S}$$. $$\square$$

> **Definition (Measurable space; measurable set).**
>
> - A measurable space is an ordered pair $$(X, \mathcal{S})$$ where $$X$$ is
>   a set and $$\mathcal{S}$$ is a $$\sigma$$-algebra on $$X$$.
> - An element of $$\mathcal{S}$$ is called an $$\mathcal{S}$$-measurable set,
>   or just a measurable set if $$\mathcal{S}$$ is clear from the context.
{: .definition #def-measurable-space }

**Example.** If $$X = \mathbb{R}$$ and $$\mathcal{S}$$ is the set of all
subsets of $$\mathbb{R}$$ that are countable or have a countable complement,
then the set of rational numbers is $$\mathcal{S}$$-measurable but the set of
positive real numbers is not.

> **Theorem (Smallest $$\sigma$$-algebra containing a collection of
> subsets).** Suppose $$X$$ is a set and $$\mathcal{A}$$ is a set of subsets
> of $$X$$. Then the intersection of all $$\sigma$$-algebras on $$X$$ that
> contain $$\mathcal{A}$$ is a $$\sigma$$-algebra on $$X$$.
{: .theorem #thm-smallest-sigma-algebra }

*Proof.* There is at least one $$\sigma$$-algebra on $$X$$ that contains
$$\mathcal{A}$$ because the $$\sigma$$-algebra consisting of all subsets of
$$X$$ contains $$\mathcal{A}$$.

Let $$\mathcal{S}$$ be the intersection of all $$\sigma$$-algebras on $$X$$
that contain $$\mathcal{A}$$. Then $$\emptyset \in \mathcal{S}$$.

Also, suppose $$E \in \mathcal{S}$$. In other words, $$E$$ is in every
$$\sigma$$-algebra on $$X$$ that contains $$\mathcal{A}$$. Hence,
$$X \setminus E \in \mathcal{S}$$.

Suppose $$E_1, E_2, \dots$$ is a sequence of elements of $$\mathcal{S}$$.
Thus, each $$E_k$$ is in every $$\sigma$$-algebra on $$X$$ that contains
$$\mathcal{A}$$. Thus $$\bigcup_{k=1}^{\infty} E_k$$ is in every
$$\sigma$$-algebra on $$X$$ that contains $$\mathcal{A}$$. Hence
$$\bigcup_{k=1}^{\infty} E_k \in \mathcal{S}$$, which completes the proof
that $$\mathcal{S}$$ is a $$\sigma$$-algebra on $$X$$. $$\square$$

**Example.** Suppose $$X$$ is a set and $$\mathcal{A}$$ is the set of subsets
of $$X$$ that consist of exactly one element. In other words,
$$\mathcal{A} = \{\{x\} : x \in X\}$$. Then, the smallest $$\sigma$$-algebra
on $$X$$ containing $$\mathcal{A}$$ is the set of all subsets $$E$$ of $$X$$
such that $$E$$ is countable or $$X \setminus E$$ is countable.

*Proof.* Let $$\mathcal{S}$$ be the intersection of all $$\sigma$$-algebras on
$$X$$ that contain $$\mathcal{A}$$. Thus, $$\{x\} \in \mathcal{S}$$ for all
$$x \in X$$ and $$X \setminus \{x\} \in \mathcal{S}$$ for all $$x \in X$$.

Thus, any countable union of $$\{x\}$$ and $$X \setminus \{x\}$$ is in
$$\mathcal{S}$$. This means that the set of all subsets $$E$$ of $$X$$ such
that $$E$$ is countable or $$X \setminus E$$ is countable is contained in
$$\mathcal{S}$$. $$\square$$

**Example.** Suppose $$\mathcal{A} = \{(0,1), (0,\infty)\}$$. Then the smallest
$$\sigma$$-algebra on $$\mathbb{R}$$ containing $$\mathcal{A}$$ is

$$
\begin{aligned}
\{\ &\emptyset,\ (0,1),\ (0,\infty),\ (-\infty,0] \cup [1,\infty), \\
&(-\infty,0],\ [1,\infty),\ (-\infty,1),\ \mathbb{R}\ \}.
\end{aligned}
$$

> **Definition (Borel set).** The smallest $$\sigma$$-algebra on
> $$\mathbb{R}$$ containing all open subsets of $$\mathbb{R}$$ is called the
> collection of Borel subsets of $$\mathbb{R}$$. An element of this
> $$\sigma$$-algebra is called a Borel set.
>
> $$=$$ smallest $$\sigma$$-algebra on $$\mathbb{R}$$ containing all open
> "intervals" of $$\mathbb{R}$$.
{: .definition #def-borel-set }

**Examples.**

- Every closed subset of $$\mathbb{R}$$ is a Borel set because every closed
  subset of $$\mathbb{R}$$ is the complement of an open subset of
  $$\mathbb{R}$$.
- Every countable subset of $$\mathbb{R}$$ is a Borel set because if
  $$B = \{x_1, x_2, \dots\}$$, then $$B = \bigcup_{k=1}^{\infty} \{x_k\}$$,
  which is a Borel set because each $$\{x_k\}$$ is a closed set.
- Every half-open interval $$[a,b)$$ where $$a, b \in \mathbb{R}$$ with
  $$a < b$$ is a Borel set since
  $$[a,b) = \bigcap_{k=1}^{\infty} \bigl( a - \frac{1}{k},\, b \bigr)$$.
- If $$f : \mathbb{R} \to \mathbb{R}$$ is a function, then the set of points at
  which $$f$$ is continuous is the intersection of a sequence of open sets and
  thus is a Borel set.

$$\langle$$Note$$\rangle$$ The intersection of every sequence of open subsets
of $$\mathbb{R}$$ is a Borel set. However, the set of all such intersections
is not the set of Borel sets: it is not closed under countable unions. Also,
the set of all countable unions of countable intersections of open subsets of
$$\mathbb{R}$$ is also not the set of Borel sets: it is not closed under
countable intersections. In other words, there is no finite procedure
involving countable unions, countable intersections, and complements for
constructing the collection of Borel sets.

> **Definition (Inverse image; $$f^{-1}(A)$$).** If $$f : X \to Y$$ is a
> function and $$A \subseteq Y$$, then the inverse image $$f^{-1}(A)$$ is
> defined by
>
> $$
> f^{-1}(A) = \{x \in X : f(x) \in A\}.
> $$
{: .definition #def-inverse-image }

> **Theorem (Algebra of inverse images).** Suppose $$f : X \to Y$$ is a
> function. Then
>
> - **(a)** $$f^{-1}(Y \setminus A) = X \setminus f^{-1}(A)$$ for every
>   $$A \subseteq Y$$.
> - **(b)** $$f^{-1}\bigl(\bigcup_{A \in \mathcal{A}} A\bigr) =
>   \bigcup_{A \in \mathcal{A}} f^{-1}(A)$$ for every set $$\mathcal{A}$$ of
>   subsets of $$Y$$.
> - **(c)** $$f^{-1}\bigl(\bigcap_{A \in \mathcal{A}} A\bigr) =
>   \bigcap_{A \in \mathcal{A}} f^{-1}(A)$$ for every set $$\mathcal{A}$$ of
>   subsets of $$Y$$.
{: .theorem #thm-inverse-image-algebra }

*Proof.* (a) Suppose $$A \subseteq Y$$. For $$x \in X$$, we have

$$
\begin{aligned}
x \in f^{-1}(Y \setminus A)
&\Longleftrightarrow f(x) \in Y \setminus A \\
&\Longleftrightarrow f(x) \notin A \\
&\Longleftrightarrow x \notin f^{-1}(A) \\
&\Longleftrightarrow x \in X \setminus f^{-1}(A).
\end{aligned}
$$

$$\therefore\ f^{-1}(Y \setminus A) = X \setminus f^{-1}(A)$$.

(b) Suppose $$\mathcal{A}$$ is a set of subsets of $$Y$$. Then,

$$
\begin{aligned}
x \in f^{-1}\Bigl( \bigcup_{A \in \mathcal{A}} A \Bigr)
&\Longleftrightarrow f(x) \in \bigcup_{A \in \mathcal{A}} A \\
&\Longleftrightarrow f(x) \in A \text{ for some } A \in \mathcal{A} \\
&\Longleftrightarrow x \in f^{-1}(A) \text{ for some } A \in \mathcal{A} \\
&\Longleftrightarrow x \in \bigcup_{A \in \mathcal{A}} f^{-1}(A).
\end{aligned}
$$

$$\therefore\ f^{-1}\bigl(\bigcup_{A \in \mathcal{A}} A\bigr) =
\bigcup_{A \in \mathcal{A}} f^{-1}(A)$$.

(c) Suppose $$\mathcal{A}$$ is a set of subsets of $$Y$$. Then,

$$
\begin{aligned}
x \in f^{-1}\Bigl( \bigcap_{A \in \mathcal{A}} A \Bigr)
&\Longleftrightarrow f(x) \in \bigcap_{A \in \mathcal{A}} A \\
&\Longleftrightarrow f(x) \in A \text{ for every } A \in \mathcal{A} \\
&\Longleftrightarrow x \in f^{-1}(A) \text{ for every } A \in \mathcal{A} \\
&\Longleftrightarrow x \in \bigcap_{A \in \mathcal{A}} f^{-1}(A).
\end{aligned}
$$

$$\square$$

> **Theorem (Inverse image of a composition).** Suppose $$f : X \to Y$$ and
> $$g : Y \to W$$ are functions. Then
>
> $$
> (g \circ f)^{-1}(A) = f^{-1}\bigl( g^{-1}(A) \bigr)
> \quad \text{for every } A \subseteq W.
> $$
{: .theorem #thm-inverse-image-composition }

*Proof.* Trivial.

> **Definition (Measurable function).** Suppose $$(X, \mathcal{S})$$ is a
> measurable space. A function $$f : X \to \mathbb{R}$$ is called
> $$\mathcal{S}$$-measurable if $$f^{-1}(B) \in \mathcal{S}$$ for every Borel
> set $$B \subseteq \mathbb{R}$$.
{: .definition #def-measurable-function }

**Examples.**

- If $$\mathcal{S} = \{\emptyset, X\}$$, then the only
  $$\mathcal{S}$$-measurable functions from $$X$$ to $$\mathbb{R}$$ are the
  constant functions.

  Why? For any Borel set $$B \subseteq \mathbb{R}$$,
  $$f^{-1}(B) = \emptyset$$ or $$f^{-1}(B) = X$$. Since
  $$f^{-1}(B) \ne \emptyset$$, $$f^{-1}(B) = X$$ for any Borel set $$B$$. It is
  clear now that $$f$$ should be a constant function. $$\square$$

- If $$\mathcal{S}$$ is the set of all subsets of $$X$$, then every function
  from $$X$$ to $$\mathbb{R}$$ is $$\mathcal{S}$$-measurable.
- If $$\mathcal{S} = \{\emptyset, (-\infty,0), [0,\infty), \mathbb{R}\}$$,
  then a function $$f : \mathbb{R} \to \mathbb{R}$$ is $$\mathcal{S}$$-measurable
  if and only if $$f$$ is constant on $$(-\infty,0)$$ and $$f$$ is constant on
  $$[0,\infty)$$.

> **Definition (Characteristic function (지표함수); $$\chi_E$$).** Suppose
> $$E$$ is a subset of a set $$X$$. The characteristic function of $$E$$ is
> the function $$\chi_E : X \to \mathbb{R}$$ defined by
>
> $$
> \chi_E(x) =
> \begin{cases}
> 1 & \text{if } x \in E, \\
> 0 & \text{if } x \notin E.
> \end{cases}
> $$
{: .definition #def-characteristic-function }

**Example.** Suppose $$(X, \mathcal{S})$$ is a measurable space with
$$\mathcal{S}$$ the collection of Borel subsets of $$\mathbb{R}$$. Also,
suppose $$E \subseteq X$$ and $$B \subseteq \mathbb{R}$$. Then,

$$
\chi_E^{-1}(B) =
\begin{cases}
E & \text{if } 0 \notin B \text{ and } 1 \in B, \\
X \setminus E & \text{if } 0 \in B \text{ and } 1 \notin B, \\
X & \text{if } 0, 1 \in B, \\
\emptyset & \text{if } 0, 1 \notin B.
\end{cases}
$$

Thus we see that $$\chi_E$$ is an $$\mathcal{S}$$-measurable iff
$$E \in \mathcal{S}$$.

The definition of an $$\mathcal{S}$$-measurable function requires the inverse
image of every Borel subset of $$\mathbb{R}$$ to be in $$\mathcal{S}$$.

> **Theorem (Condition for measurable function).** Suppose
> $$(X, \mathcal{S})$$ is a measurable space and $$f : X \to \mathbb{R}$$ is a
> function such that $$f^{-1}((a,\infty)) \in \mathcal{S}$$ for all
> $$a \in \mathbb{R}$$. Then $$f$$ is an $$\mathcal{S}$$-measurable function.
{: .theorem #thm-condition-measurable }

*Proof.* Let $$\mathcal{T} = \{A \subseteq \mathbb{R} : f^{-1}(A) \in
\mathcal{S}\}$$.

We want to show that every Borel subset of $$\mathbb{R}$$ is in
$$\mathcal{T}$$. To do this, we will first show that $$\mathcal{T}$$ is a
$$\sigma$$-algebra on $$\mathbb{R}$$.

① $$\emptyset \in \mathcal{T}$$ as $$f^{-1}(\emptyset) = \emptyset \in
\mathcal{S}$$.

② If $$A \in \mathcal{T}$$, then $$f^{-1}(A) \in \mathcal{S}$$ by its
construction. Hence $$f^{-1}(\mathbb{R} \setminus A) = X \setminus f^{-1}(A)
\in \mathcal{S}$$, meaning that $$\mathbb{R} \setminus A \in \mathcal{T}$$.

③ If $$A_1, A_2, \dots \in \mathcal{T}$$, then
$$f^{-1}(A_1), f^{-1}(A_2), \dots \in \mathcal{S}$$ by construction. Thus
$$f^{-1}(\bigcup A_k) = \bigcup f^{-1}(A_k) \in \mathcal{S}$$, meaning that
$$\bigcup A_k \in \mathcal{T}$$.

① $$\sim$$ ③ shows that $$\mathcal{T}$$ is a $$\sigma$$-algebra on
$$\mathbb{R}$$.

Now, it is clear that $$\{(a,\infty) : a \in \mathbb{R}\} \subseteq
\mathcal{T}$$.

As $$\mathcal{T}$$ is closed under complementation,
$$\{(-\infty,b] : b \in \mathbb{R}\} \subseteq \mathcal{T}$$.

Also we see that $$\{(a,b] : a, b \in \mathbb{R}, a < b\} \subseteq
\mathcal{T}$$.

Now, since

$$
(a,b) = \bigcup_{k=1}^{\infty} \Bigl( a,\, b - \frac{1}{k} \Bigr]
\quad\text{and}\quad
(-\infty,b) = \bigcup_{k=1}^{\infty} \Bigl( -k,\, b - \frac{1}{k} \Bigr],
$$

$$\{(a,b) : a, b \in \mathbb{R}, a < b\} \subseteq \mathcal{T}$$ and
$$\{(-\infty,b) : b \in \mathbb{R}\} \subseteq \mathcal{T}$$.

Thus, we can conclude that $$\mathcal{T}$$ contains every open subset of
$$\mathbb{R}$$. $$=$$ $$\mathcal{T}$$ contains every Borel subset of
$$\mathbb{R}$$ and thus $$f$$ is $$\mathcal{S}$$-measurable. $$\square$$

Now, consider the case where $$X$$ is a Borel subset of $$\mathbb{R}$$ and
$$\mathcal{S}$$ is the set of Borel subsets of $$\mathbb{R}$$ that are
contained in $$X$$.

> **Definition (Borel measurable functions).** Suppose
> $$X \subseteq \mathbb{R}$$. A function $$f : X \to \mathbb{R}$$ is called
> Borel measurable if $$f^{-1}(B)$$ is a Borel set for every Borel set
> $$B \subseteq \mathbb{R}$$.
{: .definition #def-borel-measurable }

Notably, if $$X \subseteq \mathbb{R}$$ and there exists a Borel measurable
function $$f : X \to \mathbb{R}$$, then $$X$$ must be a Borel set since
$$f^{-1}(\mathbb{R}) = X$$.

If $$X \subseteq \mathbb{R}$$ and $$f : X \to \mathbb{R}$$ is a function, then
$$f$$ is Borel measurable iff $$f^{-1}((a,\infty))$$ is a Borel set for all
$$a \in \mathbb{R}$$.

Suppose $$X$$ is a set and $$f : X \to \mathbb{R}$$ is a function. The
measurability depends on the choice of a $$\sigma$$-algebra on $$X$$. Say
that $$\sigma$$-algebra as $$\mathcal{S}$$. Then, we can discuss whether $$f$$
is $$\mathcal{S}$$-measurable.

Here, if $$X$$ is a Borel subset of $$\mathbb{R}$$, then $$\mathcal{S}$$ might
be the set of Borel sets contained in $$X$$, in which the phrase Borel
measurable means $$\mathcal{S}$$-measurable. However, regardless of
$$\mathcal{S}$$ being a collection of Borel sets, we consider inverse images
of Borel subsets of $$\mathbb{R}$$ when determining whether a function is
$$\mathcal{S}$$-measurable.

> **Theorem (Every continuous function is Borel measurable).** Every
> continuous real-valued function defined on a Borel subset of
> $$\mathbb{R}$$ is a Borel measurable function.
{: .theorem #thm-continuous-borel }

*Proof.* Suppose $$X \subseteq \mathbb{R}$$ is a Borel set and
$$f : X \to \mathbb{R}$$ is continuous. Fix $$a \in \mathbb{R}$$.

If $$x \in X$$ and $$f(x) > a$$, then (by the continuity of $$f$$) there
exists $$\delta_x > 0$$ such that $$f(y) > a$$ for all
$$y \in (x - \delta_x, x + \delta_x) \cap X$$. Thus,

$$
f^{-1}((a,\infty)) =
\Bigl( \bigcup_{x \in f^{-1}((a,\infty))} (x - \delta_x,\, x + \delta_x) \Bigr)
\cap X.
$$

The union is an open subset of $$\mathbb{R}$$, and $$X$$ is a Borel set
$$\rightarrow$$ Borel set.

$$\therefore\ f^{-1}((a,\infty))$$ is a Borel set.

$$\therefore\ f$$ is Borel measurable. $$\square$$

> **Definition (Increasing; strictly increasing).** Suppose
> $$X \subseteq \mathbb{R}$$ and $$f : X \to \mathbb{R}$$ is a function.
>
> - $$f$$ is "increasing" if $$f(x) \le f(y)$$ for all $$x, y \in X$$ with
>   $$x < y$$.
> - $$f$$ is "strictly increasing" if $$f(x) < f(y)$$ for all
>   $$x, y \in X$$ with $$x < y$$.
{: .definition #def-increasing }

> **Theorem (Every increasing function is Borel measurable).** Every
> increasing function defined on a Borel subset of $$\mathbb{R}$$ is a Borel
> measurable function.
{: .theorem #thm-increasing-borel }

*Proof.* Suppose $$X \subseteq \mathbb{R}$$ is a Borel set and
$$f : X \to \mathbb{R}$$ is increasing.

Fix $$a \in \mathbb{R}$$ and let $$b = \inf f^{-1}((a,\infty))$$. Then, it is
clear that $$f^{-1}((a,\infty)) = (b,\infty) \cap X$$ or
$$f^{-1}((a,\infty)) = [b,\infty) \cap X$$.

Either way, $$f^{-1}((a,\infty))$$ is a Borel set.

$$\therefore\ f$$ is Borel measurable. $$\square$$

> **Theorem (Composition of measurable functions).** Suppose
> $$(X, \mathcal{S})$$ is a measurable space and $$f : X \to \mathbb{R}$$ is an
> $$\mathcal{S}$$-measurable function. Suppose $$g$$ is a real-valued Borel
> measurable function defined on a subset of $$\mathbb{R}$$ that includes the
> range of $$f$$. Then $$g \circ f : X \to \mathbb{R}$$ is an
> $$\mathcal{S}$$-measurable function.
{: .theorem #thm-composition-measurable }

*Proof.* Suppose $$B \subseteq \mathbb{R}$$ is a Borel set. Then
$$(g \circ f)^{-1}(B) = f^{-1}(g^{-1}(B))$$.

Here, as $$g$$ is a Borel measurable function, $$g^{-1}(B)$$ is a Borel
subset of $$\mathbb{R}$$. Also, because $$f$$ is $$\mathcal{S}$$-measurable,
$$f^{-1}(g^{-1}(B)) \in \mathcal{S}$$.

Thus, $$(g \circ f)^{-1}(B) \in \mathcal{S}$$ and therefore $$g \circ f$$ is
$$\mathcal{S}$$-measurable. $$\square$$

> **Theorem (Algebraic operations with measurable functions).** Suppose
> $$(X, \mathcal{S})$$ is a measurable space and
> $$f, g : X \to \mathbb{R}$$ are $$\mathcal{S}$$-measurable. Then
>
> - **(a)** $$f + g$$, $$f - g$$, $$fg$$ are $$\mathcal{S}$$-measurable
>   functions.
> - **(b)** if $$g(x) \ne 0$$ for all $$x \in X$$, then $$\dfrac{f}{g}$$ is an
>   $$\mathcal{S}$$-measurable function.
{: .theorem #thm-algebraic-operations }

*Proof.* (a) Suppose $$a \in \mathbb{R}$$. Suppose
$$x \in (f+g)^{-1}((a,\infty))$$. Thus, $$(f+g)(x) > a$$.

Hence, the open interval $$(a - g(x),\, f(x))$$ is nonempty, and thus
contains some rational number $$r$$, meaning that
$$a - g(x) < r < f(x)$$.

Therefore, $$x \in f^{-1}((r,\infty))$$ and
$$x \in g^{-1}((a - r,\infty))$$.

$$
(f+g)^{-1}((a,\infty)) \subseteq \bigcup_{r \in \mathbb{Q}}
\bigl( f^{-1}((r,\infty)) \cap g^{-1}((a - r,\infty)) \bigr).
$$

Also, suppose $$x \in f^{-1}((r,\infty)) \cap g^{-1}((a - r,\infty))$$ for
some $$r \in \mathbb{Q}$$. Thus, $$r < f(x)$$ and $$a - r < g(x)$$
$$\Rightarrow$$ $$a < f(x) + g(x)$$.

$$\therefore\ x \in (f+g)^{-1}((a,\infty))$$ $$\Rightarrow$$

$$
(f+g)^{-1}((a,\infty)) \supseteq \bigcup_{r \in \mathbb{Q}}
\bigl( f^{-1}((r,\infty)) \cap g^{-1}((a - r,\infty)) \bigr).
$$

$$
\therefore\ (f+g)^{-1}((a,\infty)) = \bigcup_{r \in \mathbb{Q}}
\bigl( f^{-1}((r,\infty)) \cap g^{-1}((a - r,\infty)) \bigr).
$$

Here, $$f^{-1}((r,\infty)) \in \mathcal{S}$$ and
$$g^{-1}((a - r,\infty)) \in \mathcal{S}$$, and the countable union of
elements of $$\mathcal{S}$$ is also in $$\mathcal{S}$$. Thus,
$$(f+g)^{-1}((a,\infty)) \in \mathcal{S}$$.

$$\therefore\ f + g$$ is $$\mathcal{S}$$-measurable.

⊗ Note that as $$-x$$ is continuous, $$-g(x)$$ is $$\mathcal{S}$$-measurable.
Also, as $$x^2$$ is continuous, $$(f+g)^2$$, $$f^2$$, $$g^2$$ is
$$\mathcal{S}$$-measurable.

By Note, $$f + (-g) = f - g$$ is $$\mathcal{S}$$-measurable, and

$$
f \cdot g = \frac{1}{2} \bigl( (f+g)^2 - f^2 - g^2 \bigr)
$$

is also $$\mathcal{S}$$-measurable.

(b) Suppose $$g(x) \ne 0$$ for all $$x \in X$$. The function defined on
$$\mathbb{R} \setminus \{0\}$$, which is a Borel subset of $$\mathbb{R}$$,
that takes $$x \to \frac{1}{x}$$ is continuous and therefore is a Borel
measurable function. Thus, $$\frac{1}{g}$$ is $$\mathcal{S}$$-measurable.

$$\therefore\ f \cdot \frac{1}{g} = \frac{f}{g}$$ is
$$\mathcal{S}$$-measurable. $$\square$$

> **Theorem (Pointwise limit of $$\mathcal{S}$$-measurable functions).**
> Suppose $$(X, \mathcal{S})$$ is a measurable space and $$f_1, f_2, \dots$$
> is a sequence of $$\mathcal{S}$$-measurable functions from $$X$$ to
> $$\mathbb{R}$$. Suppose $$\lim_{k \to \infty} f_k(x)$$ exists for each
> $$x \in X$$. Define $$f : X \to \mathbb{R}$$ by
> $$f(x) = \lim_{k \to \infty} f_k(x)$$. Then $$f$$ is an
> $$\mathcal{S}$$-measurable function.
{: .theorem #thm-pointwise-limit }

*Proof.* Suppose that $$a \in \mathbb{R}$$ and
$$x \in f^{-1}((a,\infty))$$, meaning that $$\exists j \in \mathbb{Z}^+$$ such
that $$f(x) > a + \frac{1}{j}$$.

Then, the definition of limit now implies that there exists
$$m \in \mathbb{Z}^+$$ such that $$f_k(x) > a + \frac{1}{j}$$ for all
$$k \ge m$$.

$$
\therefore\ x \in \bigcup_{j=1}^{\infty} \bigcup_{m=1}^{\infty}
\bigcap_{k=m}^{\infty} f_k^{-1}\Bigl( \bigl( a + \tfrac{1}{j},\, \infty \bigr) \Bigr).
$$

$$
\therefore\ f^{-1}((a,\infty)) \subseteq \bigcup_{j} \bigcup_{m}
\bigcap_{k=m}^{\infty} f_k^{-1}\Bigl( \bigl( a + \tfrac{1}{j},\, \infty \bigr) \Bigr).
$$

Now suppose that
$$x \in \bigcup_{j} \bigcup_{m} \bigcap_{k=m}^{\infty}
f_k^{-1}\bigl( (a + 1/j, \infty) \bigr)$$.

Thus, $$\exists j, m \in \mathbb{Z}^+$$ such that
$$f_k(x) > a + \frac{1}{j}$$ for all $$k \ge m$$. Taking the limit as
$$k \to \infty$$, $$f(x) \ge a + \frac{1}{j} > a$$, meaning that
$$x \in f^{-1}((a,\infty))$$.

$$
\therefore\ f^{-1}((a,\infty)) = \bigcup_{j=1}^{\infty} \bigcup_{m=1}^{\infty}
\bigcap_{k=m}^{\infty} f_k^{-1}\Bigl( \bigl( a + \tfrac{1}{j},\, \infty \bigr) \Bigr).
$$

Thus, $$f$$ is $$\mathcal{S}$$-measurable. $$\square$$

> **Definition (Borel subsets of $$[-\infty,\infty]$$).** A subset of
> $$[-\infty,\infty]$$ is a Borel set if its intersection with
> $$\mathbb{R}$$ is a Borel set.
>
> Note: $$[-\infty,\infty] = \mathbb{R} \cup \{-\infty,\infty\}$$.
>
> $$*$$ Also, the set of Borel subsets of $$[-\infty,\infty]$$ is a
> $$\sigma$$-algebra on $$[-\infty,\infty]$$.
{: .definition #def-borel-extended }

> **Definition (Measurable function).** Suppose $$(X, \mathcal{S})$$ is a
> measurable space. A function $$f : X \to [-\infty,\infty]$$ is called
> $$\mathcal{S}$$-measurable if $$f^{-1}(B) \in \mathcal{S}$$ for every Borel
> set $$B \subseteq [-\infty,\infty]$$.
{: .definition #def-measurable-extended }

> **Theorem (Condition for measurable function).** Suppose
> $$(X, \mathcal{S})$$ is a measurable space and
> $$f : X \to [-\infty,\infty]$$ is a function such that
> $$f^{-1}((a,\infty]) \in \mathcal{S}$$ for all $$a \in \mathbb{R}$$. Then
> $$f$$ is an $$\mathcal{S}$$-measurable function.
{: .theorem #thm-condition-measurable-extended }

*Proof.* Let $$\mathcal{T} = \{A \subseteq [-\infty,\infty] : f^{-1}(A) \in
\mathcal{S}\}$$.

First we will show that $$\mathcal{T}$$ is a $$\sigma$$-algebra on
$$[-\infty,\infty]$$.

1) Certainly $$\emptyset \in \mathcal{T}$$, since
$$f^{-1}(\emptyset) = \emptyset \in \mathcal{S}$$.

2) If $$A \in \mathcal{T}$$, then $$f^{-1}(A) \in \mathcal{S}$$; hence
$$f^{-1}([-\infty,\infty] \setminus A) = X \setminus f^{-1}(A) \in
\mathcal{S}$$, and thus $$[-\infty,\infty] \setminus A \in \mathcal{T}$$.

3) If $$A_1, A_2, \dots \in \mathcal{T}$$, then
$$f^{-1}(A_1), f^{-1}(A_2), \dots \in \mathcal{S}$$; hence
$$f^{-1}(\bigcup A_k) = \bigcup f^{-1}(A_k) \in \mathcal{S}$$, and thus
$$\bigcup A_k \in \mathcal{T}$$.

By 1) $$\sim$$ 3), $$\mathcal{T}$$ is a $$\sigma$$-algebra on
$$[-\infty,\infty]$$.

Now, here by the presumptions,
$$\{(a,\infty] : a \in [-\infty,\infty]\} \subseteq \mathcal{T}$$, and
therefore $$\{[-\infty,b] : b \in [-\infty,\infty]\} \subseteq \mathcal{T}$$.

This shows that
$$\{(a,b] : a < b \text{ and } a, b \in [-\infty,\infty]\} \subseteq
\mathcal{T}$$. Because

$$
(a,b) = \bigcup_{k=1}^{\infty} \Bigl( a,\, b - \frac{1}{k} \Bigr]
\quad\text{and}\quad
(-\infty,b) = \bigcup_{k=1}^{\infty} \Bigl( -k,\, b - \frac{1}{k} \Bigr],
$$

we can conclude that $$\mathcal{T}$$ contains every open subset of
$$\mathbb{R}$$.

Also, $$[-\infty,b) = \bigcup [-\infty,\, b - \frac{1}{k}]$$ and
$$\{[-\infty,b) : b \in [-\infty,\infty]\} \subseteq \mathcal{T}$$.

Finally, $$\{\{-\infty\} \cup (a,\infty]\} \subseteq \mathcal{T}$$ since
$$\{(-\infty,a] : a \in [-\infty,\infty]\} \subseteq \mathcal{T}$$, and
$$\{[-\infty,b) \cup \{\infty\} : b \in [-\infty,\infty]\} \subseteq
\mathcal{T}$$ since $$\{[b,\infty) : b \in [-\infty,\infty]\} \subseteq
\mathcal{T}$$.

Thus, $$\mathcal{T}$$ includes every subset of $$[-\infty,\infty]$$ whose
intersection with $$\mathbb{R}$$ is a Borel set.

$$\therefore\ f$$ is $$\mathcal{S}$$-measurable. $$\square$$

> **Theorem (Infimum and supremum of a sequence of
> $$\mathcal{S}$$-measurable functions).** Suppose $$(X, \mathcal{S})$$ is a
> measurable space and $$f_1, f_2, \dots$$ is a sequence of
> $$\mathcal{S}$$-measurable functions from $$X$$ to $$[-\infty,\infty]$$.
> Define $$g, h : X \to [-\infty,\infty]$$ by
>
> $$
> g(x) = \inf\{f_k(x) : k \in \mathbb{Z}^+\}
> \quad\text{and}\quad
> h(x) = \sup\{f_k(x) : k \in \mathbb{Z}^+\}.
> $$
>
> Then, $$g$$ and $$h$$ are $$\mathcal{S}$$-measurable functions.
{: .theorem #thm-inf-sup }

*Proof.* Let $$a \in \mathbb{R}$$.

① Suppose $$x \in h^{-1}((a,\infty])$$, meaning that $$h(x) > a$$. Then by
the definition of supremum, there exists at least one $$k \in \mathbb{Z}^+$$
such that $$h(x) \ge f_k(x) > a$$.

$$\therefore\ x \in \bigcup_k f_k^{-1}((a,\infty])$$ $$\Rightarrow$$
$$h^{-1}((a,\infty]) \subseteq \bigcup_k f_k^{-1}((a,\infty])$$.

② Suppose $$x \in \bigcup_k f_k^{-1}((a,\infty])$$, meaning that for at
least one $$k \in \mathbb{Z}^+$$, $$f_k(x) > a$$. Thus,
$$\sup_k f_k(x) > a$$, i.e. $$h(x) > a$$.

$$\therefore\ x \in h^{-1}((a,\infty])$$ $$\Rightarrow$$
$$h^{-1}((a,\infty]) = \bigcup_k f_k^{-1}((a,\infty])$$.

Therefore, $$h$$ is $$\mathcal{S}$$-measurable.

Now, note that
$$g(x) = -\sup\{-f_k(x) : k \in \mathbb{Z}^+\}$$, and thus is
$$\mathcal{S}$$-measurable. $$\square$$

## Exercises 2B

> **Exercise 1.** Show that
> $$\mathcal{S} = \bigl\{ \bigcup_{n \in K} (n, n+1] : K \subseteq \mathbb{Z}
> \bigr\}$$ is a $$\sigma$$-algebra on $$\mathbb{R}$$.
{: .problem #ex-2b-1 }

*Solution.* Write $$S(K) = \bigcup_{n \in K} (n, n+1]$$ for
$$K \subseteq \mathbb{Z}$$.

① $$\emptyset \in \mathcal{S}$$ as $$\emptyset \subseteq \mathbb{Z}$$.

② For an arbitrary $$K \subseteq \mathbb{Z}$$,

$$
S(K) = \mathbb{R} \setminus S(\mathbb{Z} \setminus K).
$$

③ $$\displaystyle \bigcup_k S(K_k) = S\bigl( \bigcup_k K_k \bigr)$$.

> **Exercise 3.** Suppose $$\mathcal{S}$$ is the smallest $$\sigma$$-algebra on
> $$\mathbb{R}$$ containing $$\{(r,s] : r, s \in \mathbb{Q}\}$$. Prove that
> $$\mathcal{S}$$ is the collection of Borel subsets of $$\mathbb{R}$$.
{: .problem #ex-2b-3 }

*Solution.* Suppose $$\mathcal{S}$$ is the smallest $$\sigma$$-algebra on
$$\mathbb{R}$$ containing $$\{(r,\infty) : r \in \mathbb{Q}\}$$, then
$$\mathcal{S}$$ is the collection of Borel subsets of $$\mathbb{R}$$. It also
holds if $$(r,\infty)$$ is replaced by $$[r,\infty)$$. $$\rightarrow$$ Prove
this first.

Let $$q_1, q_2, \dots$$ be an enumeration of $$\mathbb{Q} \cap (-\infty,a)$$.
Then, $$[a,\infty) = \bigcap_{k=1}^{\infty} (q_k,\infty)$$.

Also, let $$q'_1, q'_2, \dots$$ be an enumeration of
$$\mathbb{Q} \cap (a,\infty)$$. Then, $$(a,\infty) = \bigcup_k
(q'_k,\infty)$$.

Now, $$(a,\infty) = \bigcup_{k=0}^{\infty} (a + k,\, a + k + 1]$$, and thus
$$\{(r,s] : r, s \in \mathbb{Q}\}$$ generates the collection of Borel subsets
of $$\mathbb{R}$$.

> **Exercise 4.** Suppose $$\mathcal{S}$$ is the smallest $$\sigma$$-algebra on
> $$\mathbb{R}$$ containing $$\{(r,n] : r \in \mathbb{Q}, n \in \mathbb{Z}\}$$.
> Prove that $$\mathcal{S}$$ is the collection of Borel subsets of
> $$\mathbb{R}$$.
{: .problem #ex-2b-4 }

*Solution.*

$$
\bigl( a,\, \lfloor a \rfloor + 1 \bigr] \cup \bigcup_{k=1}^{\infty}
\bigl( \lfloor a \rfloor + k,\, \lfloor a \rfloor + k + 1 \bigr]
= (a,\infty).
$$

> **Exercise 5.** Suppose $$\mathcal{S}$$ is the smallest $$\sigma$$-algebra on
> $$\mathbb{R}$$ containing $$\{(r, r+1) : r \in \mathbb{Q}\}$$. Prove that
> $$\mathcal{S}$$ is the collection of Borel subsets of $$\mathbb{R}$$.
{: .problem #ex-2b-5 }

*Solution.*

$$
(a,\infty) = \bigcup_{k=0}^{\infty} (a + k,\, a + k + 1].
$$

> **Exercise 9.** Give an example of a measurable space $$(X, \mathcal{S})$$
> and a function $$f : X \to \mathbb{R}$$ such that $$\lvert f\rvert$$ is
> $$\mathcal{S}$$-measurable but $$f$$ is not $$\mathcal{S}$$-measurable.
{: .problem #ex-2b-9 }

*Solution.* $$X = \mathbb{R}$$ and $$\mathcal{S} = \{\emptyset, X\}$$.

$$
f(x) =
\begin{cases}
1 & (x \ge 0), \\
-1 & (x < 0).
\end{cases}
$$

> **Exercise 10.** Show that the set of real numbers that have a decimal
> expansion with the digit 5 appearing infinitely often is a Borel set.
{: .problem #ex-2b-10 }

*Solution.* Consider the set of real numbers with the digit 5 right after the
decimal place:

$$
D_1 = \bigcup_{k \in \mathbb{Z}} [k + 0.5,\ k + 0.6].
$$

Say $$0.6 = 0.5\dot{9}$$ for simplicity.

Then, $$D_n = 10^{-(n-1)} D_1$$.

Thus, the set of real numbers having the digit 5 is $$\bigcup_n D_n$$.

Here, the set $$T$$ (we construct) having infinitely often digit 5, should
exclude the set of only finitely many digit 5's. That is, there exists a
positive integer $$N$$ such that $$r \notin D_z$$ for all $$z > N$$.

$$
\therefore\ T = \bigcup_n D_n \setminus \bigcup_{N \in \mathbb{N}}
\Bigl( \mathbb{R} \setminus \bigcup_{z > N} D_z \Bigr).
$$

Since $$D_n$$ is a Borel set, $$T$$ is a subset of $$\mathbb{R}$$ with only
Borel sets.

> **Exercise 11.** Suppose $$\mathcal{T}$$ is a $$\sigma$$-algebra on a set
> $$Y$$ and $$X \in \mathcal{T}$$. Let
> $$\mathcal{S} = \{E \in \mathcal{T} : E \subseteq X\}$$.
>
> - **(a)** Show that $$\mathcal{S} = \{F \cap X : F \in \mathcal{T}\}$$.
> - **(b)** Show that $$\mathcal{S}$$ is a $$\sigma$$-algebra on $$X$$.
{: .problem #ex-2b-11 }

*Solution.* $$\mathcal{T}$$: $$\sigma$$-algebra on $$Y$$, $$X \in \mathcal{T}$$,
$$\mathcal{S} = \{E \in \mathcal{T} : E \subseteq X\}$$.

(a) ① Suppose $$x \in E \subseteq X$$. Then, $$x \in X$$ and
$$E \in \mathcal{T}$$.

$$\therefore\ x \in F \cap X$$ with some $$F$$ in $$\mathcal{T}$$.
$$\therefore\ \mathcal{S} \subseteq \{F \cap X : F \in \mathcal{T}\}$$.

② Suppose $$x \in F \cap X$$ with $$F \in \mathcal{T}$$. Then,
$$F \cap X \subseteq X$$ and as $$X \in \mathcal{T}$$,
$$F \cap X \in \mathcal{T}$$.

$$\therefore\ \mathcal{S} = \{F \cap X : F \in \mathcal{T}\}$$.

(b)

- $$\emptyset \in \mathcal{S}$$ since $$\emptyset \cap X = \emptyset$$ where
  $$\emptyset \in \mathcal{T}$$.
- If $$E \in \mathcal{S}$$, $$\exists F \in \mathcal{T}$$ such that
  $$E = F \cap X$$. Thus, $$X \setminus E = X \setminus (F \cap X) =
  X \setminus F$$.

  Here, $$X \setminus F = X \cap (Y \setminus F)$$. Here, as
  $$X \in \mathcal{T}$$, $$X \subseteq Y$$ and therefore,
  $$Y \setminus F \in \mathcal{T}$$ and thus $$X \setminus E \in
  \mathcal{S}$$.
- Define $$E_1, E_2, \dots$$ a sequence of subsets of $$\mathcal{S}$$, with
  $$E_k = F_k \cap X$$ and $$F_k \in \mathcal{T}$$. Since
  $$\bigcup F_k \in \mathcal{T}$$, $$\bigcup E_k \in \mathcal{S}$$.

  Then, $$\bigcup E_k = \bigcup (F_k \cap X) = X \cap \bigcup F_k$$.

$$\mathcal{S}$$ is a $$\sigma$$-algebra on $$X$$.

> **Exercise 12.** Suppose $$f : \mathbb{R} \to \mathbb{R}$$ is a function.
>
> - **(a)** For $$k \in \mathbb{Z}^+$$, let
>
>   $$
>   G_k = \Bigl\{ a \in \mathbb{R} : \text{there exists } \delta > 0
>   \text{ such that } \lvert f(b) - f(c)\rvert < \frac{1}{k}
>   \text{ for all } b, c \in (a - \delta, a + \delta) \Bigr\}.
>   $$
>
>   Prove that $$G_k$$ is an open subset of $$\mathbb{R}$$ for each
>   $$k \in \mathbb{Z}^+$$.
> - **(b)** Prove that the set of points at which $$f$$ is continuous equals
>   $$\bigcap_{k=1}^{\infty} G_k$$.
> - **(c)** Conclude that the set of points at which $$f$$ is continuous is a
>   Borel set.
{: .problem #ex-2b-12 }

*Solution.* (a) Fix $$k \in \mathbb{Z}^+$$. If $$\delta' > \delta > 0$$, we
know that if the predicate for $$\delta'$$ holds then the predicate for
$$\delta$$ holds.

Hence, if $$a \in G_k$$ holds, meaning that there exists an open neighborhood
$$D_\delta$$ of $$a$$ such that the predicate $$P(D_\delta)$$ holds, then for
every $$a' \in D_\delta$$ we can construct a neighborhood $$D_{\delta'}$$ of
$$a'$$ that is completely enclosed by $$D_\delta$$, and thus
$$P(D_{\delta'})$$ holds. $$\therefore\ a' \in G_k$$.

$$\therefore\ G_k$$ is open.

(b) By definition: (Continuity at $$a$$: $$\forall \varepsilon > 0$$,
$$\exists \delta > 0$$ such that $$\lvert f(b) - f(c)\rvert < \varepsilon$$
for all $$b, c \in N_\delta(a)$$.)

(c) $$\bigcap_{k=1}^{\infty} G_k$$ is an intersection of countably many open
sets, making it a Borel set.

> **Exercise 13.** Suppose $$(X, \mathcal{S})$$ is a measurable space,
> $$E_1, \dots, E_n$$ are disjoint subsets of $$X$$, and
> $$c_1, \dots, c_n$$ are distinct nonzero real numbers. Prove that
> $$c_1 \chi_{E_1} + \cdots + c_n \chi_{E_n}$$ is an
> $$\mathcal{S}$$-measurable function if and only if
> $$E_1, \dots, E_n \in \mathcal{S}$$.
{: .problem #ex-2b-13 }

*Solution.* Define $$f = c_1 \chi_{E_1} + \cdots + c_n \chi_{E_n}$$.

($$\Leftarrow$$) If $$E_1, \dots, E_n \in \mathcal{S}$$, fix $$a \in \mathbb{R}$$.

If $$\max\{c_k : k = 1, \dots, n\} \le a$$ and $$a \ge 0$$,
$$f^{-1}((a,\infty)) = \emptyset \in \mathcal{S}$$.

Otherwise,

$$
f^{-1}((a,\infty)) = \bigcup_{k \in \{k : c_k > a\}} E_k
\ \Bigl( \cup \bigl( X \setminus \textstyle\bigcup_{k=1}^{n} E_k \bigr)
\text{ if } a < 0 \Bigr) \in \mathcal{S}.
$$

$$\therefore\ f^{-1}((a,\infty)) \in \mathcal{S}$$. $$\Rightarrow$$ $$f$$ is an
$$\mathcal{S}$$-measurable function.

($$\Rightarrow$$) If $$f$$ is $$\mathcal{S}$$-measurable function, it means
that for all $$k \in \{1, \dots, n\}$$,
$$f^{-1}(\{c_k\}) = E_k \in \mathcal{S}$$.

> **Exercise 14.**
>
> - **(a)** Suppose $$f_1, f_2, \dots$$ is a sequence of functions from a set
>   $$X$$ to $$\mathbb{R}$$. Explain why
>
>   $$
>   \{x \in X : \text{the sequence } f_1(x), f_2(x), \dots
>   \text{ has a limit in } \mathbb{R}\}
>   = \bigcap_{n=1}^{\infty} \bigcup_{j=1}^{\infty} \bigcap_{k=j}^{\infty}
>   (f_j - f_k)^{-1}\bigl( (-\tfrac{1}{n}, \tfrac{1}{n}) \bigr).
>   $$
>
> - **(b)** Suppose $$(X, \mathcal{S})$$ is a measurable space and
>   $$f_1, f_2, \dots$$ is a sequence of $$\mathcal{S}$$-measurable functions
>   from $$X$$ to $$\mathbb{R}$$. Prove that
>   $$\{x \in X : \text{the sequence } f_1(x), f_2(x), \dots
>   \text{ has a limit in } \mathbb{R}\}$$ is an $$\mathcal{S}$$-measurable
>   subset of $$X$$.
{: .problem #ex-2b-14 }

*Solution.* (a) A pointwise limit $$f_1(x), f_2(x), \dots$$ is convergent iff
$$\forall \varepsilon > 0$$, $$\exists j \in \mathbb{N}$$ such that
$$\lvert f_s(x) - f_k(x)\rvert < \varepsilon$$ for all $$s, k \ge j$$.

Now, taking $$s = j$$ gives $$\lvert f_j(x) - f_k(x)\rvert < \varepsilon$$ for
all $$k \ge j$$.

Also, discretize $$\varepsilon = \frac{1}{n}$$ as $$n \to \infty$$.

$$
\therefore\ \{x \in X : \text{the sequence } f_1(x), f_2(x), \dots
\text{ has a limit in } \mathbb{R}\}
= \bigcap_{n=1}^{\infty} \bigcup_{j=1}^{\infty} \bigcap_{k=j}^{\infty}
(f_j - f_k)^{-1}\bigl( (-\tfrac{1}{n}, \tfrac{1}{n}) \bigr).
$$

(b) Trivial.

> **Exercise 15.** Suppose $$X$$ is a set and $$E_1, E_2, \dots$$ is a
> disjoint sequence of subsets of $$X$$ such that
> $$\bigcup_{k=1}^{\infty} E_k = X$$. Let
> $$\mathcal{S} = \{\bigcup_{k \in K} E_k : K \subseteq \mathbb{Z}^+\}$$.
>
> - **(a)** Show that $$\mathcal{S}$$ is a $$\sigma$$-algebra on $$X$$.
> - **(b)** Prove that a function from $$X$$ to $$\mathbb{R}$$ is
>   $$\mathcal{S}$$-measurable if and only if the function is constant on
>   $$E_k$$ for every $$k \in \mathbb{Z}^+$$.
{: .problem #ex-2b-15 }

*Solution.* (a) ① Consider $$E_1, X \setminus E_1, \emptyset, \emptyset,
\dots$$. Then $$\bigcup_{k \ge 3} E_k = \emptyset$$.

② Say that $$E = \bigcup_{k \in K} E_k \in \mathcal{S}$$. Then, since
$$\bigcup_k E_k = X$$, $$X \setminus E = \bigcup_{k \notin K} E_k \in
\mathcal{S}$$.

③ Trivial.

(b) ($$\Leftarrow$$) If the function is constant on $$E_k$$ for every
$$k \in \mathbb{Z}^+$$,

$$
f^{-1}((a,\infty)) = \bigcup_{k \in K'} E_k \in \mathcal{S}.
$$

($$\Rightarrow$$) If $$f$$ is $$\mathcal{S}$$-measurable. WLOG let $$k = 1$$.
Suppose that $$f$$ is not constant on $$E_k$$. In other words, if
$$f(x) \ne f(y)$$ ($$x, y \in E_1$$), consider
$$T = f^{-1}(\{f(x)\})$$. Thus, $$y \notin T$$ and $$x \in T$$.

But as $$f$$ is $$\mathcal{S}$$-measurable, $$T \in \mathcal{S}$$. In other
words, $$T = \bigcup_{k \in K} E_k$$ for some $$K \subseteq \mathbb{Z}^+$$.

$$\rightarrow$$ $$1 \in K$$ and $$1 \notin K$$ holds, making a contradiction.

> **Exercise 16.** Suppose $$\mathcal{S}$$ is a $$\sigma$$-algebra on a set
> $$X$$ and $$A \subseteq X$$. Let
>
> $$
> \mathcal{S}_A = \{E \in \mathcal{S} : A \subseteq E \text{ or }
> A \cap E = \emptyset\}.
> $$
>
> - **(a)** Prove that $$\mathcal{S}_A$$ is a $$\sigma$$-algebra on $$X$$.
> - **(b)** Suppose $$f : X \to \mathbb{R}$$ is a function. Prove that $$f$$ is
>   measurable with respect to $$\mathcal{S}_A$$ if and only if $$f$$ is
>   measurable with respect to $$\mathcal{S}$$ and $$f$$ is constant on
>   $$A$$.
{: .problem #ex-2b-16 }

*Solution.* (a) ① Consider $$\emptyset$$ $$\Rightarrow$$
$$A \cap \emptyset = \emptyset$$ $$\therefore\ \emptyset \in
\mathcal{S}_A$$.

② If $$E \in \mathcal{S}_A$$, $$A \subseteq E$$ or $$A \cap E = \emptyset$$.

1) $$A \subseteq E$$ $$\Rightarrow$$ $$A \cap (X \setminus E) = \emptyset$$.

2) $$A \cap E = \emptyset$$, $$\Rightarrow$$ $$A \subseteq X \setminus E$$,
since $$A \subseteq X$$.

③ Trivial.

(b) ($$\Leftarrow$$) If $$f$$ is measurable with $$\mathcal{S}$$ and is
constant on $$A$$, $$f^{-1}((a,\infty)) \in \mathcal{S}$$. Suppose that
$$f(x) = c$$ for all $$x \in A$$.

If $$a \ge c$$, $$A \cap f^{-1}((a,\infty)) = \emptyset$$ and thus
$$f^{-1}((a,\infty)) \in \mathcal{S}_A$$.

Else, $$A \subseteq f^{-1}((a,\infty))$$ and thus
$$f^{-1}((a,\infty)) \in \mathcal{S}_A$$.

$$f$$ is measurable with respect to $$\mathcal{S}_A$$.

($$\Rightarrow$$) If $$f$$ is measurable with respect to $$\mathcal{S}_A$$,
since $$\mathcal{S}_A \subseteq \mathcal{S}$$,
$$f^{-1}((a,\infty)) \in \mathcal{S}_A \subseteq \mathcal{S}$$. Thus, $$f$$ is
$$\mathcal{S}$$-measurable.

Suppose that $$f$$ is not constant on $$A$$. In other words, if
$$f(x) \ne f(y)$$ for some $$x, y \in A$$.

Consider $$T = f^{-1}(\{f(x)\}) \in \mathcal{S}_A$$. Here, $$x \in T$$ and
$$y \notin T$$. Also, $$T \in \mathcal{S}_A$$.

Now, since $$x \in A$$, $$A \subseteq T$$. But, $$y \notin T$$ which
contradicts.

> **Exercise 17.** Suppose $$X$$ is a Borel subset of $$\mathbb{R}$$ and
> $$f : X \to \mathbb{R}$$ is a function such that
> $$\{x \in X : f \text{ is not continuous at } x\}$$ is a countable set.
> Prove $$f$$ is a Borel measurable function.
{: .problem #ex-2b-17 }

*Solution.* We only have to see if $$f^{-1}((a,\infty))$$ is a Borel set for
all $$a \in \mathbb{R}$$.

Since there are only countably many points where $$f$$ is not continuous,
$$D'(a) = \{x \in D : f(x) > a\}$$ ($$D = \{x \in X : f \text{ is not
continuous at } x\}$$) is a Borel set.

Now, $$f^{-1}((a,\infty)) = \{x \in X \setminus D : f(x) > a\} \cup D'(a)$$.

Here, $$\{x \in X \setminus D : f(x) > a\}$$ is countable union of domains of
continuous functions.

Thus, $$\{x \in X \setminus D : f(x) > a\}$$ is also a Borel set.

> **Exercise 18.** Suppose $$f : \mathbb{R} \to \mathbb{R}$$ is differentiable
> at every element of $$\mathbb{R}$$. Prove that $$f'$$ is a Borel measurable
> function from $$\mathbb{R}$$ to $$\mathbb{R}$$.
{: .problem #ex-2b-18 }

*Solution.* $$f'(x)$$ is the pointwise limit of

$$
f_n(x) = \frac{f(x + 1/n) - f(x)}{1/n},
$$

which is clearly Borel measurable.

> **Exercise 19.** Suppose $$X$$ is a nonempty set and $$\mathcal{S}$$ is the
> $$\sigma$$-algebra on $$X$$ consisting of all subsets of $$X$$ that are
> either countable or have a countable complement in $$X$$. Give a
> characterization of the $$\mathcal{S}$$-measurable real-valued functions on
> $$X$$.
{: .problem #ex-2b-19 }

*Solution (my handwritten answer, unfinished).*

> **Lemma.** An uncountable subset $$S'$$ of $$\mathbb{R}$$ can always be
> partitioned into two uncountable subsets $$A, B$$ such that
> $$\sup A \le \inf B$$.

Using the lemma, suppose $$f(X)$$ is uncountable. Then, we can partition as
$$A \cup B = f(X)$$ where $$A, B$$ are uncountable.

Since the range of countable subsets are always countable, $$f^{-1}(A)$$ and
$$f^{-1}(X \setminus A) = f^{-1}(B)$$ are both uncountable, meaning that
$$f^{-1}(A) \notin \mathcal{S}$$ which is a contradiction.

Thus, $$f(X)$$ is countable.

$$\therefore\ \exists X_1, X_2, \dots, X_n, \dots$$ such that
$$\bigcup_i X_i = X$$ and $$f(X_i) = \{y_i\}$$, $$y_i \ne y_j$$ for all
$$i \ne j$$.

*Expansion (mine, not part of the handwritten answer: it proves the lemma,
fills the step "$$f^{-1}(A) \notin \mathcal{S}$$", and finishes the
characterization).*

**Proof of the lemma.** Let $$U \subseteq \mathbb{R}$$ be uncountable, and for
$$q \in \mathbb{R}$$ put $$L(q) = U \cap (-\infty,q]$$ and
$$R(q) = U \cap (q,\infty)$$. We claim there is some $$q$$ with both
$$L(q)$$ and $$R(q)$$ uncountable; then $$A = L(q)$$ and $$B = R(q)$$ give
$$\sup A \le q \le \inf B$$.

Suppose not. Since $$U = L(q) \cup R(q)$$ is uncountable, exactly one of the
two is uncountable for every $$q$$. $$L(q)$$ is increasing in $$q$$, so
$$p = \sup\{q : L(q) \text{ is countable}\} \in [-\infty,\infty]$$. If
$$p = \infty$$, then $$U = \bigcup_n L(n)$$ is countable; if $$p = -\infty$$,
then every $$R(q)$$ is countable and $$U = \bigcup_n R(-n)$$ is countable.
So $$p$$ is finite, $$L(q)$$ is countable for $$q < p$$, and $$R(q)$$ is
countable for $$q > p$$. Then
$$U \subseteq \bigcup_n L(p - \tfrac{1}{n}) \cup \{p\} \cup \bigcup_n
R(p + \tfrac{1}{n})$$ is countable, a contradiction.

**The step $$f^{-1}(A) \notin \mathcal{S}$$.** Take $$q$$ as above for
$$U = f(X)$$. Then $$f^{-1}((-\infty,q]) \supseteq f^{-1}(A)$$ is
uncountable (otherwise $$A \subseteq f\bigl(f^{-1}(A)\bigr)$$ would be
countable), and likewise $$f^{-1}((q,\infty)) \supseteq f^{-1}(B \setminus
\{q\})$$ is uncountable. These two sets are complements of each other, and
neither is countable, so $$f^{-1}((-\infty,q]) \notin \mathcal{S}$$, although
$$(-\infty,q]$$ is a Borel set. This contradicts the measurability of $$f$$,
so $$f(X)$$ is countable.

**Characterization.** A function $$f : X \to \mathbb{R}$$ is
$$\mathcal{S}$$-measurable if and only if there is a $$c \in \mathbb{R}$$ such
that $$\{x \in X : f(x) \ne c\}$$ is countable. That is, $$f$$ is constant
except on a countable set.

*Proof.* ($$\Rightarrow$$) Continue from the sets $$X_i = f^{-1}(\{y_i\})$$
above. Each $$X_i \in \mathcal{S}$$ because $$\{y_i\}$$ is Borel, so each
$$X_i$$ is countable or has a countable complement. If $$X$$ is countable,
every set $$\{f \ne c\}$$ is countable and we are done. If $$X$$ is
uncountable, then since $$X = \bigcup_i X_i$$ is a countable union, some
$$X_{i_0}$$ is uncountable, hence has a countable complement. Put
$$c = y_{i_0}$$. Then $$\{f \ne c\} = X \setminus X_{i_0}$$ is countable.

($$\Leftarrow$$) Suppose $$\{f \ne c\}$$ is countable and $$B \subseteq
\mathbb{R}$$ is Borel. If $$c \in B$$, then $$f^{-1}(B) \supseteq \{f = c\}$$,
so the complement of $$f^{-1}(B)$$ lies in $$\{f \ne c\}$$ and is countable.
If $$c \notin B$$, then $$f^{-1}(B) \subseteq \{f \ne c\}$$ is countable. In
both cases $$f^{-1}(B) \in \mathcal{S}$$. $$\square$$

> **Exercise 22.** Suppose $$B \subseteq \mathbb{R}$$ and $$f : B \to
> \mathbb{R}$$ is an increasing function. Prove that $$f$$ is continuous at
> every element of $$B$$ except for a countable subset of $$B$$.
{: .problem #ex-2b-22 }

*Solution.* Increasing function $$\Rightarrow$$ can find intervals of
discontinuous ranges.

Select $$q_k$$ from each interval.

The number of intervals is mapped to $$\mathbb{Q}$$.

$$\therefore$$ countable.

> **Exercise 29.** Give an example of a measurable space $$(X, \mathcal{S})$$
> and a family $$\{f_t\}_{t \in \mathbb{R}}$$ such that each $$f_t$$ is an
> $$\mathcal{S}$$-measurable function from $$X$$ to $$[0,1]$$, but the function
> $$f : X \to [0,1]$$ defined by
>
> $$
> f(x) = \sup\{f_t(x) : t \in \mathbb{R}\}
> $$
>
> is not $$\mathcal{S}$$-measurable.
>
> [Compare this exercise to 2.53, where the index set is $$\mathbb{Z}^+$$
> rather than $$\mathbb{R}$$.]
{: .problem #ex-2b-29 }

*Solution.* Let $$E$$ be a non-Borel subset of $$\mathbb{R}$$.

$$
f_t(x) =
\begin{cases}
1 & x = t \text{ and } t \in E, \\
0 & \text{otherwise}
\end{cases}
\qquad (\text{Borel}).
$$

$$\sup\{f_t(x)\} = f(x) = \chi_E$$ $$\therefore$$ not
$$\mathcal{S}$$-measurable.

## References

- Sheldon Axler, *Measure, Integration & Real Analysis* — Section 2B and
  Exercises 2B. The exercise statements are quoted from the book.
- The notes and the exercise answers are mine, typeset from my handwritten
  notebook. The structure of each answer is unchanged; small slips in the
  answers are corrected.
- My answer to Exercise 19 is unfinished. The lemma's proof, the justification
  of $$f^{-1}(A) \notin \mathcal{S}$$ and the final characterization under
  "Expansion" are written for this post and are not from my notebook.
