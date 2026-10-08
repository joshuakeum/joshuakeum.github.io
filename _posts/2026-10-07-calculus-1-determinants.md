---
title: "Calculus 1: Matrices, Linear Maps, and Determinants"
date: 2026-10-07 09:00:00 +0900
categories: [Course Notes, Calculus 1]
tags: [matrices, linear maps, determinant, inverse matrix, permutations, cross product]
description: The matrix product as composition of linear maps; inverses, permutations, and the determinant as the unique alternating multi-linear form; and the cross product read off a determinant. Unit 5 of Calculus 1.
math: true
mermaid: false
render_with_liquid: false
---

> This unit covers textbook Chapters 6 and 7 together with §8.1, in three
> parts: **matrices and linear maps**, **inverses and the determinant**, and
> **the cross product as a determinant**. It is the longest unit of the course
> and the only one that is essentially linear algebra.
{: .prompt-info }

## What this unit answers

[Unit 4](/posts/calculus-1-coordinates-vectors/) ended on a question. Two
vectors in the plane are dependent exactly when $$ad - bc = 0$$, and three
vectors in space have a similar six-term criterion. Is there one for four
vectors in $$\mathbb{R}^4$$? There is, and reaching it means building the
object those expressions live in.

That object is the determinant, and Part 2 builds it. Part 1 answers a smaller
and more basic question first: **what is the matrix product for?** The
definition looks arbitrary when you meet it — a sum over a repeated index, rows
against columns. It is not arbitrary. It is the unique definition that makes
matrix multiplication *be* the composition of maps, and everything in Chapter 6
follows from reading it that way.

The determinant gets the same treatment. It is not introduced as a formula to
memorise; it is the unique function of the columns of a matrix that is linear in
each one separately, vanishes whenever two columns agree, and equals $$1$$ at
the identity. Those three demands force the formula, down to the last sign. Part
3 then reads the cross product off a determinant, and the geometry Unit 4 kept
gesturing at — area, volume, orientation — turns out to be what the determinant
was all along.

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

---

## Part 2 — Chapter 7: inverses and the determinant

Part 1 built the matrix product and showed it was composition. The next question
is whether a composition can be undone, and the determinant is the answer — not
a formula handed down, but the one number that decides it.

### The inverse

**Definition.** Let $$A$$ be a square matrix. If there is a square matrix $$B$$
of the same size with

$$
AB = BA = I_n ,
$$

then $$A$$ is **invertible** (가역행렬). Then $$B$$ is invertible too, each is
the **inverse** (역행렬) of the other, and one writes

$$
B = A^{-1} \quad \text{and} \quad A = B^{-1} .
$$

The definition asks for both products. It need not.

**Theorem 1.1.** For $$n \times n$$ matrices $$A$$ and $$B$$,

$$
AB = I_n \ \Longrightarrow \ BA = I_n .
$$

> On the proof the lectures were unusually frank: *I do not know a simple proof
> that you, at this stage, could follow easily. We will not cover it in this
> course. But do memorise the fact.* It is worth knowing why it is not obvious:
> $$AB = I$$ says only that $$B$$ is a **right** inverse, and for maps in
> general a right inverse need not be a left inverse. Squareness is what forces
> the two to coincide.
{: .prompt-info }

**Theorem 1.2.** If $$A$$ and $$B$$ are invertible, then

$$
(A^{-1})^{-1} = A, \qquad (AB)^{-1} = B^{-1}A^{-1} .
$$

The order reverses, exactly as it did for the transpose, and for the same
reason. The product $$AB$$ applies $$B$$ first and $$A$$ second, so undoing it
means undoing $$A$$ first.

### Worked example: inverting a 2×2 the hard way

Find the inverse of $$\begin{pmatrix} 1 & 2 \\ 1 & 3 \end{pmatrix}$$.

There is no formula yet, so write the unknown inverse out and demand that the
product be the identity:

$$
\begin{pmatrix} 1 & 2 \\ 1 & 3 \end{pmatrix}
\begin{pmatrix} x & z \\ y & w \end{pmatrix}
= \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}.
$$

Reading that one column at a time splits it into two independent systems:

$$
\begin{aligned}
\begin{pmatrix} 1 & 2 \\ 1 & 3 \end{pmatrix}
\begin{pmatrix} x \\ y \end{pmatrix}
&= \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \\[2pt]
\begin{pmatrix} 1 & 2 \\ 1 & 3 \end{pmatrix}
\begin{pmatrix} z \\ w \end{pmatrix}
&= \begin{pmatrix} 0 \\ 1 \end{pmatrix},
\end{aligned}
$$

that is,

$$
\begin{cases} x + 2y = 1 \\ x + 3y = 0 \end{cases}
\qquad
\begin{cases} z + 2w = 0 \\ z + 3w = 1 \end{cases}
$$

with solutions $$(x,y) = (3,-1)$$ and $$(z,w) = (-2,1)$$. So

$$
\begin{pmatrix} 1 & 2 \\ 1 & 3 \end{pmatrix}^{-1}
= \begin{pmatrix} 3 & -2 \\ -1 & 1 \end{pmatrix}.
$$

### Where $$ad - bc$$ comes from

Run the same computation with letters. For
$$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$$ the two systems are

