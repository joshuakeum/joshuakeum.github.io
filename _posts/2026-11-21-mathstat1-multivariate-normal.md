---
title: "Mathematical Statistics 1: Ch. 4 Part 4 — Multivariate Normal Distribution"
date: 2026-11-21 12:40:00 +0900
categories: [Study Notes, Mathematical Statistics 1]
tags: [multivariate normal, quadratic form, linear regression, conditional distribution, bivariate normal]
description: The multivariate normal distribution, its density and moment generating function, linear transformations, marginal and conditional distributions, quadratic forms and chi-square, and the sampling distributions in the linear regression model. Chapter 4, §4.4 of Mathematical Statistics 1.
math: true
mermaid: false
render_with_liquid: false
---

> My handwritten notes for Chapter 4 end with the order statistics and do not cover the multivariate normal distribution, so this post is **translated from the textbook**, §4.4. It is not my own writing. The exercises are in [Chapter 4 Exercises](/posts/mathstat1-exercises-chapter-4/).
{: .prompt-info }

## 4.4 Multivariate normal distribution

In statistical surveys one observes several related characteristics at once and makes inferences from them. As the basic model for such multidimensional data, the one-dimensional normal distribution is extended to the *multivariate normal distribution*.

> **Theorem 4.4.1.** Let $$Z_1, \dots, Z_n$$ be independent with $$N(0, 1)$$, and let $$A = (a_{ij})_{1 \le i \le n,\ 1 \le j \le n}$$ and $$\mu = (\mu_1, \dots, \mu_n)^t$$ be a constant matrix and vector. With $$X = AZ + \mu$$, that is $$X_i = a_{i1}Z_1 + \cdots + a_{in}Z_n + \mu_i$$:
>
> - (a) if $$A$$ is nonsingular, the pdf of $$X = AZ + \mu$$ is
>
>   $$
>   pdf_X(x) = (\det(2\pi\Sigma))^{-1/2}\exp\{-(x - \mu)^t\Sigma^{-1}(x - \mu)/2\}, \quad x \in \mathbb{R}^n \quad (\Sigma = AA^t);
>   $$
> - (b) the mgf of $$X = AZ + \mu$$ is $$mgf_X(t) = \exp\bigl(\mu^tt + \tfrac{1}{2}t^t\Sigma t\bigr)$$, $$t \in \mathbb{R}^n$$.
{: .theorem #thm-mvn-4-4-1 }

*Proof.* From Theorem 3.6.1 the pdf and the mgf of $$Z$$ are $$pdf_Z(z) = (2\pi)^{-n/2}e^{-z^tz/2}$$ and $$mgf_Z(s) = e^{s^ts/2}$$.

(a) For nonsingular $$A$$ the function $$u(z) = Az + \mu$$ is a one-to-one map of $$\mathbb{R}^n$$ onto $$\mathbb{R}^n$$ satisfying the conditions of Theorem 4.1.1, with inverse $$u^{-1}(x) = A^{-1}(x - \mu)$$ and Jacobian $$\det(A^{-1}) = (\det A)^{-1}$$. Hence

$$
pdf_X(x) = pdf_Z(u^{-1}(x))\lvert J_{u^{-1}}(x)\rvert = (2\pi)^{-n/2}\exp\{-\tfrac{1}{2}(A^{-1}(x - \mu))^t(A^{-1}(x - \mu))\}(\det A)^{-1},
$$

and with $$\Sigma = AA^t$$, $$\det(2\pi\Sigma) = (2\pi)^n(\det A)^2$$, giving the stated pdf.

(b) $$mgf_X(t) = E[\exp\{t^t(AZ + \mu)\}] = mgf_Z(A^tt)\exp(t^t\mu) = \exp\{\mu^tt + \tfrac{1}{2}(A^tt)^t(A^tt)\} = \exp(\mu^tt + \tfrac{1}{2}t^t\Sigma t)$$. $$\square$$

The distribution of $$X$$ found in Theorem 4.4.1 is the *multivariate normal distribution*, written $$X \sim N_n(\mu, \Sigma)$$, or $$X \sim N(\mu, \Sigma)$$ for short. In the case of (a), where $$\Sigma$$ is an invertible positive definite matrix, it is called the *nonsingular multivariate normal distribution*.

> **Theorem 4.4.2.**
>
> - (a) If $$X \sim N(\mu, \Sigma)$$, then $$E(X) = \mu$$ and $$\mathrm{Var}(X) = \Sigma$$.
> - (b) For a variance matrix $$\Sigma$$, with $$AA^t = \Sigma$$ and $$A = A^t$$ the matrix $$A = \Sigma^{1/2}$$: $$X \sim N_n(\mu, \Sigma) \Longleftrightarrow X \overset{d}{=} \Sigma^{1/2}Z + \mu$$, $$Z \sim N_n(0, I)$$.
{: .theorem #thm-mvn-4-4-2 }

*Proof.* (a) As shown in §2.5, the mean vector and variance matrix are found by differentiating the cumulant generating function $$C(t) = \log mgf_X(t) = \mu^tt + \frac{1}{2}t^t\Sigma t$$: $$E(X) = \dot{C}(0) = \mu$$, $$\mathrm{Var}(X) = \ddot{C}(0) = \Sigma$$. (b) As in Theorem 4.4.1(b), the mgf of $$\Sigma^{1/2}Z + \mu$$ with $$\Sigma^{1/2}\Sigma^{1/2} = \Sigma$$ is $$\exp\{\mu^tt + \frac{1}{2}t^t\Sigma t\}$$, so $$X \sim N_n(\mu, \Sigma)$$. $$\square$$

> **Definition of the multivariate normal distribution.** $$Z \sim N(0, I) \Leftrightarrow Z = (Z_1, \dots, Z_n)^t$$, $$Z_i \overset{iid}{\sim} N(0, 1)$$ ($$i = 1, \dots, n$$).
>
> $$X \sim N_n(\mu, \Sigma) \Leftrightarrow$$ (1) $$X \overset{d}{=} AZ + \mu$$, $$Z \sim N(0, I)$$, $$AA^t = \Sigma$$ $$\Leftrightarrow$$ (2) $$X \overset{d}{=} \Sigma^{1/2}Z + \mu$$, $$Z \sim N_n(0, I)$$, $$\Sigma^{1/2}\Sigma^{1/2} = \Sigma$$, $$\Sigma^{1/2} = (\Sigma^{1/2})^t$$ $$\Leftrightarrow$$ (3) $$mgf_X(t) = \exp\{\mu^tt + \frac{1}{2}t^t\Sigma t\}$$, $$t \in \mathbb{R}^n$$ $$\Leftrightarrow$$ (4) (when $$\Sigma$$ is positive definite) $$pdf_X(x) = (\det(2\pi\Sigma))^{-1/2}\exp\{-\frac{1}{2}(x - \mu)^t\Sigma^{-1}(x - \mu)\}$$, $$x \in \mathbb{R}^n$$.
{: .definition #def-mvn }

(In (1), $$A$$ need not be an $$n \times n$$ square matrix; any $$n \times m$$ matrix with $$AA^t = \Sigma$$ is allowed.)

**Example 4.4.1 (Bivariate normal distribution).** $$N\bigl(\binom{\mu_1}{\mu_2}, \begin{pmatrix}\sigma_1^2 & \rho\sigma_1\sigma_2 \\ \rho\sigma_1\sigma_2 & \sigma_2^2\end{pmatrix}\bigr)$$, or $$N(\mu_1, \mu_2; \sigma_1^2, \sigma_2^2, \rho)$$. Since $$\det\Sigma = \sigma_1^2\sigma_2^2(1 - \rho^2)$$, for $$\sigma_1 > 0$$, $$\sigma_2 > 0$$, $$-1 < \rho < 1$$,

$$
\Sigma^{-1} = \frac{1}{\sigma_1^2\sigma_2^2(1 - \rho^2)}\begin{pmatrix}\sigma_2^2 & -\rho\sigma_1\sigma_2 \\ -\rho\sigma_1\sigma_2 & \sigma_1^2\end{pmatrix}, \qquad f(x_1, x_2) = \frac{1}{2\pi\sigma_1\sigma_2\sqrt{1 - \rho^2}}e^{-Q/2},
$$

$$
Q = \frac{1}{1 - \rho^2}\Bigl\{\Bigl(\frac{x_1 - \mu_1}{\sigma_1}\Bigr)^2 - 2\rho\Bigl(\frac{x_1 - \mu_1}{\sigma_1}\Bigr)\Bigl(\frac{x_2 - \mu_2}{\sigma_2}\Bigr) + \Bigl(\frac{x_2 - \mu_2}{\sigma_2}\Bigr)^2\Bigr\}.
$$

For $$\rho = \pm 1$$ the variance matrix has no inverse, and $$\rho = 1 \Leftrightarrow P\bigl(\frac{X_2 - \mu_2}{\sigma_2} = \frac{X_1 - \mu_1}{\sigma_1}\bigr) = 1$$, $$\rho = -1 \Leftrightarrow P\bigl(\frac{X_2 - \mu_2}{\sigma_2} = -\frac{X_1 - \mu_1}{\sigma_1}\bigr) = 1$$.

> **Theorem 4.4.3 (Properties of the multivariate normal distribution).**
>
> - (a) If $$X \sim N(\mu, \Sigma)$$, then for a constant matrix and vector $$A$$ and $$b$$, $$AX + b \sim N(A\mu + b, A\Sigma A^t)$$.
> - (b) If $$\binom{X_1}{X_2} \sim N\bigl(\binom{\mu_1}{\mu_2}, \begin{pmatrix}\Sigma_{11} & \Sigma_{12} \\ \Sigma_{21} & \Sigma_{22}\end{pmatrix}\bigr)$$, then $$\mathrm{Cov}(X_1, X_2) = \Sigma_{12} = 0$$ implies that $$X_1$$ and $$X_2$$ are independent.
> - (c) If $$X \sim N(\mu, \Sigma)$$ and $$A, B$$ are constant matrices, then $$\mathrm{Cov}(AX, BX) = A\Sigma B^t = 0$$ implies that $$AX$$ and $$BX$$ are independent.
{: .theorem #thm-mvn-4-4-3 }

*Proof.* (a) By the definition of the multivariate normal distribution, $$X \overset{d}{=} \Sigma^{1/2}Z + \mu$$, so $$AX + b \overset{d}{=} (A\Sigma^{1/2})Z + (A\mu + b)$$ with $$(A\Sigma^{1/2})(A\Sigma^{1/2})^t = A\Sigma A^t$$; hence $$AX + b \sim N(A\mu + b, A\Sigma A^t)$$.

(b) The joint mgf of $$X_1$$ and $$X_2$$ is $$\exp\bigl\{\binom{\mu_1}{\mu_2}^t\binom{t_1}{t_2} + \frac{1}{2}\binom{t_1}{t_2}^t\begin{pmatrix}\Sigma_{11} & \Sigma_{12} \\ \Sigma_{21} & \Sigma_{22}\end{pmatrix}\binom{t_1}{t_2}\bigr\}$$. If $$\Sigma_{12} = \Sigma_{21}^t = 0$$ this equals $$\exp\{\mu_1^tt_1 + \frac{1}{2}t_1^t\Sigma_{11}t_1\}\exp\{\mu_2^tt_2 + \frac{1}{2}t_2^t\Sigma_{22}t_2\}$$, the product of a function of $$t_1$$ and a function of $$t_2$$. Therefore $$X_1$$ and $$X_2$$ are independent.

(c) From (a), $$\binom{AX}{BX} = \binom{A}{B}X \sim N\Bigl(\binom{A\mu}{B\mu}, \begin{pmatrix}A\Sigma A^t & A\Sigma B^t \\ B\Sigma A^t & B\Sigma B^t\end{pmatrix}\Bigr)$$, so by (b), $$\mathrm{Cov}(AX, BX) = A\Sigma B^t = 0$$ implies that $$AX$$ and $$BX$$ are independent. $$\square$$

**Example 4.4.2 (Independence in the bivariate normal distribution).** If two random variables $$X_1$$ and $$X_2$$ are independent, then $$\mathrm{Cov}(X_1, X_2) = 0$$, but the converse does not always hold. For $$(X_1, X_2)^t$$ following a bivariate normal distribution, however, $$\mathrm{Cov}(X_1, X_2) = 0$$ implies that $$X_1$$ and $$X_2$$ are independent.

> **Theorem 4.4.4 (Marginal and conditional distributions of the multivariate normal distribution).** Let $$\binom{X_1}{X_2} \sim N\bigl(\binom{\mu_1}{\mu_2}, \begin{pmatrix}\Sigma_{11} & \Sigma_{12} \\ \Sigma_{21} & \Sigma_{22}\end{pmatrix}\bigr)$$.
>
> - (a) (Marginal distribution.) $$X_1 \sim N(\mu_1, \Sigma_{11})$$.
> - (b) (Conditional distribution.) If the variance matrix is nonsingular, $$X_2\vert_{X_1 = x_1} \sim N\bigl(\mu_2 + \Sigma_{21}\Sigma_{11}^{-1}(x_1 - \mu_1),\ \Sigma_{22} - \Sigma_{21}\Sigma_{11}^{-1}\Sigma_{12}\bigr)$$.
{: .theorem #thm-mvn-4-4-4 }

*Proof.* (a) $$X_1 = (I, 0)\binom{X_1}{X_2}$$, so by Theorem 4.4.3(a), $$X_1 \sim N\bigl((I, 0)\binom{\mu_1}{\mu_2}, (I, 0)\Sigma\binom{I}{0}\bigr) = N(\mu_1, \Sigma_{11})$$.

(b) For a nonsingular partitioned matrix, $$\det\begin{pmatrix}\Sigma_{11} & \Sigma_{12} \\ \Sigma_{21} & \Sigma_{22}\end{pmatrix} = \det(\Sigma_{11})\det(\Sigma_{22} - \Sigma_{21}\Sigma_{11}^{-1}\Sigma_{12})$$, and with $$\Sigma_{22\cdot1} = \Sigma_{22} - \Sigma_{21}\Sigma_{11}^{-1}\Sigma_{12}$$ the inverse is the block matrix computed in Problem 5 of the [Chapter 3 Exercises](/posts/mathstat1-exercises-chapter-3/). Computing $$pdf_{X_2\vert X_1 = x_1}(x_2 \mid x_1) = pdf_{X_1, X_2}(x_1, x_2)/pdf_{X_1}(x_1)$$ proves (b). Alternatively, (b) is equivalent to $$X_2 - \mu_2 - \Sigma_{21}\Sigma_{11}^{-1}(X_1 - \mu_1)\vert_{X_1 = x_1} \sim N(0, \Sigma_{22} - \Sigma_{21}\Sigma_{11}^{-1}\Sigma_{12})$$, and

$$
\begin{pmatrix}X_1 - \mu_1 \\ X_2 - \mu_2 - \Sigma_{21}\Sigma_{11}^{-1}(X_1 - \mu_1)\end{pmatrix} = \begin{pmatrix}I & 0 \\ -\Sigma_{21}\Sigma_{11}^{-1} & I\end{pmatrix}\begin{pmatrix}X_1 - \mu_1 \\ X_2 - \mu_2\end{pmatrix},
$$

$$
\begin{pmatrix}I & 0 \\ -\Sigma_{21}\Sigma_{11}^{-1} & I\end{pmatrix}\begin{pmatrix}\Sigma_{11} & \Sigma_{12} \\ \Sigma_{21} & \Sigma_{22}\end{pmatrix}\begin{pmatrix}I & 0 \\ -\Sigma_{21}\Sigma_{11}^{-1} & I\end{pmatrix}^t = \begin{pmatrix}\Sigma_{11} & 0 \\ 0 & \Sigma_{22} - \Sigma_{21}\Sigma_{11}^{-1}\Sigma_{12}\end{pmatrix}.
$$

So by Theorem 4.4.3(a) the vector is $$N\bigl(0, \mathrm{diag}(\Sigma_{11}, \Sigma_{22\cdot1})\bigr)$$, and by Theorem 4.4.3(b), $$X_1 - \mu_1$$ and $$X_2 - \mu_2 - \Sigma_{21}\Sigma_{11}^{-1}(X_1 - \mu_1)$$ are independent, with the latter $$\sim N(0, \Sigma_{22} - \Sigma_{21}\Sigma_{11}^{-1}\Sigma_{12})$$. Hence the conditional distribution in (b) holds. $$\square$$

**Example 4.4.3 (Conditional distribution in the bivariate normal distribution $$N(\mu_1, \mu_2; \sigma_1^2, \sigma_2^2, \rho)$$).**

$$
X_2\vert_{X_1 = x_1} \sim N\bigl(\mu_2 + \rho\sigma_2(x_1 - \mu_1)/\sigma_1,\ \sigma_2^2(1 - \rho^2)\bigr).
$$

> **Theorem 4.4.5 (Distribution of quadratic forms).**
>
> - (a) If $$X \sim N_k(\mu, \Sigma)$$ and the variance matrix $$\Sigma$$ is nonsingular, then $$(X - \mu)^t\Sigma^{-1}(X - \mu) \sim \chi^2(k)$$.
> - (b) For $$Z \sim N(0, I)$$, if $$A^2 = A$$ then $$Z^tAZ \sim \chi^2(r)$$ with degrees of freedom $$r = \mathrm{trace}(A)$$.
{: .theorem #thm-mvn-4-4-5 }

(In a quadratic form $$Z^tAZ$$ the matrix $$A$$ is always assumed symmetric, since $$x^tAx = x^t\frac{A + A^t}{2}x$$. The condition $$A^2 = A$$ in (b) is in fact also necessary for $$Z^tAZ \sim \chi^2(r)$$.)

*Proof.* (a) Let $$\Sigma^{-1/2}$$ be the inverse of the symmetric matrix $$\Sigma^{1/2}$$ with $$\Sigma^{1/2}\Sigma^{1/2} = \Sigma$$. Since $$\Sigma^{-1/2}\Sigma(\Sigma^{-1/2})^t = I$$, Theorem 4.4.3(a) gives $$\Sigma^{-1/2}(X - \mu) \sim N_k(0, I)$$. So with $$Z = \Sigma^{-1/2}(X - \mu)$$, $$(X - \mu)^t\Sigma^{-1}(X - \mu) = Z^tZ = Z_1^2 + \cdots + Z_k^2$$, $$Z_i \overset{iid}{\sim} N(0, 1)$$, and by the representational definition of the chi-squared distribution it is $$\chi^2(k)$$.

(b) Since $$A$$ is a symmetric matrix with real entries it can be diagonalized: $$A = P^t\,\mathrm{diag}(\lambda_1, \dots, \lambda_n)\,P$$, $$P^tP = PP^t = I$$, where $$\lambda_1, \dots, \lambda_n$$ are the eigenvalues. If $$A^2 = A$$, then $$\lambda_i^2 = \lambda_i$$, so each $$\lambda_i$$ is $$0$$ or $$1$$. Assume $$r$$ of them are $$1$$: $$\lambda_1 = \cdots = \lambda_r = 1$$, $$\lambda_{r+1} = \cdots = \lambda_n = 0$$. Then $$Z^tAZ = (PZ)^t\begin{pmatrix}I_r & 0 \\ 0 & 0\end{pmatrix}(PZ)$$. With $$X = PZ \sim N_n(0, PP^t) = N_n(0, I)$$, $$Z^tAZ = X_1^2 + \cdots + X_r^2$$, $$X_i \overset{iid}{\sim} N(0, 1)$$, so $$Z^tAZ \sim \chi^2(r)$$. $$\square$$

**Example 4.4.4 (Sampling distribution in the one-way classification model).** In Theorem 4.2.7(a), let $$Y_i = \bar{X}_i - \bar{X} - (\mu_i - \bar{\mu})$$ ($$i = 1, \dots, k$$) and $$Y = (Y_1, \dots, Y_r)^t$$, $$r = k - 1$$. Then $$E(Y_i) = 0$$, $$\mathrm{Var}(Y_i) = (n_i^{-1} - n^{-1})\sigma^2$$, $$\mathrm{Cov}(Y_i, Y_j) = -n^{-1}\sigma^2$$ ($$i \ne j$$), so $$Y \sim N_r(0, \Sigma)$$ with $$\Sigma = [D(n_i^{-1}) - n^{-1}11^t]\sigma^2$$, and $$Y^t\Sigma^{-1}Y = \bigl(\sum_{i=1}^{r}n_iY_i^2 + n_k^{-1}(\sum_{i=1}^{r}n_iY_i)^2\bigr)/\sigma^2 = \sum_{i=1}^{k}n_iY_i^2/\sigma^2$$. By Theorem 4.4.5(a), $$\sum_in_i(\bar{X}_i - \bar{X} - (\mu_i - \bar{\mu}))^2/\sigma^2 \sim \chi^2(k - 1)$$.

**Example 4.4.5 (Sampling distribution of the sample variance).** For a random sample from $$N(\mu, \sigma^2)$$, $$X = (X_1, \dots, X_n)^t \sim N_n(\mu 1, \sigma^2I)$$, $$\bar{X} = n^{-1}1^tX$$, $$(n-1)S^2 = X^t(I - n^{-1}11^t)X$$. The matrix $$I - n^{-1}11^t$$ is symmetric with $$1^t(I - n^{-1}11^t) = 0$$, so $$\mathrm{Cov}(1^tX, (I - n^{-1}11^t)X) = 1^t(\sigma^2I)(I - n^{-1}11^t)^t = 0$$ and by Theorem 4.4.3(c) $$\bar{X}$$ and $$(I - n^{-1}11^t)X$$ are independent. Since $$(I - n^{-1}11^t)^2 = I - n^{-1}11^t$$ we have $$X^t(I - n^{-1}11^t)X = [(I - n^{-1}11^t)X]^t[(I - n^{-1}11^t)X]$$, so $$\bar{X}$$ and $$(n-1)S^2$$ are independent. Also $$(n-1)S^2/\sigma^2 = (X - \mu1)^t(I - n^{-1}11^t)(X - \mu1)/\sigma^2$$ with $$(X - \mu1)/\sigma \sim N_n(0, I)$$, $$(I - n^{-1}11^t)^2 = I - n^{-1}11^t$$ and $$\mathrm{trace}(I - n^{-1}11^t) = n - 1$$, so by Theorem 4.4.5(b), $$(n-1)S^2/\sigma^2 \sim \chi^2(n-1)$$.

## Linear regression model

The most basic model for studying functional relationships among variables is the *linear regression model*: the response variable $$Y$$ is determined by the explanatory variables $$x_0, x_1, \dots, x_p$$ and the error variable $$e$$, and the relationship is assumed to be linear.

> **Linear regression model (normal errors).**
>
> $$
> Y_i = x_{i0}\beta_0 + x_{i1}\beta_1 + \cdots + x_{ip}\beta_p + e_i, \quad e_i \overset{iid}{\sim} N(0, \sigma^2), \quad i = 1, \dots, n,
> $$
>
> or, with $$Y = (Y_1, \dots, Y_n)^t$$, $$X = (x_{ij})$$ the $$n \times (p+1)$$ matrix of rank $$p + 1$$, $$\beta = (\beta_0, \dots, \beta_p)^t$$ (the regression coefficients), $$e = (e_1, \dots, e_n)^t$$:
>
> $$
> Y = X\beta + e, \qquad e \sim N_n(0, \sigma^2I).
> $$
{: .definition #def-regression-model }

The sample regression coefficient is $$\hat{\beta} = (X^tX)^{-1}X^tY$$, and the error variance is estimated by the mean squared error sum of squares $$\hat{\sigma}^2 = (Y - X\hat{\beta})^t(Y - X\hat{\beta})/(n - p - 1)$$.

**Example 4.4.6 (Sample regression coefficients in simple linear regression).** For $$p = 1$$ and $$x_0 = 1$$, $$Y_i = \beta_0 + x_{i1}\beta_1 + e_i$$, we have $$X^tX = \begin{pmatrix}n & \sum x_{i1} \\ \sum x_{i1} & \sum x_{i1}^2\end{pmatrix}$$, $$X^tY = \binom{\sum Y_i}{\sum x_{i1}Y_i}$$ and

$$
\hat{\beta}_1 = \frac{S_{xY}}{S_{xx}}, \quad S_{xY} = \sum(x_{i1} - \bar{x}_1)Y_i, \quad S_{xx} = \sum(x_{i1} - \bar{x}_1)^2, \qquad \hat{\beta}_0 = \bar{Y} - \bar{x}_1\hat{\beta}_1,
$$

that is, $$\hat{\beta}_0 + x_{i1}\hat{\beta}_1 = \bar{Y} + (x_{i1} - \bar{x}_1)\hat{\beta}_1$$.

**Example 4.4.7.** In the simple linear regression model the mean squared error sum of squares is $$\hat{\sigma}^2 = \sum(Y_i - \hat{\beta}_0 - \hat{\beta}_1x_{i1})^2/(n - 2) = \sum(Y_i - \bar{Y} - \hat{\beta}_1(x_{i1} - \bar{x}_1))^2/(n - 2)$$.

> **Theorem 4.4.6 (Fundamental theorem of sampling distributions in the linear regression model).** In the linear regression model $$Y = X\beta + e$$, $$e \sim N_n(0, \sigma^2I)$$ with $$X$$ an $$n \times (p+1)$$ constant matrix of rank $$p + 1$$:
>
> - (a) $$\hat{\beta} \sim N_{p+1}(\beta, \sigma^2(X^tX)^{-1})$$.
> - (b) The sample regression coefficient $$\hat{\beta}$$ and the mean squared error sum of squares $$\hat{\sigma}^2$$ are independent.
> - (c) $$(n - p - 1)\hat{\sigma}^2/\sigma^2 \sim \chi^2(n - p - 1)$$.
{: .theorem #thm-regression-fundamental }

*Proof.* (a) Since $$Y \sim N(X\beta, \sigma^2I)$$, Theorem 4.4.3(a) gives $$\hat{\beta} = (X^tX)^{-1}X^tY \sim N\bigl((X^tX)^{-1}X^tX\beta, \sigma^2[(X^tX)^{-1}X^t][(X^tX)^{-1}X^t]^t\bigr) = N(\beta, \sigma^2(X^tX)^{-1})$$.

(b) Let $$\Pi = X(X^tX)^{-1}X^t$$. It is symmetric, $$\Pi^2 = \Pi$$ and $$\Pi X = X$$. Since $$Y - X\hat{\beta} = Y - \Pi Y = (I - \Pi)Y$$, $$\mathrm{Cov}((X^tX)^{-1}X^tY, (I - \Pi)Y) = (X^tX)^{-1}X^t(\sigma^2I)(I - \Pi)^t = 0$$. By Theorem 4.4.3(c), $$\hat{\beta}$$ and $$Y - X\hat{\beta}$$ are independent, hence so are $$\hat{\beta}$$ and $$\hat{\sigma}^2$$.

(c) $$(I - \Pi)^2 = I - \Pi$$ and $$(I - \Pi)X = 0$$, so $$(n - p - 1)\hat{\sigma}^2/\sigma^2 = (Y - X\beta)^t(I - \Pi)(Y - X\beta)/\sigma^2$$, where $$(Y - X\beta)/\sigma \sim N_n(0, I)$$ and $$\mathrm{trace}(I - \Pi) = n - \mathrm{trace}((X^tX)^{-1}X^tX) = n - p - 1$$. By Theorem 4.4.5(b) it is $$\chi^2(n - p - 1)$$. $$\square$$

**Example 4.4.8 (Sampling distribution in simple linear regression).** From Examples 4.4.6 and 4.4.7 and Theorem 4.4.6,

$$
\hat{\beta} = \binom{\hat{\beta}_0}{\hat{\beta}_1} \sim N\Bigl(\binom{\beta_0}{\beta_1},\ \frac{\sigma^2}{S_{xx}}\begin{pmatrix}\sum x_{i1}^2/n & -\bar{x}_1 \\ -\bar{x}_1 & 1\end{pmatrix}\Bigr), \qquad (n - 2)\hat{\sigma}^2/\sigma^2 \sim \chi^2(n - 2),
$$

and $$\hat{\beta}$$ and $$\hat{\sigma}^2$$ are independent. Therefore, by the representational definition of the $$t$$-distribution, for a constant vector $$u$$, $$\dfrac{u^t\hat{\beta} - u^t\beta}{\hat{\sigma}\sqrt{u^t(X^tX)^{-1}u}} \sim t(n - 2)$$.

## References

- 김우철, *수리통계학* (Mathematical Statistics), revised 2nd edition, 민영사, 2021 — Chapter 4, §4.4 (Examples 4.4.1 to 4.4.8, Theorems 4.4.1 to 4.4.6). Translated from the book; not from my notes.
- Mathematical Statistics 1 (326.311), Seoul National University, Spring 2025. Instructor: Jaeyong Lee (이재용).

[Previous](/posts/mathstat1-order-statistics/) · [Overview](/posts/mathstat1-overview/) · [Chapter 4 Exercises](/posts/mathstat1-exercises-chapter-4/)
