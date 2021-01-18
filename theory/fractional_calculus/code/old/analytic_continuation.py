"""
Failed attempt to compute analytic continuation numerically using truncated taylor series
"""

from matplotlib import pyplot
from scipy import special
import numpy

def gamma(x):
    return numpy.sqrt(2*numpy.pi/x)*numpy.power(x*numpy.sqrt(x*numpy.sinh(1/x) + 1/(810*x**6))/numpy.e, x)

#def gamma(x):
#    return numpy.sqrt(2*numpy.pi/x)*numpy.power(x/numpy.e, x)

class taylorSeries:
    def __init__(self, c_k, N, x_0=0.0):
        self.c_k = numpy.array(c_k, dtype=numpy.complex256)
        self.N = N
        self.x_0 = x_0

    def __call__(self, x):
        return self._evaluate(x)

    def derivative(self, x):
        return self._evaluate(x, 1)

    def test(self, x):
        for m in range(self.N):
            print("derivative: " + str(m))
            pyplot.plot(x, self._evaluate(x, m))
            pyplot.plot(x, numpy.abs(self._evaluate(x, m) - self._evaluate(x, m, 2)))
            pyplot.ylim(-10, 10)
            pyplot.show()

    def analytic_continuation(self, x_1, terms=None):
        if terms is None:
            terms = self.N

        if terms < 0:
            raise valueError("terms can not be a negative number.")
        if terms > self.N:
            raise valueError("terms can not be greater than the original series.")

        print("calculate analytic continuation at x = " + str(x_1))
        x_0 = x_1
        N = terms
        c_k = [self._evaluate(x_1, k) for k in range(N)]
        return taylorSeries(c_k, N, x_0 = x_1)

    def _evaluate(self, x, derivative=0, drop_terms=0):
        """
        Evaluate a taylor series or its derivative. when drop_terms is
        not zero then the first ((N - derivative) - drop_terms) terms
        of the series are evalutated.
        """
        if derivative < 0:
            raise valueError("Derivative order must be positive.")
        if drop_terms < 0:
            raise valueError("drop_terms can not be a negative number.")
        output = 0.0*x
        for k in range(self.N - derivative - drop_terms):
            output += self.c_k[k + derivative]*(x - self.x_0)**k/gamma(numpy.complex256(k) + 1)
        return output

def taylor_EXP(n):
    x_0 = 0.0
    N = n
    c_k = [1.0 for k in range(N)]
    return taylorSeries(c_k, N, x_0)

def taylor_LOG(n):
    x_0 = 1.0
    N = n
    c_k = [0.0] + [(-1)**(k+1)*gamma(k + 1)/k for k in numpy.arange(1, N, dtype=numpy.complex256)]
    return taylorSeries(c_k, N, x_0)

def taylor_bump(n):
    x_0 = 0.0
    N = n
    c_k = [((-1.0j)**k + 1.0j**k)*gamma(k+1)/2.0 for k in numpy.arange(N, dtype=numpy.complex256)]
    return taylorSeries(c_k, N, x_0)

N = 1700

exp = taylor_EXP(N)
log = taylor_LOG(N)
bump = taylor_bump(N)
x = numpy.linspace(-2, 5, 10000, dtype=numpy.complex256)

#pyplot.plot(x, log(x))
#pyplot.plot(x, numpy.log(x))

#pyplot.plot(x, log.derivative(x))
#pyplot.plot(x, 1.0/x)

#pyplot.plot(x, exp(x))
#pyplot.plot(x, numpy.exp(x))

#pyplot.plot(x, bump(x))
#pyplot.plot(x, 1/(x**2 + 1))
#pyplot.plot(x, bump.derivative(x))
#pyplot.plot(x, -(2*x)/(x**2 + 1)**2)

#pyplot.ylim(-10, 10)
#pyplot.show()

"""
exp2 = exp.analytic_continuation(0.5)
pyplot.plot(x, exp2(x))
pyplot.plot(x, exp(x))
pyplot.ylim(-10, 10)
pyplot.show()
"""

"""
log2 = log.analytic_continuation(1.5, N - 50)
pyplot.plot(x, log2(x))
pyplot.plot(x, log(x))
pyplot.ylim(-10, 10)
pyplot.show()
"""

m = 1.04
dx=0.01

pyplot.plot(x, bump(x), color="r")
for i in range(1, 100):
    print(i)
    bump = bump.analytic_continuation(dx*i, int(N/(m**i)))
    pyplot.plot(x, bump(x), color="g")

pyplot.plot(x, 1.0/(x**2 + 1), color="k")
pyplot.ylim(-10, 10)
pyplot.show()
