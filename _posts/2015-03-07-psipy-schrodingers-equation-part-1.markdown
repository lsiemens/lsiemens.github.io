---
layout: post
title: "PsiPy: Schrodinger's Equation (part 1)"
date: 2015-03-07 12:00:00
tags: [Python, Quantum-mechanics, Schrodinger's-equation]

use_math: true
---

This past fall I was taking my second quantum mechanics class. In that class we learnt how to deal with discreet quantum system using linear algebra and how to extend that notation to solve continuous systems. Midway though the semester I attempted to write a simple program to solve the time dependent Schrodinger equation, it was a total failure. Shortly there after I found the blog post [Quantum Python: Animating the Schrodinger Equation](http://jakevdp.github.io/blog/2012/09/05/quantum-python/) by Jake Vanderplas. In this post he describes a method for solving time dependent Schroddinger equation based on fast Fourier transforms (FFT). After experimenting with different wave functions and potentials the script appeared to accurately reproduce solutions to the one dimensional time dependent Schroddinger equation for arbitrary potentials and initial wave functions.

Seeing the success of this method when applied to one dimensional problems I decided to apply the same algorithms to two dimensional problems. But before I apply these algorithms to two dimensional problems I will first check the validity of the one dimensional solutions by comparing them to known analytical solutions of simple potentials.

## The Equations: Numerical ##
Apart from switching to momentum-space from wavenumber-space the formulas and algorithms remain largely unchanged from the original post, for a full derivation and description of the main equations and algorithms please refer to the original post by Jake Vanderplas.

Since $p=\hbar k$ the difference between the equations used and the originals is only of the occasional factor of $\hbar$. The resulting equations of note are, Schrodinger's equations in position-space and momentum-space, $$i\hbar\frac{\partial\Psi}{\partial t}(x, t)=\frac{-\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2}(x, t)+V(x)\Psi (x, t)$$

$$i\hbar\frac{\partial\Phi}{\partial t}(p, t)=\frac{p^2}{2m}\Phi(x, t)+V(i\hbar\frac{\partial}{\partial p})\Phi (p, t)$$ where $\Psi(x, t)$ is the position space wave function and $\Phi(p, t)$ is the momentum space wave function. The relations between the FFT and the wave functions is, $$\Phi(p) e^{ix_0 m\Delta p/\hbar}=\tilde{F} (\frac{\Delta x}{\sqrt{2\pi\hbar}}\Psi (x) e^{-ix_n p_0/\hbar})$$

$$\frac{\Delta x}{\sqrt{2\pi\hbar}}\Psi(x) e^{-ix_n p_0/\hbar}=F(\Phi(p) e^{ix_0 m\Delta p/\hbar})$$ where $F()$ is the discrete Fourier transform and $\tilde{F}()$ is the inverse discrete Fourier transform. And finally the change in the wave function from the two forms of Schrodinger's equations when the partial derivatives in position and momentum are dropped, $$\Psi(x,t+\Delta t)\simeq\Psi(x,t)e^{-iV(x)\Delta t/\hbar}$$

$$\Phi(p,t+\Delta t)\simeq\Phi(p,t)e^{\frac{-ip^2\Delta t}{2m\hbar}}$$ These equation should approximate the time evolution of a wave function over a small non-zero time interval. When the two equations are applied in an alternating manner as described by Jake Vanderplas the result should approximate the time evolution of a wave function according to Schrodinger's equation.

## The Equations: Analytical ##
With the groundwork for the numerical solver laid out we must also consider the analytical solver. The analytical solver will use the known steady state solutions of solvable wave functions to produce the time evolving wave functions. When solving the time dependent Schrodinger's equation using the separation of variables method the following equation which relates the time depend wave function to the time independent wave functions is derived. $$\Psi(x, t)=\sum_n c_ne^{-iE_nt/\hbar}\Psi_n(x)$$

Where $\Psi_n(x)$ is the n-th time independent solution, $E_n$ is the energy level of that solution and $c_n$ is the amplitude of that wave function. So for wave functions which can be solved, the time dependent solution is simply a sum of the constituent wave functions according to the equation above.

The analytical Schrodinger solver will simply be pre-programmed with known time independent solutions to some analytically solvable potentials. Using this it is posible to produce the time evolving solution of wave functions constructed from a finite number of energy states, and it can produce n-th order approximations of arbitrary wave functions in solvable potentials.

## Implementation ##
To aid in the implementation and the future comparison of numerical results I have decided to use Hartree atomic units. In this system notably $\hbar = 1$, the electron mass $m_e=1$, the electron charge $e=1$ and the coulomb constant $\frac{1}{4\pi\epsilon_0}=1$.

The python source code for all of the scripts and modules for the numerical and analytical solvers are available at the GitHub repository [Iprocess-Projects: PsiPy](https://github.com/lsiemens/iprocess-projects/tree/master/psipy).
