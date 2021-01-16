"""
Ideas about fractional calculus defined on C^2
J^b f(x, a) = f(x, a + b)
"""

import numpy
from matplotlib import pyplot
from scipy import special

def monomial(x, a, x_0, a_0):
    return (x - x_0)**(a - a_0)/special.gamma(a - a_0 + 1)

def exp(x, a, b):
    return b**(-a)*numpy.exp(b*x)

def projx(f, x, a):
    n = numpy.searchsorted(numpy.real(a), 0.0)
    pyplot.plot(x, f[-n, :])
    pyplot.show()

def proja(f, x, a):
    n = numpy.searchsorted(numpy.real(x), 0.0)
    pyplot.plot(a, f[:, -n])
    pyplot.show()

def plotR(f, vmin=-10, vmax=10):
    _plot_C3(numpy.real(f), vmin=vmin, vmax=vmax)

def plotI(f, vmin=-10, vmax=10):
    _plot_C3(numpy.imag(f), vmin=vmin, vmax=vmax)

def plotM(f, vmax=10):
    _plot_C3(numpy.abs(f), vmax=vmax)

def plotMl(f):
    _plot_C3(numpy.log(numpy.abs(f)))

def _plot_C3(f, vmin=None, vmax=None):
    pyplot.imshow(f, extent = [x_0, x_1, a_0, a_1], vmin=vmin, vmax=vmax)
    pyplot.show()


x_0, x_1, Nx = -5, 5, 1000
a_0, a_1, Na = -5, 5,  1000
X = numpy.linspace(x_0, x_1, Nx, dtype=numpy.complex)
dx = (x_1 - x_0)/(Nx - 1)
da = (a_1 - a_0)/(Na - 1)
A = numpy.linspace(a_0, a_1, Na, dtype=numpy.complex)

domain_x, domain_a = numpy.meshgrid(X, A[::-1])

F = monomial(domain_x, domain_a, 0, -1)
G = monomial(domain_x, domain_a, 1, -1) + monomial(domain_x, domain_a, 1, 0)
G = -monomial(domain_x, domain_a, 1, -1) + 0.5*monomial(domain_x, domain_a, 0, -3)
G = (exp(domain_x, domain_a, 1.0j) + exp(domain_x, domain_a, -1.0j))/2.0
#G = (exp(domain_x, domain_a, 2.0j) - exp(domain_x, domain_a, -2.0j))/2.0
#G = F
Gp = numpy.gradient(G)
#G = Gp[1]

projx(G, X, A)
proja(G, X, A)
plotR(G)
plotI(G)
plotM(G)
plotMl(G)
