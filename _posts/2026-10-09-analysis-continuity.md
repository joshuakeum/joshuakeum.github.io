---
title: "Mathematical Analysis: Limits and Continuity"
date: 2026-10-09 10:00:00 +0900
categories: [Course Notes, Mathematical Analysis]
tags: [limits, continuity, uniform continuity, compactness, intermediate value theorem, discontinuities]
description: Limits of functions and the sequential criterion, continuity and its topological characterization, what compactness and connectedness give when pushed through a continuous map, uniform continuity, and the classification of discontinuities. Chapter 4 of Introduction to Mathematical Analysis.
math: true
mermaid: false
render_with_liquid: false
---

> This chapter covers §§4.1–4.4. From here the course notes are the typed
> workbook: definitions and theorem statements in full, every proof and every
> exercise left as blank space. The proofs and the exercise solutions below
> are mine.
{: .prompt-info }

## What this chapter answers

Everything so far has been about *sets*. This chapter is about *maps between
them*, and it asks one question in three forms.

**What does continuity preserve?** The $$\varepsilon$$–$$\delta$$ definition is
a local statement and tells you nothing on its own. The content of the chapter
is that continuity pushes the two structural properties of
[Chapter 2](/posts/analysis-metric-spaces/) forward through the map:

- continuous image of a **compact** set is compact — and in $$\mathbb{R}$$ that
  is the **extreme value theorem**;
- continuous image of a **connected** set is connected — and in $$\mathbb{R}$$
  that is the **intermediate value theorem**.

Both of the "obvious" theorems from first-year calculus turn out to be one line
each, once the right property is in place. That is the payoff for Chapter 2.

The second thread is a distinction that first-year calculus never makes.
Continuity lets $$\delta$$ depend on the point; **uniform continuity** does
not. The difference is a quantifier order, it is invisible on any picture, and
on a compact set it vanishes entirely.

## Prerequisites

[Chapter 2](/posts/analysis-metric-spaces/) for neighbourhoods, open sets,
compactness and connectedness; [Chapter 3](/posts/analysis-sequences/) for
convergence, the algebra of limits and Cauchy sequences;
[Chapter 1](/posts/analysis-real-numbers/) for suprema and countability.

---

## Part 1 — §4.1: the limit of a function

### The definition

**Definition.** Let $$(X,d)$$ be a metric space, $$E \subseteq X$$,
$$f : E \to \mathbb{R}$$, and let $$p$$ be a **limit point of $$E$$**. Then
$$f$$ **has a limit $$L$$ at $$p$$** when

$$
\begin{aligned}
\forall \varepsilon > 0,\ \exists \delta > 0 \text{ such that } \\
\lvert f(x) - L\rvert < \varepsilon
\text{ whenever } 0 < d(x,p) < \delta ,
\end{aligned}
$$

equivalently $$f(x) \in N_\varepsilon(L)$$ for every
$$x \in E \cap \big(N_\delta(p)\setminus\{p\}\big)$$. We write
$$\lim_{x \to p} f(x) = L$$.

Three conditions in that definition do real work.

- **$$p$$ must be a limit point of $$E$$.** Otherwise some punctured
  neighbourhood of $$p$$ misses $$E$$ entirely, the condition is vacuous, and
  every $$L$$ would be a limit.
- **$$p$$ need not be in $$E$$.** Limits are about approach, not arrival.
- **$$0 < d(x,p)$$ excludes $$x = p$$.** The value $$f(p)$$, if it exists at
  all, is irrelevant to the limit. That gap between $$\lim_{x\to p} f$$ and
  $$f(p)$$ is exactly what continuity closes.

### The sequential criterion

**Theorem.** With $$E$$, $$p$$, $$f$$ as above,

$$
\lim_{x\to p} f(x) = L
$$

if and only if $$f(p_n) \to L$$ for **every** sequence $$\{p_n\}$$ in $$E$$
with $$p_n \ne p$$ and $$p_n \to p$$.

*Proof.* ($$\Rightarrow$$) Given $$\varepsilon$$, take $$\delta$$ from the
definition and then $$n_0$$ with $$d(p_n,p) < \delta$$ for $$n \ge n_0$$. Since
$$p_n \ne p$$ we have $$0 < d(p_n,p) < \delta$$, so
$$\lvert f(p_n) - L\rvert < \varepsilon$$.

($$\Leftarrow$$) Contrapositive. If the limit fails, there is
$$\varepsilon_0 > 0$$ such that no $$\delta$$ works. Taking
$$\delta = 1/n$$ gives $$p_n \in E$$ with $$0 < d(p_n, p) < 1/n$$ and
$$\lvert f(p_n) - L\rvert \ge \varepsilon_0$$. Then $$p_n \to p$$ with
$$p_n \ne p$$, and $$f(p_n) \not\to L$$. $$\square$$

> **This theorem is the chapter's main labour-saving device.** It converts
> every statement about function limits into a statement about sequence limits,
> so the whole of [Chapter 3](/posts/analysis-sequences/) becomes available at
> no cost. It is also the standard way to prove a limit does **not** exist:
> produce two sequences approaching $$p$$ along which $$f$$ tends to different
> values.
{: .prompt-tip }

**Corollary.** If $$f$$ has a limit at $$p$$, the limit is unique.

Immediate from uniqueness of sequence limits.

### Limit theorems

**Theorem.** If $$\lim_{x\to p} f(x) = A$$ and $$\lim_{x\to p} g(x) = B$$, then

$$
\begin{aligned}
\lim_{x\to p}\,[f + g] &= A + B, \\
\lim_{x\to p}\,[fg] &= AB, \\
\lim_{x\to p}\,\frac{f}{g} &= \frac{A}{B} \quad (B \ne 0).
\end{aligned}
$$

*Proof.* Apply the sequential criterion and the algebra of limits from §3.2.
$$\square$$

That is the entire proof, and it is the reason the sequential criterion was
proved first.

**Definition.** $$f$$ is **bounded on $$E$$** when there is $$M$$ with
$$\lvert f(x)\rvert \le M$$ for all $$x \in E$$.

**Theorem.** If $$g$$ is bounded on $$E$$ and
$$\lim_{x\to p} f(x) = 0$$, then $$\lim_{x\to p} f(x)g(x) = 0$$.

**Theorem (squeeze).** If $$g \le f \le h$$ on $$E$$ and
$$\lim_{x\to p} g = \lim_{x\to p} h = L$$, then $$\lim_{x\to p} f = L$$.

Both transfer from §3.2 the same way. Note again that $$g$$ is only required
to be *bounded*, not convergent — which is what makes the first one the right
tool against an oscillating factor.

### Limits at infinity

