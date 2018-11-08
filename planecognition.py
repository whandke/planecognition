import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import skimage
import skimage.morphology
import skimage.feature
from matplotlib.pyplot import figure


def processImage(image):

    image = skimage.color.rgb2gray(image)

    image = skimage.filters.gaussian(image, 3)

    for i in range(3):
        image = skimage.morphology.closing(image)

    image = skimage.feature.canny(image, sigma=3)

    for i in range(2):
        image = skimage.morphology.dilation(image)

    return image


files = [
    'images/samolot03.jpg',
    'images/samolot01.jpg',
    'images/samolot05.jpg',
    'images/samolot07.jpg',
    'images/samolot08.jpg',
    'images/samolot09.jpg'
    ]

originals = []

for f in files:
    originals.append(mpimg.imread(f))

rows = 3
cols = len(originals) / rows

f, axarray = plt.subplots(rows, cols, gridspec_kw={'wspace': 0, 'hspace': 0})

for axis in f.axes:
    axis.get_xaxis().set_visible(False)
    axis.get_yaxis().set_visible(False)
    axis.margins(0)

for r in range(rows):
    for c in range(cols):
        axarray[r, c].imshow(processImage(
            originals[c + r*cols]), cmap="gray")

plt.savefig("planes.png", dpi=1600, bbox_inches='tight')
