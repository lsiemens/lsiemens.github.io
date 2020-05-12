---
layout: post
title: "Fluid Mechanics from Particle Motion"
date: 2016-05-28
tags: [Physics, Classical-mechanics, Continuum-mechanics, Fluid-mechanics]
math: true
---

In January of 2016 I started taking my first class on fluid mechanics. In the first or second week of that class we started going over the derivation of the partial differential equations of fluid mechanics, but before covering the derivation we covered the concept of a fluid element. In essence for any given fluid the fluid element defines the smallest size scale for which the the equations of fluid mechanics still remain valid. A region of fluid satisfies the definition of a fluid element if it satisfies the following constraints. That the interactions of the particles within the element are sufficiently strong that the mean free path is small relative to the element's size and that the characteristic length scale of variations in the material properties is small relative to the element's size. That is the equations of fluid mechanics only apply at a given length scale if the statistical properties of the fluid are both well defined and smooth at that length scale.

The derivation given in class consisted of three parts. For each part we wrote a conservation law in integral form; we transformed the integral into partial differential form and used results form statistical mechanics and thermal dynamics to substitute in for the source terms in the equations. This procedure was applied to the conservation of mass, conservation of momentum and conservation of energy. If the fluid is assumed to be a Newtonian fluid, that is the stress-strain rate relationship is linear, then the stress tensor $\sigma_{ij}$ is defined in terms of the velocity gradient tensor $\partial_{x_i}u_j$. Assuming the fluid is isotropic and the stress tensor is symmetric then the stress tensor can be written as $\sigma_{ij}=-p\delta_{ij}+\mu\left(\partial_{x_i}u_j + \partial_{x_j}u_i\right)+\left(\mu_\nu-\frac{2}{3}\mu\right)\partial_{x_k}u_k\delta_{ij}$, where $p$ is the pressure, $\mu$ is the viscosity and $\mu_\nu$ is the bulk viscosity. When using this definition of the stress tensor the conservation of momentum equation is the Navier-Stokes equation. These equations can be written as, 

\begin{equation\*}\frac{D\rho}{Dt}=-\rho\partial_{x_i}u_i\end{equation\*}

\begin{equation\*}\rho\frac{Du_i}{Dt}=-\partial_{x_i}p+\rho g_i + \partial_{x_j}\left(\mu\left(\partial_{x_i}u_j + \partial_{x_j}u_i\right)+\left(\mu_\nu-\frac{2}{3}\mu\right)\partial_{x_k}u_k\delta_{ij}\right)\end{equation\*}

\begin{equation\*}\frac{De}{Dt}=-p\partial_{x_k}u_k+2\mu\left(\frac{1}{2}\left(\partial_{x_i}u_j + \partial_{x_j}u_i\right)-\frac{1}{3}\partial_{x_k}u_k\delta_{ij}\right)^2+\mu_\nu\left(\partial_{x_k}u_k\right)^2+\partial_{x_i}\left(k\partial_{x_i}T\right)\end{equation\*}

Where $\rho$ is the density, $\vec{u}$ is the bulk velocity, $\vec{g}$ is the gravitational acceleration, $e$ is the internal energy, $k$ is the coefficient of conductivity and $T$ is the temperature. Also the material derivative $\frac{D}{Dt}$ is defined as the differential operator $\frac{D}{Dt}=\left(\partial_t + \vec{u}\cdot\vec{\nabla}\right)$. These equations can be simplified by assuming that the fluid is incompressible. For an incompressible fluid $\partial_{x_i}u_i=0$. Also let us assume that $\mu$ and $k$ are constant. Then the equations simplify to the form,

\begin{equation\*}\frac{D\rho}{Dt}=0\end{equation\*}

\begin{equation\*}\rho\frac{Du_i}{Dt}=-\partial_{x_i}p+\rho g_i + \mu\partial_{x_j}\left(\partial_{x_i}u_j + \partial_{x_j}u_i\right)\end{equation\*}

\begin{equation\*}\frac{De}{Dt}=\frac{1}{2}\mu\left(\partial_{x_i}u_j + \partial_{x_j}u_i\right)^2+k\partial^2_{x_i}T\end{equation\*}

Alternatively if we assume the fluid is inviscid, the viscosity is zero, and that $k$ is constant. Then in this case the equations become,

\begin{equation\*}\frac{D\rho}{Dt}=-\rho\partial_{x_i}(u_i)\end{equation\*}

