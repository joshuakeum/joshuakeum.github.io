---
title: "Calculus 1: Power Series and the Elementary Functions"
date: 2026-10-05 11:00:00 +0900
categories: [Course Notes, Calculus 1]
tags: [power series, radius of convergence, exponential, trigonometric, hyperbolic]
description: Radius of convergence, term-by-term differentiation, and the exponential, trigonometric and hyperbolic functions defined by their series. Unit 2 of Calculus 1.
math: true
render_with_liquid: false
---

## What this unit answers

Chapter 1 asked whether a series of *numbers* converges. Now the terms carry a variable, and the same question becomes: for which $$x$$ does the sum make sense? The answer is remarkably clean — there is always a radius $$\rho$$ inside which the series converges absolutely and outside which it diverges.

Once that is established, something larger follows. A convergent power series can be differentiated and integrated one term at a time. That makes it possible to *define* $$e^x$$, $$\sin x$$, $$\cos x$$, and the hyperbolic functions by their series, derive all their properties by differentiating, and extend them to complex arguments — where Euler's formula appears almost for free.

## Prerequisites

[Unit 1](/posts/calculus-1-series/), in particular the ratio and root tests, the alternating series test, and absolute convergence. Basic differentiation and integration of polynomials.

## Power series and the radius of convergence

A **power series** is a series of the form

$$
\sum_{n=0}^{\infty} a_n x^n = a_0 + a_1 x + a_2 x^2 + \cdots .
$$

Whether it converges depends on $$x$$. So the sum defines a function on exactly the set of $$x$$ for which it converges — nothing more.

A first structural fact: **the coefficients are determined by the function.** If

$$
\sum_{n=0}^{\infty} a_n x^n = \sum_{n=0}^{\infty} b_n x^n
\quad \text{for all } x,
$$

then $$a_n = b_n$$ for every $$n$$. Two different coefficient lists cannot produce the same function.

### The dichotomy theorem

**Theorem.** Given $$\sum a_n x^n$$:

- If it converges at $$x = x_0$$, then $$\sum \lvert a_n x^n\rvert < \infty$$ for every $$x$$ with $$\lvert x\rvert < \lvert x_0\rvert$$.
- If it diverges at $$x = x_1$$, then it diverges for every $$x$$ with $$\lvert x\rvert > \lvert x_1\rvert$$.

*Proof.* Only the first statement needs work; the second is its contrapositive in disguise.

Convergence at $$x_0$$ forces $$a_n x_0^n \to 0$$ by the $$n$$-th term test, so the terms are eventually bounded: $$\lvert a_n x_0^n\rvert < 1$$ for all $$n \ge N$$. Then for $$\lvert x \rvert < \lvert x_0\rvert$$,

$$
\begin{aligned}
\sum_{n=N}^{\infty} \lvert a_n x^n\rvert
&= \sum_{n=N}^{\infty} \lvert a_n x_0^n\rvert \left\lvert \frac{x}{x_0}\right\rvert^n \\
&< \sum_{n=N}^{\infty} \left\lvert \frac{x}{x_0}\right\rvert^n < \infty,
\end{aligned}
$$

a geometric series of ratio less than $$1$$. Adding back the finitely many omitted terms changes nothing. $$\square$$

For the second statement: if the series converged at some $$x$$ with $$\lvert x\rvert > \lvert x_1\rvert$$, the first statement would force convergence at $$x_1$$, a contradiction.

So the set of convergence has no gaps. Convergence somewhere propagates inward; divergence somewhere propagates outward. Consequently there is a number $$\rho \in [0,\infty]$$, the **radius of convergence** (수렴반경), with

$$
\begin{aligned}
\sum_{n=0}^{\infty} \lvert a_n x^n\rvert < \infty &\ \text{ if } \lvert x\rvert < \rho, \\
\sum_{n=0}^{\infty} a_n x^n &\ \text{ diverges if } \lvert x\rvert > \rho .
\end{aligned}
$$

> $$\rho$$ always exists, even when you cannot compute it. Not knowing the radius is not the same as there being none.
{: .prompt-tip }

### Computing the radius

