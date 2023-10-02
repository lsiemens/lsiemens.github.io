---
layout: page
title: "Working notes: Fractional Geometry"
math: true
---

The following is a summary of my recent notes on a project to define a version of differential geometry based on fractional calculus. Note that the project has extended beyond that original goal and is no longer directly related to fractional calculus. However fractional derivatives still play a roll in special cases and provide a connection to fractals and objects with fractional dimension.

## Preliminary Work
Starting in May of 2021 I spent a couple of months thinking through some conceptual problems around fractals under the assumption that geometry using fractional calculus would produce fractals that might at least be useful analogues. I came to the conclusion that it should be possible to consider dynamics in a fractal space. For appropriate fractals they would appear from within the space to be ordinary euclidean space. It also became apparent that the dimension in the sense of the Hausdorff dimension should be thought of in terms of the topological dimension, which is always an integer and accounts for the number of coordinates and the "scaling" dimension, which contains the fractional part and relates to how the system scales.

Following this I tried to develop a version of differential geometry using fractional calculus with "An Introduction To Riemannian Geometry" by Godinho and Natário as a guide. While I was able to develop a little more intuition about how this might work, the project failed. My final note from this approach suggests considering the Grünwald-Letnikov fractional derivative, defined as

$$\mathbb{D}^q f(x) = \lim_{h \to 0} \frac{1}{h^q} \sum_{m = 0}^{\infty} (-1)^m \binom{q}{m} f(x + h(q - m))$$

Then this can be simplified by defining a "finite difference" operator $\Delta_h^q$ as

$$\Delta_h^q f(x) = \sum_{m=0}^{\infty} (-1)^m \binom{q}{m} f(x + h(q - m))$$

and the norm $\|\|h\|\|$ as $\|\|h\|\| = h^q$. The result of these definitions is that

$$\mathbb{D}^q f(x) = \lim_{h \to 0} \frac{\Delta_h^q f(x)}{\|h\|}$$

If this difference operator and norm were natural definitions in some space, then the derivative would be the fractional derivative $\mathbb{D}^q$. So if a space could be constructed where the notion of a finite difference and the lengths of intervals is modified, then the limit definition of the derivative would be modified. Finally, if it is possible to construct differential geometry in that space, then it should in some sense use this modified derivative.


## Current Work
I will briefly mention the main ideas I am building from in the following paragraph, and then cover the notes for the case of $1$ topological dimension before moving on the the case of $n$ topological dimensions.

As noted with the Grünwald-Letnikov fractional derivative, if what it means to be a finite difference is modified, then it could lead to a change in the derivative. However, I started to think along slightly different lines. For analytic functions a shift operator can be defined in terms of the exponential of the derivative. What if, instead, we exponentiated a fractional derivative but still tried to interpret it as some kind of shift operator acting on a function space? Everything that follows comes from and expands on this idea.

## One Topological Dimension

### Setup and Shift Operators
For a fractional derivative $A$ define the exponential to be,

$$e^{A} = I + A + \frac{1}{2!}A^2 + \frac{1}{3!}A^3 + \cdots$$

where $I$ is the identity operator. Suppose this operator acts to "shift" functions in some space analogous to how

$$e^{\frac{d}{dx}} f(x) = f(x) + f'(x) + \frac{1}{2!}f''(x) + \cdots = f(x + 1)$$

shifts analytic functions by $1$. If $e^{tA}$ taken in some sense to shift functions by $t$ in some space then the derivative in this space is,

$$\lim_{h \to 0} \frac{e^{hA} - I}{h} = \lim_{h \to 0} \frac{I - I + hA + \frac{h^2}{2!}A^2 + \cdots}{h} = \lim_{h \to 0} A + h(\frac{1}{2!}A^2 + \frac{h}{3!}A^3 + \cdots) = A$$

So if there exists some space where the shift operator is $e^{tA}$ then the fractional derivative $A$ is the derivative on that space. Let's assume that such spaces exists and see how far this idea can go.

Up until this point I had been assuming that I would only be dealing with fractional derivatives. However, I realized that this relationship between the exponential of an operator and the derivative applies to more general operators than fractional derivatives. I also realized that the process used to generate fractional calculus, described in my [paper](scv_fractional_calculus.pdf), can be used to make fractional versions of operators in the same, more general, set of operators. So this geometry does not directly use fractional calculus, but for any geometry constructed using an operator $A$ there are related geometries built on fractional versions of the operator $A$.

