---
title: "Mathematical Analysis: Series of Real Numbers"
date: 2026-10-09 11:30:00 +0900
categories: [Course Notes, Mathematical Analysis]
tags: [series, convergence tests, dirichlet test, rearrangement, cauchy schwarz, square summable]
description: The ratio and root tests in their sharp limsup form, Abel summation and the Dirichlet test, absolute versus conditional convergence and Riemann's rearrangement theorem, and square summable sequences with the CBS and Minkowski inequalities. Chapter 7 of Introduction to Mathematical Analysis.
math: true
mermaid: false
render_with_liquid: false
---

> This chapter covers §§7.1–7.4.
{: .prompt-info }

## What this chapter answers

A series is a sequence in disguise: $$\sum a_k$$ means the sequence of partial
sums $$S_n = \sum_{k=1}^{n}a_k$$, and convergence of the series *is*
convergence of that sequence. So nothing here is new in principle, and
everything in [Chapter 3](/posts/analysis-sequences/) applies.

What the chapter adds is three things that do not follow from the general
theory.

**Tests.** Deciding whether $$S_n$$ converges by inspecting $$S_n$$ directly is
usually hopeless; the tests decide it from the terms $$a_k$$ alone. The sharp
forms use $$\limsup$$ rather than $$\lim$$ — the reason §3.5 bothered to
define it.

**The rearrangement theorem**, which is the chapter's one genuine shock. For
an absolutely convergent series the sum does not depend on the order. For a
conditionally convergent one, **the terms can be reordered to converge to any
real number you like.** Addition is commutative; infinite addition is not.

**A geometry on sequences.** §7.4 puts an inner product on square summable
sequences and proves the Cauchy–Bunyakovsky–Schwarz and Minkowski
inequalities, turning $$\ell^2$$ into a space with lengths and angles. It is
the first infinite-dimensional space in the course.

## Prerequisites

[Chapter 3](/posts/analysis-sequences/) throughout — partial sums are
sequences, $$\limsup$$ is needed for the sharp tests, and the Cauchy criterion
is how convergence gets proved without a candidate limit.
[Chapter 5](/posts/analysis-differentiation/) supplies the weighted AM–GM used
in §7.4, and [Chapter 6](/posts/analysis-integration/) the integral
comparison.

---

## Part 1 — §7.1: convergence tests

### The two tests, sharply

**Theorem (ratio test).** For a series $$\sum a_k$$ of positive terms, set

$$
R = \limsup_{k\to\infty}\frac{a_{k+1}}{a_k},
\qquad
r = \liminf_{k\to\infty}\frac{a_{k+1}}{a_k}.
$$

Then

$$
\begin{aligned}
R < 1 &\implies \textstyle\sum a_k < \infty , \\
r > 1 &\implies \textstyle\sum a_k = \infty , \\
r \le 1 \le R &\implies \text{inconclusive}.
\end{aligned}
$$

*Proof of the first.* Pick $$\rho$$ with $$R < \rho < 1$$. By the definition of
$$\limsup$$ there is $$N$$ with $$a_{k+1}/a_k < \rho$$ for all $$k \ge N$$, so
by induction $$a_{N+j} \le a_N\rho^{j}$$. The tail is dominated by a
convergent geometric series, and the partial sums of a positive series are
increasing, so by monotone convergence they converge. $$\square$$

**Theorem (root test).** For $$\sum a_k$$ with $$a_k \ge 0$$, set
$$\alpha = \limsup_{k\to\infty}\sqrt[k]{a_k}$$. Then
$$\alpha < 1$$ gives convergence and $$\alpha > 1$$ gives divergence.

*Proof.* If $$\alpha < \rho < 1$$ then eventually $$\sqrt[k]{a_k} < \rho$$, so
$$a_k < \rho^k$$ and comparison with the geometric series applies. If
$$\alpha > 1$$ then $$a_k \ge 1$$ for infinitely many $$k$$, so $$a_k \not\to 0$$
and the series cannot converge. $$\square$$

> The notes print the root test's second clause as "$$\alpha < 1$$" twice. The
> second should read $$\alpha > 1 \Rightarrow \sum a_k$$ diverges, as above.
{: .prompt-warning }

