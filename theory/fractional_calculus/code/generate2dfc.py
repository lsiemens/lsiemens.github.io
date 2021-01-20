import numpy
import fc2dpy
from scipy import special
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation

resolution = 512 # 512
order = 128 # 128

PD = fc2dpy.polydisk(0.0 + 0.0j, 0 + -0.0j, 10.0, 10.0, resolution=resolution)
PD.set_parameterization(1.0 + 0.0j, 1.0 + 0.0j)

def encoding(a):
#    return 1.0/fc2dpy.Gamma(-a + 1) ####-------- NICE --------####
    beta = -1.5
    return (a)**beta

def hypergeometricfunction_2F1_11c(c, x, n=20):
    """
    2F1(1, 1; c; x)
    """
    out = 0
    n=128
    for i in range(n):
        out += fc2dpy.Gamma(i + 1)*fc2dpy.Gamma(c)*(x)**i/fc2dpy.Gamma(i + c)
    return out

def iv(v, z, n=10):
    out = 0
    for i in range(n):
        out += (z/2.0)**(2*i + v)/(fc2dpy.Gamma(i + 1)*fc2dpy.Gamma(i + v + 1))
    return out

def foobar1(x, a, order=None):
    return x**(a/2)*iv(-a, 2*numpy.sqrt(x))

def foobar2(x, a, order=None):
    if order is not None:
        return (x-1)**(a+1)*hypergeometricfunction_2F1_11c(a+2, 1-x, order)/fc2dpy.Gamma(a + 2)
    else:
        return (x-1)**(a+1)*hypergeometricfunction_2F1_11c(a+2, 1-x)/fc2dpy.Gamma(a + 2)

def foobar4(x, a, order=None, b=-1.0+0.0j):
    if order is not None:
        return (x-b)**(a+1)*hypergeometricfunction_2F1_11c(a+2, 1-x/b, order)/(b*fc2dpy.Gamma(a + 2)) + (x-b)**a*numpy.log(b)/fc2dpy.Gamma(a + 1)
    else:
        return (x-b)**(a+1)*hypergeometricfunction_2F1_11c(a+2, 1-x/b)/(b*fc2dpy.Gamma(a + 2)) + (x-b)**a*numpy.log(b)/fc2dpy.Gamma(a + 1)

def foobar3(x, a, order=None):
    return (x**a*(numpy.log(x) + special.digamma(1.0) - special.digamma(a + 1))/fc2dpy.Gamma(a + 1))

def foobar5(x, a, order=None):
    """
    equivelent to function encoding (a)**-1
    """
    import mpmath
    gammaincomplete = numpy.frompyfunc(mpmath.gammainc, 2, 1)
    output = (-x)**a*(gammaincomplete(-a, -x) - special.gamma(-numpy.array(a, dtype=numpy.complex128)))
    if hasattr(x, "__len__") or hasattr(a, "__len__"):
        print("array")
        return numpy.array(output, dtype=fc2dpy.array_dtype)
    else:
        print("complex")
        return numpy.complex(output)

T = fc2dpy.taylor_encoding(encoding, PD, "A")
fd = fc2dpy.generator_2d_from_1d(T, order=order)

#fd.function = foobar2
#fd.function_label = "LOG(1 + (x  - 1))"
#fd.function = foobar4
#fd.function_label = "LOG(b + (x  - b))"
#fd.function = foobar3
#fd.function_label = "ln(x)"
#fd.function = foobar5
#fd.function_label = "X^a GAMMAINC"

pyplot.ylim(-10, 10)
T.graph_encoding()
fd.vmax = 1
fd.vmin = -5
fd.graph1d_x(a=0.01)
fd.graph1d_a(x=0.01)
fd.graph2d()
