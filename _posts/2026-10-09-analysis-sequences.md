---
title: "Mathematical Analysis: Sequences of Real Numbers"
date: 2026-10-09 09:30:00 +0900
categories: [Course Notes, Mathematical Analysis]
tags: [sequences, convergence, monotone, bolzano-weierstrass, limsup, cauchy sequences]
description: Convergence in a metric space, the algebra of limits, monotone sequences, subsequences and Bolzano-Weierstrass, limit superior and inferior, and Cauchy sequences. Chapter 3 of Introduction to Mathematical Analysis.
math: true
mermaid: false
render_with_liquid: false
---

> §§3.1 and 3.2 follow the course notes. §§3.3 to 3.6 — monotone sequences,
> subsequences, limit superior and inferior, and Cauchy sequences — are
> reconstructed from the textbook, because the handwritten summary stops at
> §3.2 and the later chapters need them. Series of real numbers, which some
> orderings place here, is [Chapter 7](/posts/analysis-series/).
{: .prompt-info }

## What this chapter answers

[Chapter 2](/posts/analysis-metric-spaces/) described nearness with open sets
and limit points. This chapter describes it with **processes**: a sequence
$$\{p_n\}$$ that settles down. The two descriptions turn out to be the same
one, and that equivalence is most of the chapter's value — a topological fact
and a sequential fact are usually two readings of a single statement, and you
get to pick whichever is easier to prove.

The second question is sharper. Convergence as defined requires you to
**name the limit first**: $$p_n \to p$$ means the terms get close to $$p$$.
But in practice you have a sequence and want to know whether *some* limit
exists, without being able to produce it. Two criteria answer that, and both
are completeness in disguise:

- a **monotone** bounded sequence converges;
- a **Cauchy** sequence — one whose terms get close *to each other* — converges.

The Cauchy criterion is the important one, because it is intrinsic. It is also
the statement that fails in $$\mathbb{Q}$$, and it is what "complete metric
space" means in general.

## Prerequisites

[Chapter 1](/posts/analysis-real-numbers/) for suprema and the Archimedean
property; [Chapter 2](/posts/analysis-metric-spaces/) for neighbourhoods,
limit points, closedness and compactness.

---

## §3.1 Convergent sequences

### The definition

Let $$(X,d)$$ be a metric space.

**Definition.** A sequence $$\{p_n\}_{n=1}^{\infty}$$ in $$X$$ **converges**
when there is $$p \in X$$ such that

$$
\begin{aligned}
\forall \varepsilon > 0,\ \exists n_0 = n_0(\varepsilon) \in \mathbb{N} \\
\text{such that } \forall n \ge n_0,\ p_n \in N_\varepsilon(p).
\end{aligned}
$$

Then $$p$$ is the **limit**, written $$\lim_{n\to\infty} p_n = p$$ or
$$p_n \to p$$. A sequence that does not converge **diverges**.

Three readings of the same line, each worth having:

- **Unpacked.** For every tolerance there is a point in the list beyond which
  every term is within that tolerance.
- **In the metric.** $$d(p_n, p) \to 0$$ as a sequence of real numbers.
- **Eventually.** Every neighbourhood of $$p$$ contains **all but finitely
  many** terms.

The notation $$n_0 = n_0(\varepsilon)$$ in the notes is deliberate: the
threshold depends on the tolerance. Where that dependence is allowed to sit is
the entire difference between this definition and uniform convergence in
[Chapter 8](/posts/analysis-function-sequences/).

**Definition.** $$\{p_n\}$$ is **bounded** when there are $$p \in X$$ and
$$M > 0$$ with $$d(p, p_n) \le M$$ for all $$n$$.

### First consequences

**Theorem.** Let $$(X,d)$$ be a metric space.

1. A convergent sequence has a **unique** limit.
2. Every convergent sequence is bounded.
3. If $$E \subseteq X$$ and $$p$$ is a limit point of $$E$$, then there is a
   sequence $$\{p_n\}$$ in $$E$$ with $$p_n \ne p$$ for all $$n$$ and
   $$p_n \to p$$.

*Proof of 1.* Suppose $$p_n \to p$$ and $$p_n \to q$$ with $$p \ne q$$. Put
$$\varepsilon = \tfrac12 d(p,q) > 0$$. Beyond some index the terms lie in
$$N_\varepsilon(p)$$, and beyond some index in $$N_\varepsilon(q)$$; past both,

