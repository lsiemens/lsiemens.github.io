---
layout: post
title: "Invertible calculus"
tags: [Math, Calculus, Fractional-Calculus]
math: true
---

transcription of audio

intro
Fractional calcolus did't know how to fix problems, so ty simplified slightly tangential problem in calculus
invertibility of the derivative - symbolic D S f /= S D f
another ay  analytic / taylor - symbolic derivative a_n -> a_{n - 1}
example - Code f as symbolic andd taylor def D def S. show and plot D S f and S D f for a particular f
note only iff a in S(f', a) is a == f(0) then S D f = D S f

Fractional calcolus did't know how to fix problems, so ty simplified slightly tangential problem in calculus. innvertibility of the derivative, if we look at the fundimental theorem of calculus along with leibniz integral theorem  - symbolic D S f /= S D f
from thaat you can see that the constants of integratoion in the prosses of antidifferentiation and likewise the bounds of integration are closely relatad to why derivatives are not invertible. howevere there is clearer way to look at it if we consider only complex analytic functions. they have the property that the taylor series of complex aanalytic function can allways be analyticaly continued to the full domain of the analytic function. so the local behaviour of the taylor series defines the behaviour of the full function. so we can complietly characterize an analytic function by the coefficients of the taylor series. - symbolic derivative a_n -> a_{n - 1} - Code f as symbolic andd taylor def D def S. show and plot D S f and S D f for a particular f
So the derivatve is not invertible becaus the information contained in the first term of the taylor series is lost during differentiation and it is impossible to compietly invert this prosess. 3:00




stack functions
so what if the derivativ edid not lose infromation then it would be possible to inverte the operation in principle
why stacks (infine derivative, operer of operations, ...)
new calculus operations - symbolic D, S
information is moved Taylor <--> Stack so it is invertible - code D S f == S D f
invertable operator so it defines an abelian group under repeated composition

so what if the derivative did not loose information, looking at the behaviour of derivative and integrals on the terms of the taylor series. differentiation removes the first element in the sequence of taylor coefficients, and antidifferention adds the constant of integration to the begining of the sequenc of coefficients. the loss of information makes the derivative not invertible but what if the information was not lost but maintained with the function. adding the nessisary information to invert the derivative each time one is taken and removing it when it is used to compute the corrisponding antiderivative. it would be possible to ingeneral invert the prosses of differentiation. so what should the structure of shuch an object be. it should be the function plus some a sequence of extra information. since we are discussing analytic functions which are infinitly differentiable and can be integrated infinitly so the extra information must be an finfinitly long sequence to contain all of the information of derivatives that have been taken and antiderivative that can be taken. also we need to consider the order that the information is interacted with, if you have a function and take a number of derivative and after words take an antiderivative, then the antiderivate should use the information added by the last derivative, so the information is accessed in a "last in first out" order, so the extra information is accessed by differentiation, and integration like a stack from computer science. so lets define a new function we will call a stack function that consists of a pair of complex analytic function and a infinte sequenc of numbers indexed from one to infinity. lets now define a derivative which acts on these stack functions, such that information is preserved - symbolic D, S
so under these definitions of differentiation and antidifferentiation, these operations move information from the taylor series of the function to the stack and vise versa for antidifferentiaion. and this simple movement of information is simply and uniqly invertible.  - code D S f == S D f
so this  this new derivative and antiderivative operator are invertible so if we consider repeated compisition of the derivative on stack functions it defines an abealian group. ~8:00


analytic functions
limiting to analytic functions, representation functions by taylor serist
apply to stack functions consider derivativs- symbolic ([a, a, a, ...], [b, b, b, ...]) -> ([a, a, ...], [a, b, b, b, ...])
combining the two list to one with positive and negative indices then functions can be represented by combining the lists
calculus operators on this representation shif the list left or right - symblic define Delta, then use that to define D, S

if we only coinsider stack functions constructed from analytic functions, then we can produce a new representation of stack functions where the function in a stack function is represented by the sequence of coefficients of its taylor sereies. so in this repesentation the stack function would be two sequences, the coefficeints of the taylor series and then the coefficients of the stack. now taking the derivation of a function using this representation what it does is removes the first element from the sequence of taylor coefficients and adds it to the begining of the stack. - symbolic ([a, a, a, ...], [b, b, b, ...]) -> ([a, a, ...], [a, b, b, b, ...])
so we can see taking derivatives and antiderivative just move the first element from the taylor coefficients to the stack and vise versa. so alternativly we could represent this function as a single sequence indexed from minus infinity to infinity, with the elements indexd from zero to infinity containing the taylor coefficients, the elements with negative index contain the elements of the stack with the absolute value of the index (reverse order from zero). taking the derivative of an object in this representation simply shifts all of the elements of the sequence to the left, and antidifferentiation moves them to the right. so calculus operators in this representation is equivelent to shifting the elements of this list (which doese not remove any information and is invertible)  - symblic de
fine Delta, then use that to define D, S 10:00



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
