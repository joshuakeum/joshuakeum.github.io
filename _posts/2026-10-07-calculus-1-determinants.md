---
title: "Calculus 1: Matrices and Linear Maps"
date: 2026-10-07 09:00:00 +0900
categories: [Course Notes, Calculus 1]
tags: [matrices, linear maps, transpose, matrix product, rotation]
description: Matrix arithmetic and what the product is really for — linear maps, composition, the transpose and its one identity, and the matrix of a projection, a cross product and a rotation. Unit 5 of Calculus 1, part one.
math: true
mermaid: false
render_with_liquid: false
---

> This unit covers textbook Chapters 6 and 7 together with §8.1. **Part 1,
> Chapter 6, is below.** Determinants and the cross product as a determinant
> follow when those chapters are written up, and will be added to this page.
{: .prompt-info }

## What this unit answers

[Unit 4](/posts/calculus-1-coordinates-vectors/) ended on a question. Two
vectors in the plane are dependent exactly when $$ad - bc = 0$$, and three
vectors in space have a similar six-term criterion. Is there one for four
vectors in $$\mathbb{R}^4$$? There is, and reaching it means building the
object those expressions live in.

This part answers a smaller and more basic question first: **what is the matrix
product for?** The definition looks arbitrary when you meet it — a sum over a
repeated index, rows against columns. It is not arbitrary. It is the unique
definition that makes matrix multiplication *be* the composition of maps, and
everything in Chapter 6 follows from reading it that way.

## Prerequisites

[Unit 4](/posts/calculus-1-coordinates-vectors/) for the inner product, the
standard unit vectors $$e_1, \ldots, e_n$$, linear combinations and linear
independence, and the orthogonal projection $$P_v$$ and cross product that
reappear here as examples.

---

## Part 1 — Chapter 6: matrices and linear maps

### The vocabulary

A **matrix** is a rectangular array of real numbers. The array with $$m$$ rows
and $$n$$ columns is said to have **size** $$m \times n$$, and its horizontal
vectors are **rows** while its vertical vectors are **columns**. The entry in
position $$(i,j)$$ is written $$a_{ij}$$ and called the $$(i,j)$$-th **element**
or **entry**.

The named special cases:

- **Zero matrix** $$O$$ — every entry is $$0$$.
- **Square matrix** — $$m = n$$.
- **Diagonal element** — the $$(i,i)$$ entry of a square matrix; the collection
  of them is the **diagonal**.
- **Diagonal matrix** — square, with every off-diagonal entry $$0$$.
- **Identity matrix** $$I_n$$, or $$I$$ — diagonal, with every diagonal entry
  $$1$$.

### Arithmetic

Addition and subtraction need matrices of the **same size**, and work entry by
entry; scalar multiplication multiplies every entry:

$$
k\begin{pmatrix} a & b \\ c & d \end{pmatrix}
= \begin{pmatrix} ka & kb \\ kc & kd \end{pmatrix}
$$

Multiplication is the one with a condition on sizes:

$$
(m \times n)(n \times l) = (m \times l),
$$

so the inner dimensions must agree, and for $$AB = C = (c_{ij})$$,

$$
c_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj} .
$$

The $$(i,j)$$ entry is the $$i$$-th row of $$A$$ dotted with the $$j$$-th column
of $$B$$ — which is the first hint that this operation has something to do with
inner products.

**Properties that do hold.**

$$
\begin{aligned}
A + B &= B + A, \\
k(AB) &= (kA)B = A(kB), \\
A(B + C) &= AB + AC, \\
(A + B)C &= AC + BC, \\
A I_n = A, \quad & I_n B = B .
\end{aligned}
$$

Two remarks the notes make in passing, both load-bearing later:

- **A vector is a matrix.** A column vector is an $$n \times 1$$ matrix and a
  row vector is a $$1 \times n$$ matrix. Nothing separate needs defining.
- **Concatenation.** If $$Av_1 = w_1$$, $$Av_2 = w_2$$, $$Av_3 = w_3$$, then
  stacking the vectors side by side as columns gives

$$
A\,(v_1 \ v_2 \ v_3) = (w_1 \ w_2 \ w_3).
$$