$$
d(p,q) \le d(p,p_n) + d(p_n,q) < \varepsilon + \varepsilon = d(p,q),
$$

which is absurd. $$\square$$

The device — *halve the distance between the two candidates and watch the
triangle inequality close* — is the standard way to prove any uniqueness
statement in a metric space.

*Proof of 2.* Take $$\varepsilon = 1$$. Beyond some $$n_0$$ all terms lie in
$$N_1(p)$$. The finitely many earlier terms have finitely many distances to
$$p$$; let $$M$$ be the largest of those and $$1$$. $$\square$$

Again the pattern from [Chapter 2](/posts/analysis-metric-spaces/): **handle
all but finitely many uniformly, then take a maximum over the rest.**

*Proof of 3.* For each $$n$$, $$N_{1/n}(p)$$ contains a point
$$p_n \in E$$ with $$p_n \ne p$$, by the definition of a limit point. Then
$$d(p,p_n) < 1/n \to 0$$ by the Archimedean property. $$\square$$

> **Statement 3 is the bridge.** It converts the topological notion of a limit
> point into a sequence, and its converse is immediate. So:
>
> $$p \in \overline{E} \iff \text{some sequence in } E \text{ converges to } p,$$
>
> and consequently $$F$$ is closed exactly when it contains the limit of every
> convergent sequence of its points. From here on, "closed" can be checked
> with sequences, which is usually easier.
{: .prompt-tip }

---

## §3.2 Sequences of real numbers

In $$\mathbb{R}$$ there is arithmetic, and limits respect it.

**Theorem.** If $$a_n \to a$$ and $$b_n \to b$$, then

$$
\begin{aligned}
\text{(a)}\ & a_n + b_n \to a + b \\
\text{(b)}\ & a_n b_n \to ab \\
\text{(c)}\ & \frac{b_n}{a_n} \to \frac{b}{a}, \quad
 \text{if } a \ne 0 \text{ and all } a_n \ne 0
\end{aligned}
$$

*Proof of (a).* Given $$\varepsilon > 0$$, choose $$n_1$$ with
$$\lvert a_n - a\rvert < \varepsilon/2$$ for $$n \ge n_1$$, and $$n_2$$
similarly for $$b$$. For $$n \ge \max(n_1,n_2)$$,

$$
\begin{aligned}
\lvert (a_n+b_n) - (a+b)\rvert
 &\le \lvert a_n - a\rvert + \lvert b_n - b\rvert \\
 &< \tfrac{\varepsilon}{2} + \tfrac{\varepsilon}{2} = \varepsilon .
\end{aligned}
$$

$$\square$$

*Proof of (b).* The trick is to add and subtract a hybrid term:

$$
\begin{aligned}
\lvert a_nb_n - ab\rvert
 &= \lvert a_nb_n - a_nb + a_nb - ab\rvert \\
 &\le \lvert a_n\rvert\,\lvert b_n - b\rvert + \lvert b\rvert\,\lvert a_n - a\rvert .
\end{aligned}
$$

$$\{a_n\}$$ is bounded, by $$M$$ say, because it converges. Make the first term
below $$\varepsilon/2$$ by taking $$\lvert b_n - b\rvert < \varepsilon/(2M)$$
and the second below $$\varepsilon/2$$ by taking
$$\lvert a_n - a\rvert < \varepsilon/(2(\lvert b\rvert + 1))$$. $$\square$$

> **The two techniques in that proof are the whole subject.** *Split
> $$\varepsilon$$* so that finitely many errors sum to the budget, and *add and
> subtract a hybrid term* so that a difference of products becomes a sum of
> differences you can already control. Together with the triangle inequality
> they account for most proofs in Chapters 3 to 8.
{: .prompt-tip }

(c) follows from (b) once $$1/a_n \to 1/a$$, which needs the observation that
$$\lvert a_n\rvert$$ is eventually bounded away from $$0$$ — take
$$\varepsilon = \lvert a\rvert/2$$ in the definition — so the denominators in

$$
\left\lvert \frac1{a_n} - \frac1a \right\rvert = \frac{\lvert a - a_n\rvert}{\lvert a_n\rvert\,\lvert a\rvert}
$$

do not degenerate.

