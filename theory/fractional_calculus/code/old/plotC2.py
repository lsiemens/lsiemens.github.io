import numpy
from matplotlib import pyplot
from scipy import special

class axis:
    def __init__(self, x_0, x_1, Nx):
        self.x_0 = x_0
        self.x_1 = x_1
        self.Nx = Nx
        self.dx = (self.x_1 - self.x_0)/(self.Nx - 1)
        self.x = numpy.linspace(self.x_0, self.x_1, Nx, dtype = numpy.complex)

class domain:
    def __init__(self, *axis):
        self.axis = axis
        data = [x.x for x in axis]
        self.X = numpy.meshgrid(*data)


def monomial(x, a, x_0, a_0):
    return (x - x_0)**(a - a_0)/special.gamma(a - a_0 + 1)

def plotML(f):
    pyplot.imshow(numpy.log(numpy.abs(f)))
    pyplot.show()

x = axis(-10, 10, 1000)
a = axis(-10, 10.0, 1000)
print(x, x.x)
print(a, a.x)

dom = domain(x, a)
print("\n\n\n", dom.X)

f = monomial(dom.X[0], dom.X[1], 0, 0)
plotML(f)
