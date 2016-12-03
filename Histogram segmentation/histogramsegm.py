# -*- coding: utf-8 -*-
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

# генерация изображения с шумом

np.random.seed(1)
# Seed the generator.
# This method is called when RandomState is initialized.
# It can be called again to re-seed the generator.
# For details, see RandomState.

n = int(input('Enter n:'))
l = 256

im = np.zeros((l, l))
# Return a new array of given shape and type, filled with zeros.
# >>> s = (2,2)
# >>> np.zeros(s)
# array([[ 0.,  0.],
#        [ 0.,  0.]])


points = l*np.random.random((2, n**2))
im[(points[0]).astype(np.int), (points[1]).astype(np.int)] = 1
im = ndimage.gaussian_filter(im, sigma=l/(4.*n))
# Multidimensional Gaussian filter.
# >>> gaussian_filter(a, sigma=1)
# array([[ 4,  6,  8,  9, 11],
#        [10, 12, 14, 15, 17],
#        [20, 22, 24, 25, 27],
#        [29, 31, 33, 34, 36],
#        [35, 37, 39, 40, 42]])

mask = (im > im.mean()).astype(np.float) #маска
mask += 0.1 * im
img = mask + 0.2*np.random.randn(*mask.shape)
# Return a sample (or samples) from the “standard normal” distribution.

hist, bin_edges = np.histogram(img, bins=60)
# Compute the histogram of a set of data.

bin_centers = 0.5*(bin_edges[:-1] + bin_edges[1:])
binary_img = img > 0.5
plt.figure(figsize=(11,4))
plt.subplot(131)
# Return a subplot axes positioned by the given grid definition.
# Typical call signature:
# subplot(nrows, ncols, plot_number)

plt.imshow(img)
plt.axis('off')
plt.subplot(132)
plt.plot(bin_centers, hist, lw=2)
plt.axvline(0.5, color='r', ls='--', lw=2)
plt.text(0.57, 0.8, 'histogram', fontsize=20, transform = plt.gca().transAxes)
plt.yticks([])
# matplotlib.pyplot.yticks(*args, **kwargs)
# Get or set the y-limits of the current tick locations and labels.

plt.subplot(133)
plt.imshow(binary_img, cmap=plt.cm.gray, interpolation='nearest')
plt.axis('off')
plt.subplots_adjust(wspace=0.02, hspace=0.3, top=1, bottom=0.1, left=0, right=1)
plt.show()