import cv2
import pprint
#Template Image
template_image = cv2.imread("C:/Users/niraj/Anaconda3/Projects/Computer Vision/OpenCV/images/waldo.jpg")

#Target Image
target_image = cv2.imread("C:/Users/niraj/Anaconda3/Projects/Computer Vision/OpenCV/images/WaldoBeach.jpg")
cv2.imshow("Find Waldo", target_image)
cv2.waitKey()
#Template Matching
match = cv2.matchTemplate(image= target_image, templ= template_image, method= cv2.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(match) # max location is top left corner of template match
pprint.pprint(match)

#Draw Bounding Box
# pprint.pprint(max_loc)
#Find shape of template to draw the rectangele in target image
template_shape = template_image.shape
cv2.rectangle(img= target_image,pt1= max_loc, pt2= (max_loc[0]+ template_shape[0], max_loc[1]+ template_shape[1]), color= (0,255,0), thickness= 3 )
cv2.imshow("Waldo Found", target_image )
cv2.waitKey(0)
cv2.destroyAllWindows()
