---
title: "Mathematical Analysis: Metric Spaces and the Structure of Point Sets"
date: 2026-10-09 09:00:00 +0900
categories: [Course Notes, Mathematical Analysis]
tags: [metric spaces, open sets, compactness, heine-borel, connectedness, cantor set]
description: Distance as an axiom, then open and closed sets, limit points and closure, the relative topology, connectedness, compactness and Heine-Borel, and the Cantor set. Chapter 2 of Introduction to Mathematical Analysis.
math: true
mermaid: false
render_with_liquid: false
---

> This chapter covers §§2.1–2.5. It is where the course stops being about
> $$\mathbb{R}$$ and starts being about spaces.
{: .prompt-info }

## What this chapter answers

[Chapter 1](/posts/analysis-real-numbers/) built $$\mathbb{R}$$ out of
algebra, order and one completeness axiom. This chapter asks a different
question: **how much of that apparatus does analysis actually need?**

The answer turns out to be very little. Almost every argument about limits and
continuity uses only the notion of two points being *close*, and closeness is
captured by a single function $$d(x,y)$$ obeying three rules. Strip away
addition, multiplication and order, keep only $$d$$, and you have a **metric
space** — in which open sets, closure, convergence, continuity and compactness
all still make sense.

Two payoffs. First, generality: every theorem proved here applies to
$$\mathbb{R}$$, to $$\mathbb{R}^n$$, to spaces of functions in
[Chapter 8](/posts/analysis-function-sequences/), and to objects nobody has
thought of yet. Second, and more immediately useful, **the hypotheses become
visible**. When you prove that a continuous function on a compact set attains
its maximum, you can see exactly which property did the work — and you can see
that completeness and order were not it.

The chapter ends with the Cantor set, which exists to break every intuition
built along the way: uncountable, yet containing no interval; totally
disconnected, yet with no isolated points; and of total length zero.

## Prerequisites

[Chapter 1](/posts/analysis-real-numbers/) throughout — suprema for the
Heine–Borel argument, order-convexity for connectedness, countability for the
Cantor set, and the behaviour of arbitrary unions and intersections from §1.7.

---

## §2.1 Metric spaces

### Absolute value first

**Definition.** For $$x \in \mathbb{R}$$,

$$
\lvert x \rvert = \begin{cases} x, & x \ge 0 \\ -x, & x < 0 \end{cases}
$$

**Theorem.** For all $$x, y \in \mathbb{R}$$ and $$r > 0$$:

$$
\begin{aligned}
\text{(a)}\ & \lvert -x \rvert = \lvert x \rvert \\
\text{(b)}\ & \lvert xy \rvert = \lvert x \rvert \lvert y \rvert \\
\text{(c)}\ & \sqrt{x^2} = \lvert x \rvert \\
\text{(d)}\ & \lvert x \rvert < r \iff -r < x < r \\
\text{(e)}\ & -\lvert x \rvert \le x \le \lvert x \rvert
\end{aligned}
$$

Each is a two-case check. Part (d) is the one used constantly: it converts a
statement about magnitude into a pair of inequalities, which is how every
$$\varepsilon$$-argument gets unpacked.

**Theorem (triangle inequality).** $$\lvert x + y \rvert \le \lvert x \rvert + \lvert y \rvert$$.

*Proof.* By (e), $$-\lvert x\rvert \le x \le \lvert x\rvert$$ and
$$-\lvert y\rvert \le y \le \lvert y\rvert$$. Adding,

$$
-(\lvert x\rvert + \lvert y\rvert) \le x + y \le \lvert x\rvert + \lvert y\rvert ,
$$

and (d) read backwards gives the claim. $$\square$$

**Corollary.** For all $$x,y,z \in \mathbb{R}$$,

$$
\begin{aligned}
\text{(a)}\ & \lvert x - y\rvert \le \lvert x-z\rvert + \lvert z-y\rvert \\
\text{(b)}\ & \big\lvert \lvert x\rvert - \lvert y\rvert \big\rvert \le \lvert x-y\rvert
\end{aligned}
$$

For (a), write $$x - y = (x-z) + (z-y)$$ and apply the theorem. For (b) — the
**reverse triangle inequality** — apply (a) twice to get
$$\lvert x\rvert - \lvert y\rvert \le \lvert x-y\rvert$$ and the same with
$$x$$ and $$y$$ swapped.

Part (a) is the prototype. It says: *the distance from $$x$$ to $$y$$ is no
more than the detour through $$z$$.* That single sentence is about to become an
axiom.

### The axioms

**Definition.** Let $$X$$ be a nonempty set. A **metric** on $$X$$ is a
real-valued function $$d$$ on $$X \times X$$ such that for all
$$x,y,z \in X$$:

