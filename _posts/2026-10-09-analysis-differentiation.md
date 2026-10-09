---
title: "Mathematical Analysis: Differentiation"
date: 2026-10-09 10:30:00 +0900
categories: [Course Notes, Mathematical Analysis]
tags: [derivative, mean value theorem, rolle, darboux, lhospital, second derivative test]
description: The derivative, the mean value theorems of Rolle, Lagrange and Cauchy, Darboux's theorem on the intermediate value property of derivatives, and L'Hospital's rule. Chapter 5 of Introduction to Mathematical Analysis.
math: true
mermaid: false
render_with_liquid: false
---

> This chapter covers §§5.1–5.3. The notes give §5.1 as a list of exercises
> only, with no definitions or theorems typed, and mark the first derivative
> test, the inverse function theorem and L'Hospital's rule as *"you know it"*.
> Those statements are supplied here so the chapter stands on its own; the
> references say which.
{: .prompt-info }

## What this chapter answers

The derivative is a limit, so everything in
[Chapter 4](/posts/analysis-continuity/) applies to it and nothing in this
chapter is about *computing* derivatives. The question is different: **what can
you conclude about $$f$$ from information about $$f'$$?**

Almost all of the answer is one theorem. The **mean value theorem** converts a
statement about the derivative at an unknown single point into a statement
about the function across a whole interval, and every result in the chapter is
an application of it:

- $$f' > 0$$ on an interval $$\Rightarrow$$ $$f$$ is increasing;
- $$f' = 0$$ on an interval $$\Rightarrow$$ $$f$$ is constant;
- $$\lvert f'\rvert \le M$$ $$\Rightarrow$$ $$f$$ is Lipschitz, which is what
  §4.3 wanted and could not produce;
- inequalities, by comparing a function with its tangent line;
- L'Hospital's rule, via the Cauchy form.

The chapter also contains one genuine surprise. A derivative need not be
continuous — exercise 9 of §5.1 builds the standard example — and yet
**every derivative satisfies the intermediate value property anyway**. That is
Darboux's theorem, and it means the possible discontinuities of a derivative
are severely restricted: a derivative can oscillate, but it can never jump.

## Prerequisites

[Chapter 4](/posts/analysis-continuity/) for limits, continuity, the extreme
value theorem and the intermediate value theorem;
[Chapter 3](/posts/analysis-sequences/) for sequential arguments;
[Chapter 1](/posts/analysis-real-numbers/) for suprema.

---

## Part 1 — §5.1: the derivative

> The notes type no theory for this section, only the exercises. The
> definitions and basic theorems below are the standard ones, included so the
> rest of the chapter has something to rest on.
{: .prompt-info }

**Definition.** Let $$f$$ be real-valued on an interval $$I$$ and let
$$x_0$$ be an interior point. Then $$f$$ is **differentiable at $$x_0$$** when

$$
f'(x_0) = \lim_{h \to 0}\frac{f(x_0+h) - f(x_0)}{h}
$$

exists in $$\mathbb{R}$$, equivalently when
$$\lim_{x\to x_0}\frac{f(x)-f(x_0)}{x - x_0}$$ exists. One-sided derivatives
$$f'_{+}$$ and $$f'_{-}$$ are defined with one-sided limits.

**Theorem.** Differentiable at $$x_0$$ $$\Rightarrow$$ continuous at $$x_0$$.

*Proof.* $$f(x) - f(x_0) = \frac{f(x)-f(x_0)}{x-x_0}\cdot(x - x_0) \to f'(x_0)\cdot 0 = 0$$.
$$\square$$

The converse fails at every corner, and §5.1's exercises show the failure can
be subtler than a corner.

**Theorem (algebra of derivatives).** If $$f, g$$ are differentiable at
$$x_0$$ then so are $$f+g$$, $$fg$$ and, when $$g(x_0) \ne 0$$, $$f/g$$, with

$$
\begin{aligned}
(f+g)' &= f' + g', \\
(fg)' &= f'g + fg', \\
\left(\frac fg\right)' &= \frac{f'g - fg'}{g^2}.
\end{aligned}
$$

