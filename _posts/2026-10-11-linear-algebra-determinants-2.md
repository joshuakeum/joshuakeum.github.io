---
title: "Linear Algebra: Determinants (Part 2)"
date: 2026-10-11 02:10:00 +0900
categories: [Course Notes, Linear Algebra]
tags: [determinant, alternating multilinear forms, permutations, finite fields, characteristic]
description: Definitions, theorems with proofs, and solved problems for Chapter 4 of Linear Algebra, §4.5 — the determinant as the unique alternating n-linear function and the permutation formula — followed by the lecture on fields, characteristic, and finite fields.
math: true
mermaid: false
render_with_liquid: false
---

> **How to read the labels.** This post continues
> [Chapter 4, Part 1](/posts/linear-algebra-determinants/), which covers
> §4.1 to §4.3. It covers §4.5 and then the lecture on finite fields, which
> was given from a separate set of slides and is placed here because it
> explains a remark of §4.5. Definitions, theorems and their numbers follow
> the lecture slides, which follow the textbook (Friedberg, Insel and
> Spence, 5th edition); Theorems C.1 and C.2 are from its Appendix C. A
> **Problem a.b.k** is the $$k$$-th question for §a.b on the course problem
> sheet, with the textbook's exercise number in parentheses. Earlier results
> are cited by number and link to the post that states them.
{: .prompt-info }

Throughout, $$\mathbb{F}$$ is a field. As in Part 1, a square matrix is
often described by its rows, $$e_1, \dots, e_n$$ are the standard vectors
written as rows, and vertical dots in a matrix stand for rows that are the
same on both sides of an equation.

---

## §4.5 A Characterization of the Determinant

