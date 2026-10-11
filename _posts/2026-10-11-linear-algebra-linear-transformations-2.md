---
title: "Linear Algebra: Linear Transformations and Matrices (Part 2)"
date: 2026-10-11 01:10:00 +0900
categories: [Course Notes, Linear Algebra]
tags: [linear transformations, isomorphism, change of basis, dual space]
description: Definitions, theorems with proofs, and solved problems for Chapter 2 of Linear Algebra, §2.4 to §2.6 — invertibility and isomorphisms, the change of coordinate matrix, and dual spaces.
math: true
mermaid: false
render_with_liquid: false
---

> **How to read the labels.** This post continues
> [Chapter 2, Part 1](/posts/linear-algebra-linear-transformations/), which
> covers §2.1 to §2.3, and covers §2.4 to §2.6. The labels are as before:
> definitions, theorems and their numbers follow the lecture slides, which
> follow the textbook (Friedberg, Insel and Spence, 5th edition); an
> **Exercise a.b.c** is a textbook exercise that the lecture stated and used
> as a theorem; and a **Problem a.b.k** is the $$k$$-th question for §a.b on
> the course problem sheet. Results of Chapter 1 and of Part 1 are cited by
> number and link to the post that states them.
{: .prompt-info }

Throughout, $$V$$, $$W$$ and $$Z$$ are vector spaces over the same field
$$\mathbb{F}$$. The lecture writes $$\ker(T)$$ and $$\operatorname{im}(T)$$
where the textbook and the problem sheet write $$N(T)$$ and $$R(T)$$; these
notes use $$\ker$$ and $$\operatorname{im}$$. The identity map of $$V$$ is
$$\mathrm{id}_V$$ and the zero map is $$T_0$$.

---

## §2.4 Invertibility and Isomorphisms

