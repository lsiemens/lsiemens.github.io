---
layout: post
title: "String Dynamics"
date: 2016-04-30 12:00:00
tags: [Physics, Classical-mechanics, Continuum-mechanics]
---

Since finishing my first class on classical mechanics I have been interested in deriving the equations of motion for strings. Before I begin it should be noted that I do not have formal training in continuum mechanics, so the methods and definitions that I use may be nonstandard.

## Definitions ##
First lets define the coordinates $\ell$ and $t$, where $\ell$ is a unitless coordinate in the range [0, 1] denoting the location of a point along the string and $t$ is the time coordinate. To parameterize the string we will use the functions $\eta(\ell, t)$ and $\theta(\ell, t)$. The function $\theta(\ell, t)$ denotes the angle of an infinitesimal line segment of the string. The function $\eta(\ell, t)$ denotes the length of an infinitesimal line segment. Given these definitions the total length of the string is

$$L(t)=\int_0^1\eta(\ell, t)d\ell$$

and the spatial coordinates of the points along the string are given by

\begin{equation}X(\ell, t) = \int_0^{\ell}\eta(\ell^{\prime}, t)sin(\theta(\ell^{\prime}, t))d\ell^{\prime}\label{def_x}\end{equation}

\begin{equation}Y(\ell, t) = \int_0^{\ell}\eta(\ell^{\prime}, t)cos(\theta(\ell^{\prime}, t))d\ell^{\prime}\label{def_y}\end{equation}

In addition lets define the constants $\eta_0$, $m$, $\vec{g}$ and $k$, where $\eta_0$ is the length of an infinitesimal line segment in the absence of tension, $m$ is the linear mass density defined such that the total mass is $M=\int_0^1md\ell$, $\vec{g}$ is the gravitational acceleration vector and $k$ is the elasticity defined such that the linear potential energy density is $\frac{1}{2}k(\eta(\ell, t) - \eta_0)^2$.

Before we can construct the Lagrangian we need to be able to determine the parameter $\eta(\ell, t)$ in terms of the coordinates $X$ and $Y$. Taking the partial derivative of equation \eqref{def_x} and equation \eqref{def_y} with respect to $\ell$ results in the equations $\partial_{\ell}X=\eta(\ell, t)sin(\theta(\ell, t))$ and $\partial_{\ell}Y = \eta(\ell, t)cos(\theta(\ell, t))$. Defining $\vec{x}$ as $\vec{x} = X(\ell, t)\hat{x} + Y(\ell, t)\hat{y}$, then $\partial_{\ell}\vec{x} \cdot \partial_{\ell}\vec{x} = (\partial_{\ell}X)^2 + (\partial_{\ell}Y)^2=\eta(\ell, t)^2$, which results in the definition $\eta(\ell, t) = \pm \|\partial_{\ell}\vec{x}\|$. There is an ambiguity in the parameterization of $X(\ell, t)$ and $Y(\ell, t)$ in terms of $\eta(\ell, t)$ and $\theta(\ell, t)$. Given some $X(\ell, t)$ and $Y(\ell, t)$ a sign change in $\eta$ with a $\pm\pi$ radian shift in $\theta$ at some point $\ell_0$ will have no effect on the functions $X(\ell, t)$ and $Y(\ell, t)$.  To resolve this $\eta$ is constrained to be positive such that $\eta(\ell, t) = \lvert\partial_{\ell}\vec{x}\rvert$. Now that we can unambiguously define $\eta(\ell, t)$, it is possible to write all of the energy components in terms of the coordinates of the individual elements of the string.

The string will have two energy components, the kinetic energy and potential energy. Using the definition of $\vec{x}$ given in the preceding paragraph these energy terms can be written as

$$ E_k = \int_0^{\ell}\frac{1}{2}m(\partial_{t}\vec{x})^2d\ell^{\prime} $$

$$ E_p = \int_0^{\ell}\left(m\vec{x}\cdot\vec{g}+\frac{1}{2}k(\left|\partial_{\ell^{\prime}}\vec{x}\right|-\eta_0)^2\right)d\ell^{\prime} $$