\begin{equation\*}\rho\frac{Du_i}{Dt}=-\partial_{x_i}p+\rho g_i\end{equation\*}

\begin{equation\*}\frac{De}{Dt}=-p\partial_{x_k}u_k+k\partial^2_{x_i}T\end{equation\*}

The derivation of these equations is relatively straight forward given the necessary relations and quantities from statistical mechanics and thermal dynamics are known.

# Derivation from Particle Motion #

Fluids consist of a large number of interacting particles, presumably the fluid mechanics observed at a macroscopic level is the result of the interactions occurring at a microscopic level. If the dynamics of each particle was known it should be possible in principle to determine the macroscopic dynamics of the fluid from the collective motion of the particles. At about one third of the way through my fluid mechanics class, having already gone over the derivation for the equations given above. I became interested in trying to derive fluid motion using particle motion directly. My goal was to see how much if any of fluid mechanics, I could derive from the fundamental motion of the individual particles.

## Dynamics in State-space ##

For this analysis I made the following assumptions that each particle, with a unique index $i$, has an identical mass $m$; that its current state is the combination of its position vector $\vec{x}\_i(t)$ and velocity vector $\vec{v}\_i(t)$; and that the acceleration of every particle is described by the potential $\phi(\vec{x}, t)$ such that its acceleration is $\frac{d}{dt}v_i\vert_t=-\vec{\nabla}\phi(\vec{x}, t)\vert_{\vec{x}_i(t)}=-\vec{\nabla}\phi_i(t)$. Given these three assumptions the equations of motion for each particle can be written as,

\begin{equation}\frac{d}{dt}\begin{pmatrix} \vec{x}_i \\\\ \vec{v}_i \end{pmatrix}=\begin{pmatrix} \vec{v}_i \\\\ -\vec{\nabla}\phi_i \end{pmatrix}\label{discrete_system_dynamics}\end{equation}

Moving over to a state space description of the system. State-space has six coordinates given by the orthogonal coordinate vectors $\vec{x}$ and $\vec{v}$. The state of a single particle with a given position and velocity corresponds to a point in state-space. The particle can be represented by the distribution $m\delta(\vec{x} - \vec{x}_i)\cdot\delta(\vec{v} - \vec{v}_i)$. Given this representation of a particle in state-space the volume integral $\int_V m\delta(\vec{x} - \vec{x}_i)\cdot\delta(\vec{v} - \vec{v}_i)d^3xd^3v$, evaluated over some arbitrary volume $V$, evaluates to zero if $V$ does not contain the particle and evaluates to $m$ if it does. Given this description of the individual particles a description of the entire system can be constructed. For a system of $n$ particles the entire system is described by the distribution,

\begin{equation\*}\sigma(\vec{x}, \vec{v}, t)=m\sum_{i=0}^n\delta(\vec{x} - \vec{x}_i)\cdot\delta(\vec{v} - \vec{v}_i)\end{equation\*}

From this definition of $\sigma$ the integral over some volume $V$, in state-space, $M(t)=\int_V \sigma(\vec{x}, \vec{v}, t)d^3xd^3v$ has the property that $M(t)$ is the total mass of all particles in the volume $V$ at time $t$. So $\sigma$ is the generalization of density to state-space. Since the dynamics of $\vec{x}_i$ and $\vec{v}_i$ are described by equation \eqref{discrete_system_dynamics}, then in principle the dynamics of $\sigma(\vec{x}, \vec{v}, t)$ can be determined.

Earlier we assumed that the acceleration of each particle was determined by some general  potential $\phi(\vec{x}, t)$. Now let us specify that that potential is in general dependent on the distribution of particles $\sigma$. Also let us simplify the relation by assuming that the velocity of the particles does not have an effect on the potential. Written explicitly the potential is $\phi(\vec{x}, \rho, t)$, where $\rho$ is the density distribution such that $\rho(\vec{x}, t)=\int_{-\infty}^\infty\sigma(\vec{x}, \vec{v}, t)d^3v$.

Since $\vec{x}$ and $\vec{v}$ are orthogonal if we define the point $\vec{X}$ in state-space as $\vec{X}=\left<\vec{x}, \vec{v}\right>$ and the vector $\vec{V}$ as $\vec{V}=\left<\vec{v}, -\vec{\nabla}\phi(\vec{x}, \rho, t)\right>$, then equation \eqref{discrete_system_dynamics} can be rewritten for a given particle at the point $\vec{X}$ as $\frac{d}{dt}\vec{X}=\vec{V}$. So for particles with motion defined by equation \eqref{discrete_system_dynamics} at some arbitrary point $\vec{X}$ in state-space the generalized state-space velocity of the particle is the vector $\vec{V}$.