**Corollary.** If $$a_n \to a$$ then $$a_n + c \to a + c$$ and
$$ca_n \to ca$$ for every $$c \in \mathbb{R}$$.

**Theorem.** If $$a_n \to 0$$ and $$\{b_n\}$$ is bounded, then
$$a_nb_n \to 0$$.

*Proof.* With $$\lvert b_n\rvert \le M$$,
$$\lvert a_nb_n\rvert \le M\lvert a_n\rvert \to 0$$. $$\square$$

Note that $$\{b_n\}$$ need not converge: $$(1/n)\sin n \to 0$$ although
$$\sin n$$ has no limit. This is the correct tool whenever one factor
oscillates.

**Theorem (squeeze).** If $$a_n \le b_n \le c_n$$ for all $$n \ge n_0$$ and
$$\lim a_n = \lim c_n = L$$, then $$b_n \to L$$.

*Proof.* Given $$\varepsilon > 0$$, eventually $$L - \varepsilon < a_n$$ and
$$c_n < L + \varepsilon$$, so eventually
$$L - \varepsilon < b_n < L + \varepsilon$$. $$\square$$

The hypothesis holds only *eventually*, which is enough: convergence never
depends on any finite number of terms.

---

## §3.3 Monotone sequences

**Definition.** $$\{a_n\}$$ is **increasing** if $$a_n \le a_{n+1}$$ for all
$$n$$, **decreasing** if $$a_n \ge a_{n+1}$$, and **monotone** if either.

**Theorem (monotone convergence).** A monotone bounded sequence of real
numbers converges. If $$\{a_n\}$$ is increasing and bounded above then

$$
\lim_{n\to\infty} a_n = \sup_n a_n ,
$$

and symmetrically for decreasing sequences with the infimum.

*Proof.* Let $$\alpha = \sup_n a_n$$, which exists by completeness. Given
$$\varepsilon > 0$$, the characterisation theorem of §1.4 gives $$n_0$$ with
$$a_{n_0} > \alpha - \varepsilon$$. For $$n \ge n_0$$ monotonicity gives
$$\alpha - \varepsilon < a_{n_0} \le a_n \le \alpha$$, so
$$\lvert a_n - \alpha\rvert < \varepsilon$$. $$\square$$

> **This is the first criterion that does not require naming the limit.** You
> check two things you can see — the terms increase, the terms stay below
> something — and convergence follows. The limit is then *identified* as a
> supremum, which may be entirely unknown. This is how $$e$$ is usually
> constructed, as the limit of the increasing bounded sequence
> $$(1 + 1/n)^n$$.
{: .prompt-tip }

A monotone unbounded sequence diverges, but does so predictably:
$$a_n \to \infty$$ in the sense that for every $$M$$ there is $$n_0$$ with
$$a_n > M$$ beyond it. So **a monotone sequence either converges or tends to
$$\pm\infty$$** — it cannot oscillate.

---

## §3.4 Subsequences and Bolzano–Weierstrass

**Definition.** Given $$\{p_n\}$$ and integers
$$n_1 < n_2 < n_3 < \cdots$$, the sequence $$\{p_{n_k}\}_{k=1}^{\infty}$$ is a
**subsequence**. Note $$n_k \ge k$$ always, by induction.

**Theorem.** $$p_n \to p$$ $$\iff$$ every subsequence of $$\{p_n\}$$ converges
to $$p$$.

*Proof.* ($$\Rightarrow$$) If all terms past $$n_0$$ lie in
$$N_\varepsilon(p)$$ then so do all $$p_{n_k}$$ with $$k \ge n_0$$, since
$$n_k \ge k$$. ($$\Leftarrow$$) The sequence is a subsequence of itself.
$$\square$$

The contrapositive is how divergence is usually proved: **exhibit two
subsequences with different limits.** For $$a_n = (-1)^n$$ the even and odd
subsequences give $$1$$ and $$-1$$, so $$\{a_n\}$$ diverges.

**Theorem.** Every sequence of real numbers has a monotone subsequence.

*Proof.* Call $$m$$ a *peak* if $$a_m \ge a_n$$ for all $$n > m$$. If there are
infinitely many peaks $$m_1 < m_2 < \cdots$$, then $$\{a_{m_k}\}$$ is
decreasing. If there are finitely many, let $$N$$ exceed them all; then no
$$n \ge N$$ is a peak, so for each such $$n$$ there is a later term strictly
greater, and iterating produces an increasing subsequence. $$\square$$

