from matplotlib import pyplot
import numpy

alpha = 6
beta = numpy.sqrt(2)
theta = 0.0

x_max = 20
x = numpy.linspace(-x_max, x_max, 1024)

def f(z, theta=0.0):
    return numpy.exp(alpha*z) + numpy.exp(beta*z) + numpy.exp(theta*1.0j)

def f_prime(z, theta=0.0):
    return alpha*numpy.exp(alpha*z) + beta*numpy.exp(beta*z)

def G(u, v):
    return numpy.exp(2*alpha*u) + numpy.exp(2*beta*u) - 2*numpy.exp((alpha + beta)*u)*numpy.cos((beta - alpha)*v + numpy.pi) - 1

def G_prime(u, v):
    return 2*alpha*numpy.exp(2*alpha*u) + 2*beta*numpy.exp(2*beta*u) - 2*(alpha + beta)*numpy.exp((alpha + beta)*u)*numpy.cos((beta - alpha)*v + numpy.pi)

def f_zero(z_inital, theta=0.0, order=20):
    z = z_inital
    for i in range(order):
        z = F_u(numpy.imag(z)) + numpy.imag(z)*1.0j
        z = z - f(z, theta)/f_prime(z, theta)
        print(i, z)
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

zeros = [f_zero(0.0 + 2.0j, theta), f_zero(0.0 + 4.0j, theta)]

for i in range(6):
    zeros.append(f_zero( i*1.0j , theta))
zeros = numpy.array(zeros)

zeros_in_range = zeros[numpy.abs(zeros) < x_max]

extent = [-x_max, x_max, -x_max, x_max]
#pyplot.imshow(numpy.log(numpy.abs(f(Z))), vmax=3, extent=extent)
pyplot.imshow(numpy.angle(f(Z, theta)), cmap="hsv", extent=extent)
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
