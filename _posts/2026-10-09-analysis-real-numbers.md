---
title: "Mathematical Analysis: The Real Numbers"
date: 2026-10-09 08:30:00 +0900
categories: [Course Notes, Mathematical Analysis]
tags: [completeness, supremum, induction, countability, cantor diagonal]
description: Sets and functions, induction, the field and order axioms, and the one axiom that separates the reals from the rationals — the least upper bound property — followed by the Archimedean property, density, and Cantor's uncountability argument. Chapter 1 of Introduction to Mathematical Analysis.
math: true
mermaid: false
render_with_liquid: false
---

> This chapter covers §§1.1–1.5 and §1.7. §1.6, on binary and ternary
> expansions, was not covered; the ternary expansions reappear in
> [Chapter 2](/posts/analysis-metric-spaces/) with the Cantor set.
{: .prompt-info }

## What this chapter answers

The whole chapter turns on one question: **what is wrong with the rational
numbers?**

Nothing algebraic. $$\mathbb{Q}$$ has addition, subtraction, multiplication and
division; it is ordered compatibly with those operations; and it is dense in
itself, so between any two rationals there is another. By every structural test
in §§1.1–1.4 it looks complete.

And yet there is no rational number whose square is $$2$$. A perfectly good
length — the diagonal of a unit square — has no name in $$\mathbb{Q}$$. The
rationals have holes, and the holes are invisible to algebra and to order.

So the chapter builds the apparatus to *see* the holes, and then adds the one
axiom that fills them. The apparatus is the supremum; the axiom is the **least
upper bound property**. Everything after §1.4 in this course, in every chapter,
is a consequence.

## Prerequisites

None beyond school algebra and a willingness to treat familiar objects as
unfamiliar. The chapter is written as though $$\mathbb{R}$$ had never been met.

---

## §1.1 Sets and operations on sets

### The motivating fact

**Theorem.** There is no $$r \in \mathbb{Q}$$ with $$r^2 = 2$$.

*Proof.* Suppose $$r = p/q$$ with $$p, q \in \mathbb{Z}$$, $$q \ne 0$$, and the
fraction in lowest terms, so $$p$$ and $$q$$ are not both even. From
$$p^2 = 2q^2$$, $$p^2$$ is even, hence $$p$$ is even — if $$p$$ were odd then
$$p^2$$ would be odd. Write $$p = 2k$$. Then $$4k^2 = 2q^2$$, so
$$q^2 = 2k^2$$ and by the same argument $$q$$ is even. Both are even,
contradicting lowest terms. $$\square$$

The step worth noticing is "$$p^2$$ even $$\Rightarrow$$ $$p$$ even", which is
the contrapositive of "odd times odd is odd". Everything else is bookkeeping.

> The notes record that the gap this exposes was closed only in the 1870s, by
> **Dedekind** and **Cantor** — two different constructions of $$\mathbb{R}$$
> from $$\mathbb{Q}$$, by cuts and by Cauchy sequences respectively. This
> course takes neither route. It *axiomatises* $$\mathbb{R}$$ instead: assume a
> complete ordered field exists and work from the axioms. That is the standard
> trade. Constructing $$\mathbb{R}$$ is a worthwhile term's work that teaches
> almost nothing about analysis.
{: .prompt-tip }

### Operations

For sets $$A$$ and $$B$$:

$$
\begin{aligned}
A \cup B &= \{x : x \in A \text{ or } x \in B\} \\
A \cap B &= \{x : x \in A \text{ and } x \in B\} \\
A \setminus B &= \{x : x \in A \text{ and } x \notin B\} \\
A^{c} &= \{x : x \notin A\}
\end{aligned}
$$

$$A$$ and $$B$$ are **disjoint** when $$A \cap B = \varnothing$$. The
complement $$A^{c}$$ is relative to an understood universal set; $$A \setminus B$$
is the **relative complement**, and is the safer notation because it names the
set it is relative to.

**Theorem (distributive and De Morgan laws).**

$$
\begin{aligned}
\text{(a)}\quad A \cap (B \cup C) &= (A \cap B) \cup (A \cap C) \\
\text{(b)}\quad A \cup (B \cap C) &= (A \cup B) \cap (A \cup C) \\
\text{(c)}\quad A \setminus (B \cap C) &= (A \setminus B) \cup (A \setminus C) \\
\text{(d)}\quad A \setminus (B \cup C) &= (A \setminus B) \cap (A \setminus C)
\end{aligned}
$$

*Proof of (d), as the pattern.* Set equality is two inclusions, and each
inclusion is a chase through the definitions.

$$
\begin{aligned}
x \in A \setminus (B \cup C)
 &\iff x \in A \text{ and } x \notin B \cup C \\
 &\iff x \in A,\ x \notin B,\ x \notin C \\
 &\iff (x \in A,\ x \notin B) \text{ and } (x \in A,\ x \notin C) \\
 &\iff x \in (A\setminus B) \cap (A \setminus C).
\end{aligned}
$$

Every step is an equivalence, so the two inclusions come at once. (a), (b) and
(c) go the same way. $$\square$$

These are not interesting facts, but the proof style is the point: **a set
identity is a statement about logical connectives in disguise.** "Union" is
"or", "intersection" is "and", "complement" is "not", and De Morgan for sets is
De Morgan for logic.

### Power sets and products

$$
\begin{aligned}
\mathcal{P}(A) &= \{X : X \subseteq A\} \\
A \times B &= \{(a,b) : a \in A,\ b \in B\}
\end{aligned}
$$