That second one turns a list of vector equations into a single matrix equation,
and it is how the associativity proof works.

**Associativity.** First for a vector, $$(AB)v = A(Bv)$$, by direct expansion.
Then for matrices: write $$C = (v_1\ v_2\ v_3)$$ in columns. Since
$$(AB)v_i = A(Bv_i)$$ for each $$i$$, concatenating the three results gives

$$
(AB)C = A(BC).
$$

The vector case plus concatenation is the whole argument.

### What fails

Matrix multiplication is **not commutative**, and the notes put a star next to
it. $$AB \ne BA$$ in general, and the standard illustration is multiplying by a
diagonal matrix on each side: one scales the columns, the other scales the rows.

Three more failures, each the loss of a cancellation you are used to:

$$
\begin{aligned}
AB = O \ &\nRightarrow\ A = O \ \text{ or } \ B = O, \\
AB = AC, \ A \ne O \ &\nRightarrow\ B = C, \\
BA = CA, \ A \ne O \ &\nRightarrow\ B = C .
\end{aligned}
$$

For the first, a two-by-two example settles it:

$$
\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}
\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}
= \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}
$$

Neither factor is zero. Matrices therefore have **zero divisors**, which is
exactly what real numbers do not have, and it is why you may not cancel.

> **The binomial formula breaks.** For numbers
> $$(x+y)^2 = x^2 + 2xy + y^2$$, but for matrices
>
> $$
> (A+B)^2 = A^2 + AB + BA + B^2,
> $$
>
> which is **not** $$A^2 + 2AB + B^2$$, because the two middle terms are
> different matrices. Every algebraic identity you half-remember has to be
> re-derived without commuting anything.
{: .prompt-warning }

The identity matrix does commute with everything, so expansions involving only
$$A$$ and $$I$$ survive intact:

$$
\begin{aligned}
(A+I)^3 &= A^3 + 3A^2 + 3A + I, \\
(A+I)(A^2 - A + I) &= A^3 + I .
\end{aligned}
$$

### The transpose

The **transpose** $$A^{t}$$ reflects the matrix across its diagonal, turning
rows into columns:

