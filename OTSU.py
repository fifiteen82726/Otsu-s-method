"""
Created on Mon Oct 30 12:41:30 2017

@author: mohabmes
"""

import math
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

class OTSU():
    def __init__(self):
        self.threshold_values = []

    def generate_img(self, img):
        self.histogram_array = self.histogram(img)
        self.img = img
        t = self.threshold()


    # return array including include value from 0 ~ 255
    def histogram(self, img):
        row, col = img.shape
        arr = [0] * 256
        for i in xrange(0, row):
            for j in xrange(0, col):
                arr[img[i, j]] += 1
        plt.bar(np.arange(256), arr)
        plt.show()

        return arr

    def weight(self, start, end, whole_pixel):
        return sum(self.histogram_array[start:end]) / float(whole_pixel)

    def threshold(self):
        whole_pixel = self.img.shape[0] * self.img.shape[1]
        for i in range(1, 256):
            w0, w1 = self.weight(0, i, whole_pixel), self.weight(i, 256, whole_pixel)


image = Image.open('img/t3-gray.jpg').convert("L")
img = np.asarray(image)
OTSU().generate_img(img)


