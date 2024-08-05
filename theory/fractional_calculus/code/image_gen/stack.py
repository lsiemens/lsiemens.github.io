#!/usr/bin/python3

import os
import numpy
from matplotlib import pyplot

path = "./tmp/"
fname = "full_image"
ftype = ".bmp"
save_stack = False

files = [path + _fname for _fname in os.listdir(path) if os.path.isfile(path + _fname)]
files = [_fname for _fname in files if ".npy" in _fname]

images = []
for i, _fname in enumerate(files):
    print(f"Loaded file [{i}, {len(files)}]: {_fname}")
    images.append(numpy.load(_fname))
#    images.append(pyplot.imread(_fname).astype(float))

images = numpy.array(images)
print(images.shape)
images = numpy.mean(images, axis=0)
print(images.shape, images.dtype)

pyplot.imsave(fname + ftype, images)

if save_stack:
    numpy.save(fname + ".npy", images)