**Definition.** Let $$f$$ be real-valued with
$$\operatorname{Dom} f \cap (a,\infty) \ne \varnothing$$ for every
$$a \in \mathbb{R}$$. Then $$\lim_{x\to\infty} f(x) = L$$ when for every
$$\varepsilon > 0$$ there is $$M \in \mathbb{R}$$ such that

$$
x \in \operatorname{Dom} f,\ x > M \implies \lvert f(x) - L\rvert < \varepsilon .
$$

The shape is the same with "$$x > M$$" replacing "$$0 < d(x,p) < \delta$$":
*eventually, within tolerance.* The hypothesis on the domain is the analogue of
"$$p$$ is a limit point" — it stops the condition from being vacuous.

### Suggested exercises

**3(d). Does $$\displaystyle\lim_{x\to0}\sqrt{\lvert x\rvert}\cos\frac1x$$
exist?**

Yes, and it is $$0$$. The cosine factor is bounded by $$1$$ and
$$\sqrt{\lvert x\rvert} \to 0$$, so bounded-times-null applies:

$$
\left\lvert \sqrt{\lvert x\rvert}\cos\tfrac1x \right\rvert \le \sqrt{\lvert x\rvert} \to 0 .
$$

The cosine has no limit at $$0$$ whatsoever, which is precisely why the
*bounded* hypothesis rather than a convergence hypothesis is the one to reach
for.

**8(d). $$\displaystyle\lim_{x\to-2}\frac{\lvert x+2\rvert^{3/2}}{x+2}$$.**

Put $$t = x+2 \to 0$$. For $$t > 0$$ the quotient is
$$t^{3/2}/t = t^{1/2}$$; for $$t < 0$$ it is
$$\lvert t\rvert^{3/2}/t = -\lvert t\rvert^{1/2}$$. Both tend to $$0$$, so the
limit is $$0$$.

Had the exponent been $$1$$ instead of $$3/2$$ the two sides would have given
$$+1$$ and $$-1$$ and the limit would not exist. The extra half power is what
kills the sign.

**10. If $$f$$ has a limit at $$p$$, then $$f$$ is bounded near $$p$$:
there are $$M > 0$$ and $$\delta > 0$$ with $$\lvert f(x)\rvert \le M$$ for all
$$x \in E$$ with $$0 < d(x,p) < \delta$$.**

Take $$\varepsilon = 1$$ in the definition, giving $$\delta$$ with
$$\lvert f(x) - L\rvert < 1$$ on the punctured ball. Then

$$
\lvert f(x)\rvert \le \lvert L\rvert + \lvert f(x) - L\rvert < \lvert L\rvert + 1 =: M .
$$

$$\square$$

Choosing a *specific* $$\varepsilon$$ — here $$1$$ — is the move. The
definition gives you a statement for every $$\varepsilon$$; a boundedness claim
only needs one.

**17(e). $$\displaystyle\lim_{x\to\infty}\left(\sqrt{x^2+x} - x\right)$$.**

Multiply by the conjugate:

$$
\begin{aligned}
\sqrt{x^2+x} - x
 &= \frac{x^2 + x - x^2}{\sqrt{x^2+x}+x} \\
 &= \frac{x}{\sqrt{x^2+x}+x}
 = \frac{1}{\sqrt{1 + 1/x} + 1} ,
\end{aligned}
$$

dividing through by $$x > 0$$. As $$x \to \infty$$ this tends to
$$\tfrac12$$.

**18. If $$f : (a,\infty) \to \mathbb{R}$$ has
$$\lim_{x\to\infty} x f(x) = L \in \mathbb{R}$$, then
$$\lim_{x\to\infty} f(x) = 0$$.**

For $$x > 0$$, $$f(x) = \frac1x \cdot \big(x f(x)\big)$$. The second factor
converges, so it is bounded for large $$x$$ — by exercise 10's argument with
$$\varepsilon = 1$$ — and the first tends to $$0$$. Bounded times null gives
$$0$$. $$\square$$

---

## Part 2 — §4.2: continuous functions

### The definition

> The notes head this section "IV. 2 Limit of a Function", repeating the
> previous title. The content is continuity, and that is what it is called
> here.
{: .prompt-info }

**Definition.** Let $$E \subseteq (X,d)$$ and $$f : E \to \mathbb{R}$$. Then
$$f$$ is **continuous at $$p \in E$$** when

$$
\begin{aligned}
\forall \varepsilon > 0,\ \exists \delta > 0 \text{ such that } \\
\lvert f(x) - f(p)\rvert < \varepsilon \text{ whenever } d(x,p) < \delta ,
\end{aligned}
$$

and **continuous on $$E$$** when it is continuous at every $$p \in E$$.

Compare with the limit definition. Two changes: the limit value $$L$$ is
replaced by the actual value $$f(p)$$, and the exclusion $$0 < d(x,p)$$ is
dropped. Both are needed, and both carry consequences.

**Remark.**

1. If $$p \in E$$ is also a limit point of $$E$$, then $$f$$ is continuous at
   $$p$$ exactly when $$\lim_{x\to p} f(x) = f(p)$$. Equivalently, by the
   sequential criterion, exactly when $$f(p_n) \to f(p)$$ for **every**
   sequence $$p_n \to p$$ in $$E$$ — now with no requirement that
   $$p_n \ne p$$.
2. If $$p$$ is an **isolated point** of $$E$$, then *every* function on $$E$$
   is continuous at $$p$$. Choosing $$\delta$$ small enough that
   $$N_\delta(p) \cap E = \{p\}$$ makes the condition read
   $$\lvert f(p) - f(p)\rvert < \varepsilon$$.

Remark 2 is worth not skipping. It means continuity is interesting only at
limit points, and it is why a function on $$\mathbb{Z}$$ is automatically
continuous.

### Three examples from the notes

**Show that $$f(x) = \sin x$$ is continuous on $$\mathbb{R}$$.** From the
sum-to-product identity,

$$
\begin{aligned}
\lvert \sin x - \sin p\rvert
 &= 2\left\lvert \cos\tfrac{x+p}{2}\right\rvert \left\lvert\sin\tfrac{x-p}{2}\right\rvert \\
 &\le 2\left\lvert \sin\tfrac{x-p}{2}\right\rvert
 \le \lvert x - p\rvert ,
\end{aligned}
$$

using $$\lvert\cos\rvert \le 1$$ and $$\lvert \sin t\rvert \le \lvert t\rvert$$.
So $$\delta = \varepsilon$$ works at every $$p$$ — and the same $$\delta$$ at
every $$p$$, which is the point of §4.3.

**A function on $$(0,1)$$ discontinuous at every rational and continuous at
every irrational.** Thomae's function:

$$
f(x) = \begin{cases}
1/q, & x = p/q \text{ in lowest terms} \\
0, & x \text{ irrational}
\end{cases}
$$

At a rational $$p/q$$ the value is $$1/q > 0$$ while irrationals arbitrarily
close give $$0$$, so $$f$$ is discontinuous there. At an irrational $$x_0$$,
given $$\varepsilon > 0$$ there are only finitely many rationals in $$(0,1)$$
with denominator below $$1/\varepsilon$$; choose $$\delta$$ smaller than the
distance from $$x_0$$ to all of them. Then every point within $$\delta$$ has
$$f$$-value below $$\varepsilon$$, and $$f(x_0) = 0$$.

> The reverse — continuous at every rational and discontinuous at every
> irrational — is **impossible**. The set of continuity points of any function
> is a countable intersection of open sets, and the irrationals are such a set
> while the rationals are not. That is beyond this course, but it is worth
> knowing that the asymmetry in the exercise is real and not an accident of
> construction.
{: .prompt-tip }

**Prove or disprove: a function must be constant for its limit to be the same
at every point of its domain.** Disproved. Take

$$
f(x) = \begin{cases} 1, & x = 0 \\ 0, & x \ne 0\end{cases}
$$

on $$\mathbb{R}$$. Then $$\lim_{x\to p} f(x) = 0$$ for every $$p$$, including
$$p = 0$$, since the limit ignores the value at the point. But $$f$$ is not
constant. Changing a function at one point changes no limit anywhere.

### Compositions

**Theorem.** Let $$A, B \subseteq \mathbb{R}$$, $$f : A \to \mathbb{R}$$ with
$$\operatorname{Range} f \subseteq B$$, and $$g : B \to \mathbb{R}$$. If
$$f$$ is continuous at $$p$$ and $$g$$ is continuous at $$f(p)$$, then
$$g \circ f$$ is continuous at $$p$$.

*Proof.* Given $$\varepsilon > 0$$, continuity of $$g$$ at $$f(p)$$ gives
$$\eta > 0$$ with $$\lvert g(y) - g(f(p))\rvert < \varepsilon$$ whenever
$$\lvert y - f(p)\rvert < \eta$$. Continuity of $$f$$ at $$p$$ gives
$$\delta > 0$$ with $$\lvert f(x) - f(p)\rvert < \eta$$ whenever
$$\lvert x - p\rvert < \delta$$. Chain them. $$\square$$

The corresponding statement for *limits* is false without extra hypotheses,
which is one more reason continuity is the better-behaved notion: there is no
punctured neighbourhood to worry about, because $$f(x)$$ is allowed to equal
$$f(p)$$.

### The topological characterisation

**Theorem.** Let $$E \subseteq (X,d)$$ and $$f : E \to \mathbb{R}$$. Then

$$
f \text{ is continuous on } E
$$

if and only if $$f^{-1}(V)$$ is open in $$E$$ for every open
$$V \subseteq \mathbb{R}$$.

*Proof.* ($$\Rightarrow$$) Let $$V$$ be open and $$p \in f^{-1}(V)$$. Since
$$V$$ is open there is $$\varepsilon > 0$$ with
$$N_\varepsilon(f(p)) \subseteq V$$; continuity gives $$\delta$$ with
$$f(N_\delta(p) \cap E) \subseteq N_\varepsilon(f(p)) \subseteq V$$, so
$$N_\delta(p) \cap E \subseteq f^{-1}(V)$$ — which is exactly openness in
$$E$$.

($$\Leftarrow$$) Given $$p \in E$$ and $$\varepsilon > 0$$, the set
$$V = N_\varepsilon(f(p))$$ is open, so $$f^{-1}(V)$$ is open in $$E$$ and
contains $$p$$; take $$\delta$$ with
$$N_\delta(p) \cap E \subseteq f^{-1}(V)$$. $$\square$$

> **Why this is the definition that matters.** It mentions no $$\varepsilon$$,
> no $$\delta$$, and no metric — only open sets. It is therefore the
> definition that survives into general topology, and it is the reason
> [Chapter 1](/posts/analysis-real-numbers/) made such a fuss about inverse
> images commuting with everything while images do not. Continuity is defined
> by preimages because preimages behave.
{: .prompt-warning }

**Remark.** The forward direction is false: $$f$$ continuous and $$V$$ open in
$$E$$ do **not** give $$f(V)$$ open in $$\operatorname{Range} f$$. Take

$$
E = \{0\} \cup (1,2), \qquad
f(0) = \tfrac32, \quad f(x) = x \text{ on } (1,2).
$$

Then $$f$$ is continuous on $$E$$ — $$0$$ is isolated — and
$$\operatorname{Range} f = (1,2)$$. The set $$V = \{0\}$$ is open in $$E$$,
being an isolated point, and $$f(V) = \{\tfrac32\}$$ is a single point, not
open in $$(1,2)$$.

### Continuity and compactness

**Theorem.** If $$K$$ is a compact subset of a metric space and
$$f : K \to \mathbb{R}$$ is continuous, then $$f(K)$$ is compact.

*Proof.* Let $$\{V_\alpha\}$$ be an open cover of $$f(K)$$. Each
$$f^{-1}(V_\alpha)$$ is open in $$K$$, so $$f^{-1}(V_\alpha) = K \cap O_\alpha$$
for some open $$O_\alpha \subseteq X$$, by the relative topology theorem of
§2.2. The $$O_\alpha$$ cover $$K$$, so finitely many do, say
$$O_{\alpha_1}, \ldots, O_{\alpha_n}$$. Then
$$V_{\alpha_1}, \ldots, V_{\alpha_n}$$ cover $$f(K)$$: any
$$y = f(x) \in f(K)$$ has $$x \in O_{\alpha_j}$$ for some $$j$$, and
$$x \in K$$, so $$x \in f^{-1}(V_{\alpha_j})$$. $$\square$$

**Corollary (extreme value theorem).** If $$K \subseteq \mathbb{R}$$ is compact
and $$f : K \to \mathbb{R}$$ is continuous, there are $$p, q \in K$$ with

$$
f(q) \le f(x) \le f(p) \quad \text{for all } x \in K .
$$

*Proof.* $$f(K)$$ is compact in $$\mathbb{R}$$, hence closed and bounded by
Heine–Borel. Bounded gives $$\sup f(K)$$ and $$\inf f(K)$$ in $$\mathbb{R}$$;
closed gives that both belong to $$f(K)$$, since each is a limit point of it
or a member of it. So both are attained. $$\square$$