**Why $$\limsup$$ and not $$\lim$$.** The ratios need not converge. For

$$
a_k = \begin{cases} 2^{-k}, & k \text{ even} \\ 3^{-k}, & k \text{ odd}\end{cases}
$$

the ratio oscillates wildly and has no limit, while
$$\sqrt[k]{a_k} \le \tfrac12$$ always, so the root test settles it at once.
The $$\limsup$$ form of the test applies whenever the $$\lim$$ form does, and
in more cases besides.

### Which test is stronger

**Theorem.** For a sequence of positive numbers,

$$
\begin{aligned}
\liminf_{k\to\infty}\frac{a_{k+1}}{a_k}
 &\le \liminf_{k\to\infty}\sqrt[k]{a_k} \\
 &\le \limsup_{k\to\infty}\sqrt[k]{a_k}
 \le \limsup_{k\to\infty}\frac{a_{k+1}}{a_k} .
\end{aligned}
$$

**The root test is strictly stronger than the ratio test.** If the ratio test
concludes, the root test concludes the same way; the example above shows the
converse fails. The ratio test survives because ratios are usually easier to
compute — especially with factorials, which cancel.

### Suggested exercises

**8. If $$a_n > 0$$ for all $$n$$ and $$b_k = \frac1k\sum_{n=1}^{k}a_n$$, then
$$\sum b_k$$ diverges.**

Write $$A_k = \sum_{n=1}^k a_n$$, so $$b_k = A_k/k$$. Since $$a_1 > 0$$ and all
terms are positive, $$A_k \ge A_1 = a_1 > 0$$ for every $$k$$, hence

$$
b_k = \frac{A_k}{k} \ge \frac{a_1}{k} .
$$

The harmonic series $$\sum 1/k$$ diverges, so by comparison so does
$$\sum b_k$$. $$\square$$

**16. Cauchy condensation test.** If
$$a_1 \ge a_2 \ge \cdots \ge 0$$ then $$\sum_{k=1}^{\infty}a_k$$ converges if
and only if $$\sum_{k=0}^{\infty}2^{k}a_{2^{k}}$$ converges.

*Proof.* Both series have non-negative terms, so each converges exactly when
its partial sums are bounded, by monotone convergence.

Group the first series in blocks of lengths $$1, 2, 4, \ldots$$ and use
monotonicity to bound each block above by its first term and below by its
last. For $$n < 2^{m+1}$$,

$$
\begin{aligned}
S_n &\le a_1 + (a_2+a_3) + \cdots + (a_{2^m}+\cdots+a_{2^{m+1}-1}) \\
 &\le a_1 + 2a_2 + 4a_4 + \cdots + 2^{m}a_{2^{m}} ,
\end{aligned}
$$

so boundedness of the condensed sums bounds $$S_n$$. In the other direction,
for $$n > 2^m$$,

$$
\begin{aligned}
S_n &\ge a_1 + a_2 + (a_3+a_4) + \cdots + (a_{2^{m-1}+1}+\cdots+a_{2^m}) \\
 &\ge \tfrac12 a_1 + a_2 + 2a_4 + \cdots + 2^{m-1}a_{2^m} ,
\end{aligned}
$$

which is half the condensed partial sum. $$\square$$

**This is the quickest route to the $$p$$-series.** For $$a_k = k^{-p}$$ the
condensed series is
$$\sum 2^{k}2^{-kp} = \sum (2^{1-p})^{k}$$, geometric, converging exactly when
$$2^{1-p} < 1$$, i.e. $$p > 1$$. One line, where the integral test needs
[Chapter 6](/posts/analysis-integration/).

**19. $$c_k = \sum_{n=1}^{k}\frac1n - \ln k$$ is decreasing, positive, and
bounded below.**

*Decreasing.* Using $$\ln(1+x) \ge \frac{x}{1+x}$$ from
[Chapter 5](/posts/analysis-differentiation/) with $$x = 1/k$$,

$$
c_{k+1} - c_k = \frac{1}{k+1} - \ln\frac{k+1}{k}
 = \frac{1}{k+1} - \ln\left(1+\tfrac1k\right) \le 0 ,