$$
\begin{cases} ax + by = 1 \\ cx + dy = 0 \end{cases}
\qquad
\begin{cases} az + bw = 0 \\ cz + dw = 1 \end{cases}
$$

and eliminating one unknown at a time turns them into

$$
\begin{cases} (ad - bc)\,x = d \\ (ad - bc)\,y = -c \end{cases}
\qquad
\begin{cases} (ad - bc)\,z = -b \\ (ad - bc)\,w = a \end{cases}
$$

Everything now hangs on the single number $$ad - bc$$.

If $$ad - bc \ne 0$$, divide through:

$$
\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1}
= \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}.
$$

If $$ad - bc = 0$$, the four equations read $$0 = d$$, $$0 = -c$$, $$0 = -b$$,
$$0 = a$$. Unless $$A$$ is the zero matrix the systems have no solution at all,
and the zero matrix plainly has no inverse either. So $$A$$ is invertible
exactly when $$ad - bc \ne 0$$, and that number earns a name:

$$
\det\begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc .
$$

**Theorem 1.3.** For $$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$$ the
following are equivalent.

- $$\det A \ne 0$$.
- $$A$$ is invertible.
- The column vectors $$(a,c)^{t}$$ and $$(b,d)^{t}$$ are linearly independent.
- The row vectors $$(a,b)$$ and $$(c,d)$$ are linearly independent.

### Two questions, and one honest answer

For a general $$n \times n$$ matrix $$A$$ the $$2 \times 2$$ case raises two
questions.

1. Is there a number $$\det A$$ that decides whether $$A$$ is invertible?
2. If $$A$$ is invertible, is there a formula for $$A^{-1}$$?

The answer to the first is yes, and the next section constructs it — though, as
the lectures put it, *the definition is a bit hard*.

The answer to the second is yes and no. A formula exists, and you cannot write
it down. For a $$10 \times 10$$ matrix it would not fit on tens of thousands of
sheets of paper. For matrices of any size it is, in the lectures' phrase,
**a formula of almost no use**.

> That does not mean large inverses are out of reach. If the entries are actual
> numbers rather than letters, there are reasonably easy ways to find the
> inverse. Those methods — elementary row operations and Gauss–Jordan
> elimination — were deliberately left outside this course.
{: .prompt-tip }

### Two easy cases

Diagonal and anti-diagonal matrices invert on sight:

$$
\begin{pmatrix}
\lambda_1 & 0 & 0 \\ 0 & \lambda_2 & 0 \\ 0 & 0 & \lambda_3
\end{pmatrix}^{-1}
=
\begin{pmatrix}
1/\lambda_1 & 0 & 0 \\ 0 & 1/\lambda_2 & 0 \\ 0 & 0 & 1/\lambda_3
\end{pmatrix},
$$

$$
\begin{pmatrix}
0 & 0 & \lambda_1 \\ 0 & \lambda_2 & 0 \\ \lambda_3 & 0 & 0
\end{pmatrix}^{-1}
=
\begin{pmatrix}
0 & 0 & 1/\lambda_3 \\ 0 & 1/\lambda_2 & 0 \\ 1/\lambda_1 & 0 & 0
\end{pmatrix}.
$$

Note the second one: the reciprocals come back in the opposite order. The
anti-diagonal matrix reverses the coordinates as well as scaling them, so the
inverse has to undo the reversal too.

### What a determinant has to be

Here is the move that makes Chapter 7 worth reading. Rather than write down a
formula and check that it behaves well, write down the behaviour you want and
see what formula it forces.

Regard a square matrix as a list of its $$n$$ column vectors, so that a function
on matrices is a function of $$n$$ vector arguments.

**Definition 2.1.** A function
$$\phi : \mathcal{M}_{n \times n}(\mathbb{R}) \to \mathbb{R}$$ is

1. **multi-linear** (다중선형) if it is linear in each slot separately: for all
   scalars $$c, \tilde{c}$$ and all vectors $$v_i, \tilde{v}_i$$,

   $$
   \begin{aligned}
   &\phi(v_1, \ldots, cv_i + \tilde{c}\tilde{v}_i, \ldots, v_n) \\
   &\quad = c\,\phi(v_1, \ldots, v_i, \ldots, v_n) \\
   &\quad\quad + \tilde{c}\,\phi(v_1, \ldots, \tilde{v}_i, \ldots, v_n);
   \end{aligned}
   $$

2. **skew-symmetric** (왜대칭) if exchanging two slots flips the sign,

   $$
   \phi(\cdots, v, \cdots, w, \cdots) = -\,\phi(\cdots, w, \cdots, v, \cdots);
   $$

3. **alternating** (교대) if a repeated argument kills it,

   $$
   \phi(\cdots, v, \cdots, v, \cdots) = 0 .
   $$

**Theorem 2.2.** For multi-linear $$\phi$$: alternating $$\iff$$
skew-symmetric.

### Worked: the 2-form is forced

Take any alternating multi-linear **2-form**
$$\phi : \mathcal{M}_{2 \times 2} \to \mathbb{R}$$. Write each column in the
standard basis and expand:

$$
\begin{aligned}
\phi\begin{pmatrix} a & b \\ c & d \end{pmatrix}
&= \phi(ae_1 + ce_2,\ be_1 + de_2) \\
&= a\,\phi(e_1,\ be_1 + de_2) + c\,\phi(e_2,\ be_1 + de_2) \\
&= ab\,\phi(e_1,e_1) + ad\,\phi(e_1,e_2) \\
&\qquad + cb\,\phi(e_2,e_1) + cd\,\phi(e_2,e_2) \\
&= ad\,\phi(e_1,e_2) + cb\,\phi(e_2,e_1) \\
&= (ad - bc)\,\phi(e_1,e_2).
\end{aligned}
$$

Two of the four terms died because the argument repeated; the remaining pair
collapsed because swapping flips the sign. Nothing was assumed about $$\phi$$
except the three properties, and $$ad - bc$$ came out anyway. The $$2\times2$$
determinant was never a choice.

### The 3-form, and six familiar terms

Now an alternating multi-linear **3-form** on $$\mathcal{M}_{3\times 3}$$.
Expanding all three columns gives $$3^3 = 27$$ terms, of which every one with a
repeated $$e_i$$ vanishes, leaving $$3! = 6$$:

$$
\begin{aligned}
&\phi\begin{pmatrix} a & d & g \\ b & e & h \\ c & f & j \end{pmatrix} \\
&\ = aej\,\phi(e_1,e_2,e_3) + afh\,\phi(e_1,e_3,e_2) \\
&\ \ \ + bdj\,\phi(e_2,e_1,e_3) + bfg\,\phi(e_2,e_3,e_1) \\
&\ \ \ + cdh\,\phi(e_3,e_1,e_2) + ceg\,\phi(e_3,e_2,e_1).
\end{aligned}
$$

Each $$\phi$$ on the right is $$\pm\phi(e_1,e_2,e_3)$$, the sign depending on
how many swaps it takes to sort the arguments. Collecting,

$$
\begin{aligned}
&\phi\begin{pmatrix} a & d & g \\ b & e & h \\ c & f & j \end{pmatrix} \\
&\quad = (aej + bfg + cdh \\
&\quad\qquad - afh - bdj - ceg)\ \phi(I_3).
\end{aligned}
$$

Those six terms are exactly the criterion
[Unit 4](/posts/calculus-1-coordinates-vectors/) produced for three vectors in
$$\mathbb{R}^3$$ to be dependent, with $$j$$ written where Unit 4 wrote $$i$$
— the letter $$i$$ is wanted for a unit vector in Part 3. The expression that
looked like a curiosity there is the value of the unique 3-form here.

### The 4-form, and a worry

For $$\mathcal{M}_{4\times4}$$ the expansion has $$4^4$$ terms and $$4! = 24$$
survive. Writing them all out is hopeless; one is enough to see the issue:

$$
\cdots + a_{41}a_{22}a_{13}a_{34}\ \phi(e_4,e_2,e_1,e_3) + \cdots
$$

To collect this with the rest, $$\phi(e_4,e_2,e_1,e_3)$$ has to be turned into
$$\pm\,\phi(e_1,e_2,e_3,e_4)$$. Two swaps do it:

$$
\begin{aligned}
(4,2,1,3) \ &\xrightarrow{\,(1,4)\,} \ (1,2,4,3) \\
 &\xrightarrow{\,(3,4)\,} \ (1,2,3,4),
\end{aligned}
$$

so the sign is $$(-1)^2 = +1$$ and the term contributes
$$+\,a_{41}a_{22}a_{13}a_{34}\,\phi(I_4)$$.

But there are infinitely many routes from $$(4,2,1,3)$$ to $$(1,2,3,4)$$. Might
one of them use five swaps, and give the opposite sign? If so the whole
construction is incoherent. The worry is a reasonable one, and the next
subsection disposes of it.

### Permutations and sign

**Definition 2.3.**

1. A function $$\sigma$$ is an **$$n$$-permutation** (치환) if
   $$\sigma : \{1, 2, \ldots, n\} \to \{1, 2, \ldots, n\}$$ is a bijection.
2. A **transposition** (호환) is a permutation that exchanges two numbers and
   leaves the rest alone.
3. The **identity permutation** (항등치환) is the identity function.

Write a permutation as the list of its values. If $$\sigma(1) = 4$$,
$$\sigma(2) = 2$$, $$\sigma(3) = 1$$, $$\sigma(4) = 3$$, write
$$\sigma = (4,2,1,3)$$. Then

$$
\sigma = (4,2,1,3) \iff \sigma^{-1} = (3,2,4,1),
$$

read off by asking where each value came from. And $$\tau = (3,2,1,4)$$
exchanges $$1$$ and $$3$$ and fixes the rest, so it is a transposition, written
$$\tau = (1,3)$$.

**Theorem 2.4.**

1. Every permutation is a composition of transpositions, and there are
   infinitely many ways to write it as one.
2. The identity permutation cannot be written as a composition of an **odd**
   number of transpositions.
3. No permutation is both a composition of an odd number of transpositions and
   a composition of an even number.

*Proof.* (1) Clear. (2) Not easy. (3) Follows at once from (2). $$\square$$

> The lectures did not pretend part 2 was routine: *as a student I spent more
> than twenty-four hours trying to prove this without looking at a book, and
> failed. I got annoyed and looked it up. I expect nine out of ten of you will
> fail too.* It is offered as an exercise anyway, on the grounds that failing at
> it is a good experience.
{: .prompt-info }