**Theorem (chain rule).** If $$f$$ is differentiable at $$x_0$$ and $$g$$ is
differentiable at $$f(x_0)$$, then $$(g\circ f)'(x_0) = g'(f(x_0))f'(x_0)$$.

All are limit computations of the kind in §3.2 — the product rule is the
add-and-subtract-a-hybrid-term trick again.

### Suggested exercises

**5(c). Is $$g(x) = (x-2)\lfloor x\rfloor$$ differentiable at $$x_0 = 2$$?**

No. First, $$g(2) = 0$$, and $$g$$ *is* continuous at $$2$$ since the factor
$$(x-2)$$ kills the jump in $$\lfloor x\rfloor$$. But the one-sided difference
quotients differ. For $$2 < x < 3$$ we have $$\lfloor x\rfloor = 2$$, so

$$
\frac{g(x)-g(2)}{x-2} = \frac{2(x-2)}{x-2} = 2 ,
$$

while for $$1 < x < 2$$ we have $$\lfloor x \rfloor = 1$$ and the quotient is
$$1$$. So $$g'_{+}(2) = 2 \ne 1 = g'_{-}(2)$$. $$\square$$

**9. $$g(x) = x^2\sin\frac1x$$ for $$x \ne 0$$ and $$g(0) = 0$$.**

**(a) $$g$$ is differentiable at $$0$$ with $$g'(0) = 0$$.**

$$
\left\lvert\frac{g(h)-g(0)}{h}\right\rvert
 = \left\lvert h\sin\tfrac1h\right\rvert \le \lvert h\rvert \to 0 .
$$

**(b) $$g'$$ is not continuous at $$0$$.** For $$x \ne 0$$ the product and
chain rules give

$$
g'(x) = 2x\sin\tfrac1x - \cos\tfrac1x .
$$

The first term tends to $$0$$, but $$\cos\frac1x$$ has no limit as
$$x \to 0$$: along $$x_n = 1/(2n\pi)$$ it equals $$1$$ and along
$$x_n = 1/((2n+1)\pi)$$ it equals $$-1$$. So $$\lim_{x\to0}g'(x)$$ does not
exist, while $$g'(0) = 0$$. $$\square$$

> **This is the example to carry through the chapter.** A function can be
> differentiable everywhere and have a derivative that is not continuous
> anywhere near a point. It is why "differentiable" and "continuously
> differentiable" are different hypotheses, and it is what makes Darboux's
> theorem in §5.2 surprising rather than obvious.
{: .prompt-warning }

**15. The symmetric difference quotient.**

**(a) If $$f$$ is differentiable at an interior point $$x_0$$, then**

$$
\lim_{h\to0}\frac{f(x_0+h)-f(x_0-h)}{2h} = f'(x_0) .
$$

Split the quotient around $$f(x_0)$$:

$$
\begin{aligned}
&\frac{f(x_0+h)-f(x_0-h)}{2h} \\
&\quad = \frac12\cdot\frac{f(x_0+h)-f(x_0)}{h}
 + \frac12\cdot\frac{f(x_0)-f(x_0-h)}{h} .
\end{aligned}
$$

The first term tends to $$\tfrac12 f'(x_0)$$. In the second substitute
$$k = -h$$, turning it into
$$\tfrac12\frac{f(x_0+k)-f(x_0)}{k}$$ with $$k \to 0$$, which also tends to
$$\tfrac12 f'(x_0)$$. $$\square$$

**(b) If the symmetric limit exists, is $$f$$ differentiable at $$x_0$$?**
No. Take $$f(x) = \lvert x\rvert$$ at $$x_0 = 0$$: the symmetric quotient is

$$
\frac{\lvert h\rvert - \lvert -h\rvert}{2h} = 0
$$

for every $$h \ne 0$$, so the limit is $$0$$, yet $$f$$ is not differentiable
at $$0$$. Worse, $$f(x) = 1$$ for $$x \ne 0$$ with $$f(0) = 0$$ gives the same
symmetric limit while failing even to be continuous. **The symmetric quotient
cannot see an even failure**, because it cancels it.

---

## Part 2 — §5.2: the mean value theorem

### Interior extrema