> **Definition ($$n$$-linear function).** A function
> $$\delta \colon \mathrm{Mat}_{n \times n}(\mathbb{F}) \to \mathbb{F}$$
> is **$$n$$-linear** if it is a linear function of each row when the
> remaining $$n - 1$$ rows are held fixed: for every $$r$$,
>
> $$
> \delta \begin{pmatrix} a_1 \\ \vdots \\ a_{r-1} \\ u + tv \\ a_{r+1} \\ \vdots \\ a_n \end{pmatrix}
> = \delta \begin{pmatrix} a_1 \\ \vdots \\ a_{r-1} \\ u \\ a_{r+1} \\ \vdots \\ a_n \end{pmatrix}
> + t\,\delta \begin{pmatrix} a_1 \\ \vdots \\ a_{r-1} \\ v \\ a_{r+1} \\ \vdots \\ a_n \end{pmatrix} .
> $$
{: .definition #def-n-linear }

**Examples.**

- $$\det$$ is $$n$$-linear ([Theorem 4.3][thm-4-3]).
- For a fixed $$j$$, the product of the entries of the $$j$$-th column,
  $$\delta(A) = A_{1j} A_{2j} \cdots A_{nj}$$, is $$n$$-linear: it
  contains exactly one entry from each row.
- The product of the diagonal entries,
  $$\delta(A) = A_{11} A_{22} \cdots A_{nn}$$, is $$n$$-linear for the
  same reason.

> **Definition (Alternating).** An $$n$$-linear function
> $$\delta \colon \mathrm{Mat}_{n \times n}(\mathbb{F}) \to \mathbb{F}$$
> is **alternating** if $$\delta(A) = 0$$ whenever two adjacent rows of
> $$A$$ are identical:
>
> $$\delta \begin{pmatrix} \vdots \\ u \\ u \\ \vdots \end{pmatrix} = 0 .$$
{: .definition #def-alternating }

$$\det$$ is alternating ([Corollary to Theorem 4.4][cor-4-4]). The two
product examples above are not, for $$n \ge 2$$: both take the value
$$1$$ on the matrix whose entries are all $$1$$.

> **Theorem 4.10.** Let
> $$\delta \colon \mathrm{Mat}_{n \times n}(\mathbb{F}) \to \mathbb{F}$$
> be an alternating $$n$$-linear function.
>
> - **(a)** If $$B$$ is obtained from $$A$$ by interchanging any two
>   rows, then $$\delta(B) = -\delta(A)$$.
> - **(b)** If $$A$$ has two identical rows, adjacent or not, then
>   $$\delta(A) = 0$$.
{: .theorem #thm-4-10 }

*Proof.* (a) First let the two rows be adjacent. Putting $$u + v$$ in
both and expanding by linearity in each,

$$
0 = \delta \begin{pmatrix} \vdots \\ u + v \\ u + v \\ \vdots \end{pmatrix}
= \delta \begin{pmatrix} \vdots \\ u \\ u \\ \vdots \end{pmatrix}
+ \delta \begin{pmatrix} \vdots \\ u \\ v \\ \vdots \end{pmatrix}
+ \delta \begin{pmatrix} \vdots \\ v \\ u \\ \vdots \end{pmatrix}
+ \delta \begin{pmatrix} \vdots \\ v \\ v \\ \vdots \end{pmatrix}
= \delta \begin{pmatrix} \vdots \\ u \\ v \\ \vdots \end{pmatrix}
+ \delta \begin{pmatrix} \vdots \\ v \\ u \\ \vdots \end{pmatrix} .
$$

So interchanging two adjacent rows changes the sign. Now let the rows be
$$r < s$$. Move row $$s$$ up to position $$r$$ by $$s - r$$ interchanges
of adjacent rows; the old row $$r$$ is then in position $$r + 1$$, and
$$s - r - 1$$ further interchanges of adjacent rows move it down to
position $$s$$. The total number of sign changes is
$$2(s - r) - 1$$, which is odd.

(b) Let rows $$r < s$$ of $$A$$ be identical. If $$s = r + 1$$,
$$\delta(A) = 0$$ by definition. Otherwise interchange rows $$r + 1$$
and $$s$$ to get a matrix $$B$$ with identical adjacent rows $$r$$ and
$$r + 1$$. Then $$\delta(B) = 0$$, and
$$\delta(A) = -\delta(B) = 0$$ by (a). $$\square$$

A function with property (a) is called **skew-symmetric**. The theorem
says that alternating implies skew-symmetric. Note how (b) was obtained:
from the alternating property, with (a) used only to move rows. It is
*not* deduced from (a) alone, and it cannot be in general. The
[section on finite fields](#skew-not-alternating) below explains when
skew-symmetric fails to imply alternating.

> **Corollary 1 to Theorem 4.10.** Let $$\delta$$ be an alternating
> $$n$$-linear function. If $$B$$ is obtained from $$A$$ by adding a
> multiple of one row to another row, then $$\delta(B) = \delta(A)$$.
{: .theorem #cor-4-10-1 }

*Proof.* By linearity in the row that is changed,

$$
\delta \begin{pmatrix} \vdots \\ u \\ \vdots \\ v + tu \\ \vdots \end{pmatrix}
= \delta \begin{pmatrix} \vdots \\ u \\ \vdots \\ v \\ \vdots \end{pmatrix}
+ t\,\delta \begin{pmatrix} \vdots \\ u \\ \vdots \\ u \\ \vdots \end{pmatrix} ,
$$

and the last term is zero by [Theorem 4.10](#thm-4-10)(b). $$\square$$

> **Corollary 2 to Theorem 4.10.** Let $$\delta$$ be an alternating
> $$n$$-linear function. If
> $$A \in \mathrm{Mat}_{n \times n}(\mathbb{F})$$ has rank less than
> $$n$$, then $$\delta(A) = 0$$.
{: .theorem #cor-4-10-2 }

*Proof.* As in the [Corollary to Theorem 4.6][cor-4-6]: some row of
$$A$$ is a linear combination of the others, and adding multiples of the
other rows to it produces a zero row without changing $$\delta$$
([Corollary 1](#cor-4-10-1)). An $$n$$-linear function vanishes on a
matrix with a zero row, since $$\delta$$ is linear in that row.
$$\square$$

> **Corollary 3 to Theorem 4.10.** Let $$\delta$$ be an alternating
> $$n$$-linear function. For every elementary matrix $$E$$ and every
> $$A \in \mathrm{Mat}_{n \times n}(\mathbb{F})$$,
>
> $$\delta(EA) = \det E \cdot \delta(A) .$$
>
> In particular $$\delta(E) = \det E \cdot \delta(I_n)$$: the value is
> $$-\delta(I_n)$$, $$c\,\delta(I_n)$$ or $$\delta(I_n)$$ for $$E$$ of
> type 1, type 2 with scalar $$c$$, or type 3.
{: .theorem #cor-4-10-3 }

*Proof.* $$EA$$ is obtained from $$A$$ by the row operation that
produces $$E$$ from $$I_n$$ ([Theorem 3.1][thm-3-1]). For type 1,
$$\delta(EA) = -\delta(A)$$ by [Theorem 4.10](#thm-4-10)(a). For type 2,
$$\delta(EA) = c\,\delta(A)$$ by linearity in the row multiplied by
$$c$$. For type 3, $$\delta(EA) = \delta(A)$$ by
[Corollary 1](#cor-4-10-1). These factors $$-1$$, $$c$$ and $$1$$ are
$$\det E$$ ([determinants of elementary matrices][det-elementary]).
$$\square$$

> **Theorem 4.11.** Let
> $$\delta \colon \mathrm{Mat}_{n \times n}(\mathbb{F}) \to \mathbb{F}$$
> be an alternating $$n$$-linear function. For any
> $$A, B \in \mathrm{Mat}_{n \times n}(\mathbb{F})$$,
>
> $$\delta(AB) = \det A \cdot \delta(B) .$$
{: .theorem #thm-4-11 }

*Proof.* If $$\operatorname{rank}(A) < n$$, then
$$\operatorname{rank}(AB) < n$$ ([Theorem 3.7][thm-3-7]), so
$$\delta(AB) = 0$$ ([Corollary 2](#cor-4-10-2)), and
$$\det A = 0$$ ([Corollary to Theorem 4.6][cor-4-6]).

If $$\operatorname{rank}(A) = n$$, write $$A = E_1 E_2 \cdots E_k$$ with
elementary matrices
([Corollary 3 to Theorem 3.6][cor-3-6-3]). By
[Corollary 3](#cor-4-10-3), one factor at a time, and then
[Theorem 4.7][thm-4-7],

$$
\begin{aligned}
\delta(AB) = \delta(E_1 E_2 \cdots E_k B)
&= \det E_1 \cdot \det E_2 \cdots \det E_k \cdot \delta(B) \\
&= \det(E_1 E_2 \cdots E_k) \cdot \delta(B) = \det A \cdot \delta(B) .
\qquad \square
\end{aligned}
$$

The problem sheet states this theorem with the extra hypothesis
$$\delta(I_n) = 1$$. The slides strike that hypothesis out, noting that
editions of the textbook differ here, and the proof above does not use it.

> **Theorem 4.12.** If
> $$\delta \colon \mathrm{Mat}_{n \times n}(\mathbb{F}) \to \mathbb{F}$$
> is an alternating $$n$$-linear function with $$\delta(I_n) = 1$$, then
>
> $$\delta(A) = \det A \qquad
> \text{for every } A \in \mathrm{Mat}_{n \times n}(\mathbb{F}) .$$
{: .theorem #thm-4-12 }

*Proof.* By [Theorem 4.11](#thm-4-11),
$$\delta(A) = \delta(A I_n) = \det A \cdot \delta(I_n) = \det A$$.
$$\square$$

So the determinant is the *only* alternating $$n$$-linear function that
takes the value $$1$$ on $$I_n$$. This can be used as a definition of the
determinant, and it turns any formula with these three properties into a
formula for the determinant. The permutation formula of first-year
calculus is one.

### The permutation formula

Let $$S_n$$ be the set of permutations of $$\{1, 2, \dots, n\}$$, that
is, of bijections
$$\sigma \colon \{1, \dots, n\} \to \{1, \dots, n\}$$. Every permutation
is a composition of transpositions, and the parity of the number of
transpositions depends only on $$\sigma$$; the sign
$$\operatorname{sgn}(\sigma) \in \{\pm 1\}$$ is $$1$$ if that number is
even and $$-1$$ if it is odd. Consequently
$$\operatorname{sgn}(\tau\sigma) = -\operatorname{sgn}(\sigma)$$ for a
transposition $$\tau$$. These facts are in the
[Calculus 1 notes on determinants](/posts/calculus-1-determinants/),
where the formula below is the definition of the determinant.

> **Theorem (Leibniz formula).** For
> $$A \in \mathrm{Mat}_{n \times n}(\mathbb{F})$$,
>
> $$\det A = \sum_{\sigma \in S_n} \operatorname{sgn}(\sigma)\,
> A_{\sigma(1)1} A_{\sigma(2)2} \cdots A_{\sigma(n)n} .$$
{: .theorem #leibniz-formula }

*Proof.* Let $$\delta(A)$$ be the right side. By
[Theorem 4.12](#thm-4-12) it is enough to check three properties.

*$$\delta$$ is $$n$$-linear.* Since $$\sigma$$ is a bijection, the
product $$A_{\sigma(1)1} \cdots A_{\sigma(n)n}$$ contains exactly one
entry from each row. As a function of one row, with the others fixed, it
is a constant times one entry of that row, which is linear. A sum of
linear functions is linear.

*$$\delta(A) = 0$$ if two rows of $$A$$ are identical.* Let rows
$$r \ne s$$ be identical and let $$\tau$$ be the transposition that
exchanges $$r$$ and $$s$$. The permutations fall into pairs
$$\{\sigma, \tau\sigma\}$$ with
$$\operatorname{sgn}(\tau\sigma) = -\operatorname{sgn}(\sigma)$$. The
products for $$\sigma$$ and $$\tau\sigma$$ are equal: the row index
$$\tau\sigma(j)$$ differs from $$\sigma(j)$$ only when it is $$r$$ or
$$s$$, and rows $$r$$ and $$s$$ of $$A$$ are the same. So the two terms
of each pair cancel, and the sum is zero.

*$$\delta(I_n) = 1$$.* The product for $$\sigma$$ is nonzero only if
$$\sigma(j) = j$$ for every $$j$$, and the identity has sign $$1$$.
$$\square$$

The second step pairs the terms off instead of arguing "interchanging the
two equal rows gives $$\delta(A) = -\delta(A)$$, hence
$$\delta(A) = 0$$". That shorter argument is the step from
skew-symmetric to alternating, and it is not valid in a field where
$$1 + 1 = 0$$.

### Problems for §4.5

> **Problem 4.5.1 (Exercise 4.5.16).** Prove that if
> $$\delta \colon M_{n \times n}(F) \to F$$ is an alternating $$n$$-linear
> function, then there exists a scalar $$k$$ such that
> $$\delta(A) = k \det(A)$$ for all $$A \in M_{n \times n}(F)$$.
{: .problem #prob-4-5-1 }

*Solution.* Let $$k = \delta(I_n)$$. By [Theorem 4.11](#thm-4-11) with
$$B = I_n$$,

$$
\delta(A) = \delta(A I_n) = \det A \cdot \delta(I_n) = k \det(A) .
\qquad \square
$$

> **Problem 4.5.2 (Exercise 4.5.19).** Let
> $$\delta \colon M_{n \times n}(F) \to F$$ be an $$n$$-linear function
> and $$F$$ a field that does not have characteristic two. Prove that if
> $$\delta(B) = -\delta(A)$$ whenever $$B$$ is obtained from
> $$A \in M_{n \times n}(F)$$ by interchanging any two rows of $$A$$,
> then $$\delta(M) = 0$$ whenever $$M \in M_{n \times n}(F)$$ has two
> identical rows.
{: .problem #prob-4-5-2 }

*Solution.* Let rows $$r \ne s$$ of $$M$$ be identical. Interchanging
rows $$r$$ and $$s$$ gives $$M$$ again, so the hypothesis with
$$A = B = M$$ says $$\delta(M) = -\delta(M)$$, that is,

$$
(1 + 1)\,\delta(M) = 0 .
$$

Since $$F$$ does not have characteristic two, $$1 + 1 \ne 0$$ in $$F$$,
and multiplying by $$(1 + 1)^{-1}$$ gives $$\delta(M) = 0$$.
$$\square$$

In the terms used above: when the characteristic is not two, a
skew-symmetric $$n$$-linear function is alternating.

> **Problem 4.5.3 (Exercise 4.5.15).** Prove that
> $$\delta \colon M_{2 \times 2}(F) \to F$$ is a 2-linear function if and
> only if it has the form
>
> $$\delta(A) = A_{11} A_{22}\, a + A_{11} A_{21}\, b
> + A_{12} A_{22}\, c + A_{12} A_{21}\, d$$
>
> for some scalars $$a, b, c, d \in F$$.
{: .problem #prob-4-5-3 }

*Solution.* ($$\Leftarrow$$) Each of the four functions
$$A \mapsto A_{1p} A_{2q}$$ is 2-linear: with the second row fixed it is
a constant times one entry of the first row, and with the first row
fixed it is a constant times one entry of the second row. Sums and
scalar multiples of linear functions are linear
([Theorem 2.7][thm-2-7]), so every $$\delta$$ of the displayed form is
linear in each row.

($$\Rightarrow$$) Let $$\delta$$ be 2-linear. The rows of $$A$$ are
$$A_{11} e_1 + A_{12} e_2$$ and $$A_{21} e_1 + A_{22} e_2$$. Expanding by
linearity in the first row and then in the second,

$$
\delta(A)
= A_{11} A_{21}\,\delta \begin{pmatrix} e_1 \\ e_1 \end{pmatrix}
+ A_{11} A_{22}\,\delta \begin{pmatrix} e_1 \\ e_2 \end{pmatrix}
+ A_{12} A_{21}\,\delta \begin{pmatrix} e_2 \\ e_1 \end{pmatrix}
+ A_{12} A_{22}\,\delta \begin{pmatrix} e_2 \\ e_2 \end{pmatrix} .
$$

This is the required form, with

$$
a = \delta \begin{pmatrix} e_1 \\ e_2 \end{pmatrix} , \quad
b = \delta \begin{pmatrix} e_1 \\ e_1 \end{pmatrix} , \quad
c = \delta \begin{pmatrix} e_2 \\ e_2 \end{pmatrix} , \quad
d = \delta \begin{pmatrix} e_2 \\ e_1 \end{pmatrix} .
\qquad \square
$$

For example, $$\det$$ has $$a = 1$$, $$d = -1$$ and $$b = c = 0$$.

---

## Finite Fields

Every result so far holds over an arbitrary field, and the one place
where the field made a difference was the gap between skew-symmetric and
alternating. This section collects what the lecture said about fields in
general and then constructs the finite ones. The
[definition of a field][def-field] and of its
[characteristic][def-characteristic] are in §1.1; the slides list the
field axioms one property at a time, as (F1) to (F9), and the properties
are referred to here by name.

### Arithmetic in a field

> **Definition (Commutative ring).** A set with an addition and a
> multiplication that satisfy all the conditions in the definition of a
> field, except possibly the existence of multiplicative inverses, is a
> **commutative ring** (with unity).
{: .definition #def-commutative-ring }

**Examples.**

- $$\mathbb{Q}$$, $$\mathbb{R}$$ and $$\mathbb{C}$$ are fields.
- $$\mathbb{Q}(\sqrt2) = \{\, x + y\sqrt2 : x, y \in \mathbb{Q} \,\}$$,
  with the addition and multiplication of $$\mathbb{R}$$, is a field.
  The inverse of $$x + y\sqrt2 \ne 0$$ is

  $$
  \frac{x}{x^2 - 2y^2} - \frac{y}{x^2 - 2y^2}\sqrt2 ,
  $$

  where $$x^2 - 2y^2 \ne 0$$ because $$\sqrt2$$ is irrational.
- $$\mathbb{Z}$$ is a commutative ring and not a field. The polynomials
  with coefficients in a field form a commutative ring.
  $$\mathrm{Mat}_{n \times n}(\mathbb{F})$$ satisfies the conditions
  except that its multiplication is not commutative for $$n \ge 2$$.

> **Theorem C.1 (Cancellation Laws).** Let $$a, b, c$$ be elements of a
> field.
>
> - **(a)** If $$a + b = a + c$$, then $$b = c$$.
> - **(b)** If $$ab = ac$$ and $$a \ne 0$$, then $$b = c$$.
{: .theorem #thm-c-1 }

*Proof.* (a) Add $$-a$$ to both sides:
$$b = (-a) + (a + b) = (-a) + (a + c) = c$$. (b) Multiply both sides by
$$a^{-1}$$: $$b = a^{-1}(ab) = a^{-1}(ac) = c$$. $$\square$$

> **Theorem (Uniqueness of the identities).** The additive identity of a
> field is unique, and so is the multiplicative identity.
{: .theorem #thm-field-identities }

*Proof.* If $$0$$ and $$0'$$ are both additive identities, then
$$0' = 0' + 0 = 0$$: the first equality because $$0$$ is an identity, the
second because $$0'$$ is. In the same way $$1' = 1' \cdot 1 = 1$$.
$$\square$$

> **Corollary (Uniqueness of inverses).** Each element of a field has a
> unique additive inverse, and each nonzero element has a unique
> multiplicative inverse.
{: .theorem #cor-field-inverses }

*Proof.* If $$a + b = 0 = a + b'$$, then $$b = b'$$ by
[Theorem C.1](#thm-c-1)(a). If $$ab = 1 = ab'$$ with $$a \ne 0$$, then
$$b = b'$$ by (b). $$\square$$

> **Theorem C.2.** Let $$\mathbb{F}$$ be a field and
> $$a, b \in \mathbb{F}$$.
>
> - **(a)** $$a \cdot 0 = 0$$.
> - **(b)** $$(-a)b = a(-b) = -(ab)$$.
> - **(c)** $$(-a)(-b) = ab$$.
{: .theorem #thm-c-2 }

*Proof.* (a)
$$a \cdot 0 + a \cdot 0 = a(0 + 0) = a \cdot 0 = a \cdot 0 + 0$$, and
cancelling $$a \cdot 0$$ gives $$a \cdot 0 = 0$$.

(b) $$ab + (-a)b = (a + (-a))b = 0 \cdot b = 0$$, so $$(-a)b$$ is the
additive inverse of $$ab$$. The same argument gives $$a(-b) = -(ab)$$.

(c) By (b) twice, $$(-a)(-b) = -(a(-b)) = -(-(ab)) = ab$$. $$\square$$

> **Corollary to Theorem C.2 (No zero divisors).** In a field, if
> $$ab = 0$$, then $$a = 0$$ or $$b = 0$$. Also, $$0$$ has no
> multiplicative inverse.
{: .theorem #cor-c-2 }

*Proof.* If $$ab = 0$$ and $$a \ne 0$$, then
$$b = a^{-1}ab = a^{-1} \cdot 0 = 0$$ by
[Theorem C.2](#thm-c-2)(a). If $$0$$ had an inverse, then
$$1 = 0^{-1} \cdot 0 = 0$$, but $$0 \ne 1$$ in a field. $$\square$$

The condition $$0 \ne 1$$ cannot be dropped from the definition. If
$$0 = 1$$, then $$a = a \cdot 1 = a \cdot 0 = 0$$ for every $$a$$, and
the "field" has a single element.

### Characteristic

For a positive integer $$n$$ and $$a \in \mathbb{F}$$, write
$$n \cdot a = a + a + \cdots + a$$ with $$n$$ terms. By distributivity,
$$n \cdot a = (n \cdot 1)\,a$$ and
$$(m \cdot 1)(n \cdot 1) = (mn) \cdot 1$$. The
[characteristic][def-characteristic] of $$\mathbb{F}$$ is the smallest
positive $$p$$ with $$p \cdot 1 = 0$$, or zero if there is none.

> **Theorem (The characteristic is zero or a prime).** Let
> $$\operatorname{char} \mathbb{F} = p$$. Then $$p$$ is zero or a prime
> number. If $$p > 0$$, then $$p \cdot a = 0$$ for every
> $$a \in \mathbb{F}$$; in particular, if $$p = 2$$, then $$a = -a$$ for
> every $$a \in \mathbb{F}$$.
{: .theorem #thm-characteristic-prime }

*Proof.* Let $$p > 0$$. Then $$p \ne 1$$ because $$1 \ne 0$$. If
$$p = kl$$ with $$1 < k, l < p$$, then
$$(k \cdot 1)(l \cdot 1) = p \cdot 1 = 0$$, so $$k \cdot 1 = 0$$ or
$$l \cdot 1 = 0$$ ([no zero divisors](#cor-c-2)), contradicting the
minimality of $$p$$. So $$p$$ is prime. Next,
$$p \cdot a = (p \cdot 1)\,a = 0 \cdot a = 0$$. For $$p = 2$$ this reads
$$a + a = 0$$, that is, $$a = -a$$. $$\square$$

**Example.** $$\operatorname{char} \mathbb{F}_p = p$$ for the field
$$\mathbb{F}_p$$ of integers modulo a prime $$p$$, constructed below.

> **Skew-symmetric does not imply alternating in characteristic two.**
> Let $$\delta \colon \mathrm{Mat}_{n \times n}(\mathbb{F}) \to \mathbb{F}$$
> be $$n$$-linear.
>
> - **(a)** If $$\delta$$ is alternating, then $$\delta$$ is
>   skew-symmetric.
> - **(b)** If $$\delta$$ is skew-symmetric and
>   $$\operatorname{char} \mathbb{F} \ne 2$$, then $$\delta$$ is
>   alternating.
> - **(c)** Over $$\mathbb{F}_2$$, the function
>   $$\delta \colon \mathrm{Mat}_{2 \times 2}(\mathbb{F}_2) \to \mathbb{F}_2$$
>   given by the dot product of the two rows,
>
>   $$\delta \begin{pmatrix} u \\ v \end{pmatrix} = u_1 v_1 + u_2 v_2 ,$$
>
>   is 2-linear and skew-symmetric but not alternating.
{: .theorem #skew-not-alternating }

*Proof.* (a) is [Theorem 4.10](#thm-4-10)(a), and (b) is
[Problem 4.5.2](#prob-4-5-2).

(c) The dot product is linear in $$u$$ and in $$v$$. It is symmetric,
$$\delta \begin{pmatrix} v \\ u \end{pmatrix}
= \delta \begin{pmatrix} u \\ v \end{pmatrix}$$, and in
$$\mathbb{F}_2$$ every element is its own negative
([characteristic two](#thm-characteristic-prime)), so

$$
\delta \begin{pmatrix} v \\ u \end{pmatrix}
= -\delta \begin{pmatrix} u \\ v \end{pmatrix} .
$$

Thus $$\delta$$ is skew-symmetric; in characteristic two, skew-symmetric
and symmetric mean the same thing. But
$$\delta \begin{pmatrix} e_1 \\ e_1 \end{pmatrix} = 1 \ne 0$$, so
$$\delta$$ is not alternating. $$\square$$

This is why §4.5 asks for an *alternating* function. The function in (c)
is skew-symmetric and 2-linear, yet it is not a scalar multiple of
$$\det$$, since $$\det$$ vanishes on the matrix with both rows equal to
$$e_1$$.

### The fields $$\mathbb{F}_p$$

Fix a prime $$p$$, and consider the following subsets of
$$\mathbb{Z}$$:

$$
\langle p \rangle = \{\text{multiples of } p\} , \qquad
a + \langle p \rangle = \{\, a + n : n \in \langle p \rangle \,\}
\quad (a \in \mathbb{Z}) .
$$

> **Lemma.** $$a + \langle p \rangle = a' + \langle p \rangle$$ if and
> only if $$a - a' \in \langle p \rangle$$.
{: .theorem #lem-cosets-integers }

*Proof.* If the two sets are equal, then
$$a = a + 0 \in a' + \langle p \rangle$$, so $$a = a' + n$$ with
$$n \in \langle p \rangle$$. Conversely, if $$a = a' + n_0$$ with
$$n_0 \in \langle p \rangle$$, then
$$a + n = a' + (n_0 + n) \in a' + \langle p \rangle$$ for every
$$n \in \langle p \rangle$$, so
$$a + \langle p \rangle \subseteq a' + \langle p \rangle$$; and
$$a' = a + (-n_0)$$ gives the other inclusion. $$\square$$

This is the argument for [cosets of a subspace][ex-1-3-31], with
$$\langle p \rangle$$ in the place of the subspace. As for
[quotient spaces][def-quotient-space], define

$$
(a + \langle p \rangle) + (b + \langle p \rangle) = (a + b) + \langle p \rangle ,
\qquad
(a + \langle p \rangle)(b + \langle p \rangle) = ab + \langle p \rangle
$$

on the set
$$\mathbb{Z}/\langle p \rangle = \{\, a + \langle p \rangle : a \in \mathbb{Z} \,\}$$.
The operations are well defined: if
$$a - a', b - b' \in \langle p \rangle$$, then
$$(a + b) - (a' + b') \in \langle p \rangle$$ and
$$ab - a'b' = a(b - b') + (a - a')b' \in \langle p \rangle$$. The
associative, commutative and distributive laws hold because they hold in
$$\mathbb{Z}$$, the zero is $$0 + \langle p \rangle$$ and the one is
$$1 + \langle p \rangle$$. So $$\mathbb{Z}/\langle p \rangle$$ is a
commutative ring.

> **Theorem.** For a prime $$p$$, the ring
> $$\mathbb{Z}/\langle p \rangle$$ is a field. With each coset renamed by
> its representative among $$0, 1, \dots, p - 1$$, it is
> $$\mathbb{F}_p = \{0, 1, \dots, p - 1\}$$ with addition and
> multiplication modulo $$p$$.
{: .theorem #thm-fp-field }

*Proof.* The one is not the zero, since
$$1 - 0 \notin \langle p \rangle$$. Let $$n + \langle p \rangle$$ be
nonzero, that is, $$p$$ does not divide $$n$$. Since $$p$$ is prime,
$$\gcd(p, n) = 1$$, and so there are integers $$a, b$$ with

$$
ap + bn = 1 ,
$$

which the extended Euclidean algorithm computes. Then

$$
(b + \langle p \rangle)(n + \langle p \rangle)
= bn + \langle p \rangle = (1 - ap) + \langle p \rangle
= 1 + \langle p \rangle ,
$$

so $$b + \langle p \rangle$$ is a multiplicative inverse.

Every integer $$a$$ has a unique remainder
$$r \in \{0, 1, \dots, p - 1\}$$ on division by $$p$$, and
$$a + \langle p \rangle = r + \langle p \rangle$$ by the
[Lemma](#lem-cosets-integers). So there are exactly $$p$$ cosets, and
the operations on them are addition and multiplication followed by
reduction modulo $$p$$. $$\square$$

$$\mathbb{F}_p$$ is the field written $$\mathbb{Z}_p$$ in §1.1. In
particular $$\mathbb{F}_2 = \{0, 1\}$$ with $$1 + 1 = 0$$.

**Example.** In $$\mathbb{F}_7$$, $$1 = 1 \cdot 7 + (-2) \cdot 3$$, so
$$3^{-1} = -2 = 5$$. Indeed $$3 \cdot 5 = 15 = 2 \cdot 7 + 1$$.

The primality of $$p$$ is needed. If $$n = kl$$ with $$1 < k, l < n$$,
then in $$\mathbb{Z}/\langle n \rangle$$ the product of the nonzero
elements $$k + \langle n \rangle$$ and $$l + \langle n \rangle$$ is zero,
which cannot happen in a field ([no zero divisors](#cor-c-2)).

### Fields from irreducible polynomials

The same construction works with polynomials in place of integers.
$$\mathbb{F}[x]$$ denotes the ring of polynomials with coefficients in
the field $$\mathbb{F}$$. It has division with remainder: for
$$f, g \in \mathbb{F}[x]$$ with $$g \ne 0$$ there are unique
$$q, r \in \mathbb{F}[x]$$ with $$f = qg + r$$ and either $$r = 0$$ or
$$\deg r < \deg g$$.

> **Lemma (Bézout's identity for polynomials).** Let
> $$f(x), g(x) \in \mathbb{F}[x]$$, not both zero. Then there exist
> $$a(x), b(x) \in \mathbb{F}[x]$$ such that
>
> $$h(x) = a(x) f(x) + b(x) g(x)$$
>
> divides both $$f(x)$$ and $$g(x)$$. Every common divisor of $$f(x)$$
> and $$g(x)$$ divides $$h(x)$$, so $$h(x)$$ is a greatest common divisor:
>
> $$a(x) f(x) + b(x) g(x) = \gcd\big(f(x), g(x)\big) .$$
{: .theorem #lem-bezout }

*Proof.* Consider the set

$$
I = \{\, a(x) f(x) + b(x) g(x) : a(x), b(x) \in \mathbb{F}[x] \,\} .
$$

It has two properties: (i) if $$c, d \in I$$, then $$c + d \in I$$; and
(ii) if $$c \in I$$ and $$d \in \mathbb{F}[x]$$, then $$dc \in I$$. Let
$$h \in I$$ be a nonzero polynomial of the smallest degree. For any
$$c \in I$$, divide: $$c = qh + r$$ with $$r = 0$$ or
$$\deg r < \deg h$$. By (i) and (ii), $$r = c + (-q)h \in I$$, so
$$r = 0$$ by the choice of $$h$$. Hence every element of $$I$$ is a
multiple of $$h$$. Since $$f, g \in I$$, $$h$$ divides both.

If $$d$$ divides both $$f$$ and $$g$$, then $$d$$ divides
$$af + bg = h$$. $$\square$$

A set with properties (i) and (ii) is called an *ideal*. A greatest
common divisor is determined only up to a nonzero scalar factor, and
$$\gcd$$ here means any one of them.

> **Definition (Irreducible polynomial).** A polynomial
> $$p(x) \in \mathbb{F}[x]$$ of degree at least $$1$$ is **irreducible**
> if it is not a product of two polynomials of degree at least $$1$$.
> Equivalently, its only divisors are the nonzero constants $$c$$ and the
> polynomials $$c\,p(x)$$.
{: .definition #def-irreducible }

Let $$p(x)$$ be irreducible, and define

$$
\begin{aligned}
\langle p(x) \rangle &= \{\text{polynomials divisible by } p(x)\} , \\
a(x) + \langle p(x) \rangle
&= \{\, a(x) + f(x) : f(x) \in \langle p(x) \rangle \,\} .
\end{aligned}
$$

Exactly as for the integers,
$$a(x) + \langle p(x) \rangle = a'(x) + \langle p(x) \rangle$$ if and
only if $$a(x) - a'(x) \in \langle p(x) \rangle$$, the operations

$$
\begin{aligned}
\big(a(x) + \langle p(x) \rangle\big) + \big(b(x) + \langle p(x) \rangle\big)
&= \big(a(x) + b(x)\big) + \langle p(x) \rangle , \\
\big(a(x) + \langle p(x) \rangle\big)\big(b(x) + \langle p(x) \rangle\big)
&= a(x) b(x) + \langle p(x) \rangle
\end{aligned}
$$

are well defined, and

$$
\mathbb{F}[x]/\langle p(x) \rangle
= \{\, a(x) + \langle p(x) \rangle : a(x) \in \mathbb{F}[x] \,\}
$$

is a commutative ring.

> **Theorem.** If $$p(x) \in \mathbb{F}[x]$$ is irreducible, then
> $$\mathbb{F}[x]/\langle p(x) \rangle$$ is a field.
{: .theorem #thm-polynomial-quotient-field }

*Proof.* The one, $$1 + \langle p(x) \rangle$$, is not the zero, because
$$p(x)$$ has positive degree and does not divide $$1$$. Let
$$n(x) + \langle p(x) \rangle$$ be nonzero, so $$p(x)$$ does not divide
$$n(x)$$. By the [Lemma](#lem-bezout) there are $$a(x), b(x)$$ such that
$$h = ap + bn$$ divides both $$p$$ and $$n$$. A divisor of the
irreducible $$p$$ is a constant $$c$$ or $$c\,p$$, and $$c\,p$$ does not
divide $$n$$. So $$h$$ is a nonzero constant $$c$$, and dividing by
$$c$$ we may assume

$$
a(x) p(x) + b(x) n(x) = 1 .
$$

Then

$$
\begin{aligned}
\big(b(x) + \langle p(x) \rangle\big)\big(n(x) + \langle p(x) \rangle\big)
&= b(x) n(x) + \langle p(x) \rangle \\
&= \big(1 - a(x) p(x)\big) + \langle p(x) \rangle
= 1 + \langle p(x) \rangle . \qquad \square
\end{aligned}
$$

By division with remainder, each coset contains exactly one polynomial
that is zero or of degree less than $$d = \deg p$$. So
$$\mathbb{F}[x]/\langle p(x) \rangle$$ is a $$d$$-dimensional vector
space over $$\mathbb{F}$$, with the cosets of
$$1, x, \dots, x^{d-1}$$ as a basis. When
$$\mathbb{F} = \mathbb{F}_q$$ has $$q$$ elements, the new field has
$$q^d$$ elements.

**Example (a field with four elements).** The polynomial
$$x^2 + x + 1 \in \mathbb{F}_2[x]$$ is irreducible: a product of two
polynomials of degree $$1$$ would have a root in $$\mathbb{F}_2$$, but
its values at $$0$$ and at $$1$$ are both $$1$$. So
$$\mathbb{F}_2[x]/\langle x^2 + x + 1 \rangle$$ is a field with
$$2^2 = 4$$ elements. Write $$\alpha$$ for the coset of $$x$$; the
elements are $$0$$, $$1$$, $$\alpha$$ and $$\alpha + 1$$, and
$$\alpha^2 = \alpha + 1$$ because
$$x^2 - (x + 1) = x^2 + x + 1$$ over $$\mathbb{F}_2$$. For instance

$$
(\alpha + 1)\,\alpha = \alpha^2 + \alpha = (\alpha + 1) + \alpha = 1 ,
$$

so $$\alpha$$ and $$\alpha + 1$$ are inverses of each other. The full
tables are:

| $$+$$ | $$0$$ | $$1$$ | $$\alpha$$ | $$\alpha + 1$$ |
|---|---|---|---|---|
| $$0$$ | $$0$$ | $$1$$ | $$\alpha$$ | $$\alpha + 1$$ |
| $$1$$ | $$1$$ | $$0$$ | $$\alpha + 1$$ | $$\alpha$$ |
| $$\alpha$$ | $$\alpha$$ | $$\alpha + 1$$ | $$0$$ | $$1$$ |
| $$\alpha + 1$$ | $$\alpha + 1$$ | $$\alpha$$ | $$1$$ | $$0$$ |

| $$\cdot$$ | $$0$$ | $$1$$ | $$\alpha$$ | $$\alpha + 1$$ |
|---|---|---|---|---|
| $$0$$ | $$0$$ | $$0$$ | $$0$$ | $$0$$ |
| $$1$$ | $$0$$ | $$1$$ | $$\alpha$$ | $$\alpha + 1$$ |
| $$\alpha$$ | $$0$$ | $$\alpha$$ | $$\alpha + 1$$ | $$1$$ |
| $$\alpha + 1$$ | $$0$$ | $$\alpha + 1$$ | $$1$$ | $$\alpha$$ |

This field has characteristic two, and it is not the ring of integers
modulo $$4$$, in which $$2 \cdot 2 = 0$$.

---

## References

- Stephen H. Friedberg, Arnold J. Insel and Lawrence E. Spence, *Linear
  Algebra*, 5th edition, Pearson, 2018 — Chapter 4, §4.5, Appendix C for
  fields, and the exercises cited by number.
- Linear Algebra (881.007), Seoul National University, Fall 2023.
  Instructor: Jin Hong (홍진). Lecture slides for Chapter 4 and for finite
  fields, and the course problem sheet for Chapter 4.
- The definitions, the statements of the theorems and their numbering are
  the slides'. The three corollaries of Theorem 4.10 are unnumbered on the
  slides and are numbered here in the order the slides give them, with the
  third stated for $$\delta(EA)$$ as the proof of Theorem 4.11 uses it.
- Theorem 4.11 is stated as on the slides, without the hypothesis
  $$\delta(I_n) = 1$$ that the problem sheet includes.
- The slides state the permutation formula as a theorem and refer to
  Hong Jong Kim's *Calculus 1*, Chapter 7, for permutations and their
  signs; the proof written here checks the three properties of
  Theorem 4.12.
- In the section on finite fields, the statements are the slides'. The
  slides give the proofs of the two field theorems and of the lemma on
  polynomials; the remaining proofs are written out here. The slides call
  on unique factorization for greatest common divisors; the lemma here is
  stated so that it does not need it. The slides write the elements of the
  field with four elements as $$00, 01, 10, 11$$; here they are
  $$0, 1, \alpha, \alpha + 1$$.
- The solutions to the problems are mine.

[thm-4-3]: /posts/linear-algebra-determinants/#thm-4-3
[cor-4-4]: /posts/linear-algebra-determinants/#cor-4-4
[cor-4-6]: /posts/linear-algebra-determinants/#cor-4-6
[thm-3-1]: /posts/linear-algebra-linear-systems/#thm-3-1
[det-elementary]: /posts/linear-algebra-determinants/#det-elementary
[thm-3-7]: /posts/linear-algebra-linear-systems/#thm-3-7
[cor-3-6-3]: /posts/linear-algebra-linear-systems/#cor-3-6-3
[thm-4-7]: /posts/linear-algebra-determinants/#thm-4-7
[thm-2-7]: /posts/linear-algebra-linear-transformations/#thm-2-7
[def-field]: /posts/linear-algebra-vector-spaces/#def-field
[def-characteristic]: /posts/linear-algebra-vector-spaces/#def-characteristic
[ex-1-3-31]: /posts/linear-algebra-vector-spaces-2/#ex-1-3-31
[def-quotient-space]: /posts/linear-algebra-vector-spaces-2/#def-quotient-space
