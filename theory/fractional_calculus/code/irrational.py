from matplotlib import pyplot
import numpy


def F(z):
    return numpy.exp(-2*z) + numpy.exp(-numpy.pi*z) + 1

#range = (numpy.pi + numpy.e)*10/2
#range = 2.9685*100
range = 120
#range = 12
period = 1.0
resolution = 1200
x = numpy.linspace(-range, range, resolution)
x = x - period/2.0
x_i = x//period + 1
x_f = x % period - period/2.0
x = x + period/2.0

#pyplot.scatter(x, x_f)
#pyplot.scatter(x, x_i)
#pyplot.plot(x, period*x_i + x_f)
#pyplot.plot(x, x, c="k")
#pyplot.show()

#X, Y = numpy.meshgrid(x_f, x[::-1])
#Y = Y + 2*range*x_i
#Z = X + Y*1.0j
X, Y = numpy.meshgrid(x, x[::-1])
Z = X + Y*1.0j



extent = [-range, range, -range, range]
#extent = [-1, 1, -1, 1]

pyplot.imshow(numpy.log(numpy.abs(F(Z)/F(X))), extent=extent)
#pyplot.imshow(numpy.angle(F(Z)), extent=extent, cmap="hsv")

#pyplot.plot((period/2)*numpy.real(F(x*1.0j)/F(0)), x, c='r')
#pyplot.plot((period/2)*numpy.imag(F(x*1.0j)/F(0)), x, c='r')
#pyplot.plot(0*x, x, c='r')

#pyplot.plot((period/2)*numpy.real(F(x*1.0j -0.5)/F(-0.5))-0.5, x, c='g')
#pyplot.plot((period/2)*numpy.imag(F(x*1.0j -0.5)/F(-0.5))-0.5, x, c='g')
#pyplot.plot(0*x -0.5, x, c='g')

#pyplot.plot((period/2)*numpy.real(F(x*1.0j +0.27)/F(+0.27))+0.27, x, c='b')
#pyplot.plot((period/2)*numpy.imag(F(x*1.0j +0.27)/F(+0.27))+0.27, x, c='b')
#pyplot.plot(0*x +0.27, x, c='b')

x = numpy.linspace(0, 60, 10000)
#dx = numpy.mean(x[1:] - x[:-1])
#x = x - dx/2

a = numpy.pi
b = 2 - 1

X, Y = a - b*numpy.cos(x + numpy.pi), a*x - b*numpy.sin(x + numpy.pi)
X, Y = X/(2*numpy.pi), Y/(2*numpy.pi)
X, Y = 4.725*X, 4.725*Y
X = X -0.2 - 2.18
#X = X*0.45/1.33

# 4.5 5
pyplot.plot(X, Y)

pyplot.show()

T = [0] + (numpy.cumsum(numpy.sqrt(numpy.diff(Y)**2 + numpy.diff(X)**2))).tolist()
T = numpy.array(T)
#pyplot.scatter(T, X)
#pyplot.scatter(T, Y)
#pyplot.show()

t = numpy.linspace(0, 120, 10000)
dt = numpy.mean(t[1:] - t[:-1])
t = t + dt/2
#pyplot.scatter(numpy.interp(t, T, X), numpy.interp(t, T, Y))
pyplot.show()

z = numpy.interp(t, T, X) + numpy.interp(t, T, Y)*1.0j
#pyplot.plot(t, numpy.real(F(z)))
#pyplot.plot(t, numpy.imag(F(z)))
##pyplot.plot(t, numpy.abs(F(z)))
##pyplot.plot(t, t*0)
##pyplot.show()