**Definition.** Let $$E \subseteq \mathbb{R}$$ and $$f$$ real-valued on $$E$$.
Then $$f$$ has a **local maximum** at $$p \in E$$ when there is $$\delta > 0$$
with $$f(x) \le f(p)$$ for all $$x \in E \cap N_\delta(p)$$. Local minimum is
the mirror image.

**Theorem.** Let $$f$$ be defined on an interval $$I$$ with a local maximum or
minimum at $$p \in \operatorname{Int}(I)$$. If $$f$$ is differentiable at
$$p$$, then $$f'(p) = 0$$.

*Proof.* Say $$p$$ is a local maximum. For small $$h > 0$$,
$$\frac{f(p+h)-f(p)}{h} \le 0$$, so letting $$h \to 0+$$ gives
$$f'(p) \le 0$$. For small $$h < 0$$ the quotient is $$\ge 0$$, so
$$f'(p) \ge 0$$. $$\square$$

**Interiority is essential.** On $$[0,1]$$ the function $$f(x) = x$$ has a
maximum at $$1$$ and $$f'(1) = 1 \ne 0$$. The argument needs both one-sided
approaches to be available.

**Corollary.** If $$f$$ is continuous on $$[a,b]$$ with a relative extremum at
$$p \in (a,b)$$, then either $$f'(p)$$ fails to exist or $$f'(p) = 0$$. These
are the **critical points**, and the extreme value theorem of §4.2 guarantees
that on a closed bounded interval the extrema exist — so they are among the
critical points and the two endpoints. That is the whole of the optimisation
method from first-year calculus, now with both halves proved.

### Rolle, Lagrange, Cauchy

**Theorem (Rolle).** If $$f$$ is continuous on $$[a,b]$$, differentiable on
$$(a,b)$$, and $$f(a) = f(b)$$, then $$f'(c) = 0$$ for some $$c \in (a,b)$$.

*Proof.* $$f$$ is continuous on the compact set $$[a,b]$$, so by the extreme
value theorem it attains a maximum and a minimum. If both occur at endpoints
then, since $$f(a) = f(b)$$, the maximum equals the minimum and $$f$$ is
constant, so any interior $$c$$ works. Otherwise some extremum is attained at
an interior $$c$$, and the previous theorem gives $$f'(c) = 0$$. $$\square$$

**Theorem (mean value theorem).** If $$f$$ is continuous on $$[a,b]$$ and
differentiable on $$(a,b)$$, there is $$c \in (a,b)$$ with

$$
f(b) - f(a) = f'(c)(b-a) .
$$

*Proof.* Apply Rolle to

$$
g(x) = f(x) - f(a) - \frac{f(b)-f(a)}{b-a}(x-a) ,
$$

which is $$f$$ with the chord subtracted, so $$g(a) = g(b) = 0$$. $$\square$$

**Theorem (Cauchy mean value theorem).** If $$f, g$$ are continuous on
$$[a,b]$$ and differentiable on $$(a,b)$$, there is $$c \in (a,b)$$ with

$$
[f(b)-f(a)]\,g'(c) = [g(b)-g(a)]\,f'(c) .
$$

*Proof.* Apply Rolle to
$$h(x) = [f(b)-f(a)]g(x) - [g(b)-g(a)]f(x)$$, which has
$$h(a) = h(b) = f(b)g(a) - g(b)f(a)$$. $$\square$$

> **All three are Rolle's theorem, and Rolle is the extreme value theorem.**
> Each later statement is obtained by subtracting something from $$f$$ to make
> the endpoint values agree. The Cauchy form is written as a product rather
> than a ratio deliberately: as a ratio it would require $$g'(c) \ne 0$$, and
> the product form survives intact. [Calculus 1](/posts/calculus-1-taylor/)
> made the same point.
{: .prompt-tip }

**Worked example from the notes: $$\dfrac{x}{1+x} \le \ln(1+x) \le x$$.**

Fix $$x > 0$$ and apply the mean value theorem to $$f(t) = \ln(1+t)$$ on
$$[0,x]$$. Since $$f(0) = 0$$ and $$f'(t) = 1/(1+t)$$, there is
$$c \in (0,x)$$ with

