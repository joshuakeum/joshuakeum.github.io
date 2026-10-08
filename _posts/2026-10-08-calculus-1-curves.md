---
title: "Calculus 1: Parametrized Curves and Arc Length"
date: 2026-10-08 09:00:00 +0900
categories: [Course Notes, Calculus 1]
tags: [parametrized curves, cycloid, velocity, arc length, reparametrization, polar coordinates]
description: A curve is a moving particle, not a picture. Velocity and acceleration, the osculating plane, angular momentum and the law of equal areas, the length of a curve, and why parametrizing by arc length is almost always a waste of effort. Unit 6 of Calculus 1.
math: true
mermaid: false
render_with_liquid: false
---

> This unit covers textbook §§9.1–9.6. The rest of Chapter 9 — line integrals
> and curvature — is [Unit 7](/posts/calculus-1-line-integrals-curvature/).
{: .prompt-info }

## What this unit answers

Up to now a curve has been a *set*: the points satisfying
$$x^2 + y^2 = R^2$$, the graph of $$y = x^2$$, the solutions of a pair of
linear equations. Chapter 9 replaces that picture with a different one. A curve
is **a particle moving**, and the object of study is the map
$$t \mapsto X(t)$$ rather than its image.

The shift is not cosmetic. Three questions that are meaningless for a point set
become natural once there is a clock:

- **Is this curve differentiable?** The chapter's answer is that the question is
  badly posed until a parametrization is chosen — and that the same point set
  can have both a non-differentiable parametrization and a differentiable one.
- **How long is it?** Length is the integral of speed. That it does not depend
  on which clock you used is the content of reparametrization.
- **Why does a planet sweep out equal areas in equal times?** Because the force
  points at the sun, so a certain cross product has zero derivative. Three lines
  of [Unit 5](/posts/calculus-1-determinants/) algebra.

## Prerequisites

[Unit 4](/posts/calculus-1-coordinates-vectors/) for the inner product, the
cross product, polar and cylindrical coordinates, and centroids;
[Unit 5](/posts/calculus-1-determinants/) for the determinant, which writes the
osculating plane in one line. Single-variable differentiation and integration
throughout.

---

## Part 1 — §9.1: parametrized curves

### Representation and parametrization

Most curves arrive as an equation and have to be converted into a motion. Three
in rectangular coordinates:

- **Circle.** $$x^2 + y^2 = R^2$$ becomes $$X(t) = (R\cos t,\ R\sin t)$$.
- **Line.** $$\frac{x-1}{2} = \frac{y-4}{3} = \frac{z-2}{5}$$ becomes
  $$X(t) = (1+2t,\ 4+3t,\ 2+5t)$$.
- **Graph.** $$y = x^2$$ becomes $$X(t) = (t,\ t^2)$$.

Three in polar coordinates, where the recipe
$$r = f(\theta) \mapsto X(t) = f(t)(\cos t, \sin t)$$ does all the work:

- **General.** $$r = f(\theta)$$ becomes
  $$X(t) = (f(t)\cos t,\ f(t)\sin t)$$.
- **Logarithmic spiral.** $$r = e^{\theta}$$ becomes
  $$X(t) = (e^{t}\cos t,\ e^{t}\sin t)$$.
- **Four-petal rose.** $$r = \cos 2\theta$$ becomes
  $$X(t) = (\cos 2t \cos t,\ \cos 2t \sin t)$$.

And two that would be awkward to describe any other way:

$$
\begin{aligned}
\text{helix (나선):} \quad & X(t) = (\cos t,\ \sin t,\ t) \\
\text{cycloid:} \quad & X(t) = (t - \sin t,\ 1 - \cos t)
\end{aligned}
$$

Seen from above, the helix is uniform circular motion; the third coordinate
just climbs. English has two words for the shape, *spiral* and *helix*, where
Korean has one.

In general a parametrized curve is

$$
X(t) = (x_1(t), \ldots, x_n(t)) \in \mathbb{R}^n ,
$$

with $$t$$ the **parameter** (매개변수), usually time. A parametrized curve
describes the motion of a particle.

### Same curve or different?

A parametrized curve is usually just called a curve, and almost always that is
harmless. The sentence to internalise is a loose one, deliberately:

> *The following two parametrizations parametrize the same curve.*
>
> $$
> \begin{aligned}
> X_1(t) &= (\cos t, \sin t), \quad 0 \le t \le 2\pi, \\
> X_2(t) &= (\cos 2t, \sin 2t), \quad 0 \le t \le \pi .
> \end{aligned}
> $$
{: .prompt-tip }

One lap in $$2\pi$$ units of time, one lap in $$\pi$$. Same point set, different
motion. Which of the two you mean matters for velocity and does not matter for
length — and sorting out exactly which is which is what §9.4 and §9.5 do.

### Uniform circular motion

Radius $$r$$, angular speed $$\omega$$, starting at $$r(\cos\alpha, \sin\alpha)$$:

$$
\begin{aligned}
\text{positive (counterclockwise):}& \\
X(t) &= r(\cos(\omega t + \alpha),\ \sin(\omega t + \alpha)), \\
\text{negative (clockwise):}& \\
X(t) &= r(\cos(-\omega t + \alpha),\ \sin(-\omega t + \alpha)).
\end{aligned}
$$

The sign of $$\omega t$$ is the whole difference between the two directions.

### The cycloid

A wheel lies in the plane and rolls. Let $$O(t)$$ be the motion of its centre
and $$\omega$$ the angular speed of its rotation about that centre. A point at
distance $$d$$ from the centre moves along

$$
X(t) = O(t) + d(\cos(\varepsilon\omega t + \alpha),\ \sin(\varepsilon\omega t + \alpha)),
$$

with $$\varepsilon = \pm 1$$ fixing the sense of rotation. When the wheel rolls
along a straight line without slipping, the track of a point **on the rim** is
the **cycloid** (싸이클로이드). For the unit wheel rolling along the
$$x$$-axis, the centre is at $$(t, 1)$$ and the rim point starts at the bottom:

