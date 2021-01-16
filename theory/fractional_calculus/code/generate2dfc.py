import numpy
import fc2dpy
from scipy import special
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation

resolution = 512 # 512
order = 512 # 128

PD = fc2dpy.polydisk(0, 0, 2.0, 5.0, resolution=resolution)
PD.set_parameterization(1.0 + 0.0j, 1.0 + 0.0j)
def encoding(a):
    return 1.0/special.gamma(-a + 1) ####-------- NICE --------####

def hypergeometricfunction_2F1_11c(c, x, n=20):
    """
    2F1(1, 1; c; x)
    """
    out = 0
    n=128
    for i in range(n):
        out += special.gamma(i + 1)*special.gamma(c)*(x)**i/special.gamma(i + c)
    return out

def iv(v, z, n=10):
    out = 0
    for i in range(n):
        out += (z/2.0)**(2*i + v)/(special.gamma(i + 1)*special.gamma(i + v + 1))
    return out

def foobar1(x, a, order=None):
    return x**(a/2)*iv(-a, 2*numpy.sqrt(x))

def foobar2(x, a, order=None):
    if order is not None:
        return (x-1)**(a+1)*hypergeometricfunction_2F1_11c(a+2, 1-x, order)/special.gamma(a + 2)
    else:
        return (x-1)**(a+1)*hypergeometricfunction_2F1_11c(a+2, 1-x)/special.gamma(a + 2)

def foobar4(x, a, order=None, b=-1.0+0.0j):
    if order is not None:
        return (x-b)**(a+1)*hypergeometricfunction_2F1_11c(a+2, 1-x/b, order)/(b*special.gamma(a + 2)) + (x-b)**a*numpy.log(b)/special.gamma(a + 1)
    else:
        return (x-b)**(a+1)*hypergeometricfunction_2F1_11c(a+2, 1-x/b)/(b*special.gamma(a + 2)) + (x-b)**a*numpy.log(b)/special.gamma(a + 1)

def foobar3(x, a, order=None):
    return (x**a*(numpy.log(x) + special.digamma(1.0) - special.digamma(a + 1))/special.gamma(a + 1))

T = fc2dpy.taylor_encoding(encoding, PD, "A")
fd = fc2dpy.generator_2d_from_1d(T, order=order)

fd.function = foobar2
fd.function_label = "LOG(1 + (x  - 1))"
fd.function = foobar4
fd.function_label = "LOG(b + (x  - b))"
fd.function = foobar3
fd.function_label = "ln(x)"

pyplot.ylim(-10, 10)
#T.graph_encoding()
fd.vmax = 1
fd.vmin = -5
#fd.graph1d_x(a=-0.0)
fd.graph1d_x_order_range(a= 2.000001)
fd.graph1d_x_order_range(a= 1.750001)
fd.graph1d_x_order_range(a= 1.500001)
fd.graph1d_x_order_range(a= 1.250001)
fd.graph1d_x_order_range(a= 1.000001)
fd.graph1d_x_order_range(a= 0.750001)
fd.graph1d_x_order_range(a= 0.500001)
fd.graph1d_x_order_range(a= 0.250001)
fd.graph1d_x_order_range(a= 0.000001)
fd.graph1d_x_order_range(a=-0.250001)
fd.graph1d_x_order_range(a=-0.500001)
fd.graph1d_x_order_range(a=-0.750001)
fd.graph1d_x_order_range(a=-1.0001)
fd.graph1d_x_order_range(a=-1.2501)
fd.graph1d_x_order_range(a=-1.5001)
fd.graph1d_x_order_range(a=-1.7501)
fd.graph1d_x_order_range(a=-2.0001)
#fd.graph1d_a(x=0.0)
fd.graph2d()
