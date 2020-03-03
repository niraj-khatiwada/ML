import numpy as np
import cv2

rectangle= np.zeros((500,500), dtype='uint8')
rectangle = cv2.rectangle(rectangle, (100, 100), (355, 400), (255,255,255), -1)
# cv2.imwrite("rectangle.jpg", rectangle)

ellipse = np.zeros((500, 500), dtype='uint8')
ellipse = cv2.ellipse(ellipse, (255,255), (155,255), 30, 0, 180, (255,255,255), -1)
# cv2.imwrite("ellipse.jpg", ellipse)

#Perform Bitwise operation

#AND
bitwise_and = cv2.bitwise_and(rectangle, ellipse)
cv2.imwrite("And.jpg", bitwise_and)

#OR
bitwise_or = cv2.bitwise_or(rectangle, ellipse)
cv2.imwrite("OR.jpg", bitwise_or)

#XOR
bitwise_xor = cv2.bitwise_xor(rectangle, ellipse)
cv2.imwrite("XOR.jpg", bitwise_xor)

#NOT
bitwise_not = cv2.bitwise_not(ellipse)
cv2.imwrite("NOT.jpg", bitwise_not)