For any given instant the point in state-space $\vec{X}$ corresponds to a definite state-space velocity $\vec{V}$, so it is possible to define a flow for the state-space that evolves with time and is dependent on the instantaneous density distribution $\rho$. If we assume that the total number of particles in all of state-space is constant and that both the particles in the state-space and the arbitrary state-space volume $V$ evolve according to the instantaneous flow of the state-space, then $\frac{d}{dt}M(t)=0$, where $M(t)\int_V \sigma(\vec{x}, \vec{v}, t)d^3xd^3v$ is the total mass of particles in the state-space volume $V$. However if only the particles evolve according to the instantaneous state-space while the arbitrary volume remains static, then due to the inability for particles to be created or destroyed the following statement of conservation is true,

\begin{equation\*}\int_V \partial_t \sigma(\vec{x}, \vec{v}, t)d^3xd^3v = -\int_{\partial V}\sigma(\vec{x}, \vec{v}, t)\vec{V}\cdot d\vec{A}\end{equation\*}

where $\partial V$ is the surface of the volume $V$ and $d\vec{A}$ is the surface elemet defined such that for a particle leaving the volume $V$ the factor $\vec{V}\cdot d\vec{A}$ is positive. Using the divergence theorem the integral terms can be collected to form the equation,

\begin{equation\*}\int_V \left(\partial_t \sigma(\vec{x}, \vec{v}, t) + \vec{\nabla}_{\vec{x}, \vec{v}}\cdot\left(\vec{V}\sigma(\vec{x}, \vec{v}, t)\right)\right)d^3xd^3v = 0\end{equation\*}

where $\vec{\nabla}_{\vec{x}, \vec{v}}\cdot \left<\vec{A}\_\vec{x}, \vec{A}\_\vec{v}\right>=\vec{\nabla}\_\vec{x}\cdot\vec{A}\_\vec{x} + \vec{\nabla}\_\vec{v}\cdot\vec{A}\_\vec{v}$ is the divergence in state-space of some state-space vector $\vec{A}$. Since the integral evaluates to zero for any arbitrary state-space volume $V$ then the integrand must be zero. This leads to the differential form of the conservation statement,

\begin{equation\*}\partial_t \sigma(\vec{x}, \vec{v}, t) + \vec{\nabla}_{\vec{x}, \vec{v}}\cdot\left(\vec{V}\sigma(\vec{x}, \vec{v}, t)\right) = 0\end{equation\*}

The term $\vec{\nabla}\_{\vec{x}, \vec{v}}\cdot\left(\vec{V}\sigma(\vec{x}, \vec{v}, t)\right)$ can be written explicitly using index notation as $v_i\partial_{x_i}\sigma - \left(\partial_{x_i}\phi\right)\partial_{v_i}\sigma$. So the conservation of the number of particles in state-space where the dynamics of the particles is described by equation \eqref{discrete_system_dynamics} leads to differential equation,

\begin{equation}\partial_t \sigma + v_i\partial_{x_i}\sigma - \left(\partial_{x_i}\phi\right)\partial_{v_i}\sigma = 0\label{state_space_continuity} \end{equation}

When I first derived this equation during spring break I recognized that it was far more general then necessary to describe only fluid motion. Any physical system of point like particles described by the general potential $\phi(\vec{x}, \rho, t)$ where the number of particles is conserved would described by equation \eqref{state_space_continuity}. In fact equation \eqref{state_space_continuity} would even describe continuous distributions as long as the state-space velocity was defined as $\vec{V}=\left<\vec{v}, -\vec{\nabla}\phi(\vec{x}, \rho, t)\right>$. However what I did not recognize until latter was that this equation is actually the Boltzmann Transport Equation. If you split the potential into two parts an external potential describing the acceleration due to external forces on the system and an internal potential representing the acceleration due to interactions within the system (collisions), then equation \eqref{state_space_continuity} can be rewritten as,

\begin{equation\*}\partial_t \sigma + v_i\partial_{x_i}\sigma + F_i\partial_{v_i}\sigma = \left(\partial_{t}\sigma\right)_\text{coll}\end{equation\*}