**A continuous function on a compact set attains its maximum and its minimum.**
Both hypotheses are needed and both fail instructively: $$f(x) = x$$ on
$$(0,1)$$ is continuous on a non-compact set and attains neither; and
$$f(x) = 1/x$$ on $$(0,1]$$ is continuous and not even bounded.

### Continuity and connectedness

**Theorem (intermediate value theorem).** Let $$f : [a,b] \to \mathbb{R}$$ be
continuous with $$f(a) < f(b)$$. Then for every $$\gamma$$ with
$$f(a) < \gamma < f(b)$$ there is $$c \in (a,b)$$ with $$f(c) = \gamma$$.

*Proof.* Let $$S = \{x \in [a,b] : f(x) < \gamma\}$$. It is nonempty
($$a \in S$$) and bounded above by $$b$$, so $$c = \sup S$$ exists. Continuity
at $$c$$ rules out both $$f(c) < \gamma$$ and $$f(c) > \gamma$$: in the first
case $$f$$ stays below $$\gamma$$ on a whole neighbourhood of $$c$$, putting
points of $$S$$ above $$c$$ — impossible unless $$c = b$$, which is excluded
because $$f(b) > \gamma$$; in the second case $$f$$ stays above $$\gamma$$ near
$$c$$, so some $$\beta < c$$ already bounds $$S$$. Hence $$f(c) = \gamma$$, and
$$c \ne a, b$$ since $$f(a) < \gamma < f(b)$$. $$\square$$

**Corollary.** If $$I \subseteq \mathbb{R}$$ is an interval and
$$f : I \to \mathbb{R}$$ is continuous, then $$f(I)$$ is an interval —
equivalently, the continuous image of a connected set is connected.

The two statements of the corollary are the same because of the theorem in
§2.2 identifying the connected subsets of $$\mathbb{R}$$ with the intervals.
The structural proof is short: if $$U, V$$ disconnected $$f(I)$$, then
$$f^{-1}(U)$$ and $$f^{-1}(V)$$ would disconnect $$I$$.

> **Both great theorems of this section have the same shape.** Take a
> structural property of the domain — compact, connected — and push it through
> the map. The $$\varepsilon$$–$$\delta$$ definition is never used directly;
> the topological characterisation does all the work. This is what
> [Chapter 2](/posts/analysis-metric-spaces/) was for.
{: .prompt-tip }

### Suggested exercises

**1(c). Is $$g$$ continuous at $$x_0 = 0$$, where
$$g(x) = \frac{1-\cos x}{x}$$ for $$x \ne 0$$ and $$g(0) = 0$$?**

Yes. Using $$1 - \cos x = 2\sin^2(x/2)$$,

$$
\begin{aligned}
\frac{1-\cos x}{x} &= \frac{2\sin^2(x/2)}{x}
 = \sin\tfrac x2 \cdot \frac{\sin(x/2)}{x/2} \\
 &\to 0 \cdot 1 = 0 ,
\end{aligned}
$$

which equals $$g(0)$$.

**3. $$f(x) = x^2$$ for $$x \in \mathbb{Q}$$ and $$f(x) = x+2$$ for
$$x \notin \mathbb{Q}$$. Where is $$f$$ continuous?**

Exactly at $$x = 2$$ and $$x = -1$$.

Suppose $$f$$ is continuous at $$p$$. Both $$\mathbb{Q}$$ and its complement
are dense, so there are rationals $$r_n \to p$$ and irrationals
$$s_n \to p$$. Continuity forces

$$
p^2 = \lim f(r_n) = f(p) = \lim f(s_n) = p + 2 ,
$$

so $$p^2 - p - 2 = 0$$, i.e. $$p = 2$$ or $$p = -1$$.

Conversely at such a $$p$$ the two formulas agree, and for any $$x$$,

$$
\lvert f(x) - f(p)\rvert \le \max\left(\lvert x^2 - p^2\rvert,\ \lvert x - p\rvert\right),
$$

both of which are small when $$x$$ is near $$p$$. So $$f$$ is continuous there.
$$\square$$

**14. If $$f, g : E \to \mathbb{R}$$ are continuous at $$p$$, so are
$$\max\{f,g\}$$, $$\min\{f,g\}$$ and $$f^{+}$$.**

Write them algebraically:

$$
\begin{aligned}
\max\{f,g\} &= \tfrac12\big(f + g + \lvert f-g\rvert\big), \\
\min\{f,g\} &= \tfrac12\big(f + g - \lvert f-g\rvert\big), \\
f^{+} &= \max\{f,0\} = \tfrac12\big(f + \lvert f\rvert\big).
\end{aligned}
$$

Sums and scalar multiples of continuous functions are continuous, and
$$\lvert\cdot\rvert$$ is continuous on $$\mathbb{R}$$ — by the reverse triangle
inequality it is Lipschitz with constant $$1$$ — so each is a composition and
combination of continuous functions. $$\square$$

The identity $$\max(a,b) = \frac12(a+b+\lvert a-b\rvert)$$ is worth
remembering; it converts a case distinction into arithmetic, which is what
makes the proof one line.

**16. Every polynomial of odd degree has a real root.**

Let $$p(x) = a_nx^n + \cdots + a_0$$ with $$n$$ odd and $$a_n \ne 0$$; dividing
by $$a_n$$ we may assume $$a_n = 1$$. For large $$\lvert x\rvert$$,

$$
p(x) = x^n\left(1 + \frac{a_{n-1}}{x} + \cdots + \frac{a_0}{x^n}\right),
$$

and the bracket tends to $$1$$, so it is positive once $$\lvert x\rvert$$ is
large. Since $$n$$ is odd, $$x^n > 0$$ for large positive $$x$$ and
$$x^n < 0$$ for large negative $$x$$. So there are $$a < b$$ with $$p(a) < 0$$
and $$p(b) > 0$$, and the intermediate value theorem supplies
$$c \in (a,b)$$ with $$p(c) = 0$$. $$\square$$

Oddness is exactly what makes the two ends disagree in sign; $$x^2 + 1$$ shows
the statement fails for even degree.

**19. $$F = \{x \in E : f(x) = 0\}$$ is closed in $$E$$. Is it closed in
$$\mathbb{R}$$?**

$$F = f^{-1}(\{0\})$$ and $$\{0\}$$ is closed in $$\mathbb{R}$$, so
$$F$$ is closed in $$E$$ by the topological characterisation applied to the
complement.

Not necessarily closed in $$\mathbb{R}$$: take $$E = (0,1)$$ and $$f \equiv 0$$.
Then $$F = (0,1)$$, which is closed in $$E$$ — it is all of it — and not closed
in $$\mathbb{R}$$. The relative topology warning of §2.2, doing its job.

