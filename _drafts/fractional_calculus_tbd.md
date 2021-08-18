---
layout: post
title: "Fractional Calculus TBD"
tags: [Math, Calculus, Fractional Calculus]
math: true
---

# Outline #
tinker with fractional calculus to try to understand why it is the way it is,
semigroup propertie inhereted from derivatives and integrals
multiple definitions inhereted from interpolation of points
we can then construct a unique invertable fractional derivate on a restriced subspace of functions

## motivation ##

## look for infinitly integrable and differentiable functions ##
### link bewteen invertability and functions vanishing at - infinity ###
### absolute integral of exponential bounds ###
### breakdown under summation, motivation for function spaces ###
### two parameter monotone exponential ###
### function space $\mathbb{S}$ ###
## calculus as a single invertable operator ##
## look at the action of a fractional derivative on the terms of a taylor series ##
### fractional calculus as interfpolation given group propertie ###
## RMT analytic interpolation ##
## RMT as fractional calculus equivelent to reimann luiville fractional integral ##
### being in $\mathbb{S}$ garenties the existance and nice properteies of RLFI ###
## multiple definitions of fractional calculus is equivelent to multiple analytic interpolations ##




Fractional calculus has two aspects that I find deeply unsatisfying: the multiple incompatible definitions and that composition of operator with itself forms a semigroup not an abelian group. In this paper I demonstrate a series of conditions under which a version of fractional calculus can be uniquely defined and forms an abelian group. First I will explicitly define which operator will be extended to a fractional version. It must reproduce differntiation and integration and also have the desired algebraic properties. Then I will use Ramanujan's Master Theorem (RMT) to define the extension of the operator, and investigate its properties.

Let the proposed fractional calculus operator $J^\alpha$ have the following properties: for $\alpha \in \mathbb{Z}$ it can reproduce repeated integration and differentiation, it is a linear operator, that $J^\alpha$ forms an abelian group when acting on some suitable subset of differentiable functions and it is analytic in the parameter $\alpha$. First let us identify a suitable operator to extend into a fractional calculus with nice algebra, and function space for which this operator is well behaved. Let the operator $J^k$ for $k \in \mathbb{Z}$ be,

\begin{equation}
J^k f(x) := \begin{cases} \frac{1}{(k-1)!}\int_{-\infty}^x (x - t)^{k - 1}f(t)dt & k \geq 1 \\ f(x) & k = 0 \\ \frac{d^{\left|k\right|}}{dx^{\left|k\right|}}f(x) & k \leq -1 \end{cases}
\label{integer_calculus}
\end{equation}

Using this operator a space of functions where the operator is well behaved is any function that is bounded by positive exponentials. Let us call this set $\mathbb{S}$,

\begin{equation}
\mathbb{S} := \left\lbrace f \in C^\omega(\mathbb{C}) \middle| (\forall n \in \mathbb{Z}^+)(\exists a_n \in \mathbb{M}, b_n \in \mathbb{R}), b_n > 0, \frac{d^n}{dx^n}f(x) \in \mathbb{B}(a_n, b_n) \right\rbrace
\label{exponentialy_bounded}
\end{equation}

Where the sets $\mathbb{M}$ and $\mathbb{B}$ are defined as follows,

\begin{equation\*}
\mathbb{M} := \left\lbrace a \in C(\mathbb{R}) \middle| (\forall x, y \in \mathbb{R}), x > y, a(x) > a(y) \geq 0 \right\rbrace
\end{equation\*}

\begin{equation\*}
\mathbb{B}(a, b) := \left\lbrace f \in C^\omega(\mathbb{C}) \middle| (\forall x, x_0 \in \mathbb{R}), x \leq x_0, |f(x)| \leq a(x_0)e^{bx} \right\rbrace
\end{equation\*}
Some properties of this operator and the space on which it acts is investigated in the appendix. Note that set $\mathbb{S}$ is a subset of $C^{\omega}(\mathbb{C})$, it is a vector space and if $f(x) \in \mathbb{S}$ then $J^k f(x) \in \mathbb{S}$. Also if $f(x) \in \mathbb{S}$ then $J^k J^m f(x) = J^{k + m} f(x)$, where $k, m \in \mathbb{Z}$.

