from matplotlib import pyplot
from scipy import special
import numpy

def gamma4(x):
    """
    Using Eulers reflection formula on Robert H. Windschitl's aproximation of the Gamma function.
    The accuracy of this aproximation improves with the distance from 0 + 0i.
    """
    output = 0.0*x
    mask = numpy.real(x) > 0
    output[mask] = gamma3(x[mask] + 1)/x[mask]
    output[~mask] = numpy.pi/(numpy.sin(numpy.pi*x[~mask])*gamma3(1-x[~mask]))
    return output

def gamma3(x):
    """
    Approximation by Robert H. Windschitl

    accuracy improves with the distance from the negative real half axis.
    """
    return numpy.sqrt(2*numpy.pi/x)*numpy.power(x*numpy.sqrt(x*numpy.sinh(1/x) + 1/(810*x**6))/numpy.e, x)

def gamma2(x):
    return numpy.sqrt(2*numpy.pi/x)*numpy.power(x/numpy.e, x)

def gamma1(x):
    x = numpy.array(x, dtype=numpy.complex128)
    return special.gamma(x)

def graph2d(Z, func):
    f = func(Z)
    pyplot.imshow(numpy.real(f))
    pyplot.show()
    pyplot.imshow(numpy.imag(f))
    pyplot.show()
    pyplot.imshow(numpy.abs(f))
    pyplot.show()
    pyplot.imshow(numpy.angle(f)/(2*numpy.pi), cmap="hsv")
    pyplot.show()
    pyplot.imshow(numpy.log(numpy.abs(f)))
    pyplot.show()

def graph2derror(Z):
    f1 = gamma1(Z)
    f2 = gamma2(Z)
    f3 = gamma3(Z)
    f4 = gamma4(Z)
    def relerror(val, ref):
        return 100*(val - ref)/ref

    pyplot.imshow(numpy.real(relerror(f2, f1)), vmin=-100, vmax=100)
    pyplot.title("real sterling")
    pyplot.show()

    pyplot.imshow(numpy.real(relerror(f3, f1)), vmin=-100, vmax=100)
    pyplot.title("real sterling V2")
    pyplot.show()

    pyplot.imshow(numpy.real(relerror(f4, f1)))
    pyplot.title("real sterling V3")
    pyplot.show()

    pyplot.imshow(numpy.imag(relerror(f2, f1)), vmin=-100, vmax=100)
    pyplot.title("imag sterling")
    pyplot.show()

    pyplot.imshow(numpy.imag(relerror(f3, f1)), vmin=-100, vmax=100)
    pyplot.title("imag sterling V2")
    pyplot.show()

    pyplot.imshow(numpy.imag(relerror(f4, f1)))
    pyplot.title("imag sterling V3")
    pyplot.show()

    pyplot.imshow(numpy.abs(relerror(f2, f1)), vmin=-100, vmax=100)
    pyplot.title("abs sterling")
    pyplot.show()

    pyplot.imshow(numpy.abs(relerror(f3, f1)), vmin=-100, vmax=100)
    pyplot.title("abs sterling V2")
    pyplot.show()

    pyplot.imshow(numpy.abs(relerror(f4, f1)))
    pyplot.title("abs sterling V3")
    pyplot.show()

    pyplot.imshow(relerror(numpy.angle(f2), numpy.angle(f1)), vmin=-100, vmax=100)
    pyplot.title("angle sterling")
    pyplot.show()

    pyplot.imshow(relerror(numpy.angle(f3), numpy.angle(f1)), vmin=-100, vmax=100)
    pyplot.title("angle sterling V2")
    pyplot.show()

    pyplot.imshow(relerror(numpy.angle(f4), numpy.angle(f1)))
    pyplot.title("angle sterling V3")
    pyplot.show()

    pyplot.imshow(relerror(numpy.log(numpy.abs(f2)), numpy.log(numpy.abs(f1))), vmin=-100, vmax=100)
    pyplot.title("log abs sterling")
    pyplot.show()

    pyplot.imshow(relerror(numpy.log(numpy.abs(f3)), numpy.log(numpy.abs(f1))), vmin=-100, vmax=100)
    pyplot.title("log abs sterling V2")
    pyplot.show()

    pyplot.imshow(relerror(numpy.log(numpy.abs(f4)), numpy.log(numpy.abs(f1))))
    pyplot.title("log abs sterling V3")
    pyplot.show()


