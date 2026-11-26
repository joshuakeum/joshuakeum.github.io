---
title: "Measure Theory and Real Analysis: 2E Convergence of Measurable Functions"
date: 2026-11-14 14:10:00 +0900
categories: [Study Notes, Measure Theory and Real Analysis]
tags: [uniform convergence, egorov, simple functions, luzin, lebesgue measurable functions, dini, exercises]
description: Pointwise and uniform convergence, Egorov's theorem, approximation by simple functions, Luzin's theorem and its alternative version, Lebesgue measurable functions and the summary of Chapter 2, with worked exercises 1 to 4, 6 to 10, 14 and 15. Section 2E of Axler's Measure, Integration & Real Analysis.
math: true
mermaid: false
render_with_liquid: false
---

> Typeset from my handwritten notes for section 2E of Axler's *Measure,
> Integration & Real Analysis*. The exercise statements are the textbook's;
> the answers are mine, as I wrote them. Where an answer of mine stopped
> short, the end is completed along the same lines. Part of the
> [course overview](/posts/measure-theory-overview/).
{: .prompt-info }

## Notes

> **Definition (Pointwise and uniform convergence).** Suppose $$X$$ is a set,
> $$f$$, $$f_1, f_2, \dots$$ is a sequence of functions from $$X$$ to
> $$\mathbb{R}$$, and $$f$$ is a function from $$X$$ to $$\mathbb{R}$$.
>
> - The sequence $$f_1, f_2, \dots$$ *converges pointwise on $$X$$ to $$f$$* if
>   $$\displaystyle\lim_{k \to \infty} f_k(x) = f(x)$$ for all $$x \in X$$. In
>   other words, $$f_1, f_2, \dots$$ converges pointwise on $$X$$ to $$f$$ if
>   $$\forall x \in X$$ and $$\forall \varepsilon > 0$$, $$\exists n \in
>   \mathbb{Z}^+$$ such that $$\lvert f_k(x) - f(x)\rvert < \varepsilon$$
>   $$\forall k \ge n$$.
> - The sequence $$f_1, f_2, \dots$$ *converges uniformly on $$X$$ to $$f$$* if
>   $$\forall \varepsilon > 0$$, $$\exists n \in \mathbb{Z}^+$$ such that
>   $$\lvert f_k(x) - f(x)\rvert < \varepsilon$$ $$\forall k \ge n$$ and
>   $$\forall x \in X$$.
{: .definition #def-convergence }

$$\rightarrow$$ The pointwise limit of continuous functions need not be
continuous.

$$\rightarrow$$ However, the uniform limit of continuous functions is
continuous.

> **Theorem (Uniform limit of continuous functions is continuous).** Suppose
> $$B \subseteq \mathbb{R}$$ and $$f_1, f_2, \dots$$ is a sequence of functions
> from $$B$$ to $$\mathbb{R}$$ that converges uniformly on $$B$$ to a function
> $$f : B \to \mathbb{R}$$. Suppose $$b \in B$$ and $$f_k$$ is continuous at
> $$b$$ for all $$k \in \mathbb{Z}^+$$. Then $$f$$ is continuous at $$b$$.
{: .theorem #thm-uniform-limit }

*Proof.* Suppose $$\varepsilon > 0$$. Let $$n \in \mathbb{Z}^+$$ be such that
$$\lvert f_n(x) - f(x)\rvert < \frac{1}{3}\varepsilon$$ for all $$x \in B$$.
Since $$f_n$$ is continuous at $$b$$, there exists $$\delta > 0$$ such that
$$\lvert f_n(a) - f_n(b)\rvert < \frac{1}{3}\varepsilon$$ for all
$$a \in N_\delta(b) \cap B$$. Now, suppose $$a \in N_\delta(b) \cap B$$. Then,

$$
\lvert f(a) - f(b)\rvert \le \lvert f(a) - f_n(a)\rvert + \lvert f_n(a) -
f_n(b)\rvert + \lvert f_n(b) - f(b)\rvert < \varepsilon.
$$

Thus, $$f$$ is continuous at $$b$$. $$\square$$

> **Theorem (Egorov's Theorem).** Suppose $$(X, \mathcal{S}, \mu)$$ is a
> measure space with $$\mu(X) < \infty$$. Suppose $$f_1, f_2, \dots$$ is a
> sequence of $$\mathcal{S}$$-measurable functions from $$X$$ to $$\mathbb{R}$$
> that converges pointwise on $$X$$ to a function $$f : X \to \mathbb{R}$$.
> Then for every $$\varepsilon > 0$$, there exists a set $$E \in \mathcal{S}$$
> such that $$\mu(X \setminus E) < \varepsilon$$ and $$f_1, f_2, \dots$$
> converges *uniformly* to $$f$$ on $$E$$.
{: .theorem #thm-egorov }

*Proof.* Suppose $$\varepsilon > 0$$. Fix $$n \in \mathbb{Z}^+$$. Then the
definition of pointwise convergence gives

$$
X = \bigcup_m \bigcap_{k=m}^{\infty} \Bigl\{ x \in X : \lvert f_k(x) - f(x)\rvert
< \frac{1}{n} \Bigr\}.
$$

For $$m \in \mathbb{Z}^+$$, let
$$A_{m,n} = \bigcap_{k=m}^{\infty} \{x \in X : \lvert f_k(x) - f(x)\rvert <
\frac{1}{n}\}$$. Also, each $$A_{m,n} \in \mathcal{S}$$ as each $$f_k - f$$ is an
$$\mathcal{S}$$-measurable function. Now, $$A_{1,n} \subseteq A_{2,n} \subseteq
\cdots$$ is an increasing sequence of sets and $$X = \bigcup_m A_{m,n}$$.

This gives that $$\lim_{m \to \infty} \mu(A_{m,n}) = \mu(X)$$. $$\therefore\
\exists m_n \in \mathbb{Z}^+$$ s.t.
$$\mu(X) - \mu(A_{m_n,n}) = \mu(X \setminus A_{m_n,n}) < \dfrac{1}{2^n}
\varepsilon$$ (as $$\mu(X) < \infty$$).

Now, let $$E = \bigcap_n A_{m_n,n}$$, then

$$
\mu(X \setminus E) = \mu\Bigl( X \setminus \bigcap_n A_{m_n,n} \Bigr)
= \mu\Bigl( \bigcup_n (X \setminus A_{m_n,n}) \Bigr) \le \sum_n \mu(X \setminus
A_{m_n,n}) < \varepsilon.
$$

To complete the proof, we must verify that $$f_1, f_2, \dots$$ converges
uniformly to $$f$$ on $$E$$. To do this, suppose $$\varepsilon' > 0$$. Let
$$n \in \mathbb{Z}^+$$ be such that $$\frac{1}{n} < \varepsilon'$$. Then
$$E \subseteq A_{m_n,n}$$, which implies that
$$\lvert f_k(x) - f(x)\rvert < \frac{1}{n} < \varepsilon'$$ for all
$$k \ge m_n$$ and all $$x \in E$$. Hence, $$f_1, f_2, \dots$$ does indeed
converge uniformly to $$f$$ on $$E$$. $$\square$$

**Example.** Consider Lebesgue measure $$\lambda$$ on the interval $$[-1, 1]$$
and the sequence of functions $$f_1, f_2, \dots$$ where

$$
f_k(x) =
\begin{cases}
1 & (x \in (-\infty, -1/k) \cup (1/k, \infty)), \\
kx + 2 & (x \in [-1/k, 0)), \\
2 - kx & (x \in [0, 1/k])
\end{cases}
$$

that converges pointwise but not uniformly. Suppose $$\varepsilon > 0$$. Taking
$$E = [-1, -\frac{\varepsilon}{4}] \cup [\frac{\varepsilon}{4}, 1]$$, we have
$$\lambda([-1, 1] \setminus E) < \varepsilon$$ and $$f_1, f_2, \dots$$ converges
uniformly on $$E$$.

> **Definition (Simple functions).** A function is called *simple* if it takes
> on only finitely many values.
{: .definition #def-simple-function }

In other words, supposing $$(X, \mathcal{S})$$ is a measurable space,
$$f : X \to \mathbb{R}$$ is a simple function, and $$c_1, \dots, c_n$$ are
distinct nonzero values of $$f$$,

$$
f = c_1 \chi_{E_1} + \cdots + c_n \chi_{E_n}, \qquad E_k = f^{-1}(\{c_k\}).
$$

Here, $$f$$ is an $$\mathcal{S}$$-measurable function, iff
$$E_1, \dots, E_n \in \mathcal{S}$$.

> **Theorem (Approximation by simple functions).** Suppose $$(X, \mathcal{S})$$
> is a measurable space and $$f : X \to [-\infty, \infty]$$ is
> $$\mathcal{S}$$-measurable. Then there exists a sequence $$f_1, f_2, \dots$$
> of functions from $$X$$ to $$\mathbb{R}$$ as follows:
>
> - **(a)** each $$f_k$$ is a simple $$\mathcal{S}$$-measurable function;
> - **(b)** $$\lvert f_k(x)\rvert \le \lvert f_{k+1}(x)\rvert \le \lvert f(x)\rvert$$
>   for all $$k \in \mathbb{Z}^+$$ and all $$x \in X$$;
> - **(c)** $$\displaystyle\lim_{k \to \infty} f_k(x) = f(x)$$ for every
>   $$x \in X$$;
> - **(d)** $$f_1, f_2, \dots$$ converges uniformly on $$X$$ to $$f$$ if $$f$$ is
>   bounded.
{: .theorem #thm-simple-approximation }

*Proof.* The idea of the proof is that for each $$k \in \mathbb{Z}^+$$ and
$$n \in \mathbb{Z}$$, the interval $$[n, n+1)$$ is divided into $$2^k$$
equally sized half-open subintervals. If $$f(x) \in [0, k]$$, we define
$$f_k(x)$$ to be the left endpoint of the subinterval into which $$f(x)$$
falls; if $$f(x) \in [-k, 0)$$, we define $$f_k(x)$$ to be the right endpoint of
that subinterval. Also, if $$\lvert f(x)\rvert > k$$, we define $$f_k(x) =
\pm k$$.

In other words,

$$
f_k(x) =
\begin{cases}
\dfrac{m}{2^k} & \text{if } 0 \le f(x) \le k \text{ and } m \in \mathbb{Z}
\text{ is such that } f(x) \in \bigl[\frac{m}{2^k}, \frac{m+1}{2^k}\bigr), \\[0.7em]
\dfrac{m+1}{2^k} & \text{if } -k \le f(x) < 0 \text{ and } m \in \mathbb{Z}
\text{ is such that } f(x) \in \bigl[\frac{m}{2^k}, \frac{m+1}{2^k}\bigr), \\[0.7em]
k & \text{if } f(x) > k, \\
-k & \text{if } f(x) < -k.
\end{cases}
$$

As $$f$$ is $$\mathcal{S}$$-measurable, every $$f^{-1}\bigl(\bigl[\frac{m}{2^k},
\frac{m+1}{2^k}\bigr)\bigr) \in \mathcal{S}$$, meaning that $$f_k$$ is an
$$\mathcal{S}$$-measurable simple function. Also, by definition,
$$\lvert f_k(x) - f(x)\rvert \le \frac{1}{2^k}$$ for all $$x \in X$$ such that
$$f(x) \in [-k, k]$$, and $$\lvert f_k(x)\rvert \le \lvert f_{k+1}(x)\rvert \le
\lvert f(x)\rvert$$, meaning that (b), (c), (d) hold. $$\square$$

> **Theorem (Luzin's Theorem).** Suppose $$g : \mathbb{R} \to \mathbb{R}$$ is a
> Borel measurable function. Then, $$\forall \varepsilon > 0$$, $$\exists$$
> closed set $$F \subseteq \mathbb{R}$$ s.t. $$\lvert \mathbb{R} \setminus F\rvert
> < \varepsilon$$ and $$g\vert_F$$ is a continuous function on $$F$$.
{: .theorem #thm-luzin }

\* **Note:** $$f\vert_B$$ being continuous on $$B$$ is NOT the same as saying
that $$f$$ (on its original domain) is continuous at each point of $$B$$. For
example, $$\chi_{\mathbb{Q}}$$ is indeed discontinuous at every point of
$$\mathbb{R}$$, but restricting its domain to $$\mathbb{R} \setminus \mathbb{Q}$$,
$$\chi_{\mathbb{Q}}\vert_{\mathbb{R} \setminus \mathbb{Q}}$$ is continuous on
$$\mathbb{R} \setminus \mathbb{Q}$$ as the function is identically $$0$$ on its
domain.

**Note 2:** The meaning of Luzin's theorem is that an arbitrary Borel
measurable function is almost continuous, in the sense that its complement has
arbitrarily small measure. (A restriction to a large closed set (= whose
complement has arbitrarily small measure) is continuous.) *(Quite surprising.)*

*Proof.* First, consider the special case where
$$g = d_1\chi_{D_1} + \cdots + d_n\chi_{D_n}$$ for some distinct nonzero
$$d_1, \dots, d_n \in \mathbb{R}$$ and some disjoint Borel sets
$$D_1, \dots, D_n \subseteq \mathbb{R}$$. Suppose $$\varepsilon > 0$$. For each
$$k \in \{1, \dots, n\}$$, there exist a closed set $$F_k \subseteq D_k$$ and an
open set $$G_k \supseteq D_k$$ such that
$$\lvert G_k \setminus D_k\rvert < \frac{\varepsilon}{4n}$$ and
$$\lvert D_k \setminus F_k\rvert < \frac{\varepsilon}{2n}$$ (approximating Borel
sets by closed and open sets, 2D). Here, we have
$$\lvert G_k \setminus F_k\rvert < \frac{\varepsilon}{n}$$ for all
$$k \in \{1, \dots, n\}$$.

Let $$F = \bigl( \bigcup_k F_k \bigr) \cup \bigl( \bigcap_k (\mathbb{R}
\setminus G_k) \bigr)$$. Then $$F$$ is a closed subset of $$\mathbb{R}$$ and
$$\mathbb{R} \setminus F \subseteq \bigcup_{k=1}^{n} (G_k \setminus F_k)$$.

$$\therefore\ \lvert \mathbb{R} \setminus F\rvert < \varepsilon$$.

Also, as $$F_k \subseteq D_k$$, we see that $$g(F_k) = \{d_k\}$$. Thus,
$$g\vert_{F_k}$$ is continuous for each $$k \in \{1, \dots, n\}$$. Because
$$\bigcap_{k=1}^{n} (\mathbb{R} \setminus G_k) \subseteq \bigcap_{k=1}^{n}
(\mathbb{R} \setminus D_k)$$, we see that
$$g\bigl( \bigcap_{k=1}^{n} (\mathbb{R} \setminus G_k) \bigr) = \{0\}$$. Thus,
$$g\vert_{\bigcap_k (\mathbb{R} \setminus G_k)}$$ is continuous. Altogether,
$$g\vert_F$$ is continuous (use Exercise 9 in this section: the sets
$$F_1, \dots, F_n$$ and $$\bigcap_k (\mathbb{R} \setminus G_k)$$ are disjoint
closed sets).

Now consider an arbitrary Borel measurable function
$$g : \mathbb{R} \to \mathbb{R}$$. Approximating by simple functions, there
exists a sequence $$g_1, g_2, \dots$$ of functions from $$\mathbb{R}$$ to
$$\mathbb{R}$$ that converges pointwise on $$\mathbb{R}$$ to $$g$$, where each
$$g_k$$ is a simple Borel measurable function.

Suppose $$\varepsilon > 0$$. Thus, $$\forall k \in \mathbb{Z}^+$$, $$\exists$$
closed set $$C_k \subseteq \mathbb{R}$$ s.t.
$$\lvert \mathbb{R} \setminus C_k\rvert < \frac{\varepsilon}{2^{k+1}}$$ and
$$g_k\vert_{C_k}$$ is continuous. Define $$C = \bigcap_k C_k$$. Therefore,
$$C$$ is closed, and $$g_k\vert_C$$ is continuous $$\forall k \in \mathbb{Z}^+$$.
Also, since $$\mathbb{R} \setminus C = \bigcup_k (\mathbb{R} \setminus C_k)$$,
$$\lvert \mathbb{R} \setminus C\rvert \le \sum_k \frac{\varepsilon}{2^{k+1}} =
\frac{1}{2}\varepsilon$$.

For each $$m \in \mathbb{Z}$$, the sequence $$g_1\vert_{(m,m+1)},
g_2\vert_{(m,m+1)}, \dots$$ converges pointwise to $$g\vert_{(m,m+1)}$$. Thus,
by Egorov's theorem, $$\forall m \in \mathbb{Z}$$, there is a Borel set
$$E_m \subseteq (m, m+1)$$ s.t. $$g_1, g_2, \dots$$ converges uniformly on
$$E_m$$ and $$\lvert (m, m+1) \setminus E_m\rvert < \dfrac{\varepsilon}{2^{\lvert
m\rvert + 3}}$$.

Thus, $$g_1, g_2, \dots$$ converges uniformly to $$g$$ on $$C \cap E_m$$ and, as
each $$g_k\vert_C$$ is continuous, $$g\vert_{C \cap E_m}$$ is continuous
$$\forall m \in \mathbb{Z}$$. Letting $$D = \bigcup_{m \in \mathbb{Z}}
(C \cap E_m)$$, $$g\vert_D$$ is continuous (each $$C \cap E_m$$ lies in the open
interval $$(m, m+1)$$, and these intervals are disjoint).

Since $$\mathbb{R} \setminus D \subseteq \mathbb{Z} \cup \bigl( \bigcup_{m}
((m, m+1) \setminus E_m) \bigr) \cup (\mathbb{R} \setminus C)$$,

$$
\lvert \mathbb{R} \setminus D\rvert \le \lvert \mathbb{Z}\rvert + \sum_{m \in
\mathbb{Z}} \frac{\varepsilon}{2^{\lvert m\rvert + 3}} + \lvert \mathbb{R}
\setminus C\rvert < \frac{3}{8}\varepsilon + \frac{1}{2}\varepsilon,
$$

using $$\lvert \mathbb{Z}\rvert = 0$$ and $$\sum_{m \in \mathbb{Z}}
2^{-\lvert m\rvert} = 3$$.

That is, $$\lvert \mathbb{R} \setminus D\rvert < \frac{7}{8}\varepsilon$$. There
exists a closed set $$F \subseteq D$$ s.t. $$\lvert D \setminus F\rvert <
\varepsilon - \lvert \mathbb{R} \setminus D\rvert$$ (by the closed
approximation of 2D). Now $$\lvert \mathbb{R} \setminus F\rvert \le \lvert
\mathbb{R} \setminus D\rvert + \lvert D \setminus F\rvert < \varepsilon$$.
Because the restriction of a continuous function to a smaller domain is also
continuous, $$g\vert_F$$ is continuous, completing the proof. $$\square$$

To get another version of Luzin's theorem, we need the following result.

> **Theorem (Continuous extensions of continuous functions).**
>
> - **(a)** Every continuous function on a closed subset of $$\mathbb{R}$$ can
>   be extended to a continuous function on all of $$\mathbb{R}$$.
> - **(b)** More precisely, if $$F \subseteq \mathbb{R}$$ is closed and
>   $$g : F \to \mathbb{R}$$ is continuous, then there exists a continuous
>   function $$h : \mathbb{R} \to \mathbb{R}$$ s.t. $$h\vert_F = g$$.
{: .theorem #thm-continuous-extension }

*Proof.* Suppose $$F \subseteq \mathbb{R}$$ is closed and $$g : F \to
\mathbb{R}$$ is continuous. Thus $$\mathbb{R} \setminus F$$ is the union of a
collection of disjoint open intervals $$\{I_k\}$$. For each such interval of the
form $$(a, \infty)$$ or of the form $$(-\infty, a)$$, define $$h(x) = g(a)$$ for
all $$x$$ in the interval. For each interval $$I_k$$ of the form $$(b, c)$$ with
$$b < c$$ and $$b, c \in \mathbb{R}$$, define $$h$$ on $$[b, c]$$ to be the
linear function s.t. $$h(b) = g(b)$$ and $$h(c) = g(c)$$.

Define $$h(x) = g(x)$$ for all $$x \in F$$ for which $$h(x)$$ has not been
defined by the two paragraphs. Then $$h : \mathbb{R} \to \mathbb{R}$$ is
continuous, and $$h\vert_F = g$$. $$\square$$

The next version of Luzin's theorem can be understood by saying that the value
of a Borel measurable function can be changed on a set with small Lebesgue
measure to produce a continuous function.

> **Theorem (Alternative Luzin's theorem).** Suppose $$E \subseteq \mathbb{R}$$
> and $$g : E \to \mathbb{R}$$ is a Borel measurable function. Then, for every
> $$\varepsilon > 0$$, there exist a closed set $$F \subseteq E$$ and a
> continuous function $$h : \mathbb{R} \to \mathbb{R}$$ s.t.
> $$\lvert E \setminus F\rvert < \varepsilon$$ and $$h\vert_F = g\vert_F$$.
{: .theorem #thm-alternative-luzin }

*Proof.* Suppose $$\varepsilon > 0$$. Extend $$g$$ to a function $$\tilde{g}$$
by defining

$$
\tilde{g}(x) =
\begin{cases}
g(x) & \text{if } x \in E, \\
0 & \text{if } x \in \mathbb{R} \setminus E.
\end{cases}
$$

By the first version of Luzin's theorem, there is a closed set
$$C \subseteq \mathbb{R}$$ s.t. $$\lvert \mathbb{R} \setminus C\rvert <
\varepsilon$$ and $$\tilde{g}\vert_C$$ is continuous on $$C$$. There exists a
closed set $$F \subseteq C \cap E$$ s.t.
$$\lvert (C \cap E) \setminus F\rvert < \varepsilon - \lvert \mathbb{R}
\setminus C\rvert$$. Thus,

$$
\lvert E \setminus F\rvert \le \lvert ((C \cap E) \setminus F) \cup (\mathbb{R}
\setminus C)\rvert \le \lvert (C \cap E) \setminus F\rvert + \lvert \mathbb{R}
\setminus C\rvert < \varepsilon.
$$

Now, we can extend $$\tilde{g}\vert_F$$ to a continuous function
$$h : \mathbb{R} \to \mathbb{R}$$. As $$\tilde{g}\vert_C$$ is continuous on $$C$$
and $$F \subseteq C$$, $$\tilde{g}\vert_F$$ is continuous on $$F$$, and because
$$F \subseteq E$$, $$\tilde{g}\vert_F = g\vert_F$$. $$\square$$

> **Definition (Lebesgue measurable function).** A function
> $$f : A \to \mathbb{R}$$, where $$A \subseteq \mathbb{R}$$, is called
> *Lebesgue measurable* if $$f^{-1}(B)$$ is a Lebesgue measurable set for every
> Borel set $$B \subseteq \mathbb{R}$$.
{: .definition #def-lebesgue-measurable-function }

From the definition, we know that if $$f : A \to \mathbb{R}$$ is Lebesgue
measurable, then $$A$$ is a Lebesgue measurable subset of $$\mathbb{R}$$ since
$$f^{-1}(\mathbb{R}) = A$$. Also, if $$A$$ is a Lebesgue measurable subset of
$$\mathbb{R}$$, then the definition above is the standard definition of an
$$\mathcal{S}$$-measurable function, where $$\mathcal{S}$$ is the
$$\sigma$$-algebra of all Lebesgue measurable subsets of $$A$$.

**Summary of Chapter 2.**

- A Borel set is an element of the smallest $$\sigma$$-algebra on $$\mathbb{R}$$
  containing all the open subsets of $$\mathbb{R}$$.
- A Lebesgue measurable set is an element of the smallest $$\sigma$$-algebra on
  $$\mathbb{R}$$ that contains all the open subsets of $$\mathbb{R}$$ and all the
  subsets of $$\mathbb{R}$$ with outer measure $$0$$.
- Every Lebesgue measurable set differs from a Borel set by a set with outer
  measure $$0$$.
- Outer measure restricted to the $$\sigma$$-algebra of Lebesgue measurable sets
  is also called Lebesgue measure.
- A function $$f : A \to \mathbb{R}$$, where $$A \subseteq \mathbb{R}$$, is
  called Borel measurable if $$f^{-1}(B)$$ is a Borel set for every Borel set
  $$B \subseteq \mathbb{R}$$.
- A function $$f : A \to \mathbb{R}$$, where $$A \subseteq \mathbb{R}$$, is
  called Lebesgue measurable if $$f^{-1}(B)$$ is a Lebesgue measurable set for
  every Borel set $$B \subseteq \mathbb{R}$$.

$$\circledast$$ A great way to simplify the potential confusion about Lebesgue
measurable functions being defined by inverse images of Borel sets is to only
consider Borel measurable functions. Such is proved by the following theorem.

> **Theorem.** Every Lebesgue measurable function is almost Borel measurable
> function. Then there exists a Borel measurable function
> $$g : \mathbb{R} \to \mathbb{R}$$ s.t.
> $$\lvert \{x \in \mathbb{R} : g(x) \ne f(x)\}\rvert = 0$$.
{: .theorem #thm-almost-borel }

*Proof.* There exists a sequence $$f_1, f_2, \dots$$ of Lebesgue measurable
simple functions from $$\mathbb{R}$$ to $$\mathbb{R}$$ converging pointwise on
$$\mathbb{R}$$ to $$f$$ (approximation by simple functions). Suppose
$$k \in \mathbb{Z}^+$$. Then there exist $$c_1, \dots, c_n \in \mathbb{R}$$ and
disjoint Lebesgue measurable sets $$A_1, \dots, A_n \subseteq \mathbb{R}$$ such
that $$f_k = c_1\chi_{A_1} + \cdots + c_n\chi_{A_n}$$.

For each $$j \in \{1, \dots, n\}$$, there exists a Borel set
$$B_j \subseteq A_j$$ s.t. $$\lvert A_j \setminus B_j\rvert = 0$$ (since $$A_j$$
is Lebesgue measurable). Let $$g_k = c_1\chi_{B_1} + \cdots + c_n\chi_{B_n}$$.
Then $$g_k$$ is a Borel measurable function, and
$$\lvert \{x \in \mathbb{R} : g_k(x) \ne f_k(x)\}\rvert = 0$$ (this set is
contained in $$\bigcup_j (A_j \setminus B_j)$$).

If $$x \notin \bigcup_k \{x \in \mathbb{R} : g_k(x) \ne f_k(x)\}$$, then
$$g_k(x) = f_k(x)$$ for all $$k \in \mathbb{Z}^+$$, and hence
$$\lim_{k \to \infty} g_k(x) = f(x)$$.

Let $$E = \{x \in \mathbb{R} : \lim_{k \to \infty} g_k(x) \text{ exists}\}$$.
$$E$$ is a Borel subset of $$\mathbb{R}$$ (by exercise 2B.14(b)). Also,
$$\mathbb{R} \setminus E \subseteq \bigcup_k \{x \in \mathbb{R} : g_k(x) \ne
f_k(x)\}$$ (because there the limit exists and equals $$f(x)$$), so
$$\lvert \mathbb{R} \setminus E\rvert \le \sum_k \lvert \{g_k \ne f_k\}\rvert =
0$$.

Now, $$\lvert \mathbb{R} \setminus E\rvert = 0$$. For $$x \in \mathbb{R}$$ let

$$
g(x) = \begin{cases} \lim_{k \to \infty} g_k(x) & x \in E, \\ 0 & x \in
\mathbb{R} \setminus E. \end{cases}
$$

For $$k \in \mathbb{Z}^+$$, $$\chi_E \cdot g_k$$ is Borel measurable, and
$$g(x) = \lim_{k \to \infty} (\chi_E \cdot g_k)(x)$$. Also, $$\forall k \in
\mathbb{Z}^+$$, $$\chi_E g_k$$ is Borel measurable, implying that $$g$$ is Borel
measurable.

Now, $$\{x \in \mathbb{R} : g(x) \ne f(x)\} \subseteq \bigcup_k \{x \in
\mathbb{R} : g_k(x) \ne f_k(x)\} \cup (\mathbb{R} \setminus E)$$, so
$$\lvert \{x \in \mathbb{R} : g(x) \ne f(x)\}\rvert \le \sum_k \lvert \{x :
g_k(x) \ne f_k(x)\}\rvert + \lvert \mathbb{R} \setminus E\rvert = 0$$. $$\square$$

## Exercises

> **Exercise 1.** Suppose $$X$$ is a finite set. Explain why a sequence of
> functions from $$X$$ to $$\mathbb{R}$$ that converges pointwise on $$X$$ also
> converges uniformly on $$X$$.
{: .problem #ex-2e-1 }

*Solution.* Suppose $$f_1, f_2, \dots$$ is a sequence of functions from
$$X = \{x_1, \dots, x_n\}$$ to $$\mathbb{R}$$ that converges pointwise on $$X$$
to $$f$$. By definition, for any $$\varepsilon > 0$$ and every
$$i \in \{1, \dots, n\}$$, there exists $$m_i \in \mathbb{Z}^+$$ such that
$$\lvert f_k(x_i) - f(x_i)\rvert < \varepsilon$$ for all $$k \ge m_i$$.

Let $$m' = \max\{m_1, \dots, m_n\}$$. Since $$\{m_1, \dots, m_n\}$$ is finite,
this set has a minimum and a maximum, and $$m'$$ is finite. Then for all
$$x_i \in \{x_1, \dots, x_n\}$$ and all integers $$k \ge m'$$,
$$\lvert f_k(x_i) - f(x_i)\rvert < \varepsilon$$, meaning that
$$f_1, f_2, \dots$$ converges uniformly on $$X$$.

> **Exercise 2.** Give an example of a sequence of functions from
> $$\mathbb{Z}^+$$ to $$\mathbb{R}$$ that converges pointwise on
> $$\mathbb{Z}^+$$ but does not converge uniformly on $$\mathbb{Z}^+$$.
{: .problem #ex-2e-2 }

*Solution.* Let $$f_k : \mathbb{Z}^+ \to \mathbb{R}$$ be

$$
f_k(n) =
\begin{cases}
1 & (n = k), \\
0 & (n \ne k),
\end{cases}
\qquad\text{and}\qquad f(n) = 0 \text{ for all } n.
$$

For every $$n$$, $$f_k(n) = 0$$ for all $$k > n$$, so
$$f_k \to f$$ pointwise. But $$\sup_n \lvert f_k(n) - f(n)\rvert = 1$$ for every
$$k$$ (take $$n = k$$), so the convergence is not uniform.

> **Exercise 3.** Give an example of a sequence of continuous functions
> $$f_1, f_2, \dots$$ from $$[0, 1]$$ to $$\mathbb{R}$$ that converges pointwise
> to a function $$f : [0, 1] \to \mathbb{R}$$ that is not a bounded function.
{: .problem #ex-2e-3 }

*Solution.* Take

$$
f_n(x) = \frac{n^2 x}{n^2 x^2 + 1}.
$$

Each $$f_n$$ is continuous on $$[0, 1]$$. For $$x > 0$$,
$$f_n(x) \to \dfrac{1}{x}$$ as $$n \to \infty$$, and $$f_n(0) = 0$$ for all
$$n$$. Thus $$f_n \to f$$ pointwise, where $$f(0) = 0$$ and $$f(x) = \frac{1}{x}$$
for $$x \in (0, 1]$$, which is not bounded.

> **Exercise 4.** Prove or give a counterexample: If $$A \subseteq \mathbb{R}$$
> and $$f_1, f_2, \dots$$ is a sequence of uniformly continuous functions from
> $$A$$ to $$\mathbb{R}$$ that converges uniformly to a function
> $$f : A \to \mathbb{R}$$, then $$f$$ is uniformly continuous on $$A$$.
{: .problem #ex-2e-4 }

*Solution.* It is true. We have to prove that $$f$$ is uniformly continuous:
$$\forall \varepsilon > 0$$, $$\exists \delta > 0$$ s.t.
$$\lvert f(x) - f(y)\rvert < \varepsilon$$ for all $$x, y \in A$$ with
$$\lvert x - y\rvert < \delta$$.

Also, since $$f_1, f_2, \dots$$ uniformly converges to $$f$$, $$f$$ is
continuous on $$A$$. Let $$\varepsilon > 0$$. By uniform convergence, pick
$$N \in \mathbb{Z}^+$$ with $$\lvert f_N(x) - f(x)\rvert < \frac{\varepsilon}{3}$$
for all $$x \in A$$. Then, as $$f_N$$ is uniformly continuous, pick
$$\delta > 0$$ with $$\lvert f_N(x) - f_N(y)\rvert < \frac{\varepsilon}{3}$$
whenever $$x, y \in A$$ and $$\lvert x - y\rvert < \delta$$.

$$\therefore$$ For any $$\lvert x - y\rvert < \delta$$ with $$x, y \in A$$,

$$
\lvert f(x) - f(y)\rvert \le \lvert f(x) - f_N(x)\rvert + \lvert f_N(x) -
f_N(y)\rvert + \lvert f_N(y) - f(y)\rvert < \varepsilon,
$$

meaning that $$f$$ is uniformly continuous on $$A$$.

> **Exercise 6.** Suppose $$(X, \mathcal{S}, \mu)$$ is a measure space with
> $$\mu(X) < \infty$$. Suppose $$f_1, f_2, \dots$$ is a sequence of
> $$\mathcal{S}$$-measurable functions from $$X$$ to $$\mathbb{R}$$ such that
> $$\lim_{k \to \infty} f_k(x) = \infty$$ for each $$x \in X$$. Prove that for
> every $$\varepsilon > 0$$, there exists a set $$E \in \mathcal{S}$$ such that
> $$\mu(X \setminus E) < \varepsilon$$ and $$f_1, f_2, \dots$$ converges
> uniformly to $$\infty$$ on $$E$$ (meaning that for every $$t > 0$$, there
> exists $$n \in \mathbb{Z}^+$$ such that $$f_k(x) > t$$ for all integers
> $$k \ge n$$ and all $$x \in E$$).
{: .problem #ex-2e-6 }

*Solution.* Temporarily fix $$\varepsilon > 0$$. For $$m, n \in \mathbb{Z}^+$$,
let

$$
A_{m,n} = \bigcap_{k=m}^{\infty} \{x \in X : f_k(x) > n\}.
$$

By definition of pointwise convergence to $$\infty$$,
$$X = \bigcup_{m=1}^{\infty} A_{m,n}$$ for each $$n$$. Since each $$f_k$$ is
$$\mathcal{S}$$-measurable, each $$A_{m,n} \in \mathcal{S}$$. Now,
$$A_{1,n} \subseteq A_{2,n} \subseteq \cdots$$ and
$$X = \bigcup_{m=1}^{\infty} A_{m,n}$$, thus implying
$$\lim_{m \to \infty} \mu(A_{m,n}) = \mu(X)$$.

Thus, there exists $$m_n \in \mathbb{Z}^+$$ s.t.
$$\mu(X) - \mu(A_{m_n,n}) < \dfrac{\varepsilon}{2^n}$$ ($$\mu(X) < \infty$$), that
is, $$\mu(X \setminus A_{m_n,n}) < \dfrac{\varepsilon}{2^n}$$. Let
$$E = \bigcap_n A_{m_n,n} \in \mathcal{S}$$. Then, as
$$X \setminus E = \bigcup_n (X \setminus A_{m_n,n})$$,
$$\mu(X \setminus E) \le \sum_n \mu(X \setminus A_{m_n,n}) < \varepsilon$$.

To do this, suppose $$t > 0$$. Let $$n \in \mathbb{Z}^+$$ s.t. $$n > t$$. Then
$$E \subseteq A_{m_n,n}$$, which implies that $$f_k(x) > n > t$$ for all
$$k \ge m_n$$ and all $$x \in E$$. Hence, $$f_1, f_2, \dots$$ converges
uniformly to $$\infty$$ on $$E$$.

> **Exercise 7.** Suppose $$F$$ is a closed bounded subset of $$\mathbb{R}$$ and
> $$g_1, g_2, \dots$$ is an increasing sequence of continuous real-valued
> functions on $$F$$ (thus $$g_1(x) \le g_2(x) \le \cdots$$ for all
> $$x \in F$$) such that $$\sup\{g_1(x), g_2(x), \dots\} < \infty$$ for each
> $$x \in F$$. Define a real-valued function $$g$$ on $$F$$ by
> $$g(x) = \lim_{k \to \infty} g_k(x)$$. Prove that $$g$$ is continuous on $$F$$
> if and only if $$g_1, g_2, \dots$$ converges uniformly on $$F$$ to $$g$$.
> [The result above is called Dini's Theorem.]
{: .problem #ex-2e-7 }

*Solution.* ① ($$\Leftarrow$$) If $$g_1, g_2, \dots$$ converges uniformly on
$$F$$ to $$g$$, it is obvious that $$g$$ is continuous on $$F$$ (uniform limit of
continuous functions).

② ($$\Rightarrow$$) If $$g$$ is continuous on $$F$$, set
$$f_n = g - g_n$$. Here, we see that each $$f_n$$ is continuous,
$$f_n \ge f_{n+1} \ge 0$$, and $$f_n(x) \xrightarrow{n \to \infty} 0$$
$$\forall x \in F$$. Now, proving uniform convergence of $$g_n$$ on $$F$$ to $$g$$
requires $$\sup_F f_n \xrightarrow{n \to \infty} 0$$.

Fix $$\varepsilon > 0$$ and let $$K_n = \{x \in F : f_n(x) \ge \varepsilon\}$$.
Then, $$K_n$$ is the preimage of $$[\varepsilon, \infty)$$ under the continuous
$$f_n$$, so it is closed in $$F$$, and thus $$K_n$$ is closed (as $$F$$ is
closed), hence compact ($$F$$ is bounded). Also, if $$x \in K_{n+1}$$, then
$$f_n(x) \ge f_{n+1}(x) \ge \varepsilon$$, and thus $$x \in K_n$$, meaning that
$$K_1 \supseteq K_2 \supseteq \cdots$$.

$$\forall x \in F$$, we have $$\lim f_n(x) = 0$$, so there exists $$N \in
\mathbb{Z}^+$$ with $$f_N(x) < \varepsilon$$. Thus, $$x \notin \bigcap_n K_n$$.
Here, since for all $$n \in \mathbb{Z}^+$$, $$K_n \subseteq F$$, we get
$$\bigcap_n K_n = \emptyset$$.

$$\therefore$$ A nested sequence of nonempty compact sets must have nonempty
intersection, and thus $$\exists N \in \mathbb{Z}^+$$ s.t. $$K_N = \emptyset$$.
$$\therefore\ \forall x \in F$$, $$f_N(x) < \varepsilon$$,
meaning that $$0 \le f_n(x) \le f_N(x) < \varepsilon$$ for all $$x \in F$$ and
all $$n \ge N$$. Therefore, $$f_n$$ converges uniformly to $$0$$, meaning
$$g_n$$ converges uniformly to $$g$$ on $$F$$.

> **Exercise 8.** Suppose $$\mu$$ is the measure on $$(\mathbb{Z}^+,
> 2^{\mathbb{Z}^+})$$ defined by $$\mu(E) = \sum_{n \in E} \dfrac{1}{2^n}$$.
> Prove that for every $$\varepsilon > 0$$, there exists a set
> $$E \subseteq \mathbb{Z}^+$$ with $$\mu(\mathbb{Z}^+ \setminus E) <
> \varepsilon$$ such that $$f_1, f_2, \dots$$ converges uniformly on $$E$$ for
> every sequence of functions $$f_1, f_2, \dots$$ from $$\mathbb{Z}^+$$ to
> $$\mathbb{R}$$ that converges pointwise on $$\mathbb{Z}^+$$.
{: .problem #ex-2e-8 }

*Solution.* Fix $$\varepsilon > 0$$. We know that a sequence of functions from
$$X$$ to $$\mathbb{R}$$ that converges pointwise on $$X$$ also converges
uniformly on $$X$$ if $$X$$ is finite (Exercise 1).

Let $$M$$ be the positive integer s.t.
$$\sum_{k=M+1}^{\infty} \dfrac{1}{2^k} = \dfrac{1}{2^M} < \varepsilon$$. Define
$$E = \{1, 2, \dots, M\}$$. Then $$E \subseteq \mathbb{Z}^+$$,
$$\mu(\mathbb{Z}^+ \setminus E) < \varepsilon$$, and $$E$$ is finite, meaning
that every sequence of functions $$f_1, f_2, \dots$$ from $$\mathbb{Z}^+$$ to
$$\mathbb{R}$$ that converges pointwise on $$\mathbb{Z}^+$$ converges uniformly
on $$E$$.

> **Exercise 9.** Suppose $$F_1, \dots, F_n$$ are disjoint closed subsets of
> $$\mathbb{R}$$. Prove that if $$g : F_1 \cup \cdots \cup F_n \to \mathbb{R}$$
> is a function such that $$g\vert_{F_k}$$ is a continuous function for each
> $$k \in \{1, \dots, n\}$$, then $$g$$ is a continuous function.
{: .problem #ex-2e-9 }

*Solution.* Trivial. (A point $$x \in F_k$$ has a neighborhood disjoint from the
finitely many closed sets $$F_j$$, $$j \ne k$$, so near $$x$$ the function $$g$$
agrees with the continuous $$g\vert_{F_k}$$.)

> **Exercise 10.** Suppose $$F \subseteq \mathbb{R}$$ is such that every
> continuous function from $$F$$ to $$\mathbb{R}$$ can be extended to a
> continuous function from $$\mathbb{R}$$ to $$\mathbb{R}$$. Prove that $$F$$
> is a closed subset of $$\mathbb{R}$$.
{: .problem #ex-2e-10 }

*Solution.* Assume that $$F$$ is not closed. Then, there exists a sequence
$$a_n \in F$$ that converges to some $$\alpha \notin F$$. Let
$$f(x) = \dfrac{1}{\lvert x - \alpha\rvert}$$ for $$x \in F$$ (a continuous
function on $$F$$ as $$\alpha \notin F$$). Extend $$f$$ to a continuous function
$$\tilde{f}$$ on $$\mathbb{R}$$. Then,

$$
\tilde{f}(\alpha) = \lim_{n \to \infty} \tilde{f}(a_n) = \lim_{n \to \infty}
f(a_n) = \lim_{n \to \infty} \frac{1}{\lvert a_n - \alpha\rvert} = \infty,
$$

which is impossible, as $$\tilde{f}(\alpha)$$ is a real number.

> **Exercise 14.** Suppose $$b_1, b_2, \dots$$ is a sequence of real numbers.
> Define $$f : \mathbb{R} \to [0, \infty]$$ by
>
> $$
> f(x) =
> \begin{cases}
> \displaystyle\sum_{k=1}^{\infty} \frac{1}{4^k\lvert x - b_k\rvert} & \text{if }
> x \notin \{b_1, b_2, \dots\}, \\
> \infty & \text{if } x \in \{b_1, b_2, \dots\}.
> \end{cases}
> $$
>
> Prove that $$\lvert \{x \in \mathbb{R} : f(x) < 1\}\rvert = \infty$$.
{: .problem #ex-2e-14 }

*Solution.* Consider the set
$$A = \bigcup_k \Bigl[ b_k - \dfrac{1}{2^k},\ b_k + \dfrac{1}{2^k} \Bigr]$$.
Then, $$\forall x \in \mathbb{R} \setminus A$$,

$$
f(x) < \sum_{k=1}^{\infty} \frac{1}{4^k}\cdot 2^k = \sum_{k=1}^{\infty}
\frac{1}{2^k} = 1,
$$

since $$\lvert x - b_k\rvert > \frac{1}{2^k}$$ for every $$k$$ (so $$x \notin
\{b_1, b_2, \dots\}$$ too). Also,
$$\lvert A\rvert \le \sum_k \dfrac{2}{2^k} = 2$$, meaning
$$\lvert \mathbb{R} \setminus A\rvert = \infty$$. Hence
$$\{x \in \mathbb{R} : f(x) < 1\} \supseteq \mathbb{R} \setminus A$$ and its
outer measure is $$\infty$$.

> **Exercise 15.** Suppose $$B$$ is a Borel set and $$f : B \to \mathbb{R}$$ is
> a Lebesgue measurable function. Show that there exists a Borel measurable
> function $$g : B \to \mathbb{R}$$ such that
> $$\lvert \{x \in B : g(x) \ne f(x)\}\rvert = 0$$.
{: .problem #ex-2e-15 }

*Solution.* Define $$\tilde{f} : \mathbb{R} \to \mathbb{R}$$ by

$$
\tilde{f}(x) =
\begin{cases}
f(x) & x \in B, \\
0 & x \notin B.
\end{cases}
$$

Then for every Borel set $$A \subseteq \mathbb{R}$$,
$$\tilde{f}^{-1}(A) = f^{-1}(A)$$ if $$0 \notin A$$ and
$$\tilde{f}^{-1}(A) = f^{-1}(A) \cup (\mathbb{R} \setminus B)$$ if $$0 \in A$$,
meaning that $$\tilde{f}$$ is a Lebesgue measurable function ($$B$$ is Borel, so
$$\mathbb{R} \setminus B$$ is Lebesgue measurable).

Thus, by the theorem above (every Lebesgue measurable function is almost Borel
measurable), there exists a Borel measurable $$\tilde{g} : \mathbb{R} \to
\mathbb{R}$$ s.t. $$\lvert \{x \in \mathbb{R} : \tilde{g}(x) \ne
\tilde{f}(x)\}\rvert = 0$$. Take $$g = \tilde{g}\vert_B$$. Then, $$g$$ is Borel
measurable and $$\{x \in B : g(x) \ne f(x)\} \subseteq \{x \in \mathbb{R} :
\tilde{g}(x) \ne \tilde{f}(x)\}$$, so
$$\lvert \{x \in B : g(x) \ne f(x)\}\rvert = 0$$.

## References

- Sheldon Axler, *Measure, Integration & Real Analysis* — Section 2E and
  Exercises 2E. The exercise statements are quoted from the book.
- The notes and the exercise answers are mine, typeset from my handwritten
  notebook. The structure of each answer is unchanged; small slips in the
  answers are corrected, and answers that stopped short are completed along
  the same lines. I did not attempt Exercises 5, 11, 12 and 13, so they are not
  here.