## Lagrangian Mechanics ##
The Lagrangian of the string is $\mathscr{L}=E_k-E_p=\int_0^{1}\mathcal{L}d\ell^{\prime}$, where $\mathcal{L}$ is the Lagrangian density $\mathcal{L}=\frac{1}{2}m(\partial_t\vec{x})^2 - \left(m\vec{x}\cdot\vec{g} + \frac{1}{2}k(\lvert\partial_{\ell}\vec{x}\rvert - \eta_0)^2\right)$. The action $\mathcal{S}$ is then given by the equation $\mathcal{S} = \int_0^t\int_0^1\mathcal{L(\vec{x}, \partial_t\vec{x}, \partial_{\ell^{\prime}}\vec{x})}dtd\ell^{\prime}$. Using the form of the Euler-Lagrange equation as used in classical field theory with the coordinates $t$ and $\ell$,

$$\partial_t\frac{\partial\mathcal{L}}{\partial(\partial_t \vec{x})} + \partial_{\ell}\frac{\partial\mathcal{L}}{\partial(\partial_{\ell} \vec{x})} - \frac{\partial\mathcal{L}}{\partial \vec{x}}=0$$

Substituting the Lagrangian density into the Euler-Lagrange equation,

$$\partial_t(m\partial_t\vec{x}) + \partial_{\ell}\left(-k(\lvert\partial_{\ell}\vec{x}\rvert-\eta_0)\frac{\partial_{\ell}\vec{x}}{\lvert\partial_{\ell}\vec{x}\rvert}\right) - (-m\vec{g}) = 0$$

Evaluating the partial derivatives produces the equation, 

$$m\partial_t^2\vec{x}-k\left(\partial_{\ell}^2\vec{x}-\eta_0\frac{\partial_{\ell}^2\vec{x}}{\lvert\partial_{\ell}\vec{x}\rvert}+\eta_0\frac{\partial_{\ell}\vec{x}(\partial_{\ell}\vec{x}\cdot\partial_{\ell}^2\vec{x})}{(\partial_{\ell}\vec{x})^2\lvert\partial_{\ell}\vec{x}\rvert}\right)+m\vec{g}=0$$

While this equation was derived in two dimensional space it is generalizable to three dimensions given that the equation $\eta(\ell, t)^2=(\partial_{\ell}\vec{x})^2$ remains valid given the definition $\vec{x} = X(\ell, t)\hat{x} + Y(\ell, t)\hat{y} + Z(\ell, t)\hat{z}$. So the equation of motion for a string in three dimensional space is given by, 

\begin{equation}\partial_t^2\vec{x} = \frac{k}{m}\left(\partial_{\ell}^2\vec{x}-\eta_0\frac{\partial_{\ell}^2\vec{x}}{\lvert\partial_{\ell}\vec{x}\rvert}+\eta_0\frac{\partial_{\ell}\vec{x}(\partial_{\ell}\vec{x}\cdot\partial_{\ell}^2\vec{x})}{(\partial_{\ell}\vec{x})^2\lvert\partial_{\ell}\vec{x}\rvert}\right)-\vec{g}\label{string}\end{equation}

This equation should describe the dynamics of a string with a uniform elasticity and density in a uniform gravitational field assuming a simple linear model of elasticity. The energy component due to the stiffness of the string was not added to this derivation since it would require spatial derivatives higher than first order.

## Simplifying Cases ##
In the next three sections we will investigate simplified cases and solutions of equation \eqref{string}.

#### Case 1: String Under Tension ####
The elastic potential energy is defined as $\frac{1}{2}k(\lvert\partial_{\ell}\vec{x}\rvert - \eta_0)^2$. Assuming the string is stretched such that $\frac{\eta_0}{\lvert\partial_{\ell}\vec{x}\rvert}\ll 1$ then equation \eqref{string} reduces to the equation,

$$\partial_t^2\vec{x} = \frac{k}{m}\partial_{\ell}^2\vec{x}-\vec{g}$$

The general solution to this equation is,

$$\vec{x}(\ell, t)=\vec{F}(\ell+vt)+\vec{G}(\ell-vt)-\frac{1}{2}\vec{g}t^2+\vec{a}_1(\ell^2+(vt)^2)+\vec{a}_2t\ell+\vec{a}_3\ell+\vec{a}_4t+\vec{a}_5$$

