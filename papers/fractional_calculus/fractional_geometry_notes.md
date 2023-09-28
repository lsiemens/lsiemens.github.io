---
layout: page
title: "Working notes: Fractional Geometry"
math: true
---

The following is a summary of my recent notes on a project to define a version of differential geometry based on fractional calculus. Note that the project has extended beyond that original goal and is no longer directly related to fractional calculus. However fractional derivatives still play a roll in special cases and provide a connection to fractals and objects with fractional dimension.

## Motivation
In the generalize fractional calculus that I have been developing, see [here](/scv_fractional_calculus.pdf), the fundamental equations is $\partial_x f(x, a) = f(x, a + 1)$ ...

## Preliminary Work
Starting in May of 2021 I spent a couple of months thinking through some conceptual problems around fractals under the assumption that geometry using fractional calculus would produce fractals of that they might at least be useful analogues. I cam to the conclusion that it should be possible to consider dynamics in a fractal space. For appropriate fractals they would appear from within the space to be ordinary euclidean space. Also it became apparent that the dimension in the sense of the Hausdorff dimension should be thought of in terms of the topological dimension, which is always an integer and accounts for the number of coordinates ..., and the "scaling" dimension, which contains the fractional part and relates to how the system scales.

Following this I began tying to develop a version of differential geometry using fractional calculus with "An Introduction To Riemannian Geometry" by Godinho and Natário as a guide. While I was able to develop a little more intuition about how this might work, the project failed. My final note from this approach suggests considering the Grünwald-Letnikov fractional derivative, defined as

$$\mathbb{D}^q f(x) = \lim_{h \rightarrow 0} \frac{1}{h^q} \sum_{m = 0}^{\infty} (-1)^m \binom{q}{m} f(x + h(q - m))$$

Then this can be simplified by defining a "finite difference" operator $\Delta_h^q$ as

$$\Delta_h^q f(x) = \sum_{m=0}^{\infty} (-1)^m \binom{q}{m} f(x + h(q - m))$$

and the norm $\|\|h\|\|$ as $\|\|h\|\| = h^q$. The result of these definitions is that

$$\mathbb{D}^q f(x) = \lim_{h \rightarrow 0} \frac{\Delta_h^q f(x)}{\|h\|}$$

If this difference operator and norm where natural definitions in some space, then the derivative would be the fractional derivative $\mathbb{D}^q$. So if a space could be constructed where the notion of a finite difference and the lengths of intervals is modified, then the limit definition of the derivative would be modified. Finally if it is possible to construct differential geometry in that space, then it should in some sense use this modified derivative.
