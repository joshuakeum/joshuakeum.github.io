---
title: "Linear Algebra: Course Overview"
date: 2026-10-11 00:10:00 +0900
categories: [Course Notes, Linear Algebra]
tags: [overview, linear algebra, vector spaces, linear transformations, determinant]
description: Course information, scope, chapter contents, and notation for Linear Algebra, Fall 2023.
math: true
mermaid: false
render_with_liquid: false
---

## Course information

| Item | Detail |
|---|---|
| Course | Linear Algebra, 881.007 |
| Institution | Seoul National University |
| Department | Department of Mathematical Sciences |
| Semester | Fall 2023 |
| Credits | 3 |
| Instructor | Jin Hong (홍진) |
| Textbook | Stephen H. Friedberg, Arnold J. Insel and Lawrence E. Spence, *Linear Algebra*, 5th edition, Pearson, 2018 |

## Objective and scope

The syllabus states the objective in one line: to learn the basic theory of
linear algebra — vector spaces, linear maps, determinants, and
diagonalization.

The course covers Chapters 1 through 6 of the textbook, leaving out the
sections on applications. It assumes that vector spaces, linear maps, matrix
products and determinants are already familiar at the level of Mathematics 1
(Hong Jong Kim, *Calculus 1*, Chapters 5 to 7), written up on this site
under [Calculus 1](/posts/calculus-1-overview/). The lectures are
theory-centred in the style of a course for mathematics majors, and exam
answers are graded on whether the logical development is correct.

## How these notes are organized

Each chapter is split over two posts, cut at a section boundary near the
middle. A post lists, section by section, the **definitions** and the
**theorems with their proofs**, and then the **problems** of the course
problem sheet for that section with solutions.

- Definitions, theorem statements and theorem numbers follow the lecture
  slides, which follow the textbook's numbering.
- A result labelled **Exercise a.b.c** is a textbook exercise that the
  lecture stated and used as a theorem. The number is the textbook's.
- A **Problem a.b.k** is the $$k$$-th question for §a.b on the problem
  sheet. The sheets for Chapters 1 and 2 do not number their questions.
  Those for Chapters 3 and 4 give the textbook's exercise number, which is
  shown in parentheses after the problem number.
- The notes do not reproduce everything on the slides. Definitions,
  theorems and the examples that a later argument relies on are kept;
  routine numerical examples and summary slides are left out.
- Proofs and solutions cite the earlier results they use by number, and each
  citation links to the statement.

## Chapter contents

Section titles are the textbook's. Chapters without a link have not been
written up yet.

**Chapter 1 — Vector Spaces**

[Part 1](/posts/linear-algebra-vector-spaces/)

- §1.1 Introduction (fields, from Appendix C)
- §1.2 Vector Spaces
- §1.3 Subspaces
- §1.4 Linear Combinations and Systems of Linear Equations
- §1.5 Linear Dependence and Linear Independence

[Part 2](/posts/linear-algebra-vector-spaces-2/)

- §1.6 Bases and Dimension
- §1.7 Maximal Linearly Independent Subsets
- Quotient Spaces (lectured from separate slides; placed at the end of
  Chapter 1)

**Chapter 2 — Linear Transformations and Matrices**

[Part 1](/posts/linear-algebra-linear-transformations/)

- §2.1 Linear Transformations, Null Spaces, and Ranges
- §2.2 The Matrix Representation of a Linear Transformation
- §2.3 Composition of Linear Transformations and Matrix Multiplication
- Direct sums, projections and invariant subspaces (lectured at the end of
  the chapter; placed in §2.1 to §2.3)

[Part 2](/posts/linear-algebra-linear-transformations-2/)

- §2.4 Invertibility and Isomorphisms
- §2.5 The Change of Coordinate Matrix
- §2.6 Dual Spaces

**Chapter 3 — Elementary Matrix Operations and Systems of Linear Equations**

[Part 1](/posts/linear-algebra-linear-systems/)

- §3.1 Elementary Matrix Operations and Elementary Matrices
- §3.2 The Rank of a Matrix and Matrix Inverses

[Part 2](/posts/linear-algebra-linear-systems-2/)

- §3.3 Systems of Linear Equations — Theoretical Aspects
- §3.4 Systems of Linear Equations — Computational Aspects

**Chapter 4 — Determinants**

[Part 1](/posts/linear-algebra-determinants/)

- §4.1 Determinants of Order 2
- §4.2 Determinants of Order $$n$$
- §4.3 Properties of Determinants
- §4.4 Summary — Important Facts about Determinants (no separate section;
  its facts are stated in §4.2 and §4.3)

[Part 2](/posts/linear-algebra-determinants-2/)

- §4.5 A Characterization of the Determinant
- Finite Fields (lectured from separate slides; placed at the end of
  Chapter 4)

**Chapter 5 — Diagonalization**

**Chapter 6 — Inner Product Spaces**

## Notation

Used in Chapters 1 to 4. The table will grow as later chapters are added.

