import math
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

class OTSU():
    def __init__(self):
        self.threshold_values = 0

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

    def mean(self, start, end, weight):
        if weight == 0:
            return 0

        mean = 0
        for i in xrange(start, end):
            mean += self.histogram_array[i] * i

        return mean / float(weight)

    def threshold(self):
        whole_pixel = self.img.shape[0] * self.img.shape[1]
        max_v = 0
        t = 0

        for i in range(1, 256):
            w0, w1 = self.weight(0, i, whole_pixel), self.weight(i, 256, whole_pixel)
            u0, u1 = self.mean(0, i, w0), self.mean(i, 256, w1)
            variance_b_square = w0 * w1 * ((u0 - u1)**2)
            if variance_b_square > max_v:
                max_v = variance_b_square
                self.threshold_values = i





image = Image.open('img/t3-gray.jpg').convert("L")
img = np.asarray(image)
OTSU().generate_img(img)