**21. If $$f$$ is continuous at $$p$$ and $$f(p) > 0$$, then $$f \ge \alpha$$
near $$p$$ for some $$\alpha > 0$$.**

Take $$\varepsilon = f(p)/2 > 0$$ in the definition, giving $$\delta$$ with
$$\lvert f(x) - f(p)\rvert < f(p)/2$$ on $$N_\delta(p) \cap E$$. Then

$$
f(x) > f(p) - \tfrac{f(p)}{2} = \tfrac{f(p)}{2} =: \alpha .
$$

$$\square$$

**22. If $$f$$ is continuous at $$p$$, then $$f$$ is bounded near $$p$$.**

Same move with $$\varepsilon = 1$$:
$$\lvert f(x)\rvert \le \lvert f(p)\rvert + 1 =: M$$ on
$$E \cap N_\delta(p)$$. $$\square$$

Exercises 21 and 22 are the same technique as exercise 10 of §4.1, and the
technique is: **a qualitative conclusion follows from one well-chosen
$$\varepsilon$$.**

**25 and 28.** These are the compactness and connectedness theorems proved
above.

**29. $$K$$ compact, $$f$$ real-valued on $$K$$, and for each $$x \in K$$ there
is $$\varepsilon_x > 0$$ with $$f$$ bounded on $$N_{\varepsilon_x}(x) \cap K$$.
Then $$f$$ is bounded on $$K$$.**

The sets $$N_{\varepsilon_x}(x)$$ for $$x \in K$$ form an open cover of $$K$$,
so finitely many suffice: $$K \subseteq \bigcup_{j=1}^{n} N_{\varepsilon_{x_j}}(x_j)$$.
Let $$M_j$$ bound $$\lvert f\rvert$$ on $$N_{\varepsilon_{x_j}}(x_j) \cap K$$
and set $$M = \max_j M_j$$, which exists because there are finitely many. Then
$$\lvert f\rvert \le M$$ on $$K$$. $$\square$$

Note that $$f$$ is not assumed continuous. The exercise isolates what the
extreme value theorem really uses: **locally bounded plus compact gives
globally bounded**, and continuity enters only to supply local boundedness.

---

## Part 3 — §4.3: uniform continuity

### The quantifier that moves

**Definition.** Let $$E \subseteq (X,d)$$ and $$f : E \to \mathbb{R}$$. Then
$$f$$ is **uniformly continuous on $$E$$** when

$$
\begin{aligned}
\forall \varepsilon > 0,\ \exists \delta > 0 \text{ such that} \\
\forall x, y \in E \text{ with } d(x,y) < \delta, \\
\lvert f(x)-f(y)\rvert < \varepsilon .
\end{aligned}
$$

Set the two definitions side by side.

- **Continuity on $$E$$:** $$\forall p\ \forall\varepsilon\ \exists\delta\ \forall x$$.
- **Uniform continuity:** $$\forall\varepsilon\ \exists\delta\ \forall x, y$$.

In the first, $$\delta$$ may depend on the point. In the second it may not:
one $$\delta$$ must work everywhere. Uniform continuity is strictly stronger,
and it is a property of $$f$$ **on a set**, never at a point.

**Is $$\sin x$$ uniformly continuous on $$\mathbb{R}$$?** Yes — the estimate
$$\lvert\sin x - \sin y\rvert \le \lvert x - y\rvert$$ from §4.2 gives
$$\delta = \varepsilon$$ independently of where you are.

### Lipschitz functions

**Definition.** $$f$$ satisfies a **Lipschitz condition** on $$E$$ when there is
$$M > 0$$ with

$$
\lvert f(x) - f(y)\rvert \le M\,d(x,y) \quad \text{for all } x, y \in E .
$$

**Theorem.** A Lipschitz function is uniformly continuous.

*Proof.* Take $$\delta = \varepsilon/M$$. $$\square$$

Lipschitz is the easiest sufficient condition to check, and when $$f$$ is
differentiable with bounded derivative, the mean value theorem of
[Chapter 5](/posts/analysis-differentiation/) supplies it immediately with
$$M = \sup\lvert f'\rvert$$.

### The uniform continuity theorem

**Theorem.** If $$K$$ is compact and $$f : K \to \mathbb{R}$$ is continuous,
then $$f$$ is uniformly continuous on $$K$$.

*Proof.* Let $$\varepsilon > 0$$. For each $$p \in K$$ continuity gives
$$\delta_p > 0$$ with $$\lvert f(x) - f(p)\rvert < \varepsilon/2$$ for
$$x \in N_{\delta_p}(p) \cap K$$. The **half-sized** balls
$$N_{\delta_p/2}(p)$$ still cover $$K$$, so finitely many do, say at
$$p_1, \ldots, p_n$$. Put

$$
\delta = \tfrac12\min\{\delta_{p_1}, \ldots, \delta_{p_n}\} > 0 .
$$

Now let $$x, y \in K$$ with $$d(x,y) < \delta$$. Then $$x$$ lies in some
$$N_{\delta_{p_j}/2}(p_j)$$, and

$$
\begin{aligned}
d(y, p_j) &\le d(y,x) + d(x,p_j) \\
 &< \delta + \tfrac{\delta_{p_j}}{2} \le \delta_{p_j} ,
\end{aligned}
$$

so **both** $$x$$ and $$y$$ lie in $$N_{\delta_{p_j}}(p_j)$$ and

$$
\begin{aligned}
\lvert f(x)-f(y)\rvert
 &\le \lvert f(x)-f(p_j)\rvert + \lvert f(p_j)-f(y)\rvert \\
 &< \varepsilon .
\end{aligned}
$$

$$\square$$

> **The halving is the whole trick.** Covering by full-sized balls and taking a
> minimum does not work, because $$x$$ and $$y$$ could sit in different balls
> with nothing tying them together. Halving the radii buys the room for the
> triangle inequality to put both points in the *same* original ball. This is
> the standard device and it is worth learning as a pattern.
{: .prompt-tip }

**Remark.** Uniform continuity is **not** preserved by multiplication. Both
$$f(x) = x$$ and $$g(x) = x$$ are uniformly continuous on $$\mathbb{R}$$ —
Lipschitz with $$M = 1$$ — but $$fg(x) = x^2$$ is not. Take $$x_n = n$$ and
$$y_n = n + 1/n$$; then $$\lvert x_n - y_n\rvert \to 0$$ while

$$
\lvert y_n^2 - x_n^2\rvert = 2 + \tfrac{1}{n^2} \to 2 .
$$

No single $$\delta$$ can work for $$\varepsilon = 1$$.

### Suggested exercises