$$
\begin{aligned}
\rho &= \lim_{n\to\infty}\left\lvert \frac{a_n}{a_{n+1}}\right\rvert \\
\text{or}\quad \rho &= \lim_{n\to\infty}\frac{1}{\sqrt[n]{\lvert a_n\rvert}},
\end{aligned}
$$

whenever the limit on the right exists.

*Proof of the first formula.* Apply the ratio test to $$\sum \lvert a_n x^n\rvert$$:

$$
\left\lvert \frac{a_{n+1}x^{n+1}}{a_n x^n}\right\rvert
= \left\lvert \frac{a_{n+1}}{a_n}\right\rvert \lvert x\rvert
\longrightarrow \frac{\lvert x\rvert}{\rho}.
$$

If $$\lvert x\rvert < \rho$$ the limit is below $$1$$, so the series converges absolutely; the radius is therefore at least $$\rho$$. If $$\lvert x\rvert > \rho$$ the limit exceeds $$1$$, so $$\sum\lvert a_nx^n\rvert$$ diverges; the radius is at most $$\rho$$. Both bounds together give equality. $$\square$$

> Watch the second half of that argument. The ratio test applied to $$\sum \lvert a_n x^n\rvert$$ tells us the *absolute* series diverges, which is not immediately the same as $$\sum a_n x^n$$ diverging. It happens to be enough here, because when the ratio limit exceeds $$1$$ the terms themselves grow without bound, so the $$n$$-th term test applies directly.
{: .prompt-warning }

The root formula is proved the same way with the root test. The fully general version, valid with no existence hypothesis, is the Cauchy–Hadamard formula $$1/\rho = \limsup_n \lvert a_n\rvert^{1/n}$$; the course states only the $$\lim$$ version.

### The endpoints are genuinely undecided

At $$x = \pm\rho$$ the theory says nothing, and all four possibilities occur. With $$\rho = 1$$ in every case:

| Series | Interval of convergence |
|---|---|
| $$\sum x^n$$ | $$(-1,\,1)$$ |
| $$\sum x^n/n$$ | $$[-1,\,1)$$ |
| $$\sum (-1)^n x^n/n$$ | $$(-1,\,1]$$ |
| $$\sum x^n/n^2$$ | $$[-1,\,1]$$ |

Check the second one to see the mechanism. At $$x = -1$$ the series is $$\sum (-1)^n/n$$, which converges by the alternating series test. At $$x = 1$$ it is the harmonic series, which diverges. Endpoints must be tested one at a time, by hand, using Chapter 1 methods.

### Worked example: a radius computation

Find the interval of convergence of

$$
\sum_{n=1}^{\infty} \frac{(x-2)^n}{n\,3^n}.
$$

Write $$u = x-2$$, so $$a_n = 1/(n3^n)$$. Then

$$
\left\lvert \frac{a_n}{a_{n+1}}\right\rvert = \frac{(n+1)3^{n+1}}{n\,3^n} = 3\cdot\frac{n+1}{n} \to 3,
$$

so $$\rho = 3$$ and the series converges for $$\lvert x-2\rvert < 3$$, that is $$-1 < x < 5$$.

At $$x = 5$$ we get $$\sum 1/n$$, divergent. At $$x = -1$$ we get $$\sum (-1)^n/n$$, convergent. The interval is $$[-1,\,5)$$.

## The fundamental theorem of power series

**Theorem.** Let $$f(x) = \sum_{n=0}^{\infty} a_n x^n$$ have radius $$\rho > 0$$ (possibly $$\rho = \infty$$). Then the differentiated and integrated series

$$
\begin{aligned}
&\sum_{n=1}^{\infty} n\,a_n x^{n-1}, \\
&\sum_{n=0}^{\infty} \frac{a_n}{n+1}\,x^{n+1}
\end{aligned}
$$

both have the same radius $$\rho$$, and on $$-\rho < x < \rho$$,

$$
\begin{aligned}
f'(x) &= \sum_{n=1}^{\infty} n\,a_n x^{n-1}, \\
\int_0^x f(t)\,dt &= \sum_{n=0}^{\infty} \frac{a_n}{n+1}\,x^{n+1}.
\end{aligned}
$$

The proof is omitted in lecture and is genuinely technical; it belongs to a later analysis course.