So every permutation is **odd** (홀치환) or **even** (짝치환), never both, and
the **sign** (부호함수) is well defined:

$$
\operatorname{sgn}(\text{even}) = 1, \qquad
\operatorname{sgn}(\text{odd}) = -1 .
$$

That settles the worry in the previous subsection. The sign a term picks up does
not depend on the route taken to sort it.

**Exercises from the notes.**

- What is $$\operatorname{sgn}(3,5,1,2,4)$$?
- Show $$\operatorname{sgn}(\sigma) = \operatorname{sgn}(\sigma^{-1})$$.
- There are $$n!$$ permutations of $$n$$ objects. How many are odd?
- Search for *sliding puzzle*, *fifteen puzzle*, *Sam Loyd*. Find out what
  problem Loyd offered 1,000 dollars for, and why he was sure nobody would
  collect.

> **The fifteen puzzle.** Loyd's prize was for starting from the solved board
> with the 14 and 15 exchanged and sliding it back to order. Every legal move
> swaps the blank square with a neighbouring tile — a transposition — and
> returning the blank to its home square takes an even number of moves, because
> each move changes the colour of its square on a chessboard colouring. So only
> **even** permutations of the tiles are reachable. Exchanging two tiles is a
> single transposition, which is odd. The prize money was never at risk, and
> Theorem 2.4 is the reason.
{: .prompt-tip }

### The definition

**Theorem 2.5.** An alternating multi-linear $$n$$-form
$$\phi : \mathcal{M}_{n\times n} \to \mathbb{R}$$ is unique up to scalar
multiplication:

$$
\begin{aligned}
&\phi\big((a_{ij})_{n \times n}\big) \\
&\quad = \sum_{\sigma} \operatorname{sgn}(\sigma)\,
   a_{\sigma(1)1}a_{\sigma(2)2}\cdots a_{\sigma(n)n}\ \phi(I_n),
\end{aligned}
$$

the sum running over all $$n$$-permutations $$\sigma$$.

**Definition 2.6.** The **determinant** (행렬식) is the alternating multi-linear
$$n$$-form whose value at the identity matrix is $$1$$:

$$
\begin{aligned}
&\det\big((a_{ij})_{n \times n}\big) \\
&\quad = \sum_{\sigma} \operatorname{sgn}(\sigma)\,
   a_{\sigma(1)1}a_{\sigma(2)2}\cdots a_{\sigma(n)n} .
\end{aligned}
$$

It is worth stopping to notice what just happened. The determinant was not
defined by that sum and then shown to be well behaved. Three demands were made
of it — linear in each column, zero on a repeated column, $$1$$ at the identity
— and the uniqueness theorem says exactly one function meets them. The formula
is a consequence, not a definition.

### Properties

**Theorem 2.7.**

1. $$\det(\cdots, v, \cdots, v, \cdots) = 0$$.
2. $$\det(\cdots, v, \cdots, w, \cdots) = -\det(\cdots, w, \cdots, v, \cdots)$$.
3. $$\det(\cdots, v, \cdots, w, \cdots) = \det(\cdots, v, \cdots, w + kv, \cdots)$$.
4. $$\det A^{t} = \det A$$.

*Proof.* 1 is the alternating property and 2 the skew-symmetry, both built in.
For 3, use multi-linearity and then 1:

$$
\begin{aligned}
&\det(\cdots, v, \cdots, w + kv, \cdots) \\
&\quad = \det(\cdots, v, \cdots, w, \cdots) \\
&\quad\quad + k\det(\cdots, v, \cdots, v, \cdots) \\
&\quad = \det(\cdots, v, \cdots, w, \cdots).
\end{aligned}
$$

4 is omitted. $$\square$$

Property 3 is the one that makes determinants computable: adding a multiple of
one column to another changes nothing. Property 4 is the one that makes
everything said about columns true of rows as well, which is why Theorem 1.3
could list both.

### Why nobody computes from the definition

The sum has $$n!$$ terms and each is a product of $$n$$ entries, so evaluating
it costs $$(n-1)\cdot n!$$ multiplications.

Suppose a computer performs $$10^{16}$$ multiplications per second — one 경, ten
quadrillion — and suppose deciding the parity of a permutation and adding are
both free. How long to evaluate a $$50 \times 50$$ determinant from the
definition? Within a day? A year? 12.7 billion years, roughly the age of the
universe? That figure squared? Cubed? Raised to the fourth power?

None of them:

$$
\begin{aligned}
&\frac{49 \times 50!}
 {10^{16} \cdot 3600 \cdot 24 \cdot 365 \cdot (1.27 \times 10^{10})^{4}} \\
&\qquad = 181.66 .
\end{aligned}
$$

The answer is about $$182$$ times $$(12.7\text{ billion})^{4}$$ years.
*Astronomical time, astronomically many times over.* Ignoring the good
algebraic properties of the determinant and grinding out the definition is, in
the lectures' word, very foolish.

> There is a well-known story about a servant who asks a greedy rich man for one
> grain of rice on the first square of a chessboard and double on each square
> after, which is how most people first feel the force of exponential growth.
> The factorial makes the exponential look mild. That, the lectures suggested,
> is presumably why its symbol is an exclamation mark. For anyone who wants the
> rate written down precisely, look up **Stirling's formula**.
{: .prompt-tip }

