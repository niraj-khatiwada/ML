import cv2
import numpy as np
input_image = cv2.imread("C:/Users/niraj/Anaconda3/Projects/Computer Vision/OpenCV/images/abraham.jpg")

# cv2.imwrite('Hello Wolrd.jpg', input_image)
# grascaled_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY )
# cv2.imwrite("Grascaled.png", grascaled_image)

# print("Shape is ", input_image.shape)
grascaled_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
# print(grascaled_image[0, 0])
# print(B, G, R)
hsv_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2HSV)
# cv2.imwrite("abraham_hsv.jpg", hsv_image)
# print(hsv_image[0,0])
# print(input_image.shape)

B, G, R = cv2.split(input_image)
# cv2.imwrite("Blue.jpg", B)
# cv2.imwrite("Green.jpg", G)
# cv2.imwrite("Red.jpg", R)

merged_image = cv2.merge( [B+100, G+100, R+100])
cv2.imwrite("Merged.jpg", merged_image)