This is a much stronger statement than it looks. For a general series of functions, you may *not* differentiate term by term — the operation can destroy convergence or produce the wrong answer. Power series are the exception, and that exception is what makes the rest of this unit possible.

> Radius is preserved, but **endpoint behavior is not.** Differentiating can lose an endpoint; integrating can gain one. Only the open interval $$(-\rho,\rho)$$ is protected.
{: .prompt-warning }

### Building the standard expansions

Start from the geometric series and generate the rest by calculus. For $$-1 < x < 1$$:

$$
\frac{1}{1-x} = 1 + x + x^2 + \cdots = \sum_{n=0}^{\infty} x^n .
$$

Differentiate both sides:

$$
\frac{1}{(1-x)^2} = 1 + 2x + 3x^2 + \cdots = \sum_{n=1}^{\infty} n x^{n-1}.
$$

Substitute $$-x$$ for $$x$$:

$$
\frac{1}{1+x} = 1 - x + x^2 - \cdots = \sum_{n=0}^{\infty}(-1)^n x^n .
$$

Integrate that one from $$0$$ to $$x$$:

$$
\begin{aligned}
\ln(1+x) &= x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \cdots \\
&= \sum_{n=0}^{\infty}\frac{(-1)^n}{n+1}x^{n+1}.
\end{aligned}
$$

The theorem guarantees this for $$-1 < x < 1$$. But the right-hand side also converges at $$x = 1$$, by the alternating series test. Does the identity extend to the endpoint?

### Abel's theorem

**Theorem (Abel).** A power series function is continuous at every point of its domain of convergence — including an endpoint, when the series converges there.

Inside $$(-\rho,\rho)$$ this is immediate: the function is differentiable, hence continuous. The content is entirely at the endpoints, and that case is delicate. The course omits the proof.

With it, we may let $$x \to 1^-$$ in the logarithm series and conclude

$$
\ln 2 = 1 - \frac12 + \frac13 - \frac14 + \cdots .
$$

> This identity is **not** obvious and does not follow from the fundamental theorem alone. Convergence of the series at $$x=1$$ says the right side is *some* number; Abel's theorem is what identifies it as $$\ln 2$$. The same gap appears again with $$\arctan 1$$ below.
{: .prompt-warning }

## Analytic functions

A function is **analytic** (해석적) at a point if, on some open interval around that point, it equals a convergent power series centered there. The course calls these power series functions.

If $$f(x) = \sum a_n x^n$$ near $$0$$, differentiating $$n$$ times and evaluating at $$0$$ kills every term but one:

$$
\begin{aligned}
a_n &= \frac{f^{(n)}(0)}{n!}, \\
\text{so}\quad f(x) &= \sum_{n=0}^{\infty}\frac{f^{(n)}(0)}{n!}x^n .
\end{aligned}
$$

