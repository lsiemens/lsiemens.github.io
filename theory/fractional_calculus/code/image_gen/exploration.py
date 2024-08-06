#!/usr/bin/python3

import numpy
import fc2dpy
from scipy import special
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation

fc2dpy.array_dtype=numpy.complex256

fname_base = "./tmp/test_"
show = True
resolution = 512 # 512 4096
#resolution = 1024*3*2
order = 256 # 128

#PD = fc2dpy.polydisk(0.0 + 0.0j, 0.0 + -0.1j, 15.0, numpy.pi, resolution=resolution) #cos
PD = fc2dpy.polydisk(0.0 + 1j, 1.5 + -1j, 15.0, 5.0, resolution=resolution)
PD.set_parameterization(1.0 + 0.0j, 1.0 + 0.0j)

def encoding(a):
#    return fc2dpy.Gamma(a + 1) ####-------- NICE --------####
#    return 1.0/fc2dpy.Gamma(-a + 1) ####-------- NICE --------####
#    beta = -numpy.pi/2
#    return (a)**beta
#    return numpy.cos(a) + numpy.tan(a*numpy.exp(-1)) # cos
    return numpy.exp(-1/(a**3)) # nice

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

T = fc2dpy.taylor_encoding(encoding, PD, "A")
fd = fc2dpy.generator_2d_from_1d(T, order=order)

fd.vmax = 1
fd.vmin = -5

i = 0
stop = False
while not stop:
    i += 1
    fname = f"{fname_base}{i}.npy"
    if show:
        stop = True
        fname = None
    fd.imslice((1.0, 4), (0, 5j), (0, 10), resolution, 2*resolution, fname=fname, title="A")
#    fd.imslice((1.0j, 0), (0, 3j*2), (0, 5*2), 3*resolution//3, 5*resolution//3, fname=fname, title="B")
#    fd.imslice((1.0j, 3), (6/numpy.sqrt(37), 6*3j*2/numpy.sqrt(37)), (0, 5*2), 3*resolution//3, 5*resolution//3, fname=fname, title="C")
#    fd.imslice((1.0j, 3), (6*6/numpy.sqrt(6**2 + 6**2), 6*3j*2/numpy.sqrt(6**2 + 6**2)), (0, 5*2), 3*resolution//3, 5*resolution//3, fname=fname, title="D")
#    fd.imslice((-5, 0.707-.707j), (20, 0), (20j, 0), resolution, resolution, fname=fname, title="E")

#    fd.imslice((1.0j - 1.0j*0.5, 2*0.5), (10.0*0.707, 10.0j*0.707), (1.6*(-5.0)*0.894j, 1.6*10.0*0.894), resolution, 8*resolution//5, fname=fname, title="F")
#    fd.imslice((-7 + 5j, 0.3 + 8.25j), (20.0, 0), (20j, 0), resolution, resolution, fname=fname, title="G")
    print(f"\nDone {i} samples\n")


"""
    A
    return numpy.exp(-1/(a**3)) # nice
    fd.imslice((1.0, 4), (0, 5j), (0, 10), resolution, 2*resolution, fname=fname)

    B
    return numpy.exp(-1/(a**3)) # nice
    fd.imslice((1.0j, 0), (0, 3j*2), (0, 5*2), 3*resolution//3, 5*resolution//3, fname=fname)

    C
    return numpy.exp(-1/(a**3)) # nice
    fd.imslice((1.0j, 3), (6/numpy.sqrt(37), 6*3j*2/numpy.sqrt(37)), (0, 5*2), 3*resolution//3, 5*resolution//3, fname=fname)

    D
    return numpy.exp(-1/(a**3)) # nice
    fd.imslice((1.0j, 3), (6*6/numpy.sqrt(6**2 + 6**2), 6*3j*2/numpy.sqrt(6**2 + 6**2)), (0, 5*2), 3*resolution//3, 5*resolution//3, fname=fname)

    E
    #fractional derivative
    return numpy.exp(-1/(a**3)) # nice
    fd.imslice((-5, 0.707-.707j), (20, 0), (20j, 0), resolution, resolution, fname=fname)

    F
    return numpy.cos(a) + numpy.tan(a*numpy.exp(-1)) # cos
    fd.imslice((1.0j - 1.0j*0.5, 2*0.5), (10.0*0.707, 10.0j*0.707), (1.6*(-5.0)*0.894j, 1.6*10.0*0.894), resolution, 8*resolution//5, fname=fname)

    G
    #fractional derivative
    return numpy.cos(a) + numpy.tan(a*numpy.exp(-1)) # cos
    fd.imslice((-7 + 5j, 0.3 + 8.25j), (20.0, 0), (20j, 0), resolution, resolution, fname=fname)
"""
