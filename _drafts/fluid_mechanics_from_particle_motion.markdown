---
layout: post
title: "Fluid Mechanics from Particle Motion"
tags: [Physics, Classical-mechanics, Continuum-mechanics, Fluid-mechanics]
---

In January of 2016 I started taking my first class on fluid mechanics. In the first or second week of that class we started going over the derivation of the partial differental equations of fluid mechanics. Most resources that I have seen on the subject, including textbooks, online lecture notes and webpages, follow a simular derivation. First, the conservation of mass is stated in a general integral form, then it is transformed to a partial differental equation using some multivariable calculus identities. The equation can be stated in one of two forms, either the Eulerian form or the Lagrangian form of the equation. In the Eulerian form the coordinates index locations in space through which the fluid may flow. In this form the equation is, 

$$\partial_t\rho_\text{E}(\vec{x}, t)+\vec{\nabla}\cdot\left(\rho_\text{E}(\vec{x}, t)\vec{u}_\text{E}(\vec{x}, t)\right)=0$$

where $$\rho_{\text{E}}(\vec{x}, t)$$ is the mass density and $$\vec{u}_\text{E}(\vec{x}, t)$$ is the fluid velocity. In the Lagrangian form the coordinates index the fluid itself such that the equation describes the change in the fluid it self independent of it's location in space. In this form the equation is,

$$\frac{D\rho_\text{L}(\vec{x}_o, t)}{Dt}+\rho_{\text{L}}(\vec{x}_o, t)\vec{\nabla}\cdot\vec{u}_{\text{L}}(\vec{x}_o, t)=0$$

where $$\rho_{\text{L}}(\vec{x}_o, t)$$ is the mass density, $$\vec{u}_\text{L}(\vec{x}_o, t)$$ is the fluid velocity, $$\frac{D}{Dt}$$ is the material derivative and $$\vec{x}_o$$ is the time invariant coordinate of an element of the fluid. These two descriptions of fluid mechanics are equivalent given two definitions; that the material derivative is defined as $$\frac{D}{Dt}=\partial_t + \vec{u}\cdot\vec{\nabla}$$ and that at some time $t=t_o$ the equations $$\rho_{\text{E}}(\vec{x}, t_o)=\rho_{\text{L}}(\vec{x}_o, t_o)$$ and $$\vec{u}_{\text{E}}(\vec{x}, t_o)=\vec{u}_{\text{L}}(\vec{x}_o, t_o)$$ are true.
