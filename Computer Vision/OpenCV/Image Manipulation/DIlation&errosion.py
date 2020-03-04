import cv2
import numpy as np


input_image = cv2.imread("C:/Users/niraj/Anaconda3/Projects/Computer Vision/OpenCV/images/abraham.jpg", 0)

kernel = np.ones((5,5), dtype='uint8')

errosion = cv2.erode(input_image, kernel, iterations= 1)
cv2.imshow("Erosion", errosion)
cv2.waitKey(0)

#Dilation

dilation = cv2.dilate(input_image, kernel, iterations=1)
cv2.imshow("Dilation", dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Opening and closing
