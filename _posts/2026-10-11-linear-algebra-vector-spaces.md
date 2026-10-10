---
title: "Linear Algebra: Vector Spaces"
date: 2026-10-11 00:30:00 +0900
categories: [Course Notes, Linear Algebra]
tags: [vector spaces, subspaces, span, linear independence, basis, dimension, quotient spaces]
description: Definitions, theorems with proofs, and solved problems for Chapter 1 of Linear Algebra — fields, vector spaces, subspaces, span, linear independence, bases and dimension, maximal linearly independent subsets, and quotient spaces.
math: true
mermaid: false
render_with_liquid: false
---

> **How to read the labels.** Definitions, theorems and their numbers follow
> the lecture slides, which follow the textbook (Friedberg, Insel and Spence,
> 5th edition). A result labelled **Exercise a.b.c** is a textbook exercise
> that the lecture stated and used as a theorem; the number is the textbook's.
> A **Problem a.b.k** is the $$k$$-th question for §a.b on the course problem
> sheet, which does not number its questions. Quotient spaces were lectured
> from a separate set of slides and close the chapter.
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

By [Theorem 1.7](#thm-1-7), every $$v \in S \setminus \beta$$ lies in
$$\operatorname{span}(\beta)$$. So
$$S \subseteq \operatorname{span}(\beta) \le V$$, and
[Theorem 1.5](#thm-1-5)(b) gives
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
[Theorem 1.6](#thm-1-6)(b), so the induction hypothesis gives $$m \le n$$
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
linearly dependent by [Theorem 1.7](#thm-1-7), a contradiction. Hence
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

and [Theorem 1.5](#thm-1-5)(b) gives
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
independent by [Theorem 1.6](#thm-1-6)(b) and $$\beta$$ spans $$V$$, so
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
linear independence. By [Theorem 1.7](#thm-1-7),
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
forming a linearly independent set ([Theorem 1.6](#thm-1-6)(b)), while a
basis of $$n$$ vectors spans $$V$$. This contradicts
[Theorem 1.10](#thm-1-10)(a).

($$\Rightarrow$$) Let $$V$$ be infinite-dimensional, so that no finite subset
of $$V$$ is a basis. Build vectors $$v_1, v_2, \dots$$ one at a time.
Suppose a linearly independent $$\{v_1, \dots, v_k\}$$ has been chosen
(with $$k = 0$$ and the empty set to start). It is finite, so it is not a
basis, so it does not span $$V$$. Choose
$$v_{k+1} \notin \operatorname{span}\{v_1, \dots, v_k\}$$. Then
$$\{v_1, \dots, v_{k+1}\}$$ is linearly independent by
[Theorem 1.7](#thm-1-7).

The set $$S = \{v_1, v_2, \dots\}$$ is infinite, because each $$v_{k+1}$$
differs from the earlier ones. Every finite subset of $$S$$ lies in some
$$\{v_1, \dots, v_k\}$$, so it is linearly independent by
[Theorem 1.6](#thm-1-6)(b). Hence $$S$$ is linearly independent by
[Problem 1.5.4](#prob-1-5-4). $$\square$$

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
$$v \in \operatorname{span}(\beta)$$ by [Theorem 1.7](#thm-1-7). Therefore
$$S \subseteq \operatorname{span}(\beta)$$, and by
[Theorem 1.5](#thm-1-5)(b),
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
$$W_1$$ ([Theorem 1.4](#thm-1-4)), so it has a finite basis
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

*Solution.* *Sum.* By [Problem 1.4.4](#prob-1-4-4),

$$
V = \operatorname{span}(\beta_1 \cup \beta_2)
= \operatorname{span}(\beta_1) + \operatorname{span}(\beta_2)
= W_1 + W_2 .
$$

*Intersection.* $$\beta_1$$ and $$\beta_2$$ are disjoint linearly
independent sets whose union is linearly independent. By
[Problem 1.5.5](#prob-1-5-5),

$$
W_1 \cap W_2 = \operatorname{span}(\beta_1) \cap \operatorname{span}(\beta_2)
= \{\mathbf{0}\} .
$$

Both conditions of the [direct sum](#def-direct-sum) hold. $$\square$$

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
([Theorem 1.6](#thm-1-6)(b)) and spans $$W_2$$, so it is a basis of
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
dependent by [Theorem 1.7](#thm-1-7), and then so is every set strictly
containing $$\beta$$ ([Theorem 1.6](#thm-1-6)(a)).

> **Theorem 1.12.** Let $$S \subseteq V$$ with
> $$\operatorname{span}(S) = V$$. Any linearly independent
> $$\beta \subseteq S$$ that is maximal among the linearly independent
> subsets of $$S$$ is a basis for $$V$$.
{: .theorem #thm-1-12 }

*Proof.* Let $$v \in S \setminus \beta$$. Then $$\beta \cup \{v\}$$ is a
subset of $$S$$ strictly containing $$\beta$$, so by maximality it is
linearly dependent, and $$v \in \operatorname{span}(\beta)$$ by
[Theorem 1.7](#thm-1-7). Hence
$$S \subseteq \operatorname{span}(\beta)$$, and
[Theorem 1.5](#thm-1-5)(b) gives
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
([Exercise 1.4.13](#ex-1-4-13)). There is a basis $$\gamma$$ with

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

In the notation of the [sum of subsets](#def-sum), $$v + W = \{v\} + W$$. The
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
[Theorem 1.3](#thm-1-3) it follows directly that $$\ker T \le V$$ and
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
  Algebra*, 5th edition, Pearson, 2018 — Chapter 1, Appendix C for fields,
  and the exercises cited by number.
- Linear Algebra (881.007), Seoul National University, Fall 2023.
  Instructor: Jin Hong (홍진). Lecture slides for Chapter 1 and for quotient
  spaces, and the course problem sheet for Chapter 1.
- The definitions, the statements of the theorems and their numbering are
  the slides'. The slides give most proofs as outlines, and the proofs here
  fill in those outlines. Where the slides state a result without proof, as
  with Theorems 1.4, 1.6, 1.8 and 1.13, the proof is written out here.
- The chain and the Maximal Principle are stated as in the textbook; the
  slides refer to them only as Zorn's Lemma and the Axiom of Choice.
- The slides label the First Isomorphism Theorem with a repeated exercise
  number, so it appears here under its usual name instead.
- The solutions to the problems are mine. Problems 1.3.2, 1.3.5, 1.4.5 and
  1.6.6 are solved in a corrected form, and each correction is stated at the
  problem.