The coefficients are forced. Memorize this formula; it is the bridge to [Taylor's theorem](/posts/calculus-1-taylor/) in the next unit.

An immediate consequence: an analytic function is infinitely differentiable, since the fundamental theorem lets you differentiate the series as often as you like.

> The converse fails. Being infinitely differentiable does **not** make a function analytic. The standard counterexample is $$f(x) = e^{-1/x^2}$$ for $$x \ne 0$$ with $$f(0) = 0$$: every derivative at the origin vanishes, so its series is identically $$0$$, which equals $$f$$ only at the single point $$x=0$$. The function is smooth but not analytic at $$0$$.
{: .prompt-warning }

<!-- TODO: verify whether the course stated the e^{-1/x^2} example explicitly or only noted that smooth does not imply analytic. -->

## The exponential function

Define

$$
\exp(x) := 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots
= \sum_{n=0}^{\infty}\frac{x^n}{n!} .
$$

By the ratio test the radius is $$\infty$$, so this converges for every real $$x$$.

We would like to say $$\exp(x) = e^x$$. But $$e^x$$ was defined as a power of the number $$e$$, with no reason to be a power series function at all. The two definitions must be reconciled, not assumed equal.

**The argument.** Both functions solve the same initial value problem:

$$
f' = f, \qquad f(0) = 1 .
$$

For $$\exp$$, differentiate term by term: the derivative of $$x^n/n!$$ is $$x^{n-1}/(n-1)!$$, which shifts the series onto itself. And $$\exp(0)=1$$. For $$e^x$$, both facts are standard. Since this initial value problem has a unique solution — a fact from differential equations — the two functions coincide.

This is the template for the whole unit: *define by a series, identify by a differential equation.*

### Worked example: a series by manipulation

Find $$\sum_{n=1}^{\infty} \dfrac{n}{2^n\,n!}$$.

Cancel the $$n$$ against the factorial, then shift the index:

$$
\begin{aligned}
\sum_{n=1}^{\infty}\frac{n}{2^n n!}
&= \sum_{n=1}^{\infty}\frac{1}{2^n (n-1)!}\\
&= \frac12\sum_{m=0}^{\infty}\frac{(1/2)^{m}}{m!}
= \frac12 e^{1/2}.
\end{aligned}
$$

### Growth and irrationality

Exponentials dominate every polynomial:

$$
\lim_{x\to\infty}\frac{e^x}{x^n} = \infty \quad\text{for every } n .
$$

This is visible from the series: $$e^x$$ contains the term $$x^{n+1}/(n+1)!$$, already of higher degree than $$x^n$$.

**$$e$$ is irrational.** Sketch: suppose $$e = a/b$$ with integers $$a,b$$, and pick $$p \ge b$$. Then $$p!\,e$$ would be an integer, and so would $$p!$$ times the partial sum $$1 + 1 + \tfrac{1}{2!} + \cdots + \tfrac{1}{p!}$$, since $$p!/n!$$ is an integer for $$n \le p$$. Their difference is

$$
\begin{aligned}
&\frac{p!}{(p+1)!} + \frac{p!}{(p+2)!} + \cdots \\
&\qquad = \frac{1}{p+1} + \frac{1}{(p+1)(p+2)} + \cdots,
\end{aligned}
$$

which is strictly between $$0$$ and $$1$$. An integer cannot lie strictly between $$0$$ and $$1$$. Contradiction.

### Approximating $$e$$, with error control

Truncating after $$x^p/p!$$ leaves

$$
\begin{aligned}
\left\lvert e - \sum_{n=0}^{p}\frac{1}{n!}\right\rvert
&= \frac{1}{(p+1)!}+\frac{1}{(p+2)!}+\cdots\\
&< \frac{1}{(p+1)!}\left(1 + \frac{1}{p+2} + \frac{1}{(p+2)^2}+\cdots\right),
\end{aligned}
$$

and the bracket is a geometric series summing to $$(p+2)/(p+1)$$. So the error is below roughly $$1/(p+1)!$$, which collapses fast: $$p=7$$ already puts it under $$3\times10^{-5}$$.

> An approximation without an error bound is worthless. "$$\sqrt2 \approx 2$$" and "$$\sqrt2 \approx 1.5$$" are both *true* as bare statements; what distinguishes them is the size of the error. Saying "$$\pi \approx 3.2$$, error under $$0.1$$" is informative. Saying "$$\pi\approx3.2$$, error under $$100$$" is not. Always carry the bound.
{: .prompt-tip }

## Trigonometric functions

$$
\begin{aligned}
\sin x &= x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots \\
&= \sum_{n=0}^{\infty}\frac{(-1)^n}{(2n+1)!}x^{2n+1},
\end{aligned}
$$

$$
\begin{aligned}
\cos x &= 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots \\
&= \sum_{n=0}^{\infty}\frac{(-1)^n}{(2n)!}x^{2n},
\end{aligned}
$$

both with radius $$\infty$$.

Again the identification needs an argument, since $$\sin$$ and $$\cos$$ arrive from geometry with no reason to be power series. Define

$$
\begin{aligned}
C(x) &:= \sum_{n=0}^{\infty}\frac{(-1)^n}{(2n)!}x^{2n}, \\
S(x) &:= \sum_{n=0}^{\infty}\frac{(-1)^n}{(2n+1)!}x^{2n+1}.
\end{aligned}
$$

Term-by-term differentiation gives

$$
\begin{aligned}
C'(x) &= -S(x),\quad C(0)=1, \\
S'(x) &= C(x),\quad S(0)=0,
\end{aligned}
$$

mirroring the derivative cycle $$\sin \to \cos \to -\sin \to -\cos \to \sin$$.

Now consider

$$
g(x) = \big(S(x)-\sin x\big)^2 + \big(C(x)-\cos x\big)^2 .
$$

Differentiating and using the four relations above, every term cancels: $$g'(x) \equiv 0$$. And $$g(0) = 0$$. A function with zero derivative everywhere is constant, so $$g \equiv 0$$. A sum of two squares vanishes only when both vanish, so $$S \equiv \sin$$ and $$C \equiv \cos$$. $$\square$$

The same trick — build a nonnegative quantity measuring the discrepancy, show its derivative vanishes — is the standard proof of uniqueness for initial value problems.

### Worked example: error-controlled evaluation

Estimate $$\sin 2$$ with a stated error bound.

The series at $$x=2$$ is alternating with decreasing terms, so the alternating-series bound from Unit 1 applies directly:

$$
\begin{aligned}
\left\lvert \sin 2 - \left(2 - \frac{2^3}{3!} + \frac{2^5}{5!}\right)\right\rvert
&< \frac{2^7}{7!} \\
&= \frac{128}{5040} \approx 0.0254 .
\end{aligned}
$$

The partial sum is $$2 - 1.3\overline{3} + 0.2\overline{6} \approx 0.9333$$, and the true value is $$0.9093$$ — comfortably inside the bound.

### A warning about patterns

Not every elementary function has a tidy series. For the tangent,

$$
\tan x = x + \frac{x^3}{3} + \frac{2x^5}{15} + \cdots,
$$

and there is no simple closed form for the coefficients. Repeated differentiation of $$\tan x$$ produces rapidly uglier expressions, and dividing the sine series by the cosine series is possible but laborious. Finding the general coefficient requires machinery beyond this course.

## The complex exponential

**Definition.** For $$a, b \in \mathbb{R}$$ and $$c > 0$$:

$$
\begin{aligned}
e^{ib} &:= \cos b + i\sin b, \\
e^{a+ib} &:= e^a\,e^{ib}, \\
c^{z} &:= e^{z\ln c}.
\end{aligned}
$$

This looks arbitrary until you substitute $$ib$$ into the exponential series and sort the terms by whether the power of $$i$$ is real or imaginary:

$$
\begin{aligned}
e^{ib} &= 1 + ib + \frac{(ib)^2}{2!} + \frac{(ib)^3}{3!} + \cdots\\
&= \left(1 - \frac{b^2}{2!} + \frac{b^4}{4!} - \cdots\right)
+ i\left(b - \frac{b^3}{3!} + \frac{b^5}{5!} - \cdots\right)\\
&= \cos b + i\sin b .
\end{aligned}
$$

The definition is the only one consistent with the series. The law $$e^{z_1+z_2} = e^{z_1}e^{z_2}$$ survives for complex exponents; verifying it reduces to the addition formulas for sine and cosine.

Inverting Euler's formula expresses the trigonometric functions as exponentials:

$$
\begin{aligned}
\cos x &= \frac{e^{ix}+e^{-ix}}{2}, \\
\sin x &= \frac{e^{ix}-e^{-ix}}{2i}.
\end{aligned}
$$

Setting $$b = \pi$$ gives Euler's identity, $$e^{i\pi} + 1 = 0$$.

## Hyperbolic functions

**Definition.**

$$
\begin{aligned}
\cosh x &= \frac{e^x + e^{-x}}{2}, \\
\sinh x &= \frac{e^x - e^{-x}}{2}, \\
\tanh x &= \frac{\sinh x}{\cosh x}.
\end{aligned}
$$

Compare with the previous display: the hyperbolic functions are what you get by dropping the $$i$$'s. That single observation explains every identity below.

**Properties.**

- Pythagorean: $$\cosh^2 x - \sinh^2 x = 1$$ and $$1 - \tanh^2 x = \operatorname{sech}^2 x$$.
- Addition: $$\cosh(a+b) = \cosh a\cosh b + \sinh a \sinh b$$, and similarly for $$\sinh$$ — note the sign pattern differs from the circular case.
- Derivatives: $$(\cosh x)' = \sinh x$$, $$(\sinh x)' = \cosh x$$, $$(\tanh x)' = \operatorname{sech}^2 x$$. No minus signs anywhere.
- Series: $$\cosh x = 1 + \frac{x^2}{2!} + \frac{x^4}{4!}+\cdots$$ and $$\sinh x = x + \frac{x^3}{3!}+\frac{x^5}{5!}+\cdots$$ — the trigonometric series with the alternating signs removed.

Verifying the first identity takes one line:

$$
\begin{aligned}
\cosh^2 x - \sinh^2 x
&= \frac{(e^x+e^{-x})^2 - (e^x-e^{-x})^2}{4} \\
&= \frac{4}{4} = 1 .
\end{aligned}
$$

### Why "hyperbolic"

The identity $$\cosh^2 t - \sinh^2 t = 1$$ says that $$(\cosh t, \sinh t)$$ lies on the hyperbola $$x^2 - y^2 = 1$$, exactly as $$(\cos t, \sin t)$$ lies on the circle $$x^2+y^2=1$$.

<!-- Figure not drawn yet. Restore the line below once
     assets/img/calculus-1/hyperbola-parametrization.png exists:
![Unit circle parametrized by cosine and sine beside the unit hyperbola parametrized by cosh and sinh](/assets/img/calculus-1/hyperbola-parametrization.png)
-->

<!-- TODO: draw figure — left panel: unit circle with the point (cos t, sin t) marked; right panel: right branch of x^2 - y^2 = 1 with the point (cosh t, sinh t) marked and the asymptotes y = ±x dashed. -->

One disanalogy worth noting. In the circular parametrization $$t$$ is time under uniform circular motion, so it has a direct physical reading. In the hyperbolic parametrization $$t$$ has no such meaning; it is a parameter and nothing more.

Ellipse, parabola, and hyperbola are the **conic sections** — the curves cut from a cone by a plane, named by Apollonius. Which one appears depends on the plane's slope relative to the cone's generating line: steeper gives a hyperbola, equal gives a parabola, shallower gives an ellipse.

### Where $$\cosh$$ shows up

Circles, ellipses, parabolas, and hyperbolas all describe real physical paths — a ripple, a planetary orbit, a projectile, a comet passing through once and never returning. Is $$y = \cosh x$$ equally real?

It is. A chain or power line hanging under its own weight takes the shape $$y = \frac1k\cosh kx$$, the **catenary**.

> A suspension bridge cable is **not** a catenary. The cable carries the deck, whose weight is distributed evenly along the horizontal, not along the cable. That load produces a parabola instead. The catenary is the shape of a chain carrying only itself.
{: .prompt-info }

## Inverse functions

If $$f : A \to B$$ is one-to-one and onto, the inverse $$f^{-1} : B \to A$$ exists. In practice, a function that is strictly increasing (or strictly decreasing) on an interval is automatically one-to-one there — which is why checking $$f' > 0$$ is the usual first move.

**Theorem (derivative of an inverse).** With $$y = f(x)$$, so $$x = f^{-1}(y)$$:

$$
\begin{aligned}
\frac{d}{dy}f^{-1}(y) &= \frac{1}{f'(x)}, \\
\text{equivalently}\quad \frac{dx}{dy} &= \frac{1}{\;dy/dx\;}.
\end{aligned}
$$

*Proof.* Assume $$f^{-1}$$ is differentiable. Differentiate the identity $$f^{-1}(f(x)) \equiv x$$ by the chain rule:

$$
(f^{-1})'\big(f(x)\big)\cdot f'(x) \equiv 1 . \qquad\square
$$

The assumption is the subtle part. That $$f^{-1}$$ *is* differentiable requires proof, which the textbook relegates to an appendix.

> Reading $$dy/dx$$ as an honest fraction is a good habit here, and the formula above is one reason why. But it is a habit with limits — $$dy/dx$$ is not a quotient of two numbers, and treating it as one will eventually mislead you.
{: .prompt-tip }

### Worked example: differentiating an inverse you cannot write down

Let $$f(x) = x^3 + 2x + 5$$. Compute $$(f^{-1})'(8)$$.

First, an inverse exists: $$f'(x) = 3x^2 + 2 > 0$$ everywhere, so $$f$$ is strictly increasing. Solving the cubic explicitly is unpleasant and unnecessary — we only need the $$x$$ with $$f(x) = 8$$, and inspection gives $$x = 1$$. Then

$$
(f^{-1})'(8) = \frac{1}{f'(1)} = \frac{1}{5}.
$$

The point of the theorem is exactly this: the derivative of the inverse is computable even when the inverse is not.

As a second application, $$y = \ln x$$ inverts $$x = e^y$$, so

$$
\frac{d}{dx}\ln x = \frac{1}{\;de^y/dy\;} = \frac{1}{e^y} = \frac1x .
$$

## Inverse trigonometric functions

Sine is not one-to-one on $$\mathbb{R}$$, so domains must be restricted before inverting:

| Function | Domain | Range of inverse |
|---|---|---|
| $$\arcsin$$ | $$[-1,1]$$ | $$[-\pi/2,\ \pi/2]$$ |
| $$\arccos$$ | $$[-1,1]$$ | $$[0,\ \pi]$$ |
| $$\arctan$$ | $$(-\infty,\infty)$$ | $$(-\pi/2,\ \pi/2)$$ |

> Write $$\arcsin$$, not $$\sin^{-1}$$. The latter collides with $$1/\sin$$ and causes real errors. The prefix *arc* records that the output is an arc length on the unit circle — that is, an angle in radians.
{: .prompt-tip }

Because of the restriction, $$\arccos(\cos\theta) = \theta$$ only when $$\theta$$ already lies in $$[0,\pi]$$. For $$\theta = 6\pi/5$$ the composition returns $$4\pi/5$$ instead. Going the other way is safe: $$\cos(\arccos u) = u$$ for every $$u \in [-1,1]$$.

A useful identity, provable by differentiating and checking one value:

$$
\arcsin x + \arccos x \equiv \frac{\pi}{2}.
$$

**Derivatives.**

$$
\begin{aligned}
\frac{d}{dx}\arcsin x &= \frac{1}{\sqrt{1-x^2}}, \\
\frac{d}{dx}\arccos x &= \frac{-1}{\sqrt{1-x^2}}, \\
\frac{d}{dx}\arctan x &= \frac{1}{1+x^2}.
\end{aligned}
$$

*Proof of the first.* With $$y = \sin x$$,

$$
\begin{aligned}
(\arcsin)'(y) &= \frac{1}{(\sin x)'} = \frac{1}{\cos x} \\
&= \frac{1}{\sqrt{1-\sin^2 x}} = \frac{1}{\sqrt{1-y^2}} .
\end{aligned}
$$

