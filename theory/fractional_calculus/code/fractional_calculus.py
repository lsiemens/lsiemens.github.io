from matplotlib import pyplot
from scipy.special import gamma, factorial
import numpy

x_0 = 100

x = numpy.linspace(-x_0, x_0, 10000)

def prepFunction(f):
    return f - f[0]

def derivative(x, f):
    f_prime = numpy.zeros(shape=x.shape)
    f_prime[1:] = (f[1:] - f[:-1])/(x[1:] - x[:-1])
    return f_prime

def antiderivative(x, df):
    f = numpy.zeros(shape=x.shape)
    f[1:] = numpy.cumsum(df[1:]*(x[1:] - x[:-1]))
    return f

def antiderivative_point(x, df):
    f = numpy.sum(df[1:]*(x[1:] - x[:-1]))
    return f

def fractional_integral(x, df, alpha=1.0):
    f = numpy.zeros(shape=x.shape)
    gamma_alpha = gamma(alpha)
    for i, x_i in enumerate(x):
        f[i] = (1/gamma_alpha)*antiderivative_point(x[:i + 1], numpy.power(x_i - x[:i + 1], alpha - 1)*df[:i + 1])
    return f

def D(x, f):
    return derivative(x, f)

def aD(x, df):
    return antiderivative(x, df)