$$
\ln(1+x) = \frac{x}{1+c} .
$$

Now $$0 < c < x$$ gives $$1 < 1+c < 1+x$$, hence
$$\frac{1}{1+x} < \frac{1}{1+c} < 1$$, and multiplying by $$x > 0$$,

$$
\frac{x}{1+x} < \ln(1+x) < x .
$$

Equality holds at $$x = 0$$. $$\square$$

This is the template for **every** inequality proof by the mean value theorem:
write the difference as $$f'(c)$$ times something, then bound $$f'(c)$$ using
only the range in which $$c$$ must lie.

### Two further theorems

**Theorem.** If $$f$$ is continuous on $$[a,b)$$, differentiable on $$(a,b)$$,
and $$\lim_{x\to a+}f'(x)$$ exists, then $$f'_{+}(a)$$ exists and equals it.

*Proof.* For $$x > a$$ the mean value theorem on $$[a,x]$$ gives
$$c_x \in (a,x)$$ with $$\frac{f(x)-f(a)}{x-a} = f'(c_x)$$. As $$x \to a+$$ we
have $$c_x \to a+$$, so the right side tends to the assumed limit. $$\square$$

**A derivative cannot have a removable discontinuity.** If
$$\lim_{x\to a}f'(x) = L$$ exists then $$f'(a) = L$$ automatically. Combined
with the next theorem, this strongly constrains how a derivative can misbehave.

**Theorem (Darboux: the intermediate value property for derivatives).** Let
$$f$$ be differentiable on $$[a,b]$$ with $$f'(a) < f'(b)$$. Then for every
$$\gamma$$ with $$f'(a) < \gamma < f'(b)$$ there is $$c \in (a,b)$$ with
$$f'(c) = \gamma$$.

*Proof.* Let $$g(x) = f(x) - \gamma x$$, so $$g'(a) < 0 < g'(b)$$. Since
$$g$$ is continuous on the compact $$[a,b]$$ it attains a minimum. It is not
at $$a$$: $$g'(a) < 0$$ means $$g$$ takes smaller values just to the right. It
is not at $$b$$: $$g'(b) > 0$$ means $$g$$ takes smaller values just to the
left. So the minimum is at some interior $$c$$, where $$g'(c) = 0$$, i.e.
$$f'(c) = \gamma$$. $$\square$$

> **Derivatives satisfy the conclusion of the intermediate value theorem
> without satisfying its hypothesis.** $$f'$$ need not be continuous —
> exercise 9 of §5.1 — and yet it cannot skip a value. In particular **no
> derivative has a jump discontinuity**, so $$\lfloor x\rfloor$$ is not the
> derivative of anything. A derivative that misbehaves must do so by
> oscillating, as $$\cos(1/x)$$ does.
{: .prompt-warning }

**Theorem (first derivative test).** *The notes say "you know it".* If $$f$$ is
continuous at $$c$$ and differentiable near it, and $$f'$$ changes sign from
negative to positive across $$c$$, then $$c$$ is a local minimum; positive to
negative gives a local maximum. The proof is the mean value theorem applied on
each side.

**Theorem (inverse function theorem).** *Also "you know it".* If $$f$$ is
differentiable on an interval with $$f'(x) \ne 0$$ throughout, then $$f$$ is
strictly monotone, $$f^{-1}$$ is differentiable on $$f(I)$$, and

$$
(f^{-1})'(y) = \frac{1}{f'(f^{-1}(y))} .
$$

Monotonicity follows from Darboux — $$f'$$ cannot change sign without
vanishing — plus the mean value theorem.

### Suggested exercises

**3(d). Where is $$k(x) = \sqrt x - \tfrac12 x$$, $$x \ge 0$$, increasing and
decreasing?**

For $$x > 0$$,

$$
k'(x) = \frac{1}{2\sqrt x} - \frac12 = \frac{1 - \sqrt x}{2\sqrt x} ,
$$

