# -*- coding: utf-8 -*-
import ImageFilter
from PIL import Image
from numpy import *

def gaussian_grid(size = 5):

    """
    Создание квадратной матрицы
    gaussian_grid()

    array([[ 1,  4,  7,  4,  1],

           [ 4, 20, 33, 20,  4],

           [ 7, 33, 55, 33,  7],

           [ 4, 20, 33, 20,  4],

           [ 1,  4,  7,  4,  1]])

    """
    m = size/2
    n = m+1
    x, y = mgrid[-m:n,-m:n]
    # для матрицы 5x5 fac*exp(-0.5*(2**2 + 2**2)) = 1
    fac = exp(m**2)
    g = fac*exp(-0.5*(x**2 + y**2))
    return g.round().astype(int)
class GAUSSIAN(ImageFilter.BuiltinFilter):
    name = "Gaussian"
    gg = gaussian_grid().flatten().tolist()
    filterargs = (5,5), sum(gg), 0, tuple(gg)

im = Image.open('test1.jpg')
im1 = im.filter(GAUSSIAN)
im1.save('filteredimg1.png')

im = Image.open('test2.jpg')
im1 = im.filter(GAUSSIAN)
im1.save('filteredimg2.png')

im = Image.open('test3.jpg')
im1 = im.filter(GAUSSIAN)
im1.save('filteredimg3.png')
