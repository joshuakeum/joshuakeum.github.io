---
title: "Mathematical Statistics 1: Course Overview"
date: 2026-11-21 08:00:00 +0900
categories: [Study Notes, Mathematical Statistics 1]
tags: [overview, mathematical statistics, probability, random variables, distributions]
description: Course information, scope, contents and notation for Mathematical Statistics 1, Spring 2025.
math: true
mermaid: false
render_with_liquid: false
---

## Course information

| Item | Detail |
|---|---|
| Course | Mathematical Statistics 1, 326.311 |
| Institution | Seoul National University |
| Semester | Spring 2025 |
| Instructor | Jaeyong Lee (이재용) |
| Credits | 3 |
| Textbook | 김우철, *수리통계학* (Mathematical Statistics), revised 2nd edition, 민영사, 2021 |

## Scope

The notes cover three chapters of the textbook: Chapter 1, the probability distribution of a single random variable; Chapter 2, probability distributions of several random variables; and Chapter 3, the standard families of distributions. Chapters 1 and 2 are written up here; Chapter 3 is not yet.

The course starts from the definition of probability on a $$\sigma$$-field, with a measure-theoretic flavor that the textbook leaves out: why a $$\sigma$$-field is needed, what a random variable is as a measurable function, and why a cumulative distribution function determines a distribution. It then develops expectation and generating functions, and ends the chapter with the inequalities used throughout statistics.

## How these notes are organized

These are my handwritten lecture notes, translated into English, with the exercises I solved for the course.

- **Wording.** The translation keeps my wording.
- **Textbook.** The textbook is used only where my notes leave something out. Such material is collected at the end of each post under "Supplement from the textbook" and is a translation of the book, not my own writing.
- **Exercises.** The exercises of each chapter are in a separate post, with my answers translated as I wrote them.
- **Sections.** Each section of Chapter 1 in my notes is its own post. The notes number their sections $$1$$ to $$5$$ and then number subsections inside them; the textbook's own numbering ($$1.1$$ to $$1.6$$) is given at the top of each post.

## Chapter contents

**Chapter 1 — Probability Distributions**

- [Part 1 — Definition of Probability](/posts/mathstat1-definition-of-probability/): sample space and events, $$\sigma$$-fields, probability, its properties and continuity.
- [Part 2 — Conditional Probability and Independence](/posts/mathstat1-conditional-probability/): conditional probability, the multiplication rule, total probability, Bayes' theorem, independence of events.
- [Part 3 — Random Variables, CDFs and Density Functions](/posts/mathstat1-random-variables-cdf/): random variables and their distributions, the CDF and its characterization, discrete and continuous random variables.
- [Part 4 — Expectation, Moments and Generating Functions](/posts/mathstat1-expectation-mgf/): expectation, variance, skewness and kurtosis, moment generating and cumulant generating functions.
- [Part 5 — Inequalities](/posts/mathstat1-inequalities/): convex functions, AM–GM, Liapounov, Markov, Chebyshev and Jensen, importance sampling, the Cramér–Chernoff method.
- [Chapter 1 Exercises](/posts/mathstat1-exercises-chapter-1/): textbook exercises 1.1 to 1.5, 1.7 to 1.12, 1.14 to 1.25, inclusion–exclusion and Bonferroni's inequality, Examples 1.1.2, 1.5.6 and 1.5.7, and problems on distribution functions.

**Chapter 2 — Probability Distributions of Several Random Variables**

My notes for this chapter cover conditional distributions only (section 3). The other sections are translated from the textbook and say so at the top.

- [Part 1 — Distribution of Two Random Variables](/posts/mathstat1-joint-distribution/): joint and marginal densities, the joint CDF. *(textbook §2.1)*
- [Part 2 — Characteristics of a Joint Distribution](/posts/mathstat1-joint-characteristics/): covariance, correlation, joint moments and the joint moment generating function. *(textbook §2.2)*
- [Part 3 — Conditional Distribution and Expectation](/posts/mathstat1-conditional-distribution/): conditional density, conditional expectation, best predictor, EVVE, linear prediction. *(my notes, with §2.3 supplement)*
- [Part 4 — Independence of Random Variables](/posts/mathstat1-independence/): independence, products and sums of independent variables. *(textbook §2.4)*
- [Part 5 — Multivariate Random Variables](/posts/mathstat1-multivariate/): mean vector, variance matrix, multivariate mgf, conditional distributions, independence of several variables. *(textbook §2.5)*
- [Chapter 2 Exercises](/posts/mathstat1-exercises-chapter-2/): textbook exercises 2.1 to 2.17.

**Chapter 3 — Various Distributions** (not yet written up)

## Notation

| Symbol | Meaning |
|---|---|
| $$\mathcal{C}$$ | the sample space (the textbook writes $$S$$) |
| $$\mathbb{B}$$ | a $$\sigma$$-field on $$\mathcal{C}$$; the Borel $$\sigma$$-field when $$\mathcal{C} = \mathbb{R}$$ |
| $$P$$, $$P_X$$ | the probability, and the distribution of $$X$$: $$P_X(B) = P(X \in B)$$ |
| $$F_X$$, $$f$$ | the cumulative distribution function and the density function |
| $$E$$, $$\mathrm{Var}$$, $$\mathrm{Sd}$$ | expectation, variance and standard deviation |
| $$M_X$$, $$C_X$$ | the moment generating and the cumulant generating function |
| $$I_A$$ | the indicator function of $$A$$ |
| w.p. $$1$$ | with probability $$1$$ |

## Key takeaways

**A probability is a measure with total mass 1.** Everything in Chapter 1 comes from three axioms and from the continuity of probability, which is countable additivity in disguise.

**A distribution is determined by its CDF.** This is why the course moves from probabilities of arbitrary sets to the single function $$F_X(x) = P(X \le x)$$, which is non-decreasing, right-continuous and has limits $$0$$ and $$1$$, and which every such function arises from.

**Expectation needs absolute integrability.** The Cauchy distribution shows that a perfectly good density can have no mean; this is why the definitions carry the condition $$\int \lvert x\rvert f(x)\,dx < \infty$$.

**Generating functions turn moments into derivatives.** If the moment generating function exists near $$0$$, all moments exist, it determines the distribution, and its logarithm gives the cumulants.

**Tail bounds come from one idea.** Markov, Chebyshev and Chernoff are all the same step: apply a non-decreasing function to both sides of $$X \ge t$$ and take expectations.
