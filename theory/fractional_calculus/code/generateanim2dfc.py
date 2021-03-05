import numpy
import fc2dpy
from scipy import special
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation

resolution = 64 # 256
order = 64 # 128

PD = fc2dpy.polydisk(0, 0, 1, 1, resolution=resolution)
PD.set_parameterization(1.0 + 0.0j, 1.0 + 0.0j)

def encoding(a):
#    return 1.0/fc2dpy.Gamma(-a + 1) ####-------- NICE --------####
    beta = 2.0
    return (a)**beta

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

#fd.function = Log
#fd.function_label = "ln(x)"
#fd.function = func_inverse_a
#fd.function_label = "X^a GAMMAINC"

pyplot.ylim(-10, 10)
T.graph_encoding()
fd.vmax = 1
fd.vmin = -1
fd.graph1d_x()
fd.graph1d_a(x=0.0)
fd.graph2d()

fps = 30
number_of_frames = 30*6 #30*60
data = []
for i in range(number_of_frames):
    print(i, number_of_frames)
    speed = 2*numpy.pi/number_of_frames

    fd.polydisk.set_parameterization(1.0, numpy.cos(speed*i) + 1.0j*numpy.sin(speed*i))
#    fd.polydisk.set_parameterization(numpy.cos(speed*i) + 1.0j*numpy.sin(speed*i), 1.0)
#    temp = numpy.log(numpy.abs(fd.function(fd.polydisk.Grid_x, fd.polydisk.Grid_a, fd.order))) #1
#    temp = numpy.angle(fd.function(fd.polydisk.Grid_x, fd.polydisk.Grid_a, fd.order)) #2
    temp = fd.function(fd.polydisk.Grid_x, fd.polydisk.Grid_a, fd.order) #2
    data.append(temp)
i = 0

vmax, vmin = numpy.nanmax(numpy.abs(data)), numpy.nanmin(numpy.abs(data))
print(vmax, vmin)

fig = pyplot.figure()

def foo(i):
    pyplot.clf()
    def mapping(data, vmin, vmax):
        out = numpy.zeros(shape=data.shape + (3,))
        out[:,:,0] = numpy.clip((numpy.real(data) - vmin)/(vmax - vmin), 0, 1)
        out[:,:,1] = numpy.clip((numpy.imag(data) - vmin)/(vmax - vmin), 0, 1)
        out[:,:,2] = 0.0*numpy.real(data)
        return out
#    pyplot.imshow(data[i%len(data)], vmin=-vmax, vmax=vmax, interpolation="bicubic", cmap="magma") #1
#    pyplot.imshow(data[i%len(data)], vmin=-vmax, vmax=vmax, interpolation="nearest", cmap="hsv") #2
    pyplot.imshow(mapping(data[i%len(data)], vmin, vmax), interpolation="nearest") #2

ani = FuncAnimation(fig, foo, frames=number_of_frames, interval=1000/fps)
ani.save("anim.mp4")
pyplot.show()