The positive square root is correct because $$\cos x > 0$$ on $$(-\pi/2,\pi/2)$$. The third is identical with $$\sec^2 x = 1 + \tan^2 x$$. $$\square$$

### The arctangent series and $$\pi$$

Substituting $$-x^2$$ into the geometric series and integrating:

$$
\frac{1}{1+x^2} = 1 - x^2 + x^4 - \cdots
\ \Longrightarrow\
\arctan x = x - \frac{x^3}{3} + \frac{x^5}{5} - \cdots
$$

valid for $$-1 \le x \le 1$$ — the endpoints included, by Abel's theorem again. Setting $$x=1$$:

$$
\frac{\pi}{4} = 1 - \frac13 + \frac15 - \frac17 + \cdots .
$$

Before this, $$\pi$$ was computed by inscribing regular polygons in a circle; Archimedes used a 96-gon. A series that yields $$\pi$$ from the odd integers alone is a genuine turn in the history of mathematics.

But it is useless numerically. The terms shrink like $$1/n$$, so the alternating-series error bound says you need on the order of $$10^{6}$$ terms for six decimal places.

The fix is to evaluate at a smaller argument, where the powers decay fast:

$$
\frac{\pi}{6} = \arctan\frac{1}{\sqrt3}
= \frac{1}{\sqrt3}\left(1 - \frac{1}{3\cdot3} + \frac{1}{5\cdot 3^2} - \cdots\right).
$$

