import cv2

imagePath = "C:/Users/niraj/Anaconda3/Projects/Computer Vision/face detection using opencv/e6d0e49fb1f39374bdb727329cd4b5c1.jpg"

cascadeClassifierPath = "C:/Program Files/opencv/build/etc/haarcascades/haarcascade_frontalface_alt.xml"

cascadeClassifier = cv2.CascadeClassifier(cascadeClassifierPath)
image = cv2.imread(imagePath)

grayscaleImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

detectedface = cascadeClassifier.detectMultiScale(grayscaleImage, scaleFactor=1.1, minNeighbors=10, minSize=(30,30))

for (x, y, width, height) in detectedface:
    cv2.rectangle(image, (x, y), (x+width, y+height), (0, 0, 255), 10)

cv2.imwrite('result_shrinkhala2.jpg', image)