where $F_i$ is the external force on the distribution and $\left(\partial_{t}\sigma\right)_\text{coll}$ is the effect on the distribution due to collisions. This equation is the standard form of the Boltzmann Transport Equation.

Equation \eqref{state_space_continuity} is a general conservation equation which does describe atleast some simple models of fluids, but it cannot be directly compared to the standard equations of fluid mechanics. It must be transformed from an equation describing conservation in state-space to a set of three equations describing the conservation of mass, momentum and energy in position-space.

## Conservation of mass ##

Given the state-space density $\sigma(\vec{x}, \vec{v}, t)$ then as defined earlier the mass density is $\rho(\vec{x}, t)=\int_{-\infty}^\infty\sigma(\vec{x}, \vec{v}, t)d^3v$. In addition let us define the bulk velocity $\vec{u}$ as $u_i=\frac{1}{\rho(\vec{x}, t)}\int_{-\infty}^{\infty}v_i\sigma(\vec{x}, \vec{v}, t)d^3v$. The integral of equation \eqref{state_space_continuity} over velocity space is

\begin{equation\*}\int_{-\infty}^{\infty}\left(\partial_t \sigma + v_i\partial_{x_i}\sigma-\left(\partial_{x_i}\phi\right)\partial_{v_i}\sigma\right)d^3v=0\end{equation\*}

Evaluating the terms of this integral and applying the divergence theorem produces the equation, 

\begin{equation\*}\partial_t\rho + \partial_{x_i}\left(u_i\rho\right)-\left(\partial_{x_i}\phi\right)\oint{\sigma da_i}=0\end{equation\*}

where $da_i$ is the $i^{\text{th}}$ component of the surface element, and $\oint{\sigma da_i}$ is the surface integral over all of velocity space. Assuming $\sigma(\vec{x}, \vec{v}, t)$ drops to zero faster than $\lvert\vec{v}\rvert^{-2}$ then the surface integral converges to zero. Using this result the equation becomes,

\begin{equation}\partial_t\rho + \partial_{x_i}\left(u_i\rho\right)=0\label{conservation_of_mass}\end{equation}

So the integral of the equation \eqref{state_space_continuity} over all of velocity-space produces the conservation of mass equation.

## Conservation of momentum ##

Simply integrating over equation \eqref{state_space_continuity} produced the conservation of mass equation, in order to produce an equation for the conservation of momentum I multiplied equation \eqref{state_space_continuity} by $\vec{v}$ before integrating over velocity space.

\begin{equation\*}\int_{-\infty}^{\infty}v_i\left(\partial_t \sigma + v_j\partial_{x_j}\sigma-\left(\partial_{x_j}\phi\right)\partial_{v_j}\sigma\right)d^3v=0\end{equation\*}

After simplifying the equation, applying the product rule and divergence theorem it can be written in the form,

\begin{equation\*}\partial_t\left(u_i\rho\right) + \partial_{x_j}\left(\int_{-\infty}^{\infty}v_i v_j\sigma d^3v\right) - \left(\partial_{x_j}\phi\right)\oint v_i\sigma da_j + \rho\partial_{x_i}\phi=0\end{equation\*}

where $\oint v_i\sigma da_j$ is a surface integral over all of velocity-space. Assuming $\sigma(\vec{x}, \vec{v}, t)$ drops to zero faster than $\lvert\vec{v}\rvert^{-3}$ then the surface integral converges to zero. Then the integral can be written as,

\begin{equation}\partial_t\left(u_i\rho\right) + \partial_{x_j}\left(\int_{-\infty}^{\infty}v_i v_j\sigma d^3v\right) + \rho\partial_{x_i}\phi=0\label{incomplete_conservation_of_momentum}\end{equation}

Before continuing let us expand the tensor integral term $\int_{-\infty}^{\infty}v_i v_j\sigma d^3v$. It has a term of order $v^2$ so assuming when integrate it will produce the term $\rho u_i u_j$, it can be rewritten as, 

\begin{equation\*}\int_{-\infty}^{\infty}v_i v_j\sigma d^3v=\rho u_i u_j + \left(\int_{-\infty}^{\infty}v_i v_j\sigma d^3v - \rho u_i u_j\right)\end{equation\*}

If we define the scalar $p=\frac{1}{3}\left(\int_{-\infty}^{\infty}{v_i}^2\sigma d^3v - \rho {u_i}^2\right)$ then we can define the traceless tensor $B_{ij}=-\left(\int_{-\infty}^{\infty}v_i v_j\sigma d^3v - \rho u_i u_j\right) + p\delta_{ij}$. Given those two definitions the velocity tensor product integral can be written as,

