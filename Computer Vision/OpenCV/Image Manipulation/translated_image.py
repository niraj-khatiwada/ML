import cv2
import numpy as np
from matplotlib import pyplot as plt

input_image = cv2.imread("C:/Users/niraj/Anaconda3/Projects/Computer Vision/OpenCV/images/abraham.jpg")
height, width = input_image.shape[:2]

#Translation Matrix
T = np.array([[1, 0, width/4], [0, 1, height/4]], dtype=float)

translated_image = cv2.warpAffine(input_image,T, (height, width))
cv2.imwrite("Translated_image.jpg", translated_image )