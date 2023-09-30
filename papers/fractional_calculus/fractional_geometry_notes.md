---
layout: page
title: "Working notes: Fractional Geometry"
math: true
---

The following is a summary of my recent notes on a project to define a version of differential geometry based on fractional calculus. Note that the project has extended beyond that original goal and is no longer directly related to fractional calculus. However fractional derivatives still play a roll in special cases and provide a connection to fractals and objects with fractional dimension.

# Preliminary Work
Starting in May of 2021 I spent a couple of months thinking through some conceptual problems around fractals under the assumption that geometry using fractional calculus would produce fractals of that they might at least be useful analogues. I cam to the conclusion that it should be possible to consider dynamics in a fractal space. For appropriate fractals they would appear from within the space to be ordinary euclidean space. Also it became apparent that the dimension in the sense of the Hausdorff dimension should be thought of in terms of the topological dimension, which is always an integer and accounts for the number of coordinates ..., and the "scaling" dimension, which contains the fractional part and relates to how the system scales.

Following this I began tying to develop a version of differential geometry using fractional calculus with "An Introduction To Riemannian Geometry" by Godinho and Natário as a guide. While I was able to develop a little more intuition about how this might work, the project failed. My final note from this approach suggests considering the Grünwald-Letnikov fractional derivative, defined as

$$\mathbb{D}^q f(x) = \lim_{h \to 0} \frac{1}{h^q} \sum_{m = 0}^{\infty} (-1)^m \binom{q}{m} f(x + h(q - m))$$

Then this can be simplified by defining a "finite difference" operator $\Delta_h^q$ as

$$\Delta_h^q f(x) = \sum_{m=0}^{\infty} (-1)^m \binom{q}{m} f(x + h(q - m))$$

and the norm $\|\|h\|\|$ as $\|\|h\|\| = h^q$. The result of these definitions is that

$$\mathbb{D}^q f(x) = \lim_{h \to 0} \frac{\Delta_h^q f(x)}{\|h\|}$$

If this difference operator and norm where natural definitions in some space, then the derivative would be the fractional derivative $\mathbb{D}^q$. So if a space could be constructed where the notion of a finite difference and the lengths of intervals is modified, then the limit definition of the derivative would be modified. Finally if it is possible to construct differential geometry in that space, then it should in some sense use this modified derivative.


# Current work
I will briefly mention the main ideas I am building from and then cover the notes for the case of one topological dimension.

As noted with the Grünwald-Letnikov fractional derivative if the what it means to be a finite difference is modified, then could lead to a change in the derivative. However I started to think along slightly different lines. For analytic functions a shift operator can be defined in terms of the exponential of the derivative. What if instead we expatiated a fractional derivative but still tried to interpret it as some kind of shift operator acting on a function space. Everything that follows comes from and expands on this idea.

## Setup and Shift Operators
For a fractional derivative $A$ define the exponential to be,

$$e^{A} = I + A + \frac{1}{2!}A^2 + \frac{1}{3!}A^3 + \cdots$$

where $I$ is the identity operator. Suppose this operator acts to "shift" functions in some space analogous to how

$$e^{frac{d}{dx}} f(x) = f(x) + f'(x) + \frac{1}{2!}f''(x) + \cdots = f(x + 1)$$

shifts analytic functions by $1$. If $e^{tA}$ taken in some sense to shift functions by $t$ in some space then the derivative in this space is,

$$\lim_{h \to 0} \frac{e^{hA} - I}{h} = \lim_{h \to 0} \frac{I - I + hA + \frac{h^2}{2!}A^2 + \cdots}{h} = \lim_{h \to 0} A + h(\frac{1}{2!}A^2 + \frac{h}{3!}A^3 + \cdots) = A$$

So if there exists some space where the shift operator is $e^{tA}$ then the fractional derivative $A$ is the derivative on that space. let's assume that such spaces exists and see how far this idea can go.

