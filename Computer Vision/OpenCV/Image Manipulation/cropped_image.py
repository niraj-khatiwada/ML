import cv2

input_image = cv2.imread("C:/Users/niraj/Anaconda3/Projects/Computer Vision/OpenCV/images/abraham.jpg")

height, width = input_image.shape[:2]

cropped_image = input_image[int(height * 0.25): int(height * 0.75), int(width * 0.25): int(width * 0.75)]

cv2.imwrite("Cropped Image.jpg", cropped_image)