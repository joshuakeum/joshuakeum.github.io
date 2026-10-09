---
title: "Mathematical Analysis: Integration"
date: 2026-10-09 11:00:00 +0900
categories: [Course Notes, Mathematical Analysis]
tags: [riemann integral, darboux, measure zero, lebesgue criterion, fundamental theorem, riemann-stieltjes]
description: The Darboux construction of the Riemann integral, Riemann's criterion, Lebesgue's characterization by measure zero, the fundamental theorem of calculus, improper integrals, and Riemann-Stieltjes integration. Chapter 6 of Introduction to Mathematical Analysis.
math: true
mermaid: false
render_with_liquid: false
---

> This chapter covers §§6.1–6.5.
{: .prompt-info }

## What this chapter answers

First-year calculus defines the integral as a limit of Riemann sums and then
computes with antiderivatives. Two questions are skipped, and this chapter is
both of them.

**Which functions are integrable?** The answer is not "the continuous ones",
though those are. It is Lebesgue's criterion: a bounded function on $$[a,b]$$
is Riemann integrable exactly when **its set of discontinuities has measure
zero**. That is a sharp characterisation, and it explains every example at
once — why monotone functions integrate (countably many discontinuities, by
[Chapter 4](/posts/analysis-continuity/)), why Thomae's function integrates
despite being discontinuous on a dense set, and why the Dirichlet function
does not.

**Why does antidifferentiation compute areas?** Nothing in the definition of
the integral mentions derivatives. The fundamental theorem is a genuine
theorem, and the proof is the mean value theorem of
[Chapter 5](/posts/analysis-differentiation/).

The chapter also replaces $$\mathrm{d}x$$ by $$\mathrm{d}\alpha$$ for a
monotone $$\alpha$$. The **Riemann–Stieltjes integral** costs almost nothing
to set up and buys a single framework in which sums and integrals are the same
operation.

## Prerequisites

[Chapter 4](/posts/analysis-continuity/) for uniform continuity on compact
sets — the proof that continuous functions integrate is that theorem — and for
monotone functions; [Chapter 5](/posts/analysis-differentiation/) for the mean
value theorem; [Chapter 2](/posts/analysis-metric-spaces/) for the Cantor set
and compactness; [Chapter 1](/posts/analysis-real-numbers/) for suprema and
countability.

---

## Part 1 — §6.1: the Darboux construction

### Upper and lower integrals

Let $$f$$ be a **bounded** real-valued function on $$[a,b]$$. A **partition**
$$\mathcal{P} = \{x_0, x_1, \ldots, x_n\}$$ has
$$a = x_0 < x_1 < \cdots < x_n = b$$. Write

$$
\begin{aligned}
M_i &= \sup\{f(x) : x \in [x_{i-1},x_i]\}, \\
m_i &= \inf\{f(x) : x \in [x_{i-1},x_i]\},
\end{aligned}
$$

which exist because $$f$$ is bounded, and form

$$
\begin{aligned}
\mathcal{U}(\mathcal{P}, f) &= \sum_{i=1}^{n} M_i\,\Delta x_i , \\
\mathcal{L}(\mathcal{P}, f) &= \sum_{i=1}^{n} m_i\,\Delta x_i .
\end{aligned}
$$

**Definition.** The **upper** and **lower integrals** are

$$
\begin{aligned}
\overline{\int_a^b} f &= \inf\{\mathcal{U}(\mathcal{P},f) : \mathcal{P}\}, \\
\underline{\int_a^b} f &= \sup\{\mathcal{L}(\mathcal{P},f) : \mathcal{P}\}.
\end{aligned}
$$

Boundedness is what makes every $$M_i$$ and $$m_i$$ finite, and completeness is
what makes the outer $$\inf$$ and $$\sup$$ exist. **The integral is built out
of suprema**, which is why [Chapter 1](/posts/analysis-real-numbers/) had to
come first.

### Refinement

**Definition.** A partition $$\mathcal{P}^{*}$$ **refines** $$\mathcal{P}$$
when $$\mathcal{P} \subseteq \mathcal{P}^{*}$$ — more division points.

**Lemma.** If $$\mathcal{P}^{*}$$ refines $$\mathcal{P}$$ then

$$
\mathcal{L}(\mathcal{P},f) \le \mathcal{L}(\mathcal{P}^{*},f)
 \le \mathcal{U}(\mathcal{P}^{*},f) \le \mathcal{U}(\mathcal{P},f) .
$$

*Proof.* It suffices to add one point $$t \in (x_{i-1},x_i)$$. The supremum
over each of $$[x_{i-1},t]$$ and $$[t,x_i]$$ is at most the supremum over the
whole of $$[x_{i-1},x_i]$$, so the upper sum can only decrease; the lower sum
can only increase for the mirror reason. $$\square$$

> **Refining squeezes.** Upper sums come down, lower sums go up, and they never
> cross. That single lemma is what makes the construction work, because it
> means any two partitions can be compared through their common refinement.
{: .prompt-tip }

**Theorem.** For bounded $$f$$ on $$[a,b]$$,

$$
\underline{\int_a^b} f \;\le\; \overline{\int_a^b} f .
$$

*Proof.* Given partitions $$\mathcal{P}$$ and $$\mathcal{Q}$$, apply the lemma
to the common refinement $$\mathcal{P}\cup\mathcal{Q}$$:

