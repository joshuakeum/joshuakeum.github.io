---
title: "Mathematical Statistics 1: Homework 1"
date: 2026-11-21 09:00:00 +0900
categories: [Study Notes, Mathematical Statistics 1]
tags: [homework, inclusion-exclusion, bonferroni, bayes, continuity of probability]
description: Homework 1 of Mathematical Statistics 1 — textbook Chapter 1 exercises 1 to 5, inclusion–exclusion and Bonferroni's inequality, and the pairing probability of Example 1.1.2.
math: true
mermaid: false
render_with_liquid: false
---

> The problems are from the Homework 1 sheet of Mathematical Statistics 1 and from the textbook. The answers are my own, translated into English. Where an answer was mathematically wrong or left a step out, a note marked **Correction** or **Added** says what was changed or added; nothing else is changed. This homework uses [Part 1](/posts/mathstat1-definition-of-probability/) and [Part 2](/posts/mathstat1-conditional-probability/) of the notes.
{: .prompt-info }

## The homework sheet

1. Textbook, Chapter 1, exercises 1, 2, 3, 4, 5. (Q1 to Q5 below.)
2. For $$A_1, A_2, \dots, A_n \in \mathbb{B}$$, prove the following. (Q6 below.)
   - (a) (Principle of inclusion–exclusion)
     $$P(\cup_{k=1}^{n} A_k) = \sum_{k=1}^{n} P(A_k) - \sum_{1 \le k_1 < k_2 \le n} P(A_{k_1} \cap A_{k_2}) + \sum_{1 \le k_1 < k_2 < k_3 \le n} P(A_{k_1} \cap A_{k_2} \cap A_{k_3}) + \cdots + (-1)^{n+1} P(\cap_{k=1}^{n} A_k)$$.
   - (b) (Bonferroni's inequality)
     $$\sum_{i=1}^{n} P(A_i) - \sum_{i<j} P(A_i \cap A_j) \le P(\cup_{i=1}^{n} A_i) \le \sum_{i=1}^{n} P(A_i)$$.
3. Understand the solution of Example 1.1.2 of the textbook and write it in your own words. (Q7 below.) The textbook's solution does not argue the formulas in detail, so give detailed arguments in the submitted solution.

## Q1

> **Q1 (textbook 1.1).** When three dice are thrown, find the probability that at least one of the three dice shows a $$6$$.
{: .problem #hw-q1 }

*Proof.* For each die, let $$A_i$$ ($$i \in \{1, 2, 3\}$$) be the event that the $$i$$-th die shows a $$6$$, and let $$A$$ be the event that at least one of the three dice shows a $$6$$. We need $$P(A)$$.

Since $$A = A_1 \cup A_2 \cup A_3$$, by (b) of Theorem 1.1.2,

$$
P(A) = P(A_1 \cup A_2 \cup A_3) = P(A_1) + P(A_2) + P(A_3) - P(A_1 \cap A_2) - P(A_2 \cap A_3) - P(A_3 \cap A_1) + P(A_1 \cap A_2 \cap A_3).
$$

Moreover, for any two distinct elements $$i, j$$ of $$\{1, 2, 3\}$$, $$P(A_i) = \frac{1}{6}$$, $$P(A_i \cap A_j) = \frac{1}{36}$$, and $$P(A_1 \cap A_2 \cap A_3) = \frac{1}{216}$$. Therefore

$$
P(A) = \frac{1}{6} + \frac{1}{6} + \frac{1}{6} - \frac{1}{36} - \frac{1}{36} - \frac{1}{36} + \frac{1}{216} = \frac{91}{216}. \qquad \blacksquare
$$

## Q2

> **Q2 (textbook 1.2).** One card is drawn at random from cards marked with the numbers $$1$$ to $$10$$, one number each. Given that the card drawn is even, find the probability that the number on the card is at least $$5$$.
{: .problem #hw-q2 }

*Proof.* Let $$A$$ be the event that the card drawn is even and $$B$$ the event that its number is at least $$5$$. We need $$P(B \mid A)$$.

Let the sample space be $$\mathcal{C}$$. Since the observation is the number on the drawn card, by the definition of the sample space

$$
\mathcal{C} = \{x : 1 \le x \le 10,\ x \in \mathbb{N}\} \tag{2.1}
$$

and $$P(B \mid A) = \dfrac{P(A \cap B)}{P(A)}$$. Also $$A = \{2, 4, 6, 8, 10\}$$ and $$B = \{5, 6, 7, 8, 9, 10\}$$. Hence $$A \cap B = \{6, 8, 10\}$$, so $$P(A) = \frac{5}{10} = \frac{1}{2}$$ and $$P(A \cap B) = \frac{3}{10}$$.

Accordingly,

$$
P(B \mid A) = \frac{P(A \cap B)}{P(A)} = \frac{3/10}{1/2} = \frac{3}{5}. \qquad \blacksquare
$$

**Correction.** The last line of the original answer reads $$P(A \mid B)$$; it should be $$P(B \mid A)$$, as above. (The value $$\frac{3}{5}$$ is that of $$P(B \mid A)$$; $$P(A \mid B) = \frac{3}{6} = \frac{1}{2}$$.)

## Q3

> **Q3 (textbook 1.3).** A factory produces the same kind of spring using machines A, B and C, and the probabilities that machines A, B and C produce a defective item are known to be $$1\%$$, $$2\%$$ and $$3\%$$ respectively. Also, $$30\%$$ of all the springs produced in this factory are made by machine A, $$50\%$$ by machine B, and $$20\%$$ by machine C.
>
> - (a) When one of all the springs produced on a certain day is chosen at random, find the probability that it is defective.
> - (b) When one of all the springs produced on a certain day is chosen at random, it was defective. Under this condition, find the conditional probability that it was made by machine B.
{: .problem #hw-q3 }

**(a)** *Proof.* When one of all the springs produced on a certain day is chosen at random, let $$X_1, X_2, X_3$$ be the events that the spring was made by machine A, B, or C, and let $$Y$$ be the event that it is defective; it suffices to find $$P(Y)$$. Let the sample space be $$\mathcal{C}$$.

By the conditions of the problem, $$P(X_1) = 0.3$$, $$P(X_2) = 0.5$$, $$P(X_3) = 0.2$$. The probability that a spring produced by machine A is defective is the probability that $$Y$$ occurs given the event $$X_1$$, that is, the conditional probability $$P(Y \mid X_1)$$. Without loss of generality, machines B and C can be interpreted in the same way. Therefore $$P(Y \mid X_1) = 0.01$$, $$P(Y \mid X_2) = 0.02$$, $$P(Y \mid X_3) = 0.03$$.

A spring produced by one machine cannot be produced by another machine at the same time, and $$P(X_1) + P(X_2) + P(X_3) = 1$$, so the events $$X_1, X_2, X_3$$ partition the sample space $$\mathcal{C}$$ without common parts. Then, by the law of total probability, $$P(Y) = P(Y \mid X_1)P(X_1) + P(Y \mid X_2)P(X_2) + P(Y \mid X_3)P(X_3)$$.

Therefore $$P(Y) = 0.01 \times 0.3 + 0.02 \times 0.5 + 0.03 \times 0.2 = 0.019$$. $$\blacksquare$$

**(b)** *Proof.* Following the definitions of (a), we need $$P(X_2 \mid Y)$$.

By the definition of conditional probability, $$P(X_2 \mid Y) = \dfrac{P(X_2 \cap Y)}{P(Y)}$$, and from (a), $$P(Y) = 0.019$$. Moreover, by the multiplication rule, $$P(X_2 \cap Y) = P(Y \mid X_2)P(X_2) = 0.02 \times 0.5 = 0.01$$.

Therefore $$P(X_2 \mid Y) = \dfrac{P(X_2 \cap Y)}{P(Y)} = \dfrac{0.01}{0.019} = \dfrac{10}{19}$$. $$\blacksquare$$

## Q4

> **Q4 (textbook 1.4).** Three components are connected in parallel inside a device, and the device works normally if at least one of them works. If the failures of the components are independent and each component fails with probability $$0.05$$, find the probability that the device works normally.
{: .problem #hw-q4 }

*Proof.* Call the three components A, B, C. Let $$X_1, X_2, X_3$$ be the events that components A, B, C fail, and $$X$$ the event that the device works normally; we need $$P(X)$$.

The device works unless all three components fail, so $$X = (X_1 \cap X_2 \cap X_3)^{c}$$, and by the conditions $$P(X_i) = 0.05$$ for every $$i \in \{1, 2, 3\}$$. By the probability of the complement, $$P(X) = P\bigl((X_1 \cap X_2 \cap X_3)^{c}\bigr) = 1 - P(X_1 \cap X_2 \cap X_3)$$. Since $$X_1, X_2, X_3$$ are mutually independent, $$1 - P(X_1 \cap X_2 \cap X_3) = 1 - P(X_1)P(X_2)P(X_3)$$.

Therefore $$P(X) = 1 - P(X_1)P(X_2)P(X_3) = 1 - 0.05 \times 0.05 \times 0.05 = 0.999875$$. $$\blacksquare$$

## Q5

> **Q5 (textbook 1.5).** For a subset $$A$$ of the set of all positive real numbers, a probability is defined by
>
> $$
> P(A) = \int_A e^{-x}\,dx \tag{5.1}
> $$
>
> For $$A_k = \{x : 2 - \tfrac{1}{k} < x \le 3\}$$ ($$k = 1, 2, \dots$$), find the following events and probabilities.
>
> - (a) $$\lim_{k \to \infty} A_k$$ and $$P\bigl(\lim_{k \to \infty} A_k\bigr)$$
> - (b) $$P(A_k)$$ and $$\lim_{k \to \infty} P(A_k)$$
{: .problem #hw-q5 }

**(a)** *Proof.* To find $$\lim_{k \to \infty} A_k$$, we must first check that the limit exists. For a sequence of sets $$A_k$$, the following proposition holds.

$$
A_k \text{ converges} \Longleftrightarrow \limsup A_n = \liminf A_n =: A := \lim A_n \tag{5.2}
$$

Here we define $$\limsup A_n := \{x : x \in A_n \text{ for infinitely many } n\}$$ and $$\liminf A_n := \{x : x \in A_n \text{ for all but finitely many } n\}$$.

Then $$\limsup A_n = \liminf A_n = \{x : 2 \le x \le 3\}$$, so the sequence of sets $$A_k$$ converges, and the set it converges to is $$\lim A_n = \{x : 2 \le x \le 3\}$$. Call this set $$A$$.

Therefore, by the definition of probability,

$$
P\Bigl(\lim_{k \to \infty} A_k\Bigr) = P(A) = \int_2^3 e^{-x}\,dx = \bigl[-e^{-x}\bigr]_2^3 = e^{-2} - e^{-3} = \frac{e - 1}{e^3}. \qquad \blacksquare
$$

**Correction and Added.** In the original answer the definitions of $$\limsup$$ and $$\liminf$$ were written in terms of "limit points taken from infinitely many $$n$$"; they are written above in the standard form. The equality $$\limsup A_n = \liminf A_n = [2,3]$$ is checked as follows. If $$2 \le x \le 3$$, then $$2 - \tfrac{1}{k} < x \le 3$$ for every $$k$$, so $$x \in A_k$$ for all $$k$$. If $$x > 3$$, then $$x \notin A_k$$ for every $$k$$. If $$x < 2$$, then $$x \in A_k$$ only when $$k < \dfrac{1}{2 - x}$$, that is, for finitely many $$k$$. Hence $$\limsup A_n = \liminf A_n = [2,3]$$. (Equivalently, $$A_1 \supseteq A_2 \supseteq \cdots$$ is decreasing with $$\bigcap_k A_k = [2,3]$$, and the result agrees with the continuity of probability from above.)

**(b)** *Proof.* First, by the definition of probability,

$$
P(A_k) = \int_{2 - \frac{1}{k}}^{3} e^{-x}\,dx = \bigl[-e^{-x}\bigr]_{2 - \frac{1}{k}}^{3} = e^{-2 + \frac{1}{k}} - e^{-3}.
$$

Now we only need the limit of the sequence $$P(A_k) = e^{-2 + \frac{1}{k}} - e^{-3}$$ ($$k = 1, 2, \dots$$).

For any real number $$\varepsilon > 0$$, $$e^{2}\varepsilon > 0$$, so $$\ln(e^{2}\varepsilon + 1) > 0$$, and hence there is a natural number $$N$$ with $$N \ln(e^{2}\varepsilon + 1) > 1$$. Then $$n \ln(e^{2}\varepsilon + 1) > 1$$ for every natural number $$n \ge N$$. Accordingly, for every natural number $$n \ge N$$, $$\frac{1}{n} < \ln(e^{2}\varepsilon + 1)$$, so $$e^{1/n} < e^{2}\varepsilon + 1$$, that is, $$e^{-2 + \frac{1}{n}} - e^{-2} < \varepsilon$$. Also $$e^{-2 + \frac{1}{n}} - e^{-2} = \bigl\lvert (e^{-2 + \frac{1}{n}} - e^{-3}) - (e^{-2} - e^{-3})\bigr\rvert$$.

In summary, for any positive real number $$\varepsilon$$ there is a natural number $$N$$ such that $$\lvert P(A_n) - (e^{-2} - e^{-3})\rvert < \varepsilon$$ for all natural numbers $$n \ge N$$. Therefore $$\lim_{k \to \infty} P(A_k) = e^{-2} - e^{-3} = \dfrac{e - 1}{e^3}$$. $$\blacksquare$$

## Q6

> **Q6 (sheet problem 2).** For $$A_1, A_2, \dots, A_n \in \mathbb{B}$$, prove the following.
>
> - (a) (Principle of inclusion–exclusion)
> - (b) (Bonferroni's inequality)
{: .problem #hw-q6 }

**(a)** (Principle of inclusion–exclusion)

$$
P\Bigl(\bigcup_{k=1}^{n} A_k\Bigr) = \sum_{k=1}^{n} P(A_k) - \sum_{1 \le k_1 < k_2 \le n} P(A_{k_1} \cap A_{k_2}) + \cdots + (-1)^{n+1} P\Bigl(\bigcap_{k=1}^{n} A_k\Bigr) \tag{6.1}
$$

*Proof.* Let $$A = \bigcup_{k=1}^{n} A_k$$ ($$n \ge 2$$). We prove the principle of inclusion–exclusion by mathematical induction.

1. When $$n = 2$$. When $$A = A_1 \cup A_2$$ and $$B = A_2 \setminus A_1$$, we have $$A_1 \cap B = \emptyset$$ and $$A_1 \cup B = A$$, so by the additivity of probability $$P(A_1 \cup B) = P(A_1) + P(B) = P(A_1) + P(A_2 \setminus A_1)$$. Also, $$A_2 \setminus A_1$$ and $$A_1 \cap A_2$$ are disjoint and $$(A_2 \setminus A_1) \cup (A_1 \cap A_2) = A_2 \cap (A_1 \cup A_1^{c}) = A_2 \cap \mathcal{C} = A_2$$, so likewise by the additivity of probability $$P(A_2) = P(A_2 \setminus A_1) + P(A_1 \cap A_2)$$. In other words, $$P(A_2 \setminus A_1) = P(A_2) - P(A_1 \cap A_2)$$, so $$P(A_1 \cup B) = P(A_1) + P(A_2) - P(A_1 \cap A_2)$$.

2. Suppose the identity holds for $$n = k$$, that is,

   $$
   P\Bigl(\bigcup_{i=1}^{k} A_i\Bigr) = \sum_{i=1}^{k} P(A_i) - \sum_{1 \le i_1 < i_2 \le k} P(A_{i_1} \cap A_{i_2}) + \cdots + (-1)^{k+1} P\Bigl(\bigcap_{i=1}^{k} A_i\Bigr) \tag{6.2}
   $$

   Then, since $$\bigcup_{i=1}^{k+1} A_i = \bigl(\bigcup_{i=1}^{k} A_i\bigr) \cup A_{k+1}$$, by the result of 1,

   $$
   P\Bigl(\bigcup_{i=1}^{k+1} A_i\Bigr) = P\Bigl(\bigcup_{i=1}^{k} A_i\Bigr) + P(A_{k+1}) - P\Bigl(\Bigl(\bigcup_{i=1}^{k} A_i\Bigr) \cap A_{k+1}\Bigr) \tag{6.3}
   $$

   Also, $$\bigl(\bigcup_{i=1}^{k} A_i\bigr) \cap A_{k+1} = \bigcup_{i=1}^{k} (A_i \cap A_{k+1})$$, so by (6.2),

   $$
   \begin{aligned}
   P\Bigl(\bigcup_{i=1}^{k+1} A_i\Bigr)
   &= P\Bigl(\bigcup_{i=1}^{k} A_i\Bigr) + P(A_{k+1}) - P\Bigl(\bigcup_{i=1}^{k} (A_i \cap A_{k+1})\Bigr) \\
   &= \sum_{i=1}^{k} P(A_i) - \sum_{1 \le i_1 < i_2 \le k} P(A_{i_1} \cap A_{i_2}) + \cdots + (-1)^{k+1} P\Bigl(\bigcap_{i=1}^{k} A_i\Bigr) + P(A_{k+1}) \\
   &\quad - \Bigl[\sum_{i=1}^{k} P(A_i \cap A_{k+1}) - \sum_{1 \le i_1 < i_2 \le k} P\bigl((A_{i_1} \cap A_{k+1}) \cap (A_{i_2} \cap A_{k+1})\bigr) + \cdots + (-1)^{k+1} P\Bigl(\bigcap_{i=1}^{k} (A_i \cap A_{k+1})\Bigr)\Bigr] \\
   &= \sum_{i=1}^{k+1} P(A_i) - \sum_{1 \le i_1 < i_2 \le k+1} P(A_{i_1} \cap A_{i_2}) + \cdots + (-1)^{k+2} P\Bigl(\bigcap_{i=1}^{k+1} A_i\Bigr).
   \end{aligned}
   $$

The identity holds for $$n = 2$$, and if it holds for $$n = k$$ it also holds for $$n = k + 1$$. Therefore the principle of inclusion–exclusion holds for every natural number $$n \ge 2$$. $$\blacksquare$$

**Correction.** In the original statement of (6.1) the left side was written $$P(\cup P(A_k))$$ and the first sum $$\sum A_k$$; they are corrected above to $$P(\cup A_k)$$ and $$\sum P(A_k)$$. **Added.** In the last equality, the sets of indices of size $$r$$ in $$\{1, \dots, k+1\}$$ either omit $$k+1$$ (they come from the first line, with sign $$(-1)^{r+1}$$) or contain it (they come from the bracket, as $$A_{i_1} \cap \cdots \cap A_{i_{r-1}} \cap A_{k+1}$$ with the bracket's sign reversed, again $$(-1)^{r+1}$$), and $$P(A_{k+1})$$ is the term with $$r = 1$$ that contains $$k+1$$.

**(b)** (Bonferroni's inequality)

$$
\sum_{i=1}^{n} P(A_i) - \sum_{i<j} P(A_i \cap A_j) \le P\Bigl(\bigcup_{i=1}^{n} A_i\Bigr) \le \sum_{i=1}^{n} P(A_i) \tag{6.4}
$$

*Proof.*

1. First we prove $$P\bigl(\bigcup_{i=1}^{n} A_i\bigr) \le \sum_{i=1}^{n} P(A_i)$$. Let $$B_1 = A_1$$ and, for natural numbers $$i \ge 2$$, let $$B_i = A_i - \bigcup_{j=1}^{i-1} A_j$$.

   When $$n = 1$$, $$P(A_1) = P(A_1)$$, so the inequality holds trivially. When $$n \ge 2$$, by the definition above, $$B_i \cap B_j = \emptyset$$ for all natural numbers $$i, j$$ with $$1 \le i < j \le n$$, and $$\bigcup_{i=1}^{n} B_i = \bigcup_{i=1}^{n} A_i$$. Therefore, by the additivity of probability, $$P\bigl(\bigcup_{i=1}^{n} A_i\bigr) = P\bigl(\bigcup_{i=1}^{n} B_i\bigr) = \sum_{i=1}^{n} P(B_i)$$.

   Also, $$B_i \subset A_i$$ for every natural number $$i$$ with $$1 \le i \le n$$, so $$P(B_i) \le P(A_i)$$, and thus $$\sum_{i=1}^{n} P(B_i) \le \sum_{i=1}^{n} P(A_i)$$. In other words, $$P\bigl(\bigcup_{i=1}^{n} A_i\bigr) \le \sum_{i=1}^{n} P(A_i)$$.

2. This time we prove $$\sum_{i=1}^{n} P(A_i) - \sum_{i<j} P(A_i \cap A_j) \le P\bigl(\bigcup_{i=1}^{n} A_i\bigr)$$ ($$n \ge 2$$).

   We prove it by checking how each element $$\omega$$ of the sample space $$\mathcal{C}$$ contributes to the left side and to the right side of the inequality.

   First, if $$\omega \notin \bigcup_{i=1}^{n} A_i$$, it contributes to neither the right side nor the left side. Next, suppose that $$\omega$$ belongs to exactly $$r$$ of the sets $$A_1, \dots, A_n$$ ($$r$$ is any natural number at most $$n$$). Then $$\omega$$ is counted on the left side $$\binom{r}{1} - \binom{r}{2} = r - \dfrac{r(r-1)}{2} = \dfrac{r(3 - r)}{2}$$ times, but on the right side once. Since $$r \ge 1$$ and $$r$$ is a natural number, $$\dfrac{r(3 - r)}{2} \le 1$$. Therefore, for every element $$\omega$$ of the sample space, the contribution of $$\omega$$ to the probability is always less than or equal on the left side than on the right side, so the probability on the left side is less than or equal to the probability on the right side.

Combining 1 and 2, for every natural number $$n \ge 2$$, $$\sum_{i=1}^{n} P(A_i) - \sum_{i<j} P(A_i \cap A_j) \le P\bigl(\bigcup_{i=1}^{n} A_i\bigr) \le \sum_{i=1}^{n} P(A_i)$$ holds. $$\blacksquare$$

**Added.** The inequality $$\frac{r(3-r)}{2} \le 1$$ holds because it is equivalent to $$(r-1)(r-2) \ge 0$$, true for every integer $$r$$. The counting argument is made precise with indicator functions. Define

$$
L(\omega) = \sum_{i=1}^{n} I_{A_i}(\omega) - \sum_{i<j} I_{A_i \cap A_j}(\omega).
$$

By the counting above, $$L(\omega) \le I_{\cup A_i}(\omega)$$ for every $$\omega \in \mathcal{C}$$. Take expectations; since expectation is linear and monotone and $$E(I_A) = P(A)$$ ([Part 4](/posts/mathstat1-expectation-mgf/)), this gives $$\sum_i P(A_i) - \sum_{i<j} P(A_i \cap A_j) \le P(\cup A_i)$$.

## Q7

> **Q7 (sheet problem 3; textbook Example 1.1.2).** When $$n$$ couples line up at random in two rows, the husbands together in one row and the wives together in the other, find the probability that at least one couple ends up standing facing each other.
{: .problem #hw-q7 }

*Proof.* When $$n$$ couples line up at random in two rows, the husbands together in one row and the wives together in the other, without loss of generality we can fix the order of the people in the husbands' row and number them $$1$$ to $$n$$ in that order. Let $$A_i$$ be the event that the wife of husband $$i$$ stands facing husband $$i$$. Then the probability asked for is $$P\bigl(\bigcup_{i=1}^{n} A_i\bigr)$$.

Now, the event that exactly any prescribed $$k$$ of the $$n$$ couples face each other corresponds, among the $$n!$$ ways in which the $$n$$ wives line up in a row with order taken into account, only to the $$(n-k)!$$ ways in which the positions of those $$k$$ wives are fixed in advance, each opposite her own husband, and only the remaining $$(n-k)$$ wives line up in a row. That is, for any natural numbers $$1 \le i_1 < \cdots < i_k \le n$$, $$P\bigl(\bigcap_{j=1}^{k} A_{i_j}\bigr) = \dfrac{(n-k)!}{n!}$$. In other words, the following hold.

$$
\begin{aligned}
P(A_1) = \cdots = P(A_n) &= \frac{(n-1)!}{n!}, \\
P(A_1 \cap A_2) = \cdots = P(A_{n-1} \cap A_n) &= \frac{(n-2)!}{n!}, \\
P\Bigl(\bigcap_{i=1}^{n} A_i\Bigr) &= \frac{1}{n!}.
\end{aligned}
$$

Then, by the principle of inclusion–exclusion,

$$
\begin{aligned}
P\Bigl(\bigcup_{i=1}^{n} A_i\Bigr)
&= \sum_{k=1}^{n} P(A_k) - \sum_{1 \le k_1 < k_2 \le n} P(A_{k_1} \cap A_{k_2}) + \cdots + (-1)^{n+1} P\Bigl(\bigcap_{k=1}^{n} A_k\Bigr) \\
&= \sum_{k=1}^{n} (-1)^{k-1} \binom{n}{k} \frac{(n-k)!}{n!}
= 1 - \frac{1}{2!} + \cdots + (-1)^{n-1} \frac{1}{n!}. \qquad \blacksquare
\end{aligned}
$$

**Added.** The last equality uses $$\binom{n}{k}\dfrac{(n-k)!}{n!} = \dfrac{1}{k!}$$. As $$n \to \infty$$ the probability tends to $$1 - e^{-1} \approx 0.632$$.