1. $$d(x,y) \ge 0$$, and $$d(x,y) = 0 \iff x = y$$;
2. $$d(x,y) = d(y,x)$$ (symmetry);
3. $$d(x,y) \le d(x,z) + d(z,y)$$ (the triangle inequality).

The pair $$(X,d)$$ is a **metric space**.

The **Euclidean distance** $$d(x,y) = \lvert x - y\rvert$$ on $$\mathbb{R}$$ is
the motivating example, and the corollary above is exactly the verification
that it is a metric.

> **What was thrown away.** A metric space has no addition, no multiplication,
> no order and no completeness. What survives is: which points are near which.
> Every definition in the rest of this chapter is phrased only in terms of
> $$d$$, which is why they will transplant to $$\mathbb{R}^n$$ and to function
> spaces without a word changing.
{: .prompt-tip }

Other metrics on the same set are genuinely different spaces. On
$$\mathbb{R}^n$$ the Euclidean metric, the taxicab metric
$$\sum \lvert x_i - y_i\rvert$$ and the max metric
$$\max_i \lvert x_i - y_i\rvert$$ all satisfy the axioms. On *any* set the
**discrete metric** — $$d(x,y) = 1$$ for $$x \ne y$$ — does too, and it is the
standard source of counterexamples.

---

## §2.2 Open and closed sets

### Neighbourhoods, interiors, open sets

Throughout, $$(X,d)$$ is a metric space.

**Definition.** For $$p \in X$$ and $$\varepsilon > 0$$, the
**$$\varepsilon$$-neighbourhood** of $$p$$ is

$$
N_\varepsilon(p) = \{x \in X : d(p,x) < \varepsilon\} .
$$

**Definition.** For $$E \subseteq X$$, a point $$p \in E$$ is an **interior
point** of $$E$$ when $$N_\varepsilon(p) \subseteq E$$ for some
$$\varepsilon > 0$$. The set of interior points is the **interior**
$$\operatorname{Int}(E)$$.

**Definition.** $$O \subseteq X$$ is **open** when every point of $$O$$ is an
interior point of $$O$$. $$F \subseteq X$$ is **closed** when $$F^{c}$$ is
open.

Open and closed are not opposites. $$\varnothing$$ and $$X$$ are both; the
half-open interval $$[0,1)$$ in $$\mathbb{R}$$ is neither.

**Theorem.** Every $$\varepsilon$$-neighbourhood is open.

*Proof.* Let $$q \in N_\varepsilon(p)$$, so $$d(p,q) < \varepsilon$$. Put
$$\delta = \varepsilon - d(p,q) > 0$$. If $$x \in N_\delta(q)$$ then by the
triangle inequality

$$
d(p,x) \le d(p,q) + d(q,x) < d(p,q) + \delta = \varepsilon ,
$$

so $$N_\delta(q) \subseteq N_\varepsilon(p)$$. $$\square$$

That proof is the whole chapter in miniature: **choose the leftover radius and
let the triangle inequality close the gap.** It recurs so often that it is
worth memorising the shape rather than the statement. The same argument shows
every open interval in $$\mathbb{R}$$ is open, since an open interval is a
neighbourhood of each of its points.

### How open sets combine

**Theorem.** In any metric space $$X$$:

1. the union of *any* collection of open sets is open;
2. the intersection of *finitely many* open sets is open.

*Proof.* (1) If $$p \in \bigcup_\alpha O_\alpha$$ then $$p \in O_{\alpha_0}$$
for some $$\alpha_0$$, and an $$\varepsilon$$ that works for $$O_{\alpha_0}$$
works for the union, which is larger.

(2) If $$p \in \bigcap_{j=1}^{n} O_j$$, pick $$\varepsilon_j > 0$$ with
$$N_{\varepsilon_j}(p) \subseteq O_j$$ for each $$j$$ and set
$$\varepsilon = \min\{\varepsilon_1, \ldots, \varepsilon_n\}$$. Then
$$\varepsilon > 0$$ and $$N_\varepsilon(p)$$ lies in every $$O_j$$.
$$\square$$

**Why "finitely many" is not laziness.** The minimum of finitely many positive
numbers is positive; the infimum of infinitely many need not be. And the
theorem genuinely fails:

$$
\bigcap_{n=1}^{\infty}\left(-\tfrac1n,\ \tfrac1n\right) = \{0\},
$$

an intersection of open intervals that is not open. Taking complements gives
the closed-set version:

**Theorem.** Arbitrary intersections of closed sets are closed; finite unions
of closed sets are closed.

*Proof.* De Morgan from §1.7 plus the previous theorem. $$\square$$

> The asymmetry — arbitrary unions but finite intersections — is not an
> artefact of metric spaces. It is the definition of a **topology**, and
> everything in §2.2 that does not mention $$d$$ explicitly is really
> topology. The metric is scaffolding.
{: .prompt-tip }

