---
title: "Linear Algebra: Elementary Matrix Operations and Systems of Linear Equations (Part 1)"
date: 2026-10-11 01:30:00 +0900
categories: [Course Notes, Linear Algebra]
tags: [elementary matrices, rank, matrix inverse]
description: Definitions, theorems with proofs, and solved problems for Chapter 3 of Linear Algebra, §3.1 and §3.2 — elementary row and column operations, elementary matrices, the rank of a matrix, and the computation of matrix inverses.
math: true
mermaid: false
render_with_liquid: false
---

> **How to read the labels.** Definitions, theorems and their numbers follow
> the lecture slides, which follow the textbook (Friedberg, Insel and Spence,
> 5th edition). An **Exercise a.b.c** is a textbook exercise that the lecture
> stated and used as a theorem. A **Problem a.b.k** is the $$k$$-th question
> for §a.b on the course problem sheet; the sheet for this chapter gives the
> textbook's exercise number, shown in parentheses. Results of Chapters 1 and
> 2 are cited by number and link to the post that states them. Chapter 3 is
> split over two posts: this one covers §3.1 and §3.2, and
> [Part 2](/posts/linear-algebra-linear-systems-2/) covers §3.3 and §3.4.
{: .prompt-info }

Throughout, $$\mathbb{F}$$ is a field, $$e_1, \dots, e_n$$ are the standard
vectors of $$\mathbb{F}^n$$, and $$L_A \colon \mathbb{F}^n \to \mathbb{F}^m$$
is left multiplication by $$A \in \mathrm{Mat}_{m \times n}(\mathbb{F})$$.
The $$i$$-th row of a matrix is $$R_i$$ and its $$j$$-th column is $$C_j$$.

---

## §3.1 Elementary Matrix Operations and Elementary Matrices

