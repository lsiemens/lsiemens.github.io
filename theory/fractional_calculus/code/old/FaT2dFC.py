from matplotlib import pyplot
from scipy import special
import numpy

def graph1d(X, Z, plot=True):
    pyplot.plot(X, numpy.real(Z))
    pyplot.plot(X, numpy.imag(Z))
    if plot:
        pyplot.show()

def graph2d(Z, vmin=-10, vmax=10):
    pyplot.imshow(numpy.real(Z), vmin=-10, vmax=10)
    pyplot.show()
    pyplot.imshow(numpy.imag(Z), vmin=-10, vmax=10)
    pyplot.show()
    pyplot.imshow(numpy.abs(Z), vmin=0, vmax=10)
    pyplot.show()
    pyplot.imshow(numpy.log(numpy.abs(Z)))
    pyplot.show()

def f(a):
#    return 100.0 + 0.0*a
#    return -1.0 + a - 0.5*a
#    return 1.0/(a - 0.001) + 2.0 + a - a**2
#    return numpy.cos(a)/special.gamma(a)
#    return special.gamma(a)
#    return special.gamma(a)/special.gamma(a - 4)
#    return numpy.exp(-a**2)
#    return special.erf(a)
#    return (a + 5)**(-1/2.0) + a**2
    return numpy.cos(a)**2 + numpy.sin(3*a)**4

Pa = numpy.linspace(-10, 10, 1000)
A = Pa
Px = numpy.linspace(-1, 1, 1000)
X = Px
dx = numpy.mean(X[1:] - X[:-1])
n = 100

graph1d(Pa, f(A))
pyplot.show()

def test(x, a, n):
    v = 0.0
    for i in range(n):
        v += f(a - i)*(x - 2)**i/special.gamma(i + 1)

    return v

for i in range(5):
    graph1d(Px, test(X, 0.5, n + i), plot=False)

#for i in range(30):
#    graph1d(Px, test(X, i/30, n), plot=False)
pyplot.show()

Xx, Xa = numpy.meshgrid(X, A[::-1])

y = test(Xx, Xa, n)
yp = numpy.gradient(y)[1]/dx
graph2d(y)