def graph1dsidebyside(t, x):
    f1 = gamma1(x)
    f2 = gamma2(x)
    f3 = gamma3(x)
    f4 = gamma4(x)
    pyplot.plot(t, numpy.real(f1), label="gamma")
    pyplot.plot(t, numpy.real(f2), label="sterling")
    pyplot.plot(t, numpy.real(f3), label="sterling V2")
    pyplot.plot(t, numpy.real(f4), label="sterling V3")
    pyplot.title("real")
    pyplot.legend()
    pyplot.show()

    pyplot.plot(t, numpy.imag(f1), label="gamma")
    pyplot.plot(t, numpy.imag(f2), label="sterling")
    pyplot.plot(t, numpy.imag(f3), label="sterling V2")
    pyplot.plot(t, numpy.imag(f4), label="sterling V3")
    pyplot.title("imag")
    pyplot.legend()
    pyplot.show()

    pyplot.plot(t, numpy.abs(f1), label="gamma")
    pyplot.plot(t, numpy.abs(f2), label="sterling")
    pyplot.plot(t, numpy.abs(f3), label="sterling V2")
    pyplot.plot(t, numpy.abs(f4), label="sterling V3")
    pyplot.title("abs")
    pyplot.legend()
    pyplot.show()

    pyplot.plot(t, numpy.angle(f1)/(2*numpy.pi), label="gamma")
    pyplot.plot(t, numpy.angle(f2)/(2*numpy.pi), label="sterling")
    pyplot.plot(t, numpy.angle(f3)/(2*numpy.pi), label="sterling V2")
    pyplot.plot(t, numpy.angle(f4)/(2*numpy.pi), label="sterling V3")
    pyplot.title("angle")
    pyplot.legend()
    pyplot.show()

    pyplot.plot(t, numpy.log(numpy.abs(f1)), label="gamma")
    pyplot.plot(t, numpy.log(numpy.abs(f2)), label="sterling")
    pyplot.plot(t, numpy.log(numpy.abs(f3)), label="sterling V2")
    pyplot.plot(t, numpy.log(numpy.abs(f4)), label="sterling V3")
    pyplot.title("log abs")
    pyplot.legend()
    pyplot.show()

def graph1derror(t, x):
    def relerror(val, ref):
        return 100*(val - ref)/ref
    f1 = gamma1(x)
    f2 = gamma2(x)
    f3 = gamma3(x)
    f4 = gamma4(x)
    pyplot.plot(t, relerror(numpy.real(f2), numpy.real(f1)), label="sterling error")
    pyplot.plot(t, relerror(numpy.real(f3), numpy.real(f1)), label="sterling V2 error")
    pyplot.plot(t, relerror(numpy.real(f4), numpy.real(f1)), label="sterling V3 error")
    pyplot.title("real")
    pyplot.legend()
    pyplot.show()

    pyplot.plot(t, relerror(numpy.imag(f2), numpy.imag(f1)), label="sterling error")
    pyplot.plot(t, relerror(numpy.imag(f3), numpy.imag(f1)), label="sterling V2 error")
    pyplot.plot(t, relerror(numpy.imag(f4), numpy.imag(f1)), label="sterling V3 error")
    pyplot.title("imag")
    pyplot.legend()
    pyplot.show()

    pyplot.plot(t, relerror(numpy.abs(f2), numpy.abs(f1)), label="sterling error")
    pyplot.plot(t, relerror(numpy.abs(f3), numpy.abs(f1)), label="sterling V2 error")
    pyplot.plot(t, relerror(numpy.abs(f4), numpy.abs(f1)), label="sterling V3 error")
    pyplot.title("abs")
    pyplot.legend()
    pyplot.show()

    pyplot.plot(t, relerror(numpy.angle(f2), numpy.angle(f1)), label="sterling error")
    pyplot.plot(t, relerror(numpy.angle(f3), numpy.angle(f1)), label="sterling V2 error")
    pyplot.plot(t, relerror(numpy.angle(f4), numpy.angle(f1)), label="sterling V3 error")
    pyplot.title("angle")
    pyplot.legend()
    pyplot.show()

    pyplot.plot(t, relerror(numpy.log(numpy.abs(f2)), numpy.log(numpy.abs(f1))), label="sterling error")
    pyplot.plot(t, relerror(numpy.log(numpy.abs(f3)), numpy.log(numpy.abs(f1))), label="sterling V2 error")
    pyplot.plot(t, relerror(numpy.log(numpy.abs(f4)), numpy.log(numpy.abs(f1))), label="sterling V3 error")
    pyplot.title("log abs")
    pyplot.legend()
    pyplot.show()

range = 4.1
resolution = 2048
onedupres=100

x = numpy.linspace(-range, range, resolution*onedupres, dtype=numpy.complex256)

t = x
z = t + 0.1j

X, XI = numpy.meshgrid(x[::onedupres], 1.0j*x[::-1*onedupres])
Z = X + XI

graph1dsidebyside(x, z)
graph1derror(t, z)
graph2d(Z, gamma4)
graph2derror(Z)

