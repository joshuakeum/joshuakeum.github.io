---
title: "Linear Algebra: Elementary Matrix Operations and Systems of Linear Equations (Part 2)"
date: 2026-10-11 01:40:00 +0900
categories: [Course Notes, Linear Algebra]
tags: [systems of linear equations, gaussian elimination, reduced row echelon form]
description: Definitions, theorems with proofs, and solved problems for Chapter 3 of Linear Algebra, §3.3 and §3.4 — solution sets of systems of linear equations, consistency, Gaussian elimination, and the reduced row echelon form.
math: true
mermaid: false
render_with_liquid: false
---

> **How to read the labels.** This post continues
> [Chapter 3, Part 1](/posts/linear-algebra-linear-systems/), which covers
> §3.1 and §3.2, and covers §3.3 and §3.4. Definitions, theorems and their
> numbers follow the lecture slides, which follow the textbook (Friedberg,
> Insel and Spence, 5th edition). A **Problem a.b.k** is the $$k$$-th
> question for §a.b on the course problem sheet, with the textbook's
> exercise number in parentheses. Earlier results are cited by number and
> link to the post that states them.
{: .prompt-info }

Throughout, $$\mathbb{F}$$ is a field,
$$A \in \mathrm{Mat}_{m \times n}(\mathbb{F})$$, and
$$L_A \colon \mathbb{F}^n \to \mathbb{F}^m$$ is left multiplication by
$$A$$. Elements of $$\mathbb{F}^n$$ are columns; in running text a column
is written as a tuple $$(x_1, \dots, x_n)$$. The row operations
$$R_i \leftrightarrow R_j$$, $$R_i \mathrel{\times}= c$$ and
$$R_i \mathrel{+}= c\,R_j$$ are those of
[§3.1][def-elementary-operations].

---

## §3.3 Systems of Linear Equations — Theoretical Aspects