Up until this point I had been assuming that I would only be dealing with fractional derivatives. However, I realized that this relationship between the exponential of an operator and the derivative applies to more general operators than fractional derivatives and at about the same time that the process used to generate fractional calculus, described in my [paper](scv_fractional_calculus.pdf), can be used to make fractional versions of operators in the same, more general, set of operators. So this geometry does not directly use fractional calculus, but for any geometry constructed using an operator $A$ there are related geometries built on fractional versions of the operator $A$.

To start with, let's setup the space in which the operators will act. Since we are working in $1D$ let's use $\mathbb{R}$ and by default I will use $\chi$ to mean a variable in this space. Finally lets call this space the ambient space. I will call the space that is "shifted" by the exponential the generated space and by default I will use $x$ to mean coordinates in this space. Note that all of the primary objects that we will work with will exist both in the ambient and generated spaces. For simplicity I will assume that everything is analytic and that all of the operators map analytic functions to analytic functions.

On the ambient space define an operator $A$ which is an infinite dimensional linear operator with one dimensional null space when acting on some specified functions space. Also we will need and operator $A_0^{-1}$, which is a right inverse of $A$, and an element $\mathbb{I}$, of the null space of $A$, so that $AA_0^{-1}\mathbb{I}(\chi) = 0$. As noted above the linear operator $e^{tA}$ shifts functions in the generated space and using this the derivative in the generated space would be the operator $A$. Define the functions $\frac{x^n}{n!}=(A_0^{-1})^n\mathbb{I}$ which will form a basis for analytic functions on the generated space and are compatible with $A$ and $A_0^{-1}$. Then the function $\mathbb{I}$ is the analogue of the unit constant function and $A_0^{-1}$ is the analogue of $\int_0^x f(u)du$. An "analytic" function $f$ can be constructed as $f = \sum_{k=0}^\infty a_k \frac{x^k}{k!}$ with $\frac{x^0}{0!} = \mathbb{I}$.

Multiplication can now be defined as the bilinear operator $\times$ such that $x^n \times x^m = x^{n+m}$ so we will use the definition,

$$\frac{x^n}{n!} \times \frac{x^m}{m!} = \frac{(n + m)!}{n!m!}\frac{x^{n + m}}{(n + m)!} = \binom{n + m}{n}\frac{x^{n + m}}{(n + m)!}$$

So for functions $f = \sum a_k \frac{x^k}{k!}$ and $g = \sum b_k \frac{x^k}{k!}$, the product of the functions is,

$$f \times g = \sum_{k=0}^\infty \frac{x^k}{k!} \left( \sum_{j = 0}^k \binom{k}{j}a_{k - j}b_j \right)$$

Note $\mathbb{I} = \frac{x^0}{0!}$ is the multiplicative identity.

## Points and Function Evaluation
For real functions the evaluation of a function at a point is a linear map from the space of functions to the real numbers. Given this operator, evaluation at other points can be achieved by composing this operator with the shift operator. So given evaluation at the "origin" $E_0$, evaluation at other points is $E_0 e^{tA}$. I would expect that evaluating the terms $\frac{x^n}{n!}$ at the "origin" give the results

$$E_0(\frac{x^n}{n!}) = \begin{cases}0 & \text{if } n > 0\\ 1 & \text{if } n = 0\end{cases}$$

To properly define evaluation I constructed the Taylor series of a Gaussian with unit area, taking this to be the Dirac delta "function" as the width goes to zero. Using this function, shifts and multiplication, an arbitrary function can be evaluated at the origin. In the end the definition I used was

$$E_0(f) = \lim_{\sigma \to 0^+}\left[e^{A/\sqrt{\sigma}} - e^{-A/\sqrt{\sigma}} \right]A_0^{-1}(G_\sigma \times f)$$

where $G_\sigma$ is the function

$$G_\sigma = \frac{1}{\sqrt{\sigma \pi}} \sum_{k=0}^\infty \frac{(-1/\sigma)^k(2k)!}{k!}\frac{x^{2k}}{(2k)!}$$

