import cv2
import numpy as np


feature_image = cv2.imread("C:/Users/niraj/Anaconda3/Projects/Computer Vision/OpenCV/images/blobs.jpg", 0)
cv2.imshow("Original", feature_image)
feature_image_copy = feature_image.copy()
image_shape = feature_image.shape

cv2.waitKey(0)

#Count all blob
detector_all = cv2.SimpleBlobDetector_create()

#Load image ton detector and find all keypoints
keypoints_all = detector_all.detect(feature_image_copy)
#Draw keypoints
blob_all = cv2.drawKeypoints(image= feature_image_copy, keypoints= keypoints_all, outImage= np.zeros((1,1)), color= (0,255,0), flags= cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)
text_all = f"Total number of blobs { len(keypoints_all)}"
cv2.putText(img= blob_all, text= text_all, org = ( image_shape[1] - int(image_shape[1]/1.5), image_shape[0]- 10), fontFace= cv2.FONT_HERSHEY_PLAIN, fontScale= 1, color= (0,255,0), thickness= 2)
cv2.imshow("Blob All", blob_all)
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
detector = cv2.SimpleBlobDetector_create(params)
#Input image to detector and extract the keypoints
keypoints = detector.detect(image= feature_image)
text = f"No of circle is {len(keypoints)}"
cv2.putText(feature_image, text= text,org = ( image_shape[1] - int(image_shape[1]/1.5), image_shape[0]- 10), fontFace= cv2.FONT_HERSHEY_PLAIN , fontScale=2,color= (0,255,255), thickness=2  )
#Draw keypoints
blob = cv2.drawKeypoints(feature_image, keypoints= keypoints, outImage= np.zeros((1,1)), color= (0,0,255), flags= cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("Blob ", blob)
cv2.waitKey(0)

cv2.destroyAllWindows()