$$
\mathcal{L}(\mathcal{P},f) \le \mathcal{L}(\mathcal{P}\cup\mathcal{Q},f)
 \le \mathcal{U}(\mathcal{P}\cup\mathcal{Q},f) \le \mathcal{U}(\mathcal{Q},f) .
$$

So every lower sum is below every upper sum; take the sup on the left and the
inf on the right. $$\square$$

**Definition.** $$f$$ is **Riemann integrable** on $$[a,b]$$ when the two agree,
and the common value is $$\int_a^b f$$. The set of Riemann integrable functions
on $$[a,b]$$ is written $$\mathcal{R}[a,b]$$.

**Is the Dirichlet function integrable?** Let $$f(x) = 1$$ on $$\mathbb{Q}$$
and $$0$$ elsewhere. Every subinterval of positive length contains both
rationals and irrationals, so $$M_i = 1$$ and $$m_i = 0$$ for every partition,
giving $$\mathcal{U} = b-a$$ and $$\mathcal{L} = 0$$ always. Hence

$$
\underline{\int_0^1} f = 0 \ne 1 = \overline{\int_0^1} f ,
$$

and $$f \notin \mathcal{R}[0,1]$$. It is the standard non-integrable function,
and it is discontinuous **everywhere** — which §6.1's last theorem will show is
the real reason.

### Riemann's criterion

