from matplotlib import pyplot
from scipy import special
import numpy

class polydisk:
    """
    define a C^2 polydisk with 2d cross section
    """
    def __init__(self, x, a, r_x, r_a, resolution=1000):
        self.x = x
        self.a = a
        self.radius_x = numpy.abs(r_x)
        self.radius_a = numpy.abs(r_a)
        self.resolution = resolution

        self.Parameter_t = None
        self.Path_x = None
        self.Path_a = None
        self.label_x = None
        self.label_a = None

        self.dx = None
        self.da = None

        self.Grid_x = None
        self.Grid_a = None

        self.set_parameterization(1.0, 1.0)

    def set_parameterization(self, direction_x, direction_a):
        if (numpy.isclose(numpy.abs(direction_x), 0.0) or numpy.isclose(numpy.abs(direction_a), 0.0)):
            raise ValueError("Directions must be non-zero")
        direction_x = direction_x/numpy.abs(direction_x)
        direction_a = direction_a/numpy.abs(direction_a)

        self.Parameter_t = numpy.linspace(-1.0, 1.0, self.resolution)
        self.Path_x = self.x + direction_x*self.radius_x*self.Parameter_t
        self.Path_a = self.a + direction_a*self.radius_a*self.Parameter_t
        self.label_x = "x: ({:.2f}, {:.2f}), radius: {:.2f}".format(self.x - direction_x*self.radius_x, self.x + direction_x*self.radius_x, self.radius_x)
        self.label_a = "a: ({:.2f}, {:.2f}), radius: {:.2f}".format(self.a - direction_a*self.radius_a, self.a + direction_a*self.radius_a, self.radius_a)

        self.dx = numpy.mean(self.Path_x[1:] - self.Path_x[:-1])
        self.da = numpy.mean(self.Path_a[1:] - self.Path_a[:-1])

        self.Grid_x, self.Grid_a = numpy.meshgrid(self.Path_x, self.Path_a[::-1])

class taylor_encoding:
    """
    define a function that encode a taylor series as its value on the negative integers.
    that is g(a=-k) = d^k/dx^k f(x)
    """
    def __init__(self, encoding_function, polydisk, function_label):
        self.encoding_function = encoding_function
        self.polydisk = polydisk
        self.function_label = function_label

    def graph_encoding(self):
        data = self.encoding_function(self.polydisk.Path_a)

        pyplot.plot(self.polydisk.Parameter_t, numpy.real(data), label="real(f(a))")
        pyplot.plot(self.polydisk.Parameter_t, numpy.imag(data), label="imag(f(a))")
        pyplot.xlabel(self.polydisk.label_a)
        pyplot.ylabel("f(a)")
        pyplot.title("encoding function \"f(a) = " + self.function_label + "\"")
        pyplot.legend()
        pyplot.show()