**Theorem (Bolzano–Weierstrass, sequential form).** Every bounded sequence of
real numbers has a convergent subsequence.

*Proof.* Take a monotone subsequence by the previous theorem; it is bounded,
so it converges by §3.3. $$\square$$

This is the sequential face of the Bolzano–Weierstrass theorem of
[Chapter 2](/posts/analysis-metric-spaces/), which said a bounded infinite
*set* has a limit point. The two are the same theorem read through the bridge
of §3.1, and in a general metric space the corresponding property — every
sequence has a convergent subsequence — is called **sequential compactness**
and coincides with compactness.

---

## §3.5 Limit superior and inferior

Bolzano–Weierstrass says a bounded sequence has convergent subsequences, but
possibly many, with different limits. The $$\limsup$$ and $$\liminf$$ are the
extreme ones, and they exist for *every* bounded sequence.

**Definition.** For a bounded real sequence $$\{a_n\}$$,

$$
\begin{aligned}
\limsup_{n\to\infty} a_n &= \lim_{n\to\infty}\ \sup_{k \ge n} a_k , \\
\liminf_{n\to\infty} a_n &= \lim_{n\to\infty}\ \inf_{k \ge n} a_k .
\end{aligned}
$$

Both limits exist: $$s_n = \sup_{k \ge n} a_k$$ is decreasing in $$n$$, because
the supremum is taken over a shrinking set, and bounded below, so §3.3
applies. Symmetrically $$\inf_{k\ge n} a_k$$ increases.

For unbounded sequences the conventions of §1.4 apply, giving
$$\limsup a_n = \infty$$ and so on.

**Theorem.**

1. $$\liminf a_n \le \limsup a_n$$.
2. $$\{a_n\}$$ converges $$\iff$$ $$\liminf a_n = \limsup a_n$$, and the common
   value is the limit.
3. $$\limsup a_n$$ is the largest limit of a convergent subsequence, and
   $$\liminf a_n$$ the smallest.

*Proof of 2.* ($$\Rightarrow$$) If $$a_n \to a$$ then for every
$$\varepsilon$$, eventually all terms lie in
$$(a-\varepsilon, a+\varepsilon)$$, so eventually
$$a - \varepsilon \le \inf_{k\ge n} a_k \le \sup_{k \ge n} a_k \le a+\varepsilon$$,
and both one-sided limits are squeezed to $$a$$.

($$\Leftarrow$$) If both equal $$L$$, then for large $$n$$ both
$$\inf_{k\ge n}a_k$$ and $$\sup_{k\ge n}a_k$$ lie within $$\varepsilon$$ of
$$L$$, and $$a_n$$ is caught between them. $$\square$$

> **Why these are worth the notation.** $$\lim$$ may not exist;
> $$\limsup$$ always does. That makes it the right object whenever you need a
> number out of an arbitrary bounded sequence and cannot assume convergence —
> which is exactly the situation in the **root test** and **ratio test** of
> [Chapter 7](/posts/analysis-series/), where the sharp statements are in terms
> of $$\limsup$$ and the familiar ones in terms of $$\lim$$ are the special
> case where the limit happens to exist.
{: .prompt-tip }

---

## §3.6 Cauchy sequences

**Definition.** $$\{p_n\}$$ in $$(X,d)$$ is a **Cauchy sequence** when

$$
\begin{aligned}
\forall \varepsilon > 0,\ \exists n_0 \in \mathbb{N} \text{ such that } \\
\forall m, n \ge n_0,\ d(p_m, p_n) < \varepsilon .
\end{aligned}
$$

Compare with convergence. Convergence mentions a limit $$p$$; Cauchy does not.
That is the point: **the Cauchy condition is checkable from the sequence
alone.**

**Theorem.** Every convergent sequence is Cauchy.

*Proof.* If $$p_n \to p$$, take $$n_0$$ with $$d(p_n,p) < \varepsilon/2$$
beyond it; then for $$m,n \ge n_0$$,
$$d(p_m,p_n) \le d(p_m,p) + d(p,p_n) < \varepsilon$$. $$\square$$

**Theorem.** Every Cauchy sequence is bounded, and a Cauchy sequence with a
convergent subsequence converges.