### How you actually compute

Two facts do all the work.

**Triangular matrices.** The determinant is the product of the diagonal:

$$
\det\begin{pmatrix}
a & * & * & * \\
0 & b & * & * \\
0 & 0 & c & * \\
0 & 0 & 0 & d
\end{pmatrix} = abcd .
$$

**Row operations.** By Theorem 2.7 every matrix can be driven to triangular form
without losing track of the determinant. A common factor pulls out of a row by
multi-linearity, adding a multiple of one row to another changes nothing, and
the answer is read off the diagonal:

$$
\begin{aligned}
\det\begin{pmatrix} 2 & 4 & 6 \\ 1 & 4 & 2 \\ 3 & 5 & 7 \end{pmatrix}
&= 2 \det\begin{pmatrix} 1 & 2 & 3 \\ 1 & 4 & 2 \\ 3 & 5 & 7 \end{pmatrix} \\[2pt]
&= 2 \det\begin{pmatrix} 1 & 2 & 3 \\ 0 & 2 & -1 \\ 0 & -1 & -2 \end{pmatrix} \\[2pt]
&= 2 \det\begin{pmatrix} 1 & 2 & 3 \\ 0 & 2 & -1 \\ 0 & 0 & -5/2 \end{pmatrix} \\[2pt]
&= 2 \cdot 1 \cdot 2 \cdot \left(-\tfrac{5}{2}\right) = -10 .
\end{aligned}
$$

The cost is cubic in $$n$$ rather than factorial, which is the entire difference
between a calculation and a fantasy.

### Multiplicativity

**Theorem 2.8.**

1. $$\det(AB) = \det A \, \det B$$.
2. $$\det(A^{-1}) = \dfrac{1}{\det A}$$.

*Proof.* 1. Fix $$A$$ and write $$B$$ by its columns,
$$B = (b_1, \ldots, b_n)$$. Define

$$
\phi(b_1, \ldots, b_n) := \det AB = \det(Ab_1, \ldots, Ab_n).
$$

Because $$A$$ acts linearly on each column and $$\det$$ is alternating and
multi-linear, so is $$\phi$$. Theorem 2.5 then says
$$\phi = \det(B)\,\phi(I_n)$$, and $$\phi(I_n) = \det A$$.

2. Apply 1 to $$AA^{-1} = I_n$$. $$\square$$

The first statement is the one to remember. The determinant of a composition is
the product of the determinants, which is exactly what a notion of *scaling
factor* ought to do — and Part 3 will say what it is scaling.

**Theorem 2.9.** For a square matrix $$A$$ the following are equivalent.

- $$\det A \ne 0$$.
- $$A$$ is invertible.
- The column vectors of $$A$$ are linearly independent.
- The row vectors of $$A$$ are linearly independent.

> The lectures declined to prove this: *the proof is possible at this stage, but
> it takes a long speech, and I am worried you would be worn out by it. In the
> spirit of keeping mathematics enjoyable, let us skip it and simply memorise
> the result.* Anyone who wants it will find it in Chapter 7 of the textbook,
> where it does not read easily. The recommendation was to take Engineering
> Mathematics (공학수학, required) and Linear Algebra (선형대수, *elective, but
> required!!!*) in the second year.
{: .prompt-info }

Theorem 2.9 is the full answer to the question
[Unit 4](/posts/calculus-1-coordinates-vectors/) closed on. Are $$n$$ vectors in
$$\mathbb{R}^n$$ dependent? Put them in the columns of a matrix and take the
determinant. For $$n = 2$$ that is $$ad - bc$$; for $$n = 3$$ it is the six
terms above; for $$n = 4$$ there are $$24$$ terms and no new idea is needed.

### Off-syllabus: cofactor expansion

The next two results were marked 교과과정 외 — outside the examinable scope.

Grind out the $$3 \times 3$$ determinant and it can be rearranged in more than
one way. Along the first column,

$$
\begin{aligned}
&\det\begin{pmatrix} a & b & c \\ d & e & f \\ g & h & j \end{pmatrix} \\
&\quad = a \det\begin{pmatrix} e & f \\ h & j \end{pmatrix}
 - d \det\begin{pmatrix} b & c \\ h & j \end{pmatrix}
 + g \det\begin{pmatrix} b & c \\ e & f \end{pmatrix},
\end{aligned}
$$

and along the second row,

$$
\begin{aligned}
&\det\begin{pmatrix} a & b & c \\ d & e & f \\ g & h & j \end{pmatrix} \\
&\quad = -d \det\begin{pmatrix} b & c \\ h & j \end{pmatrix}
 + e \det\begin{pmatrix} a & c \\ g & j \end{pmatrix}
 - f \det\begin{pmatrix} a & b \\ g & h \end{pmatrix}.
\end{aligned}
$$

Same number, different route. *Does it not look as though some secret is hidden
here?*

**Definition 2.13.** Delete row $$i$$ and column $$j$$ of a square matrix; the
determinant $$M_{ij}$$ of what remains is the **minor** (소행렬식), and

$$
C_{ij} = (-1)^{i+j}M_{ij}
$$

