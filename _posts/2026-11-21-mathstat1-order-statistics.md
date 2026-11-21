---
title: "Mathematical Statistics 1: Ch. 4 Part 3 — Distribution of Order Statistics"
date: 2026-11-21 12:30:00 +0900
categories: [Study Notes, Mathematical Statistics 1]
tags: [order statistics, beta distribution, dirichlet, uniform, exponential, binomial tail]
description: The joint and marginal densities of order statistics, order statistics of the uniform distribution (beta and Dirichlet), the beta-integral form of the binomial tail, and the representation of the order statistics of an exponential sample. Chapter 4, notes section 3 of Mathematical Statistics 1.
math: true
mermaid: false
render_with_liquid: false
---

> My handwritten notes, translated into English. Chapter 4, notes section 3. It corresponds to §4.3 of the textbook. Statements and proofs follow my notes. Material taken from the textbook is collected at the end under "Supplement from the textbook". The exercises are in [Chapter 4 Exercises](/posts/mathstat1-exercises-chapter-4/).
{: .prompt-info }

## 3. Distribution of order statistics

### 3.1 Pdf of order statistics

> **Definition (Order statistic).** Let $$X_1, \dots, X_n$$ be random samples. Let $$X_{(r)}$$ be the $$r$$-th smallest sample from $$X_1, \dots, X_n$$ ($$1 \le r \le n$$). Then $$X_{(1)} \le X_{(2)} \le \cdots \le X_{(n)}$$ is the *ordered statistic*.
{: .definition #def-order-statistic }

> **Theorem (Properties of order statistics).** Let $$X_1, \dots, X_n \overset{iid}{\sim} f$$, where $$f$$ is the population pdf and $$F$$ is the population cdf. Also let $$Y = (Y_1, \dots, Y_n) = (X_{(1)}, \dots, X_{(n)})$$.
>
> 1. *Pdf of $$Y$$.* (For the discrete case it may not be defined exactly.)
>
>    $$
>    f_Y(y) = n!\prod_{i=1}^{n}f(y_i)\,I_{(y_1 < \cdots < y_n)}.
>    $$
> 2. *Pdf of $$Y_r = X_{(r)}$$.*
>
>    $$
>    f_{X_{(r)}}(x) = \frac{n!}{(r-1)!(n-r)!}f(x)\bigl(F(x)\bigr)^{r-1}\bigl(1 - F(x)\bigr)^{n-r}.
>    $$
> 3. *Pdf of $$(Y_r, Y_s) = (X_{(r)}, X_{(s)})$$* ($$r < s$$).
>
>    $$
>    f_{Y_r,Y_s}(x, y) = \frac{n!}{(r-1)!(s-r-1)!(n-s)!}\bigl(F(x)\bigr)^{r-1}\bigl(F(y) - F(x)\bigr)^{s-r-1}\bigl(1 - F(y)\bigr)^{n-s}f(x)f(y).
>    $$
{: .theorem #thm-order-statistics-pdf }

*Proof.* (1) Let $$y = (y_1, \dots, y_n) = (x_{(1)}, \dots, x_{(n)})$$. That is, for some permutation $$\pi$$ of $$[n] = \{t : t \in \mathbb{N},\ t \le n\}$$, $$y_i = x_{\pi(i)}$$. Then the Jacobian is

$$
\left\lvert\frac{\partial(y_1, \dots, y_n)}{\partial(x_1, \dots, x_n)}\right\rvert = \lvert\det(\text{permutation matrix})\rvert = 1.
$$

(The map $$x \mapsto y$$ is a many-to-one transformation: points $$x$$ that are permutations of each other go to the same $$y$$.) Therefore

$$
f(x)\,dx = \prod f(x_i)\,dx_1 \cdots dx_n = \sum_{\pi : [n]\text{'s all permutations}}\prod_{i=1}^{n}f(x_i)\,dx_1 \cdots dx_n\,I_{(x_{\pi(1)} < \cdots < x_{\pi(n)})}
$$

$$
= \sum_{\pi}\prod_{i=1}^{n}f(y_i)\,dy_1 \cdots dy_n\,I_{(y_1 < \cdots < y_n)} = n!\prod_{i=1}^{n}f(y_i)\,dy_1 \cdots dy_n\,I_{(y_1 < \cdots < y_n)}.
$$

cf) $$\displaystyle\int\prod f(x_i)I_{(x_{\pi(1)} < \cdots < x_{\pi(n)})}\,dx_1 \cdots dx_n = \int\prod f(y_i)I_{(y_1 < \cdots < y_n)}\,dy_1 \cdots dy_n$$.

(2) Integrate out the other coordinates:

$$
f_{X_{(r)}}(y_r) = \int n!\prod_{i=1}^{n}f(y_i)\,I_{(y_1 < \cdots < y_n)}\,dy_1 \cdots dy_{r-1}\,dy_{r+1} \cdots dy_n
$$

$$
= n!\,f(y_r)\int\prod_{i=1}^{r-1}f(y_i)\,I_{(y_1 < \cdots < y_{r-1} < y_r)}\,dy_1 \cdots dy_{r-1}\times\int\prod_{i=r+1}^{n}f(y_i)\,I_{(y_r < y_{r+1} < \cdots < y_n)}\,dy_{r+1} \cdots dy_n
$$

$$
= n!\,f(y_r)\,\frac{1}{(r-1)!}\int\prod_{i=1}^{r-1}f(y_i)\,I_{(y_1, \dots, y_{r-1} < y_r)}\,dy_1 \cdots dy_{r-1}\times\frac{1}{(n-r)!}\int\prod_{i=r+1}^{n}f(y_i)\,I_{(y_r < y_{r+1}, \dots, y_n)}\,dy_{r+1} \cdots dy_n
$$

$$
= \frac{n!}{(r-1)!(n-r)!}f(y_r)\bigl(F(y_r)\bigr)^{r-1}\bigl(1 - F(y_r)\bigr)^{n-r}.
$$

*Intuitive explanation.* Among the $$n$$ samples, $$r - 1$$ lie below $$x_{(r)}$$, $$1$$ is at $$x_{(r)}$$, and $$n - r$$ lie above. The number of ways to choose which is $$\dfrac{n!}{(r-1)!\,1!\,(n-r)!}$$. Since the samples are independent, the probability that $$r - 1$$ of them fall below is $$(F(x))^{r-1}$$, and that $$n - r$$ fall above is $$(1 - F(x))^{n-r}$$. $$\square$$

(3) is proved in the same way.

### 3.2 Order statistics of the uniform distribution

> **Theorem (Order statistics of the uniform distribution).** If $$X_1, \dots, X_n \overset{iid}{\sim} U(0, 1)$$, then the following hold.
>
> - (i) $$X_{(r)} \sim \mathrm{Beta}(r, n - r + 1)$$, $$r = 1, \dots, n$$.
> - (ii) $$Z = (X_{(1)}, X_{(2)} - X_{(1)}, \dots, X_{(n)} - X_{(n-1)}) \sim \mathrm{Dir}(1, \dots, 1)$$, with $$(n+1)$$ ones.
{: .theorem #thm-uniform-order-statistics }

*Proof.* (i)

$$
f_{X_{(r)}}(x) = \frac{n!}{(r-1)!(n-r)!}x^{r-1}(1 - x)^{n-r}I_{(0<x<1)} = \frac{\Gamma(n+1)}{\Gamma(r)\Gamma(n-r+1)}x^{r-1}(1 - x)^{(n-r+1)-1}.
$$

$$\therefore$$ $$X_{(r)} \sim \mathrm{Beta}(r, n - r + 1)$$.

(ii) $$Y = (Y_1, \dots, Y_n) = (X_{(1)}, \dots, X_{(n)})$$. Let

$$
Z = \begin{pmatrix}Z_1 \\ \vdots \\ Z_n\end{pmatrix} = \begin{pmatrix}Y_1 \\ Y_2 - Y_1 \\ \vdots \\ Y_n - Y_{n-1}\end{pmatrix}, \qquad\therefore\quad Y = \begin{pmatrix}Z_1 \\ Z_1 + Z_2 \\ Z_1 + Z_2 + Z_3 \\ \vdots\end{pmatrix}.
$$

$$\therefore$$ $$\Bigl\lvert\dfrac{dz}{dy}\Bigr\rvert = \det\begin{pmatrix}1 & 0 & \cdots \\ \vdots & \ddots & \\ & & \end{pmatrix} = 1$$. Then

$$
f(y)\,dy\,I_{(y_1 < \cdots < y_n)} = n!\,dy_1 \cdots dy_n\,I_{(0 < y_1 < y_2 < \cdots < y_n < 1)} = n!\,dz_1 \cdots dz_n\,I_{(0 < z_1 + \cdots + z_n < 1,\ z_i > 0\ \forall i)}
$$

$$
= \frac{\Gamma(n+1)}{\Gamma(1)\cdots\Gamma(1)}z_1^{1-1}z_2^{1-1}\cdots z_n^{1-1}(1 - z_1 - \cdots - z_n)^{1-1}\,dz_1 \cdots dz_n\,I_{(0 < z_1 + \cdots + z_n < 1,\ z_i > 0\ \forall i)} = \mathrm{Dir}(z \mid 1, \dots, 1)\quad((n+1)\text{ ones}). \qquad\square
$$

> **Theorem (Approximation of the binomial distribution using the beta distribution).** If $$X \sim \mathrm{Bin}(n, p)$$, then
>
> $$
> P(X \ge k) = \sum_{x=k}^{n}\binom{n}{x}p^x(1 - p)^{n-x} = \frac{\Gamma(n+1)}{\Gamma(k)\Gamma(n-k+1)}\int_0^px^{k-1}(1 - x)^{n-k}\,dx.
> $$
{: .theorem #thm-binomial-beta }

*Proof.* Let $$U_1, \dots, U_n \overset{iid}{\sim} U(0, 1)$$ and $$X = \sum_{i=1}^{n}I(U_i \le p) \sim \mathrm{Bin}(n, p)$$. Then $$X \ge k$$ exactly when at least $$k$$ of the $$U_i$$ are at most $$p$$, that is, when $$U_{(k)} \le p$$. $$\therefore$$

$$
P(X \ge k) = P(U_{(k)} \le p) = \int_0^p\mathrm{Beta}(x \mid k, n - k + 1)\,dx. \qquad\square
$$

### 3.3 Order statistics of the exponential distribution

> **Theorem (Order statistics of the exponential distribution).** Let $$X_1, \dots, X_n \overset{iid}{\sim} \mathrm{Exp}(1)$$.
>
> - (a) $$Z_1 = nX_{(1)}$$, $$Z_2 = (n-1)(X_{(2)} - X_{(1)})$$, $$\dots$$, $$Z_n = 1\cdot(X_{(n)} - X_{(n-1)})$$ are $$\overset{iid}{\sim} \mathrm{Exp}(1)$$.
> - (b) If $$Z_1, \dots, Z_n \overset{iid}{\sim} \mathrm{Exp}(1)$$, then
>
>   $$
>   \begin{pmatrix}X_{(1)} \\ \vdots \\ X_{(n)}\end{pmatrix} \overset{d}{=} \begin{pmatrix}\frac{1}{n}Z_1 \\ \frac{1}{n}Z_1 + \frac{1}{n-1}Z_2 \\ \vdots \\ \frac{1}{n}Z_1 + \cdots + \frac{1}{1}Z_n\end{pmatrix}.
>   $$
{: .theorem #thm-exponential-order-statistics }

**Example.** Let $$U_1, \dots, U_n \overset{iid}{\sim} U(0, 1)$$ and $$Y_1, \dots, Y_n \overset{iid}{\sim} \mathrm{Exp}(1)$$. Then

$$
\bigl(U_{(1)}, \dots, U_{(n)}\bigr) \overset{d}{=} \bigl(1 - e^{-Y_{(1)}}, \dots, 1 - e^{-Y_{(n)}}\bigr),
$$

as $$1 - e^{-Y} \sim U(0, 1)$$ when $$Y \sim \mathrm{Exp}(1)$$.

> **Theorem.** If $$X_1, \dots, X_n \overset{iid}{\sim} F$$, $$h(y) = F^{-1}(1 - e^{-y})$$, and $$Z_1, \dots, Z_n \overset{iid}{\sim} \mathrm{Exp}(1)$$, then
>
> $$
> \bigl(X_{(r)},\ 1 \le r \le n\bigr) \overset{d}{=} \Bigl(h\Bigl(\frac{1}{n}Z_1 + \cdots + \frac{1}{n-r+1}Z_r\Bigr),\ 1 \le r \le n\Bigr).
> $$
{: .theorem #thm-order-statistics-representation }

*Proof.* If $$U \sim U(0, 1)$$, then $$F^{-1}(U) \sim F$$. $$\square$$

## Supplement from the textbook

**Order statistics (§4.3).** The joint pdf of $$Y = (X_{(1)}, \dots, X_{(n)})^t$$ for a continuous population with pdf $$f(x)$$ is $$pdf_Y(y_1, \dots, y_n) = n!f(y_1)\cdots f(y_n)I_{(y_1 < \cdots < y_n)}$$ (Theorem 4.3.1). The proof uses Theorem 4.1.2: for each permutation $$\pi$$ of $$\{1, \dots, n\}$$ the restriction of the ordering map to $$\mathcal{X}_{\pi} = \{x : x_{\pi 1} < \cdots < x_{\pi n}\}$$ is one-to-one with Jacobian $$\pm 1$$, and there are $$n!$$ permutations.

**Example 4.3.1.** For a random sample of size $$3$$ from $$\mathrm{Exp}(1)$$, $$pdf_X(x_1, x_2, x_3) = e^{-(x_1+x_2+x_3)}I_{(x_1>0,x_2>0,x_3>0)}$$, and since there are $$3! = 6$$ permutations,

$$
pdf_Y(y_1, y_2, y_3) = \sum_{\pi}e^{-(y_{\pi^{-1}1} + y_{\pi^{-1}2} + y_{\pi^{-1}3})} = 6e^{-(y_1+y_2+y_3)}I_{(0<y_1<y_2<y_3)}.
$$

**Heuristic for Theorem 4.3.2(a).** For a small interval, $$P(x < X_{(r)} \le x + \lvert\Delta x\rvert) \approx c_r[P(X_1 \le x)]^{r-1}P(x < X_1 \le x + \lvert\Delta x\rvert)[P(X_1 > x + \lvert\Delta x\rvert)]^{n-r}$$, where $$c_r = \dfrac{n!}{(r-1)!\,1!\,(n-r)!}$$ is the number of ways to put $$r - 1$$, $$1$$ and $$n - r$$ of the $$n$$ sample members into the three intervals $$(-\infty, x]$$, $$(x, x + \lvert\Delta x\rvert]$$, $$(x + \lvert\Delta x\rvert, +\infty)$$. Hence $$pdf_{X_{(r)}}(x)\lvert\Delta x\rvert \approx c_r[F(x)]^{r-1}f(x)\lvert\Delta x\rvert[1 - F(x)]^{n-r}$$.

**Example 4.3.2.** For a random sample of size $$n$$ from $$U(0, 1)$$ (so $$f(x) = I_{(0,1)}(x)$$ and $$F(x) = x$$ on $$[0, 1]$$): (a) $$X_{(r)} \sim \mathrm{Beta}(r, n - r + 1)$$ with pdf $$\frac{n!}{(r-1)!(n-r)!}x^{r-1}(1 - x)^{n-r}I_{(0,1)}(x)$$; (b) $$Z = (X_{(1)}, X_{(2)} - X_{(1)}, \dots, X_{(n)} - X_{(n-1)})^t \sim \mathrm{Dirichlet}(1, \dots, 1)$$, with pdf $$\dfrac{\Gamma(n+1)}{\Gamma(1)\cdots\Gamma(1)}I_{(z_1>0,\dots,z_n>0,\ z_1+\cdots+z_n<1)}$$, because the map $$u$$ from $$\{0 < y_1 < \cdots < y_n < 1\}$$ onto $$\{z_i > 0,\ z_1 + \cdots + z_n < 1\}$$ is one-to-one with inverse Jacobian $$1$$, as in the proof above.

## References

- 김우철, *수리통계학* (Mathematical Statistics), revised 2nd edition, 민영사, 2021 — Chapter 4, §4.3 (Examples 4.3.1 and 4.3.2, Theorems 4.3.1 and 4.3.2). The supplement is translated from the book.
- Mathematical Statistics 1 (326.311), Seoul National University, Spring 2025. Instructor: Jaeyong Lee (이재용).

[Previous](/posts/mathstat1-t-f-distribution/) · [Overview](/posts/mathstat1-overview/) · [Next](/posts/mathstat1-multivariate-normal/)