\begin{equation\*}\int_{-\infty}^{\infty}v_i v_j\sigma d^3v=\rho u_i u_j + p\delta_{ij} - B_{ij}\end{equation\*}

Substituting this expanded integral back into equation \eqref{incomplete_conservation_of_momentum} and also substituting in the conservation of mass equation \eqref{conservation_of_mass} produces the conservation of momentum equation,

\begin{equation}\rho\left(\partial_t u_i + u_j\partial_{x_j}u_i\right) = -\partial_{x_i}p + \partial_{x_j}B_{ij} - \rho\partial_{x_i}\phi\label{conservation_of_momentum}\end{equation}

## Conservation of energy ##

The total energy density of the system is $E=\int_{-\infty}^{\infty}\left(\frac{1}{2}v_i^2 + \phi\right)\sigma d^3v$. Let us define $\vec{w} = \vec{v} - \vec{u}$, so then $v_i^2 = w_i^2 + 2v_i u_i + u_i^2$. An equation for the conservation of energy equation in position space can be derived by integrating the product of equation \eqref{state_space_continuity} and the factor $\frac{1}{2}v_i^2 + \phi$. To make the derivation of the conservation of energy simpler we can use the linearity of integration to break the conservation of energy equation into a kinetic energy component and a potential energy component.

### The kinetic energy component ###
Multiplying equation \eqref{state_space_continuity} by $\frac{1}{2}v_i^2$ then integrating over velocity space, the resulting equation is,

\begin{equation\*}\int_{-\infty}^{\infty}\frac{1}{2}v_i^2\left(\partial_t \sigma + v_j\partial_{x_j}\sigma-\left(\partial_{x_j}\phi\right)\partial_{v_j}\sigma\right)d^3v=0\end{equation\*}

After simplifying the equation, applying the product rule and divergence theorem, it can be written in the form

\begin{equation\*} \begin{split} & \partial_t\left(\int_{-\infty}^{\infty}\frac{1}{2}v_i^2\sigma d^3v\right) + \partial_{x_j}\left(\int_{-\infty}^{\infty}\frac{1}{2}v_i^2v_j\sigma d^3v\right) \\ & -  \left(\partial_{x_j}\phi\right)\left(\oint\left(\frac{1}{2}v_i^2\sigma\right)da_j - \int_{-\infty}^{\infty}\sigma v_j d^3v\right)=0 \end{split}\end{equation\*}

where $\oint\left(\frac{1}{2}v_i^2\sigma\right)da_j$ is a surface integral over all of velocity space. Assuming $\sigma(\vec{x}, \vec{v}, t)$ drops to zero faster than $\lvert\vec{v}\rvert^{-4}$ then the surface integral converges to zero. Expanding terms and using the result that $\int_{-\infty}^{\infty}v_i v_j\sigma d^3v=\rho u_i u_j + p\delta_{ij} - B_{ij}$ the equation can be written in the form,

\begin{equation} \begin{split} & \partial_t \left(\int_{-\infty}^{\infty}\frac{1}{2}w_i^2\sigma d^3v + \frac{1}{2}u_i^2\rho\right) + u_j\rho\partial_{x_j}\phi \\\\ & + \partial_{x_j}\left(\int_{-\infty}^{\infty}\frac{1}{2}w_i^2 v_j\sigma d^3v + \frac{1}{2}u_i^2 u_j\rho + p u_j - u_i B_{ij}\right)=0 \end{split} \label{incomplete_conservation_of_energy_kinetic} \end{equation}

### The potential energy component ###
Multiplying equation \eqref{state_space_continuity} by $\phi$ and then integrating over velocity space, but since $\phi$ is independent of $\vec{v}$ the equation evaluates to equation \eqref{conservation_of_mass} multiplied by $\phi$. Applying the product rule produces the form,

\begin{equation} \partial_t\left(\phi\rho\right) - \rho\partial_t\phi + \partial_{x_j}\left(u_j\rho\phi\right) - u_j\rho\partial_{x_j}\phi=0 \label{incomplete_conservation_of_energy_potential} \end{equation}

### Total energy density dynamics ###