> **Definition (System of linear equations).** Given scalars
> $$a_{ij}, b_i \in \mathbb{F}$$, the following is a **system of $$m$$
> linear equations in $$n$$ unknowns** $$x_1, \dots, x_n$$ over the field
> $$\mathbb{F}$$:
>
> $$
> \begin{aligned}
> a_{11} x_1 + a_{12} x_2 + \cdots + a_{1n} x_n &= b_1 \\
> a_{21} x_1 + a_{22} x_2 + \cdots + a_{2n} x_n &= b_2 \\
> &\ \,\vdots \\
> a_{m1} x_1 + a_{m2} x_2 + \cdots + a_{mn} x_n &= b_m .
> \end{aligned}
> $$
>
> With the **coefficient matrix** $$A = (a_{ij})$$ and the columns
> $$x = (x_1, \dots, x_n)$$ and $$b = (b_1, \dots, b_m)$$, the system is
> the single matrix equation $$Ax = b$$.
{: .definition #def-linear-system }

> **Definition (Solution, consistent, homogeneous).** Consider the system
> $$Ax = b$$.
>
> - **(a)** A **solution** is any $$s \in \mathbb{F}^n$$ with $$As = b$$.
> - **(b)** The **solution set** is
>   $$\{\, s \in \mathbb{F}^n : As = b \,\}$$.
> - **(c)** The system is **consistent** if its solution set is nonempty
>   and **inconsistent** if it is empty.
> - **(d)** The system is **homogeneous** if $$b = \mathbf{0}$$ and
>   **nonhomogeneous** if $$b \ne \mathbf{0}$$.
> - **(e)** $$Ax = \mathbf{0}$$ is the **homogeneous system corresponding
>   to** $$Ax = b$$.
{: .definition #def-solution-set }

A homogeneous system is always consistent, because $$\mathbf{0}$$ is a
solution.

> **Theorem 3.8.** Let
> $$A \in \mathrm{Mat}_{m \times n}(\mathbb{F})$$ and let $$K$$ be the
> solution set of $$Ax = \mathbf{0}$$. Then $$K = \ker(L_A)$$. In
> particular $$K \le \mathbb{F}^n$$ and
>
> $$\dim K = n - \operatorname{rank}(L_A) = n - \operatorname{rank}(A) .$$
{: .theorem #thm-3-8 }

*Proof.* $$K = \{\, s : As = \mathbf{0} \,\}
= \{\, s : L_A(s) = \mathbf{0} \,\} = \ker(L_A)$$, a subspace of
$$\mathbb{F}^n$$ by [Theorem 2.1][thm-2-1]. By the
[Dimension Theorem][thm-2-3],
$$\dim \ker(L_A) = n - \operatorname{rank}(L_A)$$. $$\square$$

> **Corollary to Theorem 3.8.** If $$m < n$$, then $$Ax = \mathbf{0}$$ has
> a nonzero solution.
{: .theorem #cor-3-8 }

*Proof.* $$\operatorname{rank}(A) \le m < n$$
([Theorem 3.6][thm-3-6]), so
$$\dim K = n - \operatorname{rank}(A) > 0$$ and
$$K \ne \{\mathbf{0}\}$$. $$\square$$

**Examples.** Both systems are over $$\mathbb{R}$$, in the unknowns
$$x, y, z$$.

- For
  $$\begin{pmatrix} 1 & 2 & 1 \\ 1 & -1 & -1 \end{pmatrix}
  \begin{pmatrix} x \\ y \\ z \end{pmatrix}
  = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$$
  the coefficient matrix has rank $$2$$, so $$\dim K = 3 - 2 = 1$$. The
  vector $$(1, -2, 3)$$ is a solution, hence
  $$K = \{\, t\,(1, -2, 3) : t \in \mathbb{R} \,\}$$.
- For the single equation $$x - 2y + z = 0$$ the coefficient matrix
  $$\begin{pmatrix} 1 & -2 & 1 \end{pmatrix}$$ has rank $$1$$, so
  $$\dim K = 2$$. The solutions $$(2, 1, 0)$$ and $$(-1, 0, 1)$$ are
  linearly independent, hence
  $$K = \{\, t_1 (2, 1, 0) + t_2 (-1, 0, 1) : t_1, t_2 \in \mathbb{R} \,\}$$.

> **Theorem 3.9.** Suppose $$Ax = b$$ has at least one solution $$s_0$$.
> Let $$K$$ be the solution set of $$Ax = b$$ and $$K_H$$ the solution set
> of the corresponding homogeneous system $$Ax = \mathbf{0}$$. Then
>
> $$K = s_0 + K_H = \{\, s_0 + k : k \in K_H \,\} .$$
{: .theorem #thm-3-9 }

*Proof.* If $$k \in K_H$$, then
$$A(s_0 + k) = As_0 + Ak = b + \mathbf{0} = b$$, so
$$s_0 + k \in K$$. Conversely, if $$Aw = b$$, then
$$A(w - s_0) = Aw - As_0 = b - b = \mathbf{0}$$, so
$$k = w - s_0 \in K_H$$ and $$w = s_0 + k$$. $$\square$$

In the language of [quotient spaces][def-coset], the solution set of a
consistent system is a coset of the subspace $$K_H = \ker(L_A)$$: one
particular solution, shifted by all solutions of the homogeneous system.

**Examples.** With the two coefficient matrices of the previous examples:

- $$\begin{pmatrix} 1 & 2 & 1 \\ 1 & -1 & -1 \end{pmatrix}
  \begin{pmatrix} x \\ y \\ z \end{pmatrix}
  = \begin{pmatrix} 7 \\ -4 \end{pmatrix}$$
  has the solution $$(1, 1, 4)$$, so its solution set is
  $$\{\, (1, 1, 4) + t\,(1, -2, 3) : t \in \mathbb{R} \,\}$$.
- $$x - 2y + z = 4$$ has the solution $$(4, 0, 0)$$, so its solution set
  is $$\{\, (4, 0, 0) + t_1 (2, 1, 0) + t_2 (-1, 0, 1) :
  t_1, t_2 \in \mathbb{R} \,\}$$.

> **Theorem 3.10.** Let
> $$A \in \mathrm{Mat}_{n \times n}(\mathbb{F})$$.
>
> - **(a)** If $$A$$ is invertible, then $$Ax = b$$ has exactly one
>   solution, namely $$A^{-1}b$$.
> - **(b)** If $$Ax = b$$ has exactly one solution, then $$A$$ is
>   invertible.
{: .theorem #thm-3-10 }

*Proof.* (a) $$A(A^{-1}b) = b$$, so $$A^{-1}b$$ is a solution. If
$$As = b$$, then $$s = A^{-1}As = A^{-1}b$$.

(b) Let $$s$$ be the solution. By [Theorem 3.9](#thm-3-9) the solution set
is $$s + K_H$$, and it has one element, so $$K_H = \{\mathbf{0}\}$$. That
is, $$\ker(L_A) = \{\mathbf{0}\}$$ ([Theorem 3.8](#thm-3-8)), so
$$L_A \colon \mathbb{F}^n \to \mathbb{F}^n$$ is one-to-one
([Theorem 2.4][thm-2-4]) and therefore invertible
([Theorem 2.5][thm-2-5]). Hence $$A$$ is invertible
([Corollary 2 to Theorem 2.18][cor-2-18-2]). $$\square$$

> **Definition (Augmented matrix of a system).** The **augmented matrix**
> of the system $$Ax = b$$ is the $$m \times (n+1)$$ matrix
> $$(A \mid b)$$, the coefficient matrix with the column $$b$$ adjoined
> ([augmented matrix][def-augmented-matrix]).
{: .definition #def-augmented-system }

> **Theorem 3.11.** The system $$Ax = b$$ is consistent if and only if
> $$\operatorname{rank}(A) = \operatorname{rank}(A \mid b)$$.
{: .theorem #thm-3-11 }

*Proof.* Let $$a_1, \dots, a_n$$ be the columns of $$A$$. For
$$s = (s_1, \dots, s_n)$$ we have
$$As = s_1 a_1 + \cdots + s_n a_n$$ ([Theorem 2.13][thm-2-13]), so

$$
\begin{aligned}
Ax = b \text{ is consistent}
&\iff b \in \operatorname{span}\{a_1, \dots, a_n\} \\
&\iff \operatorname{span}\{a_1, \dots, a_n\}
   = \operatorname{span}\{a_1, \dots, a_n, b\} \\
&\iff \dim \operatorname{span}\{a_1, \dots, a_n\}
   = \dim \operatorname{span}\{a_1, \dots, a_n, b\} .
\end{aligned}
$$

The last step uses that the first span is a subspace of the second, so
the two are equal exactly when their dimensions are equal
([Theorem 1.11][thm-1-11]). By [Theorem 3.5][thm-3-5] the two
dimensions are $$\operatorname{rank}(A)$$ and
$$\operatorname{rank}(A \mid b)$$. $$\square$$

**Example.** The system
$$\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}
\begin{pmatrix} x \\ y \end{pmatrix}
= \begin{pmatrix} 0 \\ 1 \end{pmatrix}$$
asks for $$x + y = 0$$ and $$x + y = 1$$, and is inconsistent. As the
theorem requires, the coefficient matrix has rank $$1$$ while the
augmented matrix
$$\left(\begin{array}{rr} 1 & 1 \\ 1 & 1 \end{array}
\;\middle\vert\; \begin{array}{r} 0 \\ 1 \end{array}\right)$$
has rank $$2$$.

### Problems for §3.3

> **Problem 3.3.1 (Exercise 3.3.9).** Prove that the system of linear
> equations $$Ax = b$$ has a solution if and only if
> $$b \in R(L_A)$$.
{: .problem #prob-3-3-1 }

*Solution.* A vector $$s \in \mathbb{F}^n$$ is a solution exactly when
$$b = As = L_A(s)$$. So a solution exists if and only if
$$b = L_A(s)$$ for some $$s \in \mathbb{F}^n$$, which is the statement
$$b \in \operatorname{im}(L_A) = R(L_A)$$. $$\square$$

> **Problem 3.3.2 (Exercise 3.3.10).** Prove or give a counterexample to
> the following statement: If the coefficient matrix of a system of $$m$$
> linear equations in $$n$$ unknowns has rank $$m$$, then the system has a
> solution.
{: .problem #prob-3-3-2 }

*Solution.* The statement is true. Let the system be $$Ax = b$$ with
$$A \in \mathrm{Mat}_{m \times n}(\mathbb{F})$$ and
$$\operatorname{rank}(A) = m$$. Then $$\operatorname{im}(L_A)$$ is a
subspace of $$\mathbb{F}^m$$ of dimension $$m$$, so
$$\operatorname{im}(L_A) = \mathbb{F}^m$$
([Theorem 1.11][thm-1-11]). Every $$b \in \mathbb{F}^m$$ therefore lies
in $$\operatorname{im}(L_A)$$, and the system has a solution by
[Problem 3.3.1](#prob-3-3-1). $$\square$$

The same conclusion follows from [Theorem 3.11](#thm-3-11): the augmented
matrix has $$m$$ rows, so
$$m = \operatorname{rank}(A) \le \operatorname{rank}(A \mid b) \le m$$.

---

## §3.4 Systems of Linear Equations — Computational Aspects

> **Definition (Equivalent systems).** Two systems of linear equations in
> the same unknowns are **equivalent** if they have the same solution set.
{: .definition #def-equivalent-systems }

> **Theorem 3.13.** Let
> $$A \in \mathrm{Mat}_{m \times n}(\mathbb{F})$$ and
> $$b \in \mathbb{F}^m$$, and let
> $$C \in \mathrm{Mat}_{m \times m}(\mathbb{F})$$ be invertible. Then the
> systems $$Ax = b$$ and $$(CA)x = Cb$$ are equivalent.
{: .theorem #thm-3-13 }

*Proof.* If $$As = b$$, then $$CAs = Cb$$. Conversely, if
$$CAs = Cb$$, multiplying by $$C^{-1}$$ gives $$As = b$$. $$\square$$

> **Corollary to Theorem 3.13.** If $$(A' \mid b')$$ is obtained from
> $$(A \mid b)$$ by a finite number of elementary row operations, then the
> systems $$Ax = b$$ and $$A'x = b'$$ are equivalent.
{: .theorem #cor-3-13 }

*Proof.* The row operations multiply on the left by a product
$$C = E_p \cdots E_1$$ of elementary matrices
([Theorem 3.1][thm-3-1]), which is invertible
([Theorem 3.2][thm-3-2]). So
$$(A' \mid b') = C\,(A \mid b) = (CA \mid Cb)$$, that is, $$A' = CA$$ and
$$b' = Cb$$, and [Theorem 3.13](#thm-3-13) applies. $$\square$$

So a system may be solved by simplifying its augmented matrix with row
operations. The target of the simplification is the following form.

> **Definition (Reduced row echelon form).** A matrix is in **reduced row
> echelon form** (RREF) if
>
> - **(a)** every zero row, if there is any, lies below every nonzero row;
> - **(b)** the first nonzero entry of each nonzero row is $$1$$, the
>   **leading 1** of the row;
> - **(c)** each leading 1 is the only nonzero entry in its column;
> - **(d)** the leading 1 of each nonzero row lies to the right of the
>   leading 1 of every row above it, so that the leading 1s descend in a
>   staircase.
{: .definition #def-rref }

**Examples.** The first matrix is in reduced row echelon form. The other
three are not: they violate (c), (d) and (b) respectively.

$$
\begin{pmatrix} 1 & 0 & 1 & 0 & 1 \\ 0 & 1 & 0 & 0 & 2 \\ 0 & 0 & 0 & 1 & 3 \end{pmatrix},
\qquad
\begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 0 \\ 1 & 0 & 1 \end{pmatrix}, \qquad
\begin{pmatrix} 0 & 1 & 0 & 2 \\ 1 & 0 & 0 & 1 \\ 0 & 0 & 1 & 1 \end{pmatrix}, \qquad
\begin{pmatrix} 2 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix} .
$$

> **Definition (Gaussian elimination).** **Gaussian elimination** reduces
> a matrix by elementary row operations in two passes.
>
> - **Forward pass.** Find the leftmost nonzero column. Interchange rows
>   to bring a nonzero entry of that column to the top, multiply the top
>   row to make that entry $$1$$, and add multiples of the top row to the
>   rows below to clear the rest of the column below it. Set the top row
>   aside and repeat on the remaining rows, until no rows or no nonzero
>   rows remain.
> - **Backward pass.** Starting from the last nonzero row and moving
>   upward, add multiples of each row to the rows above it to clear the
>   entries above its leading 1.
{: .definition #def-gaussian-elimination }

> **Theorem 3.14.** Gaussian elimination transforms any matrix into a
> matrix in reduced row echelon form.
{: .theorem #thm-3-14 }

*Proof.* After the forward pass, each nonzero row begins with a $$1$$,
because the row was scaled when it was the top row; this is (b). When a
row is set aside, every remaining row has zeros in the column of its
leading 1 and in all columns to the left, since those columns were zero
or have just been cleared. So the leading 1s of later rows lie strictly to
the right, which is (d), and the entries below each leading 1 are zero.
The pass ends when the remaining rows are all zero, so the zero rows are
at the bottom, which is (a).

In the backward pass, the row being used has zeros to the left of its
leading 1, so adding its multiples to rows above changes those rows only
in the column of the leading 1 and to its right. This clears the entries
above the leading 1 without disturbing the leading 1s of the rows above,
which lie further left, or the columns of leading 1s already treated, in
which the row being used has a zero. After the pass each leading 1 is the
only nonzero entry in its column, which is (c), and (a), (b) and (d) still
hold. $$\square$$

**Example.** Solve, over $$\mathbb{R}$$,

$$
\begin{aligned}
3x_1 + 2x_2 + 3x_3 - 2x_4 &= 1 \\
x_1 + x_2 + x_3 \phantom{{}- 2x_4} &= 3 \\
x_1 + 2x_2 + x_3 - x_4 &= 2 .
\end{aligned}
$$

Forward pass on the augmented matrix:

$$
\left(\begin{array}{rrrr} 3 & 2 & 3 & -2 \\ 1 & 1 & 1 & 0 \\ 1 & 2 & 1 & -1 \end{array}
\;\middle\vert\; \begin{array}{r} 1 \\ 3 \\ 2 \end{array}\right)
\xrightarrow{R_1 \leftrightarrow R_3}
\left(\begin{array}{rrrr} 1 & 2 & 1 & -1 \\ 1 & 1 & 1 & 0 \\ 3 & 2 & 3 & -2 \end{array}
\;\middle\vert\; \begin{array}{r} 2 \\ 3 \\ 1 \end{array}\right)
\xrightarrow[R_3 \mathrel{+}= -3R_1]{R_2 \mathrel{+}= -R_1}
\left(\begin{array}{rrrr} 1 & 2 & 1 & -1 \\ 0 & -1 & 0 & 1 \\ 0 & -4 & 0 & 1 \end{array}
\;\middle\vert\; \begin{array}{r} 2 \\ 1 \\ -5 \end{array}\right)
$$

$$
\xrightarrow[R_3 \mathrel{+}= 4R_2]{R_2 \mathrel{\times}= -1}
\left(\begin{array}{rrrr} 1 & 2 & 1 & -1 \\ 0 & 1 & 0 & -1 \\ 0 & 0 & 0 & -3 \end{array}
\;\middle\vert\; \begin{array}{r} 2 \\ -1 \\ -9 \end{array}\right)
\xrightarrow{R_3 \mathrel{\times}= -\frac13}
\left(\begin{array}{rrrr} 1 & 2 & 1 & -1 \\ 0 & 1 & 0 & -1 \\ 0 & 0 & 0 & 1 \end{array}
\;\middle\vert\; \begin{array}{r} 2 \\ -1 \\ 3 \end{array}\right) .
$$

Backward pass:

$$
\xrightarrow[R_2 \mathrel{+}= R_3]{R_1 \mathrel{+}= R_3}
\left(\begin{array}{rrrr} 1 & 2 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{array}
\;\middle\vert\; \begin{array}{r} 5 \\ 2 \\ 3 \end{array}\right)
\xrightarrow{R_1 \mathrel{+}= -2R_2}
\left(\begin{array}{rrrr} 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{array}
\;\middle\vert\; \begin{array}{r} 1 \\ 2 \\ 3 \end{array}\right) .
$$

By the [Corollary to Theorem 3.13](#cor-3-13) the original system is
equivalent to $$x_1 + x_3 = 1$$, $$x_2 = 2$$, $$x_4 = 3$$. Setting
$$x_3 = t$$,

$$
\begin{pmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{pmatrix}
= \begin{pmatrix} 1 - t \\ 2 \\ t \\ 3 \end{pmatrix}
= \begin{pmatrix} 1 \\ 2 \\ 0 \\ 3 \end{pmatrix}
+ t \begin{pmatrix} -1 \\ 0 \\ 1 \\ 0 \end{pmatrix} ,
\qquad t \in \mathbb{R} .
$$

### Reading the general solution off the reduced form

Suppose the augmented matrix $$(A \mid b)$$ is in reduced row echelon
form. If some row is $$(0 \ \cdots \ 0 \mid 1)$$, the system contains the
equation $$0 = 1$$ and is inconsistent. Otherwise, the unknowns whose
columns contain a leading 1 are the **leading variables** and the others
are the **free variables**. Each nonzero row expresses one leading
variable in terms of the free variables. Assigning a parameter to each
free variable gives the **general solution**.

**Example.** Let the augmented matrix be

$$
\left(\begin{array}{rrrrr} 1 & 0 & 2 & 0 & -4 \\ 0 & 1 & -3 & 0 & 5 \\
0 & 0 & 0 & 1 & -6 \\ 0 & 0 & 0 & 0 & 0 \end{array}
\;\middle\vert\; \begin{array}{r} 7 \\ 8 \\ 9 \\ 0 \end{array}\right) .
$$

The last row reads $$0 = 0$$ and the system is consistent. The leading
variables are $$x_1, x_2, x_4$$ and the free variables are $$x_3, x_5$$:

$$
x_1 = 7 - 2x_3 + 4x_5, \qquad x_2 = 8 + 3x_3 - 5x_5, \qquad
x_4 = 9 + 6x_5 .
$$

With $$x_3 = s$$ and $$x_5 = t$$,

$$
\begin{pmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \\ x_5 \end{pmatrix}
= \begin{pmatrix} 7 \\ 8 \\ 0 \\ 9 \\ 0 \end{pmatrix}
+ s \begin{pmatrix} -2 \\ 3 \\ 1 \\ 0 \\ 0 \end{pmatrix}
+ t \begin{pmatrix} 4 \\ -5 \\ 0 \\ 6 \\ 1 \end{pmatrix} .
$$

The first vector is a particular solution, and the other two form a basis
for the solution set of the corresponding homogeneous system. The next
theorem says that this always happens.

> **Theorem 3.15.** Let $$Ax = b$$ be a system of $$r$$ nonzero linear
> equations in $$n$$ unknowns. Suppose that
> $$\operatorname{rank}(A) = \operatorname{rank}(A \mid b)$$ and that
> $$(A \mid b)$$ is in reduced row echelon form, and let the procedure
> above write the solution set as
>
> $$\{\, s_0 + t_1 u_1 + t_2 u_2 + \cdots + t_{n-r} u_{n-r} :
> t_1, \dots, t_{n-r} \in \mathbb{F} \,\} .$$
>
> Then
>
> - **(a)** $$\operatorname{rank}(A) = r$$;
> - **(b)** $$s_0$$ is a particular solution of $$Ax = b$$;
> - **(c)** $$\{u_1, u_2, \dots, u_{n-r}\}$$ is a basis for the solution
>   set of $$Ax = \mathbf{0}$$.
{: .theorem #thm-3-15 }

*Proof.* (a) The $$r$$ rows of $$(A \mid b)$$ are nonzero and the matrix
is in reduced row echelon form. Each row has its leading 1 in a column
where every other row has $$0$$, so in a linear combination of the rows
that equals zero, every coefficient is zero. The rows are linearly
independent, and
$$\operatorname{rank}(A \mid b) = r$$
([Corollary 2 to Theorem 3.6][cor-3-6-2]). By hypothesis
$$\operatorname{rank}(A) = \operatorname{rank}(A \mid b) = r$$.

(b) Take $$t_1 = \cdots = t_{n-r} = 0$$.

(c) Let $$K$$ and $$K_H$$ be the solution sets of $$Ax = b$$ and
$$Ax = \mathbf{0}$$. By [Theorem 3.9](#thm-3-9), $$K = s_0 + K_H$$, so

$$
K_H = \{\, w - s_0 : w \in K \,\}
= \operatorname{span}\{u_1, \dots, u_{n-r}\} .
$$

By [Theorem 3.8](#thm-3-8) and (a), $$\dim K_H = n - r$$. A set of
$$n - r$$ vectors that spans a space of dimension $$n - r$$ is a basis
([Corollary 2 to Theorem 1.10][cor-1-10-2]). $$\square$$

Row operations do not change the solutions of $$Ax = \mathbf{0}$$, and
this ties the columns of a matrix to the columns of its reduced form.

> **Theorem 3.16.** Let
> $$A \in \mathrm{Mat}_{m \times n}(\mathbb{F})$$ have rank $$r > 0$$ and
> columns $$a_1, \dots, a_n$$, and let $$R$$ be a matrix in reduced row
> echelon form obtained from $$A$$ by elementary row operations, with
> columns $$r_1, \dots, r_n$$. Then the columns of $$A$$ and the columns of
> $$R$$ satisfy the same linear relations: for
> $$x_1, \dots, x_n \in \mathbb{F}$$,
>
> $$x_1 a_1 + \cdots + x_n a_n = \mathbf{0}
> \iff x_1 r_1 + \cdots + x_n r_n = \mathbf{0} .$$
>
> Consequently:
>
> - **(a)** $$R$$ has exactly $$r$$ nonzero rows.
> - **(b)** If $$j_1 < j_2 < \cdots < j_r$$ are the columns of $$R$$ that
>   contain the leading 1s, then $$r_{j_i} = e_i$$ for
>   $$i = 1, \dots, r$$.
> - **(c)** The columns $$a_{j_1}, a_{j_2}, \dots, a_{j_r}$$ of $$A$$ are
>   linearly independent, and they form a basis for the column space of
>   $$A$$.
> - **(d)** If $$r_k = d_1 e_1 + d_2 e_2 + \cdots + d_r e_r$$, then
>   $$a_k = d_1 a_{j_1} + d_2 a_{j_2} + \cdots + d_r a_{j_r}$$.
{: .theorem #thm-3-16 }

*Proof.* The row operations give $$R = MA$$ with $$M$$ a product of
elementary matrices, hence invertible
([Theorems 3.1][thm-3-1] and [3.2][thm-3-2]), and
$$r_k = M a_k$$ for every $$k$$ ([Theorem 2.13][thm-2-13]). So

$$
\sum_k x_k r_k = M \Big( \sum_k x_k a_k \Big) ,
$$

and since $$M$$ is invertible, one side is $$\mathbf{0}$$ exactly when the
other is. This is the displayed equivalence.

(a) $$\operatorname{rank}(R) = \operatorname{rank}(A) = r$$
([Corollary to Theorem 3.4][cor-3-4]). As in the proof of
[Theorem 3.15](#thm-3-15), the nonzero rows of $$R$$ are linearly
independent, so their number is the dimension of the row space, which is
$$r$$ ([Corollary 2 to Theorem 3.6][cor-3-6-2]).

(b) The column containing the leading 1 of row $$i$$ has $$1$$ in row
$$i$$ and $$0$$ elsewhere, by condition (c) of the
[reduced row echelon form](#def-rref). That column is $$e_i$$.

(c) If $$c_1 a_{j_1} + \cdots + c_r a_{j_r} = \mathbf{0}$$, the
equivalence gives $$c_1 e_1 + \cdots + c_r e_r = \mathbf{0}$$, so every
$$c_i = 0$$. These are $$r$$ linearly independent vectors in the column
space, which has dimension $$r$$ ([Theorem 3.5][thm-3-5]), so they form
a basis ([Corollary 2 to Theorem 1.10][cor-1-10-2]).

(d) Rows $$r + 1, \dots, m$$ of $$R$$ are zero, so every column of $$R$$
is a combination of $$e_1, \dots, e_r$$. The relation
$$r_k - d_1 r_{j_1} - \cdots - d_r r_{j_r} = \mathbf{0}$$ among the
columns of $$R$$ gives the same relation among the columns of $$A$$.
$$\square$$

**Example.** Let

$$
A = \begin{pmatrix} 2 & 4 & 6 & 2 & 4 \\ 1 & 2 & 3 & 1 & 1 \\
2 & 4 & 8 & 0 & 0 \\ 3 & 6 & 7 & 5 & 9 \end{pmatrix} ,
\qquad
R = \begin{pmatrix} 1 & 2 & 0 & 4 & 0 \\ 0 & 0 & 1 & -1 & 0 \\
0 & 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 & 0 \end{pmatrix} ,
$$

where $$R$$ is the reduced row echelon form of $$A$$. The leading 1s are
in columns $$1, 3, 5$$, so $$\operatorname{rank}(A) = 3$$ and
$$\{a_1, a_3, a_5\}$$ is a basis for the column space of $$A$$. The other
columns of $$R$$ are $$r_2 = 2e_1$$ and $$r_4 = 4e_1 - e_2$$, and
correspondingly

$$
a_2 = 2a_1 , \qquad
a_4 = 4a_1 - a_3 = 4 \begin{pmatrix} 2 \\ 1 \\ 2 \\ 3 \end{pmatrix}
- \begin{pmatrix} 6 \\ 3 \\ 8 \\ 7 \end{pmatrix}
= \begin{pmatrix} 2 \\ 1 \\ 0 \\ 5 \end{pmatrix} .
$$

> **Corollary to Theorem 3.16.** The reduced row echelon form of a matrix
> is unique.
{: .theorem #cor-3-16 }

*Proof.* Let $$R$$ be any matrix in reduced row echelon form obtained from
$$A$$ by elementary row operations. It is enough to show that $$A$$
determines every column of $$R$$. If $$A = O$$, then $$R = O$$. Otherwise
let $$j_1 < \cdots < j_r$$ be the columns of the leading 1s of $$R$$.

*The positions.* In $$R$$, a column $$r_k$$ that contains no leading 1
is a combination of those $$e_i$$ whose leading 1 lies to the left of
column $$k$$, because the staircase shape forces its entries below those
rows to be zero. So $$r_k$$ is a linear combination of
$$r_1, \dots, r_{k-1}$$. A column with a leading 1, say $$r_{j_i} = e_i$$,
is not a combination of the earlier columns, which all lie in
$$\operatorname{span}\{e_1, \dots, e_{i-1}\}$$. By the equivalence of
[Theorem 3.16](#thm-3-16), column $$k$$ of $$R$$ contains a leading 1 if
and only if $$a_k$$ is not a linear combination of
$$a_1, \dots, a_{k-1}$$. This condition involves $$A$$ alone, so
$$j_1, \dots, j_r$$ are determined by $$A$$.

*The entries.* For $$k = j_i$$, $$r_k = e_i$$. For any other $$k$$,
$$r_k = d_1 e_1 + \cdots + d_r e_r$$, where by
[Theorem 3.16](#thm-3-16)(d) the scalars satisfy
$$a_k = d_1 a_{j_1} + \cdots + d_r a_{j_r}$$. Since
$$a_{j_1}, \dots, a_{j_r}$$ are linearly independent, these scalars are
uniquely determined by $$A$$ ([Theorem 1.8][thm-1-8]). $$\square$$

The proof also describes $$R$$ without any computation: the leading
columns are the columns of $$A$$ that are not combinations of the columns
to their left, and every other column of $$R$$ records how the
corresponding column of $$A$$ is built from the leading ones.

### Problems for §3.4

> **Problem 3.4.1 (Exercise 3.4.9).** Let $$W$$ be the subspace of
> $$M_{2 \times 2}(\mathbb{R})$$ consisting of the symmetric
> $$2 \times 2$$ matrices. The set
>
> $$S = \left\{
> \begin{pmatrix} 0 & -1 \\ -1 & 1 \end{pmatrix},
> \begin{pmatrix} 1 & 2 \\ 2 & 3 \end{pmatrix},
> \begin{pmatrix} 2 & 1 \\ 1 & 9 \end{pmatrix},
> \begin{pmatrix} 1 & -2 \\ -2 & 4 \end{pmatrix},
> \begin{pmatrix} -1 & 2 \\ 2 & -1 \end{pmatrix}
> \right\}$$
>
> generates $$W$$. Find a subset of $$S$$ that is a basis for $$W$$.
{: .problem #prob-3-4-1 }

*Solution.* Call the matrices $$M_1, \dots, M_5$$ in the order listed.
The set
$$\beta = \{E^{11},\ E^{12} + E^{21},\ E^{22}\}$$ is a basis for $$W$$,
and the coordinate vector of
$$\begin{pmatrix} a & b \\ b & c \end{pmatrix}$$ relative to $$\beta$$
is $$(a, b, c)$$. Since $$\phi_\beta$$ is an isomorphism
([Theorem 2.21][thm-2-21]), linear relations among the $$M_k$$ are the
same as linear relations among their coordinate vectors. Put the
coordinate vectors in the columns of a matrix and reduce:

$$
\begin{pmatrix} 0 & 1 & 2 & 1 & -1 \\ -1 & 2 & 1 & -2 & 2 \\
1 & 3 & 9 & 4 & -1 \end{pmatrix}
\xrightarrow[R_2 \mathrel{+}= R_1]{R_1 \leftrightarrow R_3}
\begin{pmatrix} 1 & 3 & 9 & 4 & -1 \\ 0 & 5 & 10 & 2 & 1 \\
0 & 1 & 2 & 1 & -1 \end{pmatrix}
$$

$$
\xrightarrow[R_3 \mathrel{+}= -5R_2]{R_2 \leftrightarrow R_3}
\begin{pmatrix} 1 & 3 & 9 & 4 & -1 \\ 0 & 1 & 2 & 1 & -1 \\
0 & 0 & 0 & -3 & 6 \end{pmatrix}
\xrightarrow{R_3 \mathrel{\times}= -\frac13}
\begin{pmatrix} 1 & 3 & 9 & 4 & -1 \\ 0 & 1 & 2 & 1 & -1 \\
0 & 0 & 0 & 1 & -2 \end{pmatrix}
$$

$$
\xrightarrow[R_1 \mathrel{+}= -4R_3]{R_2 \mathrel{+}= -R_3}
\begin{pmatrix} 1 & 3 & 9 & 0 & 7 \\ 0 & 1 & 2 & 0 & 1 \\
0 & 0 & 0 & 1 & -2 \end{pmatrix}
\xrightarrow{R_1 \mathrel{+}= -3R_2}
\begin{pmatrix} 1 & 0 & 3 & 0 & 4 \\ 0 & 1 & 2 & 0 & 1 \\
0 & 0 & 0 & 1 & -2 \end{pmatrix} .
$$

The leading 1s are in columns $$1, 2, 4$$. By
[Theorem 3.16](#thm-3-16)(c) the first, second and fourth coordinate
vectors are a basis for the span of all five, so

$$
\left\{
\begin{pmatrix} 0 & -1 \\ -1 & 1 \end{pmatrix},
\begin{pmatrix} 1 & 2 \\ 2 & 3 \end{pmatrix},
\begin{pmatrix} 1 & -2 \\ -2 & 4 \end{pmatrix}
\right\}
$$

is a basis for $$\operatorname{span}(S) = W$$. Part (d) of the theorem
reads off the other two: $$M_3 = 3M_1 + 2M_2$$ and
$$M_5 = 4M_1 + M_2 - 2M_4$$, which can be checked directly. $$\square$$

> **Problem 3.4.2 (Exercise 3.4.10).** Let
>
> $$V = \{\, (x_1, x_2, x_3, x_4, x_5) \in \mathbb{R}^5 :
> x_1 - 2x_2 + 3x_3 - x_4 + 2x_5 = 0 \,\} .$$
>
> - **(a)** Show that $$S = \{(0, 1, 1, 1, 0)\}$$ is a linearly
>   independent subset of $$V$$.
> - **(b)** Extend $$S$$ to a basis for $$V$$.
{: .problem #prob-3-4-2 }

*Solution.* (a) The vector $$s = (0, 1, 1, 1, 0)$$ satisfies
$$0 - 2 + 3 - 1 + 0 = 0$$, so $$s \in V$$. A set consisting of one
nonzero vector is linearly independent.

(b) $$V$$ is the solution set of a homogeneous system whose coefficient
matrix $$\begin{pmatrix} 1 & -2 & 3 & -1 & 2 \end{pmatrix}$$ is in
reduced row echelon form and has rank $$1$$, so $$\dim V = 5 - 1 = 4$$
([Theorem 3.8](#thm-3-8)). The free variables are
$$x_2, x_3, x_4, x_5$$ and $$x_1 = 2x_2 - 3x_3 + x_4 - 2x_5$$, which
gives the basis ([Theorem 3.15](#thm-3-15))

$$
u_1 = (2, 1, 0, 0, 0), \quad u_2 = (-3, 0, 1, 0, 0), \quad
u_3 = (1, 0, 0, 1, 0), \quad u_4 = (-2, 0, 0, 0, 1) .
$$

Here $$s = u_1 + u_2 + u_3$$, so $$s$$ can take the place of $$u_3$$. The
set

$$
\{(0, 1, 1, 1, 0),\ (2, 1, 0, 0, 0),\ (-3, 0, 1, 0, 0),\ (-2, 0, 0, 0, 1)\}
$$

is linearly independent: if $$a s + b u_1 + c u_2 + d u_4 = \mathbf{0}$$,
then the fifth coordinate gives $$d = 0$$, the fourth gives $$a = 0$$, the
second gives $$a + b = 0$$ and the third gives $$a + c = 0$$, so
$$a = b = c = d = 0$$. Four linearly independent vectors in the
four-dimensional space $$V$$ form a basis
([Corollary 2 to Theorem 1.10][cor-1-10-2]), and this basis contains
$$S$$. $$\square$$

> **Problem 3.4.3 (Exercise 3.4.12).** Let $$V$$ denote the set of all
> solutions to the system of linear equations
>
> $$
> \begin{aligned}
> x_1 - x_2 \phantom{{}- x_3} + 2x_4 - 3x_5 + x_6 &= 0 \\
> 2x_1 - x_2 - x_3 + 3x_4 - 4x_5 + 4x_6 &= 0 .
> \end{aligned}
> $$
>
> - **(a)** Show that
>   $$S = \{(0, -1, 0, 1, 1, 0),\ (1, 0, 1, 1, 1, 0)\}$$ is a linearly
>   independent subset of $$V$$.
> - **(b)** Extend $$S$$ to a basis for $$V$$.
{: .problem #prob-3-4-3 }

*Solution.* Write $$v_1 = (0, -1, 0, 1, 1, 0)$$ and
$$v_2 = (1, 0, 1, 1, 1, 0)$$.

(a) Substituting $$v_1$$: $$0 + 1 + 2 - 3 + 0 = 0$$ and
$$0 + 1 - 0 + 3 - 4 + 0 = 0$$. Substituting $$v_2$$:
$$1 - 0 + 2 - 3 + 0 = 0$$ and $$2 - 0 - 1 + 3 - 4 + 0 = 0$$. So
$$v_1, v_2 \in V$$. If $$a v_1 + b v_2 = \mathbf{0}$$, the first
coordinate gives $$b = 0$$ and then the second gives $$a = 0$$. So $$S$$
is linearly independent.

(b) Reduce the coefficient matrix:

$$
\begin{pmatrix} 1 & -1 & 0 & 2 & -3 & 1 \\ 2 & -1 & -1 & 3 & -4 & 4 \end{pmatrix}
\xrightarrow{R_2 \mathrel{+}= -2R_1}
\begin{pmatrix} 1 & -1 & 0 & 2 & -3 & 1 \\ 0 & 1 & -1 & -1 & 2 & 2 \end{pmatrix}
$$

$$
\xrightarrow{R_1 \mathrel{+}= R_2}
\begin{pmatrix} 1 & 0 & -1 & 1 & -1 & 3 \\ 0 & 1 & -1 & -1 & 2 & 2 \end{pmatrix} .
$$

So $$x_1 = x_3 - x_4 + x_5 - 3x_6$$ and
$$x_2 = x_3 + x_4 - 2x_5 - 2x_6$$, with free variables
$$x_3, x_4, x_5, x_6$$, and $$\dim V = 6 - 2 = 4$$. Setting one free
variable to $$1$$ and the others to $$0$$ gives the basis
([Theorem 3.15](#thm-3-15))

$$
\begin{aligned}
u_1 &= (1, 1, 1, 0, 0, 0), & u_2 &= (-1, 1, 0, 1, 0, 0), \\
u_3 &= (1, -2, 0, 0, 1, 0), & u_4 &= (-3, -2, 0, 0, 0, 1) .
\end{aligned}
$$

Comparing the free coordinates, $$v_1 = u_2 + u_3$$ and
$$v_2 = u_1 + u_2 + u_3$$. So $$v_1$$ and $$v_2$$ can take the places of
$$u_3$$ and $$u_1$$. The set

$$
\{(0, -1, 0, 1, 1, 0),\ (1, 0, 1, 1, 1, 0),\ (-1, 1, 0, 1, 0, 0),\
(-3, -2, 0, 0, 0, 1)\}
$$

is linearly independent: if
$$a v_1 + b v_2 + c u_2 + d u_4 = \mathbf{0}$$, the third coordinate
gives $$b = 0$$, the fifth gives $$a + b = 0$$, the fourth gives
$$a + b + c = 0$$ and the sixth gives $$d = 0$$, so
$$a = b = c = d = 0$$. Four linearly independent vectors in the
four-dimensional space $$V$$ form a basis
([Corollary 2 to Theorem 1.10][cor-1-10-2]), and this basis contains
$$S$$. $$\square$$

> **Problem 3.4.4 (Exercise 3.4.14).** If $$(A \mid b)$$ is in reduced row
> echelon form, prove that $$A$$ is also in reduced row echelon form.
{: .problem #prob-3-4-4 }

*Solution.* $$A$$ is $$(A \mid b)$$ with its last column deleted. Compare
the rows.

A nonzero row of $$(A \mid b)$$ whose leading 1 is not in the last column
gives a nonzero row of $$A$$ with the same first nonzero entry, in the
same column. A row of $$(A \mid b)$$ whose leading 1 is in the last
column gives a zero row of $$A$$. There is at most one such row, since by
(d) the leading 1s are in different columns, and by (d) again it is the
last nonzero row of $$(A \mid b)$$. Zero rows of $$(A \mid b)$$ give zero
rows of $$A$$.

Now check the four conditions for $$A$$.

- (a) The zero rows of $$A$$ are the zero rows of $$(A \mid b)$$ together
  with, possibly, the last nonzero row of $$(A \mid b)$$. They lie below
  all the other rows.
- (b) The first nonzero entry of a nonzero row of $$A$$ is the leading 1
  of the same row of $$(A \mid b)$$.
- (c) That leading 1 is the only nonzero entry in its column of
  $$(A \mid b)$$, and the same column is a column of $$A$$.
- (d) The leading 1s of $$A$$ are leading 1s of $$(A \mid b)$$ in the
  same positions, so they still move to the right going down.

Hence $$A$$ is in reduced row echelon form. $$\square$$

> **Problem 3.4.5 (Exercise 3.4.2(e)).** Solve the following system of
> linear equations.
>
> $$
> \begin{aligned}
> x_1 - 4x_2 - x_3 + x_4 &= 3 \\
> 2x_1 - 8x_2 + x_3 - 4x_4 &= 9 \\
> -x_1 + 4x_2 - 2x_3 + 5x_4 &= -6
> \end{aligned}
> $$
{: .problem #prob-3-4-5 }

*Solution.* Gaussian elimination on the augmented matrix:

$$
\left(\begin{array}{rrrr} 1 & -4 & -1 & 1 \\ 2 & -8 & 1 & -4 \\ -1 & 4 & -2 & 5 \end{array}
\;\middle\vert\; \begin{array}{r} 3 \\ 9 \\ -6 \end{array}\right)
\xrightarrow[R_3 \mathrel{+}= R_1]{R_2 \mathrel{+}= -2R_1}
\left(\begin{array}{rrrr} 1 & -4 & -1 & 1 \\ 0 & 0 & 3 & -6 \\ 0 & 0 & -3 & 6 \end{array}
\;\middle\vert\; \begin{array}{r} 3 \\ 3 \\ -3 \end{array}\right)
$$

$$
\xrightarrow[R_3 \mathrel{+}= 3R_2]{R_2 \mathrel{\times}= \frac13}
\left(\begin{array}{rrrr} 1 & -4 & -1 & 1 \\ 0 & 0 & 1 & -2 \\ 0 & 0 & 0 & 0 \end{array}
\;\middle\vert\; \begin{array}{r} 3 \\ 1 \\ 0 \end{array}\right)
\xrightarrow{R_1 \mathrel{+}= R_2}
\left(\begin{array}{rrrr} 1 & -4 & 0 & -1 \\ 0 & 0 & 1 & -2 \\ 0 & 0 & 0 & 0 \end{array}
\;\middle\vert\; \begin{array}{r} 4 \\ 1 \\ 0 \end{array}\right) .
$$

The system is consistent. The leading variables are $$x_1$$ and $$x_3$$,
and the free variables are $$x_2$$ and $$x_4$$:

$$
x_1 = 4 + 4x_2 + x_4 , \qquad x_3 = 1 + 2x_4 .
$$

With $$x_2 = s$$ and $$x_4 = t$$, the solution set is

$$
\left\{
\begin{pmatrix} 4 \\ 0 \\ 1 \\ 0 \end{pmatrix}
+ s \begin{pmatrix} 4 \\ 1 \\ 0 \\ 0 \end{pmatrix}
+ t \begin{pmatrix} 1 \\ 0 \\ 2 \\ 1 \end{pmatrix}
: s, t \in \mathbb{R} \right\} .
$$

*Check.* $$(4, 0, 1, 0)$$ gives $$4 - 1 = 3$$, $$8 + 1 = 9$$ and
$$-4 - 2 = -6$$. The vectors $$(4, 1, 0, 0)$$ and $$(1, 0, 2, 1)$$ give
$$0$$ in all three equations. $$\square$$

---

## References

- Stephen H. Friedberg, Arnold J. Insel and Lawrence E. Spence, *Linear
  Algebra*, 5th edition, Pearson, 2018 — Chapter 3, §§3.3 and 3.4, and the
  exercises cited by number.
- Linear Algebra (881.007), Seoul National University, Fall 2023.
  Instructor: Jin Hong (홍진). Lecture slides for Chapter 3 and the course
  problem sheet for Chapter 3.
- The definitions, the statements of the theorems and their numbering are
  the slides'. The slides give most proofs as outlines or as pictures, and
  the proofs here fill them in. Theorem 3.14 and the corollary on the
  uniqueness of the reduced row echelon form are stated on the slides
  without proof, and their proofs are written out here.
- The slides label the theorem on equivalent systems "Theorem 3.11", a
  number already used in §3.3. It is Theorem 3.13 in the textbook and
  appears under that number here. The textbook's Theorem 3.12 belongs to a
  section on applications that the course leaves out.
- The slides state Theorem 3.16 as a picture: the columns of $$A$$ and of
  its reduced form satisfy the same linear dependence relations. The four
  parts listed here are the textbook's.
- The solutions to the problems are mine.

[def-elementary-operations]: /posts/linear-algebra-linear-systems/#def-elementary-operations
[thm-2-1]: /posts/linear-algebra-linear-transformations/#thm-2-1
[thm-2-3]: /posts/linear-algebra-linear-transformations/#thm-2-3
[thm-3-6]: /posts/linear-algebra-linear-systems/#thm-3-6
[def-coset]: /posts/linear-algebra-vector-spaces-2/#def-coset
[thm-2-4]: /posts/linear-algebra-linear-transformations/#thm-2-4
[thm-2-5]: /posts/linear-algebra-linear-transformations/#thm-2-5
[cor-2-18-2]: /posts/linear-algebra-linear-transformations-2/#cor-2-18-2
[def-augmented-matrix]: /posts/linear-algebra-linear-systems/#def-augmented-matrix
[thm-2-13]: /posts/linear-algebra-linear-transformations/#thm-2-13
[thm-1-11]: /posts/linear-algebra-vector-spaces-2/#thm-1-11
[thm-3-5]: /posts/linear-algebra-linear-systems/#thm-3-5
[thm-3-1]: /posts/linear-algebra-linear-systems/#thm-3-1
[thm-3-2]: /posts/linear-algebra-linear-systems/#thm-3-2
[cor-3-6-2]: /posts/linear-algebra-linear-systems/#cor-3-6-2
[cor-1-10-2]: /posts/linear-algebra-vector-spaces-2/#cor-1-10-2
[cor-3-4]: /posts/linear-algebra-linear-systems/#cor-3-4
[thm-1-8]: /posts/linear-algebra-vector-spaces-2/#thm-1-8
[thm-2-21]: /posts/linear-algebra-linear-transformations-2/#thm-2-21
