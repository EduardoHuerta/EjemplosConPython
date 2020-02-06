import numpy as np
import cv2
import math

import histogram as h
import cumulative_histogram as ch

imagen = cv2.imread('', cv2.IMREAD_GRAYSCALE)

height = imagen.shape[0]
width = imagen.shape[1]
pixeles = height * width

hist = h.histogram(imagen)
cum_hist = ch.cumulative_histogram(hist)
