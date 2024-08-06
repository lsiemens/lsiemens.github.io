#!/usr/bin/python3

import os
import numpy
from matplotlib import pyplot

path = "./tmp/"
fname = "full_image"
ftype = ".bmp"
save_stack = False

# use recursive summation to limit memory ussage when finding the mean value
class LoadMean:
    def __init__(self, files):
        self.files = files
        self.shape = numpy.load(self.files[0]).shape
        self.order = int(numpy.ceil(numpy.log(len(self.files))/numpy.log(2)))
        print("Order: ", self.order)

    def mean(self):
        data = self.get_summ(self.order, 0)
        return data/len(self.files)

    def get_summ(self, step_order, step_index):
        if step_order == 0:
            if step_index < len(self.files):
                print(f"Load file [{step_index + 1} / {len(self.files)}]: {self.files[step_index]}")
                return numpy.load(self.files[step_index])
            else:
                return None

        A = self.get_summ(step_order - 1, 2*step_index + 0)
        if A is None:
            return None

        B = self.get_summ(step_order - 1, 2*step_index + 1)
        if B is None:
            return A
        return A + B

files = [path + _fname for _fname in os.listdir(path) if os.path.isfile(path + _fname)]
files = [_fname for _fname in files if ".npy" in _fname]

data = LoadMean(files).mean()

"""
images = []
for i, _fname in enumerate(files):
    print(f"Loaded file [{i}, {len(files)}]: {_fname}")
    images.append(numpy.load(_fname))
#    images.append(pyplot.imread(_fname).astype(float))

images = numpy.array(images)
print(images.shape)
images = numpy.mean(images, axis=0)
print(images.shape, images.dtype)

print(numpy.isclose(images, data))
"""

pyplot.imsave(fname + ftype, data)

if save_stack:
    numpy.save(fname + ".npy", data)
