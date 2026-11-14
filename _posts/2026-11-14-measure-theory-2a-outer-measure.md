---
title: "Measure Theory and Real Analysis: 2A Outer Measure on R"
date: 2026-11-14 13:30:00 +0900
categories: [Study Notes, Measure Theory and Real Analysis]
tags: [outer measure, countable subadditivity, heine-borel, nonadditivity, exercises]
description: Length of an open interval, outer measure, countable sets, translation invariance, countable subadditivity, the Heine-Borel theorem, the outer measure of a closed interval, and the nonadditivity of outer measure, with worked exercises 1, 2, 3, 5, 6, 7, 12 and 13. Section 2A of Axler's Measure, Integration & Real Analysis.
math: true
mermaid: false
render_with_liquid: false
---

> Typeset from my handwritten notes for Chapter 2 and section 2A of Axler's
> *Measure, Integration & Real Analysis*. The exercise statements are the
> textbook's; the answers are mine, as I wrote them. Part of the [course
> overview](/posts/measure-theory-overview/).
{: .prompt-info }

## Notes

### Motivation

$$\hookrightarrow$$ How do we assign a size to a union of subsets (in
$$\mathbb{R}$$) that can be the domain of a function?

E.g. we expect the size of the set $$(1,3) \cup (7,10)$$ to be $$5$$.

