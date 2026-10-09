---
title: "Mathematical Analysis: Sequences and Series of Functions"
date: 2026-10-09 12:00:00 +0900
categories: [Course Notes, Mathematical Analysis]
tags: [pointwise convergence, uniform convergence, weierstrass m-test, interchange of limits, power series]
description: Pointwise convergence and the three interchange questions it fails, uniform convergence and what it repairs, the Weierstrass M-test, and why differentiation is the hardest limit to interchange. Chapter 8 of Introduction to Mathematical Analysis, the last.
math: true
mermaid: false
render_with_liquid: false
---

> §8.1 follows the course notes, which end there. The rest — uniform
> convergence and the three interchange theorems — is reconstructed from the
> textbook, because §8.1 consists entirely of questions that only uniform
> convergence answers. This is the last chapter of the course.
{: .prompt-info }

## What this chapter answers

One question, asked three times: **when may two limits be exchanged?**

A sequence of functions $$f_n \to f$$ carries a limit in $$n$$. Continuity,
integration and differentiation each carry a limit of their own — in $$x$$, in
the mesh of a partition, in $$h$$. Putting them together gives three
questions, and the notes pose all three and answer none:

$$
\begin{aligned}
\lim_{t\to p}\lim_{n\to\infty}f_n(t) &\overset{?}{=} \lim_{n\to\infty}\lim_{t\to p}f_n(t) \\
\int_a^b \lim_{n\to\infty} f_n &\overset{?}{=} \lim_{n\to\infty}\int_a^b f_n \\
\Big(\lim_{n\to\infty}f_n\Big)' &\overset{?}{=} \lim_{n\to\infty}f_n'
\end{aligned}
$$

Under **pointwise** convergence all three fail, and §8.1 is a collection of
counterexamples. Under **uniform** convergence the first two hold and the
third still fails — it needs the derivatives to converge uniformly instead.

The distinction is the same quantifier swap as continuity versus uniform
continuity in [Chapter 4](/posts/analysis-continuity/), one level up. That is
not a coincidence; it is the same idea, and seeing it twice is the point of
meeting it here last.

## Prerequisites

[Chapter 4](/posts/analysis-continuity/) for continuity and the
pointwise-versus-uniform distinction;
[Chapter 6](/posts/analysis-integration/) for the Riemann integral;
[Chapter 7](/posts/analysis-series/) for series and the comparison test;
[Chapter 3](/posts/analysis-sequences/) for the Cauchy criterion.

---

## Part 1 — §8.1: pointwise convergence and the interchange of limits

### The definition

**Definition.** Let $$(X,d)$$ be a metric space, $$E \subseteq X$$, and
$$\{f_n\}_{n=1}^{\infty}$$ a sequence of real-valued functions on $$E$$. Then
$$\{f_n\}$$ **converges pointwise** on $$E$$ when the numerical sequence
$$\{f_n(x)\}$$ converges for every $$x \in E$$, and the **limit function** is

$$
f(x) = \lim_{n\to\infty}f_n(x) .
$$

Unpacked: for every $$x$$ and every $$\varepsilon > 0$$ there is
$$n_0 = n_0(\varepsilon, x)$$ with $$\lvert f_n(x)-f(x)\rvert < \varepsilon$$
for $$n \ge n_0$$. **The threshold may depend on $$x$$**, and everything in
this chapter turns on that.

### Three questions, three counterexamples

**Question 1. If each $$f_n$$ is continuous at $$p$$, is $$f$$?**

No. On $$[0,1]$$ take $$f_n(x) = x^{n}$$. Each is continuous, and

$$
f(x) = \lim_{n\to\infty}x^{n} = \begin{cases}0, & 0 \le x < 1 \\ 1, & x = 1,\end{cases}
$$

which is discontinuous at $$1$$. In the notation of the question,

$$
\lim_{t\to1-}\lim_{n\to\infty}t^{n} = 0
\quad\text{but}\quad
\lim_{n\to\infty}\lim_{t\to1-}t^{n} = 1 .
$$

**The two limits do not commute.** Why: near $$x = 1$$ the convergence is
slow, so no single $$n_0$$ works for all $$x$$ at once.

**Question 2. If each $$f_n$$ is differentiable at $$p$$, is $$f$$? And does
$$f'(p) = \lim f_n'(p)$$?**

No to both. Take

$$
f_n(x) = \frac{\sin nx}{\sqrt n} \quad\text{on } \mathbb{R} .
$$

Then $$\lvert f_n(x)\rvert \le 1/\sqrt n \to 0$$, so $$f_n \to 0$$ — even
uniformly. But

$$
f_n'(x) = \sqrt n\,\cos nx ,
$$

and $$f_n'(0) = \sqrt n \to \infty$$, while $$f'(0) = 0$$. So the derivatives
diverge although the functions converge perfectly.

