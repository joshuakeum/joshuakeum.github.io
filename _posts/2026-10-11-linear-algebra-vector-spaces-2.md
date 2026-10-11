---
title: "Linear Algebra: Vector Spaces (Part 2)"
date: 2026-10-11 00:40:00 +0900
categories: [Course Notes, Linear Algebra]
tags: [vector spaces, basis, dimension, quotient spaces]
description: Definitions, theorems with proofs, and solved problems for Chapter 1 of Linear Algebra, §1.6 and §1.7 — bases and dimension, maximal linearly independent subsets, and quotient spaces.
math: true
mermaid: false
render_with_liquid: false
---

> **How to read the labels.** This post continues
> [Chapter 1, Part 1](/posts/linear-algebra-vector-spaces/), which covers
> §1.1 to §1.5. It covers §1.6 and §1.7, and then quotient spaces, which were
> lectured from a separate set of slides and close the chapter. The labels
> are as in Part 1: definitions, theorems and their numbers follow the
> lecture slides, an **Exercise a.b.c** is a textbook exercise that the
> lecture stated and used as a theorem, and a **Problem a.b.k** is the
> $$k$$-th question for §a.b on the course problem sheet. Results of Part 1
> are cited by number and link to that post.
{: .prompt-info }

Throughout, $$\mathbb{F}$$ is a field and $$V$$ is an $$\mathbb{F}$$-vector
space. Vectors are written as plain letters $$x, y, v, \dots$$ (the lecture
writes $$\vec{x}$$), the zero vector is $$\mathbf{0}$$, and $$W \le V$$ means
that $$W$$ is a subspace of $$V$$.

---

## §1.6 Bases and Dimension