### Limit points and closure

**Definition.** Let $$E \subseteq X$$.

- $$p \in X$$ is a **limit point** of $$E$$ when every $$N_\varepsilon(p)$$
  contains some $$q \in E$$ with $$q \ne p$$.
- $$p \in E$$ is an **isolated point** of $$E$$ when it is not a limit point.

A limit point need not belong to $$E$$: $$0$$ is a limit point of
$$\{1/n : n \in \mathbb{N}\}$$ and is not in it. The clause $$q \ne p$$ is
essential; without it every point of $$E$$ would qualify trivially.

**Theorem.** $$F \subseteq X$$ is closed $$\iff$$ $$F$$ contains all of its
limit points.

*Proof.* ($$\Rightarrow$$) Let $$F$$ be closed and let $$p$$ be a limit point
of $$F$$ with $$p \notin F$$. Then $$p \in F^{c}$$, which is open, so some
$$N_\varepsilon(p) \subseteq F^{c}$$ — a neighbourhood containing no point of
$$F$$ at all, contradicting that $$p$$ is a limit point.

($$\Leftarrow$$) Suppose $$F$$ contains its limit points and let
$$p \in F^{c}$$. Then $$p$$ is not a limit point of $$F$$, so some
$$N_\varepsilon(p)$$ contains no point of $$F$$ other than possibly $$p$$ —
and $$p \notin F$$, so none at all. Hence $$N_\varepsilon(p) \subseteq F^{c}$$
and $$F^{c}$$ is open. $$\square$$

**Theorem.** If $$p$$ is a limit point of $$E$$, then every
$$N_\varepsilon(p)$$ contains **infinitely many** points of $$E$$.

*Proof.* Suppose some $$N_\varepsilon(p)$$ met $$E$$ in only finitely many
points $$q_1, \ldots, q_n$$ other than $$p$$. Let
$$\delta = \min_j d(p, q_j) > 0$$ — positive because there are finitely many
and each $$q_j \ne p$$. Then $$N_\delta(p)$$ contains no point of $$E$$ except
possibly $$p$$, contradicting that $$p$$ is a limit point. $$\square$$

**Corollary.** A finite set has no limit points, and so is closed.

**Definition.** Writing $$E'$$ for the set of limit points of $$E$$, the
**closure** is $$\overline{E} = E \cup E'$$.

**Theorem.**

1. $$\overline{E}$$ is closed.
2. $$E = \overline{E} \iff E$$ is closed.
3. If $$F$$ is closed and $$E \subseteq F$$, then $$\overline{E} \subseteq F$$.

*Proof of 3, which is the content.* Let $$p \in \overline{E}$$. If $$p \in E$$
then $$p \in F$$. Otherwise $$p$$ is a limit point of $$E$$; since
$$E \subseteq F$$, every neighbourhood of $$p$$ meets $$F$$ in a point other
than $$p$$, so $$p$$ is a limit point of $$F$$, and $$F$$ is closed, so
$$p \in F$$. $$\square$$

Clause 3 says $$\overline{E}$$ is **the smallest closed set containing
$$E$$** — the intersection of all of them. That is the definition to carry;
$$E \cup E'$$ is how you compute it.

**Definition.** $$D$$ is **dense** in $$X$$ when $$\overline{D} = X$$.

$$\mathbb{Q}$$ is dense in $$\mathbb{R}$$, which is the density theorem of
§1.5 restated: every real is a rational or a limit of rationals.

### Open subsets of the line

**Theorem.** Every open $$U \subseteq \mathbb{R}$$ is a finite or countable
union of pairwise disjoint open intervals.

*Proof sketch.* For $$x \in U$$ let $$I_x$$ be the union of all open intervals
containing $$x$$ and contained in $$U$$; this is itself an open interval — the
largest one around $$x$$ inside $$U$$ — called the *component* of $$x$$. Two
components are equal or disjoint, so the distinct ones partition $$U$$. Each
contains a rational by density, distinct components contain distinct
rationals, and $$\mathbb{Q}$$ is countable by §1.7, so there are at most
countably many. $$\square$$

The proof is a nice illustration of §1.7 earning its place: **countability of
$$\mathbb{Q}$$ is what bounds the number of pieces.** No such description holds
in $$\mathbb{R}^2$$, where open sets are not unions of disjoint discs.

### The relative topology

A subtlety that causes more confusion than any other in this chapter. Openness
is not absolute; it depends on the ambient space.

**Definition.** Let $$Y \subseteq X$$.

- $$U \subseteq Y$$ is **open in $$Y$$** when for every $$p \in U$$ there is
  $$\varepsilon > 0$$ with $$N_\varepsilon(p) \cap Y \subseteq U$$.
- $$C \subseteq Y$$ is **closed in $$Y$$** when $$Y \setminus C$$ is open in
  $$Y$$.