To start with, let's setup the space in which the operators will act. Since we are working in $1D$ let's use $\mathbb{R}$ and by default I will use $\chi$ to mean a variable in this space. Finally, lets call this space the ambient space. I will call the space that is "shifted" by the exponential the generated space, and by default I will use $x$ to mean coordinates in this space. Note that all of the primary objects that we will work with will exist both in the ambient and generated spaces. For simplicity I will assume that everything is analytic and that all of the operators map analytic functions to analytic functions.

On the ambient space define an operator $A$ which is an infinite dimensional linear operator with one dimensional null space when acting on some specified functions space. We will also need an operator $A_0^{-1}$, which is a right inverse of $A$, and an element $\mathbb{I}$, of the null space of $A$, so that $AA_0^{-1}\mathbb{I}(\chi) = 0$. As noted above the linear operator $e^{tA}$ shifts functions in the generated space, and using this the derivative in the generated space would be the operator $A$. Define the functions $\frac{x^n}{n!}=(A_0^{-1})^n\mathbb{I}$ which will form a basis for analytic functions on the generated space and are compatible with $A$ and $A_0^{-1}$. Then the function $\mathbb{I}$ is the analogue of the unit constant function and $A_0^{-1}$ is the analogue of $\int_0^x f(u)du$. An "analytic" function $f$ can be constructed as $f = \sum_{k=0}^\infty a_k \frac{x^k}{k!}$ with $\frac{x^0}{0!} = \mathbb{I}$.

Multiplication can now be defined as the bilinear operator $\times$ such that $x^n \times x^m = x^{n+m}$, so we will use the definition,

$$\frac{x^n}{n!} \times \frac{x^m}{m!} = \frac{(n + m)!}{n!m!}\frac{x^{n + m}}{(n + m)!} = \binom{n + m}{n}\frac{x^{n + m}}{(n + m)!}$$

So for functions $f = \sum a_k \frac{x^k}{k!}$ and $g = \sum b_k \frac{x^k}{k!}$, the product of the functions is,

$$f \times g = \sum_{k=0}^\infty \frac{x^k}{k!} \left( \sum_{j = 0}^k \binom{k}{j}a_{k - j}b_j \right)$$

Note $\mathbb{I} = \frac{x^0}{0!}$ is the multiplicative identity.

### Points and Function Evaluation
For real functions the evaluation of a function at a point is a linear map from the space of functions to the real numbers. Given this operator, evaluation at other points can be achieved by composing this operator with the shift operator. So given evaluation at the "origin" $E_0$, evaluation at other points is $E_0 e^{tA}$. I would expect that evaluating the terms $\frac{x^n}{n!}$ at the "origin" give the results

$$E_0(\frac{x^n}{n!}) = \begin{cases}0 & \text{if } n > 0\\ 1 & \text{if } n = 0\end{cases}$$

To properly define evaluation I constructed the Taylor series of a Gaussian with unit area, taking this to be the Dirac delta "function" as the width goes to zero. Using this function, shifts and multiplication, an arbitrary function can be evaluated at the origin. In the end the definition I used was

$$E_0(f) = \lim_{\sigma \to 0^+}\left[e^{A/\sqrt{\sigma}} - e^{-A/\sqrt{\sigma}} \right]A_0^{-1}(G_\sigma \times f)$$

where $G_\sigma$ is the function

$$G_\sigma = \frac{1}{\sqrt{\sigma \pi}} \sum_{k=0}^\infty \frac{(-1/\sigma)^k(2k)!}{k!}\frac{x^{2k}}{(2k)!}$$

After computing the result of $E_0(\frac{x^n}{n!})$ explicitly using using this definition the result was

$$E_0(\frac{x^n}{n!}) = \begin{cases}0 & \text{if } n > 0\\ \mathbb{I} & \text{if } n = 0\end{cases}$$

The only difference from my initial guess is that the result is a multiple of the constant function rather than simply a real number. While it is straight forward to get a real number result it is convenient if function evaluation can be treated in the same way as the other linear operators. Now using this definition to evaluate the function $f = \sum a_k \frac{x^k}{k!}$ the result is

$$E_0(f) = \sum a_k E_0\left(\frac{x^k}{k!}\right) = a_0\mathbb{I}$$

Using the result that $E_0(e^{tA}\frac{x^n}{n!}) = \frac{t^n}{n!}$, it is possible to evaluate functions at other points, and the result is

