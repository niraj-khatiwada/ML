import cv2
import numpy as np

input_image = cv2.imread("C:/Users/niraj/Anaconda3/Projects/Computer Vision/OpenCV/images/abraham.jpg", 0)

#Sobel Edge Detection
sobel_x = cv2.Sobel(input_image, ddepth= cv2.CV_64F, dx= 0 , dy= 1, ksize= -1)
sobel_y = cv2.Sobel(input_image, ddepth= cv2.CV_64F, dx= 1, dy= 0, ksize= -1)
cv2.imshow("Sobel X", sobel_x)
cv2.imshow("Sobel Y", sobel_y)

combined = cv2.bitwise_or(sobel_x, sobel_y)
cv2.imshow("Combined", combined)
cv2.waitKey(0)

#Laplacian Edge Detection(Brings a lot of noise)
laplacian = cv2.Laplacian(input_image, ddepth= cv2.CV_64F)
cv2.imshow("Lplacian Edge", laplacian)
cv2.waitKey(0)

#Canny Edge Detection Algorithm

canny = cv2.Canny(input_image, 20, 170)
cv2.imshow("Canny", canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