$$
\begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}^{t}
= \begin{pmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{pmatrix}
$$

Its rules are unremarkable except for the last:

$$
\begin{aligned}
(A + B)^{t} &= A^{t} + B^{t}, \\
(cA)^{t} &= cA^{t}, \\
\left(A^{t}\right)^{t} &= A, \\
(AB)^{t} &= B^{t} A^{t} .
\end{aligned}
$$

**The order reverses.** That is the one to remember, and it is forced by the
sizes alone: if $$A$$ is $$m \times n$$ and $$B$$ is $$n \times l$$, then
$$A^{t}B^{t}$$ does not even have compatible dimensions, while
$$B^{t}A^{t}$$ does.

### The inner product is a matrix product

> Get into the habit of seeing every vector as a **column** vector. The notes
> are emphatic about this and say the reason becomes clear on its own with time.
> The identity below is the first instalment of that reason.
{: .prompt-tip }

With vectors as columns, the inner product is a $$1 \times 1$$ matrix product:

$$
a \cdot b = b^{t} a = a^{t} b .
$$

From that one observation comes what the notes call almost everything about the
transpose:

$$
Av \cdot w = v \cdot A^{t} w .
$$

*Proof.* The inner product of two vectors is a scalar, and a scalar is the same
thing as a $$1 \times 1$$ matrix — which is therefore equal to its own
transpose. So

$$
\begin{aligned}
Av \cdot w &= w^{t} A v \\
&= \left(w^{t} A v\right)^{t} \\
&= v^{t} A^{t} w = v \cdot A^{t} w . \qquad \square
\end{aligned}
$$

The whole proof is: transpose a number, which changes nothing, and let the
order-reversing rule do the work. **This identity is what the transpose is
for** — it moves a matrix from one side of an inner product to the other.

### Linear maps

**Theorem.** For a map $$L : \mathbb{R}^n \to \mathbb{R}^m$$, these are
equivalent:

1. There is an $$m \times n$$ matrix $$A$$ with $$L(x) = Ax$$.
2. For all scalars $$\alpha, \beta$$ and all vectors $$v, w \in \mathbb{R}^n$$,

$$
L(\alpha v + \beta w) = \alpha L(v) + \beta L(w).
$$

A map satisfying these is a **linear transformation** or **linear map**.

*Proof.* ($$1 \Rightarrow 2$$) Immediate from the distributive law:

$$
\begin{aligned}
L(\alpha v + \beta w) &= A(\alpha v + \beta w) \\
&= \alpha Av + \beta Aw = \alpha L(v) + \beta L(w).
\end{aligned}
$$

($$2 \Rightarrow 1$$) The lectures did the case $$n = 2$$, $$m = 3$$ and noted
that the general case reads the same. Write
$$L(e_1) = (a, b, c)^{t}$$ and $$L(e_2) = (d, e, f)^{t}$$. Then for any
$$(x, y)$$,

$$
\begin{aligned}
L\begin{pmatrix} x \\ y \end{pmatrix}
&= L(x e_1 + y e_2) \\
&= x\,L(e_1) + y\,L(e_2) \\
&= \begin{pmatrix} ax + dy \\ bx + ey \\ cx + fy \end{pmatrix}
= A\begin{pmatrix} x \\ y \end{pmatrix},
\end{aligned}
$$

where $$A$$ has columns $$L(e_1)$$ and $$L(e_2)$$. $$\square$$

> **The proof hands you a recipe.** The matrix of a linear map is the matrix
> whose columns are $$L(e_1), L(e_2), \ldots, L(e_n)$$ — the images of the
> standard unit vectors. Every worked example below is an application of that
> one sentence.
{: .prompt-tip }

### Composition is multiplication

Here is the answer to the question this part opened with. The notes put it
directly: the peculiar-looking definition of the matrix product exists **so that
the product represents composition.**

If $$A$$ sends $$\mathbb{R}^3 \to \mathbb{R}^3$$ and $$B$$ sends
$$\mathbb{R}^3 \to \mathbb{R}^2$$, then applying $$A$$ and then $$B$$ is

$$
B(Ax) = (BA)x,
$$

which is associativity for a vector, read from right to left. The composite map
is the matrix $$BA$$. That is the whole reason for
$$c_{ij} = \sum_k a_{ik}b_{kj}$$: any other definition would fail to compose.

It also explains the order. $$BA$$ means *$$A$$ first*, because the vector sits
on the right and is reached by $$A$$ first. The notation runs backwards relative
to reading order, and that is the price of writing $$L(x)$$ rather than $$xL$$.

### What linear maps preserve

- $$L(0) = 0$$, since $$L(0) = L(0 \cdot v) = 0 \cdot L(v) = 0$$. A map that
  moves the origin is not linear, whatever else it does.
- **The image is a span.** $$L(x) = Ax$$ is the linear combination of the
  columns of $$A$$ with coefficients the entries of $$x$$. So the image of a
  linear map is exactly the set of linear combinations of the columns — which
  is why the questions of Unit 4 about independence return here.
- **Collinear points stay collinear, or collapse.** Three collinear points go to
  three collinear points, or all to a single point. In the former case the
  **ratios of distances are preserved**:

$$
L\bigl[(1-t)P + tQ\bigr] = (1-t)L(P) + t\,L(Q).
$$

- **Parallel stays parallel.** Lines, planes and so on go to parallel lines,
  planes and so on, with degeneration allowed. A parallelogram maps to a point,
  a segment, or a parallelogram; a parallelepiped maps to a point, a segment, a
  parallelogram, or a parallelepiped. The one-line reason is

$$
L(P + tv) = L(P) + t\,L(v).
$$

That list of degenerations is worth holding on to. A linear map can collapse
dimensions but never create them, and *how much* it collapses is what the
determinant will measure.

### Worked examples: finding the matrix

**1. From images of two vectors.** Suppose
$$L(e_1) = (1,2,3)^{t}$$ and $$L\bigl((1,1)^{t}\bigr) = (a,b,c)^{t}$$. Write
the unknown matrix with columns $$(1,2,3)^{t}$$ and $$(p,q,r)^{t}$$. The first
column is already fixed by $$L(e_1)$$. For the second,

$$
A\begin{pmatrix} 1 \\ 1 \end{pmatrix}
= \begin{pmatrix} 1 + p \\ 2 + q \\ 3 + r \end{pmatrix}
= \begin{pmatrix} a \\ b \\ c \end{pmatrix},
$$

so $$p = a - 1$$, $$q = b - 2$$, $$r = c - 3$$ and

$$
A = \begin{pmatrix} 1 & a-1 \\ 2 & b-2 \\ 3 & c-3 \end{pmatrix}.
$$

The point is that $$(1,1)^{t}$$ is not a standard unit vector, so you subtract
off the part already accounted for.

**2. From images of three vectors.** Given

$$
\begin{aligned}
L\,(1,2,1)^{t} &= (1,2,3)^{t}, \\
L\,(2,3,4)^{t} &= (5,6,7)^{t}, \\
L\,(3,5,2)^{t} &= (2,1,1)^{t},
\end{aligned}
$$

concatenate all three into one matrix equation, inputs as columns on the left
and outputs as columns on the right:

$$
A\begin{pmatrix} 1 & 2 & 3 \\ 2 & 3 & 5 \\ 1 & 4 & 2 \end{pmatrix}
= \begin{pmatrix} 1 & 5 & 2 \\ 2 & 6 & 1 \\ 3 & 7 & 1 \end{pmatrix}
$$

and $$A$$ is the right-hand matrix times the inverse of the left. Finishing it
needs the inverse, or elementary row operations, and first-year mathematics does
not cover either — so the answer is left in this form. Concatenation is what
made three separate conditions into one equation.

**3. The matrix of a projection.** For $$v = (1,2,3)^{t}$$, find the matrix of
$$L(x) = P_v(x)$$. Starting from the projection formula of Unit 4 and pushing
the scalar to the right of the vector:

$$
\begin{aligned}
P_v(x) &= \frac{v \cdot x}{v \cdot v}\, v
= \frac{1}{\lvert v \rvert^2}\, v\,(v \cdot x) \\
&= \frac{1}{\lvert v \rvert^2}\, v\left(v^{t} x\right)
= \frac{1}{\lvert v \rvert^2}\left(v v^{t}\right) x .
\end{aligned}
$$

So the matrix is $$v v^{t} / \lvert v \rvert^2$$, and with
$$\lvert v \rvert^2 = 14$$,

$$
A = \frac{1}{14}\begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 3 & 6 & 9 \end{pmatrix}.
$$

> Notice the move that made this work: $$v(v \cdot x)$$ was rewritten as
> $$\left(v v^{t}\right)x$$ by **writing the scalar behind the vector**. The
> notes ask you to register this habit. A column times a row is a matrix; a row
> times a column is a scalar. Which one you get is decided by the order.
{: .prompt-tip }

**4. The matrix of a cross product.** For $$v = (a,b,c)^{t}$$, the map
$$L(x) = v \times x$$ is linear, and writing out the components,

$$
\begin{pmatrix} a \\ b \\ c \end{pmatrix} \times \begin{pmatrix} x \\ y \\ z \end{pmatrix}
= \begin{pmatrix} bz - cy \\ -az + cx \\ ay - bx \end{pmatrix},
$$

which rearranges into a matrix acting on $$(x,y,z)^{t}$$:

$$
A = \begin{pmatrix} 0 & -c & b \\ c & 0 & -a \\ -b & a & 0 \end{pmatrix}.
$$

This matrix satisfies $$A^{t} = -A$$ — it is **skew-symmetric**, which is the
matrix-level statement of the anti-symmetry $$a \times b = -\,b \times a$$ from
Unit 4. The zero diagonal is $$v \times v = 0$$.

**5. The matrix of a rotation.** Let $$R_\theta : \mathbb{R}^2 \to \mathbb{R}^2$$
rotate by $$\theta$$ about the origin. It is linear — rotating a sum rotates
each part, and rotating a scaled vector scales the rotation. So apply the
recipe and rotate the standard unit vectors:

$$
\begin{aligned}
R_\theta(e_1) &= (\cos\theta,\ \sin\theta)^{t}, \\
R_\theta(e_2) &= (-\sin\theta,\ \cos\theta)^{t},
\end{aligned}
$$

and those are the columns:

$$
R_\theta = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}.
$$