| Symbol | Meaning |
|---|---|
| $$\mathbb{F}$$ | a field; its elements are scalars |
| $$\mathbb{Z}_p$$, $$\mathbb{F}_p$$ | the integers modulo $$p$$; a field when $$p$$ is prime |
| $$V$$, $$W$$ | vector spaces over $$\mathbb{F}$$ |
| $$x, y, v, \dots$$ | vectors (the lecture writes $$\vec{x}$$) |
| $$\mathbf{0}$$ | the zero vector |
| $$W \le V$$ | $$W$$ is a subspace of $$V$$ |
| $$\mathbb{F}^n$$ | columns of $$n$$ entries from $$\mathbb{F}$$ |
| $$\mathrm{Mat}_{m \times n}(\mathbb{F})$$ | $$m \times n$$ matrices with entries from $$\mathbb{F}$$ |
| $$\mathcal{F}(S, \mathbb{F})$$ | functions from a set $$S$$ to $$\mathbb{F}$$ |
| $$P(\mathbb{F})$$, $$P_n(\mathbb{F})$$ | polynomials over $$\mathbb{F}$$; those of degree at most $$n$$ |
| $$S_1 + S_2$$ | the sum $$\{x_1 + x_2 : x_1 \in S_1,\ x_2 \in S_2\}$$ |
| $$W_1 \oplus W_2$$ | direct sum: $$W_1 + W_2$$ with $$W_1 \cap W_2 = \{\mathbf{0}\}$$ |
| $$\operatorname{span}(S)$$ | the set of linear combinations of vectors of $$S$$ |
| $$\lvert S \rvert$$ | the number of elements of $$S$$ |
| $$\dim(V)$$ | the dimension of $$V$$ |
| $$e_j$$, $$E^{ij}$$ | standard basis vectors of $$\mathbb{F}^n$$ and of $$\mathrm{Mat}_{m \times n}(\mathbb{F})$$ |
| $$[v]_\beta$$ | the coordinate vector of $$v$$ relative to a basis $$\beta$$ |
| $$v + W$$ | the coset of $$W$$ containing $$v$$ |
| $$V/W$$ | the quotient space of $$V$$ modulo $$W$$ |
| $$\ker T$$, $$\operatorname{im} T$$ | kernel and image of a linear map $$T$$ (also written $$N(T)$$, $$R(T)$$) |
| $$\mathrm{id}_V$$, $$T_0$$ | the identity map of $$V$$; the zero map |
| $$\operatorname{rank}(T)$$, $$\operatorname{nullity}(T)$$ | $$\dim \operatorname{im} T$$ and $$\dim \ker T$$ |
| $$T_W$$ | the restriction of $$T$$ to a $$T$$-invariant subspace $$W$$ |
| $$\mathcal{L}(V, W)$$, $$\mathcal{L}(V)$$ | the linear maps $$V \to W$$; the linear operators on $$V$$ |
| $$\varepsilon_n$$ | the standard ordered basis of $$\mathbb{F}^n$$ |
| $$[T]_\beta^\gamma$$, $$[T]_\beta$$ | the matrix of $$T$$ in the ordered bases $$\beta$$, $$\gamma$$; the case $$\beta = \gamma$$ |
| $$L_A$$ | left multiplication by the matrix $$A$$ |
| $$A^t$$, $$I_n$$, $$\delta_{ij}$$ | transpose, identity matrix, Kronecker delta |
| $$V \approx W$$ | $$V$$ is isomorphic to $$W$$ |
| $$\phi_\beta$$ | the standard representation $$v \mapsto [v]_\beta$$ |
| $$A \sim B$$ | $$A$$ and $$B$$ are similar matrices |
| $$V^*$$, $$V^{**}$$ | the dual space $$\mathcal{L}(V, \mathbb{F})$$; the double dual |
| $$\beta^* = \{v_1^*, \dots, v_n^*\}$$ | the dual basis of $$\beta$$ |
| $$T^t$$ | the transpose $$f \mapsto fT$$ of a linear map $$T$$ |
| $$\hat{x}$$ | evaluation at $$x$$, an element of $$V^{**}$$ |
| $$R_i \leftrightarrow R_j$$, $$R_i \mathrel{\times}= c$$, $$R_i \mathrel{+}= c\,R_j$$ | elementary row operations of types 1, 2, 3; $$C_i$$ for columns |
| $$\operatorname{rank}(A)$$ | the rank of the matrix $$A$$, that is, of $$L_A$$ |
| $$(A \mid B)$$, $$(A \mid b)$$ | augmented matrices |
| $$K$$, $$K_H$$ | the solution set of $$Ax = b$$; that of $$Ax = \mathbf{0}$$ |
| $$\det A$$, $$\lvert A \rvert$$ | the determinant of $$A$$ |
| $$\tilde{A}_{ij}$$ | $$A$$ with row $$i$$ and column $$j$$ deleted |
| $$\operatorname{adj}(A)$$ | the classical adjoint of $$A$$ |
| $$\mathcal{O}\binom{u}{v}$$ | the orientation of an ordered basis $$\{u, v\}$$ of $$\mathbb{R}^2$$ |
| $$S_n$$, $$\operatorname{sgn}(\sigma)$$ | the permutations of $$\{1, \dots, n\}$$; the sign of a permutation |
| $$\operatorname{char} \mathbb{F}$$ | the characteristic of the field $$\mathbb{F}$$ |
| $$\mathbb{F}[x]$$ | the ring of polynomials with coefficients in $$\mathbb{F}$$ |
| $$\langle p \rangle$$, $$a + \langle p \rangle$$ | the multiples of $$p$$; a coset of them |
| $$\square$$ | end of a proof or solution |
