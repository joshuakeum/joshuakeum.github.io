---
title: "Measure Theory and Real Analysis: 1A Riemann Integral"
date: 2026-11-14 13:10:00 +0900
categories: [Study Notes, Measure Theory and Real Analysis]
tags: [riemann integral, riemann sums, partition, uniform continuity, exercises]
description: Partitions, lower and upper Riemann sums and integrals, and the Riemann integrability of continuous functions, with worked exercises 1, 3, 4, 6 and 11. Section 1A of Axler's Measure, Integration & Real Analysis.
math: true
mermaid: false
render_with_liquid: false
---

> Typeset from my handwritten notes for section 1A of Axler's *Measure,
> Integration & Real Analysis*. The exercise statements are the textbook's;
> the answers are mine, as I wrote them. Part of the [course
> overview](/posts/measure-theory-overview/).
{: .prompt-info }

## Notes

> **Definition (Partition).** Suppose $$a, b \in \mathbb{R}$$ with $$a < b$$.
> A partition of $$[a,b]$$ is a finite list of the form $$x_0, \dots, x_n$$
> where $$a = x_0 < x_1 < \cdots < x_{n-1} < x_n = b$$.
{: .definition #def-partition }

$$\Rightarrow$$ Consider $$[a,b]$$ as a union of closed intervals:

$$
[a,b] = [x_0,x_1] \cup [x_1,x_2] \cup \cdots \cup [x_{n-1},x_n].
$$

> **Definition (Infimum and supremum of a function).** If $$f$$ is a
> real-valued function and $$A$$ is a subset of the domain of $$f$$, then
>
> $$
> \inf_A f = \inf\{f(x) : x \in A\}
> \quad\text{and}\quad
> \sup_A f = \sup\{f(x) : x \in A\}.
> $$
{: .definition #def-inf-sup }

> **Definition (Lower and upper Riemann sums).** Suppose
> $$f : [a,b] \to \mathbb{R}$$ is a bounded function and $$P$$ is a partition
> $$x_0, \dots, x_n$$ of $$[a,b]$$. The lower Riemann sum
> $$L(f,P,[a,b])$$ and the upper Riemann sum $$U(f,P,[a,b])$$ are defined by
>
> $$
> L(f,P,[a,b]) = \sum_{j=1}^{n} (x_j - x_{j-1}) \inf_{[x_{j-1},x_j]} f
> $$
>
> and
>
> $$
> U(f,P,[a,b]) = \sum_{j=1}^{n} (x_j - x_{j-1}) \sup_{[x_{j-1},x_j]} f.
> $$
{: .definition #def-riemann-sums }

> **Theorem (Inequalities with Riemann sums).** Suppose
> $$f : [a,b] \to \mathbb{R}$$ is a bounded function and $$P, P'$$ are
> partitions of $$[a,b]$$ such that the list defining $$P$$ is a sublist of
> the list defining $$P'$$. Then
>
> $$
> L(f,P,[a,b]) \le L(f,P',[a,b]) \le U(f,P',[a,b]) \le U(f,P,[a,b]).
> $$
{: .theorem #thm-inequalities }

*Proof.* Suppose $$P$$ is the partition $$x_0, \dots, x_n$$ and $$P'$$ is the
partition $$x'_0, \dots, x'_N$$ of $$[a,b]$$. For each $$j = 1, \dots, n$$,
there exist $$k \in \{0, \dots, N-1\}$$ and a positive integer $$m$$ such that
$$x_{j-1} = x'_k < x'_{k+1} < \cdots < x'_{k+m} = x_j$$.

We have

$$
\begin{aligned}
(x_j - x_{j-1}) \inf_{[x_{j-1},x_j]} f
&= \sum_{i=1}^{m} (x'_{k+i} - x'_{k+i-1}) \inf_{[x_{j-1},x_j]} f \\
&\le \sum_{i=1}^{m} (x'_{k+i} - x'_{k+i-1}) \inf_{[x'_{k+i-1},x'_{k+i}]} f.
\end{aligned}
$$

$$\therefore L(f,P,[a,b]) \le L(f,P',[a,b])$$.

Other inequalities are trivial. $$\square$$

> **Theorem (Lower Riemann sums $$\le$$ upper Riemann sums).** Suppose
> $$f : [a,b] \to \mathbb{R}$$ is a bounded function and $$P, P'$$ are
> partitions of $$[a,b]$$. Then
>
> $$
> L(f,P,[a,b]) \le U(f,P',[a,b]).
> $$
{: .theorem #thm-lower-le-upper-sums }

*Proof.* Let $$P''$$ be the partition of $$[a,b]$$ obtained by merging the
lists that define $$P$$ and $$P'$$. Then

$$
L(f,P,[a,b]) \le L(f,P'',[a,b]) \le U(f,P'',[a,b]) \le U(f,P',[a,b]).
\ \square
$$

> **Definition (Lower and upper Riemann integrals).** Suppose
> $$f : [a,b] \to \mathbb{R}$$ is a bounded function. The lower Riemann
> integral $$L(f,[a,b])$$ and the upper Riemann integral $$U(f,[a,b])$$ of
> $$f$$ are defined by
>
> $$
> L(f,[a,b]) = \sup_P L(f,P,[a,b])
> $$
>
> and
>
> $$
> U(f,[a,b]) = \inf_P U(f,P,[a,b]),
> $$
>
> where the supremum and infimum above are taken over all partitions $$P$$ of
> $$[a,b]$$.
{: .definition #def-riemann-integrals }

> **Theorem (Lower Riemann integral $$\le$$ upper Riemann integral).**
> Suppose $$f : [a,b] \to \mathbb{R}$$ is a bounded function. Then
>
> $$
> L(f,[a,b]) \le U(f,[a,b]).
> $$
{: .theorem #thm-lower-le-upper-integral }

> **Definition (Riemann integrable).**
>
> - A bounded function on a closed bounded interval is called Riemann
>   integrable if its lower Riemann integral equals its upper Riemann
>   integral.
> - $$\displaystyle \int_a^b f = L(f,[a,b]) = U(f,[a,b])$$.
{: .definition #def-riemann-integrable }

> **Theorem (Continuous functions are Riemann integrable).** Every
> continuous real-valued function on each closed bounded interval is Riemann
> integrable.
{: .theorem #thm-continuous }

*Proof.* Suppose $$a, b \in \mathbb{R}$$ with $$a < b$$ and
$$f : [a,b] \to \mathbb{R}$$ is a continuous function ($$=$$ $$f$$ is bounded
and is uniformly continuous).

$$\Rightarrow$$ $$\forall \varepsilon > 0$$, $$\exists \delta > 0$$ such that

$$
|f(s) - f(t)| < \varepsilon \quad \forall\, s,t \in [a,b]
\text{ with } |s-t| < \delta. \tag{*}
$$

Let $$n \in \mathbb{Z}^+$$ be such that $$\frac{b-a}{n} < \delta$$, and let
$$P$$ be the equally spaced partition $$a = x_0, x_1, \dots, x_n = b$$ of
$$[a,b]$$ with $$x_j - x_{j-1} = \frac{b-a}{n}$$ for all
$$j = 1, \dots, n$$.

Then

$$
\begin{aligned}
U(f,[a,b]) - L(f,[a,b])
&\le U(f,P,[a,b]) - L(f,P,[a,b]) \\
&= \frac{b-a}{n} \sum_{j=1}^{n}
   \Bigl( \sup_{[x_{j-1},x_j]} f - \inf_{[x_{j-1},x_j]} f \Bigr) \\
&\le (b-a)\varepsilon \quad \text{by } (*),
\end{aligned}
$$

since $$U(f,[a,b]) = \inf_P U(f,P,[a,b])$$ and
$$L(f,[a,b]) = \sup_P L(f,P,[a,b])$$.

Thus $$U(f,[a,b]) - L(f,[a,b]) \le (b-a)\varepsilon$$ for all
$$\varepsilon > 0$$.

$$\therefore\ 0 \le U(f,[a,b]) - L(f,[a,b]) \le (b-a)\varepsilon$$ for all
$$\varepsilon > 0$$.

$$\therefore\ L(f,[a,b]) = U(f,[a,b])$$, so $$f$$ is Riemann integrable.
$$\square$$

> **Theorem (Bounds of the Riemann integral).** Suppose
> $$f : [a,b] \to \mathbb{R}$$ is Riemann integrable. Then
>
> $$
> (b-a) \inf_{[a,b]} f \le \int_a^b f \le (b-a) \sup_{[a,b]} f.
> $$
{: .theorem #thm-bounds }

## Exercises 1A

> **Exercise 1.** Suppose $$f : [a,b] \to \mathbb{R}$$ is a bounded function
> such that
>
> $$
> L(f,P,[a,b]) = U(f,P,[a,b])
> $$
>
> for some partition $$P$$ of $$[a,b]$$. Prove that $$f$$ is a constant
> function on $$[a,b]$$.
{: .problem #ex-1a-1 }

*Solution.* Consider a partition $$x_0, x_1, \dots, x_n$$ of $$[a,b]$$ where
$$L(f,P,[a,b]) = U(f,P,[a,b])$$.

Then

$$
L(f,P,[a,b]) = \sum_{j=1}^{n} (x_j - x_{j-1}) \inf_{[x_{j-1},x_j]} f
$$

and

$$
U(f,P,[a,b]) = \sum_{j=1}^{n} (x_j - x_{j-1}) \sup_{[x_{j-1},x_j]} f.
$$

$$
\therefore\ \sum_{j=1}^{n} (x_j - x_{j-1})
\Bigl( \sup_{[x_{j-1},x_j]} f - \inf_{[x_{j-1},x_j]} f \Bigr) = 0.
$$

$$\therefore\ \displaystyle \sup_{[x_{j-1},x_j]} f = \inf_{[x_{j-1},x_j]} f$$
for all $$j = 1, \dots, n$$.

$$\therefore$$ $$f$$ is a constant function.

> **Exercise 3.** Suppose $$f : [a,b] \to \mathbb{R}$$ is a bounded function.
> Prove that $$f$$ is Riemann integrable if and only if for each
> $$\varepsilon > 0$$, there exists a partition $$P$$ of $$[a,b]$$ such that
>
> $$
> U(f,P,[a,b]) - L(f,P,[a,b]) < \varepsilon.
> $$
{: .problem #ex-1a-3 }

*Solution.* ($$\Rightarrow$$) If $$f$$ is Riemann integrable,

$$
\sup_P L(f,P,[a,b]) = \inf_P U(f,P,[a,b]) = k.
$$

$$\therefore\ \forall \varepsilon' > 0$$, $$\exists P$$ such that
$$L(f,P,[a,b]) > k - \varepsilon'$$ and $$U(f,P,[a,b]) < k + \varepsilon'$$.

Take $$\varepsilon' = \frac{1}{2}\varepsilon$$. Then $$\forall \varepsilon > 0$$,
$$\exists P$$ (the merge of the two partitions above) such that

$$
U(f,P,[a,b]) - L(f,P,[a,b]) < 2\varepsilon' = \varepsilon.
$$

($$\Leftarrow$$) If $$\forall \varepsilon > 0$$, $$\exists P$$ such that
$$U(f,P,[a,b]) - L(f,P,[a,b]) < \varepsilon$$,

$$\therefore\ U(f,[a,b]) - L(f,[a,b]) < \varepsilon$$ for all
$$\varepsilon > 0$$.

$$\therefore\ U(f,[a,b]) = L(f,[a,b])$$.

$$\therefore$$ $$f$$ is Riemann integrable.

> **Exercise 4.** Suppose $$f, g : [a,b] \to \mathbb{R}$$ are Riemann
> integrable. Prove that $$f + g$$ is Riemann integrable on $$[a,b]$$ and
>
> $$
> \int_a^b (f+g) = \int_a^b f + \int_a^b g.
> $$
{: .problem #ex-1a-4 }

*Solution.* Assume a partition $$P$$ of $$[a,b]$$.

$$
\begin{cases}
L(f+g,P,[a,b]) \ge L(f,P,[a,b]) + L(g,P,[a,b]) \\[0.6em]
U(f+g,P,[a,b]) \le U(f,P,[a,b]) + U(g,P,[a,b])
\end{cases}
$$

$$
\begin{aligned}
L(f+g,[a,b]) &= \sup_P L(f+g,P,[a,b]) \ge L(f,[a,b]) + L(g,[a,b]) \\
&= U(f,[a,b]) + U(g,[a,b]) \ge \inf_P U(f+g,P,[a,b]) \\
&= U(f+g,[a,b]).
\end{aligned}
$$

Here the suprema and infima are taken over a common refinement of
partitions for $$f$$ and $$g$$.

Also, $$L(f+g,[a,b]) \le U(f+g,[a,b])$$.

$$
\therefore\ L(f+g,[a,b]) = U(f+g,[a,b]) = \int_a^b f + \int_a^b g.
$$

> **Exercise 6.** Suppose $$f : [a,b] \to \mathbb{R}$$ is Riemann integrable.
> Suppose $$g : [a,b] \to \mathbb{R}$$ is a function such that
> $$g(x) = f(x)$$ for all except finitely many $$x \in [a,b]$$. Prove that
> $$g$$ is Riemann integrable on $$[a,b]$$ and
>
> $$
> \int_a^b g = \int_a^b f.
> $$
{: .problem #ex-1a-6 }

*Solution.* Define $$a < x_1 < \cdots < x_n < b$$ to be the only values in
$$[a,b]$$ such that $$g(x) \ne f(x)$$.

Consider the partition $$P$$ where
$$a < x_1 - \varepsilon < x_1 + \varepsilon < \cdots < x_n - \varepsilon < x_n + \varepsilon < b$$.

$$
\begin{aligned}
\therefore\ U(g,P,[a,b]) &= U(f,P,[a,b]) \\
&\quad + \sum_{j=1}^{n} 2\varepsilon \max\bigl(0,\, g(x_j) - f(x_j)\bigr)
\end{aligned}
$$

and

$$
\begin{aligned}
L(g,P,[a,b]) &= L(f,P,[a,b]) \\
&\quad + \sum_{j=1}^{n} 2\varepsilon \min\bigl(0,\, g(x_j) - f(x_j)\bigr).
\end{aligned}
$$

Let $$\varepsilon \to 0$$.

$$
U(g,P,[a,b]) \le U(f,P,[a,b])
\quad\text{and}\quad
L(g,P,[a,b]) \ge L(f,P,[a,b]).
$$

$$\therefore\ \displaystyle \int_a^b g = \int_a^b f$$.

> **Exercise 11.** Suppose $$f : [a,b] \to \mathbb{R}$$ is Riemann integrable.
> Define $$F : [a,b] \to \mathbb{R}$$ by
>
> $$
> F(t) =
> \begin{cases}
> 0 & \text{if } t = a, \\[0.3em]
> \displaystyle \int_a^t f & \text{if } t \in (a,b].
> \end{cases}
> $$
>
> Prove that $$F$$ is continuous on $$[a,b]$$.
{: .problem #ex-1a-11 }

*Solution.* (i) Prove that $$F$$ is right-continuous at $$t = a$$.

$$
\Longleftrightarrow\ \lim_{t \to a+} \left| \int_a^t f \right| = 0.
$$

Consider the partition containing only $$a$$ and $$t$$.

$$
\begin{aligned}
\therefore\ \int_a^t f &= U(f,[a,t]) \le U(f,P,[a,t]) \\
&= (t-a) \sup_{[a,t]} f \le (t-a) \sup_{[a,b]} f.
\end{aligned}
$$

$$\therefore$$ As $$t \to a+$$,

$$
\lim_{t \to a+} \int_a^t f \le \lim_{t \to a+} (t-a) \sup_{[a,b]} f = 0.
$$

(ii) $$F$$ is continuous at every $$p \in (a,b)$$.

$$
\Longleftrightarrow\ \lim_{t \to p-} \int_a^t f
= \lim_{t \to p+} \int_a^t f = \int_a^p f.
$$

Consider the partition only with $$t$$ and $$p$$.

$$
\begin{aligned}
\int_a^t f &= \int_a^p f - \int_t^p f
= \int_a^p f - U(f,[t,p]) \\
&\ge \int_a^p f - U(f,P,[t,p]) \\
&= \int_a^p f + (t-p) \sup_{[t,p]} f \\
&\ge \int_a^p f + (t-p) \sup_{[a,b]} f.
\end{aligned}
$$

$$\therefore\ t \to p-:\quad \displaystyle \int_a^p f = \lim_{t \to p-} \int_a^t f$$.

$$\downarrow$$

Similarly do for every point.

## References

- Sheldon Axler, *Measure, Integration & Real Analysis* — Section 1A and
  Exercises 1A. The exercise statements are quoted from the book.
- The notes and the exercise answers are mine, typeset from my handwritten
  notebook. The structure of each answer is unchanged; small slips in the
  answers are corrected.
