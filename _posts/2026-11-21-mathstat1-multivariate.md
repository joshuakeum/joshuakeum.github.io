---
title: "Mathematical Statistics 1: Ch. 2 Part 5 — Multivariate Random Variables"
date: 2026-11-21 10:10:00 +0900
categories: [Study Notes, Mathematical Statistics 1]
tags: [random vector, mean vector, covariance matrix, multivariate mgf, independence, sum of independent]
description: Distribution of a k-dimensional random variable, mean vector and variance matrix, multivariate moment generating function, conditional distribution and expectation, and independence of several random variables. Chapter 2, §2.5 of Mathematical Statistics 1.
math: true
mermaid: false
render_with_liquid: false
---

> My handwritten notes do not cover this section, so everything below is **translated from the textbook**, §2.5. It is not my own writing. It extends [Parts 1 to 4](/posts/mathstat1-joint-distribution/) from two random variables to $$k$$ of them.
{: .prompt-info }

## 2.5 Distribution of multivariate random variables

The vector $$(X_1, X_2, \dots, X_k)^t$$ whose components are the random variables $$X_1, \dots, X_k$$ is called a $$k$$-dimensional random variable, a $$k$$-variate random vector. (From here on a vector is a column vector, and $$t$$ denotes the transpose of a vector or matrix.)

