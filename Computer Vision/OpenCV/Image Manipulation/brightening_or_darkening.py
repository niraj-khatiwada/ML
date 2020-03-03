import cv2
import numpy as np

input_image = cv2.imread("C:/Users/niraj/Anaconda3/Projects/Computer Vision/OpenCV/images/abraham.jpg")

M = np.ones(input_image.shape, dtype= 'uint8')

brightened = cv2.add(input_image, M * 100)
cv2.imwrite("Brightened.jpg", brightened)