Each term now carries an extra factor of $$1/3$$, so accuracy arrives geometrically rather than harmonically. Choosing the argument well is the whole art of series-based computation.

## Common pitfalls

- **Assuming the endpoints follow the radius.** They must be tested separately, every time, and the two ends can behave differently.
- **Using the fundamental theorem at an endpoint.** It protects $$(-\rho,\rho)$$ only. Extending an identity to $$x = \pm\rho$$ needs Abel's theorem.
- **Thinking smooth implies analytic.** Infinitely many derivatives do not guarantee that the series converges back to the function.
- **Assuming $$\exp(x) = e^x$$ without argument.** The series and the power are different objects until the differential equation identifies them. The same applies to $$S, C$$ versus $$\sin,\cos$$.
- **Writing $$\sin^{-1}x$$ for $$\arcsin x$$.** Ambiguous with $$1/\sin x$$.
- **Expecting $$\arccos(\cos\theta)=\theta$$.** True only inside the restricted range.
- **Quoting an approximation with no error bound.** The bound is the content, not a decoration.
- **Mixing up circular and hyperbolic sign patterns.** $$\cos^2+\sin^2=1$$ but $$\cosh^2-\sinh^2=1$$; $$(\cos)'=-\sin$$ but $$(\cosh)'=+\sinh$$.

