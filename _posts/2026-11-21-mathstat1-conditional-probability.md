---
title: "Mathematical Statistics 1: Ch. 1 Part 2 — Conditional Probability and Independence"
date: 2026-11-21 08:20:00 +0900
categories: [Study Notes, Mathematical Statistics 1]
tags: [conditional probability, bayes theorem, independence, total probability]
description: Conditional probability, the multiplication rule, the law of total probability, Bayes' theorem, and independence of events. Chapter 1, notes section 2 of Mathematical Statistics 1.
math: true
mermaid: false
render_with_liquid: false
---

> My handwritten notes, translated into English. Section 2 of Chapter 1 in my notes. It corresponds to §1.2 of the textbook. Statements and proofs follow my notes; I only corrected expressions that were mathematically wrong. Material taken from the textbook is collected at the end under "Supplement from the textbook".
{: .prompt-info }

## 2.1 Conditional probability

> **Definition (Conditional probability).** $$\rightarrow$$ conditional distribution! (Chapter 2)
> Let $$P(C) > 0$$ (condition!!). When $$C$$ is given, the conditional probability of $$A$$ relative to $$C$$ is
>
> $$
> P(A \mid C) = \frac{P(A \cap C)}{P(C)}.
> $$
>
> $$\rightarrow$$ $$C$$ is regarded as the whole sample space.
{: .definition #def-conditional-probability }

> **Theorem (Properties of conditional probability).** If $$P(C) > 0$$ and $$C, C_1, C_2, \dots$$ are events, then
>
> - (1) $$P(C_1 \mid C) \ge 0$$.
> - (2) When $$C_1, C_2, \dots$$ are mutually disjoint, $$\displaystyle P\Bigl(\bigcup_{i=1}^{\infty} C_i \,\Big\vert\, C\Bigr) = \sum_{i=1}^{\infty} P(C_i \mid C)$$. $$\rightarrow$$ A conditional probability satisfies countable additivity.
> - (3) $$P(C \mid C) = 1$$.
> - (4) (Multiplication rule) When $$P(C_1) > 0$$,
>
>   $$
>   P(C_1 \cap C_2) = P(C_1)\,P(C_2 \mid C_1),
>   $$
>
>   $$
>   P(C_1 \cap \cdots \cap C_n) = P(C_1)\,P(C_2 \mid C_1)\,P(C_3 \mid C_1 \cap C_2) \cdots P(C_n \mid C_1 \cap \cdots \cap C_{n-1}).
>   $$
>
> - (5) (Law of total probability) $$P(C_i) > 0$$ for all $$i = 1, \dots, k$$, $$\bigcup_{i=1}^{k} C_i = \mathcal{C}$$, and the $$C_i$$ are disjoint. Then
>
>   $$
>   P(C) = \sum_{i=1}^{k} P(C_i)\,P(C \mid C_i).
>   $$
>
> - (6) (Bayes' theorem) $$P(C_i) > 0$$ for $$i = 1, \dots, k$$, $$\bigcup_{i=1}^{k} C_i = \mathcal{C}$$, and the $$C_i$$ are disjoint. $$\Rightarrow$$
>
>   $$
>   P(C_j \mid C) = \frac{P(C_j)\,P(C \mid C_j)}{\sum_{i=1}^{k} P(C_i)\,P(C \mid C_i)}.
>   $$
>
>   (The denominator is $$P(C)$$.)
{: .theorem #thm-conditional-probability-properties }

*Proof.* (5)

$$
\begin{aligned}
P(C) &= P(C \cap \mathcal{C}) \\
&= P\Bigl(C \cap \bigl(\bigcup_{i=1}^{k} C_i\bigr)\Bigr) \\
&= P\Bigl(\bigcup_{i=1}^{k} (C \cap C_i)\Bigr) \\
&= \sum_{i=1}^{k} P(C \cap C_i) \qquad (\because\ (C \cap C_i) \cap (C \cap C_j) = \phi \ \ \forall i \ne j) \\
&= \sum_{i=1}^{k} P(C_i)\,P(C \mid C_i).
\end{aligned}
$$

(6)

$$
\begin{aligned}
P(C_j \mid C) &= \frac{P(C_j)\,P(C \mid C_j)}{P(C)} \\
&= \frac{P(C_j)\,P(C \mid C_j)}{\sum_{i=1}^{k} P(C_i)\,P(C \mid C_i)} \qquad (\text{by (5)}).
\end{aligned}
$$

$$\rightarrow$$ This comes from Thomas Bayes' paper of 1763 (written to prove the existence of God). He died and then it was published (he died in 1761).

\* For an event $$C$$, this is the theorem used to infer which of the causes $$C_1, \dots, C_k$$ is the true cause. $$\rightarrow$$ A theorem for finding the *probability of a cause*.

## 2.2 Independence of events

> **Definition (Independence of events).**
>
> - (a) (For two events.) $$C_1, C_2$$ are independent $$\Longleftrightarrow$$ $$P(C_1 \cap C_2) = P(C_1)\,P(C_2)$$.
>   $$\rightarrow$$ If $$C_2 > 0$$, $$P(C_1) = P(C_1 \mid C_2)$$ (the probability given $$C_2$$ equals the original probability!!).
> - (b) (For two or more events.) $$C_1, \dots, C_n$$ are independent $$\Longleftrightarrow$$
>
>   $$
>   \begin{cases}
>   P(C_i \cap C_j) = P(C_i)P(C_j) & \forall i \ne j, \\
>   P(C_{i_1} \cap C_{i_2} \cap C_{i_3}) = P(C_{i_1})P(C_{i_2})P(C_{i_3}) & \forall i_1 < i_2 < i_3, \\
>   \ \ \vdots \\
>   P(C_1 \cap \cdots \cap C_n) = P(C_1) \cdots P(C_n).
>   \end{cases}
>   $$
>
> - (c) (For collections of events.) $$\mathcal{E}_1 = \{C_1, \dots, C_m\}$$ and $$\mathcal{E}_2 = \{A_1, \dots, A_n\}$$ are independent $$\Longleftrightarrow$$ $$C_i$$ and $$A_j$$ are independent for all $$1 \le i \le m$$, $$1 \le j \le n$$.
{: .definition #def-independence }

$$\bigstar$$ Disjoint events are **not** independent!: if one occurs, the other certainly does not occur. (Venn diagram.)

**Example.** (Not independent as a whole, but pairwise independent.) A box contains four balls, marked ①, ②, ③, and one marked with all of $$1, 2, 3$$. Let $$A_i$$ be the event that the drawn ball has $$i$$ written on it ($$i \in \{1,2,3\}$$).

$$
P(A_1) = P(A_2) = P(A_3) = \tfrac{1}{2}, \qquad
P(A_1 \cap A_2) = \cdots = P(A_3 \cap A_1) = \tfrac{1}{4}
$$

$$\rightarrow$$ $$A_1, A_2, A_3$$ are pairwise independent.

$$
P(A_1 \cap A_2 \cap A_3) = \tfrac{1}{4} \ne \tfrac{1}{8} = P(A_1)P(A_2)P(A_3).
$$

## Supplement from the textbook

> The parts below are in the textbook (§1.2) but not in my notes. They are translated from the book and are not my own writing.
{: .prompt-info }

**Prior and posterior probabilities.** Bayes' theorem is the basis of Bayesian inference. $$P(A_1), P(A_2), \dots$$ express the plausibility of several models, and $$P(A_1 \mid B), P(A_2 \mid B), \dots$$ express the plausibility of each model after observing the experimental result $$B$$. For this reason $$P(A_j)$$ and $$P(A_j \mid B)$$ are called the *prior* and *posterior* probabilities, and Bayes' theorem expresses the relation between them. In the textbook it is stated as $$P(A_j \mid B) \propto P(B \mid A_j)P(A_j)$$, where the constant of proportionality is determined by the requirement that the left sides add up to $$1$$.

**Example 1.2.2.** A factory makes $$20\%$$, $$30\%$$ and $$50\%$$ of its products on machines $$M_1, M_2, M_3$$, and the defective rates of the three machines are $$3\%$$, $$2\%$$ and $$1\%$$. One product, chosen at random, is inspected and found defective. What is the probability that each machine made it?

*Solution.* Before the inspection $$P(M_1) = 0.2$$, $$P(M_2) = 0.3$$, $$P(M_3) = 0.5$$. Let $$B$$ be the event that the product is defective; $$P(B \mid M_1) = 0.03$$, $$P(B \mid M_2) = 0.02$$, $$P(B \mid M_3) = 0.01$$. By Bayes' theorem

$$
P(M_1 \mid B) : P(M_2 \mid B) : P(M_3 \mid B) = 0.2 \times 0.03 : 0.3 \times 0.02 : 0.5 \times 0.01 = 6 : 6 : 5,
$$

so $$P(M_1 \mid B) = \tfrac{6}{17}$$, $$P(M_2 \mid B) = \tfrac{6}{17}$$, $$P(M_3 \mid B) = \tfrac{5}{17}$$.

**Example 1.2.3 (pairwise independence is not enough).** Two dice are thrown. Let $$A$$ = {the first die is even}, $$B$$ = {the second die is odd}, $$C$$ = {the sum is odd}. Then $$P(A) = P(B) = P(C) = \tfrac{1}{2}$$ and $$P(A \cap B) = P(B \cap C) = P(C \cap A) = \tfrac{1}{4}$$, so $$A, B$$; $$B, C$$; $$C, A$$ are each independent. But $$A \cap B \subseteq C$$, so $$A \cap B \cap C = A \cap B$$ and $$P(C \mid A \cap B) = 1 \ne P(C)$$: observing both $$A$$ and $$B$$ changes the likelihood of $$C$$, so the three are not independent. This is why independence of three or more events requires the product rule for every sub-collection.

**Example 1.2.5.** If $$A, B$$ are independent, then $$A, B^{c}$$ are independent. Indeed $$A = (A \cap B) \cup (A \cap B^{c})$$ is a disjoint union, so $$P(A) = P(A)P(B) + P(A \cap B^{c})$$, and

$$
P(A \cap B^{c}) = P(A) - P(A)P(B) = P(A)\bigl(1 - P(B)\bigr) = P(A)P(B^{c}).
$$

## References

- 김우철, *수리통계학* (Mathematical Statistics), revised 2nd edition, 민영사, 2021 — Chapter 1.
- Mathematical Statistics 1 (326.311), Spring 2025. Instructor: Jaeyong Lee (이재용). My handwritten lecture notes, Chapter 1.
- The notes are translated without changing their wording; remarks written in the margins of the notes are kept. Where a statement in the notes was mathematically wrong it is corrected in the text.

[Previous](/posts/mathstat1-definition-of-probability/) · [Overview](/posts/mathstat1-overview/) · [Next](/posts/mathstat1-random-variables-cdf/)
