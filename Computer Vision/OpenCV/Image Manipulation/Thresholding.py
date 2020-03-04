import cv2
import numpy as np


input_image = cv2.imread("C:/Users/niraj/Anaconda3/Projects/Computer Vision/OpenCV/images/abraham.jpg", 0)

#Basic Threshold
ret, threshold_binary = cv2.threshold(input_image, thresh=127, maxval= 255, type= cv2.THRESH_BINARY)

cv2.imshow("Binary Threshold", threshold_binary)

cv2.waitKey(0)

#Adpative Threshold( It is good habit to blur image before thresolding since it removes noise)

# blurred_image = cv2.GaussianBlur(input_image, (7,7), 0)

threshold_adaptive = cv2.adaptiveThreshold(input_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, 5)
cv2.imshow("Adaptive Threshold", threshold_adaptive)
cv2.waitKey(0)

#Otsu Adaptivr Thresholding
_, threshold_otsu = cv2.threshold(input_image, thresh= 127, maxval= 255, type= cv2.THRESH_OTSU + cv2.THRESH_BINARY)
cv2.imshow("OTSU threshold", threshold_otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()