**Theorem.** For $$Y \subseteq X$$:

1. $$U \subseteq Y$$ is open in $$Y$$ $$\iff$$ $$U = Y \cap O$$ for some open
   $$O \subseteq X$$;
2. $$C \subseteq Y$$ is closed in $$Y$$ $$\iff$$ $$C = Y \cap F$$ for some
   closed $$F \subseteq X$$.

*Proof of 1.* ($$\Leftarrow$$) If $$U = Y \cap O$$ and $$p \in U$$, take
$$\varepsilon$$ with $$N_\varepsilon(p) \subseteq O$$; then
$$N_\varepsilon(p) \cap Y \subseteq U$$.

($$\Rightarrow$$) For each $$p \in U$$ choose $$\varepsilon_p$$ with
$$N_{\varepsilon_p}(p) \cap Y \subseteq U$$ and set
$$O = \bigcup_{p \in U} N_{\varepsilon_p}(p)$$, open as a union of open sets.
Then $$Y \cap O = U$$: each $$p \in U$$ lies in its own neighbourhood and in
$$Y$$, and conversely any point of $$Y \cap O$$ is in some
$$N_{\varepsilon_p}(p) \cap Y \subseteq U$$. $$\square$$

**The example to keep.** $$[0, \tfrac12)$$ is not open in $$\mathbb{R}$$, but
it *is* open in $$Y = [0,1]$$, because
$$[0,\tfrac12) = [0,1] \cap (-1, \tfrac12)$$. "Open" without naming the
ambient space is an incomplete sentence.

### Connectedness

**Definition.** $$A \subseteq X$$ is **connected** when there do **not** exist
disjoint open sets $$U, V$$ with

$$
A \cap U \ne \varnothing,\quad A \cap V \ne \varnothing,
$$

$$
(A \cap U) \cup (A \cap V) = A .
$$

In words: $$A$$ cannot be split into two nonempty pieces that are separated by
open sets. The definition is negative, which is normal — connectedness is the
absence of a decomposition.

**Theorem.** $$S \subseteq \mathbb{R}$$ is connected $$\iff$$ $$S$$ is an
interval.

*Proof.* ($$\Rightarrow$$) Suppose $$S$$ is not an interval. By the
order-convexity characterisation of §1.4 there are $$x, y \in S$$ and
$$t \notin S$$ with $$x < t < y$$. Then $$U = (-\infty, t)$$ and
$$V = (t, \infty)$$ are disjoint open sets separating $$S$$, so $$S$$ is not
connected.

($$\Leftarrow$$) Suppose $$S$$ is an interval and $$U, V$$ disconnect it. Pick
$$x \in S \cap U$$ and $$y \in S \cap V$$, say $$x < y$$. Then
$$[x,y] \subseteq S$$ by order-convexity. Let

$$
t = \sup\big( [x,y] \cap U \big),
$$

which exists by completeness. Now $$t \in [x,y] \subseteq S$$, so $$t$$ lies
in $$U$$ or in $$V$$. If $$t \in U$$, then $$U$$ open gives a whole
neighbourhood of $$t$$ inside $$U$$, so points slightly above $$t$$ are in
$$[x,y] \cap U$$ unless $$t = y$$ — and $$t = y$$ is impossible since
$$y \in V$$ and $$U, V$$ are disjoint. So $$t$$ was not an upper bound. If
$$t \in V$$, then $$V$$ open gives a neighbourhood of $$t$$ inside $$V$$, so
some $$\beta < t$$ is already an upper bound of $$[x,y] \cap U$$, contradicting
leastness. Either way, a contradiction. $$\square$$

Note which two ingredients that used: **order-convexity** from §1.4 and
**completeness**, through the supremum. Connectedness of intervals is another
face of the completeness axiom, and it is what makes the intermediate value
theorem true in [Chapter 4](/posts/analysis-continuity/).

---

## §2.3 Compact sets

### The definition, and what it is for

**Definition.** An **open cover** of $$E \subseteq X$$ is a collection
$$\{O_\alpha\}_{\alpha \in A}$$ of open subsets of $$X$$ with
$$E \subseteq \bigcup_{\alpha} O_\alpha$$.

**Definition.** $$K \subseteq X$$ is **compact** when every open cover of
$$K$$ has a **finite subcover**: for every open cover
$$\{O_\alpha\}_{\alpha \in A}$$ there are finitely many indices
$$\alpha_1, \ldots, \alpha_n$$ with

$$
K \subseteq \bigcup_{j=1}^{n} O_{\alpha_j} .
$$