After computing the result of $E_0(\frac{x^n}{n!})$ explicitly using using this definition the result was

$$E_0(\frac{x^n}{n!}) = \begin{cases}0 & \text{if } n > 0\\ \mathbb{I} & \text{if } n = 0\end{cases}$$

The only difference from my initial guess is that result is a multiple of the constant function rather than simply a real number. While it is straight forward to get a real number result it is convenient if function evaluation can be treated in the same way as the other linear operators. Now using this definition to evaluate the function $f = \sum a_k \frac{x^k}{k!}$ the result is

$$E_0(f) = \sum a_k E_0\left(\frac{x^k}{k!}\right) = a_0\mathbb{I}$$

Using the result that $E_0(e^{tA}\frac{x^n}{n!}) = \frac{t^n}{n!}$, it is possible to evaluate functions at other points and the result is

$$E_0(e^{tA}f) = \sum a_k E_0\left( e^{tA} \frac{x^k}{k!} \right) = \sum a_k \frac{t^k}{k!} \mathbb{I} = f(t)\mathbb{I}$$

Later I realized that there was a simpler but equivalent definition of $E_0$. Recall that $A\mathbb{I} = 0$ and $A_0^{-1}\frac{x^n}{n!} = \frac{x^{n + 1}}{(n + 1)!}$ so $AA_0^{-1}\frac{x^n}{n!} = A\frac{x^{n + 1}}{(n + 1)!} = \frac{x^n}{n!}$ but if $n > 0$ then $A_0^{-1}A\frac{x^n}{n!} = A_0^{-1}\frac{x^{n - 1}}{(n - 1)!} = \frac{x^n}{n!}$ otherwise if $n=0$ then $A_0^{-1}A\mathbb{I} = A_0^{-1}0 = 0$. So the commutator of $A$ and $A_0^{-1}$ applied to the basis functions is

$$\left[A,\ A_0{-1}\right]\frac{x^n}{n!} = \begin{cases}0 & \text{if } n > 0\\ \mathbb{I} & \text{if } n = 0\end{cases} = E_0(\frac{x^n}{n!})$$

So evaluating at the "origin" is $E_0 = \left[A,\ A_0^{-1}\right]$ and the location of the origin is determined by the selection of $A_0^{-1}$.

So far I have referred to "points" and the "origin" with out defining them. I argue that a point is the operator that evaluates functions at the "point", so the point labelled $t$ is $E_t = E_0 e^{tA}$. Then given a coordinate function $f$ the coordinate representation of the point is the evaluation operator associated with that point applied to the coordinate function.

## Fractional Calculus and Fractional Dimension
While this project started as trying to incorporate fractional calculus into differential geometry it has expanded to include a much broader class of linear operators, however the operator $A$ can always be taken to be a fractional derivative. On the background Euclidean space use $\chi$ as the coordinate. Let $A = K^\gamma$ where $K^\gamma f(\chi) = \frac{1}{\Gamma(-\gamma)}\int_0^\chi f(t)(\chi - t)^{-\gamma - 1}dt$ and $A_0^{-1} = K^{-\gamma}$. Define the function $f_\beta(\chi, \alpha) = \frac{\chi^{\beta - \alpha}}{\Gamma(1 + \beta - \alpha)}$ and note that using the beta function $K^\gamma f_\beta(\chi, \alpha) = f_\beta(\chi, \alpha + \gamma)$. Taking the unit constant function to be $\mathbb{I} = f_{\gamma - 1}(\chi, 0) = \frac{\chi^{\gamma - 1}}{\Gamma(\gamma)}$, then the monomial terms are $\frac{x^n}{n!} = (A_0^{-1})^n\mathbb{I} = f_{\gamma - 1}(\chi, -n\gamma) = \frac{\chi^{\gamma(n + 1) - 1}}{\Gamma(\gamma(n + 1))}$, with $A\mathbb{I} = f_{\gamma - 1}(\chi, \gamma) = \frac{\chi^{-1}}{\Gamma(0)} = 0$.

