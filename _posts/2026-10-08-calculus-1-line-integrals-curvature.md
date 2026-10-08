---
title: "Calculus 1: Line Integrals and Curvature"
date: 2026-10-08 10:00:00 +0900
categories: [Course Notes, Calculus 1]
tags: [line integral, curvature, centre of mass, osculating circle, unit tangent, unit normal]
description: Integrating along a curve — mass, averages and centres of mass — and curvature as the acceleration you would feel travelling at unit speed. Ends with the moving frame, the osculating circle, and why slow in, quick out feels right. Unit 7 of Calculus 1, the last.
math: true
mermaid: false
render_with_liquid: false
---

> This unit covers textbook §§9.7–9.8 and closes the course.
> [Unit 6](/posts/calculus-1-curves/) covers the rest of Chapter 9 and is a
> prerequisite for all of it.
{: .prompt-info }

## What this unit answers

Two questions, and both are about turning a curve into a number.

**What does a curve weigh?** A wire of length $$L$$ and uniform density
$$\mu$$ has mass $$\mu L$$. If the density varies from point to point, the
answer must be an integral — and the whole difficulty is that the variable of
integration should be *distance along the wire*, which no parametrization gives
you directly. The resolution is one substitution, and it produces the line
integral.

**How sharply does a curve bend?** Drive a bend at constant speed and you feel
pushed outward. Define the bending as the amount of push and the definition
fails immediately, because the push depends on your speed as well as on the
road. The fix is to fix the speed: **the bending of a curve is the magnitude of
the acceleration when you travel it at unit speed.** That is curvature, and
everything in the second half follows from making it computable without ever
constructing the unit-speed parametrization.

## Prerequisites

[Unit 6](/posts/calculus-1-curves/) throughout — arc length, reparametrization,
the osculating plane, the derivative-of-a-length formula, and the
arc-length parametrization that curvature is defined through. Centroids of
point masses come from [Unit 4](/posts/calculus-1-coordinates-vectors/), and
the cross product from Units 4 and 5 supplies the usable curvature formula.

---

## Part 1 — §9.7: line integrals, mass, and centre of mass

### The mass of a curve

A curve of length $$L$$ and uniform linear density $$\mu$$ has mass $$\mu L$$.
Given instead a density function $$f(X)$$, chop the curve $$C$$ into short
pieces, weigh each as though it were uniform, and refine:

$$
\lim_{\text{refine}} \sum f(P_i) \times (\text{length of piece } i).
$$

Now parametrize $$C$$ by $$X(t)$$, $$a \le t \le b$$. The $$i$$-th piece is
traversed in time $$\Delta t$$ at speed $$\lvert X'(t_i)\rvert$$, so its length
is $$\lvert X'(t_i)\rvert\Delta t$$ and the sum becomes a Riemann sum in $$t$$:

$$
\begin{aligned}
&\lim \sum f(P_i)\times(\text{length of piece } i) \\
&\quad = \lim \sum f(X(t_i))\,\lvert X'(t_i)\rvert\,\Delta t \\
&\quad = \int_a^b f(X(t))\,\lvert X'(t)\rvert\,\mathrm{d}t .
\end{aligned}
$$

That motivates the definition.

> **Definition.** The **line integral** (선적분) of a real-valued function
> $$f$$ along a curve $$C$$ parametrized by $$X(t)$$, $$a \le t \le b$$, is
>
> $$
> \int_C f\,\mathrm{d}s := \int_a^b f(X(t))\,\lvert X'(t)\rvert\,\mathrm{d}t .
> $$
{: .prompt-tip }

Four remarks, all of which matter.

- **Read the notation.** $$\mathrm{d}s$$ is *the length of an infinitesimally
  short piece of curve*, and $$\mathrm{d}s = \lvert X'(t)\rvert\,\mathrm{d}t$$
  says that this length is *speed times an infinitesimally short time*. The
  whole definition is that one substitution.
- **It is independent of the parametrization**, for orientation-preserving
  reparametrizations. Intuitively obvious — the proof is omitted — and it is
  what makes $$\int_C f\,\mathrm{d}s$$ a property of the curve rather than of
  the clock, exactly as length was in [Unit 6](/posts/calculus-1-curves/).
- **For it to mean mass, parametrize carefully.** The particle must not go over
  the same ground twice, or that stretch of wire gets weighed twice.