$$
\begin{aligned}
X(t) &= (t, 1) + \left(\cos\left(-t - \tfrac{\pi}{2}\right),\ \sin\left(-t - \tfrac{\pi}{2}\right)\right) \\
&= (t - \sin t,\ 1 - \cos t).
\end{aligned}
$$

The two phase shifts are what make the parametrization come out this clean, and
the cycloid is the running example of the entire chapter — it turns up again
under area, under length, under arc-length parametrization and under curvature,
behaving surprisingly each time.

### Differentiability belongs to the parametrization

A curve $$X(t) = (x_1(t), \ldots, x_n(t))$$ is **differentiable** — or of class
$$C^1$$, $$C^2$$, and so on — when each component function $$x_i$$ is.

Now a trap. *Is the curve $$y = \lvert x \rvert$$ differentiable?*

The question is malformed. Differentiability is a property of a
parametrization, and none was given. Ask it properly: **does the curve
$$y = \lvert x\rvert$$ admit a differentiable parametrization?** It does.

$$
X(t) = (t,\ \lvert t \rvert), \qquad Y(t) = (t\lvert t \rvert,\ t^2).
$$

These parametrize the same point set. $$X$$ is not differentiable at $$0$$;
$$Y$$ is. The curve has a corner, and a corner does not prevent a
differentiable parametrization from existing — it only forces the particle to
come to a **complete stop** there. Do not confuse the corner in the graph of
$$y = f(x)$$ with a failure of the curve.

### Velocity, acceleration, speed

For a twice-differentiable curve $$X(t)$$:

$$
\begin{aligned}
\text{velocity (속도벡터):}\quad & v(t) = X'(t) \\
\text{acceleration (가속도벡터):}\quad & a(t) = X''(t) \\
\text{speed (속력):}\quad & v(t) = \lvert v(t) \rvert \\
\text{magnitude of acceleration:}\quad & a(t) = \lvert a(t) \rvert
\end{aligned}
$$

The notation deliberately overloads: bold-or-not, $$v$$ is a vector and $$v$$
is its length. Textbooks here write the position vector $$X(t)$$; physics books
write $$r(t)$$.

**Regular curve** (정규곡선). A differentiable curve whose speed is never zero.
When someone calls a curve with no given parametrization *regular*, they mean a
regular parametrization exists. **A curve with a corner is not regular** — by
the previous subsection the particle must stop there, so some parametrization
may be differentiable but none can be regular.

### Worked examples

**1. Circular motion.** Radius $$r$$, angular speed $$\omega$$:

$$
\begin{aligned}
X(t) &= (r\cos\omega t,\ r\sin\omega t) \\
\Rightarrow\ v(t) &= r\omega(-\sin\omega t,\ \cos\omega t), \quad \lvert v \rvert = r\omega \\
a(t) &= r\omega^2(-\cos\omega t,\ -\sin\omega t), \quad \lvert a \rvert = r\omega^2
\end{aligned}
$$

The acceleration points at the origin and has magnitude $$r\omega^2$$. That is
centripetal acceleration, derived rather than asserted.

**2. Constant acceleration.** Given $$v(0) = v_0$$ and $$r(0) = r_0$$,

$$
\begin{aligned}
a(t) = a_0 \ &\Rightarrow\ v(t) = v_0 + a_0 t \\
 &\Rightarrow\ r(t) = r_0 + v_0 t + \tfrac12 a_0 t^2 .
\end{aligned}
$$

The projectile formula, now as vectors, in any dimension.

**3. The corner really stops the particle.** For $$y = \lvert x \rvert$$ with
$$Y(t) = (t\lvert t\rvert, t^2)$$,

$$
Y(t) = \begin{cases}
(t^2, t^2), & t > 0 \\
(0,0), & t = 0 \\
(-t^2, t^2), & t < 0
\end{cases}
\ \Rightarrow\
Y'(t) = \begin{cases}
(2t, 2t), & t > 0 \\
(0,0), & t = 0 \\
(-2t, 2t), & t < 0
\end{cases}
$$

because $$\lim_{h\to 0}\frac{h\lvert h\rvert - 0}{h} = 0$$. So $$Y'(0) = (0,0)$$
— the particle halts, exactly as predicted. The curve is differentiable, and
not regular.

**4. The cycloid's cusp is a real cusp.**

$$
\begin{aligned}
X(t) &= (t - \sin t,\ 1 - \cos t) \\
\Rightarrow\ X'(t) &= (1 - \cos t,\ \sin t) \\
\Rightarrow\ v(t) &= \sqrt{(1-\cos t)^2 + \sin^2 t} \\
&= \sqrt{2 - 2\cos t} = 2\sin\tfrac{t}{2}, \quad 0 \le t \le 2\pi .
\end{aligned}
$$

The speed vanishes at $$t = 0$$ and $$t = 2\pi$$, the cusps. Which way does the
particle leave? Normalise before taking the limit, using
$$1 - \cos t = 2\sin^2\frac{t}{2}$$ and $$\sin t = 2\sin\frac t2\cos\frac t2$$:

$$
\begin{aligned}
\lim_{t\to 0+}\frac{X'(t)}{\lvert X'(t)\rvert}
 &= \lim_{t\to 0+}\left(\sin\tfrac{t}{2},\ \cos\tfrac{t}{2}\right) \\
 &= (0,1).
\end{aligned}
$$

It leaves straight up. By the same computation it arrives at the next cusp
along $$(0,-1)$$, straight down. The tangent direction jumps by $$\pi$$ across
the cusp, which is what makes it sharp rather than merely slow.

**5. Speed in polar form.** For $$r = r(\theta)$$,

