---
title: "Linear Algebra: Course Overview"
date: 2026-10-11 00:10:00 +0900
categories: [Course Notes, Linear Algebra]
tags: [overview, linear algebra, vector spaces, linear transformations]
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

Each chapter is one post. A post lists, section by section, the
**definitions** and the **theorems with their proofs**, and then the
**problems** of the course problem sheet for that section with solutions.

- Definitions, theorem statements and theorem numbers follow the lecture
  slides, which follow the textbook's numbering.
- A result labelled **Exercise a.b.c** is a textbook exercise that the
  lecture stated and used as a theorem. The number is the textbook's.
- A **Problem a.b.k** is the $$k$$-th question for §a.b on the problem
  sheet. The sheet does not number its questions.
- Proofs and solutions cite the earlier results they use by number, and each
  citation links to the statement.

## Chapter contents

Section titles are the textbook's. Chapters without a link have not been
written up yet.

**[Chapter 1 — Vector Spaces](/posts/linear-algebra-vector-spaces/)**

- §1.1 Introduction (fields, from Appendix C)
- §1.2 Vector Spaces
- §1.3 Subspaces
- §1.4 Linear Combinations and Systems of Linear Equations
- §1.5 Linear Dependence and Linear Independence
- §1.6 Bases and Dimension
- §1.7 Maximal Linearly Independent Subsets
- Quotient Spaces (lectured from separate slides; placed at the end of
  Chapter 1)

**[Chapter 2 — Linear Transformations and Matrices](/posts/linear-algebra-linear-transformations/)**

- §2.1 Linear Transformations, Null Spaces, and Ranges
- §2.2 The Matrix Representation of a Linear Transformation
- §2.3 Composition of Linear Transformations and Matrix Multiplication
- §2.4 Invertibility and Isomorphisms
- §2.5 The Change of Coordinate Matrix
- §2.6 Dual Spaces
- Direct sums, projections and invariant subspaces (lectured at the end of
  the chapter; placed in §2.1 to §2.3)

**Chapter 3 — Elementary Matrix Operations and Systems of Linear Equations**

**Chapter 4 — Determinants**

**Chapter 5 — Diagonalization**

**Chapter 6 — Inner Product Spaces**

## Notation

Used in Chapters 1 and 2. The table will grow as later chapters are added.

| Symbol | Meaning |
|---|---|
| $$\mathbb{F}$$ | a field; its elements are scalars |
| $$\mathbb{Z}_p$$ | the integers modulo $$p$$ |
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
| $$\square$$ | end of a proof or solution |