*Proof of the second half.* Suppose $$p_{n_k} \to p$$ and let
$$\varepsilon > 0$$. Choose $$n_0$$ with $$d(p_m,p_n) < \varepsilon/2$$ for
$$m,n \ge n_0$$, and choose $$k$$ with $$n_k \ge n_0$$ and
$$d(p_{n_k}, p) < \varepsilon/2$$. Then for every $$n \ge n_0$$,

$$
d(p_n, p) \le d(p_n, p_{n_k}) + d(p_{n_k}, p) < \varepsilon .
$$

$$\square$$

**Theorem (Cauchy criterion in $$\mathbb{R}$$).** A sequence of real numbers
converges $$\iff$$ it is Cauchy.

*Proof.* ($$\Rightarrow$$) Above. ($$\Leftarrow$$) A Cauchy sequence is
bounded, so by Bolzano–Weierstrass it has a convergent subsequence, and by the
previous theorem it converges. $$\square$$

> **This is completeness again, in its most useful form.** The proof used
> Bolzano–Weierstrass, which used monotone convergence, which used the
> supremum axiom. And the theorem is **false in $$\mathbb{Q}$$**: the decimal
> truncations of $$\sqrt2$$ form a Cauchy sequence of rationals with no
> rational limit. A metric space in which every Cauchy sequence converges is
> called **complete**, and this theorem is the statement that $$\mathbb{R}$$ is
> one. It is Cantor's construction of $$\mathbb{R}$$ read backwards.
{: .prompt-warning }

## Worked examples

**1. A sequence defined by recursion.** Let $$a_1 = 1$$ and
$$a_{n+1} = \sqrt{2 + a_n}$$. Show it converges and find the limit.

*Bounded above by 2:* if $$a_n \le 2$$ then
$$a_{n+1} = \sqrt{2 + a_n} \le \sqrt4 = 2$$, and $$a_1 = 1 \le 2$$, so
induction gives it for all $$n$$.

*Increasing:* $$a_{n+1} \ge a_n$$ is equivalent to
$$2 + a_n \ge a_n^2$$, i.e. $$(a_n - 2)(a_n + 1) \le 0$$, which holds since
$$0 < a_n \le 2$$.

So the sequence is monotone and bounded and converges by §3.3, to some $$L$$.
Now the recursion passes to the limit — $$a_{n+1} \to L$$ and
$$\sqrt{2+a_n} \to \sqrt{2+L}$$ — giving $$L^2 = 2 + L$$, so $$L = 2$$ (the
root $$-1$$ being impossible for a sequence of positive terms).

Note the order of operations. **Convergence must be proved before the
recursion may be solved**; setting $$L = \sqrt{2+L}$$ first proves nothing,
since a divergent sequence would satisfy nothing at all.

**2. $$\limsup$$ and $$\liminf$$ of an oscillating sequence.** For
$$a_n = (-1)^n\left(1 + \tfrac1n\right)$$,

$$
\sup_{k \ge n} a_k \to 1, \qquad \inf_{k\ge n} a_k \to -1 ,
$$

so $$\limsup a_n = 1$$ and $$\liminf a_n = -1$$. They differ, so the sequence
diverges — and $$1$$ and $$-1$$ are exactly the limits of the even and odd
subsequences, illustrating part 3 of the theorem in §3.5.

**3. Cauchy without a limit in the space.** In $$X = (0,1]$$ with the usual
metric, $$p_n = 1/n$$ is Cauchy — the terms crowd together — but has no limit
*in $$X$$*, since $$0 \notin X$$. So $$(0,1]$$ is not a complete metric space,
even though it sits inside the complete space $$\mathbb{R}$$. Completeness is
not inherited by subspaces unless they are closed.

**4. Cauchy is strictly stronger than $$d(p_{n+1},p_n) \to 0$$.** Take
$$a_n = \sqrt n$$. Then

$$
a_{n+1} - a_n = \frac{1}{\sqrt{n+1}+\sqrt n} \to 0 ,
$$

yet $$\{a_n\}$$ is unbounded and so not Cauchy. The Cauchy condition controls
*all* pairs beyond $$n_0$$, not just consecutive ones — a point the definition
makes explicit with "$$\forall m,n \ge n_0$$" and which is easy to misread.

## Common pitfalls