The elements of $$A \times B$$ are **ordered pairs**: $$(a,b) = (a',b')$$
exactly when $$a = a'$$ and $$b = b'$$. So
$$\mathbb{R}^2 = \mathbb{R} \times \mathbb{R} = \{(x,y) : x, y \in \mathbb{R}\}$$,
and the plane is a set-theoretic construction rather than a picture.

---

## §1.2 Functions

### A function is a set

**Definition.** Let $$A$$ and $$B$$ be sets. A **function** $$f$$ from $$A$$ to
$$B$$ is a subset of $$A \times B$$ such that each $$x \in A$$ is the first
component of *precisely one* ordered pair in $$f$$. In two clauses:

1. $$\forall x \in A$$, $$\exists y \in B$$ with $$(x,y) \in f$$ — every input
   gets an output;
2. $$(x,y) \in f$$ and $$(x,y') \in f$$ $$\Rightarrow$$ $$y = y'$$ — the output
   is unique.

Then $$\operatorname{Dom} f = A$$ and

$$
\operatorname{Range} f = \{y \in B : (x,y) \in f \text{ for some } x \in A\},
$$

and $$f$$ is **onto** $$B$$ when $$\operatorname{Range} f = B$$.

> Defining a function as a set of pairs rather than as a rule looks like
> pedantry and is not. A *rule* is an informal notion — is "the least $$n$$
> such that…" a rule? — whereas a set of pairs is an object you can quantify
> over, take subsets of, and count. Chapter 8's sequences *of functions* are
> only possible because a function is a thing.
{: .prompt-tip }

### Images and inverse images

**Definition.** For $$E \subseteq A$$, the **image**
$$f(E) = \{f(x) : x \in E\}$$. For $$H \subseteq B$$, the **inverse image**
$$f^{-1}(H) = \{x \in A : f(x) \in H\}$$.

The notation $$f^{-1}$$ here does **not** presuppose that $$f$$ has an inverse.
It is defined for every function, and it takes subsets to subsets.

**Theorem (images).** For $$A_1, A_2 \subseteq A$$,

$$
\begin{aligned}
f(A_1 \cup A_2) &= f(A_1) \cup f(A_2), \\
f(A_1 \cap A_2) &\subseteq f(A_1) \cap f(A_2).
\end{aligned}
$$

*Proof.* For the union: $$y \in f(A_1 \cup A_2)$$ means $$y = f(x)$$ for some
$$x$$ in $$A_1$$ or in $$A_2$$, which is exactly $$y \in f(A_1)$$ or
$$y \in f(A_2)$$.

For the intersection, only one direction survives. If $$y \in f(A_1 \cap A_2)$$
then $$y = f(x)$$ for some $$x$$ in both, so $$y$$ is in both images. The
converse fails: $$y \in f(A_1) \cap f(A_2)$$ gives $$y = f(x_1) = f(x_2)$$ with
$$x_1 \in A_1$$ and $$x_2 \in A_2$$, and **nothing forces $$x_1 = x_2$$.**
$$\square$$

**The counterexample.** Take $$f(x) = x^2$$ on $$\mathbb{R}$$ with
$$A_1 = \{1\}$$ and $$A_2 = \{-1\}$$. Then $$A_1 \cap A_2 = \varnothing$$, so
$$f(A_1 \cap A_2) = \varnothing$$, while
$$f(A_1) \cap f(A_2) = \{1\}$$. The inclusion is strict.

**Theorem (inverse images).** For $$B_1, B_2 \subseteq B$$,

$$
\begin{aligned}
f^{-1}(B_1 \cup B_2) &= f^{-1}(B_1) \cup f^{-1}(B_2), \\
f^{-1}(B_1 \cap B_2) &= f^{-1}(B_1) \cap f^{-1}(B_2), \\
f^{-1}(B \setminus B_1) &= A \setminus f^{-1}(B_1).
\end{aligned}
$$

*Proof of the second, as the pattern.*

$$
\begin{aligned}
x \in f^{-1}(B_1 \cap B_2)
 &\iff f(x) \in B_1 \cap B_2 \\
 &\iff f(x) \in B_1 \text{ and } f(x) \in B_2 \\
 &\iff x \in f^{-1}(B_1) \cap f^{-1}(B_2).
\end{aligned}
$$

The other two are identical with "or" and "not" in place of "and".
$$\square$$

> **The one thing to remember from §1.2.** Inverse images commute with
> *everything* — unions, intersections, complements — and images commute only
> with unions. The reason is visible in the proofs: $$x \in f^{-1}(H)$$ is a
> condition on the single value $$f(x)$$, so the logical connective passes
> straight through, whereas $$y \in f(E)$$ asserts the existence of some
> preimage, and existential quantifiers do not commute with "and".
>
> This asymmetry is why continuity is defined in
> [Chapter 4](/posts/analysis-continuity/) by inverse images of open sets and
> not by images. The definition that works is the one built on the operation
> that behaves.
{: .prompt-warning }

### Injections, inverses, composition

**Definition.** $$f$$ is **one-to-one** when $$x_1 \ne x_2$$ implies
$$f(x_1) \ne f(x_2)$$.

**Definition.** If $$f$$ is one-to-one from $$A$$ **onto** $$B$$, its
**inverse function** is

$$
f^{-1} = \{(y,x) \in B \times A : f(x) = y\},
$$

so that for every $$y \in B$$, $$x = f^{-1}(y)$$ if and only if $$y = f(x)$$.
Both hypotheses are needed: one-to-one makes $$f^{-1}$$ single-valued, and onto
makes it defined on all of $$B$$.

**Definition.** For $$f : A \to B$$ and $$g : B \to C$$, the **composition**

$$
g \circ f = \{(x,z) \in A \times C : z = g(f(x))\}.
$$

---

## §1.3 Mathematical induction

### The principle, and what it rests on

**Theorem (Principle of Mathematical Induction).** For each $$n \in \mathbb{N}$$
let $$P(n)$$ be a statement. If

1. $$P(1)$$ is true, and
2. $$P(n+1)$$ is true whenever $$P(n)$$ is true,

then $$P(n)$$ is true for every $$n \in \mathbb{N}$$.

Induction is not an axiom here. It is a theorem, and what it rests on is:

**Well-Ordering Principle.** Every nonempty subset of $$\mathbb{N}$$ has a
smallest element: if $$A \subseteq \mathbb{N}$$ and $$A \ne \varnothing$$, then
$$\exists k \in A$$ with $$k \le n$$ for all $$n \in A$$.

*Proof of induction from well-ordering.* Let
$$S = \{n \in \mathbb{N} : P(n) \text{ is false}\}$$ and suppose
$$S \ne \varnothing$$. By well-ordering $$S$$ has a least element $$k$$. Now
$$k \ne 1$$, since $$P(1)$$ holds by (1). So $$k - 1 \in \mathbb{N}$$, and
$$k-1 \notin S$$ by minimality, so $$P(k-1)$$ is true — whence $$P(k)$$ is true
by (2). That contradicts $$k \in S$$. Hence $$S = \varnothing$$. $$\square$$

The move is worth keeping: **to prove something holds for all $$n$$, consider
the least $$n$$ for which it fails and derive a contradiction.** The
least-counterexample argument and induction are the same argument.

### Bernoulli's inequality

**Theorem.** For every $$n \in \mathbb{N}$$ and every $$h \ge -1$$,

$$
(1+h)^n \ge 1 + nh .
$$

*Proof.* True at $$n=1$$ with equality. Assuming it at $$n$$, and using
$$1 + h \ge 0$$ so that multiplying preserves the inequality,

$$
\begin{aligned}
(1+h)^{n+1} &= (1+h)^n(1+h) \\
 &\ge (1+nh)(1+h) \\
 &= 1 + (n+1)h + nh^2 \\
 &\ge 1 + (n+1)h ,
\end{aligned}
$$

the last step because $$nh^2 \ge 0$$. $$\square$$

Discarding $$nh^2$$ is the whole trick, and it is the trick in most inequality
proofs in this course: throw away a term you can sign, and keep the bound you
wanted.

> The notes state Bernoulli without the hypothesis $$h \ge -1$$. It is needed:
> at $$h = -3$$ and $$n = 2$$ the claim reads $$4 \ge -5$$, which is fine, but
> the induction step multiplies by $$1+h$$ and reverses when $$1 + h < 0$$.
> The inequality does still hold for all real $$h$$ when $$n$$ is even, and
> fails for odd $$n$$; the clean statement is the one above.
{: .prompt-warning }

### Two variants

**Modified induction.** Starting from any $$n_0 \in \mathbb{Z}$$: if
$$P(n_0)$$ is true and $$P(k+1)$$ is true whenever $$P(k)$$ is true for
$$k \ge n_0$$, then $$P(n)$$ is true for all integers $$n \ge n_0$$.

**Theorem (Second Principle of Induction).** If $$P(1)$$ is true, and for each
$$k > 1$$, $$P(k)$$ is true whenever $$P(j)$$ is true for *all* $$j < k$$, then
$$P(n)$$ is true for every $$n$$.

*Proof.* Identical to the first: take the least $$k$$ with $$P(k)$$ false; then
every $$j < k$$ has $$P(j)$$ true, so the hypothesis gives $$P(k)$$ true, a
contradiction. $$\square$$

Strong induction is what you need whenever $$P(k)$$ depends on a predecessor
you cannot name in advance — the existence of a prime factorisation is the
standard case, since the two factors of $$k$$ are not $$k-1$$.

---

## §1.4 The completeness axiom

This is the centre of the chapter and of the course.

### Fields

**Definition.** A **field** is a set $$F$$ with two operations $$+$$ and
$$\cdot$$ satisfying, for all $$a,b,c \in F$$:

1. $$a + b \in F$$ and $$a \cdot b \in F$$ (closure)
2. $$a+b = b+a$$ and $$a \cdot b = b \cdot a$$ (commutativity)
3. $$(a+b)+c = a+(b+c)$$ and $$(ab)c = a(bc)$$ (associativity)
4. $$\exists\, 0 \in F$$ with $$a + 0 = a$$
5. $$\exists\, 1 \in F$$, $$1 \ne 0$$, with $$a \cdot 1 = a$$
6. $$\forall a$$, $$\exists -a$$ with $$a + (-a) = 0$$
7. $$\forall a \ne 0$$, $$\exists a^{-1}$$ with $$a \cdot a^{-1} = 1$$
8. $$a(b+c) = ab + ac$$ (distributivity)

The notes ask which of the familiar sets are fields. The answers:

- $$\mathbb{N}$$ — **no.** No $$0$$, and no additive inverses.
- $$\mathbb{Z}$$ — **no.** Axiom 7 fails: $$2$$ has no integer reciprocal.
- $$\mathbb{Q}$$ — **yes.**
- $$\mathbb{R}$$ — **yes.**
- $$\mathbb{C}$$ — **yes**, and this is the one to keep in mind, because
  $$\mathbb{C}$$ is a field that *cannot* be ordered. It shows that the field
  axioms and the order axioms are genuinely independent.

### Ordered fields

**Definition.** An **ordered field** is a field $$F$$ containing a subset
$$P$$ (the *positive* elements) with

- **(O1)** $$a, b \in P$$ $$\Rightarrow$$ $$a + b \in P$$ and $$ab \in P$$;
- **(O2)** for each $$a \in F$$, exactly one of $$a \in P$$, $$-a \in P$$,
  $$a = 0$$ holds (trichotomy).

Write $$a > b$$ for $$a - b \in P$$. Everything you expect then follows.

**Theorem.** In an ordered field:

$$
\begin{aligned}
\text{(a)}\ & a > b \Rightarrow a + c > b + c \\
\text{(b)}\ & a > b,\ c > 0 \Rightarrow ac > bc \\
\text{(c)}\ & a > b,\ c < 0 \Rightarrow ac < bc \\
\text{(d)}\ & a \ne 0 \Rightarrow a^2 > 0 \\
\text{(e)}\ & a > 0 \Rightarrow \tfrac1a > 0; \quad a < 0 \Rightarrow \tfrac1a < 0
\end{aligned}
$$

*Proof of (d), the one that matters.* If $$a \ne 0$$ then by (O2) either
$$a \in P$$ or $$-a \in P$$. In the first case $$a^2 = a \cdot a \in P$$ by
(O1). In the second, $$(-a)(-a) \in P$$, and $$(-a)(-a) = a^2$$, so again
$$a^2 \in P$$. $$\square$$

Part (d) is why $$\mathbb{C}$$ is not an ordered field: it would force
$$i^2 = -1 > 0$$ and $$1 = 1^2 > 0$$ simultaneously, contradicting trichotomy.
The remaining parts are the same kind of two-line argument from (O1) and (O2).

### Bounds, maxima, suprema

Let $$E \subseteq \mathbb{R}$$.

- $$E$$ is **bounded above** if some $$\beta \in \mathbb{R}$$ has
  $$x \le \beta$$ for all $$x \in E$$; such a $$\beta$$ is an **upper bound**.
- **Bounded below** and **lower bound** are the mirror image.
- $$E$$ is **bounded** if both.
- $$\alpha$$ is the **maximum** of $$E$$ if $$\alpha \in E$$ and
  $$x \le \alpha$$ for all $$x \in E$$.

**Definition (supremum).** $$\alpha \in \mathbb{R}$$ is the **supremum**, or
**least upper bound**, of $$E$$ when

1. $$\alpha$$ is an upper bound of $$E$$, and
2. $$\alpha \le \beta$$ for every upper bound $$\beta$$ of $$E$$.

The **infimum** (greatest lower bound) is the mirror image.

The difference between maximum and supremum is the whole reason the word
exists. A maximum must belong to the set; a supremum need not. The set
$$(0,1)$$ has no maximum and has supremum $$1$$. When a maximum does exist it
*is* the supremum.

**Theorem.** The supremum of a set is unique.

*Proof.* If $$\alpha$$ and $$\alpha'$$ are both least upper bounds, then each is
an upper bound, so clause 2 applied to each gives $$\alpha \le \alpha'$$ and
$$\alpha' \le \alpha$$. $$\square$$

The same two lines give uniqueness of the infimum. "The least element of a set
of bounds" is unique for the same reason the least element of anything is.

### The working characterisation

**Theorem.** Let $$A \ne \varnothing$$ be bounded above and let $$\alpha$$ be an
upper bound of $$A$$. Then

$$
\begin{aligned}
\alpha = \sup A \iff\ &\forall \beta < \alpha,\ \exists x \in A \\
 &\text{with } \beta < x \le \alpha .
\end{aligned}
$$

*Proof.* ($$\Rightarrow$$) Let $$\beta < \alpha$$. If no $$x \in A$$ exceeded
$$\beta$$, then $$\beta$$ would be an upper bound smaller than $$\alpha$$,
contradicting leastness. So some $$x \in A$$ has $$x > \beta$$, and
$$x \le \alpha$$ because $$\alpha$$ bounds $$A$$.

($$\Leftarrow$$) Let $$\beta$$ be any upper bound of $$A$$. If $$\beta < \alpha$$
the hypothesis produces $$x \in A$$ with $$x > \beta$$, contradicting that
$$\beta$$ bounds $$A$$. So $$\beta \ge \alpha$$, and $$\alpha$$ is least.
$$\square$$

> **This is the theorem you will actually use.** In practice nobody verifies
> "least among upper bounds" directly. The usable form is: *nothing below
> $$\alpha$$ is an upper bound*, i.e. for every $$\varepsilon > 0$$ there is an
> $$x \in A$$ with $$x > \alpha - \varepsilon$$. Taking $$\beta = \alpha - \varepsilon$$
> turns the theorem into exactly that, and it is the step that starts half the
> proofs in the next four chapters.
{: .prompt-tip }

### The axiom

**The Least Upper Bound Property (완비성공리).** *Every nonempty subset of
$$\mathbb{R}$$ that is bounded above has a supremum in $$\mathbb{R}$$.*

That is the axiom. It is what $$\mathbb{Q}$$ lacks: the set
$$\{x \in \mathbb{Q} : x^2 < 2\}$$ is nonempty and bounded above in
$$\mathbb{Q}$$ and has no rational least upper bound, because any candidate can
be nudged. $$\mathbb{R}$$ is, by definition, a complete ordered field.

Equivalently, as the notes put it: for nonempty $$S$$ bounded above, the set of
upper bounds $$S_{\text{upper}}$$ is a ray $$[\alpha, \infty)$$ — it has a left
endpoint, and that endpoint is $$\sup S$$.

**Theorem (greatest lower bound property).** Every nonempty
$$S \subseteq \mathbb{R}$$ bounded below has an infimum.

*Proof.* This is a theorem, not a second axiom, and the trick is reflection.
Let $$-S = \{-x : x \in S\}$$. If $$\beta$$ is a lower bound for $$S$$ then
$$-\beta$$ is an upper bound for $$-S$$, so $$-S$$ is nonempty and bounded
above and has a supremum $$\alpha$$. Then $$-\alpha = \inf S$$: it is a lower
bound since $$\alpha \ge -x$$ for all $$x \in S$$ gives $$-\alpha \le x$$; and
if $$\beta$$ is any lower bound then $$-\beta$$ is an upper bound of $$-S$$, so
$$\alpha \le -\beta$$, i.e. $$\beta \le -\alpha$$. $$\square$$

**Conventions for the unbounded and empty cases.** For nonempty
$$E \subseteq \mathbb{R}$$, write $$\sup E = \infty$$ when $$E$$ is not bounded
above and $$\inf E = -\infty$$ when it is not bounded below. For the empty set
the notes record $$\sup \varnothing = -\infty$$ and
$$\inf \varnothing = \infty$$, which is the only choice consistent with
"every real is both an upper and a lower bound of $$\varnothing$$" — vacuously,
every $$x$$ satisfies the condition, so the least upper bound is as small as
possible.

### Intervals

For $$a \le b$$ in $$\mathbb{R}$$:

$$
\begin{aligned}
(a,b) &= \{x : a < x < b\}, \\
[a,b) &= \{x : a \le x < b\}, \\
(a,b] &= \{x : a < x \le b\}, \\
[a,b] &= \{x : a \le x \le b\},
\end{aligned}
$$

together with the infinite intervals $$(a,\infty)$$, $$[a,\infty)$$,
$$(-\infty,b)$$, $$(-\infty,b]$$ and $$(-\infty,\infty) = \mathbb{R}$$. Note
$$(a,a) = \varnothing$$ and $$[a,a] = \{a\}$$.

**Characterisation.** A set $$J \subseteq \mathbb{R}$$ is an interval exactly
when it is *order-convex*:

$$
x, y \in J,\ x < t < y \ \Longrightarrow\ t \in J .
$$

This is the definition to carry forward. It says nothing about endpoints and
makes no case distinction, and it is the form that
[Chapter 2](/posts/analysis-metric-spaces/) needs to prove that the connected
subsets of $$\mathbb{R}$$ are precisely the intervals.

---

## §1.5 Consequences of the least upper bound property

Three theorems. Each is "obvious", each is false in some ordered field, and each
needs completeness.

### The Archimedean property

**Theorem.** For every $$x > 0$$ and every $$y \in \mathbb{R}$$ there is
$$n \in \mathbb{N}$$ with $$nx > y$$.

*Proof.* Suppose not: for some $$x > 0$$ and $$y$$, every $$n$$ has
$$nx \le y$$. Then $$E = \{nx : n \in \mathbb{N}\}$$ is nonempty and bounded
above by $$y$$, so by completeness $$\alpha = \sup E$$ exists. Since $$x > 0$$,
$$\alpha - x < \alpha$$, so $$\alpha - x$$ is not an upper bound of $$E$$, and
there is $$m \in \mathbb{N}$$ with $$mx > \alpha - x$$. But then
$$(m+1)x > \alpha$$ with $$(m+1)x \in E$$, contradicting that $$\alpha$$ bounds
$$E$$. $$\square$$

That is the characterisation theorem of §1.4 doing exactly the job advertised:
*something below the supremum is not an upper bound.*

**Restatement.** Given $$\varepsilon > 0$$ there is $$n_0 \in \mathbb{N}$$ with
$$n_0\varepsilon > 1$$, equivalently

$$
\frac{1}{n} < \varepsilon \quad\text{for all } n \ge n_0 .
$$

In that form it is the engine of every $$\varepsilon$$-argument in the course:
$$1/n \to 0$$, and so any tolerance can eventually be beaten by a reciprocal
integer. An ordered field in which this fails — and they exist — has infinitely
large elements.

### Density of the rationals

**Theorem.** For $$x < y$$ in $$\mathbb{R}$$ there is $$r \in \mathbb{Q}$$ with
$$x < r < y$$.

*Proof.* Since $$y - x > 0$$, Archimedes gives $$n \in \mathbb{N}$$ with
$$n(y-x) > 1$$, so $$ny > nx + 1$$. Let $$m$$ be the least integer with
$$m > nx$$ — it exists by well-ordering applied to the integers exceeding
$$nx$$, a set which is nonempty again by Archimedes. Minimality gives
$$m - 1 \le nx$$, so

$$
nx < m \le nx + 1 < ny ,
$$

and dividing by $$n > 0$$ gives $$x < m/n < y$$. $$\square$$

The two ingredients are worth separating. Archimedes supplies a denominator
large enough that the step $$1/n$$ fits inside the gap; well-ordering supplies
the numerator. Density is not a substitute for completeness — $$\mathbb{Q}$$ is
dense in itself and still has holes — but it does mean the holes are invisible
to any finite measurement.

### Roots

**Theorem.** For every $$x > 0$$ and every $$n \in \mathbb{N}$$ there is a
unique $$y > 0$$ with $$y^n = x$$.

*Proof sketch.* Uniqueness is immediate: $$0 < y_1 < y_2$$ forces
$$y_1^n < y_2^n$$. For existence, set

$$
E = \{t > 0 : t^n < x\} .
$$

$$E$$ is nonempty and bounded above, so $$y = \sup E$$ exists by completeness.
One then rules out $$y^n < x$$ and $$y^n > x$$ in turn, each by producing a
small $$h$$ for which $$(y+h)^n$$ is still below $$x$$, or $$(y-h)^n$$ still
above it — the estimates are routine, and Bernoulli's inequality from §1.3 is
the convenient tool. Both cases contradict the definition of the supremum, so
$$y^n = x$$. $$\square$$

> This is the theorem that pays for the axiom. The number $$\sqrt2$$ that §1.1
> showed was missing from $$\mathbb{Q}$$ exists in $$\mathbb{R}$$, and it exists
> *as a supremum* — as the least upper bound of the rationals whose square is
> below 2, which is exactly Dedekind's construction viewed from the other side.
{: .prompt-tip }

**Corollary.** For $$a, b > 0$$ and $$n \in \mathbb{N}$$,
$$(ab)^{1/n} = a^{1/n}b^{1/n}$$, since both sides are positive and their
$$n$$-th powers agree, and $$n$$-th roots are unique.

---

## §1.7 Countable and uncountable sets

### Cardinality by bijection

**Definition.** Sets $$A$$ and $$B$$ are **equivalent**, written
$$A \sim B$$, when there is a one-to-one function from $$A$$ onto $$B$$. They
then have the same **cardinality**.

Equivalence is reflexive (take the identity), symmetric (take the inverse,
which exists because the map is a bijection) and transitive (compose). It is
not an equivalence relation on a set, since there is no set of all sets, but it
behaves like one.

Writing $$\mathbb{N}_n = \{1, 2, \ldots, n\}$$:

- $$A$$ is **finite** if $$A = \varnothing$$ or $$A \sim \mathbb{N}_n$$ for
  some $$n$$;
- **infinite** if not finite;
- **countable** (denumerable, enumerable) if $$A \sim \mathbb{N}$$;
- **uncountable** if neither finite nor countable;
- **at most countable** if finite or countable.

An **enumeration** of a countable $$A$$ is a bijection
$$f : \mathbb{N} \to A$$, so that $$A = \{x_1, x_2, x_3, \ldots\}$$ with no
repeats. Countable means *listable*.

A **sequence** in $$A$$ is a function $$f : \mathbb{N} \to A$$, written
$$\{x_n\}$$ with $$x_n = f(n)$$. The notes are careful about a distinction worth
keeping: $$\{x_n\}$$ is the sequence, an ordered infinite list, while
$$\{x_n : n \in \mathbb{N}\}$$ is its **range**, an unordered set that may be
finite.

### Building countable sets

**Theorem.** $$\mathbb{N} \times \mathbb{N}$$ is countable.

*Proof.* List the pairs by *diagonals*: enumerate first the one pair with
$$m+n = 2$$, then the two with $$m+n = 3$$, then the three with $$m+n = 4$$, and
so on. Each diagonal is finite, every pair lies on exactly one diagonal, and
the diagonals are indexed by $$\mathbb{N}$$, so the list reaches every pair
exactly once. Explicitly, $$(m,n) \mapsto 2^{m}3^{n}$$ is one-to-one into
$$\mathbb{N}$$ by unique factorisation, which with the next theorem also
suffices. $$\square$$

**Theorem.** Every infinite subset of a countable set is countable.

*Proof sketch.* Enumerate the countable set as $$x_1, x_2, \ldots$$ and read
along the list, keeping the terms that lie in the subset. Because the subset is
infinite the process never halts, and it produces an enumeration of it.
$$\square$$

**Theorem.** If $$f$$ maps $$\mathbb{N}$$ onto $$A$$, then $$A$$ is at most
countable.

*Proof sketch.* Go along $$f(1), f(2), \ldots$$ and discard any value already
seen. What remains is a list of $$A$$ without repeats, finite or infinite.
$$\square$$

That last theorem is the useful one in practice: **to show a set is at most
countable, it is enough to surject onto it.** You do not have to arrange
injectivity by hand.

### Indexed families

**Definition.** An **indexed family** of subsets of $$X$$ with index set $$A$$
is a function $$A \to \mathcal{P}(X)$$; writing $$E_\alpha$$ for the value at
$$\alpha$$ gives the notation $$\{E_\alpha\}_{\alpha \in A}$$. With
$$A = \mathbb{N}$$ this is a sequence of sets.

$$
\begin{aligned}
\bigcup_{\alpha \in A} E_\alpha &= \{x \in X : x \in E_\alpha \text{ for some } \alpha\}, \\
\bigcap_{\alpha \in A} E_\alpha &= \{x \in X : x \in E_\alpha \text{ for all } \alpha\}.
\end{aligned}
$$

"Some" and "all" are where the quantifiers live, and everything about arbitrary
unions and intersections follows from that reading. The distributive laws, De
Morgan's laws, and the image and inverse-image theorems of §§1.1–1.2 all hold
verbatim for arbitrary families:

$$
\begin{aligned}
E \cap \textstyle\bigcup_\alpha E_\alpha &= \textstyle\bigcup_\alpha (E \cap E_\alpha), \\
\Big(\textstyle\bigcup_\alpha E_\alpha\Big)^{c} &= \textstyle\bigcap_\alpha E_\alpha^{c}, \\
f^{-1}\Big(\textstyle\bigcup_\alpha B_\alpha\Big) &= \textstyle\bigcup_\alpha f^{-1}(B_\alpha),
\end{aligned}
$$

and so on, with $$f(\bigcap_\alpha E_\alpha) \subseteq \bigcap_\alpha f(E_\alpha)$$
remaining the one inclusion that does not reverse. The proofs are the two-set
proofs with "some $$\alpha$$" in place of "1 or 2".

### The countability of $$\mathbb{Q}$$

**Theorem.** A countable union of countable sets is countable: if each
$$E_n$$ is countable and $$S = \bigcup_{n=1}^{\infty} E_n$$, then $$S$$ is
countable.

*Proof.* Enumerate each $$E_n$$ as $$x_{n,1}, x_{n,2}, \ldots$$ and lay the
whole collection out as an infinite array with $$E_n$$ as the $$n$$-th row.
The map $$(n,k) \mapsto x_{n,k}$$ is onto $$S$$, and
$$\mathbb{N}\times\mathbb{N}$$ is countable, so $$S$$ is the image of a
countable set under a surjection and is at most countable. It is infinite, so
it is countable. $$\square$$

> Choosing an enumeration of each $$E_n$$ *simultaneously* for all $$n$$ uses a
> countable form of the axiom of choice. The course does not raise this, and at
> this level it is universally left unremarked, but it is the one hidden
> ingredient in an otherwise elementary proof.
{: .prompt-info }

**Corollary.** $$\mathbb{Q}$$ is countable.

*Proof.* For each $$n \in \mathbb{N}$$ the set
$$E_n = \{m/n : m \in \mathbb{Z}\}$$ is countable, being a bijective copy of
$$\mathbb{Z}$$, and $$\mathbb{Q} = \bigcup_n E_n$$. $$\square$$

So $$\mathbb{Q}$$ is dense in $$\mathbb{R}$$ and still, in this sense, small.
Density and size are independent.

### The uncountability of $$\mathbb{R}$$

**Theorem.** $$[0,1]$$ is uncountable.

*Proof.* Suppose $$[0,1] = \{x_1, x_2, x_3, \ldots\}$$ were an enumeration.
Build nested closed intervals as follows. Split $$[0,1]$$ into three closed
thirds; at least one of them misses $$x_1$$, and call it $$I_1$$. Split
$$I_1$$ into thirds and let $$I_2$$ be one missing $$x_2$$. Continuing gives

$$
I_1 \supseteq I_2 \supseteq I_3 \supseteq \cdots,
$$

closed, bounded, nonempty, with $$x_n \notin I_n$$. Now let
$$\alpha = \sup\{\text{left endpoints of the } I_n\}$$, which exists by
completeness. Each left endpoint is below every right endpoint, so
$$\alpha \in I_n$$ for every $$n$$. But $$\alpha \in [0,1]$$ means
$$\alpha = x_N$$ for some $$N$$, and $$x_N \notin I_N$$. Contradiction.
$$\square$$

The proof uses completeness twice over — once to produce $$\alpha$$ and once in
the fact that nested closed bounded intervals have a common point, which is the
same statement. **Uncountability of $$\mathbb{R}$$ is a completeness
phenomenon**, not a counting accident: $$\mathbb{Q}$$ with the same order is
countable.

**Theorem.** The set $$A$$ of all sequences with entries in $$\{0,1\}$$ is
uncountable.

*Proof (Cantor's diagonal argument).* An element of $$A$$ is a function
$$\mathbb{N} \to \{0,1\}$$. Suppose $$A = \{f_1, f_2, f_3, \ldots\}$$ and
define $$g : \mathbb{N} \to \{0,1\}$$ by

$$
g(n) = 1 - f_n(n) .
$$

Then $$g \in A$$. But $$g \ne f_n$$ for every $$n$$, since the two differ at
$$n$$. So $$g$$ is missing from the list, and no list can be complete.
$$\square$$

Two lines, and it is the most consequential argument in the chapter. The same
device reappears as the halting problem, as Gödel's incompleteness theorem, and
as the proof that $$\mathcal{P}(A)$$ is never equivalent to $$A$$.

## Worked examples

**1. A supremum that is not attained.** Find $$\sup E$$ and $$\inf E$$ for
$$E = \{1 - 1/n : n \in \mathbb{N}\}$$.

The elements are $$0, \tfrac12, \tfrac23, \tfrac34, \ldots$$, increasing and
all below $$1$$, so $$1$$ is an upper bound. It is least: given $$\beta < 1$$,
Archimedes supplies $$n$$ with $$1/n < 1 - \beta$$, and then
$$1 - 1/n > \beta$$, so $$\beta$$ is not an upper bound. Hence $$\sup E = 1$$,
and $$1 \notin E$$, so $$E$$ has no maximum. Meanwhile
$$\inf E = \min E = 0$$.

Note which theorem did the work in each half: the characterisation of §1.4 to
reduce "least upper bound" to "nothing smaller works", and Archimedes to beat
the tolerance.

**2. Sup of a sum.** For nonempty bounded $$A, B \subseteq \mathbb{R}$$ and
$$A + B = \{a + b : a \in A, b \in B\}$$, show
$$\sup(A+B) = \sup A + \sup B$$.

Write $$\alpha = \sup A$$, $$\beta = \sup B$$. Every element of $$A+B$$ is at
most $$\alpha + \beta$$, so that is an upper bound. For leastness take
$$\varepsilon > 0$$; there are $$a \in A$$ with $$a > \alpha - \varepsilon/2$$
and $$b \in B$$ with $$b > \beta - \varepsilon/2$$, so

$$
a + b > \alpha + \beta - \varepsilon .
$$

Since $$\varepsilon$$ was arbitrary, nothing below $$\alpha+\beta$$ is an upper
bound. $$\square$$

Splitting $$\varepsilon$$ into two halves so the errors add to $$\varepsilon$$
is the single most-used technique in the whole course. It will appear in every
chapter from here.

**3. Where the analogous statement fails.** $$\sup(A \cup B) = \max(\sup A, \sup B)$$
is true, but $$\sup(A \cap B) = \min(\sup A, \sup B)$$ is false — take
$$A = \{0\}$$ and $$B = \{1\}$$, where the intersection is empty. Compare the
image/inverse-image asymmetry of §1.2: intersections are where set operations
stop commuting with everything.

## Common pitfalls

- **Confusing maximum with supremum.** A supremum always exists for a nonempty
  set bounded above; a maximum often does not. $$\sup(0,1) = 1 \notin (0,1)$$.
- **Thinking $$f^{-1}$$ requires an inverse.** The inverse image
  $$f^{-1}(H)$$ is defined for any $$f$$ and any $$H$$. Only the inverse
  *function* needs bijectivity.
- **Expecting images to behave like preimages.** $$f(A_1 \cap A_2)$$ can be
  strictly smaller than $$f(A_1) \cap f(A_2)$$, and $$f(A^{c})$$ has no
  relation to $$f(A)^{c}$$ at all.
- **Using induction when strong induction is needed.** If $$P(k)$$ depends on
  some $$P(j)$$ with $$j$$ not equal to $$k-1$$, ordinary induction does not
  reach it.
- **Dropping $$h \ge -1$$ from Bernoulli.** The induction step multiplies by
  $$1+h$$ and silently assumes it is non-negative.
- **Treating density as completeness.** $$\mathbb{Q}$$ is dense in itself and
  is not complete. Density says there is always something in between; it says
  nothing about limits existing.
- **Forgetting that $$\mathbb{Q}$$ is countable and $$\mathbb{R}$$ is not.**
  The temptation after §1.5 is to feel the two are much alike. §1.7 is placed
  immediately afterwards to kill that feeling.
- **Verifying a supremum by checking only clause 1.** Showing $$\alpha$$ bounds
  the set is half the work. The other half is showing nothing smaller does.

## Connections

- **Forward, immediately.** The supremum is the tool that builds everything:
  $$\limsup$$ and $$\liminf$$ in
  [Chapter 3](/posts/analysis-sequences/), the Darboux upper and lower
  integrals in [Chapter 6](/posts/analysis-integration/), and the least upper
  bound hiding inside the intermediate value theorem in
  [Chapter 4](/posts/analysis-continuity/) are all this one construction.
- **Forward, structurally.** The order-convexity characterisation of intervals
  is what [Chapter 2](/posts/analysis-metric-spaces/) needs for connectedness,
  and the behaviour of inverse images is what makes the topological definition
  of continuity work.
- **Countability.** The Cantor set in
  [Chapter 2](/posts/analysis-metric-spaces/) is uncountable with the diagonal
  argument of §1.7 doing the work again, and the rearrangement theorem of
  [Chapter 7](/posts/analysis-series/) depends on $$\mathbb{N}$$ being
  reorderable in uncountably many ways.
- **Outward.** The diagonal argument is the ancestor of the halting problem and
  of Gödel's first incompleteness theorem; in both, a list is assumed complete
  and an object is built to differ from its $$n$$-th entry at $$n$$.

## Summary

- **$$\sqrt 2 \notin \mathbb{Q}$$** — the hole that motivates the whole chapter
- **Set identities** are logical identities: union is "or", intersection is "and"
- **A function is a set of ordered pairs**, not a rule
- **Inverse images commute with everything**; images commute only with unions
- **Induction $$\Leftarrow$$ well-ordering**, via the least counterexample
- **Bernoulli** — $$(1+h)^n \ge 1 + nh$$ for $$h \ge -1$$
- **Field** — eight axioms; $$\mathbb{Q}, \mathbb{R}, \mathbb{C}$$ yes, $$\mathbb{N}, \mathbb{Z}$$ no
- **Ordered field** — a positive cone with closure and trichotomy; $$\mathbb{C}$$ cannot be one
- **Supremum** — least upper bound; unique; need not lie in the set
- **The usable test** — $$\alpha = \sup A$$ iff no $$\beta < \alpha$$ bounds $$A$$
- **The axiom** — nonempty and bounded above $$\Rightarrow$$ supremum exists
- **Infimum** — a theorem, by reflecting the set through $$0$$
- **Archimedean** — $$\forall \varepsilon > 0$$, eventually $$1/n < \varepsilon$$
- **Density** — a rational strictly between any two reals
- **Roots** — $$x > 0$$ has a unique positive $$n$$-th root, produced as a supremum
- **Countable** — equivalent to $$\mathbb{N}$$, i.e. listable without repeats
- **$$\mathbb{N}\times\mathbb{N}$$, countable unions, $$\mathbb{Q}$$** — all countable
- **$$[0,1]$$ and $$\{0,1\}^{\mathbb{N}}$$** — uncountable, by nesting and by diagonal

## References

- Manfred Stoll, *Introduction to Real Analysis*, 2nd edition — Chapter 1, §§1.1–1.5 and §1.7.
- Introduction to Mathematical Analysis (881.008), Spring 2023. Instructor: Ja A Jeong (정자아). Handwritten summary notes for Chapters 1 to 3.
- The notes give definitions and theorem statements and leave every proof as a blank `pf>`. All proofs above are mine. Where a proof is long or routine — the ordered-field properties (a), (b), (c), (e), the distributive laws (a), (b), (c), the existence of $$n$$-th roots, and the family versions of the De Morgan and image laws — it is sketched or stated rather than written out, following the course's own weighting.
- The worked examples are mine; the handwritten notes for Chapters 1 to 3 carry no exercises.
- Two corrections. The notes state Bernoulli's inequality without the hypothesis $$h \ge -1$$, which the induction step needs. And remark ③ under *Intervals* reads "all intervals are bounded subsets of $$\mathbb{R}$$", which contradicts remark ① on the same page listing $$(a,\infty)$$ and $$\mathbb{R}$$ as intervals; the intended claim is presumably that intervals with two real endpoints are bounded.
- The note on the axiom of choice in the countable-union proof is added here; the course does not raise it.
