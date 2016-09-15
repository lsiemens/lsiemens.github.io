---
layout: post
title: "Gaussian Moments"
tags: [Math, Calculus]
---

Let us define the $$m$$ dimensional the Gaussian distribution

\begin{equation}\sigma(\vec{x}, \vec{v}, t) = \rho(\vec{x}, t)\left(\pi a(\vec{x}, t)\right)^{-m/2} e^{-\left(v_i - u_i(\vec{x}, t)\right)^2/a(\vec{x}, t)}\label{m-gaussian}\end{equation}

The goal is to find a general equation for the moments of equation \eqref{m-gaussian}, that is solutions to equations of the form $$\int_{-\infty}^{\infty}v_i v_j\sigma d^m v$$ but generalized to any order. To simplify the equations in the following derivation I will first define some notation that will be used in the derivation.

The following derivation will deal with equations involving an arbitray number of vector components. Let $$A$$ be a rank $$n$$ tensor constructed from the $$m$$ dimensional vector $$\vec{a}$$ such that $$A_{i_1 i_2 \cdots i_{n-1} i_n} = a_{i_1} a_{i_2} \cdots a_{i_{n-1}} a_{i_n}$$. Let us simplify the notation by defining the object $$I$$ which represents the indices $$i_1$$ to $$i_n$$ such that $$a_{i_1} a_{i_2} \cdots a_{i_{n-1}} a_{i_n}=\left(a^n\right)_I$$, and let $$\left(a^{n-1}\right)_{I-1} a_{i_n} a_{i_{n+1}}=\left(a^n\right)_I a_{i_{n+1}}=\left(a^{n+1}\right)_{I+1}=a_{i_1} a_{i_2} \cdots a_{i_n} a_{i_{n+1}}$$.

Now to simplify the relation for $$C_I$$ we can expand our notation. Let $$A$$ be a rank $$n$$ tensor constructed from the $$m$$ dimensional vector $$\vec{a}$$ and the $$m$$ dimensional rank $$2$$ symmetric tensor $$b_{ij}$$ such that,

$$A_{i_1 i_2 \cdots i_{n-1} i_n} = b_{i_1 i_2} \cdots b_{i_{k-1} i_k} a_{i_{k+1}} a_{i_{k+2}}\cdots a_{i_{n-1}} a_{i_n}+\cdots+b_{i_1 i_n} \cdots b_{i_{k-1} i_k} a_{i_{k+1}} a_{i_{k+2}}\cdots a_{i_{n-2}} a_{i_{n-1}}$$

So $$A$$ is the tensor constructed to be the sum of the tensor $$b_{i_1 i_2} \cdots b_{i_{k-1} i_k} a_{i_{k+1}} a_{i_{k+2}}\cdots a_{i_{n-1}} a_{i_n}$$ and every unique permutation of its indices. Let us simplify the notation by defining the object $$I$$ which represents the indices $$i_1$$ to $$i_n$$ that $$A_I=\left[\delta^k a^{n-k}\right]_I$$.

Using this notation we can begin. As previously stated the goal is to find a general equation for the moments equation \eqref{m-gaussian}. Denoting the nth moments of the distribution by the tensor $$A_I$$, where $$\mathop{Len}(I)=n$$, the equation for the moments is,

$$A_I = \int_{-\infty}^{\infty}\left(v^n\right)_I \sigma d^m v$$

Make the argument that the tensorial form of the equation is independent of the dimension of the imbedding subspace $$m$$ because if the the indeces are constrained the result is seperable terms wich integrate to one.

## symetric moment ##
Before calculating the moments for the general Gaussian distribution \eqref{m-gaussian} let us calculate them for the distribution $$\pi^{-m/2} e^{-w_i^2}$$. The nth moments $$B_I$$ of this distribution are,

$$B_I = \pi^{-m/2}\int_{-\infty}^{\infty}\left(w^n\right)_I e^{-w_i^2} d^m w$$

where $$\mathop{Len}(I)=n$$. Now since the Gaussian integral $$\int_{-\infty}^{\infty}x^n e^{-x^2}dx$$ is,

$$\int_{-\infty}^{\infty}x^n e^{-x^2}dx=\sqrt{\frac{\pi}{2^n}}(n-1)!!\begin{cases}0, & \text{if $n$ is odd} \\ 1, & \text{if $n$ is even}\end{cases}$$

any term in $$B_I$$ with one or more pairings with an odd number indices will be zero. From this it is imediatly clear that if $$n$$ is odd then every term of $$B_I$$ will be zero. The simplest nonzero terms of $$B_I$$ is the terms where indices are paired and no two pairs of indices have the same value. Any term with repeated pairs or indeces can be constructed from a term with unique pairing by contracting with the kronecker delta. So the set terms with unique pairs of indices fully defines $$B_I$$. The term of $$B_I$$ produced from unique pairs of consecuitive indeces equals $$\sqrt{\pi}^{-m}\left(\frac{1}{2}\sqrt{\pi}\right)^{n/2}\sqrt{\pi}^{m-n/2}$$, it can be represented by the tensor $$C_I = 2^{-n/2}\left(\delta_{i_1 i_2}\cdots \delta_{i_{n-1} i_n}\right)$$. The tensor $$C_I$$ is the tensor representation of one term of $$B_I$$, but since there is no preferd ordering of indeces every term consisting of unique pairs of indices is one of the unique permutation of the indeces of $$C_I$$. So $$B_I=0$$ can be written as,

$$B_I = \sqrt{\pi}^{-m}\int_{-\infty}^{\infty}\left(w^n\right)_I e^{-w_i^2} d^m w=2^{-n}\left[\delta^{n/2}\right]_I\begin{cases}0, & \text{if $n$ is odd} \\ 1, & \text{if $n$ is even}\end{cases}$$

Now solving equation A_I. Let us define $$w_i=\left(v_i - u_i\right)/\sqrt{a}$$ and $$dv_i=\sqrt{a}dw_i$$, so $$v_i = \sqrt{a}w_i + u_i$$. Using this definition it is possible to expand $$A_I$$ using the definition of $$w_i$$, and letting the $$m=n$$. After expanding once $$A_I$$ can be written as,

$$A_I = \int_{-\infty}^{\infty}\left(v^n\right)_I \sigma d^n v=\left(\sqrt{\frac{a}{\pi}}\int_{-\infty}^{\infty}w_{i_n}e^{-w_{i_n}^2}dw_{i_n} + u_{i_n}\right)A_{I-1}$$

$$A_0 = \rho$$

www