> **Definition (Invertible function, inverse).** A function
> $$f \colon X \to Y$$ is **invertible** if there exists a function
> $$g \colon Y \to X$$ such that $$g \circ f = \mathrm{id}_X$$ and
> $$f \circ g = \mathrm{id}_Y$$. Such a $$g$$ is unique; it is the
> **inverse** of $$f$$, denoted $$f^{-1}$$.
{: .definition #def-invertible-function }

Uniqueness: if $$g$$ and $$g'$$ are both inverses, then
$$g = g \circ (f \circ g') = (g \circ f) \circ g' = g'$$.

**Notes.**

- **(a)** A function is invertible if and only if it is one-to-one and
  onto.
- **(b)** $$(f \circ g)^{-1} = g^{-1} \circ f^{-1}$$ for invertible $$f$$
  and $$g$$.
- **(c)** $$(f^{-1})^{-1} = f$$.
- **(d)** Let $$T \colon V \to W$$ be linear with $$V$$ and $$W$$ of the
  same finite dimension. Then the following are equivalent: $$T$$ is
  invertible; $$T$$ is one-to-one; $$T$$ is onto;
  $$\operatorname{rank}(T) = \dim V$$. This is [Theorem 2.5][thm-2-5]
  combined with (a).

> **Theorem 2.17.** If $$T \colon V \to W$$ is linear and invertible, then
> $$T^{-1} \colon W \to V$$ is linear.
{: .theorem #thm-2-17 }

*Proof.* Let $$y_1, y_2 \in W$$ and $$c \in \mathbb{F}$$. Since $$T$$ is
onto, $$y_1 = T(x_1)$$ and $$y_2 = T(x_2)$$ for some
$$x_1, x_2 \in V$$, and then $$x_i = T^{-1}(y_i)$$. So

$$
T^{-1}(cy_1 + y_2) = T^{-1}\big(c\,T(x_1) + T(x_2)\big)
= T^{-1}\big(T(cx_1 + x_2)\big) = cx_1 + x_2
= c\,T^{-1}(y_1) + T^{-1}(y_2) .
$$

$$\square$$

> **Corollary to Theorem 2.17.** Let $$T \colon V \to W$$ be linear and
> invertible. Then $$\dim V < \infty$$ if and only if
> $$\dim W < \infty$$, and in that case $$\dim V = \dim W$$.
{: .theorem #cor-2-17 }

*Proof.* ($$\Rightarrow$$) If $$\beta$$ is a finite basis of $$V$$, then
$$\operatorname{span}(T(\beta)) = \operatorname{im}(T) = W$$ by
[Theorem 2.2][thm-2-2], so $$W$$ is spanned by a finite set and is
finite-dimensional by [Theorem 1.9][T1.9].

($$\Leftarrow$$) Apply the same argument to the linear map $$T^{-1}$$
([Theorem 2.17](#thm-2-17)): for a finite basis $$\gamma$$ of $$W$$,
$$\operatorname{span}(T^{-1}(\gamma)) = V$$.

*Equality.* $$T$$ is one-to-one and onto, so
$$\operatorname{nullity}(T) = 0$$ and
$$\operatorname{rank}(T) = \dim W$$. By the
[Dimension Theorem][thm-2-3], $$\dim V = \dim W + 0$$. $$\square$$

> **Definition (Invertible matrix).** $$A \in \mathrm{Mat}_{n \times
> n}(\mathbb{F})$$ is **invertible** if there exists
> $$B \in \mathrm{Mat}_{n \times n}(\mathbb{F})$$ such that
> $$AB = I_n = BA$$. Such a $$B$$ is unique; it is the **inverse** of
> $$A$$, denoted $$A^{-1}$$.
{: .definition #def-invertible-matrix }

Uniqueness: if also $$AB' = I_n$$, then
$$B = B(AB') = (BA)B' = I_n B' = B'$$. Whether $$AB = I_n$$ alone already
makes $$A$$ invertible is [Problem 2.4.3](#prob-2-4-3).

> **Theorem 2.18.** Let $$V$$ and $$W$$ be finite-dimensional with ordered
> bases $$\beta$$ and $$\gamma$$, and let $$T \colon V \to W$$ be linear.
> Then $$T$$ is invertible if and only if $$[T]_\beta^\gamma$$ is
> invertible. When so,
>
> $$[T^{-1}]_\gamma^\beta = \big([T]_\beta^\gamma\big)^{-1} .$$
{: .theorem #thm-2-18 }

*Proof.* ($$\Rightarrow$$) If $$T$$ is invertible, then
$$\lvert\beta\rvert = \lvert\gamma\rvert = n$$ by the
[Corollary to Theorem 2.17](#cor-2-17), so $$[T]_\beta^\gamma$$ is square.
By [Theorem 2.11][thm-2-11],

$$
\begin{aligned}
[T^{-1}]_\gamma^\beta\,[T]_\beta^\gamma &= [T^{-1}T]_\beta
= [\mathrm{id}_V]_\beta = I_n , \\
[T]_\beta^\gamma\,[T^{-1}]_\gamma^\beta &= [TT^{-1}]_\gamma
= [\mathrm{id}_W]_\gamma = I_n .
\end{aligned}
$$

($$\Leftarrow$$) Let $$A = [T]_\beta^\gamma$$ be invertible. It is square,
so $$\lvert\beta\rvert = \lvert\gamma\rvert = n$$; write
$$\beta = \{v_1, \dots, v_n\}$$, $$\gamma = \{w_1, \dots, w_n\}$$ and
$$AB = BA = I_n$$. By the
[Linear Extension Theorem][thm-2-6] there is a linear
$$U \colon W \to V$$ with

$$
U(w_j) = \sum_{i=1}^{n} B_{ij} v_i \qquad (j = 1, \dots, n) ,
$$

and then $$[U]_\gamma^\beta = B$$. By [Theorem 2.11][thm-2-11],

$$
[UT]_\beta = [U]_\gamma^\beta [T]_\beta^\gamma = BA = I_n
= [\mathrm{id}_V]_\beta , \qquad
[TU]_\gamma = [T]_\beta^\gamma [U]_\gamma^\beta = AB = I_n
= [\mathrm{id}_W]_\gamma .
$$

Maps with equal matrices are equal
([Note (b) of §2.2][def-matrix-representation]), so
$$UT = \mathrm{id}_V$$ and $$TU = \mathrm{id}_W$$. $$\square$$

> **Corollary 1 to Theorem 2.18.** Let $$V$$ be finite-dimensional with
> ordered basis $$\beta$$ and let $$T \colon V \to V$$ be linear. Then
> $$T$$ is invertible if and only if $$[T]_\beta$$ is invertible, and then
> $$[T^{-1}]_\beta = ([T]_\beta)^{-1}$$.
{: .theorem #cor-2-18-1 }

> **Corollary 2 to Theorem 2.18.** Let
> $$A \in \mathrm{Mat}_{n \times n}(\mathbb{F})$$. Then $$L_A$$ is
> invertible if and only if $$A$$ is invertible, and then
> $$(L_A)^{-1} = L_{A^{-1}}$$.
{: .theorem #cor-2-18-2 }

*Proof.* $$[L_A]_\varepsilon = A$$ for the standard ordered basis
$$\varepsilon$$ ([Theorem 2.15][thm-2-15](a)), so the equivalence is
[Corollary 1](#cor-2-18-1). Moreover

$$
[(L_A)^{-1}]_\varepsilon = ([L_A]_\varepsilon)^{-1} = A^{-1}
= [L_{A^{-1}}]_\varepsilon ,
$$

and maps with equal matrices are equal. $$\square$$

> **Definition (Isomorphism, isomorphic).** $$V$$ is **isomorphic** to
> $$W$$, written $$V \approx W$$, if there exists an invertible linear
> transformation $$T \colon V \to W$$. Such a $$T$$ is an **isomorphism**.
{: .definition #def-isomorphism }

Being isomorphic is an equivalence relation: $$\mathrm{id}_V$$ is an
isomorphism; the inverse of an isomorphism is one
([Theorem 2.17](#thm-2-17)); and a composition of isomorphisms is one
([Theorem 2.9][thm-2-9] and [Problem 2.3.1][prob-2-3-1](c)).

**Example.** $$T \colon \mathbb{F}^2 \to P_1(\mathbb{F})$$,
$$(a_1, a_2) \mapsto a_1 + a_2 x$$, is an isomorphism: its matrix with
respect to $$\varepsilon_2$$ and $$\{1, x\}$$ is $$I_2$$, which is
invertible.

> **Theorem 2.19.** Let $$V$$ and $$W$$ be finite-dimensional. Then
> $$V \approx W$$ if and only if $$\dim V = \dim W$$.
{: .theorem #thm-2-19 }

*Proof.* ($$\Rightarrow$$) is the
[Corollary to Theorem 2.17](#cor-2-17).

($$\Leftarrow$$) Take bases $$\beta = \{v_1, \dots, v_n\}$$ of $$V$$ and
$$\gamma = \{w_1, \dots, w_n\}$$ of $$W$$. By the
[Linear Extension Theorem][thm-2-6] there is a linear
$$T \colon V \to W$$ with $$T(v_i) = w_i$$. Then
$$[T]_\beta^\gamma = I_n$$ is invertible, so $$T$$ is invertible by
[Theorem 2.18](#thm-2-18). $$\square$$

> **Corollary to Theorem 2.19.** $$V \approx \mathbb{F}^n$$ if and only if
> $$\dim V = n$$.
{: .theorem #cor-2-19 }

> **Theorem 2.20.** Let $$\dim V = n$$ and $$\dim W = m$$, with ordered
> bases $$\beta$$ and $$\gamma$$. Then
>
> $$\Phi_\beta^\gamma \colon \mathcal{L}(V, W) \to
> \mathrm{Mat}_{m \times n}(\mathbb{F}), \qquad T \mapsto [T]_\beta^\gamma ,$$
>
> is an isomorphism of vector spaces.
{: .theorem #thm-2-20 }

*Proof.* $$\Phi_\beta^\gamma$$ is linear by [Theorem 2.8][thm-2-8]:
$$[aT + U]_\beta^\gamma = a[T]_\beta^\gamma + [U]_\beta^\gamma$$. It is
one-to-one because maps with equal matrices are equal. It is onto: let
$$\beta = \{v_1, \dots, v_n\}$$, $$\gamma = \{w_1, \dots, w_m\}$$ and
$$A \in \mathrm{Mat}_{m \times n}(\mathbb{F})$$. The
[Linear Extension Theorem][thm-2-6] provides a linear
$$T \colon V \to W$$ with

$$
T(v_j) = \sum_{i=1}^{m} A_{ij} w_i \qquad (j = 1, \dots, n) ,
$$

and $$[T]_\beta^\gamma = A$$. $$\square$$

> **Corollary to Theorem 2.20.** If $$V$$ and $$W$$ are
> finite-dimensional, then
> $$\dim \mathcal{L}(V, W) = \dim V \cdot \dim W$$.
{: .theorem #cor-2-20 }

*Proof.* $$\dim \mathrm{Mat}_{m \times n}(\mathbb{F}) = mn$$, and
isomorphic spaces have the same dimension
([Corollary to Theorem 2.17](#cor-2-17)). $$\square$$

> **Definition (Standard representation).** Let $$\beta$$ be an ordered
> basis for $$V$$ with $$\dim V = n$$. The map
> $$\phi_\beta \colon V \to \mathbb{F}^n$$ given by
> $$v \mapsto [v]_\beta$$ is the **standard representation** of $$V$$ with
> respect to $$\beta$$.
{: .definition #def-standard-representation }

> **Theorem 2.21.** If $$\dim V = n$$ and $$\beta$$ is an ordered basis
> for $$V$$, then $$\phi_\beta \colon V \to \mathbb{F}^n$$ is an
> isomorphism.
{: .theorem #thm-2-21 }

*Proof.* $$\phi_\beta$$ is linear by [Exercise 2.2.8][ex-2-2-8]. If
$$[v]_\beta = \mathbf{0}$$, then $$v$$ is the combination of $$\beta$$
with all coefficients zero, so $$v = \mathbf{0}$$; thus
$$\ker(\phi_\beta) = \{\mathbf{0}\}$$ and $$\phi_\beta$$ is one-to-one
([Theorem 2.4][thm-2-4]). Since $$\dim V = \dim \mathbb{F}^n$$, it is
invertible by [Theorem 2.5][thm-2-5]. $$\square$$

![A commutative square: T maps V to W along the top, the coordinate maps phi beta and phi gamma go down to F n and F m, and left multiplication by A, the matrix of T, runs along the bottom](/assets/img/linear-algebra/coordinate-square.svg)

With $$A = [T]_\beta^\gamma$$, [Theorem 2.14][thm-2-14] says exactly that
this diagram commutes:

$$
\phi_\gamma \circ T = L_A \circ \phi_\beta .
$$

Under the identifications $$\phi_\beta$$ and $$\phi_\gamma$$, the map
$$T$$ *is* $$L_A$$.

> **Exercise 2.4.20.** Let $$T \colon V \to W$$ be linear with
> $$\dim V = n$$ and $$\dim W = m$$, let $$\beta$$ and $$\gamma$$ be
> ordered bases, and let $$A = [T]_\beta^\gamma$$. Then
>
> $$\operatorname{rank}(T) = \operatorname{rank}(L_A), \qquad
> \operatorname{nullity}(T) = \operatorname{nullity}(L_A) .$$
{: .theorem #ex-2-4-20 }

*Proof.* Since $$\phi_\beta$$ maps $$V$$ onto $$\mathbb{F}^n$$, the
commuting diagram gives

$$
\operatorname{im}(L_A) = L_A\big(\phi_\beta(V)\big)
= \phi_\gamma\big(T(V)\big) = \phi_\gamma\big(\operatorname{im}(T)\big) .
$$

The restriction of $$\phi_\gamma$$ to $$\operatorname{im}(T)$$ is a
one-to-one linear map onto
$$\phi_\gamma(\operatorname{im}(T))$$, so by the
[Dimension Theorem][thm-2-3] the two have the same dimension:
$$\operatorname{rank}(L_A) = \operatorname{rank}(T)$$. Both $$T$$ and
$$L_A$$ have an $$n$$-dimensional domain, so the Dimension Theorem again
gives
$$\operatorname{nullity}(T) = n - \operatorname{rank}(T) =
n - \operatorname{rank}(L_A) = \operatorname{nullity}(L_A)$$.
$$\square$$

### Problems for §2.4

> **Problem 2.4.1.** Let $$A$$ and $$B$$ be $$n \times n$$ invertible
> matrices. Prove that $$AB$$ is invertible and
> $$(AB)^{-1} = B^{-1}A^{-1}$$.
{: .problem #prob-2-4-1 }

*Solution.* By associativity ([Theorem 2.16][thm-2-16]) and
[Theorem 2.12][thm-2-12](c),

$$
\begin{aligned}
(AB)(B^{-1}A^{-1}) &= A(BB^{-1})A^{-1} = A I_n A^{-1} = AA^{-1} = I_n , \\
(B^{-1}A^{-1})(AB) &= B^{-1}(A^{-1}A)B = B^{-1} I_n B = B^{-1}B = I_n .
\end{aligned}
$$

So $$AB$$ is invertible, and by uniqueness of the inverse
$$(AB)^{-1} = B^{-1}A^{-1}$$. $$\square$$

> **Problem 2.4.2.** Let $$A$$ and $$B$$ be $$n \times n$$ matrices such
> that $$AB$$ is invertible. Prove that $$A$$ and $$B$$ are invertible.
{: .problem #prob-2-4-2 }

*Solution.* By [Corollary 2 to Theorem 2.18](#cor-2-18-2), $$L_{AB}$$ is
invertible, and $$L_{AB} = L_A L_B$$ by [Theorem 2.15][thm-2-15](e). So
$$L_A L_B$$ is one-to-one and onto. By [Problem 2.3.1][prob-2-3-1],
$$L_B$$ is one-to-one and $$L_A$$ is onto. Both are linear maps
$$\mathbb{F}^n \to \mathbb{F}^n$$, so by [Theorem 2.5][thm-2-5] each is
one-to-one and onto, that is, invertible. By
[Corollary 2](#cor-2-18-2) again, $$A$$ and $$B$$ are invertible.
$$\square$$

Squareness matters: for
$$A = \begin{pmatrix} 1 & 0 \end{pmatrix}$$ and
$$B = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$$, $$AB = I_1$$ is invertible
but $$A$$ and $$B$$ are not square.

> **Problem 2.4.3.** Let $$A$$ and $$B$$ be $$n \times n$$ matrices such
> that $$AB = I_n$$.
>
> - **(a)** Conclude that $$A$$ and $$B$$ are invertible.
> - **(b)** Prove $$A = B^{-1}$$.
{: .problem #prob-2-4-3 }

*Solution.* (a) $$I_n$$ is invertible, with inverse $$I_n$$. So $$AB$$ is
invertible, and $$A$$ and $$B$$ are invertible by
[Problem 2.4.2](#prob-2-4-2).

(b) Using (a), $$B^{-1}$$ exists, and

$$
A = A I_n = A(BB^{-1}) = (AB)B^{-1} = I_n B^{-1} = B^{-1} .
$$

Consequently $$BA = BB^{-1} = I_n$$ as well. $$\square$$

So for square matrices a one-sided inverse is automatically two-sided.

> **Problem 2.4.4.** Let $$V$$ and $$W$$ be $$n$$-dimensional vector
> spaces, and let $$T \colon V \to W$$ be a linear transformation. Suppose
> that $$\beta$$ is a basis for $$V$$. Prove that $$T$$ is an isomorphism
> if and only if $$T(\beta)$$ is a basis for $$W$$.
{: .problem #prob-2-4-4 }

*Solution.* ($$\Rightarrow$$) An isomorphism is one-to-one and onto, so
$$T(\beta)$$ is a basis for $$W$$ by [Problem 2.1.2][prob-2-1-2](c).

($$\Leftarrow$$) If $$T(\beta)$$ is a basis for $$W$$, then by
[Theorem 2.2][thm-2-2],

$$
\operatorname{im}(T) = \operatorname{span}(T(\beta)) = W ,
$$

so $$T$$ is onto. Since $$\dim V = \dim W = n$$, $$T$$ is also one-to-one
by [Theorem 2.5][thm-2-5]. So $$T$$ is an invertible linear map, an
isomorphism. $$\square$$

> **Problem 2.4.5.** Let $$B$$ be an $$n \times n$$ invertible matrix.
> Define $$\Phi \colon \mathrm{Mat}_{n \times n}(\mathbb{F}) \to
> \mathrm{Mat}_{n \times n}(\mathbb{F})$$ by $$\Phi(A) = B^{-1}AB$$. Prove
> that $$\Phi$$ is an isomorphism.
{: .problem #prob-2-4-5 }

*Solution.* *Linear.* By [Theorem 2.12][thm-2-12],

$$
\Phi(cA + C) = B^{-1}(cA + C)B = c\,B^{-1}AB + B^{-1}CB
= c\,\Phi(A) + \Phi(C) .
$$

*Invertible.* Define $$\Psi(A) = BAB^{-1}$$. By associativity
([Theorem 2.16][thm-2-16]),

$$
\Phi(\Psi(A)) = B^{-1}(BAB^{-1})B = (B^{-1}B)A(B^{-1}B) = A, \qquad
\Psi(\Phi(A)) = B(B^{-1}AB)B^{-1} = A .
$$

So $$\Psi$$ is the inverse of $$\Phi$$, and $$\Phi$$ is an invertible
linear map. $$\square$$

> **Problem 2.4.6.** Let $$V$$ and $$W$$ be finite-dimensional vector
> spaces and $$T \colon V \to W$$ be an isomorphism. Let $$V_0$$ be a
> subspace of $$V$$. Prove that $$\dim(V_0) = \dim(T(V_0))$$.
{: .problem #prob-2-4-6 }

This is part (b) of the textbook exercise; part (a), that $$T(V_0)$$ is a
subspace of $$W$$, is included in the solution.

*Solution.* Let $$T' \colon V_0 \to W$$ be $$T$$ restricted to $$V_0$$,
$$T'(x) = T(x)$$. It is linear, so
$$\operatorname{im}(T') = T(V_0)$$ is a subspace of $$W$$ by
[Theorem 2.1][thm-2-1]. Its kernel is
$$\ker(T) \cap V_0 = \{\mathbf{0}\}$$ because $$T$$ is one-to-one. By the
[Dimension Theorem][thm-2-3] applied to $$T'$$,

$$
\dim(V_0) = \operatorname{rank}(T') + \operatorname{nullity}(T')
= \dim(T(V_0)) + 0 .
$$

$$\square$$

Only the injectivity of $$T$$ is used.

> **Problem 2.4.7.** Let $$T \colon V \to W$$ be a linear transformation
> from an $$n$$-dimensional vector space $$V$$ to an $$m$$-dimensional
> vector space $$W$$. Let $$\beta$$ and $$\gamma$$ be ordered bases for
> $$V$$ and $$W$$, respectively. Prove that
> $$\operatorname{rank}(T) = \operatorname{rank}(L_A)$$ and
> $$\operatorname{nullity}(T) = \operatorname{nullity}(L_A)$$, where
> $$A = [T]_\beta^\gamma$$.
{: .problem #prob-2-4-7 }

*Solution.* This is [Exercise 2.4.20](#ex-2-4-20), proved above. By
[Theorem 2.14][thm-2-14],
$$\phi_\gamma(T(v)) = [T(v)]_\gamma = A[v]_\beta = L_A(\phi_\beta(v))$$
for all $$v$$, so

$$
\operatorname{im}(L_A) = L_A(\phi_\beta(V))
= \phi_\gamma(\operatorname{im}(T)) .
$$

$$\phi_\gamma$$ is an isomorphism ([Theorem 2.21](#thm-2-21)), so
[Problem 2.4.6](#prob-2-4-6) with $$V_0 = \operatorname{im}(T)$$ gives
$$\operatorname{rank}(L_A) = \operatorname{rank}(T)$$. Then, by the
[Dimension Theorem][thm-2-3] for both maps,

$$
\operatorname{nullity}(T) = n - \operatorname{rank}(T)
= n - \operatorname{rank}(L_A) = \operatorname{nullity}(L_A) .
$$

$$\square$$

---

## §2.5 The Change of Coordinate Matrix

> **Definition (Change of coordinate matrix).** Let $$V$$ be
> finite-dimensional with ordered bases $$\beta = \{v_1, \dots, v_n\}$$
> and $$\gamma = \{w_1, \dots, w_n\}$$. The matrix
>
> $$Q = [\mathrm{id}_V]_\beta^\gamma$$
>
> is a **change of coordinate matrix**. It changes $$\beta$$-coordinates
> into $$\gamma$$-coordinates, and its entries are given by
>
> $$v_j = \sum_{i=1}^{n} Q_{ij} w_i .$$
{: .definition #def-change-of-coordinates }

The $$j$$-th column of $$Q$$ is $$[v_j]_\gamma$$: the old basis vectors
written in the new basis.

> **Theorem 2.22.** Let $$V$$ be finite-dimensional with ordered bases
> $$\beta$$ and $$\gamma$$, and let
> $$Q = [\mathrm{id}_V]_\beta^\gamma$$. Then
>
> - **(a)** $$Q$$ is invertible, with
>   $$Q^{-1} = [\mathrm{id}_V]_\gamma^\beta$$;
> - **(b)** $$[v]_\gamma = Q\,[v]_\beta$$ for every $$v \in V$$.
{: .theorem #thm-2-22 }

*Proof.* (a) By [Theorem 2.11][thm-2-11],

$$
[\mathrm{id}_V]_\gamma^\beta\,[\mathrm{id}_V]_\beta^\gamma
= [\mathrm{id}_V\,\mathrm{id}_V]_\beta^\beta = [\mathrm{id}_V]_\beta = I ,
$$

and in the same way
$$[\mathrm{id}_V]_\beta^\gamma\,[\mathrm{id}_V]_\gamma^\beta = I$$.

(b) By [Theorem 2.14][thm-2-14],
$$[v]_\gamma = [\mathrm{id}_V(v)]_\gamma =
[\mathrm{id}_V]_\beta^\gamma\,[v]_\beta$$. $$\square$$

**Example.** In $$V = \mathbb{R}^2$$ take

$$
\beta = \left\{ \begin{pmatrix} 2/\sqrt5 \\ 1/\sqrt5 \end{pmatrix},
\begin{pmatrix} -1/\sqrt5 \\ 2/\sqrt5 \end{pmatrix} \right\}, \qquad
\varepsilon = \left\{ \begin{pmatrix} 1 \\ 0 \end{pmatrix},
\begin{pmatrix} 0 \\ 1 \end{pmatrix} \right\} .
$$

Then

$$
Q = [\mathrm{id}_V]_\beta^\varepsilon
= \begin{pmatrix} 2/\sqrt5 & -1/\sqrt5 \\ 1/\sqrt5 & 2/\sqrt5
\end{pmatrix} ,
\qquad
\begin{pmatrix} x \\ y \end{pmatrix}
= Q \begin{pmatrix} x' \\ y' \end{pmatrix} ,
$$

where $$(x, y)$$ are the standard coordinates and $$(x', y')$$ the
$$\beta$$-coordinates of the same point. Substituting
$$x = (2x' - y')/\sqrt5$$ and $$y = (x' + 2y')/\sqrt5$$ turns the curve

$$
2x^2 - 4xy + 5y^2 = 1 \quad\text{into}\quad (x')^2 + 6(y')^2 = 1 ,
$$

an ellipse whose axes lie along the vectors of $$\beta$$.

A linear transformation from a space to itself is a **linear operator**.

> **Theorem 2.23.** Let $$T \colon V \to V$$ be a linear operator on a
> finite-dimensional $$V$$, let $$\alpha$$ and $$\beta$$ be ordered bases
> for $$V$$, and let $$Q = [\mathrm{id}_V]_\alpha^\beta$$. Then
>
> $$[T]_\alpha = Q^{-1}\,[T]_\beta\,Q .$$
{: .theorem #thm-2-23 }

*Proof.* By [Theorem 2.11][thm-2-11] and
[Theorem 2.22](#thm-2-22)(a),

$$
\begin{aligned}
[T]_\alpha = [T\,\mathrm{id}_V]_\alpha^\alpha
&= [T]_\beta^\alpha\,[\mathrm{id}_V]_\alpha^\beta
= [\mathrm{id}_V\,T]_\beta^\alpha\,[\mathrm{id}_V]_\alpha^\beta \\
&= [\mathrm{id}_V]_\beta^\alpha\,[T]_\beta^\beta\,
[\mathrm{id}_V]_\alpha^\beta = Q^{-1}\,[T]_\beta\,Q .
\end{aligned}
$$

$$\square$$

**Example.** Let $$T$$ be the reflection of $$\mathbb{R}^2$$ about the
line $$y = 2x$$. With $$\beta = \{(1, 2), (2, -1)\}$$, a vector on the
line and a vector perpendicular to it,

$$
[T]_\beta = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}, \qquad
[\mathrm{id}]_\beta^\varepsilon = \begin{pmatrix} 1 & 2 \\ 2 & -1
\end{pmatrix}, \qquad
[\mathrm{id}]_\varepsilon^\beta
= \big([\mathrm{id}]_\beta^\varepsilon\big)^{-1}
= \frac15 \begin{pmatrix} 1 & 2 \\ 2 & -1 \end{pmatrix} .
$$

Hence

$$
[T]_\varepsilon = [\mathrm{id}]_\beta^\varepsilon\,[T]_\beta\,
[\mathrm{id}]_\varepsilon^\beta
= \frac15 \begin{pmatrix} -3 & 4 \\ 4 & 3 \end{pmatrix} .
$$

> **Definition (Similar matrices).**
> $$A, B \in \mathrm{Mat}_{n \times n}(\mathbb{F})$$ are **similar**,
> written $$A \sim B$$, if there exists an invertible
> $$Q \in \mathrm{Mat}_{n \times n}(\mathbb{F})$$ such that
> $$B = Q^{-1}AQ$$.
{: .definition #def-similar }

By [Theorem 2.23](#thm-2-23), $$[T]_\alpha \sim [T]_\beta$$: the matrices
of one operator in two bases are similar. Similarity is an equivalence
relation ([Problem 2.5.1](#prob-2-5-1)).

### Problems for §2.5

> **Problem 2.5.1.** Prove that "is similar to" is an equivalence relation
> on $$\mathrm{Mat}_{n \times n}(\mathbb{F})$$.
{: .problem #prob-2-5-1 }

*Solution.* *Reflexive.* $$A = I_n^{-1} A I_n$$, so $$A \sim A$$.

*Symmetric.* If $$B = Q^{-1}AQ$$, then multiplying by $$Q$$ on the left
and $$Q^{-1}$$ on the right gives
$$A = QBQ^{-1} = (Q^{-1})^{-1} B\,(Q^{-1})$$, and $$Q^{-1}$$ is
invertible. So $$B \sim A$$.

*Transitive.* If $$B = Q^{-1}AQ$$ and $$C = P^{-1}BP$$, then

$$
C = P^{-1}Q^{-1}AQP = (QP)^{-1} A\,(QP) ,
$$

where $$QP$$ is invertible with $$(QP)^{-1} = P^{-1}Q^{-1}$$ by
[Problem 2.4.1](#prob-2-4-1). So $$A \sim C$$. $$\square$$

> **Problem 2.5.2.** Prove that if $$A$$ and $$B$$ are similar
> $$n \times n$$ matrices, then
> $$\operatorname{tr}(A) = \operatorname{tr}(B)$$.
{: .problem #prob-2-5-2 }

*Solution.* First, $$\operatorname{tr}(CD) = \operatorname{tr}(DC)$$ for
any $$n \times n$$ matrices $$C$$ and $$D$$:

$$
\operatorname{tr}(CD) = \sum_{i=1}^{n} \sum_{k=1}^{n} C_{ik} D_{ki}
= \sum_{k=1}^{n} \sum_{i=1}^{n} D_{ki} C_{ik} = \operatorname{tr}(DC) .
$$

Now let $$B = Q^{-1}AQ$$. Taking $$C = Q^{-1}A$$ and $$D = Q$$,

$$
\operatorname{tr}(B) = \operatorname{tr}\big((Q^{-1}A)Q\big)
= \operatorname{tr}\big(Q(Q^{-1}A)\big) = \operatorname{tr}(A) .
$$

$$\square$$

So the trace of a linear operator on a finite-dimensional space can be
defined as the trace of its matrix in any basis.

---

## §2.6 Dual Spaces

> **Definition (Linear functional, dual space).** A **linear functional**
> on $$V$$ is a linear transformation from $$V$$ to its field of scalars
> $$\mathbb{F}$$. The **dual space** of $$V$$ is
>
> $$V^* = \mathcal{L}(V, \mathbb{F}) .$$
{: .definition #def-dual-space }

**Examples.**

- The **trace** $$\operatorname{tr} \colon
  \mathrm{Mat}_{n \times n}(\mathbb{F}) \to \mathbb{F}$$,
  $$A \mapsto \sum_i A_{ii}$$.
- A **Fourier coefficient**: on continuous functions
  $$f \colon [0, 2\pi] \to \mathbb{R}$$,

  $$
  f \mapsto \frac{1}{2\pi} \int_0^{2\pi} f(t) \cos(nt)\,dt .
  $$

**Note.** If $$V$$ is finite-dimensional, then $$\dim V^* = \dim V$$ by
the [Corollary to Theorem 2.20](#cor-2-20) with $$W = \mathbb{F}$$, so
$$V \approx V^* \approx V^{**}$$ by [Theorem 2.19](#thm-2-19), where
$$V^{**} = (V^*)^*$$ is the **double dual**. When $$V$$ is
infinite-dimensional, $$V^*$$ is much larger than $$V$$.

> **Theorem 2.24.** Let $$V$$ be finite-dimensional with ordered basis
> $$\beta = \{v_1, \dots, v_n\}$$, and let
> $$v_i^* \colon V \to \mathbb{F}$$ be the linear functional defined by
> $$v_i^*(v_j) = \delta_{ij}$$. Then for any $$f \in V^*$$,
>
> $$f = \sum_{i=1}^{n} f(v_i)\, v_i^* ,$$
>
> and $$\beta^* = \{v_1^*, \dots, v_n^*\}$$ is an ordered basis for
> $$V^*$$.
{: .theorem #thm-2-24 }

Each $$v_i^*$$ exists and is unique by the
[Linear Extension Theorem][thm-2-6].

*Proof.* The two sides of the claimed equality are linear functionals that
agree on the basis $$\beta$$:

$$
\Big(\sum_{i=1}^{n} f(v_i)\, v_i^*\Big)(v_j)
= \sum_{i=1}^{n} f(v_i)\,\delta_{ij} = f(v_j) .
$$

So they are equal by the [Corollary to Theorem 2.6][cor-2-6], and
$$\beta^*$$ spans $$V^*$$. If $$\sum_i a_i v_i^* = T_0$$, evaluating at
$$v_j$$ gives $$a_j = 0$$; so $$\beta^*$$ is linearly independent.
$$\square$$

> **Definition (Coordinate functions, dual basis).** The functionals
> $$v_i^*$$ are the **coordinate functions** with respect to $$\beta$$,
> and the ordered basis $$\beta^*$$ of $$V^*$$ is the **dual basis** of
> $$\beta$$.
{: .definition #def-dual-basis }

The name is explained by
$$v_i^*(a_1 v_1 + \cdots + a_n v_n) = a_i$$: the functional $$v_i^*$$
reads off the $$i$$-th coordinate.

**Note.** Each $$v_i^*$$ depends on the whole of $$\beta$$, not only on
$$v_i$$. For the basis $$\{v_1 = (1,0),\ v_2 = (0,1)\}$$ of
$$\mathbb{R}^2$$, $$(1,1) = 1v_1 + 1v_2$$, so $$v_1^*(1,1) = 1$$. For the
basis $$\{v_1 = (1,0),\ v_2 = (1,1)\}$$, $$(1,1) = 0v_1 + 1v_2$$, so
$$v_1^*(1,1) = 0$$, although $$v_1$$ is the same vector.

> **Theorem 2.25.** Let $$V$$ and $$W$$ be finite-dimensional with ordered
> bases $$\beta$$ and $$\gamma$$, and let $$T \colon V \to W$$ be linear.
> Then the map
>
> $$T^t \colon W^* \to V^*, \qquad T^t(f) = fT ,$$
>
> is linear, and
>
> $$[T^t]_{\gamma^*}^{\beta^*} = \big([T]_\beta^\gamma\big)^t .$$
{: .theorem #thm-2-25 }

> **Definition (Transpose of a linear transformation).** The map $$T^t$$
> of [Theorem 2.25](#thm-2-25) is the **transpose** of $$T$$.
{: .definition #def-transpose-map }

*Proof of Theorem 2.25.* *Well defined.* For $$f \in W^*$$, the
composition $$fT \colon V \to \mathbb{F}$$ is linear by
[Theorem 2.9][thm-2-9], so $$fT \in V^*$$.

*Linear.* $$T^t(cf + g) = (cf + g)T = c\,(fT) + gT
= c\,T^t(f) + T^t(g)$$.

*Matrix.* Let $$\beta = \{v_1, \dots, v_n\}$$ and
$$\gamma = \{w_1, \dots, w_m\}$$, with dual bases
$$\beta^* = \{v_1^*, \dots, v_n^*\}$$ and
$$\gamma^* = \{w_1^*, \dots, w_m^*\}$$. By
[Theorem 2.24](#thm-2-24),

$$
T^t(w_j^*) = \sum_{i=1}^{n} \big(T^t(w_j^*)\big)(v_i)\; v_i^* ,
$$

so the $$(i, j)$$ entry of $$[T^t]_{\gamma^*}^{\beta^*}$$ is

$$
\big(T^t(w_j^*)\big)(v_i) = (w_j^* T)(v_i) = w_j^*\big(T(v_i)\big)
= \big([T]_\beta^\gamma\big)_{ji} ,
$$

because $$w_j^*$$ reads off the $$j$$-th $$\gamma$$-coordinate of
$$T(v_i)$$, which is the $$(j, i)$$ entry of $$[T]_\beta^\gamma$$.
$$\square$$

For each $$x \in V$$ define

$$
\hat{x} \colon V^* \to \mathbb{F}, \qquad \hat{x}(f) = f(x) .
$$

It is linear, since

$$
\hat{x}(cf + g) = (cf + g)(x) = c\,f(x) + g(x)
= c\,\hat{x}(f) + \hat{x}(g) .
$$

In other words, $$\hat{x} \in (V^*)^* = V^{**}$$.

> **Lemma.** Let $$V$$ be finite-dimensional and $$x \in V$$. If
> $$\hat{x}(f) = 0$$ for all $$f \in V^*$$, then $$x = \mathbf{0}$$.
{: .theorem #lem-2-26 }

*Proof.* Suppose $$x \ne \mathbf{0}$$. Then $$\{x\}$$ is linearly
independent and extends to a basis
$$\{v_1 = x, v_2, \dots, v_n\}$$ of $$V$$
([Basis Extension Theorem][C1.10.2]). The first element of the dual basis
gives

$$
\hat{x}(v_1^*) = v_1^*(x) = v_1^*(v_1) = 1 \ne 0 ,
$$

a contradiction. $$\square$$

> **Theorem 2.26.** Let $$V$$ be finite-dimensional. Then the map
>
> $$\psi \colon V \to V^{**}, \qquad \psi(x) = \hat{x} ,$$
>
> is an isomorphism.
{: .theorem #thm-2-26 }

*Proof.* *Well defined.* $$\hat{x} \in V^{**}$$, as shown above.

*Linear.* For every $$f \in V^*$$,

$$
\psi(cx + y)(f) = f(cx + y) = c\,f(x) + f(y)
= \big(c\,\psi(x) + \psi(y)\big)(f) ,
$$

so $$\psi(cx + y) = c\,\psi(x) + \psi(y)$$.

*One-to-one.* If $$\psi(x)$$ is the zero functional, then
$$\hat{x}(f) = 0$$ for all $$f$$, so $$x = \mathbf{0}$$ by the
[Lemma](#lem-2-26). Thus $$\ker(\psi) = \{\mathbf{0}\}$$
([Theorem 2.4][thm-2-4]).

*Isomorphism.* $$\dim V = \dim V^{**}$$, so $$\psi$$ is invertible by
[Theorem 2.5][thm-2-5]. $$\square$$

Linearity has to be established before injectivity, because the kernel
criterion applies only to linear maps. The isomorphism $$\psi$$ is
**natural**: it is defined without choosing a basis, unlike an isomorphism
$$V \approx V^*$$.

> **Corollary to Theorem 2.26.** Let $$V$$ be finite-dimensional. Every
> ordered basis for $$V^*$$ is the dual basis of an ordered basis for
> $$V$$.
{: .theorem #cor-2-26 }

*Proof.* Let $$\gamma = \{f_1, f_2, \dots, f_n\}$$ be an ordered basis for
$$V^*$$, and let $$\gamma^* = \{f_1^*, \dots, f_n^*\} \subseteq V^{**}$$
be its dual basis. By [Theorem 2.26](#thm-2-26), each element of
$$\gamma^*$$ has the form

$$
f_j^* = \hat{x}_j \qquad \text{for a unique } x_j \in V .
$$

The set $$\beta = \{x_1, x_2, \dots, x_n\}$$ is a basis of $$V$$, because
it is the image of the basis $$\gamma^*$$ under the isomorphism
$$\psi^{-1}$$ ([Problem 2.1.2][prob-2-1-2](c)). Now

$$
f_i(x_j) = \hat{x}_j(f_i) = f_j^*(f_i) = \delta_{ij} ,
$$

so $$f_i$$ and the coordinate function $$x_i^*$$ agree on $$\beta$$, and
$$f_i = x_i^*$$ by the [Corollary to Theorem 2.6][cor-2-6]. Hence
$$\gamma = \beta^*$$. $$\square$$

### Problems for §2.6

> **Problem 2.6.1.** Let $$V = \mathbb{R}^3$$ and define
> $$f_1, f_2, f_3 \in V^*$$ as follows:
>
> $$f_1(x, y, z) = x - 2y, \qquad f_2(x, y, z) = x + y + z, \qquad
> f_3(x, y, z) = y - 3z .$$
>
> Prove that $$\{f_1, f_2, f_3\}$$ is a basis for $$V^*$$, and then find a
> basis for $$V$$ for which it is the dual basis.
{: .problem #prob-2-6-1 }

*Solution.* *Basis.* Suppose $$af_1 + bf_2 + cf_3$$ is the zero
functional. Evaluating at $$e_1$$, $$e_2$$, $$e_3$$ gives

$$
a + b = 0, \qquad -2a + b + c = 0, \qquad b - 3c = 0 .
$$

From the third and first equations, $$b = 3c$$ and $$a = -3c$$; the second
becomes $$6c + 3c + c = 10c = 0$$. So $$c = 0$$ and then $$a = b = 0$$.
The three functionals are linearly independent, and
$$\dim V^* = \dim V = 3$$, so they form a basis by
[Corollary 2 to Theorem 1.10][C1.10.2](b).

*The basis of $$V$$.* We need $$x_1, x_2, x_3 \in \mathbb{R}^3$$ with
$$f_i(x_j) = \delta_{ij}$$. Solve the system

$$
x - 2y = a, \qquad x + y + z = b, \qquad y - 3z = c
$$

for general $$a, b, c$$. The first equation gives $$x = a + 2y$$; the
second then gives $$z = b - a - 3y$$; the third gives
$$y - 3(b - a - 3y) = c$$, so $$10y = -3a + 3b + c$$. Hence

$$
x = \frac{2a + 3b + c}{5}, \qquad y = \frac{-3a + 3b + c}{10}, \qquad
z = \frac{-a + b - 3c}{10} .
$$

Taking $$(a, b, c) = (1,0,0)$$, $$(0,1,0)$$, $$(0,0,1)$$ in turn,

$$
x_1 = \Big(\tfrac25, -\tfrac{3}{10}, -\tfrac{1}{10}\Big), \qquad
x_2 = \Big(\tfrac35, \tfrac{3}{10}, \tfrac{1}{10}\Big), \qquad
x_3 = \Big(\tfrac15, \tfrac{1}{10}, -\tfrac{3}{10}\Big) .
$$

*Check.* $$f_1(x_1) = \tfrac25 + \tfrac{6}{10} = 1$$,
$$f_2(x_1) = \tfrac25 - \tfrac{3}{10} - \tfrac{1}{10} = 0$$,
$$f_3(x_1) = -\tfrac{3}{10} + \tfrac{3}{10} = 0$$; the other six values
are verified the same way.

*It is a basis, and $$\{f_i\}$$ is its dual.* If
$$c_1 x_1 + c_2 x_2 + c_3 x_3 = \mathbf{0}$$, applying $$f_i$$ gives
$$c_i = 0$$; so $$\beta = \{x_1, x_2, x_3\}$$ is a linearly independent set
of three vectors in $$\mathbb{R}^3$$, hence a basis. Its coordinate
functions satisfy $$x_i^*(x_j) = \delta_{ij} = f_i(x_j)$$, so
$$f_i = x_i^*$$ by the [Corollary to Theorem 2.6][cor-2-6]. Thus
$$\{f_1, f_2, f_3\} = \beta^*$$. $$\square$$

> **Problem 2.6.2.** Define $$f \in (\mathbb{R}^2)^*$$ by
> $$f(x, y) = 2x + y$$ and $$T \colon \mathbb{R}^2 \to \mathbb{R}^2$$ by
> $$T(x, y) = (3x + 2y,\ x)$$.
>
> - **(a)** Compute $$T^t(f)$$.
> - **(b)** Compute $$[T^t]_{\beta^*}$$, where $$\beta$$ is the standard
>   ordered basis for $$\mathbb{R}^2$$ and $$\beta^* = \{f_1, f_2\}$$ is
>   the dual basis.
{: .problem #prob-2-6-2 }

*Solution.* (a) By definition $$T^t(f) = fT$$, so

$$
T^t(f)(x, y) = f(3x + 2y,\ x) = 2(3x + 2y) + x = 7x + 4y .
$$

(b) The dual basis of the standard basis is $$f_1(x, y) = x$$,
$$f_2(x, y) = y$$. Then

$$
\begin{aligned}
T^t(f_1)(x, y) &= f_1(3x + 2y,\ x) = 3x + 2y, & T^t(f_1) &= 3f_1 + 2f_2 , \\
T^t(f_2)(x, y) &= f_2(3x + 2y,\ x) = x, & T^t(f_2) &= 1f_1 + 0f_2 .
\end{aligned}
$$

These coordinates are the columns:

$$
[T^t]_{\beta^*} = \begin{pmatrix} 3 & 1 \\ 2 & 0 \end{pmatrix} .
$$

*Check.* $$[T]_\beta = \begin{pmatrix} 3 & 2 \\ 1 & 0 \end{pmatrix}$$, and
its transpose is the matrix just found, as
[Theorem 2.25](#thm-2-25) requires. Also $$f = 2f_1 + f_2$$, and
$$[T^t]_{\beta^*} (2, 1)^t = (7, 4)^t$$ agrees with (a). $$\square$$

---

## References

- Stephen H. Friedberg, Arnold J. Insel and Lawrence E. Spence, *Linear
  Algebra*, 5th edition, Pearson, 2018 — Chapter 2, §§2.4 to 2.6, and the
  exercises cited by number.
- Linear Algebra (881.007), Seoul National University, Fall 2023.
  Instructor: Jin Hong (홍진). Lecture slides for Chapter 2 and the course
  problem sheet for Chapter 2.
- The definitions, the statements of the theorems and their numbering are
  the slides'. The slides give most proofs as outlines, and the proofs here
  fill in those outlines.
- The solutions to the problems are mine. The problem sheet writes
  $$N(T)$$ and $$R(T)$$ where these notes write $$\ker(T)$$ and
  $$\operatorname{im}(T)$$.

[thm-2-5]: /posts/linear-algebra-linear-transformations/#thm-2-5
[thm-2-2]: /posts/linear-algebra-linear-transformations/#thm-2-2
[T1.9]: /posts/linear-algebra-vector-spaces-2/#thm-1-9
[thm-2-3]: /posts/linear-algebra-linear-transformations/#thm-2-3
[thm-2-11]: /posts/linear-algebra-linear-transformations/#thm-2-11
[thm-2-6]: /posts/linear-algebra-linear-transformations/#thm-2-6
[def-matrix-representation]: /posts/linear-algebra-linear-transformations/#def-matrix-representation
[thm-2-15]: /posts/linear-algebra-linear-transformations/#thm-2-15
[thm-2-9]: /posts/linear-algebra-linear-transformations/#thm-2-9
[prob-2-3-1]: /posts/linear-algebra-linear-transformations/#prob-2-3-1
[thm-2-8]: /posts/linear-algebra-linear-transformations/#thm-2-8
[ex-2-2-8]: /posts/linear-algebra-linear-transformations/#ex-2-2-8
[thm-2-4]: /posts/linear-algebra-linear-transformations/#thm-2-4
[thm-2-14]: /posts/linear-algebra-linear-transformations/#thm-2-14
[thm-2-16]: /posts/linear-algebra-linear-transformations/#thm-2-16
[thm-2-12]: /posts/linear-algebra-linear-transformations/#thm-2-12
[prob-2-1-2]: /posts/linear-algebra-linear-transformations/#prob-2-1-2
[thm-2-1]: /posts/linear-algebra-linear-transformations/#thm-2-1
[cor-2-6]: /posts/linear-algebra-linear-transformations/#cor-2-6
[C1.10.2]: /posts/linear-algebra-vector-spaces-2/#cor-1-10-2
