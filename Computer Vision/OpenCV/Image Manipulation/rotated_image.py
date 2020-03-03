import numpy as np
import cv2

input_image = cv2.imread("C:/Users/niraj/Anaconda3/Projects/Computer Vision/OpenCV/images/abraham.jpg")

height, width = input_image.shape[:2]

#Rotation Matrix
M = cv2.getRotationMatrix2D((width/2, height/2), 90,  1)

rotated_image = cv2.warpAffine(input_image, M, (width, height))

cv2.imwrite("Rotated.jpg", cv2.transpose(rotated_image))