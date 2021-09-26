---
layout: post
title: "Invertible calculus"
tags: [Math, Calculus, Fractional-Calculus]
math: true
---

intro
Fractional calcolus did't know how to fix problems, so ty simplified slightly tangential problem in calculus
invertibility of the derivative - symbolic D S f /= S D f
another ay  analytic / taylor - symbolic derivative a_n -> a_{n - 1}
example - Code f as symbolic andd taylor def D def S. show and plot D S f and S D f for a particular f
note only iff a in S(f', a) is a == f(0) then S D f = D S f

stack functions
so what if the derivativ edid not lose infromation then it would be possible to inverte the operation in principle
why stacks (infine derivative, operer of operations, ...)
new calculus operations - symbolic D, S
information is moved Taylor <--> Stack so it is invertible - code D S f == S D f
invertable operator so it defines an abelian group under repeated composition

analytic functions
limiting to analytic functions, representation functions by taylor serist
apply to stack functions consider derivativs- symbolic ([a, a, a, ...], [b, b, b, ...]) -> ([a, a, ...], [a, b, b, b, ...])
combining the two list to one with positive and negative indices then functions can be represented by combining the lists
calculus operators on this representation shif the list left or right - symblic define Delta, then use that to define D, S

traditional definition of derivative
we have an operator we call the derivative but how does it compare to the ordinary limit definition of a derivative.
compute shifted function interms of taylor series, allways posible for small shifts of analytic functions - symbolic shift operation
apply the ordinary limit definition of derivatie to stack functions using shift operator - symbolic
notice that the limit definiiton of derivatives applied to stack functions reproduces our original definition of the derivative

Reproducing definite integrals
how to stack functions relate to calculus
define the conversion and projection functions - symbolic psi=:sequience->taylor polynomial pi=:projection setting negative indecies to zero
construc derivative and indegrals - symbolic def dx int interms of D and I
show equivelence to stack functions can be used to reproduce any definite intagral of that form

ODEs
is the extra data in stack functions always arbitrary is there anothery way to get to stack functinons
consdider homogenius linear ordinary differential equations with constant coeffishients
IVP solved by finding recursive solutions - code example
now igven a IVP f^(3)(0) = a, f^(4)(0) = b can also be solved by reversing the recursive equation - code example
this gives a solutions f(x) that solves IV and where Lf^(n) = 0
us reverse recursion to compute a^{-1} then y = int_0^x f(t)dt + a^{-1} this is the only antiderivative of f which solves Ly=0
taking a_n with ndegative indecies seariosly it can be thought of as finding the unique antiderivatives which satisfy Lf^(n)=0 for any n
this generalized sequence is exactly what you would find when solving Lf=0 where f is a stack function - symbolic solution
so HLODEs with constant coefficnents naruraly define stack functions as their solutions.