**Theorem (Riemann's criterion).** A bounded $$f$$ is integrable on $$[a,b]$$
if and only if for every $$\varepsilon > 0$$ there is a partition
$$\mathcal{P}$$ with

$$
\mathcal{U}(\mathcal{P},f) - \mathcal{L}(\mathcal{P},f) < \varepsilon .
$$

*Proof.* ($$\Leftarrow$$) The upper integral is at most $$\mathcal{U}$$ and the
lower at least $$\mathcal{L}$$, so their difference — which is non-negative — is
below $$\varepsilon$$ for every $$\varepsilon$$, hence zero.

($$\Rightarrow$$) Choose $$\mathcal{P}_1$$ with
$$\mathcal{U}(\mathcal{P}_1,f) < \int f + \varepsilon/2$$ and
$$\mathcal{P}_2$$ with $$\mathcal{L}(\mathcal{P}_2,f) > \int f - \varepsilon/2$$,
and take the common refinement. $$\square$$

This is the workhorse. **To prove something is integrable, produce one
partition on which the gap is small** — no need to compute anything.

**Theorem.** If $$f$$ is continuous on $$[a,b]$$, or monotone on $$[a,b]$$,
then $$f \in \mathcal{R}[a,b]$$.

*Proof (continuous).* $$[a,b]$$ is compact, so by §4.3 $$f$$ is **uniformly**
continuous. Given $$\varepsilon > 0$$ take $$\delta$$ with
$$\lvert f(x)-f(y)\rvert < \frac{\varepsilon}{b-a}$$ whenever
$$\lvert x-y\rvert < \delta$$, and let $$\mathcal{P}$$ have all subintervals
shorter than $$\delta$$. On each, $$M_i - m_i \le \frac{\varepsilon}{b-a}$$ —
the sup and inf are attained by the extreme value theorem — so

$$
\begin{aligned}
\mathcal{U} - \mathcal{L} &= \sum (M_i-m_i)\Delta x_i \\
 &\le \frac{\varepsilon}{b-a}\sum \Delta x_i = \varepsilon .
\end{aligned}
$$

*Proof (monotone).* Say $$f$$ increases. With the uniform partition into $$n$$
pieces, $$M_i = f(x_i)$$ and $$m_i = f(x_{i-1})$$, so the sum **telescopes**:

$$
\begin{aligned}
\mathcal{U} - \mathcal{L}
 &= \frac{b-a}{n}\sum_{i=1}^{n}\big(f(x_i)-f(x_{i-1})\big) \\
 &= \frac{(b-a)\big(f(b)-f(a)\big)}{n} ,
\end{aligned}
$$

which is below $$\varepsilon$$ for large $$n$$. $$\square$$

> **Uniform continuity is exactly the hypothesis the first proof needs.** Mere
> continuity would give a $$\delta$$ depending on the point, and no single
> partition would work. This is the clearest payoff in the course for the
> distinction drawn in §4.3.
{: .prompt-tip }

**Theorem (composition).** If $$f \in \mathcal{R}[a,b]$$ with
$$\operatorname{Range} f \subseteq [c,d]$$ and $$\varphi$$ is continuous on
$$[c,d]$$, then $$\varphi \circ f \in \mathcal{R}[a,b]$$.

**Corollary.** $$f \in \mathcal{R}[a,b]$$ implies $$\lvert f\rvert$$ and
$$f^2$$ are integrable — take $$\varphi(t) = \lvert t\rvert$$ and
$$\varphi(t) = t^2$$.

The order matters: $$\varphi \circ f$$ with $$\varphi$$ continuous *outside* is
fine, while $$f \circ \varphi$$ need not be. Composing an integrable function
with an integrable function can fail.

### Measure zero and Lebesgue's theorem

**Definition.** $$E \subseteq \mathbb{R}$$ has **measure zero** when for every
$$\varepsilon > 0$$ there is a finite or countable collection of open
intervals $$\{I_n\}$$ with

$$
E \subseteq \bigcup_n I_n
\quad\text{and}\quad
\sum_n \ell(I_n) < \varepsilon ,
$$

where $$\ell$$ denotes length.

**Remark (a). Every finite set has measure zero.** Cover each of the $$N$$
points by an interval of length $$\varepsilon/(2N)$$; the total is
$$\varepsilon/2 < \varepsilon$$.

**Remark (b). Every countable set has measure zero.** Enumerate it as
$$\{x_n\}$$ and cover $$x_n$$ by an interval of length
$$\varepsilon \cdot 2^{-n-1}$$. The total is

$$
\sum_{n=1}^{\infty}\frac{\varepsilon}{2^{n+1}} = \frac{\varepsilon}{2} < \varepsilon .
$$

**The $$2^{-n}$$ trick is the one to remember.** It is how countably many
errors are made to sum to a finite budget, and it recurs in
[Chapter 7](/posts/analysis-series/) and
[Chapter 8](/posts/analysis-function-sequences/).

**Remark (c). The Cantor set has measure zero, and is uncountable.** At stage
$$n$$ the set $$P_n$$ of [Chapter 2](/posts/analysis-metric-spaces/) is a union
of $$2^n$$ closed intervals of length $$3^{-n}$$, total length
$$(2/3)^n \to 0$$. Fattening each slightly to an open interval covers
$$P \subseteq P_n$$ with total length below any $$\varepsilon$$. So **measure
zero is strictly weaker than countable.**

**Theorem (Lebesgue's criterion).** A bounded $$f$$ on $$[a,b]$$ is Riemann
integrable if and only if its set of discontinuities has measure zero.

This settles every example at once.

- Continuous: no discontinuities. Integrable.
- Monotone: at most countably many discontinuities, by §4.4. Integrable.
- Dirichlet: discontinuous everywhere, and $$[0,1]$$ does not have measure
  zero. Not integrable.
- Thomae's function: discontinuous exactly on $$\mathbb{Q}$$, countable.
  Integrable.

**Worked: $$\int_0^1 f = 0$$ for Thomae's (ruler) function.** Recall
$$f(p/q) = 1/q$$ in lowest terms and $$f = 0$$ on the irrationals, so $$f$$ is
integrable by Lebesgue. Every lower sum is $$0$$, since every subinterval
contains irrationals, so $$\int_0^1 f = \underline{\int} f = 0$$. $$\square$$

One can also see it directly: given $$\varepsilon$$, only finitely many points
have $$f \ge \varepsilon/2$$, so cover them by intervals of total length
$$\varepsilon/2$$ and bound the upper sum by
$$\varepsilon/2 + \varepsilon/2$$.

### Suggested exercises

**7(a). If $$f$$ is continuous and non-negative on $$[a,b]$$ with
$$\int_a^b f = 0$$, then $$f \equiv 0$$.**

Suppose $$f(c) > 0$$ for some $$c$$. By continuity — exercise 21 of §4.2 —
there are $$\alpha > 0$$ and $$\delta > 0$$ with $$f \ge \alpha$$ on an
interval $$J \subseteq [a,b]$$ of length $$\ell > 0$$ around $$c$$. Since
$$f \ge 0$$ everywhere,

$$
\int_a^b f \ \ge\ \int_J f \ \ge\ \alpha\ell \ > \ 0 ,
$$

a contradiction. $$\square$$

**(b) Continuity is needed.** Take $$f(x) = 0$$ except $$f(c) = 1$$ at one
point. Then $$f$$ is integrable with $$\int_a^b f = 0$$, and $$f \not\equiv 0$$.

**17. Measure zero is closed under subsets and finite unions.**

**(a)** A cover of $$E$$ covers every subset of $$E$$.

**(b)** Given $$\varepsilon$$, cover $$E_1$$ with total length
$$< \varepsilon/2$$ and $$E_2$$ with total length $$< \varepsilon/2$$; the
union of the two collections is countable and covers $$E_1\cup E_2$$ with
total length $$< \varepsilon$$. $$\square$$

The same argument with $$\varepsilon 2^{-n}$$ shows a **countable** union of
measure-zero sets has measure zero — which, with remark (a), re-proves remark
(b).

**16. A bounded $$f$$ on $$[a,b]$$ with only finitely many discontinuities is
integrable — directly.**

Say $$\lvert f\rvert \le M$$ and the discontinuities are
$$c_1, \ldots, c_N$$. Given $$\varepsilon > 0$$, enclose each $$c_j$$ in an
open interval of length $$\varepsilon/(8MN)$$. Removing these leaves finitely
many closed intervals on which $$f$$ is continuous, hence uniformly
continuous, so each contributes at most $$\varepsilon/4$$ in total to
$$\mathcal{U}-\mathcal{L}$$ once partitioned finely enough. The enclosing
intervals contribute at most

$$
2M \cdot N \cdot \frac{\varepsilon}{8MN} = \frac{\varepsilon}{4} ,
$$

since $$M_i - m_i \le 2M$$ there. Riemann's criterion applies. $$\square$$

This is Lebesgue's theorem for the easiest case, done by hand. The general
proof is the same idea with the $$2^{-n}$$ trick doing the covering.

**3(a). If $$f = 0$$ except at finitely many points $$c_1,\ldots,c_n$$, then
$$f \in \mathcal{R}[a,b]$$ and $$\int_a^b f = 0$$.**

Immediate from exercise 16 — the discontinuities are finite — and every lower
sum is $$\le 0 \le$$ every upper sum while both can be made small, so the
value is $$0$$.

**(c) Is it true for all but countably many points?** **No.** The Dirichlet
function is $$0$$ except on $$\mathbb{Q}$$, which is countable, and it is not
integrable. The gap between "finite" and "countable" is exactly the gap
between controlling $$\mathcal{U}-\mathcal{L}$$ and not: countably many
exceptional points can be dense, so no partition isolates them.

> Note the contrast with Lebesgue's criterion, which *is* about measure zero
> and therefore does cover countable sets. The difference is that Lebesgue
> constrains the **discontinuities**, not the points where $$f$$ is non-zero.
> Dirichlet's function is non-zero on a countable set and discontinuous on all
> of $$[0,1]$$.
{: .prompt-warning }

---

## Part 2 — §6.2: properties of the integral

**Theorem.** If $$f \in \mathcal{R}[a,b]$$ then
$$\lvert f\rvert \in \mathcal{R}[a,b]$$ and

$$
\left\lvert\int_a^b f\right\rvert \le \int_a^b \lvert f\rvert .
$$

*Proof.* Integrability is the composition theorem with
$$\varphi(t) = \lvert t\rvert$$. For the bound,
$$-\lvert f\rvert \le f \le \lvert f\rvert$$ and the integral is monotone.
$$\square$$

The triangle inequality for integrals, and it is proved exactly like the one
for sums.

**Theorem (additivity over intervals).** For bounded $$f$$ on $$[a,b]$$ and
$$a < c < b$$,

$$
f \in \mathcal{R}[a,b] \iff f \in \mathcal{R}[a,c] \text{ and } f \in \mathcal{R}[c,b],
$$

and then $$\int_a^c f + \int_c^b f = \int_a^b f$$.

*Proof sketch.* Inserting $$c$$ into a partition only refines it, so the
Riemann criterion on $$[a,b]$$ transfers to each half and conversely.
$$\square$$

### Riemann's own definition

**Definition.** For a partition $$\mathcal{P} = \{x_0,\ldots,x_n\}$$ and tags
$$t_i \in [x_{i-1},x_i]$$, the **Riemann sum** is

$$
\mathcal{S}(\mathcal{P},f) = \sum_{i=1}^{n} f(t_i)\,\Delta x_i ,
$$

and the **mesh** is
$$\lVert\mathcal{P}\rVert = \max\{\Delta x_i : i = 1,\ldots,n\}$$.

**Definition.** $$\lim_{\lVert\mathcal{P}\rVert\to0}\mathcal{S}(\mathcal{P},f) = I$$
when for every $$\varepsilon > 0$$ there is $$\delta > 0$$ such that

$$
\left\lvert\sum_{i=1}^{n}f(t_i)\Delta x_i - I\right\rvert < \varepsilon
$$

for **every** partition with mesh below $$\delta$$ and **every** choice of
tags.

**Theorem.** For bounded $$f$$ on $$[a,b]$$ the two definitions agree:
$$\lim_{\lVert\mathcal{P}\rVert\to0}\mathcal{S}(\mathcal{P},f) = I$$ implies
$$f \in \mathcal{R}[a,b]$$ with $$\int_a^b f = I$$, and conversely.

Darboux's version is better for *proving* integrability, because it needs one
good partition rather than all fine ones; Riemann's is better for
*computing*, because it lets you choose convenient tags. The theorem says you
may use whichever is convenient.

### Suggested exercises

**2(a). Evaluate $$\int_a^b x^2\,\mathrm{d}x$$ by Riemann sums.**

$$x^2$$ is continuous, hence integrable, so any convenient partition and tags
will do. Take the uniform partition of $$[a,b]$$ with
$$h = (b-a)/n$$, $$x_i = a + ih$$, and tag with the right endpoints. Using
$$\sum_{i=1}^n i = \frac{n(n+1)}{2}$$ and
$$\sum_{i=1}^n i^2 = \frac{n(n+1)(2n+1)}{6}$$,

$$
\begin{aligned}
\mathcal{S} &= \sum_{i=1}^{n}(a+ih)^2 h \\
 &= h\left(na^2 + 2ah\tfrac{n(n+1)}{2} + h^2\tfrac{n(n+1)(2n+1)}{6}\right).
\end{aligned}
$$

With $$nh = b-a$$, the three terms tend to
$$a^2(b-a)$$, $$a(b-a)^2$$ and $$\tfrac13(b-a)^3$$, and

$$
a^2(b-a) + a(b-a)^2 + \tfrac13(b-a)^3 = \frac{b^3-a^3}{3} .
$$

$$\square$$

**6. If $$f, g \in \mathcal{R}[a,b]$$ with $$f \le g$$, then
$$\int_a^b f \le \int_a^b g$$.**

On each subinterval $$\sup f \le \sup g$$, so
$$\mathcal{U}(\mathcal{P},f) \le \mathcal{U}(\mathcal{P},g)$$ for every
partition; take infima. $$\square$$

**6 (second list). For continuous $$f$$ on $$[0,1]$$,**

$$
\lim_{n\to\infty}\frac1n\sum_{k=1}^{n}f\!\left(\frac kn\right) = \int_0^1 f(x)\,\mathrm{d}x .
$$

The left side is precisely the Riemann sum for the uniform partition of
$$[0,1]$$ into $$n$$ pieces with right-endpoint tags, and the mesh is
$$1/n \to 0$$. Since $$f$$ is continuous it is integrable, so by the theorem
above the Riemann sums converge to the integral. $$\square$$

This is the standard device for evaluating a limit of sums: **recognise it as
a Riemann sum.** For instance
$$\frac1n\sum_{k=1}^n \frac{1}{1+(k/n)^2} \to \int_0^1\frac{\mathrm dx}{1+x^2} = \frac\pi4$$.

---

## Part 3 — §6.3: the fundamental theorem of calculus

**Theorem (fundamental theorem of calculus).** If
$$f \in \mathcal{R}[a,b]$$ and $$F$$ is an antiderivative of $$f$$ on
$$[a,b]$$ — that is, $$F' = f$$ there — then

$$
\int_a^b f(x)\,\mathrm{d}x = F(b) - F(a) = \big[F(x)\big]_a^b .
$$

*Proof.* Let $$\mathcal{P} = \{x_0,\ldots,x_n\}$$ be any partition. Apply the
**mean value theorem** to $$F$$ on each $$[x_{i-1},x_i]$$: there is
$$t_i$$ inside with

$$
F(x_i) - F(x_{i-1}) = F'(t_i)\Delta x_i = f(t_i)\Delta x_i .
$$

Summing, the left side telescopes to $$F(b)-F(a)$$, so

$$
F(b)-F(a) = \sum_{i=1}^{n} f(t_i)\Delta x_i
$$

is a Riemann sum for $$f$$, and therefore lies between
$$\mathcal{L}(\mathcal{P},f)$$ and $$\mathcal{U}(\mathcal{P},f)$$ for **every**
$$\mathcal{P}$$. Since $$f$$ is integrable, the only number with that property
is $$\int_a^b f$$. $$\square$$

> **Two ingredients and no more: the mean value theorem, and a telescoping
> sum.** That is the whole of why antidifferentiation computes areas. Note
> what is *not* assumed — $$f$$ need not be continuous, only integrable with
> an antiderivative.
{: .prompt-tip }

### Suggested exercises

**2. For $$f \in \mathcal{R}[a,b]$$, the function
$$F(x) = \int_a^x f$$ is continuous on $$[a,b]$$.**

$$f$$ is bounded, say $$\lvert f\rvert \le M$$. For $$x < y$$ in $$[a,b]$$,
additivity and the triangle inequality give

$$
\lvert F(y)-F(x)\rvert = \left\lvert\int_x^y f\right\rvert
 \le \int_x^y \lvert f\rvert \le M\lvert y-x\rvert .
$$

So $$F$$ is Lipschitz with constant $$M$$, hence uniformly continuous.
$$\square$$

Worth noticing: **$$F$$ is better behaved than $$f$$.** Integration smooths —
a merely integrable $$f$$ has a Lipschitz $$F$$, and a continuous $$f$$ has a
continuously differentiable one. Differentiation does the opposite, as
[Chapter 5](/posts/analysis-differentiation/) showed.

**6(d). $$F(x) = \int_0^{x^2} f(t)\,\mathrm{d}t$$ with $$f$$ continuous: find
$$F'$$.**

Let $$G(u) = \int_0^u f$$, so $$G' = f$$ by the fundamental theorem — this is
the differentiation form, valid because $$f$$ is continuous — and
$$F(x) = G(x^2)$$. The chain rule gives

$$
F'(x) = G'(x^2)\cdot 2x = 2x\,f(x^2) .
$$

$$\square$$

**14. For continuous $$f$$ on $$[a,b]$$ with
$$M = \max\lvert f\rvert$$,**

$$
\lim_{n\to\infty}\left(\int_a^b \lvert f(x)\rvert^n\,\mathrm{d}x\right)^{1/n} = M .
$$

*Upper bound.* $$\lvert f\rvert^n \le M^n$$ gives
$$\left(\int_a^b\lvert f\rvert^n\right)^{1/n} \le M(b-a)^{1/n}$$, and
$$(b-a)^{1/n} \to 1$$.

*Lower bound.* Let $$\varepsilon > 0$$. The maximum is attained at some
$$c$$ by the extreme value theorem, and by continuity there is an interval
$$J \subseteq [a,b]$$ of length $$\ell > 0$$ on which
$$\lvert f\rvert > M - \varepsilon$$. Then

$$
\left(\int_a^b\lvert f\rvert^n\right)^{1/n}
 \ge \big((M-\varepsilon)^n \ell\big)^{1/n}
 = (M-\varepsilon)\,\ell^{1/n} ,
$$

and $$\ell^{1/n}\to1$$. So the limit is squeezed between $$M-\varepsilon$$ and
$$M$$ for every $$\varepsilon$$. $$\square$$

This says the $$L^n$$ norms converge to the sup norm, which is why the latter
is written $$\lVert f\rVert_\infty$$.

---

## Part 4 — §6.4: improper integrals

**Definition.** Let $$f$$ be real-valued on $$(a,b]$$ with
$$f \in \mathcal{R}[c,b]$$ for every $$c \in (a,b)$$. The **improper Riemann
integral** is

$$
\int_a^b f = \lim_{c \to a+}\int_c^b f ,
$$

when the limit exists. Infinite upper limits are handled the same way, with
$$\int_a^{\infty} f = \lim_{c\to\infty}\int_a^{c} f$$.

The definition exists because the Darboux construction requires $$f$$ bounded
on a bounded interval. An improper integral is a *limit of proper ones*, not a
new kind of integral.

### Suggested exercises

**1(d). Does $$\int_0^1 x\ln x\,\mathrm{d}x$$ exist, and what is it?**

The integrand is unbounded near $$0$$ — $$\ln x \to -\infty$$ — so the integral
is improper there. Integrating by parts on $$[c,1]$$,

$$
\begin{aligned}
\int_c^1 x\ln x\,\mathrm{d}x
 &= \left[\frac{x^2}{2}\ln x - \frac{x^2}{4}\right]_c^1 \\
 &= -\frac14 - \frac{c^2}{2}\ln c + \frac{c^2}{4} .
\end{aligned}
$$

As $$c \to 0+$$, $$c^2\ln c \to 0$$ — the polynomial beats the logarithm —
so the limit is $$-\tfrac14$$. $$\square$$

**5. If $$f$$ is absolutely integrable on $$[a,\infty)$$ and integrable on
$$[a,c]$$ for every $$c > a$$, then the improper integral of $$f$$ on
$$[a,\infty)$$ exists.**

Let $$F(c) = \int_a^c f$$. For $$c' > c$$,

$$
\lvert F(c') - F(c)\rvert = \left\lvert\int_c^{c'} f\right\rvert
 \le \int_c^{c'}\lvert f\rvert .
$$

Since $$\int_a^{\infty}\lvert f\rvert$$ converges, its tails go to $$0$$: given
$$\varepsilon$$ there is $$M$$ with $$\int_c^{c'}\lvert f\rvert < \varepsilon$$
for all $$c' > c > M$$. So $$F$$ satisfies the Cauchy criterion as
$$c \to \infty$$, and by the completeness of $$\mathbb{R}$$ — via
[Chapter 3](/posts/analysis-sequences/) — the limit exists. $$\square$$

**Absolute convergence implies convergence**, the integral version of the
theorem in [Chapter 7](/posts/analysis-series/), proved the same way.

**9. $$\Gamma(x) = \int_0^{\infty}e^{-t}t^{x-1}\,\mathrm{d}t$$ converges for
every $$x > 0$$.**

Split at $$1$$, since the integral is improper at both ends.

*Near $$0$$.* For $$0 < t \le 1$$ we have $$e^{-t} \le 1$$, so
$$e^{-t}t^{x-1} \le t^{x-1}$$ and

$$
\int_c^1 t^{x-1}\,\mathrm{d}t = \frac{1 - c^{x}}{x} \longrightarrow \frac1x
$$

as $$c \to 0+$$, finite because $$x > 0$$. The integrand is non-negative, so
convergence follows by monotonicity.

*Near $$\infty$$.* For large $$t$$, $$t^{x-1} \le e^{t/2}$$ — the exponential
beats any power — so $$e^{-t}t^{x-1} \le e^{-t/2}$$, whose integral to
infinity converges. $$\square$$

Both tails are handled by **comparison**, which is all one ever does with
improper integrals.

---

## Part 5 — §6.5: the Riemann–Stieltjes integral

### Replacing $$\mathrm{d}x$$

Let $$\alpha$$ be monotone increasing on $$[a,b]$$ and write
$$\Delta\alpha_i = \alpha(x_i) - \alpha(x_{i-1}) \ge 0$$. Everything from
§6.1 repeats verbatim with $$\Delta\alpha_i$$ in place of $$\Delta x_i$$:

$$
\begin{aligned}
\mathcal{U}(\mathcal{P},f,\alpha) &= \sum_{i=1}^{n}M_i\,\Delta\alpha_i , \\
\mathcal{L}(\mathcal{P},f,\alpha) &= \sum_{i=1}^{n}m_i\,\Delta\alpha_i ,
\end{aligned}
$$

$$
\begin{aligned}
\overline{\int_a^b} f\,\mathrm{d}\alpha &= \inf_{\mathcal{P}}\mathcal{U}(\mathcal{P},f,\alpha), \\
\underline{\int_a^b} f\,\mathrm{d}\alpha &= \sup_{\mathcal{P}}\mathcal{L}(\mathcal{P},f,\alpha).
\end{aligned}
$$

**Theorem.** For bounded $$f$$ and increasing $$\alpha$$,

$$
\overline{\int_a^b} f\,\mathrm{d}\alpha \ \ge\ \underline{\int_a^b} f\,\mathrm{d}\alpha ,
$$

and $$f$$ is **Riemann–Stieltjes integrable with respect to $$\alpha$$**,
written $$f \in \mathcal{R}(\alpha)$$, when they agree.

Monotonicity of $$\alpha$$ is what keeps $$\Delta\alpha_i \ge 0$$, and that is
the only place the old proofs used positivity of $$\Delta x_i$$. So the
refinement lemma, Riemann's criterion and the ordering of the integrals all
carry over unchanged.

**Theorem (Riemann's criterion).** $$f \in \mathcal{R}(\alpha)$$ if and only if
for every $$\varepsilon > 0$$ there is $$\mathcal{P}$$ with

$$
\mathcal{U}(\mathcal{P},f,\alpha) - \mathcal{L}(\mathcal{P},f,\alpha) < \varepsilon .
$$

**Theorem.** With $$\alpha$$ increasing:

- $$f$$ continuous on $$[a,b]$$ $$\Rightarrow$$ $$f \in \mathcal{R}(\alpha)$$;
- $$f$$ monotone and $$\alpha$$ continuous $$\Rightarrow$$
  $$f \in \mathcal{R}(\alpha)$$.

**Good behaviour is shared.** $$f$$ and $$\alpha$$ may not be discontinuous at
the same point — if both jump at $$c$$, no partition can make
$$\mathcal{U}-\mathcal{L}$$ small there, because the oscillation of $$f$$
multiplies a jump of $$\alpha$$ that refinement cannot shrink.

**Theorem (reduction to an ordinary integral).** If
$$f \in \mathcal{R}[a,b]$$ and $$\alpha$$ is increasing and differentiable
with $$\alpha' \in \mathcal{R}[a,b]$$, then $$f \in \mathcal{R}(\alpha)$$ and

$$
\int_a^b f\,\mathrm{d}\alpha = \int_a^b f(x)\alpha'(x)\,\mathrm{d}x .
$$

So for smooth $$\alpha$$ nothing new happens: $$\mathrm{d}\alpha = \alpha'\,\mathrm{d}x$$.
**The content is in the non-smooth $$\alpha$$**, and the extreme case is next.

### Sums as integrals

**Worked example from the notes.** Let $$I$$ be the unit step,
$$I(t) = 0$$ for $$t \le 0$$ and $$1$$ for $$t > 0$$, and set

$$
\alpha(x) = \sum_{n=1}^{N} c_n\, I(x - s_n)
$$

with $$\{s_n\}$$ a finite subset of $$(a,b]$$ and $$c_n \ge 0$$. Then for
continuous $$f$$,

$$
\int_a^b f\,\mathrm{d}\alpha = \sum_{n=1}^{N}c_n f(s_n) .
$$

*Proof.* $$\alpha$$ is increasing and constant except for a jump of size
$$c_n$$ at each $$s_n$$. Given a partition, $$\Delta\alpha_i$$ is the sum of
the $$c_n$$ for $$s_n$$ in the $$i$$-th subinterval, and zero otherwise. So
only subintervals containing some $$s_n$$ contribute, and as the mesh shrinks
each contributes $$c_n$$ times a value of $$f$$ within $$\delta$$ of
$$f(s_n)$$. Continuity of $$f$$ makes the error vanish. $$\square$$

> **This is why the Riemann–Stieltjes integral exists.** With $$\alpha(x) = x$$
> it is an ordinary integral; with $$\alpha$$ a step function it is a finite
> sum; with $$\alpha$$ a general increasing function it is both at once. One
> notation, one set of theorems, for discrete and continuous
> alike — which is exactly what a probability distribution needs, and why
> expectations are written $$\int x\,\mathrm{d}F(x)$$ whether the distribution
> is discrete or continuous.
{: .prompt-tip }

### Suggested exercises

**5(a). $$\displaystyle\int_0^{\pi/2}x\,\mathrm{d}(\sin x)$$.**

Here $$\alpha(x) = \sin x$$ is increasing and differentiable on
$$[0,\pi/2]$$ with $$\alpha' = \cos x$$ continuous, so the reduction theorem
applies:

$$
\int_0^{\pi/2}x\,\mathrm{d}(\sin x) = \int_0^{\pi/2}x\cos x\,\mathrm{d}x .
$$

Integrating by parts,
$$[x\sin x]_0^{\pi/2} - \int_0^{\pi/2}\sin x\,\mathrm{d}x = \frac\pi2 - 1$$.

**5(f). $$\displaystyle\int_0^{3}\big(x - \lfloor x\rfloor\big)\,\mathrm{d}x^3$$.**

Now $$\alpha(x) = x^3$$, increasing and smooth with
$$\alpha' = 3x^2$$, so the integral is
$$\int_0^3 (x - \lfloor x\rfloor)\,3x^2\,\mathrm{d}x$$. Split at the integers,
where $$\lfloor x\rfloor$$ is constant:

$$
\begin{aligned}
&\int_0^1 3x^3\,\mathrm{d}x + \int_1^2 3x^2(x-1)\,\mathrm{d}x \\
&\qquad + \int_2^3 3x^2(x-2)\,\mathrm{d}x .
\end{aligned}
$$

The first is $$\tfrac34$$. The second is
$$\left[\tfrac34x^4 - x^3\right]_1^2 = (12-8)-(\tfrac34-1) = \tfrac{17}{4}$$.
The third is
$$\left[\tfrac34x^4 - 2x^3\right]_2^3 = (\tfrac{243}{4}-54)-(12-16) = \tfrac{43}{4}$$.
The total is

$$
\tfrac34 + \tfrac{17}{4} + \tfrac{43}{4} = \tfrac{63}{4} .
$$

$$\square$$

Note that $$f$$ here has jump discontinuities at $$1$$ and $$2$$ while
$$\alpha$$ is continuous there, so the integral exists — the shared-jump
obstruction does not arise.

**3(a). $$\alpha$$ non-decreasing, $$f$$ bounded and
$$f \in \mathcal{R}(\alpha)$$, and $$F(x) = \int_a^x f\,\mathrm{d}\alpha$$.
Then $$\lvert F(x)-F(y)\rvert \le M\lvert\alpha(x)-\alpha(y)\rvert$$.**

Take $$M$$ with $$\lvert f\rvert \le M$$. For $$y < x$$, additivity gives
$$F(x)-F(y) = \int_y^x f\,\mathrm{d}\alpha$$, and on any partition of
$$[y,x]$$ every upper and lower sum is bounded by
$$M\sum\Delta\alpha_i = M(\alpha(x)-\alpha(y))$$ in absolute value, since
$$\Delta\alpha_i \ge 0$$ and these telescope. Hence

$$
\lvert F(x)-F(y)\rvert \le M\big(\alpha(x)-\alpha(y)\big) .
$$

$$\square$$

So $$F$$ is Lipschitz **with respect to $$\alpha$$** — exercise 2 of §6.3 is
the case $$\alpha(x) = x$$. In particular $$F$$ is continuous wherever
$$\alpha$$ is.

## Common pitfalls

- **Forgetting that $$f$$ must be bounded.** The Darboux sums are undefined
  otherwise; unbounded integrands need §6.4.
- **Thinking continuity is necessary for integrability.** Lebesgue's criterion
  allows a measure-zero set of discontinuities, which can be dense and even
  uncountable.
- **Confusing countable with measure zero.** Countable implies measure zero;
  the Cantor set shows the converse fails.
- **Confusing "zero except on a small set" with "integrable".** Exercise 3(c)
  is exactly this trap.
- **Assuming the composition theorem works in either order.**
  $$\varphi\circ f$$ needs $$\varphi$$ continuous on the outside.
- **Applying the fundamental theorem without an antiderivative on the whole
  interval.** $$F' = f$$ must hold throughout, endpoints included in the
  one-sided sense.
- **Using $$\mathrm{d}\alpha = \alpha'\,\mathrm{d}x$$ for non-differentiable
  $$\alpha$$.** That is precisely the case the Stieltjes integral exists to
  handle.
- **Letting $$f$$ and $$\alpha$$ jump at the same point.** Then
  $$f \notin \mathcal{R}(\alpha)$$.

## Connections

- **Backward.** Uniform continuity on compact sets from
  [Chapter 4](/posts/analysis-continuity/) proves continuous functions
  integrable; the countability of a monotone function's discontinuities, also
  from Chapter 4, proves monotone functions integrable; the mean value theorem
  of [Chapter 5](/posts/analysis-differentiation/) proves the fundamental
  theorem; the Cantor set of [Chapter 2](/posts/analysis-metric-spaces/)
  separates countable from measure zero; and the whole construction rests on
  the suprema of [Chapter 1](/posts/analysis-real-numbers/).
- **Forward.** [Chapter 7](/posts/analysis-series/) proves the integral
  version of absolute convergence implying convergence, and the integral test
  compares a series with an improper integral.
  [Chapter 8](/posts/analysis-function-sequences/) asks when
  $$\int \lim f_n = \lim \int f_n$$, and the answer — uniform convergence
  suffices — is one of the three interchange theorems.
- **Outward.** Measure zero is the doorway to Lebesgue measure, where the
  integral is built by partitioning the *range* instead of the domain and
  every bounded measurable function becomes integrable. The Riemann–Stieltjes
  integral is the first step toward measure-theoretic probability, where
  $$\int x\,\mathrm{d}F$$ is an expectation.

## Summary

- **Darboux** — upper and lower sums from suprema and infima; $$f$$ must be bounded
- **Refinement** lowers $$\mathcal{U}$$ and raises $$\mathcal{L}$$; common refinements compare any two partitions
- **Integrable** $$\iff$$ upper and lower integrals agree
- **Riemann's criterion** — one partition with $$\mathcal{U}-\mathcal{L} < \varepsilon$$
- **Continuous $$\Rightarrow$$ integrable**, by uniform continuity on a compact set
- **Monotone $$\Rightarrow$$ integrable**, by telescoping
- **Measure zero** — coverable by intervals of arbitrarily small total length; countable sets and the Cantor set qualify
- **Lebesgue's criterion** — integrable $$\iff$$ discontinuities have measure zero
- **Dirichlet** is not integrable; **Thomae's** is, with integral $$0$$
- **Riemann sums** with mesh $$\to 0$$ give the same integral; use Darboux to prove, Riemann to compute
- **Fundamental theorem** — mean value theorem plus telescoping
- **$$F(x) = \int_a^x f$$** is Lipschitz; integration smooths
- **Improper** — a limit of proper integrals; settle convergence by comparison
- **Riemann–Stieltjes** — $$\Delta x_i \to \Delta\alpha_i$$; smooth $$\alpha$$ gives $$\alpha'\,\mathrm{d}x$$, step $$\alpha$$ gives a finite sum
- **$$f$$ and $$\alpha$$ must not jump together**

## References

- Manfred Stoll, *Introduction to Real Analysis*, 2nd edition — Chapter 6. The suggested exercise numbers are Stoll's.
- Introduction to Mathematical Analysis (881.008), Seoul National University, Spring 2023. Instructor: Ja A Jeong (정자아). Typed lecture notes, Chapter VI.
- All proofs and all exercise solutions are mine; the notes leave every one blank. Written out in full are the refinement lemma, Riemann's criterion, integrability of continuous and of monotone functions, the fundamental theorem, and the step-function Stieltjes computation, because each carries a technique. The composition theorem, the additivity of the integral over subintervals, Lebesgue's criterion and the equivalence of the Darboux and Riemann definitions are stated and used but not proved, following the course's own weighting.
- The remark that a countable union of measure-zero sets has measure zero, and the observation that $$f$$ and $$\alpha$$ cannot share a discontinuity, are added here; the notes state neither.