**2(c). $$h(x) = \sin\frac1x$$ is not uniformly continuous on $$(0,\infty)$$.**

Take

$$
x_n = \frac{1}{2n\pi + \pi/2}, \qquad y_n = \frac{1}{2n\pi} .
$$

Both tend to $$0$$, so $$\lvert x_n - y_n\rvert \to 0$$, while
$$h(x_n) = \sin(2n\pi + \pi/2) = 1$$ and $$h(y_n) = \sin(2n\pi) = 0$$. The
difference is $$1$$ for every $$n$$, so no $$\delta$$ works for
$$\varepsilon = 1$$. $$\square$$

The failure is at $$0$$: the oscillation does not slow down as $$x$$ shrinks.

**4(c). $$h(x) = \sin\frac1x$$ is Lipschitz on $$(a,\infty)$$ for $$a > 0$$.**

Here $$h'(x) = -\frac{1}{x^2}\cos\frac1x$$, so
$$\lvert h'(x)\rvert \le 1/a^2$$ on $$(a,\infty)$$, and the mean value theorem
gives

$$
\lvert h(x) - h(y)\rvert \le \frac{1}{a^2}\lvert x - y\rvert .
$$

$$\square$$

Compare with 2(c): the same function, and bounding the domain away from $$0$$
is exactly what rescues it.

**8. If $$f$$ is uniformly continuous on $$E$$ and $$\{x_n\}$$ is Cauchy in
$$E$$, then $$\{f(x_n)\}$$ is Cauchy.**

Given $$\varepsilon$$, take $$\delta$$ from uniform continuity and then
$$n_0$$ with $$d(x_m, x_n) < \delta$$ for $$m,n \ge n_0$$. Then
$$\lvert f(x_m) - f(x_n)\rvert < \varepsilon$$. $$\square$$

**Mere continuity is not enough.** On $$E = (0,1]$$ the function
$$f(x) = 1/x$$ is continuous, $$x_n = 1/n$$ is Cauchy, and
$$f(x_n) = n$$ is not. This is the cleanest statement of what uniform
continuity buys: **it preserves Cauchyness**, and so a uniformly continuous
function on a dense subset extends continuously to the whole space.

**10. If $$E \subseteq \mathbb{R}$$ is bounded and $$f$$ is uniformly
continuous on $$E$$, then $$f$$ is bounded on $$E$$.**

Take $$\delta$$ for $$\varepsilon = 1$$. Since $$E$$ is bounded,
$$E \subseteq [-R, R]$$ for some $$R$$, and $$[-R,R]$$ can be cut into
finitely many intervals $$I_1, \ldots, I_N$$ each of length less than
$$\delta$$. Discard those meeting $$E$$ in nothing; in each remaining one pick
$$t_j \in E \cap I_j$$. Any $$x \in E$$ lies in some kept $$I_j$$, and then
$$\lvert x - t_j\rvert < \delta$$, so

$$
\lvert f(x)\rvert \le \lvert f(t_j)\rvert + 1 \le \max_j \lvert f(t_j)\rvert + 1 .
$$

$$\square$$

Boundedness of $$E$$ is essential: $$f(x) = x$$ is uniformly continuous on
$$\mathbb{R}$$ and unbounded.

**12. If $$f$$ is continuous on $$[a,\infty)$$ and
$$\lim_{x\to\infty} f(x) = L \in \mathbb{R}$$, then $$f$$ is (a) bounded and
(b) uniformly continuous on $$[a,\infty)$$.**

(a) Take $$M$$ with $$\lvert f(x) - L\rvert < 1$$ for $$x > M$$, so
$$\lvert f\rvert \le \lvert L\rvert + 1$$ there. On $$[a, M]$$, which is
compact, $$f$$ is bounded by the extreme value theorem. Take the larger bound.

(b) Given $$\varepsilon > 0$$, take $$M$$ with
$$\lvert f(x) - L\rvert < \varepsilon/2$$ for $$x > M$$; then for any
$$x, y > M$$,

$$
\lvert f(x)-f(y)\rvert \le \lvert f(x)-L\rvert + \lvert L-f(y)\rvert < \varepsilon .
$$

On the compact set $$[a, M+1]$$, $$f$$ is uniformly continuous by the uniform
continuity theorem; let $$\delta_1$$ be its modulus for $$\varepsilon$$. Put
$$\delta = \min(\delta_1, 1)$$. Any $$x,y$$ with $$\lvert x-y\rvert < \delta$$
either both exceed $$M$$, or both lie in $$[a, M+1]$$ — since they are within
$$1$$ of each other and at least one is at most $$M$$. Either case gives
$$\lvert f(x)-f(y)\rvert < \varepsilon$$. $$\square$$

> The notes state this exercise without assuming $$f$$ continuous, which part
> (b) needs: a wildly discontinuous $$f$$ on $$[a, M]$$ with the right
> behaviour at infinity satisfies the hypothesis as written and is not
> uniformly continuous. Continuity is assumed here.
{: .prompt-warning }

---

## Part 4 — §4.4: monotone functions and discontinuities

### One-sided limits

**Definition.** Let $$E \subseteq \mathbb{R}$$, $$f$$ real-valued on $$E$$, and
let $$p$$ be a limit point of $$E \cap (p,\infty)$$. Then $$f$$ has a
**right limit** $$L$$ at $$p$$ when for every $$\varepsilon > 0$$ there is
$$\delta > 0$$ with

$$
\begin{aligned}
\lvert f(x) - L\rvert &< \varepsilon \\
\text{for all } x \in E \text{ with } & p < x < p+\delta ,
\end{aligned}
$$

written $$f(p+) = \lim_{x \to p+} f(x)$$. The left limit $$f(p-)$$ is the
mirror image.

**Definition.** $$f$$ is **right continuous** at $$p \in E$$ when for every
$$\varepsilon > 0$$ there is $$\delta > 0$$ with
$$\lvert f(x) - f(p)\rvert < \varepsilon$$ for all $$x \in E$$ with
$$p \le x < p + \delta$$.

**Remark.** Every function is right continuous at $$p$$ if $$p$$ is isolated in
$$E$$, or is not a limit point of $$E \cap (p,\infty)$$ — the same vacuity as
before.

**Theorem.** $$f : (a,b) \to \mathbb{R}$$ is right continuous at
$$p \in (a,b)$$ $$\iff$$ $$f(p+)$$ exists and equals $$f(p)$$.

### Classifying discontinuities

Let $$f$$ fail to be continuous at $$p$$.

- **Removable.** $$\lim_{x\to p} f(x)$$ exists but either differs from
  $$f(p)$$ or $$f(p)$$ is undefined. Redefining one value repairs it.
