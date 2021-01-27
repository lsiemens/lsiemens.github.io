from matplotlib import pyplot
import numpy
import cplot
from matplotlib.animation import FuncAnimation

alpha = 0.0
beta = numpy.sqrt(2.0)

def F(z, theta=0.0):
    return numpy.exp(alpha*z) + numpy.exp(beta*z) + numpy.exp(theta*1.0j)

x = numpy.linspace(12,-12, 100)
t = numpy.linspace(0, 4*numpy.pi, 60)
X, Y, T = numpy.meshgrid(x, x[::-1], t)
Z = X + Y*1.0j

extent = [-12, 12, -12, 12]

pyplot.imshow(numpy.log(numpy.abs(F(Z[:,:,0], T[:,:,0]))), vmax=3, vmin=-2)
pyplot.show()

pyplot.imshow(numpy.log(numpy.abs(F(Z[:,:,20], T[:,:,20]))), vmax=3, vmin=-2)
pyplot.show()

pyplot.imshow(numpy.log(numpy.abs(F(Z[:,:,40], T[:,:,40]))), vmax=3, vmin=-2)
pyplot.show()


fig = pyplot.figure()
num_frames = len(t)
fps = 30

def foo(i):
    print(i)
#    pyplot.imshow(numpy.angle(F(Z[:, :, i], T[:, :, i])), cmap="hsv")
    pyplot.imshow(numpy.log(numpy.abs(F(Z[:,:,i], T[:,:,i]))), vmax=3, vmin=-2)
#    cplot.cimshow(F(Z[:,:,i], T[:,:,i]), logMag=True, vmax=4, vmin=-2)


ani = FuncAnimation(fig, foo, frames=num_frames, interval=1000/fps)
ani.save("t.mp4")

import os
os.system("xdg-open t.mp4")