## Fractional extension using RMT ##
Now that we have a suitable linear operator to extend, we need a procedure to actually extend the operator. We will use RMT for this purpose as given by G. H. Hardy \cite[p.~186]{hardy1940ramanujan}. Given a sequence $\phi(k)$, where $k \in \mathbb{Z}^+$, then

\begin{equation\*}
g(u) = \sum_{k=0}^\infty \frac{\phi(k)(-u)^k}{k!}
\end{equation\*}

If the series converges and its Mellin transform exists then the following result holds,

\begin{equation\*}
\int_0^{\infty} u^{s-1}g(u)du = \Gamma(s)\phi(-s)
\end{equation\*}

where $\phi(-s)$ is the analytic interpolation of the sequence $\phi(k)$ subject to some growth constraints \cite[p.~188--189]{hardy1940ramanujan}.
Using RMT fractional calculus can be defined in the following manner. For some function $f(x) \in \mathbb{S}$ consider the action of the operator $J^k$ at a point $x_0$. Every version of fractional calculus consists of producing an interpolation over some or all of this sequence. RMT can be used to find one such interpolation. Let us define $\phi(k)$ in terms of a function $f(x) \in \mathbb{S}$ ,

\begin{equation\*}
\phi(k) = \left(J^{-k}f\right)(x_0) = \left. \frac{d^k}{dx^k}f(x) \right|_{x = x_0}
\end{equation\*}

In this case $g(u)$ is,

\begin{equation\*}
g(u) = \sum_{k=0}^\infty \frac{(-u)^k}{k!} \left. \frac{d^k}{dx^k}f(x)\right|_{x=x_0}
\end{equation\*}

Note that $g(u)$ is the Taylor expansion of $f(x_0 - u)$ in terms of $u$. Now using $f(x_0 - u)$ in the Mellin transform,

\begin{equation\*}
\int_0^{\infty} u^{\alpha-1}f(x_0 - u)du = \Gamma(\alpha)\phi(-\alpha) = \left. \Gamma(\alpha)J^{\alpha}f(x)\right|_{x=x_0}
\end{equation\*}

Using the substitution $t = x_0 - u$, the integral becomes,

\begin{equation\*}
\int_{x_0}^{-\infty} -(x_0 - t)^{\alpha-1}f(t)dt = \left. \Gamma(\alpha)J^{\alpha}f(x) \right|_{x=x_0}
\end{equation\*}

Finally rearranging, and applying for arbitrary $x$,

\begin{equation\*}
J^{\alpha}f(x) = \frac{1}{\Gamma(\alpha)} \int_{-\infty}^{x} (x - t)^{\alpha-1} f(t)dt
\end{equation\*}

The operator $J^{\alpha}$ is only defined on the region $\mathfrak{R}(\alpha) \geq 1$, but since it is constructed by RMT it is analytic on this region. So the complete Operator must be defined in terms of the analytic continuation of the interpolation produced by RMT. In the case of this operator its domain can be extended by using integration by parts given $f(x) \in \mathbb{S}$,

\beign{equation\*}
J^{\alpha}\frac{d}{dx}f(x) = \frac{1}{\Gamma(\alpha)}\int_{-\infty}^x (x-t)^{\alpha-1} \left( \frac{d}{dt} f(t) \right)dt = \frac{\alpha-1}{\Gamma(\alpha)}\int_{-\infty}^x (x-t)^{\alpha-2}f(t)dt=\frac{1}{\Gamma(\alpha-1)}\int_{-\infty}^x (x-t)^{\alpha-2}f(t)dt = J^{\alpha-1}f(x)
\end{equation\*}

Using this repeatedly allows for $J^{\alpha}$ to be extended to the region $\mathfrak{R}(\alpha-n) \geq 1$ for $n \in \mathbb{Z}^+$,

\begin{equation}
J^{\alpha}\frac{d^n}{dx^n}f(x)=J^{\alpha-n}f(x)
\label{analytic_continuation}
\end{equation}

Therefore using RMT to interpolate between the derivatives of $f(x)$ yields an analytic function that interpolates between the derivatives and integrals. However, the operator $J^{\alpha}$ produced from RMT is not unique.

\begin{equation\*}
\psi(\alpha) \in C^{\omega}(\mathbb{C}), \psi(k) = 0, k \in \mathbb{Z}^-
\end{equation\*}