For failure of differentiability itself, $$f_n(x) = \sqrt{x^2 + 1/n}$$
converges uniformly to $$\lvert x\rvert$$, which is not differentiable at
$$0$$ although every $$f_n$$ is.

**Question 3. If each $$f_n$$ is Riemann integrable on $$[a,b]$$, is $$f$$?
And does $$\int f = \lim \int f_n$$?**

No to both. For integrability, enumerate $$\mathbb{Q}\cap[0,1]$$ as
$$\{q_1,q_2,\ldots\}$$ and let $$f_n = 1$$ on $$\{q_1,\ldots,q_n\}$$ and $$0$$
elsewhere. Each $$f_n$$ is integrable with $$\int_0^1 f_n = 0$$ — finitely
many discontinuities, by [Chapter 6](/posts/analysis-integration/) — but
$$f_n \to$$ the Dirichlet function pointwise, which is not integrable at all.

For the value, take the **moving spike** on $$[0,1]$$: let $$f_n$$ be the
piecewise linear function that is $$0$$ outside $$(0, 2/n)$$, rises to $$n$$
at $$x = 1/n$$ and falls back. Each triangle has area $$1$$, so
$$\int_0^1 f_n = 1$$ for every $$n$$. But for any fixed $$x > 0$$ we have
$$f_n(x) = 0$$ once $$2/n < x$$, and $$f_n(0) = 0$$ always, so
$$f_n \to 0$$ pointwise and

$$
\int_0^1 \lim_n f_n = 0 \ne 1 = \lim_n\int_0^1 f_n .
$$

> **The mass escapes.** The spike keeps unit area while sliding towards
> $$0$$ and growing thinner. Pointwise convergence sees only what happens at
> each fixed $$x$$, and no fixed $$x$$ ever notices.
{: .prompt-warning }

### Suggested exercises

**2(a). Pointwise limit of $$\left\{\dfrac{nx}{1+nx}\right\}$$ on
$$[0,\infty)$$.**

At $$x = 0$$ every term is $$0$$. For $$x > 0$$, divide through by $$n$$:

$$
\frac{nx}{1+nx} = \frac{x}{1/n + x} \longrightarrow 1 .
$$

So

$$
f(x) = \begin{cases}0, & x = 0 \\ 1, & x > 0,\end{cases}
$$

discontinuous at $$0$$ although every $$f_n$$ is continuous. Another instance
of question 1, and again the convergence is slow near the bad point:
$$f_n(1/n) = 1/2$$ for every $$n$$.

**3(c). For which $$x$$ does $$\displaystyle\sum_{n=1}^{\infty}\frac{1}{3^{nx}}$$
converge?**

Write the terms as $$(3^{-x})^{n}$$, a geometric series with ratio
$$r = 3^{-x}$$. It converges exactly when $$\lvert r\rvert < 1$$, that is
$$3^{-x} < 1$$, that is $$x > 0$$. For $$x \le 0$$ the terms do not tend to
$$0$$. So the series converges precisely for $$x > 0$$, with sum
$$\dfrac{3^{-x}}{1-3^{-x}} = \dfrac{1}{3^{x}-1}$$.

Note that the convergence is **not uniform** on $$(0,\infty)$$: as
$$x \to 0+$$ the sum blows up, so no tail can be made small independently of
$$x$$. It *is* uniform on $$[\delta,\infty)$$ for each $$\delta > 0$$, by the
M-test below with $$M_n = 3^{-n\delta}$$.

---

## Part 2 — uniform convergence

> From here the notes stop. What follows is the standard treatment, included
> because §8.1 asks three questions whose only answer is uniform convergence.
{: .prompt-info }

### The definition

**Definition.** $$\{f_n\}$$ **converges uniformly** to $$f$$ on $$E$$ when

$$
\begin{aligned}
\forall\varepsilon>0,\ \exists n_0 \text{ such that} \\
\forall n \ge n_0,\ \forall x \in E, \\
\lvert f_n(x)-f(x)\rvert < \varepsilon .
\end{aligned}
$$

Set it beside pointwise convergence:

- **Pointwise:** $$\forall x\ \forall\varepsilon\ \exists n_0\ \forall n \ge n_0$$.
- **Uniform:** $$\forall\varepsilon\ \exists n_0\ \forall n \ge n_0\ \forall x$$.

Exactly the swap that separated continuity from uniform continuity in
[Chapter 4](/posts/analysis-continuity/).

**An equivalent form.** Defining
$$\lVert g\rVert_{\infty} = \sup_{x\in E}\lvert g(x)\rvert$$, uniform
convergence says

$$
\lVert f_n - f\rVert_{\infty} \longrightarrow 0 .
$$

So it is ordinary convergence in a metric space — the space of bounded
functions on $$E$$ with the **sup metric**. Everything
[Chapter 3](/posts/analysis-sequences/) proved about convergence in a metric
space applies at once, including the Cauchy criterion.