The potential $\phi$ can be split into two components, the internal potential $\phi_{\text{in}}$ and a potential due to the external environment $\phi_{\text{ext}}$, such that $\phi = \phi_{\text{in}} + \phi_{\text{ext}}$. Let us define two energy densities, the internal energy density $e$ and the external energy density $\eta$, such that $e(\vec{x}, t)=\int_{-\infty}^{\infty}\left(\frac{1}{2}w_i^2 + \phi_{\text{in}}\right)\sigma d^3v$ and $\eta(\vec{x}, t)=\left(\frac{1}{2}u_i^2 + \phi_{\text{ext}}\right)\rho$. From these definitions the total energy density is then $E=e + \eta$, since the cross term $\int_{-\infty}^{\infty}w_i u_i\sigma d^3v=0$. Adding the two energy components from equation \eqref{incomplete_conservation_of_energy_kinetic} and equation \eqref{incomplete_conservation_of_energy_potential} produces the equation

\begin{equation\*}\begin{split} & \partial_t\left(\int_{-\infty}^{\infty}\frac{1}{2}w_i^2\sigma d^3v + \frac{1}{2}u_i^2\rho\right) + u_j\rho\partial_{x_j}\phi \\ & + \partial_{x_j}\left(\int_{-\infty}^{\infty}\frac{1}{2}w_i^2v_j\sigma d^3v + \frac{1}{2}u_i^2 u_j\rho + p u_j - u_i B_{ij}\right) \\ & + \partial_t\left(\phi\rho\right) - \rho\partial_t\phi + \partial_{x_j}\left(u_j\rho\phi\right) - u_j\rho\partial_{x_j}\phi=0 \end{split}\end{equation\*}

After expanding the potential into its two components, expanding the equation using the definition of $v_i$ and applying the definition internal energy density the equation can be put in the form,

\begin{equation\*}\begin{split} & \partial_t\left(e + \eta\right) + \partial_{x_j}\left(e u_j + \eta u_j\right) \\ & + \partial_{x_j}\left(\int_{-\infty}^{\infty}\frac{1}{2}w_i^2 w_j\sigma d^3v + p u_j - u_i B_{ij}\right) - \rho\partial_t\phi=0 \end{split}\end{equation\*}

Defining the vector $\vec{C}$ as $C_i = \int_{-\infty}^{\infty}\frac{1}{2}w_j^2 w_i\sigma d^3v$ and using it to simplify the equation results in the form

\begin{equation} \begin{split} & \partial_t\left(e + \eta\right) + \partial_{x_j}\left(e u_j + \eta u_j\right) \\ & + \partial_{x_j}\left(C_j + p u_j - u_i B_{ij}\right) - \rho \partial_t\phi=0 \end{split} \label{incomplete_conservation_of_energy} \end{equation}

Equation \eqref{incomplete_conservation_of_energy} describes the dynamics of the total energy density. Using equation \eqref{conservation_of_momentum} an equation for the external energy density can be derived. Which when combined with equation \eqref{incomplete_conservation_of_energy} will produce an equation for the internal energy density.

### External energy density dynamics ###
To generate an equation for the external energy density, let us multiply equation \eqref{conservation_of_momentum} by $u_i$, rearranging and applying the product rule, the equation becomes

\begin{equation\*}\begin{split} & \partial_t\left(\frac{1}{2}u_i^2\rho\right) - \frac{1}{2}u_i^2\partial_t\rho + \partial_{x_j}\left(\frac{1}{2}u_i^2\rho u_j\right) \\ & - \frac{1}{2}u_i^2\partial_{x_j}\left(\rho u_j\right) + u_i\left(\partial_{x_i}p - \partial_{x_j}B_{ij} + \rho\partial_{x_i}\phi\right)=0 \end{split}\end{equation\*}

Adding a potential energy component $\partial_t\left(\rho\phi_{\text{ext}} - \rho\phi_{\text{ext}}\right) + \partial_{x_j}\left(u_j\rho\phi_{\text{ext}} - u_j\rho\phi_{\text{ext}}\right)=0$, simplifying the equation and substituting in equation \eqref{conservation_of_mass} results in the equation,

\begin{equation} \partial_t\eta + \partial_{x_j}\left(\eta u_j\right) - \rho\partial_t\phi_{\text{ext}} + u_j\partial_{x_j}p - u_i \partial_{x_j}B_{ij} + u_j\rho\partial_{x_j}\phi_{\text{in}}=0 \label{incomplete_conservation_of_energy_external} \end{equation}