> **Definition (Basis).** A subset $$\beta \subseteq V$$ is a **basis** of
> $$V$$ if $$\beta$$ spans $$V$$ and is linearly independent.
{: .definition #def-basis }

**Examples.**

- $$\varnothing$$ is a basis for $$V = \{\mathbf{0}\}$$.
- $$\varepsilon = \{e_1, e_2, \dots, e_n\}$$ is the **standard basis** for
  $$\mathbb{F}^n$$.
- $$\{E^{ij} : 1 \le i \le m,\ 1 \le j \le n\}$$ is a basis for
  $$\mathrm{Mat}_{m \times n}(\mathbb{F})$$, where $$E^{ij}$$ has a $$1$$ in
  position $$(i,j)$$ and zeros elsewhere.
- $$\{1, x, x^2, \dots, x^n\}$$ is the **standard basis** for
  $$P_n(\mathbb{F})$$, and the infinite set $$\{1, x, x^2, \dots\}$$ is a
  basis for $$P(\mathbb{F})$$.

> **Theorem 1.8.** Let $$\beta = \{u_1, u_2, \dots, u_n\} \subseteq V$$ with
> $$u_i \ne u_j$$ whenever $$i \ne j$$. Then $$\beta$$ is a basis for $$V$$
> if and only if every $$v \in V$$ can be expressed **uniquely** in the form
>
> $$v = a_1 u_1 + a_2 u_2 + \cdots + a_n u_n$$
>
> for some $$a_1, a_2, \dots, a_n \in \mathbb{F}$$.
{: .theorem #thm-1-8 }

*Proof.* ($$\Rightarrow$$) Such an expression exists because $$\beta$$ spans
$$V$$. If $$v = \sum a_i u_i = \sum b_i u_i$$, then
$$\sum (a_i - b_i) u_i = \mathbf{0}$$, and linear independence gives
$$a_i = b_i$$ for every $$i$$.

($$\Leftarrow$$) Existence of the expressions says that $$\beta$$ spans
$$V$$. The zero vector has the expression $$\sum 0 u_i$$, and by uniqueness
it has no other; so $$\beta$$ is linearly independent. $$\square$$

**Note.** For a basis $$\beta = \{u_1, \dots, u_n\}$$ taken in this order,
the theorem makes the map

$$
V \to \mathbb{F}^n, \qquad
v = a_1 u_1 + \cdots + a_n u_n \;\mapsto\;
[v]_\beta = \begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_n \end{pmatrix}
$$

a bijection. Ordered bases and the coordinate vector $$[v]_\beta$$ are taken
up in §2.2.

> **Theorem 1.9.** If $$\operatorname{span}(S) = V$$ for some **finite** set
> $$S \subseteq V$$, then some subset of $$S$$ is a basis for $$V$$. In
> particular $$V$$ has a finite basis.
{: .theorem #thm-1-9 }

*Proof.* If $$S = \varnothing$$ or $$S = \{\mathbf{0}\}$$, then
$$V = \{\mathbf{0}\}$$ and $$\varnothing \subseteq S$$ is a basis. Otherwise
$$S$$ contains a nonzero vector $$v_1$$, and $$\{v_1\}$$ is linearly
independent. Keep adjoining vectors of $$S$$ for as long as the set stays
linearly independent. Since $$S$$ is finite, this stops at a linearly
independent $$\beta = \{v_1, \dots, v_k\} \subseteq S$$ such that either
$$\beta = S$$ or adjoining any further vector of $$S$$ breaks linear
independence.

By [Theorem 1.7][thm-1-7], every $$v \in S \setminus \beta$$ lies in
$$\operatorname{span}(\beta)$$. So
$$S \subseteq \operatorname{span}(\beta) \le V$$, and
[Theorem 1.5][thm-1-5](b) gives
$$V = \operatorname{span}(S) \subseteq \operatorname{span}(\beta)$$. Thus
$$\beta$$ spans $$V$$ and is linearly independent. $$\square$$

**Example.** For $$S = \{(2,3), (0,0), (1,0), (0,1)\} \subseteq
\mathbb{R}^2$$ the procedure may keep $$(2,3)$$, must skip $$(0,0)$$, keeps
$$(1,0)$$, and must then skip $$(0,1)$$, giving the basis
$$\{(2,3), (1,0)\}$$. For an infinite spanning set the finite process is not
available; see [Problem 1.6.4](#prob-1-6-4) when $$V$$ is finite-dimensional
and [Theorem 1.12](#thm-1-12) with [Theorem 1.13](#thm-1-13) in general.

> **Theorem 1.10 (Replacement Theorem).** Let $$G \subseteq V$$ with
> $$\operatorname{span}(G) = V$$ and $$\lvert G \rvert = n$$, and let
> $$L \subseteq V$$ be linearly independent with $$\lvert L \rvert = m$$.
> Then
>
> - **(a)** $$m \le n$$;
> - **(b)** there exists $$H \subseteq G$$ such that
>   $$\lvert H \rvert = n - m$$ and
>   $$\operatorname{span}(L \cup H) = V$$.
{: .theorem #thm-1-10 }

*Proof.* By induction on $$m$$.

*Base case* $$m = 0$$. Then $$L = \varnothing$$, $$0 \le n$$, and $$H = G$$
works.

*Inductive step.* Assume the claim for $$m$$ and let
$$L = \{v_1, \dots, v_m, v_{m+1}\}$$ be linearly independent. The subset
$$\{v_1, \dots, v_m\}$$ is linearly independent by
[Theorem 1.6][thm-1-6](b), so the induction hypothesis gives $$m \le n$$
and a subset

$$
H = \{u_{m+1}, \dots, u_n\} \subseteq G \quad\text{with}\quad
\operatorname{span}\big(\{v_1, \dots, v_m\} \cup \{u_{m+1}, \dots, u_n\}\big)
= V .
$$

So we may write

$$
v_{m+1} = a_1 v_1 + \cdots + a_m v_m + b_{m+1} u_{m+1} + \cdots + b_n u_n .
$$

If $$m = n$$, or if every $$b_j = 0$$, this says
$$v_{m+1} \in \operatorname{span}\{v_1, \dots, v_m\}$$, and then $$L$$ is
linearly dependent by [Theorem 1.7][thm-1-7], a contradiction. Hence
$$m < n$$, which is $$m + 1 \le n$$, and some $$b_j \ne 0$$. Renumber so that
$$b_{m+1} \ne 0$$. Solving,

$$
u_{m+1} = b_{m+1}^{-1}\big(v_{m+1} - a_1 v_1 - \cdots - a_m v_m
- b_{m+2} u_{m+2} - \cdots - b_n u_n\big) .
$$

Put $$H' = \{u_{m+2}, \dots, u_n\}$$, a subset of $$G$$ with
$$n - (m + 1)$$ vectors. The display shows
$$u_{m+1} \in \operatorname{span}(L \cup H')$$, so

$$
\{v_1, \dots, v_m\} \cup \{u_{m+1}, \dots, u_n\}
\subseteq \operatorname{span}(L \cup H') ,
$$

and [Theorem 1.5][thm-1-5](b) gives
$$V \subseteq \operatorname{span}(L \cup H')$$. $$\square$$

In words: $$v_{m+1}$$ is inserted into the spanning set and one $$u_j$$ is
removed, without changing the span.

> **Corollary 1 to Theorem 1.10.** Suppose $$V$$ has a finite basis. Then
>
> - **(a)** every basis of $$V$$ is finite;
> - **(b)** every basis of $$V$$ has the same number of elements.
{: .theorem #cor-1-10-1 }

*Proof.* Let $$\beta$$ be a finite basis and $$\gamma$$ another basis.

(a) If $$\gamma$$ were infinite, it would have a finite subset $$\gamma'$$
with $$\lvert \beta \rvert + 1$$ elements. Then $$\gamma'$$ is linearly
independent by [Theorem 1.6][thm-1-6](b) and $$\beta$$ spans $$V$$, so
[Theorem 1.10](#thm-1-10)(a) gives
$$\lvert \gamma' \rvert \le \lvert \beta \rvert$$, a contradiction.

(b) $$\gamma$$ is linearly independent and $$\beta$$ spans, so
$$\lvert \gamma \rvert \le \lvert \beta \rvert$$ by
[Theorem 1.10](#thm-1-10)(a). Exchanging the roles,
$$\lvert \beta \rvert \le \lvert \gamma \rvert$$. $$\square$$

> **Definition (Dimension).** $$V$$ is **finite-dimensional** if it has a
> basis with finitely many elements. The number of elements of such a basis
> is the **dimension** of $$V$$, written $$\dim(V)$$. $$V$$ is
> **infinite-dimensional** if it is not finite-dimensional.
{: .definition #def-dimension }

The dimension is well defined by [Corollary 1](#cor-1-10-1)(b). By (a), a
space with an infinite basis has no finite basis.

**Examples.** $$\dim(\{\mathbf{0}\}) = 0$$, $$\dim(\mathbb{F}^n) = n$$,
$$\dim(\mathrm{Mat}_{m \times n}(\mathbb{F})) = mn$$,
$$\dim(P_n(\mathbb{F})) = n + 1$$ and $$\dim_{\mathbb{R}}(\mathbb{C}) = 2$$.
$$P(\mathbb{F})$$ is infinite-dimensional.

> **Corollary 2 to Theorem 1.10.** Let $$\dim(V) = n$$ and let
> $$G, L \subseteq V$$.
>
> - **(a)** If $$\operatorname{span}(G) = V$$ and $$G$$ is finite, then
>   $$\lvert G \rvert \ge n$$. Further, if $$\lvert G \rvert = n$$, then
>   $$G$$ is a basis.
> - **(b)** If $$L$$ is linearly independent and $$\lvert L \rvert = n$$,
>   then $$L$$ is a basis.
> - **(c)** **(Basis Extension Theorem)** If $$L$$ is linearly independent,
>   then there exists a basis of $$V$$ containing $$L$$.
{: .theorem #cor-1-10-2 }

*Proof.* Fix a basis $$\beta$$ of $$V$$; then $$\lvert \beta \rvert = n$$.

(a) By [Theorem 1.9](#thm-1-9) some $$H \subseteq G$$ is a basis, and
$$\lvert H \rvert = n$$ by [Corollary 1](#cor-1-10-1). So
$$\lvert G \rvert \ge \lvert H \rvert = n$$, and if
$$\lvert G \rvert = n$$ then $$G = H$$ is a basis.

(b) Apply [Theorem 1.10](#thm-1-10) with $$\beta$$ as the spanning set:
there is $$H \subseteq \beta$$ with
$$\lvert H \rvert = \lvert \beta \rvert - \lvert L \rvert = 0$$ and
$$\operatorname{span}(L \cup H) = V$$. So $$L$$ spans $$V$$.

(c) Every finite subset of $$L$$ is linearly independent, so it has at most
$$n$$ elements by [Theorem 1.10](#thm-1-10)(a); hence $$L$$ itself is finite
with $$\lvert L \rvert \le n$$. By [Theorem 1.10](#thm-1-10)(b) there is
$$H \subseteq \beta$$ with $$\lvert L \rvert + \lvert H \rvert = n$$ and
$$\operatorname{span}(L \cup H) = V$$. From (a),
$$n \le \lvert L \cup H \rvert$$. On the other hand
$$\lvert L \cup H \rvert \le \lvert L \rvert + \lvert H \rvert = n$$. So
$$\lvert L \cup H \rvert = n$$, and $$L \cup H$$ is a basis by (a) again.
$$\square$$

**Example.** $$\{(1,0), (1,1)\} \subseteq \mathbb{F}^2$$ is linearly
independent and has $$2 = \dim(\mathbb{F}^2)$$ elements, so it is a basis by
(b) with no need to check that it spans.

> **Theorem 1.11.** Let $$\dim V < \infty$$ and $$W \le V$$. Then
>
> - **(a)** $$\dim W < \infty$$;
> - **(b)** $$\dim W \le \dim V$$;
> - **(c)** if $$\dim W = \dim V$$, then $$W = V$$.
{: .theorem #thm-1-11 }

*Proof.* (a), (b) If $$W = \{\mathbf{0}\}$$, then
$$\dim W = 0 \le \dim V$$. Otherwise choose a nonzero $$v_1 \in W$$ and keep
adjoining vectors of $$W$$ for as long as the set stays linearly
independent. A linearly independent subset of $$V$$ has at most $$\dim V$$
elements by [Theorem 1.10](#thm-1-10)(a), so the process stops at a linearly
independent $$\{v_1, v_2, \dots, v_k\} \subseteq W$$ with
$$k \le \dim V$$ such that adjoining any further vector of $$W$$ breaks
linear independence. By [Theorem 1.7][thm-1-7],
$$\operatorname{span}\{v_1, \dots, v_k\} = W$$. So
$$\{v_1, \dots, v_k\}$$ is a basis of $$W$$ and $$\dim W = k \le \dim V$$.

(c) If $$\dim W = \dim V$$, a basis of $$W$$ is a linearly independent subset
of $$V$$ with $$\dim V$$ elements, hence a basis of $$V$$ by
[Corollary 2](#cor-1-10-2)(b). So $$W = V$$. $$\square$$

Conclusions such as (c), reached by counting basis vectors, are called
**dimension arguments**.

> **Corollary to Theorem 1.11 (Basis Extension Theorem).** Let
> $$\dim V < \infty$$ and $$W \le V$$. Then any basis of $$W$$ may be
> extended to a basis of $$V$$.
{: .theorem #cor-1-11 }

*Proof.* A basis of $$W$$ is a linearly independent subset of $$V$$, so
[Corollary 2](#cor-1-10-2)(c) applies. $$\square$$

**Example.** In $$\mathbb{F}^5$$ let

$$
W = \{(a_1, \dots, a_5) : a_1 + a_3 + a_5 = 0,\ a_2 = a_4\} .
$$

Choosing $$a_3, a_4, a_5$$ freely determines $$a_1 = -a_3 - a_5$$ and
$$a_2 = a_4$$, so

$$
\{(-1, 0, 1, 0, 0),\ (0, 1, 0, 1, 0),\ (-1, 0, 0, 0, 1)\}
$$

is a basis of $$W$$ and $$\dim W = 3$$.

### Problems for §1.6

> **Problem 1.6.1.** Let $$u$$ and $$v$$ be distinct vectors of a vector
> space $$V$$. Show that if $$\{u, v\}$$ is a basis for $$V$$ and $$a$$ and
> $$b$$ are nonzero scalars, then both $$\{u + v, au\}$$ and
> $$\{au, bv\}$$ are also bases for $$V$$.
{: .problem #prob-1-6-1 }

*Solution.* Since $$\{u, v\}$$ is a basis with two elements,
$$\dim V = 2$$. By [Corollary 2 to Theorem 1.10](#cor-1-10-2)(b) it is
enough to show that each set is a linearly independent set of two vectors.

For $$\{u + v, au\}$$: if $$c(u + v) + d(au) = \mathbf{0}$$, then
$$(c + da)u + cv = \mathbf{0}$$, so $$c = 0$$ and $$c + da = 0$$ by the
independence of $$\{u, v\}$$. Then $$da = 0$$, and $$d = 0$$ because
$$a \ne 0$$.

For $$\{au, bv\}$$: if $$c(au) + d(bv) = \mathbf{0}$$, then $$ca = 0$$ and
$$db = 0$$, so $$c = d = 0$$ because $$a, b \ne 0$$.

In both cases only the trivial combination vanishes, which also shows that
the two listed vectors are distinct. $$\square$$

> **Problem 1.6.2.** Let $$V$$ be a vector space and let
> $$u_1, u_2, \dots, u_n$$ be distinct vectors in $$V$$. Prove that if each
> $$v \in V$$ can be uniquely expressed as a linear combination of vectors of
> $$\beta = \{u_1, u_2, \dots, u_n\}$$, then $$\beta$$ is a basis for $$V$$.
{: .problem #prob-1-6-2 }

*Solution.* This is the direction ($$\Leftarrow$$) of
[Theorem 1.8](#thm-1-8). Every $$v$$ is a linear combination of vectors of
$$\beta$$, so $$\beta$$ spans $$V$$. If
$$a_1 u_1 + \cdots + a_n u_n = \mathbf{0}$$, compare with
$$0u_1 + \cdots + 0u_n = \mathbf{0}$$: uniqueness of the expression of
$$\mathbf{0}$$ forces every $$a_i = 0$$. So $$\beta$$ is linearly
independent. $$\square$$

> **Problem 1.6.3.** Prove that a vector space is infinite-dimensional if and
> only if it contains an infinite linearly independent subset.
{: .problem #prob-1-6-3 }

*Solution.* ($$\Leftarrow$$) By contraposition. If $$\dim V = n$$ is finite,
an infinite linearly independent subset would contain $$n + 1$$ vectors
forming a linearly independent set ([Theorem 1.6][thm-1-6](b)), while a
basis of $$n$$ vectors spans $$V$$. This contradicts
[Theorem 1.10](#thm-1-10)(a).

($$\Rightarrow$$) Let $$V$$ be infinite-dimensional, so that no finite subset
of $$V$$ is a basis. Build vectors $$v_1, v_2, \dots$$ one at a time.
Suppose a linearly independent $$\{v_1, \dots, v_k\}$$ has been chosen
(with $$k = 0$$ and the empty set to start). It is finite, so it is not a
basis, so it does not span $$V$$. Choose
$$v_{k+1} \notin \operatorname{span}\{v_1, \dots, v_k\}$$. Then
$$\{v_1, \dots, v_{k+1}\}$$ is linearly independent by
[Theorem 1.7][thm-1-7].

The set $$S = \{v_1, v_2, \dots\}$$ is infinite, because each $$v_{k+1}$$
differs from the earlier ones. Every finite subset of $$S$$ lies in some
$$\{v_1, \dots, v_k\}$$, so it is linearly independent by
[Theorem 1.6][thm-1-6](b). Hence $$S$$ is linearly independent by
[Problem 1.5.4][prob-1-5-4]. $$\square$$

> **Problem 1.6.4.** Let $$V$$ be a vector space having dimension $$n$$, and
> let $$S$$ be a subset of $$V$$ that generates $$V$$.
>
> - **(a)** Prove that there is a subset of $$S$$ that is a basis for $$V$$.
> - **(b)** Prove that $$S$$ contains at least $$n$$ vectors.
{: .problem #prob-1-6-4 }

$$S$$ may be infinite, so [Theorem 1.9](#thm-1-9) does not apply directly.
This is Exercise 1.6.20 of the textbook, which the lecture cites next to
Theorem 1.9.

*Solution.* (a) A basis of $$V$$ has $$n$$ vectors and spans $$V$$, so every
linearly independent subset of $$V$$ has at most $$n$$ elements by
[Theorem 1.10](#thm-1-10)(a). The linearly independent subsets of $$S$$
include $$\varnothing$$, so among them there is one, $$\beta$$, with the
largest number of elements.

Let $$v \in S \setminus \beta$$. The set $$\beta \cup \{v\} \subseteq S$$
has more elements than $$\beta$$, so it is linearly dependent, and
$$v \in \operatorname{span}(\beta)$$ by [Theorem 1.7][thm-1-7]. Therefore
$$S \subseteq \operatorname{span}(\beta)$$, and by
[Theorem 1.5][thm-1-5](b),
$$V = \operatorname{span}(S) \subseteq \operatorname{span}(\beta)$$. So
$$\beta \subseteq S$$ is a basis for $$V$$.

(b) The basis $$\beta \subseteq S$$ has exactly $$n$$ elements by
[Corollary 1 to Theorem 1.10](#cor-1-10-1). So $$S$$ contains at least
$$n$$ vectors. $$\square$$

> **Problem 1.6.5.** Prove that if $$W_1$$ and $$W_2$$ are finite-dimensional
> subspaces of a vector space $$V$$, then the subspace $$W_1 + W_2$$ is
> finite-dimensional and
>
> $$\dim(W_1 + W_2) = \dim(W_1) + \dim(W_2) - \dim(W_1 \cap W_2) .$$
{: .problem #prob-1-6-5 }

*Solution.* $$W_1 \cap W_2$$ is a subspace of the finite-dimensional space
$$W_1$$ ([Theorem 1.4][thm-1-4]), so it has a finite basis
$$\{u_1, \dots, u_k\}$$ by [Theorem 1.11](#thm-1-11). By the
[Corollary to Theorem 1.11](#cor-1-11), extend it to a basis of $$W_1$$ and
to a basis of $$W_2$$:

$$
\{u_1, \dots, u_k, v_1, \dots, v_m\} \text{ for } W_1, \qquad
\{u_1, \dots, u_k, w_1, \dots, w_p\} \text{ for } W_2 .
$$

Claim: $$\beta = \{u_1, \dots, u_k, v_1, \dots, v_m, w_1, \dots, w_p\}$$ is
a basis of $$W_1 + W_2$$ with $$k + m + p$$ elements.

*Spanning.* An element of $$W_1 + W_2$$ is $$x_1 + x_2$$ with $$x_1$$ a
combination of the $$u_i, v_j$$ and $$x_2$$ a combination of the
$$u_i, w_l$$; the sum is a combination of vectors of $$\beta$$.

*Independence.* Suppose

$$
\sum_i a_i u_i + \sum_j b_j v_j + \sum_l c_l w_l = \mathbf{0} .
$$

Then

$$
\sum_l c_l w_l = -\sum_i a_i u_i - \sum_j b_j v_j \in W_1 ,
$$

and the left side is in $$W_2$$, so it lies in $$W_1 \cap W_2$$ and equals
$$\sum_i d_i u_i$$ for some scalars $$d_i$$. Thus
$$\sum_l c_l w_l - \sum_i d_i u_i = \mathbf{0}$$, and the independence of
the basis of $$W_2$$ gives every $$c_l = 0$$. The original relation becomes
$$\sum_i a_i u_i + \sum_j b_j v_j = \mathbf{0}$$, and the independence of
the basis of $$W_1$$ gives every $$a_i = 0$$ and every $$b_j = 0$$. Since
only the trivial combination vanishes, the $$k + m + p$$ listed vectors are
distinct and linearly independent.

Hence $$W_1 + W_2$$ is finite-dimensional and

$$
\dim(W_1 + W_2) = k + m + p = (k + m) + (k + p) - k
= \dim(W_1) + \dim(W_2) - \dim(W_1 \cap W_2) .
$$

$$\square$$

> **Problem 1.6.6.** Let $$\beta_1$$ and $$\beta_2$$ be disjoint bases for
> subspaces $$W_1$$ and $$W_2$$, respectively, of a vector space $$V$$. Prove
> that if $$\beta_1 \cup \beta_2$$ is a basis for $$V$$, then
> $$V = W_1 \oplus W_2$$.
{: .problem #prob-1-6-6 }

The sheet prints $$\beta_1 \cap \beta_2$$, which is empty for disjoint
bases; the union is meant.

*Solution.* *Sum.* By [Problem 1.4.4][prob-1-4-4],

$$
V = \operatorname{span}(\beta_1 \cup \beta_2)
= \operatorname{span}(\beta_1) + \operatorname{span}(\beta_2)
= W_1 + W_2 .
$$

*Intersection.* $$\beta_1$$ and $$\beta_2$$ are disjoint linearly
independent sets whose union is linearly independent. By
[Problem 1.5.5][prob-1-5-5],

$$
W_1 \cap W_2 = \operatorname{span}(\beta_1) \cap \operatorname{span}(\beta_2)
= \{\mathbf{0}\} .
$$

Both conditions of the [direct sum][def-direct-sum] hold. $$\square$$

> **Problem 1.6.7.** Prove that if $$W_1$$ is any subspace of a
> finite-dimensional vector space $$V$$, then there exists a subspace
> $$W_2$$ of $$V$$ such that $$V = W_1 \oplus W_2$$.
{: .problem #prob-1-6-7 }

*Solution.* By [Theorem 1.11](#thm-1-11), $$W_1$$ has a finite basis
$$\beta_1$$, and by the [Corollary to Theorem 1.11](#cor-1-11) it extends to
a basis $$\beta \supseteq \beta_1$$ of $$V$$. Put
$$\beta_2 = \beta \setminus \beta_1$$ and
$$W_2 = \operatorname{span}(\beta_2)$$.

$$\beta_2$$ is linearly independent as a subset of $$\beta$$
([Theorem 1.6][thm-1-6](b)) and spans $$W_2$$, so it is a basis of
$$W_2$$. The bases $$\beta_1$$ and $$\beta_2$$ are disjoint and
$$\beta_1 \cup \beta_2 = \beta$$ is a basis for $$V$$. By
[Problem 1.6.6](#prob-1-6-6), $$V = W_1 \oplus W_2$$. $$\square$$

The complement $$W_2$$ is not unique: it depends on how $$\beta_1$$ is
extended.

---

## §1.7 Maximal Linearly Independent Subsets

> **Definition (Maximal member).** Let $$\mathcal{F}$$ be a family of sets.
> A member $$M$$ of $$\mathcal{F}$$ is **maximal** (with respect to set
> inclusion) if $$M$$ is contained in no other member of $$\mathcal{F}$$.
{: .definition #def-maximal }

Maximal means "nothing in the family is larger", not "larger than everything
in the family". A family can have many maximal members, or none.

**Note.** Any basis $$\beta$$ of $$V$$ is maximal among the linearly
independent subsets of $$V$$: every $$v \notin \beta$$ lies in
$$\operatorname{span}(\beta) = V$$, so $$\beta \cup \{v\}$$ is linearly
dependent by [Theorem 1.7][thm-1-7], and then so is every set strictly
containing $$\beta$$ ([Theorem 1.6][thm-1-6](a)).

> **Theorem 1.12.** Let $$S \subseteq V$$ with
> $$\operatorname{span}(S) = V$$. Any linearly independent
> $$\beta \subseteq S$$ that is maximal among the linearly independent
> subsets of $$S$$ is a basis for $$V$$.
{: .theorem #thm-1-12 }

*Proof.* Let $$v \in S \setminus \beta$$. Then $$\beta \cup \{v\}$$ is a
subset of $$S$$ strictly containing $$\beta$$, so by maximality it is
linearly dependent, and $$v \in \operatorname{span}(\beta)$$ by
[Theorem 1.7][thm-1-7]. Hence
$$S \subseteq \operatorname{span}(\beta)$$, and
[Theorem 1.5][thm-1-5](b) gives
$$V = \operatorname{span}(S) \subseteq \operatorname{span}(\beta)$$.
$$\square$$

> **Corollary to Theorem 1.12.** A subset of $$V$$ is a basis of $$V$$ if and
> only if it is a maximal linearly independent subset of $$V$$.
{: .theorem #cor-1-12 }

*Proof.* ($$\Rightarrow$$) is the Note above. ($$\Leftarrow$$) is
[Theorem 1.12](#thm-1-12) with $$S = V$$. $$\square$$

In a space that is not known to be finite-dimensional, the existence of a
maximal linearly independent subset needs a set-theoretic principle.

> **Definition (Chain).** A collection $$\mathcal{C}$$ of sets is a
> **chain** if for every $$A, B \in \mathcal{C}$$, either $$A \subseteq B$$
> or $$B \subseteq A$$.
{: .definition #def-chain }

> **Maximal Principle (Zorn's Lemma, for families of sets).** Let
> $$\mathcal{F}$$ be a family of sets. If for each chain
> $$\mathcal{C} \subseteq \mathcal{F}$$ there exists a member of
> $$\mathcal{F}$$ that contains each member of $$\mathcal{C}$$, then
> $$\mathcal{F}$$ contains a maximal member.
{: .theorem #maximal-principle }

The Maximal Principle is not proved from the other axioms of set theory; it
is equivalent to the Axiom of Choice and is taken as an assumption.

> **Theorem 1.13.** Let $$S \subseteq V$$ be linearly independent. Then there
> exists a maximal linearly independent subset of $$V$$ that contains $$S$$.
{: .theorem #thm-1-13 }

*Proof.* Let $$\mathcal{F}$$ be the family of all linearly independent
subsets of $$V$$ that contain $$S$$. Let $$\mathcal{C} \subseteq
\mathcal{F}$$ be a chain. If $$\mathcal{C}$$ is empty, $$S \in \mathcal{F}$$
contains each of its members. Otherwise let $$U$$ be the union of the
members of $$\mathcal{C}$$. Then $$U$$ contains each member of
$$\mathcal{C}$$ and contains $$S$$. It remains to see that $$U$$ is linearly
independent.

Let $$u_1, \dots, u_n$$ be distinct vectors of $$U$$. Each $$u_i$$ lies in
some member $$A_i$$ of $$\mathcal{C}$$. Because $$\mathcal{C}$$ is a chain,
one of $$A_1, \dots, A_n$$ contains all the others, say $$A_k$$. Then
$$u_1, \dots, u_n \in A_k$$, and $$A_k$$ is linearly independent, so
$$a_1 u_1 + \cdots + a_n u_n = \mathbf{0}$$ forces every $$a_i = 0$$. Hence
$$U \in \mathcal{F}$$.

By the [Maximal Principle](#maximal-principle), $$\mathcal{F}$$ has a
maximal member $$M$$. It contains $$S$$. If $$N \supseteq M$$ is a linearly
independent subset of $$V$$, then $$N \supseteq S$$, so
$$N \in \mathcal{F}$$ and $$N = M$$ by maximality. So $$M$$ is a maximal
linearly independent subset of $$V$$. $$\square$$

> **Corollary to Theorem 1.13.** Every vector space has a basis.
{: .theorem #cor-1-13 }

*Proof.* Apply [Theorem 1.13](#thm-1-13) to $$S = \varnothing$$ and then the
[Corollary to Theorem 1.12](#cor-1-12). $$\square$$

**Example.** $$\mathbb{R}$$ is a $$\mathbb{Q}$$-vector space, so it has a
basis over $$\mathbb{Q}$$, although none can be written down. It is also true
that any two bases of a vector space have the same cardinality, finite or
not.

### Problems for §1.7

> **Problem 1.7.1.** Let $$\beta$$ be a subset of an infinite-dimensional
> vector space $$V$$. Prove that $$\beta$$ is a basis for $$V$$ if and only
> if for each nonzero vector $$v$$ in $$V$$, there exist unique vectors
> $$u_1, u_2, \dots, u_n$$ in $$\beta$$ and unique nonzero scalars
> $$a_1, a_2, \dots, a_n$$ such that
>
> $$v = \sum_{i=1}^{n} a_i u_i .$$
{: .problem #prob-1-7-1 }

Here the $$u_i$$ are distinct, and uniqueness means: the set
$$\{u_1, \dots, u_n\}$$ and the coefficient attached to each of its vectors
are determined by $$v$$.

*Solution.* ($$\Rightarrow$$) *Existence.* $$\beta$$ spans $$V$$, so $$v$$
is a linear combination of distinct vectors of $$\beta$$. Delete the terms
with coefficient zero; at least one term remains because
$$v \ne \mathbf{0}$$.

*Uniqueness.* Suppose

$$
v = \sum_{i=1}^{n} a_i u_i = \sum_{j=1}^{m} b_j w_j
$$

with all $$a_i, b_j$$ nonzero, the $$u_i$$ distinct and the $$w_j$$
distinct. Let $$x_1, \dots, x_r$$ be the distinct vectors occurring among
the $$u_i$$ and $$w_j$$, and write both sums over all of them:
$$v = \sum_k a'_k x_k = \sum_k b'_k x_k$$, where $$a'_k$$ is the coefficient
of $$x_k$$ in the first sum, or $$0$$ if $$x_k$$ is not one of the $$u_i$$,
and similarly $$b'_k$$. Then $$\sum_k (a'_k - b'_k) x_k = \mathbf{0}$$, and
linear independence gives $$a'_k = b'_k$$ for all $$k$$. Since the original
coefficients are nonzero, $$x_k$$ is one of the $$u_i$$ exactly when
$$a'_k \ne 0$$, exactly when $$b'_k \ne 0$$, exactly when $$x_k$$ is one of
the $$w_j$$. So the two sets of vectors coincide and the coefficients agree.

($$\Leftarrow$$) *Spanning.* Every nonzero vector is a linear combination of
vectors of $$\beta$$ by hypothesis. $$V \ne \{\mathbf{0}\}$$ because it is
infinite-dimensional, so $$\beta \ne \varnothing$$ and
$$\mathbf{0} \in \operatorname{span}(\beta)$$ too.

*The zero vector is not in $$\beta$$.* Suppose $$\mathbf{0} \in \beta$$ and pick a
nonzero $$v$$ with its representation $$v = \sum a_i u_i$$. If
$$\mathbf{0}$$ is not among the $$u_i$$, then
$$v = \sum a_i u_i + 1 \cdot \mathbf{0}$$ is a second representation. If it
is among them, deleting that term gives a second representation (the term
cannot be the only one, since $$v \ne \mathbf{0}$$). Either way uniqueness
is violated.

*Independence.* Suppose a nontrivial representation
$$\sum_{i=1}^{n} a_i u_i = \mathbf{0}$$ exists with distinct
$$u_i \in \beta$$. Deleting zero terms, assume every $$a_i \ne 0$$ and
$$n \ge 1$$. If $$n = 1$$, then $$a_1 u_1 = \mathbf{0}$$ with
$$a_1 \ne 0$$ gives $$u_1 = \mathbf{0} \in \beta$$, which was excluded. If
$$n \ge 2$$, then

$$
u_1 = \sum_{i=2}^{n} (-a_1^{-1} a_i)\, u_i
$$

represents the nonzero vector $$u_1$$ with nonzero coefficients by the
vectors $$u_2, \dots, u_n$$, while $$u_1 = 1 u_1$$ represents it by the
single vector $$u_1$$. These are two different representations,
contradicting uniqueness. So $$\beta$$ is linearly independent, and it is a
basis. $$\square$$

> **Problem 1.7.2.** Prove the following. Let $$S_1$$ and $$S_2$$ be subsets
> of a vector space $$V$$ such that $$S_1 \subseteq S_2$$. If $$S_1$$ is
> linearly independent and $$S_2$$ generates $$V$$, then there exists a basis
> $$\beta$$ for $$V$$ such that $$S_1 \subseteq \beta \subseteq S_2$$.
{: .problem #prob-1-7-2 }

*Solution.* Let $$\mathcal{F}$$ be the family of all linearly independent
sets $$A$$ with $$S_1 \subseteq A \subseteq S_2$$. Let
$$\mathcal{C} \subseteq \mathcal{F}$$ be a chain. If $$\mathcal{C}$$ is
empty, $$S_1 \in \mathcal{F}$$ contains each of its members. Otherwise let
$$U$$ be the union of the members of $$\mathcal{C}$$. Then
$$S_1 \subseteq U \subseteq S_2$$, and $$U$$ is linearly independent by the
argument in the proof of [Theorem 1.13](#thm-1-13): finitely many vectors of
$$U$$ lie together in a single member of the chain. So
$$U \in \mathcal{F}$$ contains each member of $$\mathcal{C}$$.

By the [Maximal Principle](#maximal-principle), $$\mathcal{F}$$ has a
maximal member $$\beta$$, and $$S_1 \subseteq \beta \subseteq S_2$$. If
$$B$$ is linearly independent with $$\beta \subseteq B \subseteq S_2$$,
then $$S_1 \subseteq B$$, so $$B \in \mathcal{F}$$ and $$B = \beta$$. Thus
$$\beta$$ is maximal among the linearly independent subsets of $$S_2$$.
Since $$S_2$$ generates $$V$$, [Theorem 1.12](#thm-1-12) shows that
$$\beta$$ is a basis for $$V$$. $$\square$$

> **Problem 1.7.3.** Prove the following. Let $$\beta$$ be a basis for a
> vector space $$V$$, and let $$S$$ be a linearly independent subset of
> $$V$$. There exists a subset $$S_1$$ of $$\beta$$ such that
> $$S \cup S_1$$ is a basis for $$V$$.
{: .problem #prob-1-7-3 }

*Solution.* Apply [Problem 1.7.2](#prob-1-7-2) to the linearly independent
set $$S$$ and the set $$S \cup \beta$$, which contains $$S$$ and generates
$$V$$ because it contains the basis $$\beta$$
([Exercise 1.4.13][ex-1-4-13]). There is a basis $$\gamma$$ with

$$
S \subseteq \gamma \subseteq S \cup \beta .
$$

Put $$S_1 = \gamma \setminus S$$. Then $$S_1 \subseteq \beta$$ and
$$S \cup S_1 = \gamma$$ is a basis for $$V$$. $$\square$$

This is the Replacement Theorem without any finiteness: a linearly
independent set can be completed to a basis using vectors of a given basis.

---

## Quotient Spaces

A subspace $$W \le V$$ cuts $$V$$ into parallel copies of itself. Treating
each copy as a single point gives a new vector space, $$V/W$$.

### Cosets

> **Definition (Coset).** For $$W \le V$$ and $$v \in V$$, the set
>
> $$v + W = \{\, v + w : w \in W \,\}$$
>
> is the **coset** of $$W$$ containing $$v$$, and $$v$$ is a
> **representative** of the coset.
{: .definition #def-coset }

In the notation of the [sum of subsets][def-sum], $$v + W = \{v\} + W$$. The
coset contains $$v$$ because $$v = v + \mathbf{0}$$.

![The plane with a line W through the origin and two lines parallel to it; two arrows from the origin ending on the same parallel line differ by a vector along W](/assets/img/linear-algebra/cosets.svg)

In $$\mathbb{R}^2$$ with $$W$$ a line through the origin, the cosets of
$$W$$ are the lines parallel to $$W$$. Two vectors name the same coset
exactly when their difference is parallel to $$W$$.

> **Exercise 1.3.31 (Equality of cosets).** Let $$W \le V$$ and
> $$v_1, v_2 \in V$$. The following are equivalent.
>
> - **(i)** $$v_1 + W = v_2 + W$$.
> - **(ii)** $$v_1 \in v_2 + W$$; that is, $$v_1 = v_2 + w$$ for some
>   $$w \in W$$.
> - **(iii)** $$v_2 \in v_1 + W$$; that is, $$v_2 = v_1 + w$$ for some
>   $$w \in W$$.
> - **(iv)** $$v_1 - v_2 \in W$$ (equivalently, $$v_2 - v_1 \in W$$).
> - **(v)** $$(v_1 + W) \cap (v_2 + W) \ne \varnothing$$.
{: .theorem #ex-1-3-31 }

*Proof.* (ii) $$\Leftrightarrow$$ (iv): $$v_1 = v_2 + w$$ says
$$v_1 - v_2 = w$$. (iii) $$\Leftrightarrow$$ (iv): $$v_2 = v_1 + w$$ says
$$v_2 - v_1 = w$$, and $$v_2 - v_1 \in W$$ if and only if
$$v_1 - v_2 = -(v_2 - v_1) \in W$$.

(i) $$\Rightarrow$$ (ii): $$v_1 = v_1 + \mathbf{0} \in v_1 + W = v_2 + W$$.

(ii) $$\Rightarrow$$ (i): Suppose $$v_1 = v_2 + w_2$$ with $$w_2 \in W$$.
For any $$w \in W$$,

$$
v_1 + w = v_2 + (w_2 + w) \in v_2 + W ,
$$

so $$v_1 + W \subseteq v_2 + W$$. By the equivalences already shown, (iii)
holds as well, $$v_2 = v_1 + w_1$$, and the same argument gives the converse
inclusion.

(i) $$\Rightarrow$$ (v): $$v_1$$ lies in both cosets.

(v) $$\Rightarrow$$ (iv): If $$v_1 + w_1 = v_2 + w_2$$ with
$$w_1, w_2 \in W$$, then $$v_1 - v_2 = w_2 - w_1 \in W$$. $$\square$$

Two consequences. By (v), two cosets of $$W$$ are either equal or disjoint,
so the cosets partition $$V$$. And taking $$v_2 = \mathbf{0}$$ in (iv),
$$v + W = W$$ if and only if $$v \in W$$; a coset other than $$W$$ itself
does not contain $$\mathbf{0}$$ and is not a subspace.

### The quotient space

> **Definition (Quotient space).** Let $$W \le V$$. The set of all cosets of
> $$W$$,
>
> $$V/W = \{\, v + W : v \in V \,\} ,$$
>
> with the operations
>
> $$
> \begin{aligned}
> (x + W) + (y + W) &= (x + y) + W , \\
> c\,(x + W) &= cx + W ,
> \end{aligned}
> $$
>
> is an $$\mathbb{F}$$-vector space, the **quotient space** of $$V$$ modulo
> $$W$$.
{: .definition #def-quotient-space }

The operations are defined through representatives, and a coset has many
representatives. So the definition carries two claims that need proof: the
operations are **well defined**, and the eight axioms hold.

*Proof that the operations are well defined.* Suppose
$$x_1 + W = x_2 + W$$ and $$y_1 + W = y_2 + W$$. By
[Exercise 1.3.31](#ex-1-3-31), $$x_1 - x_2 \in W$$ and
$$y_1 - y_2 \in W$$. Then

$$
\begin{aligned}
(x_1 + y_1) - (x_2 + y_2) &= (x_1 - x_2) + (y_1 - y_2) \in W , \\
cx_1 - cx_2 &= c\,(x_1 - x_2) \in W ,
\end{aligned}
$$

because $$W$$ is a subspace. By [Exercise 1.3.31](#ex-1-3-31) again,

$$
(x_1 + y_1) + W = (x_2 + y_2) + W , \qquad cx_1 + W = cx_2 + W .
$$

So the results do not depend on the representatives chosen. $$\square$$

![Four parallel lines: W and the cosets of x, of y and of x plus y. The sum of two other representatives lands on the same line as x plus y](/assets/img/linear-algebra/coset-addition.svg)

*Proof of the axioms.* Each axiom for $$V/W$$ follows from the same axiom
for $$V$$ applied to representatives. For example, (VS1) and (VS7):

$$
\begin{aligned}
(x + W) + (y + W) &= (x + y) + W = (y + x) + W = (y + W) + (x + W) , \\
c\big((x + W) + (y + W)\big) &= c(x + y) + W = (cx + cy) + W
= c(x + W) + c(y + W) .
\end{aligned}
$$

The zero vector of $$V/W$$ is the coset $$\mathbf{0} + W = W$$, since
$$(x + W) + (\mathbf{0} + W) = x + W$$. The additive inverse of $$x + W$$ is
$$(-x) + W$$, since $$(x + W) + ((-x) + W) = \mathbf{0} + W$$. $$\square$$

A coset $$v + W$$ is the zero vector of $$V/W$$ exactly when $$v \in W$$.
Passing to $$V/W$$ sets every vector of $$W$$ to zero and identifies vectors
that differ by an element of $$W$$.

> **Exercise 1.6.35 (Basis and dimension of a quotient).** Let $$W \le V$$,
> let $$\{w_1, \dots, w_k\}$$ be a basis for $$W$$, and let
>
> $$\{w_1, \dots, w_k, v_{k+1}, \dots, v_n\}$$
>
> be a basis for $$V$$ extending it. Then
>
> $$\{\, v_{k+1} + W,\ \dots,\ v_n + W \,\}$$
>
> is a basis for $$V/W$$. Consequently, if $$\dim V < \infty$$, then
>
> $$\dim (V/W) = \dim V - \dim W .$$
{: .theorem #ex-1-6-35 }

*Proof.* *Spanning.* Let $$v + W \in V/W$$ and write
$$v = \sum_i a_i w_i + \sum_j b_j v_j$$. The vectors $$v$$ and
$$\sum_j b_j v_j$$ differ by $$\sum_i a_i w_i \in W$$, so by
[Exercise 1.3.31](#ex-1-3-31) and the definition of the operations,

$$
v + W = \Big(\sum_j b_j v_j\Big) + W = \sum_j b_j\,(v_j + W) .
$$

*Independence.* Suppose $$\sum_j b_j (v_j + W) = \mathbf{0} + W$$. The left
side is $$\big(\sum_j b_j v_j\big) + W$$, so
$$\sum_j b_j v_j \in W$$ and therefore
$$\sum_j b_j v_j = \sum_i a_i w_i$$ for some scalars $$a_i$$. Then

$$
\sum_i a_i w_i - \sum_j b_j v_j = \mathbf{0} ,
$$

and the linear independence of the basis of $$V$$ gives every
$$b_j = 0$$. In particular the $$n - k$$ listed cosets are distinct.

*Dimension.* If $$\dim V < \infty$$, then $$W$$ has a finite basis
([Theorem 1.11](#thm-1-11)) and it extends to a basis of $$V$$
([Corollary to Theorem 1.11](#cor-1-11)), so the first part applies and
$$\dim(V/W) = n - k$$. $$\square$$

### Linear maps on quotients

The remaining results concern linear maps, the subject of Chapter 2. The
definitions they need are these.

> **Definition (Linear map, kernel, image, isomorphism).** Let $$V$$ and
> $$W$$ be $$\mathbb{F}$$-vector spaces. A map $$T \colon V \to W$$ is
> **linear** if
>
> $$T(x + y) = T(x) + T(y) \quad\text{and}\quad T(cx) = c\,T(x)$$
>
> for all $$x, y \in V$$ and $$c \in \mathbb{F}$$. Its **kernel** and
> **image** are
>
> $$
> \ker T = \{\, v \in V : T(v) = \mathbf{0} \,\}, \qquad
> \operatorname{im} T = \{\, T(v) : v \in V \,\} .
> $$
>
> A linear map that is one-to-one and onto is an **isomorphism**.
{: .definition #def-linear-map }

A linear map sends $$\mathbf{0}$$ to $$\mathbf{0}$$, since
$$T(\mathbf{0}) = T(0 \cdot \mathbf{0}) = 0\,T(\mathbf{0}) = \mathbf{0}$$,
and satisfies $$T(x - y) = T(x) - T(y)$$. With
[Theorem 1.3][thm-1-3] it follows directly that $$\ker T \le V$$ and
$$\operatorname{im} T \le W$$. The kernel and image are also called the
null space $$N(T)$$ and the range $$R(T)$$.

> **Exercise 2.1.42 (The natural projection).** Let $$W \le V$$ and define
>
> $$\pi \colon V \to V/W, \qquad \pi(v) = v + W .$$
>
> - **(a)** $$\pi$$ is linear, $$\operatorname{im} \pi = V/W$$ and
>   $$\ker \pi = W$$.
> - **(b)** If $$\dim V < \infty$$, then
>   $$\dim (V/W) = \dim V - \dim W$$.
{: .theorem #ex-2-1-42 }

*Proof.* (a) Linearity is the definition of the operations on $$V/W$$:

$$
\pi(x + y) = (x + y) + W = (x + W) + (y + W) = \pi(x) + \pi(y), \qquad
\pi(cx) = cx + W = c\,\pi(x) .
$$

Every coset $$v + W$$ equals $$\pi(v)$$, so $$\pi$$ is onto. Finally
$$\pi(v) = \mathbf{0} + W$$ if and only if $$v \in W$$, by
[Exercise 1.3.31](#ex-1-3-31); so $$\ker \pi = W$$.

(b) This is the dimension count of [Exercise 1.6.35](#ex-1-6-35). It also
follows from (a) and the dimension theorem of Chapter 2,
$$\dim \operatorname{im} T + \dim \ker T = \dim V$$, applied to
$$T = \pi$$. $$\square$$

By (a), every subspace is the kernel of some linear map.

> **First Isomorphism Theorem.** Let $$T \colon V \to W$$ be linear.
>
> - **(a)** The map
>   $$\overline{T} \colon V/\ker T \to W$$ given by
>   $$\overline{T}(v + \ker T) = T(v)$$ is well defined.
> - **(b)** $$\overline{T}$$ is linear.
> - **(c)** $$\overline{T} \colon V/\ker T \to \operatorname{im} T$$ is an
>   isomorphism.
{: .theorem #thm-first-isomorphism }

*Proof.* Write $$K = \ker T$$.

(a) If $$v_1 + K = v_2 + K$$, then $$v_1 - v_2 \in K$$ by
[Exercise 1.3.31](#ex-1-3-31), so
$$T(v_1) - T(v_2) = T(v_1 - v_2) = \mathbf{0}$$. The value $$T(v)$$ depends
only on the coset of $$v$$.

(b) By the definition of the operations on $$V/K$$ and the linearity of
$$T$$,

$$
\begin{aligned}
\overline{T}\big((x + K) + (y + K)\big) &= \overline{T}\big((x + y) + K\big)
= T(x + y) = T(x) + T(y) \\
&= \overline{T}(x + K) + \overline{T}(y + K) , \\
\overline{T}\big(c\,(x + K)\big) &= \overline{T}(cx + K) = T(cx) = c\,T(x)
= c\,\overline{T}(x + K) .
\end{aligned}
$$

(c) The values of $$\overline{T}$$ are exactly the vectors $$T(v)$$, so
$$\overline{T}$$ maps onto $$\operatorname{im} T$$. If
$$\overline{T}(v_1 + K) = \overline{T}(v_2 + K)$$, then
$$T(v_1 - v_2) = \mathbf{0}$$, so $$v_1 - v_2 \in K$$ and
$$v_1 + K = v_2 + K$$ by [Exercise 1.3.31](#ex-1-3-31). So
$$\overline{T}$$ is one-to-one. $$\square$$

By construction $$T = \overline{T} \circ \pi$$, where
$$\pi \colon V \to V/\ker T$$ is the
[natural projection](#ex-2-1-42): every linear map is a projection onto a
quotient followed by an isomorphism onto its image. When
$$\dim V < \infty$$, comparing dimensions through (c) and
[Exercise 1.6.35](#ex-1-6-35) gives

$$
\dim V - \dim \ker T = \dim \operatorname{im} T ,
$$

the dimension theorem.

![Two commutative diagrams: a triangle in which T equals T bar after the projection pi onto V over ker T, and a square in which pi after T equals T bar after pi on V over W](/assets/img/linear-algebra/quotient-diagrams.svg)

> **Definition (Invariant subspace).** Let $$T \colon V \to V$$ be linear. A
> subspace $$W \le V$$ is **$$T$$-invariant** if $$T(w) \in W$$ for every
> $$w \in W$$.
{: .definition #def-invariant-subspace }

> **Exercise 5.4.27 (The map induced on a quotient).** Let
> $$T \colon V \to V$$ be linear and let $$W \le V$$ be $$T$$-invariant.
>
> - **(a)** The map $$\overline{T} \colon V/W \to V/W$$ given by
>   $$\overline{T}(v + W) = T(v) + W$$ is well defined.
> - **(b)** $$\overline{T}$$ is linear.
{: .theorem #ex-5-4-27 }

*Proof.* (a) If $$v_1 + W = v_2 + W$$, then $$v_1 - v_2 \in W$$, so
$$T(v_1) - T(v_2) = T(v_1 - v_2) \in W$$ because $$W$$ is
$$T$$-invariant. Hence $$T(v_1) + W = T(v_2) + W$$ by
[Exercise 1.3.31](#ex-1-3-31).

(b) As in the previous proof,

$$
\begin{aligned}
\overline{T}\big((x + W) + (y + W)\big) &= T(x + y) + W
= (T(x) + W) + (T(y) + W) \\
&= \overline{T}(x + W) + \overline{T}(y + W) , \\
\overline{T}\big(c\,(x + W)\big) &= T(cx) + W = c\,(T(x) + W)
= c\,\overline{T}(x + W) .
\end{aligned}
$$

$$\square$$

By definition $$\pi \circ T = \overline{T} \circ \pi$$, which is the square
in the figure. When $$V$$ is finite-dimensional and
$$\{\mathbf{0}\} \ne W \ne V$$, both $$W$$ and $$V/W$$ have smaller
dimension than $$V$$, so a statement about $$T$$ can be reduced to
statements about $$T$$ restricted to $$W$$ and about $$\overline{T}$$. This
is what makes quotient spaces a tool for induction on the dimension.

---

## References

- Stephen H. Friedberg, Arnold J. Insel and Lawrence E. Spence, *Linear
  Algebra*, 5th edition, Pearson, 2018 — Chapter 1, §§1.6 and 1.7, and the
  exercises cited by number.
- Linear Algebra (881.007), Seoul National University, Fall 2023.
  Instructor: Jin Hong (홍진). Lecture slides for Chapter 1 and for quotient
  spaces, and the course problem sheet for Chapter 1.
- The definitions, the statements of the theorems and their numbering are
  the slides'. The slides give most proofs as outlines, and the proofs here
  fill in those outlines. Where the slides state a result without proof, as
  with Theorems 1.8 and 1.13, the proof is written out here.
- The chain and the Maximal Principle are stated as in the textbook; the
  slides refer to them only as Zorn's Lemma and the Axiom of Choice.
- The slides label the First Isomorphism Theorem with a repeated exercise
  number, so it appears here under its usual name instead.
- The solutions to the problems are mine. Problem 1.6.6 is solved in a
  corrected form, and the correction is stated at the problem.

[thm-1-7]: /posts/linear-algebra-vector-spaces/#thm-1-7
[thm-1-5]: /posts/linear-algebra-vector-spaces/#thm-1-5
[thm-1-6]: /posts/linear-algebra-vector-spaces/#thm-1-6
[prob-1-5-4]: /posts/linear-algebra-vector-spaces/#prob-1-5-4
[thm-1-4]: /posts/linear-algebra-vector-spaces/#thm-1-4
[prob-1-4-4]: /posts/linear-algebra-vector-spaces/#prob-1-4-4
[prob-1-5-5]: /posts/linear-algebra-vector-spaces/#prob-1-5-5
[def-direct-sum]: /posts/linear-algebra-vector-spaces/#def-direct-sum
[ex-1-4-13]: /posts/linear-algebra-vector-spaces/#ex-1-4-13
[def-sum]: /posts/linear-algebra-vector-spaces/#def-sum
[thm-1-3]: /posts/linear-algebra-vector-spaces/#thm-1-3
