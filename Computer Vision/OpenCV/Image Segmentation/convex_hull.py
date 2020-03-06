
import cv2
import numpy as np

input_image = cv2.imread("C:/Users/niraj/Anaconda3/Projects/Computer Vision/OpenCV/images/hand.jpg")
input_image_copy = input_image.copy()
cv2.imshow("Original", input_image)
cv2.waitKey(0)

#Grayscalle

grayscaled = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

#Canny edge
# edged = cv2.Canny(grayscaled, 20, 180)
# cv2.imshow("Canny Edge", edged)
# cv2.waitKey(0)

#Thresholding
ret, threshold = cv2.threshold(grayscaled, 170, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold", threshold)
cv2.waitKey(0)

#Find Contours
image,contours, hierarchy = cv2.findContours(image= threshold, mode= cv2.RETR_LIST, method= cv2.CHAIN_APPROX_NONE)
# cv2.imshow("Contours", image)
# cv2.waitKey(0)

#Find sorted contours first

sorted_contours = sorted(contours, key= cv2.contourArea, reverse= False)
#print(sorted_contours)

for i in sorted_contours[:len(sorted_contours)-1]:
    convex_hull = cv2.convexHull(i)
    cv2.drawContours(input_image, [convex_hull], 0, (0,255,0), 3)
    cv2.imshow("Convex Hull", input_image)

cv2.waitKey(0)
cv2.destroyAllWindows()