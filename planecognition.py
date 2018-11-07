import matplotlib.pyplot as pyplot
import matplotlib.image as mpimg
import numpy as np
import skimage

img = mpimg.imread('images/samolot00.jpg')

img = skimage.color.rgb2gray(img)

img = skimage.filters.sobel(img)

imgplot = pyplot.imshow(img, cmap="gray")
pyplot.show()