- **The constant function $$1$$ gives length.** $$\int_C \mathrm{d}s$$ is the
  length of $$C$$, which is the arc-length integral of Unit 6 with the weight
  removed.

### Averages

The average of a function defined on a curve is its integral divided by the
length:

$$
\bar f = \frac{\displaystyle\int_C f\,\mathrm{d}s}{\displaystyle\int_C \mathrm{d}s} .
$$

Numerator: the integral. Denominator: the length. The same shape as an average
of numbers, with counting replaced by measuring.

### Vector-valued integrands

A **vector-valued function** means something like

$$
\begin{aligned}
F(x,y) &= (x^2y,\ x\sin y), \\
G(x,y,z) &= (xyz,\ a^2z,\ \sin x\,e^{yz}).
\end{aligned}
$$

For $$F = (f_1, \ldots, f_n)$$ the line integral along $$C$$ is taken
componentwise, as every vector-valued integral in this course has been:

$$
\int_C F\,\mathrm{d}s := \left(\int_C f_1\,\mathrm{d}s,\ \ldots,\ \int_C f_n\,\mathrm{d}s\right).
$$

### The centre of mass of a curve

[Unit 4](/posts/calculus-1-coordinates-vectors/) did this for finitely many
point masses: the centre of mass $$G$$ of
$$A_1(m_1), \ldots, A_n(m_n)$$ in $$\mathbb{R}^n$$ is the point satisfying

$$
m_1\overrightarrow{GA_1} + \cdots + m_n\overrightarrow{GA_n} = 0 ,
$$

with total mass $$m_1 + \cdots + m_n$$, so that

$$
G = \frac{m_1A_1 + \cdots + m_nA_n}{m_1 + \cdots + m_n}.
$$

A curve is point mass distributed continuously. Replace the sum by a line
integral and the defining condition reads

$$
\int_C \mu(X)\,\overrightarrow{GX}\,\mathrm{d}s
 = \int_C \mu(X)(X - G)\,\mathrm{d}s = 0 ,
$$

with total mass $$\int_C \mu\,\mathrm{d}s$$. Solving,

$$
G = \frac{\displaystyle\int_C \mu(X)\,X\,\mathrm{d}s}{\displaystyle\int_C \mu(X)\,\mathrm{d}s}.
$$

For a plane curve, written out:

$$
\bar x = \frac{\int_C \mu x\,\mathrm{d}s}{\int_C \mu\,\mathrm{d}s},
\qquad
\bar y = \frac{\int_C \mu y\,\mathrm{d}s}{\int_C \mu\,\mathrm{d}s}.
$$

When $$\mu \equiv 1$$ the centre of mass is called the **geometric centre**:

$$
\bar x = \frac{\int_C x\,\mathrm{d}s}{\int_C \mathrm{d}s},
\qquad
\bar y = \frac{\int_C y\,\mathrm{d}s}{\int_C \mathrm{d}s}
$$

— the average position, in the sense of the previous subsection.

### Worked examples

The recipe never changes: **parametrize, differentiate, take the speed, mind
the interval, integrate if you can.**

**1. Integrate $$f(x,y) = x^2 + e^{y}$$ over $$x^2 + y^2 = 4$$.**

- Parametrize: $$X(t) = (2\cos t,\ 2\sin t)$$, $$0 \le t \le 2\pi$$.
- Velocity and speed: $$X'(t) = (-2\sin t,\ 2\cos t)$$,
  $$\lvert X'(t)\rvert \equiv 2$$.
- Write the integral, watching the interval:

  $$
  \int_C f\,\mathrm{d}s = \int_0^{2\pi}\left((2\cos t)^2 + e^{2\sin t}\right)\cdot 2\,\mathrm{d}t .
  $$

- Evaluate if possible. This one is not possible — $$e^{2\sin t}$$ has no
  elementary antiderivative. Setting the integral up correctly is the whole
  exercise.

**2. Integrate $$f(x,y) = x$$ over $$y = x^2$$, $$0 \le x \le 3$$.**

$$
\begin{aligned}
X(t) &= (t, t^2), \quad 0 \le t \le 3 \\
X'(t) &= (1, 2t), \quad \lvert X'(t)\rvert = \sqrt{1 + 4t^2} \\
\int_C f\,\mathrm{d}s &= \int_0^3 t\sqrt{1 + 4t^2}\,\mathrm{d}t
\end{aligned}
$$