> **Read the definition as a tool, not a property.** Compactness says: *any
> infinite amount of local information about $$K$$ can be reduced to a finite
> amount.* Every single use of it in this course is the same move — cover
> $$K$$ by neighbourhoods on which something good happens, extract a finite
> subcover, and then take a **minimum** or **maximum** over finitely many
> things, which exists, instead of an infimum or supremum over infinitely
> many, which may not be attained.
{: .prompt-tip }

### Basic properties

**Theorem.**

1. Every compact subset of a metric space is closed.
2. Every closed subset of a compact set is compact.

*Proof of 1.* Let $$K$$ be compact and $$p \notin K$$; we find a neighbourhood
of $$p$$ missing $$K$$. For each $$q \in K$$ put
$$r_q = \tfrac12 d(p,q) > 0$$. The neighbourhoods $$N_{r_q}(q)$$ cover $$K$$,
so finitely many do: $$K \subseteq \bigcup_{j=1}^{n} N_{r_{q_j}}(q_j)$$. Let
$$r = \min_j r_{q_j} > 0$$. Then $$N_r(p)$$ is disjoint from each
$$N_{r_{q_j}}(q_j)$$ — a point in both would make
$$d(p,q_j) < r + r_{q_j} \le 2r_{q_j} = d(p,q_j)$$ — and hence from $$K$$. So
$$K^{c}$$ is open. $$\square$$

There is the pattern, exactly as advertised: cover, extract a finite subcover,
take a minimum.

*Proof of 2.* Let $$F \subseteq K$$ be closed with $$K$$ compact, and let
$$\{O_\alpha\}$$ cover $$F$$. Adjoin the open set $$F^{c}$$ to get a cover of
$$K$$. Extract a finite subcover of $$K$$; discard $$F^{c}$$ from it if
present. What remains is a finite subcover of $$F$$. $$\square$$

**Corollary.** If $$F$$ is closed and $$K$$ compact, $$F \cap K$$ is compact —
it is a closed subset of $$K$$.

### Compactness and infinite sets

**Theorem.** If $$E$$ is an infinite subset of a compact set $$K$$, then $$E$$
has a limit point in $$K$$.

*Proof.* Suppose not: no point of $$K$$ is a limit point of $$E$$. Then each
$$q \in K$$ has a neighbourhood $$N_q$$ meeting $$E$$ in at most the single
point $$q$$. These cover $$K$$, so finitely many cover $$K$$, and hence cover
$$E$$. But each contributes at most one point of $$E$$, so $$E$$ is finite — a
contradiction. $$\square$$

**Theorem (nested compact sets).** If $$\{K_n\}$$ are nonempty compact sets
with $$K_n \supseteq K_{n+1}$$ for all $$n$$, then
$$K = \bigcap_{n=1}^{\infty} K_n$$ is nonempty and compact.

*Proof.* Compactness of $$K$$ is immediate: it is a closed subset of $$K_1$$.
For nonemptiness, suppose $$K = \varnothing$$. Then the open sets
$$O_n = K_n^{c}$$ cover $$K_1$$, so finitely many do, and since they increase,
$$K_1 \subseteq K_N^{c}$$ for a single $$N$$. But
$$K_N \subseteq K_1$$ and $$K_N \ne \varnothing$$, so $$K_N$$ meets $$K_1$$ —
a contradiction. $$\square$$

The nonemptiness is the useful half, and it is where the finite intersection
property lives: **compactness converts "every finite subfamily has a common
point" into "the whole family has a common point".**

---

## §2.4 Compact subsets of $$\mathbb{R}$$

### Heine–Borel

**Theorem (Heine–Borel).** Every closed bounded interval $$[a,b]$$ is compact.

*Proof.* Let $$\{O_\alpha\}$$ be an open cover of $$[a,b]$$ and set

$$
E = \{x \in [a,b] : [a,x] \text{ has a finite subcover}\} .
$$

$$E$$ is nonempty, since $$a \in E$$ — one set covers $$[a,a]$$ — and bounded
above by $$b$$, so $$c = \sup E$$ exists by completeness. We show $$c \in E$$
and $$c = b$$.

Since $$c \in [a,b]$$, some $$O_{\alpha_0}$$ contains $$c$$, and being open it
contains $$(c - \delta, c + \delta)$$ for some $$\delta > 0$$. Because $$c$$ is
the supremum, there is $$x \in E$$ with $$x > c - \delta$$, so $$[a,x]$$ has a
finite subcover; adjoining $$O_{\alpha_0}$$ covers $$[a, c]$$ — indeed it
covers $$[a, t]$$ for any $$t < c + \delta$$ in $$[a,b]$$.

So $$c \in E$$. And if $$c < b$$, the same finite collection covers
$$[a,t]$$ for some $$t$$ strictly between $$c$$ and $$\min(b, c+\delta)$$,
putting $$t \in E$$ with $$t > c$$ and contradicting the supremum. Hence
$$c = b$$ and $$[a,b] \in E$$. $$\square$$

