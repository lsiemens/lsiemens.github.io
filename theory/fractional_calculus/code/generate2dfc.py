import numpy
import fc2dpy
from scipy import special
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation

fc2dpy.array_dtype=numpy.complex256

resolution = 256 # 512 4096
order = 128 # 128

PD = fc2dpy.polydisk(0.0 + 0.0j, 0.0 + -0.1j, 15.0, numpy.pi, resolution=resolution) #cos
#PD = fc2dpy.polydisk(0.0 + 1j, 1.5 + -1j, 15.0, 5.0, resolution=resolution)
PD.set_parameterization(1.0 + 0.0j, 1.0 + 0.0j)

def encoding(a):
#    return fc2dpy.Gamma(a + 1) ####-------- NICE --------####
#    return 1.0/fc2dpy.Gamma(-a + 1) ####-------- NICE --------####
#    beta = -numpy.pi/2
#    return (a)**beta
    return numpy.cos(a) + numpy.tan(a) # cos
#    return numpy.exp(-1/(a**3)) # nice

def Log(x, a, order=None):
    return (x**a*(numpy.log(x) + special.digamma(1.0) - special.digamma(a + 1))/fc2dpy.Gamma(a + 1))

def func_inverse_a(x, a, order=None):
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

#def foo(x, a, order=None):
#    return x + 0*a

T = fc2dpy.taylor_encoding(encoding, PD, "A")
fd = fc2dpy.generator_2d_from_1d(T, order=order)

#fd.function = Log
#fd.function_label = "ln(x)"
#fd.function = func_inverse_a
#fd.function_label = "X^a GAMMAINC"
#fd.function = foo
#fd.function_label = "X"

pyplot.ylim(-10, 10)
T.graph_encoding()
fd.vmax = 1
fd.vmin = -5
fd.graph1d_x(a=0.01)
fd.graph1d_a(x=0.01)
#fd.g2cxplane()
fd.graphXplane()
fd.graphAplane()
fd.graph2d()
