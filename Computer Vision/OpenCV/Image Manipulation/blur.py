import cv2
import numpy as np

input_image = cv2.imread("C:/Users/niraj/Anaconda3/Projects/Computer Vision/OpenCV/images/abraham.jpg")

kernel = np.ones((7,7), dtype='float32') / 49
blurred = cv2.filter2D(input_image, -1, kernel)
cv2.imwrite("Blur Filter2D.jpg", blurred)