$$
\begin{aligned}
X(\theta) &= r(\theta)(\cos\theta,\ \sin\theta) \\
\Rightarrow\ X'(\theta) &= r'(\cos\theta, \sin\theta) + r(-\sin\theta, \cos\theta).
\end{aligned}
$$

Those two vectors are orthogonal — their inner product is
$$-\cos\theta\sin\theta + \sin\theta\cos\theta = 0$$ — so Pythagoras applies
termwise and

$$
\lvert X'(\theta) \rvert = \sqrt{r'^2 + r^2}.
$$

**6. The angle between position and velocity.** Call it $$\alpha$$. Since
$$X \cdot X' = r r'$$ and $$\lvert X \rvert = r$$,

$$
\cos\alpha = \frac{r'(\theta)}{\sqrt{r'(\theta)^2 + r(\theta)^2}} .
$$

**7. The logarithmic spiral is an equiangular spiral.** For $$r = e^{\theta}$$,

$$
\cos\alpha = \frac{e^{\theta}}{\sqrt{e^{2\theta} + e^{2\theta}}}
 = \frac{1}{\sqrt2} \ \Rightarrow\ \alpha = \frac{\pi}{4}.
$$

The angle does not depend on $$\theta$$. The spiral meets every ray from the
origin at the same angle, which is why it is also called the equiangular
spiral — and why a moth flying at a fixed angle to a point light source spirals
into it.

### The calculus of vector functions

**Theorem 1.1.**

$$
\begin{aligned}
(X + Y)' &= X' + Y' \\
(X \cdot Y)' &= X' \cdot Y + X \cdot Y' \\
(fX)' &= f'X + fX' \\
(X \times Y)' &= X' \times Y + X \times Y'
\end{aligned}
$$

Every one is the product rule. The last two matter because they let a geometric
hypothesis be differentiated directly.

**1. Motion on a sphere.** If a particle moves on a sphere centred at the
origin, position and velocity are perpendicular. Obvious geometrically; one
line algebraically:

$$
\begin{aligned}
\lvert X \rvert^2 = X \cdot X &\equiv \text{const} \\
 \Rightarrow\ X' \cdot X + X \cdot X' &\equiv 0 \\
 \Rightarrow\ X' \cdot X &\equiv 0 .
\end{aligned}
$$

**2. Constant speed.** If the speed is constant, velocity and acceleration are
always perpendicular:

$$
\lvert X' \rvert^2 \equiv \text{const}
 \ \Rightarrow\ X'' \cdot X' \equiv 0 .
$$

This is the one to remember. Constant speed does not mean no acceleration — it
means all the acceleration is turning, none of it is speeding up.

**3. Differentiating a length.**