> This is the single most important proof in the chapter, and it is pure
> completeness: the set $$E$$ of "already finitely covered" initial segments,
> its supremum, and the characterisation theorem of §1.4 saying nothing below
> the supremum is an upper bound. Heine–Borel is false in $$\mathbb{Q}$$, and
> this is where it breaks.
{: .prompt-warning }

### The equivalence

**Theorem (Heine–Borel–Bolzano–Weierstrass).** For $$K \subseteq \mathbb{R}$$
the following are equivalent.

1. $$K$$ is closed and bounded.
2. $$K$$ is compact.
3. Every infinite subset of $$K$$ has a limit point in $$K$$.

*Proof.* (1) $$\Rightarrow$$ (2): bounded means $$K \subseteq [a,b]$$ for some
interval, which is compact by Heine–Borel, and a closed subset of a compact set
is compact.

(2) $$\Rightarrow$$ (3): proved in §2.3.

(3) $$\Rightarrow$$ (1): if $$K$$ were unbounded, pick $$x_n \in K$$ with
$$\lvert x_n\rvert > n$$; the resulting infinite set has no limit point
anywhere. If $$K$$ were not closed, some limit point $$p$$ of $$K$$ lies
outside it; choosing $$x_n \in K$$ with $$\lvert x_n - p\rvert < 1/n$$ gives an
infinite subset whose only limit point is $$p \notin K$$. $$\square$$

**Theorem (Bolzano–Weierstrass).** Every bounded infinite subset of
$$\mathbb{R}$$ has a limit point.

*Proof.* A bounded set lies in some $$[a,b]$$, which is compact, so §2.3
applies. $$\square$$

### Up to $$\mathbb{R}^n$$

**Definition.** $$E \subseteq \mathbb{R}^n$$ is **bounded** when there is
$$M > 0$$ with $$d_2(p, 0) \le M$$ for all $$p \in E$$; equivalently
$$\lvert p_i \rvert \le M$$ for every coordinate of every $$p \in E$$.

The equivalence is the standard comparison between the Euclidean and max
metrics, $$\max_i \lvert p_i\rvert \le d_2(p,0) \le \sqrt{n}\max_i\lvert p_i\rvert$$.

**Theorem.** $$E \subseteq \mathbb{R}^n$$ is compact $$\iff$$ $$E$$ is closed
and bounded.

*Proof sketch.* The argument is Heine–Borel again with closed boxes
$$[a_1,b_1] \times \cdots \times [a_n,b_n]$$ in place of intervals, via
repeated bisection: if a box had no finite subcover, one of its $$2^n$$ halves
would not either, and the nested boxes shrink to a point which must lie in some
cover element — which then covers a whole small box, a contradiction.
$$\square$$

**Theorem (nested interval property).** If $$\{I_n\}$$ are nonempty closed
bounded intervals with $$I_n \supseteq I_{n+1}$$, then
$$\bigcap_{n=1}^{\infty} I_n = [a,b]$$ for some $$a \le b$$.

*Proof.* Write $$I_n = [a_n, b_n]$$. The $$a_n$$ increase and are bounded above
by every $$b_m$$, so $$a = \sup_n a_n$$ exists and $$a \le b := \inf_n b_n$$.
A point lies in every $$I_n$$ exactly when it is $$\ge$$ every $$a_n$$ and
$$\le$$ every $$b_n$$, i.e. exactly when it lies in $$[a,b]$$. $$\square$$

Nothing beyond completeness again — and this is the statement that
[Chapter 1](/posts/analysis-real-numbers/) used to prove $$[0,1]$$
uncountable.

---

## §2.5 The Cantor set

### Construction

Start with $$P_0 = [0,1]$$ and repeatedly delete open middle thirds:

$$
\begin{aligned}
P_1 &= \left[0,\tfrac13\right] \cup \left[\tfrac23, 1\right], \\
P_2 &= \left[0,\tfrac19\right] \cup \left[\tfrac29,\tfrac13\right] \\
 &\quad \cup \left[\tfrac23,\tfrac79\right] \cup \left[\tfrac89,1\right],
\end{aligned}
$$

and in general $$P_n = \bigcup_{j=1}^{2^n} J_{n,j}$$, a union of $$2^n$$ closed
intervals each of length $$3^{-n}$$. Each $$P_n$$ is a finite union of closed
bounded intervals, hence closed and bounded, hence compact. Since
$$P_0 \supseteq P_1 \supseteq \cdots$$, the **Cantor ternary set**

$$
P = \bigcap_{n=0}^{\infty} P_n
$$

is nonempty and compact by the nested-compact-sets theorem of §2.3.

### The seven properties

**1. $$P$$ is nonempty and compact.** Just established.

