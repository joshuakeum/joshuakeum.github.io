---
title: "Linear Algebra: Determinants (Part 1)"
date: 2026-10-11 02:00:00 +0900
categories: [Course Notes, Linear Algebra]
tags: [determinant, cofactor expansion, orientation, cramer's rule, classical adjoint]
description: Definitions, theorems with proofs, and solved problems for Chapter 4 of Linear Algebra, §4.1 to §4.3 — determinants of order 2, area and orientation, cofactor expansion, row operations, the product rule, Cramer's rule, and the classical adjoint.
math: true
mermaid: false
render_with_liquid: false
---

> **How to read the labels.** Definitions, theorems and their numbers follow
> the lecture slides, which follow the textbook (Friedberg, Insel and Spence,
> 5th edition). An **Exercise a.b.c** is a textbook exercise that the lecture
> stated and used as a theorem. A **Problem a.b.k** is the $$k$$-th question
> for §a.b on the course problem sheet, with the textbook's exercise number
> in parentheses. Results of Chapters 1 to 3 are cited by number and link to
> the post that states them. Chapter 4 is split over two posts: this one
> covers §4.1 to §4.3, and
> [Part 2](/posts/linear-algebra-determinants-2/) covers §4.5 and the
> lecture on finite fields. §4.4 of the textbook is a summary of §4.1 to
> §4.3 and has no separate section here.
{: .prompt-info }

Throughout, $$\mathbb{F}$$ is a field and matrices are square unless stated
otherwise. In this chapter a matrix is often described by its rows: for row
vectors $$a_1, \dots, a_n \in \mathbb{F}^n$$,

$$
\begin{pmatrix} a_1 \\ \vdots \\ a_n \end{pmatrix}
$$

is the $$n \times n$$ matrix whose $$i$$-th row is $$a_i$$. Here
$$e_1, \dots, e_n$$ denote the standard vectors written as rows, so that
the matrix with rows $$e_1, \dots, e_n$$ is $$I_n$$.

---

## §4.1 Determinants of Order 2

> **Definition (Determinant of a $$2 \times 2$$ matrix).** The
> **determinant** of
> $$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}
> \in \mathrm{Mat}_{2 \times 2}(\mathbb{F})$$
> is the scalar
>
> $$\det A = \lvert A \rvert = ad - bc .$$
{: .definition #def-det-2 }

**Example.**
$$\det \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} = 1 \cdot 4 - 2 \cdot 3 = -2$$
and
$$\det \begin{pmatrix} 3 & 2 \\ 6 & 4 \end{pmatrix} = 3 \cdot 4 - 2 \cdot 6 = 0$$,
but the sum of the two matrices has

$$
\det \begin{pmatrix} 4 & 4 \\ 9 & 8 \end{pmatrix} = 32 - 36 = -4 \ne -2 + 0 .
$$

So $$\det \colon \mathrm{Mat}_{2 \times 2}(\mathbb{F}) \to \mathbb{F}$$ is
not a linear map. It is linear in a weaker sense, one row at a time.