class function_FD:
    """
    2d fractionaly differentiable function
    """
    def __init__(self, function, polydisk, function_label):
        self.function = function
        self.polydisk = polydisk
        self.function_label = function_label
        self.vmin = None
        self.vmax = None
        self.order = None
        self.generating_function_label = "$f(0, a) = " + self.function_label + "$ with $\delta_x f(x, a) = f(x, a - 1)$"

    def derivative(self):
        def fractional_function(x, a, order=None):
            print(len(numpy.gradient(self.function(x, a, order=order))))
            return numpy.gradient(self.function(x, a, order=order))[1]/self.polydisk.dx
        data = function_FD(fractional_function, self.polydisk, self.function_label)
        return data

    def graph1d_x(self, a=None):
        if a is None:
            a = self.polydisk.a
        data = self.function(self.polydisk.Path_x, a)
        pyplot.plot(self.polydisk.Parameter_t, numpy.real(data), label="$real(f(x, a_0))$")
        pyplot.plot(self.polydisk.Parameter_t, numpy.imag(data), label="$imag(f(x, a_0))$")

        pyplot.xlabel(self.polydisk.label_x)
        pyplot.ylabel("$f(x, a_0)$")
        pyplot.ylim(self.vmin, self.vmax)
        pyplot.title("$f(x, a_0)$, $a_0 = {:.2f}$\n".format(a) + self.generating_function_label)
        pyplot.legend()
        pyplot.show()

    def graph1d_a(self, x=None):
        if x is None:
            x = self.polydisk.x
        data = self.function(x, self.polydisk.Path_a)
        pyplot.plot(self.polydisk.Parameter_t, numpy.real(data), label="$real(f(x_0, a))$")
        pyplot.plot(self.polydisk.Parameter_t, numpy.imag(data), label="$imag(f(x_0, a))$")

        pyplot.xlabel(self.polydisk.label_a)
        pyplot.ylabel("$f(x_0, a)$")
        pyplot.ylim(self.vmin, self.vmax)
        pyplot.title("$f(x_0, a)$, $x_0 = {:.2f}$\n".format(x) + self.generating_function_label)
        pyplot.legend()
        pyplot.show()

    def graph1d_x_order_range(self, a=None, order_min=100, order_range=10):
        self.generating_function_label = "$f(0, a) = " + self.function_label + "$ with $\delta_x f(x, a) = f(x, a - 1)$"
        if a is None:
            a = self.polydisk.a

        data = self.function(self.polydisk.Path_x, a, order = order_min)
        pyplot.plot(self.polydisk.Parameter_t, numpy.real(data), label="$real(f(x, a_0))$")
        pyplot.plot(self.polydisk.Parameter_t, numpy.imag(data), label="$imag(f(x, a_0))$")

        for i in range(order_min + 1, order_min + order_range + 1):
            data = self.function(self.polydisk.Path_x, a, order=i)
            pyplot.plot(self.polydisk.Parameter_t, numpy.real(data))
            pyplot.plot(self.polydisk.Parameter_t, numpy.imag(data))

        pyplot.xlabel(self.polydisk.label_x)
        pyplot.ylabel("$f(x, a_0)$")
        pyplot.ylim(10*self.vmin, 10*self.vmax)
        pyplot.title("$f(x, a_0)$, $a_0 = {:.2f}$\n".format(a) + self.generating_function_label)
        pyplot.legend()
        pyplot.show()

    def graph2d(self):
        extent = [-1, 1.0, -1.0, 1.0]

        data = self.function(self.polydisk.Grid_x, self.polydisk.Grid_a, self.order)

        pyplot.imshow(numpy.real(data), extent=extent, vmin=self.vmin, vmax=self.vmax)
        pyplot.xlabel(self.polydisk.label_x)
        pyplot.ylabel(self.polydisk.label_a)
        pyplot.title("$real(f(x, a))$\n" + self.generating_function_label)
        pyplot.show()

        pyplot.imshow(numpy.imag(data), extent=extent, vmin=self.vmin, vmax=self.vmax)
        pyplot.xlabel(self.polydisk.label_x)
        pyplot.ylabel(self.polydisk.label_a)
        pyplot.title("$imag(f(x, a))$\n" + self.generating_function_label)
        pyplot.show()

        vmax = None
        if (self.vmax is not None) and (self.vmin is not None):
            vmax = max(numpy.abs(self.vmax), numpy.abs(self.vmin))
        else:
            if self.vmin is not None:
                vmax = numpy.abs(self.vmin)
            if self.vmax is not None:
                vmax = numpy.abs(self.vmax)
        pyplot.imshow(numpy.abs(data), extent=extent, vmin=0.0, vmax=vmax)
        pyplot.xlabel(self.polydisk.label_x)
        pyplot.ylabel(self.polydisk.label_a)
        pyplot.title("$abs(f(x, a))$\n" + self.generating_function_label)
        pyplot.show()

        pyplot.imshow(numpy.angle(data), extent=extent)
        pyplot.xlabel(self.polydisk.label_x)
        pyplot.ylabel(self.polydisk.label_a)
        pyplot.title("$arg(f(x, a))$\n" + self.generating_function_label)
        pyplot.show()

        pyplot.imshow(numpy.log(numpy.abs(data)), extent=extent)
        pyplot.xlabel(self.polydisk.label_x)
        pyplot.ylabel(self.polydisk.label_a)
        pyplot.title("$ln(abs(f(x, a)))$\n" + self.generating_function_label)
        pyplot.show()

    def graph2d_zeros(self, show=True):
        extent = [-1, 1.0, -1.0, 1.0]

        data = self.function(self.polydisk.Grid_x, self.polydisk.Grid_a, self.order)

        pyplot.imshow(numpy.log(numpy.abs(data)), extent=extent)
        pyplot.xlabel(self.polydisk.label_x)
        pyplot.ylabel(self.polydisk.label_a)
        pyplot.title("$ln(abs(f(x, a)))$\n" + self.generating_function_label)

        if show:
            pyplot.show()

def generator_2d_from_1d(encoding, order = 100):
    """
    construct 2d fractionaly differentiable function from 1d encodeing of a taylor series
    """
    if (order < 1):
        raise ValueError("Taylor expansion must contain 1 or more terms")

    _order = order

    def fractional_function(x, a, order=None):
        if order is None:
            order = _order
        output = 0.0
        for i in range(order):
            output += encoding.encoding_function(a - i)*x**i/special.gamma(i + 1)
        return output

    data = function_FD(fractional_function, encoding.polydisk, encoding.function_label)
    return data
