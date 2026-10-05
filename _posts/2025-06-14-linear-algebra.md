---
title: "MATH 221: Linear Algebra"
date: 2025-06-14 18:00:00 +0900
categories: [Mathematics, Linear Algebra]
tags: [linear-algebra, proofs, eigenvalues]
description: Course summary for MATH 221 — vector spaces, linear maps, eigenvalues, and the spectral theorem.
math: true
---

> This is an example post showing the structure I use for course summaries.
> Copy `_drafts/course-summary-template.md`{: .filepath } to start a new one.
{: .prompt-tip }

## At a glance

| | |
| --- | --- |
| **Course** | MATH 221 — Linear Algebra |
| **Term** | 2025 Spring |
| **Credits** | 3 |
| **Textbook** | Axler, *Linear Algebra Done Right*, 4th ed. |

## What the course covered

The course built linear algebra up from vector spaces rather than from matrices,
treating matrices as the coordinate representation of a linear map once a basis
is fixed. Roughly four blocks:

1. **Vector spaces and subspaces** — spanning sets, linear independence, bases,
   dimension, and direct sums.
2. **Linear maps** — the null space and range, the rank-nullity theorem, and the
   correspondence between linear maps and matrices.
3. **Eigenvalues and diagonalization** — invariant subspaces, characteristic and
   minimal polynomials, and conditions for diagonalizability.
4. **Inner product spaces** — orthonormal bases, Gram-Schmidt, adjoints, and the
   spectral theorem for self-adjoint operators.

## Key ideas worth remembering

### Rank-nullity

For a linear map $T : V \to W$ with $V$ finite-dimensional,

$$\dim V = \dim \operatorname{null} T + \dim \operatorname{range} T.$$

Most of the dimension-counting arguments in the course reduced to this one
identity.

### Diagonalizability

An operator on a finite-dimensional complex vector space is diagonalizable
exactly when its minimal polynomial factors into distinct linear factors.
Having $\dim V$ distinct eigenvalues is sufficient but not necessary — the
identity map is the standard counterexample.

### The spectral theorem

Every self-adjoint operator on a finite-dimensional real inner product space has
an orthonormal basis of eigenvectors, and all its eigenvalues are real. This is
what makes symmetric matrices so much better behaved than general ones.

## What I found hard

Quotient spaces took the longest to click. The construction felt formal until I
started reading $V / U$ as "$V$ with everything in $U$ collapsed to zero," which
makes the first isomorphism theorem read almost tautologically.

## Resources I actually used

- Axler, *Linear Algebra Done Right* — the primary text, and worth reading in order.
- 3Blue1Brown's *Essence of Linear Algebra* — good for geometric intuition before
  the formal treatment.

## Takeaway

Starting from vector spaces instead of matrices made the later material much
easier; by the time determinants appeared they were a consequence rather than a
definition.