is the **cofactor** (여인수).

**Theorem 2.14 (Laplace expansion, cofactor expansion).** For an
$$n \times n$$ matrix $$A = (a_{ij})$$, expanding along any row or any column
gives the determinant:

$$
\begin{aligned}
\det A &= \sum_{k=1}^{n}(-1)^{i+k}a_{ik}M_{ik} = \sum_{k=1}^{n}a_{ik}C_{ik} \\
       &= \sum_{k=1}^{n}(-1)^{k+j}a_{kj}M_{kj} = \sum_{k=1}^{n}a_{kj}C_{kj}.
\end{aligned}
$$

*Proof.* It is the defining sum rearranged. $$\square$$

Two warnings came with it.

The first is computational. The formula looks like a method — reduce to
determinants one size smaller, repeat, and eventually arrive. That is true and
it does not help: the astronomical count above does not improve in the
slightest. From a computational point of view cofactor expansion is useless.

The second is about definitions, and it is the sharper of the two. Some books
*define* the determinant by cofactor expansion, as a way around the
alternating-multi-linear-form idea, which beginners may find hard.

> *I once lectured that way myself. I now think it is not a good strategy at
> all. If you meet a book that introduces cofactor expansion as the definition
> of the determinant, you may regard that as a somewhat problematic approach.
> The problem is precisely this: **is it well defined?***
>
> The point is exact. Define $$\det$$ by expansion along the first row and you
> immediately owe a proof that expanding along the third column gives the same
> number — which is Theorem 2.14, now load-bearing rather than incidental.
> Define it as the unique form with three properties and you owe nothing of the
> kind.
{: .prompt-warning }

### Off-syllabus: the inverse formula

**Theorem 2.15.** For $$A = (a_{ij})_{n\times n}$$ with cofactors $$C_{ij}$$,

$$
A^{-1} = \frac{1}{\det A}\left(C_{ij}\right)^{t} .
$$

Engineering mathematics textbooks label this the *useful formula*. The lectures
instructed students to cross that out and write **almost useless formula**: it
is unusable for anything but the smallest sizes, which is the promise made back
in Theorem 1.3's aftermath, now kept.

For $$3 \times 3$$, with the transpose already taken,

$$
\begin{aligned}
&\begin{pmatrix} a & b & c \\ d & e & f \\ g & h & j \end{pmatrix}^{-1} \\
&\quad = \frac{1}{\det A}
\begin{pmatrix}
C_{11} & C_{21} & C_{31} \\
C_{12} & C_{22} & C_{32} \\
C_{13} & C_{23} & C_{33}
\end{pmatrix},
\end{aligned}
$$

where

$$
\begin{aligned}
C_{11} &= ej - fh, & C_{21} &= -(bj - ch), \\
C_{12} &= -(dj - fg), & C_{22} &= aj - cg, \\
C_{13} &= dh - eg, & C_{23} &= -(ah - bg), \\
C_{31} &= bf - ce, & C_{32} &= -(af - cd), \\
C_{33} &= ae - bd. & &
\end{aligned}
$$

Where it does earn its keep is on small matrices whose entries are *functions*
rather than numbers, since there is nothing to compute numerically and the
pattern is all you have. The notes close on exactly such a matrix, the one
attached to the spherical coordinates of
[Unit 4](/posts/calculus-1-coordinates-vectors/):

$$
\begin{cases}
x = \rho \sin\varphi \cos\theta \\
y = \rho \sin\varphi \sin\theta \\
z = \rho \cos\varphi
\end{cases}
$$

$$
\begin{aligned}
&\frac{\partial(x,y,z)}{\partial(\rho,\varphi,\theta)} \\
&= \begin{pmatrix}
\sin\varphi\cos\theta & \rho\cos\varphi\cos\theta & -\rho\sin\varphi\sin\theta \\
\sin\varphi\sin\theta & \rho\cos\varphi\sin\theta & \rho\sin\varphi\cos\theta \\
\cos\varphi & -\rho\sin\varphi & 0
\end{pmatrix}.
\end{aligned}
$$

This is the **Jacobian matrix**, and it belongs to Mathematics 2. The lectures'
advice was not to worry about it yet — but it is worth seeing once, because it
is the point at which the determinant stops being linear algebra and becomes the
thing that makes a change of variables work under an integral sign.

---

## Part 3 — §8.1: the cross product is a determinant

[Unit 4](/posts/calculus-1-coordinates-vectors/) already defined the cross
product and listed its properties; the lectures declined to wait for Chapter 8
on the grounds that everyone had met it at school. What Chapter 8 adds is the
reason it looks the way it does.

### The determinant form

**Definition 1.1** is Unit 4's componentwise definition again, for
$$a = (a_1,a_2,a_3)$$ and $$b = (b_1,b_2,b_3)$$. Written in terms of the
standard unit vectors it reads

$$
\begin{aligned}
a \times b &= (a_2b_3 - a_3b_2)\,i \\
&\quad + (a_3b_1 - a_1b_3)\,j \\
&\quad + (a_1b_2 - a_2b_1)\,k ,
\end{aligned}
$$

which is exactly

$$
a \times b =
\begin{vmatrix}
i & j & k \\
a_1 & a_2 & a_3 \\
b_1 & b_2 & b_3
\end{vmatrix}.
$$

