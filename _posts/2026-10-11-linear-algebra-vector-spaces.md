---
title: "Linear Algebra: Vector Spaces (Part 1)"
date: 2026-10-11 00:30:00 +0900
categories: [Course Notes, Linear Algebra]
tags: [vector spaces, subspaces, span, linear independence]
description: Definitions, theorems with proofs, and solved problems for Chapter 1 of Linear Algebra, §1.1 to §1.5 — fields, vector spaces, subspaces, span, and linear dependence and independence.
math: true
mermaid: false
render_with_liquid: false
---

> **How to read the labels.** Definitions, theorems and their numbers follow
> the lecture slides, which follow the textbook (Friedberg, Insel and Spence,
> 5th edition). A result labelled **Exercise a.b.c** is a textbook exercise
> that the lecture stated and used as a theorem; the number is the textbook's.
> A **Problem a.b.k** is the $$k$$-th question for §a.b on the course problem
> sheet, which does not number its questions. Chapter 1 is split over two
> posts: this one covers §1.1 to §1.5, and
> [Part 2](/posts/linear-algebra-vector-spaces-2/) covers §1.6, §1.7 and
> quotient spaces.
{: .prompt-info }

Throughout, $$\mathbb{F}$$ is a field and $$V$$ is an $$\mathbb{F}$$-vector
space. Vectors are written as plain letters $$x, y, v, \dots$$ (the lecture
writes $$\vec{x}$$), the zero vector is $$\mathbf{0}$$, and $$W \le V$$ means
that $$W$$ is a subspace of $$V$$.

---

## §1.1 Fields

The scalars of a vector space come from a field: a number system in which the
four arithmetic operations work as they do for rational numbers.

