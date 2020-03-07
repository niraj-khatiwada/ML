import cv2
import numpy as np


feature_image = cv2.imread("C:/Users/niraj/Anaconda3/Projects/Computer Vision/OpenCV/images/soduku.jpg")
cv2.imshow("Original", feature_image)
feature_image_copy = feature_image.copy()
cv2.waitKey(0)

#Graysclaed
grayscaled = cv2.cvtColor(feature_image_copy, cv2.COLOR_BGR2GRAY)

#Thresholding
# ret, threshold = cv2.threshold(grayscaled, thresh= 100, maxval= 255, type= cv2.THRESH_BINARY)

#Canny Edge
edged = cv2.Canny(grayscaled, 127, 255)
cv2.imshow("Grayscaled and Edged ", edged)
cv2.waitKey(0)

#Houghs Line detection
hough_lines = cv2.HoughLinesP(edged, rho= 1, theta= np.pi/180, threshold = 150, minLineLength=5, maxLineGap= 15 )
print(hough_lines[0])
print(hough_lines.shape)
print(len(hough_lines))

for i in range(len(hough_lines)):
    for x1, y1, x2, y2 in hough_lines[i]:
       cv2.line(feature_image_copy, (x1, y1), (x2, y2), (0,255,0), 3)


cv2.imshow("Hough lines Detected", feature_image_copy)
cv2.waitKey(0)


cv2.destroyAllWindows()