where $\vec{F}(x)$ and $\vec{G}(x)$ are both arbitrary functions, $v$ satisfies $v^2=\frac{k}{m}$ and where $\vec{a}\_1$, $\vec{a}\_2$, $\vec{a}\_3$, $\vec{a}\_4$ and $\vec{a}\_5$ are arbitrary constant vectors. The actual velocity of a wave in the string is $c(\ell)=v\lvert\partial_{\ell}\vec{x}\rvert$. From the standard derivation of the equations for a vibrating string the wave velocity is $c=\sqrt{\frac{T}{\mu}}$, where $T$ is the magnitude of the tension and $\mu$ is the linear mass density. In terms of the quantities defined in this derivation the tension $T$ is $T=k\lvert\partial_{\ell}\vec{x}\rvert$ and the linear mass density $\mu$ is $\mu=\frac{m}{\lvert\partial_{\ell}\vec{x}\rvert}$, which leads to the equation for the velocity $c=\sqrt{\frac{k\eta^2(\ell)}{m}}=v\eta(\ell)$. So the assumption that $\eta_0$ is small relative to $\eta(\ell)$ leads to the expected result, that the string under tension is described by a vector form of the one dimensional wave equation and that the velocity of waves depends on the local tension and linear density of the string.

#### Case 2: Near Vertical String ####
Given $\vec{g}=g\hat{z}$ the necessary assumptions for a near vertical string are that $\frac{\left|\partial_\ell X\right|}{\left|\partial_\ell Z\right|}\ll 1$ and $\frac{\left|\partial_\ell Y\right|}{\left|\partial_\ell Z\right|}\ll 1$. Using these assumptions equation \eqref{string} simplifies to the equation,

$$\partial_t^2\vec{x} = \frac{k}{m}\left(\partial_{\ell}^2\vec{x}-\eta_0\frac{\partial_{\ell}^2\vec{x}}{\lvert\partial_{\ell}Z\rvert}+\eta_0\frac{\partial_{\ell}\vec{x}\partial_{\ell}^2Z}{\partial_{\ell}Z\lvert\partial_{\ell}Z\rvert}\right)-g\hat{z}$$

This equation can be further simplified when written in expanded form,

$$\partial_t^2X = \frac{k}{m}\partial_{\ell}^2X\left(1-\frac{\eta_0}{\lvert\partial_{\ell}Z\rvert}\right)$$

$$\partial_t^2Y = \frac{k}{m}\partial_{\ell}^2Y\left(1-\frac{\eta_0}{\lvert\partial_{\ell}Z\rvert}\right)$$

$$\partial_t^2Z = \frac{k}{m}\partial_{\ell}^2Z-g$$

In this approximation the equation for the vertical component of the wave is just the one dimensional wave equation. The equations for the horizontal components are a modified wave equation which behaves in one way if the string is under tension and behaves differently if it is under compression. If the string is locally under tension $\lvert\partial_{\ell}Z\rvert\gt\eta_0$ then the horizontal components behave like a form of wave equations. If the string is locally under compression then the sign of the equation is flipped and rather than oscillatory behavior any perturbations from vertical grow exponentially.

#### Case 3: Inelastic String ####
For the case of an inelastic string assume that the elastic potential energy is small relative to the other sources of energy, that is $\frac{1}{2}k(\lvert\partial_{\ell}\vec{x}\rvert - \eta_0)^2\ll E_\text{total}$ and that the coefficient $k$ is large such that $\frac{1}{2}k\eta_0^2\gg E_\text{total}$. These assumptions lead to the condition that $\lvert\frac{\lvert\partial_{\ell}\vec{x}\rvert}{\eta_0}-1\rvert\ll 1$, given these assumptions equation \eqref{string} reduces to the equation,

$$\partial_t^2\vec{x} = \frac{k}{m}\frac{\partial_{\ell}\vec{x}(\partial_{\ell}\vec{x}\cdot\partial_{\ell}^2\vec{x})}{(\partial_{\ell}\vec{x})^2}-\vec{g}$$

In the case of a near vertical inelastic string the equations become,

$$\partial_t^2\vec{x} = \frac{k}{m}\frac{\partial_{\ell}\vec{x}\partial_{\ell}^2Z}{\partial_{\ell}Z}-g\hat{z}$$

When this equation is expanded it has the form,

$$\partial_t^2X = \frac{k}{m}\frac{\partial_{\ell}X\partial_{\ell}^2Z}{\partial_{\ell}Z}$$

$$\partial_t^2Y = \frac{k}{m}\frac{\partial_{\ell}Y\partial_{\ell}^2Z}{\partial_{\ell}Z}$$

$$\partial_t^2Z = \frac{k}{m}\partial_{\ell}^2Z - g$$

In this approximation again the equation for the vertical component assuming the string is nearly vertical is the one dimensional wave equation. In the horizontal components the equations will exhibit exponential growth or oscillatory behavior depending on the overall sign of $\frac{\partial_{\ell}^2Z}{\partial_{\ell}Z}$. 
