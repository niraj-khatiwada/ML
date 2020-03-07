import cv2
import numpy as np


feature_image = cv2.imread("C:/Users/niraj/Anaconda3/Projects/Computer Vision/OpenCV/images/Sunflowers.jpg", 0)
cv2.imshow("Original", feature_image)
feature_image_copy = feature_image.copy()
cv2.waitKey(0)

#Create Detectors
detector = cv2.SimpleBlobDetector()

#Input Image to Detector and obtain Keypoints
keypoints = detector.detect(image= feature_image)

#Draw keypoints in the image
#Out image is just a (1,1) numpy zeros array

blobs = cv2.drawKeypoints(feature_image, keypoints= keypoints,outImage= np.zeros((1,1)) , color= (0,255,0), flags= cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("Blob Detected", blobs)
cv2.waitKey(0)




cv2.destroyAllWindows()