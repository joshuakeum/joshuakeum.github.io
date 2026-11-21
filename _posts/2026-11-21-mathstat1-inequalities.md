---
title: "Mathematical Statistics 1: Ch. 1 Part 5 — Inequalities"
date: 2026-11-21 08:50:00 +0900
categories: [Study Notes, Mathematical Statistics 1]
tags: [inequalities, jensen, chebyshev, importance sampling, chernoff]
description: Convex functions, the arithmetic–geometric mean inequality, Liapounov, Markov, Chebyshev and Jensen inequalities, importance sampling and the Cramér–Chernoff method. Chapter 1, notes section 5 of Mathematical Statistics 1.
math: true
mermaid: false
render_with_liquid: false
---

> My handwritten notes, translated into English. Section 5 of Chapter 1 in my notes. It corresponds to §1.6 of the textbook; sections 5.6 and 5.7 (importance sampling and the Cramér–Chernoff method) go beyond the textbook. Statements and proofs follow my notes. Material taken from the textbook is collected at the end under "Supplement from the textbook".
{: .prompt-info }

## 5.1 Convex functions

> **Definition (Convex function).**
>
> - (1) A function $$\phi : (a,b) \to \mathbb{R}$$ is called *convex* if $$\phi(\alpha x + (1 - \alpha) y) \le \alpha\phi(x) + (1 - \alpha)\phi(y)$$ for all $$a \le x < y \le b$$ and all $$\alpha \in (0,1)$$. If "$$<$$" holds in the inequality above, $$\phi$$ is called *strictly convex*.
> - (2) If $$-\phi$$ is (strictly) convex, $$\phi$$ is called (strictly) *concave*.
{: .definition #def-convex }

(Figure: the chord from $$(x, \phi(x))$$ to $$(y, \phi(y))$$ lies above the graph; at $$t = \alpha x + (1 - \alpha) y$$ it has height $$\alpha\phi(x) + (1 - \alpha)\phi(y)$$ while the graph has height $$\phi(\alpha x + (1 - \alpha)y)$$; $$t$$ divides $$[x,y]$$ in the ratio $$(1 - \alpha) : \alpha$$.)

**Note.** Inequalities equivalent to convexity ($$t = \alpha x + (1 - \alpha) y$$). Write $$s_1 = \frac{\phi(y) - \phi(t)}{y - t}$$, $$s_2 = \frac{\phi(y) - \phi(x)}{y - x}$$ and $$s_3 = \frac{\phi(t) - \phi(x)}{t - x}$$ for the slopes of the chords (the notes label them ①, ②, ③).

- (i) $$\phi(t) \le \alpha\phi(x) + (1 - \alpha)\phi(y)$$
- (ii) $$\dfrac{\phi(t) - \phi(x)}{t - x} \le \dfrac{\phi(y) - \phi(x)}{y - x}$$ $$\Rightarrow$$ $$s_3 \le s_2$$
- (iii) $$\dfrac{\phi(t) - \phi(x)}{t - x} \le \dfrac{\phi(y) - \phi(t)}{y - t}$$ $$\Rightarrow$$ $$s_3 \le s_1$$ $$\rightarrow$$ Check by yourself.
- (iv) $$\dfrac{\phi(y) - \phi(x)}{y - x} \le \dfrac{\phi(y) - \phi(t)}{y - t}$$ $$\Rightarrow$$ $$s_2 \le s_1$$

> **Theorem.** When $$\phi$$ is differentiable on $$(a,b)$$,
>
> - (1) $$\phi$$ is convex $$\Longleftrightarrow$$ $$\phi'(x) \le \phi'(y)$$ for all $$a < x < y < b$$.
> - (2) $$\phi$$ is strictly convex $$\Longleftrightarrow$$ $$\phi'(x) < \phi'(y)$$ for all $$a < x < y < b$$.
>
> When $$\phi$$ is twice differentiable,
>
> - (3) $$\phi$$ is convex $$\Longleftrightarrow$$ $$\phi''(x) \ge 0$$ for all $$x$$.
> - (4) $$\phi$$ is strictly convex $$\Longleftarrow$$ $$\phi''(x) > 0$$ for all $$x$$.
{: .theorem #thm-convex-derivative }

*Proof.* (Check the others.) (a) ($$\Rightarrow$$) For $$x < y$$, the slopes satisfy $$s_1 \ge s_2 \ge s_3$$ (①, ②, ③ in the notes) (see the figure with the points $$x$$, $$x + \Delta x$$, $$y$$, $$y + \Delta y$$), which leads to $$\phi'(x) \le \phi'(y)$$.

**Examples.**

① $$\log x$$ ($$x > 0$$) is concave: $$\dfrac{d}{dx}\log x = \dfrac{1}{x}$$ $$\rightarrow$$ decreasing $$\rightarrow$$ strictly concave.

② $$e^x$$ is convex: $$\dfrac{d}{dx} e^x = e^x$$ $$\rightarrow$$ increasing $$\rightarrow$$ strictly convex.

## 5.2 Arithmetic mean and geometric mean

> **Theorem (Arithmetic mean and geometric mean).**
>
> - (a) $$\sqrt{a}\sqrt{b} \le \frac{1}{2}(a + b)$$ for all $$a, b > 0$$.
> - (b) $$a^{\alpha} b^{\beta} \le \alpha a + \beta b$$ for all $$a, b > 0$$, $$\alpha + \beta = 1$$, $$\alpha, \beta > 0$$.
> - (c) $$cd \le \frac{1}{p} c^p + \frac{1}{q} d^q$$, $$\frac{1}{p} + \frac{1}{q} = 1$$, $$p, q > 1$$, $$c, d > 0$$.
{: .theorem #thm-am-gm }

*Proof.* (b)

$$
\begin{aligned}
a^{\alpha} b^{\beta} \le \alpha a + \beta b
&\Longleftrightarrow \Bigl(\frac{a}{a+b}\Bigr)^{\alpha}\Bigl(\frac{b}{a+b}\Bigr)^{\beta} \le \alpha\frac{a}{a+b} + \beta\frac{b}{a+b} \\
&\Longleftrightarrow \alpha\log\Bigl(\frac{a}{a+b}\Bigr) + \beta\log\Bigl(\frac{b}{a+b}\Bigr) \le \log\Bigl(\alpha\frac{a}{a+b} + \beta\frac{b}{a+b}\Bigr).
\end{aligned}
$$

The last inequality holds by the concavity of the $$\log$$ function.

(c) Let $$a^{\alpha} = c$$ and $$b^{\beta} = d$$, $$\alpha = \frac{1}{p}$$ and $$\beta = \frac{1}{q}$$ in (b).

## 5.3 Liapounov's inequality

> **Theorem (Liapounov's inequality).** If $$E\lvert X\rvert ^s < \infty$$, then
>
> $$
> \bigl(E|X|^r\bigr)^{1/r} \le \bigl(E|X|^s\bigr)^{1/s} \qquad \text{where } 0 < r < s,
> $$
>
> and $$E\lvert X\rvert ^r < \infty$$.
{: .theorem #thm-liapounov }

Note. $$\bigl(E\lvert X\rvert ^r\bigr)^{1/r} = \\lvert X\\rvert _r$$ (the norm of $$X$$). $$\hookrightarrow$$ $$\\lvert X\\rvert _r$$ increases with $$r$$ (strictly, unless $$\lvert X\rvert $$ is almost surely constant).

*Proof.* Let $$c = \dfrac{\lvert X\rvert ^r}{(E\lvert X\rvert ^s)^{r/s}}$$, $$d = 1$$, $$p = \dfrac{s}{r}$$, $$\dfrac{1}{q} = 1 - \dfrac{1}{p} = \dfrac{s - r}{s}$$. Then, by (c) of the above theorem,

$$
\frac{|X|^r}{(E|X|^s)^{r/s}} \times 1 \le \frac{r}{s}\Bigl(\frac{|X|^r}{(E|X|^s)^{r/s}}\Bigr)^{s/r} + \frac{s - r}{s}\cdot 1^{\frac{s}{s-r}}.
$$

$$\downarrow$$ Take the expectation and rearrange.

$$
\frac{E|X|^r}{(E|X|^s)^{r/s}} \le \frac{r}{s}\cdot\frac{E|X|^s}{E|X|^s} + \frac{s - r}{s} = 1.
$$

$$
\therefore\ \bigl(E|X|^r\bigr)^{1/r} \le \bigl(E|X|^s\bigr)^{1/s}. \qquad \square
$$

## 5.4 Markov's and Chebyshev's inequalities

> **Theorem (Markov's inequality, Chebyshev's inequality).** $$\rightarrow$$ Tail probabilities of a random variable.
>
> - (a) *Markov.* If $$X \ge 0$$ w.p. $$1$$ (with probability $$1$$) $$\Longleftrightarrow$$ $$P(X \ge 0) = 1$$, then
>
>   $$
>   P(X \ge c) \le \frac{1}{c}\,E(X) \qquad \forall c > 0.
>   $$
>
> - (b) $$\displaystyle P(\lvert Z\rvert  \ge c) \le \frac{E\lvert Z\rvert ^r}{c^r}$$ for all $$r, c > 0$$.
> - (c) *Chebyshev.* $$\displaystyle P\bigl(\lvert X - EX\rvert  \ge k\sqrt{\mathrm{Var}(X)}\bigr) \le \frac{1}{k^2}$$, $$k > 0$$.
{: .theorem #thm-markov-chebyshev }

*Proof.* (a)

$$
EX \ge E\bigl(X\, I(X \ge c)\bigr) \quad (\because\ X \ge X\, I(X \ge c) \text{ w.p. } 1)
\ \ge\ E\bigl(c\, I(X \ge c)\bigr) = c\,E\bigl(I(X \ge c)\bigr) = c\,P(X \ge c).
$$

$$P(X \ge c) \le \dfrac{1}{c}\, EX$$ as $$c > 0$$.

(b) $$P(\lvert Z\rvert  \ge c) = P(\lvert Z\rvert ^r \ge c^r)$$ $$\rightarrow$$ (Markov) $$\le \dfrac{1}{c^r}\, E\lvert Z\rvert ^r$$.

(c) It is the second inequality when $$r = 2$$.

Note. $$P(\lvert X - EX\rvert  \ge 2\sigma) \le \tfrac{1}{4}$$ by Chebyshev.

## 5.5 Jensen's inequality

> **Theorem (Jensen's inequality).** If $$\phi$$ is convex on $$I$$ where $$I$$ is an open interval of $$\mathbb{R}$$, and $$E\lvert X\rvert  < \infty$$, $$P(X \in I) = 1$$, then
>
> $$
> \phi\bigl(E(X)\bigr) \le E\bigl(\phi(X)\bigr).
> $$
{: .theorem #thm-jensen }

*Proof.* Assume that $$\phi''$$ exists, and $$\mu = EX$$. (It generally holds, but the proof is difficult.)

$$
\phi(x) = \phi(\mu) + \phi'(\mu)(x - \mu) + \tfrac{1}{2}\phi''(\mu^*)(x - \mu)^2, \qquad \text{where } \mu^* \in (x, \mu).
$$

Change $$x$$ to $$X$$. $$\rightarrow$$ $$\mu^*$$ becomes a new random variable.

$$
E\,\phi(X) = \phi(\mu) + \underbrace{E\bigl[\phi'(\mu)(X - \mu)\bigr]}_{=\,0} + \underbrace{E\bigl[\tfrac{1}{2}\phi''(\mu^*)(X - \mu)^2\bigr]}_{\ge\,0} \ \ge\ \phi\bigl(E(X)\bigr).
$$

\* If we do not use the existence of $$\phi''$$, we use that the tangent line is under the function when it is convex.

**Examples.**

$$
e^{EX} \le E(e^X), \qquad -\log(EX) \le -E(\log X), \qquad (EX)^r \le E(X^r) \quad (\text{if } r > 1,\ X \ge 0 \text{ w.p. } 1).
$$

## 5.6 The importance sampling equation

> **Theorem (Equation of importance sampling).** $$\rightarrow$$ importance sampling
>
> - (a) *Importance Sampling Equation.* Let $$f, g$$ be pdfs and $$h$$ any function. Let $$f(x)h(x) = 0$$ if $$g(x) = 0$$. Then
>
>   $$
>   E_f\bigl(h(X)\bigr) = E_g\Bigl(\frac{h(X)\,f(X)}{g(X)}\Bigr).
>   $$
>
>   \* $$E_f$$ denotes the expectation value of $$X$$ when $$X \sim f$$.
> - (b) *Corollary.* Let $$f, g$$ be pdfs and $$f(x) = 0$$ if $$g(x) = 0$$. Then
>
>   $$
>   P_f(X > c) = E_g\Bigl[\frac{f(X)}{g(X)} \,\Big|\, X > c\Bigr] \times P_g(X > c), \qquad c \in \mathbb{R}.
>   $$
{: .theorem #thm-importance-sampling }

*Proof.* (a) $$E_f h(X) = \displaystyle\int h(x) f(x)\,dx = \int \frac{h(x) f(x)}{g(x)}\, g(x)\,dx = E_g\Bigl(\frac{h(X) f(X)}{g(X)}\Bigr)$$.

(b)

$$
\begin{aligned}
P_f(X > c) = E_f\, I(X > c) &= E_g\Bigl[\frac{f(X)}{g(X)}\, I(X > c)\Bigr] \\
&= E_g\Bigl[\frac{f(X)}{g(X)}\, I(X > c) \,\Big|\, X > c\Bigr] P_g(X > c)
 + \underbrace{E_g\Bigl[\frac{f(X)}{g(X)}\, I(X > c) \,\Big|\, X \le c\Bigr]}_{=\,0} P_g(X \le c) \\
&= E_g\Bigl[\frac{f(X)}{g(X)} \,\Big|\, X > c\Bigr] P_g(X > c).
\end{aligned}
$$

**Note (Monte Carlo method).** $$E_f h(X) \approx \dfrac{1}{n}\sum h(X_i)$$, $$X_i \overset{\text{iid}}{\sim} f$$. If it is hard to sample from $$f$$, then sample from $$g$$. Then, by the identity,

$$
E_g\Bigl[\frac{h(X) f(X)}{g(X)}\Bigr] \approx \frac{1}{n}\sum \frac{h(X_i) f(X_i)}{g(X_i)}, \qquad X_i \overset{\text{iid}}{\sim} g.
$$

**Example (upper and lower bounds of the tail probability of the normal distribution).** If $$Z \sim N(0,1)$$, then

$$
\Bigl(1 - \frac{1}{c^2}\Bigr)\frac{e^{-c^2/2}}{c\sqrt{2\pi}} < P(Z > c) < \frac{e^{-c^2/2}}{c\sqrt{2\pi}} \qquad \forall c > 0.
$$

*Proof.* $$f(x) = \frac{1}{\sqrt{2\pi}}\, e^{-x^2/2}$$, $$g(x) = c\, e^{-cx}$$ ($$x > 0$$). $$P(Z > c) = \int_c^{\infty} f(x)\,dx$$ $$\rightarrow$$ hard to calculate exactly.

$$
\begin{aligned}
P(Z > c) &= E_g\Bigl(\frac{f(X)}{g(X)} \,\Big|\, X > c\Bigr) P_g(X > c)
= E_g\Bigl(\frac{\frac{1}{\sqrt{2\pi}}\, e^{-X^2/2}}{c\, e^{-cX}} \,\Big|\, X > c\Bigr) e^{-c^2} \\
&= \frac{e^{-c^2}}{c\sqrt{2\pi}}\; E_g\Bigl[\frac{e^{-X^2/2}}{e^{-cX}} \,\Big|\, X > c\Bigr]
= \frac{e^{-c^2}}{c\sqrt{2\pi}}\; E_g\Bigl(\frac{e^{-\frac{1}{2}(X + c)^2}}{e^{-c(X + c)}}\Bigr)
\end{aligned}
$$

(Check by yourself. $$\hookrightarrow$$ The memoryless property of the exponential distribution: $$[X \mid X > c] \overset{d}{=} [X + c]$$.)

$$
= \frac{e^{-c^2}}{c\sqrt{2\pi}}\; E_g\Bigl(e^{-\frac{1}{2}X^2 + \frac{1}{2}c^2}\Bigr)
= \frac{e^{-c^2/2}}{c\sqrt{2\pi}}\; E_g\bigl(e^{-\frac{1}{2}X^2}\bigr).
$$

$$
\therefore\ \frac{e^{-c^2/2}}{c\sqrt{2\pi}}\, E_g\bigl(1 - \tfrac{1}{2}X^2\bigr) \le P(X > c) \le \frac{e^{-c^2/2}}{c\sqrt{2\pi}}
\qquad (\text{when } \lambda \ge 0,\ 1 - \lambda \le e^{-\lambda} \le 1).
$$

Since $$E_g(X^2) = 2/c^2$$ for the exponential density $$g$$, the left side is $$\bigl(1 - \frac{1}{c^2}\bigr)\frac{e^{-c^2/2}}{c\sqrt{2\pi}}$$.

## 5.7 The Cramér–Chernoff method

> **Lemma (Chernoff inequality).** $$X$$: a random variable taking real values, and $$C(\lambda) = \log E\,e^{\lambda X}$$: the cgf of $$X$$. Then
>
> $$
> P(X \ge t) \le e^{-C^*(t)} \quad \forall t \in \mathbb{R},
> \qquad \text{where } C^*(t) = \sup_{\lambda \ge 0}\bigl(\lambda t - C(\lambda)\bigr)
> $$
>
> (the Legendre transform of the cgf).
{: .theorem #lem-chernoff }

*Proof.* For all $$\lambda > 0$$,

$$
\begin{aligned}
P(X \ge t) = P(e^{\lambda X} \ge e^{\lambda t})
&\le \frac{1}{e^{\lambda t}}\, E(e^{\lambda X}) = e^{-\lambda t}\, E(e^{\lambda X}) \\
&= e^{-\lambda t}\, e^{C(\lambda)} = e^{-(\lambda t - C(\lambda))}.
\end{aligned}
$$

$$
\therefore\ P(X \ge t) \le \inf_{\lambda \ge 0} e^{-(\lambda t - C(\lambda))} = e^{-\sup_{\lambda \ge 0}(\lambda t - C(\lambda))} = e^{-C^*(t)}.
$$

**Example (tail probability of the normal distribution).** Let $$X \sim N(0,1)$$. $$\rightarrow$$ $$M_X(t) = e^{t^2/2}$$, $$C_X(t) = \tfrac{1}{2}t^2$$. Then $$P(X \ge t) \le e^{-C^*(t)}$$ where $$C^*(t) = \sup_{\lambda \ge 0}\bigl(\lambda t - \tfrac{1}{2}\lambda^2\bigr)$$.

$$
\therefore\ C^*(t) = \sup_{\lambda \ge 0}\Bigl(-\tfrac{1}{2}(\lambda - t)^2 + \tfrac{1}{2}t^2\Bigr) = \tfrac{1}{2}t^2 \quad (\text{attained at } \lambda = t,\ t \ge 0).
$$

$$
\therefore\ P(X \ge t) \le e^{-\frac{1}{2}t^2}. \qquad \rightarrow \text{ a less precise upper bound than the importance sampling bound.}
$$

## Supplement from the textbook

> The parts below are in the textbook (§1.6) but not in my notes. They are translated from the book and are not my own writing.
{: .prompt-info }

**Example 1.6.1.** $$\phi(x) = x^2$$ is convex on the whole real line, so for a random variable $$X$$ with an expectation, $$E(X^2) = E(\phi(X)) \ge \phi(E(X)) = (E(X))^2$$.

**Liapounov's inequality via Jensen's inequality.** If $$p > 1$$, then $$\phi(y) = y^p$$ ($$y \ge 0$$) is convex, so for a random variable $$Y \ge 0$$ with an expectation, Jensen gives $$(E(Y))^p \le E(Y^p)$$. Take $$p = s/r > 1$$ and $$Y = \lvert X\rvert^r$$. Here $$E(Y) = E\bigl(\lvert X\rvert^r (I(\lvert X\rvert \le 1) + I(\lvert X\rvert > 1))\bigr) \le E(1 + \lvert X\rvert^s) < \infty$$, so

$$
\bigl(E(\lvert X\rvert^r)\bigr)^{s/r} = (E(Y))^p \le E(Y^p) = E\bigl((\lvert X\rvert^r)^{s/r}\bigr) = E(\lvert X\rvert^s),
$$

which is Liapounov's inequality.

**Proof of Markov's inequality through indicator functions.** The key is to write a probability as the expectation of an indicator function: $$P(\lvert Z\rvert \ge k) = E\bigl(I(\lvert Z\rvert^r/k^r \ge 1)\bigr)$$. Since an indicator is $$0$$ or $$1$$, $$I(\lvert Z\rvert^r/k^r \ge 1) \le (\lvert Z\rvert^r/k^r)\, I(\lvert Z\rvert^r/k^r \ge 1) \le \lvert Z\rvert^r/k^r$$, and taking expectations gives $$P(\lvert Z\rvert \ge k) \le E(\lvert Z\rvert^r)/k^r$$. Chebyshev's inequality follows by substituting $$Z = X - E(X)$$, $$r = 2$$: $$P(\lvert X - E(X)\rvert \ge k) \le \mathrm{Var}(X)/k^2$$.

**Example 1.6.2 (probability outside six sigma).** If $$X$$ has mean $$\mu$$ and standard deviation $$\sigma$$ ($$0 < \sigma < \infty$$), Chebyshev gives $$P(\lvert X - \mu\rvert \ge 6\sigma) \le 1/36 = 0.0277\cdots$$. Whatever the distribution of $$X$$, the probability outside six standard deviations from the mean is at most $$2.8\%$$.

## References

- 김우철, *수리통계학* (Mathematical Statistics), revised 2nd edition, 민영사, 2021 — Chapter 1.
- Mathematical Statistics 1 (326.311), Spring 2025. Instructor: Jaeyong Lee (이재용). My handwritten lecture notes, Chapter 1.
- The notes are translated without changing their wording; remarks written in the margins of the notes are kept.

[Previous](/posts/mathstat1-expectation-mgf/) · [Overview](/posts/mathstat1-overview/)