### Fluid mechanics energy equation: Internal energy equation ###
To remove the external energy density from equation \eqref{incomplete_conservation_of_energy} subtract equation \eqref{incomplete_conservation_of_energy_external} from it, resulting in the equation

\begin{equation\*}\begin{split} & \partial_t\left(e + \eta\right) + \partial_{x_j}\left(e u_j + \eta u_j\right) - \rho\partial_t\phi + \partial_{x_j}\left(C_j + p u_j - u_i B_{ij}\right) \\ & - \partial_t\eta - \partial_{x_j}\left(\eta u_j\right) + \rho\partial_t\phi_{\text{ext}} - u_j\partial_{x_j}p + u_i\partial_{x_j}B_{ij} - u_j\rho\partial_{x_j}\phi_{\text{in}}=0 \end{split}\end{equation\*}

After applying the product rule and simplifying produces the equation for the conservation of internal energy,

\begin{equation}\partial_t e + \partial_{x_i}\left(e u_i\right) = \rho\partial_t\phi_{\text{in}} + \rho u_i\partial_{x_i}\phi_{\text{in}} - \partial_{x_i}C_i - p\partial_{x_i}u_i + B_{ij}\partial_{x_j}u_i\label{conservation_of_energy} \end{equation}

## General Conservation Equations ##

The equation for the dynamics of a distribution in state-space was derived from particle motion and found to be equivalent to the Boltzmann Transport Equation,

\begin{equation\*}\partial_t \sigma + v_i\partial_{x_i}\sigma - \left(\partial_{x_i}\phi\right)\partial_{v_i}\sigma = 0\end{equation\*}

That equation was then used to derive equations for the conservation of mass, momentum and energy,

\begin{equation\*}\partial_t\rho + \partial_{x_i}\left(u_i\rho\right)=0\end{equation\*}

\begin{equation\*}\rho\left(\partial_t u_i + u_j\partial_{x_j}u_i\right) = -\partial_{x_i}p + \partial_{x_j}B_{ij} - \rho\partial_{x_i}\phi\end{equation\*}

\begin{equation\*}\partial_t E + \partial_{x_i}\left(E u_i\right) = - \partial_{x_j}\left(C_j + p u_j - u_i B_{ij}\right) + \rho \partial_t\phi\end{equation\*}

where the density $\rho$ is $\rho=\int_{-\infty}^{\infty}\sigma d^3v$, the bulk velocity $u_i$ is $u_i=\frac{1}{\rho}\int_{-\infty}^{\infty}v_i \sigma d^3v$, the scalar $p$ is $p=\frac{1}{3}\left(\int_{-\infty}^{\infty}{v_i}^2\sigma d^3v - \rho {u_i}^2\right)$, the traceless tensor $B_{ij}$ is $B_{ij}=-\left(\int_{-\infty}^{\infty}v_i v_j\sigma d^3v - \rho u_i u_j\right) + p\delta_{ij}$, the total energy density $E$ is $E=\int_{-\infty}^{\infty}\left(\frac{1}{2}v_i^2 + \phi\right)\sigma d^3v$, the velocity $w_i$ is $w_i=v_i-u_i$, the internal energy density $e$ is $e=\int_{-\infty}^{\infty}\left(\frac{1}{2}w_i^2 + \phi_{\text{in}}\right)\sigma d^3v$, the external energy density $\eta$ is $E=\left(\frac{1}{2}u_i^2 + \phi_{\text{ext}}\right)\rho$ and the vector $C_i$ is $C_i = \int_{-\infty}^{\infty}\frac{1}{2}w_j^2 w_i\sigma d^3v$. Since the total energy density is $E=e+\eta$, the energy equation can be split into the two equations,

\begin{equation\*}\partial_t\eta + \partial_{x_i}\left(\eta u_i\right) = \rho\partial_t\phi_{\text{ext}} - \rho u_i\partial_{x_i}\phi_{\text{in}} - u_j\partial_{x_j}p + u_i \partial_{x_j}B_{ij}\end{equation\*}

\begin{equation\*}\partial_t e + \partial_{x_i}\left(e u_i\right) = \rho\partial_t\phi_{\text{in}} + \rho u_i\partial_{x_i}\phi_{\text{in}} - \partial_{x_i}C_i - p\partial_{x_i}u_i + B_{ij}\partial_{x_j}u_i\end{equation\*}