$$E_0(e^{tA}f) = \sum a_k E_0\left( e^{tA} \frac{x^k}{k!} \right) = \sum a_k \frac{t^k}{k!} \mathbb{I} = f(t)\mathbb{I}$$

Later, I realized that there was a simpler but equivalent definition of $E_0$. Recall that $A\mathbb{I} = 0$ and $A_0^{-1}\frac{x^n}{n!} = \frac{x^{n + 1}}{(n + 1)!}$ so $AA_0^{-1}\frac{x^n}{n!} = A\frac{x^{n + 1}}{(n + 1)!} = \frac{x^n}{n!}$ but if $n > 0$ then $A_0^{-1}A\frac{x^n}{n!} = A_0^{-1}\frac{x^{n - 1}}{(n - 1)!} = \frac{x^n}{n!}$ otherwise if $n=0$ then $A_0^{-1}A\mathbb{I} = A_0^{-1}0 = 0$. So the commutator of $A$ and $A_0^{-1}$ applied to the basis functions is

$$\left[A,\ A_0{-1}\right]\frac{x^n}{n!} = \begin{cases}0 & \text{if } n > 0\\ \mathbb{I} & \text{if } n = 0\end{cases} = E_0(\frac{x^n}{n!})$$

So evaluating at the "origin" is $E_0 = \left[A,\ A_0^{-1}\right]$ and the location of the origin is determined by the selection of $A_0^{-1}$.

So far I have referred to "points" and the "origin" without defining them. I argue that a point is the operator that evaluates functions at the "point", so the point labelled $t$ is $E_t = E_0 e^{tA}$. Then given a coordinate function $f$ the coordinate representation of the point is the evaluation operator associated with that point applied to the coordinate function.

### Fractional Calculus and Fractional Dimension
While this project started as trying to incorporate fractional calculus into differential geometry it has expanded to include a much broader class of linear operators, however the operator $A$ can always be taken to be a fractional derivative. On the background Euclidean space use $\chi$ as the coordinate. Let $A = K^\gamma$ where $K^\gamma f(\chi) = \frac{1}{\Gamma(-\gamma)}\int_0^\chi f(t)(\chi - t)^{-\gamma - 1}dt$ and $A_0^{-1} = K^{-\gamma}$. Define the function $f_\beta(\chi, \alpha) = \frac{\chi^{\beta - \alpha}}{\Gamma(1 + \beta - \alpha)}$ and note that using the beta function $K^\gamma f_\beta(\chi, \alpha) = f_\beta(\chi, \alpha + \gamma)$. Taking the unit constant function to be $\mathbb{I} = f_{\gamma - 1}(\chi, 0) = \frac{\chi^{\gamma - 1}}{\Gamma(\gamma)}$, then the monomial terms are $\frac{x^n}{n!} = (A_0^{-1})^n\mathbb{I} = f_{\gamma - 1}(\chi, -n\gamma) = \frac{\chi^{\gamma(n + 1) - 1}}{\Gamma(\gamma(n + 1))}$, with $A\mathbb{I} = f_{\gamma - 1}(\chi, \gamma) = \frac{\chi^{-1}}{\Gamma(0)} = 0$.

Now let's consider a line segment between the points $E_0$ and $E_1$. While I am not at this point yet, let's assume that a metric and the other necessary structures can be defined, and that an Euclidean-like metric exists where the coordinate function is $x(\chi) = \frac{\chi^{2\gamma - 1}}{\Gamma(2\gamma)}$, and the distance between points $p$ and $q$ is $Len(p, q) = (E_q - E_p)x = (q - p)\mathbb{I}$. The length of the segment in question is $Len(0, 1) = \mathbb{I}$. Splitting this into $n$ smaller line segments of equal size, the small segments have points at $\frac{k}{n}$ with $k \in [0, n]$. The sum of the lengths of the small segments is $\sum_{k=1}^n(E_{\frac{k}{n}} - E_{\frac{k - 1}{n}})x = \sum_{k=1}^n(\frac{k}{n} - \frac{k - 1}{n})\mathbb{I} = \mathbb{I}$, so the length of the interval is not changed when splitting into multiple small intervals.

Now let's consider transformations of the underlying space. Let $\chi \to s\chi$, then applying this scaling of space to $\frac{x^n}{n!}$ gives