$$

since $$\ln(1+1/k) \ge \frac{1/k}{1+1/k} = \frac{1}{k+1}$$.

*Positive, hence bounded below by $$0$$.* Using the other half of the same
inequality, $$\ln(1+x) \le x$$ with $$x = 1/n$$,

$$
\ln k = \sum_{n=1}^{k-1}\ln\frac{n+1}{n} \le \sum_{n=1}^{k-1}\frac1n < \sum_{n=1}^{k}\frac1n ,
$$

so $$c_k > 0$$. $$\square$$

By monotone convergence $$\{c_k\}$$ converges; its limit is the
**Euler–Mascheroni constant** $$\gamma \approx 0.5772$$, whose irrationality
is still unknown. Note that both halves came from the single inequality proved
by the mean value theorem in §5.2.

**21. For $$p, q > 0$$, the series**

$$
\sum_{k=1}^{\infty}\frac{(p+1)(p+2)\cdots(p+k)}{(q+1)(q+2)\cdots(q+k)}
$$

**converges exactly when $$q > p+1$$.**

The ratio of consecutive terms is

$$
\frac{a_{k+1}}{a_k} = \frac{p+k+1}{q+k+1} = 1 - \frac{q-p}{q+k+1} ,
$$

which tends to $$1$$, so the ratio test is inconclusive — the
$$r \le 1 \le R$$ case. The series lies exactly on the boundary where the test
fails, which is why the problem is set.

Instead compare with a $$p$$-series. Taking logarithms,

$$
\ln a_k = \sum_{j=1}^{k}\ln\frac{p+j}{q+j}
 = \sum_{j=1}^{k}\ln\left(1 - \frac{q-p}{q+j}\right),
$$

and since $$\ln(1-t) = -t + O(t^2)$$ for small $$t$$, the sum behaves like
$$-(q-p)\sum_{j\le k}\frac1j \approx -(q-p)\ln k$$. Hence
$$a_k \approx k^{-(q-p)}$$, and $$\sum a_k$$ converges exactly when
$$q - p > 1$$. $$\square$$

> This is **Raabe's test** in disguise: when the ratio tends to $$1$$, the
> rate at which it does so decides the question, and
> $$a_{k+1}/a_k \approx 1 - \beta/k$$ converges precisely when
> $$\beta > 1$$. Worth recognising, because the ratio test is silent on an
> entire family of natural series.
{: .prompt-tip }

---

## Part 2 — §7.2: the Dirichlet test

### Summation by parts