> **Definition (Elementary row and column operations).** Let
> $$A \in \mathrm{Mat}_{m \times n}(\mathbb{F})$$. The following are the
> **elementary row (column) operations** on $$A$$.
>
> - **(Type 1)** Interchange two rows (columns).
> - **(Type 2)** Multiply a row (column) by a nonzero scalar.
> - **(Type 3)** Add a scalar multiple of one row (column) to another row
>   (column).
{: .definition #def-elementary-operations }

The slides write the operations in a compact form, used here as well:

| Notation | Operation |
|---|---|
| $$R_i \leftrightarrow R_j$$ | interchange rows $$i$$ and $$j$$ |
| $$R_i \mathrel{\times}= c$$ | multiply row $$i$$ by $$c \ne 0$$ |
| $$R_i \mathrel{+}= c\,R_j$$ | add $$c$$ times row $$j$$ to row $$i$$, where $$i \ne j$$ |

and likewise $$C_i \leftrightarrow C_j$$, $$C_i \mathrel{\times}= c$$ and
$$C_i \mathrel{+}= c\,C_j$$ for columns.

**Example.** One operation of each type, applied to the same matrix:

$$
\begin{pmatrix} 1 & 2 & 3 & 4 \\ 2 & 1 & -1 & 3 \\ 4 & 0 & 1 & 2 \end{pmatrix}
\xrightarrow{R_1 \leftrightarrow R_2}
\begin{pmatrix} 2 & 1 & -1 & 3 \\ 1 & 2 & 3 & 4 \\ 4 & 0 & 1 & 2 \end{pmatrix} ,
$$

$$
\begin{pmatrix} 1 & 2 & 3 & 4 \\ 2 & 1 & -1 & 3 \\ 4 & 0 & 1 & 2 \end{pmatrix}
\xrightarrow{C_2 \mathrel{\times}= 3}
\begin{pmatrix} 1 & 6 & 3 & 4 \\ 2 & 3 & -1 & 3 \\ 4 & 0 & 1 & 2 \end{pmatrix} ,
$$

$$
\begin{pmatrix} 1 & 2 & 3 & 4 \\ 2 & 1 & -1 & 3 \\ 4 & 0 & 1 & 2 \end{pmatrix}
\xrightarrow{R_1 \mathrel{+}= 4R_3}
\begin{pmatrix} 17 & 2 & 7 & 12 \\ 2 & 1 & -1 & 3 \\ 4 & 0 & 1 & 2 \end{pmatrix} .
$$

Each elementary operation is undone by an elementary operation of the same
type: $$R_i \leftrightarrow R_j$$ by itself, $$R_i \mathrel{\times}= c$$ by
$$R_i \mathrel{\times}= c^{-1}$$, and $$R_i \mathrel{+}= c\,R_j$$ by
$$R_i \mathrel{+}= (-c)\,R_j$$.

> **Definition (Elementary matrix).** An $$n \times n$$ **elementary
> matrix** is a matrix obtained by applying one elementary operation to
> $$I_n$$. The type of the operation is the **type** of the elementary
> matrix.
{: .definition #def-elementary-matrix }

**Example.** The three operations of the previous example, applied to an
identity matrix of the matching size, give

$$
\begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad
\begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 3 & 0 & 0 \\ 0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \end{pmatrix}, \qquad
\begin{pmatrix} 1 & 0 & 4 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} .
$$

On $$I_n$$, a row operation and a column operation of the same type give the
same matrices. Interchanging rows $$i$$ and $$j$$ of $$I_n$$ is the same as
interchanging columns $$i$$ and $$j$$; multiplying row $$i$$ by $$c$$ is the
same as multiplying column $$i$$ by $$c$$; and
$$R_i \mathrel{+}= c\,R_j$$ gives the same matrix as
$$C_j \mathrel{+}= c\,C_i$$. So every elementary matrix arises both from a
row operation and from a column operation.

> **Theorem 3.1.** Let
> $$A \in \mathrm{Mat}_{m \times n}(\mathbb{F})$$.
>
> - **(Rows)** If $$A_{\mathrm{row}}$$ is obtained from $$A$$ by an
>   elementary row operation and $$E_m$$ is obtained from $$I_m$$ by the
>   same operation, then $$A_{\mathrm{row}} = E_m A$$.
> - **(Columns)** If $$A_{\mathrm{col}}$$ is obtained from $$A$$ by an
>   elementary column operation and $$E_n$$ is obtained from $$I_n$$ by the
>   same operation, then $$A_{\mathrm{col}} = A E_n$$.
{: .theorem #thm-3-1 }

*Proof.* For any $$E \in \mathrm{Mat}_{m \times m}(\mathbb{F})$$, the
$$i$$-th row of $$EA$$ is the $$i$$-th row of $$E$$ times $$A$$
([Theorem 2.13][thm-2-13]), which is

$$
\sum_{k=1}^{m} E_{ik}\,(\text{row } k \text{ of } A) .
$$

So the rows of $$EA$$ are the linear combinations of the rows of $$A$$
whose coefficients are read off the rows of $$E$$. The $$i$$-th row of
$$I_m$$ picks out row $$i$$ of $$A$$. Now let $$E = E_m$$.

- *Type 1,* $$R_p \leftrightarrow R_q$$. Rows $$p$$ and $$q$$ of $$E$$ are
  rows $$q$$ and $$p$$ of $$I_m$$, so rows $$p$$ and $$q$$ of $$EA$$ are
  rows $$q$$ and $$p$$ of $$A$$. The other rows are unchanged.
- *Type 2,* $$R_p \mathrel{\times}= c$$. Row $$p$$ of $$E$$ is $$c$$ times
  row $$p$$ of $$I_m$$, so row $$p$$ of $$EA$$ is $$c$$ times row $$p$$ of
  $$A$$.
- *Type 3,* $$R_p \mathrel{+}= c\,R_q$$. Row $$p$$ of $$E$$ is row $$p$$ of
  $$I_m$$ plus $$c$$ times row $$q$$ of $$I_m$$, so row $$p$$ of $$EA$$ is
  row $$p$$ of $$A$$ plus $$c$$ times row $$q$$ of $$A$$.

In each case $$EA = A_{\mathrm{row}}$$. The column statement is the same
argument with the columns of $$AE$$: the $$j$$-th column of $$AE$$ is
$$\sum_k E_{kj}\,(\text{column } k \text{ of } A)$$, a combination of the
columns of $$A$$ with coefficients read off the $$j$$-th column of
$$E = E_n$$. $$\square$$

**Example.** For the first operation of the example above,

$$
\begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}
\begin{pmatrix} 1 & 2 & 3 & 4 \\ 2 & 1 & -1 & 3 \\ 4 & 0 & 1 & 2 \end{pmatrix}
=
\begin{pmatrix} 2 & 1 & -1 & 3 \\ 1 & 2 & 3 & 4 \\ 4 & 0 & 1 & 2 \end{pmatrix} .
$$

> **Theorem 3.2.** Elementary matrices are invertible, and the inverse of an
> elementary matrix is an elementary matrix of the same type.
{: .theorem #thm-3-2 }

*Proof.* Let $$E$$ be obtained from $$I_n$$ by an elementary row operation,
and let $$E'$$ be obtained from $$I_n$$ by the operation of the same type
that undoes it. By [Theorem 3.1](#thm-3-1), $$E'E$$ is the result of
applying the undoing operation to $$E$$, which is $$I_n$$. In the same way
$$EE' = I_n$$, because the first operation undoes the second. So $$E$$ is
invertible and $$E^{-1} = E'$$. $$\square$$

**Example.**

$$
\begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}^{-1}
= \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad
\begin{pmatrix} 1 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 1 \end{pmatrix}^{-1}
= \begin{pmatrix} 1 & 0 & 0 \\ 0 & \tfrac13 & 0 \\ 0 & 0 & 1 \end{pmatrix},
$$

$$
\begin{pmatrix} 1 & 0 & 4 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}^{-1}
= \begin{pmatrix} 1 & 0 & -4 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} .
$$

### Problems for §3.1

