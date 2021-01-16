import numpy
import fc2dpy
from scipy import special
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation

resolution = 256 # 512
order = 128 # 128

PD = fc2dpy.polydisk(0, 0, 10, 5, resolution=resolution)
PD.set_parameterization(1.0 + 0.0j, 1.0 + 0.0j)
def encoding(a):
    return 1.0/special.gamma(-a + 1) ####-------- NICE --------####

def hypergeometricfunction_2F1_11c(c, x, n=10):
    """
    2F1(1, 1; c; x)
    """
    out = 0
    for i in range(n):
        out += special.gamma(i + 1)*special.gamma(c)*(x)**i/special.gamma(i + c)
    return out

def iv(v, z, n=10):
    out = 0
    for i in range(n):
        out += (z/2.0)**(2*i + v)/(special.gamma(i + 1)*special.gamma(i + v + 1))
    return out

#def foobar(x, a, order=None):
#    return x**(a/2)*iv(-a, 2*numpy.sqrt(x))

def foobar(x, a, order=None):
    return x**(a+1)*hypergeometricfunction_2F1_11c(a+2, -x)/special.gamma(a + 2)

T = fc2dpy.taylor_encoding(encoding, PD, "cos(a)/(a-1)")
fd = fc2dpy.generator_2d_from_1d(T, order=order)

fd.function = foobar

pyplot.ylim(-10, 10)
T.graph_encoding()
fd.vmax = 1
fd.vmin = -1
fd.graph1d_x()
fd.graph1d_a(x=0.0)
fd.graph2d()

n = 30*60 #30*60
data = []
for i in range(n):
    print(i, n)
    speed = 2*numpy.pi/n

#    fd.polydisk.set_parameterization(1.0, numpy.cos(speed*i) + 1.0j*numpy.sin(speed*i))
#    fd.polydisk.set_parameterization(numpy.cos(speed*i) + 1.0j*numpy.sin(speed*i), 1.0)
    fd.polydisk.set_parameterization(numpy.cos(2*speed*i) + 1.0j*numpy.sin(2*speed*i), numpy.cos(3*speed*i) + 1.0j*numpy.sin(3*speed*i))
#    temp = numpy.log(numpy.abs(fd.function(fd.polydisk.Grid_x, fd.polydisk.Grid_a, fd.order))) #1
    temp = numpy.angle(fd.function(fd.polydisk.Grid_x, fd.polydisk.Grid_a, fd.order)) #2
    data.append(temp)
i = 0

vmax, vmin = numpy.nanmax(data), numpy.nanmin(data)
print(vmax, vmin)

fig = pyplot.figure()

def foo(i):
    pyplot.clf()
#    pyplot.imshow(data[i%len(data)], vmin=-vmax, vmax=vmax, interpolation="bicubic", cmap="magma") #1
    pyplot.imshow(data[i%len(data)], vmin=-vmax, vmax=vmax, interpolation="bicubic", cmap="plasma") #2

ani = FuncAnimation(fig, foo, frames=n, interval=16)
ani.save("anim.mp4")
pyplot.show()