**Theorem (Cauchy criterion).** $$\{f_n\}$$ converges uniformly on $$E$$ if
and only if for every $$\varepsilon > 0$$ there is $$n_0$$ with

$$
\begin{aligned}
\lvert f_m(x) - f_n(x)\rvert &< \varepsilon \\
\text{for all } m,n \ge n_0 \text{ and}&\text{ all } x \in E .
\end{aligned}
$$

**Checking the two earlier examples.** For $$f_n(x) = x^n$$ on $$[0,1]$$,
$$\lVert f_n - f\rVert_{\infty} = \sup_{0\le x<1}x^{n} = 1$$ for every
$$n$$ — the convergence is pointwise and not uniform. For the moving spike,
$$\lVert f_n - 0\rVert_{\infty} = n \to \infty$$. Both failures are visible
immediately in the sup norm, which is the practical way to test.

### What uniform convergence repairs

**Theorem (continuity).** If each $$f_n$$ is continuous on $$E$$ and
$$f_n \to f$$ uniformly, then $$f$$ is continuous on $$E$$.

*Proof.* Fix $$p \in E$$ and $$\varepsilon > 0$$. Choose $$n$$ with
$$\lVert f_n - f\rVert_{\infty} < \varepsilon/3$$, then $$\delta$$ from
continuity of that single $$f_n$$ at $$p$$. For $$d(x,p) < \delta$$,

$$
\begin{aligned}
\lvert f(x)-f(p)\rvert
 &\le \lvert f(x)-f_n(x)\rvert \\
 &\quad + \lvert f_n(x)-f_n(p)\rvert \\
 &\quad + \lvert f_n(p)-f(p)\rvert
 < \varepsilon .
\end{aligned}
$$

$$\square$$

> **The $$\varepsilon/3$$ argument** is the single most quoted proof in
> analysis. Two of the three thirds come from uniform convergence — at
> $$x$$ and at $$p$$, and they need the *same* $$n$$, which is exactly what
> pointwise convergence cannot supply — and the middle third from continuity
> of one fixed function.
{: .prompt-tip }

**Theorem (integration).** If each $$f_n \in \mathcal{R}[a,b]$$ and
$$f_n \to f$$ uniformly on $$[a,b]$$, then $$f \in \mathcal{R}[a,b]$$ and

$$
\int_a^b f = \lim_{n\to\infty}\int_a^b f_n .
$$

*Proof of the value, granting integrability.* With
$$\varepsilon_n = \lVert f_n-f\rVert_{\infty} \to 0$$,

$$
\begin{aligned}
\left\lvert\int_a^b f_n - \int_a^b f\right\rvert
 &\le \int_a^b\lvert f_n - f\rvert \\
 &\le \varepsilon_n (b-a) \to 0 .
\end{aligned}
$$

$$\square$$

The factor $$b-a$$ is why the interval must be bounded, and the moving spike
shows what goes wrong without uniformity: there
$$\varepsilon_n = n$$ and the bound is useless.