positive for $$0 < x < 1$$ and negative for $$x > 1$$. So $$k$$ increases on
$$[0,1]$$ and decreases on $$[1,\infty)$$, with a local — in fact global —
maximum $$k(1) = \tfrac12$$. The minimum on $$[0,\infty)$$ is $$k(0) = 0$$,
attained at an endpoint where $$k'$$ does not exist: $$k'(x) \to +\infty$$ as
$$x \to 0+$$. A reminder that the corollary above lists *both* kinds of
critical point.

**5(d). $$(1+x)^{\alpha} \ge 1 + \alpha x$$ for $$x > -1$$, $$\alpha > 1$$.**

Let $$f(x) = (1+x)^{\alpha} - 1 - \alpha x$$, so $$f(0) = 0$$ and

$$
f'(x) = \alpha\left[(1+x)^{\alpha-1} - 1\right] .
$$

Since $$\alpha - 1 > 0$$, the function $$t \mapsto t^{\alpha-1}$$ is increasing
on $$(0,\infty)$$, so $$(1+x)^{\alpha-1} > 1$$ for $$x > 0$$ and $$< 1$$ for
$$-1 < x < 0$$. Hence $$f' < 0$$ on $$(-1,0)$$ and $$f' > 0$$ on
$$(0,\infty)$$, so $$f$$ has a global minimum at $$0$$ with $$f(0) = 0$$.
Therefore $$f \ge 0$$. $$\square$$

This is **Bernoulli's inequality for real exponents**; the integer case was
proved by induction in [Chapter 1](/posts/analysis-real-numbers/). Calculus
replaces the induction.

**6(b). $$a^{\alpha}b^{1-\alpha} \le \alpha a + (1-\alpha)b$$ for
$$a, b > 0$$ and $$0 < \alpha < 1$$.**

Fix $$b$$ and set $$h(a) = \alpha a + (1-\alpha)b - a^{\alpha}b^{1-\alpha}$$.
Then

$$
h'(a) = \alpha - \alpha a^{\alpha-1}b^{1-\alpha}
 = \alpha\left[1 - \left(\tfrac ba\right)^{1-\alpha}\right] ,
$$

which is negative for $$a < b$$ and positive for $$a > b$$. So $$h$$ has a
global minimum at $$a = b$$, where $$h(b) = \alpha b + (1-\alpha)b - b = 0$$.
Hence $$h \ge 0$$. $$\square$$

This is **weighted AM–GM**, equivalently Young's inequality, and it is the
engine behind Hölder's inequality. It returns in
[Chapter 7](/posts/analysis-series/) for square summable sequences.

**7. Second derivative test.** $$f$$ differentiable on $$(a,b)$$,
$$c \in (a,b)$$ with $$f'(c) = 0$$ and $$f''(c)$$ existing.

**(a) $$f''(c) > 0$$ $$\Rightarrow$$ local minimum.** By definition