This one is an easy substitution: $$u = 1 + 4t^2$$ gives
$$\frac{1}{12}\left(37^{3/2} - 1\right) \approx 18.7$$.

**3. Integrate $$f(x,y) = x$$ over $$y = \sqrt{x}$$, $$0 \le x \le 3$$.**
Parametrize by $$y$$ to avoid the square root:

$$
\begin{aligned}
X(t) &= (t^2, t), \quad 0 \le t \le \sqrt3 \\
X'(t) &= (2t, 1), \quad \lvert X'(t)\rvert = \sqrt{4t^2 + 1} \\
\int_C f\,\mathrm{d}s &= \int_0^{\sqrt3} t^2\sqrt{4t^2 + 1}\,\mathrm{d}t
\end{aligned}
$$

> **An open question from the notes.** Against this integral the lectures wrote:
> *it looks to me as though this one cannot be evaluated. What do you think?*
>
> It can. Substituting $$2t = \sinh u$$ turns it into
> $$\frac{1}{8}\int \sinh^2 u\cosh^2 u\,\mathrm{d}u = \frac{1}{32}\int\sinh^2 2u\,\mathrm{d}u$$,
> which integrates to
> $$\frac{1}{256}\sinh 4u - \frac{1}{64}u$$ with
> $$u = \operatorname{arcsinh} 2t$$. The value is about $$4.84$$. The
> difference from example 1 is real, though: there the obstruction is
> $$e^{2\sin t}$$, which genuinely has no elementary antiderivative, while here
> the integrand is an algebraic function of $$t$$ and the hyperbolic
> substitution always closes it.
{: .prompt-tip }

**4. The centre of the upper half of the unit circle.**

$$
\begin{aligned}
X(t) &= (\cos t, \sin t), \quad 0 \le t \le \pi \\
X'(t) &= (-\sin t, \cos t), \quad \lvert X'(t)\rvert \equiv 1
\end{aligned}
$$

By symmetry $$\bar x = 0$$, and the length is $$\pi$$, so

$$
\bar y = \frac{\displaystyle\int_C y\,\mathrm{d}s}{\pi}
 = \frac{\displaystyle\int_0^{\pi}\sin t\,\mathrm{d}t}{\pi} = \frac{2}{\pi}.
$$

About $$0.64$$ — below the top of the arc, as it must be, and not the $$0.5$$ a
filled half-disc would give, because a wire has all its mass out on the rim.

---

## Part 2 — §9.8: curvature

### Defining it

We want a real number measuring how bent a curve is at a point. Driving a
curved road at constant speed, you feel your body thrown outward; why not
define the bending as the amount of that throw?

Because it is not well defined: the throw depends on the speed as well as on
the road. So fix the speed. The answer, as the lectures put it, *you have
probably already guessed*:

> *The bending of a curve is the magnitude of the acceleration when you travel
> it at constant speed $$1$$.*
{: .prompt-tip }

**Definition.** For a curve $$Y(s)$$ parametrized by arc length, at the point
$$Y(s)$$,

$$
\begin{aligned}
\text{curvature vector:}\quad &\boldsymbol\kappa = Y''(s) \\
\text{curvature:}\quad &\kappa = \lvert Y''(s)\rvert
\end{aligned}
$$

Observe that the curvature vector lies in the osculating plane — it is a second
derivative, which is one of the two vectors spanning that plane — and that it is
perpendicular to the velocity, because the speed is constant and
[Unit 6](/posts/calculus-1-curves/) showed constant speed forces
$$Y'\cdot Y'' \equiv 0$$.

### Making it computable

Can we find the curvature vector of $$y = x^2$$ at $$(1,1)$$? An awkward
feeling sets in, because Unit 6 tried to parametrize the parabola by arc length
and **gave up**. The definition is unusable as it stands. We need the curvature
of a curve given by *any* parametrization.

Let $$X(t)$$ be the curve and $$Y(s)$$ its arc-length reparametrization. Since
$$Y'(s)$$ is parallel to $$X'(t)$$ and has length $$1$$,