> **Definition (Length of an open interval).** The length $$\ell(I)$$ of an
> open interval $$I$$ is defined by
>
> $$
> \ell(I) =
> \begin{cases}
> b - a & \text{if } I = (a,b) \text{ for some } a, b \in \mathbb{R}
>   \text{ with } a < b, \\
> 0 & \text{if } I = \emptyset, \\
> \infty & \text{if } I = (-\infty, a) \text{ or } I = (a, \infty)
>   \text{ for some } a \in \mathbb{R}, \\
> \infty & \text{if } I = (-\infty, \infty).
> \end{cases}
> $$
{: .definition #def-length }

> **Definition (Outer measure; $$\lvert A\rvert$$).** The outer measure $$\lvert A\rvert$$ of a set
> $$A \subseteq \mathbb{R}$$ is defined by
>
> $$
> |A| = \inf \Bigl\{ \sum_{k=1}^{\infty} \ell(I_k) :
> I_1, I_2, \dots \text{ are open intervals such that }
> A \subseteq \bigcup_{k=1}^{\infty} I_k \Bigr\}.
> $$
{: .definition #def-outer-measure }

**Example.** Suppose $$A = \{a_1, a_2, \dots, a_n\}$$ where
$$a_k \in \mathbb{R}$$ for all $$k = 1, \dots, n$$. Let $$\varepsilon > 0$$.
Define a sequence $$I_1, \dots, I_k, \dots$$ of open intervals by

$$
I_k =
\begin{cases}
(a_k - \varepsilon,\, a_k + \varepsilon) & \text{if } k \le n, \\
\emptyset & \text{if } k > n.
\end{cases}
$$

$$\therefore\ A \subseteq \bigcup_{k=1}^{\infty} I_k$$ and
$$\sum \ell(I_k) = 2\varepsilon n$$.

$$\lvert A\rvert \le 2\varepsilon n$$. $$\varepsilon \to 0$$ $$\therefore\ \lvert A\rvert = 0$$.

> **Theorem (Countable sets have outer measure 0).** Every countable subset of
> $$\mathbb{R}$$ has outer measure $$0$$.
{: .theorem #thm-countable }

*Proof.* Suppose $$A = \{a_1, a_2, \dots\}$$ is a countable subset of
$$\mathbb{R}$$ and $$\varepsilon > 0$$.

For $$k \in \mathbb{Z}^+$$, define
$$I_k = \bigl( a_k - \frac{1}{2^k}\varepsilon,\ a_k + \frac{1}{2^k}\varepsilon \bigr)$$.
Then $$I_1, I_2, \dots$$ is a sequence of open intervals whose union contains
$$A$$.

Thus,

$$
|A| \le \sum_{k=1}^{\infty} \ell(I_k)
= \varepsilon \sum_{k=1}^{\infty} \frac{1}{2^{k-1}} = 2\varepsilon \to 0.
$$

$$\therefore\ \lvert A\rvert = 0$$.

$$\hookrightarrow$$ $$\lvert \mathbb{Q}\rvert = 0$$. $$\square$$

> **Theorem (Outer measure preserves order).** Suppose $$A$$ and $$B$$ are
> subsets of $$\mathbb{R}$$ with $$A \subseteq B$$. Then $$\lvert A\rvert \le \lvert B\rvert$$.
{: .theorem #thm-order }

*Proof.* Suppose $$I_1, I_2, \dots$$ is a sequence of open intervals with
$$B \subseteq \bigcup I_k$$. Then $$A \subseteq B \subseteq \bigcup I_k$$.

$$\therefore\ \lvert A\rvert \le \sum \ell(I_k)$$.

$$\therefore\ \lvert A\rvert \le \inf\{\sum \ell(I_k)\} = \lvert B\rvert$$. $$\square$$

> **Definition (Translation; $$t + A$$).** If $$t \in \mathbb{R}$$ and
> $$A \subseteq \mathbb{R}$$, the translation $$t + A$$ is defined by
>
> $$
> t + A = \{t + a : a \in A\}.
> $$
{: .definition #def-translation }

> **Theorem (Outer measure is translation invariant).** Suppose
> $$t \in \mathbb{R}$$ and $$A \subseteq \mathbb{R}$$. Then
> $$\lvert t + A\rvert = \lvert A\rvert$$.
{: .theorem #thm-translation }

*Proof.* Suppose $$I_1, I_2, \dots$$ is a sequence of open intervals whose
union contains $$A$$. Then $$t + I_1, t + I_2, \dots$$ is a sequence whose
union contains $$t + A$$.

① $$\lvert t + A\rvert \le \sum \ell(t + I_k) = \sum \ell(I_k)$$.

$$\therefore\ \lvert t + A\rvert \le \inf \sum \ell(I_k) = \lvert A\rvert$$.

② Consider $$A = -t + (t + A)$$.

$$\therefore\ \lvert A\rvert = \lvert (-t) + (t + A)\rvert \le \lvert t + A\rvert$$ by ①.

$$\therefore\ \lvert A\rvert = \lvert t + A\rvert$$. $$\square$$

> **Theorem (Countable subadditivity of outer measure).** Suppose
> $$A_1, A_2, \dots$$ is a sequence of subsets of $$\mathbb{R}$$. Then
>
> $$
> \Bigl| \bigcup_{k=1}^{\infty} A_k \Bigr| \le \sum_{k=1}^{\infty} |A_k|.
> $$
{: .theorem #thm-subadditivity }

*Proof.* If $$\lvert A_k\rvert = +\infty$$ for some $$k \in \mathbb{Z}^+$$, then the
inequality definitely holds. Thus, assume $$\lvert A_k\rvert < \infty$$ for all
$$k \in \mathbb{Z}^+$$.

Let $$\varepsilon > 0$$. For each $$k \in \mathbb{Z}^+$$, let
$$I_{1,k}, I_{2,k}, \dots$$ be a sequence of open intervals whose union
contains $$A_k$$ such that

$$
\sum_{j=1}^{\infty} \ell(I_{j,k}) \le \frac{1}{2^k}\varepsilon + |A_k|.
$$

$$
\therefore\ \sum_{k=1}^{\infty} \sum_{j=1}^{\infty} \ell(I_{j,k})
\le \varepsilon + \sum_{k=1}^{\infty} |A_k|.
$$

Now,

$$
\sum_{k=1}^{\infty} \sum_{j=1}^{\infty} \ell(I_{j,k})
= \sum_{n=2}^{\infty} \sum_{k=1}^{n-1} \ell(I_{k,n-k}).
$$

$$\hookrightarrow$$ finite series of sequences. (more treated as a sequence
itself.)

$$
\therefore\ \Bigl| \bigcup_{k=1}^{\infty} A_k \Bigr|
\le \sum_{n=2}^{\infty} \Bigl( \sum_{k=1}^{n-1} \ell(I_{k,n-k}) \Bigr)
\le \varepsilon + \sum_{k=1}^{\infty} |A_k|.
$$

$$\varepsilon \to 0$$;
$$\displaystyle \Bigl\lvert \bigcup_{k=1}^{\infty} A_k \Bigr\rvert \le \sum_{k=1}^{\infty} \lvert A_k\rvert$$.
$$\square$$

Also, countable subadditivity implies finite subadditivity.

Now, here we prove the outer measure of closed bounded intervals. First,
let's define the "open cover" and "finite subcover".

> **Definition (Open cover).** Suppose $$A \subseteq \mathbb{R}$$. A collection
> $$\mathcal{C}$$ of open subsets of $$\mathbb{R}$$ is called an open cover of
> $$A$$ if $$A$$ is contained in the union of all the sets in
> $$\mathcal{C}$$.
{: .definition #def-open-cover }

> **Definition (Finite subcover).** An open cover $$\mathcal{C}$$ of $$A$$ is
> said to have a finite subcover if $$A$$ is contained in the union of some
> finite list of sets in $$\mathcal{C}$$.
{: .definition #def-finite-subcover }

> **Theorem (Heine–Borel Theorem) ★.** Every open cover of a closed bounded
> subset of $$\mathbb{R}$$ has a finite subcover.
{: .theorem #thm-heine-borel }

*Proof.* Suppose $$F$$ is a closed bounded subset of $$\mathbb{R}$$ and
$$\mathcal{C}$$ is an open cover of $$F$$.

First, consider the case where $$F = [a,b]$$ for some $$a, b \in \mathbb{R}$$
with $$a < b$$.

Let $$D = \{d \in [a,b] : [a,d] \text{ has a finite subcover from }
\mathcal{C}\}$$.

Note that $$a \in D$$ (because $$a$$ should be in $$G$$ for some
$$G \in \mathcal{C}$$) $$\Rightarrow$$ $$D$$ is not empty.

Now, let $$s = \sup D$$.

Thus, $$s \in [a,b]$$. Hence there exists an open set $$G \in \mathcal{C}$$
such that $$s \in G$$. Let $$\delta > 0$$ be such that
$$(s - \delta, s + \delta) \subseteq G$$.

Because $$s = \sup D$$, there exist $$d \in (s - \delta, s]$$ and
$$n \in \mathbb{Z}^+$$ and $$G_1, \dots, G_n \in \mathcal{C}$$ such that

$$
[a,d] \subseteq \bigcup_{k=1}^{n} G_k \quad \leftarrow \text{ finite subcover.}
$$

Now $$[a,d'] \subseteq G \cup G_1 \cup \cdots \cup G_n$$ for all
$$d' \in [s, s + \delta)$$.

Thus $$d' \in D$$ for all $$d' \in [s, s + \delta) \cap [a,b]$$.
$$\Rightarrow$$ $$s = b$$.

Furthermore, setting $$d' = b$$,
$$[a,b] \subseteq G \cup G_1 \cup \cdots \cup G_n$$, having a finite subcover
from $$\mathcal{C}$$. Completing the proof in the case where $$F = [a,b]$$.

Now, suppose that $$F$$ is an arbitrary closed bounded subset of
$$\mathbb{R}$$ and that $$\mathcal{C}$$ is an open cover of $$F$$.

Let $$a, b \in \mathbb{R}$$ be such that $$F \subseteq [a,b]$$.

Note that $$\mathcal{C} \cup \{\mathbb{R} \setminus F\}$$ is an open cover of
$$\mathbb{R}$$ and hence is an open cover of $$[a,b]$$.

$$\therefore\ [a,b] \subseteq G_1 \cup G_2 \cup \cdots \cup G_n \cup
(\mathbb{R} \setminus F)$$ (by the first half of the proof).

$$\therefore\ F \subseteq G_1 \cup G_2 \cup \cdots \cup G_n$$
($$\because$$ $$F \subseteq [a,b]$$, $$F \cap (\mathbb{R} \setminus F) =
\emptyset$$). $$\square$$

> **Theorem (Outer measure of a closed interval).** Suppose
> $$a, b \in \mathbb{R}$$ with $$a < b$$. Then $$\lvert [a,b]\rvert = b - a$$.
{: .theorem #thm-closed-interval }

*Proof.* ① If $$\varepsilon > 0$$, then $$(a - \varepsilon, b + \varepsilon),
\emptyset, \emptyset, \dots$$ is a sequence of open intervals whose union
contains $$[a,b]$$.

$$\therefore\ \lvert [a,b]\rvert \le b - a + 2\varepsilon$$. $$\Rightarrow$$
$$\varepsilon \to 0$$; $$\lvert [a,b]\rvert \le b - a$$.

② Suppose $$I_1, I_2, \dots$$ is a sequence of open intervals such that
$$[a,b] \subseteq \bigcup_{k=1}^{\infty} I_k$$.

By the Heine–Borel theorem, $$\exists n \in \mathbb{Z}^+$$ such that
$$[a,b] \subseteq \bigcup_{k=1}^{n} I_k$$.

\* Statement: $$\displaystyle \sum_{k=1}^{n} \ell(I_k) \ge b - a$$ for all
$$n \in \mathbb{Z}^+$$.

(i) If $$n = 1$$, $$[a,b] \subseteq I_1$$. $$\therefore\ \ell(I_1) \ge b - a$$
clearly follows.

(ii) Suppose that for some $$n \in \mathbb{Z}^+$$, if
$$[a,b] \subseteq \bigcup_{k=1}^{n} I_k$$ holds, then
$$\sum_{k=1}^{n} \ell(I_k) \ge b - a$$ (for all choices).

Now, suppose an open interval $$I_{n+1}$$.

Clearly, $$[a,b] \subseteq I_1 \cup \cdots \cup I_n \cup I_{n+1}$$.

Thus, $$b$$ is in at least one of the intervals
$$I_1, \dots, I_n, I_{n+1}$$.

By relabeling, we can assume that $$b \in I_{n+1}$$. Suppose
$$I_{n+1} = (c,d)$$.

- If $$c \le a$$, then $$\ell(I_{n+1}) \ge b - a$$.
- Otherwise, $$a < c < b < d$$.

Hence, $$[a,c] \subseteq I_1 \cup \cdots \cup I_n$$ as
$$[a,b] \subseteq I_1 \cup \cdots \cup I_n \cup I_{n+1}$$.

$$\therefore$$ By the first statement,
$$\sum_{k=1}^{n} \ell(I_k) \ge c - a$$ and $$\ell(I_{n+1}) \ge b - c$$.

$$
\therefore\ \sum_{k=1}^{n+1} \ell(I_k) \ge (c - a) + (b - c) = b - a.
$$

$$
\therefore\ \sum_{k=1}^{\infty} \ell(I_k) \ge \sum_{k=1}^{n} \ell(I_k)
\ge b - a.
$$

$$
\therefore\ \inf \sum_{k=1}^{\infty} \ell(I_n) = |[a,b]| \ge b - a.
$$

$$\therefore\ \lvert [a,b]\rvert = b - a$$. $$\square$$

> **Corollary (Nontrivial intervals are uncountable).** Every interval in
> $$\mathbb{R}$$ that contains at least two distinct elements is uncountable.
{: .theorem #cor-uncountable }

*Proof.* Suppose $$I$$ is an interval that contains $$a, b \in \mathbb{R}$$
with $$a < b$$.

$$\Rightarrow$$ $$\lvert I\rvert \ge \lvert [a,b]\rvert = b - a > 0$$.

Then, since every countable subset of $$\mathbb{R}$$ has outer measure $$0$$,
we can conclude that $$I$$ is uncountable. $$\square$$

> **Theorem (Nonadditivity of outer measure).** There exist disjoint subsets
> $$A$$ and $$B$$ of $$\mathbb{R}$$ such that
>
> $$
> |A \cup B| \ne |A| + |B|.
> $$
{: .theorem #thm-nonadditivity }

$$\rightarrow$$ Sad property.

*Proof.* For $$a \in [-1,1]$$, let $$\tilde{a}$$ be the set of numbers in
$$[-1,1]$$ that differ from $$a$$ by a rational number.

($$\Leftrightarrow$$ $$\tilde{a} = \{c \in [-1,1] : a - c \in \mathbb{Q}\}$$.)

Now, if $$a, b \in [-1,1]$$ and $$\tilde{a} \cap \tilde{b} \ne \emptyset$$,
then $$\tilde{a} = \tilde{b}$$ $$\cdots (*)$$.

> $$(*)$$ Proof: Suppose $$\exists d \in \tilde{a} \cap \tilde{b}$$. Then,
> $$a - d \in \mathbb{Q}$$ and $$b - d \in \mathbb{Q}$$.
>
> $$\therefore\ a - b \in \mathbb{Q}$$.
>
> $$\therefore$$ From $$a - c = (a - b) + (b - c)$$, if
> $$c \in [-1,1]$$, then $$a - c \in \mathbb{Q} \Leftrightarrow
> b - c \in \mathbb{Q}$$.
>
> $$\therefore\ \tilde{a} = \tilde{b}$$.

Clearly, $$a \in \tilde{a}$$ for all $$a \in [-1,1]$$ $$\Rightarrow$$
$$[-1,1] = \displaystyle \bigcup_{a \in [-1,1]} \tilde{a}$$.

(Let $$V$$ be a set that contains exactly one element in each of the
distinct sets in $$\{\tilde{a} : a \in [-1,1]\}$$.

$$\rightarrow$$ This step involves the Axiom of Choice. $$=$$ The set $$V$$
arises by choosing one element from each equivalence class.)

Let $$r_1, r_2, \dots$$ be a sequence of distinct rational numbers such that
$$[-2,2] \cap \mathbb{Q} = \{r_1, r_2, \dots\}$$.

Then, if $$a \in [-1,1]$$, letting $$v$$ be the unique element of
$$V \cap \tilde{a}$$, we have $$a - v \in \mathbb{Q}$$, which implies that
$$a = r_k + v \in r_k + V$$ for some $$k \in \mathbb{Z}^+$$.

Thus, $$[-1,1] \subseteq \bigcup_{k=1}^{\infty} (r_k + V)$$.

$$
|[-1,1]| \le \Bigl| \bigcup_{k=1}^{\infty} (r_k + V) \Bigr|
\le \sum_{k=1}^{\infty} |r_k + V|.
$$

$$\therefore\ \sum_{k=1}^{\infty} \lvert V\rvert \ge 2$$, and thus $$\lvert V\rvert > 0$$.

Note that the sets $$r_1 + V, r_2 + V, \dots$$ are disjoint. $$\cdots (**)$$

> $$(**)$$ Proof: Assume that $$\exists t \in (r_j + V) \cap (r_k + V)$$.
> Then, $$t = r_j + v_1 = r_k + v_2$$ for some $$v_1, v_2 \in V$$, which
> implies that $$v_1 - v_2 = r_k - r_j \in \mathbb{Q}$$.
>
> Then, since $$V \cap \tilde{a}$$ has exactly one element, $$v_1 = v_2$$.
>
> $$\therefore\ r_j = r_k \Rightarrow j = k$$.

Let $$n \in \mathbb{Z}^+$$. Clearly $$\bigcup_{k=1}^{n} (r_k + V)
\subseteq [-3,3]$$ because $$V \subseteq [-1,1]$$ and each
$$r_k \in [-2,2]$$.

$$\therefore\ \Bigl\lvert \bigcup_{k=1}^{n} (r_k + V) \Bigr\rvert \le 6$$.

However, $$\displaystyle \sum_{k=1}^{n} \lvert r_k + V\rvert =
\sum_{k=1}^{n} \lvert V\rvert = n\lvert V\rvert$$.

Then, since $$\lvert V\rvert > 0$$, we can choose $$n \in \mathbb{Z}^+$$ such that
$$n\lvert V\rvert > 6$$.

Thus,

$$
\Bigl| \bigcup_{k=1}^{n} (r_k + V) \Bigr| < \sum_{k=1}^{n} |r_k + V|.
\ \square
$$

$$\hookrightarrow$$ If $$A_1, A_2, \dots$$ are disjoint, we expect
$$\bigl\lvert \bigcup_{k=1}^{n} A_k \bigr\rvert = \sum_{k=1}^{n} \lvert A_k\rvert$$.

But the result above suggests that there exist disjoint subsets with
$$\bigl\lvert \bigcup_{k=1}^{n} A_k \bigr\rvert \ne \sum_{k=1}^{n} \lvert A_k\rvert$$.

## Exercises 2A

> **Exercise 1.** Prove that if $$A$$ and $$B$$ are subsets of $$\mathbb{R}$$
> and $$\lvert B\rvert = 0$$, then $$\lvert A \cup B\rvert = \lvert A\rvert$$.
{: .problem #ex-2a-1 }

*Solution.* If $$A$$ and $$B$$ are subsets of $$\mathbb{R}$$ and
$$\lvert B\rvert = 0$$, by the countable subadditivity of outer measure,

$$
|A \cup B| \le |A| + |B| = |A|.
$$

Also, since $$A \subseteq A \cup B$$, $$\lvert A\rvert \le \lvert A \cup B\rvert$$.

$$\therefore\ \lvert A \cup B\rvert = \lvert A\rvert$$.

> **Exercise 2.** Suppose $$A \subseteq \mathbb{R}$$ and $$t \in \mathbb{R}$$.
> Let $$tA = \{ta : a \in A\}$$. Prove that $$\lvert tA\rvert = \lvert t\rvert \,\lvert A\rvert$$.
>
> [Assume that $$0 \cdot \infty$$ is defined to be $$0$$.]
{: .problem #ex-2a-2 }

*Solution.* Suppose $$A \subseteq \mathbb{R}$$ and $$t \in \mathbb{R}$$. Let
$$tA = \{ta : a \in A\}$$.

Then, every open interval cover $$I_1, I_2, \dots$$ has a one-to-one
correspondence to $$tI_1, tI_2, \dots$$.

$$
\therefore\ \sum_{k=1}^{\infty} \ell(tI_k)
= |t| \sum_{k=1}^{\infty} \ell(I_k).
$$

$$\therefore\ \lvert tA\rvert = \lvert t\rvert \,\lvert A\rvert$$.

> **Exercise 3.** Prove that if $$A, B \subseteq \mathbb{R}$$ and
> $$\lvert A\rvert < \infty$$, then $$\lvert B \setminus A\rvert \ge \lvert B\rvert - \lvert A\rvert$$.
{: .problem #ex-2a-3 }

*Solution.* If $$A, B \subseteq \mathbb{R}$$ and $$\lvert A\rvert < \infty$$, as
$$A \cup (B \cap A^c) = B$$,

$$
|A \cup (B \cap A^c)| = |B| \le |A| + |B \cap A^c|
\quad \text{(countable subadditivity)},
$$

$$\therefore\ \lvert B \setminus A\rvert \ge \lvert B\rvert - \lvert A\rvert$$.

> **Exercise 5.** Suppose $$\mathcal{A}$$ is a set of closed subsets of
> $$\mathbb{R}$$ such that $$\bigcap_{F \in \mathcal{A}} F = \emptyset$$. Prove
> that if $$\mathcal{A}$$ contains at least one bounded set, then there exist
> $$n \in \mathbb{Z}^+$$ and $$F_1, \dots, F_n \in \mathcal{A}$$ such that
> $$F_1 \cap \cdots \cap F_n = \emptyset$$.
{: .problem #ex-2a-5 }

*Solution.* $$\mathcal{A}$$ is a set of closed subsets of $$\mathbb{R}$$ such
that $$\bigcap_{F \in \mathcal{A}} F = \emptyset$$.

If $$\mathcal{A}$$ contains at least one bounded set, define $$\mathcal{A}'$$
the set of closed and bounded sets in $$\mathcal{A}$$. Choose (by random) one
set $$B$$ in $$\mathcal{A}'$$. (Axiom of Choice)

Then, since

$$
\bigcap_{F \in \mathcal{A}} F
= \Bigl( \bigcap_{F \in \mathcal{A} \setminus \{B\}} F \Bigr) \cap B
= \emptyset,
$$

$$
B \subseteq \mathbb{R} \setminus \Bigl( \bigcap_{F \in \mathcal{A} \setminus \{B\}} F \Bigr)
= \bigcup_{F \in \mathcal{A} \setminus \{B\}} (\mathbb{R} \setminus F),
$$

where each $$\mathbb{R} \setminus F$$ is open.

This means that $$\bigcup_{F \in \mathcal{A} \setminus \{B\}} (\mathbb{R} \setminus F)$$
is the open cover of $$B$$, thus resulting in its finite subcover
$$\mathbb{R} \setminus F_1, \dots, \mathbb{R} \setminus F_n$$ such that
$$B \subseteq \bigcup_{k=1}^{n} (\mathbb{R} \setminus F_k)$$.

$$\therefore\ B \cap \Bigl( \bigcap_{k=1}^{n} F_k \Bigr) = \emptyset$$.
$$\square$$

> **Exercise 6.** Prove that if $$a, b \in \mathbb{R}$$ and $$a < b$$, then
>
> $$
> |(a,b)| = |[a,b)| = |(a,b]| = b - a.
> $$
{: .problem #ex-2a-6 }

*Solution.* ① $$\lvert (a,b)\rvert = b - a$$ $$\Rightarrow$$ By Def.

② $$\lvert (a,b]\rvert = \lvert (a,b) \cup \{b\}\rvert = \lvert (a,b)\rvert = b - a$$
($$\because$$ $$\lvert \text{finite subsets}\rvert = 0$$).

③ Same for $$\lvert [a,b)\rvert = b - a$$.

> **Exercise 7.** Suppose $$a, b, c, d$$ are real numbers with $$a < b$$ and
> $$c < d$$. Prove that
>
> $$
> |(a,b) \cup (c,d)| = (b - a) + (d - c)
> $$
>
> if and only if $$(a,b) \cap (c,d) = \emptyset$$.
{: .problem #ex-2a-7 }

*Solution.* ① If $$(a,b) \cap (c,d) = \emptyset$$, WLOG set
$$a < b < c < d$$.

$$
|(a,b) \cup (c,d)| = |(a,d) \setminus [b,c]| \le |(a,b)| + |(c,d)|.
$$

$$
\therefore\ |(a,b)| + |(c,d)| \ge |(a,b) \cup (c,d)|
\ge |(a,d)| - |[b,c]|.
$$

$$\therefore\ (b - a) + (d - c) = \lvert (a,b) \cup (c,d)\rvert$$.

② If $$\lvert (a,b) \cup (c,d)\rvert = (b - a) + (d - c) = \lvert (a,b)\rvert + \lvert (c,d)\rvert$$, it
should be $$\lvert (a,b) \cap (c,d)\rvert = 0$$.

$$\therefore\ (a,b) \cap (c,d) = \emptyset$$ as $$(a,b)$$ and $$(c,d)$$ are
open intervals.

> **Exercise 12.** Suppose $$r_1, r_2, \dots$$ is a sequence that contains
> every rational number. Let
>
> $$
> F = \mathbb{R} \setminus \bigcup_{k=1}^{\infty}
> \Bigl( r_k - \frac{1}{2^k},\ r_k + \frac{1}{2^k} \Bigr).
> $$
>
> - **(a)** Show that $$F$$ is a closed subset of $$\mathbb{R}$$.
> - **(b)** Prove that if $$I$$ is an interval contained in $$F$$, then
>   $$I$$ contains at most one element.
> - **(c)** Prove that $$\lvert F\rvert = \infty$$.
{: .problem #ex-2a-12 }

*Solution.* Suppose $$r_1, r_2, \dots$$ is a sequence that contains every
rational number. Let
$$F = \mathbb{R} \setminus \bigcup_{k=1}^{\infty}
\bigl( r_k - \frac{1}{2^k}, r_k + \frac{1}{2^k} \bigr)$$.

(a) $$F^c = \bigcup_{k=1}^{\infty}
\bigl( r_k - \frac{1}{2^k}, r_k + \frac{1}{2^k} \bigr)$$ $$\rightarrow$$ open
$$\therefore$$ $$F$$ is closed.

(b) If $$I$$ is an interval contained in $$F$$ that contains at least two
elements of $$F$$, then it is uncountable, and contains a rational number.
But since $$F^c$$ contains all rational numbers, it makes a contradiction.

(c) From subadditivity, we have

$$
\begin{aligned}
|\mathbb{R} \setminus F|
&= \Bigl| \bigcup_{k=1}^{\infty}
   \Bigl( r_k - \frac{1}{2^k},\ r_k + \frac{1}{2^k} \Bigr) \Bigr| \\
&\le \sum_{k=1}^{\infty} \ell\Bigl(
   \Bigl( r_k - \frac{1}{2^k},\ r_k + \frac{1}{2^k} \Bigr) \Bigr) \\
&= \sum_{k=1}^{\infty} \frac{1}{2^{k-1}} = 2.
\end{aligned}
$$

Thus, $$F = \mathbb{R} \setminus (\mathbb{R} \setminus F)$$, and

$$
|F| \ge |\mathbb{R}| - |\mathbb{R} \setminus F| = +\infty.
$$

$$\therefore\ \lvert F\rvert = +\infty$$.

> **Exercise 13.** Suppose $$\varepsilon > 0$$. Prove that there exists a
> subset $$F$$ of $$[0,1]$$ such that $$F$$ is closed, every element of $$F$$
> is an irrational number, and $$\lvert F\rvert > 1 - \varepsilon$$.
{: .problem #ex-2a-13 }

*Solution.* Let $$r_1, r_2, \dots$$ be an enumeration of
$$\mathbb{Q} \cap [0,1]$$. Then denote

$$
F = [0,1] \setminus \bigcup_{k=1}^{\infty}
\Bigl( r_k - \frac{\varepsilon}{2^{k+1}},\ r_k + \frac{\varepsilon}{2^{k+1}} \Bigr).
$$

By Exercise 12, we know that $$F$$ is closed and every element of $$F$$ is
irrational.

Also,

$$
\begin{aligned}
|[0,1] \setminus F|
&\le \Bigl| \bigcup_{k=1}^{\infty}
   \Bigl( r_k - \frac{\varepsilon}{2^{k+1}},\ r_k + \frac{\varepsilon}{2^{k+1}} \Bigr) \Bigr| \\
&\le \sum_{k=1}^{\infty} \ell\Bigl(
   \Bigl( r_k - \frac{\varepsilon}{2^{k+1}},\ r_k + \frac{\varepsilon}{2^{k+1}} \Bigr) \Bigr) \\
&= \sum_{k=1}^{\infty} \frac{\varepsilon}{2^k} = \varepsilon.
\end{aligned}
$$

Thus, $$\lvert F\rvert \ge \lvert [0,1]\rvert - \lvert [0,1] \setminus F\rvert \ge 1 - \varepsilon$$.

Applying this with $$\varepsilon / 2$$ in place of $$\varepsilon$$ gives
$$\lvert F\rvert \ge 1 - \varepsilon / 2 > 1 - \varepsilon$$.

## References

- Sheldon Axler, *Measure, Integration & Real Analysis* — Chapter 2 and
  Section 2A with Exercises 2A. The exercise statements are quoted from the
  book.
- The notes and the exercise answers are mine, typeset from my handwritten
  notebook. The structure of each answer is unchanged; small slips in the
  answers are corrected.