**2. $$P$$ contains every endpoint of every $$J_{n,k}$$.** Endpoints are never
removed: deletion takes open middle thirds, and an endpoint of $$J_{n,k}$$ is
an endpoint of some $$J_{m,j}$$ at every later stage.

**3. Every point of $$P$$ is a limit point of $$P$$.** Let $$x \in P$$ and
$$\varepsilon > 0$$. Choose $$n$$ with $$3^{-n} < \varepsilon$$. Then $$x$$
lies in some $$J_{n,j}$$, an interval of length $$3^{-n}$$ contained in
$$N_\varepsilon(x)$$, and both endpoints of $$J_{n,j}$$ are in $$P$$ by
property 2. At least one of them differs from $$x$$. $$\square$$

A set that is closed with no isolated points is called **perfect**. $$P$$ is
perfect and, by property 5, contains no interval — which is the combination
that makes it strange.

**4. The total length removed is $$1$$.** At stage $$n$$ we remove $$2^{n-1}$$
intervals of length $$3^{-n}$$, so the total is

$$
\begin{aligned}
\sum_{n=1}^{\infty} \frac{2^{n-1}}{3^{n}}
 &= \frac13 \sum_{k=0}^{\infty}\left(\frac23\right)^{k} \\
 &= \frac13 \cdot \frac{1}{1 - \tfrac23} = 1 .
\end{aligned}
$$

So $$P$$ has "length zero" in the sense of measure, while property 7 below
says it has as many points as $$[0,1]$$ itself.

**5. $$P$$ contains no interval.** An interval of positive length $$\ell$$
cannot fit inside $$P_n$$ once $$3^{-n} < \ell$$, since the pieces of $$P_n$$
are that short. So no interval survives into $$P$$.

**6. Ternary characterisation.** Writing $$x \in [0,1]$$ in base 3 as
$$x = 0.n_1n_2n_3\ldots$$,

$$
x \in P \iff n_k \in \{0,2\} \text{ for all } k
$$

for a suitable choice of expansion. Deleting the open middle third at stage
$$k$$ removes exactly the numbers whose $$k$$-th ternary digit must be $$1$$;
the endpoints survive because they admit a second expansion ending in
repeating $$2$$s, which is why "for a suitable choice" is needed — for example
$$\tfrac13 = 0.1000\ldots = 0.0222\ldots$$ and the second form qualifies.

**7. $$P$$ is uncountable.** By property 6, $$P$$ is in bijection with the set
of all sequences in $$\{0,2\}$$, which is in bijection with the set of all
sequences in $$\{0,1\}$$, shown uncountable by Cantor's diagonal argument in
§1.7. $$\square$$

> **Why the Cantor set is in the course.** Every property above contradicts an
> intuition picked up earlier. It is uncountable yet has total length zero — so
> cardinality and size are unrelated. It has no isolated points yet contains no
> interval — so "no gaps locally" does not mean "solid". It is compact,
> perfect, and totally disconnected at once. Keep it as the standard test of
> any conjecture about subsets of $$\mathbb{R}$$.
{: .prompt-warning }

## Worked examples

**1. A set that is neither open nor closed.** $$[0,1) \subseteq \mathbb{R}$$.
Not open: $$0$$ is not interior, since every $$N_\varepsilon(0)$$ contains
negative numbers. Not closed: $$1$$ is a limit point not belonging to it.

**2. The discrete metric.** On any set $$X$$ put $$d(x,y) = 1$$ for
$$x \ne y$$ and $$0$$ otherwise. Then $$N_{1/2}(p) = \{p\}$$, so every subset
is open, hence every subset is closed, and there are no limit points at all.
Which subsets are compact? Only the finite ones: the cover by singletons has a
finite subcover exactly when $$K$$ is finite. So in a general metric space,
"closed and bounded" does **not** imply compact — $$X$$ itself is closed and
bounded in the discrete metric and is not compact when infinite. Heine–Borel is
a theorem about $$\mathbb{R}^n$$, not about metric spaces.

**3. Where the finite subcover is forced.** Show directly that $$(0,1]$$ is not
compact. The sets $$O_n = (1/n, 2)$$ for $$n \in \mathbb{N}$$ are open and
cover $$(0,1]$$, since every $$x > 0$$ exceeds some $$1/n$$. Any finite
subfamily has a largest index $$N$$ and so covers only $$(1/N, 1]$$, missing
points near $$0$$. The failure is exactly the missing endpoint, which is to say
exactly the failure of closedness.

**4. Interior, closure, limit points of $$\mathbb{Q}$$ in $$\mathbb{R}$$.**
$$\operatorname{Int}(\mathbb{Q}) = \varnothing$$, since every interval contains
irrationals. $$\mathbb{Q}' = \mathbb{R}$$ and
$$\overline{\mathbb{Q}} = \mathbb{R}$$, by density. So $$\mathbb{Q}$$ is
dense with empty interior — the two are compatible, and the Cantor set is the
opposite extreme: closed with empty interior and *not* dense.