Now compose two rotations. Rotating by $$\theta$$ and then by $$\varphi$$ must
be rotation by $$\theta + \varphi$$, so $$R_\varphi R_\theta = R_{\theta+\varphi}$$.
Multiplying the two matrices and comparing entries reproduces the **angle
addition formulas** for sine and cosine. They are not an extra fact; they are
the statement that rotation composes.

## Common pitfalls

- **Cancelling.** $$AB = AC$$ with $$A \ne O$$ does not give $$B = C$$. Matrices
  have zero divisors.
- **Writing $$(A+B)^2 = A^2 + 2AB + B^2$$.** The middle terms are $$AB$$ and
  $$BA$$, and they differ.
- **Getting the transpose of a product backwards.** $$(AB)^{t} = B^{t}A^{t}$$.
  If in doubt, check the sizes — only one order is even defined.
- **Reading $$BA$$ as "$$B$$ first".** The vector is on the right, so $$A$$ acts
  first.
- **Forgetting $$L(0) = 0$$.** A translation is not a linear map, which is why
  Unit 4 kept translations and isometries as a separate idea.
- **Treating a non-standard input as a basis vector.** The columns of the matrix
  are the images of $$e_1, \ldots, e_n$$ specifically; anything else needs
  solving for, as in example 1.
- **Putting the scalar in front out of habit.** $$v(v \cdot x)$$ and
  $$(vv^{t})x$$ are the same thing, but only the second is visibly a matrix
  acting on a vector.

