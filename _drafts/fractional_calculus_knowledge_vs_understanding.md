---
layout: post
title: "Fractional Calculus: Knowlage vs Understanding"
tags: [Math, Calculus, Fractional Calculus]
math: true
---

calculational level: work with FC and its properties
abstract: you need knowlage as a foundation, and understanding to build
but how do you build understanding, I dont know so I tinkered.

# setup #
Introduce fractional calculus: sqrt of derivative, volume of 1.5 dimensional box
my problem: multiple definitions, semigroup propertie but I want a unique operator with index rule
I know my feeling about FC are wrong so maby go for understanding of why it wrong would be usefull

first lets be clear what we me by fractional derivative. definition of a fractional derivative ...

# index rule #
Understanding: differential calculus has semigroup plroperty so FC cannot do better.
circumvent knowlage: Restrict calculus to where it is invertable
Understanding: looking at taylor series makes it clear why differentiation is not invertable
circumvent knowlage: modify functions and differentiation such that calculus is invertable

# multiple definitions #
how to understand the multiple definitions of fractional calculus, it was not obvios to me
so maby a change of prespective would be useful. so how do you find a useful change of prespective
I dont know so I tinkered. like last time think about taylor series, and to make our lives simpler,
lets only consider analytic functions and assume the FD of an analytic function is analytic.
so FD is replacing taylor coefficients with functions $a_n(\alpha)$.
now if we assume the index rule then ... $a_n(\alpha) = a_0(\alpha + n)$
Understanding: So given that graphing the taylor coefficents as points each fractional derivative
corrispondes to a interpolation between those points. 
Knowlage: there are nessisaraly an infine number of differnt equially valid interpolations,
even in this restricted case there is not just a large number of differnt FD there must be an
infinite number of differnt incompatible fractional derivative operators.

but if we think about solving ODEs we expect to find infine numbers of solutions, so we must add
additional constraints to select one unique solution. simularily you might be able to find some
condition that is reasonable that FC must satisfy which uniquely selects one interpolation from
the infinite posible solutions.