- **Jump** (first kind). Both $$f(p+)$$ and $$f(p-)$$ exist, but $$f$$ is not
  continuous at $$p$$. No redefinition repairs it, because the two sides
  disagree.
- **Second kind.** Anything else — at least one one-sided limit fails to
  exist.

$$\sin(1/x)$$ at $$0$$ is the standard discontinuity of the second kind;
$$\lfloor x \rfloor$$ at an integer is a jump; and
$$f(x) = x\sin(1/x)$$ undefined at $$0$$ is removable.

**Is $$g(x) = \sin(2\pi x \lfloor x\rfloor)$$ continuous at each
$$n \in \mathbb{Z}$$?** Yes. Just left of $$n$$, $$\lfloor x\rfloor = n-1$$ and
$$g(x) = \sin(2\pi x(n-1)) \to \sin(2\pi n(n-1)) = 0$$, since
$$n(n-1)$$ is an integer. Just right of $$n$$, $$\lfloor x\rfloor = n$$ and
$$g(x) \to \sin(2\pi n^2) = 0$$. And $$g(n) = \sin(2\pi n^2) = 0$$. All three
agree.

**Is $$g$$ uniformly continuous on $$\mathbb{R}$$?** No. On $$[n, n+1)$$ it is
$$\sin(2\pi n x)$$, of period $$1/n$$, so the oscillation speeds up without
bound. Take $$x_n = n$$ and $$y_n = n + \frac{1}{4n}$$: then
$$\lvert x_n - y_n\rvert \to 0$$ while

$$
g(y_n) = \sin\!\left(2\pi n^2 + \tfrac{\pi}{2}\right) = 1, \qquad g(x_n) = 0 .
$$

### Monotone functions

**Theorem.** Let $$I$$ be an open interval and $$f : I \to \mathbb{R}$$
monotone increasing. Then $$f(p+)$$ and $$f(p-)$$ exist at every $$p \in I$$,
and

$$
\sup_{x<p} f(x) = f(p-) \le f(p) \le f(p+) = \inf_{x>p} f(x) .
$$

Moreover $$p < q$$ in $$I$$ implies $$f(p+) \le f(q-)$$.

*Proof.* The set $$\{f(x) : x < p\}$$ is bounded above by $$f(p)$$, so its
supremum $$\alpha$$ exists. Given $$\varepsilon > 0$$, there is $$x_0 < p$$
with $$f(x_0) > \alpha - \varepsilon$$, and monotonicity gives
$$\alpha - \varepsilon < f(x) \le \alpha$$ for all $$x \in (x_0, p)$$. That is
exactly $$f(p-) = \alpha$$. The right-hand statement is the mirror image with
an infimum. $$\square$$

> **A monotone function has no discontinuities of the second kind.** Both
> one-sided limits always exist; the only thing that can go wrong is that they
> differ. So every discontinuity of a monotone function is a jump.
{: .prompt-tip }

**Corollary.** The set of discontinuities of a monotone function on an open
interval is **at most countable**.

*Proof.* At each discontinuity $$p$$ the interval $$\big(f(p-), f(p+)\big)$$ is
nonempty, and by the last clause of the theorem these intervals are pairwise
disjoint for distinct $$p$$. Each contains a rational, distinct intervals
contain distinct rationals, and $$\mathbb{Q}$$ is countable. $$\square$$

That is the same argument as the decomposition of open subsets of
$$\mathbb{R}$$ in §2.2: **disjoint intervals are countable because
$$\mathbb{Q}$$ is.**

### Prescribing the discontinuities

The converse is true, and strikingly so.

**Theorem.** Let $$a < b$$, let $$\{x_n\}$$ be a countable subset of
$$(a,b)$$, and let $$\{c_n\}$$ be positive reals with
$$\sum_{n=1}^{\infty} c_n$$ convergent. Then there is a monotone increasing
$$f$$ on $$[a,b]$$ with

1. $$f(a) = 0$$ and $$f(b) = \sum_{n=1}^{\infty} c_n$$;
2. $$f$$ continuous on $$[a,b] \setminus \{x_n\}$$;
3. $$f(x_n+) = f(x_n)$$ for every $$n$$;
4. $$f$$ discontinuous at each $$x_n$$, with jump
   $$f(x_n) - f(x_n-) = c_n$$.

*Construction.* Put

$$
f(x) = \sum_{\{n\,:\,x_n \le x\}} c_n ,
$$

the sum of the weights of all the listed points at or below $$x$$. The series
converges absolutely, so the order of summation is irrelevant — which matters,
because $$\{x_n\}$$ carries no order. Monotonicity is clear, the jump at
$$x_n$$ is $$c_n$$ because $$x_n$$ enters the sum exactly at $$x = x_n$$, and
continuity elsewhere follows from the tail of a convergent series being small.
$$\square$$

Take $$\{x_n\}$$ to be an enumeration of the rationals in $$(0,1)$$ and
$$c_n = 2^{-n}$$: the result is an increasing function on $$[0,1]$$
discontinuous at **every rational** and continuous at every irrational.
Together with the corollary, this says the countable sets are *exactly* the
possible discontinuity sets of monotone functions.

### Inverse functions

**Theorem.** If $$I \subseteq \mathbb{R}$$ is an interval and
$$f : I \to \mathbb{R}$$ is strictly monotone and continuous, then $$f^{-1}$$
is strictly monotone and continuous on $$f(I)$$.

*Proof sketch.* Strict monotonicity of $$f^{-1}$$ is immediate. For
continuity, $$f(I)$$ is an interval by the intermediate value theorem, and
$$(f^{-1})^{-1}(U) = f(U)$$ is open for open $$U$$ by exercise 14 below; the
topological characterisation finishes it. $$\square$$

### Suggested exercises

**7(b). $$g(x) = 2\pi x\lfloor x\rfloor$$ is not uniformly continuous on
$$\mathbb{R}$$.**

Take $$x_n = n - \frac1n$$ and $$y_n = n$$ for $$n \ge 2$$, so
$$\lfloor x_n\rfloor = n-1$$ and $$\lfloor y_n\rfloor = n$$. Then

$$
\begin{aligned}
g(y_n) - g(x_n)
 &= 2\pi n^2 - 2\pi\left(n - \tfrac1n\right)(n-1) \\
 &= 2\pi\left(n + 1 - \tfrac1n\right) \to \infty ,
\end{aligned}
$$

while $$\lvert x_n - y_n\rvert = 1/n \to 0$$. $$\square$$

**14. $$I$$ an open interval, $$f$$ continuous and strictly increasing on
$$I$$.**

