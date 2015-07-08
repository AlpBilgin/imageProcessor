__author__ = 'pc'

from scipy import misc

import numpy


image = misc.imread('a.jpg')
print (image)
print (image.shape)
print (image[0][0][0])