> **Problem 3.1.1 (Exercise 3.1.12).** Let $$A$$ be an $$m \times n$$
> matrix. Prove that there exists a sequence of elementary row operations of
> types 1 and 3 that transforms $$A$$ into an upper triangular matrix.
{: .problem #prob-3-1-1 }

*Solution.* An $$m \times n$$ matrix $$B$$ is upper triangular when
$$B_{ij} = 0$$ for all $$i > j$$. The proof is by induction on the number of
rows $$m$$, for all $$n$$ at once.

If $$m = 1$$, there are no entries with $$i > j$$, and $$A$$ is already
upper triangular.

Let $$m \ge 2$$ and suppose the claim holds for matrices with $$m - 1$$
rows. First clear the first column below its top entry.

- If the first column of $$A$$ is zero, do nothing.
- Otherwise some $$A_{i1} \ne 0$$. If $$A_{11} = 0$$, apply
  $$R_1 \leftrightarrow R_i$$ (type 1), so that the $$(1,1)$$ entry
  $$a$$ is nonzero. Then for each $$i \ge 2$$ apply
  $$R_i \mathrel{+}= (-a_{i1}/a)\,R_1$$ (type 3), where $$a_{i1}$$ is the
  current $$(i,1)$$ entry. This makes the $$(i,1)$$ entry zero.

The matrix now has the form

$$
\begin{pmatrix} a & r \\ \mathbf{0} & A' \end{pmatrix} ,
$$

where $$r$$ is a row of $$n - 1$$ entries and $$A'$$ is
$$(m-1) \times (n-1)$$. If $$n = 1$$ there is no $$A'$$ and the matrix is
upper triangular. Otherwise, by the induction hypothesis, a sequence of row
operations of types 1 and 3 makes $$A'$$ upper triangular. Apply the same
operations to rows $$2, \dots, m$$ of the whole matrix. They involve only
those rows, whose first entries are all zero, so the first column and the
first row do not change. In the result, an entry in position $$(i, j)$$
with $$i > j$$ is either in the first column, where it is zero, or it is
the $$(i-1, j-1)$$ entry of the upper triangular form of $$A'$$ with
$$i - 1 > j - 1$$, where it is zero as well. $$\square$$

---

## §3.2 The Rank of a Matrix and Matrix Inverses

> **Definition (Rank of a matrix).** The **rank** of
> $$A \in \mathrm{Mat}_{m \times n}(\mathbb{F})$$, written
> $$\operatorname{rank}(A)$$, is the rank of the linear transformation
> $$L_A \colon \mathbb{F}^n \to \mathbb{F}^m$$.
{: .definition #def-rank-matrix }

**Note (invertible means full rank).** For
$$A \in \mathrm{Mat}_{n \times n}(\mathbb{F})$$ the following are
equivalent: $$A$$ is invertible; $$L_A$$ is invertible
([Corollary 2 to Theorem 2.18][cor-2-18-2]); $$L_A$$ is onto, that is,
$$\operatorname{rank}(L_A) = \dim \mathbb{F}^n$$
([Theorem 2.5][thm-2-5]); and $$\operatorname{rank}(A) = n$$. So an
$$n \times n$$ matrix is invertible if and only if its rank is $$n$$.

> **Theorem 3.3.** Let $$T \colon V \to W$$ be linear, where $$V$$ and
> $$W$$ are finite-dimensional with ordered bases $$\beta$$ and
> $$\gamma$$. Then
>
> $$\operatorname{rank}(T) = \operatorname{rank}\big([T]_\beta^\gamma\big) .$$
{: .theorem #thm-3-3 }

*Proof.* Let $$A = [T]_\beta^\gamma$$. By definition
$$\operatorname{rank}(A) = \operatorname{rank}(L_A)$$, and
$$\operatorname{rank}(L_A) = \operatorname{rank}(T)$$ is
[Exercise 2.4.20][ex-2-4-20]: the standard representation
$$\phi_\gamma$$ carries $$\operatorname{im}(T)$$ isomorphically onto
$$\operatorname{im}(L_A)$$. $$\square$$

So the rank of a linear transformation between finite-dimensional spaces
can be computed from any of its matrices, and the rest of the section is
about the rank of a matrix.

> **Theorem 3.4.** Let
> $$A \in \mathrm{Mat}_{m \times n}(\mathbb{F})$$, and let
> $$P \in \mathrm{Mat}_{m \times m}(\mathbb{F})$$ and
> $$Q \in \mathrm{Mat}_{n \times n}(\mathbb{F})$$ be invertible. Then
>
> - **(a)** $$\operatorname{rank}(AQ) = \operatorname{rank}(A)$$,
> - **(b)** $$\operatorname{rank}(PA) = \operatorname{rank}(A)$$,
> - **(c)** $$\operatorname{rank}(PAQ) = \operatorname{rank}(A)$$.
{: .theorem #thm-3-4 }

*Proof.* Recall that $$L_{AQ} = L_A L_Q$$ and $$L_{PA} = L_P L_A$$
([Theorem 2.15][thm-2-15]), and that $$L_P$$ and $$L_Q$$ are invertible
([Corollary 2 to Theorem 2.18][cor-2-18-2]).

(a) Since $$L_Q$$ is onto,

$$
\operatorname{im}(L_{AQ}) = L_A\big(L_Q(\mathbb{F}^n)\big)
= L_A(\mathbb{F}^n) = \operatorname{im}(L_A) ,
$$

and the two ranks are the dimensions of the same space.

(b) Here
$$\operatorname{im}(L_{PA}) = L_P\big(L_A(\mathbb{F}^n)\big)
= L_P\big(\operatorname{im}(L_A)\big)$$. The restriction of $$L_P$$ to the
subspace $$\operatorname{im}(L_A)$$ is linear and one-to-one, so its
nullity is zero and, by the [Dimension Theorem][thm-2-3], its image
$$L_P(\operatorname{im}(L_A))$$ has the same dimension as
$$\operatorname{im}(L_A)$$.

(c) By (a) and then (b),
$$\operatorname{rank}(PAQ) = \operatorname{rank}(PA)
= \operatorname{rank}(A)$$. $$\square$$

> **Corollary to Theorem 3.4.** Elementary row and column operations on a
> matrix are rank-preserving.
{: .theorem #cor-3-4 }

*Proof.* An elementary row operation replaces $$A$$ by $$EA$$ and an
elementary column operation replaces it by $$AE$$, where $$E$$ is an
elementary matrix ([Theorem 3.1](#thm-3-1)). Elementary matrices are
invertible ([Theorem 3.2](#thm-3-2)), so
[Theorem 3.4](#thm-3-4) applies. $$\square$$

> **Definition (Column space, row space).** The **column space** of a
> matrix is the span of its columns, and the **row space** is the span of
> its rows.
{: .definition #def-column-space }

> **Theorem 3.5.** The rank of a matrix is the dimension of its column
> space. Equivalently, it is the maximum number of linearly independent
> columns of the matrix.
{: .theorem #thm-3-5 }

*Proof.* Let $$A \in \mathrm{Mat}_{m \times n}(\mathbb{F})$$. The standard
basis $$\{e_1, \dots, e_n\}$$ of $$\mathbb{F}^n$$ is mapped by $$L_A$$ to
$$L_A(e_j) = Ae_j$$, the $$j$$-th column of $$A$$
([Theorem 2.13][thm-2-13]). By [Theorem 2.2][thm-2-2],

$$
\operatorname{im}(L_A)
= \operatorname{span}\{L_A(e_1), \dots, L_A(e_n)\}
= \text{column space of } A ,
$$

so $$\operatorname{rank}(A) = \dim \operatorname{im}(L_A)$$ is the
dimension of the column space. Some subset of the columns is a basis for
the column space ([Theorem 1.9][thm-1-9]), and no linearly independent
set of columns has more elements than a basis
([Corollary 2 to Theorem 1.10][cor-1-10-2]), so this dimension is the
maximum number of linearly independent columns. $$\square$$

**Example.** By the [Corollary to Theorem 3.4](#cor-3-4), the rank can be
found by simplifying the matrix with row and column operations until the
rank is evident:

$$
\begin{pmatrix} 1 & 2 & 1 \\ 1 & 0 & 3 \\ 1 & 1 & 2 \end{pmatrix}
\xrightarrow[R_3 \mathrel{+}= -R_1]{R_2 \mathrel{+}= -R_1}
\begin{pmatrix} 1 & 2 & 1 \\ 0 & -2 & 2 \\ 0 & -1 & 1 \end{pmatrix}
\xrightarrow[C_3 \mathrel{+}= -C_1]{C_2 \mathrel{+}= -2C_1}
\begin{pmatrix} 1 & 0 & 0 \\ 0 & -2 & 2 \\ 0 & -1 & 1 \end{pmatrix}
\xrightarrow{C_2 \mathrel{+}= C_3}
\begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 2 \\ 0 & 0 & 1 \end{pmatrix}
$$

$$
\xrightarrow{R_2 \mathrel{+}= -2R_3}
\begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}
\xrightarrow{R_2 \leftrightarrow R_3}
\begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}
\xrightarrow{C_2 \leftrightarrow C_3}
\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix} .
$$

The last matrix has column space
$$\operatorname{span}\{e_1, e_2\}$$, so the rank is $$2$$.

**Note (one operation at a time).** When two operations are written over
one arrow, they are still performed one after the other. Applying
$$R_2 \mathrel{+}= R_1$$ and $$R_1 \mathrel{+}= R_2$$ to $$I_2$$ "at the
same time", each using the original rows, would give
$$\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$$, which has rank $$1$$.
That is not a sequence of elementary operations. Done in order,

$$
\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}
\xrightarrow{R_2 \mathrel{+}= R_1}
\begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}
\xrightarrow{R_1 \mathrel{+}= R_2}
\begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} ,
$$

and the rank stays $$2$$.

> **Theorem 3.6.** Let
> $$A \in \mathrm{Mat}_{m \times n}(\mathbb{F})$$ with
> $$\operatorname{rank}(A) = r$$. Then $$r \le \min(m, n)$$, and a finite
> number of elementary row and column operations transforms $$A$$ into the
> matrix
>
> $$D = \begin{pmatrix} I_r & O_{r \times (n-r)} \\
> O_{(m-r) \times r} & O_{(m-r) \times (n-r)} \end{pmatrix} .$$
{: .theorem #thm-3-6 }

*Proof.* The column space of $$A$$ is a subspace of $$\mathbb{F}^m$$
spanned by $$n$$ vectors, so its dimension $$r$$ is at most $$m$$
([Theorem 1.11][thm-1-11]) and at most $$n$$
([Corollary 2 to Theorem 1.10][cor-1-10-2]).

For the reduction, it is enough to show that $$A$$ can be transformed into
a matrix of the form $$D$$ with *some* number $$s$$ of ones. Indeed, the
operations preserve the rank ([Corollary to Theorem 3.4](#cor-3-4)), and
the column space of such a matrix is
$$\operatorname{span}\{e_1, \dots, e_s\}$$, of dimension $$s$$
([Theorem 3.5](#thm-3-5)). So $$s = r$$.

The reduction is by induction on $$m$$, for all $$n$$ at once. If
$$A = O$$ there is nothing to do ($$s = 0$$). Otherwise:

1. Some entry $$A_{ij}$$ is nonzero. Apply $$R_1 \leftrightarrow R_i$$ and
   $$C_1 \leftrightarrow C_j$$ to move it to position $$(1,1)$$, and
   multiply the first row by its inverse, so that the $$(1,1)$$ entry
   is $$1$$.
2. Add multiples of the first row to the other rows to make the rest of the
   first column zero. Then add multiples of the first column to the other
   columns to make the rest of the first row zero.

The matrix is now
$$\begin{pmatrix} 1 & \mathbf{0} \\ \mathbf{0} & A' \end{pmatrix}$$ with
$$A'$$ of size $$(m-1) \times (n-1)$$. If $$m = 1$$ or $$n = 1$$ there is
no $$A'$$ and the matrix has the required form, which also settles the
base case $$m = 1$$. Otherwise, by the induction hypothesis, $$A'$$ can be
brought to the required form by elementary operations. Performed on rows
$$2, \dots, m$$ and columns $$2, \dots, n$$ of the whole matrix, these
operations do not change the first row or the first column, whose entries
outside position $$(1,1)$$ are zero. The result has the form $$D$$.
$$\square$$

**Example.** The procedure of the proof, with each step clearing one row
and one column:

$$
\begin{pmatrix} 0 & 2 & 4 & 2 & 2 \\ 4 & 4 & 4 & 8 & 0 \\ 8 & 2 & 0 & 10 & 2 \\
6 & 3 & 2 & 9 & 1 \end{pmatrix}
\longrightarrow
\begin{pmatrix} 1 & 0 & 0 & 0 & 0 \\ 0 & 2 & 4 & 2 & 2 \\ 0 & -6 & -8 & -6 & 2 \\
0 & -3 & -4 & -3 & 1 \end{pmatrix}
$$

$$
\longrightarrow
\begin{pmatrix} 1 & 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 4 & 0 & 8 \\
0 & 0 & 2 & 0 & 4 \end{pmatrix}
\longrightarrow
\begin{pmatrix} 1 & 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \end{pmatrix} .
$$

The first arrow is $$R_1 \leftrightarrow R_2$$,
$$R_1 \mathrel{\times}= \tfrac14$$, then $$R_3 \mathrel{+}= -8R_1$$ and
$$R_4 \mathrel{+}= -6R_1$$, then $$C_2 \mathrel{+}= -C_1$$,
$$C_3 \mathrel{+}= -C_1$$ and $$C_4 \mathrel{+}= -2C_1$$. The second and
third arrows repeat this on the lower right block. The rank is $$3$$.

> **Corollary 1 to Theorem 3.6.** Let
> $$A \in \mathrm{Mat}_{m \times n}(\mathbb{F})$$ with
> $$\operatorname{rank}(A) = r$$. Then there exist invertible matrices
> $$P \in \mathrm{Mat}_{m \times m}(\mathbb{F})$$ and
> $$Q \in \mathrm{Mat}_{n \times n}(\mathbb{F})$$ such that
>
> $$PAQ = \begin{pmatrix} I_r & O \\ O & O \end{pmatrix} .$$
{: .theorem #cor-3-6-1 }

*Proof.* By [Theorem 3.6](#thm-3-6), elementary row and column operations
take $$A$$ to $$D$$. By [Theorem 3.1](#thm-3-1) each row operation is a
multiplication on the left by an elementary $$m \times m$$ matrix, and each
column operation is a multiplication on the right by an elementary
$$n \times n$$ matrix. So

$$
D = E_p \cdots E_2 E_1\, A\, G_1 G_2 \cdots G_q
$$

for elementary matrices $$E_i$$ and $$G_j$$. Put
$$P = E_p \cdots E_1$$ and $$Q = G_1 \cdots G_q$$. Both are products of
invertible matrices ([Theorem 3.2](#thm-3-2)), hence invertible.
$$\square$$

> **Corollary 2 to Theorem 3.6.** Let
> $$A \in \mathrm{Mat}_{m \times n}(\mathbb{F})$$.
>
> - **(a)** $$\operatorname{rank}(A^t) = \operatorname{rank}(A)$$.
> - **(b)** The row space and the column space of $$A$$ have the same
>   dimension, $$\operatorname{rank}(A)$$. In particular, the rank of
>   $$A$$ is also the maximum number of linearly independent rows.
{: .theorem #cor-3-6-2 }

*Proof.* (a) Let $$PAQ = D$$ as in
[Corollary 1](#cor-3-6-1), with $$r = \operatorname{rank}(A)$$. Then
$$D^t = Q^t A^t P^t$$. The matrices $$Q^t$$ and $$P^t$$ are invertible,
with inverses $$(Q^{-1})^t$$ and $$(P^{-1})^t$$, and $$D^t$$ is the
$$n \times m$$ matrix of the same shape as $$D$$, of rank $$r$$. By
[Theorem 3.4](#thm-3-4),

$$
\operatorname{rank}(A^t) = \operatorname{rank}(Q^t A^t P^t)
= \operatorname{rank}(D^t) = r = \operatorname{rank}(A) .
$$

(b) The rows of $$A$$ are the columns of $$A^t$$, so the dimension of the
row space of $$A$$ is the dimension of the column space of $$A^t$$, which
is $$\operatorname{rank}(A^t) = \operatorname{rank}(A)$$ by
[Theorem 3.5](#thm-3-5) and (a). $$\square$$

> **Corollary 3 to Theorem 3.6.** Every invertible matrix is a product of
> elementary matrices.
{: .theorem #cor-3-6-3 }

*Proof.* Let $$A \in \mathrm{Mat}_{n \times n}(\mathbb{F})$$ be invertible.
Then $$\operatorname{rank}(A) = n$$, so $$D = I_n$$ and
[Corollary 1](#cor-3-6-1) gives $$PAQ = I_n$$ with
$$P = E_p \cdots E_1$$ and $$Q = G_1 \cdots G_q$$ products of elementary
matrices. Hence

$$
A = P^{-1} Q^{-1}
= E_1^{-1} \cdots E_p^{-1}\, G_q^{-1} \cdots G_1^{-1} ,
$$

and the inverse of an elementary matrix is again an elementary matrix
([Theorem 3.2](#thm-3-2)). $$\square$$

> **Theorem 3.7.** Let $$T \colon V \to W$$ and $$U \colon W \to Z$$ be
> linear transformations on finite-dimensional vector spaces, and let
> $$A$$ and $$B$$ be matrices for which $$AB$$ is defined. Then
>
> - **(a)** $$\operatorname{rank}(UT) \le \operatorname{rank}(U)$$,
> - **(b)** $$\operatorname{rank}(UT) \le \operatorname{rank}(T)$$,
> - **(c)** $$\operatorname{rank}(AB) \le \operatorname{rank}(A)$$,
> - **(d)** $$\operatorname{rank}(AB) \le \operatorname{rank}(B)$$.
{: .theorem #thm-3-7 }

*Proof.* (a)
$$\operatorname{im}(UT) = U(T(V)) \subseteq U(W) = \operatorname{im}(U)$$,
and a subspace has dimension at most that of the space containing it
([Theorem 1.11][thm-1-11]).

(b) $$\operatorname{im}(UT) = U(\operatorname{im}(T))$$. If $$\gamma$$ is
a basis for $$\operatorname{im}(T)$$, then $$U(\gamma)$$ spans
$$U(\operatorname{im}(T))$$ ([Theorem 2.2][thm-2-2], applied to the
restriction of $$U$$ to $$\operatorname{im}(T)$$). A space spanned by at
most $$\lvert \gamma \rvert$$ vectors has dimension at most
$$\lvert \gamma \rvert = \operatorname{rank}(T)$$
([Corollary 2 to Theorem 1.10][cor-1-10-2]).

(c) By (a) and [Theorem 2.15][thm-2-15],
$$\operatorname{rank}(AB) = \operatorname{rank}(L_A L_B)
\le \operatorname{rank}(L_A) = \operatorname{rank}(A)$$.

(d) By (b),
$$\operatorname{rank}(AB) = \operatorname{rank}(L_A L_B)
\le \operatorname{rank}(L_B) = \operatorname{rank}(B)$$. $$\square$$

### Computing the inverse of a matrix

> **Definition (Augmented matrix).** For
> $$A \in \mathrm{Mat}_{m \times n}(\mathbb{F})$$ and
> $$B \in \mathrm{Mat}_{m \times p}(\mathbb{F})$$, the **augmented
> matrix** $$(A \mid B)$$ is the $$m \times (n + p)$$ matrix whose first
> $$n$$ columns are the columns of $$A$$ and whose last $$p$$ columns are
> the columns of $$B$$.
{: .definition #def-augmented-matrix }

For an $$m \times m$$ matrix $$M$$, the columns of $$M(A \mid B)$$ are
$$M$$ times the columns of $$(A \mid B)$$, so

$$
M\,(A \mid B) = (MA \mid MB) .
$$

> **Inverse by row reduction.** Let
> $$A \in \mathrm{Mat}_{n \times n}(\mathbb{F})$$.
>
> - **(a)** If $$A$$ is invertible, then $$(A \mid I_n)$$ can be
>   transformed into $$(I_n \mid A^{-1})$$ by a finite number of elementary
>   row operations.
> - **(b)** If $$(A \mid I_n)$$ can be transformed into $$(I_n \mid B)$$ by
>   a finite number of elementary row operations, then $$A$$ is invertible
>   and $$B = A^{-1}$$.
> - **(c)** If $$A$$ is not invertible, then no sequence of elementary row
>   operations transforms $$(A \mid I_n)$$ into a matrix of the form
>   $$(I_n \mid B)$$.
{: .theorem #inverse-by-row-reduction }

*Proof.* A sequence of elementary row operations multiplies the matrix on
the left by a product $$M = E_p \cdots E_1$$ of elementary matrices
([Theorem 3.1](#thm-3-1)), and $$M$$ is invertible
([Theorem 3.2](#thm-3-2)). It takes $$(A \mid I_n)$$ to
$$(MA \mid M)$$.

(a) $$A^{-1}$$ is invertible, hence a product of elementary matrices
([Corollary 3 to Theorem 3.6](#cor-3-6-3)). The corresponding row
operations give $$(A^{-1}A \mid A^{-1}) = (I_n \mid A^{-1})$$.

(b) If $$(MA \mid M) = (I_n \mid B)$$, then $$MA = I_n$$ and $$M = B$$.
Since $$M$$ is invertible, $$A = M^{-1}$$ is invertible and
$$A^{-1} = M = B$$.

(c) This is the contrapositive of (b). In practice the failure shows up as
a zero row: $$\operatorname{rank}(MA) = \operatorname{rank}(A) < n$$
([Theorem 3.4](#thm-3-4)), so the left block can never become $$I_n$$.
$$\square$$

Only row operations are used. Mixing in column operations would multiply
on the right as well, and the right block would no longer be the inverse.

**Example.** Let
$$A = \begin{pmatrix} 0 & 3 & 2 \\ 2 & 0 & -1 \\ 1 & 2 & 1 \end{pmatrix}$$.

$$
\left(\begin{array}{rrr} 0 & 3 & 2 \\ 2 & 0 & -1 \\ 1 & 2 & 1 \end{array}
\;\middle\vert\;
\begin{array}{rrr} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array}\right)
\xrightarrow{R_1 \leftrightarrow R_3}
\left(\begin{array}{rrr} 1 & 2 & 1 \\ 2 & 0 & -1 \\ 0 & 3 & 2 \end{array}
\;\middle\vert\;
\begin{array}{rrr} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{array}\right)
$$

$$
\xrightarrow{R_2 \mathrel{+}= -2R_1}
\left(\begin{array}{rrr} 1 & 2 & 1 \\ 0 & -4 & -3 \\ 0 & 3 & 2 \end{array}
\;\middle\vert\;
\begin{array}{rrr} 0 & 0 & 1 \\ 0 & 1 & -2 \\ 1 & 0 & 0 \end{array}\right)
\xrightarrow{R_2 \mathrel{+}= R_3}
\left(\begin{array}{rrr} 1 & 2 & 1 \\ 0 & -1 & -1 \\ 0 & 3 & 2 \end{array}
\;\middle\vert\;
\begin{array}{rrr} 0 & 0 & 1 \\ 1 & 1 & -2 \\ 1 & 0 & 0 \end{array}\right)
$$

$$
\xrightarrow[R_3 \mathrel{+}= 3R_2]{R_1 \mathrel{+}= 2R_2}
\left(\begin{array}{rrr} 1 & 0 & -1 \\ 0 & -1 & -1 \\ 0 & 0 & -1 \end{array}
\;\middle\vert\;
\begin{array}{rrr} 2 & 2 & -3 \\ 1 & 1 & -2 \\ 4 & 3 & -6 \end{array}\right)
\xrightarrow[R_3 \mathrel{\times}= -1]{R_2 \mathrel{\times}= -1}
\left(\begin{array}{rrr} 1 & 0 & -1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array}
\;\middle\vert\;
\begin{array}{rrr} 2 & 2 & -3 \\ -1 & -1 & 2 \\ -4 & -3 & 6 \end{array}\right)
$$

$$
\xrightarrow[R_2 \mathrel{+}= -R_3]{R_1 \mathrel{+}= R_3}
\left(\begin{array}{rrr} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array}
\;\middle\vert\;
\begin{array}{rrr} -2 & -1 & 3 \\ 3 & 2 & -4 \\ -4 & -3 & 6 \end{array}\right) .
$$

So

$$
A^{-1} = \begin{pmatrix} -2 & -1 & 3 \\ 3 & 2 & -4 \\ -4 & -3 & 6 \end{pmatrix} ,
$$

and multiplying out confirms $$A A^{-1} = I_3$$.

**Example (a matrix that is not invertible).** For
$$A = \begin{pmatrix} 0 & 3 & 3 \\ 2 & 0 & -2 \\ 1 & 3 & 2 \end{pmatrix}$$,
the operations $$R_1 \leftrightarrow R_3$$, $$R_2 \mathrel{+}= -2R_1$$ and
$$R_2 \mathrel{+}= 2R_3$$ turn the left block into

$$
\begin{pmatrix} 1 & 3 & 2 \\ 0 & 0 & 0 \\ 0 & 3 & 3 \end{pmatrix} .
$$

A zero row has appeared, so $$\operatorname{rank}(A) = 2 < 3$$ and $$A$$
is not invertible.

### Problems for §3.2

> **Problem 3.2.1 (Exercise 3.2.11).** Let
>
> $$B = \begin{pmatrix} 1 & 0 & \cdots & 0 \\ 0 & & & \\ \vdots & & B' & \\
> 0 & & & \end{pmatrix} ,$$
>
> where $$B'$$ is an $$m \times n$$ submatrix of $$B$$. Prove that if
> $$\operatorname{rank}(B) = r$$, then
> $$\operatorname{rank}(B') = r - 1$$.
{: .problem #prob-3-2-1 }

*Solution.* Let $$s = \operatorname{rank}(B')$$ and let
$$\{w_1, \dots, w_s\}$$ be a basis for the column space of $$B'$$, a
subspace of $$\mathbb{F}^m$$ ([Theorem 3.5](#thm-3-5)). For
$$y \in \mathbb{F}^m$$ write $$\hat{y} \in \mathbb{F}^{m+1}$$ for the
column with first entry $$0$$ followed by the entries of $$y$$. The map
$$y \mapsto \hat{y}$$ is linear.

The columns of $$B$$ are $$e_1$$ and the vectors $$\hat{b}$$, where $$b$$
runs over the columns of $$B'$$. Each such $$b$$ is a linear combination
of $$w_1, \dots, w_s$$, so $$\hat{b}$$ is the same combination of
$$\hat{w}_1, \dots, \hat{w}_s$$. Hence

$$
\{e_1, \hat{w}_1, \dots, \hat{w}_s\}
$$

spans the column space of $$B$$. It is linearly independent: if
$$a\,e_1 + c_1 \hat{w}_1 + \cdots + c_s \hat{w}_s = \mathbf{0}$$, the
first entry gives $$a = 0$$ and the remaining entries give
$$c_1 w_1 + \cdots + c_s w_s = \mathbf{0}$$, so every $$c_i = 0$$. It is
therefore a basis for the column space of $$B$$, and
$$r = \operatorname{rank}(B) = s + 1$$. $$\square$$

> **Problem 3.2.2 (Exercise 3.2.14).** Let $$T, U \colon V \to W$$ be
> linear transformations.
>
> - **(a)** Prove that $$R(T + U) \subseteq R(T) + R(U)$$.
> - **(b)** Prove that if $$W$$ is finite-dimensional, then
>   $$\operatorname{rank}(T + U) \le \operatorname{rank}(T) +
>   \operatorname{rank}(U)$$.
> - **(c)** Prove that
>   $$\operatorname{rank}(A + B) \le \operatorname{rank}(A) +
>   \operatorname{rank}(B)$$ for any $$m \times n$$ matrices $$A$$ and
>   $$B$$.
{: .problem #prob-3-2-2 }

*Solution.* (a) For $$v \in V$$,
$$(T + U)(v) = T(v) + U(v)$$ with $$T(v) \in \operatorname{im}(T)$$ and
$$U(v) \in \operatorname{im}(U)$$. So every element of
$$\operatorname{im}(T + U)$$ lies in
$$\operatorname{im}(T) + \operatorname{im}(U)$$.

(b) The sum $$\operatorname{im}(T) + \operatorname{im}(U)$$ is a subspace
of $$W$$ ([Exercise 1.3.23][ex-1-3-23]). Let $$\beta_1$$ and
$$\beta_2$$ be bases for $$\operatorname{im}(T)$$ and
$$\operatorname{im}(U)$$; they are finite because $$W$$ is
finite-dimensional ([Theorem 1.11][thm-1-11]). Every element of the sum
is a combination of vectors of $$\beta_1$$ plus a combination of vectors
of $$\beta_2$$, so $$\beta_1 \cup \beta_2$$ spans the sum and

$$
\dim\big(\operatorname{im}(T) + \operatorname{im}(U)\big)
\le \lvert \beta_1 \cup \beta_2 \rvert
\le \operatorname{rank}(T) + \operatorname{rank}(U)
$$

by [Corollary 2 to Theorem 1.10][cor-1-10-2]. By (a) and
[Theorem 1.11][thm-1-11],
$$\operatorname{rank}(T + U) \le
\dim(\operatorname{im}(T) + \operatorname{im}(U))$$.

(c) $$L_{A+B} = L_A + L_B$$ ([Theorem 2.15][thm-2-15]), so (b) with
$$T = L_A$$ and $$U = L_B$$ gives
$$\operatorname{rank}(A + B) = \operatorname{rank}(L_A + L_B)
\le \operatorname{rank}(L_A) + \operatorname{rank}(L_B)
= \operatorname{rank}(A) + \operatorname{rank}(B)$$. $$\square$$

> **Problem 3.2.3 (Exercise 3.2.19).** Let $$A$$ be an $$m \times n$$
> matrix with rank $$m$$ and $$B$$ be an $$n \times p$$ matrix with rank
> $$n$$. Determine the rank of $$AB$$. Justify your answer.
{: .problem #prob-3-2-3 }

*Solution.* $$\operatorname{rank}(AB) = m$$.

The image of $$L_B \colon \mathbb{F}^p \to \mathbb{F}^n$$ is a subspace of
$$\mathbb{F}^n$$ of dimension $$n$$, so it is all of $$\mathbb{F}^n$$
([Theorem 1.11][thm-1-11]): $$L_B$$ is onto. In the same way
$$L_A \colon \mathbb{F}^n \to \mathbb{F}^m$$ is onto. Therefore

$$
\operatorname{im}(L_{AB}) = L_A\big(L_B(\mathbb{F}^p)\big)
= L_A(\mathbb{F}^n) = \mathbb{F}^m ,
$$

and $$\operatorname{rank}(AB) = \dim \mathbb{F}^m = m$$. $$\square$$

> **Problem 3.2.4 (Exercise 3.2.21).** Let $$A$$ be an $$m \times n$$
> matrix with rank $$m$$. Prove that there exists an $$n \times m$$ matrix
> $$B$$ such that $$AB = I_m$$.
{: .problem #prob-3-2-4 }

*Solution.* Since $$\operatorname{rank}(A) = m = \dim \mathbb{F}^m$$, the
map $$L_A \colon \mathbb{F}^n \to \mathbb{F}^m$$ is onto
([Theorem 1.11][thm-1-11]). For each $$j = 1, \dots, m$$ choose
$$b_j \in \mathbb{F}^n$$ with $$A b_j = e_j$$, and let $$B$$ be the
$$n \times m$$ matrix whose columns are $$b_1, \dots, b_m$$. The $$j$$-th
column of $$AB$$ is $$A b_j = e_j$$ ([Theorem 2.13][thm-2-13]), so
$$AB = I_m$$. $$\square$$

---

## References

- Stephen H. Friedberg, Arnold J. Insel and Lawrence E. Spence, *Linear
  Algebra*, 5th edition, Pearson, 2018 — Chapter 3, §§3.1 and 3.2, and the
  exercises cited by number.
- Linear Algebra (881.007), Seoul National University, Fall 2023.
  Instructor: Jin Hong (홍진). Lecture slides for Chapter 3 and the course
  problem sheet for Chapter 3.
- The definitions, the statements of the theorems and their numbering are
  the slides'. The slides give most proofs as outlines, and the proofs here
  fill in those outlines. Theorems 3.1, 3.2 and 3.6 are stated on the
  slides without proof, and their proofs are written out here.
- The slides leave the three corollaries of Theorem 3.6 unnumbered; they
  are numbered here in the textbook's order. The statement on computing an
  inverse by row reduction collects two notes of the slides.
- Not every worked example of the slides is reproduced. In the example of
  a matrix that is not invertible, the slide labels its last step
  $$R_2 \mathrel{+}= R_3$$; the step that produces the zero row shown
  there is $$R_2 \mathrel{+}= 2R_3$$, used here.
- The solutions to the problems are mine.

[thm-2-13]: /posts/linear-algebra-linear-transformations/#thm-2-13
[cor-2-18-2]: /posts/linear-algebra-linear-transformations-2/#cor-2-18-2
[thm-2-5]: /posts/linear-algebra-linear-transformations/#thm-2-5
[ex-2-4-20]: /posts/linear-algebra-linear-transformations-2/#ex-2-4-20
[thm-2-15]: /posts/linear-algebra-linear-transformations/#thm-2-15
[thm-2-3]: /posts/linear-algebra-linear-transformations/#thm-2-3
[thm-2-2]: /posts/linear-algebra-linear-transformations/#thm-2-2
[thm-1-9]: /posts/linear-algebra-vector-spaces-2/#thm-1-9
[cor-1-10-2]: /posts/linear-algebra-vector-spaces-2/#cor-1-10-2
[thm-1-11]: /posts/linear-algebra-vector-spaces-2/#thm-1-11
[ex-1-3-23]: /posts/linear-algebra-vector-spaces/#ex-1-3-23