> **Definition (Field).** A **field** is a set $$\mathbb{F}$$ with two
> operations, addition and multiplication, such that for all
> $$a, b, c \in \mathbb{F}$$:
>
> - **(F1)** $$a + b = b + a$$ and $$ab = ba$$.
> - **(F2)** $$(a + b) + c = a + (b + c)$$ and $$(ab)c = a(bc)$$.
> - **(F3)** There are distinct elements $$0$$ and $$1$$ in $$\mathbb{F}$$
>   with $$0 + a = a$$ and $$1a = a$$.
> - **(F4)** Each $$a$$ has an **additive inverse** $$-a$$, with
>   $$a + (-a) = 0$$, and each $$b \ne 0$$ has a **multiplicative inverse**
>   $$b^{-1}$$, with $$b\,b^{-1} = 1$$.
> - **(F5)** $$a(b + c) = ab + ac$$.
{: .definition #def-field }

Subtraction is addition of the additive inverse, $$a - b = a + (-b)$$, and
division is multiplication by the multiplicative inverse,
$$a \div b = a\,b^{-1}$$.

**Examples.**

- $$\mathbb{Q}$$, $$\mathbb{R}$$ and $$\mathbb{C}$$ are fields.
- $$\mathbb{Z}$$ is not a field: $$2$$ has no multiplicative inverse in
  $$\mathbb{Z}$$.
- $$\mathbb{Z}_5 = \{0, 1, 2, 3, 4\}$$ with addition and multiplication modulo
  $$5$$ is a field. The multiplicative inverses are $$1 \cdot 1 = 1$$,
  $$2 \cdot 3 = 1$$, $$3 \cdot 2 = 1$$ and $$4 \cdot 4 = 1$$.
- $$\mathbb{Z}_6$$ with the operations modulo $$6$$ is not a field: $$2x$$ is
  one of $$0, 2, 4$$ for every $$x$$, so $$2x = 1$$ has no solution.

> **Definition (Characteristic of a field).** The **characteristic** of
> $$\mathbb{F}$$ is the smallest positive integer $$p$$ for which the sum of
> $$p$$ ones is zero,
>
> $$\underbrace{1 + 1 + \cdots + 1}_{p} = 0 ,$$
>
> and is **zero** if there is no such $$p$$.
{: .definition #def-characteristic }

$$\mathbb{Q}$$, $$\mathbb{R}$$ and $$\mathbb{C}$$ have characteristic zero and
$$\mathbb{Z}_5$$ has characteristic five. In a field of characteristic two,
$$1 + 1 = 0$$, so $$a + a = 0$$ and $$-a = a$$ for every $$a$$. In a field
whose characteristic is not two, the element $$2 = 1 + 1$$ is nonzero and can
be divided by.

---

## §1.2 Vector Spaces

Addition and scalar multiplication in $$\mathbb{R}^n$$ satisfy eight
identities. A vector space is any set with two operations that satisfy the
same eight.

> **Definition (Vector space).** Let $$\mathbb{F}$$ be a field, let $$V$$ be
> a set, and let there be two maps
>
> $$
> \begin{aligned}
> + &\colon V \times V \to V, & (x, y) &\mapsto x + y, \\
> \cdot\; &\colon \mathbb{F} \times V \to V, & (a, x) &\mapsto ax .
> \end{aligned}
> $$
>
> The structure $$\langle V, +, \cdot \rangle$$ is an
> **$$\mathbb{F}$$-vector space** (a **vector space over $$\mathbb{F}$$**) if:
>
> - **(VS1)** $$x + y = y + x$$ for all $$x, y \in V$$.
> - **(VS2)** $$(x + y) + z = x + (y + z)$$ for all $$x, y, z \in V$$.
> - **(VS3)** There exists $$\mathbf{0} \in V$$ such that
>   $$x + \mathbf{0} = x$$ for all $$x \in V$$.
> - **(VS4)** For each $$x \in V$$ there exists $$x' \in V$$ such that
>   $$x + x' = \mathbf{0}$$.
> - **(VS5)** $$1x = x$$ for all $$x \in V$$.
> - **(VS6)** $$a(bx) = (ab)x$$ for all $$a, b \in \mathbb{F}$$ and
>   $$x \in V$$.
> - **(VS7)** $$a(x + y) = ax + ay$$ for all $$a \in \mathbb{F}$$ and
>   $$x, y \in V$$.
> - **(VS8)** $$(a + b)x = ax + bx$$ for all $$a, b \in \mathbb{F}$$ and
>   $$x \in V$$.
>
> Elements of $$V$$ are **vectors** and elements of $$\mathbb{F}$$ are
> **scalars**.
{: .definition #def-vector-space }

The order of the quantifiers separates (VS3) from (VS4). In (VS3) one vector
$$\mathbf{0}$$ serves every $$x$$ at once. In (VS4) the vector $$x'$$ is
chosen after $$x$$ and depends on it.

**Examples.**

- **$$\mathbb{F}^n$$**, the set of columns with $$n$$ entries from
  $$\mathbb{F}$$, with coordinatewise addition and scalar multiplication, is
  an $$\mathbb{F}$$-vector space. So $$\mathbb{R}^n$$ is an
  $$\mathbb{R}$$-vector space, $$\mathbb{C}^n$$ a $$\mathbb{C}$$-vector space
  and $$\mathbb{Q}^n$$ a $$\mathbb{Q}$$-vector space.
- $$\mathbb{C}^n$$ with the same addition, and scalar multiplication only by
  real numbers, is an $$\mathbb{R}$$-vector space. The field is part of the
  structure.
- **$$\mathrm{Mat}_{m \times n}(\mathbb{F})$$**, the $$m \times n$$ matrices
  with entries from $$\mathbb{F}$$, with $$(A + B)_{ij} = a_{ij} + b_{ij}$$
  and $$(tA)_{ij} = t\,a_{ij}$$.
- **$$\mathcal{F}(S, \mathbb{F})$$**, the functions $$f \colon S \to
  \mathbb{F}$$ on any set $$S$$, with $$(f + g)(s) = f(s) + g(s)$$ and
  $$(cf)(s) = c\,f(s)$$.
- **$$P(\mathbb{F})$$**, the polynomials with coefficients in $$\mathbb{F}$$,
  with the usual addition and multiplication by a scalar. The product of two
  polynomials is not part of the vector space structure.
- $$\mathbb{R}$$ is a $$\mathbb{Q}$$-vector space.
- $$\mathbb{R}_{>0} = \{x \in \mathbb{R} : x > 0\}$$ with "addition"
  $$x \oplus y = xy$$ and "scalar multiplication" $$c \odot x = x^{c}$$ for
  $$c \in \mathbb{R}$$ is an $$\mathbb{R}$$-vector space. Its zero vector is
  the number $$1$$, and the vector $$x'$$ of (VS4) is $$1/x$$.

> **Theorem 1.1 (Cancellation Law for Vector Addition).** If
> $$x, y, z \in V$$ and $$x + z = y + z$$, then $$x = y$$.
{: .theorem #thm-1-1 }

*Proof.* By (VS4) there is $$z' \in V$$ with $$z + z' = \mathbf{0}$$. Then

$$
\begin{aligned}
(x + z) + z' &= (y + z) + z' \\
x + (z + z') &= y + (z + z') && \text{(VS2)} \\
x + \mathbf{0} &= y + \mathbf{0} && \text{(VS4)} \\
x &= y && \text{(VS3)}
\end{aligned}
$$

$$\square$$

By (VS1) the law also holds in the form $$z + x = z + y \Rightarrow x = y$$.
Cancellation is a property of vector addition, not of every operation: in
$$\mathbb{Z}_6$$, $$1 \cdot 2 = 4 \cdot 2$$ although $$1 \ne 4$$.

> **Corollary 1 to Theorem 1.1 (Uniqueness of the zero vector).** The vector
> $$\mathbf{0}$$ of (VS3) is unique.
{: .theorem #cor-1-1-1 }

*Proof.* Suppose $$\mathbf{0}_1$$ and $$\mathbf{0}_2$$ both satisfy (VS3).
Then $$\mathbf{0}_2 + \mathbf{0}_1 = \mathbf{0}_2$$ and
$$\mathbf{0}_1 + \mathbf{0}_2 = \mathbf{0}_1$$, and the two left sides are
equal by (VS1). Hence $$\mathbf{0}_1 = \mathbf{0}_2$$. $$\square$$

> **Corollary 2 to Theorem 1.1 (Uniqueness of the additive inverse).** The
> vector $$x'$$ of (VS4) is uniquely determined by $$x$$.
{: .theorem #cor-1-1-2 }

*Proof.* If $$x_1$$ and $$x_2$$ both qualify as the $$x'$$ of (VS4), then

$$
x_1 + x = x + x_1 = \mathbf{0} = x + x_2 = x_2 + x ,
$$

and [Theorem 1.1](#thm-1-1) gives $$x_1 = x_2$$. $$\square$$

The unique vector of (VS3) is the **zero vector** $$\mathbf{0}$$. The unique
vector $$x'$$ of (VS4) is the **additive inverse** of $$x$$, written $$-x$$,
and $$x - y$$ means $$x + (-y)$$.

> **Theorem 1.2.** For each $$x \in V$$ and each $$a \in \mathbb{F}$$:
>
> - **(1)** $$0x = \mathbf{0}$$.
> - **(2)** $$(-a)x = -(ax) = a(-x)$$.
> - **(3)** $$a\mathbf{0} = \mathbf{0}$$.
{: .theorem #thm-1-2 }

*Proof.* (1) By (VS3), (VS1) and (VS8),

$$
\mathbf{0} + 0x = 0x = (0 + 0)x = 0x + 0x ,
$$

so $$\mathbf{0} = 0x$$ by [Theorem 1.1](#thm-1-1).

(3) By (VS3), (VS1) and (VS7),

$$
\mathbf{0} + a\mathbf{0} = a\mathbf{0} = a(\mathbf{0} + \mathbf{0})
= a\mathbf{0} + a\mathbf{0} ,
$$

so $$\mathbf{0} = a\mathbf{0}$$ by [Theorem 1.1](#thm-1-1).

(2) By (VS8) and part (1),

$$
ax + (-a)x = (a + (-a))x = 0x = \mathbf{0} ,
$$

so $$(-a)x$$ is the additive inverse of $$ax$$ by
[Corollary 2](#cor-1-1-2): $$(-a)x = -(ax)$$. By (VS7) and part (3),

$$
ax + a(-x) = a(x + (-x)) = a\mathbf{0} = \mathbf{0} ,
$$

so $$a(-x) = -(ax)$$ as well. $$\square$$

With $$a = 1$$, part (2) reads $$(-1)x = -x$$.

### Problems for §1.2

> **Problem 1.2.1.** Prove the following propositions.
>
> - **(a)** The zero vector $$\mathbf{0}$$ that satisfies (VS3) is unique.
> - **(b)** The inverse vector $$y$$ that satisfies (VS4) is unique for a
>   vector $$x$$.
> - **(c)** For every scalar $$a \in \mathbb{F}$$, $$a\mathbf{0} = \mathbf{0}$$.
{: .problem #prob-1-2-1 }

*Solution.* (a) This is [Corollary 1 to Theorem 1.1](#cor-1-1-1). If
$$\mathbf{0}_1$$ and $$\mathbf{0}_2$$ both satisfy (VS3), then

$$
\mathbf{0}_1 = \mathbf{0}_1 + \mathbf{0}_2 = \mathbf{0}_2 + \mathbf{0}_1
= \mathbf{0}_2 ,
$$

using (VS3) for $$\mathbf{0}_2$$, then (VS1), then (VS3) for
$$\mathbf{0}_1$$.

(b) This is [Corollary 2 to Theorem 1.1](#cor-1-1-2). If
$$x + y_1 = \mathbf{0}$$ and $$x + y_2 = \mathbf{0}$$, then

$$
y_1 = y_1 + \mathbf{0} = y_1 + (x + y_2) = (y_1 + x) + y_2
= \mathbf{0} + y_2 = y_2 ,
$$

using (VS3), the choice of $$y_2$$, (VS2), then (VS1) with the choice of
$$y_1$$, and finally (VS1) with (VS3).

(c) This is [Theorem 1.2](#thm-1-2)(3):
$$\mathbf{0} + a\mathbf{0} = a\mathbf{0} = a(\mathbf{0} + \mathbf{0}) =
a\mathbf{0} + a\mathbf{0}$$, and cancelling $$a\mathbf{0}$$ by
[Theorem 1.1](#thm-1-1) leaves $$\mathbf{0} = a\mathbf{0}$$. $$\square$$

> **Problem 1.2.2.** Let $$V = \{(a_1, a_2, \dots, a_n) : a_i \in
> \mathbb{R},\ i = 1, 2, \dots, n\}$$, with the operations of
> $$\mathbb{F}^n$$ (coordinatewise addition and coordinatewise multiplication
> by a scalar). Is $$V$$ a $$\mathbb{C}$$-vector space?
{: .problem #prob-1-2-2 }

*Solution.* No. A $$\mathbb{C}$$-vector space needs a scalar multiplication
$$\mathbb{C} \times V \to V$$, and coordinatewise multiplication does not map
into $$V$$:

$$
i\,(1, 0, \dots, 0) = (i, 0, \dots, 0) \notin V ,
$$

because $$i \notin \mathbb{R}$$. So $$V$$ is not closed under multiplication
by complex scalars and the definition fails before any of (VS1) to (VS8) is
examined. With real scalars the same set is the $$\mathbb{R}$$-vector space
$$\mathbb{R}^n$$. $$\square$$

---

## §1.3 Subspaces

> **Definition (Subspace).** A subset $$W \subseteq V$$ is a **subspace** of
> $$V$$, written $$W \le V$$, if $$W$$ is an $$\mathbb{F}$$-vector space with
> the operations defined on $$V$$.
{: .definition #def-subspace }

The operations of $$V$$ restrict to maps $$W \times W \to V$$ and
$$\mathbb{F} \times W \to V$$. For $$W$$ to be a vector space these must land
in $$W$$: the subset must be **closed** under both operations.

**Examples.** $$V \le V$$, and $$\{\mathbf{0}\} \le V$$, the **zero
subspace**. The $$\mathbb{R}$$-vector space $$\mathbb{R}_{>0}$$ of §1.2 is a
subset of $$\mathbb{R}^1$$ but not a subspace of it, because its operations
are not those of $$\mathbb{R}^1$$.

> **Theorem 1.3.** Let $$W \subseteq V$$. Then
> $$W \le V$$ if and only if
>
> - **(a)** $$\mathbf{0} \in W$$;
> - **(b)** $$x + y \in W$$ whenever $$x, y \in W$$;
> - **(c)** $$cx \in W$$ whenever $$c \in \mathbb{F}$$ and $$x \in W$$.
{: .theorem #thm-1-3 }

*Proof.* ($$\Rightarrow$$) If $$W$$ is a vector space under the operations of
$$V$$, those operations map into $$W$$, which is (b) and (c). Let
$$\mathbf{0}_W$$ be the zero vector of $$W$$ and $$\mathbf{0}_V$$ that of
$$V$$. Then

$$
\mathbf{0}_V + \mathbf{0}_W = \mathbf{0}_W + \mathbf{0}_V = \mathbf{0}_W
= \mathbf{0}_W + \mathbf{0}_W ,
$$

where the first two equalities are (VS1) and (VS3) in $$V$$ and the last is
(VS3) in $$W$$. By [Theorem 1.1](#thm-1-1) in $$V$$,
$$\mathbf{0}_V = \mathbf{0}_W \in W$$, which is (a).

($$\Leftarrow$$) By (b) and (c) the operations of $$V$$ restrict to
operations on $$W$$. (VS1), (VS2) and (VS5) to (VS8) hold for all vectors of
$$V$$, so they hold for the vectors of $$W$$. (VS3) holds in $$W$$ because
$$\mathbf{0} \in W$$ by (a). For (VS4), if $$x \in W$$ then
$$-x = (-1)x \in W$$ by [Theorem 1.2](#thm-1-2)(2) and (c). $$\square$$

Condition (a) may be replaced by $$W \ne \varnothing$$; see
[Problem 1.3.1](#prob-1-3-1).

**Examples.**

- The **symmetric** matrices, those with $$A^t = A$$ where
  $$(A^t)_{ij} = A_{ji}$$, form a subspace of
  $$\mathrm{Mat}_{n \times n}(\mathbb{F})$$.
- The matrices with positive entries do **not** form a subspace of
  $$\mathrm{Mat}_{m \times n}(\mathbb{R})$$: the zero matrix is missing.
- $$P_n(\mathbb{F})$$, the polynomials of degree at most $$n$$ together with
  the zero polynomial, is a subspace of $$P(\mathbb{F})$$.
- The continuous functions form a subspace of
  $$\mathcal{F}(\mathbb{R}, \mathbb{R})$$.
- $$W_1, W_2 \le V$$ does **not** imply $$W_1 \cup W_2 \le V$$. The two
  coordinate axes of $$\mathbb{R}^2$$ are subspaces, and their union contains
  $$(1,0)$$ and $$(0,1)$$ but not the sum $$(1,1)$$. See
  [Problem 1.3.2](#prob-1-3-2).

> **Theorem 1.4.** If $$W_i \le V$$ for each $$i$$ in an index set $$I$$,
> then
>
> $$\bigcap_{i \in I} W_i \le V .$$
{: .theorem #thm-1-4 }

*Proof.* Write $$W = \bigcap_{i \in I} W_i$$ and check
[Theorem 1.3](#thm-1-3). (a) $$\mathbf{0} \in W_i$$ for every $$i$$, so
$$\mathbf{0} \in W$$. (b) If $$x, y \in W$$, then $$x, y \in W_i$$ for every
$$i$$, so $$x + y \in W_i$$ for every $$i$$, so $$x + y \in W$$. (c) In the
same way $$cx \in W_i$$ for every $$i$$, so $$cx \in W$$. $$\square$$

> **Definition (Sum of subsets).** For nonempty $$S_1, S_2 \subseteq V$$,
> their **sum** is the set
>
> $$S_1 + S_2 = \{\, x_1 + x_2 : x_1 \in S_1,\ x_2 \in S_2 \,\} .$$
{: .definition #def-sum }

> **Exercise 1.3.23.** Let $$W_1, W_2 \le V$$.
>
> - **(a)** $$W_1 + W_2$$ is a subspace of $$V$$ that contains both $$W_1$$
>   and $$W_2$$.
> - **(b)** If $$W \le V$$ and $$W_1, W_2 \subseteq W$$, then
>   $$W_1 + W_2 \le W$$.
>
> So $$W_1 + W_2$$ is the smallest subspace of $$V$$ containing $$W_1$$ and
> $$W_2$$.
{: .theorem #ex-1-3-23 }

*Proof.* (a) For $$w_1 \in W_1$$, $$w_1 = w_1 + \mathbf{0} \in W_1 + W_2$$
because $$\mathbf{0} \in W_2$$; so $$W_1 \subseteq W_1 + W_2$$, and likewise
$$W_2 \subseteq W_1 + W_2$$. For [Theorem 1.3](#thm-1-3):
$$\mathbf{0} = \mathbf{0} + \mathbf{0} \in W_1 + W_2$$, and for
$$x_1, y_1 \in W_1$$, $$x_2, y_2 \in W_2$$ and $$c \in \mathbb{F}$$,

$$
\begin{aligned}
(x_1 + x_2) + (y_1 + y_2) &= (x_1 + y_1) + (x_2 + y_2) \in W_1 + W_2 , \\
c(x_1 + x_2) &= cx_1 + cx_2 \in W_1 + W_2 .
\end{aligned}
$$

(b) If $$x_1 \in W_1 \subseteq W$$ and $$x_2 \in W_2 \subseteq W$$, then
$$x_1 + x_2 \in W$$ because $$W$$ is closed under addition. So
$$W_1 + W_2 \subseteq W$$, and $$W_1 + W_2$$ is a subspace by (a).
$$\square$$

> **Definition (Direct sum).** $$V$$ is the **direct sum** of
> $$W_1, W_2 \le V$$, written $$V = W_1 \oplus W_2$$, if
>
> - **(a)** $$W_1 + W_2 = V$$, and
> - **(b)** $$W_1 \cap W_2 = \{\mathbf{0}\}$$.
{: .definition #def-direct-sum }

> **Exercise 1.3.30.** Let $$W_1, W_2 \le V$$. Then $$V = W_1 \oplus W_2$$
> if and only if each vector in $$V$$ can be written **uniquely** in the form
> $$x_1 + x_2$$ with $$x_1 \in W_1$$ and $$x_2 \in W_2$$.
{: .theorem #ex-1-3-30 }

*Proof.* ($$\Rightarrow$$) Every vector has such a form because
$$W_1 + W_2 = V$$. If $$x_1 + x_2 = y_1 + y_2$$ with $$x_1, y_1 \in W_1$$
and $$x_2, y_2 \in W_2$$, then

$$
x_1 - y_1 = y_2 - x_2 \in W_1 \cap W_2 = \{\mathbf{0}\} ,
$$

so $$x_1 = y_1$$ and $$x_2 = y_2$$.

($$\Leftarrow$$) Every vector has such a form, so $$W_1 + W_2 = V$$. Let
$$w \in W_1 \cap W_2$$. Then

$$
\mathbf{0} = \mathbf{0} + \mathbf{0} = w + (-w)
$$

are two representations of the zero vector with first term in $$W_1$$ and
second term in $$W_2$$. By uniqueness $$w = \mathbf{0}$$, so
$$W_1 \cap W_2 = \{\mathbf{0}\}$$. $$\square$$

### Problems for §1.3

> **Problem 1.3.1.** Prove that a subset $$W$$ of a vector space $$V$$ is a
> subspace of $$V$$ if and only if $$W \ne \varnothing$$ and, whenever
> $$a \in \mathbb{F}$$ and $$x, y \in W$$, then $$ax \in W$$ and
> $$x + y \in W$$.
{: .problem #prob-1-3-1 }

*Solution.* ($$\Rightarrow$$) By [Theorem 1.3](#thm-1-3), a subspace contains
$$\mathbf{0}$$, so it is nonempty, and it satisfies (b) and (c), which are the
two closure conditions.

($$\Leftarrow$$) The closure conditions are (b) and (c) of
[Theorem 1.3](#thm-1-3), so only (a) is missing. Since $$W \ne \varnothing$$,
pick $$x \in W$$. Then $$0x \in W$$ by closure under scalar multiplication,
and $$0x = \mathbf{0}$$ by [Theorem 1.2](#thm-1-2)(1). Hence
$$\mathbf{0} \in W$$ and $$W \le V$$. $$\square$$

> **Problem 1.3.2.** Let $$W_1$$ and $$W_2$$ be subspaces of a vector space
> $$V$$. Prove that $$W_1 \cap W_2$$ is a subspace of $$V$$. Prove that
> $$W_1 \cup W_2$$ is a subspace of $$V$$ if and only if
> $$W_1 \subseteq W_2$$ or $$W_1 \supseteq W_2$$.
{: .problem #prob-1-3-2 }

The sheet prints $$W_1 \cup W_2$$ in the first sentence as well. The union of
two subspaces is not a subspace in general, which is what the second sentence
characterizes, so the first sentence is read as the intersection.

*Solution.* The intersection is a subspace by [Theorem 1.4](#thm-1-4) with
$$I = \{1, 2\}$$.

($$\Leftarrow$$) If $$W_1 \subseteq W_2$$ then $$W_1 \cup W_2 = W_2$$, a
subspace. If $$W_1 \supseteq W_2$$ then $$W_1 \cup W_2 = W_1$$, a subspace.

($$\Rightarrow$$) Suppose $$W_1 \cup W_2 \le V$$ and, for contradiction, that
neither subspace contains the other. Choose $$x \in W_1 \setminus W_2$$ and
$$y \in W_2 \setminus W_1$$. Both lie in $$W_1 \cup W_2$$, which is closed
under addition, so $$x + y \in W_1$$ or $$x + y \in W_2$$.

- If $$x + y \in W_1$$, then $$y = (x + y) - x \in W_1$$, contradicting
  $$y \notin W_1$$.
- If $$x + y \in W_2$$, then $$x = (x + y) - y \in W_2$$, contradicting
  $$x \notin W_2$$.

So one of the two contains the other. $$\square$$

> **Problem 1.3.3.** Let $$W_1$$ and $$W_2$$ be subspaces of a vector space
> $$V$$.
>
> - **(a)** Prove that $$W_1 + W_2$$ is a subspace of $$V$$ that contains
>   both $$W_1$$ and $$W_2$$.
> - **(b)** Prove that any subspace of $$V$$ that contains both $$W_1$$ and
>   $$W_2$$ must also contain $$W_1 + W_2$$.
{: .problem #prob-1-3-3 }

*Solution.* This is [Exercise 1.3.23](#ex-1-3-23), proved above. In short:
(a) $$w_1 = w_1 + \mathbf{0}$$ and $$w_2 = \mathbf{0} + w_2$$ put $$W_1$$ and
$$W_2$$ inside $$W_1 + W_2$$, and the identities
$$(x_1 + x_2) + (y_1 + y_2) = (x_1 + y_1) + (x_2 + y_2)$$ and
$$c(x_1 + x_2) = cx_1 + cx_2$$ give closure. (b) A subspace containing
$$W_1$$ and $$W_2$$ is closed under addition, so it contains every
$$x_1 + x_2$$. $$\square$$

> **Problem 1.3.4.** Show that $$\mathbb{F}^n$$ is the direct sum of the
> subspaces
>
> $$W_1 = \{(a_1, a_2, \dots, a_n) \in \mathbb{F}^n : a_n = 0\}$$
>
> and
>
> $$W_2 = \{(a_1, a_2, \dots, a_n) \in \mathbb{F}^n :
> a_1 = a_2 = \cdots = a_{n-1} = 0\} .$$
{: .problem #prob-1-3-4 }

*Solution.* Both sets contain the zero vector and are closed under the
coordinatewise operations, since a sum or scalar multiple of vectors with a
zero in a given coordinate again has a zero there. So $$W_1, W_2 \le
\mathbb{F}^n$$ by [Theorem 1.3](#thm-1-3).

*Sum.* Every vector splits as

$$
(a_1, \dots, a_{n-1}, a_n)
= (a_1, \dots, a_{n-1}, 0) + (0, \dots, 0, a_n) \in W_1 + W_2 ,
$$

so $$W_1 + W_2 = \mathbb{F}^n$$.

*Intersection.* If $$(a_1, \dots, a_n) \in W_1 \cap W_2$$, then $$a_n = 0$$
and $$a_1 = \cdots = a_{n-1} = 0$$, so the vector is $$\mathbf{0}$$. Hence
$$W_1 \cap W_2 = \{\mathbf{0}\}$$ and
$$\mathbb{F}^n = W_1 \oplus W_2$$. $$\square$$

> **Problem 1.3.5.** Let $$W_1$$ and $$W_2$$ be subspaces of a vector space
> $$V$$. Prove that $$V$$ is the direct sum of $$W_1$$ and $$W_2$$ if and
> only if each vector in $$V$$ can be *uniquely* written as $$x_1 + x_2$$,
> where $$x_1 \in W_1$$ and $$x_2 \in W_2$$.
{: .problem #prob-1-3-5 }

The sheet prints $$x_2 \in W_1$$; the second summand belongs to $$W_2$$.

*Solution.* This is [Exercise 1.3.30](#ex-1-3-30), proved above. For
uniqueness from the direct sum, $$x_1 + x_2 = y_1 + y_2$$ gives
$$x_1 - y_1 = y_2 - x_2 \in W_1 \cap W_2 = \{\mathbf{0}\}$$. For the
converse, existence gives $$W_1 + W_2 = V$$, and for
$$w \in W_1 \cap W_2$$ the two representations
$$\mathbf{0} + \mathbf{0} = w + (-w)$$ of the zero vector force
$$w = \mathbf{0}$$. $$\square$$

---

## §1.4 Linear Combinations and Systems of Linear Equations

> **Definition (Linear combination).** Let $$S \subseteq V$$ be nonempty. A
> vector $$v \in V$$ is a **linear combination** of vectors of $$S$$ if
>
> $$v = a_1 s_1 + a_2 s_2 + \cdots + a_k s_k$$
>
> for some vectors $$s_1, s_2, \dots, s_k \in S$$ and scalars
> $$a_1, a_2, \dots, a_k \in \mathbb{F}$$, the **coefficients**.
{: .definition #def-linear-combination }

A linear combination is always a **finite** sum, even when $$S$$ is infinite.
The zero vector is a linear combination of any nonempty $$S$$, since
$$\mathbf{0} = 0s$$.

**Linear combinations and linear systems.** Asking whether a vector is a
linear combination of given vectors is asking whether a system of linear
equations has a solution. In $$\mathbb{R}^2$$,

$$
a \begin{pmatrix} 1 \\ 2 \end{pmatrix} + b \begin{pmatrix} 3 \\ 4 \end{pmatrix}
= \begin{pmatrix} 5 \\ 6 \end{pmatrix}
\iff
\begin{cases} a + 3b = 5 \\ 2a + 4b = 6 . \end{cases}
$$

A system is solved by transforming it into an equivalent simpler one with
three operations, none of which changes the solution set:

1. interchanging two equations;
2. multiplying an equation by a nonzero scalar;
3. adding a scalar multiple of one equation to another.

The target form has three properties: the first nonzero coefficient of each
equation is $$1$$; the unknown carrying that leading $$1$$ appears in no other
equation; and the leading unknowns move to the right from one equation to the
next. The leading unknowns are then expressed through the remaining ones,
which serve as free parameters. For example,

$$
\begin{cases} 2x + 4y - z = 7 \\ x + 2y - 2z = 2 \end{cases}
\;\to\;
\begin{cases} x + 2y - 2z = 2 \\ 3z = 3 \end{cases}
\;\to\;
\begin{cases} x + 2y = 4 \\ z = 1 \end{cases}
$$

so $$x = 4 - 2t$$, $$y = t$$, $$z = 1$$ with $$t$$ free.

> **Definition (Span).** Let $$S \subseteq V$$ be nonempty. The **span** of
> $$S$$ is the set
>
> $$\operatorname{span}(S) = \{\text{linear combinations of vectors in } S\} .$$
>
> By convention $$\operatorname{span}(\varnothing) = \{\mathbf{0}\}$$.
{: .definition #def-span }

> **Theorem 1.5.** Let $$S \subseteq V$$.
>
> - **(a)** $$S \subseteq \operatorname{span}(S) \le V$$.
> - **(b)** If $$S \subseteq W \le V$$, then
>   $$\operatorname{span}(S) \subseteq W$$.
>
> So $$\operatorname{span}(S)$$ is the smallest subspace of $$V$$ containing
> $$S$$.
{: .theorem #thm-1-5 }

*Proof.* If $$S = \varnothing$$, then
$$\operatorname{span}(S) = \{\mathbf{0}\}$$ is a subspace, contains
$$\varnothing$$, and is contained in every subspace. Let
$$S \ne \varnothing$$.

(a) Each $$s \in S$$ equals $$1s \in \operatorname{span}(S)$$. For
[Theorem 1.3](#thm-1-3): $$\mathbf{0} = 0s \in \operatorname{span}(S)$$ for
any $$s \in S$$; the sum of two linear combinations of vectors of $$S$$ is a
linear combination of vectors of $$S$$; and

$$
c(a_1 s_1 + \cdots + a_k s_k) = (ca_1)s_1 + \cdots + (ca_k)s_k
$$

is one too.

(b) Let $$a_1 s_1 + \cdots + a_k s_k \in \operatorname{span}(S)$$. Each
$$s_i$$ lies in $$W$$, so each $$a_i s_i \in W$$ by
[Theorem 1.3](#thm-1-3)(c), and the sum lies in $$W$$ by
[Theorem 1.3](#thm-1-3)(b) applied $$k - 1$$ times. $$\square$$

> **Definition (Spanning set).** A subset $$S \subseteq V$$ **spans** (or
> **generates**) $$V$$ if $$\operatorname{span}(S) = V$$.
{: .definition #def-spans }

**Example.** $$S = \{(1,0), (0,1)\}$$ spans $$\mathbb{R}^2$$, since
$$a(1,0) + b(0,1) = (a,b)$$.

> **Exercise 1.4.13.** If $$S_1 \subseteq S_2 \subseteq V$$, then
> $$\operatorname{span}(S_1) \le \operatorname{span}(S_2)$$.
{: .theorem #ex-1-4-13 }

*Proof.* By [Theorem 1.5](#thm-1-5)(a),
$$S_1 \subseteq S_2 \subseteq \operatorname{span}(S_2) \le V$$. By
[Theorem 1.5](#thm-1-5)(b) with $$W = \operatorname{span}(S_2)$$,
$$\operatorname{span}(S_1) \subseteq \operatorname{span}(S_2)$$, and
$$\operatorname{span}(S_1)$$ is a subspace. $$\square$$

### Problems for §1.4

> **Problem 1.4.1.** Solve the following systems of linear equations by the
> method introduced in this section.
>
> **(a)**
>
> $$
> \begin{aligned}
> 2x_1 - 2x_2 - 3x_3 &= -2 \\
> 3x_1 - 3x_2 - 2x_3 + 5x_4 &= 7 \\
> x_1 - x_2 - 2x_3 - x_4 &= -3
> \end{aligned}
> $$
>
> **(e)**
>
> $$
> \begin{aligned}
> x_1 + 2x_2 - 4x_3 - x_4 + x_5 &= 7 \\
> -x_1 + 10x_3 - 3x_4 - 4x_5 &= -16 \\
> 2x_1 + 5x_2 - 5x_3 - 4x_4 - x_5 &= 2 \\
> 4x_1 + 11x_2 - 7x_3 - 10x_4 - 2x_5 &= 7
> \end{aligned}
> $$
{: .problem #prob-1-4-1 }

*Solution.* (a) Interchange the first and third equations, then subtract
$$3$$ times the new first equation from the second and $$2$$ times it from
the third:

$$
\begin{aligned}
x_1 - x_2 - 2x_3 - x_4 &= -3 \\
4x_3 + 8x_4 &= 16 \\
x_3 + 2x_4 &= 4
\end{aligned}
$$

Multiply the second equation by $$\tfrac14$$; it becomes
$$x_3 + 2x_4 = 4$$, and subtracting it from the third leaves $$0 = 0$$.
Adding $$2$$ times it to the first removes $$x_3$$ there:

$$
\begin{aligned}
x_1 - x_2 + 3x_4 &= 5 \\
x_3 + 2x_4 &= 4
\end{aligned}
$$

The leading unknowns are $$x_1$$ and $$x_3$$; $$x_2 = s$$ and $$x_4 = t$$ are
free. The solution set is

$$
(x_1, x_2, x_3, x_4) = (5, 0, 4, 0) + s\,(1, 1, 0, 0) + t\,(-3, 0, -2, 1),
\qquad s, t \in \mathbb{R} .
$$

*Check.* $$2(5 + s - 3t) - 2s - 3(4 - 2t) = -2$$,
$$3(5 + s - 3t) - 3s - 2(4 - 2t) + 5t = 7$$ and
$$(5 + s - 3t) - s - 2(4 - 2t) - t = -3$$.

(e) Add the first equation to the second, subtract $$2$$ times the first from
the third, and subtract $$4$$ times the first from the fourth:

$$
\begin{aligned}
x_1 + 2x_2 - 4x_3 - x_4 + x_5 &= 7 \\
2x_2 + 6x_3 - 4x_4 - 3x_5 &= -9 \\
x_2 + 3x_3 - 2x_4 - 3x_5 &= -12 \\
3x_2 + 9x_3 - 6x_4 - 6x_5 &= -21
\end{aligned}
$$

Interchange the second and third equations. Subtracting $$2$$ times the new
second equation from the new third gives $$3x_5 = 15$$, and subtracting
$$3$$ times it from the fourth gives $$3x_5 = 15$$ again:

$$
\begin{aligned}
x_1 + 2x_2 - 4x_3 - x_4 + x_5 &= 7 \\
x_2 + 3x_3 - 2x_4 - 3x_5 &= -12 \\
x_5 &= 5
\end{aligned}
$$

after multiplying by $$\tfrac13$$ and discarding the repeated equation. Use
$$x_5 = 5$$ to remove $$x_5$$ from the first two equations, then subtract
$$2$$ times the second from the first:

$$
\begin{aligned}
x_1 - 10x_3 + 3x_4 &= -4 \\
x_2 + 3x_3 - 2x_4 &= 3 \\
x_5 &= 5
\end{aligned}
$$

The leading unknowns are $$x_1, x_2, x_5$$; $$x_3 = s$$ and $$x_4 = t$$ are
free. The solution set is

$$
(x_1, \dots, x_5) = (-4, 3, 0, 0, 5) + s\,(10, -3, 1, 0, 0)
+ t\,(-3, 2, 0, 1, 0), \qquad s, t \in \mathbb{R} .
$$

*Check in the second original equation.*
$$-(-4 + 10s - 3t) + 10s - 3t - 4 \cdot 5 = -16$$. $$\square$$

> **Problem 1.4.2.** Show that a subset $$W$$ of a vector space $$V$$ is a
> subspace of $$V$$ if and only if $$\operatorname{span}(W) = W$$.
{: .problem #prob-1-4-2 }

*Solution.* ($$\Rightarrow$$) Let $$W \le V$$. Then
$$W \subseteq \operatorname{span}(W)$$ by [Theorem 1.5](#thm-1-5)(a), and
$$\operatorname{span}(W) \subseteq W$$ by [Theorem 1.5](#thm-1-5)(b) applied
to $$W \subseteq W \le V$$.

($$\Leftarrow$$) $$\operatorname{span}(W)$$ is a subspace by
[Theorem 1.5](#thm-1-5)(a), so $$W = \operatorname{span}(W)$$ is one.
$$\square$$

> **Problem 1.4.3.** If $$S_1$$ and $$S_2$$ are subsets of a vector space
> $$V$$ such that $$S_1 \subseteq S_2$$, show that
> $$\operatorname{span}(S_1) \subseteq \operatorname{span}(S_2)$$.
{: .problem #prob-1-4-3 }

*Solution.* This is [Exercise 1.4.13](#ex-1-4-13):
$$\operatorname{span}(S_2)$$ is a subspace containing $$S_2$$, hence
containing $$S_1$$, and by [Theorem 1.5](#thm-1-5)(b) every subspace
containing $$S_1$$ contains $$\operatorname{span}(S_1)$$. $$\square$$

> **Problem 1.4.4.** If $$S_1$$ and $$S_2$$ are arbitrary subsets of a vector
> space $$V$$, show that
>
> $$\operatorname{span}(S_1 \cup S_2)
> = \operatorname{span}(S_1) + \operatorname{span}(S_2) .$$
{: .problem #prob-1-4-4 }

*Solution.* ($$\supseteq$$) By [Exercise 1.4.13](#ex-1-4-13),
$$\operatorname{span}(S_1)$$ and $$\operatorname{span}(S_2)$$ are both
contained in the subspace $$\operatorname{span}(S_1 \cup S_2)$$. By
[Exercise 1.3.23](#ex-1-3-23)(b), so is their sum.

($$\subseteq$$) By [Exercise 1.3.23](#ex-1-3-23)(a),
$$\operatorname{span}(S_1) + \operatorname{span}(S_2)$$ is a subspace
containing $$\operatorname{span}(S_1) \supseteq S_1$$ and
$$\operatorname{span}(S_2) \supseteq S_2$$, so it contains
$$S_1 \cup S_2$$. By [Theorem 1.5](#thm-1-5)(b) it contains
$$\operatorname{span}(S_1 \cup S_2)$$. $$\square$$

> **Problem 1.4.5.** Let $$S_1$$ and $$S_2$$ be subsets of a vector space
> $$V$$. Show that
>
> $$\operatorname{span}(S_1 \cap S_2)
> = \operatorname{span}(S_1) \cap \operatorname{span}(S_2) .$$
{: .problem #prob-1-4-5 }

The equality as printed is false in general. What holds is the inclusion
$$\subseteq$$, and it can be strict.

*Solution.* *The inclusion.* Since $$S_1 \cap S_2 \subseteq S_1$$,
[Exercise 1.4.13](#ex-1-4-13) gives
$$\operatorname{span}(S_1 \cap S_2) \subseteq \operatorname{span}(S_1)$$,
and likewise for $$S_2$$. Hence

$$
\operatorname{span}(S_1 \cap S_2)
\subseteq \operatorname{span}(S_1) \cap \operatorname{span}(S_2) .
$$

*Strict inclusion.* In $$V = \mathbb{R}$$ take $$S_1 = \{1\}$$ and
$$S_2 = \{2\}$$. Then $$S_1 \cap S_2 = \varnothing$$ and
$$\operatorname{span}(S_1 \cap S_2) = \{0\}$$, while
$$\operatorname{span}(S_1) \cap \operatorname{span}(S_2) = \mathbb{R}$$.

*Equality.* Equality does hold in some cases, for instance when
$$S_1 \subseteq S_2$$: then both sides equal $$\operatorname{span}(S_1)$$,
because $$\operatorname{span}(S_1) \subseteq \operatorname{span}(S_2)$$.
$$\square$$

---

## §1.5 Linear Dependence and Linear Independence

> **Definition (Linearly dependent, linearly independent).** A subset
> $$S \subseteq V$$ is **linearly dependent** if there exist distinct vectors
> $$s_1, s_2, \dots, s_k \in S$$ and scalars
> $$a_1, a_2, \dots, a_k \in \mathbb{F}$$, **not all zero**, such that
>
> $$a_1 s_1 + a_2 s_2 + \cdots + a_k s_k = \mathbf{0} .$$
>
> Otherwise $$S$$ is **linearly independent**.
{: .definition #def-linear-independence }

A representation $$a_1 s_1 + \cdots + a_k s_k = \mathbf{0}$$ with distinct
$$s_i$$ is **trivial** if every $$a_i = 0$$ and **nontrivial** otherwise.

**Notes.**

- **(a)** $$\varnothing$$ is linearly independent: there are no vectors to
  form a nontrivial representation.
- **(b)** $$\{v\}$$ with $$v \ne \mathbf{0}$$ is linearly independent: if
  $$av = \mathbf{0}$$ with $$a \ne 0$$, then
  $$v = a^{-1}(av) = \mathbf{0}$$.
- **(c)** $$S$$ is linearly independent if and only if the only
  representation of $$\mathbf{0}$$ as a linear combination of distinct
  vectors from $$S$$ is the trivial one.
- **(d)** $$S$$ is linearly dependent if and only if at least one vector in
  $$S$$ is a linear combination of other vectors from $$S$$. (A nontrivial
  representation with $$a_1 \ne 0$$ solves to
  $$s_1 = -a_1^{-1}(a_2 s_2 + \cdots + a_k s_k)$$, and conversely. For
  $$S = \{\mathbf{0}\}$$ the "other vectors" form the empty set, whose span
  is $$\{\mathbf{0}\}$$.)

**Example.** $$S = \{(1,0,0), (1,1,0), (1,1,1)\} \subseteq \mathbb{R}^3$$ is
linearly independent: $$a(1,0,0) + b(1,1,0) + c(1,1,1) = (a+b+c,\ b+c,\ c)$$
is zero only when $$c = 0$$, then $$b = 0$$, then $$a = 0$$.

> **Theorem 1.6.** Let $$S_1 \subseteq S_2 \subseteq V$$.
>
> - **(a)** If $$S_1$$ is linearly dependent, then $$S_2$$ is linearly
>   dependent.
> - **(b)** If $$S_2$$ is linearly independent, then $$S_1$$ is linearly
>   independent.
{: .theorem #thm-1-6 }

*Proof.* (a) A nontrivial representation of $$\mathbf{0}$$ by distinct
vectors of $$S_1$$ is one by distinct vectors of $$S_2$$. (b) is the
contrapositive of (a). $$\square$$

> **Theorem 1.7.** Let $$S \subseteq V$$ be linearly independent and let
> $$v \in V \setminus S$$. Then $$S \cup \{v\}$$ is linearly dependent if and
> only if $$v \in \operatorname{span}(S)$$.
{: .theorem #thm-1-7 }

*Proof.* ($$\Rightarrow$$) There are distinct vectors of $$S \cup \{v\}$$
and scalars, not all zero, giving a nontrivial representation of
$$\mathbf{0}$$. Because $$S$$ is linearly independent, the representation
must involve $$v$$, with a nonzero coefficient:

$$
bv + a_1 s_1 + \cdots + a_k s_k = \mathbf{0}, \qquad b \ne 0,\quad
s_i \in S .
$$

Then $$v = -b^{-1}(a_1 s_1 + \cdots + a_k s_k) \in \operatorname{span}(S)$$.
(If no $$s_i$$ occurs, $$v = \mathbf{0} \in \operatorname{span}(S)$$.)

($$\Leftarrow$$) If $$v = a_1 s_1 + \cdots + a_k s_k$$ with distinct
$$s_i \in S$$, then

$$
a_1 s_1 + \cdots + a_k s_k + (-1)v = \mathbf{0}
$$

is a nontrivial representation of $$\mathbf{0}$$ by distinct vectors of
$$S \cup \{v\}$$: the vectors are distinct because $$v \notin S$$, and the
coefficient $$-1$$ is nonzero. $$\square$$

No finiteness is assumed anywhere in this theorem. In the equivalent form
used most often: for linearly independent $$S$$ and $$v \notin S$$,

$$
S \cup \{v\} \text{ is linearly independent}
\iff v \notin \operatorname{span}(S) .
$$

### Problems for §1.5

> **Problem 1.5.1.** In $$\mathbb{F}^n$$, let $$e_j$$ denote the vector whose
> $$j$$-th coordinate is $$1$$ and whose other coordinates are $$0$$. Prove
> that $$\{e_1, e_2, \dots, e_n\}$$ is linearly independent.
{: .problem #prob-1-5-1 }

*Solution.* The vectors are distinct, and for scalars $$a_1, \dots, a_n$$,

$$
a_1 e_1 + a_2 e_2 + \cdots + a_n e_n = (a_1, a_2, \dots, a_n) .
$$

If this is the zero vector, every $$a_j = 0$$. So only the trivial
representation of $$\mathbf{0}$$ exists. $$\square$$

> **Problem 1.5.2.** Let $$S = \{(1,1,0), (1,0,1), (0,1,1)\}$$ be a subset
> of the vector space $$\mathbb{F}^3$$.
>
> - **(a)** Prove that if $$\mathbb{F} = \mathbb{R}$$, then $$S$$ is linearly
>   independent.
> - **(b)** Prove that if $$\mathbb{F}$$ has characteristic two, then $$S$$
>   is linearly dependent.
{: .problem #prob-1-5-2 }

*Solution.* For scalars $$a, b, c$$,

$$
a(1,1,0) + b(1,0,1) + c(0,1,1) = (a + b,\ a + c,\ b + c) .
$$

(a) Suppose this is zero, so $$a + b = 0$$, $$a + c = 0$$ and $$b + c = 0$$.
Subtracting the second equation from the first gives $$b - c = 0$$; adding
that to the third gives $$2b = 0$$. In $$\mathbb{R}$$, $$2 \ne 0$$, so
$$b = 0$$, and then $$a = 0$$ and $$c = 0$$. Only the trivial representation
exists.

(b) Take $$a = b = c = 1$$. The combination is $$(1 + 1, 1 + 1, 1 + 1) =
(0, 0, 0)$$ because $$1 + 1 = 0$$ in characteristic two. The three vectors
are distinct and the coefficients are nonzero, so this is a nontrivial
representation of $$\mathbf{0}$$. $$\square$$

The same argument as (a) works over any field whose characteristic is not
two.

> **Problem 1.5.3.** Let $$V$$ be a vector space over a field of
> characteristic not equal to two.
>
> - **(a)** Let $$u$$ and $$v$$ be distinct vectors in $$V$$. Prove that
>   $$\{u, v\}$$ is linearly independent if and only if
>   $$\{u + v, u - v\}$$ is linearly independent.
> - **(b)** Let $$u$$, $$v$$ and $$w$$ be distinct vectors in $$V$$. Prove
>   that $$\{u, v, w\}$$ is linearly independent if and only if
>   $$\{u + v, v + w, w + u\}$$ is linearly independent.
{: .problem #prob-1-5-3 }

Each set on the right is read as a list: its linear independence means that
the only scalars giving $$\mathbf{0}$$ are zero. This implies that the listed
vectors are distinct. Because the characteristic is not two, $$2$$ is nonzero
in $$\mathbb{F}$$ and $$\tfrac12$$ exists.

*Solution.* (a) ($$\Rightarrow$$) Suppose $$a(u + v) + b(u - v) =
\mathbf{0}$$. Then $$(a + b)u + (a - b)v = \mathbf{0}$$, so $$a + b = 0$$ and
$$a - b = 0$$ by the independence of $$\{u, v\}$$. Adding, $$2a = 0$$, so
$$a = 0$$ and then $$b = 0$$.

($$\Leftarrow$$) Suppose $$au + bv = \mathbf{0}$$. Since

$$
u = \tfrac12\big[(u + v) + (u - v)\big], \qquad
v = \tfrac12\big[(u + v) - (u - v)\big],
$$

this reads

$$
\tfrac12 (a + b)(u + v) + \tfrac12 (a - b)(u - v) = \mathbf{0} .
$$

By the independence of $$\{u + v, u - v\}$$, $$a + b = 0$$ and
$$a - b = 0$$, so $$2a = 0$$, $$a = 0$$ and $$b = 0$$.

(b) ($$\Rightarrow$$) Suppose $$a(u + v) + b(v + w) + c(w + u) =
\mathbf{0}$$. Then

$$
(a + c)u + (a + b)v + (b + c)w = \mathbf{0} ,
$$

so $$a + c = 0$$, $$a + b = 0$$ and $$b + c = 0$$. The first two give
$$b = c$$, and then the third gives $$2b = 0$$. Hence $$b = 0$$, $$c = 0$$
and $$a = 0$$.

($$\Leftarrow$$) Suppose $$au + bv + cw = \mathbf{0}$$. Since

$$
\begin{aligned}
u &= \tfrac12\big[(u + v) - (v + w) + (w + u)\big], \\
v &= \tfrac12\big[(u + v) + (v + w) - (w + u)\big], \\
w &= \tfrac12\big[-(u + v) + (v + w) + (w + u)\big],
\end{aligned}
$$

this reads

$$
\tfrac12(a + b - c)(u + v) + \tfrac12(-a + b + c)(v + w)
+ \tfrac12(a - b + c)(w + u) = \mathbf{0} .
$$

By the independence of $$\{u + v, v + w, w + u\}$$,

$$
a + b - c = 0, \qquad -a + b + c = 0, \qquad a - b + c = 0 .
$$

Adding the first two gives $$2b = 0$$, so $$b = 0$$. Then $$a = c$$ and
$$a = -c$$, so $$2a = 0$$, and $$a = c = 0$$. $$\square$$

> **Problem 1.5.4.** Prove that a set $$S$$ of vectors is linearly
> independent if and only if each finite subset of $$S$$ is linearly
> independent.
{: .problem #prob-1-5-4 }

*Solution.* ($$\Rightarrow$$) Every subset of a linearly independent set is
linearly independent by [Theorem 1.6](#thm-1-6)(b).

($$\Leftarrow$$) By contraposition. If $$S$$ is linearly dependent, there are
distinct $$s_1, \dots, s_k \in S$$ and scalars, not all zero, with
$$a_1 s_1 + \cdots + a_k s_k = \mathbf{0}$$. The same equation shows that the
finite subset $$\{s_1, \dots, s_k\}$$ of $$S$$ is linearly dependent.
$$\square$$

> **Problem 1.5.5.** Let $$S_1$$ and $$S_2$$ be disjoint linearly independent
> subsets of $$V$$. Prove that $$S_1 \cup S_2$$ is linearly dependent if and
> only if
> $$\operatorname{span}(S_1) \cap \operatorname{span}(S_2) \ne \{\mathbf{0}\}$$.
{: .problem #prob-1-5-5 }

*Solution.* ($$\Rightarrow$$) A nontrivial representation of $$\mathbf{0}$$
by distinct vectors of $$S_1 \cup S_2$$ can be sorted into its
$$S_1$$-part and its $$S_2$$-part:

$$
a_1 u_1 + \cdots + a_m u_m + b_1 w_1 + \cdots + b_n w_n = \mathbf{0},
\qquad u_i \in S_1,\ w_j \in S_2 ,
$$

with the $$u_i$$ distinct, the $$w_j$$ distinct, and not all coefficients
zero. Put

$$
x = a_1 u_1 + \cdots + a_m u_m = -(b_1 w_1 + \cdots + b_n w_n)
\in \operatorname{span}(S_1) \cap \operatorname{span}(S_2) .
$$

If $$x = \mathbf{0}$$, then every $$a_i = 0$$ because $$S_1$$ is linearly
independent and every $$b_j = 0$$ because $$S_2$$ is, contradicting
nontriviality. So $$x \ne \mathbf{0}$$ and the intersection is not
$$\{\mathbf{0}\}$$.

($$\Leftarrow$$) Let $$x \ne \mathbf{0}$$ lie in both spans:

$$
x = a_1 u_1 + \cdots + a_m u_m = b_1 w_1 + \cdots + b_n w_n
$$

with distinct $$u_i \in S_1$$ and distinct $$w_j \in S_2$$. Then

$$
a_1 u_1 + \cdots + a_m u_m - b_1 w_1 - \cdots - b_n w_n = \mathbf{0} .
$$

Because $$S_1 \cap S_2 = \varnothing$$, the vectors
$$u_1, \dots, u_m, w_1, \dots, w_n$$ are all distinct, and because
$$x \ne \mathbf{0}$$, some $$a_i \ne 0$$. This is a nontrivial representation
of $$\mathbf{0}$$ by distinct vectors of $$S_1 \cup S_2$$. $$\square$$

Disjointness is used only in the second half, to know that no $$u_i$$
coincides with a $$w_j$$.

---

## References

- Stephen H. Friedberg, Arnold J. Insel and Lawrence E. Spence, *Linear
  Algebra*, 5th edition, Pearson, 2018 — Chapter 1, §§1.1 to 1.5, Appendix C
  for fields, and the exercises cited by number.
- Linear Algebra (881.007), Seoul National University, Fall 2023.
  Instructor: Jin Hong (홍진). Lecture slides for Chapter 1 and the course
  problem sheet for Chapter 1.
- The definitions, the statements of the theorems and their numbering are
  the slides'. The slides give most proofs as outlines, and the proofs here
  fill in those outlines. Where the slides state a result without proof, as
  with Theorems 1.4 and 1.6, the proof is written out here.
- The solutions to the problems are mine. Problems 1.3.2, 1.3.5 and 1.4.5
  are solved in a corrected form, and each correction is stated at the
  problem.
