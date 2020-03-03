import numpy as np
import cv2

input_image = cv2.imread("C:/Users/niraj/Anaconda3/Projects/Computer Vision/OpenCV/images/abraham.jpg")

height, width = input_image.shape[:2]

resized_image = cv2.resize(input_image, (width, height), interpolation= cv2.INTER_LANCZOS4)

cv2.imwrite("Resized.jpg", resized_image)