from matplotlib import pyplot
import numpy
from skimage import color
import warnings

class _color_space:
    _LC_curve = None

    @staticmethod
    def HSLtoRGB(H, S, L):
        """
        all input from 0 to 1
        """
        # in HSV
        V = L + S*numpy.minimum(L, 1-L)
        S = 2*(1 - L/V)
        S[V==0] = 0*S[V==0]

        C = numpy.moveaxis(numpy.stack([H, S, V]), 0, -1)

        # in sRGB
        C = color.hsv2rgb(C)
        return C

    @staticmethod
    def HLtoRGB(H, L):
        return _color_space.HSLtoRGB(H, 1.0, L)

    @staticmethod
    def CIELHtoRGB(L, h):
        return _color_space.CIELCHtoRGB(L, _color_space._maxUnsaturatedChroma(L), h)

    @staticmethod
    def CIELCHtoRGB(L, C, h, strict=False):
        """
        all input from 0 to 1
        """
        L = 100*L
        C = 127*C
        h = 2*numpy.pi*h

        # in CIELab
        a = C*numpy.cos(h)
        b = C*numpy.sin(h)
        C = numpy.moveaxis(numpy.stack([L, a, b]), 0, -1)

        # in sRGB
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            C = color.lab2rgb(C.astype(numpy.float64))

        if strict:
            C[C[:,:,0] >= 1] = (-1,-1,-1) + 0*C[C[:,:,0] >= 1]
            C[C[:,:,1] >= 1] = (-1,-1,-1) + 0*C[C[:,:,1] >= 1]
            C[C[:,:,2] >= 1] = (-1,-1,-1) + 0*C[C[:,:,2] >= 1]

            C[C[:,:,0] <= 0] = (-1,-1,-1) + 0*C[C[:,:,0] <= 0]
            C[C[:,:,1] <= 0] = (-1,-1,-1) + 0*C[C[:,:,1] <= 0]
            C[C[:,:,2] <= 0] = (-1,-1,-1) + 0*C[C[:,:,2] <= 0]
        return C

    @staticmethod
    def _findMinMaxChroma(luminance, Chroma_range=[0.0, 1.0], resolution=360, depth=10):
        """
        Given the a specific luminance find the maximum Chroma value that is valid (rgb coordinates are not over saturated) for any h in the CIELCH model.
        """
        Chroma = numpy.linspace(Chroma_range[0], Chroma_range[1], 4)

        h = numpy.linspace(0.0, 1.0, resolution)
        C, h = numpy.meshgrid(Chroma[1:-1], h)

        mask = (_color_space.CIELCHtoRGB(luminance + 0*C, C, h, strict=True)[:, :, 0] == -1)
        mask = [False] + numpy.any(mask, axis=0).tolist() + [True]
        index = mask.index(True)

        if depth > 0:
            return _color_space._findMinMaxChroma(luminance, [Chroma[index - 1], Chroma[index]], resolution=resolution, depth=depth-1)

        return (Chroma[index] + Chroma[index - 1])/2.0

    @staticmethod
    def _initalize_LC_curve():
        """
        Initaliaze max chroma curve
        """
        if _color_space._LC_curve is None:
            C = []
            L = numpy.linspace(0, 1, 64)
            for luminance in L:
                C.append(_color_space._findMinMaxChroma(luminance))
            C = numpy.array(C)
            _color_space._LC_curve = {"L":L, "C":C}
        else:
            raise ValueError("This exception type should be changed. Do not reinitalize LC curve")

    @staticmethod
    def _maxUnsaturatedChroma(L):
        """
        Return maximum chroma given a luminance such that the CIELCH model is not over saturated
        """
        if _color_space._LC_curve is None:
            _color_space._initalize_LC_curve()

        return numpy.interp(L.astype(numpy.float64), _color_space._LC_curve["L"], _color_space._LC_curve["C"], 0.0, 0.0)

_color_space = _color_space()

def cimshow(data, extent=[-1.0, 1.0, -1.0, 1.0], logMag=False, modRange=False, vmin=None, vmax=None, fname=None):
    angle = (numpy.angle(data) + numpy.pi)/(2*numpy.pi)

    if logMag:
        value = numpy.log(numpy.abs(data))/numpy.log(10.0)
    else:
        value = numpy.abs(data)

    if vmin is None:
        vmin = numpy.min(value)
    if vmax is None:
        vmax = numpy.max(value)
    value = (value - vmin)/(vmax - vmin)

    if modRange:
        value = value % 1.0
    else:
        value = numpy.clip(value, 0.0, 1.0)

    if fname is None:
        pyplot.imshow(_color_space.CIELHtoRGB(value, angle).astype(numpy.float64), extent=extent, interpolation="bicubic")
    else:
#        pyplot.imsave(fname, _color_space.CIELHtoRGB(value, angle).astype(numpy.float64))
        numpy.save(fname, _color_space.CIELHtoRGB(value, angle).astype(numpy.float64))