- **Letting $$n_0$$ depend on $$n$$.** It may depend on $$\varepsilon$$ only.
  Reading the quantifiers in the wrong order is the most common error in the
  chapter.
- **Solving a recursion before proving convergence.** Example 1 above.
- **Thinking consecutive terms closing up implies Cauchy.** $$\sqrt n$$ refutes
  it.
- **Assuming a bounded sequence converges.** It has a convergent
  *subsequence*; that is all Bolzano–Weierstrass gives.
- **Forgetting that $$\limsup$$ always exists.** When a problem says "suppose
  the limit exists", check whether $$\limsup$$ would do instead; often the
  hypothesis is unnecessary.
- **Using the algebra of limits before knowing both limits exist.**
  $$\lim(a_n + b_n)$$ can exist while neither $$\lim a_n$$ nor $$\lim b_n$$
  does, as with $$a_n = (-1)^n$$ and $$b_n = -(-1)^n$$.
- **Expecting completeness to be topological.** $$(0,1)$$ and $$\mathbb{R}$$
  are homeomorphic, one is complete and the other is not. Completeness is a
  property of the metric, not of the open sets.

## Connections

- **Backward.** Monotone convergence is the supremum axiom of
  [Chapter 1](/posts/analysis-real-numbers/) with the terms attached;
  Bolzano–Weierstrass is the limit-point theorem of
  [Chapter 2](/posts/analysis-metric-spaces/) read sequentially; and §3.1's
  bridge theorem turns every statement about closure into a statement about
  sequences.
- **Forward.** [Chapter 4](/posts/analysis-continuity/) opens with the
  sequential criterion for limits of functions, which makes every theorem here
  available for continuity at no cost. The Cauchy criterion becomes the Cauchy
  criterion for series in [Chapter 7](/posts/analysis-series/) and, applied to
  the sup metric, the Weierstrass M-test in
  [Chapter 8](/posts/analysis-function-sequences/). $$\limsup$$ is what makes
  the root and ratio tests sharp.
- **Outward.** "Every Cauchy sequence converges" is the definition of a
  complete metric space, and completeness is the hypothesis in the contraction
  mapping theorem, which in turn gives existence and uniqueness for
  differential equations.

## Summary

- **Convergence** — $$\forall\varepsilon\,\exists n_0\,\forall n \ge n_0:\ d(p_n,p) < \varepsilon$$; $$n_0$$ depends on $$\varepsilon$$ alone
- **Limits are unique**, and convergent sequences are bounded
- **The bridge** — $$p \in \overline{E}$$ iff some sequence in $$E$$ converges to $$p$$
- **Algebra of limits** — sums, products, quotients, via splitting $$\varepsilon$$ and a hybrid term
- **Squeeze** — and all hypotheses need only hold eventually
- **Monotone + bounded $$\Rightarrow$$ convergent**, with limit the supremum
- **Subsequence** — $$p_n \to p$$ iff every subsequence does; two different subsequential limits prove divergence
- **Every real sequence has a monotone subsequence**
- **Bolzano–Weierstrass** — every bounded sequence has a convergent subsequence
- **$$\limsup$$, $$\liminf$$** — always exist; equal iff convergent; the extreme subsequential limits
- **Cauchy** — $$\forall m,n \ge n_0$$, not just consecutive terms
- **In $$\mathbb{R}$$: Cauchy $$\iff$$ convergent** — the practical form of completeness, false in $$\mathbb{Q}$$

## References

- Manfred Stoll, *Introduction to Real Analysis*, 2nd edition — the chapter on sequences of real numbers.
- Introduction to Mathematical Analysis (881.008), Spring 2023. Instructor: Ja A Jeong (정자아). Handwritten summary notes for Chapters 1 to 3.
- §§3.1 and 3.2 follow the notes, which give the definitions and the statements of the uniqueness, boundedness, limit-point, algebra-of-limits, bounded-times-null and squeeze theorems, with every proof left blank. Those proofs are mine.
- §§3.3 to 3.6 are **not in the notes**: the handwritten summary ends at §3.2. They are reconstructed from the textbook's standard treatment because Chapters 4 to 8 use them throughout — the ratio and root tests need $$\limsup$$, and the Cauchy criterion is the form of completeness those chapters actually invoke. If the course covered them differently, this is the place where these write-ups part company with it.
- All worked examples are mine; the handwritten notes carry no exercises.
