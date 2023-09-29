---
layout: page
title: "Working notes: Fractional Geometry"
math: true
---

The following is a summary of my recent notes on a project to define a version of differential geometry based on fractional calculus. Note that the project has extended beyond that original goal and is no longer directly related to fractional calculus. However fractional derivatives still play a roll in special cases and provide a connection to fractals and objects with fractional dimension.

# Motivation
In the generalize fractional calculus that I have been developing, see [here](/scv_fractional_calculus.pdf), the fundamental equations is $\partial_x f(x, a) = f(x, a + 1)$ ...

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

For an infinite dimensional linear operator $A$ with 1D null space acting on a suitable function space, then define the exponential to be,

$$e^{tA} = I + tA + \frac{t^2}{2!}A^2 + \frac{t^3}{3!}A^3 + \cdots$$

where $t$ is a real variable. Suppose this operator acts to "shift" functions in some space analogous to how

$$e^{t\frac{d}{dx}} f(x) = f(x) + tf'(x) + \frac{t^2}{2!}f''(x) + \cdots = f(x + t)$$

shifts analytic functions by $t$. If $e^{tA}$ taken in some sense to shift functions by $t$ in some space then the derivative in this space is,

$$\lim_{h \to 0} \frac{e^{hA} - I}{h} = \lim_{h \to 0} \frac{I - I + hA + \frac{h^2}{2!}A^2 + \cdots}{h} = \lim_{h \to 0} A + h(\frac{1}{2!}A^2 + \frac{h}{3!}A^3 + \cdots) = A$$

So if there exists some space where the shift operator is $e^{tA}$ then $A$ is the derivative on that space. Let us assume such a space exists and see how far this idea can go. Given a right inverse $A_0^{-1}$ such that $AA_0^{-1} = I$ and an element $\mathbb{I}$ from the null space of $A$, define the functions $\frac{x^n}{n!}=(A_0^{-1})^n\mathbb{I}$ which will form a basis for analytic functions on this space and are compatible with $A$ and $A_0^{-1}$. Then the function $\mathbb{I}$ is the analogue of the unit constant function and $A_0^{-1}$ is the analogue of $\int_0^x f(u)du$. An "analytic" function $f$ can be constructed as $f = \sum_{k=0}^\infty a_k \frac{x^k}{k!}$ with $\frac{x^0}{0!} = \mathbb{I}$.

Multiplication can now be defined as the bilinear operator $\times$ such that $x^n \times x^m = x^{n+m}$ so use the definition,

$$\frac{x^n}{n!} \times \frac{x^m}{m!} = \frac{(n + m)!}{n!m!}\frac{x^{n + m}}{(n + m)!} = \binom{n + m}{n}\frac{x^{n + m}}{(n + m)!}$$

So for functions $f = \sum a_k \frac{x^k}{k!}$ and $g = \sum b_k \frac{x^k}{k!}$, then the product of the functions is,

$$f \times g = \sum_{k=0}^\infty \frac{x^k}{k!} \left( \sum_{j = 0}^k \binom{k}{j}a_{k - j}b_j \right)$$

Note $\mathbb{I} = \frac{x^0}{0!}$ is the multiplicative identity.$x(\mathcal{x})$

## Points and Function Evaluation