## Connections

- **Backward.** The projection and the cross product come from
  [Unit 4](/posts/calculus-1-coordinates-vectors/) and reappear here as
  matrices, which is a fair summary of what this chapter does to the previous
  one. The image of a linear map being the span of the columns connects directly
  to the independence questions that closed Unit 4.
- **Forward.** The question of when $$Ax = b$$ can be solved, and the inverse
  that example 2 needed but could not use, is what the determinant answers.
  That is Chapter 7, and it will be added to this page.
- **Outward.** That rotation matrices compose to give the angle addition
  formulas is the first case of a general principle: a group of symmetries
  becomes a set of matrices, and composing symmetries becomes multiplying them.

## Summary

- **Product** — $$c_{ij} = \sum_k a_{ik}b_{kj}$$, defined on sizes
  $$(m \times n)(n \times l)$$
- **Not commutative** — $$AB \ne BA$$; no cancellation; zero divisors exist
- **Transpose** — $$(AB)^{t} = B^{t}A^{t}$$, order reversed
- **Inner product** — $$a \cdot b = a^{t}b$$, and $$Av \cdot w = v \cdot A^{t}w$$
- **Linear map** — $$L(\alpha v + \beta w) = \alpha L(v) + \beta L(w)$$, equivalently $$L(x) = Ax$$
- **Its matrix** — columns are $$L(e_1), \ldots, L(e_n)$$
- **Composition** — is the matrix product, $$B(Ax) = (BA)x$$
- **Image** — the span of the columns of $$A$$
- **Projection onto $$v$$** — $$vv^{t} / \lvert v \rvert^2$$
- **Cross product by $$v$$** — skew-symmetric, $$A^{t} = -A$$
- **Rotation by $$\theta$$** — columns $$(\cos\theta, \sin\theta)^{t}$$ and $$(-\sin\theta, \cos\theta)^{t}$$

## References

- Hong Jong Kim, *Calculus 1+* (미적분학 1+), 2nd revised edition, Seoul National University Press — Chapter 6.
- Mathematics 1 (수학 1, L0442.000100), Seoul National University, Spring 2022. Instructor: Choi Hyung Gyu (최형규). Lecture notes for Chapter 6 dated 24 April 2022.
- The rotation example is from the handwritten additions to those notes; the printed text ends at the cross-product matrix.
- Inverses and elementary row operations were explicitly left outside the first-year syllabus.
