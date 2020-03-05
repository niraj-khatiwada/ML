import cv2
import numpy as np

input_image = cv2.imread("C:/Users/niraj/Anaconda3/Projects/Computer Vision/OpenCV/images/house.jpg")
input_image_copy = input_image.copy()
cv2.imshow("Original", input_image)
cv2.waitKey(0)

#Grayscalle

grayscaled = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

#Canny edge
edged = cv2.Canny(grayscaled, 20, 180)
cv2.imshow("Canny Edge", edged)
cv2.waitKey(0)

#Find Contours
image,contours, hierarchy = cv2.findContours(image= edged, mode= cv2.RETR_LIST, method= cv2.CHAIN_APPROX_NONE)
cv2.imshow("Contours", image)
cv2.waitKey(0)

for i in contours:
    x,y,w,z = cv2.boundingRect(i)
    # print(cv2.boundingRect(i))
    cv2.rectangle(input_image_copy, (x,y), (x+w, y+z), (0,0,255), 3)
    cv2.imshow("Rectangle", input_image_copy)
    cv2.waitKey(0)

#Apply approximation

for i in contours:
    accuracy = 0.05  * cv2.arcLength(i, closed= True)
    approx = cv2.approxPolyDP(i, accuracy, closed= True)
    cv2.drawContours(input_image, [approx], 0, (255,255,0), 3)
    cv2.imshow("Approximated", input_image)
    cv2.waitKey(0)


cv2.destroyAllWindows()