## Common pitfalls

- **Treating "open" and "closed" as opposites.** Sets can be both or neither.
  The negation of open is "some point is not interior", not "closed".
- **Forgetting the ambient space.** $$[0,\tfrac12)$$ is open in $$[0,1]$$ and
  not in $$\mathbb{R}$$. Always say open *in what*.
- **Intersecting infinitely many open sets.** The theorem says finitely many,
  and $$\bigcap_n(-1/n, 1/n) = \{0\}$$ shows why.
- **Dropping $$q \ne p$$ from the definition of a limit point.** Without it
  every point of $$E$$ is a limit point and isolated points disappear.
- **Believing closed and bounded implies compact.** True in $$\mathbb{R}^n$$
  and false in general; the discrete metric is the counterexample to keep.
- **Thinking compactness is about size.** A compact set can be uncountable
  (the Cantor set, $$[0,1]$$) and a non-compact set can be countable
  ($$\mathbb{N}$$ in $$\mathbb{R}$$, or $$\{1/n\}$$ without its limit point).
- **Confusing $$\overline{E}$$ with $$E'$$.** The closure includes the isolated
  points of $$E$$; the derived set $$E'$$ does not.
- **Assuming a perfect set must contain an interval.** The Cantor set is the
  standing refutation.

## Connections

- **Backward.** The supremum of [Chapter 1](/posts/analysis-real-numbers/)
  drives the Heine–Borel proof, the connectedness theorem and the nested
  interval property; countability of $$\mathbb{Q}$$ bounds the components of an
  open subset of $$\mathbb{R}$$; and Cantor's diagonal argument returns to show
  $$P$$ uncountable.
- **Forward.** [Chapter 3](/posts/analysis-sequences/) redoes limit points in
  the language of sequences, and the Bolzano–Weierstrass theorem reappears as a
  statement about subsequences.
  [Chapter 4](/posts/analysis-continuity/) defines continuity by inverse images
  of open sets, proves that continuous images of compact sets are compact —
  giving the extreme value theorem — and that continuous images of connected
  sets are connected, giving the intermediate value theorem. Both of this
  chapter's structural properties exist to be pushed through a continuous map.
- **Outward.** Dropping the metric and keeping only the behaviour of open sets
  under arbitrary unions and finite intersections gives general topology.
  Dropping the intervals and keeping the total-length computation of property 4
  gives measure theory.

## Summary

- **Metric** — $$d \ge 0$$ with $$d = 0$$ only on the diagonal, symmetric, triangle inequality
- **Neighbourhood** — $$N_\varepsilon(p) = \{x : d(p,x) < \varepsilon\}$$, and it is open
- **Open** — every point interior; **closed** — complement open; neither is the negation of the other
- **Unions and intersections** — arbitrary unions of open, finite intersections of open
- **Limit point** — every neighbourhood meets $$E$$ away from $$p$$; then it meets it infinitely often
- **Closed** $$\iff$$ contains its limit points $$\iff$$ equals its closure
- **Closure** — $$\overline{E} = E \cup E'$$, the smallest closed set containing $$E$$
- **Open in $$Y$$** — exactly the sets $$Y \cap O$$ with $$O$$ open in $$X$$
- **Connected in $$\mathbb{R}$$** $$\iff$$ an interval
- **Compact** — every open cover has a finite subcover; used to replace a sup by a max
- **Compact $$\Rightarrow$$ closed**; closed subset of compact is compact
- **Heine–Borel** — in $$\mathbb{R}^n$$, compact $$\iff$$ closed and bounded; false in general metric spaces
- **Nested compacts** have a common point
- **Cantor set** — compact, perfect, uncountable, no intervals, total length removed $$1$$

## References

- Manfred Stoll, *Introduction to Real Analysis*, 2nd edition — the metric space and point-set material, §§2.1–2.5 in this course's numbering.
- Introduction to Mathematical Analysis, Spring 2023. Instructor: Ja A Jeong. Handwritten summary notes for Chapters 1 to 3.
- As in [Chapter 1](/posts/analysis-real-numbers/), the notes give definitions and theorem statements and leave every proof blank. All proofs above are mine. The characterisation of open subsets of $$\mathbb{R}$$ and the $$\mathbb{R}^n$$ form of Heine–Borel are sketched rather than written out; everything else that the notes marked as a theorem is proved.
- The worked examples, the discrete-metric counterexample and the remarks on what compactness is *for* are mine; the handwritten notes carry no exercises.
- The notes write the open and closed set definitions for subsets of $$\mathbb{R}$$ specifically, then use them for general metric spaces throughout. They are stated here for a general $$(X,d)$$ from the start, which is how they are used.
