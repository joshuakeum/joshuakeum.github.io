---
title: "Measure Theory and Real Analysis: 1B Riemann Integral Is Not Good Enough"
date: 2026-11-14 13:20:00 +0900
categories: [Study Notes, Measure Theory and Real Analysis]
tags: [riemann integral, unbounded functions, pointwise limits, exercises]
description: Why Riemann integration is not enough, through an unbounded function and a sequence of Riemann integrable functions whose pointwise limit is not, with worked exercises 1 and 4. Section 1B of Axler's Measure, Integration & Real Analysis.
math: true
mermaid: false
render_with_liquid: false
---

> Typeset from my handwritten notes for section 1B of Axler's *Measure,
> Integration & Real Analysis*. The exercise statements are the textbook's;
> the answers are mine, as I wrote them. Part of the [course
> overview](/posts/measure-theory-overview/).
{: .prompt-info }

## Notes

**Example (an unbounded function).** Define
$$f : [0,1] \to \mathbb{R}$$ by

$$
f(x) =
\begin{cases}
\dfrac{1}{\sqrt{x}} & (0 < x \le 1), \\[0.5em]
0 & (x = 0).
\end{cases}
$$

If $$x_0, x_1, \dots, x_n$$ is a partition of $$[0,1]$$, then
$$\displaystyle \sup_{[x_0,x_1]} f = \infty$$.

$$\downarrow$$

The upper Riemann sum of $$f$$ is thus $$\infty$$.

However,

$$
\int_x^1 f(t)\,dt = 2 - 2\sqrt{x}.
$$

$$
\therefore\ \lim_{x \to 0+} \int_x^1 f(t)\,dt = 2.
$$

**Example (a pointwise limit).** Let $$r_1, r_2, \dots$$ be a sequence that
includes each rational number in $$[0,1]$$ only once and doesn't include any
other. For $$k \in \mathbb{Z}^+$$, define $$f_k : [0,1] \to \mathbb{R}$$ by

$$
f_k(x) =
\begin{cases}
1 & \text{if } x \in \{r_1, \dots, r_k\}, \\
0 & \text{otherwise.}
\end{cases}
$$

Then, by [Exercise 1A.6](/posts/measure-theory-1a-riemann-integral/#ex-1a-6),

$$
\int_0^1 f_k = \int_0^1 0 = 0.
$$

However, defining $$f : [0,1] \to \mathbb{R}$$ by

$$
f(x) =
\begin{cases}
1 & x \in \mathbb{Q}, \\
0 & x \notin \mathbb{Q},
\end{cases}
$$

$$f$$ is not Riemann integrable as $$U(f,P,[0,1]) = 1$$ and
$$L(f,P,[0,1]) = 0$$ for all $$P$$.

In other words,

$$
\lim_{k \to \infty} \int_0^1 f_k(x) = 0 \ne \int_0^1 f.
$$

$$\hookrightarrow$$ A pointwise limit of a sequence of Riemann integrable
functions need not be Riemann integrable.

> **Theorem.** Suppose $$a, b, M \in \mathbb{R}$$ with $$a < b$$. Suppose
> $$f_1, f_2, \dots$$ is a sequence of "Riemann integrable" functions such
> that $$|f_k(x)| \le M$$. Suppose $$\lim_{k \to \infty} f_k(x)$$ exists for
> each $$x \in [a,b]$$. Define $$f : [a,b] \to \mathbb{R}$$ by
> $$f(x) = \lim_{k \to \infty} f_k(x)$$. If $$f$$ is Riemann integrable on
> $$[a,b]$$, then
>
> $$
> \int_a^b f = \lim_{k \to \infty} \int_a^b f_k.
> $$
{: .theorem #thm-interchange }

$$\hookrightarrow$$ Not too strong! (Does not work well with limits.)

## Exercises 1B

> **Exercise 1.** Define $$f : [0,1] \to \mathbb{R}$$ as follows:
>
> $$
> f(a) =
> \begin{cases}
> 0 & \text{if } a \text{ is irrational}, \\[0.3em]
> \dfrac{1}{n} & \text{if } a \text{ is rational and } n \text{ is the smallest positive integer such that } a = \dfrac{m}{n} \text{ for some integer } m.
> \end{cases}
> $$
>
> Show that $$f$$ is Riemann integrable and compute $$\displaystyle \int_0^1 f$$.
{: .problem #ex-1b-1 }

*Solution.* Divide $$[0,1]$$ into $$n(n-1)+2$$ equal subintervals
(partition $$P$$). All rational numbers $$q_k$$ with denominator at most $$n$$ are in at most
two subintervals; every other subinterval has supremum at most
$$\frac{1}{n+1}$$.

$$
\begin{aligned}
\therefore\ U(f,P,[0,1])
&\le \frac{2}{n(n-1)+2} \sum_{k=1}^{2+n(n-1)/2} f(q_k) + \frac{1}{n+1} \\
&\le \frac{2}{n(n-1)+2} \cdot
   \Bigl( 1 + 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{3} + \cdots \Bigr)
   + \frac{1}{n+1} \\
&= \frac{2}{n(n-1)+2} \cdot
   \Bigl( 2 + \sum_{k=2}^{n} \frac{k-1}{k} \Bigr) + \frac{1}{n+1} \\
&= \frac{2}{n(n-1)+2} \times
   \Bigl( n + 1 - \sum_{k=2}^{n} \frac{1}{k} \Bigr) + \frac{1}{n+1} \\
&\le \frac{2(n+1)}{n(n-1)+2} + \frac{1}{n+1}.
\end{aligned}
$$

$$
\therefore\ 0 \le U(f,[0,1]) \le U(f,P,[0,1])
\le \frac{2(n+1)}{n(n-1)+2} + \frac{1}{n+1} \xrightarrow{\,n \to \infty\,} 0.
$$

$$\therefore\ L(f,[0,1]) = U(f,[0,1]) = 0$$.

> **Exercise 4.** Give an example of bounded functions
> $$f, g : [0,1] \to \mathbb{R}$$ such that
>
> $$
> L(f,[0,1]) + L(g,[0,1]) < L(f+g,[0,1])
> $$
>
> and
>
> $$
> U(f+g,[0,1]) < U(f,[0,1]) + U(g,[0,1]).
> $$
{: .problem #ex-1b-4 }

*Solution.*

$$
f(x) =
\begin{cases}
1 & x \in \mathbb{Q}, \\
0 & x \notin \mathbb{Q},
\end{cases}
\qquad
g(x) =
\begin{cases}
1 & x \notin \mathbb{Q}, \\
0 & x \in \mathbb{Q}.
\end{cases}
$$

Then $$L(f,[0,1]) = L(g,[0,1]) = 0$$ and $$U(f,[0,1]) = U(g,[0,1]) = 1$$,
while $$f + g = 1$$, so $$L(f+g,[0,1]) = U(f+g,[0,1]) = 1$$. Hence
$$0 + 0 < 1$$ and $$1 < 1 + 1$$.

## References

- Sheldon Axler, *Measure, Integration & Real Analysis* — Section 1B and
  Exercises 1B. The exercise statements are quoted from the book.
- The notes and the exercise answers are mine, typeset from my handwritten
  notebook. The structure of each answer is unchanged; small slips in the
  answers are corrected.
