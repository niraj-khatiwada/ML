import cv2

input_image = cv2.imread("C:/Users/niraj/Documents/ML/OpenCV/images/abraham.jpg")

# cv2.imwrite('Hello Wolrd.jpg', input_image)
grascaled_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY )
cv2.imwrite("Grascaled.png", grascaled_image)

# print("Shape is ", input_image.shape)