$$\frac{x^n}{n!}(s\chi) = \frac{(s\chi)^{\gamma(n + 1) - 1}}{\Gamma(\gamma(n + 1))} = s^{\gamma(n + 1) - 1}\frac{x^n}{n!}(\chi)$$

Applying this to a function $f(x(\chi)) = \sum_{k=0}^\infty a_k \frac{x^k}{k!}(\chi)$ then gives

$$f(x(s\chi)) = \sum_{k=0}^\infty a_k s^{\gamma(k + 1) - 1} \frac{x^k}{k!}(\chi) = s^{\gamma - 1}\sum_{k=0}^\infty a_k s^{\gamma k} \frac{x^k}{k!}(\chi) = s^{\gamma - 1}f(s^\gamma x(\chi))$$

Aside from the constant factor $s^{\gamma - 1}$ this looks like scaling the underlying space $\chi$ by $s$ is equivalent to scaling the generated space $x$ by $s^\gamma$ where $\gamma$ is the exponent of the fractional derivative. Note if $\gamma = 1$ (i.e. the generated space is not fractional) then the constant factor is $1$ and this just corresponds to scaling. So let's define scaling in a fractional space as the map $g(\chi) \to s^{1 - \gamma}g(s\chi)$ which is just ordinary scaling if the space is not fractional. Using this definition of scaling

$$f(x(\chi)) \to s^{1 - \gamma}f(x(s\chi)) = f(s^\gamma x(\chi))$$

So the length of an interval from $0$ to $p$ transforms under scaling the underlying space as $Len(0, p) \to s^{1 - \gamma}(E_p - E_0)x(s\chi) = s^{\gamma}Len(0, p)$ implying that the "dimension" is $d = \gamma$. In particular the topological dimension is $d = 1$ and the Hausdorff dimension is $d = \gamma$ with respect to the ambient space.

### Vectors and Dual Vectors
Although it is somewhat trivial, in $1D$ a vector field can be constructed as $f(x) \times A$ for some function $f(x)$. Then a vector at a point $p$ is $E_p(f(x) \times A) = \vec{v}$, acting the vector $\vec{v}$ on a function $g(x)$ gives $\vec{v}(g(x)) = E_p(f(x)) \times E_p(A g(x))$, that is $\vec{v} = f(p)E_p A$. For a vector space $V$, a dual vector $\vec{w}$ is an element of the space $V^*$ consisting of the linear maps of the form $\vec{w}:V \to \mathbb{R}$. There is a canonical map from functions to dual vectors such that for a function $g$ and a vector field $\vec{X} = f(x) \times A$, then the dual vector $dg$ is a dual vector field where

$$dg(\vec{X}) = \vec{X}(g(x)) = f(x) \times A g(x)$$

Applying any point $E_p$ to $dg$ gives a linear map from vectors at $p$ to $\mathbb{R}$ and so $dg$ is a dual vector field.

## N Topological Dimensions
Using an ambient space $\mathbb{R}^n$, with coordinates $\vec{\chi}$, define the operators $A_i$ and $A_{0i}^{-1}$ acting on functions in this ambient space. The set of operators $A_i$ should be a Lie algebra with respect to the commutator so that $[A_i, A_j] = A_i A_j - A_j A_i$ exists and the result is a linear combination of the operators $A_i$. Then there are structure coefficients $f_{ij}^k$ such that $[A_i, A_j] = f_{ij}^kA_k$. If the structure coefficients are all zero, the operators commute and shift operators will compose simply using the equation $e^{tA_i}e^{sA_j} = e^{tA_i + sA_j}$. If the operators $A_i$ do not commute then the Baker-Campbell-Hausdorff formula should describe how shift operators will compose. In that case I also expect similar complications to cause function multiplication to not commute.

### Product Space
To make the algebra simpler, going forward I will assume that the generated space is a product space of $n$ 1D generated spaces. In this case for all $i$ and $j$, $[A_i, A_j] = 0$ and $[A_{0i}^{-1}, A_{0j}^{-1}] = 0$, also if $i \neq j$ then $[A_i, A_{0j}^{-1}] = 0$ and finally the basis of the function space is the product of the basis of the individual function spaces for each dimension. So functions are defined as a multi-variable Taylor series. A function, $f$ for example, will be denoted using one of $f$, $f(\vec{\chi})$, $f(\vec{x})$ or $f(x_1, \cdots, x_n)$ where $x_i = A_{0i}^{-1} \mathbb{I}(\chi)$ and $\vec{x} = (x_1, \cdots, x_n)$. Note, $\mathbb{I}(\vec{\chi})$ is the product of the individual constant unit functions. Vector fields have the form $\vec{X} = f_i(\vec{x}) \times A_i$ for $n$ functions $f_i(\vec{x})$. The commutator of two vector fields $\vec{X} = f_i \times A_i$ and $\vec{Y} = g_i \times A_i$ is $[\vec{X}, \vec{Y}] = \left(f_i(A_i g_j) - g_i(A_i f_j)\right)A_j$ and is itself a vector field. However, note that this is not necessarily true if the space is not a product space.