## Connections

- **Backward.** Every convergence claim here is an application of Unit 1: the ratio and root tests give the radius, the alternating test handles endpoints and error bounds, absolute convergence is what the dichotomy theorem actually delivers.
- **Forward.** [Taylor's theorem](/posts/calculus-1-taylor/) takes up the question this unit leaves open: for a function that is *not* given as a series, when does its Taylor series converge back to it, and how large is the error after finitely many terms? The coefficient formula $$a_n = f^{(n)}(0)/n!$$ is the shared hinge.
- **Outward.** The complex exponential is the foundation of Fourier analysis; the catenary is a standard first example in the calculus of variations; the identification of a function with the solution of an initial value problem is the central technique of differential equations.

## Summary

Series to know cold:

| Function | Series | Interval |
|---|---|---|
| $$\dfrac{1}{1-x}$$ | $$\sum_{n\ge0} x^n$$ | $$\vert x\vert<1$$ |
| $$\ln(1+x)$$ | $$\sum_{n\ge0}\frac{(-1)^n}{n+1}x^{n+1}$$ | $$-1<x\le1$$ |
| $$e^x$$ | $$\sum_{n\ge0}\frac{x^n}{n!}$$ | all $$x$$ |
| $$\sin x$$ | $$\sum_{n\ge0}\frac{(-1)^n}{(2n+1)!}x^{2n+1}$$ | all $$x$$ |
| $$\cos x$$ | $$\sum_{n\ge0}\frac{(-1)^n}{(2n)!}x^{2n}$$ | all $$x$$ |
| $$\sinh x$$ | $$\sum_{n\ge0}\frac{x^{2n+1}}{(2n+1)!}$$ | all $$x$$ |
| $$\cosh x$$ | $$\sum_{n\ge0}\frac{x^{2n}}{(2n)!}$$ | all $$x$$ |
| $$\arctan x$$ | $$\sum_{n\ge0}\frac{(-1)^n}{2n+1}x^{2n+1}$$ | $$-1\le x\le1$$ |

Key facts:

- Radius: $$\rho = \lim\lvert a_n/a_{n+1}\rvert$$ or $$\rho = \lim 1/\sqrt[n]{\lvert a_n\rvert}$$; endpoints tested by hand.
- Term-by-term differentiation and integration are valid on $$(-\rho,\rho)$$ and preserve $$\rho$$.
- Abel: a power series function is continuous wherever it converges, endpoints included.
- Analytic $$\Rightarrow$$ smooth, but not conversely; coefficients satisfy $$a_n = f^{(n)}(0)/n!$$.
- Euler: $$e^{ib} = \cos b + i\sin b$$; hyperbolic functions are the same construction with the $$i$$'s removed.
- Inverses: $$(f^{-1})'(y) = 1/f'(x)$$, computable without knowing $$f^{-1}$$.

## References

- Hong Jong Kim, *Calculus 1+* (미적분학 1+), 2nd revised edition, Seoul National University Press — Chapter 2 (Theorem 2.1.4, Theorem 2.2.1, pp. 62–88).
- Mathematics 1 (수학 1, L0442.000100), Seoul National University, Spring 2022. Instructor: Choi Hyung Gyu (최형규).
- The complex exponential material was presented as outside the examinable scope.
