from matplotlib import pyplot
import numpy
import cplot
from matplotlib.animation import FuncAnimation

def F(z, theta=0.0):
#    return numpy.exp(numpy.pi*(z + theta*1.0j)) + numpy.exp(numpy.e*(z + theta*1.0j)) + 1
#    return numpy.exp(numpy.pi*z + theta*1.0j) + numpy.exp(numpy.e*z) + 1
    return numpy.exp(numpy.pi*z) + numpy.exp(numpy.e*z) + numpy.exp(theta*1.0j)

x = numpy.linspace(12,-12, 512)
t = numpy.linspace(0, 4*numpy.pi, 60)
#X, Y, T = numpy.meshgrid(x, x[::-1], t)
X, Y= numpy.meshgrid(x, x[::-1])
Z = X + Y*1.0j
print(Z.shape)

extent = [-12, 12, -12, 12]

pyplot.imshow((( (numpy.log(numpy.abs(F(Z + 60.0j))) - numpy.log(numpy.abs(F(Z)))) )), cmap="hsv", extent=extent)
pyplot.show()

fig = pyplot.figure()
num_frames = len(t)
fps = 30

def foo(i):
    print(i)
    pyplot.clf()
#    pyplot.imshow(numpy.angle(F(Z, 2*numpy.pi*i/num_frames)), cmap="hsv")
    pyplot.imshow(numpy.log(numpy.abs(F(Z[:,:,i], T[:,:,i]))), vmax=3, vmin=-2)
#    cplot.cimshow(F(Z[:,:,i], T[:,:,i]), logMag=True, vmax=4, vmin=-2)


#ani = FuncAnimation(fig, foo, frames=num_frames, interval=1000/fps)
#ani.save("t.mp4")
#pyplot.show()