The top row holds vectors rather than numbers, so this is not literally a
determinant. Expand it by cofactors along that row anyway and the three
components drop out in order. It is the standard mnemonic, and after Chapter 7
it is more than a mnemonic — every property Unit 4 listed is a determinant
property wearing different clothes.

- $$a \times b = -\,b \times a$$ is Theorem 2.7(2): exchanging $$a$$ and $$b$$
  exchanges two rows.
- $$(a \times b)\cdot a = 0$$ and $$(a \times b)\cdot b = 0$$ are
  Theorem 2.7(1): by the triple product below, each puts the same vector into
  two rows at once.
- Bilinearity is multi-linearity.

The remaining two properties — that
$$\lvert a \times b \rvert = \lvert a \rvert \lvert b \rvert \sin\theta$$ is
the area of the parallelogram, and that $$a, b, a\times b$$ are positively
oriented — are the ones that will turn into the geometry of the determinant
itself.

### The triple product

$$
a \cdot (b \times c) = (a \times b)\cdot c = \det(a,b,c).
$$

> On proving it the lectures were brisk: *the comfortable thing is simply to
> grind it out. It is not especially complicated, and there is no need to spend
> time and passion coming up with a nice idea. But if you insist on pretending
> to have one — the formula tells you what the value of a determinant means.*
{: .prompt-info }

That last clause is the whole point of the section. Up to here the determinant
has been algebra: the unique alternating multi-linear form, the number that is
non-zero exactly when a matrix is invertible. The triple product hands it a
geometric meaning.

### What a determinant means

For $$a, b, c \in \mathbb{R}^3$$:

- $$\det(a,b,c) \ne 0 \iff a, b, c$$ are linearly independent.
- $$\det(a,b,c) > 0 \iff a, b, c$$ are positively oriented.
- $$\lvert \det(a,b,c) \rvert$$ is the volume of the parallelepiped
  (평행육면체) spanned by $$a$$, $$b$$ and $$c$$.

The third is the triple product read as base times height. By property 4 of
Unit 4, $$\lvert b \times c \rvert$$ is the area of the parallelogram on $$b$$
and $$c$$; by property 3, $$b \times c$$ is perpendicular to it. So in
$$\lvert a \cdot (b \times c)\rvert$$ the inner product picks out exactly the
component of $$a$$ standing above that base — the height — and multiplies the
two together.

Three statements, and between them the whole unit closes:

- **Independence** was Unit 4's unanswered question, and Theorem 2.9 answers it
  in every dimension.
- **Orientation** is the sign that the skew-symmetry was tracking all along.
- **Volume** is what $$\det(AB) = \det A \det B$$ was measuring all along. A
  linear map scales volume by its determinant, and composing two maps
  multiplies the two factors.

In $$\mathbb{R}^n$$ the same reading holds — $$\lvert \det \rvert$$ is the
volume of the $$n$$-dimensional parallelepiped on the columns — which is why
dependence and vanishing determinant are the same statement. Flat bodies have
no volume.

### Distance from a point to a line

The cross product measures a perpendicular component, so it measures distances
to lines, just as the inner product measured distances to hyperplanes in Unit 4.

For the line $$X(t) = P + tv$$ in $$\mathbb{R}^3$$ and a point $$Q$$, the
distance is

$$
\left\lvert \overrightarrow{PQ} \times \frac{v}{\lvert v \rvert} \right\rvert
= \left\lvert (Q - P) \times \frac{v}{\lvert v \rvert} \right\rvert .
$$

Crossing with a **unit** vector multiplies length by $$\sin\theta$$, and
$$\lvert \overrightarrow{PQ}\rvert \sin\theta$$ is precisely the perpendicular
drop from $$Q$$ to the line.

For the line through two points $$A$$ and $$B$$,

$$
\begin{aligned}
&\left\lvert \overrightarrow{AQ} \times \frac{A - B}{\lvert A - B \rvert}\right\rvert \\
&\quad = \frac{\lvert (Q-A) \times (A-B) \rvert}{\lvert A - B \rvert} \\
&\quad = \frac{\lvert (Q-A) \times (Q-B) \rvert}{\lvert A - B \rvert}.
\end{aligned}
$$

The last equality looks like a slip and is not. Since
$$Q - B = (Q - A) + (A - B)$$, bilinearity splits the cross product into
$$(Q-A)\times(Q-A)$$, which vanishes, plus $$(Q-A)\times(A-B)$$. The symmetric
form on the right is usually the easier one to use, since both vectors run from
a point of the line to $$Q$$ and neither needs the direction vector computed
first.

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
- **Getting the inverse of a product backwards.** $$(AB)^{-1} = B^{-1}A^{-1}$$,
  the same reversal as the transpose and for the same reason.
- **Writing $$\det(A + B) = \det A + \det B$$.** The determinant is linear in
  each column *separately*, which is a different and much weaker statement. It
  is multiplicative, not additive.
- **Mishandling a scalar multiple.** Pulling $$k$$ out of *one* column gives a
  factor $$k$$; pulling it out of an $$n \times n$$ matrix gives
  $$\det(kA) = k^n \det A$$.
- **Treating the cofactor formulas as calculation methods.** Both Theorem 2.14
  and Theorem 2.15 are structural facts. Row-reduce instead.