> **Joint pdf of a discrete $$k$$-dimensional random variable.**
>
> - (a) $$f(x_1, \dots, x_k) \ge 0$$ for all $$x_i$$, and $$f(x_1, \dots, x_k) = 0$$ unless each $$x_i \in \{x_{i1}, x_{i2}, \dots\}$$.
> - (b) $$\sum_{x_1}\cdots\sum_{x_k}f(x_1, \dots, x_k) = 1$$.
> - (c) $$\sum_{x_1 : a_1 \le x_1 \le b_1}\cdots\sum_{x_k : a_k \le x_k \le b_k}f(x_1, \dots, x_k) = P(a_1 \le X_1 \le b_1, \dots, a_k \le X_k \le b_k)$$.
{: .definition #def-joint-pdf-discrete-k }

> **Joint pdf of a continuous $$k$$-dimensional random variable.**
>
> - (a) $$f(x_1, \dots, x_k) \ge 0$$ for all $$x_i$$.
> - (b) $$\displaystyle\int_{-\infty}^{+\infty}\cdots\int_{-\infty}^{+\infty}f(x_1, \dots, x_k)\,dx_k\cdots dx_1 = 1$$.
> - (c) $$\displaystyle\int_{a_1}^{b_1}\cdots\int_{a_k}^{b_k}f(x_1, \dots, x_k)\,dx_k\cdots dx_1 = P(a_1 \le X_1 \le b_1, \dots, a_k \le X_k \le b_k)$$.
{: .definition #def-joint-pdf-continuous-k }

**Example 2.5.1.** A box contains two white, three black, four red and five yellow balls. Four balls are drawn together; let $$X_1, X_2, X_3$$ be the numbers of white, black and red balls drawn. The joint pdf of $$(X_1, X_2, X_3)^t$$ is

$$
f(x_1, x_2, x_3) = \frac{\binom{2}{x_1}\binom{3}{x_2}\binom{4}{x_3}\binom{5}{4 - x_1 - x_2 - x_3}}{\binom{14}{4}},
$$

$$x_1 = 0, 1, 2$$, $$x_2 = 0, 1, 2, 3$$, $$x_3 = 0, 1, 2, 3, 4$$, $$x_1 + x_2 + x_3 \le 4$$.

**Example 2.5.2.** Find the constant $$c$$ for which $$f(x_1, x_2, x_3) = c\,e^{-x_1 - x_2 - x_3}I_{(0 \le x_1 \le x_2 \le x_3)}$$ is the joint pdf of $$(X_1, X_2, X_3)^t$$.

*Solution.* The total probability must be $$1$$:

$$
\int_0^{\infty}\int_{x_1}^{\infty}\int_{x_2}^{\infty}c\,e^{-x_1 - x_2 - x_3}\,dx_3\,dx_2\,dx_1 = c\int_0^{\infty}e^{-x_1}\Bigl[-\frac{e^{-2x_2}}{2}\Bigr]_{x_1}^{\infty}dx_1 = \frac{c}{2}\int_0^{\infty}e^{-3x_1}\,dx_1 = \frac{c}{6} = 1,
$$

so $$c = 6$$.

> **Marginal pdfs.** If the joint pdf of the $$k$$-dimensional random variable $$(X_1, \dots, X_k)^t$$ is $$f(x_1, \dots, x_k)$$, the marginal pdfs $$f_1(x)$$ of $$X_1$$ and $$f_{1,2}(x, y)$$ of $$(X_1, X_2)^t$$ are
>
> - (a) $$f_1(x) = \sum_{x_2}\cdots\sum_{x_k}f(x, x_2, \dots, x_k)$$ (discrete), $$\int\cdots\int f(x, x_2, \dots, x_k)\,dx_k\cdots dx_2$$ (continuous);
> - (b) $$f_{1,2}(x, y) = \sum_{x_3}\cdots\sum_{x_k}f(x, y, x_3, \dots, x_k)$$ (discrete), $$\int\cdots\int f(x, y, x_3, \dots, x_k)\,dx_k\cdots dx_3$$ (continuous).
{: .definition #def-marginal-pdf-k }

**Example 2.5.3.** In Example 2.5.1 the marginal pdf of $$(X_1, X_2)^t$$ is $$f_{1,2}(x, y) = \sum_{x_3}f(x, y, x_3) = \binom{2}{x}\binom{3}{y}\sum_{x_3}\binom{4}{x_3}\binom{5}{4 - x - y - x_3}\Big/\binom{14}{4}$$, hence

$$
f_{1,2}(x, y) = \binom{2}{x}\binom{3}{y}\binom{9}{4 - x - y}\Big/\binom{14}{4}, \quad x = 0, 1, 2,\ y = 0, 1, 2, 3,\ x + y \le 4.
$$

**Example 2.5.4.** In Example 2.5.2 the joint pdf of $$(X_1, X_2, X_3)^t$$ is $$f(x_1, x_2, x_3) = 6e^{-x_1 - x_2 - x_3}I_{(0 \le x_1 \le x_2 \le x_3)}$$, so the marginal pdf of $$(X_1, X_3)^t$$ is $$f_{1,3}(x, z) = \int f(x, x_2, z)\,dx_2 = 6e^{-x-z}\int_x^z e^{-x_2}\,dx_2\, I_{(0 \le x \le z)}$$, that is,

$$
f_{1,3}(x, z) = 6\bigl(e^{-2x - z} - e^{-x - 2z}\bigr)I_{(0 \le x \le z)},
$$

and the marginal pdf of $$X_1$$ is $$f_1(x) = 6\int_x^{\infty}\bigl(e^{-2x - z} - e^{-x - 2z}\bigr)\,dz\, I_{(0 \le x)} = 3e^{-3x}I_{(x \ge 0)}$$.

As for one dimension, the pdf and the cdf of a multivariate random variable correspond one-to-one; for example, in the continuous case $$F(x_1, \dots, x_k) = P(X_1 \le x_1, \dots, X_k \le x_k) = \int_{-\infty}^{x_1}\cdots\int_{-\infty}^{x_k}f(t_1, \dots, t_k)\,dt_k\cdots dt_1$$ and, at a point of continuity of $$f$$, $$f(x_1, \dots, x_k) = \dfrac{\partial^k}{\partial x_1\cdots\partial x_k}F(x_1, \dots, x_k)$$.

> **Expectation of a function of a random vector.** If the joint pdf of $$(X_1, \dots, X_k)^t$$ is $$f$$ and $$g$$ is a real-valued function, then
>
> $$
> E[g(X_1, \dots, X_k)] = \sum_{x_1}\cdots\sum_{x_k}g(x_1, \dots, x_k)f(x_1, \dots, x_k) \ \text{ (discrete)}, \qquad \int\cdots\int g(x_1, \dots, x_k)f(x_1, \dots, x_k)\,dx_k\cdots dx_1 \ \text{ (continuous)},
> $$
>
> if this is a real number.
{: .definition #def-expectation-k }

**Example 2.5.5.** If the joint pdf of $$(X_1, X_2, X_3)^t$$ is $$f(x_1, x_2, x_3) = 120x_1(1 - x_1 - x_2 - x_3)I_{(x_1 \ge 0,\ x_2 \ge 0,\ x_3 \ge 0,\ x_1 + x_2 + x_3 \le 1)}$$, find $$E(X_1X_2)$$.

*Solution.* Writing $$(x, y, z)$$ for $$(x_1, x_2, x_3)$$,

$$
E(X_1X_2) = \iiint_{\substack{0 \le x,\,y,\,z \\ x + y + z \le 1}}xy\cdot 120x(1 - x - y - z)\,dz\,dy\,dx = \int_0^1\Bigl\{120x^2\int_0^{1-x}y\Bigl\{\int_0^{1-x-y}(1 - x - y - z)\,dz\Bigr\}dy\Bigr\}dx = \int_0^1 5x^2(1 - x)^4\,dx = \frac{1}{21}.
$$

> **Theorem 2.5.1 (Properties of expectation).** (a) *(Linearity.)* $$E[c_1g_1(X_1, \dots, X_k) + c_2g_2(X_1, \dots, X_k)] = c_1E[g_1] + c_2E[g_2]$$. (b) *(Monotonicity.)* If $$g_1 \le g_2$$, then $$E[g_1] \le E[g_2]$$. (Assuming each expectation is a real number.)
{: .theorem #thm-expectation-properties-k }

> **Mean vector and variance matrix.** For the random vector $$\mathbf{X} = (X_1, \dots, X_k)^t$$, the matrix and vector having as elements the mean, variance and covariances $$\mu_i = E(X_i)$$, $$\sigma_{i,j} = \mathrm{Cov}(X_i, X_j)$$ ($$i, j = 1, \dots, k$$) are the *mean vector* and the *variance–covariance matrix* (variance matrix) of $$\mathbf{X}$$:
>
> $$
> E(\mathbf{X}) = (\mu_1, \dots, \mu_k)^t = (E(X_1), \dots, E(X_k))^t, \qquad
> \mathrm{Var}(\mathbf{X}) = \begin{pmatrix}\sigma_{1,1} & \cdots & \sigma_{1,k} \\ \vdots & & \vdots \\ \sigma_{k,1} & \cdots & \sigma_{k,k}\end{pmatrix} = \bigl(\mathrm{Cov}(X_i, X_j)\bigr)_{1 \le i, j \le k}.
> $$
{: .definition #def-mean-variance-matrix }

**Example 2.5.6.** For $$\mathbf{X} = (X_1, X_2)^t$$ with pdf $$f(x, y) = 120xy(1 - x - y)I_{(x \ge 0,\ y \ge 0,\ x + y \le 1)}$$ of Example 2.2.1, by the calculations of Examples 2.2.2 to 2.2.4,

$$
E(\mathbf{X}) = \begin{pmatrix}1/3 \\ 1/3\end{pmatrix}, \qquad \mathrm{Var}(\mathbf{X}) = \begin{pmatrix}2/63 & -1/63 \\ -1/63 & 2/63\end{pmatrix}.
$$

**Example 2.5.7.** For $$f(x, y) = 2e^{-x-y}I_{(0 \le x \le y)}$$ of Example 2.1.2, by the calculations of Example 2.2.5,

$$
E(\mathbf{X}) = \begin{pmatrix}1/2 \\ 3/2\end{pmatrix}, \qquad \mathrm{Var}(\mathbf{X}) = \begin{pmatrix}1/4 & 1/4 \\ 1/4 & 5/4\end{pmatrix}.
$$

As $$E[(X_1, \dots, X_k)^t] = (E(X_1), \dots, E(X_k))^t$$, the expectation of a matrix of random variables $$(W_{i,j})$$ is the matrix of the expectations, $$E[(W_{i,j})] = (E(W_{i,j}))$$.

> **Theorem 2.5.2 (Expectation of a matrix of random variables).** For matrices of random variables $$V = (V_{i,j})$$, $$W = (W_{i,j})$$: (a) $$E(CWD) = CE(W)D$$ ($$C, D$$ matrices with constant elements); (b) $$E(V + W) = E(V) + E(W)$$.
{: .theorem #thm-matrix-expectation }

With matrices of random variables, the mean vector and variance matrix are written compactly. With $$\boldsymbol{\mu} = E(\mathbf{X})$$, $$(\mathbf{X} - \boldsymbol{\mu})(\mathbf{X} - \boldsymbol{\mu})^t = ((X_i - \mu_i)(X_j - \mu_j))$$, so

$$
\mathrm{Var}(\mathbf{X}) = (\mathrm{Cov}(X_i, X_j)) = E[(\mathbf{X} - \boldsymbol{\mu})(\mathbf{X} - \boldsymbol{\mu})^t].
$$

Generalizing, the covariance matrix of $$\mathbf{X} = (X_1, \dots, X_k)^t$$ and $$\mathbf{Y} = (Y_1, \dots, Y_l)^t$$ is $$\mathrm{Cov}(\mathbf{X}, \mathbf{Y}) = (\mathrm{Cov}(X_i, Y_j))_{1 \le i \le k,\ 1 \le j \le l}$$ ($$k \times l$$), and with $$\boldsymbol{\eta} = E(\mathbf{Y})$$, $$\mathrm{Cov}(\mathbf{X}, \mathbf{Y}) = E[(\mathbf{X} - \boldsymbol{\mu})(\mathbf{Y} - \boldsymbol{\eta})^t]$$.

> **Theorem 2.5.3 (Properties of the mean vector and the variance matrix).** For matrices and vectors of constants $$A, C, b, d$$:
>
> - (a) $$E(A\mathbf{X} + b) = AE(\mathbf{X}) + b$$.
> - (b) $$\mathrm{Var}(A\mathbf{X} + b) = A\,\mathrm{Var}(\mathbf{X})A^t$$.
> - (c) $$\mathrm{Cov}(A\mathbf{X} + b,\ C\mathbf{Y} + d) = A\,\mathrm{Cov}(\mathbf{X}, \mathbf{Y})C^t$$.
> - (d) $$\mathrm{Cov}(\mathbf{X} + \mathbf{Y}, \mathbf{Z}) = \mathrm{Cov}(\mathbf{X}, \mathbf{Z}) + \mathrm{Cov}(\mathbf{Y}, \mathbf{Z})$$, $$\mathrm{Cov}(\mathbf{X}, \mathbf{Z} + \mathbf{W}) = \mathrm{Cov}(\mathbf{X}, \mathbf{Z}) + \mathrm{Cov}(\mathbf{X}, \mathbf{W})$$.
> - (e) $$\mathrm{Cov}(\mathbf{Y}, \mathbf{X}) = (\mathrm{Cov}(\mathbf{X}, \mathbf{Y}))^t$$, $$\mathrm{Var}(\mathbf{X}) = \mathrm{Cov}(\mathbf{X}, \mathbf{X})$$.
> - (f) $$\mathrm{Var}(\mathbf{X} + \mathbf{Y}) = \mathrm{Var}(\mathbf{X}) + \mathrm{Var}(\mathbf{Y}) + \mathrm{Cov}(\mathbf{X}, \mathbf{Y}) + \mathrm{Cov}(\mathbf{Y}, \mathbf{X})$$.
{: .theorem #thm-mean-variance-properties }

*Proof.* Clear from the properties of expectation and the definition of the covariance matrix. $$\square$$

**Example 2.5.8.** For $$\mathbf{X} = (X_1, X_2)^t$$ with $$f(x, y) = 2e^{-x-y}I_{(0 \le x \le y)}$$, by Example 2.5.7, $$E(\mathbf{X}) = (1/2, 3/2)^t$$ and $$\mathrm{Var}(\mathbf{X}) = \begin{pmatrix}1/4 & 1/4 \\ 1/4 & 5/4\end{pmatrix}$$. Let $$\mathbf{Y} = (Y_1, Y_2)^t = (2X_1, X_2 - X_1)^t$$. Then $$\mathbf{Y} = A\mathbf{X}$$ with $$A = \begin{pmatrix}2 & 0 \\ -1 & 1\end{pmatrix}$$, so

$$
E(\mathbf{Y}) = A\begin{pmatrix}1/2 \\ 3/2\end{pmatrix} = \begin{pmatrix}1 \\ 1\end{pmatrix}, \qquad \mathrm{Var}(\mathbf{Y}) = A\begin{pmatrix}1/4 & 1/4 \\ 1/4 & 5/4\end{pmatrix}A^t = \begin{pmatrix}1 & 0 \\ 0 & 1\end{pmatrix}.
$$

> **Theorem 2.5.4 (Properties of the variance matrix).** The variance matrix $$\mathrm{Var}(\mathbf{X})$$ of $$\mathbf{X} = (X_1, \dots, X_k)^t$$ is a symmetric nonnegative definite matrix: $$\mathrm{Var}(\mathbf{X}) = (\mathrm{Var}(\mathbf{X}))^t$$ and $$a^t\mathrm{Var}(\mathbf{X})a \ge 0$$ for all $$a \in \mathbb{R}^k$$.
{: .theorem #thm-variance-matrix-nonneg }

*Proof.* That the variance matrix is symmetric is clear, and since $$a^t\mathbf{X}$$ is a real-valued random variable, $$a^t\mathrm{Var}(\mathbf{X})a = \mathrm{Var}(a^t\mathbf{X}) \ge 0$$ for all $$a \in \mathbb{R}^k$$. $$\square$$

Since the variance matrix is a symmetric nonnegative definite matrix, by the diagonalization theorem there is an orthogonal matrix $$P = (p_1, \dots, p_k)$$ ($$p_i^tp_i = 1$$, $$p_i^tp_j = 0$$ for $$i \ne j$$) and eigenvalues $$\lambda_1 \ge \lambda_2 \ge \cdots \ge \lambda_k \ge 0$$ with $$\mathrm{Var}(\mathbf{X}) = P\,\mathrm{diag}(\lambda_i)P^t$$. Hence $$\mathrm{Var}(P^t\mathbf{X}) = \mathrm{diag}(\lambda_i)$$: in the coordinates $$P^t\mathbf{X}$$ the components are uncorrelated and their variances are $$\lambda_1 \ge \cdots \ge \lambda_k \ge 0$$. The components corresponding to $$\lambda_1 \ge \lambda_2 \ge \cdots$$ are called the first principal component, the second principal component, and so on. The eigenvectors and eigenvalues of the variance matrix express the main directions and the size of the spread of the distribution.

> **Multivariate joint moment and joint moment generating function.** When $$E(\lvert X_1^{r_1}\cdots X_k^{r_k}\rvert) < +\infty$$, $$E(X_1^{r_1}\cdots X_k^{r_k})$$ is the $$(r_1, \dots, r_k)$$-th joint moment of $$\mathbf{X}$$, written $$m_{r_1, \dots, r_k}$$. If $$E(e^{t_1X_1 + \cdots + t_kX_k})$$ is a real number for $$t_i$$ in open intervals containing $$0$$, the function
>
> $$
> M(t_1, \dots, t_k) = E\bigl(e^{t_1X_1 + \cdots + t_kX_k}\bigr), \quad -h_i < t_i < h_i\ (\exists h_i > 0)\ (i = 1, \dots, k)
> $$
>
> is the joint moment generating function of $$\mathbf{X}$$.
{: .definition #def-joint-mgf-k }

> **Theorem 2.5.5 (Properties of the joint moment generating function).**
>
> - (a) *(Generation of joint moments.)* If the joint mgf of $$\mathbf{X}$$ exists, then all joint moments exist and
>
>   $$
>   E(X_1^{r_1}\cdots X_k^{r_k}) = \Bigl[\frac{\partial^{r_1 + \cdots + r_k}}{\partial t_1^{r_1}\cdots\partial t_k^{r_k}}M(t_1, \dots, t_k)\Bigr]_{t_1 = \cdots = t_k = 0}, \quad M(t_1, \dots, t_k) = \sum_{r_1 = 0}^{\infty}\cdots\sum_{r_k = 0}^{\infty}\frac{E(X_1^{r_1}\cdots X_k^{r_k})}{r_1!\cdots r_k!}t_1^{r_1}\cdots t_k^{r_k}.
>   $$
>
> - (b) *(Determination of the distribution.)* If the joint mgfs of $$\mathbf{X}$$ and $$\mathbf{Y}$$ exist and agree on an open interval containing $$0$$, then the distributions of $$\mathbf{X}$$ and $$\mathbf{Y}$$ agree.
{: .theorem #thm-joint-mgf-properties-k }

The joint cumulant generating function is $$C(t_1, \dots, t_k) = \log M(t_1, \dots, t_k)$$, and differentiating it,

$$
\Bigl[\frac{\partial}{\partial t_i}C(t_1, \dots, t_k)\Bigr]_{t_1 = \cdots = t_k = 0} = E(X_i), \qquad \Bigl[\frac{\partial^2}{\partial t_i\partial t_j}C(t_1, \dots, t_k)\Bigr]_{t_1 = \cdots = t_k = 0} = \mathrm{Cov}(X_i, X_j).
$$

In vector notation, $$C(\mathbf{t}) = \dot{C}(0)^t\mathbf{t} + \frac{1}{2}\mathbf{t}^t\ddot{C}(0)\mathbf{t} + \cdots$$, $$E(\mathbf{X}) = \dot{C}(0)$$ and $$\mathrm{Var}(\mathbf{X}) = \ddot{C}(0)$$, where $$\dot{C}$$ is the gradient vector and $$\ddot{C}$$ the Hessian matrix.

**Example 2.5.9.** For $$f(x_1, x_2, x_3) = 6e^{-x_1 - x_2 - x_3}I_{(0 \le x_1 \le x_2 \le x_3)}$$ of Example 2.5.2, the joint mgf is

$$
M_{\mathbf{X}}(\mathbf{t}) = \iiint_{0 \le x_1 \le x_2 \le x_3}e^{t_1x_1 + t_2x_2 + t_3x_3}\cdot 6e^{-x_1 - x_2 - x_3}\,dx_3\,dx_2\,dx_1 = 6(3 - t_1 - t_2 - t_3)^{-1}(2 - t_2 - t_3)^{-1}(1 - t_3)^{-1},
$$

for $$t_1 + t_2 + t_3 < 3$$, $$t_2 + t_3 < 2$$, $$t_3 < 1$$. Hence the joint cumulant generating function is, for $$(t_1 + t_2 + t_3)/3 < 1$$, $$(t_2 + t_3)/2 < 1$$, $$t_3 < 1$$,

$$
C(\mathbf{t}) = -\log\Bigl(1 - \frac{t_1 + t_2 + t_3}{3}\Bigr) - \log\Bigl(1 - \frac{t_2 + t_3}{2}\Bigr) - \log(1 - t_3).
$$

Using $$-\log(1 - A) = A + A^2/2 + A^3/3 + \cdots$$ ($$-1 < A < 1$$) and arranging the result by order in $$t_1, t_2, t_3$$,

$$
C(\mathbf{t}) = \frac{1}{3}t_1 + \frac{5}{6}t_2 + \frac{11}{6}t_3 + \frac{1}{2}\Bigl(\frac{1}{9}t_1^2 + \frac{13}{36}t_2^2 + \frac{49}{36}t_3^2 + \frac{1}{9}\cdot 2t_1t_2 + \frac{1}{9}\cdot 2t_1t_3 + \frac{13}{36}\cdot 2t_2t_3\Bigr) + \cdots
$$

and from the coefficients of the terms of first and second order,

$$
E(\mathbf{X}) = \begin{pmatrix}1/3 \\ 5/6 \\ 11/6\end{pmatrix}, \qquad \mathrm{Var}(\mathbf{X}) = \frac{1}{36}\begin{pmatrix}4 & 4 & 4 \\ 4 & 13 & 13 \\ 4 & 13 & 49\end{pmatrix}.
$$

**Conditional distribution of multivariate random variables.** For $$(X_1, \dots, X_k)^t$$ with joint pdf $$f_{1,2,\dots,k}$$ and marginal pdf $$f_1$$ of $$X_1$$, the conditional pdf of $$(X_2, \dots, X_k)^t$$ given $$X_1 = x_1$$ is $$f_{2,\dots,k \mid 1}(x_2, \dots, x_k \mid x_1) = \dfrac{f_{1,2,\dots,k}(x_1, x_2, \dots, x_k)}{f_1(x_1)}$$ ($$x_1 : f_1(x_1) > 0$$). Also, the conditional pdf of $$X_1$$ given $$(X_2, \dots, X_k)^t = (x_2, \dots, x_k)^t$$ is $$f_{1 \mid 2,\dots,k}(x_1 \mid x_2, \dots, x_k) = \dfrac{f_{1,2,\dots,k}(x_1, \dots, x_k)}{f_{2,\dots,k}(x_2, \dots, x_k)}$$ ($$f_{2,\dots,k}(x_2, \dots, x_k) > 0$$). In general, for random vectors $$\mathbf{X}, \mathbf{Y}$$ with joint pdf $$f_{\mathbf{X},\mathbf{Y}}(x, y)$$ and marginal pdf $$f_{\mathbf{X}}(x)$$ of $$\mathbf{X}$$, the conditional pdf of $$\mathbf{Y}$$ given $$\mathbf{X} = x$$ is $$f_{\mathbf{Y} \mid \mathbf{X}}(y \mid x) = f_{\mathbf{X},\mathbf{Y}}(x, y)/f_{\mathbf{X}}(x)$$ ($$x : f_{\mathbf{X}}(x) > 0$$).

**Example 2.5.10.** For $$f(x_1, x_2, x_3) = 120x_1(1 - x_1 - x_2 - x_3)I_{(x_1 \ge 0,\ x_2 \ge 0,\ x_3 \ge 0,\ x_1 + x_2 + x_3 \le 1)}$$ of Example 2.5.5, the marginal pdfs of $$X_1$$ and of $$(X_2, X_3)^t$$ are

$$
f_1(x_1) = 20x_1(1 - x_1)^3I_{(0 \le x_1 \le 1)}, \qquad f_{2,3}(x_2, x_3) = 20(1 - x_2 - x_3)^3I_{(x_2 \ge 0,\ x_3 \ge 0,\ x_2 + x_3 \le 1)}.
$$

Hence the conditional pdf of $$(X_2, X_3)^t$$ given $$X_1 = x_1$$ is $$f_{2,3 \mid 1}(x_2, x_3 \mid x_1) = \dfrac{6(1 - x_1 - x_2 - x_3)}{(1 - x_1)^3}I_{(x_2 \ge 0,\ x_3 \ge 0,\ x_2 + x_3 \le 1 - x_1)}$$, and the conditional pdf of $$X_1$$ given $$(X_2, X_3)^t = (x_2, x_3)^t$$ is $$f_{1 \mid 2,3}(x_1 \mid x_2, x_3) = \dfrac{6x_1(1 - x_1 - x_2 - x_3)}{(1 - x_2 - x_3)^3}I_{(0 \le x_1 \le 1 - x_2 - x_3)}$$.

> **Conditional expectation of multivariate random variables.** For $$\mathbf{X} = (X_1, \dots, X_k)^t$$, $$\mathbf{Y} = (Y_1, \dots, Y_l)^t$$, given $$\mathbf{X} = x$$ the conditional expectation of a real-valued function $$g(\mathbf{X}, \mathbf{Y})$$ is $$E(g(\mathbf{X}, \mathbf{Y}) \mid \mathbf{X} = x) = \sum_{y_1}\cdots\sum_{y_l}g(x, y_1, \dots, y_l)f_{\mathbf{Y} \mid \mathbf{X}}(y_1, \dots, y_l \mid x)$$ (discrete), or $$\int\cdots\int g(x, y_1, \dots, y_l)f_{\mathbf{Y} \mid \mathbf{X}}(y_1, \dots, y_l \mid x)\,dy_l\cdots dy_1$$ (continuous), assuming absolute convergence. The conditional mean vector and conditional variance matrix are $$E(\mathbf{Y} \mid \mathbf{X}) = (E(Y_1 \mid \mathbf{X}), \dots, E(Y_l \mid \mathbf{X}))^t$$ and $$\mathrm{Var}(\mathbf{Y} \mid \mathbf{X}) = (\mathrm{Cov}(Y_i, Y_j \mid \mathbf{X}))_{1 \le i, j \le l}$$.
{: .definition #def-conditional-expectation-k }

> **Theorem 2.5.6 (Properties of conditional expectation).** (a) $$E[E(\mathbf{Y} \mid \mathbf{X})] = E(\mathbf{Y})$$. (b) $$\mathrm{Cov}(\mathbf{Y} - E(\mathbf{Y} \mid \mathbf{X}),\ v(\mathbf{X})) = 0$$ for all $$v(\mathbf{X})$$.
{: .theorem #thm-conditional-expectation-properties-k }

**Example 2.5.11.** In Example 2.5.10, given $$X_1 = x_1$$ the conditional pdf of $$(X_2, X_3)^t$$ is $$f_{2,3 \mid 1} = \dfrac{6(1 - x_1 - x_2 - x_3)}{(1 - x_1)^3}I_{(\cdots)}$$, so

$$
E(X_2 \mid X_1 = x_1) = (1 - x_1)/4, \quad E(X_2^2 \mid X_1 = x_1) = (1 - x_1)^2/10, \quad E(X_2X_3 \mid X_1 = x_1) = (1 - x_1)^2/20,
$$

$$
\mathrm{Var}(X_2 \mid X_1 = x_1) = (1/10 - 1/16)(1 - x_1)^2 = (3/80)(1 - x_1)^2, \qquad \mathrm{Cov}(X_2, X_3 \mid X_1 = x_1) = (1/20 - 1/16)(1 - x_1)^2 = (-1/80)(1 - x_1)^2.
$$

$$
\therefore\ E\Bigl[\binom{X_2}{X_3}\Big\vert X_1\Bigr] = \binom{1/4}{1/4}(1 - X_1), \qquad \mathrm{Var}\Bigl[\binom{X_2}{X_3}\Big\vert X_1\Bigr] = \frac{1}{80}\begin{pmatrix}3 & -1 \\ -1 & 3\end{pmatrix}(1 - X_1)^2.
$$

> **Theorem 2.5.7 (Decomposition of the variance matrix).** $$\mathrm{Var}(\mathbf{Y}) = E[\mathrm{Var}(\mathbf{Y} \mid \mathbf{X})] + \mathrm{Var}[E(\mathbf{Y} \mid \mathbf{X})]$$.
{: .theorem #thm-variance-matrix-decomposition }

*Proof.* From the properties of conditional expectation, $$\mathrm{Cov}(\mathbf{Y} - E(\mathbf{Y} \mid \mathbf{X}), E(\mathbf{Y} \mid \mathbf{X})) = 0$$, so $$\mathrm{Var}(\mathbf{Y}) = \mathrm{Var}[(\mathbf{Y} - E(\mathbf{Y} \mid \mathbf{X})) \oplus E(\mathbf{Y} \mid \mathbf{X})] = \mathrm{Var}(\mathbf{Y} - E(\mathbf{Y} \mid \mathbf{X})) + \mathrm{Var}[E(\mathbf{Y} \mid \mathbf{X})]$$. With $$W = \mathbf{Y} - E(\mathbf{Y} \mid \mathbf{X})$$, $$E(WW^t \mid \mathbf{X}) = \mathrm{Var}(\mathbf{Y} \mid \mathbf{X})$$, so $$\mathrm{Var}(W) = E(WW^t) = E[E(WW^t \mid \mathbf{X})] = E[\mathrm{Var}(\mathbf{Y} \mid \mathbf{X})]$$. $$\square$$

**Example 2.5.12.** In Example 2.5.10 the marginal pdf of $$(X_2, X_3)^t$$ is $$f_{2,3}(x_2, x_3) = 20(1 - x_2 - x_3)^3I_{(\cdots)}$$, so $$\mathrm{Var}(\mathbf{Y}) = \begin{pmatrix}\mathrm{Var}(X_2) & \mathrm{Cov}(X_2, X_3) \\ \mathrm{Cov}(X_2, X_3) & \mathrm{Var}(X_3)\end{pmatrix} = \dfrac{1}{252}\begin{pmatrix}5 & -1 \\ -1 & 5\end{pmatrix}$$ for $$\mathbf{Y} = (X_2, X_3)^t$$. From Example 2.5.11, $$E(\mathbf{Y} \mid X_1) = \binom{1/4}{1/4}(1 - X_1)$$ and $$\mathrm{Var}(\mathbf{Y} \mid X_1) = \dfrac{1}{80}\begin{pmatrix}3 & -1 \\ -1 & 3\end{pmatrix}(1 - X_1)^2$$. With $$f_1(x_1) = 20x_1(1 - x_1)^3I_{(0 \le x_1 \le 1)}$$, $$E[(1 - X_1)^2] = 10/21$$ and $$\mathrm{Var}(X_1) = 2/63$$, hence

$$
E[\mathrm{Var}(\mathbf{Y} \mid X_1)] = \frac{1}{168}\begin{pmatrix}3 & -1 \\ -1 & 3\end{pmatrix}, \qquad \mathrm{Var}[E(\mathbf{Y} \mid X_1)] = \binom{1/4}{1/4}\mathrm{Var}(1 - X_1)\binom{1/4}{1/4}^t = \frac{1}{504}\begin{pmatrix}1 & 1 \\ 1 & 1\end{pmatrix},
$$

and the sum is $$\frac{1}{252}\begin{pmatrix}5 & -1 \\ -1 & 5\end{pmatrix} = \mathrm{Var}(\mathbf{Y})$$, as in Theorem 2.5.7.

> **Theorem 2.5.8 (Least squares predictor of multivariate random variables).** Among vector-valued functions $$u(\mathbf{X}) = (u_1(\mathbf{X}), \dots, u_k(\mathbf{X}))^t$$ of the random vector $$\mathbf{X}$$, the one minimizing $$E[\lVert\mathbf{Y} - u(\mathbf{X})\rVert^2] = E[(Y_1 - u_1(\mathbf{X}))^2 + \cdots + (Y_k - u_k(\mathbf{X}))^2]$$ is $$E(\mathbf{Y} \mid \mathbf{X}) = (E(Y_1 \mid \mathbf{X}), \dots, E(Y_k \mid \mathbf{X}))^t$$. That is, $$E[\lVert\mathbf{Y} - E(\mathbf{Y} \mid \mathbf{X})\rVert^2] \le E[\lVert\mathbf{Y} - u(\mathbf{X})\rVert^2]$$ for all $$u(\mathbf{X})$$.
{: .theorem #thm-least-squares-predictor-k }

*Proof.* By property (b) of conditional expectation, in the same way as Theorem 2.3.5. $$\square$$

## Independence of several random variables

For random variables $$X_1, \dots, X_n$$, if $$P(X_1 \in A_1, \dots, X_n \in A_n) = P(X_1 \in A_1)\cdots P(X_n \in A_n)$$ for all $$A_i$$ ($$i = 1, \dots, n$$), the random variables $$X_1, \dots, X_n$$ are called *mutually independent*. This independence is defined in the same way for multivariate random variables, and the following theorem holds.

> **Theorem 2.5.9 (Independence of multivariate random variables).** Each of the following conditions is necessary and sufficient for the multivariate random variables $$X_1, \dots, X_n$$ to be mutually independent.
>
> - (a) (pdf) $$pdf_{1,\dots,n}(x_1, \dots, x_n) = pdf_1(x_1)\cdots pdf_n(x_n)$$ for all $$x_i$$ ($$i = 1, \dots, n$$).
> - (b) (mgf) $$mgf_{1,\dots,n}(t_1, \dots, t_n) = mgf_1(t_1)\cdots mgf_n(t_n)$$ for all $$t_i$$ with $$\lVert t_i\rVert < h_i$$ ($$\exists h_i > 0$$) ($$i = 1, \dots, n$$). (Assuming the mgf exists.)
{: .theorem #thm-independence-multivariate }

**Example 2.5.13.** For $$f_{1,2,3}(x_1, x_2, x_3) = 6e^{-x_1 - x_2 - x_3}I_{(0 \le x_1 \le x_2 \le x_3)}$$ of Example 2.5.2, the marginal densities of $$X_1, X_2, X_3$$ are

$$
f_1(x_1) = 3e^{-3x_1}I_{(x_1 \ge 0)}, \qquad f_2(x_2) = 6e^{-2x_2}(1 - e^{-x_2})I_{(x_2 \ge 0)}, \qquad f_3(x_3) = 3e^{-x_3}(1 - e^{-x_3})^2I_{(x_3 \ge 0)}.
$$

Since the joint pdf is not the product of the marginal pdfs, $$X_1, X_2, X_3$$ are not mutually independent.

As for two random variables, to establish the mutual independence of several random variables through Theorem 2.5.9 one need not find the marginal pdfs or marginal mgfs: instead of (a), (b) one may apply (a′) there exist functions $$g_1, \dots, g_n$$ with $$pdf_{1,\dots,n}(x_1, \dots, x_n) = g_1(x_1)\cdots g_n(x_n)$$; (b′) there exist functions $$m_1, \dots, m_n$$ with $$mgf_{1,\dots,n}(t_1, \dots, t_n) = m_1(t_1)\cdots m_n(t_n)$$.

**Example 2.5.14.** For $$\mathbf{X} = (X_1, X_2, X_3)^t$$ of Example 2.5.9 and $$Y_1 = X_1$$, $$Y_2 = X_2 - X_1$$, $$Y_3 = X_3 - X_2$$, show that $$Y_1, Y_2, Y_3$$ are mutually independent.

*Solution.* By Example 2.5.9, $$M_{\mathbf{X}}(t_1, t_2, t_3) = 6(3 - t_1 - t_2 - t_3)^{-1}(2 - t_2 - t_3)^{-1}(1 - t_3)^{-1}$$, $$t_1 + t_2 + t_3 < 3$$, $$t_2 + t_3 < 2$$, $$t_3 < 1$$. Hence the joint mgf of $$\mathbf{Y} = (Y_1, Y_2, Y_3)^t$$ is

$$
\begin{aligned}
M_{\mathbf{Y}}(s_1, s_2, s_3) &= E\bigl(e^{s_1Y_1 + s_2Y_2 + s_3Y_3}\bigr) = E\bigl[e^{s_1X_1 + s_2(X_2 - X_1) + s_3(X_3 - X_2)}\bigr] = E\bigl[e^{(s_1 - s_2)X_1 + (s_2 - s_3)X_2 + s_3X_3}\bigr] \\
&= 6\bigl(3 - (s_1 - s_2) - (s_2 - s_3) - s_3\bigr)^{-1}\bigl(2 - (s_2 - s_3) - s_3\bigr)^{-1}(1 - s_3)^{-1} = 6(3 - s_1)^{-1}(2 - s_2)^{-1}(1 - s_3)^{-1},
\end{aligned}
$$

for $$s_1 < 3$$, $$s_2 < 2$$, $$s_3 < 1$$, which has the form $$m_1(s_1)m_2(s_2)m_3(s_3)$$. Therefore $$Y_1, Y_2, Y_3$$ are mutually independent.

> **Theorem 2.5.10 (Properties of independent multivariate random variables).**
>
> - (a) *(Functions of independent random variables.)* If $$X_1, \dots, X_n$$ are mutually independent, so are the functions $$g_1(X_1), \dots, g_n(X_n)$$.
> - (b) *(Expectation of a product.)* If they are mutually independent, then $$E[g_1(X_1)\cdots g_n(X_n)] = E[g_1(X_1)]\cdots E[g_n(X_n)]$$ for real-valued $$g_1, \dots, g_n$$. (Assuming the expectations are defined as real numbers.)
> - (c) *(Independence and correlation.)* If they are mutually independent, then $$\mathrm{Cov}(X_i, X_j) = 0$$ ($$i \ne j$$) ($$i, j = 1, \dots, n$$). (Assuming the covariance matrix is a real matrix.)
{: .theorem #thm-independent-multivariate-properties }

> **Theorem 2.5.11 (Sum of mutually independent random variables).**
>
> - (a) *(Variance matrix of a sum.)* If $$X_1, \dots, X_n$$ are mutually independent, then $$\mathrm{Var}(X_1 + \cdots + X_n) = \mathrm{Var}(X_1) + \cdots + \mathrm{Var}(X_n)$$.
> - (b) *(Mgf of a sum.)* If $$X_1, \dots, X_n$$ are mutually independent, then $$mgf_{X_1 + \cdots + X_n}(t) = mgf_{X_1}(t)\cdots mgf_{X_n}(t)$$.
{: .theorem #thm-sum-independent }

*Proof.* (a) By (d) of Theorem 2.5.3 (linearity of the covariance matrix), $$\mathrm{Var}(X_1 + \cdots + X_n) = \mathrm{Cov}\bigl(\sum_i X_i, \sum_j X_j\bigr) = \sum_{i=1}^{n}\sum_{j=1}^{n}\mathrm{Cov}(X_i, X_j)$$, so (a) follows from the relation between independence and correlation in Theorem 2.5.10. (b) From the definition of the mgf and property (b) of Theorem 2.5.10,

$$
mgf_{X_1 + \cdots + X_n}(t) = E\bigl[e^{t'(X_1 + \cdots + X_n)}\bigr] = E(e^{t'X_1})\cdots E(e^{t'X_n}) = mgf_{X_1}(t)\cdots mgf_{X_n}(t). \qquad \square
$$

## References

- 김우철, *수리통계학* (Mathematical Statistics), revised 2nd edition, 민영사, 2021 — Chapter 2, §2.5 (Examples 2.5.1 to 2.5.14, Theorems 2.5.1 to 2.5.11). Translated from the book; not from my notes.
- Mathematical Statistics 1 (326.311), Seoul National University, Spring 2025. Instructor: Jaeyong Lee (이재용).

[Previous](/posts/mathstat1-independence/) · [Overview](/posts/mathstat1-overview/) · [Homework 3, Chapter 2 Exercises](/posts/mathstat1-homework-3-chapter-2/)
