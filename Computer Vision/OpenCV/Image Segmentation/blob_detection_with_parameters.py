import cv2
import numpy as np


feature_image = cv2.imread("C:/Users/niraj/Anaconda3/Projects/Computer Vision/OpenCV/images/blobs.jpg", 0)
cv2.imshow("Original", feature_image)
feature_image_copy = feature_image.copy()
cv2.waitKey(0)

#Filter Blob Parameters
params = cv2.SimpleBlobDetector_Params()

#Set Area
params.filterByArea = True
params.minArea = 100

#Set Circularity
params.filterByCircularity = True
params.minCircularity = 0.9

#Set Convexity
params.filterByConvexity = False
params.minConvexity = 0.2

#Set Inertai
params.filterByInertia = True
params.minInertiaRatio = 0.01

#Create Blob Detecor
detector = cv2.SimpleBlobDetector(params)
print(detector)
#Input image to detector and extract the keypoints
keypoints = detector.detect(image= feature_image)

#Draw keypoints
blob = cv2.drawKeypoints(feature_image, keypoints= keypoints, outImage= np.zeros((1,1)), color= (255,0,0))
cv2.imshow("Blob ", blob)
cv2.waitKey(0)

cv2.destroyAllWindows()