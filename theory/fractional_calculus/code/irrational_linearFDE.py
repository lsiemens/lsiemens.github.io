from matplotlib import pyplot
import numpy

C_i = [1, 1, 1]
alpha_i = [0, numpy.pi, numpy.sqrt(2)]

# sum_{i=0}^\infinity C_i \partial_{x}^{\alpha_i} f(x, a) = T f(x, a) = 0

# f_b = e^{e^{b} x - a b}

# T f_b(x, a) = f_b(x, a) (sum_{i=0}^\infinity C_i e^{\alpha_i b})

def f_b(z, a, b):
    return numpy.exp(numpy.exp(b)*z - a*b)

def Tf_zero(b):
    Tf = 0*b + 0.0j
    for C, alpha in zip(C_i, alpha_i):
        Tf += C*numpy.exp(alpha*b)
    return Tf

def Tf_zero_rotate(b, index):
    C_temp = C_i[:index] + C_i[index + 1:]
    alpha_temp = alpha_i[:index] + alpha_i[index + 1:]

    Tf_rot = 0*b
    for C, alpha in zip(C_temp, alpha_temp):
        Tf_rot += C*numpy.exp(alpha*b)
#    return numpy.abs(Tf_rot/numpy.exp(alpha_i[index]*b))**2 - numpy.abs(C_i[index])**2
    return numpy.abs(Tf_rot)**2 - numpy.abs(C_i[index]*numpy.exp(alpha_i[index]*b))**2

b_max = 2*numpy.pi
b = numpy.linspace(-b_max, b_max, 512)
extent = [-b_max, b_max, -b_max, b_max]

X, Y = numpy.meshgrid(b, b[::-1])
B = X + Y*1.0j

#pyplot.imshow(numpy.abs(Tf_zero(B)))
#pyplot.show()

pyplot.imshow(numpy.angle(Tf_zero(B)), cmap="hsv", extent=extent)
pyplot.show()

pyplot.imshow(numpy.log(numpy.abs(Tf_zero(B)/Tf_zero(b))), extent=extent)
pyplot.show()

#pyplot.imshow(Tf_zero_rotate(B, 1))
#pyplot.show()

pyplot.imshow(numpy.log(numpy.abs(Tf_zero_rotate(B, 1))), vmax=20.0, vmin=-20, extent=extent)
pyplot.show()
