import cv2
import numpy as np

input_image = cv2.imread("C:/Users/niraj/Anaconda3/Projects/Computer Vision/OpenCV/images/abraham.jpg")

kernel = np.array([[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]])

sharpened = cv2.filter2D(input_image, -1, kernel)
cv2.imwrite("Sharpened.jpg", sharpened)