Now let's consider a line segment between the points $E_0$ and $E_1$. While I am not at this point yes, let's assume that a metric and the other necessary structures can be defined and that an Euclidean like metric exists where the coordinate function is $x(\chi) = \frac{\chi^{2\gamma - 1}}{\Gamma(2\gamma)}$ and the distance between points $p$, $q$ is $Len(p, q) = (E_q - E_p)x = (q - p)\mathbb{I}$. The length of the segment in question is $Len(0, 1) = \mathbb{I}$. Splitting this into $n$ smaller line segments of equal size. The small segments have points at $\frac{k}{n}$ with $k \in [0, n]$. The sum of the lengths of the small segments is $\sum_{k=1}^n(E_{\frac{k}{n}} - E_{\frac{k - 1}{n}})x = \sum_{k=1}^n(\frac{k}{n} - \frac{k - 1}{n})\mathbb{I} = \mathbb{I}$, so the length of the interval is not changed when splitting into multiple small intervals.

Now let's consider transformations of the underlying space. Let $\chi \to s\chi$, then applying this scaling of space to $\frac{x^n}{n!}$ gives

$$\frac{x^n}{n!}(s\chi) = \frac{(s\chi)^{\gamma(n + 1) - 1}}{\Gamma(\gamma(n + 1))} = s^{\gamma(n + 1) - 1}\frac{x^n}{n!}(\chi)$$

Applying this to a function $f(x(\chi)) = \sum_{k=0}^\infty a_k \frac{x^k}{k!}(\chi)$ then gives

$$f(x(s\chi)) = \sum_{k=0}^\infty a_k s^{\gamma(k + 1) - 1} \frac{x^k}{k!}(\chi) = s^{\gamma - 1}\sum_{k=0}^\infty a_k s^{\gamma k} \frac{x^k}{k!}(\chi) = s^{\gamma - 1}f(s^\gamma x(\chi))$$

Aside from the constant factor $s^{\gamma - 1}$ this looks like scaling the underlying space $\chi$ by $s$ is equivalent to scaling the generated space $x$ by $s^\gamma$ where $\gamma$ is the exponent of the fractional derivative. Note if $\gamma = 1$ (i.e. the generated space is not fractional) then the constant factor is $1$ and this just corresponds to scaling. So let's define scaling in a fractional space as the map $g(\chi) \to s^{1 - \gamma}g(s\chi)$ which is just ordinary scaling if the space is not fractional. Using this definition of scaling

$$f(x(\chi)) \to s^{1 - \gamma}f(x(s\chi)) = f(s^\gamma x(\chi))$$

So the length of an interval from $0$ to $p$ transforms under scaling the underlying space as $Len(0, p) \to s^{1 - \gamma}(E_p - E_0)x(s\chi) = s^{\gamma}Len(0, p)$ implying that the "dimension" is $d = \gamma$. In particular the topological dimension is $d = 1$ and the Hausdorff dimension is $d = \gamma$ with respect to the ambient space.

## Vectors and Dual Vectors
Although it is somewhat trivial in $1D$ a vector field can be constructed as $f(x) \times A$, for some function $f(x)$, Then a vector at a point $p$ is $E_p(f(x) \times A) = \vec{v}$. Acting the vector $\vec{v}$ on a function $g(x)$ gives $\vec{v}(g(x)) = E_p(f(x)) \times E_p(A g(x))$, that is $\vec{v} = f(p)E_p A$. For a vector space $V$, a dual vector $\vec{w}$ is an element of the space $V^*$ consisting of the linear maps of the form $\vec{w}:V \to \mathbb{R}$. There is a canonical map from functions to dual vectors such that for a function $g$ and a vector field $\vec{X} = f(x) \times A$ then the dual vector $dg$ is a dual vector field where

$$dg(\vec{X}) = \vec{X}(g(x)) = f(x) \times A g(x)$$

Applying any point $E_p$ to $dg$ gives a linear map from vectors at $p$ to $\mathbb{R}$ and so $dg$ is a dual vector field.