- **Mixing up the two off-diagonal cofactors.** The transpose in
  $$A^{-1} = \frac{1}{\det A}(C_{ij})^{t}$$ is easy to drop, and dropping it
  gives a wrong answer that still looks plausible.
- **Reading the $$i, j, k$$ determinant too literally.** It is a mnemonic whose
  first row is not made of numbers. Everything else about it is honest, but the
  object itself is not a matrix over $$\mathbb{R}$$.
- **Forgetting to normalise in the distance formula.** It is
  $$v / \lvert v \rvert$$, not $$v$$. With $$v$$ unnormalised the answer is the
  distance times $$\lvert v \rvert$$.

## Connections

- **Backward.** The projection and the cross product come from
  [Unit 4](/posts/calculus-1-coordinates-vectors/) and reappear here as
  matrices, which is a fair summary of what Chapter 6 does to the previous
  chapter. Unit 4's dependence criteria — $$ad - bc$$ for two vectors, six
  terms for three — are the $$2$$- and $$3$$-forms of Part 2, and its unanswered
  question about four vectors in $$\mathbb{R}^4$$ is answered by Theorem 2.9.
- **Within the unit.** Part 1 asks what the matrix product is for and finds
  composition; Part 2 asks when a composition can be undone and finds the
  determinant; Part 3 asks what the determinant *is* and finds signed volume.
  Each answer is forced rather than chosen, which is the characteristic shape of
  this material.
- **Forward.** The Jacobian that closes Chapter 7 is a determinant measuring how
  a change of coordinates scales volume, and it is the engine of multivariable
  integration in Mathematics 2. Nearer at hand, the cross product in determinant
  form is what [Unit 6](/posts/calculus-1-curves/) needs for the moving frame of
  a space curve, and curvature and torsion in
  [Unit 7](/posts/calculus-1-line-integrals-curvature/) are built from it.
- **Outward.** That rotation matrices compose to give the angle addition
  formulas is the first case of a general principle: a group of symmetries
  becomes a set of matrices, and composing symmetries becomes multiplying them.
  Determinant $$1$$ picks out the rotations among them, and the sign of the
  determinant is what distinguishes a rotation from a reflection.

## Summary

**Part 1 — matrices and linear maps**

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

**Part 2 — inverses and the determinant**

- **Inverse** — $$AB = BA = I_n$$; and $$AB = I_n$$ alone already forces it
- **Order reverses** — $$(AB)^{-1} = B^{-1}A^{-1}$$
- **2×2 inverse** — $$\frac{1}{ad-bc}\begin{pmatrix} d & -b \\ -c & a\end{pmatrix}$$, when $$ad - bc \ne 0$$
- **Three demands** — multi-linear, alternating, $$1$$ at $$I_n$$ — determine $$\det$$ uniquely
- **Definition** — $$\det A = \sum_\sigma \operatorname{sgn}(\sigma)\,a_{\sigma(1)1}\cdots a_{\sigma(n)n}$$
- **Sign** — every permutation is odd or even, never both (Theorem 2.4)
- **Properties** — repeated column gives $$0$$; swapping flips the sign; adding a multiple of a column changes nothing; $$\det A^{t} = \det A$$
- **Multiplicative** — $$\det AB = \det A \det B$$, so $$\det A^{-1} = 1/\det A$$
- **Invertible** $$\iff \det A \ne 0 \iff$$ columns independent $$\iff$$ rows independent
- **Computation** — row-reduce to triangular and multiply the diagonal; never the definition
- **Off-syllabus** — cofactor expansion and $$A^{-1} = \frac{1}{\det A}(C_{ij})^{t}$$, both structural rather than practical

**Part 3 — the cross product**

- **Determinant form** — $$a \times b$$ is the formal determinant with rows $$(i,j,k)$$, $$a$$, $$b$$
- **Triple product** — $$a \cdot (b \times c) = (a \times b) \cdot c = \det(a,b,c)$$
- **Geometry** — $$\det \ne 0$$ is independence, $$\det > 0$$ is positive orientation, $$\lvert \det \rvert$$ is volume
- **Distance to a line** — $$\lvert \overrightarrow{PQ} \times v/\lvert v \rvert \rvert$$

## References

- Hong Jong Kim, *Calculus 1+* (미적분학 1+), 2nd revised edition, Seoul National University Press — Chapters 6, 7 and §8.1.
- Mathematics 1 (수학 1, L0442.000100), Seoul National University, Spring 2022. Instructor: Choi Hyung Gyu (최형규). Lecture notes for Chapter 6 dated 24 April 2022; Chapters 7 and 8 dated 28 April 2022.
- The rotation example in Part 1 is from the handwritten additions to those notes; the printed text ends at the cross-product matrix.
- Inverses by elementary row operations and Gauss–Jordan elimination were explicitly left outside the first-year syllabus.
- Cofactor expansion (Theorems 2.13–2.14) and the inverse formula (Theorem 2.15) were marked 교과과정 외, outside the examinable scope. §7.4.2, on properties of the determinant, was the one appendix the course did examine.
- The fifteen-puzzle argument in the sidebar is the standard parity solution to the exercise the notes set; the notes posed the question and left the answer to the reader.