**(a) If $$U \subseteq I$$ is open then $$f(U)$$ is open.** By §2.2, $$U$$ is a
countable disjoint union of open intervals, and images commute with unions, so
it suffices to treat $$U = (c,d)$$. Since $$f$$ is continuous, $$f((c,d))$$ is
an interval; since $$f$$ is strictly increasing it lies strictly between the
values approached at the ends, so

$$
f\big((c,d)\big) = \big(f(c+),\ f(d-)\big),
$$

an open interval. (If $$c$$ or $$d$$ is an endpoint of $$I$$, read the
one-sided limit as the appropriate infinite value.)

**(b) $$f^{-1}$$ is continuous on $$f(I)$$.** For open $$V$$,
$$(f^{-1})^{-1}(V) = f(V \cap I)$$, which is open by (a). The topological
characterisation gives continuity. $$\square$$

**15. A one-to-one continuous $$f$$ on an interval $$I$$ is strictly
monotone.**

Suppose not. Then there are $$a < b < c$$ in $$I$$ with $$f(b)$$ not strictly
between $$f(a)$$ and $$f(c)$$ — otherwise the order is preserved or reversed
consistently throughout, which is monotonicity. Say
$$f(b) > \max\big(f(a), f(c)\big)$$, and pick $$\gamma$$ with

$$
\max\big(f(a), f(c)\big) < \gamma < f(b) .
$$

The intermediate value theorem on $$[a,b]$$ gives $$s \in (a,b)$$ with
$$f(s) = \gamma$$, and on $$[b,c]$$ gives $$t \in (b,c)$$ with
$$f(t) = \gamma$$. Then $$s < b < t$$ so $$s \ne t$$, contradicting
injectivity. The case $$f(b) < \min(f(a),f(c))$$ is symmetric. $$\square$$

This is why "continuous and invertible" on an interval always means
"monotone", and why the inverse function theorem above has the hypotheses it
does.

## Common pitfalls

- **Forgetting $$p$$ must be a limit point** in the definition of a function
  limit. Without it the statement is vacuous.
- **Letting $$f(p)$$ influence $$\lim_{x\to p} f$$.** It cannot; the punctured
  ball excludes it.
- **Reading "continuous at a point" for uniform continuity.** Uniform
  continuity is a property of a function *on a set*. There is no such thing as
  uniform continuity at a point.
- **Using $$f(V)$$ instead of $$f^{-1}(V)$$** in the topological
  characterisation. Open images are an entirely different and much rarer
  property.
- **Thinking "closed in $$E$$" means "closed in $$\mathbb{R}$$".** Exercise 19
  exists to break this.
- **Applying the extreme value theorem without compactness.** On $$(0,1)$$ a
  continuous function need not attain, or even have, a maximum.
- **Covering by full-sized balls** in the uniform continuity theorem. The
  halving is not decoration.
- **Expecting uniform continuity to survive products.** $$x \cdot x = x^2$$
  refutes it.
- **Assuming a monotone function can have a wild discontinuity.** It cannot —
  every discontinuity of a monotone function is a jump, and there are at most
  countably many.

## Connections

- **Backward.** The sequential criterion imports all of
  [Chapter 3](/posts/analysis-sequences/) at a stroke. Compactness and
  connectedness from [Chapter 2](/posts/analysis-metric-spaces/) become the
  extreme value and intermediate value theorems. The countability of
  $$\mathbb{Q}$$ from [Chapter 1](/posts/analysis-real-numbers/) counts the
  discontinuities of a monotone function.
- **Forward.** [Chapter 5](/posts/analysis-differentiation/) needs continuity
  as the hypothesis of every mean value theorem, and supplies the Lipschitz
  bound that §4.3 could only assume.
  [Chapter 6](/posts/analysis-integration/) integrates continuous functions on
  $$[a,b]$$, and the proof that the integral exists is the uniform continuity
  theorem of §4.3 doing the work.
  [Chapter 8](/posts/analysis-function-sequences/) replays the whole
  pointwise-versus-uniform distinction one level up, with sequences of
  functions in place of points.
- **Outward.** The topological characterisation is the definition of
  continuity in general topology, where no $$\varepsilon$$ exists to speak of.
  The monotone discontinuity theorem is the first step toward functions of
  bounded variation and the Riemann–Stieltjes integral of
  [Chapter 6](/posts/analysis-integration/).

## Summary

- **Limit at $$p$$** — needs $$p$$ a limit point; ignores $$f(p)$$
- **Sequential criterion** — limits of functions reduce to limits of sequences; the standard way to disprove a limit
- **Limit theorems** — sums, products, quotients, bounded-times-null, squeeze, all inherited from Chapter 3
- **Continuity at $$p$$** — the limit exists and equals $$f(p)$$; automatic at isolated points
- **Topological characterisation** — continuous $$\iff$$ preimages of open sets are open in $$E$$
- **Compactness** — $$f(K)$$ compact; hence the extreme value theorem
- **Connectedness** — $$f(I)$$ an interval; hence the intermediate value theorem
- **Uniform continuity** — one $$\delta$$ for all points; strictly stronger; not closed under products
- **Lipschitz $$\Rightarrow$$ uniformly continuous**
- **Continuous on compact $$\Rightarrow$$ uniformly continuous**, by halving the radii
- **Uniform continuity preserves Cauchy sequences**; continuity does not
- **Discontinuities** — removable, jump, second kind
- **Monotone** — one-sided limits always exist, so every discontinuity is a jump, and there are at most countably many
- **Any countable set** is the discontinuity set of some monotone function
- **Strictly monotone + continuous on an interval** $$\Rightarrow$$ continuous inverse

## References

- Manfred Stoll, *Introduction to Real Analysis*, 2nd edition — Chapter 4. The suggested exercise numbers are Stoll's.
- Introduction to Mathematical Analysis (881.008), Spring 2023. Instructor: Ja A Jeong (정자아). Typed lecture notes, Chapter IV.
- The notes give definitions, theorem statements and the exercise list, with every proof and every solution left as blank space. All proofs and all exercise solutions above are mine. Proofs are written out where the argument carries a technique worth keeping — the sequential criterion, the topological characterisation, compactness and connectedness under continuous maps, the halving argument for uniform continuity, and the countability of the discontinuities of a monotone function — and compressed elsewhere.
- Two notes on the source. §4.2 is headed "Limit of a Function" in the notes, repeating §4.1's title; its content is continuity. And exercise 12 of §4.3 omits the continuity hypothesis that part (b) requires; it is assumed here, with the gap flagged in place.
- The example showing that a continuous image of a relatively open set need not be relatively open, Thomae's function, and the counterexamples for products of uniformly continuous functions are mine; the notes mark these as exercises without giving them.
