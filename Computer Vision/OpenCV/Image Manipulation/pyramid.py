import cv2

input_image = cv2.imread("C:/Users/niraj/Anaconda3/Projects/Computer Vision/OpenCV/images/abraham.jpg")

cv2.imwrite("Pyramid.jpg", cv2.pyrDown(input_image))