**Theorem (Abel's partial summation formula).** Let $$\{a_k\}$$, $$\{b_k\}$$
be real sequences, and set $$A_0 = 0$$ and $$A_n = \sum_{k=1}^{n}a_k$$. Then
for $$1 \le p \le q$$,

$$
\begin{aligned}
\sum_{k=p}^{q-1}a_kb_k
 &= \sum_{k=p}^{q-1}A_k(b_k - b_{k+1}) \\
 &\quad + A_qb_q - A_{p-1}b_p .
\end{aligned}
$$

*Proof.* Substitute $$a_k = A_k - A_{k-1}$$ and reindex — the sum telescopes.
$$\square$$

This is **integration by parts for sums**: a product $$a_kb_k$$ is traded for
a product of the "antiderivative" $$A_k$$ with the "derivative"
$$b_k - b_{k+1}$$, plus boundary terms. The analogy is exact, and so is the
use: it converts a series you cannot control into one you can.

### The test

**Theorem (Dirichlet test).** Suppose

1. the partial sums $$A_n = \sum_{k=1}^{n}a_k$$ form a **bounded** sequence;
2. $$b_1 \ge b_2 \ge \cdots$$;
3. $$b_k \to 0$$.

Then $$\sum_{k=1}^{\infty}a_kb_k$$ converges.

*Proof.* Say $$\lvert A_n\rvert \le M$$. By Abel's formula, for $$q > p$$,

$$
\begin{aligned}
\left\lvert\sum_{k=p}^{q-1}a_kb_k\right\rvert
 &\le M\sum_{k=p}^{q-1}(b_k - b_{k+1}) + Mb_q + Mb_p \\
 &= M(b_p - b_q) + Mb_q + Mb_p = 2Mb_p ,
\end{aligned}
$$

using $$b_k - b_{k+1} \ge 0$$ to drop the absolute values and telescoping.
Since $$b_p \to 0$$, the partial sums satisfy the Cauchy criterion, and
$$\mathbb{R}$$ is complete. $$\square$$

Note what the hypotheses are doing. The $$a_k$$ need not have a convergent
sum at all — only bounded partial sums, which allows oscillation. The
$$b_k$$ supply the decay. **Neither series need converge on its own.**

**Theorem (alternating series).** If $$b_1 \ge b_2 \ge \cdots \ge 0$$ with
$$b_k \to 0$$, then $$s = \sum_{k=1}^{\infty}(-1)^{k+1}b_k$$ converges, and
with $$s_n$$ the $$n$$-th partial sum,

$$
\lvert s - s_n\rvert \le b_{n+1} \quad\text{for every } n .
$$

*Proof.* Take $$a_k = (-1)^{k+1}$$, whose partial sums alternate between
$$0$$ and $$1$$ and are bounded; Dirichlet gives convergence. The error bound
follows because the tail is itself an alternating series with decreasing
terms, so it lies between $$0$$ and its first term. $$\square$$

**The error bound is the practically useful half.** It says the truncation
error of an alternating series never exceeds the first omitted term, which is
why alternating series are the easiest to compute with.

**Trigonometric series.** If $$b_1 \ge b_2 \ge \cdots$$ with $$b_k \to 0$$,
then

$$
\sum_{k=1}^{\infty}b_k\sin kt
$$

converges for every $$t \in \mathbb{R}$$, and

$$
\sum_{k=1}^{\infty}b_k\cos kt
$$

converges for every $$t$$ except possibly $$t = 2p\pi$$, $$p \in \mathbb{Z}$$.

*Why.* The partial sums of $$\sin kt$$ and $$\cos kt$$ are bounded for
$$t \notin 2\pi\mathbb{Z}$$ — sum the geometric series $$\sum e^{ikt}$$ and
take real and imaginary parts, giving a denominator
$$\lvert 1-e^{it}\rvert \ne 0$$ — so Dirichlet applies. At
$$t \in 2\pi\mathbb{Z}$$ the sine terms all vanish, which is why the sine
series has no exception, while the cosine series becomes $$\sum b_k$$, which
may diverge.

> $$\sum \frac{\sin kt}{k}$$ converges for every real $$t$$ although
> $$\sum \frac{1}{k}$$ does not. The oscillation of $$\sin kt$$ is doing the
> work, and the Dirichlet test is the tool that measures it.
{: .prompt-tip }

### Suggested exercises

**5(g). Test $$\displaystyle\sum_{k=1}^{\infty}\frac{\sin kt}{k^{p}}$$ for
$$t \in \mathbb{R}$$, $$p > 0$$.**

Converges for every such $$t$$ and $$p$$. Take $$a_k = \sin kt$$ and
$$b_k = k^{-p}$$. The $$b_k$$ decrease to $$0$$ since $$p > 0$$, and the
partial sums of $$\sin kt$$ are bounded, as above — for
$$t \in 2\pi\mathbb{Z}$$ they are identically $$0$$. Dirichlet applies.

For $$p > 1$$ the convergence is absolute, by comparison with the
$$p$$-series. For $$0 < p \le 1$$ it is **conditional** when
$$t \notin \pi\mathbb{Z}$$, since $$\sum\lvert\sin kt\rvert/k^{p}$$ then
diverges.

**1. If $$\sum a_k$$ converges and $$\{b_k\}$$ is monotone and bounded, then
$$\sum a_kb_k$$ converges.**

This is **Abel's test**, and it follows from Dirichlet by a shift. Being
monotone and bounded, $$b_k \to b$$ for some $$b$$, by §3.3. Write
$$b_k = b + c_k$$ where $$c_k = b_k - b$$ is monotone with $$c_k \to 0$$.
Then

$$
\sum a_kb_k = b\sum a_k + \sum a_kc_k .
$$

The first converges by hypothesis. For the second: $$\sum a_k$$ converges, so
its partial sums converge and are therefore bounded, and $$\{c_k\}$$ decreases
to $$0$$ — or increases to $$0$$, in which case apply the argument to
$$\{-c_k\}$$. Dirichlet gives convergence. $$\square$$

The trick of **splitting off the limit** so that what remains tends to zero is
worth keeping; it converts Abel's test into Dirichlet's in two lines.

---

## Part 3 — §7.3: absolute and conditional convergence

**Definition.** $$\sum a_k$$ **converges absolutely** when
$$\sum\lvert a_k\rvert$$ converges. It converges **conditionally** when it
converges but not absolutely.

**Theorem.** Every absolutely convergent series converges.

*Proof.* The Cauchy criterion for $$\sum\lvert a_k\rvert$$ gives, for
$$n > m$$ large,

$$
\left\lvert\sum_{k=m+1}^{n}a_k\right\rvert \le \sum_{k=m+1}^{n}\lvert a_k\rvert < \varepsilon ,
$$

so the partial sums of $$\sum a_k$$ are Cauchy, and $$\mathbb{R}$$ is
complete. $$\square$$

**Completeness is doing the work.** In $$\mathbb{Q}$$ the statement is false.

**Theorem (the tests, for general terms).** With
$$\alpha = \limsup\sqrt[k]{\lvert a_k\rvert}$$ and
$$R = \limsup\lvert a_{k+1}/a_k\rvert$$,
$$r = \liminf\lvert a_{k+1}/a_k\rvert$$:

$$
\begin{aligned}
\alpha < 1 \text{ or } R < 1 &\implies \textstyle\sum a_k \text{ absolutely convergent}; \\
\alpha > 1 \text{ or } r > 1 &\implies \textstyle\sum a_k \text{ divergent}; \\
\text{otherwise} &\implies \text{inconclusive}.
\end{aligned}
$$

The tests are really tests for *absolute* convergence; they say nothing about
the conditional case, which is what §7.2 is for.

### Rearrangement

**Definition.** A **rearrangement** of $$\sum a_k$$ is $$\sum a'_k$$ where
$$a'_k = a_{\sigma(k)}$$ for some bijection
$$\sigma : \mathbb{N} \to \mathbb{N}$$.

**Theorem.** If $$\sum a_k$$ converges absolutely, every rearrangement
converges to the same sum.

**Theorem (Riemann).** If $$\sum a_k$$ converges conditionally, then for every
$$\alpha \in \mathbb{R}$$ there is a rearrangement converging to $$\alpha$$.

*Proof idea.* Conditional convergence forces both
$$\sum a_k^{+} = \infty$$ and $$\sum a_k^{-} = \infty$$, where
$$a^{\pm}$$ are the positive and negative parts — if both were finite the
series would converge absolutely, and if exactly one were finite the series
would diverge. Meanwhile $$a_k \to 0$$. So: take positive terms in order until
the partial sum first exceeds $$\alpha$$, then negative terms until it first
drops below, then positive again, and so on. Each supply is inexhaustible, so
the process never stalls; and because $$a_k \to 0$$, the overshoot at each
turn tends to $$0$$. The partial sums converge to $$\alpha$$. $$\square$$

**Remark.** The same construction with two targets gives, for any
$$-\infty \le \alpha \le \beta \le \infty$$, a rearrangement with

$$
\liminf_{n\to\infty}S_n = \alpha, \qquad \limsup_{n\to\infty}S_n = \beta .
$$

Overshoot past $$\beta$$ and undershoot past $$\alpha$$ alternately instead of
converging.

> **Absolute convergence is what licenses treating an infinite sum like a
> finite one.** Commutativity of addition does not survive the passage to
> infinity by itself, and a conditionally convergent series has no sum in any
> order-independent sense — its apparent value is an artefact of the order you
> happened to write it in.
{: .prompt-warning }

### Suggested exercises

**6(g). Test $$\displaystyle\sum_{k=1}^{\infty}\frac{(-1)^k k^k}{(k+1)^k}$$ for
absolute and conditional convergence.**

Neither: the series **diverges**. The modulus of the $$k$$-th term is

$$
\frac{k^k}{(k+1)^k} = \left(\frac{k}{k+1}\right)^{k}
 = \left(1 + \frac1k\right)^{-k} \longrightarrow \frac1e ,
$$

so $$a_k \not\to 0$$ and the $$n$$-th term test rules out convergence.
$$\square$$

A reminder to check the simplest test first; the alternating sign is a
distraction here.

**9. $$1 + \tfrac12 - \tfrac13 + \tfrac14 + \tfrac15 - \tfrac16 + \cdots$$
diverges.**

The pattern is two positive terms then one negative, so group in threes:

$$
T_m = \sum_{j=1}^{m}\left(\frac{1}{3j-2} + \frac{1}{3j-1} - \frac{1}{3j}\right).
$$

Each bracket is at least

$$
\frac{1}{3j-2} + \frac{1}{3j-1} - \frac{1}{3j} \ \ge\ \frac{1}{3j} ,
$$

since the first two terms each exceed $$\frac{1}{3j}$$. So
$$T_m \ge \frac13\sum_{j=1}^m \frac1j \to \infty$$. The full partial sums
differ from the $$T_m$$ by at most two terms, each tending to $$0$$, so they
diverge too. $$\square$$

This is a **rearrangement of the alternating harmonic series**, which
converges to $$\ln 2$$. Riemann's theorem in action: reordering so that
positives outnumber negatives two to one sends the sum to $$+\infty$$.

**12. If $$a_k \ge 0$$ and $$\sum a_k = \infty$$, then $$\sum a'_k = \infty$$
for every rearrangement.**

With non-negative terms the partial sums are increasing, so the series either
converges or tends to $$\infty$$. Any partial sum $$\sum_{k\le n}a'_k$$ is a
sum of finitely many distinct $$a_j$$, hence is at most
$$\sum_{j \le N}a_j$$ for $$N$$ large enough to include all of them; and
conversely each $$\sum_{j\le N}a_j$$ is at most some
$$\sum_{k\le n}a'_k$$. So the two families of partial sums are mutually
cofinal and have the same supremum, namely $$\infty$$. $$\square$$

**For non-negative terms, rearrangement changes nothing** — the sum is a
supremum over finite subsets, which has no order in it. The pathology needs
cancellation.

**14. If every rearrangement of $$\sum a_k$$ converges, then $$\sum a_k$$
converges absolutely.**

Contrapositive. Suppose $$\sum a_k$$ does not converge absolutely. If it
diverges, the identity rearrangement already fails. If it converges
conditionally, Riemann's theorem provides a rearrangement converging to any
chosen value — and the same construction, overshooting without ever turning
back, provides one that diverges to $$+\infty$$. Either way some rearrangement
fails to converge. $$\square$$

So **absolute convergence is exactly order-independence**, and the two notions
could be used to define each other.

---

## Part 4 — §7.4: square summable sequences

### The space $$\ell^2$$

**Definition.** A sequence $$\{a_k\}$$ is **square summable**, written
$$\{a_k\} \in \ell^2$$, when

$$
\sum_{k=1}^{\infty}a_k^2 < \infty ,
$$

and its **norm** is

$$
\big\lVert \{a_k\}\big\rVert_2 = \sqrt{\sum_{k=1}^{\infty}a_k^2} .
$$

Square summable is weaker than summable: $$\{1/k\} \in \ell^2$$ since
$$\sum 1/k^2$$ converges, while $$\sum 1/k$$ does not.

### The CBS inequality

**Theorem (Cauchy–Bunyakovsky–Schwarz).** For real numbers,

$$
\sum_{k=1}^{n}\lvert a_kb_k\rvert
 \le \sqrt{\sum_{k=1}^{n}a_k^2}\ \sqrt{\sum_{k=1}^{n}b_k^2} .
$$

*Proof.* Write $$A = \sqrt{\sum a_k^2}$$ and $$B = \sqrt{\sum b_k^2}$$,
assuming both non-zero. By the arithmetic–geometric mean inequality
$$uv \le \tfrac12(u^2+v^2)$$ applied to
$$u = \lvert a_k\rvert/A$$ and $$v = \lvert b_k\rvert/B$$,

$$
\begin{aligned}
\sum_{k=1}^{n}\frac{\lvert a_kb_k\rvert}{AB}
 &\le \frac12\left(\frac{\sum a_k^2}{A^2} + \frac{\sum b_k^2}{B^2}\right) \\
 &= 1 .
\end{aligned}
$$

$$\square$$

The normalisation is the whole trick: scale each sequence to norm $$1$$, where
the inequality is easy, then scale back. The AM–GM step is the case
$$\alpha = \tfrac12$$ of exercise 6(b) of
[Chapter 5](/posts/analysis-differentiation/).

**Corollary.** If $$\{a_k\},\{b_k\} \in \ell^2$$ then $$\sum a_kb_k$$ converges
absolutely and

$$
\sum_{k=1}^{\infty}\lvert a_kb_k\rvert
 \le \big\lVert\{a_k\}\big\rVert_2\,\big\lVert\{b_k\}\big\rVert_2 .
$$

Let $$n \to \infty$$ in the theorem; the partial sums are increasing and
bounded.

**Definition (inner product).** For $$a, b \in \ell^2$$,

$$
\langle a, b\rangle = \sum_{k=1}^{\infty}a_kb_k ,
$$

which converges by the corollary, and

$$
\lvert\langle a,b\rangle\rvert \le \lVert a\rVert_2\,\lVert b\rVert_2 .
$$

### Minkowski

**Theorem (Minkowski's inequality — the triangle inequality for
$$\ell^2$$).** If $$\{a_k\},\{b_k\} \in \ell^2$$ then
$$\{a_k+b_k\} \in \ell^2$$ and

$$
\big\lVert\{a_k+b_k\}\big\rVert_2 \le \big\lVert\{a_k\}\big\rVert_2 + \big\lVert\{b_k\}\big\rVert_2 .
$$

*Proof.* Expand and apply CBS to the cross term:

$$
\begin{aligned}
\sum (a_k+b_k)^2 &= \sum a_k^2 + 2\sum a_kb_k + \sum b_k^2 \\
 &\le \lVert a\rVert_2^2 + 2\lVert a\rVert_2\lVert b\rVert_2 + \lVert b\rVert_2^2 \\
 &= \big(\lVert a\rVert_2 + \lVert b\rVert_2\big)^2 .
\end{aligned}
$$

Finiteness of the left side also proves $$\{a_k+b_k\} \in \ell^2$$.
$$\square$$

> **$$\ell^2$$ is a metric space, and an infinite-dimensional one.** With
> $$d(a,b) = \lVert a - b\rVert_2$$, Minkowski is exactly the triangle
> inequality that [Chapter 2](/posts/analysis-metric-spaces/) demanded, and
> the inner product supplies angles. It is complete, and it is the model for
> every Hilbert space — the natural home of Fourier series and of quantum
> mechanics.
{: .prompt-tip }

### Suggested exercise

**1(a). Is $$\left\{\dfrac{1}{\ln k}\right\}_{k=2}^{\infty}$$ in
$$\ell^2$$?**

No. We need $$\sum_{k=2}^{\infty}\frac{1}{(\ln k)^2}$$ to converge, and it
does not: $$\ln k$$ grows more slowly than any positive power of $$k$$, so for
large $$k$$,

$$
(\ln k)^2 \le k \quad\Longrightarrow\quad \frac{1}{(\ln k)^2} \ge \frac1k ,
$$

and comparison with the harmonic series gives divergence. $$\square$$

The inequality $$(\ln k)^2 \le k$$ for large $$k$$ is itself the statement
that $$(\ln k)^2/k \to 0$$, which is two applications of L'Hospital from
[Chapter 5](/posts/analysis-differentiation/). **Logarithms lose to every
power**, which is the comparison to reach for whenever one appears.

## Common pitfalls

- **Using the ratio test when the limit is $$1$$.** It is genuinely
  inconclusive; exercise 21 is a whole family living there.
- **Writing $$\lim$$ where $$\limsup$$ is meant.** The ratios or roots need not
  converge, and the sharp statements are in $$\limsup$$.
- **Forgetting the $$n$$-th term test.** If $$a_k \not\to 0$$ nothing else
  matters; exercise 6(g) is that case dressed up.
- **Applying Dirichlet without checking all three hypotheses.** Bounded
  partial sums, monotone $$b_k$$, and $$b_k \to 0$$ — dropping monotonicity
  breaks the telescoping in the proof.
- **Treating a conditionally convergent series as a number.** Its value
  depends on the order of summation.
- **Rearranging inside a proof without justification.** Legitimate for
  non-negative or absolutely convergent series; nowhere else.
- **Assuming $$\ell^2$$ contains only summable sequences.** $$\{1/k\}$$ is the
  standing counterexample.
- **Forgetting that CBS needs both sequences in $$\ell^2$$.** The finite form
  always holds; the infinite form needs both sides finite.

## Connections

- **Backward.** Partial sums are sequences, so monotone convergence, the
  Cauchy criterion and $$\limsup$$ all come from
  [Chapter 3](/posts/analysis-sequences/); the logarithmic inequality that
  settles the Euler–Mascheroni constant and the AM–GM behind CBS come from
  [Chapter 5](/posts/analysis-differentiation/); and absolute convergence
  implying convergence is the same argument as its integral form in
  [Chapter 6](/posts/analysis-integration/).
- **Forward.** [Chapter 8](/posts/analysis-function-sequences/) replaces the
  numbers $$a_k$$ by functions, and the Weierstrass M-test is the comparison
  test with the sup norm in place of absolute value. Uniform convergence of
  the trigonometric series of §7.2 is what makes Fourier theory work.
- **Outward.** $$\ell^2$$ is the first Hilbert space, and Riemann's
  rearrangement theorem has a converse in higher dimensions — the
  Lévy–Steinitz theorem, where the achievable sums form an affine subspace
  rather than all of $$\mathbb{R}$$.

## Summary

- **Series = sequence of partial sums**; everything from Chapter 3 applies
- **Ratio test** — $$R < 1$$ converges, $$r > 1$$ diverges, between is silent
- **Root test** — $$\limsup\sqrt[k]{a_k} < 1$$ converges; strictly stronger than the ratio test
- **Condensation** — $$\sum a_k$$ and $$\sum 2^k a_{2^k}$$ share their fate for decreasing non-negative terms; gives the $$p$$-series instantly
- **Abel summation** — integration by parts for sums
- **Dirichlet test** — bounded $$A_n$$, monotone $$b_k \to 0$$; neither series need converge alone
- **Alternating series** — converges, with error at most the first omitted term
- **Absolute $$\Rightarrow$$ convergent**, by the Cauchy criterion and completeness
- **Rearrangement** — absolute convergence keeps the sum; conditional convergence reaches every real
- **Order-independence $$\iff$$ absolute convergence**
- **$$\ell^2$$** — square summable; strictly larger than summable
- **CBS** — $$\sum\lvert a_kb_k\rvert \le \lVert a\rVert_2\lVert b\rVert_2$$, by normalising and AM–GM
- **Minkowski** — the triangle inequality, making $$\ell^2$$ a metric space

## References

- Manfred Stoll, *Introduction to Real Analysis*, 2nd edition — Chapter 7. The suggested exercise numbers are Stoll's.
- Introduction to Mathematical Analysis (881.008), Spring 2023. Instructor: Ja A Jeong (정자아). Typed lecture notes, Chapter VII.
- All proofs and all exercise solutions are mine; the notes leave every one blank. Written out in full are the ratio and root tests, Abel summation, the Dirichlet test and its alternating-series corollary, absolute convergence implying convergence, CBS and Minkowski. The comparison between the four ratio and root limits, the absolute-convergence rearrangement theorem and Riemann's rearrangement theorem are stated with a proof idea rather than in full, following the course's weighting.
- One correction. The notes state the root test with "$$\alpha < 1 \Rightarrow \sum a_k < \infty$$" twice; the second clause should be $$\alpha > 1 \Rightarrow$$ divergence.
- The identification of exercise 21 as a Raabe-type problem, the remark that non-negative series are rearrangement-invariant because their sum is a supremum over finite subsets, and the note on $$\ell^2$$ as the first Hilbert space are added here.
