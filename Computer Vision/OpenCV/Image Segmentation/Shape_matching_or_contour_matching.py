import cv2
import numpy as np
from statistics import mean

feature_image = cv2.imread("C:/Users/niraj/Anaconda3/Projects/Computer Vision/OpenCV/images/4star.jpg")
feature_image_copy = feature_image.copy()
cv2.imshow("Feature Image", feature_image)
cv2.waitKey(0)

target_image = cv2.imread("C:/Users/niraj/Anaconda3/Projects/Computer Vision/OpenCV/images/shapestomatch.jpg")
cv2.imshow("Target Image", target_image)
cv2.waitKey(0)
#Grayscaled
grayscaled_feature = cv2.cvtColor(feature_image, cv2.COLOR_BGR2GRAY)
grayscaled_target = cv2.cvtColor(target_image, cv2.COLOR_BGR2GRAY)

#Thresholding
ret_feature, threshold_feature = cv2.threshold(grayscaled_feature, 127, 255, 0)
ret_target, threshold_target = cv2.threshold(grayscaled_target, 127, 255, 0)

#Canny Edge
edge_target = cv2.Canny(threshold_target, 127, 255)

#Contours
image_feature, contours_feature, heirarchy = cv2.findContours(threshold_feature, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
image_target, contours_target, hierarchy = cv2.findContours(edge_target, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)


#Sorted contours
sorted_contrours_feature = sorted(contours_feature, key=cv2.contourArea, reverse= False)
actual_contour = sorted_contrours_feature[-2]
cv2.drawContours(feature_image_copy, [actual_contour], -1, (0,0,255), 3)
cv2.imshow("Shape to be matched", feature_image_copy)
cv2.waitKey(0)
sorted_contrours_target = sorted(contours_target, key=cv2.contourArea, reverse= False)

#check shape of each contour
for i in sorted_contrours_target[:len(sorted_contrours_target)-1]:
    #Approximating Contours
    accuracy = 0.05 * cv2.arcLength(i, closed= True)
    approx = cv2.approxPolyDP(i, accuracy, closed= True)
    print(len(approx))
    #Shape matching
    shape_match = cv2.matchShapes(actual_contour, approx, 2, 0.0)
    print(shape_match)
    if shape_match < 0.15:
        matched = i
    else:
        matched = []

cv2.drawContours(target_image, [matched], -1, (0,0,255), 3)
cv2.imshow("Matched",target_image )
cv2.waitKey(0)
cv2.destroyAllWindows()