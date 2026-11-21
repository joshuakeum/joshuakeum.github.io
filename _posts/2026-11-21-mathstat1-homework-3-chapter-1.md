---
title: "Mathematical Statistics 1: Homework 3, Chapter 1 Exercises"
date: 2026-11-21 09:20:00 +0900
categories: [Study Notes, Mathematical Statistics 1]
tags: [homework, cumulants, skewness, kurtosis, jensen, mgf]
description: Homework 3 of Mathematical Statistics 1, the Chapter 1 part — textbook exercises 1.18 to 1.25 on moments, cumulants, skewness, kurtosis, Jensen's inequality and moment generating functions.
math: true
mermaid: false
render_with_liquid: false
---

> The problems are from the Homework 3 sheet ("Chapter 1, exercises 18–25; Chapter 2, all problems") and from the textbook. This post holds the Chapter 1 part; the Chapter 2 part is in [Homework 3, Chapter 2 Exercises](/posts/mathstat1-homework-3-chapter-2/). The answers are my own, translated into English. Small slips are corrected and each correction is marked **Correction**. The structure of every answer is unchanged. This homework uses [Part 4](/posts/mathstat1-expectation-mgf/) and [Part 5](/posts/mathstat1-inequalities/) of the notes.
{: .prompt-info }

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

**Correction.** The condition for $$t/\sigma$$ to lie in $$(-h_1, h_1)$$ is $$\lvert t\rvert < \sigma h_1$$; the original wrote $$h_1/\sigma$$.

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

**Correction.** The original concluded $$E(-\log X) \le -\log E(X)$$; Jensen's inequality for the convex function $$\phi$$ is $$\phi(E(X)) \le E(\phi(X))$$, which is the inequality above (it is also the one in the notes, $$-\log(EX) \le -E(\log X)$$).

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

**Correction.** In the first half the original concluded "$$P(X \ge 1) \le 0$$, therefore $$P(X \le 1) = 0$$"; the event is $$P(X \ge 1)$$, as above.

## References

- 김우철, *수리통계학* (Mathematical Statistics), revised 2nd edition, 민영사, 2021 — Chapter 1 exercises 1.18 to 1.25. The exercise statements are translated from the book.
- Mathematical Statistics 1 (326.311), Seoul National University, Spring 2025. Instructor: Jaeyong Lee (이재용). Homework 3 sheet.
- The answers are mine, translated into English. Small slips are corrected where marked; the structure of every answer is unchanged.

[Overview](/posts/mathstat1-overview/) · [Homework 2](/posts/mathstat1-homework-2/) · [Homework 3, Chapter 2 Exercises](/posts/mathstat1-homework-3-chapter-2/)