> **Theorem 4.1.** The function
> $$\det \colon \mathrm{Mat}_{2 \times 2}(\mathbb{F}) \to \mathbb{F}$$ is a
> linear function of each row when the other row is held fixed: for
> $$u, v, w \in \mathbb{F}^2$$ and $$t \in \mathbb{F}$$,
>
> $$
> \det \begin{pmatrix} u + tv \\ w \end{pmatrix}
> = \det \begin{pmatrix} u \\ w \end{pmatrix}
> + t \det \begin{pmatrix} v \\ w \end{pmatrix} ,
> \qquad
> \det \begin{pmatrix} w \\ u + tv \end{pmatrix}
> = \det \begin{pmatrix} w \\ u \end{pmatrix}
> + t \det \begin{pmatrix} w \\ v \end{pmatrix} .
> $$
{: .theorem #thm-4-1 }

*Proof.* Let $$u = (u_1, u_2)$$, $$v = (v_1, v_2)$$ and
$$w = (w_1, w_2)$$. Then

$$
\begin{aligned}
\det \begin{pmatrix} u_1 + tv_1 & u_2 + tv_2 \\ w_1 & w_2 \end{pmatrix}
&= (u_1 + tv_1) w_2 - (u_2 + tv_2) w_1 \\
&= (u_1 w_2 - u_2 w_1) + t\,(v_1 w_2 - v_2 w_1) ,
\end{aligned}
$$

which is the first identity. The second is the same computation with the
rows exchanged. $$\square$$

> **Theorem 4.2.** Let
> $$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}
> \in \mathrm{Mat}_{2 \times 2}(\mathbb{F})$$.
> Then $$\det A \ne 0$$ if and only if $$A$$ is invertible. In that case
>
> $$A^{-1} = \frac{1}{\det A}
> \begin{pmatrix} d & -b \\ -c & a \end{pmatrix} .$$
{: .theorem #thm-4-2 }

*Proof.* Let
$$B = \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$$. Multiplying out,

$$
AB = (ad - bc) \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = BA .
$$

If $$\det A \ne 0$$, then $$\frac{1}{\det A} B$$ is an inverse of $$A$$.
If $$\det A = 0$$ and $$A$$ were invertible, then
$$B = A^{-1}(AB) = O$$, so $$a = b = c = d = 0$$ and $$A = O$$, which is
not invertible. $$\square$$

### Area and orientation

> **Definition (Orientation).** For an ordered basis $$\{u, v\}$$ of
> $$\mathbb{R}^2$$, its **orientation** is the number
>
> $$
> \mathcal{O} \begin{pmatrix} u \\ v \end{pmatrix}
> = \frac{\det \begin{pmatrix} u \\ v \end{pmatrix}}
>        {\left\lvert \det \begin{pmatrix} u \\ v \end{pmatrix} \right\rvert}
> \in \{\pm 1\} .
> $$
>
> For $$u, v$$ that do not form a basis we set
> $$\mathcal{O} \begin{pmatrix} u \\ v \end{pmatrix} = 1$$.
{: .definition #def-orientation }

The denominator is nonzero for a basis: the matrix with rows $$u, v$$ then
has rank $$2$$, so it is invertible and its determinant is nonzero
([Theorem 4.2](#thm-4-2)).

**Examples.**
$$\mathcal{O} \begin{pmatrix} e_1 \\ e_2 \end{pmatrix} = 1$$,
$$\mathcal{O} \begin{pmatrix} e_2 \\ e_1 \end{pmatrix} = -1$$ and
$$\mathcal{O} \begin{pmatrix} e_1 \\ -e_2 \end{pmatrix} = -1$$.

An ordered basis $$\{u, v\}$$ of $$\mathbb{R}^2$$ is **right-handed** if
$$u$$ can be rotated counterclockwise through an angle $$\theta$$ with
$$0 < \theta < \pi$$ to point in the direction of $$v$$, and
**left-handed** otherwise. [Problem 4.1.2](#prob-4-1-2) shows that the
orientation is $$1$$ exactly for right-handed bases.

![Two panels, each with two arrows u and v from the origin and the shaded parallelogram they determine. On the left, turning from u to v is counterclockwise: right-handed, orientation plus one, positive determinant. On the right the labels are exchanged and the turn is clockwise: left-handed, orientation minus one, negative determinant](/assets/img/linear-algebra/orientation.svg)

> **Area of a parallelogram.** For $$u, v \in \mathbb{R}^2$$, let
> $$\operatorname{Area}(u, v)$$ be the area of the parallelogram with
> adjacent sides $$u$$ and $$v$$. Then
>
> $$
> \mathcal{O} \begin{pmatrix} u \\ v \end{pmatrix} \operatorname{Area}(u, v)
> = \det \begin{pmatrix} u \\ v \end{pmatrix} ,
> \qquad\text{so}\qquad
> \operatorname{Area}(u, v)
> = \left\lvert \det \begin{pmatrix} u \\ v \end{pmatrix} \right\rvert .
> $$
{: .theorem #area-parallelogram }

*Proof.* The argument takes the elementary properties of area and of
handedness from the plane geometry in the figures. If $$u, v$$ do not form
a basis, the parallelogram is degenerate and both sides are zero. Write
$$\delta \begin{pmatrix} u \\ v \end{pmatrix}$$ for the left side, the
*signed area*.

*Step 1.* For a basis $$\{u, v\}$$ and $$a, b \in \mathbb{R}$$,

$$
\delta \begin{pmatrix} u \\ v + au \end{pmatrix}
= \delta \begin{pmatrix} u \\ v \end{pmatrix} ,
\qquad
\delta \begin{pmatrix} u \\ bv \end{pmatrix}
= b\,\delta \begin{pmatrix} u \\ v \end{pmatrix} .
$$

The first is a shear: the parallelogram keeps its base $$u$$ and its
height, and $$v + au$$ stays on the same side of the line through $$u$$,
so area and orientation are unchanged. The second is a stretch of one
side by $$\lvert b \rvert$$, which multiplies the area by
$$\lvert b \rvert$$, and a negative $$b$$ reverses the orientation.
Together,

$$
\delta \begin{pmatrix} u \\ au + bv \end{pmatrix}
= b\,\delta \begin{pmatrix} u \\ v \end{pmatrix} .
$$

![Two panels. Left: the parallelograms on u, v and on u, v plus a u share the base u and have the same height, so their areas are equal. Right: the parallelogram on u and 2v is two copies of the one on u and v, so its area is twice as large](/assets/img/linear-algebra/parallelogram-shear.svg)

*Step 2.* $$\delta$$ is linear in the second row. Fix a basis
$$\{u, v\}$$ and let $$w_1 = a_1 u + b_1 v$$ and
$$w_2 = a_2 u + b_2 v$$. By Step 1,

$$
\delta \begin{pmatrix} u \\ w_1 + t w_2 \end{pmatrix}
= (b_1 + t b_2)\,\delta \begin{pmatrix} u \\ v \end{pmatrix}
= \delta \begin{pmatrix} u \\ w_1 \end{pmatrix}
+ t\,\delta \begin{pmatrix} u \\ w_2 \end{pmatrix} .
$$

Exchanging the two sides of a parallelogram keeps the area and reverses
the orientation, so
$$\delta \begin{pmatrix} v \\ u \end{pmatrix}
= -\delta \begin{pmatrix} u \\ v \end{pmatrix}$$,
and $$\delta$$ is linear in the first row as well.

*Step 3.* Expand both rows in the standard basis. The unit square gives
$$\delta \begin{pmatrix} e_1 \\ e_2 \end{pmatrix} = 1$$, hence
$$\delta \begin{pmatrix} e_2 \\ e_1 \end{pmatrix} = -1$$, and
$$\delta \begin{pmatrix} e_i \\ e_i \end{pmatrix} = 0$$. Therefore

$$
\delta \begin{pmatrix} a & b \\ c & d \end{pmatrix}
= ad\,\delta \begin{pmatrix} e_1 \\ e_2 \end{pmatrix}
+ bc\,\delta \begin{pmatrix} e_2 \\ e_1 \end{pmatrix}
= ad - bc . \qquad \square
$$

Step 3 uses only three properties of $$\delta$$: it is linear in each
row, it vanishes when the two rows are equal, and it is $$1$$ on
$$I_2$$. [Problem 4.1.1](#prob-4-1-1) shows that these three properties
force a function to be the determinant, over any field.
[§4.5](/posts/linear-algebra-determinants-2/) does the same for
$$n \times n$$ matrices.

### Problems for §4.1

> **Problem 4.1.1 (Exercise 4.1.12).** Let
> $$\delta \colon M_{2 \times 2}(F) \to F$$ be a function with the
> following three properties.
>
> - **(i)** $$\delta$$ is a linear function of each row of the matrix when
>   the other row is held fixed.
> - **(ii)** If the two rows of $$A \in M_{2 \times 2}(F)$$ are identical,
>   then $$\delta(A) = 0$$.
> - **(iii)** If $$I$$ is the $$2 \times 2$$ identity matrix, then
>   $$\delta(I) = 1$$.
>
> Prove that $$\delta(A) = \det(A)$$ for all $$A \in M_{2 \times 2}(F)$$.
{: .problem #prob-4-1-1 }

*Solution.* First, exchanging the rows changes the sign. For rows
$$u, v$$, properties (ii) and (i) give

$$
0 = \delta \begin{pmatrix} u + v \\ u + v \end{pmatrix}
= \delta \begin{pmatrix} u \\ u \end{pmatrix}
+ \delta \begin{pmatrix} u \\ v \end{pmatrix}
+ \delta \begin{pmatrix} v \\ u \end{pmatrix}
+ \delta \begin{pmatrix} v \\ v \end{pmatrix}
= \delta \begin{pmatrix} u \\ v \end{pmatrix}
+ \delta \begin{pmatrix} v \\ u \end{pmatrix} .
$$

Now let $$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$$. Its rows
are $$a e_1 + b e_2$$ and $$c e_1 + d e_2$$. Expanding by (i) in the
first row and then in the second,

$$
\delta(A)
= ac\,\delta \begin{pmatrix} e_1 \\ e_1 \end{pmatrix}
+ ad\,\delta \begin{pmatrix} e_1 \\ e_2 \end{pmatrix}
+ bc\,\delta \begin{pmatrix} e_2 \\ e_1 \end{pmatrix}
+ bd\,\delta \begin{pmatrix} e_2 \\ e_2 \end{pmatrix} .
$$

The first and last terms vanish by (ii). By (iii),
$$\delta \begin{pmatrix} e_1 \\ e_2 \end{pmatrix} = \delta(I) = 1$$, and
by the sign rule
$$\delta \begin{pmatrix} e_2 \\ e_1 \end{pmatrix} = -1$$. Hence
$$\delta(A) = ad - bc = \det(A)$$. $$\square$$

> **Problem 4.1.2 (Exercise 4.1.13).** Let $$\{u, v\}$$ be an ordered
> basis for $$\mathbb{R}^2$$. Prove that
>
> $$\mathcal{O} \begin{pmatrix} u \\ v \end{pmatrix} = 1$$
>
> if and only if $$\{u, v\}$$ forms a right-handed coordinate system.
{: .problem #prob-4-1-2 }

*Solution.* Write the two vectors in polar form,

$$
u = (r \cos\alpha,\ r \sin\alpha), \qquad
v = (s \cos\beta,\ s \sin\beta), \qquad r, s > 0 .
$$

Then

$$
\det \begin{pmatrix} u \\ v \end{pmatrix}
= rs\,(\cos\alpha \sin\beta - \sin\alpha \cos\beta)
= rs \sin(\beta - \alpha) .
$$

Let $$\theta$$ be the angle of the counterclockwise rotation that takes
the direction of $$u$$ to the direction of $$v$$, chosen with
$$0 \le \theta < 2\pi$$. Then $$\theta$$ differs from $$\beta - \alpha$$
by a multiple of $$2\pi$$, so
$$\det \begin{pmatrix} u \\ v \end{pmatrix} = rs \sin\theta$$. Since
$$\{u, v\}$$ is a basis, $$v$$ is not a multiple of $$u$$, so
$$\theta \ne 0$$ and $$\theta \ne \pi$$. Therefore

$$
\mathcal{O} \begin{pmatrix} u \\ v \end{pmatrix} = 1
\iff \sin\theta > 0
\iff 0 < \theta < \pi ,
$$

and the last condition says that $$\{u, v\}$$ is right-handed.
$$\square$$

---

## §4.2 Determinants of Order $$n$$

For $$A \in \mathrm{Mat}_{n \times n}(\mathbb{F})$$ with $$n \ge 2$$,
$$\tilde{A}_{ij}$$ denotes the $$(n-1) \times (n-1)$$ matrix obtained from
$$A$$ by deleting row $$i$$ and column $$j$$. For example, if

$$
A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix} ,
\qquad\text{then}\qquad
\tilde{A}_{11} = \begin{pmatrix} 5 & 6 \\ 8 & 9 \end{pmatrix} , \quad
\tilde{A}_{32} = \begin{pmatrix} 1 & 3 \\ 4 & 6 \end{pmatrix} .
$$

> **Definition (Determinant, cofactor).** Let
> $$A \in \mathrm{Mat}_{n \times n}(\mathbb{F})$$. The **determinant** of
> $$A$$, written $$\det(A)$$ or $$\lvert A \rvert$$, is defined
> recursively: $$\det(A) = A_{11}$$ for $$n = 1$$, and
>
> $$\det(A) = \sum_{j=1}^{n} (-1)^{1+j} A_{1j} \det(\tilde{A}_{1j})$$
>
> for $$n \ge 2$$. The scalar $$(-1)^{i+j} \det(\tilde{A}_{ij})$$ is the
> **$$(i,j)$$-cofactor** of $$A$$, and the formula is the **cofactor
> expansion along the first row** of $$A$$.
{: .definition #def-determinant }

**Examples.**

- For $$n = 2$$ the formula gives
  $$\det \begin{pmatrix} a & b \\ c & d \end{pmatrix} = a \cdot d - b \cdot c$$,
  in agreement with §4.1.
- Expanding along the first row,

  $$
  \det \begin{pmatrix} 1 & 3 & -3 \\ -3 & -5 & 2 \\ -4 & 4 & -6 \end{pmatrix}
  = 1 \cdot (30 - 8) - 3 \cdot (18 + 8) + (-3) \cdot (-12 - 20) = 40 .
  $$

- $$\det(I_n) = 1$$, by induction on $$n$$: the first row of $$I_n$$ is
  $$e_1$$ and deleting its first row and column leaves $$I_{n-1}$$.

> **Theorem 4.3.** The determinant of an $$n \times n$$ matrix is a linear
> function of each row when the remaining rows are held fixed: for
> $$1 \le r \le n$$, rows $$a_i, u, v \in \mathbb{F}^n$$ and
> $$t \in \mathbb{F}$$,
>
> $$
> \det \begin{pmatrix} a_1 \\ \vdots \\ a_{r-1} \\ u + tv \\ a_{r+1} \\ \vdots \\ a_n \end{pmatrix}
> = \det \begin{pmatrix} a_1 \\ \vdots \\ a_{r-1} \\ u \\ a_{r+1} \\ \vdots \\ a_n \end{pmatrix}
> + t \det \begin{pmatrix} a_1 \\ \vdots \\ a_{r-1} \\ v \\ a_{r+1} \\ \vdots \\ a_n \end{pmatrix} .
> $$
{: .theorem #thm-4-3 }

*Proof.* By induction on $$n$$. The case $$n = 1$$ is clear. Let
$$n \ge 2$$ and assume the theorem for $$(n-1) \times (n-1)$$ matrices.
Call the three matrices $$A$$, $$B$$ and $$C$$, so that their $$r$$-th
rows are $$u + tv$$, $$u$$ and $$v$$ and their other rows agree.

*Case $$r = 1$$.* The three matrices agree outside the first row, so
$$\tilde{A}_{1j} = \tilde{B}_{1j} = \tilde{C}_{1j}$$, and
$$A_{1j} = u_j + t v_j$$. Hence

$$
\det A = \sum_{j} (-1)^{1+j} (u_j + t v_j) \det(\tilde{A}_{1j})
= \det B + t \det C .
$$

*Case $$r > 1$$.* The first rows agree,
$$A_{1j} = B_{1j} = C_{1j}$$. The matrices $$\tilde{A}_{1j}$$,
$$\tilde{B}_{1j}$$, $$\tilde{C}_{1j}$$ agree except in row $$r - 1$$,
where they hold the rows $$u + tv$$, $$u$$, $$v$$ with the $$j$$-th entry
removed. By the induction hypothesis
$$\det(\tilde{A}_{1j}) = \det(\tilde{B}_{1j}) + t \det(\tilde{C}_{1j})$$,
and so

$$
\det A = \sum_{j} (-1)^{1+j} A_{1j}
\big( \det(\tilde{B}_{1j}) + t \det(\tilde{C}_{1j}) \big)
= \det B + t \det C . \qquad \square
$$

> **Corollary to Theorem 4.3.** If $$A$$ has a row consisting entirely of
> zeros, then $$\det A = 0$$.
{: .theorem #cor-4-3 }

*Proof.* Write the zero row as $$\mathbf{0} + 1 \cdot \mathbf{0}$$. By
[Theorem 4.3](#thm-4-3), $$\det A = \det A + \det A$$, so
$$\det A = 0$$. $$\square$$

The definition expands along the first row. The next lemma is the step
that allows any row to be used.

> **Lemma.** Let $$B \in \mathrm{Mat}_{n \times n}(\mathbb{F})$$ with
> $$n \ge 2$$. If the $$i$$-th row of $$B$$ is $$e_k$$ for some $$k$$,
> then
>
> $$\det B = (-1)^{i+k} \det(\tilde{B}_{ik}) .$$
{: .theorem #lem-4-4 }

*Proof.* By induction on $$n$$. For $$n = 2$$ there are four cases, each
checked directly; for instance, with $$i = 2$$ and $$k = 1$$,
$$\det \begin{pmatrix} a & b \\ 1 & 0 \end{pmatrix} = -b
= (-1)^{2+1} \det(\tilde{B}_{21})$$.

Let $$n \ge 3$$ and assume the lemma for $$(n-1) \times (n-1)$$ matrices.
If $$i = 1$$, the first row of $$B$$ is $$e_k$$ and the definition gives
$$\det B = (-1)^{1+k} \det(\tilde{B}_{1k})$$ at once. Let $$i > 1$$. For
$$j \ne k$$, let $$C_{ij}$$ be the $$(n-2) \times (n-2)$$ matrix obtained
from $$B$$ by deleting rows $$1$$ and $$i$$ and columns $$j$$ and $$k$$.

Row $$i - 1$$ of $$\tilde{B}_{1j}$$ is the row $$e_k$$ with its $$j$$-th
entry removed. This is $$e_{k-1}$$ if $$j < k$$, the zero row if
$$j = k$$, and $$e_k$$ if $$j > k$$, as rows of length $$n - 1$$. By the
induction hypothesis and the
[Corollary to Theorem 4.3](#cor-4-3),

$$
\det(\tilde{B}_{1j}) =
\begin{cases}
(-1)^{(i-1)+(k-1)} \det(C_{ij}) & \text{if } j < k, \\
0 & \text{if } j = k, \\
(-1)^{(i-1)+k} \det(C_{ij}) & \text{if } j > k .
\end{cases}
$$

Substituting into the definition of $$\det B$$,

$$
\det B
= (-1)^{i+k} \Big[ \sum_{j < k} (-1)^{1+j} B_{1j} \det(C_{ij})
+ \sum_{j > k} (-1)^{1+(j-1)} B_{1j} \det(C_{ij}) \Big] .
$$

The bracket is the cofactor expansion of $$\tilde{B}_{ik}$$ along its
first row. Indeed, the first row of $$\tilde{B}_{ik}$$ is the first row of
$$B$$ without $$B_{1k}$$, so $$B_{1j}$$ stands in column $$j$$ if
$$j < k$$ and in column $$j - 1$$ if $$j > k$$, and deleting the first
row and that column from $$\tilde{B}_{ik}$$ leaves $$C_{ij}$$. Hence
$$\det B = (-1)^{i+k} \det(\tilde{B}_{ik})$$. $$\square$$

> **Theorem 4.4 (Cofactor expansion along any row).** Let
> $$A \in \mathrm{Mat}_{n \times n}(\mathbb{F})$$. For every
> $$i = 1, \dots, n$$,
>
> $$\det(A) = \sum_{j=1}^{n} (-1)^{i+j} A_{ij} \det(\tilde{A}_{ij}) .$$
{: .theorem #thm-4-4 }

*Proof.* For $$i = 1$$ this is the definition, so let $$i > 1$$. The
$$i$$-th row of $$A$$ is $$\sum_{k} A_{ik} e_k$$. Let $$B_k$$ be the
matrix obtained from $$A$$ by replacing its $$i$$-th row by $$e_k$$. By
[Theorem 4.3](#thm-4-3) and then the [Lemma](#lem-4-4),

$$
\det A = \sum_{k=1}^{n} A_{ik} \det B_k
= \sum_{k=1}^{n} (-1)^{i+k} A_{ik} \det(\tilde{A}_{ik}) ,
$$

because deleting row $$i$$ and column $$k$$ from $$B_k$$ gives the same
matrix as deleting them from $$A$$. $$\square$$

> **Corollary to Theorem 4.4.** If $$A$$ has two identical rows, then
> $$\det A = 0$$.
{: .theorem #cor-4-4 }

*Proof.* By induction on $$n \ge 2$$. For $$n = 2$$,
$$\det \begin{pmatrix} a & b \\ a & b \end{pmatrix} = ab - ba = 0$$. Let
$$n \ge 3$$, let rows $$r$$ and $$s$$ of $$A$$ be identical, and choose a
row $$i$$ different from both. Each $$\tilde{A}_{ij}$$ still contains
rows $$r$$ and $$s$$ of $$A$$ with the $$j$$-th entry removed, so it has
two identical rows and $$\det(\tilde{A}_{ij}) = 0$$ by the induction
hypothesis. Expanding along row $$i$$ ([Theorem 4.4](#thm-4-4)) gives
$$\det A = 0$$. $$\square$$

> **Theorem 4.5.** If $$B$$ is obtained from
> $$A \in \mathrm{Mat}_{n \times n}(\mathbb{F})$$ by interchanging two
> rows, then $$\det B = -\det A$$:
>
> $$
> \det \begin{pmatrix} \vdots \\ u \\ \vdots \\ v \\ \vdots \end{pmatrix}
> = -\det \begin{pmatrix} \vdots \\ v \\ \vdots \\ u \\ \vdots \end{pmatrix} .
> $$
{: .theorem #thm-4-5 }

*Proof.* Put $$u + v$$ in both of the two rows and leave the other rows
as they are. The result has two identical rows, so its determinant is
zero ([Corollary to Theorem 4.4](#cor-4-4)). Expanding by linearity in
each of the two rows ([Theorem 4.3](#thm-4-3)),

$$
0 = \det \begin{pmatrix} \vdots \\ u + v \\ \vdots \\ u + v \\ \vdots \end{pmatrix}
= \det \begin{pmatrix} \vdots \\ u \\ \vdots \\ u \\ \vdots \end{pmatrix}
+ \det \begin{pmatrix} \vdots \\ u \\ \vdots \\ v \\ \vdots \end{pmatrix}
+ \det \begin{pmatrix} \vdots \\ v \\ \vdots \\ u \\ \vdots \end{pmatrix}
+ \det \begin{pmatrix} \vdots \\ v \\ \vdots \\ v \\ \vdots \end{pmatrix} .
$$

The first and last terms are zero for the same reason, which leaves
$$\det A + \det B = 0$$. $$\square$$

> **Theorem 4.6.** If $$B$$ is obtained from
> $$A \in \mathrm{Mat}_{n \times n}(\mathbb{F})$$ by adding a multiple of
> one row to another row, then $$\det B = \det A$$:
>
> $$
> \det \begin{pmatrix} \vdots \\ u \\ \vdots \\ v + tu \\ \vdots \end{pmatrix}
> = \det \begin{pmatrix} \vdots \\ u \\ \vdots \\ v \\ \vdots \end{pmatrix} .
> $$
{: .theorem #thm-4-6 }

*Proof.* By [Theorem 4.3](#thm-4-3),

$$
\det \begin{pmatrix} \vdots \\ u \\ \vdots \\ v + tu \\ \vdots \end{pmatrix}
= \det \begin{pmatrix} \vdots \\ u \\ \vdots \\ v \\ \vdots \end{pmatrix}
+ t \det \begin{pmatrix} \vdots \\ u \\ \vdots \\ u \\ \vdots \end{pmatrix} ,
$$

and the last determinant is zero
([Corollary to Theorem 4.4](#cor-4-4)). The same computation applies when
the row $$u$$ lies below the row that is changed. $$\square$$

> **Corollary to Theorem 4.6.** If
> $$A \in \mathrm{Mat}_{n \times n}(\mathbb{F})$$ has rank less than
> $$n$$, then $$\det A = 0$$.
{: .theorem #cor-4-6 }

*Proof.* The row space of $$A$$ has dimension
$$\operatorname{rank}(A) < n$$
([Corollary 2 to Theorem 3.6][cor-3-6-2]), so the $$n$$ rows are
linearly dependent and some row is a linear combination of the others,
$$a_r = \sum_{i \ne r} c_i a_i$$. Adding $$-c_i$$ times row $$i$$ to row
$$r$$, for each $$i \ne r$$, turns row $$r$$ into a zero row and does not
change the determinant ([Theorem 4.6](#thm-4-6)). A matrix with a zero
row has determinant zero ([Corollary to Theorem 4.3](#cor-4-3)).
$$\square$$

Theorems 4.3, 4.5 and 4.6 say what each elementary row operation does to a
determinant.

> **Determinants and elementary row operations.** Let
> $$A \in \mathrm{Mat}_{n \times n}(\mathbb{F})$$.
>
> - **(Type 1)** Interchanging two rows multiplies the determinant by
>   $$-1$$.
> - **(Type 2)** Multiplying a row by a scalar $$c$$ multiplies the
>   determinant by $$c$$.
> - **(Type 3)** Adding a multiple of one row to another row leaves the
>   determinant unchanged.
>
> Consequently an elementary matrix $$E$$ has $$\det E = -1$$, $$c$$ or
> $$1$$ according to its type, and
>
> $$\det(EA) = \det E \cdot \det A$$
>
> for every elementary matrix $$E$$.
{: .theorem #det-elementary }

*Proof.* The three statements are [Theorem 4.5](#thm-4-5),
[Theorem 4.3](#thm-4-3) with $$u = \mathbf{0}$$, and
[Theorem 4.6](#thm-4-6). Applying them to $$I_n$$, whose determinant is
$$1$$, gives the determinants of the elementary matrices. Finally $$EA$$
is the result of applying to $$A$$ the row operation that produces $$E$$
from $$I_n$$ ([Theorem 3.1][thm-3-1]), so $$\det(EA)$$ is $$\det A$$
multiplied by the same factor $$-1$$, $$c$$ or $$1$$, which is
$$\det E$$. $$\square$$

> **Exercise 4.2.23.** The determinant of an upper triangular matrix is
> the product of its diagonal entries.
{: .theorem #ex-4-2-23 }

*Proof.* By induction on $$n$$; the case $$n = 1$$ is clear. If $$A$$ is
upper triangular and $$n \ge 2$$, its last row is
$$(0, \dots, 0, A_{nn})$$. Expanding along the last row
([Theorem 4.4](#thm-4-4)),
$$\det A = (-1)^{n+n} A_{nn} \det(\tilde{A}_{nn})$$, and
$$\tilde{A}_{nn}$$ is upper triangular with diagonal entries
$$A_{11}, \dots, A_{n-1,n-1}$$. $$\square$$

**Example.**
$$\det \begin{pmatrix} 3 & 2 & 1 \\ 0 & 4 & 5 \\ 0 & 0 & 6 \end{pmatrix}
= 3 \cdot 4 \cdot 6 = 72$$.

Together these give the practical way to compute a determinant: reduce
the matrix to upper triangular form by row operations, keeping track of
the factors.

**Example.**

$$
\begin{aligned}
\det \begin{pmatrix} 0 & 1 & 3 & -3 \\ 2 & 0 & 0 & 1 \\ -2 & -3 & -5 & 2 \\ 4 & -4 & 4 & -6 \end{pmatrix}
&= -\det \begin{pmatrix} 2 & 0 & 0 & 1 \\ 0 & 1 & 3 & -3 \\ -2 & -3 & -5 & 2 \\ 4 & -4 & 4 & -6 \end{pmatrix} \\
&= -\det \begin{pmatrix} 2 & 0 & 0 & 1 \\ 0 & 1 & 3 & -3 \\ 0 & -3 & -5 & 3 \\ 0 & -4 & 4 & -8 \end{pmatrix}
= -\det \begin{pmatrix} 2 & 0 & 0 & 1 \\ 0 & 1 & 3 & -3 \\ 0 & 0 & 4 & -6 \\ 0 & 0 & 16 & -20 \end{pmatrix} \\
&= -\det \begin{pmatrix} 2 & 0 & 0 & 1 \\ 0 & 1 & 3 & -3 \\ 0 & 0 & 4 & -6 \\ 0 & 0 & 0 & 4 \end{pmatrix}
= -2 \cdot 1 \cdot 4 \cdot 4 = -32 .
\end{aligned}
$$

The steps are $$R_1 \leftrightarrow R_2$$, which changes the sign; then
$$R_3 \mathrel{+}= R_1$$ and $$R_4 \mathrel{+}= -2R_1$$; then
$$R_3 \mathrel{+}= 3R_2$$ and $$R_4 \mathrel{+}= 4R_2$$; then
$$R_4 \mathrel{+}= -4R_3$$.

### Problems for §4.2

> **Problem 4.2.1 (Exercise 4.2.29).** Prove that if $$E$$ is an
> elementary matrix, then $$\det(E^t) = \det(E)$$.
{: .problem #prob-4-2-1 }

*Solution.* Consider the three types.

- *Type 1.* $$E$$ is $$I_n$$ with rows $$i$$ and $$j$$ interchanged. Its
  nonzero entries are $$E_{ij} = E_{ji} = 1$$ and $$E_{kk} = 1$$ for
  $$k \ne i, j$$, so $$E$$ is symmetric and $$E^t = E$$.
- *Type 2.* $$E$$ is diagonal, so $$E^t = E$$.
- *Type 3.* $$E$$ is $$I_n$$ with one extra entry $$c$$ in a position
  $$(i, j)$$ with $$i \ne j$$. Then $$E^t$$ is $$I_n$$ with the extra
  entry $$c$$ in position $$(j, i)$$, which is again an elementary matrix
  of type 3. Both have determinant $$1$$
  ([determinants of elementary matrices](#det-elementary)).

In every case $$\det(E^t) = \det(E)$$. $$\square$$

---

## §4.3 Properties of Determinants

> **Theorem 4.7.** For any
> $$A, B \in \mathrm{Mat}_{n \times n}(\mathbb{F})$$,
>
> $$\det(AB) = \det A \cdot \det B .$$
{: .theorem #thm-4-7 }

*Proof.* If $$\operatorname{rank}(A) < n$$, then $$\det A = 0$$
([Corollary to Theorem 4.6](#cor-4-6)). Also
$$\operatorname{rank}(AB) \le \operatorname{rank}(A) < n$$
([Theorem 3.7][thm-3-7]), so $$\det(AB) = 0$$ as well.

If $$\operatorname{rank}(A) = n$$, then $$A$$ is invertible and is a
product of elementary matrices, $$A = E_1 E_2 \cdots E_k$$
([Corollary 3 to Theorem 3.6][cor-3-6-3]). Using
$$\det(EC) = \det E \cdot \det C$$ for each elementary matrix
([determinants and elementary row operations](#det-elementary)), one
factor at a time,

$$
\det(AB) = \det(E_1 E_2 \cdots E_k B)
= \det E_1 \cdot \det(E_2 \cdots E_k B)
= \cdots
= \det E_1 \cdots \det E_k \cdot \det B .
$$

The same computation with $$B = I_n$$ gives
$$\det A = \det E_1 \cdots \det E_k$$. $$\square$$

> **Corollary to Theorem 4.7.** A matrix
> $$A \in \mathrm{Mat}_{n \times n}(\mathbb{F})$$ is invertible if and
> only if $$\det A \ne 0$$. If $$A$$ is invertible, then
>
> $$\det(A^{-1}) = \frac{1}{\det A} .$$
{: .theorem #cor-4-7 }

*Proof.* If $$A$$ is not invertible, its rank is less than $$n$$ and
$$\det A = 0$$ ([Corollary to Theorem 4.6](#cor-4-6)). If $$A$$ is
invertible, then
$$1 = \det I_n = \det(AA^{-1}) = \det A \cdot \det(A^{-1})$$, so
$$\det A \ne 0$$ and $$\det(A^{-1})$$ is its inverse. $$\square$$

**Notes.**

- $$\det(AB) = \det(BA)$$, since both equal $$\det A \cdot \det B$$.
- [Similar][def-similar] matrices have the same determinant: if
  $$B = Q^{-1}AQ$$, then
  $$\det B = \det(Q^{-1}) \det A \det Q = \det A$$.

> **Exercise 4.3.16.** If
> $$A, B \in \mathrm{Mat}_{n \times n}(\mathbb{F})$$ satisfy
> $$AB = I_n$$, then $$A$$ is invertible and $$A^{-1} = B$$.
{: .theorem #ex-4-3-16 }

*Proof.* $$1 = \det I_n = \det(AB) = \det A \cdot \det B$$, so
$$\det A \ne 0$$ and $$A$$ is invertible
([Corollary to Theorem 4.7](#cor-4-7)). Then
$$B = A^{-1}AB = A^{-1}$$. $$\square$$

> **Theorem 4.8.** For any
> $$A \in \mathrm{Mat}_{n \times n}(\mathbb{F})$$,
>
> $$\det(A^t) = \det A .$$
{: .theorem #thm-4-8 }

*Proof.* If $$A$$ is not invertible, then
$$\operatorname{rank}(A^t) = \operatorname{rank}(A) < n$$
([Corollary 2 to Theorem 3.6][cor-3-6-2]) and both determinants are zero.

If $$A$$ is invertible, write $$A = E_1 E_2 \cdots E_k$$ with elementary
matrices $$E_i$$. Then $$A^t = E_k^t \cdots E_2^t E_1^t$$, and
$$\det(E^t) = \det E$$ for each elementary matrix
([Problem 4.2.1](#prob-4-2-1)). By [Theorem 4.7](#thm-4-7),

$$
\det(A^t) = \det(E_k^t) \cdots \det(E_1^t)
= \det E_k \cdots \det E_1 = \det A . \qquad \square
$$

> **Corollary to Theorem 4.8.** Every statement about determinants that
> is formulated for rows is also true for columns. In particular:
>
> - the determinant is a linear function of each column when the other
>   columns are held fixed;
> - an elementary column operation of type 1, 2 or 3 multiplies the
>   determinant by $$-1$$, by the scalar $$c$$, or by $$1$$;
> - for every $$j$$, the **cofactor expansion along the $$j$$-th column**
>   holds:
>
>   $$\det(A) = \sum_{i=1}^{n} (-1)^{i+j} A_{ij} \det(\tilde{A}_{ij}) .$$
{: .theorem #cor-4-8 }

*Proof.* The columns of $$A$$ are the rows of $$A^t$$, and
$$\det A = \det(A^t)$$. So a row statement applied to $$A^t$$ is the
column statement for $$A$$. For the expansion, the cofactor expansion of
$$A^t$$ along its $$j$$-th row ([Theorem 4.4](#thm-4-4)) is

$$
\det(A^t) = \sum_{i=1}^{n} (-1)^{j+i} (A^t)_{ji}
\det\big( \widetilde{(A^t)}_{ji} \big) ,
$$

where $$(A^t)_{ji} = A_{ij}$$ and
$$\widetilde{(A^t)}_{ji} = (\tilde{A}_{ij})^t$$ has the same determinant
as $$\tilde{A}_{ij}$$. $$\square$$

> **Exercise 4.3.21.** Let $$A$$ and $$C$$ be square matrices, and let
> $$B$$ and the zero matrix $$O$$ have the sizes that make the block
> matrix below square. Then
>
> $$\det \begin{pmatrix} A & B \\ O & C \end{pmatrix}
> = \det A \cdot \det C .$$
{: .theorem #ex-4-3-21 }

*Proof.* Let $$A$$ be $$k \times k$$ and call the block matrix $$M$$. The
proof is by induction on $$k$$, expanding along the first column
([Corollary to Theorem 4.8](#cor-4-8)).

If $$k = 1$$ and $$A = (a)$$, the first column of $$M$$ has the single
possibly nonzero entry $$a$$, and deleting its row and column leaves
$$C$$. So $$\det M = a \det C$$.

Let $$k \ge 2$$. The first column of $$M$$ is the first column of $$A$$
followed by zeros, so

$$
\det M = \sum_{i=1}^{k} (-1)^{i+1} A_{i1} \det(\tilde{M}_{i1}) ,
\qquad
\tilde{M}_{i1} = \begin{pmatrix} \tilde{A}_{i1} & B_i \\ O & C \end{pmatrix} ,
$$

where $$B_i$$ is $$B$$ without its $$i$$-th row. By the induction
hypothesis
$$\det(\tilde{M}_{i1}) = \det(\tilde{A}_{i1}) \cdot \det C$$, and
therefore

$$
\det M = \Big( \sum_{i=1}^{k} (-1)^{i+1} A_{i1} \det(\tilde{A}_{i1}) \Big)
\det C = \det A \cdot \det C . \qquad \square
$$

The slides list the same statement also as Exercise 4.4.6.

> **Theorem 4.9 (Cramer's Rule).** Let
> $$A \in \mathrm{Mat}_{n \times n}(\mathbb{F})$$ be invertible, and let
> $$s = (s_1, \dots, s_n)$$ be the unique solution of $$Ax = b$$. Then for
> each $$k = 1, \dots, n$$,
>
> $$s_k = \frac{\det M_k}{\det A} ,$$
>
> where $$M_k$$ is the matrix obtained from $$A$$ by replacing its
> $$k$$-th column by $$b$$.
{: .theorem #thm-4-9 }

*Proof.* The solution exists and is unique by
[Theorem 3.10][thm-3-10]. Let $$X_k$$ be the matrix obtained from
$$I_n$$ by replacing its $$k$$-th column by $$s$$. The $$j$$-th column of
$$AX_k$$ is $$A$$ times the $$j$$-th column of $$X_k$$
([Theorem 2.13][thm-2-13]): it is $$Ae_j$$, the $$j$$-th column of
$$A$$, for $$j \ne k$$, and it is $$As = b$$ for $$j = k$$. That is,

$$
A X_k = M_k .
$$

The $$k$$-th row of $$X_k$$ has the single nonzero entry $$s_k$$ in
position $$k$$, and deleting row $$k$$ and column $$k$$ from $$X_k$$
leaves $$I_{n-1}$$. Expanding along that row
([Theorem 4.4](#thm-4-4)) gives $$\det X_k = s_k$$. By
[Theorem 4.7](#thm-4-7), $$\det M_k = \det A \cdot s_k$$, and
$$\det A \ne 0$$ ([Corollary to Theorem 4.7](#cor-4-7)).
$$\square$$

**Example.** For

$$
\begin{aligned}
x_1 + 2x_2 + 3x_3 &= 2 \\
x_1 \phantom{{}+ 2x_2} + x_3 &= 3 \\
x_1 + x_2 - x_3 &= 1
\end{aligned}
\qquad\qquad
A = \begin{pmatrix} 1 & 2 & 3 \\ 1 & 0 & 1 \\ 1 & 1 & -1 \end{pmatrix} ,
\quad b = \begin{pmatrix} 2 \\ 3 \\ 1 \end{pmatrix} ,
$$

we have $$\det A = 6$$ and

$$
x_1 = \frac{1}{6} \det \begin{pmatrix} 2 & 2 & 3 \\ 3 & 0 & 1 \\ 1 & 1 & -1 \end{pmatrix}
= \frac{15}{6} = \frac52 , \qquad
x_2 = \frac{1}{6} \det \begin{pmatrix} 1 & 2 & 3 \\ 1 & 3 & 1 \\ 1 & 1 & -1 \end{pmatrix}
= \frac{-6}{6} = -1 ,
$$

$$
x_3 = \frac{1}{6} \det \begin{pmatrix} 1 & 2 & 2 \\ 1 & 0 & 3 \\ 1 & 1 & 1 \end{pmatrix}
= \frac{3}{6} = \frac12 .
$$

Cramer's rule is rarely the fast way to solve a system; Gaussian
elimination is. Its value is theoretical. For instance, if $$A$$ and
$$b$$ have integer entries and $$\det A = \pm 1$$, the rule shows that
the solution has integer entries.

> **Definition (Classical adjoint).** The **classical adjoint** of
> $$A \in \mathrm{Mat}_{n \times n}(\mathbb{F})$$ is the
> $$n \times n$$ matrix $$\operatorname{adj}(A)$$ whose $$(i, j)$$ entry
> is the $$(j, i)$$-cofactor of $$A$$:
>
> $$\operatorname{adj}(A)_{ij} = (-1)^{i+j} \det(\tilde{A}_{ji}) .$$
{: .definition #def-classical-adjoint }

> **Exercise 4.3.25.** For every
> $$A \in \mathrm{Mat}_{n \times n}(\mathbb{F})$$, invertible or not,
>
> $$A \operatorname{adj}(A) = (\det A)\, I_n .$$
>
> Consequently, if $$A$$ is invertible, then
>
> $$A^{-1} = \frac{1}{\det A} \operatorname{adj}(A) .$$
{: .theorem #ex-4-3-25 }

*Proof.* The $$(i, j)$$ entry of $$A \operatorname{adj}(A)$$ is

$$
\sum_{k=1}^{n} A_{ik} \operatorname{adj}(A)_{kj}
= \sum_{k=1}^{n} (-1)^{j+k} A_{ik} \det(\tilde{A}_{jk}) .
$$

If $$i = j$$, this is the cofactor expansion of $$\det A$$ along row
$$i$$ ([Theorem 4.4](#thm-4-4)). If $$i \ne j$$, let $$A'$$ be the matrix
obtained from $$A$$ by replacing row $$j$$ with a copy of row $$i$$. Then
$$A'_{jk} = A_{ik}$$ and $$\tilde{A'}_{jk} = \tilde{A}_{jk}$$, so the sum
is the cofactor expansion of $$\det A'$$ along row $$j$$. Since $$A'$$
has two identical rows, $$\det A' = 0$$
([Corollary to Theorem 4.4](#cor-4-4)). Hence the $$(i, j)$$ entry is
$$(\det A)\,\delta_{ij}$$.

If $$A$$ is invertible, then $$\det A \ne 0$$ and
$$A \cdot \frac{1}{\det A} \operatorname{adj}(A) = I_n$$, so
$$\frac{1}{\det A} \operatorname{adj}(A) = A^{-1}$$ by
[Exercise 4.3.16](#ex-4-3-16). $$\square$$

The slides reach the formula for $$A^{-1}$$ from Cramer's rule: the
$$i$$-th column of $$A^{-1}$$ is the solution of $$Ax = e_i$$, and its
entries are quotients of determinants in which one column of $$A$$ is
replaced by $$e_i$$.

> **Exercise 4.3.22 (Vandermonde determinant).** For
> $$c_0, c_1, \dots, c_n \in \mathbb{F}$$,
>
> $$
> \det \begin{pmatrix}
> 1 & c_0 & c_0^2 & \cdots & c_0^n \\
> 1 & c_1 & c_1^2 & \cdots & c_1^n \\
> \vdots & \vdots & \vdots & & \vdots \\
> 1 & c_n & c_n^2 & \cdots & c_n^n
> \end{pmatrix}
> = \prod_{0 \le i < j \le n} (c_j - c_i) .
> $$
>
> In particular the determinant is nonzero if and only if
> $$c_0, \dots, c_n$$ are distinct.
{: .theorem #ex-4-3-22 }

*Proof.* Call the matrix $$V(c_0, \dots, c_n)$$ and number its rows and
columns from $$0$$ to $$n$$, so that the $$(i, j)$$ entry is
$$c_i^{\,j}$$. The proof is by induction on $$n$$. For $$n = 0$$ the
matrix is $$(1)$$ and the empty product is $$1$$.

Let $$n \ge 1$$. For $$j = n, n-1, \dots, 1$$, in this order, subtract
$$c_0$$ times column $$j - 1$$ from column $$j$$. These are column
operations of type 3 and do not change the determinant
([Corollary to Theorem 4.8](#cor-4-8)). Going from right to left, each
step uses a column that is still in its original state, so the new
$$(i, j)$$ entry for $$j \ge 1$$ is

$$
c_i^{\,j} - c_0\, c_i^{\,j-1} = c_i^{\,j-1} (c_i - c_0) .
$$

Row $$0$$ becomes $$(1, 0, \dots, 0)$$. Expanding along it leaves the
$$n \times n$$ matrix whose $$i$$-th row, for $$i = 1, \dots, n$$, is
$$(c_i - c_0)$$ times $$(1, c_i, \dots, c_i^{\,n-1})$$. Taking the
factor out of each row ([Theorem 4.3](#thm-4-3)) and using the induction
hypothesis,

$$
\det V(c_0, \dots, c_n)
= \prod_{i=1}^{n} (c_i - c_0) \cdot \det V(c_1, \dots, c_n)
= \prod_{i=1}^{n} (c_i - c_0) \prod_{1 \le i < j \le n} (c_j - c_i) .
$$

A product in a field is zero exactly when one of its factors is zero,
which gives the last statement. $$\square$$

### Problems for §4.3

> **Problem 4.3.1 (Exercise 4.3.20).** Suppose that
> $$M \in M_{n \times n}(F)$$ can be written in the form
>
> $$M = \begin{pmatrix} A & B \\ O & I \end{pmatrix} ,$$
>
> where $$A$$ is a square matrix. Prove that $$\det(M) = \det(A)$$.
{: .problem #prob-4-3-1 }

*Solution.* Let $$I = I_l$$, so that $$A$$ is
$$(n - l) \times (n - l)$$. The proof is by induction on $$l$$. In every
case the last row of $$M$$ is $$e_n$$, so by the
[Lemma](#lem-4-4) before Theorem 4.4,

$$
\det M = (-1)^{n+n} \det(\tilde{M}_{nn}) = \det(\tilde{M}_{nn}) .
$$

If $$l = 1$$, then $$\tilde{M}_{nn} = A$$ and we are done. If
$$l \ge 2$$, then

$$
\tilde{M}_{nn} = \begin{pmatrix} A & B' \\ O & I_{l-1} \end{pmatrix} ,
$$

where $$B'$$ is $$B$$ without its last column, and
$$\det(\tilde{M}_{nn}) = \det A$$ by the induction hypothesis.
$$\square$$

> **Problem 4.3.2 (Exercise 4.3.21).** Prove that if
> $$M \in M_{n \times n}(F)$$ can be written in the form
>
> $$M = \begin{pmatrix} A & B \\ O & C \end{pmatrix} ,$$
>
> where $$A$$ and $$C$$ are square matrices, then
> $$\det(M) = \det(A) \cdot \det(C)$$.
{: .problem #prob-4-3-2 }

*Solution.* This is [Exercise 4.3.21](#ex-4-3-21), proved above by
induction. Here is a second proof, from
[Problem 4.3.1](#prob-4-3-1). Let $$A$$ be $$k \times k$$ and $$C$$ be
$$l \times l$$. Block multiplication gives

$$
\begin{pmatrix} A & B \\ O & C \end{pmatrix}
= \begin{pmatrix} I_k & O \\ O & C \end{pmatrix}
\begin{pmatrix} A & B \\ O & I_l \end{pmatrix} .
$$

The second factor has determinant $$\det A$$ by
[Problem 4.3.1](#prob-4-3-1). For the first factor, the first row is
$$e_1$$, so by the [Lemma](#lem-4-4) its determinant equals the
determinant of the matrix with its first row and column deleted, which is
$$\begin{pmatrix} I_{k-1} & O \\ O & C \end{pmatrix}$$, or $$C$$ itself
when $$k = 1$$. Repeating $$k$$ times, the first factor has determinant
$$\det C$$. By [Theorem 4.7](#thm-4-7),
$$\det M = \det C \cdot \det A$$. $$\square$$

> **Problem 4.3.3 (Exercise 4.3.22).** Let
> $$T \colon P_n(F) \to F^{n+1}$$ be the linear transformation defined by
> $$T(f) = (f(c_0), f(c_1), \dots, f(c_n))$$, where
> $$c_0, c_1, \dots, c_n$$ are distinct scalars in an infinite field
> $$F$$. Let $$\beta$$ be the standard ordered basis for $$P_n(F)$$ and
> $$\gamma$$ the standard ordered basis for $$F^{n+1}$$.
>
> - **(a)** Show that $$M = [T]_\beta^\gamma$$ has the form
>
>   $$\begin{pmatrix}
>   1 & c_0 & c_0^2 & \cdots & c_0^n \\
>   1 & c_1 & c_1^2 & \cdots & c_1^n \\
>   \vdots & \vdots & \vdots & & \vdots \\
>   1 & c_n & c_n^2 & \cdots & c_n^n
>   \end{pmatrix} .$$
>
>   A matrix with this form is called a **Vandermonde matrix**.
> - **(b)** Prove that $$\det(M) \ne 0$$.
{: .problem #prob-4-3-3 }

*Solution.* (a) $$\beta = \{1, x, x^2, \dots, x^n\}$$. The column of
$$M$$ belonging to $$x^j$$ is
$$[T(x^j)]_\gamma = T(x^j) = (c_0^{\,j}, c_1^{\,j}, \dots, c_n^{\,j})$$,
written as a column. For $$j = 0, 1, \dots, n$$ these are the columns of
the displayed matrix.

(b) By [Exercise 4.3.22](#ex-4-3-22),
$$\det M = \prod_{0 \le i < j \le n} (c_j - c_i)$$, a product of nonzero
scalars because the $$c_i$$ are distinct. A product of nonzero elements
of a field is nonzero. $$\square$$

A second argument for (b) avoids the formula. If $$T(f) = \mathbf{0}$$,
then $$f$$ has the $$n + 1$$ distinct roots $$c_0, \dots, c_n$$, and a
nonzero polynomial of degree at most $$n$$ has at most $$n$$ roots, so
$$f = 0$$. Thus $$T$$ is one-to-one, hence invertible
([Theorems 2.4][thm-2-4] and [2.5][thm-2-5]), so $$M$$ is invertible
([Theorem 2.18][thm-2-18]) and $$\det M \ne 0$$
([Corollary to Theorem 4.7](#cor-4-7)).

> **Problem 4.3.4 (Exercise 4.3.23).** Let
> $$A \in M_{n \times n}(F)$$ be nonzero. For any $$m$$
> ($$1 \le m \le n$$), an $$m \times m$$ **submatrix** is obtained by
> deleting any $$n - m$$ rows and any $$n - m$$ columns of $$A$$.
>
> - **(a)** Let $$k$$ ($$1 \le k \le n$$) denote the largest integer such
>   that some $$k \times k$$ submatrix has a nonzero determinant. Prove
>   that $$\operatorname{rank}(A) = k$$.
> - **(b)** Conversely, suppose that $$\operatorname{rank}(A) = k$$. Prove
>   that there exists a $$k \times k$$ submatrix with a nonzero
>   determinant.
{: .problem #prob-4-3-4 }

*Solution.* Let $$r = \operatorname{rank}(A)$$; since $$A \ne O$$,
$$r \ge 1$$. Two claims give both parts.

*Claim 1. If some $$m \times m$$ submatrix $$N$$ has
$$\det N \ne 0$$, then $$r \ge m$$.* Let $$N$$ use the rows
$$i_1 < \cdots < i_m$$ and the columns $$j_1 < \cdots < j_m$$ of $$A$$.
Since $$\det N \ne 0$$, $$N$$ is invertible
([Corollary to Theorem 4.7](#cor-4-7)) and its columns are linearly
independent. Suppose
$$c_1 a_{j_1} + \cdots + c_m a_{j_m} = \mathbf{0}$$ for the corresponding
columns of $$A$$. Reading this equation only in the rows
$$i_1, \dots, i_m$$ gives the same combination of the columns of $$N$$,
so every $$c_t = 0$$. Thus $$A$$ has $$m$$ linearly independent columns
and $$r \ge m$$ ([Theorem 3.5][thm-3-5]).

*Claim 2. Some $$r \times r$$ submatrix has a nonzero determinant.* By
[Theorem 3.5][thm-3-5], $$A$$ has $$r$$ linearly independent columns.
Let $$A_1$$ be the $$n \times r$$ matrix formed by them, so
$$\operatorname{rank}(A_1) = r$$. Its row space also has dimension $$r$$
([Corollary 2 to Theorem 3.6][cor-3-6-2]), so $$A_1$$ has $$r$$ linearly
independent rows. Let $$N$$ be the $$r \times r$$ matrix formed by those
rows. The rows of $$N$$ are linearly independent, so
$$\operatorname{rank}(N) = r$$, $$N$$ is invertible and
$$\det N \ne 0$$. And $$N$$ is a submatrix of $$A$$.

(a) By Claim 1, $$r \ge k$$. By Claim 2 and the maximality of $$k$$,
$$k \ge r$$. So $$\operatorname{rank}(A) = k$$.

(b) This is Claim 2 with $$r = k$$. $$\square$$

> **Problem 4.3.5 (Exercise 4.3.27).** Let $$C$$ be the classical adjoint
> of $$A \in M_{n \times n}(F)$$. Prove the following statements.
>
> - **(a)** $$\det(C) = [\det(A)]^{n-1}$$.
> - **(b)** $$C^t$$ is the classical adjoint of $$A^t$$.
> - **(c)** If $$A$$ is an invertible upper triangular matrix, then
>   $$C$$ and $$A^{-1}$$ are both upper triangular matrices.
{: .problem #prob-4-3-5 }

*Solution.* Assume $$n \ge 2$$, so that the cofactors are determinants of
matrices of positive size.

(a) By [Exercise 4.3.25](#ex-4-3-25), $$AC = (\det A)\, I_n$$. Taking
determinants,

$$
\det A \cdot \det C = \det\big( (\det A)\, I_n \big) = (\det A)^n .
$$

If $$\det A \ne 0$$, dividing by $$\det A$$ gives
$$\det C = (\det A)^{n-1}$$.

If $$\det A = 0$$, the claim is $$\det C = 0$$. Here $$AC = O$$. Suppose
$$C$$ were invertible. Then $$A = (AC)C^{-1} = O$$, and every cofactor of
the zero matrix is zero, so $$C = O$$, which is not invertible. Hence
$$C$$ is not invertible and $$\det C = 0$$
([Corollary to Theorem 4.7](#cor-4-7)).

(b) Deleting row $$j$$ and column $$i$$ from $$A^t$$ gives the transpose
of the matrix obtained by deleting row $$i$$ and column $$j$$ from
$$A$$. So, by [Theorem 4.8](#thm-4-8),

$$
\operatorname{adj}(A^t)_{ij}
= (-1)^{i+j} \det\big( \widetilde{(A^t)}_{ji} \big)
= (-1)^{i+j} \det\big( (\tilde{A}_{ij})^t \big)
= (-1)^{i+j} \det(\tilde{A}_{ij})
= C_{ji} = (C^t)_{ij} .
$$

(c) We show $$C_{ij} = 0$$ for $$i > j$$. Fix $$i > j$$;
$$C_{ij} = (-1)^{i+j} \det(\tilde{A}_{ji})$$. The $$(p, q)$$ entry of
$$\tilde{A}_{ji}$$ is $$A_{p'q'}$$, where

$$
p' = \begin{cases} p & (p < j) \\ p + 1 & (p \ge j) \end{cases}
\qquad\text{and}\qquad
q' = \begin{cases} q & (q < i) \\ q + 1 & (q \ge i) . \end{cases}
$$

*$$\tilde{A}_{ji}$$ is upper triangular.* Let $$p > q$$. If $$q < i$$,
then $$q' = q < p \le p'$$. If $$q \ge i$$, then
$$p > q \ge i > j$$, so $$p' = p + 1 > q + 1 = q'$$. In both cases
$$p' > q'$$ and $$A_{p'q'} = 0$$.

*It has a zero on its diagonal.* Take $$p = q = j$$. Since $$j < i$$,
$$p' = j + 1$$ and $$q' = j$$, and $$A_{j+1,\,j} = 0$$.

By [Exercise 4.2.23](#ex-4-2-23),
$$\det(\tilde{A}_{ji})$$ is the product of the diagonal entries, which
is zero. So $$C$$ is upper triangular, and so is
$$A^{-1} = \frac{1}{\det A}\, C$$
([Exercise 4.3.25](#ex-4-3-25)). $$\square$$

---

## References

- Stephen H. Friedberg, Arnold J. Insel and Lawrence E. Spence, *Linear
  Algebra*, 5th edition, Pearson, 2018 — Chapter 4, §§4.1 to 4.4, and the
  exercises cited by number.
- Linear Algebra (881.007), Seoul National University, Fall 2023.
  Instructor: Jin Hong (홍진). Lecture slides for Chapter 4 and the course
  problem sheet for Chapter 4.
- The definitions, the statements of the theorems and their numbering are
  the slides'. The slides give the proofs of Theorem 4.3, the Lemma and
  Theorem 4.4 as pictures and one-line outlines; the proofs written here
  follow the textbook.
- The slides state the area formula as a note with a geometric argument,
  reproduced here in three steps. The slides' note on functions
  $$\gamma \colon \mathbb{F}^2 \times \mathbb{F}^2 \to \mathbb{F}$$ that
  are linear in each row and vanish on equal rows is covered by
  Problem 4.1.1.
- The statement on determinants and elementary row operations collects
  remarks made on the slides beside Theorems 4.5 and 4.6 and in the
  summary of §4.4.
- In §4.3 the slides prove Theorems 4.7 and 4.8 and outline the block
  determinant, the adjoint identity and the Vandermonde determinant; the
  remaining details are filled in here. The slides' pictures of the
  orientation of three vectors in $$\mathbb{R}^3$$ are not reproduced.
- The solutions to the problems are mine. Problem 4.3.5 is solved for
  $$n \ge 2$$.

[cor-3-6-2]: /posts/linear-algebra-linear-systems/#cor-3-6-2
[thm-3-1]: /posts/linear-algebra-linear-systems/#thm-3-1
[thm-3-7]: /posts/linear-algebra-linear-systems/#thm-3-7
[cor-3-6-3]: /posts/linear-algebra-linear-systems/#cor-3-6-3
[def-similar]: /posts/linear-algebra-linear-transformations-2/#def-similar
[thm-3-10]: /posts/linear-algebra-linear-systems-2/#thm-3-10
[thm-2-13]: /posts/linear-algebra-linear-transformations/#thm-2-13
[thm-2-4]: /posts/linear-algebra-linear-transformations/#thm-2-4
[thm-2-5]: /posts/linear-algebra-linear-transformations/#thm-2-5
[thm-2-18]: /posts/linear-algebra-linear-transformations-2/#thm-2-18
[thm-3-5]: /posts/linear-algebra-linear-systems/#thm-3-5
