import cv2
import numpy as np

input_image = cv2.imread("C:/Users/niraj/Anaconda3/Projects/Computer Vision/OpenCV/images/someshapes.jpg")

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


#Sorting contours by area
a=[]
def contour_areas(contours):    
    for i in contours:
        area = cv2.contourArea(i)
        a.append(area)
    return a
# print(contour_areas(contours))
sorted_contours = sorted(contours, key= cv2.contourArea, reverse=True)
print("Sorted Contours", sorted_contours)

for i in sorted_contours:
    cv2.drawContours(input_image, [i] , -1, (0,255,0), 3)
    cv2.imshow("Drawn Contours", input_image)
    cv2.waitKey(0)
#Draw contours
# cv2.drawContours(input_image, contours, -1, (0,0,255), 3)
cv2.waitKey(0)
cv2.destroyAllWindows()