### Flow of Vector Fields
Out of curiosity I tried computing $e^{t\vec{X}}$ for some simple vector fields and found that the result of these operators acting on functions was the flow of the function along the vector field. I was surprised to find that this seems to be true in general. This can be seen by the following argument. For a vector field $\vec{X}$ due to the product rule for two functions $f(\vec{x})$ and $g(\vec{x})$ the following holds

$$e^{\vec{X}}(f \times g) = \left( e^{\vec{X}}f \right) \times \left( e^{\vec{X}}g \right)$$

The implication is that since $e^{\vec{X}}$ is a linear operator it acts on functions term by term and since each term is the the product of the basis functions $x_i$, then the exponential can be pulled into each of the multiplicative terms. So for a term in a function being acted on by $e^{\vec{X}}$ then $e^{\vec{X}} \Pi_{k=1}^n (x_k)^{n_k} = \Pi_{k=1}^n (e^{\vec{X}}x_k)^{n_k}$ where $n_k \in [0, 1, 2, \cdots]$. So for a vector field $\vec{X}$ and function $f$ then

$$e^{t\vec{X}}f(x_1, \cdots, x_n) = f(e^{t\vec{X}}x_1, \cdots, e^{t\vec{X}}x_n)$$

and defining the functions $G_i(t, x_1, \cdots, x_n) = e^{t\vec{X}}x_i$ then $e^{t\vec{X}}f = f \circ \vec{G}$. The function $G_i$ is the coordinates for the flow of the vector field, for example, at $t = 0$ differentiating the previous equation leads to $\vec{X} = \left. \partial_t G_i(t, x_1, \cdots, x_n) \right\|_{t=0} A_i$.

### Solve Differential Equations
When searching to find other arguments and proofs that the exponential of a vector field can solve for the flow, I found an argument that finally convinced me that it works and that it applies more generally than just to linear differential operators. I was trying to see if this method would fail when using the limit definition of the exponential. Generalizing from the definition $e^x = \lim_{n \to \infty} \left(I + \frac{x}{n}\right)^n$, I tried the calculation $e^{t\vec{X}}f = \lim_{n \to \infty} \left( I + \frac{t\vec{X}}{n} \right)^nf$. Defining $\Delta t = \frac{t}{n}$ the equation then becomes

$$e^{t\vec{X}}f = lim_{n \to \infty} \left(I + \Delta t \vec{X} \right)^nf$$

It was straight forward to rewrite this as a recursive equation starting with $f_0 = f$, terminating with $e^{t\vec{X}}f = f_n$ and using $f_{k+1} = (I + \Delta t\vec{X})f_k = f_k + \Delta t \vec{X} f_k$ in the limit as $n \to \infty$.

So $e^{t\vec{X}}f$ can be identified as the solution found by Euler's method applied to the initial value problem associated with the vector field, where the function $f$ is the initial value. So for a system with a state denoted by $f(t)$ and an operator $A$ such that $A \circ f(t) = \partial_t f(t)$, then the initial value problem is solved by

$$e^{tA}f(0) = \lim_{n \to \infty} \left( I + \frac{t}{n}A \right)^n f(0)$$

where $\left( I + \frac{t}{n}A \right)^n$ denotes repeated composition. This should be applicable to essentially any problem solvable with Euler's method, even coupled and nonlinear systems. Note that if the system in question is linear then $\left( I + \frac{t}{n}A \right)^n$ can be expanded. Using this, if the operator $A$ is a linear operator then after some algebra it follows that

$$e^{tA} = \lim_{n \to \infty} \left( I + \frac{t}{n}A \right)^n = \sum_{k=0}^\infty \frac{(tA)^k}{k!}$$

In the case of a linear system the limit definition of the exponential, which can be related to Euler's method, is equivalent to the Taylor series definition of the exponential, although in this case it is applied to linear operators instead of matrices.