$$
Y'(s) = \frac{X'(t)}{\lvert X'(t)\rvert} .
$$

Now use the chain rule
$$\frac{\mathrm d}{\mathrm ds} = \frac{\mathrm dt}{\mathrm ds}\frac{\mathrm d}{\mathrm dt}$$
together with $$\frac{\mathrm ds}{\mathrm dt} = \lvert X'(t)\rvert$$ and the
inverse function rule
$$\frac{\mathrm dt}{\mathrm ds} = 1\big/\frac{\mathrm ds}{\mathrm dt}$$:

$$
\begin{aligned}
\boldsymbol\kappa = Y''(s)
 &= \frac{\mathrm d}{\mathrm ds}\left(\frac{X'}{\lvert X'\rvert}\right) \\
 &= \frac{\mathrm d}{\mathrm dt}\left(\frac{X'}{\lvert X'\rvert}\right)\frac{\mathrm dt}{\mathrm ds} \\
 &= \frac{1}{\lvert X'(t)\rvert}\left(\frac{X'(t)}{\lvert X'(t)\rvert}\right)' .
\end{aligned}
$$

That is already a usable formula. Pushing it further needs only the
derivative-of-a-length identity from
[Unit 6](/posts/calculus-1-curves/),
$$\frac{\mathrm d}{\mathrm dt}\lvert v\rvert = \frac{v\cdot v'}{\lvert v\rvert}$$,
and the quotient rule:

$$
\begin{aligned}
\boldsymbol\kappa
 &= \frac{1}{\lvert X'\rvert}\left(\frac{X'}{\lvert X'\rvert}\right)' \\
 &= \frac{1}{\lvert X'\rvert}\left(\frac{X''\lvert X'\rvert - X'\frac{\mathrm d}{\mathrm dt}\lvert X'\rvert}{\lvert X'\rvert^2}\right) \\
 &= \frac{1}{\lvert X'\rvert^2}X'' - \frac{\frac{\mathrm d}{\mathrm dt}\lvert X'\rvert}{\lvert X'\rvert^3}X' \\
 &= \frac{1}{\lvert X'\rvert^2}X'' - \frac{X'\cdot X''}{\lvert X'\rvert^4}X' .
\end{aligned}
$$

Rearranged, the same statement reads

$$
\lvert X'\rvert^2 X'' = \lvert X'\rvert^4\boldsymbol\kappa + (X'\cdot X'')X'
$$

or

$$
X'' = \lvert X'\rvert^2\boldsymbol\kappa
 + \left(\frac{\mathrm d}{\mathrm dt}\lvert X'\rvert\right)\frac{X'}{\lvert X'\rvert}.
$$

The last form is worth reading before moving on: the acceleration splits into a
piece along the curvature vector and a piece along the velocity. Turning, and
speeding up.

### Curvature without the curvature vector

Usually only the number is wanted. Use the fact that $$\boldsymbol\kappa$$ and
$$X'$$ are perpendicular, so that squaring the rearranged identity kills the
cross term:

$$
\begin{aligned}
\big\lvert \lvert X'\rvert^2X''\big\rvert^2
 &= \big\lvert \lvert X'\rvert^4\boldsymbol\kappa + (X''\cdot X')X'\big\rvert^2 \\
\Rightarrow\ \lvert X'\rvert^4\lvert X''\rvert^2
 &= \lvert X'\rvert^8\kappa^2 + (X''\cdot X')^2\lvert X'\rvert^2 .
\end{aligned}
$$

Solving for $$\kappa$$ and recognising the Lagrange identity from
[Unit 4](/posts/calculus-1-coordinates-vectors/) —
$$\lvert a\times b\rvert^2 = \lvert a\rvert^2\lvert b\rvert^2 - (a\cdot b)^2$$ —

$$
\begin{aligned}
\kappa &= \frac{\sqrt{\lvert X'\rvert^2\lvert X''\rvert^2 - (X'\cdot X'')^2}}{\lvert X'\rvert^3} \\
 &= \frac{\lvert X' \times X''\rvert}{\lvert X'\rvert^3}.
\end{aligned}
$$

> This is the formula to use in a computation. The lectures said so explicitly:
> on the final examination it may be used without proof, unless a proof is
> asked for.
{: .prompt-info }

### The moving frame, and slow in quick out

Since $$X'$$ and $$\boldsymbol\kappa$$ are perpendicular, normalising both gives
an orthonormal pair:

$$
t = \frac{X'}{\lvert X'\rvert}, \qquad n = \frac{\boldsymbol\kappa}{\kappa} .
$$

$$t$$ is the **unit tangent vector** and $$n$$ the **unit normal vector**.
Writing the speed as $$\lvert X'(t)\rvert = v(t)$$, the decomposition of the
acceleration becomes

$$
X'' = \kappa v^2\,n + v'\,t .
$$

Every driving sensation is in that line. Now cash it out.

Anyone with a little driving experience, taking a short bend, slows down
*before* entering the curve (**slow in**) and accelerates once inside it to
leave a little quickly (**quick out**). Why drive that way? Because the body
asks for it — it feels comfortable. Here is why.

1. The body feels a force opposite to the acceleration,
   $$-mX'' = -m\kappa v^2 n - mv't$$.
2. The **normal** component $$-m\kappa v^2 n$$ throws the body sideways, which
   is uncomfortable. It carries $$v^2$$, so slowing down helps — and helps
   quadratically.
3. The **tangential** component $$-mv't$$ presses the body back into the seat,
   which is comfortable. So accelerating, making $$v'$$ large, helps — but only
   briefly, since the speed must not get large.

Slow in, quick out is the strategy that keeps $$\kappa v^2$$ small where
$$\kappa$$ is large and spends the discomfort budget on $$v'$$ instead. And it
is why a road must be $$C^2$$, as [Unit 6](/posts/calculus-1-curves/) insisted:
if $$\kappa$$ jumps, so does the sideways force, and no amount of slowing down
smooths it out.

### The formulas, collected

- **Definition**, for $$Y(s)$$ by arc length —
  $$\boldsymbol\kappa = Y''(s)$$, $$\kappa = \lvert Y''(s)\rvert$$
- **Any parametrization** —
  $$\boldsymbol\kappa = \dfrac{1}{\lvert X'\rvert}\left(\dfrac{X'}{\lvert X'\rvert}\right)'$$
- **Expanded** —
  $$\boldsymbol\kappa = \dfrac{1}{\lvert X'\rvert^2}X'' - \dfrac{\frac{\mathrm d}{\mathrm dt}\lvert X'\rvert}{\lvert X'\rvert^3}X'$$
- **Equivalently** —
  $$\boldsymbol\kappa = \dfrac{1}{\lvert X'\rvert^2}X'' - \dfrac{X'\cdot X''}{\lvert X'\rvert^4}X'$$
- **The curvature formula** —
  $$\kappa = \dfrac{\lvert X'\times X''\rvert}{\lvert X'\rvert^3}$$
- **Acceleration in the moving frame** —
  $$X'' = \kappa v^2 n + v't$$

### Worked examples

**1. A line** has curvature $$0$$ everywhere.

**2. A circle** of radius $$r$$ has curvature $$1/r$$ everywhere. With
$$X(t) = (r\cos t, r\sin t)$$ we get $$\lvert X'\rvert = r$$,
$$\lvert X''\rvert = r$$ and $$X'\cdot X'' = 0$$, so

$$
\kappa = \frac{\sqrt{r^2\cdot r^2 - 0}}{r^3} = \frac{1}{r}.
$$

Small circles bend hard. For any curve, the **radius of curvature** (곡률반경)
is defined as $$1/\kappa$$, which is the radius of the circle that bends the
same amount.

**3. The helix** $$X(t) = (a\cos t, a\sin t, bt)$$:
$$\lvert X'\rvert = \sqrt{a^2+b^2}$$, $$\lvert X''\rvert = a$$,
$$X'\cdot X'' = 0$$, so

$$
\kappa = \frac{a\sqrt{a^2+b^2}}{(a^2+b^2)^{3/2}} = \frac{a}{a^2 + b^2},
$$

constant along the helix — and recovering $$1/a$$ when $$b = 0$$, as a circle
should.

**4. The cycloid** $$X(t) = (t - \sin t, 1 - \cos t)$$, $$0 \le t \le 2\pi$$:

$$
\begin{cases}
X' = (1 - \cos t,\ \sin t) \\
X'' = (\sin t,\ \cos t) \\
X'\cdot X'' = \sin t
\end{cases}
$$

$$
\begin{aligned}
\Rightarrow\ \kappa
 &= \frac{\sqrt{(2 - 2\cos t) - \sin^2 t}}{\{2\sin(t/2)\}^3} \\
 &= \frac{\sqrt{(1 - \cos t)^2}}{\{2\sin(t/2)\}^3} \\
 &= \frac{2\sin^2(t/2)}{8\sin^3(t/2)} = \frac{1}{4\sin(t/2)} .
\end{aligned}
$$

So $$\lim_{t\to 0+}\kappa = \infty$$.

> The notes record the lecturer as still unsatisfied: *I have yet to produce a
> proper explanation of this fact.* One honest observation, which is not
> presented as that explanation: Unit 6 computed the unit tangent at the cusp
> to be $$(0,1)$$ leaving and $$(0,-1)$$ arriving. The direction of travel
> reverses through $$\pi$$ across a point where zero arc length is accumulated,
> and curvature is turning per unit arc length. An infinite value is what that
> arithmetic has to give.
{: .prompt-warning }

**5–8. The cases the notes list as headings.** Four more parametrizations are
written down with no answer attached, as exercises. The standard results, for
reference:

- **Graph** $$X(t) = (t, f(t))$$:
  $$\kappa = \dfrac{\lvert f''\rvert}{(1 + f'^2)^{3/2}}$$.
- **Catenary** $$y = \frac1a\cosh ax$$: from the graph formula,
  $$\kappa = \dfrac{a}{\cosh^2 ax} = \dfrac{1}{a y^2}$$.
- **Ellipse** $$X(t) = (a\cos t, b\sin t)$$: the cross product is the constant
  $$ab$$, so $$\kappa = \dfrac{ab}{(a^2\sin^2 t + b^2\cos^2 t)^{3/2}}$$ —
  largest at the ends of the major axis.
- **Polar** $$X(\theta) = r(\theta)(\cos\theta, \sin\theta)$$:
  $$\kappa = \dfrac{\lvert r^2 + 2r'^2 - rr''\rvert}{(r^2 + r'^2)^{3/2}}$$,
  which gives $$1/R$$ for $$r \equiv R$$.

### The osculating circle

The **osculating circle** (접촉원) at a point $$P$$ of a curve is the circle
tangent to the curve at $$P$$ that

1. lies in the osculating plane,
2. has radius $$\dfrac{1}{\text{curvature}}$$, and
3. has its centre $$O$$ on the side the curve bends towards — that is,
   $$\overrightarrow{PO}$$ points the same way as the curvature vector.

Its centre is therefore at

$$
P + \frac{\boldsymbol\kappa(P)}{\kappa(P)^2}
 \qquad \left(= P + \frac{1}{\kappa}\,n\right),
$$

one radius from $$P$$ along the unit normal. **The osculating circle is the
circle that fits the curve most closely** — it matches position, tangent
direction and curvature, which is as much as a circle can match.

That is the last definition of the course, and it is a fitting one. Unit 3
approximated a function near a point by a polynomial that matched its
derivatives; Unit 7 approximates a curve near a point by a circle that matches
its derivatives. Same idea, different category.

## Common pitfalls

- **Forgetting the speed factor.** $$\int_C f\,\mathrm{d}s$$ is *not*
  $$\int f(X(t))\,\mathrm{d}t$$. The $$\lvert X'(t)\rvert$$ is the whole content
  of the definition.
- **Parametrizing over the curve twice.** Running $$0 \le t \le 4\pi$$ around a
  circle doubles the mass. For a line integral to be a mass, the
  parametrization must be injective.
- **Taking the centre of mass of a wire to be that of the region it bounds.**
  The upper unit semicircle has $$\bar y = 2/\pi \approx 0.64$$; the filled
  half-disc has $$4/(3\pi) \approx 0.42$$. Different objects.
- **Using the arc-length definition of curvature to compute.** You will almost
  never have $$Y(s)$$. Use
  $$\kappa = \lvert X'\times X''\rvert/\lvert X'\rvert^3$$.
- **Cubing the wrong thing.** The denominator is $$\lvert X'\rvert^3$$, not
  $$\lvert X'\rvert^2$$ — dimensionally, curvature is one over a length.
- **Assuming $$\lvert X''\rvert$$ is the curvature.** It is only when the speed
  is $$1$$. Otherwise $$X''$$ also contains the $$v't$$ term, which has nothing
  to do with bending.
- **Expecting $$C^1$$ to be enough for a smooth ride.** Curvature is a second
  derivative. Two circular arcs joined tangentially are $$C^1$$ and still jolt.

## Connections

- **Backward.** The line integral is [Unit 6](/posts/calculus-1-curves/)'s arc
  length with a weight attached, and the centre of mass is
  [Unit 4](/posts/calculus-1-coordinates-vectors/)'s centroid with the sum
  replaced by an integral. Curvature is defined through Unit 6's arc-length
  parametrization and computed through Unit 6's derivative-of-a-length formula;
  the usable formula is the Lagrange identity of Unit 4, which
  [Unit 5](/posts/calculus-1-determinants/) turned into a determinant.
- **Across the course.** The osculating circle is Taylor's theorem of
  [Unit 3](/posts/calculus-1-taylor/) for curves: match as many derivatives as
  the approximating object has freedom for. The tangent line matches one, the
  osculating circle matches two.
- **Forward.** $$\mathrm{d}s = \lvert X'\rvert\,\mathrm{d}t$$ becomes
  $$\mathrm{d}A$$ and $$\mathrm{d}V$$ in Mathematics 2, where the Jacobian that
  closed [Unit 5](/posts/calculus-1-determinants/) supplies the factor. The
  moving frame $$(t, n)$$ gains a third vector, the binormal, and the
  Frenet–Serret formulas add torsion to curvature — at which point a space
  curve is determined, up to rigid motion, by two functions of arc length.

## Summary

**Line integrals**

- **Definition** — $$\int_C f\,\mathrm{d}s = \int_a^b f(X(t))\lvert X'(t)\rvert\,\mathrm{d}t$$
- **Reading it** — $$\mathrm{d}s = \lvert X'(t)\rvert\,\mathrm{d}t$$: length is speed times time
- **Invariance** — unchanged by orientation-preserving reparametrization
- **Length** — $$\int_C \mathrm{d}s$$
- **Average** — $$\bar f = \int_C f\,\mathrm{d}s \big/ \int_C \mathrm{d}s$$
- **Vector-valued** — componentwise
- **Centre of mass** — $$G = \int_C \mu X\,\mathrm{d}s \big/ \int_C \mu\,\mathrm{d}s$$; geometric centre is the case $$\mu \equiv 1$$
- **Method** — parametrize, differentiate, take the speed, fix the interval, integrate

**Curvature**

- **Idea** — the magnitude of the acceleration at unit speed
- **Definition** — $$\boldsymbol\kappa = Y''(s)$$, $$\kappa = \lvert Y''(s)\rvert$$ for $$Y$$ by arc length
- **Computation** — $$\kappa = \lvert X'\times X''\rvert / \lvert X'\rvert^3$$
- **Perpendicularity** — $$\boldsymbol\kappa \perp X'$$, and $$\boldsymbol\kappa$$ lies in the osculating plane
- **Moving frame** — $$t = X'/\lvert X'\rvert$$, $$n = \boldsymbol\kappa/\kappa$$, and $$X'' = \kappa v^2 n + v't$$
- **Line** $$0$$; **circle of radius $$r$$** $$1/r$$; **helix** $$a/(a^2+b^2)$$; **cycloid** $$1/(4\sin(t/2))$$
- **Graph** — $$\lvert f''\rvert/(1+f'^2)^{3/2}$$
- **Radius of curvature** — $$1/\kappa$$
- **Osculating circle** — radius $$1/\kappa$$, centre $$P + \boldsymbol\kappa/\kappa^2$$, in the osculating plane

## References

- Hong Jong Kim, *Calculus 1+* (미적분학 1+), 2nd revised edition, Seoul National University Press — §§9.7–9.8.
- Mathematics 1 (수학 1, L0442.000100), Seoul National University, Spring 2022. Instructor: Choi Hyung Gyu (최형규). Lecture notes for Chapter 9 dated 28 April 2022.
- The answer to the open question in worked example 3 is supplied here; the notes pose it and leave it to the reader. The observation about the cycloid's infinite curvature is likewise added, and is explicitly not the explanation the notes were looking for.
- Curvature results for the graph, catenary, ellipse and polar cases are standard and are supplied here; the notes list those four as headings with no worked answer, as exercises.
- Two transcription slips in the notes are corrected silently in the derivations above: the tangential force in the slow-in-quick-out argument is $$-mv't$$, not $$-m\kappa v't$$; and the cycloid's curvature radicand is $$1 - 2\cos t + \cos^2 t$$, which is $$(1-\cos t)^2$$ as the next line of the notes states.