Assuming the dynamics of some state-space density distribution is described equation \eqref{state_space_continuity}, then the set of conservation equations given above will describe the dynamics of the system. Unlike the standard equations of fluid mechanics the only constraints are that the state-space dynamics must be described by equation \eqref{state_space_continuity} and that the velocity distribution $\frac{\sigma(\vec{x}, \vec{v},t)}{\rho(\vec{x}, t)}$, at large velocities, must drop to zero faster than $\lvert\vec{v}\rvert^{-4}$.

# Simple Model: Gaussian Distribution #

Assuming that the state-space density is the product of a Gaussian velocity distribution and a density distribution, then the state-space density can be expressed as,

\begin{equation}\sigma(\vec{x}, \vec{v}) = \rho(\vec{x})\left(\pi a\right)^{-3/2} e^{-\left(v_i - u_i(\vec{x})\right)^2/a}\label{state-space}\end{equation}

where $a$ characterizes the width of the velocity distribution. Also to simplify the equation let us assume that the potential $\phi$ does not depend explicitly on time then it can be represented as $\phi=\phi(\vec{x}, \rho)$. First let us evaluate the first three moments of the state-space distribution in velocity space. The zeroth moment is $\int_{-\infty}^{\infty}\sigma d^3v=\rho$ and evaluates to the density by construction. The first moment is $\int_{-\infty}^{\infty}v_i\sigma d^3v=u_i \rho$ and it evaluates to the density again by construction. The second moment is $\int_{-\infty}^{\infty}v_i v_j \sigma d^3v=\rho u_i u_j + \rho \frac{a}{2}\delta_{ij}$. In addition the integral $\int_{-\infty}^{\infty}\frac{1}{2}w_j^2 w_i\sigma d^3v$ evaluates to $\int_{-\infty}^{\infty}\frac{1}{2}w_j^2 w_i\sigma d^3v=0$ due to the symmetry of the distribution.

Using these integrals we can evaluate the defined quantities $\rho$, $u_i$, $E$, $e$, $\eta$, $p$, $B_{ij}$ and $C_i$. The first two $\rho$ and $u_i$ are trivial since they were built into the state-space distribution by construction. The energy components evaluate to $E=\frac{1}{2}\rho u_i^2 + \frac{3}{4}\rho a + \rho \phi$, $e=\frac{3}{4}\rho a + \rho \phi_{\text{in}}$ and $\eta=\frac{1}{2}\rho u_i^2 + \rho \phi_{\text{ext}}$. Then the final quantities evaluate to $p=\rho \frac{a}{2}$, $B_{ij}=0$ and $C_i=0$.  So given the state-space density defined, the equations of fluid mechanics derived from equation \eqref{state_space_continuity} are,

\begin{equation\*}\partial_t\rho + \vec{\nabla}\cdot\left(\vec{u}\rho\right)=0\end{equation\*}

\begin{equation\*}\rho\left(\partial_t \vec{u} + \vec{u}\cdot\vec{\nabla}\vec{u}\right) = - \vec{\nabla} p - \rho\vec{\nabla}\phi\end{equation\*}

\begin{equation\*}\partial_t E + \vec{\nabla}\cdot\left(E \vec{u}\right) = - \vec{\nabla}\cdot\left(p \vec{u}\right)\end{equation\*}

If the energy $E$ is split into the internal and external components the energy equation produces,

\begin{equation\*}\partial_t\eta + \vec{\nabla}\cdot\left(\eta \vec{u}\right) = - \rho\vec{u}\cdot\vec{\nabla}\phi_{\text{in}} - \vec{u}\cdot\vec{\nabla}p\end{equation\*}

\begin{equation\*}\partial_te + \vec{\nabla}\cdot\left(e \vec{u}\right) = \rho\vec{u}\cdot\vec{\nabla}\phi_{\text{in}} - p\vec{\nabla}\cdot\vec{u}\end{equation\*}

So given the state-space density \eqref{state-space} the conservation equations reduce to the conservation equations for an inviscid fluid with zero thermal conductivity. These missing terms in the conservation equations are due to the symmetry of the state-space distribution. The assumption that the velocity distribution is always a Gaussian distribution means that for any infinitesimal region of fluid there exists a reference frame such the velocity distribution as viewed from that frame is spherically symmetric. So transport terms which rely on the inherent asymmetry of the state-space distribution must necessarily reduce to zero. This simple state-space distribution successfully reproduces a simple model of fluid dynamics but to reproduce the viscosity and thermal conductivity terms it will be necessarily to use a more general state-space distribution.