\begin{equation\*}
\left(J'^{\alpha}f\right)(x_0) = \left. J^{\alpha}f(x)\right|_{x=x_0} + \psi(\alpha)
\end{equation\*}

Evaluating the function at the points $k \in \mathbb{Z}^-$

\begin{equation\*}
\left(J'^{\alpha}f\right)(x_0) = \left(J^{\alpha}f\right)(x_0) + \psi(\alpha) = \left. J^{\alpha}f(x)\right|_{x=x_0}, k \in \mathbb{Z}^-
\end{equation\*}

This new function $\left( J'^{\alpha}f\right)(x_0)$ also satisfies the basic properties expected of fractional calculus. This demonstrates that using RMT to define a fractional calculus, produces many of the algebraic properties I am looking for, but it is not unique. In order to define a unique fractional calculus operator using RMT an additional constraint must be added. Let us denote an arbitrary compatible fractional calculus operator as $I^\alpha$. Define a new operator $R^\alpha$ as,

\begin{equation\*}
R^\alpha f(x) = I^\alpha f(x) - J^\alpha f(x)
\end{equation\*}

where $J^\alpha$ is the operator found using RMT. If we can prove that $R^\alpha = 0$ when some additional constraint is applied, then that constraint would force the operator $I^\alpha$ to be uniquely defined. To start apply the generalized Leibniz rule, given in \textit{Fractional Integrals and Derivatives} \cite[p.~280]{samko1993fractional}, to the operator $I^\alpha$,

\begin{equation\*}I^\alpha f(x)g(x) = \sum_{n=0}^\infty \binom{-\alpha}{n}\left( I^{\alpha + n}f(x) \right)\left( \frac{d^n}{dx^n} g(x)\right) = \sum_{n=0}^\infty \binom{-\alpha}{n}\left( \left(J^{\alpha + n} + R^{\alpha + n}\right)f(x) \right)\left( \frac{d^n}{dx^n} g(x)\right)
\end{equation\*}

Then subtracting $J^\alpha f(x)g(x)$ from both sides, 

\begin{equation}
I^\alpha f(x)g(x) - \sum_{n=0}^\infty \binom{-\alpha}{n}\left( J^{\alpha + n}f(x) \right)\left( \frac{d^n}{dx^n} g(x)\right) = R^\alpha f(x)g(x) = \sum_{n=0}^\infty \binom{-\alpha}{n}\left( R^{\alpha + n}f(x) \right)\left( \frac{d^n}{dx^n} g(x)\right)
\label{RemainderOperatorProductRule}
\end{equation}

Now that we are setup, look at the set of ODEs $\frac{d^n}{dx^n}f(x) = f(x)$. From this the following general statement can be made,

\begin{equation\*}
\exists f(x) \forall n \in \mathbb{Z}, \frac{d^n}{dx^n}f(x) = f(x), f(0) = 1
\end{equation\*}

given that negative integers in the index $n$ are interpreted as repeated integrals of the form $\int_{-\infty}^x f(t)dt$. This statement is true and admits only one solution $f(x) = e^x$. Let us generalize this statement to a fractional form,

\begin{equation}
\exists f(x) \forall \alpha \in \mathbb{C}, \frac{d^\alpha}{dx^\alpha}f(x) = f(x), f(0) = 1
\label{ConstaintOnFractionalCalculus}
\end{equation}

From statement \eqref{ConstaintOnFractionalCalculus} we can conclude that if $f(x)$ exists it must be $f(x) = e^x$, since it necessitates that $\frac{d}{dx}f(x) = f(x)$ and $f(0) = 1$. We will now require that statement \eqref{ConstaintOnFractionalCalculus} applies to fractional calculus. Using this condition $R^\alpha$ can be calculated in the case where $f(x) = e^x$. Using this constraint $I^\alpha e^x = e^x$, but since $J^\alpha e^x = e^x$ then $R^\alpha e^x = 0$. Now apply this result to \eqref{RemainderOperatorProductRule} with $f(x) = e^x$ and $g(x) = e^{-x}h(x)$ with $h(x) \in \mathbb{S}$.

\begin{equation\*}
R^\alpha h(x) = \sum_{n=0}^\infty \binom{-\alpha}{n}\left( R^{\alpha + n}e^x \right)\left( \frac{d^n}{dx^n} h(x)e^{-x}\right) = \sum_{n=0}^\infty \binom{-\alpha}{n} 0 \left( \frac{d^n}{dx^n} h(x)e^{-x}\right) = 0
\end{equation\*}

Given statement \eqref{ConstaintOnFractionalCalculus} is true, then $R^\alpha = 0$, so the operator $J^{\alpha}$ is the compatible fractional calculus operator. This operator still is only defined for $\mathfrak{\alpha} \geq 1$. Using the analytic continuation of the functions produced by RMT \eqref{analytic_continuation} a general form of the operator can be defined as,

\begin{equation}
J^{\alpha}f(x) = \frac{1}{\Gamma(\alpha+n)}\int_{-\infty}^x (x-t)^{\alpha+n-1}\left( \frac{d^n}{dt^n} f(t) \right)dt
\label{fractional_calculus}
\end{equation}

where $f \in \mathbb{S}$, $n \in \mathbb{Z}^+$, $\alpha \in \mathbb{C}$ and $\mathfrak{R}(\alpha + n) \geq 1$.

## Properties of $J^{\alpha}$ ##
Now that we have $J^{\alpha}$ uniquely defined we can check if it maintains the properties that were built into the operator $J^k$. Note that the operator \eqref{fractional_calculus} is a linear operator for all $\alpha \in \mathbb{C}$ and that for $\alpha \in \mathbb{Z}$ it is equivalent to the operator $J^k$. Given $f \in \mathbb{S}$, $\alpha \in \mathbb{C}$, $n \in \mathbb{Z}^+$ and $\mathfrak{R}(\alpha + n) \geq 1$ then using Libnitz's integral rule,

\begin{equation\*}
\frac{d}{dx} J^{\alpha} f(x) = \frac{d}{dx}\frac{1}{\Gamma(\alpha + n)}\int_{-\infty}^x (x-t)^{\alpha+n-1} \left( \frac{d^n}{dt^n} f(t) \right)dt = \frac{\alpha+n-1}{\Gamma(\alpha+n)}\int_{-\infty}^x (x-t)^{\alpha+n-2} \left( \frac{d^n}{dt^n} f(t) \right)dt = J^{\alpha-1}f(x)
\end{equation\*}

and using integration by parts,

\begin{equation\*}
J^{\alpha} \left( \frac{d}{dx} f(x) \right) = \frac{1}{\Gamma(\alpha+n)}\int_{-\infty}^x (x-t)^{\alpha+n-1} \left( \frac{d^{n+1}}{dt^{n+1}} f(t) \right)dt = -\frac{1-n-\alpha}{\Gamma(\alpha+n)}\int_{-\infty}^x (x-t)^{\alpha+n-2} \left( \frac{d^n}{dt^n} f(t) \right)dt = J^{\alpha-1}f(x)
\end{equation\*}

So the operator $J^\alpha$ and derivative commute, and applying this property repeatedly yields $\frac{d^m}{dx^m}J^{\alpha}f(x) = J^{\alpha-m}f(x) = J^{\alpha}\frac{d^m}{dx^m}f(x)$, where $m \in \mathbb{Z}^+$.

Given $f \in \mathbb{S}$, $\alpha, \beta \in \mathbb{C}$, $n,m \in \mathbb{Z}^+$, $\mathfrak{R}(\alpha + n) \geq 1$ and $\mathfrak{R}(\beta + m) \geq 1$ then,

\begin{equation\*}
J^{\alpha}J^{\beta} f(x) = \frac{1}{\Gamma(\alpha + n)}\int_{-\infty}^x (x-t)^{\alpha+n-1} \left( \frac{d^n}{dt^n} \frac{1}{\Gamma(\beta+m)}\int_{-\infty}^t (t-s)^{\beta+m-1} \left( \frac{d^m}{ds^m} f(s) \right)ds \right)dt
\end{equation\*}

Rearranging and using the fact that derivatives commute with $J^{\alpha}$,

\begin{equation\*}
J^{\alpha}J^{\beta} f(x) = \frac{d^{n+m}}{dx^{n+m}}\frac{1}{\Gamma(\alpha+n)\Gamma(\beta+m)}\int_{-\infty}^x \int_{-\infty}^t (x-t)^{\alpha+n-1}(t-s)^{\beta+m-1} f(s) ds dt
\end{equation\*}

Swapping the order of integration,

\begin{equation\*}
J^{\alpha}J^{\beta} f(x) = \frac{d^{n+m}}{dx^{n+m}}\frac{1}{\Gamma(\alpha+n)\Gamma(\beta+m)} \int_{-\infty}^x \int_{s}^x (x-t)^{\alpha+n-1}(t-s)^{\beta+m-1} f(s) dt ds
\end{equation\*}

Using a change of variables with $t=x-(x-s)r$ and rearranging yields,
\begin{equation\*}
J^{\alpha}J^{\beta} f(x) = \frac{d^{n+m}}{dx^{n+m}}\frac{1}{\Gamma(\alpha+n)\Gamma(\beta+m)} \int_{-\infty}^x (x-s)^{\alpha+\beta+n+m-1} f(s)ds \int_0^1 r^{\alpha+n-1}(1 - r)^{\beta+m-1}dr
\end{equation\*}

Identifying the beta integral ,$\int_0^1 r^{\alpha+n-1}(1-r)^{\beta+m-1}dr=\frac{\Gamma(\alpha+n)\Gamma(\beta+m)}{\Gamma(\alpha+\beta+n+m)}$, and then rearranging,

\begin{equation\*}
J^{\alpha}J^{\beta} f(x) = \frac{d^{n+m}}{dx^{n+m}}\frac{1}{\Gamma(\alpha+\beta+n+m)} \int_{-\infty}^x (x-s)^{\alpha+\beta+n+m-1} f(s)ds = \frac{d^{n+m}}{dx^{n+m}} J^{\alpha+\beta+n+m} f(x) = J^{\alpha + \beta} f(x)
\end{equation\*}

Relaxing constraints on $J^\alpha$ to allow Schwartz distributions enables us to reconstruct other standard fractional calculus definitions. Denote the Heaviside function as $H(x)$. The Riemann-Liouville fractional integral ${}_aI_x^\alpha$ can be defined as,

\begin{equation\*}
{}_aI_x^\alpha f(x) = \frac{1}{\Gamma(\alpha)}\int_a^x (x - t)^{\alpha - 1}f(t)dt = \frac{1}{\Gamma(\alpha)}\int_{-\infty}^x (x - t)^{\alpha - 1}H(t - a)f(t)dt = J^\alpha \left(H(x - a)f(x)\right)
\end{equation\*}

The Riemann-Liouville fractional derivative ${}_aD_x^\alpha f(x)$, where $n = \lceil \alpha \rceil$

\begin{equaiton\*}
{}_aD_x^\alpha f(x) = \frac{d^n}{dx^n} {}_aI_x^{n - \alpha} f(x) = \frac{d^n}{dx^n} J^{n - \alpha} \left(H(x - a)f(x)\right) = J^{-\alpha} \left(H(x - a)f(x)\right)
\end{equation\*}

The Caputo derivative ${}_a^C D_x^\alpha f(x)$ is,

\begin{equation\*}
{}_a^C D_x^\alpha f(x) = \frac{1}{\Gamma(n - \alpha)} \int_a^x (x - t)^{n - \alpha - 1} \left( \frac{d^n}{dt^n}f(t) \right) dt = J^{n - \alpha} \left(H(x - a)\frac{d^n}{dx^n}f(x)\right)
\end{equation\*}

So $J^\alpha$ is a commuting linear operator. With the property $J^{\alpha}J^{\beta} f(x) =J^{\alpha+\beta} f(x) =J^{\alpha}J^{\beta} f(x)$, where $\alpha,\beta \in \mathbb{C}$ and $f \in \mathbb{S}$. Also given Schwartz distributions are allowed, when $a = -\infty$ and $f(x) \in \mathbb{S}$ then, $J^\alpha f(x) = {}_{a}I_x^\alpha f(x) = {}_{a}D_x^{-\alpha} f(x) = {}_{a}^C D_x^{-\alpha} f(x)$.

## Conclusion ##
We have seen that RMT can be used to extend a calculus operator to a fractional version, and that the fractional calculus operator described is compatible with multiple definitions of fractional calculus operators given the constraints applied. Also this fractional calculus operator uniquely satisfies the conditions we imposed on fractional calculus when statement \eqref{ConstaintOnFractionalCalculus} is added as an additional constraint. And finally the operator can be generalized. If we modified the operator $J^k$ to use a different lower limit of integration and found a corresponding space of functions on which the operator is invertible then it should be possible to apply RMT to define a unique fractional calculus on that set of functions. So if the lower limit of integration was set to $\infty i$ the resulting operator should be a version of fractional calculus defined on a set that includes periodic functions.