$$
f''(c) = \lim_{x\to c}\frac{f'(x)-f'(c)}{x-c} = \lim_{x\to c}\frac{f'(x)}{x-c} ,
$$

using $$f'(c) = 0$$. A limit that is positive forces the quotient to be
positive near $$c$$, so $$f'(x) < 0$$ for $$x$$ slightly below $$c$$ and
$$f'(x) > 0$$ slightly above. The mean value theorem then makes $$f$$
decreasing on the left and increasing on the right of $$c$$.

**(b)** Symmetric.

**(c) $$f''(c) = 0$$ decides nothing.** At $$c = 0$$ all three of
$$x^4$$ (minimum), $$-x^4$$ (maximum) and $$x^3$$ (neither) have
$$f'(0) = f''(0) = 0$$.

**11(a). $$f$$ differentiable on an interval $$I$$. Then $$f'$$ is bounded on
$$I$$ if and only if $$f$$ is Lipschitz.**

($$\Rightarrow$$) If $$\lvert f'\rvert \le M$$, the mean value theorem gives
$$c$$ between $$x$$ and $$y$$ with

$$
\lvert f(x)-f(y)\rvert = \lvert f'(c)\rvert\,\lvert x - y\rvert \le M\lvert x-y\rvert .
$$

($$\Leftarrow$$) If $$\lvert f(x)-f(y)\rvert \le M\lvert x-y\rvert$$ then every
difference quotient is bounded by $$M$$ in absolute value, so its limit
$$f'(x)$$ is too. $$\square$$

**This closes the loop with §4.3.** Lipschitz implies uniformly continuous was
proved there with no way to verify the hypothesis; the mean value theorem
supplies it from a bound on $$f'$$.

**14. $$f'$$ exists on $$(a,b)$$ and $$c \in (a,b)$$.**

**(a) There is a sequence $$x_n \to c$$ with $$x_n \ne c$$ and
$$f'(x_n) \to f'(c)$$.** Take $$h_n \to 0$$ with $$c + h_n \in (a,b)$$. The
mean value theorem on the interval between $$c$$ and $$c + h_n$$ gives
$$x_n$$ strictly between them with

$$
f'(x_n) = \frac{f(c+h_n)-f(c)}{h_n} \longrightarrow f'(c) ,
$$

and $$x_n \to c$$ by squeezing. $$\square$$

**(b) Does $$f'(x_n) \to f'(c)$$ for *every* $$x_n \to c$$?** No — that would
say $$f'$$ is continuous at $$c$$. Exercise 9 of §5.1 refutes it: with
$$g(x) = x^2\sin(1/x)$$ and $$c = 0$$ we have $$g'(0) = 0$$, but along
$$x_n = 1/(2n\pi)$$,

$$
g'(x_n) = 2x_n\sin(2n\pi) - \cos(2n\pi) = -1 \not\to 0 .
$$

So part (a) produces *some* good sequence, which is all the mean value theorem
can promise.

**8. If $$\lvert f(x)-f(y)\rvert \le M\lvert x-y\rvert^{\alpha}$$ on
$$(a,b)$$ with $$\alpha > 1$$, then $$f$$ is constant.**

For $$x \ne y$$,

$$
\left\lvert\frac{f(x)-f(y)}{x-y}\right\rvert \le M\lvert x-y\rvert^{\alpha-1} ,
$$

and $$\alpha - 1 > 0$$, so letting $$y \to x$$ gives $$f'(x) = 0$$ for every
$$x$$. The mean value theorem then makes $$f$$ constant on the interval.
$$\square$$

The exponent is everything. At $$\alpha = 1$$ this is the Lipschitz condition,
satisfied by plenty of non-constant functions; anything above $$1$$ collapses.

**19. If $$g$$ is differentiable on $$(a,b)$$ with
$$\lvert g'\rvert \le M$$, there is $$\varepsilon > 0$$ making
$$f(x) = x + \varepsilon g(x)$$ one-to-one.**

If $$M = 0$$ then $$g$$ is constant and any $$\varepsilon$$ works. Otherwise
take $$\varepsilon = 1/(2M)$$. Then

$$
f'(x) = 1 + \varepsilon g'(x) \ge 1 - \varepsilon M = \tfrac12 > 0 ,
$$

so by the mean value theorem $$f$$ is strictly increasing on $$(a,b)$$ and
hence injective. $$\square$$

A small perturbation of the identity stays injective, provided the
perturbation has bounded derivative — a one-dimensional shadow of the inverse
function theorem in several variables.

---

## Part 3 — §5.3: L'Hospital's rule

**Definition.** Let $$f$$ be real-valued on $$E \subseteq \mathbb{R}$$ and let
$$p$$ be a limit point of $$E$$. Then **$$f$$ diverges to $$\infty$$ at
$$p$$** when for every $$M \in \mathbb{R}$$ there is $$\delta > 0$$ with
$$f(x) > M$$ for all $$x \in N_\delta(p) \cap E$$, $$x \ne p$$.

**Theorem (L'Hospital's rule).** *The notes say "you know it, I believe".* Let
$$f, g$$ be differentiable on $$(a,b)$$ with $$g' \ne 0$$ there, and suppose
either

$$
\lim_{x\to a+} f(x) = \lim_{x\to a+} g(x) = 0
$$

or $$\lvert g(x)\rvert \to \infty$$. If
$$\lim_{x\to a+}\frac{f'(x)}{g'(x)} = L$$ exists, in $$\mathbb{R}$$ or as
$$\pm\infty$$, then

$$
\lim_{x\to a+}\frac{f(x)}{g(x)} = L .
$$

The same holds at $$b-$$ and at $$\pm\infty$$.

*Proof idea.* For the $$0/0$$ case, extend $$f$$ and $$g$$ by $$0$$ at $$a$$
and apply the **Cauchy** mean value theorem on $$[a,x]$$: there is
$$c_x \in (a,x)$$ with

$$
\frac{f(x)}{g(x)} = \frac{f(x)-f(a)}{g(x)-g(a)} = \frac{f'(c_x)}{g'(c_x)} ,
$$

and $$c_x \to a+$$ as $$x \to a+$$. That is the whole content, and it is why
the Cauchy form of the mean value theorem exists at all.

> **The implication runs one way only.** L'Hospital says *if*
> $$\lim f'/g'$$ exists *then* $$\lim f/g$$ equals it. If $$\lim f'/g'$$
> fails to exist, nothing follows — exercise 7 below is exactly that case, and
> it is the most common way the rule is misused.
{: .prompt-warning }

**Worked example from the notes: $$\displaystyle\lim_{x\to0+}\frac{e^{-1/x}}{x^2}$$.**

Substitute $$t = 1/x$$, so $$t \to +\infty$$ and the expression becomes

$$
t^2 e^{-t} = \frac{t^2}{e^{t}} \longrightarrow 0 ,
$$

since the exponential beats any polynomial — two applications of L'Hospital to
$$t^2/e^t$$ give $$2t/e^t$$ then $$2/e^t \to 0$$. So the limit is $$0$$.

Applying L'Hospital directly in $$x$$ would be a mistake: the expression is
$$0/0$$ in form, but differentiating makes it worse, since each derivative of
$$e^{-1/x}$$ brings down another factor of $$1/x^2$$. **Substituting first is
the move.**

### Suggested exercises

**6(a). $$\displaystyle\lim_{x\to1}\frac{x^5+2x-3}{2x^3-x^2-1}$$.**

Both numerator and denominator vanish at $$x = 1$$, so the form is $$0/0$$.
Differentiating,

$$
\lim_{x\to1}\frac{5x^4+2}{6x^2-2x} = \frac{7}{4} .
$$

The denominator $$6 - 2 = 4$$ is non-zero, so the rule applies and the answer
is $$\tfrac74$$. (Factoring out $$(x-1)$$ from both gives the same thing and is
arguably cleaner.)

**7. $$f(x) = x^2\sin\frac1x$$ and $$g(x) = \sin x$$: show
$$\lim_{x\to0}\frac{f}{g}$$ exists but $$\lim_{x\to0}\frac{f'}{g'}$$ does
not.**

For the first, split off the standard limit:

$$
\frac{f(x)}{g(x)} = \frac{x}{\sin x}\cdot x\sin\tfrac1x
 \longrightarrow 1 \cdot 0 = 0 ,
$$

since $$x/\sin x \to 1$$ and $$x\sin(1/x) \to 0$$ by bounded-times-null.

For the second, $$f'(x) = 2x\sin\frac1x - \cos\frac1x$$ and
$$g'(x) = \cos x \to 1$$, so

$$
\frac{f'(x)}{g'(x)} = \frac{2x\sin\frac1x - \cos\frac1x}{\cos x}
$$

has no limit as $$x \to 0$$, because $$\cos\frac1x$$ oscillates between
$$-1$$ and $$1$$ while everything else converges. $$\square$$

> **This is the counterexample that fixes the direction of the rule.** The
> limit of the quotient exists and equals $$0$$; the limit of the quotient of
> derivatives does not exist at all. L'Hospital was never applicable here, and
> concluding "the limit does not exist" from the failure of the right-hand side
> would be wrong.
{: .prompt-warning }

## Common pitfalls

- **Using L'Hospital in the wrong direction.** Failure of $$\lim f'/g'$$ says
  nothing about $$\lim f/g$$.
- **Applying L'Hospital without checking the form.** It needs $$0/0$$ or
  $$\infty$$ in the denominator, and $$g' \ne 0$$ near the point.
- **Expecting $$f'$$ to be continuous.** $$x^2\sin(1/x)$$ is the standard
  refutation, and it reappears in three different exercises for that reason.
- **Expecting $$f'$$ to be arbitrary.** Darboux forbids jump discontinuities,
  so not every function is a derivative.
- **Forgetting interiority in the extremum theorem.** At an endpoint the
  derivative need not vanish.
- **Reading the mean value theorem as giving a usable $$c$$.** You never learn
  where $$c$$ is. Every application bounds $$f'$$ over the whole interval
  instead.
- **Trusting the second derivative test at $$f''(c) = 0$$.** Three different
  outcomes are available.
- **Believing the symmetric difference quotient detects differentiability.**
  It cancels even failures, including discontinuities.

## Connections

- **Backward.** Rolle is the extreme value theorem of
  [Chapter 4](/posts/analysis-continuity/), so the mean value theorem is
  compactness in disguise; Darboux's proof is the same argument again. The
  Lipschitz criterion of exercise 11 supplies the hypothesis that §4.3 could
  only assume. Bernoulli's inequality is proved here for real exponents, where
  [Chapter 1](/posts/analysis-real-numbers/) could only do integers.
- **Forward.** [Chapter 6](/posts/analysis-integration/) uses the mean value
  theorem to prove the fundamental theorem of calculus, and the mean value
  theorem for integrals is its mirror image. The weighted AM–GM of exercise
  6(b) becomes Hölder's inequality in
  [Chapter 7](/posts/analysis-series/). Term-by-term differentiation of a
  series in [Chapter 8](/posts/analysis-function-sequences/) is where
  differentiability turns out to be the hardest operation to interchange with
  a limit.
- **Outward.** Taylor's theorem with the Lagrange remainder — covered in
  [Calculus 1](/posts/calculus-1-taylor/) — is the mean value theorem iterated,
  and the contraction mapping theorem uses exercise 19's estimate to solve
  equations.

## Summary

- **Derivative** — a limit of difference quotients; differentiable $$\Rightarrow$$ continuous, never the converse
- **$$x^2\sin(1/x)$$** — differentiable everywhere with discontinuous derivative
- **Symmetric quotient** — equals $$f'(x_0)$$ when that exists, and can exist when it does not
- **Interior extremum** $$\Rightarrow$$ $$f' = 0$$, if the derivative exists
- **Rolle** — equal endpoint values give a stationary point; it is the extreme value theorem
- **Mean value theorem** — $$f(b)-f(a) = f'(c)(b-a)$$; subtract the chord and apply Rolle
- **Cauchy MVT** — in product form, so no non-vanishing hypothesis is needed
- **Consequences** — $$f' > 0$$ gives increasing, $$f' = 0$$ gives constant, $$\lvert f'\rvert \le M$$ gives Lipschitz
- **Inequalities** — write the difference as $$f'(c)$$ times a length and bound $$f'$$
- **Darboux** — every derivative has the intermediate value property, so none has a jump
- **A derivative has no removable discontinuity** either
- **Second derivative test** — conclusive except when $$f''(c) = 0$$
- **L'Hospital** — via the Cauchy MVT; one-directional

## References

- Manfred Stoll, *Introduction to Real Analysis*, 2nd edition — Chapter 5. The suggested exercise numbers are Stoll's.
- Introduction to Mathematical Analysis, Spring 2023. Instructor: Ja A Jeong. Typed lecture notes, Chapter V.
- All proofs and all exercise solutions are mine; the notes leave every one blank.
- §5.1 contains **no theory in the notes** — only the three exercises. The definition of the derivative, differentiability implying continuity, the algebra of derivatives and the chain rule are supplied here from the textbook's standard treatment so the chapter is self-contained.
- The notes mark the first derivative test, the inverse function theorem and L'Hospital's rule as *"you know it"* and state nothing further. They are stated here, with a proof sketch for L'Hospital since the Cauchy mean value theorem exists precisely to prove it.
- One correction. The notes state Darboux's theorem as "Let $$f : [a,b] \to \mathbb{R}$$ be continuous and suppose $$f'(a) < f'(b)$$ … $$\exists c$$ with $$f(c) = \gamma$$". The hypothesis must be differentiability, not continuity, and the conclusion is $$f'(c) = \gamma$$; both are corrected above.