$$
\frac{\mathrm{d}}{\mathrm{d}t}\lvert P(t) \rvert
 = \frac{P(t)\cdot P'(t)}{\lvert P(t) \rvert}.
$$

*Proof.* Differentiate $$\lvert P\rvert^2$$ two ways:
$$\frac{\mathrm d}{\mathrm dt}\lvert P\rvert^2 = 2\lvert P\rvert \frac{\mathrm d}{\mathrm dt}\lvert P\rvert$$
by the chain rule, and $$= 2P\cdot P'$$ by the product rule. $$\square$$

This small formula is the engine of the curvature computation in
[Unit 7](/posts/calculus-1-line-integrals-curvature/); it is worth keeping.

**4. Straight-line motion.** A particle moves in a straight line exactly when
velocity and acceleration are always parallel. When they also point the same
way, $$a \cdot v = \lvert a \rvert \lvert v \rvert$$, and example 3 gives

$$
\frac{\mathrm{d}}{\mathrm{d}t}\lvert v \rvert = \frac{v \cdot a}{\lvert v \rvert} = \lvert a \rvert ,
$$

so the scalar acceleration is the derivative of the speed — the
one-dimensional picture, recovered as the special case where it is valid.

---

## Part 2 — §9.2: acceleration and the osculating plane

### The osculating plane

For a curve $$r(t)$$ in $$\mathbb{R}^n$$, the plane through $$r(t_0)$$ spanned
by the velocity and acceleration vectors,

$$
\begin{aligned}
\{\,r(t_0) + a\,r'(t_0) + b\,r''(t_0) \mid \ &a, b \in \mathbb{R}\,\} \\
 &\subset \mathbb{R}^n ,
\end{aligned}
$$

is the **osculating plane** (접촉평면) at $$r(t_0)$$. It is the plane the curve
is, to second order, moving in.

In $$\mathbb{R}^3$$ it has a one-line equation, and
[Unit 5](/posts/calculus-1-determinants/) supplies both halves of it:

$$
\begin{aligned}
0 &= (X - r(t_0)) \cdot (r'(t_0) \times r''(t_0)) \\
&= \det\big(X - r(t_0),\ r'(t_0),\ r''(t_0)\big).
\end{aligned}
$$

A point lies in the plane exactly when the three vectors are dependent, which
is exactly when the determinant vanishes. The cross product gives the normal;
the determinant says the same thing without naming it.

**Worked example: the helix at $$t = 0$$.** For
$$r(t) = (\cos t, \sin t, t)$$,

$$
\begin{aligned}
r'(t) &= (-\sin t,\ \cos t,\ 1), \\
r''(t) &= (-\cos t,\ -\sin t,\ 0),
\end{aligned}
$$

so $$r(0) = (1,0,0)$$, $$r'(0) = (0,1,1)$$, $$r''(0) = (-1,0,0)$$ and

$$
0 = \det\begin{pmatrix} x - 1 & 0 & -1 \\ y & 1 & 0 \\ z & 1 & 0 \end{pmatrix}
 = -y + z .
$$

The osculating plane is $$z = y$$. It contains the whole $$x$$-direction, since
the acceleration at $$t=0$$ points along $$-x$$.

> The notes stop here with a question to the class — *this felt a bit strange
> before; what was strange about it?* — and no recorded answer. It is left open.
{: .prompt-info }

### Integrating a vector function

Componentwise, as one would hope:

$$
\begin{aligned}
\int_a^b X(t)\,\mathrm{d}t
 := \Big(&\int_a^b x_1(t)\,\mathrm{d}t,\ \ldots, \\
 &\int_a^b x_n(t)\,\mathrm{d}t\Big).
\end{aligned}
$$

**Theorem 2.1.** Integrating velocity gives displacement; integrating
acceleration gives change in velocity.

$$
\begin{aligned}
\int_a^t X'(u)\,\mathrm{d}u &= X(t) - X(a), \\
\int_a^t X''(w)\,\mathrm{d}w &= X'(t) - X'(a).
\end{aligned}
$$

### Inertial navigation

Here is what that theorem is for. An aircraft knows its initial position
$$r(t_0)$$ and initial velocity $$v(t_0)$$, and carries gyroscopes and
accelerometers that report its acceleration at every instant. Integrate twice:

$$
\begin{aligned}
v(t) &= \int_{t_0}^{t} a(w)\,\mathrm{d}w + v(t_0) \\
\Rightarrow\ r(t) &= \int_{t_0}^{t}\left(\int_{t_0}^{u} a(w)\,\mathrm{d}w + v(t_0)\right)\mathrm{d}u + r(t_0).
\end{aligned}
$$

That is an **inertial navigation system** (INS, 관성항법장치). The principle is
trivial — it is Theorem 2.1 — and the lectures said so plainly: what actually
made INS possible was the gyroscope, a work of genius, not the integral.

INS accumulates error and is markedly less accurate than GPS. It is still used,
because GPS needs signals from four or more satellites and INS needs nothing at
all from outside. If a war destroyed the satellites, a cruise missile could not
rely on GPS.

---

## Part 3 — §9.3: plane curves and polar coordinates

### Rotation as a vector

In $$\mathbb{R}^3$$, a physical quantity associated with rotation about the
origin can be packed into a single vector: its direction is the axis of
rotation, oriented by the right-hand rule, and its magnitude measures how much
rotation there is. This is why the cross product — which produces exactly such
a vector out of two others — is the natural language for rotational mechanics.

### Angular momentum

For a point of mass $$m$$ with position vector $$r(t)$$, the **angular
momentum** (각운동량) about the origin is

$$
L = r(t) \times m\,r'(t).
$$

The textbook writes the position as $$X(t)$$ and quietly sets $$m = 1$$, a
convention the lectures noted that physicists dislike.

### The area swept by the radial line

The segment joining the origin to the particle — the **radial line** — sweeps
out area as the particle moves. Over $$a \le t \le b$$ that area is the
integral of (the magnitude of) the angular momentum:

$$
\begin{aligned}
&\lim \sum \tfrac12 \lvert r(t_i) \times r'(t_i)\rvert\,\Delta t_i \\
&\qquad = \int_a^b \tfrac12 \lvert r(t) \times r'(t)\rvert\,\mathrm{d}t .
\end{aligned}
$$

Each term is the area of a thin triangle with sides $$r$$ and $$r'\Delta t$$,
and $$\frac12\lvert u \times w\rvert$$ is the area of the triangle on $$u$$ and
$$w$$ — property 4 of the cross product from
[Unit 4](/posts/calculus-1-coordinates-vectors/), doing real work.

### Central force and the law of equal areas

> **Central force** $$\iff$$ **the angular momentum vector is constant.**
{: .prompt-tip }

A stone flies along a curve $$r(t)$$ under a **central force** $$F$$ — one
always parallel to the position vector. By Newton's second law,

$$
F(r(t)) = m\,r''(t) \ \parallel\ r(t).
$$

Differentiate the angular momentum:

$$
\begin{aligned}
L' &= (r \times m r')' = r' \times m r' + r \times m r'' \\
&= 0 + 0 = 0
\end{aligned}
$$

— the first term because $$u \times u = 0$$, the second because $$r''$$ is
parallel to $$r$$. So $$r \times m r' \equiv$$ constant vector, and by the
previous subsection the area swept per unit time is constant. **Kepler's second
law**, in three lines, from the product rule for the cross product.

### Velocity and acceleration in polar form

Let a curve given in polar form be parametrized as

$$
X(t) = r(t)\big(\cos\theta(t),\ \sin\theta(t),\ 0\big) = r(t)\,u(t),
$$

and write $$u^{*}$$ for $$u$$ rotated a quarter turn, so that

$$
u'(t) = \theta'(-\sin\theta, \cos\theta, 0) = \theta' u^{*} .
$$

The four facts to carry are

$$
\begin{aligned}
u' &= \theta' u^{*}, & (u^{*})' &= -\theta' u, \\
\lvert u \rvert = \lvert u^{*}\rvert &\equiv 1, & u \cdot u^{*} &\equiv 0 .
\end{aligned}
$$

With those, differentiating twice gives the standard polar decomposition — the
lectures insisted on doing this one by hand:

$$
\begin{aligned}
X' &= r'u + r\theta' u^{*} \\
X'' &= (r'' - r\theta'^2)\,u + (2r'\theta' + r\theta'')\,u^{*}
\end{aligned}
$$

The radial term $$-r\theta'^2$$ is the centripetal acceleration and the
$$2r'\theta'$$ is the Coriolis term; both fall out of the product rule rather
than being postulated.

The angular momentum becomes

$$
\begin{aligned}
X \times mX' &= mr^2\theta'\,(u \times u^{*}), \\
\lvert X \times mX'\rvert &= mr^2\lvert\theta'\rvert ,
\end{aligned}
$$

since the radial part contributes $$u \times u = 0$$. Writing
$$\lvert \theta'(t)\rvert = \omega$$, physics books state this as

$$
\lVert L \rVert = mr^2\omega .
$$

### Area in polar coordinates

$$
\text{area} = \int_{\theta_0}^{\theta_1} \tfrac12 r^2\,\mathrm{d}\theta .
$$

**1. Archimedean spiral** $$r = k\theta$$, $$0 \le \theta \le 2\pi$$:

$$
\begin{aligned}
A &= \int_0^{2\pi}\tfrac12 (k\theta)^2\,\mathrm{d}\theta = \tfrac{4}{3}\pi^3k^2 \\
 &= \tfrac13 \pi(2\pi k)^2 = \tfrac13 D ,
\end{aligned}
$$

where $$D$$ is the area of the circle of radius $$2\pi k$$ that the spiral ends
on. Exactly one third — a clean fact with no obvious reason to be clean.

**2. One arch of the cycloid.** Area between
$$X(t) = (t - \sin t, 1 - \cos t)$$ and the $$x$$-axis.

*First solution,* the ordinary one. With $$\mathrm dx = (1-\cos t)\,\mathrm dt$$,

$$
\begin{aligned}
A &= \int_0^{2\pi} y\,\mathrm{d}x = \int_0^{2\pi}(1-\cos t)^2\,\mathrm{d}t \\
&= \int_0^{2\pi}(1 - 2\cos t + \cos^2 t)\,\mathrm{d}t = 3\pi = 3D ,
\end{aligned}
$$

three times the area $$D = \pi$$ of the rolling circle.

*Second solution,* described by the notes as *needlessly complicated*, using
the swept-area integral. The arch starts at the origin, so the radial line
sweeps exactly the region under it. Since the curve lies in the plane
$$z = 0$$,

$$
\begin{aligned}
X \times X' &= \begin{vmatrix} i & j & k \\ t - \sin t & 1 - \cos t & 0 \\ 1 - \cos t & \sin t & 0\end{vmatrix} \\
&= \big(0,\ 0,\ (t - \sin t)\sin t - (1-\cos t)^2\big),
\end{aligned}
$$

and the third component factors as
$$2\sin\frac t2\left(t\cos\frac t2 - 2\sin\frac t2\right)$$, which is negative
throughout $$0 < t < 2\pi$$. So

$$
\begin{aligned}
A &= \int_0^{2\pi} \tfrac12\left[(1-\cos t)^2 - (t - \sin t)\sin t\right]\mathrm{d}t \\
&= \tfrac12\left[3\pi - (-3\pi)\right] = 3\pi .
\end{aligned}
$$

Same answer, four times the work. The point of showing it is that the swept-area
integral is not a special trick for planets.

### Kepler's laws

1. The orbit of Mars is an ellipse with the sun at a focus. *(Not easy.)*
2. Equal areas in equal times. *(By the vector product — done above.)*
3. The square of a planet's period is proportional to the cube of the major
   axis. *(Not easy.)*

Two of the three are hard. The one this chapter can prove is the one that is
really a statement about a cross product with zero derivative.

---

## Part 4 — §9.4: reparametrization

Let $$X(t)$$ be a curve on an interval $$I \subset \mathbb{R}$$, let
$$J \subset \mathbb{R}$$ be another interval, and let $$g : J \to I$$ be an
invertible $$C^1$$ function:

$$
J \xrightarrow{\ g\ } I \xrightarrow{\ X\ } \mathbb{R}^n,
\qquad \tilde X(s) := X(g(s)).
$$

Then $$\tilde X$$ is a **reparametrization** (재매개화) of $$X$$. It is
**orientation-preserving** (동향) when $$g$$ is increasing and
**orientation-reversing** (역향) when $$g$$ is decreasing.

**Theorem 4.1 (chain rule).**

$$
\tilde X'(s) = \big(X(g(s))\big)' = X'(g(s))\,g'(s).
$$

Two consequences follow immediately, and they are what reparametrization is
*for*:

- Since $$g' \ne 0$$, if $$X$$ is regular then so is $$\tilde X$$. Regularity is
  a property of the curve, not the clock.
- Differentiating once more,

  $$
  \begin{aligned}
  \tilde X'(s) &= X'(t)\,g'(s) \\
  \tilde X''(s) &= X''(t)\,(g'(s))^2 + X'(t)\,g''(s)
  \end{aligned}
  $$

  so $$\tilde X''$$ lies in the span of $$X'$$ and $$X''$$, and $$\tilde X'$$ is
  a multiple of $$X'$$. Hence if $$X'$$ and $$X''$$ are independent so are
  $$\tilde X'$$ and $$\tilde X''$$, **and the two curves have the same
  osculating plane at the same point.** The osculating plane depends only on the
  shape of the curve.

That last line is the template for everything that follows. A quantity worth
naming is one that survives reparametrization.

---

## Part 5 — §9.5: the length of a curve

The length of a parametrized curve $$X(t)$$, $$a \le t \le b$$, is the integral
of its speed:

$$
l = \int_a^b \lvert X'(t)\rvert\,\mathrm{d}t .
$$

> The lectures declined to belabour either this or its invariance under
> reparametrization: *the textbook explains it in detail; I will not say much.
> And the fact that length is unchanged by reparametrization is utterly
> obvious, so I will not say much about that either.* Distance travelled is
> speed integrated over time, and it does not matter whose watch you used.
{: .prompt-info }

### Worked examples

**1. Helix.** $$X(t) = (a\cos t, a\sin t, bt)$$, $$0 \le t \le 2\pi$$:

$$
\lvert X'(t)\rvert = \sqrt{a^2 + b^2}
 \ \Rightarrow\ l = 2\pi\sqrt{a^2 + b^2}.
$$

**2. One arch of the cycloid.**

$$
\lvert X'(t)\rvert = 2\left\lvert\sin\tfrac t2\right\rvert
 \ \Rightarrow\ l = \int_0^{2\pi} 2\sin\tfrac t2\,\mathrm{d}t = 8 .
$$

Eight. A circle rolls, and the curve it traces has integer length — exactly
four diameters of the rolling circle, with no $$\pi$$ anywhere. *This is really
remarkable.*

**3. Hypocycloid and epicycloid.** A wheel rolling inside a circle traces a
**hypocycloid**; rolling outside, an **epicycloid**. Take a base circle of
radius $$4$$ and a wheel of radius $$1$$:

$$
\begin{aligned}
H(t) &= (3\cos t, 3\sin t) + (\cos(-3t), \sin(-3t)) \\
E(t) &= (5\cos t, 5\sin t) + (\cos(5t + \pi), \sin(5t + \pi))
\end{aligned}
$$

Differentiating and squaring, the cross terms collapse by the cosine addition
formula:

$$
\begin{aligned}
\lvert H'(t)\rvert^2 &= 18 - 18\cos 4t = 36\sin^2 2t \\
\lvert E'(t)\rvert^2 &= 50 - 50\cos 4t = 100\sin^2 2t
\end{aligned}
$$

so each arch has length

$$
\begin{aligned}
l_1 &= \int_0^{\pi/2} 6\sin 2t\,\mathrm{d}t = 6, \\
l_2 &= \int_0^{\pi/2} 10\sin 2t\,\mathrm{d}t = 10,
\end{aligned}
$$

and

$$
l_1 + l_2 = 16 .
$$

> **Is that 16 suspicious?** It should be. Roll the wheel along *any* base
> curve instead of a circle and you get a left-hand cycloid and a right-hand
> one; their lengths still add to a constant that depends only on the base. The
> theorem is the lecturer's own:
>
> Hyounggyu Choi (2020), *Invariance of the Length and the Area of Cycloids*,
> The American Mathematical Monthly **127**:6, 537–544.
>
> A sequel extends it to the area and volume of cycloid and trochoid
> *surfaces*.
{: .prompt-tip }

**4. Part of a cycloid arch.** For $$2 - d \le y \le 2$$, with
$$y = 1 - \cos t_0$$ at the cut,

$$
\begin{aligned}
l &= 8 - 2\int_0^{t_0} 2\sin\tfrac t2\,\mathrm{d}t = 8\cos\tfrac{t_0}{2} \\
&= 8\sqrt{\tfrac{1 + \cos t_0}{2}} = 8\sqrt{\tfrac d2} = 4\sqrt{2d}.
\end{aligned}
$$

**5. A graph.** $$X(t) = (t, f(t))$$ gives
$$\lvert X'(t)\rvert = \sqrt{1 + f'(t)^2}$$, the familiar arc-length integrand.

**6. The catenary.** A hanging cable of uniform density takes the shape of
$$y = \frac1a\cosh ax$$ — proved in the textbook's appendix — and the curve is
called the **catenary** (현수선). Its length is as clean as its shape:

$$
l = \int_0^b \sqrt{1 + \sinh^2 t}\,\mathrm{d}t = \int_0^b \cosh t\,\mathrm{d}t = \sinh b
$$

for $$y = \cosh x$$ on $$0 \le x \le b$$, because $$1 + \sinh^2 = \cosh^2$$ is
exactly what the square root needs.

**7. The ellipse, and a confession.** $$X(t) = (a\cos t, b\sin t)$$ gives
$$\lvert X'\rvert = \sqrt{a^2\sin^2 t + b^2\cos^2 t}$$. Now compare the circle
with the ellipse.

**Area.** The circle gives $$\pi r^2$$ and the ellipse gives $$\pi ab$$ — the
same formula with the two radii kept apart.

**Length.** The circle gives $$2\pi r$$. The ellipse gives

$$
l = \int_0^{2\pi}\sqrt{a^2\sin^2 t + b^2\cos^2 t}\,\mathrm{d}t
$$

and there it stops. The area generalises perfectly. The length does not. *Humanity has achieved
great mathematical things. We still do not know the length of an ellipse* — not
in closed form; the integral is the elliptic integral that gave the whole family
of elliptic functions its name.

**8. Polar form.** $$X(\theta) = r(\theta)(\cos\theta, \sin\theta)$$ gives

$$
\lvert X'(\theta)\rvert = \sqrt{r(\theta)^2 + r'(\theta)^2},
$$

which is worked example 5 of Part 1 again.

**9. The cardioid** $$r = 2 - 2\cos\theta$$:

$$
\begin{aligned}
\lvert X'(\theta)\rvert &= \sqrt{(2-2\cos\theta)^2 + 4\sin^2\theta} \\
&= \sqrt{8 - 8\cos\theta} = 4\left\lvert\sin\tfrac\theta2\right\rvert
\end{aligned}
$$

$$
\Rightarrow\ l = \int_0^{2\pi} 4\sin\tfrac\theta2\,\mathrm{d}\theta = 16 .
$$

The cardioid is the epicycloid traced by a unit circle rolling outside a unit
circle — so this $$16$$ is the $$16$$ from example 3, not a coincidence.

**10. The four-bug pursuit curve.** Four cockroaches at the corners of a square
each chase the next; each traces $$r = \frac{10}{\sqrt2}e^{\theta}$$. Since
$$r' = r$$, we get $$\lvert X'\rvert = \sqrt{2}\,r = 10e^{\theta}$$ and

$$
l = \int_{-\infty}^{0} 10 e^{\theta}\,\mathrm{d}\theta = 10 .
$$

Infinitely many turns, finite distance — and the distance equals the side of
the square they started on.

**11. Spherical geodesics.** A **geodesic** is a shortest curve joining two
points. That the geodesics on a sphere are arcs of great circles is in the
textbook; the lectures left it to be read.

---

## Part 6 — §9.6: parametrization by arc length

For a parametrized curve $$Y(s)$$, two conditions are equivalent: the speed is
always $$1$$, and the length travelled always equals the time elapsed.

$$
\lvert Y'(s)\rvert \equiv 1
\iff \int_{s_0}^{s}\lvert Y'(u)\rvert\,\mathrm{d}u \equiv s - s_0 .
$$

Such a curve is **parametrized by arc length** (호의 길이로 매개화).

### How to do it

Take a regular curve $$X(t)$$ and look for an orientation-preserving
reparametrization $$Y(s) = X(g(s))$$ with $$\lvert Y'(s)\rvert \equiv 1$$ and
$$g'(s) > 0$$. By the chain rule,

$$
\lvert Y'(s)\rvert = \lvert X'(t)\rvert\,\frac{\mathrm{d}t}{\mathrm{d}s} \equiv 1 ,
$$

and by the inverse function theorem that is the same as

$$
\frac{\mathrm{d}s}{\mathrm{d}t} = \lvert X'(t)\rvert ,
$$

so

$$
s = \int_a^{t} \lvert X'(u)\rvert\,\mathrm{d}u
\qquad\text{or simply}\qquad
s = \int \lvert X'(t)\rvert\,\mathrm{d}t .
$$

That expresses $$s$$ as a function of $$t$$. What is wanted is $$t$$ as a
function of $$s$$ — so **invert**. The lower limit $$a$$ is arbitrary;
$$a = 0$$ is often convenient, and any antiderivative of the speed will do.

### Worked examples

**1. Circle.** $$X(t) = (r\cos\omega t, r\sin\omega t)$$:

$$
\begin{aligned}
s &= \int r\omega\,\mathrm{d}t = r\omega t
 \ \Rightarrow\ t = \frac{s}{r\omega} \\
\Rightarrow\ Y(s) &= \left(r\cos\frac{s}{r\omega},\ r\sin\frac{s}{r\omega}\right).
\end{aligned}
$$

**2. Helix.** $$X(t) = (a\cos t, a\sin t, bt)$$. Writing $$c = \sqrt{a^2+b^2}$$,

$$
\begin{aligned}
s &= ct \ \Rightarrow\ t = \frac sc \\
\Rightarrow\ Y(s) &= \left(a\cos\frac sc,\ a\sin\frac sc,\ \frac{bs}{c}\right).
\end{aligned}
$$

**3. Logarithmic spiral.** $$X(t) = e^{t}(\cos t, \sin t)$$:

$$
\begin{aligned}
s &= \sqrt2 e^{t} \ \Rightarrow\ t = \ln\frac{s}{\sqrt2} \\
\Rightarrow\ Y(s) &= \frac{s}{\sqrt2}\left(\cos\ln\frac{s}{\sqrt2},\ \sin\ln\frac{s}{\sqrt2}\right).
\end{aligned}
$$

**4. Cycloid**, $$0 < t < 2\pi$$:

$$
s = \int 2\sin\tfrac t2\,\mathrm{d}t = -4\cos\tfrac t2
\ \Rightarrow\ t = 2\arccos\left(\frac{-s}{4}\right),
$$

and substituting that back into $$(t - \sin t, 1 - \cos t)$$ gives a formula
with $$\arccos$$ nested inside $$\sin$$ and $$\cos$$ — correct, and already
unpleasant.

**5. The parabola, where it breaks down.** For $$y = x^2$$, take
$$X(t) = (t, t^2)$$, so $$\lvert X'(t)\rvert = \sqrt{1 + 4t^2}$$ and
$$s = \int\sqrt{1+4t^2}\,\mathrm{d}t$$. Substitute $$2t = \sinh u$$, so that
$$\sqrt{1+4t^2} = \cosh u$$ and $$2\,\mathrm{d}t = \cosh u\,\mathrm{d}u$$:

$$
\begin{aligned}
s &= \tfrac12\int \cosh^2 u\,\mathrm{d}u = \tfrac12\int \frac{1 + \cosh 2u}{2}\,\mathrm{d}u \\
&= \tfrac14 u + \tfrac18\sinh 2u ,
\end{aligned}
$$

which is *some* function of $$t$$. And now invert it. *Let us stop here.*

### Why bother, then?

That example is the point of the section. Parametrizing a concrete curve by arc
length is practically impossible, because inverting the function is practically
impossible. The lectures put the obvious question directly:

> *Among all the many parametrizations of a concrete curve, what exactly is the
> reason for struggling to find the one by arc length?*
{: .prompt-warning }

And answered it honestly. Unless the motion is along a line or a circle, there
is no motion less natural than constant speed. Why work hard to find the
equation of an unnatural motion? There is neither a reason nor an occasion.

Arc length is needed **theoretically**. Both of the *Monthly* papers above
concern curves parametrized by arc length — but they *assume* the curve is so
parametrized and develop the theory; they never compute the parametrization.
In the lecturer's experience, thinking about an arc-length-parametrized curve
is a way of arranging a convenient setting for some other job, never an end in
itself, and concrete calculation is almost never required.

So the five examples above are, in the lectures' own verdict, meaningless —
set purely to make students sweat. *Think of them as military drill.*

[Unit 7](/posts/calculus-1-line-integrals-curvature/) immediately proves the
point. Curvature is *defined* through the arc-length parametrization and then
computed through a formula that never constructs it.

### A postscript on road design

There is one place where the smoothness class of a curve has consequences you
can feel.

> Driving on an old national highway you sometimes get the sensation that the
> car will fly off the road no matter how much you slow down. A road shaped
> like the curve in the taegeuk symbol — two semicircles joined — must never be
> built, because **that curve is not $$C^2$$.** A road must be designed as a
> $$C^2$$ regular curve. The standards are written down in a road design
> specification that someone worked hard to produce.
{: .prompt-warning }

Two semicircles of opposite sense joined end to end have a continuous tangent,
so the curve is $$C^1$$ and looks perfectly smooth. But the second derivative
jumps, and in [Unit 7](/posts/calculus-1-line-integrals-curvature/) the second
derivative turns out to be exactly the curvature — so the sideways force on the
driver changes discontinuously at the join. The real road uses a clothoid, whose
curvature grows linearly, precisely so that the steering wheel can be turned at
a finite rate.

## Common pitfalls

- **Asking whether a curve is differentiable.** The question needs a
  parametrization. $$y = \lvert x\rvert$$ has a differentiable parametrization
  and a non-differentiable one.
- **Confusing differentiable with regular.** $$Y(t) = (t\lvert t\rvert, t^2)$$
  is differentiable everywhere and regular nowhere near $$0$$, because the speed
  vanishes there.
- **Thinking constant speed means zero acceleration.** It means the acceleration
  is perpendicular to the velocity — all turning, no speeding up.
- **Dropping the absolute value in $$\lvert X'\rvert$$.** The cycloid's speed is
  $$2\lvert\sin\frac t2\rvert$$; it is only $$2\sin\frac t2$$ because
  $$0 \le t \le 2\pi$$ keeps the sine non-negative. Over two arches it matters.
- **Using $$\sqrt{r^2 + r'^2}$$ with the wrong variable.** In polar form the
  parameter is $$\theta$$, so the length element is
  $$\sqrt{r^2 + r'^2}\,\mathrm{d}\theta$$, not $$\mathrm{d}t$$.
- **Forgetting that the swept-area integral needs the origin.**
  $$\int\frac12\lvert r \times r'\rvert$$ is the area swept by the radial line
  from the origin, which equals the area under a curve only when the curve
  starts and ends on a ray through the origin — as the cycloid arch happens to.
- **Expecting to parametrize by arc length.** You will get as far as $$s(t)$$
  and stop at the inverse. That is the normal outcome, not a failure.

## Connections

- **Backward.** The cross product and its area interpretation from
  [Unit 4](/posts/calculus-1-coordinates-vectors/) become angular momentum and
  swept area; the determinant from
  [Unit 5](/posts/calculus-1-determinants/) writes the osculating plane in one
  line. Polar coordinates from Unit 4 return as a parametrization, and the
  conic sections from the same unit are what Kepler's first law is about.
- **Forward.** Everything here is setup for
  [Unit 7](/posts/calculus-1-line-integrals-curvature/). The line integral is
  $$\lvert X'\rvert\,\mathrm{d}t$$ with a weight; curvature is the second
  derivative of the arc-length parametrization; the osculating plane is where
  the osculating circle lives; and the derivative-of-a-length formula from
  Theorem 1.1 is the computation that makes curvature calculable.
- **Outward.** Inertial navigation is Theorem 2.1 with hardware. Kepler's second
  law is the product rule. Road design is the gap between $$C^1$$ and $$C^2$$.
  This is the chapter where the course's machinery starts paying rent.

## Summary

- **Parametrized curve** — $$X(t) = (x_1(t), \ldots, x_n(t))$$; a motion, not a
  point set
- **Differentiability** — a property of the parametrization, not of the curve
- **Regular** — differentiable with speed never zero; corners are not regular
- **Velocity, acceleration, speed** — $$X'$$, $$X''$$, $$\lvert X'\rvert$$
- **Constant speed** $$\Rightarrow$$ $$X'\cdot X'' \equiv 0$$
- **Length of a vector** — $$\frac{\mathrm d}{\mathrm dt}\lvert P\rvert = \frac{P\cdot P'}{\lvert P\rvert}$$
- **Osculating plane** — through $$r(t_0)$$, spanned by $$r'$$ and $$r''$$; in
  $$\mathbb{R}^3$$, $$\det(X - r(t_0), r', r'') = 0$$
- **Angular momentum** — $$L = r \times mr'$$; central force $$\iff$$ $$L$$ constant $$\iff$$ equal areas
- **Polar motion** — $$X' = r'u + r\theta'u^{*}$$, $$X'' = (r''-r\theta'^2)u + (2r'\theta'+r\theta'')u^{*}$$
- **Polar area** — $$\int \frac12 r^2\,\mathrm{d}\theta$$
- **Reparametrization** — $$\tilde X(s) = X(g(s))$$; regularity, independence of
  $$X', X''$$, and the osculating plane all survive it
- **Length** — $$l = \int_a^b\lvert X'(t)\rvert\,\mathrm{d}t$$; invariant under reparametrization
- **Cycloid arch** — length $$8$$, area $$3\pi$$
- **Arc length parametrization** — $$\lvert Y'\rvert \equiv 1$$; find
  $$s = \int\lvert X'\rvert\,\mathrm{d}t$$ and invert, which usually cannot be done

## References

- Hong Jong Kim, *Calculus 1+* (미적분학 1+), 2nd revised edition, Seoul National University Press — §§9.1–9.6. Exercise references above (p308, p309, p337, p339–p342) are to that text.
- Mathematics 1 (수학 1, L0442.000100), Seoul National University, Spring 2022. Instructor: Choi Hyung Gyu (최형규). Lecture notes for Chapter 9 dated 28 April 2022.
- Hyounggyu Choi (2020), *Invariance of the Length and the Area of Cycloids*, The American Mathematical Monthly **127**:6, 537–544 — the lecturer's own paper, cited in the notes as the explanation of the 16.
- Hyounggyu Choi (2022), *Invariance of the Area and the Volume of Cycloid Surfaces and Trochoid Surfaces*, The American Mathematical Monthly, to appear.
- Two computations were redone rather than copied. In the second solution for the cycloid's area the notes factor the cross product as $$2\sin\frac t2(t\cos\frac t2 - 2)$$; the correct factorisation is $$2\sin\frac t2(t\cos\frac t2 - 2\sin\frac t2)$$, which is what gives $$3\pi$$. In the parabola's arc-length substitution the factor $$\frac12$$ from $$2\,\mathrm dt = \cosh u\,\mathrm du$$ is carried here; the notes drop it, which does not affect the conclusion that the inverse is intractable.
- The limiting unit tangent at the cycloid's cusp is computed here as $$(\sin\frac t2, \cos\frac t2) \to (0,1)$$; the notes' intermediate expression is garbled in the scan, but the stated limit agrees.
