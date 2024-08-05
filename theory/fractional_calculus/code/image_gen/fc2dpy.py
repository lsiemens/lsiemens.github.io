from matplotlib import pyplot
from scipy import special
import time
import numpy
import cplot

default_rng = numpy.random.default_rng()
array_dtype = numpy.complex256
approximate_gamma = True

def _GammaRHW(x):
    """
    Approximation by Robert H. Windschitl

    accuracy improves with the distance from the negative real half axis.
    """
    return numpy.sqrt(2*numpy.pi/x)*numpy.power(x*numpy.sqrt(x*numpy.sinh(1/x) + 1/(810*x**6))/numpy.e, x)

def Gamma(x):
    """
    Using Eulers reflection formula on Robert H. Windschitl's aproximation of the Gamma function.
    The accuracy of this aproximation improves with the distance from 0 + 0i.
    """
    # for accurate gamma use scipy, for large input values use approximate function
    if not approximate_gamma:
        return special.gamma(x)

    output = 0.0*x
    mask = numpy.real(x) > 0
    try:
        output[mask] = _GammaRHW(x[mask] + 1)/x[mask]
        output[~mask] = numpy.pi/(numpy.sin(numpy.pi*x[~mask])*_GammaRHW(1-x[~mask]))
    except TypeError: # handle non-iterable types
        return Gamma(numpy.array([x], dtype=array_dtype))[0]
    return output

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
        self.label_xj = None
        self.label_a = None
        self.label_aj = None

        self.dx = None
        self.da = None

        self.Grid_x = None
        self.Grid_a = None

        self.Complex_Plane_x = None
        self.Complex_Plane_a = None

        self.set_parameterization(1.0, 1.0)

    def set_parameterization(self, direction_x, direction_a):
        if (numpy.isclose(numpy.abs(direction_x), 0.0) or numpy.isclose(numpy.abs(direction_a), 0.0)):
            raise ValueError("Directions must be non-zero")
        direction_x = direction_x/numpy.abs(direction_x)
        direction_a = direction_a/numpy.abs(direction_a)

        self.Parameter_t = numpy.linspace(-1.0, 1.0, self.resolution, dtype=array_dtype)
        self.Path_x = self.x + direction_x*self.radius_x*self.Parameter_t
        self.Path_a = self.a + direction_a*self.radius_a*self.Parameter_t
        self.label_x = "x: ({:.2f}, {:.2f}), radius: {:.2f}".format(self.x - direction_x*self.radius_x, self.x + direction_x*self.radius_x, self.radius_x)
        self.label_xj = "x: ({:.2f}, {:.2f}), radius: {:.2f}".format((self.x - direction_x*self.radius_x)*1.0j, (self.x + direction_x*self.radius_x)*1.0j, self.radius_x)
        self.label_a = "a: ({:.2f}, {:.2f}), radius: {:.2f}".format(self.a - direction_a*self.radius_a, self.a + direction_a*self.radius_a, self.radius_a)
        self.label_aj = "a: ({:.2f}, {:.2f}), radius: {:.2f}".format((self.a - direction_a*self.radius_a)*1.0j, (self.a + direction_a*self.radius_a)*1.0j, self.radius_a)

        self.dx = numpy.mean(self.Path_x[1:] - self.Path_x[:-1])
        self.da = numpy.mean(self.Path_a[1:] - self.Path_a[:-1])

        self.Grid_x, self.Grid_a = numpy.meshgrid(self.Path_x, self.Path_a[::-1])

        plane_x, plane_xj = numpy.meshgrid(self.Path_x, self.Path_x[::-1]*1.0j)
        self.Complex_Plane_x = plane_x + plane_xj
        plane_a, plane_aj = numpy.meshgrid(self.Path_a, self.Path_a[::-1]*1.0j)
        self.Complex_Plane_a = plane_a + plane_aj

        self.Parameter_t = numpy.real(self.Parameter_t)

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

    def imslice(self, origin, vertical_vector, horizontal_vector, vertical_resolution, horizontal_resolution, fname=None):
        print("resolution aspect ratio: ", horizontal_resolution/vertical_resolution)
        print("parameter aspect ratio: ", numpy.sqrt(numpy.abs(horizontal_vector[0])**2 + numpy.abs(horizontal_vector[1])**2)/numpy.sqrt(numpy.abs(vertical_vector[0])**2 + numpy.abs(vertical_vector[1])**2), "\n")

        vertical_x = numpy.linspace(origin[0] - vertical_vector[0], origin[0] + vertical_vector[0], vertical_resolution, dtype=array_dtype)
        horizontal_x = numpy.linspace(origin[0] - horizontal_vector[0], origin[0] + horizontal_vector[0], horizontal_resolution, dtype=array_dtype)
        vertical_dx = vertical_vector[0]/(vertical_resolution - 1)
        horizontal_dx = horizontal_vector[0]/(horizontal_resolution - 1)

        vertical_a = numpy.linspace(origin[1] - vertical_vector[1], origin[1] + vertical_vector[1], vertical_resolution, dtype=array_dtype)
        horizontal_a = numpy.linspace(origin[1] - horizontal_vector[1], origin[1] + horizontal_vector[1], horizontal_resolution, dtype=array_dtype)
        vertical_da = vertical_vector[1]/(vertical_resolution - 1)
        horizontal_da = horizontal_vector[1]/(horizontal_resolution - 1)

        jitter = default_rng.uniform(-1, 1, (2, vertical_resolution, horizontal_resolution))

        Grid_xh, Grid_xv = numpy.meshgrid(horizontal_x, vertical_x[::-1])
        Grid_ah, Grid_av = numpy.meshgrid(horizontal_a, vertical_a[::-1])
        Grid_x = (Grid_xh + horizontal_dx*jitter[0]) + (Grid_xv + vertical_dx*jitter[1])
        Grid_a = (Grid_ah + horizontal_da*jitter[0]) + (Grid_av + vertical_da*jitter[1])

        extent = [-1.0, 1.0, -1.0, 1.0]
        data = self.function(Grid_x, Grid_a, self.order)

        cplot.cimshow(data, extent=extent, modRange=True, vmin=self.vmin, vmax=self.vmax, fname=fname)
        if fname is None:
            pyplot.show()

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

    def graphXplane(self, a=None):
        if a is None:
            a = self.polydisk.a

        extent = [-1.0, 1.0, -1.0, 1.0]
        data = self.function(self.polydisk.Complex_Plane_x, a, self.order)

        cplot.cimshow(data, extent=extent, modRange=True, vmin=self.vmin, vmax=self.vmax)
        pyplot.xlabel(self.polydisk.label_x)
        pyplot.ylabel(self.polydisk.label_xj)
        pyplot.title("$abs(f(x, a_0))$ $mod$ ${:.1f}$, $arg(f(x, a_0))$, $a_0={:.2f}$\n".format(self.vmax - self.vmin, a) + self.generating_function_label)
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
        pyplot.ylabel(self.polydisk.label_xj)
        pyplot.title("$abs(f(x, a_0))$, $a_0={:.2f}$\n".format(a) + self.generating_function_label)
        pyplot.show()

        pyplot.imshow(numpy.angle(data)/(2*numpy.pi), extent=extent, cmap="hsv")
        pyplot.xlabel(self.polydisk.label_x)
        pyplot.ylabel(self.polydisk.label_xj)
        pyplot.title("$arg(f(x, a_0))$, $a_0={:.2f}$\n".format(a) + self.generating_function_label)
        pyplot.show()

        cplot.cimshow(data, extent=extent, logMag=True)
        pyplot.xlabel(self.polydisk.label_x)
        pyplot.ylabel(self.polydisk.label_xj)
        pyplot.title("$log_{{10}}(abs(f(x, a_0)))$, $arg(f(x, a_0))$, $a_0={:.2f}$\n".format(a) + self.generating_function_label)
        pyplot.show()

        cplot.cimshow(data, extent=extent, logMag=True, modRange=True, vmin=0, vmax=1)
        pyplot.xlabel(self.polydisk.label_x)
        pyplot.ylabel(self.polydisk.label_xj)
        pyplot.title("$log_{{10}}(abs(f(x, a_0)))$ $mod$ $1.0$, $arg(f(x, a_0))$, $a_0={:.2f}$\n".format(a) + self.generating_function_label)
        pyplot.show()

        pyplot.imshow(numpy.log(numpy.abs(data))/numpy.log(10), extent=extent)
        pyplot.xlabel(self.polydisk.label_x)
        pyplot.ylabel(self.polydisk.label_xj)
        pyplot.title("$log_{{10}}(abs(f(x, a_0)))$, $a_0={:.2f}$\n".format(a) + self.generating_function_label)
        pyplot.show()

    def graphAplane(self, x=None):
        if x is None:
            x = self.polydisk.x

        extent = [-1.0, 1.0, -1.0, 1.0]
        data = self.function(x, self.polydisk.Complex_Plane_a, self.order)

        cplot.cimshow(data, extent=extent, modRange=True, vmin=self.vmin, vmax=self.vmax)
        pyplot.xlabel(self.polydisk.label_a)
        pyplot.ylabel(self.polydisk.label_aj)
        pyplot.title("$abs(f(x_0, a))$ $mod$ ${:.1f}$, $arg(f(x_0, a))$, $x_0={:.2f}$\n".format(self.vmax - self.vmin, x) + self.generating_function_label)
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
        pyplot.xlabel(self.polydisk.label_a)
        pyplot.ylabel(self.polydisk.label_aj)
        pyplot.title("$abs(f(x_0, a))$, $x_0={:.2f}$\n".format(x) + self.generating_function_label)
        pyplot.show()

        pyplot.imshow(numpy.angle(data)/(2*numpy.pi), extent=extent, cmap="hsv")
        pyplot.xlabel(self.polydisk.label_a)
        pyplot.ylabel(self.polydisk.label_aj)
        pyplot.title("$arg(f(x_0, a))$, $x_0={:.2f}$\n".format(x) + self.generating_function_label)
        pyplot.show()

        cplot.cimshow(data, extent=extent, logMag=True)
        pyplot.xlabel(self.polydisk.label_a)
        pyplot.ylabel(self.polydisk.label_aj)
        pyplot.title("$log_{{10}}(abs(f(x_0, a)))$, $arg(f(x_0, a))$, $x_0={:.2f}$\n".format(x) + self.generating_function_label)
        pyplot.show()

        cplot.cimshow(data, extent=extent, logMag=True, modRange=True, vmin=0, vmax=1)
        pyplot.xlabel(self.polydisk.label_a)
        pyplot.ylabel(self.polydisk.label_aj)
        pyplot.title("$log_{{10}}(abs(f(x_0, a)))$ $mod$ $1.0$, $arg(f(x_0, a))$, $x_0={:.2f}$\n".format(x) + self.generating_function_label)
        pyplot.show()

        pyplot.imshow(numpy.log(numpy.abs(data))/numpy.log(10), extent=extent)
        pyplot.xlabel(self.polydisk.label_a)
        pyplot.ylabel(self.polydisk.label_aj)
        pyplot.title("$log_{{10}}(abs(f(x_0, a)))$, $x_0={:.2f}$\n".format(x) + self.generating_function_label)
        pyplot.show()

    def graph2d(self):
        extent = [-1.0, 1.0, -1.0, 1.0]
        data = self.function(self.polydisk.Grid_x, self.polydisk.Grid_a, self.order)

        cplot.cimshow(data, extent=extent, modRange=True, vmin=self.vmin, vmax=self.vmax)
        pyplot.xlabel(self.polydisk.label_x)
        pyplot.ylabel(self.polydisk.label_a)
        pyplot.title("$abs(f(x, a))$ $mod$ ${0:.1f}$, $arg(f(x, a))$\n".format(self.vmax - self.vmin) + self.generating_function_label)
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

        pyplot.imshow(numpy.angle(data)/(2*numpy.pi), extent=extent, cmap="hsv")
        pyplot.xlabel(self.polydisk.label_x)
        pyplot.ylabel(self.polydisk.label_a)
        pyplot.title("$arg(f(x, a))$\n" + self.generating_function_label)
        pyplot.show()

        cplot.cimshow(data, extent=extent, logMag=True)
        pyplot.xlabel(self.polydisk.label_x)
        pyplot.ylabel(self.polydisk.label_a)
        pyplot.title("$log_{10}(abs(f(x, a)))$, $arg(f(x, a))$\n" + self.generating_function_label)
        pyplot.show()

        cplot.cimshow(data, extent=extent, logMag=True, modRange=True, vmin=0, vmax=1)
        pyplot.xlabel(self.polydisk.label_x)
        pyplot.ylabel(self.polydisk.label_a)
        pyplot.title("$log_{10}(abs(f(x, a)))$ $mod$ $1.0$, $arg(f(x, a))$\n" + self.generating_function_label)
        pyplot.show()

        pyplot.imshow(numpy.log(numpy.abs(data))/numpy.log(10), extent=extent)
        pyplot.xlabel(self.polydisk.label_x)
        pyplot.ylabel(self.polydisk.label_a)
        pyplot.title("$log_{10}(abs(f(x, a)))$\n" + self.generating_function_label)
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

        start = time.time()
        for i in range(order):
            estimate = (time.time() - start)*(order/(i + 1) - 1.0)
            print(f"Taylor series term {i + 1} of {order}. ETA: " + estimateTime(start, i, order), end="\r")
            output += encoding.encoding_function(a - i)*x**i/Gamma(i + 1)
        estimate = (time.time() - start)*(order/(i + 1) - 1.0)
        print(f"Taylor series term {i + 1} of {order}. ETA: " + estimateTime(start, i, order))
        print(f"Taylor series finished. Computation time: " + estimateTime(start, 0, 2))
        return output

    data = function_FD(fractional_function, encoding.polydisk, encoding.function_label)
    return data

def estimateTime(start, iteration, N):
    estimate = (time.time() - start)*(N/(iteration + 1) - 1.0)
    if estimate < 60:
        return f"{estimate:.3f}s" + 10*" "
    elif estimate < 60*60:
        minutes, seconds = divmod(estimate, 60)
        return f"{minutes}m {seconds:.3f}s" + 10*" "
    else:
        hours, estimate = divmod(estimate, 60)
        minutes, seconds = divmod(estimate, 60)
        return f"{hours}h + {minutes}m {seconds:.3f}s" + 10*" "
