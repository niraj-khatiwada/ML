'''I havce done of rectangle only'''
import cv2


feature_image = cv2.imread("C:/Users/niraj/Anaconda3/Projects/Computer Vision/OpenCV/images/someshapes.jpg")
feature_image_copy = feature_image.copy()
cv2.imshow("Feature Image", feature_image)
cv2.waitKey(0)

target_image = cv2.imread("C:/Users/niraj/Anaconda3/Projects/Computer Vision/OpenCV/images/polygons.jpg")
target_image_copy = target_image.copy()
cv2.imshow("Target Image", target_image)
cv2.waitKey(0)

# Grayscaled
grayscaled_feature = cv2.cvtColor(feature_image, cv2.COLOR_BGR2GRAY)
grayscaled_target = cv2.cvtColor(target_image, cv2.COLOR_BGR2GRAY)

# Canny Edge
edge_feature = cv2.Canny(grayscaled_feature, 127, 255)
edge_target = cv2.Canny(grayscaled_target, 127, 255)

# Thresholding
ret_feature, threshold_feature = cv2.threshold(edge_feature, 127, 255, 0)
ret_target, threshold_target = cv2.threshold(edge_target, 127, 255, 0)

# Contours
image_feature, contours_feature, heirarchy = cv2.findContours(threshold_feature, cv2.RETR_CCOMP,
                                                              cv2.CHAIN_APPROX_SIMPLE)
image_target, contours_target, hierarchy = cv2.findContours(edge_target, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

#Sorted contours
sorted_feature = sorted(contours_feature, key= cv2.contourArea, reverse= False)
sorted_target = sorted(contours_target, key= cv2.contourArea, reverse= False)


matched_reactangle = []

for i in sorted_target[:len(sorted_target) - 1]:
    accuracy = 0.01 * cv2.arcLength(i, closed= True)
    approx_target = cv2.approxPolyDP(i, accuracy, closed= True)
    print("target approx length", len(approx_target))
    cv2.drawContours(target_image_copy, [approx_target], -1, (0,255,0), 3)
    cv2.imshow("---target----", target_image_copy)
    for ii in sorted_feature[:len(sorted_feature) - 1]:
        approx_feature = cv2.approxPolyDP(ii, accuracy, closed= True)
        print("feature approx length", len(approx_feature))
        cv2.drawContours(feature_image_copy, [approx_feature], -1, (0, 255, 255), 3)
        cv2.imshow("----feature---", feature_image_copy)
        if len(approx_target) == len(approx_feature) == 4:
            x, y, w, h = cv2.boundingRect(i)
            cv2.rectangle(target_image_copy, (x,y), (x+w, y+h), (0,255,20), -1)
            matched_reactangle.append(i)

cv2.drawContours(target_image, matched_reactangle, -1, (0, 0, 255), 1)
cv2.imshow("Matched", target_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


