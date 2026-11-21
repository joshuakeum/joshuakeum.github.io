---
title: "Mathematical Statistics 1: Chapter 1 Exercises"
date: 2026-11-21 09:00:00 +0900
categories: [Study Notes, Mathematical Statistics 1]
tags: [exercises, probability, cdf, expectation, moment generating function, cumulants, inequalities]
description: Worked exercises for Chapter 1 of Mathematical Statistics 1 — probability, conditional probability, inclusion–exclusion, distribution functions, expectation, moment generating functions, cumulants, and inequalities.
math: true
mermaid: false
render_with_liquid: false
---

> The exercise statements are from the textbook; the answers are my own, translated into English. These exercises use [Parts 1 to 5](/posts/mathstat1-definition-of-probability/) of the notes.
{: .prompt-info }

## Exercises 1.1 to 1.5, inclusion–exclusion, and Example 1.1.2

### Exercise 1.1

> **Exercise 1.1.** When three dice are thrown, find the probability that at least one of the three dice shows a $$6$$.
{: .problem #ex1-q1 }

*Proof.* For each die, let $$A_i$$ ($$i \in \{1, 2, 3\}$$) be the event that the $$i$$-th die shows a $$6$$, and let $$A$$ be the event that at least one of the three dice shows a $$6$$. We need $$P(A)$$.

Since $$A = A_1 \cup A_2 \cup A_3$$, by (b) of Theorem 1.1.2,

$$
P(A) = P(A_1 \cup A_2 \cup A_3) = P(A_1) + P(A_2) + P(A_3) - P(A_1 \cap A_2) - P(A_2 \cap A_3) - P(A_3 \cap A_1) + P(A_1 \cap A_2 \cap A_3).
$$

Moreover, for any two distinct elements $$i, j$$ of $$\{1, 2, 3\}$$, $$P(A_i) = \frac{1}{6}$$, $$P(A_i \cap A_j) = \frac{1}{36}$$, and $$P(A_1 \cap A_2 \cap A_3) = \frac{1}{216}$$. Therefore

$$
P(A) = \frac{1}{6} + \frac{1}{6} + \frac{1}{6} - \frac{1}{36} - \frac{1}{36} - \frac{1}{36} + \frac{1}{216} = \frac{91}{216}. \qquad \blacksquare
$$

### Exercise 1.2

> **Exercise 1.2.** One card is drawn at random from cards marked with the numbers $$1$$ to $$10$$, one number each. Given that the card drawn is even, find the probability that the number on the card is at least $$5$$.
{: .problem #ex1-q2 }

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

### Exercise 1.3

> **Exercise 1.3.** A factory produces the same kind of spring using machines A, B and C, and the probabilities that machines A, B and C produce a defective item are known to be $$1\%$$, $$2\%$$ and $$3\%$$ respectively. Also, $$30\%$$ of all the springs produced in this factory are made by machine A, $$50\%$$ by machine B, and $$20\%$$ by machine C.
>
> - (a) When one of all the springs produced on a certain day is chosen at random, find the probability that it is defective.
> - (b) When one of all the springs produced on a certain day is chosen at random, it was defective. Under this condition, find the conditional probability that it was made by machine B.
{: .problem #ex1-q3 }

**(a)** *Proof.* When one of all the springs produced on a certain day is chosen at random, let $$X_1, X_2, X_3$$ be the events that the spring was made by machine A, B, or C, and let $$Y$$ be the event that it is defective; it suffices to find $$P(Y)$$. Let the sample space be $$\mathcal{C}$$.

By the conditions of the problem, $$P(X_1) = 0.3$$, $$P(X_2) = 0.5$$, $$P(X_3) = 0.2$$. The probability that a spring produced by machine A is defective is the probability that $$Y$$ occurs given the event $$X_1$$, that is, the conditional probability $$P(Y \mid X_1)$$. Without loss of generality, machines B and C can be interpreted in the same way. Therefore $$P(Y \mid X_1) = 0.01$$, $$P(Y \mid X_2) = 0.02$$, $$P(Y \mid X_3) = 0.03$$.

A spring produced by one machine cannot be produced by another machine at the same time, and $$P(X_1) + P(X_2) + P(X_3) = 1$$, so the events $$X_1, X_2, X_3$$ partition the sample space $$\mathcal{C}$$ without common parts. Then, by the law of total probability, $$P(Y) = P(Y \mid X_1)P(X_1) + P(Y \mid X_2)P(X_2) + P(Y \mid X_3)P(X_3)$$.

Therefore $$P(Y) = 0.01 \times 0.3 + 0.02 \times 0.5 + 0.03 \times 0.2 = 0.019$$. $$\blacksquare$$

**(b)** *Proof.* Following the definitions of (a), we need $$P(X_2 \mid Y)$$.

By the definition of conditional probability, $$P(X_2 \mid Y) = \dfrac{P(X_2 \cap Y)}{P(Y)}$$, and from (a), $$P(Y) = 0.019$$. Moreover, by the multiplication rule, $$P(X_2 \cap Y) = P(Y \mid X_2)P(X_2) = 0.02 \times 0.5 = 0.01$$.

Therefore $$P(X_2 \mid Y) = \dfrac{P(X_2 \cap Y)}{P(Y)} = \dfrac{0.01}{0.019} = \dfrac{10}{19}$$. $$\blacksquare$$

### Exercise 1.4

> **Exercise 1.4.** Three components are connected in parallel inside a device, and the device works normally if at least one of them works. If the failures of the components are independent and each component fails with probability $$0.05$$, find the probability that the device works normally.
{: .problem #ex1-q4 }

*Proof.* Call the three components A, B, C. Let $$X_1, X_2, X_3$$ be the events that components A, B, C fail, and $$X$$ the event that the device works normally; we need $$P(X)$$.

The device works unless all three components fail, so $$X = (X_1 \cap X_2 \cap X_3)^{c}$$, and by the conditions $$P(X_i) = 0.05$$ for every $$i \in \{1, 2, 3\}$$. By the probability of the complement, $$P(X) = P\bigl((X_1 \cap X_2 \cap X_3)^{c}\bigr) = 1 - P(X_1 \cap X_2 \cap X_3)$$. Since $$X_1, X_2, X_3$$ are mutually independent, $$1 - P(X_1 \cap X_2 \cap X_3) = 1 - P(X_1)P(X_2)P(X_3)$$.

Therefore $$P(X) = 1 - P(X_1)P(X_2)P(X_3) = 1 - 0.05 \times 0.05 \times 0.05 = 0.999875$$. $$\blacksquare$$

### Exercise 1.5

> **Exercise 1.5.** For a subset $$A$$ of the set of all positive real numbers, a probability is defined by
>
> $$
> P(A) = \int_A e^{-x}\,dx \tag{5.1}
> $$
>
> For $$A_k = \{x : 2 - \tfrac{1}{k} < x \le 3\}$$ ($$k = 1, 2, \dots$$), find the following events and probabilities.
>
> - (a) $$\lim_{k \to \infty} A_k$$ and $$P\bigl(\lim_{k \to \infty} A_k\bigr)$$
> - (b) $$P(A_k)$$ and $$\lim_{k \to \infty} P(A_k)$$
{: .problem #ex1-q5 }

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

The equality $$\limsup A_n = \liminf A_n = [2,3]$$ is checked as follows. If $$2 \le x \le 3$$, then $$2 - \tfrac{1}{k} < x \le 3$$ for every $$k$$, so $$x \in A_k$$ for all $$k$$. If $$x > 3$$, then $$x \notin A_k$$ for every $$k$$. If $$x < 2$$, then $$x \in A_k$$ only when $$k < \dfrac{1}{2 - x}$$, that is, for finitely many $$k$$. Hence $$\limsup A_n = \liminf A_n = [2,3]$$. (Equivalently, $$A_1 \supseteq A_2 \supseteq \cdots$$ is decreasing with $$\bigcap_k A_k = [2,3]$$, and the result agrees with the continuity of probability from above.)

**(b)** *Proof.* First, by the definition of probability,

$$
P(A_k) = \int_{2 - \frac{1}{k}}^{3} e^{-x}\,dx = \bigl[-e^{-x}\bigr]_{2 - \frac{1}{k}}^{3} = e^{-2 + \frac{1}{k}} - e^{-3}.
$$

Now we only need the limit of the sequence $$P(A_k) = e^{-2 + \frac{1}{k}} - e^{-3}$$ ($$k = 1, 2, \dots$$).

For any real number $$\varepsilon > 0$$, $$e^{2}\varepsilon > 0$$, so $$\ln(e^{2}\varepsilon + 1) > 0$$, and hence there is a natural number $$N$$ with $$N \ln(e^{2}\varepsilon + 1) > 1$$. Then $$n \ln(e^{2}\varepsilon + 1) > 1$$ for every natural number $$n \ge N$$. Accordingly, for every natural number $$n \ge N$$, $$\frac{1}{n} < \ln(e^{2}\varepsilon + 1)$$, so $$e^{1/n} < e^{2}\varepsilon + 1$$, that is, $$e^{-2 + \frac{1}{n}} - e^{-2} < \varepsilon$$. Also $$e^{-2 + \frac{1}{n}} - e^{-2} = \bigl\lvert (e^{-2 + \frac{1}{n}} - e^{-3}) - (e^{-2} - e^{-3})\bigr\rvert$$.

In summary, for any positive real number $$\varepsilon$$ there is a natural number $$N$$ such that $$\lvert P(A_n) - (e^{-2} - e^{-3})\rvert < \varepsilon$$ for all natural numbers $$n \ge N$$. Therefore $$\lim_{k \to \infty} P(A_k) = e^{-2} - e^{-3} = \dfrac{e - 1}{e^3}$$. $$\blacksquare$$

### Inclusion–exclusion and Bonferroni's inequality

> **Exercise.** For $$A_1, A_2, \dots, A_n \in \mathbb{B}$$, prove the following.
>
> - (a) (Principle of inclusion–exclusion)
> - (b) (Bonferroni's inequality)
{: .problem #ex1-q6 }

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

In the last equality, the sets of indices of size $$r$$ in $$\{1, \dots, k+1\}$$ either omit $$k+1$$ (they come from the first line, with sign $$(-1)^{r+1}$$) or contain it (they come from the bracket, as $$A_{i_1} \cap \cdots \cap A_{i_{r-1}} \cap A_{k+1}$$ with the bracket's sign reversed, again $$(-1)^{r+1}$$), and $$P(A_{k+1})$$ is the term with $$r = 1$$ that contains $$k+1$$.

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

The inequality $$\frac{r(3-r)}{2} \le 1$$ holds because it is equivalent to $$(r-1)(r-2) \ge 0$$, true for every integer $$r$$. The counting argument is made precise with indicator functions. Define

$$
L(\omega) = \sum_{i=1}^{n} I_{A_i}(\omega) - \sum_{i<j} I_{A_i \cap A_j}(\omega).
$$

By the counting above, $$L(\omega) \le I_{\cup A_i}(\omega)$$ for every $$\omega \in \mathcal{C}$$. Take expectations; since expectation is linear and monotone and $$E(I_A) = P(A)$$ ([Part 4](/posts/mathstat1-expectation-mgf/)), this gives $$\sum_i P(A_i) - \sum_{i<j} P(A_i \cap A_j) \le P(\cup A_i)$$.

### Example 1.1.2

> **Example 1.1.2.** When $$n$$ couples line up at random in two rows, the husbands together in one row and the wives together in the other, find the probability that at least one couple ends up standing facing each other.
{: .problem #ex1-q7 }

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

The last equality uses $$\binom{n}{k}\dfrac{(n-k)!}{n!} = \dfrac{1}{k!}$$. As $$n \to \infty$$ the probability tends to $$1 - e^{-1} \approx 0.632$$.

## Exercises 1.7 to 1.17 and further problems

### Exercise 1.7

> **Exercise 1.7.** The cumulative distribution function of a random variable $$X$$ is
>
> $$
> F(x) =
> \begin{cases}
> 0 & x < 0 \\
> x/4 + 1/4 & 0 \le x < 2 \\
> 1 & x \ge 2
> \end{cases}
> $$
>
> and $$C_k = \{x : 1/k \le x \le 2 - 1/k\}$$, $$D_k = \{x : -1/k < x < 1 + 1/k\}$$ ($$k = 1, 2, \dots$$). Find the following events and probabilities.
>
> - (a) $$\lim_{k \to \infty} C_k$$ and $$P(X \in \lim_{k \to \infty} C_k)$$
> - (b) $$\lim_{k \to \infty} D_k$$ and $$P(X \in \lim_{k \to \infty} D_k)$$
{: .problem #hw2-1-7 }

**(a)** For every natural number $$k$$, $$\frac{1}{k} \ge \frac{1}{k+1}$$, so $$C_k \subseteq C_{k+1}$$. In other words, $$C_1 \subseteq C_2 \subseteq \cdots \subseteq C_k \subseteq C_{k+1} \subseteq \cdots$$.

Therefore what we want is $$\lim_{k \to \infty} C_k = \bigcup_{k=1}^{\infty} C_k$$, and by the continuity of probability measure,

$$
P\Bigl(X \in \lim_{k \to \infty} C_k\Bigr) = P\Bigl(\bigcup_{k=1}^{\infty} C_k\Bigr) = \lim_{k \to \infty} P(C_k).
$$

In other words, we need $$\bigcup_{k=1}^{\infty} C_k$$ and $$\lim_{k \to \infty} P(C_k)$$.

For every natural number $$k$$, $$C_k \subseteq (0,2)$$, and if $$x \in (0,2)$$, there is an $$n \in \mathbb{N}$$ with $$\frac{1}{n} \le x \le 2 - \frac{1}{n}$$. Hence $$\bigcup_{k=1}^{\infty} C_k = \lim_{k \to \infty} C_k = \{x : 0 < x < 2\}$$.

Also, for any natural number $$k$$, $$P(C_k) = P\{x : \tfrac{1}{k} \le x \le 2 - \tfrac{1}{k}\} = F(2 - \tfrac{1}{k}) - \lim_{x \to \frac{1}{k}-} F(x)$$. Since $$0 < \frac{1}{k} < 2$$ and $$0 < 2 - \frac{1}{k} < 2$$, $$\lim_{x \to \frac{1}{k}-} F(x) = F(\tfrac{1}{k}) = \frac{1}{4k} + \frac{1}{4}$$.

$$
\therefore\ P(C_k) = F\bigl(2 - \tfrac{1}{k}\bigr) - F\bigl(\tfrac{1}{k}\bigr)
= \tfrac{1}{4}\bigl(2 - \tfrac{1}{k}\bigr) + \tfrac{1}{4} - \bigl(\tfrac{1}{4k} + \tfrac{1}{4}\bigr) = \tfrac{1}{2} - \tfrac{1}{2k}.
$$

Therefore $$\lim_{k \to \infty} P(C_k) = \lim_{k \to \infty}\bigl(\tfrac{1}{2} - \tfrac{1}{2k}\bigr) = \tfrac{1}{2}$$.

**(b)** For every natural number $$k$$, $$\frac{1}{k} \ge \frac{1}{k+1}$$, so $$D_k \supseteq D_{k+1}$$. In other words, $$D_1 \supseteq D_2 \supseteq \cdots \supseteq D_k \supseteq D_{k+1} \supseteq \cdots$$.

Therefore what we want is $$\lim_{k \to \infty} D_k = \bigcap_{k=1}^{\infty} D_k$$, and by the continuity of probability measure,

$$
P\Bigl(X \in \lim_{k \to \infty} D_k\Bigr) = P\Bigl(\bigcap_{k=1}^{\infty} D_k\Bigr) = \lim_{k \to \infty} P(D_k).
$$

For every natural number $$k$$, $$(0,1) \subseteq D_k$$, and if $$x \in (-\infty, 0) \cup (1, \infty)$$, there is an $$n \in \mathbb{N}$$ with $$x \notin (-\frac{1}{n}, 1 + \frac{1}{n})$$. Hence $$\bigcap_{k=1}^{\infty} D_k = \lim_{k \to \infty} D_k = \{x : 0 \le x \le 1\}$$.

Also, for any natural number $$k$$, $$P(D_k) = P\{x : -\tfrac{1}{k} < x < 1 + \tfrac{1}{k}\} = \lim_{x \to (1 + \frac{1}{k})-} F(x) - F(-\tfrac{1}{k})$$. Since $$-1 \le -\frac{1}{k} < 0$$ and $$0 < 1 + \frac{1}{k} \le 2$$, $$\lim_{x \to (1 + \frac{1}{k})-} F(x) = \frac{1}{4}(1 + \frac{1}{k}) + \frac{1}{4} = \frac{1}{2} + \frac{1}{4k}$$.

$$
\therefore\ P(D_k) = \tfrac{1}{2} + \tfrac{1}{4k} - 0 = \tfrac{1}{2} + \tfrac{1}{4k}.
$$

Therefore $$\lim_{k \to \infty} P(D_k) = \lim_{k \to \infty}\bigl(\tfrac{1}{2} + \tfrac{1}{4k}\bigr) = \tfrac{1}{2}$$.

### Exercise 1.8

> **Exercise 1.8.** Find the probability density function of $$X$$ when its cumulative distribution function is as follows.
>
> - (a) $$F(x) = 0$$ for $$x < 1$$, and $$F(x) = 1 - (1/2)^k$$ for $$k \le x < k + 1$$ ($$k = 1, 2, \dots$$)
> - (b) $$F(x) = 0$$ ($$x < 0$$), $$x^2$$ ($$0 \le x < 1$$), $$1$$ ($$x \ge 1$$)
> - (c) $$F(x) = 0$$ ($$x < 0$$), $$1 - e^{-x^2}$$ ($$x \ge 0$$)
{: .problem #hw2-1-8 }

**(a)** To find the density function of $$X$$ we have to check whether $$X$$ is a discrete random variable, a continuous random variable, or neither.

For any $$k \in \mathbb{N}$$, $$P(X = k) = F(k) - \lim_{x \to k-} F(x) = \bigl(1 - (\tfrac{1}{2})^k\bigr) - \bigl(1 - (\tfrac{1}{2})^{k-1}\bigr) = (\tfrac{1}{2})^k$$. Also, for any $$p \in \{t : t \in \mathbb{R},\ t \notin \mathbb{N}\}$$, if $$p < 1$$, $$P(X = p) = F(p) - \lim_{x \to p-} F(x) = 0 - 0 = 0$$, and if $$p > 1$$, there is a natural number $$n$$ with $$n \le p < n + 1$$, so $$P(X = p) = F(p) - \lim_{x \to p-} F(x) = \bigl(1 - (\tfrac{1}{2})^{n}\bigr) - \bigl(1 - (\tfrac{1}{2})^{n}\bigr) = 0$$.

In other words, when $$x \in \mathbb{N}$$, $$P(X = x) \ne 0$$, and when $$x \notin \mathbb{N}$$, $$P(X = x) = 0$$, and since the set of points with $$P(X = x) \ne 0$$ is countable, $$X$$ is a discrete random variable.

Then the density function $$f$$ of the discrete random variable $$X$$ is $$P(X = x)$$. Therefore

$$
f(x) = P(X = x) =
\begin{cases}
(\tfrac{1}{2})^x & (x \in \mathbb{N}) \\
0 & (x \notin \mathbb{N}).
\end{cases}
$$

**(b)** For the cumulative distribution function $$F$$ of $$X$$, define $$f(x) = 2x\, I_{[0,1)}(x)$$. Then, letting $$G(x) = \int_{-\infty}^{x} f(t)\,dt$$, there is a random variable $$X'$$ having $$G$$ as its cumulative distribution function, and if $$F(x) = G(x)$$, then by the uniqueness of the cumulative distribution function, $$f$$ is a probability density function of $$F$$.

Therefore, to show that there is a random variable $$X'$$ having $$G$$ as its cumulative distribution function, we show that $$F = G$$. Here, $$G(x)$$ is, if $$x < 0$$, $$G(x) = \int_{-\infty}^{x} 0\,dt = 0$$; if $$0 \le x < 1$$, $$G(x) = \int_{-\infty}^{0} 0\,dt + \int_0^x 2t\,dt = x^2$$; and if $$x \ge 1$$, $$G(x) = \int_{-\infty}^{0} 0\,dt + \lim_{k \to 1-}\int_0^k 2t\,dt + \int_1^x 0\,dt = 1$$.

That is, $$G(x) = 0$$ ($$x < 0$$), $$x^2$$ ($$0 \le x < 1$$), $$1$$ ($$x \ge 1$$).

Also, since by the conditions of the problem $$X$$ having $$F$$ as its cumulative distribution function was assumed to exist, showing $$F = G$$ is enough, and then by the uniqueness of the cumulative distribution function there is a random variable with $$G$$ as its cumulative distribution function, and $$f$$ is the density function of $$F$$. In other words, it suffices to show $$F = G$$. For any $$t \in \mathbb{R}$$, $$G(t) = F(t)$$. Therefore $$f$$ is a probability density function of $$F$$.

**(c)** For the cumulative distribution function $$F(x) = 0$$ ($$x < 0$$), $$1 - e^{-x^2}$$ ($$x \ge 0$$), define $$f(x) = 2x e^{-x^2} I_{[x \ge 0]}$$. Let $$G(x) = \int_{-\infty}^{x} f(t)\,dt$$. As in (b), it suffices to show $$F = G$$. If $$x < 0$$, $$G(x) = \int_{-\infty}^{x} 0\,dt = 0$$, and if $$x \ge 0$$, $$\int_{-\infty}^{x} f(t)\,dt = \int_{-\infty}^{0} 0\,dt + \int_0^x 2t e^{-t^2}\,dt = 1 - e^{-x^2}$$. That is, for any $$t \in \mathbb{R}$$, $$G(t) = F(t)$$. Therefore $$f$$ is a probability density function of $$F$$.

### Exercise 1.9

> **Exercise 1.9.** Find the constant $$c$$ and the cumulative distribution function of $$X$$ when its probability density function is
>
> - (a) $$f(x) = c\,(2/3)^x$$, $$x = 0, 1, 2, \dots$$
> - (b) $$f(x) = c\,x^2(1 - x)\, I_{(0,1)}(x)$$
> - (c) $$f(x) = c\, e^{-2\lvert x\rvert}$$, $$-\infty < x < +\infty$$
{: .problem #hw2-1-9 }

**(a)** Since the set of $$x$$ with $$f(x) \ne 0$$ is countable, $$X$$ is a discrete random variable. Therefore the cumulative distribution function of $$X$$ can be found as $$F(x) = P(X \le x) = \sum_{t \in \mathbb{Z}_+,\, t \le x} f(t)$$.

Here $$\lim_{x \to \infty} F(x) = \sum_{x=0}^{\infty} f(x) = 1$$, and we want to find the constant of proportionality $$c$$ using $$\sum_{x=0}^{\infty} f(x) = 1$$. Since $$\sum_{x=0}^{\infty} f(x)$$ is an infinite geometric series with first term $$c$$ and common ratio $$\frac{2}{3}$$,

$$
\sum_{x=0}^{\infty} f(x) = \sum_{x=0}^{\infty} c\,\bigl(\tfrac{2}{3}\bigr)^x = \frac{c}{1 - \frac{2}{3}} = 3c = 1.
$$

$$\therefore\ c = \frac{1}{3}$$.

Also, when $$x < 0$$, $$F(x) = \sum_{t \in \mathbb{Z}_+,\, t \le x} f(t) = 0$$. When $$x \ge 0$$, there is a non-negative integer $$n$$ with $$n \le x < n + 1$$, and then

$$
F(x) = \sum_{t=0}^{n} f(t) = \sum_{t=0}^{n} \tfrac{1}{3}\bigl(\tfrac{2}{3}\bigr)^t = \frac{\frac{1}{3}\bigl(1 - (\frac{2}{3})^{n+1}\bigr)}{1 - \frac{2}{3}} = 1 - \bigl(\tfrac{2}{3}\bigr)^{n+1}.
$$

In other words, the cumulative distribution function is, for a non-negative integer $$n$$,

$$
F(x) =
\begin{cases}
0 & (x < 0) \\
1 - (\frac{2}{3})^{n+1} & (n \le x < n + 1).
\end{cases}
$$

**(b)** The cumulative distribution function of $$X$$ can be found as $$F(x) = P(X \le x) = \int_{-\infty}^{x} f(t)\,dt$$. Also, we want to find $$c$$ through $$\lim_{x \to \infty} F(x) = 1$$, that is, $$\lim_{x \to \infty}\int_{-\infty}^{x} f(t)\,dt = 1$$.

If $$x \le 0$$, $$F(x) = \int_{-\infty}^{x} f(t)\,dt = \int_{-\infty}^{x} 0\,dt = 0$$. If $$0 < x < 1$$,

$$
F(x) = \int_{-\infty}^{0} 0\,dt + \int_0^x c\,t^2(1 - t)\,dt = c\,x^3\bigl(\tfrac{1}{3} - \tfrac{1}{4}x\bigr),
$$

and if $$x \ge 1$$, $$F(x) = \int_{-\infty}^{0} 0\,dt + \int_0^1 c\,t^2(1 - t)\,dt + \int_1^{\infty} 0\,dt = \frac{1}{12}c$$.

Therefore $$\lim_{x \to \infty} F(x) = \frac{1}{12}c = 1$$, so $$c = 12$$. The cumulative distribution function of $$X$$ is

$$
F(x) =
\begin{cases}
0 & (x \le 0) \\
4x^3 - 3x^4 & (0 < x < 1) \\
1 & (x \ge 1).
\end{cases}
$$

**(c)** The probability density function of $$X$$ is $$f(x) = c\,e^{-2\lvert x\rvert} = c\,e^{2x} I_{(x<0)} + c\,e^{-2x} I_{(x \ge 0)}$$. The cumulative distribution function of $$X$$ can be found as $$F(x) = P(X \le x) = \int_{-\infty}^{x} f(t)\,dt$$. We want to find $$c$$ through $$\lim_{x \to \infty} F(x) = 1$$, that is, $$\lim_{x \to \infty}\int_{-\infty}^{x} f(t)\,dt = 1$$.

If $$x < 0$$, $$F(x) = \int_{-\infty}^{x} c\,e^{2t}\,dt = \frac{1}{2}c\,e^{2x}$$, and if $$x \ge 0$$,

$$
F(x) = \int_{-\infty}^{0} c\,e^{2t}\,dt + \int_0^x c\,e^{-2t}\,dt = c - \tfrac{1}{2}c\,e^{-2x}.
$$

Therefore $$\lim_{x \to \infty} F(x) = c = 1$$, so $$c = 1$$. The cumulative distribution function of $$X$$ is

$$
F(x) =
\begin{cases}
\frac{1}{2}e^{2x} & (x < 0) \\
1 - \frac{1}{2}e^{-2x} & (x \ge 0).
\end{cases}
$$

### Exercise 1.10

> **Exercise 1.10.** Find the range of the positive number $$\alpha$$ for which the expectation of $$X$$ exists, i.e. $$E(X) < +\infty$$, when the probability density function of $$X$$ is $$f(x) = \alpha\, x^{-\alpha - 1} I_{(1,\infty)}(x)$$.
{: .problem #hw2-1-10 }

To find the range of the positive number $$\alpha$$ for which $$E(\lvert X\rvert) < \infty$$, by the definition of expectation we need the range of the positive number $$\alpha$$ for which $$\int_{-\infty}^{\infty} \lvert x\rvert f(x)\,dx < \infty$$.

$$
\int_{-\infty}^{\infty} \lvert x\rvert f(x)\,dx = \int_{-\infty}^{1} x \cdot 0\,dx + \lim_{t \to 1+}\int_t^{\infty} x\,(\alpha x^{-\alpha - 1})\,dx = \lim_{t \to 1+}\int_t^{\infty} \alpha\, x^{-\alpha}\,dx.
$$

That is, we need the range of $$\alpha$$ with $$\lim_{t \to 1+}\int_t^{\infty} \alpha x^{-\alpha}\,dx < \infty$$.

If $$\alpha \ne 1$$,

$$
\lim_{t \to 1+}\int_t^{\infty} \alpha x^{-\alpha}\,dx = \lim_{t \to 1+}\Bigl[\frac{\alpha}{1 - \alpha}x^{1-\alpha}\Bigr]_t^{\infty} = \lim_{k \to \infty}\lim_{t \to 1+}\Bigl[\frac{\alpha}{1 - \alpha}x^{1-\alpha}\Bigr]_t^{k}
= \frac{\alpha}{1 - \alpha}\lim_{k \to \infty}k^{1-\alpha} - \frac{\alpha}{1 - \alpha}.
$$

Here, if $$0 < \alpha < 1$$, then $$1 - \alpha > 0$$, so $$\lim_{k \to \infty}k^{1-\alpha} = \infty$$, and if $$\alpha > 1$$, $$\lim_{k \to \infty}k^{1-\alpha} = \lim_{k \to \infty}\frac{1}{k^{\alpha - 1}} = 0$$.

That is, $$\lim_{k \to \infty}k^{1-\alpha}$$ converges only when $$\alpha > 1$$, so only in that range $$\int_{-\infty}^{\infty} \lvert x\rvert f(x)\,dx$$ converges, to $$\frac{\alpha}{\alpha - 1}$$.

Also, if $$\alpha = 1$$, $$\lim_{t \to 1+}\int_t^{\infty}\frac{1}{x}\,dx = \lim_{k \to \infty}\lim_{t \to 1+}(\log k - \log t) = \lim_{k \to \infty}\log k = \infty$$, so $$\int_{-\infty}^{\infty} \lvert x\rvert f(x)\,dx$$ diverges.

Therefore the positive numbers $$\alpha$$ with $$\int_{-\infty}^{\infty} \lvert x\rvert f(x)\,dx < \infty$$ are $$\alpha > 1$$, and only in that case does the random variable $$X$$ have an expectation.

### Exercise 1.11

> **Exercise 1.11.**
>
> - (a) Show that for a random variable $$X$$ and any positive number $$k$$, $$k\,P(X > k) \le E\bigl(X\,I(X > k)\bigr)$$.
> - (b) Show that when a continuous random variable $$X$$ taking the value $$0$$ or positive values has an expectation, i.e. $$E(X) < +\infty$$, $$\lim_{x \to +\infty} x\,P(X > x) = 0$$.
> - (c) Show that when a continuous random variable $$X$$ taking the value $$0$$ or positive values has an expectation and its cumulative distribution function $$F$$ is differentiable at every point, $$EX = \int_0^{+\infty}(1 - F(x))\,dx$$.
{: .problem #hw2-1-11 }

**(a)** For a random variable $$X$$ and any positive number $$k$$ we want to prove the inequality $$k\,P(X > k) \le E(X\,I(X > k))$$. Since $$P(X > k) = E(I(X > k))$$, it suffices to prove $$k\,E(I(X > k)) \le E(X\,I(X > k))$$.

Then $$E(X\,I(X > k)) - k\,E(I(X > k)) = E(X\,I(X > k)) - E(k\,I(X > k)) = E\bigl((X - k)\,I(X > k)\bigr)$$, and for the random variable $$(X - k)\,I(X > k)$$, when $$X > k$$ we have $$X - k \ge 0$$, and when $$X \le k$$ it is $$0 \ge 0$$, so $$(X - k)\,I(X > k) \ge 0$$. Therefore $$E\bigl((X - k)\,I(X > k)\bigr) \ge 0$$, so $$E(X\,I(X > k)) \ge k\,E(I(X > k))$$.

**(b)** For a continuous random variable $$X$$ taking the value $$0$$ or positive values with $$E(X) < \infty$$, we want to show $$\lim_{x \to \infty}x\,P(X > x) = 0$$. By the given condition, $$\int_{-\infty}^{\infty} x f(x)\,dx < \infty$$, and when $$x < 0$$, $$P(X = x) = 0$$, so $$\int_{-\infty}^{\infty} x f(x)\,dx = \int_0^{\infty} x f(x)\,dx < \infty$$. Also, from (a), $$\lim_{x \to \infty} x\,P(X > x) \le \lim_{x \to \infty} E(X\,I(X > x))$$.

Also $$P(X > x) \ge 0$$, and if $$x < 0$$ then $$P(X = x) = 0$$, so $$x\,P(X > x) \ge 0$$ for every real $$x$$, that is, $$\lim_{x \to \infty} x\,P(X > x) \ge 0$$. Therefore it suffices to show $$\lim_{x \to \infty} E(X\,I(X > x)) = 0$$. Let $$a = \int_0^{\infty} x f(x)\,dx$$. Then $$a = \lim_{x \to \infty}\int_0^x t f(t)\,dt < \infty$$, so

$$
\lim_{x \to \infty} E(X\,I(X > x)) = \lim_{x \to \infty}\int_0^{\infty} t f(t)\,I_{(t > x)}\,dt = \lim_{x \to \infty}\int_x^{\infty} t f(t)\,dt
= \lim_{x \to \infty}\Bigl(\int_0^{\infty} t f(t)\,dt - \int_0^{x} t f(t)\,dt\Bigr) = \int_0^{\infty} t f(t)\,dt - \lim_{x \to \infty}\int_0^{x} t f(t)\,dt = a - a = 0.
$$

Therefore $$\lim_{x \to \infty} E(X\,I(X > x)) = 0$$, so $$0 \le \lim_{x \to \infty} x\,P(X > x) \le \lim_{x \to \infty}E(X\,I(X > x)) = 0$$, and so $$\lim_{x \to \infty} x\,P(X > x) = 0$$.

**(c)** For a continuous random variable $$X$$ taking the value $$0$$ or positive values, whose expectation exists and whose cumulative distribution function $$F$$ is differentiable at every point, we want to show $$E(X) = \int_0^{\infty}(1 - F(x))\,dx$$. By (b), $$\lim_{x \to \infty} x\,P(X > x) = 0$$, so $$\lim_{x \to \infty} x\,P(X > x) = \lim_{x \to \infty} x\,(1 - P(X \le x)) = \lim_{x \to \infty} x\,(1 - F(x)) = 0$$.

Then, by integration by parts,

$$
\lim_{x \to \infty}\int_0^{x}\bigl(-t f(t)\bigr)\,dt = \lim_{x \to \infty} x\,(1 - F(x)) - \lim_{x \to \infty}\int_0^{x}(1 - F(t))\,dt = -\int_0^{\infty}(1 - F(t))\,dt.
$$

In other words, $$\int_0^{\infty}(1 - F(t))\,dt = \int_0^{\infty} t f(t)\,dt = E(X)$$.

### Exercise 1.12

> **Exercise 1.12.** Find (a) $$E(X)$$, $$\mathrm{Var}(X)$$ and (b) $$E(2X + 3)$$, $$\mathrm{Var}(2X + 3)$$ when the probability density function of $$X$$ is $$f(x) = \frac{2}{9}(2 - x)(1 + x)\,I_{[-1,2]}(x)$$.
{: .problem #hw2-1-12 }

**(a)** We want $$E(X)$$ and $$\mathrm{Var}(X)$$. These are $$E(X) = \int_{-\infty}^{\infty} x f(x)\,dx$$ and $$\mathrm{Var}(X) = \int_{-\infty}^{\infty}(x - E(X))^2 f(x)\,dx$$.

$$
E(X) = \int_{-\infty}^{\infty} x\cdot\bigl(\tfrac{2}{9}(2 - x)(1 + x)\,I_{[-1,2]}\bigr)dx = \frac{2}{9}\int_{-1}^{2} x(1 + x)(2 - x)\,dx = \frac{2}{9}\Bigl[x^2 + \tfrac{1}{3}x^3 - \tfrac{1}{4}x^4\Bigr]_{-1}^{2} = \frac{1}{2},
$$

and

$$
\mathrm{Var}(X) = \int_{-\infty}^{\infty}\bigl(x - \tfrac{1}{2}\bigr)^2\cdot\tfrac{2}{9}(2 - x)(1 + x)\,I_{[-1,2]}\,dx
= \frac{2}{9}\int_{-1}^{2}\bigl(x - \tfrac{1}{2}\bigr)^2(2 - x)(1 + x)\,dx = \frac{9}{20}.
$$

**(b)** We want $$E(2X + 3)$$ and $$\mathrm{Var}(2X + 3)$$. By the linearity of expectation, $$E(2X + 3) = 2E(X) + 3$$, and by the properties of variance, $$\mathrm{Var}(2X + 3) = 4\,\mathrm{Var}(X)$$. Therefore $$E(2X + 3) = 2E(X) + 3 = 2 \times \frac{1}{2} + 3 = 4$$ and $$\mathrm{Var}(2X + 3) = 4\,\mathrm{Var}(X) = 4 \times \frac{9}{20} = \frac{9}{5}$$.

### Exercise 1.14

> **Exercise 1.14.** For a continuous random variable $$X$$, if there is a unique $$m$$ with $$P(X \le m) = 1/2$$, $$m$$ is called the median of the distribution of $$X$$. For a continuous random variable $$X$$ with a unique median and $$E(\lvert X\rvert) < +\infty$$, show that
>
> $$
> E(\lvert X - a\rvert) = E(\lvert X - m\rvert) + 2\int_m^a (a - x) f(x)\,dx,
> $$
>
> and from this show that the value of $$a$$ minimizing $$E[\lvert X - a\rvert]$$ is the median $$m$$. (Hint: when $$a > m$$, $$\lvert x - a\rvert - \lvert x - m\rvert = (a - m)\{I(x \le m) - I(x > m)\} + 2(a - x)I(m < x \le a)$$.)
{: .problem #hw2-1-14 }

For a continuous random variable with a unique median $$m$$ and $$E(\lvert X\rvert) < \infty$$ we first want to prove $$E(\lvert X - a\rvert) = E(\lvert X - m\rvert) + 2\int_m^a (a - x) f(x)\,dx$$. Let $$f(x)$$ be the probability density function of $$X$$.

Since $$m$$ is unique, $$P(X \le m) = \frac{1}{2}$$ holds for exactly one $$m$$, and:

- when $$a > m$$, $$\lvert x - a\rvert - \lvert x - m\rvert = (a - m)\{I(x \le m) - I(x > m)\} + 2(a - x)\,I(m < x \le a)$$;
- when $$a = m$$, $$\lvert x - a\rvert - \lvert x - m\rvert = \lvert x - m\rvert - \lvert x - m\rvert = 0$$;
- when $$a < m$$, $$\lvert x - a\rvert - \lvert x - m\rvert = (a - m)\{I(x \le m) - I(x > m)\} + 2(x - a)\,I(a < x \le m)$$.

Then, when $$a > m$$,

$$
\begin{aligned}
E(\lvert X - a\rvert) - E(\lvert X - m\rvert) &= \int_{-\infty}^{\infty}\lvert x - a\rvert f(x)\,dx - \int_{-\infty}^{\infty}\lvert x - m\rvert f(x)\,dx \\
&= \int_{-\infty}^{\infty}\bigl(\lvert x - a\rvert - \lvert x - m\rvert\bigr) f(x)\,dx \\
&= \int_{-\infty}^{\infty}\Bigl[(a - m)\{I(x \le m) - I(x > m)\} + 2(a - x)\,I(m < x \le a)\Bigr] f(x)\,dx \\
&= \int_{-\infty}^{m}(a - m) f(x)\,dx - \int_m^{\infty}(a - m) f(x)\,dx + 2\int_m^{a}(a - x) f(x)\,dx.
\end{aligned}
$$

Also, $$P(X \le m) = \int_{-\infty}^{m} f(x)\,dx = \frac{1}{2}$$, so $$\int_m^{\infty} f(x)\,dx = P(X > m) = 1 - P(X \le m) = \frac{1}{2}$$. Hence

$$
E(\lvert X - a\rvert) - E(\lvert X - m\rvert) = \frac{a - m}{2} - \frac{a - m}{2} + 2\int_m^{a}(a - x) f(x)\,dx = 2\int_m^{a}(a - x)\,f(x)\,dx.
$$

When $$a < m$$ also,

$$
\begin{aligned}
E(\lvert X - a\rvert) - E(\lvert X - m\rvert) &= \int_{-\infty}^{\infty}\bigl(\lvert x - a\rvert - \lvert x - m\rvert\bigr) f(x)\,dx
= \int_{-\infty}^{\infty}\Bigl[(a - m)\{I(x \le m) - I(x > m)\} + 2(x - a)\,I(a < x \le m)\Bigr] f(x)\,dx \\
&= \int_{-\infty}^{m}(a - m) f(x)\,dx - \int_m^{\infty}(a - m) f(x)\,dx + 2\int_a^{m}(x - a) f(x)\,dx = \frac{a - m}{2} - \frac{a - m}{2} + 2\int_m^{a}(a - x) f(x)\,dx.
\end{aligned}
$$

When $$a = m$$, $$E(\lvert X - a\rvert) - E(\lvert X - m\rvert) = 0 = 2\int_m^{a}(a - x) f(x)\,dx$$.

Therefore, for every real number $$a$$, $$E(\lvert X - a\rvert) - E(\lvert X - m\rvert) = 2\int_m^{a}(a - x) f(x)\,dx$$, so

$$
E(\lvert X - a\rvert) = E(\lvert X - m\rvert) + 2\int_m^{a}(a - x) f(x)\,dx.
$$

Next we show that the value of $$a$$ minimizing $$E(\lvert X - a\rvert)$$ is the median $$m$$. If the cumulative distribution function of $$X$$ is $$F$$, then since $$E(\lvert X - a\rvert) - E(\lvert X - m\rvert) = 2\int_m^{a}(a - x) f(x)\,dx$$,

$$
\frac{d}{da}E(\lvert X - a\rvert) = \frac{d}{da}\,2\int_m^{a}(a - x) f(x)\,dx = 2\,\frac{d}{da}\Bigl(a\int_m^{a} f(x)\,dx - \int_m^{a} x f(x)\,dx\Bigr)
= 2\Bigl(\int_m^{a} f(x)\,dx + a f(a) - a f(a)\Bigr) = 2\bigl(F(a) - F(m)\bigr).
$$

Here the point with $$F(x) = \frac{1}{2}$$ is unique, namely $$m$$, and since $$F$$ is non-decreasing, for any real number $$x$$ with $$x < m$$, $$F(x) < F(m) = \frac{1}{2}$$, and if $$x > m$$, $$F(x) > F(m) = \frac{1}{2}$$. In other words, $$\frac{d}{da}E(\lvert X - a\rvert) = 2(F(a) - F(m)) = 0$$ holds only at $$a = m$$, and since the derivative is negative for $$a < m$$ and positive for $$a > m$$, $$E(\lvert X - a\rvert)$$ attains its minimum at $$a = m$$.

### Exercise 1.15

> **Exercise 1.15.** Find the moment generating function of $$X$$ when its probability density function is
>
> $$
> f(x) =
> \begin{cases}
> \frac{1}{2}e^{x}, & x < 0 \\
> e^{-2x}, & x > 0.
> \end{cases}
> $$
{: .problem #hw2-1-15 }

When the probability density function $$f$$ of $$X$$ exists and $$f(x) = \frac{1}{2}e^{x}$$ ($$x < 0$$), $$e^{-2x}$$ ($$x > 0$$), we want the moment generating function of $$X$$. Writing $$M_X(t)$$ for it, we check whether there is a positive real number $$h$$ with $$M_X(t) = E(e^{tX}) < \infty$$ for $$\lvert t\rvert < h$$, and then find $$M_X(t)$$.

By the definition of expectation,

$$
M_X(t) = E(e^{tX}) = \int_{-\infty}^{\infty} e^{tx} f(x)\,dx = \int_{-\infty}^{0} e^{tx}\cdot\tfrac{1}{2}e^{x}\,dx + \int_0^{\infty} e^{tx}\cdot e^{-2x}\,dx = \frac{1}{2}\int_{-\infty}^{0} e^{(t+1)x}\,dx + \int_0^{\infty} e^{(t-2)x}\,dx.
$$

For a positive number $$h < 1$$, consider any real number $$t$$ with $$\lvert t\rvert < h$$. Then $$t > -1$$ and $$t < 2$$, so

$$
M_X(t) = \frac{1}{2}\lim_{k \to \infty}\Bigl[\frac{1}{t+1}e^{(t+1)x}\Bigr]_{-k}^{0} + \lim_{k \to \infty}\Bigl[\frac{1}{t-2}e^{(t-2)x}\Bigr]_0^{k}
= \frac{1}{2(t+1)}\lim_{k \to \infty}\Bigl(1 - \frac{1}{e^{(t+1)k}}\Bigr) - \frac{1}{2-t}\lim_{k \to \infty}\Bigl(\frac{1}{e^{(2-t)k}} - 1\Bigr) = \frac{1}{2(t+1)} + \frac{1}{2-t},
$$

which converges. That is, for any real number $$t$$ with $$\lvert t\rvert < h$$ there is a positive number $$h$$ with $$M_X(t) < \infty$$; $$M_X(t)$$ exists for $$\lvert t\rvert < h$$, and the moment generating function is

$$
M_X(t) = \frac{1}{2(t+1)} + \frac{1}{2-t} = \frac{t + 4}{2(t+1)(2-t)}.
$$

### Exercise 1.16

> **Exercise 1.16.** Find the moment generating function, the mean and the variance of $$X$$ when its probability density function is $$f(x) = \frac{1}{2}e^{-\lvert x\rvert}$$, $$-\infty < x < +\infty$$.
{: .problem #hw2-1-16 }

When the probability density function $$f$$ of $$X$$ exists and $$f(x) = \frac{1}{2}e^{-\lvert x\rvert}$$, first we find the moment generating function. Writing $$M_X(t)$$ for it, we check whether there is a positive real number $$h$$ with $$M_X(t) = E(e^{tX}) < \infty$$ for $$\lvert t\rvert < h$$, and then find $$M_X(t)$$.

By the definition of expectation,

$$
M_X(t) = E(e^{tX}) = \int_{-\infty}^{\infty} e^{tx}\Bigl(\frac{1}{2}e^{-\lvert x\rvert}\Bigr)dx = \frac{1}{2}\int_{-\infty}^{0} e^{(t+1)x}\,dx + \frac{1}{2}\int_0^{\infty} e^{(t-1)x}\,dx.
$$

For a positive number $$h < 1$$, consider any real number $$t$$ with $$\lvert t\rvert < h$$. Then $$t > -1$$ and $$t < 1$$, so

$$
M_X(t) = \frac{1}{2}\lim_{k \to \infty}\Bigl[\frac{1}{t+1}e^{(t+1)x}\Bigr]_{-k}^{0} + \frac{1}{2}\lim_{k \to \infty}\Bigl[\frac{1}{t-1}e^{(t-1)x}\Bigr]_0^{k}
= \frac{1}{2(t+1)} + \frac{1}{2(1-t)} = \frac{1}{1 - t^2} < \infty.
$$

That is, for any real number $$t$$ with $$\lvert t\rvert < h$$ there is a positive number $$h$$ with $$M_X(t) < \infty$$; $$M_X(t)$$ exists for $$\lvert t\rvert < h$$, and the moment generating function is $$M_X(t) = \dfrac{1}{1 - t^2}$$.

Now we find the mean and the variance of $$X$$. By the properties of the moment generating function, $$E(X) = \dfrac{d}{dt}M_X(t)\Big\vert_{t=0}$$ and $$E(X^2) = \dfrac{d^2}{dt^2}M_X(t)\Big\vert_{t=0}$$, and by the properties of variance, $$\mathrm{Var}(X) = E(X^2) - (E(X))^2$$. Therefore

$$
E(X) = \frac{d}{dt}\Bigl(\frac{1}{1 - t^2}\Bigr)\Big|_{t=0} = \frac{2t}{(1 - t^2)^2}\Big|_{t=0} = 0,
\qquad
E(X^2) = \frac{d^2}{dt^2}\Bigl(\frac{1}{1 - t^2}\Bigr)\Big|_{t=0} = \frac{2(1 + 3t^2)}{(1 - t^2)^3}\Big|_{t=0} = 2.
$$

Therefore $$E(X) = 0$$ and $$\mathrm{Var}(X) = E(X^2) - (E(X))^2 = 2$$.

### Exercise 1.17

> **Exercise 1.17.** The moment generating function of a random variable $$X$$ is known to exist, and $$E(X^{2r}) = (2r)!/2^r r!$$ ($$r = 1, 2, 3, \dots$$), $$E(X^{2r-1}) = 0$$ ($$r = 1, 2, 3, \dots$$). Find the moment generating function of $$X$$.
{: .problem #hw2-1-17 }

Since the moment generating function of $$X$$ is known to exist, writing $$M_X(t)$$ for it, there is a positive number $$h$$ with $$M_X(t) = \sum_{k=0}^{\infty}\frac{E(X^k)}{k!}t^k$$ for every real number $$t$$ with $$\lvert t\rvert < h$$. Therefore, considering such an $$h$$, for every real $$t$$ with $$\lvert t\rvert < h$$,

$$
M_X(t) = \sum_{k=0}^{\infty}\frac{E(X^k)}{k!}t^k = 1 + \sum_{r=1}^{\infty}\frac{E(X^{2r})}{(2r)!}t^{2r} + \sum_{r=1}^{\infty}\frac{E(X^{2r-1})}{(2r-1)!}t^{2r-1}
= 1 + \sum_{r=1}^{\infty}\frac{1}{(2r)!}\cdot\frac{(2r)!}{2^r r!}t^{2r} + \sum_{r=1}^{\infty}\frac{0}{(2r-1)!}t^{2r-1}
= 1 + \sum_{r=1}^{\infty}\frac{1}{2^r}\cdot\frac{1}{r!}t^{2r} = \sum_{r=0}^{\infty}\frac{1}{r!}\Bigl(\frac{t^2}{2}\Bigr)^r.
$$

Also, $$e^x = \sum_{n=0}^{\infty}\frac{1}{n!}x^n$$, so for every real number $$t$$ with $$\lvert t\rvert < h$$, $$M_X(t) = \sum_{r=0}^{\infty}\frac{1}{r!}\bigl(\frac{t^2}{2}\bigr)^r = e^{t^2/2}$$.

### Example 1.5.6

> **Example 1.5.6.** The probability density function of $$X$$ is $$f(x) = e^{-x}I_{(x>0)}$$ (the standard exponential distribution). Find its moment generating function and its moments.
{: .problem #hw2-p2 }

Let $$f(x) = e^{-x}I_{(x>0)}$$ and let $$M_X(t)$$ be the moment generating function of $$X$$. We want to show $$E(X^k) = k!$$ for every natural number $$k$$.

$$
M_X(t) = E(e^{tX}) = \int_{-\infty}^{\infty} e^{tx} f(x)\,dx = \int_{-\infty}^{\infty} e^{tx}e^{-x}I_{(x>0)}\,dx = \int_0^{\infty} e^{(t-1)x}\,dx.
$$

For a positive number $$h < 1$$, consider any real number $$t$$ with $$\lvert t\rvert < h$$. Then $$t < 1$$, so

$$
M_X(t) = \lim_{k \to \infty}\Bigl[\frac{1}{t-1}e^{(t-1)x}\Bigr]_0^{k} = \frac{1}{t-1}\lim_{k \to \infty}\Bigl(\frac{1}{e^{(1-t)k}} - 1\Bigr) = \frac{1}{1-t} < \infty.
$$

For a positive number $$h$$ satisfying this, for every real number $$t$$ with $$\lvert t\rvert < h$$, $$M_X(t) = \sum_{k=0}^{\infty}\frac{E(X^k)}{k!}t^k$$ and $$M_X(t) = \frac{1}{1-t} = \sum_{k=0}^{\infty}t^k$$, so

$$
\sum_{k=0}^{\infty}\frac{E(X^k)}{k!}t^k = \sum_{k=0}^{\infty}t^k = \sum_{k=0}^{\infty}\frac{k!}{k!}t^k.
$$

Therefore, for every natural number $$k$$, $$\dfrac{E(X^k)}{k!} = \dfrac{k!}{k!}$$, so $$E(X^k) = k!$$.

### Example 1.5.7

> **Example 1.5.7.** The moment generating function of a random variable $$X$$ is known to exist and its moments are $$E(X^k) = 2^k k!$$. Find the moment generating function and the probability density function of $$X$$.
{: .problem #hw2-p3 }

Writing $$M_X(t)$$ for the moment generating function of $$X$$, there is a positive number $$h$$ with $$M_X(t) = \sum_{k=0}^{\infty}\frac{E(X^k)}{k!}t^k$$ for every real number $$t$$ with $$\lvert t\rvert < h$$. Then

$$
M_X(t) = \sum_{k=0}^{\infty}\frac{1}{k!}\cdot 2^k\cdot k!\cdot t^k = \sum_{k=0}^{\infty}(2t)^k,
$$

and if $$h < \frac{1}{2}$$, then $$\lvert 2t\rvert < 1$$, so $$M_X(t) = \sum_{k=0}^{\infty}(2t)^k = \dfrac{1}{1 - 2t}$$.

On the other hand, let a random variable $$Y$$ have the probability density function $$f(x) = \frac{1}{2}e^{-x/2}I_{(x>0)}$$, and let $$M_Y(t)$$ be its moment generating function. Then

$$
M_Y(t) = E(e^{tY}) = \int_{-\infty}^{\infty} e^{tx}f(x)\,dx = \frac{1}{2}\int_0^{\infty} e^{(t - \frac{1}{2})x}\,dx,
$$

and for $$t < \frac{1}{2}$$ this integral converges. That is, for $$t < \frac{1}{2}$$,

$$
M_Y(t) = \frac{1}{2}\Bigl[\frac{1}{t - \frac{1}{2}}e^{(t - \frac{1}{2})x}\Bigr]_0^{\infty} = \frac{1}{1 - 2t}.
$$

Therefore, considering a positive number $$h < \frac{1}{2}$$, for every real number $$t$$ with $$\lvert t\rvert < h$$, $$M_X(t) = M_Y(t) = \dfrac{1}{1 - 2t}$$, so by the uniqueness of the moment generating function, $$f(x)$$ is a probability density function of $$X$$.

### The discontinuities of a CDF

> **Exercise.** Show that the set of discontinuities of a cumulative distribution function $$F$$ is countable.
{: .problem #hw2-p4 }

Let $$F$$ be the cumulative distribution function of a random variable $$X$$, and let $$A \subseteq \mathbb{R}$$ be the set of discontinuities of $$F$$. It suffices to show that $$A$$ is at most countable. By the characterization theorem of the cumulative distribution function, $$F$$ is non-decreasing on the whole real line. In other words, $$F(x) \le F(y)$$ for all $$x < y$$ ($$x, y \in \mathbb{R}$$).

For any element $$k$$ of $$A$$, define $$\lim_{x \to k+}F(x) = F(k+)$$ and $$\lim_{x \to k-}F(x) = F(k-)$$. Since a cumulative distribution function is right-continuous, $$F(k+) = F(k)$$. Also, $$F(x)$$ is discontinuous at $$x = k$$, so $$F(k) \ne F(k-)$$. Then for any real number $$\varepsilon > 0$$, $$k - \varepsilon < k$$, so $$F(k - \varepsilon) \le F(k)$$. Therefore, for every element $$k$$ of $$A$$, $$F(k-) < F(k) = F(k+)$$.

Then, for each element $$k$$, by the denseness of the rational numbers there is a rational number $$r_k \in \mathbb{Q}$$ with $$F(k-) < r_k < F(k+)$$.

Also, for two real elements $$p, q$$ of $$A$$ with $$p < q$$, for any real number $$\varepsilon' > 0$$ with $$p \le q - \varepsilon'$$ we have $$F(p) \le F(q - \varepsilon')$$, so $$F(p) \le F(q-)$$. Hence $$F(p-) < r_p < F(p+) \le F(q-) < r_q < F(q+)$$, so if $$p < q$$, then $$r_p < r_q$$.

Then let the function $$f : p \mapsto r_p$$ ($$\forall p \in A$$). This function $$f$$ is a one-to-one correspondence between $$A$$ and some subset of $$\mathbb{Q}$$, so $$A$$ is equivalent to some subset of $$\mathbb{Q}$$. Therefore, since $$\mathbb{Q}$$ is a countable set, $$A$$ is at most countable.

### Existence of a random variable with a given CDF

> **Exercise.** Let $$F : \mathbb{R} \to (0,1)$$ be nondecreasing, with $$\lim_{x \to -\infty}F(x) = 0$$, $$\lim_{x \to \infty}F(x) = 1$$, right-continuous, and suppose that its inverse $$F^{-1}$$ exists. Show that there is a random variable having $$F$$ as its cumulative distribution function.
{: .problem #hw2-p5 }

Let $$X$$ be a random variable whose cumulative distribution function is

$$
G(x) =
\begin{cases}
0 & (x < 0) \\
x & (0 \le x < 1) \\
1 & (x \ge 1).
\end{cases}
$$

Define a random variable $$Y$$ by $$Y(c) = F^{-1}(X(c))$$ for every element $$c$$ of the sample space $$\mathcal{C}$$; we want to show that its cumulative distribution function is $$F(x)$$. That is, it suffices to show $$F(x) = P(Y \le x)$$.

When $$F$$ satisfies the four given conditions, let $$F(\mathbb{R}) = \{F(x) : x \in \mathbb{R}\}$$ be the range of $$F$$. Then $$F$$ is nondecreasing and $$\lim_{x \to -\infty}F(x) = 0$$, $$\lim_{x \to \infty}F(x) = 1$$, so $$F(\mathbb{R}) \subseteq (0,1)$$. Here $$F$$ is a bijection, so the set $$F(\mathbb{R}) = (0,1)$$.

Also, since the inverse function $$F^{-1}$$ of $$F$$ exists, the function $$F : \mathbb{R} \to F(\mathbb{R})$$ is a one-to-one correspondence. Therefore, for any two real numbers $$x, y$$ with $$x < y$$, $$F(x) \ne F(y)$$, and since $$F$$ is nondecreasing, $$F(x) < F(y)$$. In other words, by the existence of the inverse function, for any real number $$p \in F(\mathbb{R}) = (0,1)$$ there is a unique real number $$t$$ with $$F(t) = p$$.

Therefore, since the cumulative distribution function of $$X$$ is defined on the whole real line, for any real number $$p \in (0,1)$$ there is an element $$c$$ of $$\mathcal{C}$$ with $$X(c) = p$$, and for that $$c$$, $$Y(c) = F^{-1}(X(c)) = F^{-1}(p) = t$$.

Now we prove $$F(x) = P(Y \le x)$$. Then $$P(Y \le x) = P(F^{-1}(X) \le x) = P(X \le F(x)) = G(F(x))$$, and since $$F(\mathbb{R}) = (0,1)$$, $$0 < F(x) < 1$$. Therefore $$P(Y \le x) = G(F(x)) = F(x)$$. That is, the random variable $$Y$$ has the cumulative distribution function $$F(x)$$.

(1) A random variable with the distribution function $$G$$ exists: take $$\mathcal{C} = (0,1)$$ with the uniform probability $$P(dx) = dx$$ and $$X(c) = c$$. (2) $$F^{-1}$$ is defined only on $$(0,1)$$, and $$X$$ takes the values $$0$$ or $$1$$ only with probability $$0$$; $$Y$$ may be defined arbitrarily there (say, $$0$$), which does not affect $$P(Y \le x)$$. (3) The step $$P(F^{-1}(X) \le x) = P(X \le F(x))$$ uses that $$F$$ is strictly increasing: $$F^{-1}(u) \le x \Longleftrightarrow u \le F(x)$$.

### Symmetric distributions

> **Exercise.** If $$X$$ is symmetric about $$\alpha$$ and continuous, show that its density function $$f$$ satisfies $$f(\alpha - x) = f(\alpha + x)$$ for all $$x \in \mathbb{R}$$.
{: .problem #hw2-p6 }

For a continuous random variable $$X$$ that is symmetric about $$\alpha$$ and whose density function $$f$$ exists and is continuous, we want to show $$f(\alpha - x) = f(\alpha + x)$$ for all real $$x$$. By the condition, for all real $$x$$, $$P(X \ge \alpha + x) = P(X \le \alpha - x)$$, so $$1 - P(X < \alpha + x) = P(X \le \alpha - x)$$. In other words, if $$F$$ is the cumulative distribution function of $$X$$, then $$1 - \lim_{t \to (\alpha + x)-}F(t) = F(\alpha - x)$$.

Then, since $$f$$ is continuous, $$F$$ is also continuous, and therefore $$\lim_{t \to (\alpha + x)-}F(t) = F(\alpha + x)$$. That is, $$1 - F(\alpha + x) = F(\alpha - x)$$, and since $$F(x) = \int_{-\infty}^{x}f(t)\,dt$$, differentiating both sides gives $$-f(\alpha + x) = -f(\alpha - x)$$. That is, for all real $$x$$, $$f(\alpha + x) = f(\alpha - x)$$.

If $$f$$ is not assumed continuous, a density is determined only up to a set of probability $$0$$, so the same computation (with $$F' = f$$ almost everywhere) gives $$f(\alpha + x) = f(\alpha - x)$$ for almost every $$x$$.

## Exercises 1.18 to 1.25

### Exercise 1.18

> **Exercise 1.18.** The moment generating function of a random variable $$X$$ is known to exist, and the $$k$$-th moment is $$m_k = \frac{1}{3}k!\,\{2 + (-1/2)^k\}$$ ($$k = 1, 2, \dots$$). Find (a) the probability density function of $$X$$ and (b) the $$r$$-th cumulant ($$r = 1, 2, \dots$$) of $$X$$.
{: .problem #hw3-1-18 }

**(a)** Let $$f_X$$ be the probability density function of $$X$$. By the uniqueness of the moment generating function, the probability distribution of a random variable $$Y$$ having the same moment generating function as $$X$$ is the same as that of $$X$$.

The moment generating function $$M_X(t)$$ of $$X$$ exists and its $$k$$-th moment is $$m_k = \frac{1}{3}k!\,(2 + (-\frac{1}{2})^k)$$ ($$k = 1, 2, \dots$$), so by the properties of the moment generating function,

$$
M_X(t) = \sum_{k=0}^{\infty}\frac{E(X^k)}{k!}t^k = \sum_{k=0}^{\infty}\frac{1}{k!}m_k t^k = \sum_{k=0}^{\infty}\frac{1}{3}\bigl(2 + (-\tfrac{1}{2})^k\bigr)t^k = \sum_{k=0}^{\infty}\Bigl(\tfrac{2}{3}t^k + \tfrac{1}{3}\bigl(-\tfrac{t}{2}\bigr)^k\Bigr).
$$

The range of $$t$$ in which $$M(t)$$ exists is $$-1 < t < 1$$. Then, for $$-1 < t < 1$$, by the formula for the sum of an infinite geometric series,

$$
M_X(t) = \frac{2/3}{1 - t} + \frac{1/3}{1 - (-t/2)} = \frac{2}{3}\Bigl(\frac{1}{1 - t} + \frac{1}{2 + t}\Bigr).
$$

Now suppose that a random variable $$Y$$ has a probability density function $$f_Y$$ with $$f_Y(y) = \frac{2}{3}e^{-y}I_{(y>0)} + \frac{2}{3}e^{2y}I_{(y<0)}$$, and let its moment generating function be $$M_Y(t)$$. Then $$M_Y(t) = E(e^{tY}) = \int_{-\infty}^{\infty}e^{ty}f_Y(y)\,dy = \int_0^{\infty}\frac{2}{3}e^{(t-1)y}\,dy + \int_{-\infty}^{0}\frac{2}{3}e^{(t+2)y}\,dy$$, so for $$-1 < t < 1$$,

$$
M_Y(t) = \frac{2/3}{1 - t} + \frac{2/3}{t + 2} = M_X(t).
$$

Therefore, for $$-1 < t < 1$$, the moment generating functions of $$X$$ and $$Y$$ are the same, so the probability distributions of $$X$$ and $$Y$$ are the same, and the probability density function of $$Y$$ can serve as that of $$X$$. That is,

$$
f_X(x) = \tfrac{2}{3}e^{-x}I_{(x>0)} + \tfrac{2}{3}e^{2x}I_{(x<0)}.
$$

**(b)** Let the $$r$$-th cumulant of $$X$$ be $$C_r$$. By the definition and properties of the cumulant generating function, writing $$C_X(t)$$ for the cumulant generating function of $$X$$, $$\log M_X(t) = C_X(t) = \sum_{r=0}^{\infty}\frac{C_r}{r!}t^r$$. Therefore, if we find the power series of $$\log M_X(t)$$, we know $$C_r$$.

For $$-1 < t < 1$$,

$$
\log M_X(t) = \log\frac{2}{3}\Bigl(\frac{1}{1-t} + \frac{1}{2+t}\Bigr) = \log\frac{2}{(1-t)(2+t)} = \log 2 - \log(1-t) - \log(2+t).
$$

Also, $$\frac{1}{1-t} = \sum_{r=0}^{\infty}t^r$$, so by the basic theorem of power series, $$-\log(1-t) = \sum_{r=0}^{\infty}\frac{1}{r+1}t^{r+1}$$ ($$-1 < t < 1$$). Therefore

$$
\log M_X(t) = \log 2 - \log(1-t) - \log(2+t) = -\log(1-t) - \log\bigl(1 + \tfrac{1}{2}t\bigr)
= \sum_{r=0}^{\infty}\frac{1}{r+1}t^{r+1} + \sum_{r=0}^{\infty}\frac{1}{r+1}\Bigl(-\frac{t}{2}\Bigr)^{r+1}
= \sum_{r=0}^{\infty}\frac{1}{r+1}\Bigl(1 + \bigl(-\tfrac{1}{2}\bigr)^{r+1}\Bigr)t^{r+1} = \sum_{r=1}^{\infty}\frac{1}{r}\Bigl(1 + \bigl(-\tfrac{1}{2}\bigr)^{r}\Bigr)t^{r}.
$$

Therefore $$C_0 = 0$$, and for every $$r \ge 1$$, $$\dfrac{C_r}{r!} = \dfrac{1}{r}\bigl(1 + (-\tfrac{1}{2})^r\bigr)$$, so

$$
C_r = (r-1)!\,\Bigl(1 + \bigl(-\tfrac{1}{2}\bigr)^r\Bigr).
$$

### Exercise 1.19

> **Exercise 1.19.** From the relation between the moments $$m_r(Z)$$ and the cumulants $$c_r(Z)$$ of the standardized random variable $$Z = (X - \mu)/\sigma$$, show that
>
> $$
> c_3(Z) = m_3(Z), \qquad c_4(Z) = m_4(Z) - 3.
> $$
>
> The third cumulant $$c_3(Z) = E\bigl[\bigl(\frac{X - \mu}{\sigma}\bigr)^3\bigr]$$ and the fourth cumulant $$c_4(Z) = E\bigl[\bigl(\frac{X - \mu}{\sigma}\bigr)^4\bigr] - 3$$ of $$Z$$ are called the skewness and the kurtosis of $$X$$ respectively.
{: .problem #hw3-1-19 }

First, let us express the relation between the moments $$m_r(Z)$$ and the cumulants $$C_r(Z)$$ of the standardized random variable $$Z = \frac{X - \mu}{\sigma}$$. Then $$E(Z) = E\bigl(\frac{X - \mu}{\sigma}\bigr) = \frac{1}{\sigma}(E(X) - \mu) = 0$$ and $$\mathrm{Var}(Z) = \mathrm{Var}\bigl(\frac{X - \mu}{\sigma}\bigr) = \frac{1}{\sigma^2}\mathrm{Var}(X) = 1$$.

Therefore $$m_0(Z) = 1$$, $$m_1(Z) = 0$$, $$m_2(Z) = E(Z^2) = \mathrm{Var}(Z) + (E(Z))^2 = 1$$, and $$C_0(Z) = 0$$. Also, for every natural number $$k \ge 2$$, $$C_k(Z) = m_k(Z) - \sum_{j=1}^{k-1}\binom{k-1}{j}C_{k-j}m_j$$. Since $$C_1(Z) = m_1(Z)$$, $$C_1(Z) = 0$$, and $$C_2(Z) = m_2(Z) - \binom{1}{1}C_1(Z)m_1(Z) = m_2(Z) = 1$$.

Also, for every natural number $$k \ge 1$$, $$m_k(Z) = \sum_{j=0}^{k-1}\binom{k-1}{j}C_{k-j}m_j$$, so

$$
m_3(Z) = \tbinom{2}{0}C_3(Z)m_0(Z) + \tbinom{2}{1}C_2(Z)m_1(Z) + \tbinom{2}{2}C_1(Z)m_2(Z) = C_3(Z) + 2 \times C_2(Z) \times 0 + 1 \times 0 \times m_2(Z) = C_3(Z).
$$

Moreover,

$$
m_4(Z) = \tbinom{3}{0}C_4(Z)m_0(Z) + \tbinom{3}{1}C_3(Z)m_1(Z) + \tbinom{3}{2}C_2(Z)m_2(Z) + \tbinom{3}{3}C_1(Z)m_3(Z) = C_4(Z) + 3C_2(Z)m_2(Z) = C_4(Z) + 3.
$$

Therefore $$m_3(Z) = C_3(Z)$$ and $$C_4(Z) = m_4(Z) - 3$$.

### Exercise 1.20

> **Exercise 1.20.** From the relation between the cumulant generating function of the standardized random variable $$Z = (X - \mu)/\sigma$$ and that of $$X$$, show that the following relation holds between the cumulants of $$Z$$ and those of $$X$$:
>
> $$
> c_r\Bigl(\frac{X - \mu}{\sigma}\Bigr) = c_r(X)/\sigma^r \quad (r = 3, 4, \dots).
> $$
{: .problem #hw3-1-20 }

Let us express the relation between the cumulant generating function of the standardized random variable $$Z = \frac{X - \mu}{\sigma}$$ and that of $$X$$. Assuming that the cumulant generating functions of the two random variables exist, for some positive real number $$h_1$$, $$C_X(t) = \log M_X(t) = \log E(e^{tX})$$ for $$t \in (-h_1, h_1)$$, and for some positive real number $$h_2$$, for $$t \in (-h_2, h_2)$$,

$$
C_Z(t) = \log M_Z(t) = \log E(e^{tZ}) = \log E\bigl(e^{t\frac{X - \mu}{\sigma}}\bigr) = \log\Bigl(e^{-\frac{t\mu}{\sigma}}E\bigl(e^{\frac{t}{\sigma}X}\bigr)\Bigr) = -\frac{t\mu}{\sigma} + \log E\bigl(e^{(t/\sigma)X}\bigr).
$$

That is, letting $$h = \min(\sigma h_1, h_2)$$, for $$t \in (-h, h)$$, $$C_Z(t) = -\frac{t\mu}{\sigma} + C_X\bigl(\frac{t}{\sigma}\bigr)$$. Then, by the definition of the cumulant generating function, $$C_Z(t) = \sum_{k=0}^{\infty}\frac{C_k(Z)}{k!}t^k$$ and $$C_X(t) = \sum_{k=0}^{\infty}\frac{C_k(X)}{k!}t^k$$, so

$$
\sum_{k=0}^{\infty}\frac{C_k(Z)}{k!}t^k = -\frac{t\mu}{\sigma} + \sum_{k=0}^{\infty}\frac{C_k(X)}{k!}\Bigl(\frac{t}{\sigma}\Bigr)^k = -\frac{t\mu}{\sigma} + \sum_{k=0}^{\infty}\frac{1}{k!}\cdot\frac{C_k(X)}{\sigma^k}t^k.
$$

Therefore, for every natural number $$r \ge 3$$, $$C_r(Z) = \dfrac{C_r(X)}{\sigma^r}$$.

### Exercise 1.21

> **Exercise 1.21.** When the moment generating function of a random variable $$X$$ is $$M(t) = (1 - t)^{-3}$$, $$t < 1$$, find the skewness and the kurtosis of $$X$$ defined in Exercise 1.19.
{: .problem #hw3-1-21 }

Let us find the skewness and the kurtosis of $$X$$ through the cumulant generating function of the standardized $$X$$. The expectation of $$X$$ is $$E(X) = \frac{d}{dt}M(t)\big\vert_{t=0} = 3$$, and the variance of $$X$$ is $$\mathrm{Var}(X) = E(X^2) - (E(X))^2 = \frac{d^2}{dt^2}M(t)\big\vert_{t=0} - 9 = 12 - 9 = 3$$.

Therefore, letting $$Z$$ be the standardized $$X$$, $$Z = \frac{X - 3}{\sqrt{3}}$$. By Exercise 1.20, if the cumulant generating function of $$X$$ is $$C_X(t)$$ and that of $$Z$$ is $$C_Z(t)$$, $$C_Z(t) = C_X\bigl(\frac{1}{\sqrt{3}}t\bigr) - \frac{3}{\sqrt{3}}t = C_X\bigl(\frac{1}{\sqrt{3}}t\bigr) - \sqrt{3}\,t$$, and $$C_X(t) = \log M(t) = -3\log(1 - t)$$ ($$t < 1$$). Organizing this, $$C_Z(t) = -3\log\bigl(1 - \frac{t}{\sqrt{3}}\bigr) - \sqrt{3}\,t$$ ($$t < \sqrt{3}$$).

The skewness and the kurtosis of $$X$$ are $$c_3(Z) = \frac{d^3}{dt^3}C_Z(t)\big\vert_{t=0}$$ and $$c_4(Z) = \frac{d^4}{dt^4}C_Z(t)\big\vert_{t=0}$$ respectively, so

$$
c_3(Z) = \frac{6}{(\sqrt{3} - 0)^3} = \frac{2\sqrt{3}}{3}, \qquad c_4(Z) = \frac{6 \cdot 3}{(\sqrt{3} - 0)^4} = 2.
$$

### Exercise 1.22

> **Exercise 1.22.** Find the skewness and the kurtosis of $$X$$ defined in Exercise 1.19 when its probability density function is
>
> - (a) $$f(x) = e^{-x}I_{(0,+\infty)}(x)$$
> - (b) $$f(x) = \frac{1}{2}e^{-\lvert x\rvert}$$, $$-\infty < x < +\infty$$
{: .problem #hw3-1-22 }

**(a)** Let $$Z$$ be the standardized random variable of $$X$$. By the relation between the probability density function and the moment generating function, writing $$M_X(t)$$ for the moment generating function of $$X$$ and $$C_X(t)$$ for its cumulant generating function,

$$
M_X(t) = E(e^{tX}) = \int_{-\infty}^{\infty}e^{tx}f(x)\,dx = \int_{-\infty}^{\infty}e^{tx}e^{-x}I_{(0,\infty)}\,dx = \int_0^{\infty}e^{(t-1)x}\,dx = \frac{1}{1-t},
$$

and $$M_X(t)$$ is defined on $$-1 < t < 1$$. Then $$C_X(t) = \log M_X(t) = -\log(1 - t)$$ ($$-1 < t < 1$$), and for $$-1 < t < 1$$, $$-\log(1-t) = \sum_{r=1}^{\infty}\frac{1}{r}t^r = \sum_{r=1}^{\infty}\frac{(r-1)!}{r!}t^r$$, so $$C_X(t) = \sum_{r=1}^{\infty}\frac{(r-1)!}{r!}t^r$$ ($$-1 < t < 1$$).

Then, for a natural number $$r \ge 1$$, letting the $$r$$-th cumulant of $$X$$ be $$C_r(X)$$, $$C_r(X) = (r-1)!$$. Also $$\sigma^2 = \frac{d^2}{dt^2}M_X(t)\big\vert_{t=0} - \bigl\{\frac{d}{dt}M_X(t)\big\vert_{t=0}\bigr\}^2$$, so $$\sigma^2 = \frac{2}{(1-0)^3} - \bigl(\frac{1}{(1-0)^2}\bigr)^2 = 1$$. Therefore, for a natural number $$r \ge 3$$, letting the $$r$$-th cumulant of $$Z$$ be $$C_r(Z)$$, $$C_r(Z) = \dfrac{C_r(X)}{\sigma^r} = \dfrac{C_r(X)}{1^r} = C_r(X)$$, so $$C_3(Z) = C_3(X) = 2! = 2$$ and $$C_4(Z) = C_4(X) = 3! = 6$$. That is, the skewness of $$X$$ is $$2$$ and the kurtosis is $$6$$.

**(b)** Let $$Z$$ be the standardized random variable of $$X$$. Writing $$M_X(t)$$ for the moment generating function of $$X$$ and $$C_X(t)$$ for its cumulant generating function,

$$
M_X(t) = E(e^{tX}) = \int_{-\infty}^{\infty}e^{tx}f(x)\,dx = \frac{1}{2}\int_{-\infty}^{\infty}e^{tx}e^{-\lvert x\rvert}\,dx = \frac{1}{2}\Bigl(\int_{-\infty}^{0}e^{(t+1)x}\,dx + \int_0^{\infty}e^{(t-1)x}\,dx\Bigr) = \frac{1/2}{1+t} + \frac{1/2}{1-t} = \frac{1}{1 - t^2},
$$

and $$M_X(t)$$ is defined on $$-1 < t < 1$$. Then $$C_X(t) = \log M_X(t) = -\log(1 - t^2)$$ ($$-1 < t < 1$$), and for $$-1 < t < 1$$, $$-\log(1 - t^2) = \sum_{r=1}^{\infty}\frac{1}{r}t^{2r} = \sum_{r=1}^{\infty}\frac{2\cdot(2r-1)!}{(2r)!}t^{2r}$$, so

$$
C_X(t) = \sum_{r=1}^{\infty}\frac{2\,(2r-1)!}{(2r)!}t^{2r} + \sum_{r=1}^{\infty}\frac{0}{(2r-1)!}t^{2r-1} \qquad (-1 < t < 1).
$$

Then, for a natural number $$r \ge 1$$, letting the $$r$$-th cumulant of $$X$$ be $$C_r(X)$$, if $$r$$ is even, $$C_r(X) = 2(r-1)!$$, and if $$r$$ is odd, $$C_r(X) = 0$$. Also $$\sigma^2 = \frac{d^2}{dt^2}M_X(t)\big\vert_{t=0} - \bigl\{\frac{d}{dt}M_X(t)\big\vert_{t=0}\bigr\}^2 = 2 - 0 = 2$$. Therefore, for a natural number $$r \ge 3$$, $$C_r(Z) = \dfrac{C_r(X)}{\sigma^r} = \dfrac{C_r(X)}{\sqrt{2}^{\,r}}$$, so $$C_3(Z) = \dfrac{C_3(X)}{\sqrt{2}^{\,3}} = \dfrac{0}{2\sqrt{2}} = 0$$ and $$C_4(Z) = \dfrac{C_4(X)}{\sqrt{2}^{\,4}} = \dfrac{2\cdot 3!}{4} = 3$$. That is, the skewness of $$X$$ is $$0$$ and the kurtosis is $$3$$.

### Exercise 1.23

> **Exercise 1.23.** For a random variable $$X$$ taking positive values, write the correct inequality sign in the parentheses.
>
> - (a) $$E(-\log X)\ (\quad)\ -\log EX$$
> - (b) $$EX^r\ (\quad)\ (EX)^r$$ ($$0 < r < 1$$)
{: .problem #hw3-1-23 }

**(a)** For a random variable $$X$$ taking positive values, let the function $$\phi(x)$$ be $$\phi(x) = -\log x$$. Then for any two real numbers $$x, y \in (0,\infty)$$ with $$x < y$$, $$\phi'(x) = -\frac{1}{x} < -\frac{1}{y} = \phi'(y)$$, so by the theorem, $$\phi(x)$$ is strictly convex on the interval $$(0,\infty)$$. Then, by Jensen's inequality, $$-\log E(X) \le E(-\log X)$$, that is,

$$
E(-\log X)\ \ge\ -\log E(X).
$$

**(b)** For a random variable $$X$$ taking positive values, let the function $$\phi(x)$$ be $$\phi(x) = x^r$$ ($$0 < r < 1$$). Then for any two real numbers $$x, y \in (0,\infty)$$ with $$x < y$$, $$\phi'(x) = r x^{r-1} > r y^{r-1} = \phi'(y)$$, so by the theorem, $$\phi(x)$$ is strictly concave on the interval $$(0,\infty)$$. Then, by Jensen's inequality, $$\{E(X)\}^r \ge E(X^r)$$, that is,

$$
E(X^r)\ \le\ (E(X))^r.
$$

### Exercise 1.24

> **Exercise 1.24.** When the moment generating function $$mgf_X(t)$$ of a random variable $$X$$ exists for $$-h < t < h$$ ($$h > 0$$), show that
>
> $$
> P(X \ge a) \le e^{-at}\,mgf_X(t) \quad \forall t : 0 \le t < h, \qquad
> P(X \le a) \le e^{-at}\,mgf_X(t) \quad \forall t : -h < t \le 0.
> $$
{: .problem #hw3-1-24 }

First we prove $$P(X \ge a) \le e^{-at}\,mgf_X(t)$$ for all $$t$$ with $$0 \le t < h$$. For any positive real number $$t$$ with $$0 < t < h$$, $$P(X \ge a) = P(tX \ge ta)$$, and since the function $$e^x$$ is a one-to-one correspondence, $$P(X \ge a) = P(e^{tX} \ge e^{ta})$$. Here $$e^{tX}$$ is a random variable taking only positive values, so by Markov's inequality, $$P(e^{tX} \ge e^{ta}) \le \frac{1}{e^{ta}}E(e^{tX})$$. That is, we can show $$P(X \ge a) \le e^{-ta}\,mgf_X(t)$$ for all $$t$$ with $$0 < t < h$$. Also, when $$t = 0$$, $$e^{-a\cdot 0}mgf_X(0) = 1 \ge P(X \ge a)$$ holds trivially by the axioms of probability, so for any real number $$t$$ with $$0 \le t < h$$, $$P(X \ge a) \le e^{-at}\,mgf_X(t)$$.

Conversely, this time we prove $$P(X \le a) \le e^{-at}\,mgf_X(t)$$ for all $$t$$ with $$-h < t \le 0$$. When $$t = 0$$ it holds as above. For any real number $$t$$ with $$-h < t < 0$$, $$P(X \le a) = P(tX \ge ta) = P(e^{tX} \ge e^{ta})$$. Thinking as above, by Markov's inequality, $$P(X \le a) \le e^{-at}\,mgf_X(t)$$ for all $$t$$ with $$-h < t < 0$$. Therefore, for any real number $$t$$ with $$-h < t \le 0$$, $$P(X \le a) \le e^{-at}\,mgf_X(t)$$.

### Exercise 1.25

> **Exercise 1.25.** The moment generating function $$mgf_X(t)$$ of a random variable $$X$$ exists for every real number $$t$$, and $$mgf_X(t) = \dfrac{e^t - e^{-t}}{2t}$$ ($$t \ne 0$$), $$mgf_X(0) = 1$$. Show that $$P(-1 < X < 1) = 1$$.
{: .problem #hw3-1-25 }

The moment generating function $$mgf_X(t)$$ of the random variable $$X$$ exists for every real number $$t$$, and $$mgf_X(t) = \frac{e^t - e^{-t}}{2t}$$ ($$t \ne 0$$), $$1$$ ($$t = 0$$). We want to show $$P(-1 < X < 1) = 1$$ through $$P(X \ge 1) = 0$$ and $$P(X \le -1) = 0$$.

By the theorem of Exercise 1.24, $$P(X \ge 1) \le e^{-t}\,mgf_X(t)$$ for all $$t > 0$$. Therefore

$$
P(X \ge 1) \le \inf_{t>0}e^{-t}\,mgf_X(t) = \inf_{t>0}\frac{1}{2t}\bigl(1 - e^{-2t}\bigr),
$$

and letting $$f(t) = \frac{1}{2t}(1 - e^{-2t})$$, $$f'(t) = \frac{1}{2t^2}\{(2t + 1)e^{-2t} - 1\}$$, so $$f'(t) < 0$$ for $$t > 0$$. Therefore, since $$f(t)$$ is strictly decreasing on the interval $$(0,\infty)$$,

$$
\inf_{t>0}e^{-t}\,mgf_X(t) = \lim_{t \to \infty}\frac{1}{2t}\bigl(1 - e^{-2t}\bigr) = 0.
$$

That is, $$P(X \ge 1) \le 0$$, so $$P(X \ge 1) = 0$$.

In a similar way, $$P(X \le -1) \le e^{t}\,mgf_X(t)$$ for all $$t < 0$$. Then $$P(X \le -1) \le \inf_{t<0}e^{t}\,mgf_X(t) = \inf_{t<0}\frac{1}{2t}\bigl(e^{2t} - 1\bigr)$$, and letting $$f(t) = \frac{1}{2t}(e^{2t} - 1)$$, $$f'(t) = \frac{(2t - 1)e^{2t} + 1}{2t^2}$$, so $$f'(t) > 0$$ for $$t < 0$$. Therefore $$f$$ is strictly increasing on the interval $$(-\infty, 0)$$, so

$$
\inf_{t<0}f(t) = \lim_{t \to -\infty}f(t) = \lim_{t \to -\infty}\frac{e^{2t} - 1}{2t} = 0.
$$

That is, $$P(X \le -1) \le 0$$, so $$P(X \le -1) = 0$$, and combining with the above,

$$
P(-1 < X < 1) = 1 - P(X \le -1) - P(X \ge 1) = 1 - 0 - 0 = 1.
$$
## References

- 김우철, *수리통계학* (Mathematical Statistics), revised 2nd edition, 민영사, 2021 — Chapter 1 exercises and Examples 1.1.2, 1.5.6, 1.5.7. The exercise statements are translated from the book.
- Mathematical Statistics 1 (326.311), Seoul National University, Spring 2025. Instructor: Jaeyong Lee (이재용).
- The answers are mine, translated into English.

[Overview](/posts/mathstat1-overview/) · [Chapter 2 Exercises](/posts/mathstat1-exercises-chapter-2/)