**Theorem (differentiation).** Let $$\{f_n\}$$ be differentiable on
$$[a,b]$$, suppose $$\{f_n(x_0)\}$$ converges for some $$x_0$$, and suppose
$$\{f_n'\}$$ converges **uniformly** on $$[a,b]$$. Then $$\{f_n\}$$ converges
uniformly to some $$f$$, and

$$
f'(x) = \lim_{n\to\infty}f_n'(x) .
$$

**Read the hypotheses carefully.** It is not enough for $$f_n$$ to converge
uniformly — $$\frac{\sin nx}{\sqrt n}$$ does, and the conclusion fails. What
is needed is uniform convergence of the **derivatives**, plus convergence at a
single point to pin down the constant. Differentiation is the hardest
operation to interchange with a limit because it is the one that amplifies
small wiggles.

### Series of functions and the M-test

A series $$\sum_{n=1}^{\infty}g_n$$ of functions converges uniformly when its
partial sums do, so every theorem above applies verbatim.

**Theorem (Weierstrass M-test).** Suppose
$$\lvert g_n(x)\rvert \le M_n$$ for all $$x \in E$$, and
$$\sum_{n=1}^{\infty}M_n < \infty$$. Then $$\sum g_n$$ converges uniformly
and absolutely on $$E$$.

*Proof.* For $$m < n$$ and every $$x$$,

$$
\left\lvert\sum_{k=m+1}^{n}g_k(x)\right\rvert \le \sum_{k=m+1}^{n}M_k ,
$$

and the right side is small for large $$m$$ by the Cauchy criterion for
$$\sum M_n$$. The bound does not involve $$x$$, so the partial sums are
uniformly Cauchy. $$\square$$

**This is the comparison test of [Chapter 7](/posts/analysis-series/) with the
sup norm in place of the absolute value**, and it is how uniform convergence
is verified in practice. For instance
$$\sum \frac{\sin nx}{n^2}$$ converges uniformly on $$\mathbb{R}$$ with
$$M_n = 1/n^2$$, so its sum is continuous and may be integrated term by term.

**Power series.** A power series $$\sum a_n(x-c)^{n}$$ with radius of
convergence $$R$$ converges uniformly on every closed interval strictly inside
$$(c-R, c+R)$$, by the M-test with $$M_n = \lvert a_n\rvert \rho^{n}$$ for
$$\rho < R$$. So its sum is continuous there, may be integrated term by term,
and — because the differentiated series has the same radius — may be
differentiated term by term as well. That is the theorem which makes the
Taylor series of [Calculus 1](/posts/calculus-1-power-series/) legitimate, and
it is the natural endpoint of the course.

## Common pitfalls

- **Letting $$n_0$$ depend on $$x$$** and calling the convergence uniform.
  The whole chapter is that distinction.
- **Expecting uniform convergence of $$f_n$$ to control $$f_n'$$.**
  $$\frac{\sin nx}{\sqrt n}$$ converges uniformly to $$0$$ with derivatives
  blowing up.
- **Forgetting the point hypothesis in the differentiation theorem.** Without
  $$\{f_n(x_0)\}$$ converging, the $$f_n$$ can drift apart by constants.
- **Using the M-test with $$M_n$$ depending on $$x$$.** Then it is not a
  bound, and the proof's last step fails.
- **Assuming uniform convergence on an open interval** for a power series. It
  holds on compact subintervals, not necessarily up to the radius.
- **Integrating a pointwise limit over an unbounded interval.** Even uniform
  convergence does not survive it — the factor $$b-a$$ is infinite, and a
  spike can escape to infinity instead of to a point.

## Connections

- **Backward.** The quantifier swap is the one from
  [Chapter 4](/posts/analysis-continuity/), and the sup metric makes uniform
  convergence a special case of convergence in a metric space from
  [Chapter 3](/posts/analysis-sequences/). The M-test is the comparison test
  of [Chapter 7](/posts/analysis-series/), and the integration theorem needs
  [Chapter 6](/posts/analysis-integration/).
- **Across the course.** Every chapter contributes a counterexample here: the
  Dirichlet function from Chapter 6 as a non-integrable pointwise limit, the
  countability of $$\mathbb{Q}$$ from Chapter 1 to build it, and the
  oscillating derivative of Chapter 5 as the obstruction to interchanging
  differentiation.
- **Outward.** The space of continuous functions on $$[a,b]$$ with the sup
  metric is complete, and uniform convergence is convergence in it — the
  setting for the Stone–Weierstrass theorem, for Fourier series, and for the
  contraction mapping proof of existence for differential equations. The
  failure of the interchange under pointwise convergence is what Lebesgue
  integration repairs, with the dominated convergence theorem in place of
  uniformity.

## Summary

- **Pointwise** — $$n_0$$ may depend on $$x$$; **uniform** — it may not
- **Sup norm** — uniform convergence is $$\lVert f_n - f\rVert_{\infty}\to0$$, hence ordinary convergence in a metric space
- **Pointwise fails all three interchanges** — $$x^n$$ for continuity, the moving spike for integration, $$\frac{\sin nx}{\sqrt n}$$ for differentiation
- **Uniform + continuous $$\Rightarrow$$ continuous**, by the $$\varepsilon/3$$ argument
- **Uniform + integrable $$\Rightarrow$$ integrable**, with $$\int\lim = \lim\int$$ on a bounded interval
- **Differentiation needs $$f_n'$$ uniformly convergent**, plus convergence at one point
- **Weierstrass M-test** — $$\lvert g_n\rvert \le M_n$$ with $$\sum M_n < \infty$$ gives uniform convergence
- **Power series** converge uniformly on compact subintervals of the disc of convergence, so they may be differentiated and integrated term by term

## References

- Manfred Stoll, *Introduction to Real Analysis*, 2nd edition — Chapter 8.
- Introduction to Mathematical Analysis (881.008), Seoul National University, Spring 2023. Instructor: Ja A Jeong (정자아). Typed lecture notes, Chapter VIII.
- §8.1 follows the notes, which give the definition of pointwise convergence, pose the three interchange questions as exercises with blank space, and list two suggested exercises. The counterexamples and the exercise solutions are mine.
- **The notes end at §8.1.** Part 2 — uniform convergence, the Cauchy criterion, the continuity, integration and differentiation theorems, the Weierstrass M-test and the power series corollary — is reconstructed from the textbook's standard treatment. It is included because §8.1 is entirely questions, and uniform convergence is their answer; without it the chapter has no content. If the course covered this material differently, or did not reach it, this is where these write-ups part company with it.
