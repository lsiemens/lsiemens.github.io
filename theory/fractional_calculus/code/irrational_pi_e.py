from matplotlib import pyplot
import numpy

x_max = 20
x = numpy.linspace(-x_max, x_max, 1024)

def f(z, theta=0.0):
    return numpy.exp(numpy.e*z) + numpy.exp(numpy.pi*z) + numpy.exp(theta*1.0j)

def f_prime(z, theta=0.0):
    return numpy.e*numpy.exp(numpy.e*z) + numpy.pi*numpy.exp(numpy.pi*z)

def G(u, v):
    return numpy.exp(2*numpy.e*u) + numpy.exp(2*numpy.pi*u) - 2*numpy.exp((numpy.e + numpy.pi)*u)*numpy.cos((numpy.e - numpy.pi)*v + numpy.pi) - 1

def G_prime(u, v):
    return 2*numpy.e*numpy.exp(2*numpy.e*u) + 2*numpy.pi*numpy.exp(2*numpy.pi*u) - 2*(numpy.e + numpy.pi)*numpy.exp((numpy.e + numpy.pi)*u)*numpy.cos((numpy.e - numpy.pi)*v + numpy.pi)

def f_zero(z_inital, theta=0.0, order=20):
    z = z_inital
    for i in range(order):
        z = F_u(numpy.imag(z)) + numpy.imag(z)*1.0j
        z = z - f(z, theta)/f_prime(z, theta)
    return z

def F_u(v, order=20):
    try:
        u = numpy.ones(shape=v.shape)
    except AttributeError:
        u = 1.0

    for i in range(order):
        u = u - G(u, v)/G_prime(u, v)
    return u

def solution(x, b, a=0.0):
    return numpy.exp(numpy.exp(b)*x - a*b)

X, Y = numpy.meshgrid(x, x[::-1])
Z = X + Y*1.0j

zeros = [f_zero(0.0 + 1.0j), f_zero(0.0 + 3.0j)]

for i in range(300):
    zeros.append(f_zero(2*zeros[-1] - zeros[-2]))
zeros = numpy.array(zeros)

zeros_in_range = zeros[numpy.abs(zeros) < x_max]

extent = [-x_max, x_max, -x_max, x_max]
#pyplot.imshow(numpy.log(numpy.abs(f(Z))), vmax=3, extent=extent)
pyplot.imshow(numpy.angle(f(Z)), cmap="hsv", extent=extent)
pyplot.scatter(numpy.real(zeros_in_range), numpy.imag(zeros_in_range))
pyplot.plot(F_u(x, 20), x, c="k")
pyplot.show()


pyplot.scatter(numpy.real(numpy.exp(zeros)), numpy.imag(numpy.exp(zeros)), c="k")
pyplot.show()

from scipy import special
data = 0*Z
for i, zero in enumerate(zeros):
    data += solution(Z, zero) #/special.gamma(i + 1)

pyplot.imshow(numpy.log(numpy.abs(data)), extent=extent)
#pyplot.imshow(numpy.angle(data), extent=extent, cmap="hsv")
pyplot.show()

pyplot.imshow(numpy.angle(data), extent=extent, cmap="hsv")
pyplot.show()
