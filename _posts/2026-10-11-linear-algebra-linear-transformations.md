---
title: "Linear Algebra: Linear Transformations and Matrices (Part 1)"
date: 2026-10-11 01:00:00 +0900
categories: [Course Notes, Linear Algebra]
tags: [linear transformations, kernel, image, rank-nullity, matrix representation]
description: Definitions, theorems with proofs, and solved problems for Chapter 2 of Linear Algebra, §2.1 to §2.3 — linear transformations, kernel and image, the dimension theorem, matrix representations, and composition and matrix multiplication.
math: true
mermaid: false
render_with_liquid: false
---

> **How to read the labels.** As in
> [Chapter 1](/posts/linear-algebra-vector-spaces/), definitions, theorems
> and their numbers follow the lecture slides, which follow the textbook
> (Friedberg, Insel and Spence, 5th edition). An **Exercise a.b.c** is a
> textbook exercise that the lecture stated and used as a theorem. A
> **Problem a.b.k** is the $$k$$-th question for §a.b on the course problem
> sheet. Results of Chapter 1 are cited by number and link to that chapter.
> Chapter 2 is split over two posts: this one covers §2.1 to §2.3, and
> [Part 2](/posts/linear-algebra-linear-transformations-2/) covers §2.4 to
> §2.6.
{: .prompt-info }

Throughout, $$V$$, $$W$$ and $$Z$$ are vector spaces over the same field
$$\mathbb{F}$$. The lecture writes $$\ker(T)$$ and $$\operatorname{im}(T)$$
where the textbook and the problem sheet write $$N(T)$$ and $$R(T)$$; these
notes use $$\ker$$ and $$\operatorname{im}$$. The identity map of $$V$$ is
$$\mathrm{id}_V$$ and the zero map is $$T_0$$.

---

## §2.1 Linear Transformations, Null Spaces, and Ranges

> **Definition (Linear transformation).** A function $$T \colon V \to W$$
> is a **linear transformation** (or simply **linear**) if
>
> - **(a)** $$T(x + y) = T(x) + T(y)$$, and
> - **(b)** $$T(cx) = c\,T(x)$$
>
> for all $$x, y \in V$$ and $$c \in \mathbb{F}$$.
{: .definition #def-linear-transformation }

A linear transformation is a map that preserves the vector space structure.

**Notes.**

- If $$T$$ is linear, then $$T(\mathbf{0}_V) = \mathbf{0}_W$$:
  $$T(\mathbf{0}) = T(0 \cdot \mathbf{0}) = 0\,T(\mathbf{0}) = \mathbf{0}$$.
- For a function $$T \colon V \to W$$ the following are equivalent: $$T$$
  is linear; $$T(cx + y) = c\,T(x) + T(y)$$ for all $$x, y \in V$$ and
  $$c \in \mathbb{F}$$; and

  $$
  T\Big(\sum_{i=1}^{k} c_i v_i\Big) = \sum_{i=1}^{k} c_i\,T(v_i)
  $$

  for all $$v_1, \dots, v_k \in V$$ and $$c_1, \dots, c_k \in \mathbb{F}$$.
- A linear $$T$$ satisfies $$T(x - y) = T(x) - T(y)$$.

**Examples.**

- **Left multiplication.** For $$A \in \mathrm{Mat}_{m \times n}(\mathbb{F})$$,
  the map $$L_A \colon \mathbb{F}^n \to \mathbb{F}^m$$, $$x \mapsto Ax$$, is
  linear.
- **Rotation** by $$\theta$$, **reflection** about a line through the origin,
  and **projection** onto such a line are linear maps
  $$\mathbb{R}^2 \to \mathbb{R}^2$$. The rotation is

  $$
  T_\theta \begin{pmatrix} x \\ y \end{pmatrix}
  = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta
  \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} .
  $$

- **Differentiation** $$D \colon C^1 \to C^0$$, $$f \mapsto f'$$, from
  continuously differentiable functions to continuous functions.
- The **identity transformation** $$\mathrm{id}_V \colon V \to V$$,
  $$v \mapsto v$$, and the **zero transformation** $$T_0 \colon V \to W$$,
  $$v \mapsto \mathbf{0}_W$$.

> **Definition (Kernel, image).** Let $$T \colon V \to W$$ be linear.
>
> - The **kernel** (or **null space**, $$N(T)$$) of $$T$$ is
>   $$\ker(T) = \{\, v \in V : T(v) = \mathbf{0} \,\}$$.
> - The **image** (or **range**, $$R(T)$$) of $$T$$ is
>   $$\operatorname{im}(T) = \{\, T(v) : v \in V \,\}$$.
{: .definition #def-kernel-image }

> **Theorem 2.1.** If $$T \colon V \to W$$ is linear, then
> $$\ker(T) \le V$$ and $$\operatorname{im}(T) \le W$$.
{: .theorem #thm-2-1 }

*Proof.* Use [Theorem 1.3][T1.3].

*Kernel.* $$T(\mathbf{0}) = \mathbf{0}$$, so
$$\mathbf{0} \in \ker(T)$$. If $$x, y \in \ker(T)$$ and
$$c \in \mathbb{F}$$, then $$T(x + y) = T(x) + T(y) = \mathbf{0}$$ and
$$T(cx) = c\,T(x) = \mathbf{0}$$.

*Image.* $$\mathbf{0} = T(\mathbf{0}) \in \operatorname{im}(T)$$. If
$$T(x), T(y) \in \operatorname{im}(T)$$ and $$c \in \mathbb{F}$$, then
$$T(x) + T(y) = T(x + y)$$ and $$c\,T(x) = T(cx)$$ are in
$$\operatorname{im}(T)$$. $$\square$$

**Example.** $$\ker(\mathrm{id}_V) = \{\mathbf{0}\}$$ and
$$\operatorname{im}(\mathrm{id}_V) = V$$; $$\ker(T_0) = V$$ and
$$\operatorname{im}(T_0) = \{\mathbf{0}\}$$.

> **Theorem 2.2.** Let $$T \colon V \to W$$ be linear and let
> $$\beta = \{v_i\}_{i \in I}$$ be a basis for $$V$$, possibly infinite.
> Then
>
> $$\operatorname{im}(T) = \operatorname{span}(T(\beta))
> = \operatorname{span}\big(\{T(v_i)\}_{i \in I}\big) .$$
{: .theorem #thm-2-2 }

*Proof.* $$T(\beta) \subseteq \operatorname{im}(T) \le W$$, so
$$\operatorname{span}(T(\beta)) \subseteq \operatorname{im}(T)$$ by
[Theorem 1.5][T1.5](b). Conversely, an element of $$\operatorname{im}(T)$$
is $$T(v)$$ with $$v = c_1 v_{i_1} + \cdots + c_k v_{i_k}$$, so

$$
T(v) = c_1 T(v_{i_1}) + \cdots + c_k T(v_{i_k})
\in \operatorname{span}(T(\beta)) .
$$

$$\square$$

The proof uses only that $$\beta$$ spans $$V$$, not that it is linearly
independent.

> **Definition (Nullity, rank).** Let $$T \colon V \to W$$ be linear. When
> the dimensions are finite,
>
> $$\operatorname{nullity}(T) = \dim(\ker(T)), \qquad
> \operatorname{rank}(T) = \dim(\operatorname{im}(T)) .$$
{: .definition #def-rank-nullity }

> **Theorem 2.3 (Dimension Theorem; Rank–Nullity Theorem).** Let
> $$T \colon V \to W$$ be linear with $$\dim V < \infty$$. Then
>
> $$\operatorname{rank}(T) + \operatorname{nullity}(T) = \dim V .$$
{: .theorem #thm-2-3 }

*Proof.* $$\ker(T) \le V$$ is finite-dimensional by
[Theorem 1.11][T1.11]. Take a basis $$\{v_1, \dots, v_k\}$$ of
$$\ker(T)$$ and extend it, by the
[Basis Extension Theorem][C1.11], to a basis

$$
\beta = \{v_1, \dots, v_k, v_{k+1}, \dots, v_n\}
$$

of $$V$$. Claim: $$\gamma = \{T(v_{k+1}), \dots, T(v_n)\}$$ is a basis for
$$\operatorname{im}(T)$$ with $$n - k$$ elements.

*Spanning.* By [Theorem 2.2](#thm-2-2),
$$\operatorname{im}(T) = \operatorname{span}(T(\beta))$$, and
$$T(v_i) = \mathbf{0}$$ for $$i \le k$$, so $$\gamma$$ spans
$$\operatorname{im}(T)$$.

*Independence.* Suppose

$$
\mathbf{0} = c_{k+1} T(v_{k+1}) + \cdots + c_n T(v_n)
= T(c_{k+1} v_{k+1} + \cdots + c_n v_n) .
$$

Then $$c_{k+1} v_{k+1} + \cdots + c_n v_n \in \ker(T)$$, so

$$
a_1 v_1 + \cdots + a_k v_k = c_{k+1} v_{k+1} + \cdots + c_n v_n
$$

for some scalars $$a_i$$. By the linear independence of $$\beta$$, every
coefficient is zero. In particular the $$n - k$$ listed vectors are
distinct.

Hence $$\operatorname{rank}(T) = n - k$$ and
$$\operatorname{nullity}(T) = k$$. $$\square$$

In short: a basis of the kernel extends to a basis of $$V$$, and the images
of the added vectors form a basis of the image.

**Example.** Let $$T \colon P_2(\mathbb{R}) \to
\mathrm{Mat}_{2 \times 2}(\mathbb{R})$$ be

$$
T(f) = \begin{pmatrix} f(1) - f(2) & 0 \\ 0 & f(0) \end{pmatrix} .
$$

With $$\beta = \{1, x, x^2\}$$, [Theorem 2.2](#thm-2-2) gives

$$
\operatorname{im}(T) = \operatorname{span}\left\{
\begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix},
\begin{pmatrix} -1 & 0 \\ 0 & 0 \end{pmatrix},
\begin{pmatrix} -3 & 0 \\ 0 & 0 \end{pmatrix} \right\} ,
$$

so $$\operatorname{rank}(T) = 2$$ and
$$\operatorname{nullity}(T) = 3 - 2 = 1$$.

> **Theorem 2.4.** Let $$T \colon V \to W$$ be linear. Then $$T$$ is
> one-to-one if and only if $$\ker(T) = \{\mathbf{0}\}$$.
{: .theorem #thm-2-4 }

*Proof.* For $$x, y \in V$$,

$$
T(x) = T(y) \iff T(x) - T(y) = \mathbf{0} \iff T(x - y) = \mathbf{0}
\iff x - y \in \ker(T) .
$$

($$\Leftarrow$$) If $$\ker(T) = \{\mathbf{0}\}$$, then $$T(x) = T(y)$$
gives $$x - y = \mathbf{0}$$. ($$\Rightarrow$$) If $$T$$ is one-to-one and
$$x \in \ker(T)$$, then $$T(x) = \mathbf{0} = T(\mathbf{0})$$, so
$$x = \mathbf{0}$$. $$\square$$

> **Theorem 2.5.** Let $$T \colon V \to W$$ be linear with
> $$\dim V = \dim W < \infty$$. The following are equivalent.
>
> - **(a)** $$T$$ is one-to-one.
> - **(b)** $$T$$ is onto.
> - **(c)** $$\operatorname{rank}(T) = \dim V$$.
{: .theorem #thm-2-5 }

*Proof.* By [Theorem 2.4](#thm-2-4) and [Theorem 2.3](#thm-2-3),

$$
T \text{ one-to-one} \iff \operatorname{nullity}(T) = 0
\iff \operatorname{rank}(T) = \dim V ,
$$

so (a) $$\Leftrightarrow$$ (c). Since $$\dim V = \dim W$$ and
$$\operatorname{im}(T) \le W$$, [Theorem 1.11][T1.11](c) gives

$$
\operatorname{rank}(T) = \dim V \iff \dim \operatorname{im}(T) = \dim W
\iff \operatorname{im}(T) = W ,
$$

so (c) $$\Leftrightarrow$$ (b). $$\square$$

**Example.** $$T \colon \mathbb{F}^2 \to \mathbb{F}^2$$,
$$(a_1, a_2) \mapsto (a_1 + a_2, a_2)$$, has
$$\ker(T) = \{\mathbf{0}\}$$, so it is one-to-one and therefore also onto.

> **Theorem 2.6 (Linear Extension Theorem).** Let
> $$\{v_1, v_2, \dots, v_n\}$$ be a basis for $$V$$ and let
> $$w_1, w_2, \dots, w_n \in W$$, not necessarily distinct. Then there
> exists exactly one linear transformation $$T \colon V \to W$$ such that
> $$T(v_i) = w_i$$ for $$i = 1, 2, \dots, n$$.
{: .theorem #thm-2-6 }

*Proof.* *Uniqueness.* Any linear $$T$$ with $$T(v_i) = w_i$$ must satisfy

$$
T\Big(\sum_{i=1}^{n} c_i v_i\Big) = \sum_{i=1}^{n} c_i w_i ,
$$

and every vector of $$V$$ has the form $$\sum c_i v_i$$. So there is no
choice.

*Existence.* By [Theorem 1.8][T1.8], each element of $$V$$ can be written
uniquely as $$\sum c_i v_i$$, so the rule
$$\sum c_i v_i \mapsto \sum c_i w_i$$ is a well-defined function
$$T \colon V \to W$$, and $$T(v_i) = w_i$$. It is linear: for
$$x = \sum a_i v_i$$, $$y = \sum b_i v_i$$ and $$c \in \mathbb{F}$$,

$$
cx + y = \sum_{i=1}^{n} (c a_i + b_i) v_i
\;\mapsto\; \sum_{i=1}^{n} (c a_i + b_i) w_i
= c \sum_{i=1}^{n} a_i w_i + \sum_{i=1}^{n} b_i w_i = c\,T(x) + T(y) .
$$

$$\square$$

> **Corollary to Theorem 2.6.** Let $$\{v_1, v_2, \dots, v_n\}$$ be a basis
> for $$V$$. If $$U, T \colon V \to W$$ are linear with
> $$U(v_i) = T(v_i)$$ for $$i = 1, 2, \dots, n$$, then $$U = T$$.
{: .theorem #cor-2-6 }

*Proof.* Both are linear transformations sending $$v_i$$ to
$$w_i = T(v_i)$$; by the uniqueness in [Theorem 2.6](#thm-2-6) they are
equal. $$\square$$

A linear map is determined by its values on a basis, and those values can be
prescribed freely.

### Direct sums, projections and invariant subspaces

The lecture treated the following exercises together at the end of the
chapter. They start from the [direct sum][D-directsum] of Chapter 1.

> **Exercise 1.6.33.** Let $$\beta_1$$ and $$\beta_2$$ be bases for
> $$W_1, W_2 \le V$$.
>
> - **(a)** If $$V = W_1 \oplus W_2$$, then
>   $$\beta_1 \cap \beta_2 = \varnothing$$ and $$\beta_1 \cup \beta_2$$ is a
>   basis for $$V$$.
> - **(b)** If $$\beta_1 \cap \beta_2 = \varnothing$$ and
>   $$\beta_1 \cup \beta_2$$ is a basis for $$V$$, then
>   $$V = W_1 \oplus W_2$$.
{: .theorem #ex-1-6-33 }

*Proof.* (a) $$\beta_1 \cap \beta_2 \subseteq W_1 \cap W_2 =
\{\mathbf{0}\}$$, and a basis does not contain $$\mathbf{0}$$, so
$$\beta_1 \cap \beta_2 = \varnothing$$. By [Problem 1.4.4][P1.4.4],

$$
\operatorname{span}(\beta_1 \cup \beta_2)
= \operatorname{span}(\beta_1) + \operatorname{span}(\beta_2)
= W_1 + W_2 = V .
$$

$$\beta_1$$ and $$\beta_2$$ are disjoint linearly independent sets with
$$\operatorname{span}(\beta_1) \cap \operatorname{span}(\beta_2) =
W_1 \cap W_2 = \{\mathbf{0}\}$$, so $$\beta_1 \cup \beta_2$$ is linearly
independent by [Problem 1.5.5][P1.5.5].

(b) This is [Problem 1.6.6][P1.6.6]. $$\square$$

> **Exercise 1.6.34(a).** Let $$V$$ be finite-dimensional and
> $$W_1 \le V$$. Then there exists $$W_2 \le V$$ such that
> $$V = W_1 \oplus W_2$$.
{: .theorem #ex-1-6-34 }

*Proof.* This is [Problem 1.6.7][P1.6.7]: extend a basis of $$W_1$$ to a
basis of $$V$$ by the [Basis Extension Theorem][C1.11] and let $$W_2$$ be
the span of the added vectors. $$\square$$

Such a $$W_2$$ is a **direct sum complement** of $$W_1$$. It is not
determined by $$W_1$$. The statement is also true when $$V$$ is
infinite-dimensional, with [Problem 1.7.3][P1.7.3] in place of the Basis
Extension Theorem.

> **Definition (Projection).** Let $$V = W_1 \oplus W_2$$. The function
> $$T \colon V \to V$$ that maps each $$x = x_1 + x_2$$, where
> $$x_1 \in W_1$$ and $$x_2 \in W_2$$, to $$x_1$$ is the **projection** of
> $$V$$ on $$W_1$$ along $$W_2$$.
{: .definition #def-projection }

$$T$$ is well defined because the decomposition $$x = x_1 + x_2$$ is unique
([Exercise 1.3.30][E1.3.30]).

![A plane with two lines through the origin, W1 and W2. A vector x is split by a parallelogram into x1 on W1 and x2 on W2, and the projection sends x to x1. A different complement W2 prime sends the same x to a different point of W1](/assets/img/linear-algebra/projection.svg)

The projection depends on $$W_2$$ as well as on $$W_1$$: a different
complement moves $$x$$ to a different point of $$W_1$$.

> **Exercise 2.1.27.** Let $$V = W_1 \oplus W_2$$ and let
> $$T \colon V \to V$$ be the projection on $$W_1$$ along $$W_2$$.
>
> - **(a)** $$T$$ is linear, and $$W_1 = \{\, x \in V : T(x) = x \,\}$$.
> - **(b)** $$W_1 = \operatorname{im}(T)$$ and $$W_2 = \ker(T)$$.
{: .theorem #ex-2-1-27 }

*Proof.* (a) Let $$x = x_1 + x_2$$ and $$y = y_1 + y_2$$ with
$$x_1, y_1 \in W_1$$ and $$x_2, y_2 \in W_2$$, and let
$$c \in \mathbb{F}$$. Then

$$
cx + y = (cx_1 + y_1) + (cx_2 + y_2), \qquad
cx_1 + y_1 \in W_1,\quad cx_2 + y_2 \in W_2 ,
$$

and this is *the* decomposition of $$cx + y$$, so
$$T(cx + y) = cx_1 + y_1 = c\,T(x) + T(y)$$.

If $$x \in W_1$$, its decomposition is $$x = x + \mathbf{0}$$, so
$$T(x) = x$$. Conversely, if $$T(x) = x$$, then $$x = x_1 \in W_1$$.

(b) $$\operatorname{im}(T) \subseteq W_1$$ by definition, and
$$W_1 \subseteq \operatorname{im}(T)$$ because $$x = T(x)$$ for
$$x \in W_1$$. Also $$T(x) = \mathbf{0}$$ if and only if
$$x_1 = \mathbf{0}$$, if and only if $$x = x_2 \in W_2$$. $$\square$$

So every projection is the projection on its image along its kernel, and
$$W_1$$ is the subspace of fixed points.

> **Definition (Invariant subspace, restriction).** Let
> $$T \colon V \to V$$ be linear. A subspace $$W \le V$$ is
> **$$T$$-invariant** if $$T(W) \subseteq W$$. If $$W$$ is
> $$T$$-invariant, the **restriction** of $$T$$ to $$W$$ is the linear
> transformation $$T_W \colon W \to W$$ given by $$T_W(x) = T(x)$$.
{: .definition #def-invariant }

A $$T$$-invariant subspace is mapped into itself as a set; its vectors need
not be fixed one by one.

> **Exercise 2.1.31.** Let $$V = W_1 \oplus W_2$$ and let
> $$T \colon V \to V$$ be the projection on $$W_1$$ along $$W_2$$. Then
> $$W_1$$ is $$T$$-invariant and $$T_{W_1} = \mathrm{id}_{W_1}$$.
{: .theorem #ex-2-1-31 }

*Proof.* By [Exercise 2.1.27](#ex-2-1-27)(a), $$T(x) = x$$ for every
$$x \in W_1$$. So $$T(W_1) \subseteq W_1$$ and $$T_{W_1}(x) = x$$.
$$\square$$

### Problems for §2.1

> **Problem 2.1.1.** Let $$T \colon V \to W$$ be linear, and let
> $$\{w_1, w_2, \dots, w_k\}$$ be a linearly independent set of $$k$$
> vectors from $$\operatorname{im}(T)$$. Prove that if
> $$S = \{v_1, v_2, \dots, v_k\}$$ is chosen so that $$T(v_i) = w_i$$ for
> $$i = 1, 2, \dots, k$$, then $$S$$ is linearly independent.
{: .problem #prob-2-1-1 }

*Solution.* The $$v_i$$ are distinct because their images $$w_i$$ are.
Suppose $$a_1 v_1 + \cdots + a_k v_k = \mathbf{0}$$. Applying $$T$$,

$$
\mathbf{0} = T(a_1 v_1 + \cdots + a_k v_k) = a_1 w_1 + \cdots + a_k w_k ,
$$

and the linear independence of $$\{w_1, \dots, w_k\}$$ gives every
$$a_i = 0$$. $$\square$$

> **Problem 2.1.2.** Let $$T \colon V \to W$$ be linear.
>
> - **(a)** Prove that $$T$$ is one-to-one if and only if $$T$$ carries
>   linearly independent subsets of $$V$$ onto linearly independent subsets
>   of $$W$$.
> - **(b)** Suppose that $$T$$ is one-to-one and that $$S$$ is a subset of
>   $$V$$. Prove that $$S$$ is linearly independent if and only if
>   $$T(S)$$ is linearly independent.
> - **(c)** Suppose $$\beta = \{v_1, v_2, \dots, v_n\}$$ is a basis for
>   $$V$$ and $$T$$ is one-to-one and onto. Prove that
>   $$T(\beta) = \{T(v_1), T(v_2), \dots, T(v_n)\}$$ is a basis for $$W$$.
{: .problem #prob-2-1-2 }

*Solution.* (a) ($$\Rightarrow$$) Let $$S \subseteq V$$ be linearly
independent and let $$y_1, \dots, y_k$$ be distinct vectors of $$T(S)$$.
Choose $$s_i \in S$$ with $$T(s_i) = y_i$$; the $$s_i$$ are distinct
because the $$y_i$$ are. If $$a_1 y_1 + \cdots + a_k y_k = \mathbf{0}$$,
then $$T(a_1 s_1 + \cdots + a_k s_k) = \mathbf{0}$$, so
$$a_1 s_1 + \cdots + a_k s_k \in \ker(T) = \{\mathbf{0}\}$$ by
[Theorem 2.4](#thm-2-4), and every $$a_i = 0$$ because $$S$$ is linearly
independent.

($$\Leftarrow$$) By contraposition. If $$T$$ is not one-to-one, there is
$$x \ne \mathbf{0}$$ with $$T(x) = \mathbf{0}$$
([Theorem 2.4](#thm-2-4)). Then $$\{x\}$$ is linearly independent but
$$T(\{x\}) = \{\mathbf{0}\}$$ is linearly dependent.

(b) ($$\Rightarrow$$) is part (a). ($$\Leftarrow$$) Let
$$s_1, \dots, s_k$$ be distinct vectors of $$S$$ with
$$a_1 s_1 + \cdots + a_k s_k = \mathbf{0}$$. Applying $$T$$,
$$a_1 T(s_1) + \cdots + a_k T(s_k) = \mathbf{0}$$. The vectors
$$T(s_i)$$ are distinct because $$T$$ is one-to-one, and they lie in the
linearly independent set $$T(S)$$, so every $$a_i = 0$$.

(c) $$T(\beta)$$ is linearly independent by (a), and
$$\operatorname{span}(T(\beta)) = \operatorname{im}(T) = W$$ by
[Theorem 2.2](#thm-2-2) and because $$T$$ is onto. $$\square$$

> **Problem 2.1.3.** Let $$V$$ and $$W$$ be finite-dimensional vector
> spaces and $$T \colon V \to W$$ be linear.
>
> - **(a)** Prove that if $$\dim(V) < \dim(W)$$, then $$T$$ cannot be onto.
> - **(b)** Prove that if $$\dim(V) > \dim(W)$$, then $$T$$ cannot be
>   one-to-one.
{: .problem #prob-2-1-3 }

*Solution.* Both parts use the [Dimension Theorem](#thm-2-3),
$$\operatorname{rank}(T) + \operatorname{nullity}(T) = \dim V$$.

(a) $$\operatorname{rank}(T) = \dim V - \operatorname{nullity}(T) \le
\dim V < \dim W$$, so $$\operatorname{im}(T) \ne W$$.

(b) $$\operatorname{rank}(T) \le \dim W$$ by [Theorem 1.11][T1.11](b),
because $$\operatorname{im}(T) \le W$$. So

$$
\operatorname{nullity}(T) = \dim V - \operatorname{rank}(T)
\ge \dim V - \dim W > 0 ,
$$

hence $$\ker(T) \ne \{\mathbf{0}\}$$ and $$T$$ is not one-to-one by
[Theorem 2.4](#thm-2-4). $$\square$$

> **Problem 2.1.4.** Let $$T \colon V \to W$$ be linear, $$b \in W$$, and
> let $$K = \{\, x \in V : T(x) = b \,\}$$ be nonempty. Prove that if
> $$s \in K$$, then $$K = \{s\} + \ker(T)$$.
{: .problem #prob-2-1-4 }

*Solution.* ($$\subseteq$$) Let $$x \in K$$. Then
$$T(x - s) = T(x) - T(s) = b - b = \mathbf{0}$$, so
$$x - s \in \ker(T)$$ and $$x = s + (x - s) \in \{s\} + \ker(T)$$.

($$\supseteq$$) Let $$n \in \ker(T)$$. Then
$$T(s + n) = T(s) + T(n) = b + \mathbf{0} = b$$, so $$s + n \in K$$.
$$\square$$

In the language of Chapter 1, the solution set of $$T(x) = b$$ is the
[coset][D-coset] $$s + \ker(T)$$ of the kernel.

> **Problem 2.1.5.** Assume that $$T \colon V \to V$$ is the projection on
> $$W_1$$ along $$W_2$$.
>
> - **(a)** Prove that $$T$$ is linear and
>   $$W_1 = \{\, x \in V : T(x) = x \,\}$$.
> - **(b)** Prove that $$W_1 = \operatorname{im}(T)$$ and
>   $$W_2 = \ker(T)$$.
{: .problem #prob-2-1-5 }

*Solution.* This is [Exercise 2.1.27](#ex-2-1-27), proved above. The key
point in (a) is uniqueness of the decomposition: from $$x = x_1 + x_2$$ and
$$y = y_1 + y_2$$ the decomposition of $$cx + y$$ is
$$(cx_1 + y_1) + (cx_2 + y_2)$$, so
$$T(cx + y) = cx_1 + y_1 = c\,T(x) + T(y)$$; and $$T(x) = x$$ exactly when
$$x = x_1$$. For (b), $$T(x) = x_1$$ ranges over $$W_1$$ and vanishes
exactly when $$x = x_2 \in W_2$$. $$\square$$

> **Problem 2.1.6.** Suppose that $$T$$ is the projection on $$W$$ along
> some subspace $$W'$$. Prove that $$W$$ is $$T$$-invariant and that
> $$T_W = I_W$$.
{: .problem #prob-2-1-6 }

*Solution.* This is [Exercise 2.1.31](#ex-2-1-31). By
[Problem 2.1.5](#prob-2-1-5)(a), $$T(x) = x$$ for every $$x \in W$$. Hence
$$T(W) \subseteq W$$, and the restriction satisfies
$$T_W(x) = T(x) = x$$ for all $$x \in W$$, which says
$$T_W = \mathrm{id}_W$$. $$\square$$

> **Problem 2.1.7.** Let $$T \colon V \to V$$ be linear. Suppose that
> $$V = \operatorname{im}(T) \oplus W$$ and $$W$$ is $$T$$-invariant.
>
> - **(a)** Prove that $$W \subseteq \ker(T)$$.
> - **(b)** Show that if $$V$$ is finite-dimensional, then
>   $$W = \ker(T)$$.
{: .problem #prob-2-1-7 }

*Solution.* (a) Let $$x \in W$$. Then $$T(x) \in W$$ because $$W$$ is
$$T$$-invariant, and $$T(x) \in \operatorname{im}(T)$$. So

$$
T(x) \in \operatorname{im}(T) \cap W = \{\mathbf{0}\} ,
$$

that is, $$x \in \ker(T)$$.

(b) By [Problem 1.6.5][P1.6.5] with
$$\operatorname{im}(T) \cap W = \{\mathbf{0}\}$$,

$$
\dim V = \dim \operatorname{im}(T) + \dim W .
$$

By the [Dimension Theorem](#thm-2-3),
$$\dim V = \dim \operatorname{im}(T) + \dim \ker(T)$$. Hence
$$\dim W = \dim \ker(T)$$. Since $$W \le \ker(T)$$ by (a),
[Theorem 1.11][T1.11](c) gives $$W = \ker(T)$$. $$\square$$

> **Problem 2.1.8.** Let $$T \colon V \to V$$ be linear and suppose that
> $$W$$ is $$T$$-invariant. Prove that
> $$\ker(T_W) = \ker(T) \cap W$$ and
> $$\operatorname{im}(T_W) = T(W)$$.
{: .problem #prob-2-1-8 }

*Solution.* A vector $$x$$ lies in $$\ker(T_W)$$ exactly when $$x \in W$$
and $$T_W(x) = T(x) = \mathbf{0}$$, that is, when
$$x \in \ker(T) \cap W$$. And

$$
\operatorname{im}(T_W) = \{\, T_W(x) : x \in W \,\}
= \{\, T(x) : x \in W \,\} = T(W) .
$$

$$\square$$

> **Problem 2.1.9.** Let $$V$$ be a finite-dimensional vector space and
> $$T \colon V \to V$$ be linear.
>
> - **(a)** Suppose that $$V = \operatorname{im}(T) + \ker(T)$$. Prove that
>   $$V = \operatorname{im}(T) \oplus \ker(T)$$.
> - **(b)** Suppose that
>   $$\operatorname{im}(T) \cap \ker(T) = \{\mathbf{0}\}$$. Prove that
>   $$V = \operatorname{im}(T) \oplus \ker(T)$$.
{: .problem #prob-2-1-9 }

*Solution.* By [Problem 1.6.5][P1.6.5] and the
[Dimension Theorem](#thm-2-3),

$$
\begin{aligned}
\dim\big(\operatorname{im}(T) + \ker(T)\big)
&= \operatorname{rank}(T) + \operatorname{nullity}(T)
 - \dim\big(\operatorname{im}(T) \cap \ker(T)\big) \\
&= \dim V - \dim\big(\operatorname{im}(T) \cap \ker(T)\big) .
\end{aligned}
$$

(a) If $$\operatorname{im}(T) + \ker(T) = V$$, the left side is
$$\dim V$$, so
$$\dim(\operatorname{im}(T) \cap \ker(T)) = 0$$ and the intersection is
$$\{\mathbf{0}\}$$.

(b) If the intersection is $$\{\mathbf{0}\}$$, then
$$\dim(\operatorname{im}(T) + \ker(T)) = \dim V$$, so
$$\operatorname{im}(T) + \ker(T) = V$$ by [Theorem 1.11][T1.11](c).

In both cases both conditions of the [direct sum][D-directsum] hold.
$$\square$$

Finite dimension is essential: for the left shift on sequences,
$$T(a_1, a_2, \dots) = (a_2, a_3, \dots)$$, the image is everything and the
kernel is not zero, so (a) fails.

---

## §2.2 The Matrix Representation of a Linear Transformation

> **Definition (Ordered basis).** Let $$\dim V < \infty$$. An **ordered
> basis** for $$V$$ is a basis for $$V$$ with a specific order.
{: .definition #def-ordered-basis }

**Examples.** $$\varepsilon_n = \{e_1, e_2, \dots, e_n\}$$ is the
**standard ordered basis** for $$\mathbb{F}^n$$, and
$$\{1, x, x^2, \dots, x^n\}$$ is the standard ordered basis for
$$P_n(\mathbb{F})$$.

> **Definition (Coordinate vector).** Let
> $$\beta = \{u_1, u_2, \dots, u_n\}$$ be an ordered basis for $$V$$. For
> $$v \in V$$ write
>
> $$v = a_1 u_1 + a_2 u_2 + \cdots + a_n u_n ,$$
>
> where the $$a_i$$ are uniquely determined by $$v$$ and $$\beta$$
> ([Theorem 1.8][T1.8]). The **coordinate vector** of $$v$$ relative to
> $$\beta$$ is the element of $$\mathbb{F}^n$$
>
> $$[v]_\beta = \begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_n \end{pmatrix} .$$
{: .definition #def-coordinate-vector }

**Example.** For $$\beta = \{1, x, x^2\}$$ in $$P_2(\mathbb{R})$$,
$$[4 + 6x - 7x^2]_\beta = (4, 6, -7)^t$$.

> **Exercise 2.2.8.** For any ordered basis $$\beta$$ of an
> $$n$$-dimensional $$V$$, the map $$V \to \mathbb{F}^n$$ given by
> $$v \mapsto [v]_\beta$$ is linear.
{: .theorem #ex-2-2-8 }

*Proof.* If $$x = \sum a_i u_i$$ and $$y = \sum b_i u_i$$, then
$$cx + y = \sum (c a_i + b_i) u_i$$, so the $$i$$-th coordinate of
$$cx + y$$ is $$c a_i + b_i$$. That is,
$$[cx + y]_\beta = c\,[x]_\beta + [y]_\beta$$. $$\square$$

> **Definition (Matrix representation).** Let $$T \colon V \to W$$ be
> linear, and let $$\beta = \{v_1, v_2, \dots, v_n\}$$ and
> $$\gamma = \{w_1, w_2, \dots, w_m\}$$ be ordered bases for $$V$$ and
> $$W$$. There are uniquely determined scalars $$a_{ij} \in \mathbb{F}$$
> such that
>
> $$T(v_j) = a_{1j} w_1 + a_{2j} w_2 + \cdots + a_{mj} w_m
> \qquad (j = 1, \dots, n) .$$
>
> The $$m \times n$$ matrix $$A = (a_{ij})$$ is the **matrix
> representation** of $$T$$ with respect to the ordered bases $$\beta$$ and
> $$\gamma$$, written $$A = [T]_\beta^\gamma$$. When $$V = W$$ and
> $$\beta = \gamma$$, we write $$A = [T]_\beta$$.
{: .definition #def-matrix-representation }

**Notes.**

- **(a)** The $$j$$-th column of $$[T]_\beta^\gamma$$ is
  $$[T(v_j)]_\gamma$$. Mind the order of the indices: the coefficients of
  $$T(v_j)$$ run down a column.
- **(b)** If $$U \colon V \to W$$ is also linear and
  $$[T]_\beta^\gamma = [U]_\beta^\gamma$$, then $$T = U$$. Indeed, equal
  columns give $$T(v_j) = U(v_j)$$ for every $$j$$, and the
  [Corollary to Theorem 2.6](#cor-2-6) applies.

**Examples.**

- $$[T_0]_\beta^\gamma = O_{m \times n}$$ and
  $$[\mathrm{id}_V]_\beta = I_n$$.
- For $$T \colon \mathbb{R}^2 \to \mathbb{R}^3$$,
  $$(a_1, a_2) \mapsto (a_1 + 3a_2,\ 0,\ 2a_1 - 4a_2)$$, with the standard
  ordered bases, $$T(e_1) = (1, 0, 2)$$ and $$T(e_2) = (3, 0, -4)$$, so

  $$
  [T]_{\varepsilon_2}^{\varepsilon_3}
  = \begin{pmatrix} 1 & 3 \\ 0 & 0 \\ 2 & -4 \end{pmatrix} .
  $$

> **Definition (Sum and scalar multiple of functions).** Let
> $$U, T \colon V \to W$$ be functions and let $$a \in \mathbb{F}$$. Define
> $$U + T \colon V \to W$$ and $$aT \colon V \to W$$ by
>
> $$(U + T)(v) = U(v) + T(v), \qquad (aT)(v) = a\,T(v)
> \qquad (v \in V) .$$
{: .definition #def-sum-of-maps }

> **Theorem 2.7.** Let $$U, T \colon V \to W$$ be linear and
> $$a \in \mathbb{F}$$.
>
> - **(a)** $$aU + T$$ is linear.
> - **(b)** The set of all linear transformations from $$V$$ to $$W$$, with
>   the operations above, is an $$\mathbb{F}$$-vector space.
{: .theorem #thm-2-7 }

*Proof.* (a) For $$x, y \in V$$ and $$c \in \mathbb{F}$$,

$$
\begin{aligned}
(aU + T)(cx + y) &= a\,U(cx + y) + T(cx + y) \\
&= a\big(c\,U(x) + U(y)\big) + c\,T(x) + T(y) \\
&= c\big(a\,U(x) + T(x)\big) + \big(a\,U(y) + T(y)\big) \\
&= c\,(aU + T)(x) + (aU + T)(y) .
\end{aligned}
$$

(b) The set of all functions $$V \to W$$ with these pointwise operations is
a vector space; the axioms hold because they hold in $$W$$ at each point.
The linear ones form a subspace by [Theorem 1.3][T1.3]: the zero function
$$T_0$$ is linear, and sums and scalar multiples of linear maps are linear
by (a). The zero vector is $$T_0$$ and the additive inverse of $$T$$ is
$$(-1)T$$. $$\square$$

> **Notation.** $$\mathcal{L}(V, W) = \{\, T \colon V \to W \text{ linear}
> \,\}$$ and $$\mathcal{L}(V) = \mathcal{L}(V, V)$$.
{: .definition #def-L-V-W }

> **Theorem 2.8.** Let $$V$$ and $$W$$ be finite-dimensional with ordered
> bases $$\beta$$ and $$\gamma$$, and let $$T, U \in \mathcal{L}(V, W)$$.
>
> - **(a)** $$[T + U]_\beta^\gamma = [T]_\beta^\gamma + [U]_\beta^\gamma$$.
> - **(b)** $$[aT]_\beta^\gamma = a\,[T]_\beta^\gamma$$ for
>   $$a \in \mathbb{F}$$.
{: .theorem #thm-2-8 }

*Proof.* Compare $$j$$-th columns, using
[Exercise 2.2.8](#ex-2-2-8):

$$
[(T + U)(v_j)]_\gamma = [T(v_j) + U(v_j)]_\gamma
= [T(v_j)]_\gamma + [U(v_j)]_\gamma , \qquad
[(aT)(v_j)]_\gamma = a\,[T(v_j)]_\gamma .
$$

$$\square$$

So the map $$\mathcal{L}(V, W) \to \mathrm{Mat}_{m \times n}(\mathbb{F})$$,
$$T \mapsto [T]_\beta^\gamma$$, is linear. It is an isomorphism by
[Theorem 2.20][thm-2-20].

> **Exercise 2.2.11.** Let $$T \colon V \to V$$ be linear, let $$W \le V$$
> be $$T$$-invariant, and let $$\dim W = k$$ and $$\dim V = n$$. Then
> there exists an ordered basis $$\beta$$ for $$V$$ such that
>
> $$[T]_\beta = \begin{pmatrix} A & B \\ O & C \end{pmatrix},$$
>
> where $$A \in \mathrm{Mat}_{k \times k}(\mathbb{F})$$,
> $$B \in \mathrm{Mat}_{k \times (n-k)}(\mathbb{F})$$ and
> $$C \in \mathrm{Mat}_{(n-k) \times (n-k)}(\mathbb{F})$$.
{: .theorem #ex-2-2-11 }

*Proof.* Take an ordered basis $$\{v_1, \dots, v_k\}$$ of $$W$$ and extend
it, by the [Basis Extension Theorem][C1.11], to an ordered basis
$$\beta = \{v_1, \dots, v_k, v_{k+1}, \dots, v_n\}$$ of $$V$$. For
$$j \le k$$, $$T(v_j) \in W = \operatorname{span}\{v_1, \dots, v_k\}$$
because $$W$$ is $$T$$-invariant, so the coordinates of $$T(v_j)$$ on
$$v_{k+1}, \dots, v_n$$ are zero. These are the entries of the first $$k$$
columns of $$[T]_\beta$$ below row $$k$$. $$\square$$

The block $$A$$ is the matrix of the restriction $$T_W$$ in the basis
$$\{v_1, \dots, v_k\}$$.

### Problems for §2.2

> **Problem 2.2.1.** Let $$V$$ be the vector space of complex numbers over
> the field $$\mathbb{R}$$. Define $$T \colon V \to V$$ by
> $$T(z) = \bar{z}$$, where $$\bar{z}$$ is the complex conjugate of
> $$z$$. Prove that $$T$$ is linear, and compute $$[T]_\beta$$, where
> $$\beta = \{1, i\}$$.
{: .problem #prob-2-2-1 }

*Solution.* For $$z, w \in \mathbb{C}$$ and a **real** scalar $$c$$,

$$
T(cz + w) = \overline{cz + w} = \bar{c}\,\bar{z} + \bar{w}
= c\,\bar{z} + \bar{w} = c\,T(z) + T(w) ,
$$

since $$\bar{c} = c$$ for real $$c$$. So $$T$$ is linear over
$$\mathbb{R}$$.

For the matrix, $$T(1) = 1 = 1 \cdot 1 + 0 \cdot i$$ and
$$T(i) = -i = 0 \cdot 1 + (-1) \cdot i$$. These coordinate vectors are the
columns:

$$
[T]_\beta = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} .
$$

$$\square$$

$$T$$ is not linear when $$\mathbb{C}$$ is regarded as a vector space over
$$\mathbb{C}$$: $$T(i \cdot 1) = -i$$ but $$i\,T(1) = i$$.

> **Problem 2.2.2.** Let $$\beta = \{v_1, v_2, \dots, v_n\}$$ be a basis
> for a vector space $$V$$ and $$T \colon V \to V$$ be a linear
> transformation. Prove that $$[T]_\beta$$ is upper triangular if and only
> if $$T(v_j) \in \operatorname{span}(\{v_1, v_2, \dots, v_j\})$$ for
> $$j = 1, 2, \dots, n$$.
{: .problem #prob-2-2-2 }

The sheet prints $$T(v_j) \in \{v_1, \dots, v_j\}$$; the span is meant.

*Solution.* Let $$A = [T]_\beta$$, so that
$$T(v_j) = \sum_{i=1}^{n} A_{ij} v_i$$. Upper triangular means
$$A_{ij} = 0$$ whenever $$i > j$$.

($$\Rightarrow$$) If $$A_{ij} = 0$$ for $$i > j$$, then
$$T(v_j) = \sum_{i \le j} A_{ij} v_i \in
\operatorname{span}\{v_1, \dots, v_j\}$$.

($$\Leftarrow$$) If $$T(v_j) = \sum_{i \le j} c_i v_i$$, then by the
uniqueness of coordinates ([Theorem 1.8][T1.8]) $$A_{ij} = c_i$$ for
$$i \le j$$ and $$A_{ij} = 0$$ for $$i > j$$. $$\square$$

In the terms of [Exercise 2.2.11](#ex-2-2-11): $$[T]_\beta$$ is upper
triangular exactly when every $$\operatorname{span}\{v_1, \dots, v_j\}$$ is
$$T$$-invariant.

> **Problem 2.2.3.** Let $$V$$ and $$W$$ be vector spaces, and let $$T$$
> and $$U$$ be nonzero linear transformations from $$V$$ into $$W$$. If
> $$\operatorname{im}(T) \cap \operatorname{im}(U) = \{\mathbf{0}\}$$,
> prove that $$\{T, U\}$$ is a linearly independent subset of
> $$\mathcal{L}(V, W)$$.
{: .problem #prob-2-2-3 }

*Solution.* Suppose $$aT + bU = T_0$$, the zero vector of
$$\mathcal{L}(V, W)$$. For every $$x \in V$$,

$$
a\,T(x) = -b\,U(x), \qquad
a\,T(x) = T(ax) \in \operatorname{im}(T), \quad
-b\,U(x) = U(-bx) \in \operatorname{im}(U) ,
$$

so $$a\,T(x) \in \operatorname{im}(T) \cap \operatorname{im}(U) =
\{\mathbf{0}\}$$. Since $$T \ne T_0$$, choose $$x$$ with
$$T(x) \ne \mathbf{0}$$; then $$a\,T(x) = \mathbf{0}$$ forces $$a = 0$$.
The same argument with $$U$$ gives $$b = 0$$.

So only the trivial combination vanishes. In particular $$T \ne U$$, so
$$\{T, U\}$$ is a linearly independent set of two vectors. $$\square$$

---

## §2.3 Composition of Linear Transformations and Matrix Multiplication

> **Theorem 2.9.** Let $$T \colon V \to W$$ and $$U \colon W \to Z$$ be
> linear. Then $$UT = U \circ T \colon V \to Z$$ is linear.
{: .theorem #thm-2-9 }

*Proof.* $$UT(cx + y) = U\big(c\,T(x) + T(y)\big) = c\,UT(x) + UT(y)$$.
$$\square$$

> **Notation.** For $$T \colon V \to V$$ we write $$T^0 = \mathrm{id}_V$$,
> $$T^1 = T$$, $$T^2 = TT$$, and $$T^{k+1} = T\,T^k$$.
{: .definition #def-powers }

> **Theorem 2.10.** Let $$T, U_1, U_2 \in \mathcal{L}(V)$$. Then
>
> - **(a)** $$T(U_1 + U_2) = TU_1 + TU_2$$ and
>   $$(U_1 + U_2)T = U_1 T + U_2 T$$;
> - **(b)** $$T(U_1 U_2) = (TU_1)U_2$$;
> - **(c)** $$T\,\mathrm{id}_V = \mathrm{id}_V\,T = T$$;
> - **(d)** $$a(U_1 U_2) = (aU_1)U_2 = U_1(aU_2)$$ for all
>   $$a \in \mathbb{F}$$.
{: .theorem #thm-2-10 }

*Proof.* Evaluate at $$x \in V$$. (a) By the linearity of $$T$$,
$$T\big(U_1(x) + U_2(x)\big) = TU_1(x) + TU_2(x)$$; the second identity is
the definition of the sum, $$(U_1 + U_2)(T(x)) = U_1 T(x) + U_2 T(x)$$.
(b) Composition of functions is associative. (c) is immediate. (d)
$$a\,U_1(U_2(x)) = (aU_1)(U_2(x))$$ by definition, and
$$a\,U_1(U_2(x)) = U_1(a\,U_2(x))$$ by the linearity of $$U_1$$.
$$\square$$

The same identities hold, with the same proofs, for maps between different
spaces whenever the compositions are defined.

> **Definition (Matrix product, identity matrix, transpose).** For
> $$A \in \mathrm{Mat}_{m \times n}(\mathbb{F})$$ and
> $$B \in \mathrm{Mat}_{n \times p}(\mathbb{F})$$, the **product**
> $$AB \in \mathrm{Mat}_{m \times p}(\mathbb{F})$$ is
>
> $$(AB)_{ij} = \sum_{k=1}^{n} A_{ik} B_{kj} .$$
>
> The **Kronecker delta** is $$\delta_{ij} = 1$$ if $$i = j$$ and
> $$\delta_{ij} = 0$$ otherwise, and the $$n \times n$$ **identity
> matrix** is $$(I_n)_{ij} = \delta_{ij}$$. The **transpose** of
> $$A \in \mathrm{Mat}_{m \times n}(\mathbb{F})$$ is the $$n \times m$$
> matrix with $$(A^t)_{ij} = A_{ji}$$.
{: .definition #def-matrix-product }

The transpose satisfies $$(A^t)^t = A$$, $$(cA)^t = cA^t$$,
$$(A + B)^t = A^t + B^t$$ and $$(AB)^t = B^t A^t$$. For the last,
$$((AB)^t)_{ij} = (AB)_{ji} = \sum_k A_{jk} B_{ki}
= \sum_k (B^t)_{ik} (A^t)_{kj} = (B^t A^t)_{ij}$$.

> **Theorem 2.11.** Let $$V$$, $$W$$, $$Z$$ be finite-dimensional with
> ordered bases $$\alpha$$, $$\beta$$, $$\gamma$$, and let
> $$T \colon V \to W$$ and $$U \colon W \to Z$$ be linear. Then
>
> $$[UT]_\alpha^\gamma = [U]_\beta^\gamma\,[T]_\alpha^\beta .$$
{: .theorem #thm-2-11 }

*Proof.* Let $$\alpha = \{v_1, \dots, v_n\}$$,
$$\beta = \{w_1, \dots, w_m\}$$, $$\gamma = \{z_1, \dots, z_p\}$$,
$$A = [U]_\beta^\gamma$$ and $$B = [T]_\alpha^\beta$$. For each $$j$$,

$$
\begin{aligned}
UT(v_j) &= U\Big(\sum_{k=1}^{m} B_{kj} w_k\Big)
= \sum_{k=1}^{m} B_{kj}\,U(w_k) \\
&= \sum_{k=1}^{m} B_{kj} \sum_{i=1}^{p} A_{ik} z_i
= \sum_{i=1}^{p} \Big(\sum_{k=1}^{m} A_{ik} B_{kj}\Big) z_i
= \sum_{i=1}^{p} (AB)_{ij}\, z_i .
\end{aligned}
$$

So the $$(i, j)$$ entry of $$[UT]_\alpha^\gamma$$ is $$(AB)_{ij}$$.
$$\square$$

Matrix multiplication is defined the way it is so that this theorem holds.

> **Corollary to Theorem 2.11.** Let $$V$$ be finite-dimensional with
> ordered basis $$\beta$$ and let $$T, U \in \mathcal{L}(V)$$. Then
> $$[UT]_\beta = [U]_\beta\,[T]_\beta$$.
{: .theorem #cor-2-11 }

> **Theorem 2.12.** Let $$A$$ be $$m \times n$$, and let the other matrices
> have sizes for which the expressions are defined. Then
>
> - **(a)** $$A(B + C) = AB + AC$$ and $$(D + E)A = DA + EA$$;
> - **(b)** $$t(AB) = (tA)B = A(tB)$$ for $$t \in \mathbb{F}$$;
> - **(c)** $$I_m A = A = A I_n$$.
{: .theorem #thm-2-12 }

*Proof.* Compare entries. (a)
$$\sum_k A_{ik}(B_{kj} + C_{kj}) = \sum_k A_{ik} B_{kj} + \sum_k A_{ik}
C_{kj}$$, and likewise on the other side. (b) All three have $$(i,j)$$
entry $$\sum_k t\,A_{ik} B_{kj}$$. (c)
$$(I_m A)_{ij} = \sum_k \delta_{ik} A_{kj} = A_{ij}$$ and
$$(A I_n)_{ij} = \sum_k A_{ik} \delta_{kj} = A_{ij}$$. $$\square$$

> **Theorem 2.13.** Let $$A \in \mathrm{Mat}_{m \times n}(\mathbb{F})$$ and
> $$B \in \mathrm{Mat}_{n \times p}(\mathbb{F})$$.
>
> - **(a)** The $$j$$-th column of $$AB$$ is $$A$$ times the $$j$$-th
>   column of $$B$$, and it is a linear combination of the columns of
>   $$A$$.
> - **(b)** The $$i$$-th row of $$AB$$ is the $$i$$-th row of $$A$$ times
>   $$B$$, and it is a linear combination of the rows of $$B$$.
> - **(c)** The $$j$$-th column of $$B$$ is $$B e_j$$.
{: .theorem #thm-2-13 }

*Proof.* Let $$a_k$$ denote the $$k$$-th column of $$A$$ and $$b_j$$ the
$$j$$-th column of $$B$$. The $$i$$-th entry of the $$j$$-th column of
$$AB$$ is

$$
(AB)_{ij} = \sum_{k=1}^{n} A_{ik} B_{kj} = (A b_j)_i ,
$$

and the same sum is the $$i$$-th entry of
$$\sum_k B_{kj}\, a_k$$. This is (a). Part (b) is the same computation
read along rows, and (c) is (a) applied to $$B I_p = B$$, whose $$j$$-th
column is $$B$$ times the $$j$$-th column $$e_j$$ of $$I_p$$. $$\square$$

In particular, for a column vector $$x \in \mathbb{F}^n$$,

$$
Ax = x_1 a_1 + x_2 a_2 + \cdots + x_n a_n .
$$

> **Theorem 2.14.** Let $$V$$ and $$W$$ be finite-dimensional with ordered
> bases $$\beta$$ and $$\gamma$$, and let $$T \colon V \to W$$ be linear.
> Then for each $$x \in V$$,
>
> $$[T(x)]_\gamma = [T]_\beta^\gamma\,[x]_\beta .$$
{: .theorem #thm-2-14 }

*Proof.* Let $$\beta = \{v_1, \dots, v_n\}$$ and
$$x = a_1 v_1 + \cdots + a_n v_n$$, so $$[x]_\beta = (a_1, \dots, a_n)^t$$.
By [Exercise 2.2.8](#ex-2-2-8),

$$
[T(x)]_\gamma = [a_1 T(v_1) + \cdots + a_n T(v_n)]_\gamma
= a_1 [T(v_1)]_\gamma + \cdots + a_n [T(v_n)]_\gamma .
$$

The vectors $$[T(v_j)]_\gamma$$ are the columns of $$[T]_\beta^\gamma$$, so
the right side is $$[T]_\beta^\gamma [x]_\beta$$ by
[Theorem 2.13](#thm-2-13). $$\square$$

**Example.** For $$D \colon P_3(\mathbb{R}) \to P_2(\mathbb{R})$$,
$$f \mapsto f'$$, with $$\beta = \{1, x, x^2, x^3\}$$ and
$$\gamma = \{1, x, x^2\}$$,

$$
[D]_\beta^\gamma = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 2 & 0 \\
0 & 0 & 0 & 3 \end{pmatrix} ,
$$

and multiplying it by $$[f]_\beta$$ gives $$[f']_\gamma$$.

> **Definition (Left-multiplication transformation).** Let
> $$A \in \mathrm{Mat}_{m \times n}(\mathbb{F})$$. The mapping
>
> $$L_A \colon \mathbb{F}^n \to \mathbb{F}^m, \qquad L_A(x) = Ax ,$$
>
> is a **left-multiplication transformation**. It is linear, by
> [Theorem 2.12](#thm-2-12).
{: .definition #def-left-multiplication }

> **Theorem 2.15.** Let
> $$A, B \in \mathrm{Mat}_{m \times n}(\mathbb{F})$$,
> $$D \in \mathrm{Mat}_{n \times p}(\mathbb{F})$$ and
> $$c \in \mathbb{F}$$, and let $$\varepsilon_n$$, $$\varepsilon_m$$ be the
> standard ordered bases for $$\mathbb{F}^n$$ and $$\mathbb{F}^m$$. Then
>
> - **(a)** $$[L_A]_{\varepsilon_n}^{\varepsilon_m} = A$$;
> - **(b)** $$L_A = L_B$$ if and only if $$A = B$$;
> - **(c)** $$L_{A+B} = L_A + L_B$$ and $$L_{cA} = c\,L_A$$;
> - **(d)** if $$T \colon \mathbb{F}^n \to \mathbb{F}^m$$ is linear, then
>   there exists a unique $$C \in \mathrm{Mat}_{m \times n}(\mathbb{F})$$
>   such that $$T = L_C$$; in fact
>   $$C = [T]_{\varepsilon_n}^{\varepsilon_m}$$;
> - **(e)** $$L_{AD} = L_A L_D$$;
> - **(f)** $$L_{I_n} = \mathrm{id}_{\mathbb{F}^n}$$ (the case $$m = n$$).
{: .theorem #thm-2-15 }

*Proof.* For a vector $$y$$ of $$\mathbb{F}^m$$,
$$[y]_{\varepsilon_m} = y$$.

(a) The $$j$$-th column of $$[L_A]_{\varepsilon_n}^{\varepsilon_m}$$ is
$$[L_A(e_j)]_{\varepsilon_m} = A e_j$$, the $$j$$-th column of $$A$$
([Theorem 2.13](#thm-2-13)(c)).

(b) If $$L_A = L_B$$, then
$$A = [L_A]_{\varepsilon_n}^{\varepsilon_m} =
[L_B]_{\varepsilon_n}^{\varepsilon_m} = B$$ by (a). The converse is clear.

(c) $$(A + B)x = Ax + Bx$$ and $$(cA)x = c(Ax)$$ by
[Theorem 2.12](#thm-2-12).

(d) Put $$C = [T]_{\varepsilon_n}^{\varepsilon_m}$$. By
[Theorem 2.14](#thm-2-14),
$$T(x) = [T(x)]_{\varepsilon_m} = C\,[x]_{\varepsilon_n} = Cx = L_C(x)$$.
Uniqueness is (b).

(e) For each $$j$$, by [Theorem 2.13](#thm-2-13),

$$
L_{AD}(e_j) = (AD)e_j = A(De_j) = L_A(L_D(e_j)) ,
$$

since $$(AD)e_j$$ is the $$j$$-th column of $$AD$$, which is $$A$$ times
the $$j$$-th column $$De_j$$ of $$D$$. The linear maps $$L_{AD}$$ and
$$L_A L_D$$ agree on a basis, so they are equal by the
[Corollary to Theorem 2.6](#cor-2-6).

(f) $$L_{I_n}(x) = I_n x = x$$ by [Theorem 2.12](#thm-2-12)(c).
$$\square$$

By (d), every linear map $$\mathbb{F}^n \to \mathbb{F}^m$$ comes from a
matrix.

> **Theorem 2.16.** If the
> products are defined, $$A(BC) = (AB)C$$.
{: .theorem #thm-2-16 }

*Proof.* By [Theorem 2.15](#thm-2-15)(e) and the associativity of
composition,

$$
L_{A(BC)} = L_A L_{BC} = L_A (L_B L_C) = (L_A L_B) L_C = L_{AB} L_C
= L_{(AB)C} ,
$$

and [Theorem 2.15](#thm-2-15)(b) gives $$A(BC) = (AB)C$$. $$\square$$

> **Exercise 2.3.17.** Let $$T \colon V \to V$$ be linear. Then $$T$$ is a
> projection if and only if $$T^2 = T$$. In that case $$T$$ is the
> projection on $$\operatorname{im}(T) = \{\, y : T(y) = y \,\}$$ along
> $$\ker(T)$$.
{: .theorem #ex-2-3-17 }

*Proof.* ($$\Rightarrow$$) Let $$T$$ be the projection on $$W_1$$ along
$$W_2$$. For $$x = x_1 + x_2$$,

$$
T^2(x) = T(T(x)) = T(x_1) = T(x_1 + \mathbf{0}) = x_1 = T(x) .
$$

($$\Leftarrow$$) Let $$T^2 = T$$. Every $$x \in V$$ is

$$
x = T(x) + \big(x - T(x)\big), \qquad T(x) \in \operatorname{im}(T),
\qquad T\big(x - T(x)\big) = T(x) - T^2(x) = \mathbf{0} ,
$$

so $$V = \operatorname{im}(T) + \ker(T)$$. If
$$y = T(x) \in \operatorname{im}(T) \cap \ker(T)$$, then
$$\mathbf{0} = T(y) = T(T(x)) = T(x) = y$$. So
$$V = \operatorname{im}(T) \oplus \ker(T)$$, and the display shows that the
$$\operatorname{im}(T)$$-component of $$x$$ is $$T(x)$$: $$T$$ is the
projection on $$\operatorname{im}(T)$$ along $$\ker(T)$$. Finally, if
$$y = T(x)$$ then $$T(y) = T^2(x) = y$$, and if $$T(y) = y$$ then
$$y \in \operatorname{im}(T)$$; so
$$\operatorname{im}(T) = \{y : T(y) = y\}$$. $$\square$$

### Problems for §2.3

> **Problem 2.3.1.** Let $$V$$, $$W$$ and $$Z$$ be vector spaces, and let
> $$T \colon V \to W$$ and $$U \colon W \to Z$$ be linear.
>
> - **(a)** Prove that if $$UT$$ is one-to-one, then $$T$$ is one-to-one.
> - **(b)** Prove that if $$UT$$ is onto, then $$U$$ is onto.
> - **(c)** Prove that if $$U$$ and $$T$$ are bijective, then $$UT$$ is
>   also.
{: .problem #prob-2-3-1 }

*Solution.* (a) If $$T(x) = T(y)$$, then $$UT(x) = UT(y)$$, so
$$x = y$$ because $$UT$$ is one-to-one.

(b) Let $$z \in Z$$. Since $$UT$$ is onto, $$z = UT(x) = U(T(x))$$ for some
$$x \in V$$, so $$z$$ is the image under $$U$$ of $$T(x) \in W$$.

(c) *One-to-one.* If $$UT(x) = UT(y)$$, then $$T(x) = T(y)$$ because
$$U$$ is one-to-one, and then $$x = y$$ because $$T$$ is. *Onto.* Given
$$z \in Z$$, choose $$w \in W$$ with $$U(w) = z$$ and $$x \in V$$ with
$$T(x) = w$$; then $$UT(x) = z$$. $$\square$$

Linearity is not used; the statements hold for arbitrary functions.

> **Problem 2.3.2.** Let $$V$$ be a finite-dimensional vector space, and
> let $$T \colon V \to V$$ be linear.
>
> - **(a)** If $$\operatorname{rank}(T) = \operatorname{rank}(T^2)$$, prove
>   that $$\operatorname{im}(T) \cap \ker(T) = \{\mathbf{0}\}$$. Deduce
>   that $$V = \operatorname{im}(T) \oplus \ker(T)$$.
> - **(b)** Prove that
>   $$V = \operatorname{im}(T^k) \oplus \ker(T^k)$$ for some positive
>   integer $$k$$.
{: .problem #prob-2-3-2 }

*Solution.* (a) The subspace $$R = \operatorname{im}(T)$$ is
$$T$$-invariant, since $$T(R) \subseteq \operatorname{im}(T)$$. Consider
the restriction $$T_R \colon R \to R$$. By
[Problem 2.1.8](#prob-2-1-8),

$$
\operatorname{im}(T_R) = T(R) = \operatorname{im}(T^2), \qquad
\ker(T_R) = \ker(T) \cap R .
$$

Now $$\operatorname{im}(T^2) \le R$$ and
$$\dim \operatorname{im}(T^2) = \operatorname{rank}(T^2) =
\operatorname{rank}(T) = \dim R$$, so
$$\operatorname{im}(T^2) = R$$ by [Theorem 1.11][T1.11](c). Thus $$T_R$$
is onto, hence one-to-one by [Theorem 2.5](#thm-2-5), hence
$$\ker(T_R) = \{\mathbf{0}\}$$ by [Theorem 2.4](#thm-2-4). That is,
$$\operatorname{im}(T) \cap \ker(T) = \{\mathbf{0}\}$$, and
$$V = \operatorname{im}(T) \oplus \ker(T)$$ follows from
[Problem 2.1.9](#prob-2-1-9)(b).

(b) Since $$T^{m+1}(x) = T^m(T(x))$$,

$$
\operatorname{im}(T) \supseteq \operatorname{im}(T^2) \supseteq
\operatorname{im}(T^3) \supseteq \cdots ,
$$

so the ranks form a non-increasing sequence of non-negative integers. It
cannot decrease forever, so
$$\operatorname{rank}(T^k) = \operatorname{rank}(T^{k+1})$$ for some
$$k \ge 1$$, and then
$$\operatorname{im}(T^{k+1}) = \operatorname{im}(T^k)$$ by
[Theorem 1.11][T1.11](c).

From that point the images stop shrinking: if
$$\operatorname{im}(T^m) = \operatorname{im}(T^k)$$ for some
$$m \ge k$$, then

$$
\operatorname{im}(T^{m+1}) = T\big(\operatorname{im}(T^m)\big)
= T\big(\operatorname{im}(T^k)\big) = \operatorname{im}(T^{k+1})
= \operatorname{im}(T^k) .
$$

By induction $$\operatorname{im}(T^{2k}) = \operatorname{im}(T^k)$$, so
$$\operatorname{rank}\big((T^k)^2\big) = \operatorname{rank}(T^k)$$.
Part (a) applied to the linear map $$T^k$$ gives
$$V = \operatorname{im}(T^k) \oplus \ker(T^k)$$. $$\square$$

> **Problem 2.3.3.** Let $$V$$ be a vector space and $$T \colon V \to V$$
> be a linear transformation. Prove that $$T = T^2$$ if and only if $$T$$
> is a projection on $$W_1 = \{\, y : T(y) = y \,\}$$ along $$\ker(T)$$.
{: .problem #prob-2-3-3 }

*Solution.* This is [Exercise 2.3.17](#ex-2-3-17), proved above.

($$\Leftarrow$$) For a projection, $$T(x) = x_1 \in W_1$$ is fixed by
$$T$$, so $$T^2(x) = T(x_1) = x_1 = T(x)$$.

($$\Rightarrow$$) If $$T^2 = T$$, then
$$x = T(x) + (x - T(x))$$ with $$T(T(x)) = T(x)$$, so
$$T(x) \in W_1$$, and $$T(x - T(x)) = \mathbf{0}$$, so
$$x - T(x) \in \ker(T)$$. Hence $$V = W_1 + \ker(T)$$. If
$$y \in W_1 \cap \ker(T)$$, then $$y = T(y) = \mathbf{0}$$. So
$$V = W_1 \oplus \ker(T)$$, and $$T$$ sends
$$x$$ to its $$W_1$$-component $$T(x)$$. $$\square$$

---

## References

- Stephen H. Friedberg, Arnold J. Insel and Lawrence E. Spence, *Linear
  Algebra*, 5th edition, Pearson, 2018 — Chapter 2, §§2.1 to 2.3, and the
  exercises cited by number.
- Linear Algebra (881.007), Seoul National University, Fall 2023.
  Instructor: Jin Hong (홍진). Lecture slides for Chapter 2 and the course
  problem sheet for Chapter 2.
- The definitions, the statements of the theorems and their numbering are
  the slides'. The slides give most proofs as outlines, and the proofs here
  fill in those outlines. Where the slides state a result without proof, as
  with the matrix identities of Theorems 2.12, 2.13 and 2.16 and with
  Theorems 2.1, 2.10 and 2.15, the proof is written out here.
- The slides present the matrix identities and Theorem 2.14 before §2.2 and
  collect the exercises on direct sums, projections and invariant subspaces
  at the end. Here each result is placed in the textbook section it belongs
  to.
- The solutions to the problems are mine. The problem sheet writes
  $$N(T)$$ and $$R(T)$$ where these notes write $$\ker(T)$$ and
  $$\operatorname{im}(T)$$. Problem 2.2.2 is solved in a corrected form,
  stated at the problem.

[T1.3]: /posts/linear-algebra-vector-spaces/#thm-1-3
[T1.5]: /posts/linear-algebra-vector-spaces/#thm-1-5
[T1.11]: /posts/linear-algebra-vector-spaces-2/#thm-1-11
[C1.11]: /posts/linear-algebra-vector-spaces-2/#cor-1-11
[T1.8]: /posts/linear-algebra-vector-spaces-2/#thm-1-8
[D-directsum]: /posts/linear-algebra-vector-spaces/#def-direct-sum
[P1.4.4]: /posts/linear-algebra-vector-spaces/#prob-1-4-4
[P1.5.5]: /posts/linear-algebra-vector-spaces/#prob-1-5-5
[P1.6.6]: /posts/linear-algebra-vector-spaces-2/#prob-1-6-6
[P1.6.7]: /posts/linear-algebra-vector-spaces-2/#prob-1-6-7
[P1.7.3]: /posts/linear-algebra-vector-spaces-2/#prob-1-7-3
[E1.3.30]: /posts/linear-algebra-vector-spaces/#ex-1-3-30
[D-coset]: /posts/linear-algebra-vector-spaces-2/#def-coset
[P1.6.5]: /posts/linear-algebra-vector-spaces-2/#prob-1-6-5
[thm-2-20]: /posts/linear-algebra-linear-transformations-2/#thm-2-20
